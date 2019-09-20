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

TODO

### Without docker

#### Set-up virtualenv

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

### Execution

Work in progress...

### Tests

```bash
$ pytest tests/
```