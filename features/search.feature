# language: es

Característica: Búsqueda de producto en MercadoLibre

  Como usuario registrado
  Quiero buscar productos en MercadoLibre
  Para encontrar artículos disponibles en el marketplace

  @smoke @search
  Esquema del escenario: Buscar un producto válido retorna resultados relevantes

    Dado que estoy en la página principal de MercadoLibre
    Cuando escribo "<product>" en la barra de búsqueda
    Y presiono Enter
    Entonces debería ver resultados relacionados a "<product>"

    Ejemplos:
      | product |
      | laptop  |
      | celular |
      | teclado |

  @regression @search
  Escenario: Buscar con término vacío no abandona la página principal

    Dado que estoy en la página principal de MercadoLibre
    Cuando escribo "" en la barra de búsqueda
    Y presiono Enter
    Entonces debería permanecer en la página principal de MercadoLibre