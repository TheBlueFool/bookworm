import pytest
from selenium import webdriver

from bookworm import create_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    # create the app with common test config
    app = create_app({
        'TESTING': True,
        'FLASK_ENV': 'development'
    })

    # create the database and load test data
    with app.app_context():
        pass

    yield app

    # close and remove the temporary database
    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def browser():
    """Create and configure a new firefox browser instance for each test."""
    browser = webdriver.Firefox()

    yield browser

    browser.quit()
