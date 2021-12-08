import sys
import requests
import argparse

def get_total_height():
    parser = argparse.ArgumentParser(description='Macheight Test')

    parser.add_argument('height', type=int,
                        help='Total height in inches adds up')

    args = parser.parse_args()

    if args.height < 0:
        parser.error('height must be greater than zero')

    return args.height

def get_players():
    
    players = requests.get('https://mach-eight.uc.r.appspot.com/')
    
    if players.status_code != 200:
        sys.exit("Error reading players data")
    
    players = players.json()
    
    if not players['values']:
        sys.exit("Players data not defined")
    
    return players['values']

def get_name(p):
    return p['first_name'] + ' ' + p['last_name'] + '(' + p['h_in'] + ')'

def get_group_name(p):
    return '    - ' + get_name(p) + '\n'

def get_main_name(p):
    return get_name(p) + ':\n'

def get_players_group_by_height(players):

    players_group_by_height = {}

    for p in players:
        if not p['h_in'] in players_group_by_height:
            players_group_by_height[p['h_in']] = get_group_name(p)
        else:
            players_group_by_height[p['h_in']] += get_group_name(p)

    return players_group_by_height

def print_players_pairs(height_total, players, players_group_by_height):

    players_pairs = ''
    height_used = {}

    for p in players:
        height = str(height_total - int(p['h_in']))
        if not p['h_in'] in height_used and height in players_group_by_height:
            players_pairs += get_main_name(p) + players_group_by_height[height]
            height_used[height] = True

    print(players_pairs)

def main():

    total_height = get_total_height()

    players = get_players()

    players_group_by_height = get_players_group_by_height(players)

    print_players_pairs(total_height, players, players_group_by_height)

main()
