from pages.base_page import BasePage


class AddPlayer (BasePage):
    email_button_xpath = "//main//div[2]/div/div[1]/div/div/input"
    phone_button_xpath = "//main//div[4]/div/div/input"
    age_button_xpath = "//main//div[7]/div/div/input"
    add_language_xpath = "//span[contains(text(),'Add language')]"
    add_link_you_tube_xpath = "//span[contains(text(),'Add link to Youtube')]"
    main_position_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/p"
    name_button_xpath = "//main//div[2]/div/label"
    surname_button_xpath = "//main//div[3]/div/div/input"
    height_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input"
    achievements_button_xpath = "// label[contains(text(), 'Achievements')]"

