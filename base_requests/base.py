import allure


class Base:

    @allure.step('Проверка статуса кода')
    def status_code_checking(self, response, status_code):
        assert response.status_code == status_code
