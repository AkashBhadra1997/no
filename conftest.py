from pytest import fixture
from requests import Session
from json import load
from yaml import safe_load

def _session():
    session = Session()
    with open("C:/Users/akash/PycharmProjects/Api automation Project1/resourse/config.yml") as f:
        data = safe_load(f)
        env = data["test_environment"]
        end_point = env["login_endpoint"]
        base_url = env["base_url"]
    with open("C:/Users/akash/PycharmProjects/Api automation Project1/Payloads/paylod.json") as file:
        data = load(fp=file)
        payload = data["login"]
        response = session.post(base_url+end_point,json=payload)
        return session