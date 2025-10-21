import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("AUTOUSE. Sending data to analytics service")


@pytest.fixture(scope="session")
def settings():
    print("SESSION. Initializing autotests settings")

@pytest.fixture(scope="class")
def user():
    print("CLASS. Creating users data 1 time per test class")

@pytest.fixture(scope="function")
def browser():
    print("FUNCTION. Opening browser per autotest")

class TestUserFlow:
    def test_user_can_login(self,settings,user,browser):
        ...

    def test_user_can_create_course(self,settings,user,browser):
        ...

class TestAccountFlow:
    def test_user_account(self,settings,user,browser):
        ...