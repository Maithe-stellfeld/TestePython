from selenium import webdriver
from selenium.webdriver.common.by import By

class HotmartPagina:
    def init(self, driver):
        self.driver = driver
        self.seletor_logotipo = (By.CSS_SELECTOR, "a.navbar-brand")

    def verificar_logotipo_presente(self):
        logotipo = self.driver.find_element(*self.seletor_logotipo)
        return logotipo.is_displayed()

def test_verificar_logotipo_presente_hotmart():
    url = "https://www.hotmart.com/"
    driver = webdriver.Chrome()  
    driver.get(url)

    pagina = HotmartPagina(driver)
    resultado = pagina.verificar_logotipo_presente()

    driver.quit()

    assert resultado, "O logotipo não está presente na página."

test_verificar_logotipo_presente_hotmart()
