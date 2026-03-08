import pytest

@pytest.mark.xfail(reason="detected bug in the app, due to it test is failing with an error")
def test_with_bug():
    assert 1==2

@pytest.mark.xfail(reason="bug fixed, but test still have mark xfail")
def test_without_bug():
    ...