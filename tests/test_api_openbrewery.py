import requests
import pytest
import json
from jsonschema import validate


@pytest.mark.parametrize("beer_shop", ['banjo-brewing-fayetteville',
                                       'barrel-brothers-brewing-company-windsor',
                                       'bay-brewing-company-miami'])
def test_list_breweries(beer_shop):
    res = requests.get(url=f"https://api.openbrewerydb.org/breweries/{beer_shop}")
    json_file = 'json_schemas/schema6.json'
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


@pytest.mark.parametrize("city", ['San Diego'])
def test_breweries_by_city(city):
    res = requests.get(url=f"https://api.openbrewerydb.org/breweries?by_city={city}&per_page=3")
    json_file = 'json_schemas/schema7.json'
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


@pytest.mark.parametrize("imya", ['3cross Fermentation Cooperative',
                                  '4th Tap Brewing Cooperative',
                                  'Broken Clock Brewing Cooperative'])
def test_breweries_by_name(imya):
    res = requests.get(url=f"https://api.openbrewerydb.org/breweries?by_name={imya}&per_page=3")
    json_file = 'json_schemas/schema8.json'
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


@pytest.mark.parametrize("type", ['micro'])
def test_breweries_by_type(type):
    res = requests.get(url=f"https://api.openbrewerydb.org/breweries?by_type={type}&per_page=3")
    json_file = 'json_schemas/schema9.json'
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


@pytest.mark.parametrize('query', ['Barrel Dog Brewing',
                                   'Boss Dog Brewing',
                                   'Diving Dog Brewhouse',
                                   'Dog Days Brewing',
                                   'Dog Money Restaurant',
                                   'Dog Tag Brewing',
                                   'Dreaming Dog Brewery'])
def test_autocomplete(query):
    res = requests.get(url=f"https://api.openbrewerydb.org/breweries/autocomplete?query={query}")
    json_file = "json_schemas/schema10.json"
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
