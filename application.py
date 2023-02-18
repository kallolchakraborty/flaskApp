import os  # https://docs.python.org/3/library/os.html
from flask import Flask, request, abort  # https://flask.palletsprojects.com/en/2.2.x/
from cfenv import AppEnv  # https://pypi.org/project/cfenv/
from hdbcli import dbapi  # https://pypi.org/project/hdbcli/
from sap import xssec  # https://www.npmjs.com/package/@sap/xssec

# the __name__ is a built-in special variable that evaluates the name of the current module.
# if the source file is executed as the main program, the interpreter sets the __name__ variable
# to have a value “__main__”. if this file is being imported from another module, __name__ will be set to the module’s name.
app = Flask(__name__)
env = AppEnv()

hana_service = "hana"
# fetching all the details of the 'hana' service
hana = env.get_service(label=hana_service)

# the module 'os' provides a portable way of using operating system dependent functionality.
port = int(os.environ.get("PORT", 3000))

uaa_service = env.get_service(name="pyuaa").credentials


@app.route("/")
def hello():
    if "authorization" not in request.headers:
        abort(403)
    access_token = request.headers.get("authorization")[7:]
    security_context = xssec.create_security_context(access_token, uaa_service)
    isAuthorized = security_context.check_scope("openid")

    if not isAuthorized:
        abort(403)

    print("entering the connecting phase:------->")
    conn = dbapi.connect(
        address=hana.credentials["host"],
        port=int(hana.credentials["port"]),
        user=hana.credentials["user"],
        password=hana.credentials["password"],
        encrypt="true",
        sslTrustStore=hana.credentials["certificate"],
    )
    
    cursor = conn.cursor()
    cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY")
    ro = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return "Current time is: " + str(ro["CURRENT_UTCTIMESTAMP"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
