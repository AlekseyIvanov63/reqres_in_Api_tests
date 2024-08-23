import pytest
import allure
from base_requests.base import Base
from base_requests.post_base import PostBase
from data.data_post import DataPost


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, нет поля "name" в запросе')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_no_name(endpoint_api_users, expected):
    params = DataPost().no_name_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, нет поля "job" в запросе')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_no_job(endpoint_api_users, expected):
    params = DataPost().no_job_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, без тела запроса')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_no_body(endpoint_api_users, expected):
    params = DataPost().no_body_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, количество символов в "name" 100')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_max_name(endpoint_api_users, expected):
    params = DataPost().max_name_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, количество символов в "job" 100')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_max_job(endpoint_api_users, expected):
    params = DataPost().max_job_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, пустое поле "name"')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_empty_name(endpoint_api_users, expected):
    params = DataPost().empty_name_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)


@allure.epic("API")
@allure.title('Проверка статуса кода 400 POST, пустое поле "job"')
@pytest.mark.parametrize("expected", [400])
def test_post_negative_empty_job(endpoint_api_users, expected):
    params = DataPost().empty_job_params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)
