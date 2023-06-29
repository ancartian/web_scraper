import requests
from bs4 import BeautifulSoup

# URL de la página web a scrape
url = "https://es.wikipedia.org/wiki/Historia_de_la_Argentina"

# Realizar la solicitud HTTP GET
response = requests.get(url)

# Verificar el estado de la solicitud
if response.status_code == 200:
    # Parsear el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Ejemplo: Extraer todos los enlaces de la página
    enlaces = soup.find_all("a")
    for enlace in enlaces:
        print(enlace.get("href"))
else:
    print("Error al realizar la solicitud:", response.status_code)
