import pytest
from core.config import Config


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests against")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def config(env):
    return Config(env=env)


@pytest.fixture(scope="session")
def base_url(config):
    return config.base_url