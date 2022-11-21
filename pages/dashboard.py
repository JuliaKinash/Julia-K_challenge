import time

from pages.base_page import BasePage
class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    scouts_panel_button_xpath = "//h6[contains(@class,'MuiTypography-h6')]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_count = "//main/div[2]/div[1]//b"
    events_count_xpath = "//main/div[2]/div[4]/div/div[1]"
    dev_team_photo_xpath = "//*[contains(@class,'MuiCardMedia-root jss8')]"
    dev_team_button_xpath = '//main/div[3]//a[1]/span[2]'
    matches_count_xpath = "//main/div [2]/div [2]//b"
    activity_button_xpath = "//h2[contains(text(),'Activity')]"
    expected_title = "Scouts panel"
    dashboard_url ='https://scouts-test.futbolkolektyw.pl/'
    add_player_button_xpath = "//main/div[3]/div[2]/div/div/a/button/span[1]"
    futbal_kolektyw_logo_xpath ="//*[@title='Logo Scouts Panel']"

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.futbal_kolektyw_logo_xpath)
        assert self.expected_title(self.dashboard_url) == self.expected_title
    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

