
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenditures = []
total_expenditure = 0

# Sample list of items for the dropdown
items_list = ["HM", "BJ", "TJ", "PK", "SM"]

@app.route('/')
def index():
    return render_template('index.html', expenditures=expenditures, items_list=items_list, total_expenditure=total_expenditure)

@app.route('/add_expenditure', methods=['POST'])
def add_expenditure():
    global total_expenditure
    item = request.form['item']
    amount = float(request.form['amount'])

    # Check if the item already exists in expenditures
    for expenditure in expenditures:
        if expenditure['item'] == item:
            expenditure['amount'] += amount
            break
    else:
        expenditures.append({'item': item, 'amount': amount})

    total_expenditure += amount

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
