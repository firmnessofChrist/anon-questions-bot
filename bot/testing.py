from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Вставь реальный пароль!
uri = "mongodb+srv://potappv230:bm6D8xG8hpjkvAOc@cluster0.wddm1sm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("✅ Подключение успешно!")
except Exception as e:
    print("❌ Ошибка подключения:")
    print(e)
