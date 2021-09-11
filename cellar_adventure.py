import sim.cellar
import config
from utils import *

char_info = query_char_info(config.wallet_addr)
print('You have', len(char_info), 'characters')

adventure_id = [id for id in char_info.keys() if char_info[id]
                ['cellar_time_pass']]
print(len(adventure_id), 'can adventure()')

for id in adventure_id:
    r = sim.cellar.sim_reward(char_info[id]['attr'][0], char_info[id]['attr'][1],
                              char_info[id]['attr'][2], char_info[id]['level'], char_info[id]['class'])
    if r > 0 and char_info[id]['cellar_time_pass']:
        print('Send', id, 'to The Cellar .adventure(), reward:', r)
        adventure_tx = cellar_contract.functions.adventure(int(id)).buildTransaction({
            'chainId': 250,
            'gas': 200000,
            'gasPrice': int(w3.eth.generate_gas_price()*1.05) if predefined_gas == 0 else predefined_gas,
            'nonce': nonce
        })
        print(adventure_tx)
        signed_tx = w3.eth.account.sign_transaction(
            adventure_tx, private_key=wallet_private_key)
        print(signed_tx.hash)
        w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        nonce += 1
