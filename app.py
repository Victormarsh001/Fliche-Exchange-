from flask import Flask, render_template, request

app = Flask(__name__)

tokens = [
  {'logo': '/static/avax.jpeg', 'name':'AvaCoin'},
  
  {'logo': '/static/bnb.jpeg', 'name':'Binance'},
  
  {'logo': '/static/btcash.jpeg', 'name':'Bitcoin Cash'},
  
  {'logo': '/static/btcoin.jpeg', 'name':'Bitcoin'},
  
  {'logo': '/static/celo.jpeg', 'name':'Celo'},
  
  {'logo': '/static/dodge.jpeg', 'name':'Dodge Coin'},
  
  {'logo': '/static/eth.jpeg', 'name':'Ethereum'},
  
  {'logo': '/static/ftm.jpeg', 'name':'Fantom'},
  
  {'logo': '/static/ltc.jpeg', 'name':'Litecoin'},
  
  {'logo': '/static/matic.jpeg', 'name':'Matic'},
  
  {'logo': '/static/near.jpeg', 'name':'Near'},
  
  {'logo': '/static/not.jpeg', 'name':'Notcoin'},
  
  {'logo': '/static/ton.jpeg', 'name':'Toncoin'},
  
  {'logo': '/static/trc.jpeg', 'name':'Tether(Trc20)'},
  
  {'logo': '/static/trx.jpeg', 'name':'Tron'},
  
  {'logo': '/static/xrp.jpeg', 'name':'Ripple(XRP)'},
  
  {'logo': '/static/zec.jpeg', 'name':'Zecoin'},
  
]

@app.route('/')
def hello_world():
  return render_template('trade.html', coin=tokens)

@app.route('/trade')
def trade():
  token = request.args.get('item')
  logo = request.args.get('img')
  
  return render_template('trad.html', item=token, img=logo)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)