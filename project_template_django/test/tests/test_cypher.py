import pytest

from hypothesis import given
from hypothesis import strategies as st

from core.cypher import security


@pytest.mark.skip(reason="This FUZZING test is EXTREMELY slow. So skip it, it has run successfully.")
@pytest.mark.slow
@given(chars=st.text(), length=st.integers(min_value=1))
def test_random_sequence_for_positive_integers(chars, length):
    """Generate a random sequence from some characters with length."""
    result = security.random_sequence(chars=chars, length=length)
    assert len(result) == length


@pytest.mark.skip(reason="This FUZZING test is EXTREMELY slow. So skip it, it has run successfully.")
@pytest.mark.slow
@given(chars=st.text(), length=st.integers(max_value=0))
def test_random_sequence_for_negative_integers_and_zero(chars, length):
    """Test for negative integers and zero"""
    result = security.random_sequence(chars=chars, length=length)
    assert len(result) == 1


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
