import hashlib

types_hash = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']

class generate_hash:
    def md5_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.md5(text1).hexdigest()

    def sha1_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha1(text1).hexdigest()
    
    def sha224_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha224(text1).hexdigest()

    def sha256_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha256(text1).hexdigest()


    def sha384_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha384(text1).hexdigest()


    def sha512_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha512(text1).hexdigest()

    def blake2b_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.blake2b(text1).hexdigest()


    def blake2s_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.blake2s(text1).hexdigest()


    def sha3_224_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha3_224(text1).hexdigest()


    def sha3_256_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha3_256(text1).hexdigest()


    def sha3_384_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha3_384(text1).hexdigest()


    def sha3_512_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.sha3_512(text1).hexdigest()