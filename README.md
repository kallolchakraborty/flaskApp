## Python Flask Application
---
Python flask application with security

### Important Points

1. `brew install python3`: python installation
2. `python3 -m venv environment_name`: virtual environment creation. 
    ref: https://docs.python.org/3/library/venv.html
3. `source path_of_enviroment/bin/activate`: activate the enviroment. 
    ref: https://code.visualstudio.com/docs/python/tutorial-flask
4. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`: hombrew installation
    ref: https://brew.sh/
5. `brew install cloudfoundry/tap/cf-cli@7`: install cloud foundry cli
    ref: https://github.com/cloudfoundry/cli/wiki/V7-CLI-Installation-Guide
6. `cf login -a api_endpoint`: login to the cloud foundry
7. `cf create-service hana securestore pyhana`: create a hana service instance. service plan: `securestore`.
8. `pip3 install hdbcli`: install the `hdbcli client` outside the project folder in the previously created virtual environment.
9. `pip3 install cfenv`: install the `cfenv`. 