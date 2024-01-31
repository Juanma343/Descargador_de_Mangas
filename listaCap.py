import configurar_webdriver

from selenium.webdriver.common.by import By

def listaAnz(url):
    driver = configurar_webdriver.iniciar_Chrome()
    driver.get(url)
    lista = driver.find_element(By.CSS_SELECTOR, "ul.chapters").find_elements(By.CSS_SELECTOR, "li")
    listaSalida = []
    for i in lista:
        listaSalida.append([i.find_element(By.CSS_SELECTOR, "h5.chapter-title-rtl").text,i.find_element(By.CSS_SELECTOR, "h5.chapter-title-rtl").find_element(By.CSS_SELECTOR, "a").get_property("href")])
        # print(i.find_element(By.CSS_SELECTOR, "h5.chapter-title-rtl").text)
        # print(i.find_element(By.CSS_SELECTOR, "h5.chapter-title-rtl").find_element(By.CSS_SELECTOR, "a").get_property("href"))
    driver.quit()
    return listaSalida
    # estado = driver.find_element(By.CSS_SELECTOR, "span.label-success").text

def finalizadoAnz(url):
    driver = configurar_webdriver.iniciar_Chrome()
    driver.get(url)
    estado = driver.find_element(By.CSS_SELECTOR, "span.label").text
    driver.quit()
    if estado == "Finalizado":
        return True
    else:
        return False

if __name__ == "__main__":
    url = "https://www.anzmangashd.com/manga/heros"
    print(finalizadoAnz(url))