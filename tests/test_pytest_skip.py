import pytest

@pytest.mark.skip(reason="feature in development")
def test_feature_in_development():
    ...

@pytest.mark.skip(reason="feature in development")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...
