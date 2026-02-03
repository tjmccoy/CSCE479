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
    padded_text = pad(plaintext, DES3.block_size)

    return cipher.encrypt(padded_text)

def decrypt_3des(ciphertext, key, i_vec):
    cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=i_vec)

    return unpad(cipher.decrypt(ciphertext), DES3.block_size)

def brute_force_aes(n, ciphertext, i_vec, plaintext):
    start_time = time.perf_counter_ns()

    for i in range(n):
        key = i.to_bytes(16, byteorder="big")
        try:
            decryption_result = decrypt_aes(ciphertext, key, i_vec)

            if decryption_result == plaintext:
                return key
            else:
                continue

        except ValueError:
            pass
        
    end_time = time.perf_counter_ns()
    elapsed_time_ns = end_time - start_time

    print(f'time to check {n} keys (AES): {elapsed_time_ns / 1_000_000_000} seconds')
    return elapsed_time_ns

def brute_force_des3(n, ciphertext, i_vec, plaintext):
    start_time = time.perf_counter_ns()

    for i in range(n):
        key = i.to_bytes(16, byteorder="big")
        try:
            decryption_result = decrypt_3des(ciphertext, key, i_vec)

            if decryption_result == plaintext:
                return key
            else:
                continue

        except ValueError:
            pass

    end_time = time.perf_counter_ns()
    elapsed_time_ns = end_time - start_time

    print(f'time to check {n} keys (DES3): {elapsed_time_ns / 1_000_000_000} seconds')

    return elapsed_time_ns


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

    print('\n-=-=-=-=-=-=-=-=-= BRUTE FORCE =-=-=-=-=-=-=-=-=-\n')
    num_attempts = 1024
    ns_per_year = 31_536_000_000_000_000
    aes_ns = brute_force_aes(num_attempts, aes_encrypted_data, aes_iv, data)
    des3_ns = brute_force_des3(num_attempts, des3_encrypted_data, des3_iv, data)

    print(f'Result (AES): Time to check {num_attempts} keys={aes_ns / 1_000_000_000} sec. Estimated time to check all 2^128 keys={(aes_ns / ns_per_year) * (2 ** 118)} years.')
    print(f'Result (DES3): Time to check {num_attempts} keys={des3_ns / 1_000_000_000} sec. Estimated time to check all 2^128 keys={(des3_ns / ns_per_year) * (2 ** 118)} years.')

if __name__ == "__main__":
    main()
