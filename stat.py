from config import *
from utils import *

char_info = query_char_info(wallet_addr)
print('You have', len(char_info), 'characters')

for id in char_info.keys():
    print("{:7d} {:2d} {:2d} {:6d}".format(int(id), char_info[id]['class'], char_info[id]['level'], int(char_info[id]['xp']/1e18)))