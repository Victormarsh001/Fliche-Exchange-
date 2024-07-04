import random
from flask import Flask, render_template, request

app = Flask(__name__)
rev = ["Ava @ Japan: Great app for crypto trading",
"Liam @ France: Easy to use, love the features",
"Noah @ Brazil: Awesome for beginners",
"Eva @ Germany: Great for cryptocurrency exchange",
"Lucas @ Australia: Excellent performance",
"Mia @ Italy: So easy to navigate",
"Oliver @ Spain: Fantastic for trading",
"Charlotte @ China: Love the updates",
"William @ India: Best app for crypto",
"Amelia @ Russia: Great support team",
"George @ South Africa: Super fast transactions",
"Harriet @ South Korea: Amazing features",
"Benjamin @ Mexico: So intuitive",
"Alice @ Turkey: Love the UI",
"Henry @ Poland: Excellent app",
"Eleanor @ Indonesia: Great job",
"Alexander @ Netherlands: Super impressed",
"Sophia @ Switzerland: Fantastic",
"Elijah @ Sweden: Love it",
"Emily @ Greece: Great app",
"James @ Belgium: Super useful",
"Abigail @ Austria: Excellent",
"Gabriel @ Romania: Awesome",
"Julia @ Portugal: Love the features",
"Michael @ Czech Republic: Great performance",
"Hannah @ Hungary: Fantastic app",
"Daniel @ Norway: Super impressed",
"Isabella @ Denmark: Love the design",
"Logan @ Finland: Excellent support",
"Sophie @ New Zealand: Great job"]


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
  revs = [i for i in random.sample(rev, 10)]
  
  
  value = request.args.get('amount')
  
  return render_template('profile.html', revs=revs, coin=tokens, value=value)

@app.route('/trade')
def trade():
  token = request.args.get('item')
  logo = request.args.get('img')
  
  return render_template('trad.html', item=token, img=logo)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)