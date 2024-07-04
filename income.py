from pymongo import MongoClient

class Income:
    def __init__(self, db):
        self.collection = db["incomes"]

    def add_income(self, amount, source, date):
        income_data = {
            "amount": amount,
            "source": source,
            "date": date
        }
        self.collection.insert_one(income_data)

    def get_incomes(self):
        return list(self.collection.find())
