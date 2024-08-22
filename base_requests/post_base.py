import allure
import requests
from base_requests.base import Base

class PostBase(Base):

    @allure.step('POST запрос')
    def post_request(self, endpoint, params):
        response = requests.post(endpoint, data=params)

        if response.status_code == 201:
            return response
        else:
            print(f"Произошла ошибка: {response.status_code}")
            print(response.text)
