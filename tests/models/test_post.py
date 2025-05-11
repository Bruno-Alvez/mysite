import pytest


@pytest.fixture
def post_published():

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'