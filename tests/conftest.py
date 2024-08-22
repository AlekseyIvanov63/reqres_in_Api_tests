import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://reqres.in/api/users",
        help="This is request url"
    )


@pytest.fixture
def endpoint_api_users(request):
    return request.config.getoption("--url")
