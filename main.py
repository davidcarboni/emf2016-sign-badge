from http_client import get
from buttons import *
from dialogs import notice
from wifi import is_connected


DIALOG_TITLE = "EMF Number One"


if not is_connected():
    notice("It looks like your wifi isn't connected, so you probably won't be able to access the sign. You may want to reset your badge?", DIALOG_TITLE)


def wiggle():
    request("Let's give it some wiggle!", "I see you baby, #shakingthadass!!", "/lights")


def disco():
    request("Let's get disco, honey!", "Hope you enjoyed some disco action!!", "/disco")


def request(before, after, uri):
    notice(before, title=DIALOG_TITLE)
    try:
        url = "http://carboni.io" + uri
        print("GET: " + url)
        response = get(url).raise_for_status().content
        print("EMF number one says: " + repr(response))
        notice("Got a reply from emf number one: " + repr(response), title=DIALOG_TITLE)
        notice(after, title=DIALOG_TITLE)
        print("finish!")
    except Exception as ex:
        print("Error: " + repr(ex))
        notice("Aw shoot, we got an error: " + repr(ex), title=DIALOG_TITLE)


while True:
    if is_triggered("BTN_A"):
        wiggle()
    elif is_triggered("BTN_B"):
        disco()


