# -*- coding: utf-8 -*-
"""Calendario oficial del Mundial 2026 (fixturedownload.com).

Aporta lo que el scraping de FlashScore no tenía: la hora exacta de inicio en
UTC de cada partido y los resultados reales de los ya jugados. Con la hora UTC
y la sede se calcula la fecha local del estadio, que es la fecha "oficial" del
partido (las fechas del scraping venían en hora europea y los partidos
nocturnos de América aparecían corridos un día).

El feed se intenta refrescar en cada ejecución; si la descarga falla se usa la
copia guardada en Data/calendario_oficial.json.
"""

import os
import json
import urllib.request
from datetime import datetime, timedelta

FEED_URL = 'https://fixturedownload.com/feed/json/fifa-world-cup-2026'
RUTA_JSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         'Data', 'calendario_oficial.json')

# Nombres del feed (inglés) -> nombres del repo (español)
NOMBRES_ES = {
    'Algeria': 'Argelia', 'Argentina': 'Argentina', 'Australia': 'Australia',
    'Austria': 'Austria', 'Belgium': 'Bélgica', 'Bosnia and Herzegovina': 'Bosnia-Herzegovina',
    'Brazil': 'Brasil', 'Cabo Verde': 'Cabo Verde', 'Canada': 'Canadá',
    'Colombia': 'Colombia', 'Congo DR': 'RD Congo', 'Croatia': 'Croacia',
    'Curaçao': 'Curazao', 'Czechia': 'República Checa', "Côte d'Ivoire": 'Costa de Marfil',
    'Ecuador': 'Ecuador', 'Egypt': 'Egipto', 'England': 'Inglaterra',
    'France': 'Francia', 'Germany': 'Alemania', 'Ghana': 'Ghana',
    'Haiti': 'Haití', 'IR Iran': 'Irán', 'Iraq': 'Irak',
    'Japan': 'Japón', 'Jordan': 'Jordania', 'Korea Republic': 'Corea del Sur',
    'Mexico': 'México', 'Morocco': 'Marruecos', 'Netherlands': 'Países Bajos',
    'New Zealand': 'Nueva Zelanda', 'Norway': 'Noruega', 'Panama': 'Panamá',
    'Paraguay': 'Paraguay', 'Portugal': 'Portugal', 'Qatar': 'Catar',
    'Saudi Arabia': 'Arabia Saudí', 'Scotland': 'Escocia', 'Senegal': 'Senegal',
    'South Africa': 'Sudáfrica', 'Spain': 'España', 'Sweden': 'Suecia',
    'Switzerland': 'Suiza', 'Tunisia': 'Túnez', 'Türkiye': 'Turquía',
    'USA': 'EE. UU.', 'Uruguay': 'Uruguay', 'Uzbekistan': 'Uzbekistán',
}

# Desfase horario de cada sede en junio/julio de 2026 (con horario de verano en
# EE. UU./Canadá; México ya no aplica DST)
OFFSET_SEDES = {
    'Mexico City Stadium': -6, 'Guadalajara Stadium': -6, 'Monterrey Stadium': -6,
    'Toronto Stadium': -4, 'Boston Stadium': -4, 'New York/New Jersey Stadium': -4,
    'Philadelphia Stadium': -4, 'Miami Stadium': -4, 'Atlanta Stadium': -4,
    'Dallas Stadium': -5, 'Houston Stadium': -5, 'Kansas City Stadium': -5,
    'Los Angeles Stadium': -7, 'San Francisco Bay Area Stadium': -7,
    'Seattle Stadium': -7, 'BC Place Vancouver': -7,
}

CIUDADES = {
    'Mexico City Stadium': 'Ciudad de México', 'Guadalajara Stadium': 'Guadalajara',
    'Monterrey Stadium': 'Monterrey', 'Toronto Stadium': 'Toronto',
    'Boston Stadium': 'Boston', 'New York/New Jersey Stadium': 'Nueva York/NJ',
    'Philadelphia Stadium': 'Filadelfia', 'Miami Stadium': 'Miami',
    'Atlanta Stadium': 'Atlanta', 'Dallas Stadium': 'Dallas',
    'Houston Stadium': 'Houston', 'Kansas City Stadium': 'Kansas City',
    'Los Angeles Stadium': 'Los Ángeles', 'San Francisco Bay Area Stadium': 'San Francisco',
    'Seattle Stadium': 'Seattle', 'BC Place Vancouver': 'Vancouver',
}


def refrescar_feed():
    """Descarga el feed y lo guarda en Data/. Devuelve True si lo consiguió."""
    try:
        peticion = urllib.request.Request(FEED_URL, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/126.0 Safari/537.36'})
        with urllib.request.urlopen(peticion, timeout=30) as r:
            datos = json.loads(r.read().decode('utf-8'))
        if isinstance(datos, list) and len(datos) >= 72:
            with open(RUTA_JSON, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False)
            return True
    except Exception as e:
        print(f'  (no se pudo refrescar el calendario oficial: {e}; uso la copia local)')
    return False


def cargar_partidos_grupos(refrescar=True):
    """Lista de partidos de la fase de grupos con nombres en español:
    [{'local','visitante','utc','fecha_oficial','ciudad','gl','gv'}].
    'fecha_oficial' es la fecha local del estadio; gl/gv son los goles reales
    (None si aún no se ha jugado)."""
    if refrescar:
        refrescar_feed()
    with open(RUTA_JSON, encoding='utf-8') as f:
        feed = json.load(f)

    partidos = []
    for m in feed:
        if not m.get('Group'):
            continue  # eliminatorias: equipos aún por determinar
        local, visitante = NOMBRES_ES.get(m['HomeTeam']), NOMBRES_ES.get(m['AwayTeam'])
        if not local or not visitante:
            raise ValueError(f"Equipo sin traducción: {m['HomeTeam']} / {m['AwayTeam']}")
        utc = datetime.strptime(m['DateUtc'], '%Y-%m-%d %H:%M:%SZ')
        offset = OFFSET_SEDES.get(m['Location'], -5)
        fecha_oficial = (utc + timedelta(hours=offset)).strftime('%Y-%m-%d')
        partidos.append({
            'local': local, 'visitante': visitante,
            'utc': utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'fecha_oficial': fecha_oficial,
            'ciudad': CIUDADES.get(m['Location'], m['Location']),
            'gl': m.get('HomeTeamScore'), 'gv': m.get('AwayTeamScore'),
        })
    return partidos


def mapa_fechas_oficiales(refrescar=True):
    """{(local, visitante): fecha_oficial} con la orientación del feed y la
    invertida, para casar con el orden del repo sea cual sea."""
    mapa = {}
    for p in cargar_partidos_grupos(refrescar):
        mapa[(p['local'], p['visitante'])] = p['fecha_oficial']
        mapa.setdefault((p['visitante'], p['local']), p['fecha_oficial'])
    return mapa
