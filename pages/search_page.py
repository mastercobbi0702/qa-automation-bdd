import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from config.settings import BASE_URL

logger = logging.getLogger(__name__)


class SearchPage(BasePage):
    """Page Object para la funcionalidad de búsqueda de MercadoLibre."""

    URL = BASE_URL

    # --- Locators ---
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.nav-search-input")
    RESULT_ITEMS = (By.CSS_SELECTOR, "li.ui-search-layout__item h2")

    # --- Actions ---

    def open(self):
        """Abre la página principal de MercadoLibre."""
        logger.info(f"Abriendo homepage: {self.URL}")
        super().open(self.URL)

    def write_product(self, product: str):
        """Escribe el término de búsqueda en la barra de búsqueda."""
        logger.info(f"Buscando producto: '{product}'")
        search_input = self.find_clickable(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(product)

    def press_enter(self):
        """Presiona Enter para ejecutar la búsqueda."""
        logger.info("Presionando Enter para buscar")
        self.find_element(self.SEARCH_INPUT).send_keys(Keys.ENTER)

    # --- Queries ---

    def get_results(self) -> list:
        """Retorna los elementos WebElement de los resultados de búsqueda."""
        return self.find_elements(self.RESULT_ITEMS)

    def get_result_titles(self) -> list[str]:
        """Retorna los títulos de los resultados como lista de strings."""
        titles = [el.text.strip() for el in self.get_results() if el.text.strip()]
        logger.info(f"Resultados encontrados: {len(titles)}")
        return titles

    def is_on_homepage(self) -> bool:
        """Verifica si el navegador está en la página principal."""
        return self.URL in self.get_current_url()