# -*- coding: cp1251 -*-






def print_dict(d, prefix=""): 
   
    for k, v in d.items(): 
        if isinstance(v, dict): 
            print_dict(v, f"{prefix}{k} ") 
        elif isinstance(v, list): 
            for i in v: 
                print_dict(i, f"{prefix}{k} ") 
        else: 
            print(f"{prefix}{k}: {v} ") 
    



data = {
"address": "0x544444444444",
"ETH": {
"balance": 444,
"totalIn": 444,
"totalOut": 4
},
"count_txs": 2,
"tokens": [
{
"fst_token_info": {
"address": "0x44444",
"name": "fdf",
"decimals": 0,
"symbol": "dsfdsf",
"total_supply": "3228562189",
"owner": "0x44444",
"last_updated": 1519022607901,
"issuances_count": 0,
"holders_count": 137528,
"price": False
},
"balance": 5000,
"totalIn": 0,
"total_out": 0
},
{
"sec_token_info": {
"address": "0x44444",
"name": "ggg",
"decimals": "2",
"symbol": "fff",
"total_supply": "250000000000",
"owner": "0x44444",
"last_updated": 1520452201,
"issuances_count": 0,
"holders_count": 20707,
"price": False
},
"balance": 500,
"totalIn": 0,
"total_out": 0
}
]
}
print_dict(data)
print("#####################################################################################")
data["ETH"]['total_diff']=100
print_dict(data)
print("#####################################################################################")
data["tokens"][0]["fst_token_info"]['name']='doge';
print_dict(data)
print("#####################################################################################")
data['ETH']['totalOut'] = data['tokens'][1].pop('total_out') 
print_dict(data)

print("#####################################################################################")
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
print_dict(data)

