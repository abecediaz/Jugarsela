from passlib.hash import pbkdf2_sha256
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from datetime import datetime
import random
import requests
import time
import csv
import os

from informacion_api import informacion_api
def apixd():
    informacion_api: list = [{2015: [('Boca Juniors', '64'), ('San Lorenzo', '61'), ('Rosario Central', '59'), ('Racing Club', '57'), ('Independiente', '54'), ('Belgrano Cordoba', '51'), ('Estudiantes L.P.', '51'), ('Banfield', '50'), ('River Plate', '49'), ('Tigre', '46'), ('Quilmes', '45'), ('Gimnasia L.P.', '44'), ('Lanus', '42'), ('Union Santa Fe', '41'), ('Aldosivi', '40'), ('Newells Old Boys', '40'), ('San Martin S.J.', '37'), ('Olimpo Bahia Blanca', '36'), ('Colon Santa Fe', '34'), ('Argentinos JRS', '33'), ('Defensa Y Justicia', '32'), ('Godoy Cruz', '32'), ('Huracan', '30'), ('Sarmiento Junin', '30'), ('Temperley', '30'), ('Nueva Chicago', '29'), ('Velez Sarsfield', '29'), ('Arsenal Sarandi', '27'), ('Atletico DE Rafaela', '23'), ('Crucero Del Norte', '14')], 2016: [('Boca Juniors', '63'), ('River Plate', '56'), ('Estudiantes L.P.', '56'), ('Racing Club', '55'), ('Banfield', '54'), ('Independiente', '53'), ('San Lorenzo', '53'), ('Lanus', '50'), ('Newells Old Boys', '49'), ('Defensa Y Justicia', '49'), ('Colon Santa Fe', '49'), ('Rosario Central', '44'), ('Gimnasia L.P.', '43'), ('Godoy Cruz', '43'), ('Talleres Cordoba', '42'), ('Olimpo Bahia Blanca', '38'), ('Atletico DE Rafaela', '37'), ('Temperley', '37'), ('Velez Sarsfield', '37'), ('Patronato', '34'), ('Atletico Tucuman', '33'), ('San Martin S.J.', '33'), ('Union Santa Fe', '32'), ('Tigre', '31'), ('Huracan', '29'), ('Sarmiento Junin', '28'), ('Arsenal Sarandi', '27'), ('Belgrano Cordoba', '26'), ('Quilmes', '25'), ('Aldosivi', '25')], 2017: [('Boca Juniors', '37'), ('Talleres Cordoba', '30'), ('San Lorenzo', '28'), ('Godoy Cruz', '27'), ('Union Santa Fe', '26'), ('Independiente', '25'), ('Huracan', '24'), ('Estudiantes L.P.', '24'), ('Belgrano Cordoba', '24'), ('Atletico Tucuman', '23'), ('Argentinos JRS', '23'), ('Colon Santa Fe', '23'), ('Racing Club', '22'), ('Defensa Y Justicia', '21'), ('San Martin S.J.', '21'), ('Patronato', '20'), ('Rosario Central', '20'), ('Banfield', '19'), ('River Plate', '18'), ('Gimnasia L.P.', '18'), ('Lanus', '18'), ('Velez Sarsfield', '17'), ('Newells Old Boys', '13'), ('Chacarita Juniors', '12'), ('Tigre', '12'), ('Temperley', '12'), ('Olimpo Bahia Blanca', '9'), ('Arsenal Sarandi', '7')], 2018: [('Racing Club', '57'), ('Defensa Y Justicia', '53'), ('Boca Juniors', '51'), ('River Plate', '45'), ('Atletico Tucuman', '42'), ('Velez Sarsfield', '40'), ('Independiente', '38'), ('Union Santa Fe', '36'), ('Tigre', '36'), ('Huracan', '35'), ('Lanus', '34'), ('Talleres Cordoba', '33'), ('Aldosivi', '33'), ('Godoy Cruz', '32'), ('Newells Old Boys', '29'), ('Banfield', '29'), ('Estudiantes L.P.', '29'), ('Gimnasia L.P.', '29'), ('Patronato', '26'), ('Rosario Central', '26'), ('San Martin S.J.', '25'), ('Belgrano Cordoba', '24'), ('San Lorenzo', '23'), ('Colon Santa Fe', '23'), ('San Martin Tucuman', '23'), ('Argentinos Jrs', '22')], 2019: [('Boca Juniors', '48'), ('River Plate', '47'), ('Velez Sarsfield', '39'), ('Racing Club', '39'), ('Argentinos JRS', '39'), ('Defensa Y Justicia', '36'), ('Lanus', '36'), ('San Lorenzo', '36'), ('Rosario Central', '36'), ('Newells Old Boys', '35'), ('Arsenal Sarandi', '34'), ('Talleres Cordoba', '34'), ('Estudiantes L.P.', '30'), ('Independiente', '29'), ('Atletico Tucuman', '29'), ('Union Santa Fe', '27'), ('Banfield', '26'), ('Central Cordoba de Santiago', '26'), ('Gimnasia L.P.', '23'), ('Patronato', '23'), ('Huracan', '22'), ('Aldosivi', '22'), ('Colon Santa Fe', '18'), ('Godoy Cruz', '18')], 2020: {'Copa Liga Profesional - Winners Stage: Group A': [('Boca Juniors', '9'), ('River Plate', '8'), ('Argentinos JRS', '8'), ('Arsenal Sarandi', '7'), ('Independiente', '6'), ('Huracan', '3')], 'Copa Liga Profesional - Winners Stage: Group B': [('Banfield', '12'), ('Talleres Cordoba', '11'), ('Gimnasia L.P.', '7'), ('Colon Santa Fe', '4'), ('San Lorenzo', '4'), ('Atletico Tucuman', '4')], 'Copa Liga Profesional - Losers Stage: Group A': [('Rosario Central', '10'), ('Lanus', '8'), ('Defensa Y Justicia', '8'), ('Union Santa Fe', '7'), ('Aldosivi', '4'), ('Patronato', '4')], 'Copa Liga Profesional - Losers Stage: Group B': [('Velez Sarsfield', '12'), ('Newells Old Boys', '9'), ('Racing Club', '8'), ('Central Cordoba de Santiago', '5'), ('Estudiantes L.P.', '4'), ('Godoy Cruz', '4')], 'Copa Liga Profesional - First Stage: Group 1': [('Atletico Tucuman', '18'), ('Arsenal Sarandi', '7'), ('Union Santa Fe', '7'), ('Racing Club', '3')], 'Copa Liga Profesional - First Stage: Group 2': [('Colon Santa Fe', '13'), ('Independiente', '12'), ('Central Cordoba de Santiago', '5'), ('Defensa Y Justicia', '2')], 'Copa Liga Profesional - First Stage: Group 3': [('River Plate', '15'), ('Banfield', '11'), ('Rosario Central', '7'), ('Godoy Cruz', '1')], 'Copa Liga Profesional - First Stage: Group 4': [('Boca Juniors', '10'), ('Talleres Cordoba', '9'), ('Newells Old Boys', '7'), ('Lanus', '7')], 'Copa Liga Profesional - First Stage: Group 5': [('San Lorenzo', '12'), ('Argentinos JRS', '10'), ('Aldosivi', '8'), ('Estudiantes L.P.', '2')], 'Copa Liga Profesional - First Stage: Group 6': [('Huracan', '11'), ('Gimnasia L.P.', '9'), ('Velez Sarsfield', '9'), ('Patronato', '2')]}, 2021: {'Primera Fase': [('Colon Santa Fe', '25'), ('Estudiantes L.P.', '22'), ('River Plate', '21'), ('Racing Club', '21'), ('San Lorenzo', '21'), ('Banfield', '20'), ('Argentinos JRS', '19'), ('Rosario Central', '18'), ('Central Cordoba de Santiago', '17'), ('Godoy Cruz', '15'), ('Platense', '14'), ('Arsenal Sarandi', '12'), ('Aldosivi', '11')], 'Segunda Fase': [('River Plate', '54'), ('Defensa Y Justicia', '47'), ('Talleres Cordoba', '46'), ('Boca Juniors', '41'), ('Velez Sarsfield', '39'), ('Estudiantes L.P.', '39'), ('Colon Santa Fe', '39'), ('Huracan', '38'), ('Independiente', '38'), ('Lanus', '37'), ('Gimnasia L.P.', '36'), ('Union Santa Fe', '34'), ('Aldosivi', '33'), ('Argentinos JRS', '32'), ('Racing Club', '32'), ('Rosario Central', '32'), ('Godoy Cruz', '31'), ('Platense', '31'), ('Newells Old Boys', '28'), ('Banfield', '27'), ('San Lorenzo', '27'), ('Central Cordoba de Santiago', '26'), ('Patronato', '25'), ('Sarmiento Junin', '24'), ('Atletico Tucuman', '22'), ('Arsenal Sarandi', '21')]}, 2022: {'Primera Fase': [('Racing Club', '30'), ('River Plate', '29'), ('Defensa Y Justicia', '25'), ('Argentinos JRS', '25'), ('Gimnasia L.P.', '24'), ('Newells Old Boys', '23'), ('Sarmiento Junin', '21'), ('Banfield', '19'), ('Union Santa Fe', '17'), ('San Lorenzo', '15'), ('Atletico Tucuman', '11'), ('Talleres Cordoba', '11'), ('Platense', '10'), ('Patronato', '10')], 'Segunda Fase': [('Boca Juniors', '52'), ('Racing Club', '50'), ('River Plate', '47'), ('Huracan', '47'), ('Atletico Tucuman', '46'), ('San Lorenzo', '43'), ('Tigre', '43'), ('Argentinos JRS', '42'), ('Gimnasia L.P.', '41'), ('Patronato', '40'), ('Newells Old Boys', '40'), ('Defensa Y Justicia', '40'), ('Talleres Cordoba', '35'), ('Independiente', '35'), ('Godoy Cruz', '35'), ('Central Cordoba de Santiago', '34'), ('Barracas Central', '34'), ('Estudiantes L.P.', '33'), ('Platense', '32'), ('Rosario Central', '32'), ('Sarmiento Junin', '32'), ('Union Santa Fe', '32'), ('Arsenal Sarandi', '30'), ('Banfield', '30'), ('Colon Santa Fe', '29'), ('Velez Sarsfield', '28'), ('Lanus', '21'), ('Aldosivi', '16')]}, 2023: {'Primera Fase': [('River Plate', '47'), ('Talleres Cordoba', '40'), ('San Lorenzo', '37'), ('Estudiantes L.P.', '35'), ('Lanus', '34'), ('Rosario Central', '34'), ('Defensa Y Justicia', '33'), ('Belgrano Cordoba', '31'), ('Argentinos JRS', '29'), ('Godoy Cruz', '29'), ('Boca Juniors', '28'), ('Newells Old Boys', '28'), ('Platense', '26'), ('Racing Club', '26'), ('Sarmiento Junin', '25'), ('Gimnasia L.P.', '25'), ('Central Cordoba de Santiago', '24'), ('Colon Santa Fe', '23'), ('Barracas Central', '23'), ('Tigre', '22'), ('Instituto Cordoba', '22'), ('Independiente', '21'), ('Atletico Tucuman', '21'), ('Union Santa Fe', '20'), ('Velez Sarsfield', '18'), ('Huracan', '18'), ('Banfield', '18'), ('Arsenal Sarandi', '17')], 'Segunda Fase': [('Argentinos JRS', '0'), ('Arsenal Sarandi', '0'), ('Atletico Tucuman', '0'), ('Banfield', '0'), ('Barracas Central', '0'), ('Colon Santa Fe', '0'), ('Gimnasia L.P.', '0'), ('Huracan', '0'), ('Independiente', '0'), ('Instituto Cordoba', '0'), ('River Plate', '0'), ('Rosario Central', '0'), ('Talleres Cordoba', '0'), ('Velez Sarsfield', '0')]}}, {'Gimnasia L.P.': {'id': '434', 'a�o': '1887', 'escudo': 'https://media-2.api-sports.io/football/teams/434.png', 'estadio': 'Estadio Juan Carmelo Zerillo', 'direccion': 'Avenida 60 y 118', 'ciudad': 'La Plata, Provincia de Buenos Aires', 'capacidad': '24544', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/77.png', 'plantel': None, 'estadisticas': None}, 'River Plate': {'id': '435', 'a�o': '1901', 'escudo': 'https://media-2.api-sports.io/football/teams/435.png', 'estadio': 'Estadio M�s Monumental', 'direccion': 'Avenida Presidente Jos� Figueroa Alcorta 7597, N��ez', 'ciudad': 'Capital Federal, Ciudad de Buenos Aires', 'capacidad': '83214', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/19570.png', 'plantel': None, 'estadisticas': None}, 'Racing Club': {'id': '436', 'a�o': '1903', 'escudo': 'https://media-2.api-sports.io/football/teams/436.png', 'estadio': 'Estadio Presidente Juan Domingo Per�n', 'direccion': 'Calle Mozart y Orestes Omar Corbatta', 'ciudad': 'Avellaneda, Provincia de Buenos Aires', 'capacidad': '51500', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/99.png', 'plantel': None, 'estadisticas': None}, 'Rosario Central': {'id': '437', 'a�o': '1889', 'escudo': 'https://media-2.api-sports.io/football/teams/437.png', 'estadio': 'Estadio Gigante de Arroyito', 'direccion': 'Avenida G�nova y Avenida Centenario Rosario Central, Arroyito', 'ciudad': 'Rosario, Provincia de Santa Fe', 'capacidad': '41654', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/19391.png', 'plantel': None, 'estadisticas': None}, 'Velez Sarsfield': {'id': '438', 'a�o': '1910', 'escudo': 'https://media-2.api-sports.io/football/teams/438.png', 'estadio': 'Estadio Jos� Amalfitani', 'direccion': 'Avenida Juan B. Justo 9200, Liniers', 'ciudad': 'Capital Federal, Ciudad de Buenos Aires', 'capacidad': '49747', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/115.png', 'plantel': None, 'estadisticas': None}, 'Godoy Cruz': {'id': '439', 'a�o': '1921', 'escudo': 'https://media-1.api-sports.io/football/teams/439.png', 'estadio': 'Estadio Malvinas Argentinas', 'direccion': 'Calle San Francisco De Asis y Boulogne Sur Mer Mendoza', 'ciudad': 'Mendoza, Provincia de Mendoza', 'capacidad': '40268', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/80.png', 'plantel': None, 'estadisticas': None}, 'Belgrano Cordoba': {'id': '440', 'a�o': '1905', 'escudo': 'https://media-3.api-sports.io/football/teams/440.png', 'estadio': 'Estadio Julio C�sar Villagra', 'direccion': 'Calle Dr. Arturo Orgaz 510 y La Rioja, Barrio Alberdi', 'ciudad': 'Ciudad de C�rdoba, Provincia de C�rdoba', 'capacidad': '28000', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/45.png', 'plantel': None, 'estadisticas': None}, 'Union Santa Fe': {'id': '441', 'a�o': '1907', 'escudo': 'https://media-3.api-sports.io/football/teams/441.png', 'estadio': 'Estadio 15 de Abril', 'direccion': 'Bulevar Pellegrini y Avenida Vicente L�pez y Planes 3513', 'ciudad': 'Ciudad de Santa Fe, Provincia de Santa Fe', 'capacidad': '27000', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/1933.png', 'plantel': None, 'estadisticas': None}, 'Defensa Y Justicia': {'id': '442', 'a�o': '1935', 'escudo': 'https://media-2.api-sports.io/football/teams/442.png', 'estadio': 'Estadio Norberto Tito Tomaghello', 'direccion': 'Avenida Humahuaca y Calle 611', 'ciudad': 'Florencio Varela, Provincia de Buenos Aires', 'capacidad': '20000', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/59.png', 'plantel': None, 'estadisticas': None}, 'Olimpo Bahia Blanca': {'id': '443', 'a�o': '1910', 'escudo': 'https://media-2.api-sports.io/football/teams/443.png', 'estadio': 'Estadio Roberto Natalio Carminatti', 'direccion': 'Avenida Col�n y Calle Angel Brunel', 'ciudad': 'Bah�a Blanca, Provincia de Buenos Aires', 'capacidad': '15000', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/95.png', 'plantel': None, 'estadisticas': None}, 'Patronato': {'id': '444', 'a�o': '1914', 'escudo': 'https://media-2.api-sports.io/football/teams/444.png', 'estadio': 'Estadio Presb�tero Bartolom� Grella', 'direccion': 'Calle Ayacucho y Calle Churruar�n', 'ciudad': 'Paran�, Provincia de Entre R�os', 'capacidad': '22000', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/96.png', 'plantel': None, 'estadisticas': None}, 'Huracan': {'id': '445', 'a�o': '1908', 'escudo': 'https://media-3.api-sports.io/football/teams/445.png', 'estadio': 'Estadio Tom�s Adolfo Duc�', 'direccion': 'Avenida Amancio Alcorta 2570, Parque Patricios', 'ciudad': 'Capital Federal, Ciudad de Buenos Aires', 'capacidad': '48314', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/82.png', 'plantel': None, 'estadisticas': None}, 'Lanus': {'id': '446', 'a�o': '1915', 'escudo': 'https://media-1.api-sports.io/football/teams/446.png', 'estadio': 'Estadio Ciudad de Lan�s - N�stor D�az P�rez', 'direccion': 'Calle General J. Arias y J. H�ctor Guidi', 'ciudad': 'Lan�s, Provincia de Buenos Aires', 'capacidad': '46619', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/88.png', 'plantel': None, 'estadisticas': None}, 'Colon Santa Fe': {'id': '448', 'a�o': '1905', 'escudo': 'https://media-3.api-sports.io/football/teams/448.png', 'estadio': 'Estadio Brigadier General Estanislao L�pez', 'direccion': 'Calle Juan Jos� Paso y Boulevard Doctor Zavalla', 'ciudad': 'Ciudad de Santa Fe, Provincia de Santa Fe', 'capacidad': '40000', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/57.png', 'plantel': None, 'estadisticas': None}, 'Banfield': {'id': '449', 'a�o': '1896', 'escudo': 'https://media-2.api-sports.io/football/teams/449.png', 'estadio': 'Estadio Florencio Sol�', 'direccion': 'Calle General Arenales y Pe�a', 'ciudad': 'Lomas de Zamora, Provincia de Buenos Aires', 'capacidad': '34901', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/43.png', 'plantel': None, 'estadisticas': None}, 'Estudiantes L.P.': {'id': '450', 'a�o': '1905', 'escudo': 'https://media-3.api-sports.io/football/teams/450.png', 'estadio': 'Estadio �nico Diego Armando Maradona', 'direccion': 'Avenida 25 y 32', 'ciudad': 'La Plata, Provincia de Buenos Aires', 'capacidad': '53000', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/12716.png', 'plantel': None, 'estadisticas': None}, 'Boca Juniors': {'id': '451', 'a�o': '1905', 'escudo': 'https://media-3.api-sports.io/football/teams/451.png', 'estadio': 'Estadio Alberto Jos� Armando', 'direccion': 'Brandsen 805, La Boca', 'ciudad': 'Ciudad de Buenos Aires', 'capacidad': '49000', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/46.png', 'plantel': None, 'estadisticas': None}, 'Tigre': {'id': '452', 'a�o': '1902', 'escudo': 'https://media-3.api-sports.io/football/teams/452.png', 'estadio': 'Estadio Jos� Dellagiovanna', 'direccion': 'Avenida Presidente Per�n 2650 esq. Guido Spano 1053, Victoria', 'ciudad': 'San Fernando, Provincia de Buenos Aires', 'capacidad': '26282', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/112.png', 'plantel': None, 'estadisticas': None}, 'Independiente': {'id': '453', 'a�o': '1905', 'escudo': 'https://media-1.api-sports.io/football/teams/453.png', 'estadio': 'Estadio Libertadores de Am�rica', 'direccion': 'Calle Ricardo Enrique Bochini 751/83 esq. Alsina', 'ciudad': 'Avellaneda, Provincia de Buenos Aires', 'capacidad': '52364', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/7131.png', 'plantel': None, 'estadisticas': None}, 'Temperley': {'id': '454', 'a�o': '1912', 'escudo': 'https://media-2.api-sports.io/football/teams/454.png', 'estadio': 'Estadio Alfredo Mart�n Beranger', 'direccion': 'Avenida 9 de Julio 360 (entre Coronel Dorrego y Coronel Brandsen)', 'ciudad': 'Temperley, Provincia de Buenos Aires', 'capacidad': '19500', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/111.png', 'plantel': None, 'estadisticas': None}, 'Atletico Tucuman': {'id': '455', 'a�o': '1902', 'escudo': 'https://media-2.api-sports.io/football/teams/455.png', 'estadio': 'Estadio Monumental Presidente Jos� Fierro', 'direccion': '25 de Mayo 1351 y Rep�blica de Chile, Barrio Norte', 'ciudad': 'San Miguel de Tucum�n, Provincia de Tucum�n', 'capacidad': '35200', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/42.png', 'plantel': None, 'estadisticas': None}, 'Talleres Cordoba': {'id': '456', 'a�o': '1913', 'escudo': 'https://media-1.api-sports.io/football/teams/456.png', 'estadio': 'Estadio Mario Alberto Kempes', 'direccion': 'Avenida C�rcano, Chateau Carreras', 'ciudad': 'Ciudad de C�rdoba, Provincia de C�rdoba', 'capacidad': '57503', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/110.png', 'plantel': None, 'estadisticas': None}, 'Newells Old Boys': {'id': '457', 'a�o': '1903', 'escudo': 'https://media-2.api-sports.io/football/teams/457.png', 'estadio': 'Estadio Marcelo Alberto Bielsa', 'direccion': 'Parque de la Independencia, Barrio Centro', 'ciudad': 'Rosario, Provincia de Santa Fe', 'capacidad': '42000', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/93.png', 'plantel': None, 'estadisticas': None}, 'Arsenal Sarandi': {'id': '459', 'a�o': '1957', 'escudo': 'https://media-2.api-sports.io/football/teams/459.png', 'estadio': 'Estadio Julio Humberto Grondona', 'direccion': 'Avenida Juan D�az de Sol�s 3660, Sarand�', 'ciudad': 'Avellaneda, Provincia de Buenos Aires', 'capacidad': '18300', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/38.png', 'plantel': None, 'estadisticas': None}, 'San Lorenzo': {'id': '460', 'a�o': '1908', 'escudo': 'https://media-1.api-sports.io/football/teams/460.png', 'estadio': 'Estadio Pedro Bidega�n', 'direccion': 'Avenida Perito Moreno y Avenida Varela 1437', 'ciudad': 'Capital Federal, Ciudad de Buenos Aires', 'capacidad': '43494', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/103.png', 'plantel': None, 'estadisticas': None}, 'San Martin S.J.': {'id': '461', 'a�o': '1907', 'escudo': 'https://media-2.api-sports.io/football/teams/461.png', 'estadio': 'Estadio Ingeniero Hilario S�nchez', 'direccion': 'Calle Mendoza 1164 Norte', 'ciudad': 'San Juan, Provincia de San Juan', 'capacidad': '19000', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/104.png', 'plantel': None, 'estadisticas': None}, 'Aldosivi': {'id': '463', 'a�o': '1913', 'escudo': 'https://media-3.api-sports.io/football/teams/463.png', 'estadio': 'Estadio Jos� Mar�a Minella', 'direccion': 'Avenida de las Olimpiadas y Ort�z de Z�rate', 'ciudad': 'Mar del Plata, Provincia de Buenos Aires', 'capacidad': '35354', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/33.png', 'plantel': None, 'estadisticas': None}, 'Atletico DE Rafaela': {'id': '465', 'a�o': '1907', 'escudo': 'https://media-2.api-sports.io/football/teams/465.png', 'estadio': 'Estadio Nuevo Monumental', 'direccion': 'Calle Urquiza y Primera Junta, Barrio Alberdi', 'ciudad': 'Rafaela, Provincia de Santa Fe', 'capacidad': '16000', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/41.png', 'plantel': None, 'estadisticas': None}, 'Sarmiento Junin': {'id': '474', 'a�o': '1911', 'escudo': 'https://media-1.api-sports.io/football/teams/474.png', 'estadio': 'Estadio Eva Per�n de Jun�n', 'direccion': 'Calle Arias y  Necochea 25', 'ciudad': 'Jun�n, Provincia de Buenos Aires', 'capacidad': '22000', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/107.png', 'plantel': None, 'estadisticas': None}, 'Quilmes': {'id': '480', 'a�o': '1887', 'escudo': 'https://media-1.api-sports.io/football/teams/480.png', 'estadio': 'Estadio Centenario Dr. Jos� Luis Meiszner', 'direccion': 'Avenida Vicente L�pez y Esqui�, Barrio Libertador General San Mart�n', 'ciudad': 'Quilmes, Provincia de Buenos Aires', 'capacidad': '30200', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/98.png', 'plantel': None, 'estadisticas': None}, 'Chacarita Juniors': {'id': '447', 'a�o': '1906', 'escudo': 'https://media-3.api-sports.io/football/teams/447.png', 'estadio': 'Estadio de Chacarita Juniors', 'direccion': 'Calle Gutierrez 351, Villa Maip�', 'ciudad': 'General San Mart�n, Provincia de Buenos Aires', 'capacidad': '24300', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/54.png', 'plantel': None, 'estadisticas': None}, 'Argentinos JRS': {'id': '458', 'a�o': '1904', 'escudo': 'https://media-2.api-sports.io/football/teams/458.png', 'estadio': 'Estadio Diego Armando Maradona', 'direccion': 'Calle Gavil�n 2151 y Juan Agust�n Garc�a, La Paternal', 'ciudad': 'Capital Federal, Ciudad de Buenos Aires', 'capacidad': '24380', 'superficie': 'grass', 'foto': 'https://media-1.api-sports.io/football/venues/37.png', 'plantel': None, 'estadisticas': None}, 'San Martin Tucuman': {'id': '485', 'a�o': '1909', 'escudo': 'https://media-2.api-sports.io/football/teams/485.png', 'estadio': 'Estadio La Ciudadela', 'direccion': 'Calle Beccer y Avenida Pellegrini', 'ciudad': 'San Miguel de Tucum�n, Provincia de Tucum�n', 'capacidad': '27000', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/105.png', 'plantel': None, 'estadisticas': None}, 'Central Cordoba de Santiago': {'id': '1065', 'a�o': '1919', 'escudo': 'https://media-3.api-sports.io/football/teams/1065.png', 'estadio': 'Estadio Alfredo Terrera', 'direccion': 'Calle Granadero Saavedra', 'ciudad': 'Santiago del Estero, Provincia de Santiago del Est', 'capacidad': '16000', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/2997.png', 'plantel': None, 'estadisticas': None}, 'Platense': {'id': '1064', 'a�o': '1905', 'escudo': 'https://media-3.api-sports.io/football/teams/1064.png', 'estadio': 'Estadio Ciudad de Vicente L�pez', 'direccion': 'Calle Juan Zufriategui 2021 (Avenida General Paz), Florida', 'ciudad': 'Vicente L�pez, Provincia de Buenos Aires', 'capacidad': '31030', 'superficie': 'grass', 'foto': 'https://media-2.api-sports.io/football/venues/97.png', 'plantel': None, 'estadisticas': None}, 'Barracas Central': {'id': '2432', 'a�o': '1904', 'escudo': 'https://media-3.api-sports.io/football/teams/2432.png', 'estadio': 'Estadio Claudio Fabi�n Tapia', 'direccion': 'Avenida Olavar�a 3400 y Luna, Bairro Barracas', 'ciudad': 'Capital Federal, Ciudad de Buenos Aires', 'capacidad': '4400', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/44.png', 'plantel': None, 'estadisticas': None}, 'Instituto Cordoba': {'id': '478', 'a�o': '1918', 'escudo': 'https://media-1.api-sports.io/football/teams/478.png', 'estadio': 'Estadio Juan Domingo Per�n', 'direccion': 'Calle Jujuy 2602 y Lope de Vega, Alta C�rdoba', 'ciudad': 'Ciudad de C�rdoba, Provincia de C�rdoba', 'capacidad': '26535', 'superficie': 'grass', 'foto': 'https://media-3.api-sports.io/football/venues/84.png', 'plantel': ['Jonathan Dellarossa (midfielder)', 'Jorge Carlos Carranza (goalkeeper)', 'Emanuel Bilbao (goalkeeper)', 'Manuel Roffo (goalkeeper)', 'Sebasti�n Corda (defender)', 'Giuliano Cerato (defender)', 'Fernando Rub�n Alarc�n (defender)', 'An�bal Jonathan Gast�n Bay (defender)', 'Oscar Ezequiel Jonathan Parnisari (defender)', 'Julio Leonel Mosevich (defender)', 'Gonzalo Requena (defender)', 'Joaqu�n Varela Moreno (defender)', 'Juan Jos� Franco Arrellaga (midfielder)', 'Roberto Agust�n Bochi (midfielder)', 'Gregorio Rodr�guez (midfielder)', 'Gabriel Maximiliano Graciani (midfielder)', 'Franco Nahuel Watson (midfielder)', 'Nicol�s Hugo Linares (midfielder)', 'Leonardo Monje (midfielder)', 'Gast�n Andr�s Lodico (midfielder)'], 'estadisticas': {'0-15': 1, '16-30': 3, '31-45': 6, '46-60': 2, '61-75': 2, '76-90': 0, '91-105': 2, '106-120': 0}}}, {'971182': {'fecha': ('2023', '08', '20'), 'local': 'Velez Sarsfield', 'visitante': 'Barracas Central'}, '971183': {'fecha': ('2023', '08', '20'), 'local': 'Argentinos JRS', 'visitante': 'River Plate'}, '971184': {'fecha': ('2023', '08', '20'), 'local': 'Rosario Central', 'visitante': 'Atletico Tucuman'}, '971185': {'fecha': ('2023', '08', '20'), 'local': 'Huracan', 'visitante': 'Banfield'}, '971186': {'fecha': ('2023', '08', '20'), 'local': 'Gimnasia L.P.', 'visitante': 'Talleres Cordoba'}, '971187': {'fecha': ('2023', '08', '20'), 'local': 'Independiente', 'visitante': 'Colon Santa Fe'}, '971188': {'fecha': ('2023', '08', '20'), 'local': 'Boca Juniors', 'visitante': 'Platense'}, '971189': {'fecha': ('2023', '08', '20'), 'local': 'Defensa Y Justicia', 'visitante': 'Godoy Cruz'}, '971190': {'fecha': ('2023', '08', '20'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Newells Old Boys'}, '971191': {'fecha': ('2023', '08', '20'), 'local': 'Lanus', 'visitante': 'San Lorenzo'}, '971192': {'fecha': ('2023', '08', '20'), 'local': 'Belgrano Cordoba', 'visitante': 'Estudiantes L.P.'}, '971193': {'fecha': ('2023', '08', '20'), 'local': 'Union Santa Fe', 'visitante': 'Racing Club'}, '971194': {'fecha': ('2023', '08', '27'), 'local': 'Independiente', 'visitante': 'Velez Sarsfield'}, '971195': {'fecha': ('2023', '08', '27'), 'local': 'Colon Santa Fe', 'visitante': 'Gimnasia L.P.'}, '971196': {'fecha': ('2023', '08', '27'), 'local': 'Talleres Cordoba', 'visitante': 'Huracan'}, '971197': {'fecha': ('2023', '08', '27'), 'local': 'Banfield', 'visitante': 'Rosario Central'}, '971198': {'fecha': ('2023', '08', '27'), 'local': 'Arsenal Sarandi', 'visitante': 'Argentinos JRS'}, '971199': {'fecha': ('2023', '08', '27'), 'local': 'River Plate', 'visitante': 'Barracas Central'}, '971200': {'fecha': ('2023', '08', '27'), 'local': 'Tigre', 'visitante': 'Racing Club'}, '971201': {'fecha': ('2023', '08', '27'), 'local': 'Estudiantes L.P.', 'visitante': 'Union Santa Fe'}, '971202': {'fecha': ('2023', '08', '27'), 'local': 'San Lorenzo', 'visitante': 'Belgrano Cordoba'}, '971203': {'fecha': ('2023', '08', '27'), 'local': 'Newells Old Boys', 'visitante': 'Lanus'}, '971204': {'fecha': ('2023', '08', '27'), 'local': 'Godoy Cruz', 'visitante': 'Central Cordoba de Santiago'}, '971205': {'fecha': ('2023', '08', '27'), 'local': 'Platense', 'visitante': 'Defensa Y Justicia'}, '971206': {'fecha': ('2023', '09', '03'), 'local': 'Velez Sarsfield', 'visitante': 'River Plate'}, '971207': {'fecha': ('2023', '09', '03'), 'local': 'Barracas Central', 'visitante': 'Arsenal Sarandi'}, '971208': {'fecha': ('2023', '09', '03'), 'local': 'Argentinos JRS', 'visitante': 'Atletico Tucuman'}, '971209': {'fecha': ('2023', '09', '03'), 'local': 'Rosario Central', 'visitante': 'Talleres Cordoba'}, '971210': {'fecha': ('2023', '09', '03'), 'local': 'Huracan', 'visitante': 'Colon Santa Fe'}, '971211': {'fecha': ('2023', '09', '03'), 'local': 'Gimnasia L.P.', 'visitante': 'Independiente'}, '971212': {'fecha': ('2023', '09', '03'), 'local': 'Boca Juniors', 'visitante': 'Tigre'}, '971213': {'fecha': ('2023', '09', '03'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Platense'}, '971214': {'fecha': ('2023', '09', '03'), 'local': 'Lanus', 'visitante': 'Godoy Cruz'}, '971215': {'fecha': ('2023', '09', '03'), 'local': 'Belgrano Cordoba', 'visitante': 'Newells Old Boys'}, '971216': {'fecha': ('2023', '09', '03'), 'local': 'Union Santa Fe', 'visitante': 'San Lorenzo'}, '971217': {'fecha': ('2023', '09', '03'), 'local': 'Racing Club', 'visitante': 'Estudiantes L.P.'}, '971218': {'fecha': ('2023', '09', '10'), 'local': 'Gimnasia L.P.', 'visitante': 'Velez Sarsfield'}, '971219': {'fecha': ('2023', '09', '10'), 'local': 'Independiente', 'visitante': 'Huracan'}, '971220': {'fecha': ('2023', '09', '10'), 'local': 'Colon Santa Fe', 'visitante': 'Rosario Central'}, '971221': {'fecha': ('2023', '09', '10'), 'local': 'Banfield', 'visitante': 'Argentinos JRS'}, '971222': {'fecha': ('2023', '09', '10'), 'local': 'Atletico Tucuman', 'visitante': 'Barracas Central'}, '971223': {'fecha': ('2023', '09', '10'), 'local': 'Arsenal Sarandi', 'visitante': 'River Plate'}, '971224': {'fecha': ('2023', '09', '10'), 'local': 'Tigre', 'visitante': 'Estudiantes L.P.'}, '971225': {'fecha': ('2023', '09', '10'), 'local': 'San Lorenzo', 'visitante': 'Racing Club'}, '971226': {'fecha': ('2023', '09', '10'), 'local': 'Newells Old Boys', 'visitante': 'Union Santa Fe'}, '971227': {'fecha': ('2023', '09', '10'), 'local': 'Godoy Cruz', 'visitante': 'Belgrano Cordoba'}, '971228': {'fecha': ('2023', '09', '10'), 'local': 'Platense', 'visitante': 'Lanus'}, '971229': {'fecha': ('2023', '09', '10'), 'local': 'Boca Juniors', 'visitante': 'Defensa Y Justicia'}, '971230': {'fecha': ('2023', '09', '17'), 'local': 'Velez Sarsfield', 'visitante': 'Arsenal Sarandi'}, '971231': {'fecha': ('2023', '09', '17'), 'local': 'River Plate', 'visitante': 'Atletico Tucuman'}, '971232': {'fecha': ('2023', '09', '17'), 'local': 'Barracas Central', 'visitante': 'Banfield'}, '971233': {'fecha': ('2023', '09', '17'), 'local': 'Argentinos JRS', 'visitante': 'Talleres Cordoba'}, '971234': {'fecha': ('2023', '09', '17'), 'local': 'Rosario Central', 'visitante': 'Independiente'}, '971235': {'fecha': ('2023', '09', '17'), 'local': 'Huracan', 'visitante': 'Gimnasia L.P.'}, '971236': {'fecha': ('2023', '09', '17'), 'local': 'Defensa Y Justicia', 'visitante': 'Tigre'}, '971237': {'fecha': ('2023', '09', '17'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Boca Juniors'}, '971238': {'fecha': ('2023', '09', '17'), 'local': 'Belgrano Cordoba', 'visitante': 'Platense'}, '971239': {'fecha': ('2023', '09', '17'), 'local': 'Union Santa Fe', 'visitante': 'Godoy Cruz'}, '971240': {'fecha': ('2023', '09', '17'), 'local': 'Racing Club', 'visitante': 'Newells Old Boys'}, '971241': {'fecha': ('2023', '09', '17'), 'local': 'Estudiantes L.P.', 'visitante': 'San Lorenzo'}, '971242': {'fecha': ('2023', '09', '24'), 'local': 'Huracan', 'visitante': 'Velez Sarsfield'}, '971243': {'fecha': ('2023', '09', '24'), 'local': 'Gimnasia L.P.', 'visitante': 'Rosario Central'}, '971244': {'fecha': ('2023', '09', '24'), 'local': 'Colon Santa Fe', 'visitante': 'Argentinos JRS'}, '971245': {'fecha': ('2023', '09', '24'), 'local': 'Talleres Cordoba', 'visitante': 'Barracas Central'}, '971246': {'fecha': ('2023', '09', '24'), 'local': 'Banfield', 'visitante': 'River Plate'}, '971247': {'fecha': ('2023', '09', '24'), 'local': 'Atletico Tucuman', 'visitante': 'Arsenal Sarandi'}, '971248': {'fecha': ('2023', '09', '24'), 'local': 'Tigre', 'visitante': 'San Lorenzo'}, '971249': {'fecha': ('2023', '09', '24'), 'local': 'Newells Old Boys', 'visitante': 'Estudiantes L.P.'}, '971250': {'fecha': ('2023', '09', '24'), 'local': 'Godoy Cruz', 'visitante': 'Racing Club'}, '971251': {'fecha': ('2023', '09', '24'), 'local': 'Platense', 'visitante': 'Union Santa Fe'}, '971252': {'fecha': ('2023', '09', '24'), 'local': 'Boca Juniors', 'visitante': 'Lanus'}, '971253': {'fecha': ('2023', '09', '24'), 'local': 'Defensa Y Justicia', 'visitante': 'Central Cordoba de Santiago'}, '971254': {'fecha': ('2023', '10', '01'), 'local': 'Colon Santa Fe', 'visitante': 'Union Santa Fe'}, '971255': {'fecha': ('2023', '10', '01'), 'local': 'San Lorenzo', 'visitante': 'Huracan'}, '971256': {'fecha': ('2023', '10', '01'), 'local': 'Estudiantes L.P.', 'visitante': 'Gimnasia L.P.'}, '971257': {'fecha': ('2023', '10', '01'), 'local': 'Rosario Central', 'visitante': 'Newells Old Boys'}, '971258': {'fecha': ('2023', '10', '01'), 'local': 'Racing Club', 'visitante': 'Independiente'}, '971259': {'fecha': ('2023', '10', '01'), 'local': 'Boca Juniors', 'visitante': 'River Plate'}, '971260': {'fecha': ('2023', '10', '01'), 'local': 'Talleres Cordoba', 'visitante': 'Belgrano Cordoba'}, '971261': {'fecha': ('2023', '10', '01'), 'local': 'Platense', 'visitante': 'Argentinos JRS'}, '971262': {'fecha': ('2023', '10', '01'), 'local': 'Velez Sarsfield', 'visitante': 'Tigre'}, '971263': {'fecha': ('2023', '10', '01'), 'local': 'Defensa Y Justicia', 'visitante': 'Arsenal Sarandi'}, '971264': {'fecha': ('2023', '10', '01'), 'local': 'Banfield', 'visitante': 'Lanus'}, '971265': {'fecha': ('2023', '10', '01'), 'local': 'Atletico Tucuman', 'visitante': 'Central Cordoba de Santiago'}, '971266': {'fecha': ('2023', '10', '08'), 'local': 'Velez Sarsfield', 'visitante': 'Atletico Tucuman'}, '971267': {'fecha': ('2023', '10', '08'), 'local': 'Arsenal Sarandi', 'visitante': 'Banfield'}, '971268': {'fecha': ('2023', '10', '08'), 'local': 'River Plate', 'visitante': 'Talleres Cordoba'}, '971269': {'fecha': ('2023', '10', '08'), 'local': 'Barracas Central', 'visitante': 'Colon Santa Fe'}, '971270': {'fecha': ('2023', '10', '08'), 'local': 'Argentinos JRS', 'visitante': 'Independiente'}, '971271': {'fecha': ('2023', '10', '08'), 'local': 'Rosario Central', 'visitante': 'Huracan'}, '971272': {'fecha': ('2023', '10', '08'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Tigre'}, '971273': {'fecha': ('2023', '10', '08'), 'local': 'Lanus', 'visitante': 'Defensa Y Justicia'}, '971274': {'fecha': ('2023', '10', '08'), 'local': 'Belgrano Cordoba', 'visitante': 'Boca Juniors'}, '971275': {'fecha': ('2023', '10', '08'), 'local': 'Racing Club', 'visitante': 'Platense'}, '971276': {'fecha': ('2023', '10', '08'), 'local': 'Estudiantes L.P.', 'visitante': 'Godoy Cruz'}, '971277': {'fecha': ('2023', '10', '08'), 'local': 'San Lorenzo', 'visitante': 'Newells Old Boys'}, '971278': {'fecha': ('2023', '10', '15'), 'local': 'Rosario Central', 'visitante': 'Velez Sarsfield'}, '971279': {'fecha': ('2023', '10', '15'), 'local': 'Gimnasia L.P.', 'visitante': 'Argentinos JRS'}, '971280': {'fecha': ('2023', '10', '15'), 'local': 'Independiente', 'visitante': 'Barracas Central'}, '971281': {'fecha': ('2023', '10', '15'), 'local': 'Colon Santa Fe', 'visitante': 'River Plate'}, '971282': {'fecha': ('2023', '10', '15'), 'local': 'Talleres Cordoba', 'visitante': 'Arsenal Sarandi'}, '971283': {'fecha': ('2023', '10', '15'), 'local': 'Banfield', 'visitante': 'Atletico Tucuman'}, '971284': {'fecha': ('2023', '10', '15'), 'local': 'Tigre', 'visitante': 'Newells Old Boys'}, '971285': {'fecha': ('2023', '10', '15'), 'local': 'Godoy Cruz', 'visitante': 'San Lorenzo'}, '971286': {'fecha': ('2023', '10', '15'), 'local': 'Platense', 'visitante': 'Estudiantes L.P.'}, '971287': {'fecha': ('2023', '10', '15'), 'local': 'Boca Juniors', 'visitante': 'Union Santa Fe'}, '971288': {'fecha': ('2023', '10', '15'), 'local': 'Defensa Y Justicia', 'visitante': 'Belgrano Cordoba'}, '971289': {'fecha': ('2023', '10', '15'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Lanus'}, '971290': {'fecha': ('2023', '10', '22'), 'local': 'Velez Sarsfield', 'visitante': 'Banfield'}, '971291': {'fecha': ('2023', '10', '22'), 'local': 'Atletico Tucuman', 'visitante': 'Talleres Cordoba'}, '971292': {'fecha': ('2023', '10', '22'), 'local': 'Arsenal Sarandi', 'visitante': 'Colon Santa Fe'}, '971293': {'fecha': ('2023', '10', '22'), 'local': 'River Plate', 'visitante': 'Independiente'}, '971294': {'fecha': ('2023', '10', '22'), 'local': 'Barracas Central', 'visitante': 'Gimnasia L.P.'}, '971295': {'fecha': ('2023', '10', '22'), 'local': 'Argentinos JRS', 'visitante': 'Huracan'}, '971296': {'fecha': ('2023', '10', '22'), 'local': 'Lanus', 'visitante': 'Tigre'}, '971297': {'fecha': ('2023', '10', '22'), 'local': 'Belgrano Cordoba', 'visitante': 'Central Cordoba de Santiago'}, '971298': {'fecha': ('2023', '10', '22'), 'local': 'Union Santa Fe', 'visitante': 'Defensa Y Justicia'}, '971299': {'fecha': ('2023', '10', '22'), 'local': 'Racing Club', 'visitante': 'Boca Juniors'}, '971300': {'fecha': ('2023', '10', '22'), 'local': 'San Lorenzo', 'visitante': 'Platense'}, '971301': {'fecha': ('2023', '10', '22'), 'local': 'Newells Old Boys', 'visitante': 'Godoy Cruz'}, '971302': {'fecha': ('2023', '10', '29'), 'local': 'Rosario Central', 'visitante': 'Argentinos JRS'}, '971303': {'fecha': ('2023', '10', '29'), 'local': 'Huracan', 'visitante': 'Barracas Central'}, '971304': {'fecha': ('2023', '10', '29'), 'local': 'Gimnasia L.P.', 'visitante': 'River Plate'}, '971305': {'fecha': ('2023', '10', '29'), 'local': 'Independiente', 'visitante': 'Arsenal Sarandi'}, '971306': {'fecha': ('2023', '10', '29'), 'local': 'Colon Santa Fe', 'visitante': 'Atletico Tucuman'}, '971307': {'fecha': ('2023', '10', '29'), 'local': 'Talleres Cordoba', 'visitante': 'Banfield'}, '971308': {'fecha': ('2023', '10', '29'), 'local': 'Tigre', 'visitante': 'Godoy Cruz'}, '971309': {'fecha': ('2023', '10', '29'), 'local': 'Platense', 'visitante': 'Newells Old Boys'}, '971310': {'fecha': ('2023', '10', '29'), 'local': 'Boca Juniors', 'visitante': 'Estudiantes L.P.'}, '971311': {'fecha': ('2023', '10', '29'), 'local': 'Defensa Y Justicia', 'visitante': 'Racing Club'}, '971312': {'fecha': ('2023', '10', '29'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Union Santa Fe'}, '971313': {'fecha': ('2023', '10', '29'), 'local': 'Lanus', 'visitante': 'Belgrano Cordoba'}, '971314': {'fecha': ('2023', '11', '05'), 'local': 'Velez Sarsfield', 'visitante': 'Talleres Cordoba'}, '971315': {'fecha': ('2023', '11', '05'), 'local': 'Banfield', 'visitante': 'Colon Santa Fe'}, '971316': {'fecha': ('2023', '11', '05'), 'local': 'Atletico Tucuman', 'visitante': 'Independiente'}, '971317': {'fecha': ('2023', '11', '05'), 'local': 'Arsenal Sarandi', 'visitante': 'Gimnasia L.P.'}, '971318': {'fecha': ('2023', '11', '05'), 'local': 'River Plate', 'visitante': 'Huracan'}, '971319': {'fecha': ('2023', '11', '05'), 'local': 'Barracas Central', 'visitante': 'Rosario Central'}, '971320': {'fecha': ('2023', '11', '05'), 'local': 'Belgrano Cordoba', 'visitante': 'Tigre'}, '971321': {'fecha': ('2023', '11', '05'), 'local': 'Union Santa Fe', 'visitante': 'Lanus'}, '971322': {'fecha': ('2023', '11', '05'), 'local': 'Racing Club', 'visitante': 'Central Cordoba de Santiago'}, '971323': {'fecha': ('2023', '11', '05'), 'local': 'Estudiantes L.P.', 'visitante': 'Defensa Y Justicia'}, '971324': {'fecha': ('2023', '11', '05'), 'local': 'San Lorenzo', 'visitante': 'Boca Juniors'}, '971325': {'fecha': ('2023', '11', '05'), 'local': 'Godoy Cruz', 'visitante': 'Platense'}, '971326': {'fecha': ('2023', '11', '12'), 'local': 'Argentinos JRS', 'visitante': 'Velez Sarsfield'}, '971327': {'fecha': ('2023', '11', '12'), 'local': 'Rosario Central', 'visitante': 'River Plate'}, '971328': {'fecha': ('2023', '11', '12'), 'local': 'Huracan', 'visitante': 'Arsenal Sarandi'}, '971329': {'fecha': ('2023', '11', '12'), 'local': 'Gimnasia L.P.', 'visitante': 'Atletico Tucuman'}, '971330': {'fecha': ('2023', '11', '12'), 'local': 'Independiente', 'visitante': 'Banfield'}, '971331': {'fecha': ('2023', '11', '12'), 'local': 'Colon Santa Fe', 'visitante': 'Talleres Cordoba'}, '971332': {'fecha': ('2023', '11', '12'), 'local': 'Tigre', 'visitante': 'Platense'}, '971333': {'fecha': ('2023', '11', '12'), 'local': 'Boca Juniors', 'visitante': 'Newells Old Boys'}, '971334': {'fecha': ('2023', '11', '12'), 'local': 'Defensa Y Justicia', 'visitante': 'San Lorenzo'}, '971335': {'fecha': ('2023', '11', '12'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Estudiantes L.P.'}, '971336': {'fecha': ('2023', '11', '12'), 'local': 'Lanus', 'visitante': 'Racing Club'}, '971337': {'fecha': ('2023', '11', '12'), 'local': 'Belgrano Cordoba', 'visitante': 'Union Santa Fe'}, '971338': {'fecha': ('2023', '11', '19'), 'local': 'Velez Sarsfield', 'visitante': 'Colon Santa Fe'}, '971339': {'fecha': ('2023', '11', '19'), 'local': 'Talleres Cordoba', 'visitante': 'Independiente'}, '971340': {'fecha': ('2023', '11', '19'), 'local': 'Banfield', 'visitante': 'Gimnasia L.P.'}, '971341': {'fecha': ('2023', '11', '19'), 'local': 'Atletico Tucuman', 'visitante': 'Huracan'}, '971342': {'fecha': ('2023', '11', '19'), 'local': 'Arsenal Sarandi', 'visitante': 'Rosario Central'}, '971343': {'fecha': ('2023', '11', '19'), 'local': 'Barracas Central', 'visitante': 'Argentinos JRS'}, '971344': {'fecha': ('2023', '11', '19'), 'local': 'Union Santa Fe', 'visitante': 'Tigre'}, '971345': {'fecha': ('2023', '11', '19'), 'local': 'Racing Club', 'visitante': 'Belgrano Cordoba'}, '971346': {'fecha': ('2023', '11', '19'), 'local': 'Estudiantes L.P.', 'visitante': 'Lanus'}, '971347': {'fecha': ('2023', '11', '19'), 'local': 'San Lorenzo', 'visitante': 'Central Cordoba de Santiago'}, '971348': {'fecha': ('2023', '11', '19'), 'local': 'Newells Old Boys', 'visitante': 'Defensa Y Justicia'}, '971349': {'fecha': ('2023', '11', '19'), 'local': 'Godoy Cruz', 'visitante': 'Boca Juniors'}, '971591': {'fecha': ('2023', '06', '22'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Gimnasia L.P.'}, '971592': {'fecha': ('2023', '06', '23'), 'local': 'Huracan', 'visitante': 'Newells Old Boys'}, '971593': {'fecha': ('2023', '06', '24'), 'local': 'Union Santa Fe', 'visitante': 'Independiente'}, '971594': {'fecha': ('2023', '06', '23'), 'local': 'Godoy Cruz', 'visitante': 'Boca Juniors'}, '971595': {'fecha': ('2023', '06', '24'), 'local': 'Lanus', 'visitante': 'Talleres Cordoba'}, '971596': {'fecha': ('2023', '06', '25'), 'local': 'Arsenal Sarandi', 'visitante': 'Platense'}, '971597': {'fecha': ('2023', '06', '22'), 'local': 'Tigre', 'visitante': 'Velez Sarsfield'}, '971598': {'fecha': ('2023', '06', '24'), 'local': 'Argentinos JRS', 'visitante': 'Defensa Y Justicia'}, '971599': {'fecha': ('2023', '06', '26'), 'local': 'Belgrano Cordoba', 'visitante': 'Banfield'}, '971600': {'fecha': ('2023', '06', '22'), 'local': 'Racing Club', 'visitante': 'Barracas Central'}, '971601': {'fecha': ('2023', '06', '25'), 'local': 'Rosario Central', 'visitante': 'Colon Santa Fe'}, '971602': {'fecha': ('2023', '06', '21'), 'local': 'Estudiantes L.P.', 'visitante': 'San Lorenzo'}, '971603': {'fecha': ('2023', '07', '02'), 'local': 'Estudiantes L.P.', 'visitante': 'Central Cordoba de Santiago'}, '971604': {'fecha': ('2023', '07', '02'), 'local': 'San Lorenzo', 'visitante': 'Rosario Central'}, '971605': {'fecha': ('2023', '07', '02'), 'local': 'Colon Santa Fe', 'visitante': 'Racing Club'}, '971606': {'fecha': ('2023', '07', '02'), 'local': 'Barracas Central', 'visitante': 'River Plate'}, '971607': {'fecha': ('2023', '07', '02'), 'local': 'Banfield', 'visitante': 'Argentinos JRS'}, '971608': {'fecha': ('2023', '07', '02'), 'local': 'Defensa Y Justicia', 'visitante': 'Tigre'}, '971609': {'fecha': ('2023', '07', '02'), 'local': 'Velez Sarsfield', 'visitante': 'Arsenal Sarandi'}, '971610': {'fecha': ('2023', '07', '02'), 'local': 'Platense', 'visitante': 'Lanus'}, '971611': {'fecha': ('2023', '07', '02'), 'local': 'Talleres Cordoba', 'visitante': 'Godoy Cruz'}, '971612': {'fecha': ('2023', '07', '02'), 'local': 'Atletico Tucuman', 'visitante': 'Union Santa Fe'}, '971613': {'fecha': ('2023', '07', '02'), 'local': 'Independiente', 'visitante': 'Huracan'}, '971614': {'fecha': ('2023', '07', '02'), 'local': 'Newells Old Boys', 'visitante': 'Gimnasia L.P.'}, '971615': {'fecha': ('2023', '07', '05'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Newells Old Boys'}, '971616': {'fecha': ('2023', '07', '05'), 'local': 'Gimnasia L.P.', 'visitante': 'Independiente'}, '971617': {'fecha': ('2023', '07', '05'), 'local': 'Huracan', 'visitante': 'Atletico Tucuman'}, '971618': {'fecha': ('2023', '07', '05'), 'local': 'Union Santa Fe', 'visitante': 'Boca Juniors'}, '971619': {'fecha': ('2023', '07', '05'), 'local': 'Godoy Cruz', 'visitante': 'Platense'}, '971620': {'fecha': ('2023', '07', '05'), 'local': 'Lanus', 'visitante': 'Velez Sarsfield'}, '971621': {'fecha': ('2023', '07', '05'), 'local': 'Arsenal Sarandi', 'visitante': 'Defensa Y Justicia'}, '971622': {'fecha': ('2023', '07', '05'), 'local': 'Tigre', 'visitante': 'Banfield'}, '971623': {'fecha': ('2023', '07', '05'), 'local': 'Belgrano Cordoba', 'visitante': 'Barracas Central'}, '971624': {'fecha': ('2023', '07', '05'), 'local': 'River Plate', 'visitante': 'Colon Santa Fe'}, '971625': {'fecha': ('2023', '07', '05'), 'local': 'Racing Club', 'visitante': 'San Lorenzo'}, '971626': {'fecha': ('2023', '07', '05'), 'local': 'Rosario Central', 'visitante': 'Estudiantes L.P.'}, '971627': {'fecha': ('2023', '07', '09'), 'local': 'Rosario Central', 'visitante': 'Central Cordoba de Santiago'}, '971628': {'fecha': ('2023', '07', '09'), 'local': 'Estudiantes L.P.', 'visitante': 'Racing Club'}, '971629': {'fecha': ('2023', '07', '09'), 'local': 'San Lorenzo', 'visitante': 'River Plate'}, '971630': {'fecha': ('2023', '07', '09'), 'local': 'Colon Santa Fe', 'visitante': 'Belgrano Cordoba'}, '971631': {'fecha': ('2023', '07', '09'), 'local': 'Barracas Central', 'visitante': 'Argentinos JRS'}, '971632': {'fecha': ('2023', '07', '09'), 'local': 'Banfield', 'visitante': 'Arsenal Sarandi'}, '971633': {'fecha': ('2023', '07', '09'), 'local': 'Defensa Y Justicia', 'visitante': 'Lanus'}, '971634': {'fecha': ('2023', '07', '09'), 'local': 'Velez Sarsfield', 'visitante': 'Godoy Cruz'}, '971635': {'fecha': ('2023', '07', '09'), 'local': 'Talleres Cordoba', 'visitante': 'Union Santa Fe'}, '971636': {'fecha': ('2023', '07', '09'), 'local': 'Boca Juniors', 'visitante': 'Huracan'}, '971637': {'fecha': ('2023', '07', '09'), 'local': 'Atletico Tucuman', 'visitante': 'Gimnasia L.P.'}, '971638': {'fecha': ('2023', '07', '09'), 'local': 'Independiente', 'visitante': 'Newells Old Boys'}, '971639': {'fecha': ('2023', '07', '16'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Independiente'}, '971640': {'fecha': ('2023', '07', '16'), 'local': 'Newells Old Boys', 'visitante': 'Atletico Tucuman'}, '971641': {'fecha': ('2023', '07', '16'), 'local': 'Gimnasia L.P.', 'visitante': 'Boca Juniors'}, '971642': {'fecha': ('2023', '07', '16'), 'local': 'Huracan', 'visitante': 'Talleres Cordoba'}, '971643': {'fecha': ('2023', '07', '16'), 'local': 'Union Santa Fe', 'visitante': 'Platense'}, '971644': {'fecha': ('2023', '07', '16'), 'local': 'Godoy Cruz', 'visitante': 'Defensa Y Justicia'}, '971645': {'fecha': ('2023', '07', '16'), 'local': 'Lanus', 'visitante': 'Banfield'}, '971646': {'fecha': ('2023', '07', '16'), 'local': 'Tigre', 'visitante': 'Barracas Central'}, '971647': {'fecha': ('2023', '07', '16'), 'local': 'Argentinos JRS', 'visitante': 'Colon Santa Fe'}, '971648': {'fecha': ('2023', '07', '16'), 'local': 'Belgrano Cordoba', 'visitante': 'San Lorenzo'}, '971649': {'fecha': ('2023', '07', '16'), 'local': 'River Plate', 'visitante': 'Estudiantes L.P.'}, '971650': {'fecha': ('2023', '07', '16'), 'local': 'Racing Club', 'visitante': 'Rosario Central'}, '971651': {'fecha': ('2023', '07', '23'), 'local': 'Racing Club', 'visitante': 'Central Cordoba de Santiago'}, '971652': {'fecha': ('2023', '07', '23'), 'local': 'Rosario Central', 'visitante': 'River Plate'}, '971653': {'fecha': ('2023', '07', '23'), 'local': 'Estudiantes L.P.', 'visitante': 'Belgrano Cordoba'}, '971654': {'fecha': ('2023', '07', '23'), 'local': 'San Lorenzo', 'visitante': 'Argentinos JRS'}, '971655': {'fecha': ('2023', '07', '23'), 'local': 'Colon Santa Fe', 'visitante': 'Tigre'}, '971656': {'fecha': ('2023', '07', '23'), 'local': 'Barracas Central', 'visitante': 'Arsenal Sarandi'}, '971657': {'fecha': ('2023', '07', '23'), 'local': 'Banfield', 'visitante': 'Godoy Cruz'}, '971658': {'fecha': ('2023', '07', '23'), 'local': 'Velez Sarsfield', 'visitante': 'Union Santa Fe'}, '971659': {'fecha': ('2023', '07', '23'), 'local': 'Platense', 'visitante': 'Huracan'}, '971660': {'fecha': ('2023', '07', '23'), 'local': 'Talleres Cordoba', 'visitante': 'Gimnasia L.P.'}, '971661': {'fecha': ('2023', '07', '23'), 'local': 'Boca Juniors', 'visitante': 'Newells Old Boys'}, '971662': {'fecha': ('2023', '07', '23'), 'local': 'Atletico Tucuman', 'visitante': 'Independiente'}, '971663': {'fecha': ('2023', '07', '30'), 'local': 'Central Cordoba de Santiago', 'visitante': 'Atletico Tucuman'}, '971664': {'fecha': ('2023', '07', '30'), 'local': 'Independiente', 'visitante': 'Boca Juniors'}, '971665': {'fecha': ('2023', '07', '30'), 'local': 'Newells Old Boys', 'visitante': 'Talleres Cordoba'}, '971666': {'fecha': ('2023', '07', '30'), 'local': 'Gimnasia L.P.', 'visitante': 'Platense'}, '971667': {'fecha': ('2023', '07', '30'), 'local': 'Huracan', 'visitante': 'Velez Sarsfield'}, '971668': {'fecha': ('2023', '07', '30'), 'local': 'Union Santa Fe', 'visitante': 'Defensa Y Justicia'}, '971669': {'fecha': ('2023', '07', '30'), 'local': 'Lanus', 'visitante': 'Barracas Central'}, '971670': {'fecha': ('2023', '07', '30'), 'local': 'Arsenal Sarandi', 'visitante': 'Colon Santa Fe'}, '971671': {'fecha': ('2023', '07', '30'), 'local': 'Tigre', 'visitante': 'San Lorenzo'}, '971672': {'fecha': ('2023', '07', '30'), 'local': 'Argentinos JRS', 'visitante': 'Estudiantes L.P.'}, '971673': {'fecha': ('2023', '07', '30'), 'local': 'Belgrano Cordoba', 'visitante': 'Rosario Central'}, '971674': {'fecha': ('2023', '07', '30'), 'local': 'River Plate', 'visitante': 'Racing Club'}, '988669': {'fecha': ('2023', '08', '20'), 'local': 'Instituto Cordoba', 'visitante': 'Arsenal Sarandi'}, '988670': {'fecha': ('2023', '08', '20'), 'local': 'Sarmiento Junin', 'visitante': 'Tigre'}, '988671': {'fecha': ('2023', '08', '27'), 'local': 'Atletico Tucuman', 'visitante': 'Instituto Cordoba'}, '988672': {'fecha': ('2023', '08', '27'), 'local': 'Sarmiento Junin', 'visitante': 'Boca Juniors'}, '988673': {'fecha': ('2023', '09', '03'), 'local': 'Instituto Cordoba', 'visitante': 'Banfield'}, '988674': {'fecha': ('2023', '09', '03'), 'local': 'Defensa Y Justicia', 'visitante': 'Sarmiento Junin'}, '988675': {'fecha': ('2023', '09', '10'), 'local': 'Talleres Cordoba', 'visitante': 'Instituto Cordoba'}, '988676': {'fecha': ('2023', '09', '10'), 'local': 'Sarmiento Junin', 'visitante': 'Central Cordoba de Santiago'}, '988677': {'fecha': ('2023', '09', '17'), 'local': 'Instituto Cordoba', 'visitante': 'Colon Santa Fe'}, '988678': {'fecha': ('2023', '09', '17'), 'local': 'Lanus', 'visitante': 'Sarmiento Junin'}, '988679': {'fecha': ('2023', '09', '24'), 'local': 'Independiente', 'visitante': 'Instituto Cordoba'}, '988680': {'fecha': ('2023', '09', '24'), 'local': 'Sarmiento Junin', 'visitante': 'Belgrano Cordoba'}, '988681': {'fecha': ('2023', '10', '01'), 'local': 'Barracas Central', 'visitante': 'Sarmiento Junin'}, '988682': {'fecha': ('2023', '10', '01'), 'local': 'Instituto Cordoba', 'visitante': 'Godoy Cruz'}, '988683': {'fecha': ('2023', '10', '08'), 'local': 'Instituto Cordoba', 'visitante': 'Gimnasia L.P.'}, '988684': {'fecha': ('2023', '10', '08'), 'local': 'Union Santa Fe', 'visitante': 'Sarmiento Junin'}, '988685': {'fecha': ('2023', '10', '15'), 'local': 'Huracan', 'visitante': 'Instituto Cordoba'}, '988686': {'fecha': ('2023', '10', '15'), 'local': 'Sarmiento Junin', 'visitante': 'Racing Club'}, '988687': {'fecha': ('2023', '10', '22'), 'local': 'Instituto Cordoba', 'visitante': 'Rosario Central'}, '988688': {'fecha': ('2023', '10', '22'), 'local': 'Estudiantes L.P.', 'visitante': 'Sarmiento Junin'}, '988689': {'fecha': ('2023', '10', '29'), 'local': 'Instituto Cordoba', 'visitante': 'Velez Sarsfield'}, '988690': {'fecha': ('2023', '10', '29'), 'local': 'Sarmiento Junin', 'visitante': 'San Lorenzo'}, '988691': {'fecha': ('2023', '11', '05'), 'local': 'Argentinos JRS', 'visitante': 'Instituto Cordoba'}, '988692': {'fecha': ('2023', '11', '05'), 'local': 'Newells Old Boys', 'visitante': 'Sarmiento Junin'}, '988693': {'fecha': ('2023', '11', '12'), 'local': 'Instituto Cordoba', 'visitante': 'Barracas Central'}, '988694': {'fecha': ('2023', '11', '12'), 'local': 'Sarmiento Junin', 'visitante': 'Godoy Cruz'}, '988695': {'fecha': ('2023', '11', '19'), 'local': 'River Plate', 'visitante': 'Instituto Cordoba'}, '988696': {'fecha': ('2023', '11', '19'), 'local': 'Platense', 'visitante': 'Sarmiento Junin'}, '988736': {'fecha': ('2023', '06', '25'), 'local': 'Sarmiento Junin', 'visitante': 'Atletico Tucuman'}, '988737': {'fecha': ('2023', '06', '22'), 'local': 'River Plate', 'visitante': 'Instituto Cordoba'}, '988738': {'fecha': ('2023', '07', '02'), 'local': 'Instituto Cordoba', 'visitante': 'Belgrano Cordoba'}, '988739': {'fecha': ('2023', '07', '02'), 'local': 'Boca Juniors', 'visitante': 'Sarmiento Junin'}, '988740': {'fecha': ('2023', '07', '05'), 'local': 'Sarmiento Junin', 'visitante': 'Talleres Cordoba'}, '988741': {'fecha': ('2023', '07', '05'), 'local': 'Argentinos JRS', 'visitante': 'Instituto Cordoba'}, '988742': {'fecha': ('2023', '07', '09'), 'local': 'Instituto Cordoba', 'visitante': 'Tigre'}, '988743': {'fecha': ('2023', '07', '09'), 'local': 'Platense', 'visitante': 'Sarmiento Junin'}, '988744': {'fecha': ('2023', '07', '16'), 'local': 'Sarmiento Junin', 'visitante': 'Velez Sarsfield'}, '988745': {'fecha': ('2023', '07', '16'), 'local': 'Arsenal Sarandi', 'visitante': 'Instituto Cordoba'}, '988746': {'fecha': ('2023', '07', '23'), 'local': 'Instituto Cordoba', 'visitante': 'Lanus'}, '988747': {'fecha': ('2023', '07', '23'), 'local': 'Defensa Y Justicia', 'visitante': 'Sarmiento Junin'}, '988748': {'fecha': ('2023', '07', '30'), 'local': 'Sarmiento Junin', 'visitante': 'Banfield'}, '988749': {'fecha': ('2023', '07', '30'), 'local': 'Godoy Cruz', 'visitante': 'Instituto Cordoba'}}]
    
    return informacion_api
def diccionario_api(API: dict) -> list:
    """
    PRE: Un parámetro dict. Recopila toda la información que se va a emplear (o no) a lo largo
         del programa en una lista de diccionarios.
    POST: Un valor de retorno list. Devuelve una lista con los tres diccionarios creados.
    """
    imprimir_carga(0)

    temporadas: dict = diccionario_temporadas(API)
    equipos: dict = diccionario_equipos(API, temporadas)
    fixtures: dict = diccionario_fixtures (API)

    informacion_api: list = [temporadas, equipos, fixtures]

    imprimir_carga(4)
    time.sleep(0.5)

    return(informacion_api)

def imprimir_carga(tiempo: int) -> None:
    """
    PRE: Un parámetro int. Recibe el valor de un número entero.
    POST: Ningún valor de retorno. Imprime la cadena que se encuentra en la posición del entero ingresado.
    """
    CARGA: list = [
    "0% ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ 100%", "33% ▮ ▮ ▮ ▯ ▯ ▯ ▯ ▯ ▯ ▯ 100%",
    "66% ▮ ▮ ▮ ▮ ▮ ▮ ▯ ▯ ▯ ▯ 100%", "99% ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▯ 100%",
    "100% ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ ▮ 100%", "Cargando..."
    ]

    os.system("cls")
    print(CARGA[5])
    print(CARGA[tiempo])

    return(None)

def diccionario_temporadas(API: dict) -> dict:
    """
    PRE: Un parámetro dict. Crea el diccionario "temporadas" el cual almacena los años de la liga
         como clave, y los resultados de las posiciones como sus valores.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" ordenado por años de forma
          ascendente.
    """
    temporadas: dict = {}
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["temporadas"], headers=API["HEADERS"])).json()).get("response")
    seasons: dict = (response[0]).get("seasons")

    for season in seasons:
        if (season.get("year") not in temporadas):
            if (int(season.get("year")) < 2020):
                temporadas[season.get("year")] = []

            elif (int(season.get("year")) == 2020):
                temporadas[season.get("year")] = {}

            else:
                temporadas[season.get("year")] = {
                "Primera Fase": [],
                "Segunda Fase": []
                }

    temporadas: dict = informacion_posiciones(API, temporadas)
    imprimir_carga(1)

    return(temporadas)

def diccionario_equipos(API: dict, temporadas: dict) -> dict:
    """
    PRE: Dos parámetros dict. La función extrae, de cada temporada, los datos necesarios de los
         equipos que alguna vez participaron en la liga y almacena los nombres como claves, y
         los datos dentro de otro diccionario.
    POST: Un valor de retorno dict. Devuelve el diccionario "equipos" con la información detallada.
    """
    equipos: dict = {}

    for key in temporadas:
        
        time.sleep(6.0)
        response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["equipos"] + str(key), headers=API["HEADERS"])).json()).get("response")

        for i in range (len(response)):

            nombre_equipo: str = response[i]["team"]["name"]
            code: str = str(response[i]["team"]["id"])
            año: str = str(response[i]["team"]["founded"])
            escudo: str = response[i]["team"]["logo"]
            nombre_estadio: str = response[i]["venue"]["name"]
            direccion: str = response[i]["venue"]["address"]
            ciudad: str = response[i]["venue"]["city"]
            capacidad: str = str(response[i]["venue"]["capacity"])
            superficie: str = traducir_dato(response[i]["venue"]["surface"].lower())
            foto: str = response[i]["venue"]["image"]

            if (int(key) != 2023):

                if (nombre_equipo not in equipos):
                    equipos[nombre_equipo] = {
					"id": code,
					"año": año,
					"escudo": escudo,
					"estadio": nombre_estadio,
					"direccion": direccion,
					"ciudad": ciudad,
					"capacidad": capacidad,
					"superficie": superficie,
					"foto": foto,
					"plantel": None,
					"estadisticas": None
					}

            else:
                
                plantel: list = informacion_planteles(API, code)
                estadistica: dict = informacion_estadisticas(API, code)

                if (nombre_equipo not in equipos):
                    equipos[nombre_equipo] = {
					"id": code,
					"año": año,
					"escudo": escudo,
					"estadio": nombre_estadio,
					"direccion": direccion,
					"ciudad": ciudad,
					"capacidad": capacidad,
					"superficie": superficie,
					"foto": foto,
					"plantel": plantel,
					"estadisticas": estadistica
					}
    
    imprimir_carga(2)

    return(equipos)

def diccionario_fixtures(API: dict) -> dict:
    """
    PRE: Un parámetro dict. La función extrae los datos necesarios del fixture 2023 y los almacena
         por id en el diccionario "fixtures".
    POST: Un valor de retorno dict. Devuelve el diccionario "fixtures" con la información detallada.
    """
    time.sleep(6.0)

    fixtures: dict = {}
    hoy: str = fecha_actual()
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["fixtures"], headers=API["HEADERS"])).json()).get("response")

    for i in range (len(response)):

        fecha: tuple = reordenar_fecha(response[i]["fixture"]["date"])

        if (fecha[0]+fecha[1]+fecha[2] >= hoy):

            code: str = str(response[i]["fixture"]["id"])
            local: str = response[i]["teams"]["home"]["name"]
            visitante: str = response[i]["teams"]["away"]["name"]

            if (code not in fixtures):
                fixtures[code] = {
                "fecha": fecha,
                "local": local,
                "visitante": visitante,
                }

    imprimir_carga(3)

    return(fixtures)

def informacion_planteles(API: dict, code: str) -> list:
    """
    PRE: Un parámetro dict. Un parámetro str. Por cada equipo participante de la temporada 2023, la
         función extrae los datos disponibles del plantel y los almacena en una lista.
    POST: Un valor de retorno list. Devuelve la lista "plantel" con la información detallada.
    """
    time.sleep(6.0)

    plantel: list = []
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["planteles"] + code, headers=API["HEADERS"])).json()).get("response")

    for i in range (len(response)):

        nombre_completo: str = response[i]["player"]["firstname"] + " " + response[i]["player"]["lastname"] 
        posicion: str = traducir_dato((response[i]["statistics"][0]["games"]["position"]).lower())

        if ((response[i]["statistics"][0]["games"]["captain"]) == True):
            dato_completo: str = f"{nombre_completo} ({posicion}), CAPITÁN"

        else:
            dato_completo: str = f"{nombre_completo} ({posicion})"

        plantel.append(dato_completo)

    return(plantel)

def informacion_posiciones(API: dict, temporadas: dict) -> dict:
    """
    PRE: Dos parámetros dict. La función extrae, por temporada, las posiciones
         y los puntos de los equipos en la liga y los almacena en el diccionario "temporadas" por orden.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información nueva agregada.
    """
    for key in temporadas:

        time.sleep(6.0)

        response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["posiciones"] + str(key), headers=API["HEADERS"])).json()).get("response")
        league: dict = (response[0]).get("league")

        if (int(key) < 2020):
            temporadas: dict = posiciones_sistema_antiguo(key, league, temporadas)

        elif (int(key) == 2020):
            temporadas: dict = posiciones_sistema_2020(key, league, temporadas)

        else:
            temporadas: dict = posiciones_sistema_nuevo(key, league, temporadas)

    return(temporadas)

def posiciones_sistema_antiguo(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Si la temporada es previa al 2019 (inclusive) la función
         ordena la información segun como haya funcionado el sistema de posiciones de ese año.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información detallada.
    """
    for i in range (len(league["standings"][0])):

        equipo: str = league["standings"][0][i]["team"]["name"]
        puntos: str = str(league["standings"][0][i]["points"])

        temporadas[key].append((equipo, puntos))

    return(temporadas)

def posiciones_sistema_2020(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Si la temporada es 2020 la función ordena la
         información segun como haya funcionado el sistema de posiciones de ese año.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información detallada.
    """
    for i in range (len(league["standings"])):

        for j in range (len(league["standings"][i])):

            grupo: str = league["standings"][i][j]["group"]
            equipo: str = league["standings"][i][j]["team"]["name"]
            puntos: str = str(league["standings"][i][j]["points"])

            if (grupo not in temporadas[key]):
                temporadas[key][grupo] = []
            
            if (i <= 4):
                    temporadas[key][grupo].append((equipo, puntos))
            
            else:
                    temporadas[key][grupo].append((equipo, puntos))
    
    return(temporadas)

def posiciones_sistema_nuevo(key: str, league: dict, temporadas: dict) -> dict:
    """
    PRE: Un parámetro str. Dos parámetros dict. Si la temporada es a partir del 2021 (inclusive) la
         función ordena la información segun como haya funcionado el sistema de posiciones de ese año.
    POST: Un valor de retorno dict. Devuelve el diccionario "temporadas" con la información detallada.
    """
    for i in range (len(league["standings"][0])):

        equipo: str = league["standings"][0][i]["team"]["name"]
        puntos: str = str(league["standings"][0][i]["points"])

        temporadas[key]["Segunda Fase"].append((equipo, puntos))

    for i in range (len(league["standings"][1])):

        equipo: str = league["standings"][1][i]["team"]["name"]
        puntos: str = str(league["standings"][1][i]["points"])

        temporadas[key]["Primera Fase"].append((equipo, puntos))
    
    return(temporadas)

def informacion_predicciones(API: dict, code: str) -> str:
    """
    PRE: Un parámetro dict. Un parámetro str. Por cada partido aún no jugado, la función extrae
         el nombre del equipo que la API cree será el ganador.
    POST: Un valor de retorno str. Devuelve la predicción.
    """
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["predicciones"] + code, headers=API["HEADERS"])).json()).get("response")

    prediccion: str = response[0]["predictions"]["winner"]["name"]

    return(prediccion)

def informacion_estadisticas(API: dict, code: str) -> dict:
    """
    PRE: Un parámetro dict. Un parámetro str. La función extrae las estadísticas de goles por minuto de
         los equipos de la temporada 2023.
    POST: Un valor de retorno dict. Devuelve el diccionario "estadicticas" con la información detallada.
    """
    time.sleep(6.0)

    estadistica: dict = {}
    response: list = ((requests.request("GET", API["URL"] + API["ENDPOINTS"]["estadisticas"] + code, headers=API["HEADERS"])).json()).get("response")

    for intervalo in response["goals"]["for"]["minute"]:
        
        if (response["goals"]["for"]["minute"][intervalo]["total"] == None):
            goles: int = 0

        else:
            goles: int = response["goals"]["for"]["minute"][intervalo]["total"]
        
        estadistica[intervalo] = goles

    return(estadistica)

def traducir_dato(dato: str) -> str:
    """
    PRE: Un parámetros str. Recibe una palabra en inglés.
    POST: Un valor de retorno str. Devuelve la cadena traducida al español según corresponda.
    """
    if (dato == "grass"):
        traduccion: str = "Pasto sintético"

    elif (dato == "goalkeeper"):
        traduccion: str = "Arquero"

    elif (dato == "defender"):
        traduccion: str = "Defensor"

    elif (dato == "midfielder"):
        traduccion: str = "Mediocampista"

    return(dato)

def reordenar_fecha(fecha: str) -> tuple:
    """
    PRE: Un parámetro str. Recibe una fecha y hora con la siguiente forma 'XXXX-XX-XXTXX:XX:XX+XX:XX',
         extrae unicamente la fecha y le da un nuevo formato.
    POST: Un valor de retorno tuple. Devuelve la fecha en una tupla '(año, mes, día)'.
    """
    año: str = fecha[:4:]
    mes: str = fecha[5:7:]
    dia: str = fecha[8:10:]

    return ((año, mes, dia))

def fecha_actual()->str:
    #Devuelve un string en el formato YYYYMMDD de la fecha actual
    
    año = str((datetime.now()).year)
    mes = str((datetime.now()).month)
    dia = str((datetime.now()).day)
    if len(mes)!=2:
        mes = "0"+mes
    cadena = (año+mes+dia)
    return cadena

def registro_transacciones(mail:str,tipo:int,importe:int,lista_transacciones:list):
    #El type in del mail se puede modificar
    #Toma la fecha de hoy
    #El tipo de transaccion se determina con los valores 0,1 y 2 de la siguiente manera
    if tipo == 0:
        resultado = "deposita"
    elif tipo==1:
        resultado = "gana"
    elif tipo==2:
        resultado="pierde"
        
    fecha = fecha_actual()
    datos_de_escritura = [[mail,fecha,resultado,importe]]
    lista_transacciones.append(datos_de_escritura)
    

def mayor_ganador (usuarios_diccionario:dict, transacciones_listado:list) -> None:
    cantidad_apuestas = {} # usuario: cantidad
    mayor_ganador = ""
    mayor_veces_ganado = 0


    for i in range(len(transacciones_listado)):
        if transacciones_listado[i][2] == "Gana":
            if transacciones_listado[i][0] not in cantidad_apuestas:
                cantidad_apuestas[transacciones_listado[i][0]] = 1
            else: cantidad_apuestas[transacciones_listado[i][0]] += 1

    for i in cantidad_apuestas:
        if cantidad_apuestas[i] >= mayor_veces_ganado:
            mayor_veces_ganado = cantidad_apuestas[i]
            mayor_ganador = i

    print(f"El usuario que más veces ganó es {usuarios_diccionario[mayor_ganador][0]}")
    
def mayor_apostador (usuarios_diccionario:dict) -> None:
    mayor_apostador = ""
    mayor_cantidad_apostada = float(0)

    for i in usuarios_diccionario:
        if usuarios_diccionario[i][2] >= mayor_cantidad_apostada:
            mayor_cantidad_apostada = usuarios_diccionario[i][2]
            mayor_apostador = usuarios_diccionario[i][0]

    print(f"El usuario que más dinero apostó es {mayor_apostador} ")

def cargar_dinero (email:str, usuarios_diccionario:dict, transacciones_listado:list) -> None:
    print("Carga de Dinero")
    dinero = float(input("Ingrese la cantidad de dinero que quiere ingresar en su cuenta: "))
    while dinero <= 0: dinero = float(input("Error, ingrese la cantidad de dinero que quiere ingresar en su cuenta: "))
    
    usuarios_diccionario[email][4] += dinero
    transacciones_listado.append([email,"fecha","Deposita",usuarios_diccionario[email][4]])
    print(f"Dinero disponible: {usuarios_diccionario[email][4]}")

def grafica_goles (informacion_api:list) -> None:
    print("Grafica de Goles")
    equipo = str(input("Ingrese el equipo para ver sus goles por partido: ")) #validacion del equipo

    # estadisticas = informacion_api[2][equipo]["estadisticas"]

    estadisticas = {"3": 5, "5": 8,"6": 10}
    minutos: list = []
    goles: list = []

    for tiempo in estadisticas:
        minutos.append(tiempo)
        goles.append(estadisticas[tiempo])

    plt.xlabel('MINUTOS')
    plt.ylabel('GOLES')
    plt.title('GOLES REALIZADOS POR INTERVALO DE TIEMPO')

    plt.bar(minutos, goles)
    plt.show()

def informacion_equipo(informacion_api:list) -> None:
    equipos = informacion_api[1]

    print("Informacion de equipos")
    equipo = input("Ingrese el nombre de un equipo para ver su informacion: ")
    while equipo not in informacion_api[1]:
        equipo = input("Equipo no encontrado, ingrese el nombre de otro equipo para ver su informacion: ")

    print("Informacion del estadio")

    # print(f"El estadio de {equipos["NOMBRE EQUIPO"]} fue bautizado como {equipos["NOMBRE EQUIPO"]["estadio"]'. El mismo se encuentra en equipos["NOMBRE EQUIPO"]["direccion"], equipos["NOMBRE EQUIPO"]["ciudad"]. Tiene una capacidad total de equipos["NOMBRE EQUIPO"]["capacidad"] espectadores, y su superficie está hecha de equipos["NOMBRE EQUIPO"]["superficie"].")

    plt.imshow(equipos["NOMBRE EQUIPO"]["foto"])
    plt.show()

    print(f"Y su escudo, es el siguiente")

    plt.imshow(equipos["NOMBRE EQUIPO"]["escudo"])
    plt.show()

def tabla_posiciones(informacion_api:list) -> None:
    temporadas = informacion_api[0]

    print("Tabla de posiciones de la Liga Profesional")
    temporada = int(input("Ingrese la temporada de la cual quiere ver su ranking: "))
    while temporada < 2015 or temporada > 2023:
        temporada = int(input("Las temporadas disponibles son 2015-2023, ingrese la temporada de la cual quiere ver su ranking: "))

    if temporada == 2020:
        for i in temporadas["2015-2019"]["1er Año"]:
            print(temporadas[temporada][i][0]) #EQUIPOS
            print(temporadas[temporada][i][0]) #PUNTOS

def listado_equipos(informacion_api:list) -> None:
    print("Listado de equipos de la Liga Profesional correspondiente temporada 2023")
    for i in informacion_api[1]:
        print(informacion_api[1][i])
    equipo = input("Ingrese el nombre de un equipo para ver su plantel: ")
    while equipo not in informacion_api[1]:
        equipo = input("Equipo no encontrado, ingrese el nombre de otro equipo para ver su plantel: ")

    print("plantel")

def definir_partidos(equipo:str,fixtures:dict)->dict:
    partidos = {}
   
    for partido in fixtures:
        local = fixtures[partido]["local"].upper()
        visitante = fixtures[partido]["visitante"].upper()
        if equipo == local or equipo == visitante:
            info_partidos:list = fixtures[partido]
            partidos[partido] = info_partidos   

    return partidos

def encuadrado(objeto:str)->str:
    objeto = objeto + " " * (35 - (len(objeto)))
    return objeto

def mostrar_fixture(equipo:str,fixture:dict):
    partidos_a_alegir = (definir_partidos(equipo,fixture)).items()
    indice = 0
    if len(partidos_a_alegir)> 0:
        print("| "+"Local"+" "*30+"|"+"visitante"+" "*26+"|"+"Fecha"+" "*3+"|")
        for partido in partidos_a_alegir:
            indice=indice+1
            año,mes,dia = partido[1]["fecha"]
            partido_fecha = año+mes+dia
            partido_local = partido[1]["local"]
            partido_visitante = partido[1]["visitante"]
            
            #AGREGO ESPACIADO PARA EL CUADRO
            partido_local = encuadrado(partido_local)
            partido_visitante = encuadrado(partido_visitante)
            print(f"|{indice}| {partido_local}|{partido_visitante}|{partido_fecha}|")
            
        partido_elegido = int(input("Elija un partido "))
        partidos_a_alegir = list(partidos_a_alegir)
        return partidos_a_alegir[partido_elegido-1] # El numero 1 es el 0 de la lista.
    

def validar_apuesta_lv()-> str:
    lov = input("Ingrese a que equipo apostara Ganador(L)/Empate/Ganador(V) ")
    validado = False
    
    while validado is False:
        lov = lov.upper()
        if lov != "GANADOR(L)" and lov != "EMPATE" and lov != "GANADOR(V)": 
            lov = input("El termino ingresado no es correcto, Ganador(L)/Empate/Ganador(V)")
        else:
            validado = True
            if lov =="GANADOR(L)":
                apuesta = 1
            if lov == "EMPATE":
                apuesta = 2
            if lov == "GANADOR(V)":
                apuesta = 3
    return apuesta

def apuesta_dinero(dinero_disponible:int)->int:
    #FALTA AGREGAR LA FUNCION QUE AGREGA DINERO EN LA CUENTA
    cantidad_apostada = int(input("Ingrese la cantidad de dinero a apostar"))
    apuesta_check = False
    
    
    while apuesta_check is False:
        if cantidad_apostada > dinero_disponible:
            
            print("La cantidad de dinero que quieres apostar no se encuentra disponible en tu cuenta")
            print("1. Cargar mas dinero a la cuenta")
            print("2. Cambiar la cantidad apostada")
            print("3. Cancelar la operacion")
            respuesta = input("Que curso de accion desea tomar?")
            
            
            if respuesta == "1":
                #ACA VA LA FUNCION QUE CARGA PLATA A LA CUENTA
                pass
            
            elif respuesta == "2":
                cantidad_apostada = intinput("Ingrese la nueva cantidad a apostar")
                
            elif respuesta == "3":
                cantidad_apostada = -1
                apuesta_check = True
        else:
            apuesta_check = True
            
    return cantidad_apostada
        
def pago_apuesta(resultado_apostado:int,dinero_apostado:int,prediccion:int,resultado_final:int,ratio_pago:int)->tuple:
    balance_final = 0
    tipo = ""
    
    if resultado_apostado == resultado_final:
        tipo = "Gana"
        if resultado_apostado == 2:
            balance_final == dinero_apostado + (dinero_apostado*ratio_pago)/2
        elif resultado_apostado == prediccion:
            balance_final == dinero_apostado + (dinero_apostado*ratio_pago)/10
        else:
            balance_final == dinero_apostado + (dinero_apostado*ratio_pago)
    else:
        tipo = "Pierde"
        balance_final = -dinero_apostado
        
    return (balance_final,tipo) 

def resultados_apuesta(apuesta,partido,api):
    id = partido[0]
    resultado_apostado,dinero_apostado = apuesta
    prediccion = informacion_predicciones("API", id)
    ganador = random.randint(1,3)
    ratio_pago = random.randint(1,4)
    
    return pago_apuesta(resultado_apostado,dinero_apostado,prediccion,ganador,ratio_pago)

def definir_apuesta(datos_del_partido,dinero_en_cuenta): 
    #ARGUMENTOS A DEFINIR, FUNCION INCOMPLETA
    local_o_visitante =  validar_apuesta_lv()
   
    cantidad_apostada = apuesta_dinero(dinero_en_cuenta)
   
    
    valor_apuesta = [local_o_visitante,cantidad_apostada]
    return valor_apuesta
    
def printear_equipos_disponibles(equipos:dict)->None:
    i = 0
    for equipo in equipos.keys():
        i = i + 1
        print(f"{i}. {equipo}")
        
def validar_equipos(lista_equipos:dict)->str:
    equipo = input("Ingrese el nombre del equipo \n")
    valido = False
    while valido is False:
        equipo = equipo.upper()
        for equipo_en_lista in lista_equipos:
            equipo_en_lista = equipo_en_lista.upper()
            if equipo == equipo_en_lista:
                valido = True
                continue
            
        if valido is False:
            printear_equipos_disponibles(lista_equipos)
    
            equipo = input("Equipo invalido, ingrese un equipo que se encuentre en la lista \n")
            
    return equipo

def menu_apuesta(mail:str,dict_usuarios:dict,dict_transacciones:dict,dict_equipos:dict,fixture:dict)->None:
    dinero_en_cuenta = int(dict_usuarios[mail][4])
    is_partido_elegido = False
    while is_partido_elegido is False:
        printear_equipos_disponibles(dict_equipos)
        equipo = validar_equipos(dict_equipos)
    
        partido = mostrar_fixture(equipo,fixture)
        if len(partido)>0: 
            is_partido_elegido = True
        else:
            print("No existen partidos del equipo elegido. Por favor elija otro equipo")
    
    apuesta = definir_apuesta(partido,dinero_en_cuenta)
    if apuesta[1] != -1:
        tipo,dinero_a_modificar = resultados_apuesta(apuesta,partido)
        #registro_transacciones(mail,tipo,dinero_a_modificar,dict_transacciones)
        #AGREGAR: MODIFICAR LA CANTIDAD DE DINERO EN EL DOCUMENTO DE USUARIOS


def apuesta_main () -> None:
    print("Menu de apuestas")


def opt_menu() -> None:
    opt = str(input("Ingrese una opción: "))
    while opt not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: opt = str(input("Ingrese una opción valida: "))
    print(f"-"*20)
    return opt

def print_menu() -> None:
    print(f"-"*20)
    print(f"Esta es la interfaz, seleccione lo que desea hacer")
    print(f"1. Ver el listado de equipos")
    print(f"2. Ver la tabla de posiciones de la Liga profesional")
    print(f"3. Ver informacion de un equipo")
    print(f"4. Ver grafica de goles por equipo")
    print(f"5. Cargar dinero")
    print(f"6. Ver el usuario que más dinero apostó")
    print(f"7. Ver el usuario que más veces ganó ")
    print(f"8. Apostar")
    print(f"9. Cerrar sesion")
    print(f"-"*20)

def registrarse(usuarios_diccionario:dict) -> None:
    print(f"-"*20)
    print(f"Proporcione sus datos para crear una nueva cuenta")
    email = str(input("Email: ")) 
    usuario = str(input("Nombre de Usuario: "))
    contraseña = str(input("Contraseña: "))
    hash = pbkdf2_sha256.hash(contraseña)

    for i in usuarios_diccionario:
        if email == i:
            print(f"-"*20)
            print("Usuario ya existente, elija una opcion para continuar")
            return
        if "@" and ".com" not in email:
            print(f"-"*20)
            print("Formato de email incorrecto, elija una opcion para continuar")
            return

    print(f"-"*20)
    print("Usuario creado exitosamente, inicie seion para continuar")
    usuarios_diccionario[email] = [usuario, hash, 0, 00000000, 0] 

def iniciar_sesion(usuarios_diccionario:dict) -> None:
    print(f"-"*20)
    print(f"Inicio de Sesion")
    email = str(input("Email: ")) 
    contraseña = str(input("Contraseña: "))

    for i in usuarios_diccionario:
        # if email == i and pbkdf2_sha256.verify(contraseña, usuarios_diccionario[email][1]):
        if email == i and contraseña == usuarios_diccionario[email][1]:
            print(f"-"*20)
            print(f"Bienvenido {usuarios_diccionario[i][0]}")
            return email

    print(f"-"*20)
    print("Combinacion de usuario y contraseña incorecta, elija una opcion para continuar")
    email = ""
    return email

def opt_bienvenida() -> None:
    opt = str(input("Ingrese una opción: "))
    while opt not in ["1", "2", "3"]: opt = str(input("Ingrese una opción valida: "))
    return opt

def print_bienvenida() -> None:
    print(f"-"*20)
    print(f"1. Iniciar Sesion")
    print(f"2. Registrarse")
    print(f"3. Salir")
    print(f"-"*20)

def transacciones_lista_to_csv(lista_transacciones:list)->None:
    with open("transacciones.csv","a") as transacciones:
        escritura_csv = csv.writer(transacciones)
        escritura_csv.writerows(lista_transacciones)
    
def transacciones_csv_to_listado(transacciones_listado: list) -> None: #EL DOCUMENTO TRANSACCIONES ES UN REGISTRO, NO HACE FALTA LEERLO; HAGO FUNCION PARA ESCRIBIR EN APPEND
    with open("transacciones.csv", newline='', encoding="UTF-8") as transacciones_csv:
        csv_reader = csv.reader(transacciones_csv, delimiter=',')
        next(csv_reader) 
        for fila in csv_reader:
            transacciones_listado.append([fila[0],fila[1],fila[2],float(fila[3])])

def usuarios_csv_to_diccionario(usuarios_diccionario: dict) -> None:
    with open("usuarios.csv", newline='', encoding="UTF-8") as usarios_csv:
        csv_reader = csv.reader(usarios_csv, delimiter=',')
        next(csv_reader) 
        for fila in csv_reader:
            usuarios_diccionario[fila[0]] = [(fila[1]),(fila[2]), float(fila[3]),int(fila[4]), float(fila[5])]
   
def finalizar_programa(lista_transacciones,lista_usuarios):
    transacciones_lista_to_csv(lista_transacciones)
    #ACA IRIA LA FUNCION QUE MODIFICA EL ARCHIVO DE USUARIOS ()
    
def main () -> None:
    TEMPORADAS = 0 
    EQUIPOS = 1
    FIXTURE = 2
    API: dict = {
        "URL": "https://v3.football.api-sports.io/",

        "ENDPOINTS": {
            "temporadas": "leagues?id=128",
            "equipos": "teams?league=128&season=",
            "fixtures": "fixtures?league=128&season=2023",
            "estadisticas": "teams/statistics?league=128&season=2023" + "&team=",
            "predicciones": "predictions?fixture=",
            "planteles": "players?league=128&season=2023" + "&team=",
            "posiciones": "standings?league=128&season="
            },

        "HEADERS": {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "2dd5cdf12ff3a61bb332ad97d9fa2164"#"d6b40bb947b90f57f825bd5d2508b001"
            }
        }
    
    #informacion_api: list = diccionario_api(API)

    lista_transacciones = [] # Lista con los registros que hay que agregar al archivo transacciones
    usuarios_diccionario = {} # email(id):[usuario, contraseña, cantidad_apostada, fecha_última_apuesta, dinero_disponible]
    transacciones_listado = [] # email(id):[fecha, resultado, importe]
    informacion_api =  apixd()  #informacion_api: list = diccionario_api(API)

    email = ""
    usuarios_csv_to_diccionario(usuarios_diccionario)
    transacciones_csv_to_listado(transacciones_listado)

    print(f"Bienvenido")
    print_bienvenida()
    opt = opt_bienvenida()
    while opt != "3":
        if opt == "1":
            email = iniciar_sesion(usuarios_diccionario)
        elif opt == "2":
            registrarse(usuarios_diccionario)

        while email != "":
            print_menu()
            opcion = opt_menu()

            while opcion != "9":
                if opcion == "1":
                    listado_equipos(informacion_api) 
                elif opcion == "2":
                    tabla_posiciones(informacion_api)
                elif opcion == "3":
                    informacion_equipo(informacion_api)
                elif opcion == "4":
                    grafica_goles(informacion_api)
                elif opcion == "5":
                    cargar_dinero(email, usuarios_diccionario, transacciones_listado)
                elif opcion == "6":
                    mayor_apostador(usuarios_diccionario)
                elif opcion == "7":
                    mayor_ganador(usuarios_diccionario,transacciones_listado)
                elif opcion == "8":
                    menu_apuesta(email,usuarios_diccionario,transacciones_listado,informacion_api[1],informacion_api[2])

                print_menu()
                opcion = opt_menu()
            email = ""

        print_bienvenida()
        opt = opt_bienvenida()
        
main()