from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
    )

    page = browser.new_page()

    page.goto("https://orteil.dashnet.org/cookieclicker/")

    page.wait_for_timeout(15000)

    while True:

        # 點主餅乾
        page.evaluate("Game.ClickCookie()")

        # 黃金餅乾
        page.evaluate("Game.shimmers.forEach(s => s.pop())")

        # 自動購買升級
        page.evaluate("Game.UpgradesInStore.forEach(u => u.buy())")

        # ROI 最佳建築選擇
        page.evaluate("""
        let best = null;
        let bestRatio = 0;

        Game.ObjectsById.forEach(o => {
            let ratio = o.storedCps / o.price;

            if (ratio > bestRatio) {
                bestRatio = ratio;
                best = o;
            }
        });

        if (best) best.buy();
        """)

        time.sleep(0.01)