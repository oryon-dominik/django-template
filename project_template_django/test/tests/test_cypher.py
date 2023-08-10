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
    with pytest.raises(ValueError, match=r"^Length must be positive-nonzero.$"):
        security.random_sequence(alphabet="something", length=0)
    with pytest.raises(ValueError, match=r"^Length must be positive-nonzero.$"):
        security.random_sequence(alphabet="something", length=-1)
    with pytest.raises(ValueError, match=r"^Length must be less than MAXIMUM_LENGTH=1000.$"):
        security.random_sequence(alphabet="something", length=1001)


def test_random_sequence_for_invalid_alphabets():
    with pytest.raises(ValueError, match=r"^No characters provided.$"):
        security.random_sequence(alphabet="", length=1)
    with pytest.raises(
        ValueError, match=r"^Length of the alphabet len\(alphabet\)=1001 must be less than MAXIMUM_LENGTH=1000.$"
    ):
        security.random_sequence(alphabet="-" * 1001, length=1)


@pytest.mark.parametrize("invalid_type", ["", "string", 1, 1.0, True, False, None, [], {}])
def test_hashme_fails_for_invalid_types(invalid_type):
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
    with pytest.raises(ValueError, match=r"^Length must be positive-nonzero.$"):
        security.random_sequence(alphabet="something", length=0)
    with pytest.raises(ValueError, match=r"^Length must be positive-nonzero.$"):
        security.random_sequence(alphabet="something", length=-1)
    with pytest.raises(ValueError, match=r"^Length must be less than MAXIMUM_LENGTH=1000.$"):
        security.random_sequence(alphabet="something", length=1001)


def test_random_sequence_for_invalid_alphabets():
    with pytest.raises(ValueError, match=r"^No characters provided.$"):
        security.random_sequence(alphabet="", length=1)
    with pytest.raises(
        ValueError, match=r"^Length of the alphabet len\(alphabet\)=1001 must be less than MAXIMUM_LENGTH=1000.$"
    ):
        security.random_sequence(alphabet="-" * 1001, length=1)


@pytest.mark.parametrize("invalid_type", ["", "string", 1, 1.0, True, False, None, [], {}])
def test_hashme_fails_for_invalid_types(invalid_type):
    with pytest.raises(TypeError, match=r"^Invalid type for path: type\(path\)=<class '.*'>$"):
        security.hashme(file=invalid_type)  # type: ignore

    with pytest.raises(TypeError, match=r"^Invalid type for path: type\(path\)=<class '.*'>$"):
        security.hashme(file=invalid_type)  # type: ignore
