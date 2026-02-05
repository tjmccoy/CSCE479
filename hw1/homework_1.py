"""
CSCE 479 - Homework 1
This script demonstrates symmetric encryption and decryption using AES-128 and Triple DES (3DES) algorithms.
It also includes brute-force functions to attempt key recovery by trying all possible keys within a specified range.
"""
from Cryptodome.Cipher import AES, DES3
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import time

def encrypt_aes(plaintext, key, i_vec):
    """
    This function ecrypts the given plaintext using AES encryption in CBC mode.
    
    :param plaintext: The text to be encrypted
    :param key: The key to be used for encryption
    :param i_vec: The initialization vector (IV) to be used for encryption
    """
    cipher = AES.new(key, mode=AES.MODE_CBC, iv=i_vec)
    padded_text = pad(plaintext, 16)

    return cipher.encrypt(padded_text)

def decrypt_aes(ciphertext, key, i_vec):
    """
    This function decrypts the given ciphertext using AES decryption in CBC mode.
    
    :param ciphertext: The text to be decrypted
    :param key: The key to be used for decryption
    :param i_vec: The initialization vector (IV) to be used for decryption
    """
    cipher = AES.new(key, mode=AES.MODE_CBC, iv=i_vec)

    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def encrypt_3des(plaintext, key, i_vec):
    """
    This function encrypts the given plaintext using Triple DES (3DES) encryption in CBC mode.
    
    :param plaintext: The text to be encrypted
    :param key: The key to be used for encryption
    :param i_vec: The initialization vector (IV) to be used for encryption
    """
    cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=i_vec)
    padded_text = pad(plaintext, DES3.block_size)


    return cipher.encrypt(padded_text)

def decrypt_3des(ciphertext, key, i_vec):
    """
    This function decrypts the given ciphertext using Triple DES (3DES) decryption in CBC mode.
    
    :param ciphertext: The text to be decrypted
    :param key: The key to be used for decryption
    :param i_vec: The initialization vector (IV) to be used for decryption
    """
    cipher = DES3.new(key, mode=DES3.MODE_CBC, iv=i_vec)

    return unpad(cipher.decrypt(ciphertext), DES3.block_size)

def brute_force_aes(n, ciphertext, i_vec, plaintext):
    """
    This function attempts to brute-force the AES key by trying all possible keys within a specified range [0, n).
    
    :param n: The range of keys to try from [0, n)
    :param ciphertext: The ciphertext to be decrypted
    :param i_vec: The initialization vector (IV) to be used for decryption
    :param plaintext: The expected plaintext that should result from decryption
    """
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

    return elapsed_time_ns

def brute_force_des3(n, ciphertext, i_vec, plaintext):
    """
    This function attempts to brute-force the Triple DES (3DES) key by trying all possible keys within a specified range [0, n).
    
    :param n: The range of keys to try from [0, n)
    :param ciphertext: The ciphertext to be decrypted
    :param i_vec: The initialization vector (IV) to be used for decryption
    :param plaintext: The expected plaintext that should result from decryption
    """
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

    return elapsed_time_ns


def main():
    """
    Main function to demonstrate encryption, decryption, and brute-force key searching for AES-128 and 3DES.
    """
    aes_key = get_random_bytes(16)
    aes_iv = get_random_bytes(16)
    des3_key = DES3.adjust_key_parity(get_random_bytes(24))
    des3_iv = get_random_bytes(8)
    data = b'Super secret message'
    
    print('\n-=-=-=-=-=-=-=-=-= AES-128 =-=-=-=-=-=-=-=-=-\n')
    print(f'data: {data}\n')
    aes_encrypted_data = encrypt_aes(data, aes_key, aes_iv)
    print(f'encrypted data: {aes_encrypted_data}\n')

    aes_decrypted_data = decrypt_aes(aes_encrypted_data, aes_key, aes_iv)
    print(f'decrypted data: {aes_decrypted_data}')

    print('\n-=-=-=-=-=-=-=-=-=-= DES3 =-=-=-=-=-=-=-=-=-=-\n')
    print(f'data: {data}\n')
    des3_encrypted_data = encrypt_3des(data, des3_key, des3_iv)
    print(f'encrypted data: {des3_encrypted_data}\n')

    des3_decrypted_data = decrypt_3des(des3_encrypted_data, des3_key, des3_iv)
    print(f'decrypted data: {des3_decrypted_data}')

    print('\n-=-=-=-=-=-=-=-=-= BRUTE FORCE =-=-=-=-=-=-=-=-=-\n')
    num_attempts = 1024
    ns_per_year = 31_536_000_000_000_000
    aes_ns = brute_force_aes(num_attempts, aes_encrypted_data, aes_iv, data)
    des3_ns = brute_force_des3(num_attempts, des3_encrypted_data, des3_iv, data)

    print(f'Result (AES): Time to check {num_attempts} keys={aes_ns / 1_000_000_000} sec. Estimated time to check all 2^128 keys={(aes_ns / ns_per_year) * (2 ** 118)} years.')
    print(f'Result (DES3): Time to check {num_attempts} keys={des3_ns / 1_000_000_000} sec. Estimated time to check all 2^168 keys={(des3_ns / ns_per_year) * (2 ** 158)} years.')

if __name__ == "__main__":
    main()
