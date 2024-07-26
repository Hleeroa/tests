import pytest
import requests
import selenium
from selenium import webdriver
from functions.main import perimeter, area, quadratics


# -------------------------------------task#1----------------------------------------------------

@pytest.mark.parametrize(
    'a, b, expected',
    ([2, 3, 10],
     [2, 2, 8],
     )
)
def test_perimeter_1(a, b, expected):
    actual = perimeter(a, b)
    assert actual == expected


@pytest.mark.xfail
def test_perimeter_2():
    a = 3
    b = 0
    expected = 0
    actual = perimeter(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    'a, b, expected',
    ([2, 3, 6],
     [2, 2, 4],
     )
)
def test_area_1(a, b, expected):
    actual = area(a, b)
    assert actual == expected


@pytest.mark.xfail
def test_area_2():
    a = 3
    b = 0
    expected = 0
    actual = area(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    'a, b, c, expected',
    ([1, 2, 3, 'Kорней нет'],
     [-1, 2, 3, (-1, 3)],
     [1, 2, 1, -1]
     )
)
def test_quadratics_1(a, b, c, expected):
    actual = quadratics(a, b, c)
    assert actual == expected

# -------------------------------------task#2----------------------------------------------------

class TestYandexDisk:
    def set_up(self):
        headers = {'Authorization': 'OAuth <<enter_your_OAuth_here>>'}    # enter your access token from Yandex Poligon here
        return headers

    def test_create_folder_201(self):
        params = {'path': 'pass'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources?',
                                headers=self.set_up(),
                                params=params)
        assert response.status_code == 201

    def test_create_folder_409(self):
        params = {'path': 'pass'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources?',
                                headers=self.set_up(),
                                params=params)
        assert response.status_code == 409

    def test_create_folder_401(self):
        params = {'path': 'pass'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources?',
                                params=params)
        assert response.status_code == 401

    def test_create_folder_400(self):
        params = {'path': 'pass'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources?',
                                headers=self.set_up())
        assert response.status_code == 400

    def test_create_folder_404(self):
        params = {'path': 'pass'}
        response = requests.put(url='https://cloud-api.yandex.net/v1/disk/resource?',
                                headers=self.set_up(),
                                params=params)
        assert response.status_code == 404


# -------------------------------------task#3----------------------------------------------------
class TestYandexAuth:
    def setup(self):
        driver = webdriver.Chrome()
        return driver

    def test_ya_auth(self):
        driver = self.setup()
        driver.get("https://passport.yandex.ru/auth/")
        assert "Авторизация" in driver.title

    def teardown(self):
        self.setup().close()
