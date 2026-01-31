from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# message to be encrypted
message = b"""I don't really care if you cry 
            On the real, you should've never lied
            Should've saw the way she looked me in my eyes
            She said, Baby, I am not afraid to die
            Push me to the edge
            All my friends are dead, push me to the edge
            All my friends are dead, push me to the edge"""

# Pad the plaintext to the correct block size
plaintext_padded = pad(message, 16)

# generate key and IV
key = get_random_bytes(16)
initialization_vector = get_random_bytes(16)

# create cipher object for encryption
# AES.MODE_CBC = Cipher Block Chaining
encryption_cipher = AES.new(key, AES.MODE_CBC, iv=initialization_vector)

# encrypt the message
ciphertext = encryption_cipher.encrypt(plaintext_padded)

# create cipher object to be used for decryption
decryption_cipher = AES.new(key, AES.MODE_CBC, iv=initialization_vector)

# decrypt and remove padding
result = unpad(decryption_cipher.decrypt(ciphertext), AES.block_size)

# and the result is:
print(result)