import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class TripleDES:
    def __init__(self):
        pass

    def key_length(self) -> int:
        """The funtion lets the user to choose length of key and generates a key 

        Returns:
            int: length key triple DES
        """
        try:
            length = int(input("Enter the length (64, 128, or 192): "))
            if length not in [64, 128, 192]:
                raise ValueError("Invalid key length. Please enter 64, 128, or 192.")
            key_length_bytes = length // 8
            key = os.urandom(key_length_bytes)
            return key
        except ValueError as e:
                print("Invalid input.")