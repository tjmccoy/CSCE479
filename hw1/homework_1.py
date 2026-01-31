from Cryptodome.Cipher import AES, DES3
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import time

def encrypt_aes(plaintext, key, i_vec):
    cipher = AES.new(key, mode=AES.MODE_CBC, iv=i_vec)
    padded_text = pad(plaintext, 16)

    return cipher.encrypt(padded_text)

def decrypt_aes(ciphertext, key, i_vec):
    cipher = AES.new(key, mode=AES.MODE_CBC, iv=i_vec)

    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def encrypt_3des(plaintext, key, i_vec):
    cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=i_vec)
    padded_text = pad(plaintext, 16)

    return cipher.encrypt(padded_text)

def decrypt_3des(ciphertext, key, i_vec):
    cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=i_vec)

    return unpad(cipher.decrypt(ciphertext), DES3.block_size)

def brute_force_aes(ciphertext, i_vec):
    n = 1000
    start_time = time.perf_counter_ns()

    for i in range(n):
        key = i.to_bytes(16, byteorder="big")
        try:
            _ = decrypt_aes(ciphertext, key, i_vec)
        except ValueError as e:
            pass
        
    end_time = time.perf_counter_ns()

    print(f'time to check {n} keys: {(end_time - start_time) / 1_000_000_000} seconds')


def main():
    key = get_random_bytes(16)
    aes_iv = get_random_bytes(16)
    des3_iv = get_random_bytes(8)
    data = b'All my friends are dead, push me to the edge'
    
    print('\n-=-=-=-=-=-=-=-=-= AES-128 =-=-=-=-=-=-=-=-=-\n')
    print(f'data: {data}\n')
    aes_encrypted_data = encrypt_aes(data, key, aes_iv)
    print(f'encrypted data: {aes_encrypted_data}\n')

    aes_decrypted_data = decrypt_aes(aes_encrypted_data, key, aes_iv)
    print(f'decrypted data: {aes_decrypted_data}\n')

    print('\n-=-=-=-=-=-=-=-=-=-= DES3 =-=-=-=-=-=-=-=-=-=-\n')
    print(f'data: {data}\n')
    des3_encrypted_data = encrypt_3des(data, key, des3_iv)
    print(f'encrypted data: {des3_encrypted_data}\n')

    des3_decrypted_data = decrypt_3des(des3_encrypted_data, key, des3_iv)
    print(f'decrypted data: {des3_decrypted_data}\n')

    print('\n-=-=-=-=-=-=-=-=-= BRUTE FORCE AES-128 =-=-=-=-=-=-=-=-=-\n')
    brute_force_aes(aes_encrypted_data, aes_iv)

if __name__ == "__main__":
    main()
