import hashlib

types_hash = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']

class generate_hash:
    def md5_hash(text):
        text1 = str.encode(text, encoding='utf-8')
        return hashlib.md5(text1).hexdigest()