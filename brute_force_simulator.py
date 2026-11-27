
import string


def estimate_cracking_time(
    password_length,
    character_set_size,
    guesses_per_second=1000
):
    if password_length <= 0:
        raise ValueError("Password length must be greater than zero.")

    if character_set_size <= 0:
        raise ValueError("Character set size must be greater than zero.")

    if guesses_per_second <= 0:
        raise ValueError("Guess rate must be greater than zero.")

    total_combinations = character_set_size ** password_length

    worst_case_seconds = (
        total_combinations / guesses_per_second
    )

    average_case_seconds = worst_case_seconds / 2

    return {
        "total_combinations": total_combinations,
        "worst_case_seconds": worst_case_seconds,
        "average_case_seconds": average_case_seconds
    }


def simulate_password_test(test_password, sample_candidates):

    if not isinstance(test_password, str):
        raise ValueError("Test password must be text.")

    attempts = 0

    for candidate in sample_candidates:

        attempts += 1

        if candidate == test_password:
            return {
                "found": True,
                "attempts": attempts,
                "message": "Test password found in the sample list."
            }

    return {
        "found": False,
        "attempts": attempts,
        "message": "Test password not found in the sample list."
    }


def get_character_set_size(password):

    if not isinstance(password, str):
        raise ValueError("Password must be text.")

    size = 0

    if any(c in string.ascii_lowercase for c in password):
        size += 26

    if any(c in string.ascii_uppercase for c in password):
        size += 26

    if any(c in string.digits for c in password):
        size += 10

    if any(c in string.punctuation for c in password):
        size += len(string.punctuation)

    return size
