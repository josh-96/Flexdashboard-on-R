import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def extract_surf_report(url, user_agent):
    
        
        headers = {'User-Agent': user_agent}
        page = requests.get(url, headers=headers) #extraire du texte à partir de l'URL
        soup = BeautifulSoup(page.content, 'html.parser')
        
        
        # Find the relevant elements using their class names
        date_elements = soup.find_all('div', class_='title')
        dates = [element.b.text.strip() for element in date_elements if element.b and not element.a]
        days = np.repeat(dates,8)
        
        
        #  Differentes heures
        time_elements = soup.find_all('div', class_='cell date with-border')
        times = [time.text.strip() for time in time_elements]
        
        # Différentes intervalles de la hauteur de la vague
        desc_list_vague = soup.find_all('div', class_ ="cell large waves with-border") # va chercher les informations pour lesquelles on a une balise td avec la classe desc
        # Extraer el texto de cada elemento
        desc_list_vague_text = [item.get_text() for item in desc_list_vague]

        desc_list_vague_text
        
        # Qualité de la vague
        desc_list_star = soup.find_all('div', class_ ="cell stars with-border") # va chercher les informations pour lesquelles on a une balise td avec la classe desc
        desc_list_star
        
        star_number = []
        for i in desc_list_star:
            a = 3 - (len(str(i).split('fa fa-star-o')) - 1) 
            star_number.append(a)
        star_number
        
        
        #extraction de la vitesse et la direction du vent :
        
        desc_list = soup.find_all('div', class_ ="cell large-bis-bis with-border") 
        orientation_vent = []
        vitesse_vent=[]
        
        

        for i in desc_list:
            i.text.replace('\n','')  
            orientation= str(i).split('alt="')[1].split('"')[0]
            i.text.replace('\n','')
            vitesse_vent.append( i.text.replace('\n',''))
            orientation_vent.append(orientation)
        
        # Constitution de la dataframe
        all_extract = {}
        all_extract['days'] = days
        all_extract['times'] = times
        all_extract['star'] = star_number
        all_extract['vague'] = desc_list_vague_text
        all_extract['orientation_vent'] = orientation_vent
        all_extract['vitesse_vent'] = vitesse_vent

        df_extract = pd.DataFrame(all_extract)
        
        # Exporter la base de données sous forme CSV
        df_extract.to_csv("set_path/surf_data.csv")

        


url= "https://www.surf-report.com/meteo-surf/lacanau-s1043.html"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
extract_surf_report(url, user_agent)
print("success")
        
        
        
        
        
        

