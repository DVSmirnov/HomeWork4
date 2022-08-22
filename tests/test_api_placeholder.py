import requests
import pytest
import json
from jsonschema import validate


def test_getting_resource():
    res = requests.get(url='https://jsonplaceholder.typicode.com/posts')
    json_file = "json_schemas/schema11.json"
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


@pytest.mark.parametrize("postId", ['1'])
def test_comments(postId):
    res = requests.get(url=f'https://jsonplaceholder.typicode.com/posts/{postId}/comments')
    json_file = "json_schemas/schema12.json"
    assert validate_json(res=res.json(), json_file=json_file)
    assert res.status_code == 200


def validate_json2(res, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=res, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("userId", ['1'])
def test_users(userId):
    res = requests.get(url=f'https://jsonplaceholder.typicode.com/users/{userId}/todos')
    json_file = "json_schemas/schema13.json"
    assert validate_json(res=res.json(), json_file=json_file)
    assert res.status_code == 200


def validate_json3(res, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=res, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("albumId", ['1'])
def test_albums(albumId):
    res = requests.get(url=f'https://jsonplaceholder.typicode.com/albums/{albumId}/photos')
    json_file = "json_schemas/schema14.json"
    assert validate_json(res=res.json(), json_file=json_file)
    assert res.status_code == 200


def validate_json4(res, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=res, schema=json_file)
        return True
    except Exception as exp:
        print(exp)


@pytest.mark.parametrize("userId", ['1'])
def test_users2(userId):
    res = requests.get(url=f'https://jsonplaceholder.typicode.com/users/{userId}/posts')
    json_file = "json_schemas/schema15.json"
    assert validate_json(res=res.json(), json_file=json_file)
    assert res.status_code == 200


def validate_json5(res, json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    try:
        validate(instance=res, schema=json_file)
        return True
    except Exception as exp:
        print(exp)
