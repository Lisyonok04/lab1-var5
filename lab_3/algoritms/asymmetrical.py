from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import logging

logger = logging.getLogger()
logger.setLevel('INFO')


class RSA:
    def __init__(self):
        pass

    def key_generation() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Function generates asymmetric keys

        Returns:
            tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]: public and private keys
        """
        key = rsa.generate_private_key(public_exponent = 65537, key_size = 2048)
        private_key = key
        public_key = key.public_key()
        logging.info('Asymmetric keys have been generated')
        return private_key, public_key
    
    
