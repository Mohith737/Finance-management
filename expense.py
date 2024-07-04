from pymongo import MongoClient

class Expense:
    def __init__(self, db):
        self.collection = db["expenses"]

    def add_expense(self, amount, category, date):
        expense_data = {
            "amount": amount,
            "category": category,
            "date": date
        }
        self.collection.insert_one(expense_data)

    def get_expenses(self):
        return list(self.collection.find())
