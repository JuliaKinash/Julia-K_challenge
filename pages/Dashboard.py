from pages.base_page import BasePage


class Dashboard (BasePage):
    button_xpath = "//*[@id='login']"
    scouts_panel_button_xpath = "//h6[contains(@class,'MuiTypography-h6')]"
    main_page_button_xpath = "//ul[1]/div[1]/div[2]/span"
    players_count ="//main/div[2]/div[1]//b"
    events_count_xpath = "//main/div[2]/div[4]/div/div[1]"
    dev_team_photo_xpath = "//*[contains(@class,'MuiCardMedia-root jss8')]"
    dev_team_button_xpath ='//main/div[3]//a[1]/span[2]'
    add_player_button_xpath ="//span[contains(text(),'Add player')]"
    matches_count_xpath ="//main/div [2]/div [2]//b"
    activity_button_xpath = "//h2[contains(text(),'Activity')]"

