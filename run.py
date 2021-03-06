from flask import Flask, render_template

app = Flask(__name__)

burgers = [
['Classic Burger', '$4.99'],
['Cheese Burger', '$5.99'],
['Chicken Burger', '$5.99'],
['Double Burger', '$6.99']
]

drinks = [
['Cola', '$0.99'],
['Ginger Ale', '$1.99'],
['Sprite', '$0.99'],
['Coffee', '$4.50']
]

sides = [
['Fries', '$1.99'],
['Onion Rings', '$1.99'],
['Chicken Nuggets', '$3.99'],
['Salad', '1.99']
]



@app.route('/')

def index():
    return render_template('index.html', disclaimer='may contain traces of nuts', burgers=burgers, drinks=drinks, sides=sides)


@app.route('/order')
def order():
    return render_template('order.html')
