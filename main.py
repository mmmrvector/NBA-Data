import crawler
import json

lakers_players = ['Lonzo Ball', 'Michael Beasley', 'Isaac Bonga', 'Kentavious Caldwell-Pope', 'Alex Caruso', 'Tyson Chandler',
                  'Josh Hart', 'Brandon Ingram', 'LeBron James', 'Kyle Kuzma', 'JaVale McGee', 'Svi Mykhailiuk', 'Rajon Rondo',
                  'Lance Stephenson', 'Moritz Wagner', 'Johnathan Williams', 'Ivica Zubac']


'''
已知球队内所有球员名字，得到球员数据
'''
for player_name in lakers_players:
    player_number = crawler.get_player_number_from_name(player_name)
    pp = crawler.get_player(player_number)
    ss = json.dumps(pp, default=lambda  obj:obj.__dict__, ensure_ascii=False)
    #ss2 = json.dumps(pp.avg_stats.data[0], default=lambda  obj:obj.__dict__, ensure_ascii=False)
    print(ss)

'''
由球队名得到球员数据
'''
team_name = ['ATL', 'CHI', 'BKN']
for team in team_name:
    player_numbers = crawler.get_player_numbers_from_team_name(team)
    print(team)
    for player_number in player_numbers:
        pp = crawler.get_player(player_number)
        ss = json.dumps(pp, default=lambda obj: obj.__dict__, ensure_ascii=False)
        print(ss)