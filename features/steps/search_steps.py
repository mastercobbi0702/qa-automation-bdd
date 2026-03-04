import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers

from pages.search_page import SearchPage

FEATURE_FILE = str(Path(__file__).parent.parent / "search.feature")

# Vincula todos los escenarios del feature con estos step definitions
scenarios(FEATURE_FILE)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def search_page(driver):
    """Fixture que retorna una instancia de SearchPage lista para usar."""
    return SearchPage(driver)


# ---------------------------------------------------------------------------
# Steps — Esquema del escenario: Buscar un producto válido
# ---------------------------------------------------------------------------

@given("que estoy en la página principal de MercadoLibre")
def open_homepage(search_page):
    search_page.open()


@when(parsers.parse('escribo "{product}" en la barra de búsqueda'))
def write_product(search_page, product):
    search_page.write_product(product)


@when("presiono Enter")
def press_enter(search_page):
    search_page.press_enter()


@then(parsers.parse('debería ver resultados relacionados a "{product}"'))
def verify_results(search_page, product):
    titles = search_page.get_result_titles()

    assert len(titles) > 0, (
        f"No se encontraron resultados para '{product}'"
    )

    product_lower = product.lower()
    matching = [t for t in titles if product_lower in t.lower()]

    assert len(matching) > 0, (
        f"Ningún resultado contiene '{product}'.\n"
        f"Primeros resultados encontrados: {titles[:5]}"
    )


# ---------------------------------------------------------------------------
# Steps — Escenario: Búsqueda vacía
# ---------------------------------------------------------------------------

@when('escribo "" en la barra de búsqueda')
def write_empty_search(search_page):
    search_page.write_product("")


@then("debería permanecer en la página principal de MercadoLibre")
def verify_on_homepage(search_page):
    assert search_page.is_on_homepage(), (
        f"El usuario fue redirigido fuera del homepage. "
        f"URL actual: {search_page.get_current_url()}"
    )