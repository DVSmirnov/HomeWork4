import requests
import pytest
import json
from jsonschema import validate


def test_dogs_breeds_random():
    res = requests.get(url="https://dog.ceo/api/breeds/image/random")
    json_file = 'json_schemas/schema.json'
    assert validate_json(res=res.json(), json_file=json_file)
    assert res.status_code == 200


def validate_json(res, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=res, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("breed", ['affenpinscher',
                                   'african',
                                   'airedale',
                                   'akita'])
def test_breed(breed):
    response = requests.get(url=f"https://dog.ceo/api/breed/{breed}/list")
    json_file = 'json_schemas/schema2.json'
    assert validate_json(res=response.json(), json_file=json_file)
    assert response.status_code == 200


def validate_json2(response, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=response, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("number, breed", [('1', 'hound'),
                                           ('2', 'akita'),
                                           ('3', 'hound')])
def test_breed_number(number, breed):
    response = requests.get(url=f"https://dog.ceo/api/breed/{breed}/images/random/{number}")
    json_file = 'json_schemas/schema3.json'
    assert validate_json(res=response.json(), json_file=json_file)
    assert response.status_code == 200


def validate_json3(response, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=response, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("breed", ['hound', 'akita'])
def test_breed2(breed):
    response = requests.get(url=f"https://dog.ceo/api/breed/{breed}/images/random")
    json_file = 'json_schemas/schema4.json'
    assert validate_json(res=response.json(), json_file=json_file)
    assert response.status_code == 200


def validate_json4(response, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=response, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("breed", ['afghan'])
def test_hound_photo(breed):
    response = requests.get(url=f"https://dog.ceo/api/breed/hound/{breed}/images")
    json_file = 'json_schemas/schema5.json'
    assert validate_json(res=response.json(), json_file=json_file)
    assert response.status_code == 200


def validate_json5(response, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=response, schema=json_file)
        return True
    except Exception as exp:
        print(exp)
