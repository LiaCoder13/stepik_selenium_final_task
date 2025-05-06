from .base_page import BasePage
from .locators import ProductPageLocators
 
class ProductPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_btn.click()

    def should_be_product_added_to_basket(self):
        self.should_be_product_name()
        self.should_be_product_cost()
 
    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == product_name_in_basket, f"Expected {product_name}, get {product_name_in_basket}"
    
    def should_be_product_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        product_cost_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_BASKET).text
        assert product_cost == product_cost_in_basket, f"Expected {product_cost}, get {product_cost_in_basket}"