import pytest
import allure
from api_base.base import Base
from model.base_model import Response
from api_base.get_base import GetBase


@allure.epic("API")
@allure.title('Проверка статуса кода 200 Get /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_status_code_request_get(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка json-схемы ответа Get /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_json_schema_request_get(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)
    Response(**response.json())


@allure.epic("API")
@allure.title('Проверка headers ответа Get /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_headers_request_get(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)
    Response(**response.json())
    GetBase().headers_checking_get(response)
