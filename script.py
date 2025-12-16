import velesresearch as vls
import anyascii

AUT_items = """cegła
sznurek
beczka
butelka
długopis
grzebień
gumka recepturka
guzik
linijka
mop
opona
parasol
poduszka
puszka
spinacz
wieszak
zapalniczka
doniczka
pudełko
patyk""".splitlines()

AUT_pages = []
for item in AUT_items:
    item_a = anyascii.anyascii(item)
    p = vls.page(
        f"AUT_{item_a}",
        vls.info(f"AUT_intro_{item_a}", "Wymyśl zastosowania"),
        vls.panel(
            f"panel_AUT_{item_a}",
            vls.image(f"img_{item_a}", vls.convertImage(f"./images/{item_a}.png")),
            vls.multipleText(
                f"AUT_{item_a}",
                f"Wymyśl zastosowania dla: {item}",
                [{"name": f"{i+1}"} for i in range(3)],
            ),
        ),
    )
    AUT_pages.append(p)

vls.survey(AUT_pages, customCode=vls.getJS("./custom_buttons.js"))
