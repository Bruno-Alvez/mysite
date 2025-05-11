# tests/conftest.py

import pytest
from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')
