from Crypto.Cipher import AES
import hashlib, base64

def unpad(s):
    return s[:-ord(s[-1])]

def aes_decrypt(encdata, key):
    enc = base64.b64decode(encdata)
    key_hash = hashlib.sha256(key.encode()).digest()
    iv = enc[:16]
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(enc[16:])
    return unpad(decrypted.decode())

def full_decode(wrapped, key):
    clean = wrapped.replace('<', '').replace('>', '')
    return aes_decrypt(base64.b64decode(clean).decode(), key)