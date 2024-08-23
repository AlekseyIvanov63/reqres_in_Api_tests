import allure
import requests
from base_requests.base import Base
from data.data_post import DataPost

class PostBase(Base):

    @allure.step('POST запрос')
    def post_request(self, endpoint, params):
        response = requests.post(endpoint, data=params)

        if response.status_code == 201:
            return response
        else:
            print(f"Произошла ошибка: {response.status_code}")
            print(response.text)


    @allure.step('Сравнение body ответа с body запроса')
    def comparison_body_response(self, response):
        assert DataPost().posit_params['name'] == response['name']
        assert DataPost().posit_params['job'] == response['job']

    @allure.step('Проверить headers POST запроса')
    def headers_checking_post(self, response):
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert response.headers['Connection'] == 'keep-alive'
        assert response.headers['X-Powered-By'] == 'Express'
        assert response.headers['Server'] == 'cloudflare'
        assert response.headers['Via'] == '1.1 vegur'
        assert response.headers['CF-Cache-Status'] == 'DYNAMIC'
