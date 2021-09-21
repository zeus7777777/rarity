import threading

from utils import *

market_contract = w3.eth.contract(address=market_contract_addr, abi=market_contract_abi)

count = market_contract.functions.listLength().call()
print('Total characters in market:', count)

idxs = []
prices = []
for i in range(count//100):
    _i, _p = market_contract.functions.listsAt(i*100, 100).call()
    idxs.extend(_i)
    prices.extend(_p)
if count%100!=0:
    _i, _p = market_contract.functions.listsAt((i+1)*100, count%100).call()
d = {}
for i in range(len(idxs)):
    d[idxs[i]] = {'price': prices[i]}

processed = {'c': 0}
def _thread(id):
    c = rm_contract.functions['class'](int(id)).call()
    l = rm_contract.functions.level(int(id)).call()
    x = rm_contract.functions.xp(int(id)).call()
    d[id] = {
        'price': d[id]['price']/1e18,
        'class': c, 
        'level': l, 
        'xp': x/1e18, 
    }
    processed['c'] += 1
    if processed['c']%50 == 0:
        print('read', processed['c'])

threads = []
for id in d.keys():
    t = threading.Thread(target=_thread, args=(id,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

arr = [[k, d[k]['price'], d[k]['class'], d[k]['level'], d[k]['xp']] for k in d.keys()]
arr = sorted(arr, key=lambda x: (-(x[4]+(x[3]-1)*(x[3]-1)*1000), -x[3], -x[1]))

with open('result.txt', 'w') as f:
    for i in range(len(arr)):
        f.write('id: {:7d}, lv: {:3d}, xp: {:6d}, price: {:8d}\n'.format(int(arr[i][0]), int(arr[i][3]), int(arr[i][4]), int(arr[i][1])))
