from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import subprocess

# Global DB URI
db_uri = None

def prompt_connection_uri():
    global db_uri
    while True:
        uri = input("\nPrompt the MongoDB connection string [default: mongodb://localhost:27017]: ").strip()
        db_uri = uri or "mongodb://localhost:27017"
        print(f"Trying to connect to {db_uri}...")
        if test_connection():
            print(f"✔ Connected to MongoDB at {db_uri}")
            break
        else:
            print("✖ Connection failed. Please try again.\n")

# Test MongoDB connection
def test_connection():
    try:
        client = MongoClient(db_uri, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        return True
    except ConnectionFailure as e:
        return False

# Perform a MongoDB dump using mongodump
def dump_mongo():
    db_name = input("Enter the name of the database to back up: ").strip()
    output_dir = input("Enter the output directory [default: ./dump]: ").strip() or "./dump"
    try:
        subprocess.run(['mongodump', '--uri', db_uri, '--db', db_name, '--out', output_dir], check=True)
        print("✔ Database dump completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"✖ Error during database dump: {e}")

# Restore MongoDB from a backup using mongorestore
def restore_mongodb():
    db_name = input("Enter the name of the database to restore: ").strip()
    backup_path = input(f"Enter the backup path [default: ./dump/{db_name}]: ").strip() or f"./dump/{db_name}"
    try:
        subprocess.run(["mongorestore", "--uri", db_uri, "--db", db_name, backup_path], check=True)
        print(f"✔ Restore completed from {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"✖ Restore failed: {e}")

# Visualize collections in a DB
def list_collections():
    db_name = input("Enter the name of the database: ").strip()
    try:
        client = MongoClient(db_uri)
        db = client[db_name]
        collections = db.list_collection_names()
        if collections:
            print(f"✔ Collections in database '{db_name}':")
            for col in collections:
                print(f"  - {col}")
        else:
            print(f"⚠ No collections found in database '{db_name}'.")
    except Exception as e:
        print(f"✖ Error retrieving collections: {e}")

# Create database and collection
def create_database():
    db_name = input("Enter the name of the new database: ").strip()
    collection_name = input("Enter the name of a collection to create: ").strip()
    
    if not db_name or not collection_name:
        print("✖ Database and collection names cannot be empty.")
        return

    try:
        client = MongoClient(db_uri)
        db = client[db_name]
        collection = db[collection_name]
        collection.insert_one({"created": True})
        print(f"✔ Database '{db_name}' and collection '{collection_name}' created successfully.")
    except Exception as e:
        print(f"✖ Failed to create database: {e}")

# Show list of databases on the server
def list_databases():
    try:
        client = MongoClient(db_uri)
        db_list = client.list_database_names()
        if db_list:
            print("✔ Databases available on the server:")
            for db_name in db_list:
                print(f"  - {db_name}")
        else:
            print("⚠ No databases found on the server.")
    except Exception as e:
        print(f"✖ Failed to list databases: {e}")

# Main menu with match-case
def main():
    print("Welcome on the MongoTools App")
    prompt_connection_uri()  # Ask for and test connection

    while True:
        print("\n====== MongoTools Menu ======")
        print("1. Test MongoDB Connection")
        print("2. Dump Database")
        print("3. Restore Database")
        print("4. Check Collections")
        print("5. Show List of Databases")
        print("6. Exit Program")
        choice = input("Select an option [1-6]: ").strip()

        try:
            match choice:
                case "1":
                    if test_connection():
                        print(f"✔ Connection to {db_uri} successful.")
                    else:
                        print("✖ Connection failed.")
                case "2":
                    dump_mongo()
                case "3":
                    restore_mongodb()
                case "4":
                    list_collections()
                case "5":
                    list_databases()
                case "6":
                    print("👋 Exiting the program.")
                    break
                case _:
                    print("⚠ Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"✖ An error occurred: {e}")

if __name__ == '__main__':
    main()
