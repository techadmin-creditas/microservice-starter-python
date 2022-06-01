# Introduction 
Starter-Kit to build REST based Microservice using Python and Flask framework.

The starter pack has following features:
1. Flask framework to build REST API with async
2. Integrated with Open API 3.x using connexion framework.
3. Three Layer arcticture within the microservice i.e. 
    - Controller
    - Service
    - Basic DAO/providers 
4. Common REST Middleware for Logging, tracing and exception handling.
5. Hosted as a contanarised application.

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

*Note: In case of terminal not working after installing python 3.10, open the vscode terminal and run the ```sudo apt-get --reinstall install python3-minimal``` command.*


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
- URL to open Swagger UI - http://localhost:5001/starterkit/v1/ui/
- To open the health Url - http://localhost:5001/health

## Run Service on Docker
Follow the steps below to create and run as a container

- You can use docker-compose to build and run the application
    > ```docker compose -p Starter-Kit -f .\docker-compose.yaml up -d```
- URL to open the Swagger UI - http://localhost:8080/starterkit/v1/ui/
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


# Links to Read
- Install Python 3.10 on ubuntu [how to](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)
- Connexion CLI - https://connexion.readthedocs.io/en/latest/cli.html
- Data Classes - https://docs.python.org/3.10/library/dataclasses.html#dataclasses.dataclass


# ToDo
- Error handling
    open api spec's.
    override & custom error.\
- Spinx doc
- Unit test & Component test
- Connect to data layer
- configuration file


paused - https://connexion.readthedocs.io/en/latest/routing.html


