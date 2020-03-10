import hashlib

h = hashlib.sha256()
h.update(b"My.Secret.Password")
print(h.hexdigest())
