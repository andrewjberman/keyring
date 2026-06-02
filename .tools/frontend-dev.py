"""
frontend-dev CLI — constitution-driven Playwright visual test runner.

Replaces the unregistered /frontend-dev plugin command. Invoked by the
frontend-dev Skill (or directly via Bash) to run a scripted browser
scenario against the portal, capture console errors + screenshots, and
emit an ACTIONABLE_FIXES JSON block the agent can parse and act on.

Usage:
    python .tools/frontend-dev.py \\
        --constitution portal/.frontend-dev/testing/<name>.json \\
        [--base http://localhost:5175] \\
        [--scenario <scenario_name>] \\
        [--out-dir .frontend-dev-results/<timestamp>]

Exit codes:
    0 - scenario(s) PASS (all acceptance criteria met, no blocking issues)
    1 - scenario(s) FAIL (blocking issues found)
    2 - harness error (Playwright missing, server down, bad constitution)

Output:
    <out-dir>/results.json       - full machine-readable results
    <out-dir>/*.png              - screenshots
    stdout                       - human-readable log + ACTIONABLE_FIXES block

Constitution schema: see portal/.frontend-dev/testing/README.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from playwright.sync_api import (
        Page,
        TimeoutError as PWTimeoutError,
        sync_playwright,
    )
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
    sys.exit(2)


# Fallback executable if the system-Edge channel is unavailable. Updated 2026-06-02
# from the stale chromium-1208 (slow ~6.7s) to chromium-1223 (~2s). Primary path is
# the system-Edge channel (see launch logic below, ~1s). Root-cause note: the agent
# headless-smoke outage was the Playwright MCP running under bun (bun cannot drive
# Playwright's browser transport); this Python runner uses Python-Playwright (its own
# Node driver) and was only ever slow/stale-pinned, never bun-broken.
CHROMIUM_PATH = r"C:\Users\AndrewBerman\AppData\Local\ms-playwright\chromium-1223\chrome-win64\chrome.exe"


def log(msg: str) -> None:
    # Windows cp1252 stdout chokes on chart-legend arrows / em-dashes from page text.
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"), flush=True)


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_constitution(path: Path) -> dict[str, Any]:
    if not path.exists():
        log(f"ERROR: constitution not found: {path}")
        sys.exit(2)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        log(f"ERROR: constitution JSON invalid: {e}")
        sys.exit(2)


def do_login(page: Page, login_cfg: dict[str, Any], base: str) -> bool:
    # Always start at base — the app redirects to login if unauthenticated.
    # Going directly to /login may 404 if the app mounts auth at root.
    email = login_cfg["email"]
    password = login_cfg["password"]

    page.goto(base, wait_until="networkidle", timeout=30000)
    log(f"  AUTH: landed at {page.url}")

    # If we're already past login (e.g. token in storage), done.
    if "login" not in page.url.lower() and page.locator('input[type="password"]').count() == 0:
        log("  AUTH: already authenticated")
        return True

    email_count = page.locator('input[type="email"]').count()
    pwd_count = page.locator('input[type="password"]').count()
    log(f"  AUTH: form inputs email={email_count} password={pwd_count}")
    if pwd_count == 0:
        log(f"  AUTH: login form not found at {page.url}")
        return False

    email_loc = page.locator('input[type="email"]').first
    pwd_loc = page.locator('input[type="password"]').first
    if email_count == 0:
        log("  AUTH: email input missing (pwd-only login?)")
        return False
    email_loc.fill(email)
    pwd_loc.fill(password)

    submit = page.locator('button[type="submit"]')
    log(f"  AUTH: submit button count={submit.count()}")
    if submit.count() > 0:
        submit.first.click()
    else:
        pwd_loc.press("Enter")

    try:
        page.wait_for_url(lambda u: "login" not in u.lower(), timeout=20000)
    except PWTimeoutError:
        page.wait_for_timeout(4000)

    cur = page.url
    log(f"  AUTH: post-submit URL={cur}")
    token = page.evaluate("() => localStorage.getItem('accessToken')")
    log(f"  AUTH: localStorage token present={token is not None and len(str(token)) > 20}")
    if "login" not in cur.lower():
        return True

    # Fallback: localStorage token + client-side push
    token = page.evaluate("() => localStorage.getItem('accessToken')")
    if token and len(str(token)) > 20:
        target = login_cfg.get("post_login_path", "/advisor-intelligence")
        page.evaluate(
            "(p) => { window.history.pushState({}, '', p); "
            "window.dispatchEvent(new PopStateEvent('popstate')); }",
            target,
        )
        page.wait_for_timeout(2500)
        return "login" not in page.url.lower()

    return False


class ScenarioRunner:
    def __init__(self, page: Page, base: str, out_dir: Path, scenario: dict[str, Any]):
        self.page = page
        self.base = base
        self.out_dir = out_dir
        self.scenario = scenario
        self.name = scenario.get("name", "unnamed")
        self.console_errors: list[str] = []
        self.page_errors: list[str] = []
        self.issues: list[dict[str, Any]] = []
        self.screenshots: list[str] = []
        self.ss_idx = 0
        self._hook_console()

    def _hook_console(self) -> None:
        def on_console(msg):
            if msg.type == "error":
                t = msg.text
                if "401" in t or "403" in t:
                    return  # pre-auth noise
                self.console_errors.append(t)
                log(f"  [CONSOLE ERROR] {t[:160]}")

        def on_pageerror(err):
            t = f"PAGE_ERROR: {err.message}"
            self.page_errors.append(t)
            log(f"  [PAGE ERROR] {t[:160]}")

        self.page.on("console", on_console)
        self.page.on("pageerror", on_pageerror)

    def screenshot(self, label: str) -> str:
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in label)[:50]
        fname = self.out_dir / f"{self.ss_idx:02d}-{self.name}-{safe}.png"
        self.ss_idx += 1
        try:
            self.page.screenshot(path=str(fname), full_page=False)
            self.screenshots.append(str(fname))
        except Exception as e:
            log(f"  SS FAILED: {label} ({e})")
        return str(fname)

    def fail(self, description: str, severity: str = "blocking", **extra) -> None:
        issue = {"description": description, "severity": severity, "scenario": self.name}
        issue.update(extra)
        self.issues.append(issue)
        log(f"  FAIL [{severity}]: {description}")

    def nav(self, path: str) -> None:
        """Client-side navigation via pushState — preserves auth context.

        Avoids page.goto() / window.location.reload() which drop React auth state
        in the portal. If pushState doesn't take, that's a real issue the agent
        needs to see — do not paper over with a reload.
        """
        self.page.evaluate(
            "(p) => { window.history.pushState({}, '', p); "
            "window.dispatchEvent(new PopStateEvent('popstate')); }",
            path,
        )
        self.page.wait_for_timeout(2500)
        log(f"  NAV: pushState({path}) -> url={self.page.url}")

    def _resolve_locator(self, step: dict[str, Any]):
        if "selector" in step:
            return self.page.locator(step["selector"])
        if "text" in step:
            return self.page.locator("button, [role='tab'], [role='button']").filter(
                has_text=step["text"]
            )
        if "role" in step:
            return self.page.get_by_role(step["role"], name=step.get("name"), exact=step.get("exact", False))
        raise ValueError(f"step has no locator: {step}")

    def run_step(self, step: dict[str, Any]) -> None:
        action = step.get("action")
        if action == "goto":
            path = step["path"]
            full = path if path.startswith("http") else self.base + path
            self.page.goto(full, wait_until="networkidle", timeout=step.get("timeout_ms", 20000))
            self.page.wait_for_timeout(step.get("wait_ms", 500))
        elif action == "nav":
            self.nav(step["path"])
        elif action == "click":
            loc = self._resolve_locator(step).first
            loc.click(timeout=step.get("timeout_ms", 5000))
            self.page.wait_for_timeout(step.get("wait_ms", 500))
        elif action == "click_tab":
            loc = self.page.locator('[role="tab"], button').filter(has_text=step["text"]).first
            if loc.count() == 0:
                self.fail(f"tab not found: {step['text']}", severity="blocking", step=step)
                return
            loc.click(timeout=step.get("timeout_ms", 5000))
            self.page.wait_for_timeout(step.get("wait_ms", 1500))
        elif action == "wait":
            self.page.wait_for_timeout(step["ms"])
        elif action == "screenshot":
            self.screenshot(step.get("label", f"step-{self.ss_idx}"))
        elif action == "assert_visible":
            loc = self._resolve_locator(step)
            if loc.count() == 0:
                self.fail(
                    step.get("message", f"expected visible: {step}"),
                    severity=step.get("severity", "blocking"),
                    step=step,
                )
        elif action == "assert_not_blank":
            self._check_not_blank(step)
        elif action == "rapid_cycle":
            self._rapid_cycle(step)
        elif action == "assert_no_console_errors":
            self._check_console_errors(step)
        elif action == "inspect":
            self._inspect(step)
        elif action == "js_eval":
            result = self.page.evaluate(step["script"])
            self.page.wait_for_timeout(step.get("wait_ms", 500))
            log(f"  EVAL: {step['script']!r} -> {result}")
        else:
            self.fail(f"unknown action: {action}", severity="blocking", step=step)

    def _inspect(self, step: dict[str, Any]) -> None:
        """Capture observed values into issues[] as severity='info' entries.

        step = {
          "action": "inspect",
          "label": "sidebar-nav-items",
          "selector": "nav a",            # CSS selector for elements
          "extract": "textContent"         # 'textContent' (default) | 'href' | 'count'
        }
        Extracted values are written to the issues list as info-severity records
        so the harness exits 0 but the agent can read them in ACTIONABLE_FIXES.
        """
        label = step.get("label", "inspect")
        sel = step["selector"]
        extract = step.get("extract", "textContent")
        if extract == "count":
            value = self.page.locator(sel).count()
            self.issues.append({
                "severity": "info", "scenario": self.name,
                "description": f"INSPECT[{label}] count({sel}) = {value}",
            })
            log(f"  INSPECT[{label}] count = {value}")
            return
        if extract == "textContent":
            values = self.page.locator(sel).all_text_contents()
            cleaned = [v.strip() for v in values if v.strip()]
            self.issues.append({
                "severity": "info", "scenario": self.name,
                "description": f"INSPECT[{label}] {sel} -> {cleaned}",
            })
            log(f"  INSPECT[{label}] -> {cleaned}")
            return
        if extract == "href":
            values = [
                el.get_attribute("href")
                for el in self.page.locator(sel).element_handles()
            ]
            self.issues.append({
                "severity": "info", "scenario": self.name,
                "description": f"INSPECT[{label}] href({sel}) -> {values}",
            })
            log(f"  INSPECT[{label}] href -> {values}")
            return
        self.fail(f"unknown extract type: {extract}", severity="blocking", step=step)

    def _check_not_blank(self, step: dict[str, Any]) -> None:
        """Assert that a chart container has non-trivial rendered content.

        Works for ApexCharts (.apexcharts-canvas) and Recharts (.recharts-surface).
        'Blank' means the container exists but has 0 child SVG/canvas elements.
        """
        container_sel = step.get("selector", ".apexcharts-canvas, .recharts-surface, svg")
        min_children = step.get("min_children", 1)
        loc = self.page.locator(container_sel)
        n = loc.count()
        if n == 0:
            self.fail(
                step.get("message", f"chart container not found: {container_sel}"),
                severity=step.get("severity", "blocking"),
                step=step,
            )
            return
        # Check first container has content
        child_count = self.page.evaluate(
            "(sel) => { const el = document.querySelector(sel); "
            "return el ? el.querySelectorAll('path, rect, circle, g').length : 0; }",
            container_sel.split(",")[0].strip(),
        )
        if child_count < min_children:
            self.fail(
                step.get("message", f"chart blank: {container_sel} has {child_count} children (<{min_children})"),
                severity=step.get("severity", "blocking"),
                step=step,
                observed_children=child_count,
            )

    def _rapid_cycle(self, step: dict[str, Any]) -> None:
        """Cycle through a list of click targets rapidly.

        step = {
          "action": "rapid_cycle",
          "targets": [{"text": "GEO"}, {"text": "ADV"}, {"text": "OFC"}],
          "repeat": 10,
          "interval_ms": 50,
          "check_between": {"selector": ".apexcharts-canvas", "min_children": 1},
          "screenshot_every": 5
        }
        """
        targets = step["targets"]
        repeat = step.get("repeat", 10)
        interval = step.get("interval_ms", 50)
        check = step.get("check_between")
        ss_every = step.get("screenshot_every", 0)

        blanks = 0
        for i in range(repeat):
            for t_idx, tgt in enumerate(targets):
                try:
                    loc = self._resolve_locator(tgt).first
                    loc.click(timeout=3000)
                except Exception as e:
                    self.fail(
                        f"rapid_cycle iter {i} target {t_idx} click failed: {e}",
                        severity="blocking",
                        step=tgt,
                    )
                    return
                self.page.wait_for_timeout(interval)
                if check:
                    sel = check.get("selector", ".apexcharts-canvas, .recharts-surface")
                    min_children = check.get("min_children", 1)
                    primary = sel.split(",")[0].strip()
                    child_count = self.page.evaluate(
                        "(sel) => { const el = document.querySelector(sel); "
                        "return el ? el.querySelectorAll('path, rect, circle, g').length : -1; }",
                        primary,
                    )
                    if child_count == 0:
                        blanks += 1
                        log(f"    BLANK DETECTED iter={i} target_idx={t_idx} sel={primary}")
            if ss_every and (i + 1) % ss_every == 0:
                self.screenshot(f"cycle-{i+1}")

        if blanks > step.get("blank_tolerance", 0):
            self.fail(
                f"rapid_cycle saw {blanks} blank-render events across {repeat}x{len(targets)} toggles (tolerance {step.get('blank_tolerance', 0)})",
                severity="blocking",
                step=step,
                blank_count=blanks,
            )
        else:
            log(f"  OK: rapid_cycle {repeat}x{len(targets)} toggles, blanks={blanks}")

    def _check_console_errors(self, step: dict[str, Any]) -> None:
        crash_kw = step.get("crash_keywords", [
            "typeerror", "uncaught", "cannot read", "is not a function", "page_error",
        ])
        errs = self.console_errors + self.page_errors
        crashes = [e for e in errs if any(k in e.lower() for k in crash_kw)]
        if crashes:
            self.fail(
                f"crash errors: {crashes[0][:200]}",
                severity="blocking",
                step=step,
                all_crashes=crashes[:5],
            )

    def run(self) -> None:
        log(f"\n[SCENARIO] {self.name}")
        for step in self.scenario.get("setup", []):
            self.run_step(step)
        for step in self.scenario.get("steps", []):
            self.run_step(step)
        for step in self.scenario.get("teardown", []):
            self.run_step(step)


def build_actionable_fixes(all_issues: list[dict[str, Any]]) -> dict[str, Any]:
    """Coerce issues into the ACTIONABLE_FIXES schema.

    The tester cannot auto-generate file_path/old_code/new_code for UI
    regressions — those require human/agent judgment. We emit issues
    without fix code; the coordinating agent is responsible for editing.
    """
    return {
        "status": "FAIL" if any(i.get("severity") == "blocking" for i in all_issues) else "PASS",
        "issues": all_issues,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--constitution", required=True, type=Path)
    ap.add_argument("--base", default="http://localhost:5175")
    ap.add_argument("--scenario", default=None, help="run only this scenario name")
    ap.add_argument("--out-dir", default=None, type=Path)
    ap.add_argument("--headless", action="store_true", default=True)
    ap.add_argument("--headed", dest="headless", action="store_false")
    ap.add_argument("--login-email", default=None, help="override constitution login.email")
    ap.add_argument("--login-password", default=None, help="override constitution login.password")
    args = ap.parse_args()

    cfg = load_constitution(args.constitution)
    out_dir = args.out_dir or Path(".frontend-dev-results") / now_stamp()
    out_dir.mkdir(parents=True, exist_ok=True)
    log(f"[frontend-dev] constitution={args.constitution} base={args.base} out={out_dir}")

    scenarios = cfg.get("scenarios", [])
    if args.scenario:
        scenarios = [s for s in scenarios if s.get("name") == args.scenario]
        if not scenarios:
            log(f"ERROR: scenario '{args.scenario}' not found in constitution")
            return 2

    all_issues: list[dict[str, Any]] = []
    all_screenshots: list[str] = []
    all_console: list[str] = []

    with sync_playwright() as p:
        launch_kwargs = {"headless": args.headless}
        # Prefer system Edge (Chromium-family, current, ~1s, no bundled-revision
        # dependency). Fall back to the pinned bundled chromium, then Playwright default.
        try:
            browser = p.chromium.launch(channel="msedge", **launch_kwargs)
        except Exception:
            if Path(CHROMIUM_PATH).exists():
                launch_kwargs["executable_path"] = CHROMIUM_PATH
            browser = p.chromium.launch(**launch_kwargs)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        try:
            if "login" in cfg:
                if args.login_email:
                    cfg["login"] = {**cfg["login"], "email": args.login_email}
                if args.login_password:
                    cfg["login"] = {**cfg["login"], "password": args.login_password}
                log(f"[AUTH] logging in as {cfg['login'].get('email')}")
                if not do_login(page, cfg["login"], args.base):
                    log("ERROR: login failed")
                    browser.close()
                    result = {
                        "status": "FAIL",
                        "issues": [{"description": "login failed", "severity": "blocking"}],
                        "screenshots": [],
                        "console_errors": [],
                    }
                    (out_dir / "results.json").write_text(json.dumps(result, indent=2))
                    _emit_block(result)
                    return 1
                log("[AUTH] OK")

            for scn in scenarios:
                runner = ScenarioRunner(page, args.base, out_dir, scn)
                try:
                    runner.run()
                except Exception as e:
                    runner.fail(f"scenario crashed: {e}", severity="blocking")
                    log(traceback.format_exc())
                all_issues.extend(runner.issues)
                all_screenshots.extend(runner.screenshots)
                all_console.extend(runner.console_errors + runner.page_errors)
        finally:
            browser.close()

    result = {
        "status": "FAIL" if any(i.get("severity") == "blocking" for i in all_issues) else "PASS",
        "issues": all_issues,
        "screenshots": all_screenshots,
        "console_errors": sorted(set(all_console)),
        "constitution": str(args.constitution),
        "out_dir": str(out_dir),
    }
    (out_dir / "results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    _emit_block(result)
    return 0 if result["status"] == "PASS" else 1


def _emit_block(result: dict[str, Any]) -> None:
    log("")
    log("---ACTIONABLE_FIXES_START---")
    log(json.dumps(result, indent=2))
    log("---ACTIONABLE_FIXES_END---")


if __name__ == "__main__":
    sys.exit(main())
