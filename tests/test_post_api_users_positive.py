import pytest
import allure
from base_requests.base import Base
from base_requests.post_base import PostBase
from data.data_post import DataPost
from model.post_model import PostResponse


@allure.epic("API")
@allure.title('Проверка статуса кода 201 POST /api/users ')
@pytest.mark.parametrize("expected", [201])
def test_post_status_code(endpoint_api_users, expected):
    params = DataPost().params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка json-схемы ответа POST /api/users ')
@pytest.mark.parametrize("expected", [201])
def test_post_json_schema(endpoint_api_users, expected):
    params = DataPost().params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)
    PostResponse(**response.json())


@allure.epic("API")
@allure.title('Проверка body ответа POST /api/users ')
@pytest.mark.parametrize("expected", [201])
def test_post_json_schema(endpoint_api_users, expected):
    params = DataPost().params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)
    data = response.json()
    PostResponse(**data)
    PostBase().comparison_body_response(data)


@allure.epic("API")
@allure.title('Проверка headers ответа POST /api/users ')
@pytest.mark.parametrize("expected", [201])
def test_post_headers(endpoint_api_users, expected):
    params = DataPost().params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)
    PostResponse(**response.json())
    PostBase().headers_checking_post(response)
