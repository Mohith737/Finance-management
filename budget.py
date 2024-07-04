from pymongo import MongoClient

class Budget:
    def __init__(self, db):
        self.collection = db["budgets"]

    def set_budget(self, category, amount):
        budget_data = {
            "category": category,
            "amount": amount
        }
        self.collection.update_one(
            {"category": category},
            {"$set": budget_data},
            upsert=True
        )

    def get_budgets(self):
        return list(self.collection.find())
