from typing import Dict


def login_admin(admin: Dict) -> bool:
    admin_all = [{"username": "renan", "password": "12345"}]
    if admin.get("username") and admin.get("password"):
        for index in admin_all:
            if str(admin.get("username")).lower() == str(index.get("username")).lower():
                if admin.get("password") == index.get("password"):
                    return True
    return False
