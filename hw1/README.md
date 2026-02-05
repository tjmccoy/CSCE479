# CSCE 479 - Homework #1
### Overview
This Python script demonstrates symmetric encryption/decryption using
* AES-128 (CBC Mode)
* 3DES (CBC Mode)

It encrypts and decrypts a sample message and then performs a small brute-force key search simulation
to measure how long it would take to guess the key.

Our goal is to compare performance between AES-128 and 3DES and how long it would take to brute force
the key for both encryption schemes.

### Requirements
* Linux Ubuntu
* Python 3.X
* PyCryptodome Library (https://www.pycryptodome.org/src/installation#compiling-in-linux-ubuntu)

### Installation
1. `sudo apt-get install build-essential python3-dev`
2. `pip install pycryptodomex`
3. `pip install pycryptodome-test-vectors`
4. Test using: `python3 -m Cryptodome.SelfTest`

### Running the Script
1. Navigate to directory containing the script
2. `python3 homework_1.py`

### Example Output
![](hw1/images/sample-output.png)