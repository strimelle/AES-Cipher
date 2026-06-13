# AES-Cipher

## Project Description
AES-Cipher is a desktop GUI application created with Python, Tkinter, and PyCryptodome.
The program allows the user to encrypt and decrypt text using the AES algorithm.

The user can:
- enter plaintext or ciphertext
- enter a secret key
- choose the operation: Encrypt or Decrypt
- choose the AES mode: ECB, CBC, or CFB
- choose the key size: 128 bits, 192 bits, or 256 bits

## Technologies Used
- Python
- Tkinter
- PyCryptodome

## Features
- Text encryption and decryption
- AES modes:
  - ECB
  - CBC
  - CFB
- AES key sizes:
  - 128 bits
  - 192 bits
  - 256 bits
- GUI interface
- Custom application icon

## How AES Works
AES (Advanced Encryption Standard) is a symmetric encryption algorithm.
This means that the same secret key is used for both encryption and decryption.

AES always works with a 128-bit block size, but it can use different key lengths:
- 128-bit key
- 192-bit key
- 256-bit key

A longer key generally provides stronger protection against brute-force attacks.

## AES Modes Used in This Project

### ECB
ECB (Electronic Codebook) encrypts each block independently.
It does not use an IV.
It is the simplest mode, but it is the least secure because identical plaintext blocks produce identical ciphertext blocks.

### CBC
CBC (Cipher Block Chaining) links each block with the previous encrypted block.
It uses an IV (Initialization Vector).
This makes it more secure than ECB.

### CFB
CFB (Cipher Feedback) also uses an IV.
It works more like a stream mode and can encrypt data continuously.

## Key Processing
The user enters a secret key as text.
Because AES requires a fixed key length, the program transforms the user key using SHA-256.

Then the program takes:
- first 16 bytes for 128-bit AES
- first 24 bytes for 192-bit AES
- first 32 bytes for 256-bit AES

This ensures that the key always matches the selected AES key size.

## IV Usage
For CBC and CFB modes, the program generates a random 16-byte IV.
The IV is stored together with the encrypted data and used again during decryption.

ECB mode does not use an IV.

## How to Run the Project

### 1. Install dependencies
```bash
pip install pycryptodome
```
### 2. Run the program
```bash
python main.py
```
## Project Structure
```bash
AES-Cipher/
├── main.py
├── aes_util.py
├── file_util.py
├── icon.png
├── .gitignore
└── README.md
```

##Example Usage

### 1. Enter a plaintext message
### 2. Enter a secret key
### 3. Select AES mode
### 4. Select key size
### 5. Choose Encrypt
### 6. Press GO!
### 7. Copy the encrypted text
### 8. Choose Decrypt
### 9. Paste the encrypted text
### 10. Enter the same key, mode, and key size
### 11. Press GO! to get the original text back
