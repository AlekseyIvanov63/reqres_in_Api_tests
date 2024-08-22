import pytest
import allure
from base_requests.base import Base
from base_requests.post_base import PostBase
from data.data_post import DataPost


@allure.epic("API")
@allure.title('Проверка статуса кода 201 POST /api/users ')
@pytest.mark.parametrize("expected", [201])
def test_status_code_request_post(endpoint_api_users, expected):
    params = DataPost().params
    response = PostBase().post_request(endpoint_api_users, params)
    Base().status_code_checking(response, expected)
