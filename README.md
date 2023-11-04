from pymongo import MongoClient

class CustomMongoClient:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
    
    def get_client(self):
        return self.client

# Créez une instance de CustomMongoClient au niveau de votre application
custom_client = CustomMongoClient()

# Utilisez custom_client.get_client() pour obtenir le client MongoDB
# ...

# À la fin de votre application, vous pouvez fermer la connexion si nécessaire
custom_client.get_client().close()