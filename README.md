## Helixa Challenge

The project concerns the creation of an REST API for finding items within a tree. Starting from 2 JSON structured at several levels, the API must allow to search in each of them (separately) the last level elements that contain a given string in 2 modes:

* Search for the leaves on the whole tree
* Search for leaves on a specific sublayer (passed in input to the API)
 
A plus is the realization of automatic tests.

Attached are the 2 JSON files:
* categories.json
* psyhographics.json

### Categories.json 
The search must be done for the name field. The children are identified by the children field.
### Psychographics.json
The research must be done for the label field. The children are identified by the values ​​field.


## How to run the application

### With Docker

To run the application, just run the docker-compose:

```bash
$ docker-compose build
```

We have two images:

    - redis: we use the redis server as a cache
    - helixa_app: the application
    
You can run the application within the container ``helixa_app`` by running:

```bash
$ python3 /app/helixa_app/appy.py
``` 

This should run the application.

### Without docker

#### Set-up virtualenv

**Note:** here we use python 3.7 but the application can run with python 3.6+ (or, at least, it should)

1. Create virtualenv:
```bash
$ virtualenv -p python3.7 venv37
```

2. Activate virtualenv
```bash
$ source ./venv37/bin/activate
```
**Note:** In order to exit from virtual environment use `deactivate`

3. Install all python core libraries
```bash
$ pip install -r requirements.txt
```

#### Execution

You can run the application by executing the module ``app.py``. This will run the application on localhost and the default port is 5000.
There are a bunch of env variables to set:
    
    HELIXA_APP_CONFIG=path/to/conf/file.ini
    LOG_PATH=path/to/logs/
    LOG_LEVEL=log level 
    LOG_CONF=path/to/log/config/file.ini
    REDIS_HOST_ADDRESS=redis host address
    REDIS_PORT_BIND=redis port
    USE_REDIS_CACHE=true if you want to use redis as a cache. false otherwise
    DATABASE_CONNECTION=connection string to connect the db (sqlite:///helixa_app_dev.db)

To run the application, you can run the command
```bash
$ ./local_run/run_helixa_app.sh
```
This will run gunicorn who serves the application. The default address is 0.0.0.0:5000.


### Tests

```bash
$ pytest --cov=helixa_app tests/
```

## Before start making changes...
#### Install git client Hooks

1. Open with a terminal and execute
```bash
$ git config core.hooksPath git-hooks
```

This command set git to use hooks saved in `git-hooks` instead of the default `.git/hooks/`.

The pre-commit hook performs a check using:
 * flake8 (blocking) 
 * pylint (non blocking)
 
After that, it runs all the tests with coverage. If all the tests pass, it performs the commit.
