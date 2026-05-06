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

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1280, "height": 720},
    }

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": True   # 🔥 QUAN TRỌNG
    }