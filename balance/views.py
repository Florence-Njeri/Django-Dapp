from django.shortcuts import render
from web3 import Web3

def index(request):
    contract_address = 'YOUR_CONTACT_ADDRESS'
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/INFRA_API_KEY'))
    balance_wei = w3.eth.get_balance(contract_address)
    balance_eth = w3.from_wei(balance_wei, 'ether')

    return render(request, 'index.html', {'balance': balance_eth})



