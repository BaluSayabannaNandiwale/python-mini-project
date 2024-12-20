import hashlib
import hmac

def hostapd_password_hash(password, salt, iterations=4096):
    """
    Hash a password using the Hostapd algorithm (PBKDF2-HMAC-SHA256)

    :param password: The password to hash
    :param salt: A random salt value (at least 16 bytes)
    :param iterations: The number of iterations (default: 4096)
    :return: The hashed password as a hexadecimal string
    """
    password_bytes = password.encode()
    salt_bytes = salt.encode()

    # Create a PBKDF2 key derivation function
    kdf = hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, iterations)

    # Calculate the HMAC-SHA256 of the derived key
    hmac_bytes = hmac.new(kdf, password_bytes, hashlib.sha256).digest()

    # Return the hashed password as a hexadecimal string
    return hmac_bytes.hex()

# Example usage:
password = "my_secret_password"
salt = "random_salt_value_here"  # Generate a random salt value

hashed_password = hostapd_password_hash(password, salt)
print("Hashed password:", hashed_password)
