"""
orion-inspector.py -- Orion Advisor login flow selector scanner.

Fully automatic — no interactive pauses. Navigates the Orion login flow,
captures HTML + element maps at each observable stage, writes a selector spec.

Stages:
  1. Login page loaded (always captured)
  2. After username fill (if ORION_USER env var or Secrets Manager available)
  3. After password fill + submit attempt
  4. Post-submit page (OTP challenge or dashboard)
  5. OTP input page HTML capture (stops here — does not submit OTP)

Usage:
    python .tools/orion-inspector.py [--out-dir <path>] [--headless]

Credentials (optional — captures more stages if available):
    Set env vars:  ORION_USER=<email>  ORION_PASS=<password>
    Or store in:   AWS Secrets Manager at orion/credentials
                   {"username": "...", "password": "..."}

Output:
    <out-dir>/stage-{N}-{label}.png    screenshot
    <out-dir>/stage-{N}-{label}.html   full page source
    <out-dir>/stage-{N}-{label}.json   extracted elements
    <out-dir>/selector-spec.md         assembled spec for orion_export.ts
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright, Page, ConsoleMessage, TimeoutError as PWTimeoutError
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
    sys.exit(2)

CHROMIUM_PATH = r"C:\Users\AndrewBerman\AppData\Local\ms-playwright\chromium-1208\chrome-win64\chrome.exe"
ORION_LOGIN_URL = "https://login.orionadvisor.com/"
NAV_TIMEOUT = 30_000
SETTLE_MS = 2_000


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def log(msg: str) -> None:
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)


def get_credentials() -> tuple[str, str] | tuple[None, None]:
    """Try env vars first, then Secrets Manager."""
    user = os.environ.get("ORION_USER")
    pwd = os.environ.get("ORION_PASS")
    if user and pwd:
        log("[creds] Using ORION_USER / ORION_PASS env vars.")
        return user, pwd

    try:
        result = subprocess.run(
            ["aws", "secretsmanager", "get-secret-value",
             "--secret-id", "orion/credentials",
             "--query", "SecretString", "--output", "text"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0:
            secret = json.loads(result.stdout.strip())
            user = secret.get("username") or secret.get("user")
            pwd = secret.get("password") or secret.get("pass")
            if user and pwd:
                log("[creds] Loaded from Secrets Manager: orion/credentials")
                return user, pwd
    except Exception:
        pass

    log("[creds] No credentials available -- capturing login page structure only.")
    return None, None


def extract_elements(page: Page) -> dict:
    try:
        return page.evaluate("""() => {
            const toObj = el => ({
                tag: el.tagName.toLowerCase(),
                id: el.id || null,
                name: el.getAttribute('name') || null,
                type: el.getAttribute('type') || null,
                placeholder: el.getAttribute('placeholder') || null,
                class: (el.className || '').toString().slice(0, 200),
                data_attrs: Object.fromEntries(
                    [...el.attributes]
                        .filter(a => a.name.startsWith('data-'))
                        .map(a => [a.name, a.value])
                ),
                aria_label: el.getAttribute('aria-label') || null,
                text: (el.innerText || '').trim().slice(0, 120),
                selector_candidates: [
                    el.id ? '#' + el.id : null,
                    el.getAttribute('name') ? '[name="' + el.getAttribute('name') + '"]' : null,
                    el.getAttribute('placeholder')
                        ? '[placeholder="' + el.getAttribute('placeholder') + '"]' : null,
                    el.getAttribute('type') && el.tagName.toLowerCase() !== 'button'
                        ? el.tagName.toLowerCase() + '[type="' + el.getAttribute('type') + '"]' : null,
                    el.getAttribute('aria-label')
                        ? '[aria-label="' + el.getAttribute('aria-label') + '"]' : null,
                ].filter(Boolean),
            });

            return {
                url: location.href,
                title: document.title,
                inputs: [...document.querySelectorAll('input, textarea, select')].map(toObj),
                buttons: [...document.querySelectorAll(
                    'button, [role="button"], input[type="submit"], input[type="button"]'
                )].map(toObj),
                links: [...document.querySelectorAll('a')].slice(0, 20).map(toObj),
                forms: [...document.querySelectorAll('form')].map(f => ({
                    id: f.id || null,
                    action: f.action || null,
                    method: f.method || null,
                    class: (f.className || '').toString().slice(0, 100),
                })),
                iframes: [...document.querySelectorAll('iframe')].map(f => ({
                    src: f.src || null, id: f.id || null, name: f.name || null,
                })),
            };
        }""")
    except Exception as e:
        return {"error": str(e)}


def capture(page: Page, out: Path, n: int, label: str, console_log: list) -> dict:
    safe = label.replace(" ", "-").replace("/", "-")
    prefix = f"stage-{n:02d}-{safe}"

    shot = out / f"{prefix}.png"
    page.screenshot(path=str(shot), full_page=True)

    html = out / f"{prefix}.html"
    content = page.content()
    html.write_text(content, encoding="utf-8")

    elems = extract_elements(page)
    data = {
        "stage": n, "label": label, "url": page.url,
        "elements": elems, "console_log": list(console_log),
    }
    (out / f"{prefix}.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    n_in = len(elems.get("inputs", []))
    n_btn = len(elems.get("buttons", []))
    log(f"  Stage {n}: {label} | {n_in} inputs, {n_btn} buttons | {shot.name}")
    console_log.clear()
    return data


def build_spec(stages: list[dict], out: Path) -> None:
    lines = [
        "# Orion Advisor Login Flow — Selector Spec",
        f"Generated: {stamp()}",
        "Source: orion-inspector.py automated scan",
        "",
    ]
    for s in stages:
        elems = s.get("elements", {})
        inputs = elems.get("inputs", [])
        buttons = elems.get("buttons", [])
        iframes = elems.get("iframes", [])

        lines += [f"## Stage {s['stage']}: {s['label']}", f"URL: `{s['url']}`", ""]

        if inputs:
            lines.append("### Inputs")
            for i in inputs:
                cands = " | ".join(f"`{c}`" for c in i.get("selector_candidates", []))
                lines.append(
                    f"- **{i['tag']}** type=`{i['type']}` "
                    f"id=`{i['id']}` name=`{i['name']}` "
                    f"placeholder=`{i['placeholder']}` "
                    f"aria-label=`{i['aria_label']}`  "
                    f"-- {cands or 'no candidates'}"
                )
            lines.append("")

        if buttons:
            lines.append("### Buttons")
            for b in buttons[:8]:
                cands = " | ".join(f"`{c}`" for c in b.get("selector_candidates", []))
                lines.append(
                    f"- **{b['tag']}** text=`{b['text']}` "
                    f"id=`{b['id']}` type=`{b['type']}`  "
                    f"-- {cands or 'no candidates'}"
                )
            lines.append("")

        if iframes:
            lines.append(f"### iframes")
            for f in iframes:
                lines.append(f"- src=`{f['src']}` id=`{f['id']}` name=`{f['name']}`")
            lines.append("")

        forms = elems.get("forms", [])
        if forms:
            lines.append("### Forms")
            for f in forms:
                lines.append(f"- id=`{f['id']}` action=`{f['action']}` method=`{f['method']}`")
            lines.append("")

    (out / "selector-spec.md").write_text("\n".join(lines), encoding="utf-8")
    log(f"[spec] {out / 'selector-spec.md'}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--headless", action="store_true")
    args = parser.parse_args()

    out = Path(args.out_dir) if args.out_dir else Path(".frontend-dev-results") / f"orion-{stamp()}"
    out.mkdir(parents=True, exist_ok=True)
    log(f"Output: {out.resolve()}\n")

    username, password = get_credentials()
    stages: list[dict] = []
    console_log: list[str] = []

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            executable_path=CHROMIUM_PATH,
            headless=args.headless,
            args=["--start-maximized"] if not args.headless else [],
        )
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        page.on("console", lambda m: console_log.append(f"[{m.type}] {m.text}"))

        # Stage 1: Login page
        log(f"Navigating to {ORION_LOGIN_URL} ...")
        page.goto(ORION_LOGIN_URL, wait_until="networkidle", timeout=NAV_TIMEOUT)
        page.wait_for_timeout(SETTLE_MS)
        stages.append(capture(page, out, 1, "login-page", console_log))

        if not username:
            log("\nNo credentials — stopping after login page capture.")
            browser.close()
            build_spec(stages, out)
            return

        # Stage 2: Fill username + click Continue (step 1 of 2-step login)
        log("Filling username ...")
        page.fill('#Username', username)
        page.wait_for_timeout(600)
        stages.append(capture(page, out, 2, "username-filled", console_log))

        log("Clicking Continue (step 1 submit) ...")
        page.click('#btn_userName')
        # Wait for password field to appear (page swaps in-place)
        try:
            page.wait_for_selector('#password', timeout=10_000)
        except PWTimeoutError:
            log("  WARN: #password not found after Continue — capturing current state")
        page.wait_for_timeout(800)
        stages.append(capture(page, out, 3, "password-page", console_log))

        # Stage 3: Fill password + click Log In (step 2 of 2-step login)
        log("Filling password ...")
        if page.locator('#password').count() > 0:
            page.fill('#password', password)
            log("  Password filled via: #password")
        else:
            log("  WARN: #password not found — login may have failed at step 1")
        page.wait_for_timeout(600)
        stages.append(capture(page, out, 4, "password-filled", console_log))

        log("Clicking Log In (#submit) ...")
        pre_url = page.url
        try:
            page.click('#submit')
        except Exception:
            log("  WARN: #submit not found — trying Enter")
            page.keyboard.press("Enter")

        # Wait for URL to change (navigation away from login page) or OTP on same URL
        # Give 15s for server round-trip + any redirect chain
        try:
            page.wait_for_function(
                f"() => document.title !== 'Login' || location.href !== '{pre_url}'",
                timeout=15_000,
            )
            log(f"  Navigation detected: {page.url}")
        except PWTimeoutError:
            log("  WARN: No navigation detected after 15s — possible CAPTCHA or auth error")
        page.wait_for_timeout(2_000)
        stages.append(capture(page, out, 5, "post-login", console_log))

        # Stage 6: OTP challenge detection
        log("Checking for OTP challenge ...")
        otp_selectors = [
            'input[type="tel"]', 'input[autocomplete="one-time-code"]',
            '#AuthCode', '#Code', '#otp', '#verificationCode',
            '[name="otp"]', '[name="code"]', '[name="token"]', '[name="AuthCode"]',
            '[placeholder*="code" i]', '[placeholder*="otp" i]', '[placeholder*="verif" i]',
        ]
        otp_found = any(page.locator(sel).count() > 0 for sel in otp_selectors)
        # Also check if #passwordError is visible (login failure)
        login_failed = page.locator('#passwordError').is_visible()
        if login_failed:
            log("  LOGIN FAILED: #passwordError is visible -- wrong credentials or reCAPTCHA blocked")
        elif otp_found:
            log("  OTP challenge detected -- capturing page structure (not submitting).")
        else:
            log("  No OTP challenge detected -- likely logged in. Capturing post-auth page.")
        stages.append(capture(page, out, 6, "otp-or-post-auth", console_log))

        browser.close()

    build_spec(stages, out)

    log(f"\n=== DONE === {len(stages)} stages captured")
    log(f"Spec: {out / 'selector-spec.md'}")
    log(f"Screenshots: {out}/stage-*.png")


if __name__ == "__main__":
    main()
