"""
AC6 hardware screenshot validation for DASH_STSTRP.001 (commit c9b0f649)
Read-only. No code changes.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright, Page

BASE_URL = "http://localhost:5175"
OUT_DIR = Path("C:/Windows/Temp/ac6_strips")
OUT_DIR.mkdir(parents=True, exist_ok=True)

results: list[dict] = []


def auth_via_devbypass(page: Page) -> bool:
    """Navigate to root, wait for React mount, call devBypass."""
    print("INFO: Loading root URL...")
    page.goto(BASE_URL + "/")
    # Wait for React app to mount (window.__devBypass is registered in useEffect)
    try:
        page.wait_for_function("typeof window.__devBypass === 'function'", timeout=15000)
        print("INFO: React mounted, calling devBypass()...")
        page.evaluate("window.__devBypass()")
        # Wait for auth state to propagate — URL should leave /login
        page.wait_for_function(
            "!window.location.pathname.includes('/login') && !window.location.pathname.includes('/auth')",
            timeout=8000
        )
        page.wait_for_timeout(1500)
        print(f"INFO: Authenticated. Current URL: {page.url}")
        return True
    except Exception as e:
        print(f"WARN: devBypass failed: {e}")
        page.screenshot(path=str(OUT_DIR / "auth_failure.png"))
        return False


def goto_and_wait(page: Page, path: str, wait_text: str | None = None) -> None:
    page.goto(BASE_URL + path)
    page.wait_for_load_state("networkidle", timeout=12000)
    if wait_text:
        try:
            page.wait_for_selector(f"text={wait_text}", timeout=8000)
        except Exception:
            pass
    page.wait_for_timeout(2000)


def check_strip_wrapping(page: Page, anchor_text: str) -> dict:
    """
    Find a strip by a unique text anchor inside it, then check if
    the flex row children all share the same offsetTop (single row).
    """
    info = page.evaluate("""(anchorText) => {
        // Find element containing the anchor text
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let textNode;
        while ((textNode = walker.nextNode())) {
            if (textNode.textContent.trim() === anchorText) {
                // Walk up to find the flex-row container (direct parent of pills)
                let el = textNode.parentElement;
                for (let i = 0; i < 6; i++) {
                    if (!el) break;
                    const style = window.getComputedStyle(el);
                    if (style.display === 'flex' && el.children.length >= 4) {
                        // Found a flex container with multiple children — this is the strip row
                        const children = Array.from(el.children).filter(c => c.offsetWidth > 0);
                        const rects = children.map(c => c.getBoundingClientRect());
                        const tops = rects.map(r => Math.round(r.top));
                        const uniqueTops = [...new Set(tops)];
                        return {
                            found: true,
                            containerWidth: Math.round(el.getBoundingClientRect().width),
                            containerHeight: Math.round(el.getBoundingClientRect().height),
                            childCount: children.length,
                            uniqueRowCount: uniqueTops.length,
                            wraps: uniqueTops.length > 1,
                            tops: tops,
                        };
                    }
                    el = el.parentElement;
                }
                return { found: true, containerFound: false, note: 'flex container not found near anchor' };
            }
        }
        return { found: false };
    }""", anchor_text)
    return info


def screenshot_area_by_text(page: Page, anchor_text: str, label: str) -> str | None:
    """Screenshot the region containing anchor_text by finding its bounding box."""
    filepath = OUT_DIR / f"{label.replace(' ', '_')}.png"
    try:
        # Evaluate to find bbox of container
        bbox = page.evaluate("""(anchorText) => {
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            let textNode;
            while ((textNode = walker.nextNode())) {
                if (textNode.textContent.trim() === anchorText) {
                    let el = textNode.parentElement;
                    for (let i = 0; i < 8; i++) {
                        if (!el) break;
                        const style = window.getComputedStyle(el);
                        if (style.display === 'flex' && el.children.length >= 4) {
                            // Go one level up to include any outer wrapper
                            const parent = el.parentElement || el;
                            const r = parent.getBoundingClientRect();
                            return { x: r.x, y: r.y - 8, width: r.width, height: r.height + 16 };
                        }
                        el = el.parentElement;
                    }
                }
            }
            return null;
        }""", anchor_text)

        if bbox and bbox.get("width", 0) > 0:
            page.screenshot(
                path=str(filepath),
                clip={"x": max(0, bbox["x"]), "y": max(0, bbox["y"]),
                      "width": bbox["width"], "height": max(bbox["height"], 60)}
            )
            return str(filepath)
    except Exception as e:
        print(f"WARN: screenshot_area failed for '{anchor_text}': {e}")
    return None


def run_validation() -> dict:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        # Use default viewport matching a 1366-wide display at 100% zoom
        context = browser.new_context(viewport={"width": 1366, "height": 768}, device_scale_factor=1.0)
        page = context.new_page()

        if not auth_via_devbypass(page):
            print("BLOCKED: Auth failed — cannot proceed with validation")
            browser.close()
            return {"overall": "BLOCKED", "reason": "auth failed"}

        # ── STRIP 1 & 2: Model Portfolios ──────────────────────────────────
        print("\nINFO: Navigating to Model Portfolios...")
        goto_and_wait(page, "/model-portfolios", "Total Holdings")
        page.screenshot(path=str(OUT_DIR / "01_ModelPortfolios_full.png"))

        # AccountDistributionMetrics: anchor = "Total Holdings"
        wrap1 = check_strip_wrapping(page, "Total Holdings")
        ss1 = screenshot_area_by_text(page, "Total Holdings", "01_AccountDistributionMetrics")
        status1 = "PASS" if wrap1.get("found") and not wrap1.get("wraps") else (
            "ELEMENT_NOT_FOUND" if not wrap1.get("found") else "FAIL"
        )
        results.append({"label": "AccountDistributionMetrics", "status": status1, "layout": wrap1, "screenshot": ss1})
        print(f"  AccountDistributionMetrics: {status1} | {wrap1}")

        # AUMGrowthMetrics: anchor = "Total AUA"
        wrap2 = check_strip_wrapping(page, "Total AUA")
        ss2 = screenshot_area_by_text(page, "Total AUA", "02_AUMGrowthMetrics")
        status2 = "PASS" if wrap2.get("found") and not wrap2.get("wraps") else (
            "ELEMENT_NOT_FOUND" if not wrap2.get("found") else "FAIL"
        )
        results.append({"label": "AUMGrowthMetrics", "status": status2, "layout": wrap2, "screenshot": ss2})
        print(f"  AUMGrowthMetrics: {status2} | {wrap2}")

        # ── STRIP 3: AdvisorIntelligence Distribution Snapshot ────────────
        print("\nINFO: Navigating to AdvisorIntelligence...")
        goto_and_wait(page, "/advisor-intelligence")
        page.wait_for_timeout(3000)  # extra wait for data fetch
        page.screenshot(path=str(OUT_DIR / "03_AdvisorIntelligence_Distribution_full.png"))

        # DistributionTab snapshot strip — look for "Snapshot" anchor near the strip
        # The stat strip in DistributionTab has metric labels. Try "Total Accounts" or "Median"
        wrap3 = check_strip_wrapping(page, "Median")
        if not wrap3.get("found"):
            wrap3 = check_strip_wrapping(page, "Total Accounts")
        ss3 = screenshot_area_by_text(page, "Median", "03_SegmentAnalytics_Snapshot")
        status3 = "PASS" if wrap3.get("found") and not wrap3.get("wraps") else (
            "ELEMENT_NOT_FOUND" if not wrap3.get("found") else "FAIL"
        )
        results.append({"label": "SegmentAnalytics_snapshot_strip", "status": status3, "layout": wrap3, "screenshot": ss3})
        print(f"  SegmentAnalytics snapshot: {status3} | {wrap3}")

        # ── STRIP 4: AdvisorIntelligence Books ConsolidatedOverviewPanel ──
        print("\nINFO: Clicking Books tab...")
        try:
            # Try clicking the Books tab button
            books_tab = page.locator("button, [role='tab']").filter(has_text="Books").first
            books_tab.click(timeout=5000)
            page.wait_for_timeout(3000)
        except Exception as e:
            print(f"WARN: Books tab click failed: {e}")
            # Try by text directly
            try:
                page.get_by_role("tab", name="Books").click(timeout=3000)
                page.wait_for_timeout(2000)
            except Exception:
                pass

        page.screenshot(path=str(OUT_DIR / "04_AdvisorIntelligence_Books_full.png"))

        # ConsolidatedOverviewPanel: look for "Firm AUA" or "Total Accounts" in Books context
        wrap4 = check_strip_wrapping(page, "Firm AUA")
        if not wrap4.get("found"):
            wrap4 = check_strip_wrapping(page, "Advisors")
        ss4 = screenshot_area_by_text(page, "Firm AUA", "04_ConsolidatedOverviewPanel")
        status4 = "PASS" if wrap4.get("found") and not wrap4.get("wraps") else (
            "ELEMENT_NOT_FOUND" if not wrap4.get("found") else "FAIL"
        )
        results.append({"label": "ConsolidatedOverviewPanel", "status": status4, "layout": wrap4, "screenshot": ss4})
        print(f"  ConsolidatedOverviewPanel: {status4} | {wrap4}")

        browser.close()

    # ── Summary ────────────────────────────────────────────────────────────
    all_pass = all(r["status"] == "PASS" for r in results)
    not_found = [r["label"] for r in results if r["status"] == "ELEMENT_NOT_FOUND"]
    print("\n===== AC6 VALIDATION SUMMARY =====")
    for r in results:
        lay = r.get("layout", {})
        detail = ""
        if lay.get("found") and lay.get("containerFound") is not False:
            detail = f" | {lay.get('containerWidth')}px wide | {lay.get('childCount')} items | {lay.get('uniqueRowCount')} row(s)"
        print(f"  {r['status']:25s} {r['label']}{detail}")
    print(f"\nOVERALL: {'PASS' if all_pass else 'FAIL'}")
    if not_found:
        print(f"NOT FOUND (manual check needed): {not_found}")
    print(f"Screenshots: {OUT_DIR}")

    report = {
        "overall": "PASS" if all_pass else "FAIL",
        "not_found": not_found,
        "strips": results,
        "screenshots_dir": str(OUT_DIR),
    }
    (OUT_DIR / "ac6_report.json").write_text(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    report = run_validation()
    sys.exit(0 if report["overall"] in ("PASS",) else 1)
