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
- MongoDB Atlas and MongoDB Compass
- [pymongo](https://pypi.org/project/pymongo/)
- MongoDB tools (`mongodump`, `mongorestore`)
- A running MongoDB instance (default: `localhost:27017`)

## Project Structure

```
.
├── .gitignore
├── dump.py <- USE THIS TO BACKUP YOUR DATABASE DATA
├── load_data.py <- USE THIS TO RESTORE YOUR DATABASE DATA
├── README.md
└── dump/
    └── <your-backup-database>/
        |- <data-backups>
```

# Usage of the dump.py and load_data.py

### 1. Dump the Database

Use [dump.py](dump.py) to export the contents of a MongoDB database.

```sh
python dump.py
```

- You will be prompted to enter the database name to export.
- The script uses `mongodump` to create a BSON dump in the `./dump` directory.

### 2. Restore the Database

Use [load_data.py](load_data.py) to restore the database from a BSON dump.

```sh
python load_data.py
```

- By default, it restores the `library` database from `./dump/library`.
- You can modify the script to restore a different database or path.

## Data Files

- **books.bson**, **loans.bson**, **users.bson**: BSON files containing the data for each collection.
- **books.metadata.json**, **loans.metadata.json**, **users.metadata.json**: Metadata for each collection.
- **prelude.json**: Contains server and tool version information.

## Notes

- Ensure MongoDB is running locally before using the scripts.
- The dump directory is excluded from version control via [.gitignore](.gitignore).
