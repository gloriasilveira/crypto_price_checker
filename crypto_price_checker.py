# crypto_price_checker.py

import requests
import json
from tabulate import tabulate
from datetime import datetime

# Step 1: Get current coin values
####################################
BTC_response = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
for coin in BTC_response.json():
    btc_current_price = float(coin["price_usd"])
    btc_change = float(coin["percent_change_24h"])

ETH_response = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
for coin in ETH_response.json():
    eth_current_price = float(coin["price_usd"])
    eth_change = float(coin["percent_change_24h"])

LTC_response = requests.get('https://api.coinmarketcap.com/v1/ticker/litecoin/')
for coin in LTC_response.json():
    ltc_current_price = float(coin["price_usd"])
    ltc_change = float(coin["percent_change_24h"])

LEND_response = requests.get('https://api.coinmarketcap.com/v1/ticker/ethlend/')
for coin in LEND_response.json():
    lend_current_price = float(coin["price_usd"])
    lend_change = float(coin["percent_change_24h"])

POE_response = requests.get('https://api.coinmarketcap.com/v1/ticker/poet/')
for coin in POE_response.json():
    poe_current_price = float(coin["price_usd"])
    poe_change = float(coin["percent_change_24h"])

VOISE_response = requests.get('https://api.coinmarketcap.com/v1/ticker/voisecom/')
for coin in VOISE_response.json():
    voise_current_price = float(coin["price_usd"])
    voise_change = float(coin["percent_change_24h"])

ONION_response = requests.get('https://api.coinmarketcap.com/v1/ticker/deeponion/')
for coin in ONION_response.json():
    onion_current_price = float(coin["price_usd"])
    onion_change = float(coin["percent_change_24h"])

# Monero
XMR_response = requests.get('https://api.coinmarketcap.com/v1/ticker/monero/')
for coin in XMR_response.json():
    xmr_current_price = float(coin["price_usd"])
    xmr_change = float(coin["percent_change_24h"])

DASH_response = requests.get('https://api.coinmarketcap.com/v1/ticker/dash/')
for coin in DASH_response.json():
    dash_current_price = float(coin["price_usd"])
    dash_change = float(coin["percent_change_24h"])

ADA_response = requests.get('https://api.coinmarketcap.com/v1/ticker/cardano/')
for coin in ADA_response.json():
    ada_current_price = float(coin["price_usd"])
    ada_change = float(coin["percent_change_24h"])

PHORE_response = requests.get('https://api.coinmarketcap.com/v1/ticker/phore/')
for coin in PHORE_response.json():
    phore_current_price = float(coin["price_usd"])
    phore_change = float(coin["percent_change_24h"])

XSH_response = requests.get('https://api.coinmarketcap.com/v1/ticker/shield-xsh/')
for coin in XSH_response.json():
    xsh_current_price = float(coin["price_usd"])
    xsh_change = float(coin["percent_change_24h"])

XRP_response = requests.get('https://api.coinmarketcap.com/v1/ticker/ripple/')
for coin in XRP_response.json():
    xrp_current_price = float(coin["price_usd"])
    xrp_change = float(coin["percent_change_24h"])

XLM_response = requests.get('https://api.coinmarketcap.com/v1/ticker/stellar/')
for coin in XLM_response.json():
    xlm_current_price = float(coin["price_usd"])
    xlm_change = float(coin["percent_change_24h"])

LSK_response = requests.get('https://api.coinmarketcap.com/v1/ticker/lisk/')
for coin in LSK_response.json():
    lsk_current_price = float(coin["price_usd"])
    lsk_change = float(coin["percent_change_24h"])

CAT_response = requests.get('https://api.coinmarketcap.com/v1/ticker/bitclave/')
for coin in CAT_response.json():
    cat_current_price = float(coin["price_usd"])
    cat_change = float(coin["percent_change_24h"])
  
# Get current time object
current_time = str(datetime.now())

# Step 2: Display Prices to User
##################################

print '======================================================================'
print '                       Current Prices                                 '
print '======================================================================'
print '            Time checked: ' + current_time + '                        '
print '======================================================================'

print tabulate([['BTC', btc_change, btc_current_price], ['ETH', eth_change, eth_current_price], ['LTC', ltc_change, ltc_current_price], ['LEND', lend_change, lend_current_price], ['POE', poe_change, poe_current_price], ['VOISE', voise_change, voise_current_price], ['ONION', onion_change, onion_current_price], ['Monero', xmr_change, xmr_current_price], ['DASH', dash_change, dash_current_price], ['ADA', ada_change, ada_current_price], ['PHORE', phore_change, phore_current_price], ['Shield/XSH', xsh_change, xsh_current_price], ['Ripple/XRP', xrp_change, xrp_current_price], ['Stellar/XLM', xlm_change, xlm_current_price], ['Lisk/LSK', lsk_change, lsk_current_price], ['Bitclave/CAT', cat_change, cat_current_price]], headers=[' ', '% Change Last 24hrs', 'Current Price'])

print '======================================================================'
