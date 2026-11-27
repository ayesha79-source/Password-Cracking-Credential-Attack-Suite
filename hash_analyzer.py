
import hashlib
import re


def generate_hash(password, algorithm="sha256"):
    supported = ["md5", "sha1", "sha256", "sha512"]

    if algorithm not in supported:
        raise ValueError("Unsupported hashing algorithm")

    return hashlib.new(
        algorithm,
        password.encode("utf-8")
    ).hexdigest()


def identify_hash_format(hash_value):
    hash_value = hash_value.strip()

    # Linux password hash formats (synthetic examples)
    if hash_value.startswith("$6$"):
        return "Linux SHA-512 crypt format"

    if hash_value.startswith("$5$"):
        return "Linux SHA-256 crypt format"

    if hash_value.startswith("$1$"):
        return "Linux MD5 crypt format"

    if hash_value.startswith("$y$"):
        return "Linux yescrypt format"

    # Windows NTLM and MD5 have the same hexadecimal length.
    if re.fullmatch(r"[a-fA-F0-9]{32}", hash_value):
        return "Possible MD5 or NTLM (cannot distinguish by length alone)"

    if re.fullmatch(r"[a-fA-F0-9]{40}", hash_value):
        return "Possible SHA-1"

    if re.fullmatch(r"[a-fA-F0-9]{64}", hash_value):
        return "Possible SHA-256"

    if re.fullmatch(r"[a-fA-F0-9]{128}", hash_value):
        return "Possible SHA-512"

    return "Unknown or unsupported format"
