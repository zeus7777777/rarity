from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy

from config import *
from utils import *

w3 = Web3(Web3.HTTPProvider('https://rpc.ftm.tools/'))
w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

nonce = w3.eth.get_transaction_count(wallet_addr)
height = w3.eth.get_block('latest').number
rm = w3.eth.contract(address=rm_contract_addr, abi=rm_contract_abi)

print('height:', height)
print('gas price:', w3.eth.generate_gas_price())
print('tx count:', w3.eth.get_transaction_count(wallet_addr))

nft_set = retrieve_nft(wallet_addr)
print('You have', len(nft_set), 'characters')

query_char_info(rm, nft_set)