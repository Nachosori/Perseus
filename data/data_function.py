import requests
from bs4 import BeautifulSoup
import pandas as pd

# Extrae de la pagina web la tabla con las palabras y sus traducciones.

def table_html(url):
    html = requests.get(url).content
    df_list = pd.read_html(html, encoding="utf-8")
    df = df_list[-1]
    return df

# Limpia la tabla para que se queden solo los datos necesarios.

def table_cleaning(df):
    df = df[[('Unnamed: 1_level_0','Word'), ('Unnamed: 7_level_0', 'Definition')]]
    df.columns = ["Word", "Definition"]
    df = df.dropna()
    df[df["Definition"] == "[unavailable]"].index
    df = df.drop(df[df["Definition"] == "[unavailable]"].index)
    return df

