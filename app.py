from flask import Flask, render_template, request, redirect, url_for
from config import get_database
from models.income import Income
from models.expense import Expense
from models.budget import Budget

app = Flask(__name__)
db = get_database()

income = Income(db)
expense = Expense(db)
budget = Budget(db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/income')
def show_income():
    incomes = income.get_incomes()
    return render_template('income.html', incomes=incomes)

@app.route('/expense')
def show_expense():
    expenses = expense.get_expenses()
    return render_template('expense.html', expenses=expenses)

@app.route('/budget')
def show_budget():
    budgets = budget.get_budgets()
    return render_template('budget.html', budgets=budgets)

@app.route('/add_income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        amount = request.form['amount']
        source = request.form['source']
        date = request.form['date']
        income.add_income(amount, source, date)
        return redirect(url_for('show_income'))
    return render_template('add_income.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']
        expense.add_expense(amount, category, date)
        return redirect(url_for('show_expense'))
    return render_template('add_expense.html')

@app.route('/set_budget', methods=['GET', 'POST'])
def set_budget():
    if request.method == 'POST':
        category = request.form['category']
        amount = request.form['amount']
        budget.set_budget(category, amount)
        return redirect(url_for('show_budget'))
    return render_template('set_budget.html')

if __name__ == '__main__':
    app.run(debug=True)
