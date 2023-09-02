from playwright.sync_api import sync_playwright
from time import sleep
with sync_playwright() as p:
    navegador=p.chromium.launch(headless=False) #headless
    pag= navegador.new_page()
    sleep(1)
    pag.goto("https://translate.google.com/")
    sleep(1)
    pag.locator('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]').click()
    sleep(1)
    pag.fill('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea','''I do not love you as if you were salt-rose, or topaz,
or the arrow of carnations the fire shoots off.
I love you as certain dark things are to be loved,
in secret, between the shadow and the soul.


''')
    sleep(1)
    pag.locator('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/div[4]/div[2]/div/div[2]/span/button/div[3]').click()
    sleep(70)

