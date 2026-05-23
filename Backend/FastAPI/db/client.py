from pymongo import MongoClient

#Base de datos local

# db_cliente = MongoClient().local

# Base de datos remota

db_cliente = MongoClient(
    "mongodb+srv://test:test@cluster0.yglq6cz.mongodb.net/?appName=Cluster0").test