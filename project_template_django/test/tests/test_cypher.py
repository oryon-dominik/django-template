from core.cypher.security import random_sequence
import string


def test_random_sequence():
    """Generate a random sequence from some characters with length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    length = 10
    result = random_sequence(chars=chars, length=length)
    assert len(result) == length
