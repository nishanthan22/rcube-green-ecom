import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI and Database name from environment variables
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")  # Ensure DB_NAME is set in the .env file

if not db_name:
    raise ValueError("No database name specified in the .env file. Please add DB_NAME to your .env file.")

# Create a MongoClient
client = MongoClient(mongo_uri)

# Access the specified database
db = client[db_name]


def create_collection(collection_name):
    """Create a collection explicitly if it doesn't exist."""
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
        print(f"Collection '{collection_name}' created.")
    else:
        print(f"Collection '{collection_name}' already exists.")


def get_collection(collection_name):
    """Retrieve a collection by name."""
    return db[collection_name]


def check_connection():
    """Check if the connection to MongoDB is working."""
    try:
        # Perform an operation to check the connection
        server_info = client.server_info()  # Will throw an exception if the server is not available
        print("MongoDB connection is working.")
        return True
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return False


# Check the connection when running this script
if __name__ == "__main__":
    if check_connection():
        print("Connection to MongoDB is successful.")
    else:
        print("Connection to MongoDB failed.")
