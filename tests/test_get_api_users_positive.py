import pytest
import allure
from model.get_model import GetResponse
from base_requests.get_base import GetBase
from base_requests.base import Base


@allure.epic("API")
@allure.feature('Positive tests GET')
@allure.title('Проверка статуса кода 200 GET /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_get_status_code(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.feature('Positive tests GET')
@allure.title('Проверка json-схемы ответа GET /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_get_json_schema(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)
    GetResponse(**response.json())


@allure.epic("API")
@allure.feature('Positive tests GET')
@allure.title('Проверка headers ответа GET /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_get_headers(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)
    GetResponse(**response.json())
    GetBase().headers_checking_get(response)
