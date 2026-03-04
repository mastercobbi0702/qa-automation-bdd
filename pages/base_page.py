import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.settings import EXPLICIT_WAIT

logger = logging.getLogger(__name__)


class BasePage:
    """
    Clase base para todos los Page Objects.
    Centraliza el manejo de waits, búsqueda de elementos y acciones comunes.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open(self, url: str):
        """Navega a una URL específica."""
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def find_element(self, locator: tuple):
        """Espera a que el elemento esté presente en el DOM y lo retorna."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element not found after {EXPLICIT_WAIT}s: {locator}")
            raise

    def find_clickable(self, locator: tuple):
        """Espera a que el elemento sea clickeable y lo retorna."""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            logger.error(f"Element not clickable after {EXPLICIT_WAIT}s: {locator}")
            raise

    def find_elements(self, locator: tuple) -> list:
        """Espera a que al menos un elemento esté presente y retorna la lista."""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            logger.warning(f"No elements found for: {locator}")
            return []

    def get_current_url(self) -> str:
        """Retorna la URL actual del navegador."""
        return self.driver.current_url

    def get_title(self) -> str:
        """Retorna el título de la página actual."""
        return self.driver.title