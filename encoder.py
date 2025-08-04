from Crypto.Cipher import AES
import hashlib, base64, os

def pad(text):
    return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)

def aes_encrypt(text, key):
    key_hash = hashlib.sha256(key.encode()).digest()
    iv = os.urandom(16)
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    enc = cipher.encrypt(pad(text).encode())
    return base64.b64encode(iv + enc).decode()

def encode_pipeline(message, key):
    enc = aes_encrypt(message, key)
    # Add symbolic wrappers
    return ''.join(f"<{c}>" for c in base64.b64encode(enc.encode()).decode())
