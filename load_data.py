import subprocess

def restore_mongodb(db_name, backup_path):
    try:
        subprocess.run([
            "mongorestore",
            "--db", db_name,
            backup_path
        ], check=True)
        print(f"✔ Restore completed from {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Restore failed: {e}")

# Esempio d'uso
restore_mongodb("library", "./dump/library")