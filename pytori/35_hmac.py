import hmac, hashlib
key = b"secret"
msg = b"hello"
print(key)
print(msg)
print(hmac.new(key, msg, hashlib.sha256).hexdigest())