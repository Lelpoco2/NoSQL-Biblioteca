from pymongo import MongoClient
import subprocess


try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['library']
    books = db['books']
    loans = db['loans']
    users = db['users']

    # Fetch all documents from the collection
    book_documents = books.find()
    loan_documents = loans.find()
    user_documents = users.find()

    # # Print documents
    # print("Books:")
    # for book in book_documents:
    #     print(book)
    # print("\nLoans:")
    # for loan in loan_documents:
    #     print(loan)
    # print("\nUsers:")
    # for user in user_documents:
    #     print(user)

except Exception as e:
    print(f"An error occurred: {e}")


def dump_mongo(db_name, output_dir):
    try:
        subprocess.run(['mongodump', '--db', db_name, '--out', output_dir], check=True)

        print("MongoDB dump completed successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while dumping MongoDB: {e}")


db_name = input("Quale database vuoi esportare?")

dump_mongo(db_name, './dump')
