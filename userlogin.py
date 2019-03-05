def userLogin(un, pw, driver):
    """
    automates userLogin
    """
    # UserId, Password, btnlogin
    driver.find_element_by_id("UserId").send_keys(un)
    driver.find_element_by_id("Password").send_keys(pw)
    driver.find_element_by_id("btnlogin").click()


def userLoginIdirect(un, pw, driver):
    """
    automates userLogin
    """
    # div.@id=navigation-wrapper
    # div.navbar-header
    # div.add_on_menu_for_ipad hidden-lg hidden-xs
    # div.login_ipad visible-md visible-sm login_form
    # a.btn btn-primary
    # //div[@class='nav navbar-nav navbar-right visible-lg login_form']//a[@class='btn btn-primary'][contains(text(),'Login')]
    loginButton = "//div[@id='login_container_web']//a[@class='btn btn-primary'][contains(text(),'Login')]"
    # loginButton = "//div[@id='navigation-wrapper']/div[@class='navbar-header']/div[@class='add_on_menu_for_ipad hidden-lg hidden-xs']/div[@class='login_ipad visible-md visible-sm login_form']/a[@class='btn btn-primary']"
    driver.find_element_by_xpath(loginButton).click()

    driver.find_element_by_id("username").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id("login-command").click()
