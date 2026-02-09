# encrypt.py
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def generate_key_from_password(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, cipher):
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

def run_encryption(password: str, salt_path="salt.bin"):
    # Load salt
    with open(salt_path, "rb") as f:
        salt = f.read()
    key = generate_key_from_password(password, salt)
    cipher = Fernet(key)

    # Encrypt files
    encrypt_file(r"E:\Python scripts\RT_IOT2022_NORMAL_TRAFFIC.csv", cipher)
    encrypt_file(r"E:\Python scripts\RT_IOT2022.csv", cipher)

    print("Files encrypted successfully!")

if __name__ == "__main__":
    password = input("Enter your password to lock files: ")
    run_encryption(password)
