from typing import List


class DependencyClassCallDuringUnitTestException(Exception):
    pass


class UserNotLoggedInException(Exception):
    pass


class Trip:
    pass


class User:
    def __init__(self):
        self.trips: List[Trip] = []
        self.friends: List[User] = []

    def add_friend(self, user: "User"):
        self.friends.append(user)

    def add_trip(self, trip: Trip):
        self.trips.append(trip)

    def get_friends(self) -> List["User"]:
        return self.friends


def _is_user_logged_in(user: User):
    raise DependencyClassCallDuringUnitTestException(
        "UserSession.isUserLoggedIn() should not be called in an unit test"
    )


def _get_logged_user():
    raise DependencyClassCallDuringUnitTestException(
        "UserSession.getLoggedUser() should not be called in an unit test"
    )


def _find_trips_by_user(user: User):
    raise DependencyClassCallDuringUnitTestException(
        "TripDAO should not be invoked on an unit test."
    )


def get_trips_by_user(user):
    if not (logged_user := _get_logged_user()):
        raise UserNotLoggedInException()

    if logged_user in user.get_friends():
        return _find_trips_by_user(user)

    return []
