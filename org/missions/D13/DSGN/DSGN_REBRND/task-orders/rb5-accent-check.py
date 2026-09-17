"""rb5-accent-check.py -- DSGN_REBRND.TO-RB-s-5 Amendment 1: are Andrew's identity accents restored?

Issuer artifact (2.0.0_SA_COO~D), READ-ONLY to the worker. It grades the seven sites named by the
Andrew-direct of 2026-09-14 ~15:0xZ and ~15:2xZ
(org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_150xZ_DSGN_REBRND_RESTORE_SELECTIVE_INDIGO_ACCENTS_AND_AN_INDIGO_FAVICON.md):

  1 page-title rule      PageHeaderVariants.tsx  the w-[3px] rule is FILLED with the accent
  2 header subtext       PageHeaderVariants.tsx  the description <p> TEXT is the accent
  3 active tab           TabNavigation.tsx       the active branch has accent TEXT and an accent BORDER
  4 sidebar active item  App.tsx                 accent FILL + white label (the white left rule is RETIRED by
                                                 Andrew-direct 2026-09-14 ~19:5xZ: "that little white outline
                                                 ... is not necessary, please take that out")
  5 user avatar          App.tsx                 the avatar circle is FILLED with the accent
  6 favicon              index.html + public/    rel=icon points at an existing file carrying #5F3BE3 and white
  7 apple-touch-icon     index.html + public/    points at an existing PNG that is not the old two-squares icon

Each site prints RESTORED | ABSENT | NOT-FOUND with its file:line and the class string it read. A site the
checker cannot find is NOT-FOUND, never RESTORED, so an empty sweep cannot score as a pass.

Usage: python rb5-accent-check.py [<portal root>]    (default: ./portal, run from the workspace worktree)
"""

import hashlib
import re
import sys
from pathlib import Path

ACCENT = r"hsl\(var\(--(?:semantic-action-primary|primary|primary-purple|accent)\)\)"
OLD_TOUCH_ICON_MD5 = "9b099e3ab4f3d3b6aa3bd63b047f2676"  # public/favicon.png at portal a65b939a
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
WHITE_LABEL = ("text-white", "text-[hsl(var(--palette-white))]")
WHITE_RULE = ("border-white", "border-[hsl(var(--palette-white))]")


def has(prefix, cls):
    return re.search(prefix + r"-\[" + ACCENT + r"\]", cls) is not None


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def read(path):
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def find(text, pattern, keep=None):
    for m in re.finditer(pattern, text):
        if keep is None or keep(m.group(1)):
            return m.group(1), line_of(text, m.start())
    return None, None


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("portal")
    phv = root / "src/components/PageHeaderVariants.tsx"
    tab = root / "src/components/TabNavigation.tsx"
    app = root / "src/App.tsx"
    html = root / "index.html"
    results = []

    def site(n, name, path, text, pattern, test, keep=None):
        if text is None:
            results.append((n, name, "NOT-FOUND", f"{path} unreadable", ""))
            return
        cls, ln = find(text, pattern, keep)
        if cls is None:
            results.append((n, name, "NOT-FOUND", f"{path}: anchor not matched", ""))
            return
        results.append((n, name, "RESTORED" if test(cls) else "ABSENT", f"{path.name}:{ln}", cls))

    t_phv, t_tab, t_app = read(phv), read(tab), read(app)
    site(1, "page-title rule", phv, t_phv, r'className="(w-\[3px\][^"]*)"', lambda c: has("bg", c))
    site(2, "header subtext", phv, t_phv, r'\{description && \([\s\S]*?<p className="([^"]*)"', lambda c: has("text", c))
    site(3, "active tab", tab, t_tab, r"isActive\s*\?\s*'([^']*)'", lambda c: has("text", c) and has("border", c),
         keep=lambda c: "border" in c)
    site(4, "sidebar active item", app, t_app, r"isActive\s*\?\s*'([^']*)'",
         lambda c: has("bg", c) and any(w in c for w in WHITE_LABEL) and "border-l-2" in c,
         keep=lambda c: "border-l-2" in c or "bg-[hsl(var(--primary))]" in c)
    site(5, "user avatar", app, t_app, r'<div className="([^"]*rounded-full[^"]*)"[^>]*>\s*\{user\?\.name',
         lambda c: has("bg", c))

    t_html = read(html)
    for n, name, rel in ((6, "favicon", "icon"), (7, "apple-touch-icon", "apple-touch-icon")):
        if t_html is None:
            results.append((n, name, "NOT-FOUND", f"{html} unreadable", ""))
            continue
        href, ln = find(t_html, r'<link rel="' + rel + r'"[^>]*href="([^"]+)"')
        if href is None:
            results.append((n, name, "NOT-FOUND", "index.html: no rel=" + rel, ""))
            continue
        target = root / "public" / href.lstrip("/")
        if not target.is_file():
            results.append((n, name, "ABSENT", f"index.html:{ln}", f"{href} -> no such file"))
            continue
        data = target.read_bytes()
        if n == 6:
            low = data.decode("utf-8", errors="replace").lower()
            ok = "5f3be3" in low and ("#fff" in low or "white" in low)
            why = f"{href} ({len(data)} B) indigo={'5f3be3' in low}"
        else:
            md5 = hashlib.md5(data).hexdigest()
            ok = data[:8] == PNG_MAGIC and md5 != OLD_TOUCH_ICON_MD5
            why = f"{href} ({len(data)} B) png={data[:8] == PNG_MAGIC} md5={md5}"
        results.append((n, name, "RESTORED" if ok else "ABSENT", f"index.html:{ln}", why))

    for n, name, state, where, ev in results:
        print(f"SITE {n} {name:20s} {state:10s} {where}  {ev}")
    restored = sum(1 for r in results if r[2] == "RESTORED")
    print(f"SITES RESTORED: {restored} of {len(results)} (denominator 7)")
    print("VERDICT:", "ACCENTS-RESTORED" if restored == 7 and len(results) == 7 else "ACCENTS-INCOMPLETE")


if __name__ == "__main__":
    main()
