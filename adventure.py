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

filter_nft_adventure(rm, nft_set)
print(len(nft_set), 'can adventure()')

input('press enter to start adventure()')

for id in nft_set:
    adventure_tx = rm.functions.adventure(int(id)).buildTransaction({
        'chainId': 250,
        'gas': 200000,
        'gasPrice': int(w3.eth.generate_gas_price()*1.05),
        'nonce': nonce
    })
    print('adventure(' + str(id) + ')')
    print(adventure_tx)

    signed_tx = w3.eth.account.sign_transaction(
        adventure_tx, private_key=wallet_private_key)
    print(signed_tx.hash)
    w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    nonce += 1
