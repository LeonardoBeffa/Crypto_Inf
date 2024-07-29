# Análise de Investimentos em Criptomoedas

Este script fornece uma análise comparativa do valor de investimentos em criptomoedas nas plataformas Binance e Bybit. Ele recupera informações sobre o preço atual das criptomoedas e calcula o valor total dos investimentos em reais (BRL) com base em uma simulação de valor investido.

## Funcionalidade

1. **Recuperação de Dados:**
   - Obtém o preço das criptomoedas em dólares (USD) e converte para reais (BRL) usando a API da Binance e CoinGecko.
   - Utiliza a API da Binance para obter preços das criptomoedas listadas e a API da CoinGecko para as criptomoedas da Bybit.

2. **Simulação de Investimento:**
   - Permite simular o valor investido em diferentes criptomoedas, exibindo o valor atual dos tokens e a diferença em relação ao valor investido.

3. **Exibição dos Resultados:**
   - Apresenta os dados em tabelas formatadas, mostrando o preço das criptomoedas em USD e BRL, a quantidade de tokens, o valor total em BRL e a simulação do valor investido.
   - Exibe a diferença entre o valor total atual e o valor investido, com destaque em verde se positivo e vermelho se negativo.

## Como Usar

1. **Configuração Inicial:**
   - Modifique as variáveis `simulacao`, `investido_bybit` e `investido_binance` com os valores desejados.
   - Atualize as listas `binance_currencies`, `qtd_token_binance`, `bybit_currencies` e `qtd_token_bybit` com as criptomoedas e quantidades desejadas.

2. **Execução:**
   - Execute o script em um ambiente que suporte Python e que tenha as bibliotecas necessárias instaladas (`requests`, `tabulate`, `termcolor`).
   - O script executará a cada 120 segundos, exibindo as informações atualizadas.

## Dependências

- `requests`: Biblioteca para fazer requisições HTTP.
- `tabulate`: Biblioteca para formatar tabelas.
- `termcolor`: Biblioteca para colorir a saída no terminal.
- `os`: Utilizada para limpar o terminal.

## Exemplo de Saída

```plaintext
Data: 29/07/2024 14:30:00

Binance
Criptomoeda  Preço (USDT $)  Preço (BRL R$)     Quantidade       Valor em BRL (R$)   Simulação de R$50
BTCUSDT      $30,000.0000    R$150,000.0000     2.09816386       R$314,527.1000      R$0.0000
DOGEUSDT     $0.0750         R$0.3750           500.00           R$187.5000          R$133.3333
...

Total R$314,527.1000     Diferença: R$264,527.1000     Investido: R$50,000.0000

Bybit
Criptomoeda       Preço (USD $)  Preço (BRL R$)  Quantidade            Valor em BRL (R$)   Simulação de R$50
baby-doge-coin    $0.0005        R$0.0025        17,936,562,870.3773   R$44,484,153.1175   R$0.0000
milady-meme-coin  $0.0020        R$0.0100        1,042,654,703.2596    R$10,426,547.0259   R$5,000.0000
...

Total R$54,910,700.1434     Diferença: R$20,700.1434     Investido: R$32,200.0000
