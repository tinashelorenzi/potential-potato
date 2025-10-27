import hashlib

#All the functions to compute hashing

def to_byte(word):
    word_as_byte = bytes(word,'utf-8')
    return word_as_byte

def calculate_sha256(string_byte):
    hash_key = hashlib.sha256(string_byte).hexdigest()
    return hash_key