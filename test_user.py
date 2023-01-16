from tripservice import User


def test_can_check_if_friends_with_another_user():
    john = User()
    jane = User()
    joe = User()

    john.add_friend(jane)

    assert john.is_friends_with(jane)
    assert not john.is_friends_with(joe)
