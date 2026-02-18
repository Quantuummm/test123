"""Extract MCATalyst question-bank data via the app's public API using Playwright.

Usage:
  python extract_mcat_report_playwright.py --out all_questions.json
"""

import argparse
import asyncio
import json
from playwright.async_api import async_playwright

APP_ID = "6914dd3b63a9f7b967491eba"
API_BASE = f"https://base44.app/api/apps/{APP_ID}/entities/Question"


async def fetch_all_questions():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://app.mcat-alyst.com/home", wait_until="domcontentloaded")
        data = await page.evaluate(
            """async (apiBase) => {
                const q = { is_active: true };
                const url = apiBase + '?q=' + encodeURIComponent(JSON.stringify(q));
                const resp = await fetch(url);
                return await resp.json();
            }""",
            API_BASE,
        )
        await browser.close()
        return data


async def main(out_path: str):
    rows = await fetch_all_questions()
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(rows)} questions to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="all_questions.json")
    args = parser.parse_args()
    asyncio.run(main(args.out))
