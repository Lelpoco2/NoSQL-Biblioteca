from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import subprocess

# Global DB URI
db_uri = input("Prompt the MongoDB connection string [default:mongodb://localhost:27017]:")

# Test MongoDB connection
def test_connection(db_uri="mongodb://localhost:27017"):
    try:
        client = MongoClient(db_uri, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        print(f"✔ Connection to {db_uri} successful.")
        return True
    except ConnectionFailure as e:
        print("✖ Failed to connect to MongoDB:", e)
        return False

# Perform a MongoDB dump using mongodump
def dump_mongo():
    db_name = input("Enter the name of the database to back up: ").strip()
    output_dir = input("Enter the output directory [default: ./dump]: ").strip() or "./dump"
    try:
        subprocess.run(['mongodump', '--db', db_name, '--out', output_dir], check=True)
        print("✔ Database dump completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"✖ Error during database dump: {e}")

# Restore MongoDB from a backup using mongorestore
def restore_mongodb():
    db_name = input("Enter the name of the database to restore: ").strip()
    backup_path = input(f"Enter the backup path [default: ./dump/{db_name}]: ").strip() or f"./dump/{db_name}"
    try:
        subprocess.run(["mongorestore", "--db", db_name, backup_path], check=True)
        print(f"✔ Restore completed from {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"✖ Restore failed: {e}")


# Visulize collection in a DB
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


#Create database and collection
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
        # Inserisce un documento di test per creare il database
        result = collection.insert_one({"created": True})
        print(f"✔ Database '{db_name}' and collection '{collection_name}' created successfully.")
    except Exception as e:
        print(f"✖ Failed to create database: {e}")

# Menu principale con match-case (Python 3.10+)
def main():
    while True:
        print("\n====== MongoDB Utility Menu ======")
        print("1. Test MongoDB Connection")
        print("2. Dump Database")
        print("3. Restore Database")
        print("4. Check Collection")
        print("5.Exit")
        choice = input("Select an option [1-4]: ").strip()

        try:
            match choice:
                case "1":
                    test_connection()
                case "2":
                    dump_mongo()
                case "3":
                    restore_mongodb()
                case "4":
                    list_collections()
                case "5":
                    print("Exiting the program.")
                    break
                case _:
                    print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"✖ An error occurred: {e}")

if __name__ == '__main__':
    main()
