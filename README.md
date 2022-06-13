# Introduction 
This servcie provides access to static configuration based on:
- Section and key - The section to be fetched with optional key
- Entity (company_id) - The default or the specified entity as header attribute 'entity'
- Language - The default or specified locale in the header 'accept-language'

```curl
curl --location --request GET 'http://localhost:5001/configuration/v1/ui/verification-otp' \
--header 'entity: entity01' \
--header 'accept-language: hi_in'
```

# Setup & Configuration

Ensure that following softwares are installed on your machine
- Python 3.9 and above, recomended is to use Python 3.10
- Visual Code as your editor (optionally pycharm)
- If you are using Windows, it is recommended to enable WSL2

*Note: For Mac and Linux, ensure pip and venv are also installed, for python3.*

## Setup for Ubuntu 24.04 (including WSL for Ubuntu distro)

- Install Python: 
    > ```sudo apt install python3.10```
- Set default python version (update symlink): 
    > ```sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 2```
- Install Pip (python package manager):
    > ```sudo apt install pip```
- Install Make: 
    > ```sudo apt install make```

## Creating Virtual Environment

Python application are typically build in its own virtual environment, that allows one to control the modules and environment configuration.

In you terminal, run the following command
- Create a new Virtual environment
    > ```python -m venv .env```
- Activate the environment
    > ```.\.env\Scripts\activate```
- Install the required packages
    > ```pip install -r .\requirements.txt```

*Note: For Mac and Linux, there are similar commands*

# Running the service
## Mock Service
With spec first approach, it is very easy to run the mock service, to run a mock server run the following command

> ```connexion run .\openapi\spec.yaml --mock=all -v```

## Run Service Locally
To launch the service locally you can use the following command

- Run the application 
    > ```python .\src\app.py```
- URL to open Swagger UI - http://localhost:5001/configuration/v1/ui/
- To open the health Url - http://localhost:5001/health

## Run Service on Docker
Follow the steps below to create and run as a container

- You can use docker-compose to build and run the application
    > ```docker compose -p Configuration -f .\docker-compose.yaml up -d```
- URL to open the Swagger UI - http://localhost:8080/configuration/v1/ui/
- To open the health Url - http://localhost:8080/health


# Testing the service

There are two type of tests that would be written and needs to be executed, follow the steps below to setup and run the tests

- Unit Test - These would be written to test a function in isolation, these needs to be written for any helper function that is not part of business functionality.
- Component Test - These would be written to test the service in its entirety, mocking the ends that are dependent on outside data.

## Running the tests

Setup the environment

```
python -m venv .testenv
.\.testenv\Scripts\activate
pip install -r .\requirements.txt
pip install -r .\test-requirements.txt
```

Running the tests
- Unit test - ```pytest .\tests\unit\```
- Component test - ```pytest .\tests\component\```
