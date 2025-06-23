import hashlib

def hash_credentials(input):
    hasher = hashlib.sha256()
    hasher.update(input.encode('utf-8'))
    return hasher.digest()  # Returns the hash as a byte object