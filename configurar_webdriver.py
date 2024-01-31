# Descarga e instala el driver de Chrome para Selenium
from webdriver_manager.chrome import ChromeDriverManager
# Importa el driver de selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# para modificar las opciones del websdriver
from selenium.webdriver.chrome.options import Options


def iniciar_Chrome():
    """Inicia chrome y lo configura"""
    
    # Intstalamos el driver de chrome
    ruta = ChromeDriverManager().install()
    # OPCIONES DE CHROME
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f'user-agent={user_agent}') # Cambia el user agent
    # options.add_argument("--headless") # Ejecuta chrome en modo headless
    options.add_argument("--window-size=1000,1000") # Cambia el tamaño de la ventana
    # options.add_argument("--start-maximized") # Maximiza la ventana
    options.add_argument("--disable-extensions") # Desactiva las extensiones
    options.add_argument("--disable-web-security") # Desactiva la politica de mismo origen o Same Origin Policy (SOP)
    options.add_argument("--disable-notifications") # Desactiva las notificaciones de chrome
    options.add_argument("--ignore-certificate-errors") # Ignora los errores de certificado
    options.add_argument("--no-sandbox") # Desactiva el sandbox
    options.add_argument("--log-level=3") # Desactiva los logs, con el 3 no se mustra nada en el log
    options.add_argument("--allow-running-insecure-content") # Permite correr contenido inseguro
    options.add_argument("--no-default-browser-check") # No comprueba si es el navegador por defecto
    options.add_argument("--no-first-run") # No ejecuta la primera ejecución
    options.add_argument("--no-proxy-server") # No usa un servidor proxy
    options.add_argument("--disable-blink-features=AutomationControlled") # Desactiva el navigator webdriver para que no detecte el bot
    # PARAMETROS PARA OMITIR EN EL INICIO DE CHRMOEDRIVER
    exp_opt = [
            'enable-automation' # Parametro a omitir
            'ignore-certificate-errors', # Para ignnorar errores de certificado
            'enable-logging', # Para habilitar los logs de listening
        ]
    options.add_experimental_option('excludeSwitches', exp_opt) # Omitimos el parametro enable-automation
    # PARAMETROS QUE DEFINEN PREFERENCIAS EN CHRMEDRIVER
    prefs = {
        "profile.default_content_setting_values.notifications": 2, # 1: Permitir, 2: Bloquear, 0: Preguntar
        "intl.accept_languages": ["es-ES", "es"], # Cambia el idioma de chrome
        "credentials_enable_service": False, # Desactiva el guardado de contraseñas
        }
    options.add_experimental_option('prefs', prefs) # Omitimos el parametro enable-automation

    # Insatanciamos el servicio de chromeDriver
    s = Service(ruta)
    # Iniciamos el webdriver de selenium con chrome
    driver = webdriver.Chrome(service=s, options=options)  # añadimos el argumento options=options para que se apliquen las opciones
    # posicionar la ventana en la esquina superior izquierda
    driver.set_window_position(0, 0)
    # Devolvemos el driver
    return driver

if __name__ == "__main__":
    driver = iniciar_Chrome()
    driver.get("https://www.google.com")
    print(driver.page_source)
    driver.quit()