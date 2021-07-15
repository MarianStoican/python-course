import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

stage_table = soup.find(class_='clasament_general white-shadow etape_meciuri')


print("-------------------------------------------------------------------------------------------------")

teams_rows_etapa1 = stage_table.findAll(class_='echipa-etapa-1')
teams_rows_etapa2 = stage_table.findAll(class_='echipa-etapa-2')


def scrap(teams_rows):
    teams = []
    for team in teams_rows:
        teams_cell = team.find('a')
        team_name = teams_cell.find(class_='hiddenMobile').text.strip()
        teams.append(team_name)
    return teams


teams1 = scrap(teams_rows_etapa1)
teams2 = scrap(teams_rows_etapa2)

for i in range(0, len(teams2)):
    print(teams1[i] + '  -  ' + teams2[i])
