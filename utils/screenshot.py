import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def take_screenshot(driver, name: str, directory: str = "screenshots") -> str:
    """
    Captura una screenshot del navegador y la guarda en el directorio indicado.

    Args:
        driver: Instancia del WebDriver de Selenium.
        name: Nombre base del archivo (sin extensión).
        directory: Carpeta donde guardar la screenshot.

    Returns:
        Ruta absoluta del archivo guardado.
    """
    os.makedirs(directory, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"{name}_{timestamp}.png")
    driver.save_screenshot(filename)
    logger.info(f"Screenshot guardada: {filename}")
    return filename
