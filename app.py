import sys
import requests
import argparse

def parse_args():
    """Parse and validate the input args."""

    parser = argparse.ArgumentParser(description='Macheight Test')

    parser.add_argument('total_height', type=int,
                        help='Total height in inches adds up')

    parser.add_argument('--print_height', action='store_true',
                        help='Print height of each player')

    args = parser.parse_args()

    if args.total_height <= 0:
        parser.error('total_height must be greater than zero')

    return args

def get_players():
    """Get all players from the repo and return them in a list.

    For simplicity, we assume that each player have all attributes
    well-defined. Therefore, we don't validate them.
    """

    players = requests.get('https://mach-eight.uc.r.appspot.com/')

    if players.status_code != 200:
        sys.exit("Error reading players data")

    players = players.json()

    if not players['values']:
        sys.exit("Players data not defined")

    return players['values']

def get_name(p, print_height):
    """Return the player name together with the height for debugging purpose."""

    return (p['first_name'] + ' ' + p['last_name'] +
            ('(' + p['h_in'] + ')' if print_height else ''))

def get_players_names(players, print_height):
    """Return a dictionary which maps indexes with players names.

    Complexity: O(n)
    """

    names = {}
    idx = 0
    for p in players:
        names[str(idx)] = get_name(p, print_height)
        idx += 1

    return names

def get_players_group_by_height(players):
    """Group all players based on the height in inches.

    Return:
    Dictionary where each key corresponds to players height and
    the values correpond to a concatenated string of indexes, where
    each index corresponds to a particular player.

    Complexity: O(n)
    """

    players_group_by_height = {}
    idx = 0
    for p in players:
        if not p['h_in'] in players_group_by_height:
            players_group_by_height[p['h_in']] = '-' + str(idx) + ' '
        else:
            players_group_by_height[p['h_in']] += '-' + str(idx) + ' '
        idx += 1

    return players_group_by_height

def print_players_pairs(total_height, players, players_group_by_height, names):
    """Print a list of all pairs of players whose height adds up to total_height

    Keyword arguments:
    total_height -- integer value

    Complexity: O(n)
    """

    # The following block has a complexity of O(n) where n is the number of
    # players
    players_pairs_tmp = ''
    height_used = {} # avoid duplicated pairs
    idx = 0
    for p in players:
        height = str(total_height - int(p['h_in']))
        if not p['h_in'] in height_used and height in players_group_by_height:
            players_pairs_tmp += str(idx) + ' ' + players_group_by_height[height]
            height_used[height] = True
        idx += 1

    # The split built-in function has a complexity of O(m) where m is the number
    # of characters in the string. For the current case, m can be represented as
    # k*n, where k is (to some extend) the number of digits of each index
    # representing each player, and n in the number of players. For the case of
    # the Big-O notation, the constant k can be left out, leading to a
    # complexity of O(n).
    players_pairs_tmp = players_pairs_tmp.split()

    # The following block has a complexity of O(n) where n is roughly the number
    # of players
    players_pairs = ''
    for p in players_pairs_tmp:
        if p[0] != '-':
            p1 = p
            continue
        # The following if-statement avoids pairing a player with himself
        if '-' + p1 != p:
            players_pairs += names[p1] + ' - ' + names[p[1:]] + '\n'

    if players_pairs == '':
        print('No matches found')
    else:
        print(players_pairs)

def main(total_height, print_height):
    """Print a list of all pairs of players whose height adds up to total_height

    Keyword arguments:
    total_height -- integer value

    Edge cases considered:
    - Avoid duplicated pairs of players.
    - Avoid pairing a player with himself.

    Complexity:
    Each block of code has a complexity of n. If we join the complexity of all
    blocks, it would lead to n + n + n + ... = kn, with k << n. Therefore,
    k can be left out, leading to a complexity of O(n).
    """

    players = get_players()

    # complexity O(n)
    names = get_players_names(players, print_height)

    # complexity O(n)
    players_group_by_height = get_players_group_by_height(players)

    # complexity O(n)
    print_players_pairs(total_height, players, players_group_by_height, names)

if __name__ == '__main__':
    """Command line call."""

    args = parse_args()
    main(args.total_height, args.print_height)
