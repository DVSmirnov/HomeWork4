import requests


def test_status_code_url(base_url, status_code):
    response = requests.get(url=base_url)
    assert response.status_code == status_code
