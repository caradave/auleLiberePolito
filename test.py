from bs4 import BeautifulSoup
import requests

url = 'https://www.swas.polito.it/dotnet/orari_lezione_pub/RicercaAuleLiberePerFasceOrarie.aspx'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

divName='Pagina_gv_AuleLibere_lbl_AuleLibere_'
fasciaOraria='Pagina_gv_AuleLibere_lbl_FasciaOraria_'
allFree=dict()
a=0
end=False


while(end!=True):
    try:
        orario=((soup.find_all('span', id=fasciaOraria+str(a)))[0].get_text(separator=" ", strip=True))
        aule=((soup.find_all('span', id=divName+str(a)))[0].get_text(separator=" ", strip=True))
        a+=1
    except:
        end=True
    if(end!=True):
        allFree[orario]=aule


        
print(allFree)