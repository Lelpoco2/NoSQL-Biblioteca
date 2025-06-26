# NoSQL-Library

## Reference Approach
- Many-to-many relationships: users and books with multiple loans are better managed with references.

- Avoid data duplication: book and user data kept separate, allowing consistent updates.

- Scalability: large number of loans won’t bloat documents or hit size limits.

- Flexible and performant queries: references and indexes enable efficient searches across users, books, and loans.

- Simple maintenance: localized updates without modifying duplicated data.


This project provides utilities to **dump** and **restore** a MongoDB database for a library management system, but can be used also for other type of databases. 


## Prerequisites

- Python 3.x
- [MongoDB Atlas](https://www.mongodb.com/it-it/products/platform/atlas-database) 
- [MongoDB Compass](https://www.mongodb.com/products/tools/compass)
- [pymongo](https://pypi.org/project/pymongo/)
- MongoDB tools (`mongodump`, `mongorestore`)
- A running MongoDB instance (default: `localhost:27017`)

## Project Structure

```
.
├── .gitignore
├── MongoTools.py           <- RUN THIS PROGRAM
├── README.md               <- Documentation
└── dump/                   <- default backup path 
    └── <database-name>/    <- folder named as DB
        |- <data-backups>   <- .bson and .json files
```
## How the programm works ?

The MongoTools.py script is an interactive command-line utility that allows you to perform essential MongoDB administrative tasks. It provides a simple menu interface to interact with your MongoDB server.

### Features
Once launched, the program will:

Prompt for a MongoDB connection URI

Default: mongodb://localhost:27017

Useful for switching between local and remote MongoDB instances.

Display a menu of operations, including:

- Test connection to the MongoDB server

- Dump (backup) a specific database to the ./dump directory

- Restore a database from a backup

- List all collections within a specified database

- Create a new database by inserting a document into a new collection

- List all databases available on the connected server

- Exit the utility

Backup and restore support using mongodump and mongorestore under the hood.

Dumps are stored in the ./dump/<\database-name>/ directory.

These backups include .bson data files and .metadata.json files.

## Data Files

- **books.bson**, **loans.bson**, **users.bson**: BSON files containing the data for each collection.
- **books.metadata.json**, **loans.metadata.json**, **users.metadata.json**: Metadata for each collection.
- **prelude.json**: Contains server and tool version information.

## Notes

- Ensure MongoDB is running locally before using the scripts.
- The dump directory is excluded from version control via [.gitignore](.gitignore).
