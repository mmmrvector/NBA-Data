import urllib.parse
import urllib.request
import string
from bs4 import BeautifulSoup
import csv
import re
import player

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 ', 'refer':'link' }

def get_response(url):
    req = urllib.request.Request(url, headers=headers)
    data = urllib.request.urlopen(req).read()
    data = data.decode('utf-8', 'ignore')
    return data

#获得球员信息
def get_player(player_number):
    pp = player.Player()

    net_addr = "http://www.stat-nba.com/player/" + str(player_number) + ".html"
    url = urllib.parse.quote(net_addr, safe=string.printable)
    data = get_response(url)
    soup = BeautifulSoup(data, features="html.parser")

    #获取球员基本信息
    player_info = soup.select('.playerinfo')
    player_info = player_info[0].select('.detail')[0]
    for row in player_info.select('.row'):
        row_content = row.select('.column')[0].get_text()
        if row_content == '全　　名:':
            pp.name = row.get_text().replace(row_content, '')
        if row_content == '位　　置:':
            pp.position = row.get_text().replace(row_content, '')
        if row_content == '身　　高:':
            pp.height = row.get_text().replace(row_content, '')
        if row_content == '体　　重:':
            pp.weight = row.get_text().replace(row_content, '')
        if row_content == '出生日期:':
            pp.date_of_birth = row.get_text().replace(row_content, '')
        if row_content == '出生城市:':
            pp.city = row.get_text().replace(row_content, '')
        if row_content == '当前薪金:':
            pp.current_payment = row.get_text().replace(row_content, '')
            pattern = re.compile(r'([0-9]+)万美元')
            pp.current_payment = pattern.findall(pp.current_payment)[0]

    #获取球员平均数据
    rows = []
    table = soup.find('table', id = 'stat_box_avg')
    for trs in table.select('tr'):
        row = []
        for td in trs.select('td'):
            td_class_content = td.get('class')
            if td_class_content != None:
                row.append(td.get_text())
        if row != None and len(row) != 0 :
            #rows.append(row)
            class_row = player.avg_stat_row(row)
            rows.append(class_row)
    pp.avg_stats.append_rows(rows)

    #获取球员进阶数据
    rows = []
    table = soup.find('table', id = 'stat_box_advanced_basic')
    for trs in table.select('tr'):
        row = []
        for td in trs.select('td'):
            td_class_content = td.get('class')
            if td_class_content != None:
                row.append(td.get_text())
        if row != None and len(row) != 0:
            # rows.append(row)
            class_row = player.advanced_basic_row(row)
            rows.append(class_row)
    pp.advanced_basic_stats.append_rows(rows)

    return pp

#由球员名字获取球员编号
def get_player_number_from_name(player_name):
    net_addr = "http://www.stat-nba.com/playerList.php?name="+player_name.replace(' ', '+')
    url = urllib.parse.quote(net_addr, safe=string.printable)
    data = get_response(url)
    soup = BeautifulSoup(data, features="html.parser")
    #只选择第一个球员
    first_player = soup.select('.playerList')[0]
    player_number = first_player.find_all('a')[0].get('href')
    pattern = re.compile(r'\./player/([0-9]+)\.html')
    player_number = pattern.findall(player_number)[0]
    return player_number

#由球队名获取球员编号，返回球员编号数组
def get_player_numbers_from_team_name(team_name):
    net_addr = "http://www.stat-nba.com/team/" + team_name + ".html"
    url = urllib.parse.quote(net_addr, safe=string.printable)
    data = get_response(url)
    soup = BeautifulSoup(data, features="html.parser")
    div = soup.select('#stat_box_team')[0]
    table = div.select('.stat_box')[0]
    player_numbers = []
    for trs in table.select('tr'):
        for td in trs.select('td'):
            td_class_content = td.get('class')
            if td_class_content != None and 'player_name' in td_class_content:
                try:
                    player_number = td.a.get('href')
                    pattern = re.compile(r'/player/([0-9]+)\.html')
                    player_number = pattern.findall(player_number)[0]
                    player_numbers.append(int(player_number))
                except(Exception):
                    print("not player data")
    return player_numbers


'''''
#写入csv文件
headerss = ['season', 'tm', 'g', 'gs', 'mp', 'fgper', 'fg', 'fga', 'threepper', 'threep', 'threepa', 'ftper', 'ft', 'fta', 'trb', 'orb', 'drb', 'ast', 'stl', 'blk',
           'tov', 'pf', 'pts', 'w', 'l']
with open('data.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headerss)
    f_csv.writerows(rows)
'''''