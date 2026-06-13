import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def deriveKey(secretKey, keySize):

    keyHash=hashlib.sha256(secretKey.encode("utf-8")).digest()

    if keySize == "128 bits":
        keyHash=hashlib.sha256(secretKey.encode("utf-8")).digest()
        return keyHash[:16]
    elif keySize == "192 bits":
        keyHash=hashlib.sha256(secretKey.encode("utf-8")).digest()
        return keyHash[:24]
    elif keySize == "256 bits":
        return keyHash[:32]
    else:
        raise ValueError("Invalid key size")


def encryptText(message, secretKey, mode, keySize):
    key = deriveKey(secretKey, keySize)
    data=message.encode("utf-8")

    if mode == "ECB":
        cipher=AES.new(key, AES.MODE_ECB)
        cipherText=cipher.encrypt(pad(data, AES.block_size))
        return base64.b64encode(cipherText).decode("utf-8")

    elif mode == "CBC":
        iv=get_random_bytes(16)
        cipher=AES.new(key, AES.MODE_CBC, iv)
        cipherText=cipher.encrypt(pad(data, AES.block_size))
        return base64.b64encode(iv + cipherText).decode("utf-8")

    elif mode == "CFB":
        iv=get_random_bytes(16)
        cipher=AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
        cipherText=cipher.encrypt(data)
        return base64.b64encode(iv + cipherText).decode("utf-8")
    else:
        raise ValueError("Invalid mode")




def decryptText(message, secretKey, mode, keySize):
    key = deriveKey(secretKey, keySize)
    data = base64.b64decode(message)

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(data)
        decrypted=unpad(decrypted, AES.block_size)
        return decrypted.decode("utf-8")

    elif mode == "CBC":
        iv=data[:16]
        cipherText = data[16:]
        cipher=AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted=cipher.decrypt(cipherText)
        decrypted=unpad(decrypted, AES.block_size)
        return decrypted.decode("utf-8")

    elif mode == "CFB":
        iv=data[:16]
        cipherText=data[16:]
        cipher=AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
        decrypted=cipher.decrypt(cipherText)
        return decrypted.decode("utf-8")
    else:
        raise ValueError("Invalid mode")