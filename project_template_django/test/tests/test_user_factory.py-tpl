import pytest


@pytest.mark.django_db(transaction=True)
def test_fixture_users_passwords_were_set_correctly(verified_user, unverified_user, valid_password):
    assert verified_user.check_password(raw_password=valid_password), "Password shall be valid."
    assert unverified_user.check_password(raw_password=valid_password), "Password shall be valid."


@pytest.mark.django_db(transaction=True)
def test_and_again_user_data(user, verified_user, unverified_user):
    """The user fixture shall not be overwritten by other user fixtures."""
    assert user.username != verified_user.username, "Usernames shall be different."
    assert user.username != unverified_user.username, "Usernames shall be different."
