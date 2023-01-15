from unittest.mock import MagicMock

import pytest

from tripservice import get_trips_by_user, User, Trip, UserNotLoggedInException


def test_no_trips_returned_for_users_without_trips(mocker: MagicMock):
    john = User()
    mocker.patch("tripservice._get_logged_user", return_value=john)
    assert get_trips_by_user(john) == []


def test_user_can_get_trips_of_their_friends(mocker: MagicMock):
    john = User()
    jane = User()
    mocker.patch("tripservice._get_logged_user", return_value=john)

    jane.add_friend(john)
    jane.add_trip(Trip())
    jane.add_trip(Trip())
    jane.add_trip(Trip())

    mocker.patch("tripservice._find_trips_by_user", return_value=jane.trips)
    assert len(get_trips_by_user(jane)) == 3


def test_raises_an_exception_for_non_logged_user(mocker: MagicMock):
    guest = None
    john = User()

    mocker.patch("tripservice._get_logged_user", return_value=guest)
    with pytest.raises(UserNotLoggedInException):
        get_trips_by_user(john)


def test_returns_empty_list_for_users_that_are_not_friends(mocker: MagicMock):
    john = User()
    jane = User()

    mocker.patch("tripservice._get_logged_user", return_value=john)
    assert get_trips_by_user(jane) == []
