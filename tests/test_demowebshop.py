import allure
from selene import have


def test_auth(app):
    app.open("")
    with allure.step('Проверка успешной авторизации'):
        app.element(".account").should(have.text("vgtrk520@yandex.ru"))


def test_delete_product_from_wishlist(demoshop, app):
    app.open("")
    with allure.step('Добавление товара в список желаемого'):
        demoshop.add_product_to_wishlist()
    with allure.step('Проверка удаления товара из списка желаемого'):
        app.element('.ico-wishlist').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_cart(demoshop, app):
    app.open("")
    with allure.step('Добавление товара в карзину'):
        demoshop.add_product_to_cart()
    with allure.step('Проверка удаления товара из карзины'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_delete_customer_address(demoshop, app):
    app.open("")
    with allure.step('Добавление адреса'):
        demoshop.add_address_user()
    with allure.step('Проверка удаления адреса'):
        app.element('.account').click()
        app.element('.side-2 [href="/customer/addresses"]').click()
        app.element('.delete-address-button').click()
        app.driver.switch_to.alert.accept()
        app.element('.address-list').with_(timeout=20).should(have.text('No addresses'))


def test_logout(app):
    app.open("")
    with allure.step('Проверка логаута'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))
