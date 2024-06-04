import time
from datetime import datetime
import requests
from tabulate import tabulate
from termcolor import colored
import os

os.system('cls')

key = "https://api.binance.com/api/v3/ticker/price?symbol="

#Alterar somente esses parametros.
#Inicio:
simulacao = 50 #simula um valor investido.
investido_bybit = 32200.00 #valor investido na plataforma
investido_binance = 5480.00 #valor investido na plataforma

#Crypto que quer visualizar.
binance_currencies = ["BTCUSDT"  , "DOGEUSDT"   , "PEPEUSDT" , "BNBUSDT"   , "SHIBUSDT"  , "BONKUSDT", "LUNCUSDT"] #Nome da crypto exemplo: "BTCUSDT"
qtd_token_binance = ["2.09816386", "500.00", "1000000.0", "5.16736981", "32944019.62", "239889628.12", "1932298.89304212"] #Quantidade da crypto exemplo: "2.58416386"

bybit_currencies = ["baby-doge-coin", "milady-meme-coin"] #Nome da crypto exemplo: "baby-doge-coin"
qtd_token_bybit = ["17936562870.3773", "1042654703.2596"] #Quantidade da crypto exemplo: "8793656870.3773"
#Fim.

def get_usdt_brl_price(key):
    brl = "USDTBRL"
    url_brl = key + brl
    data = requests.get(url_brl).json()
    price_brl = float(data['price'])
    print(f"{data['symbol']} Preço é ${price_brl}")
    return price_brl

def binance(currencies, qtd_token, key, simu):
    # Binance
    print("\n" + colored("Binance", "red", attrs=["bold"]))
    
    total_value = 0

    table_data = []
    for currency, token in zip(currencies, qtd_token):
        url = key + currency
        data = requests.get(url).json()
        price_usdt = float(data['price'])
        convert = price_usdt * price_brl
        valor_token = float(token) * convert
        total_value += valor_token

        price_usdt_str = "${:.20f}".format(price_usdt).rstrip('0').rstrip('.')
        convert_str = "R${:.20f}".format(convert).rstrip('0').rstrip('.')
        valor_token_str = "R${:.20f}".format(valor_token).rstrip('0').rstrip('.')
        
        sim_value_binance = simu / convert
        sim_value_binance_str = colored("{:.20f}".format(sim_value_binance).rstrip('0').rstrip('.'), "blue")

        table_data.append([currency, price_usdt_str, convert_str, token, valor_token_str, sim_value_binance_str])

    print(tabulate(table_data, headers=["Criptomoeda", "Preço (USDT $)", "Preço (BRL R$)", "Quantidade", "Valor em BRL (R$)", f"Simulação de R${simu}"], numalign="center"))
    
    total_value_str = "R${:.20f}".format(total_value).rstrip('0').rstrip('.')
    diferenca = total_value - investido_binance
    diferenca_str = "R${:.20f}".format(diferenca).rstrip('0').rstrip('.')
    investido_binance_str = "R${:.20f}".format(investido_binance).rstrip('0').rstrip('.')
    if diferenca > 0:
        diferenca_str = colored(diferenca_str, "green")
    else:
        diferenca_str = colored(diferenca_str, "red")
    
    print()
    print("Total R$", total_value_str, "     Diferença:", diferenca_str, "     Investido:", investido_binance_str)

def bybit(name_ticker,token_bybit,simu):
    # Bybit
    print("\n" + colored("Bybit", "red", attrs=["bold"]))

    total_value_bybit = 0

    table_data_bybit = []
    for name, token in zip(name_ticker, token_bybit):
        url_gec = f"https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd"
        response = requests.get(url_gec)
        price_data = response.json()
        convertido = float(price_data[name]['usd']) * float(price_brl)
        valor_token_bybit = float(token) * convertido
        total_value_bybit += valor_token_bybit

        price_usd_str = "${:.20f}".format(price_data[name]['usd']).rstrip('0').rstrip('.')
        convert_str = "R${:.20f}".format(convertido).rstrip('0').rstrip('.')
        valor_token_str = "R${:.20f}".format(valor_token_bybit).rstrip('0').rstrip('.')
        
        sim_value_bybit = simu / convertido
        sim_value_bybit_str = colored("{:.20f}".format(sim_value_bybit).rstrip('0').rstrip('.'), "blue")

        table_data_bybit.append([name.upper(), price_usd_str, convert_str, token, valor_token_str, sim_value_bybit_str])

    print(tabulate(table_data_bybit, headers=["Criptomoeda", "Preço (USD $)", "Preço (BRL R$)", "Quantidade", "Valor em BRL (R$)", f"Simulação de R${simu}"], numalign="center"))
    total_value_bybit_str = "R${:.20f}".format(total_value_bybit).rstrip('0').rstrip('.')
    diferenca_bybit = total_value_bybit - investido_bybit
    diferenca_bybit_str = "R${:.20f}".format(diferenca_bybit).rstrip('0').rstrip('.')
    investido_bybit_str = "R${:.20f}".format(investido_bybit).rstrip('0').rstrip('.')
    if diferenca_bybit > 0:
        diferenca_bybit_str = colored(diferenca_bybit_str, "green")
    else:
        diferenca_bybit_str = colored(diferenca_bybit_str, "red")
    
    print()
    print("Total R$", total_value_bybit_str, "     Diferença:", diferenca_bybit_str, "     Investido:", investido_bybit_str)
    print()

while True:
    print("\nData:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    price_brl = get_usdt_brl_price(key)
    binance(binance_currencies, qtd_token_binance, key, simulacao)
    bybit(bybit_currencies,qtd_token_bybit, simulacao)

    for i in range(120, 0, -5):
        print(f"Próxima execução em {i} segundos...", end="\r")
        time.sleep(5)