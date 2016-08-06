from http_client import *
from buttons import *
from dialogs import *

DIALOG_TITLE = "EMF Number One

def wiggle():
    request("Let's give it some wiggle!", "Hopefully you saw the lights wiggle!!", "/lights")


def disco():
    request("Let's get disco, honey!", "Hopefully you saw some disco action!!", "/disco")


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


