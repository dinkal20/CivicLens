"""One-time migration: move existing admin users into the admin collection
and remove role fields from all citizen records in users.
Run: python migrate_accounts.py
"""
from config import admin_collection, users_collection


def migrate():
    moved = 0
    for old_admin in users_collection.find({"role": {"$in": ["admin", "administrator"]}}):
        email = str(old_admin.get("email", "")).strip().lower()
        if not email:
            continue
        existing = admin_collection.find_one({"email": email})
        if not existing:
            document = {
                key: old_admin[key]
                for key in ("name", "email", "password_hash", "created_at")
                if key in old_admin
            }
            document["email"] = email
            admin_collection.insert_one(document)
            moved += 1
        users_collection.delete_one({"_id": old_admin["_id"]})

    result = users_collection.update_many({}, {"$unset": {"role": ""}})
    print(f"Migration complete. Admin accounts moved: {moved}.")
    print(f"Role fields removed from citizen records: {result.modified_count}.")


if __name__ == "__main__":
    migrate()
