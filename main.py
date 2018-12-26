import crawler
import json

lakers_players = ['Lonzo Ball', 'Michael Beasley', 'Isaac Bonga', 'Kentavious Caldwell-Pope', 'Alex Caruso', 'Tyson Chandler',
                  'Josh Hart', 'Brandon Ingram', 'LeBron James', 'Kyle Kuzma', 'JaVale McGee', 'Svi Mykhailiuk', 'Rajon Rondo',
                  'Lance Stephenson', 'Moritz Wagner', 'Johnathan Williams', 'Ivica Zubac']


James = crawler.get_player(1862)
print(James.date_of_birth)

for player_name in lakers_players:
    player_number = crawler.get_player_number_from_name(player_name)
    pp = crawler.get_player(player_number)
    ss = json.dumps(pp, default=lambda  obj:obj.__dict__, ensure_ascii=False)
    #ss2 = json.dumps(pp.avg_stats.data[0], default=lambda  obj:obj.__dict__, ensure_ascii=False)
    print(ss)