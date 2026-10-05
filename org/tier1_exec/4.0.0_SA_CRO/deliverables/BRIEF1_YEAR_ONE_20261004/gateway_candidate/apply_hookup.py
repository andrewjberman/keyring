"""Apply the /yearinreview hookup to an opal-gateway app/server.py (three exact, anchored edits; fails loud)."""
import sys

p = sys.argv[1]
with open(p, encoding="utf-8", newline="") as f:
    t = f.read()
if "yearinreview_view" in t:
    raise SystemExit("ALREADY-APPLIED: server.py already names yearinreview_view")

edits = [
    ("rivalfunds_view, sprint_view, token_broker",
     "rivalfunds_view, sprint_view, token_broker, yearinreview_view"),
    ("or rivalfunds_view.is_rivalfunds_path(path):",
     "or rivalfunds_view.is_rivalfunds_path(path) or yearinreview_view.is_yearinreview_path(path):"),
    ('        Route("/rivalfunds/{day}", rivalfunds_view.rivalfunds_day, methods=["GET"]),\n',
     '        Route("/rivalfunds/{day}", rivalfunds_view.rivalfunds_day, methods=["GET"]),\n'
     '        # Brief #1 (4.0.0_SA_CRO~2026): the Year One Operating Review, one static page in the release.\n'
     '        Route("/yearinreview", yearinreview_view.yearinreview_page, methods=["GET"]),\n'
     '        Route("/yearinreview/", yearinreview_view.yearinreview_redirect, methods=["GET"]),\n'),
]
for old, new in edits:
    n = t.count(old)
    if n != 1:
        raise SystemExit("ANCHOR-COUNT %d (want 1) for: %r" % (n, old[:60]))
    t = t.replace(old, new, 1)
with open(p, "w", encoding="utf-8", newline="") as f:
    f.write(t)
print("OK: 3 edits applied to", p)
