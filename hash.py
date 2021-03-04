import hashlib
from generate_hash import generate_hash


def test_hash(hash1, text, type_hash):
    gh = generate_hash()
    if type_hash.lower() == 'md5' and hash1 == gh.md5_hash(text):
        return True
    elif type_hash.lower() == 'sha1' and hash1 == gh.sha1_hash(text):
        return True
    elif type_hash.lower() == 'sha224' and hash1 == gh.sha224_hash(text):
        return True
    elif type_hash.lower() == 'sha256' and hash1 == gh.sha256_hash(text):
        return True
    elif type_hash.lower() == 'sha384' and hash1 == gh.sha384_hash(text):
        return True
    elif type_hash.lower() == 'sha512' and hash1 == gh.sha512_hash(text):
        return True
    elif type_hash.lower() == 'blake2b' and hash1 == gh.blake2b_hash(text):
        return True
    elif type_hash.lower() == 'blake2s' and hash1 == gh.blake2s_hash(text):
        return True
    elif type_hash.lower() == 'sha3_224' and hash1 == gh.sha3_224_hash(text):
        return True
    elif type_hash.lower() == 'sha3_256' and hash1 == gh.sha3_256_hash(text):
        return True
    elif type_hash.lower() == 'sha3_384' and hash1 == gh.sha3_384_hash(text):
        return True
    elif type_hash.lower() == 'sha3_512' and hash1 == gh.sha3_512_hash(text):
        return True
    else:
        return False
