import hashlib


class StringEncodeDecode:

    # Encode password using MD5, SHA256 and DJANFO AUTH Make Password Hash
    def encode_password(self, password):
        encode_md5 = hashlib.md5(password.encode()).hexdigest()
        encode_sha1 = hashlib.sha256(encode_md5.encode()).hexdigest()
        return encode_sha1