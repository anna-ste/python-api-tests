# Testing API with python and behave 
 
## Setup execution environment
1. Install Python 3.7 

The most reliable way of python3 installation is by downloading relevant python installer for your platform from the official site.
It supports all existing and popular platforms. Go to https://www.python.org/downloads/ and find platform specific installer.
It will handle all the system links, paths, pip linking automatically.

2. To install dependencies run `pip install -r requirements.txt`

3. Create an account  and create an API key, configure this key with static 2 factor authentication

## Global variables

* Ways of setting variables: 
    1. In `config` create file `settings_local.json` and copy content of `settings.json`. In `settings_local.json` you can set necessary values for variables used in framework such as `api_key`.
    2. Set environment variables. Use same naming as in `settings.json`, but capital letters, for example, if in `settings.json` we have `api_key`, environment variable should be named `API_KEY`.
   

* Priority of execution:
    1. `settings.json` will be overwritten by `settings_local.json`.
    2. `settings_local.json` will be overwritten by environment variables.


## Implemented tests
1. Retrieve the server time
2. Retrieve XBT/USD trading pair
3. Retrieve open orders on the account with configured 2FA


## Execution and Reporting locally

To run your tests with behave
behave -f allure -o reports -f pretty

For reports
allure serve reports


## Execution and Reporting in docker container

To run in container  

`docker build -t anna2154/behave . `

`docker run -p 8080:8080/tcp -it anna2154/behave  /bin/bash`

 Open reports reports
 
 http://localhost:8080/index.html#