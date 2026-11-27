
import math
import re


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "letmein",
    "iloveyou"
}


def analyze_password(password):

    score = 0
    feedback = []

    if not password:
        return {
            "strength": "Not Assessed",
            "score": 0,
            "entropy": 0,
            "feedback": ["Please enter a password."]
        }

    # 1. Password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Consider using at least 12 characters.")

    # 2. Character variety
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # 3. Common password detection
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password.")

    # 4. Repeated character detection
    if re.search(r"(.)\1{3,}", password):
        score = max(0, score - 1)
        feedback.append("Avoid long repeated character patterns.")

    # 5. Sequential pattern detection
    sequences = [
        "123456",
        "abcdef",
        "qwerty",
        "987654"
    ]

    if any(seq in password.lower() for seq in sequences):
        score = max(0, score - 1)
        feedback.append("Avoid predictable sequential patterns.")

    # 6. Character-set-based theoretical entropy
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^A-Za-z0-9]", password):
        charset += 32

    entropy = (
        len(password) * math.log2(charset)
        if charset > 0 else 0
    )

    # 7. Final strength classification
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "entropy": round(entropy, 2),
        "feedback": feedback
    }
