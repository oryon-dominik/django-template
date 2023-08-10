import pytest
from hypothesis import given
from hypothesis import strategies as st

from core.cypher import security


@given(alphabet=st.text(min_size=1, max_size=1000), length=st.integers(min_value=1, max_value=1000))
def test_random_sequence_for_positive_integers(alphabet, length):
    """Generate a random sequence from some characters with length."""
    result = security.random_sequence(alphabet=alphabet, length=length)
    assert len(result) == length


def test_random_sequence_for_integers_out_of_range():
    with pytest.raises(ValueError):
        security.random_sequence(alphabet="something", length=0)
    with pytest.raises(ValueError):
        security.random_sequence(alphabet="something", length=-1)
    with pytest.raises(ValueError):
        security.random_sequence(alphabet="something", length=1001)


def test_random_sequence_for_invalid_alphabets():
    with pytest.raises(ValueError):
        security.random_sequence(alphabet="", length=1)
    with pytest.raises(ValueError):
        security.random_sequence(alphabet="-"*1001, length=1)


def test_hashme_fails_for_none():
    """Test for non-existent file"""
    with pytest.raises(TypeError):
        security.hashme(file=None)  # type: ignore


def test_hashme_fails_for_ints():
    """Test for non-existent file"""
    with pytest.raises(OSError):
        security.hashme(file=123)  # type: ignore


def test_hashme_fails_for_empty_paths():
    """Test for non-existent file"""
    with pytest.raises(FileNotFoundError):
        security.hashme(file="")  # type: ignore
