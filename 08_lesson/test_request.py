import requests

api_key = '62kwFhtCCi6m2fyL19OQ+KoR8hPAfrXCCIQAbB4RXqOlJlPlMUnNwi4cr0nmEcSu'

HEADERS = {"Authorization": f"Bearer {api_key}"}

baseUrl = 'https://ru.yougile.com'


def test_create_project():
    body = {
    "title": "Проект"
     }
    response = requests.post(baseUrl + '/api-v2/projects', json=body, headers=HEADERS)

    assert response.status_code == 201

    assert response.json()["id"]

def test_negative_create_project():
    body = {
    "title": ""
     }
    response = requests.post(baseUrl + '/api-v2/projects', json=body, headers=HEADERS)

    assert response.status_code == 400

def test_edit_project():
        body = {
            "title": "Проект"
        }
        response = requests.post(baseUrl + '/api-v2/projects', json=body, headers=HEADERS)

        assert response.status_code == 201

        assert response.json()["id"]

        project_id = response.json()["id"]

        new_title = 'New title'
        response2 = requests.put(
            f"{baseUrl}/api-v2/projects/{project_id}",
            json={"title": new_title},
            headers=HEADERS,
        )
        assert response2.status_code == 200, response2.text
        assert response2.json().get("id") == project_id

def test_negative_edit_project():

    project_id = '123'

    new_title = 'New title'
    response2 = requests.put(
        f"{baseUrl}/api-v2/projects/{project_id}",
        json={"title": new_title},
        headers=HEADERS,
    )
    assert response2.status_code == 404, response2.text

def test_get_project():
        body = {
            "title": "Проект"
        }
        response = requests.post(baseUrl + '/api-v2/projects', json=body, headers=HEADERS)

        assert response.status_code == 201

        assert response.json()["id"]

        project_id = response.json()["id"]

        response2 = requests.get(
            f"{baseUrl}/api-v2/projects/{project_id}",

        headers=HEADERS,
        )
        assert response2.status_code == 200, response2.text
        assert response2.json().get("id") == project_id

def test_negative_get_project():

    project_id = '123'

    response2 = requests.get(
        f"{baseUrl}/api-v2/projects/{project_id}",
        headers=HEADERS,
    )
    assert response2.status_code == 404, response2.text