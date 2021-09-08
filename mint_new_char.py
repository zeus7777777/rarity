from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy

from config import *
from utils import *

summon_cnt = [0]*11
assert(len(summon_cnt) == 11)

w3 = Web3(Web3.HTTPProvider('https://rpc.ftm.tools/'))
w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

nonce = w3.eth.get_transaction_count(wallet_addr)
rm = w3.eth.contract(address=rm_contract_addr, abi=rm_contract_abi)

print('gas price:', w3.eth.generate_gas_price())
if predefined_gas != 0:
    print('use predefined gas instead:', predefined_gas)
print('tx count:', w3.eth.get_transaction_count(wallet_addr))

input('press enter to continue')

for i in range(len(summon_cnt)):
    for _ in range(summon_cnt[i]):
        summon_tx = rm.functions.summon(i+1).buildTransaction({
            'chainId': 250,
            'gas': 200000,
            'gasPrice': int(w3.eth.generate_gas_price()*1.05) if predefined_gas == 0 else predefined_gas,
            'nonce': nonce
        })
        print(summon_tx)

        signed_tx = w3.eth.account.sign_transaction(
            summon_tx, private_key=wallet_private_key)
        print(signed_tx.hash)
        w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        nonce += 1
