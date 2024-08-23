import allure
import requests
from base_requests.base import Base

class GetBase(Base):

    @allure.step('Get запрос')
    def get_request(self, endpoint):
        return requests.get(endpoint)

    @allure.step('Проверить headers GET запроса')
    def headers_checking_get(self, response):
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert response.headers['Transfer-Encoding'] == 'chunked'
        assert response.headers['Connection'] == 'keep-alive'
        assert response.headers['Vary'] == 'Accept-Encoding'
        assert response.headers['Server'] == 'cloudflare'
        assert response.headers['Content-Encoding'] == 'gzip'
        assert response.headers['Cache-Control'] == 'max-age=14400'
