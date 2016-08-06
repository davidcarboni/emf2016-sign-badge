from http_client import get
import ugfx
import buttons
import wifi
from dialogs import notice

DIALOG_TITLE = "EMF Number One"


def dialog(message):
    notice(message, title=DIALOG_TITLE)
    drawui()

    
if not wifi.is_connected():
    dialog("It looks like your wifi isn't connected, so you probably won't be able to access the sign. You may want to reset your badge?")


def wiggle():
    request("Let's give it some wiggle!", "I see you baby, #shakingthadass!!", "/lights")
    drawui()


def disco():
    request("Let's get disco, honey!", "Hope you enjoyed some disco action!!", "/disco")
    drawui()


def request(before, after, uri):
    dialog(before)
    drawui()
    try:
        url = "http://carboni.io" + uri
        print("GET: " + url)
        response = get(url).raise_for_status().content
        print("EMF number one says: " + repr(response))
        dialog("Got a reply from emf number one: " + repr(response))
        dialog(after)
        print("finish!")
    except Exception as ex:
        print("Error: " + repr(ex))
        dialog("Aw shoot, we got an error: " + repr(ex) + " - it might be that wifi disconnected?")


def drawui():
    ugfx.init()
    buttons.init()
    ugfx.clear(ugfx.html_color(0x87F717))

    ugfx.set_default_font(ugfx.FONT_MEDIUM)

    ugfx.fill_circle(50,50, 20, ugfx.WHITE)
    ugfx.fill_circle(50, 100, 20, ugfx.WHITE)

    ugfx.text(45, 45, "A", ugfx.RED)
    ugfx.text(45, 95, "B", ugfx.RED)

    ugfx.text(95, 45, "Wiggle the lights", ugfx.WHITE)
    ugfx.text(95, 95, "Disco Inferno", ugfx.WHITE)

    ugfx.fill_polygon(270,50, [ [0,0], [40,0], [40, 175], [0, 175] ], ugfx.RED)#  , [230, 100], [230, 60]
    ugfx.fill_polygon(270,50, [ [0,0], [-20,10], [-20, 50], [0, 40] ], ugfx.RED)#  , [230, 100], [230, 60]

    ugfx.area(283, 61, 14, 10, ugfx.WHITE)
    ugfx.area(283, 79, 14, 10, ugfx.WHITE)
    ugfx.area(283, 97, 14, 10, ugfx.WHITE)
    ugfx.area(283, 115, 14, 10, ugfx.WHITE)
    ugfx.area(283, 133, 14, 10, ugfx.WHITE)
    ugfx.area(283, 151, 14, 10, ugfx.WHITE)
    ugfx.area(283, 169, 14, 10, ugfx.WHITE)
    ugfx.area(283, 187, 14, 10, ugfx.WHITE)


drawui()
while True:
    if buttons.is_triggered("BTN_A"):
        wiggle()
    elif buttons.is_triggered("BTN_B"):
        disco()