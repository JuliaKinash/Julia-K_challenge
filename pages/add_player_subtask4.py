import time
from turtle import position

import self as self

from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    add_player_button_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name=surname']"
    age_field_xpath = "//input[@name='age']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//form/div[3]/button[1]/span[1]"
    add_player_form_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add/'
    expected_title = "Add player"
    title_of_box_xpath = "//form/descendant::div/div/span[2]"
    header_of_box = 'Add player'

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, name):
        self.field_send_keys(self.main_position_field_xpath, name)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_form_url) == self.expected_title
