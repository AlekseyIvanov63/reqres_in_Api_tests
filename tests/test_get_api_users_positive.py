import pytest
import allure
from model.base_model import Response
from base_requests.get_base import GetBase
from base_requests.base import Base


@allure.epic("API")
@allure.title('Проверка статуса кода 200 GET /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_status_code_request_get(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка json-схемы ответа GET /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_json_schema_request_get(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)
    Response(**response.json())


@allure.epic("API")
@allure.title('Проверка headers ответа GET /api/users ')
@pytest.mark.parametrize("expected", [200])
def test_headers_request_get(endpoint_api_users, expected):
    response = GetBase().get_request(endpoint_api_users)
    Base().status_code_checking(response, expected)
    Response(**response.json())
    GetBase().headers_checking_get(response)
