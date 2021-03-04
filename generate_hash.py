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

    def more_hash(text):
        sp_hash = []
        for i in types_hash:
            bar.next()
            if i == 'md5':
                sp_hash.append([generate_hash.md5_hash(text), i])
            elif i == 'sha1':
                sp_hash.append([generate_hash.sha1_hash(text), i])
            elif i == 'sha224':
                sp_hash.append([generate_hash.sha224_hash(text), i])
            elif i == 'sha256':
                sp_hash.append([generate_hash.sha256_hash(text), i])
            elif i == 'sha384':
                sp_hash.append([generate_hash.sha384_hash(text), i])
            elif i == 'sha512':
                sp_hash.append([generate_hash.sha512_hash(text), i])
            elif i == 'blake2b':
                sp_hash.append([generate_hash.blake2b_hash(text), i])
            elif i == 'blake2s':
                sp_hash.append([generate_hash.blake2s_hash(text), i])
            elif i == 'sha3_224':
                sp_hash.append([generate_hash.sha3_224_hash(text), i])
            elif i == 'sha3_256':
                sp_hash.append([generate_hash.sha3_256_hash(text), i])
            elif i == 'sha3_384':
                sp_hash.append([generate_hash.sha3_384_hash(text), i])
            elif i == 'sha3_512':
                sp_hash.append([generate_hash.sha3_512_hash(text), i])
        return sp_hash