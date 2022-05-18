from pages import SearchHelper
import requests


def test_search_books(browser):     #проверяем наличие произведений писателя
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.enter_word("мандзони")
    main_page.click_on_the_search_button()
    elements = main_page.check_results()
    assert len(elements) > 0


def test_button_homepage(browser):     #проверяем статус-код перехода на главную страницу
    main_page = SearchHelper(browser)
    main_page.current_page()
    main_page.click_homepage()
    response = requests.get(url='https://www.bookvoed.ru/')
    assert response.status_code == 200, "Wrong response code"


def test_catalog_button(browser):  # проверяем наличие выпадающего меню "каталог"
    main_page = SearchHelper(browser)
    main_page.current_page()
    main_page.click_on_the_catalog_button()
    element = main_page.check_sidebar()
    assert element != 0


def test_hello_spb(browser):     #проверяем статус-код перехода на страницу по ссылке из header-меню
    main_page = SearchHelper(browser)
    main_page.go_to_page()
    main_page.click_hello_spb()
    response = requests.get(url="https://www.bookvoed.ru/goods-from-spb")
    assert response.status_code == 200, "Wrong response code"


def test_auth_form(browser):     #проверяем отображение поля авторизации
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.click_cabinet()
    auth = main_page.check_auth()
    assert auth.is_displayed


def test_auth_log_field(browser):     #проверяем отображение поля ввода "логин/.." авторизации
    main_page = SearchHelper(browser)
    main_page.current_page()
    main_page.click_cabinet()
    auth_log_field = main_page.check_auth_log_field()
    assert auth_log_field.is_displayed


def test_auth_pass_field(browser):      #проверяем отображение поля "пароль" автооризации
    main_page = SearchHelper(browser)
    main_page.current_page()
    main_page.click_cabinet()
    auth_pass_field = main_page.check_auth_pass_field()
    assert auth_pass_field.is_displayed


def test_auth_button_enter(browser):     #проверяем отображение кнопки "войти"
    main_page = SearchHelper(browser)
    main_page.current_page()
    main_page.click_cabinet()
    auth_button_enter = main_page.check_auth_button_enter()
    assert auth_button_enter.is_displayed


def test_invalid_auth(browser):      #проверяем выводится ли сообщение об ошибке
    main_page = SearchHelper(browser)
    main_page.current_page()
    main_page.enter_log()
    main_page.enter_pass()
    main_page.click_auth_button_enter()
    res = main_page.check_response_invalid_auth()
    assert res.is_displayed
