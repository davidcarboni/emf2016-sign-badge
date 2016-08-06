from http_client import *
from buttons import *
from dialogs import *


def wiggle():
    request("Let's give it some wiggle!", "Hopefully you saw the lights wiggle!!", "/lights")


def disco():
    request("Let's get disco, honey!", "Hopefully you saw some disco action!!", "/disco")


def request(before, after, uri):
    notice(before)
    try:
        response = get("http://carboni.io/" + uri).raise_for_status().content
        print("EMF number one says: " + repr(response))
        notice("Got a reply from emf number one: " + repr(response))
        notice(after)
        print("finish!")
    except Exception as ex:
        print("Error: " + repr(ex))
        notice("Aw shoot, we got an error: " + repr(ex))


while True:
    if is_triggered("BTN_A"):
        wiggle()
    elif is_triggered("BTN_B"):
        disco()


