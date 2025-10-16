import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regression
def test_regresssion_case():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        ...

    def test_logout(self):
        ...


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.critical
def test_critical_login():
    ...
