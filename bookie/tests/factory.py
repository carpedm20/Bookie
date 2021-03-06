"""Provide tools for generating objects for testing purposes."""
from random import randint
import random
import string

from bookie.models import DBSession
from bookie.models import Bmark
from bookie.models import Tag
from bookie.models.applog import AppLog
from bookie.models.auth import User


def random_int(max=1000):
    """Generate a random integer value

    :param max: Maximum value to hit.
    """
    return randint(0, max)


def random_string(length=None):
    """Generates a random string from urandom.

    :param length: Specify the number of chars in the generated string.
    """
    chars = string.ascii_uppercase + string.digits
    str_length = length if length is not None else random_int()
    return unicode(u''.join(random.choice(chars) for x in range(str_length)))


def random_url():
    """Generate a random url that is totally bogus."""
    url = u"http://{0}.com".format(random_string())
    return url


def make_applog(message=None, status=None):
    """Generate applog instances."""
    if status is None:
        status = random_int(max=3)

    if message is None:
        message = random_string(100)

    alog = AppLog(**{
        'user': random_string(10),
        'component': random_string(10),
        'status': status,
        'message': message,
        'payload': u'',
    })
    return alog


def make_tag(name=None):
    if not name:
        name = random_string(255)

    return Tag(name)


def make_bookmark(user=None):
    """Generate a fake bookmark for testing use."""
    bmark = Bmark(random_url(),
                  username=u"admin",
                  desc=random_string(),
                  ext=random_string(),
                  tags=u"bookmarks")

    if user:
        bmark.username = user.username
        bmark.user = user

    DBSession.add(bmark)
    DBSession.flush()
    return bmark


def make_user(username=None):
    """Generate a fake user to test against."""
    user = User()

    if not username:
        username = random_string(10)

    user.username = username

    DBSession.add(user)
    DBSession.flush()
    return user
