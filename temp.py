import requests
import json


def get_access_token(config, email, password):
    # url = config["email_url"]
    url = "https://backend-core-etas.digital.auto/v2/auth/login"
    sending_obj = {"email": email, "password": password}
    response = requests.post(url, json=sending_obj)
    data = json.loads(response.content)
    return data["tokens"]["access"]["token"]


def get_self(config, token):
    url = "https://backend-core-etas.digital.auto/v2/users/self"
    headers = {"Authorization": f"Bearer {token}"}
    print(headers)
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


def delete_model(config, token, model_id):
    url = f"https://backend-core-etas.digital.auto/v2/models/{model_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    return response.json()


token = get_access_token("", "vuy4hc@bosch.com", "blablabla")
print(delete_model("", token, "665ee097a178be0027e53296"))