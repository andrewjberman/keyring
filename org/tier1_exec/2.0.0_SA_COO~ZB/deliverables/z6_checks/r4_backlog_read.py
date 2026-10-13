"""OPAL_BBGTML Z6 repair 4 -- the intake BACKLOG READ (read-only; CTO ruling 61e3067f5c disposition 4).

Answers, before the identity pin changes: how many tickets would the FIRST good intake pass post into
the client ticket channel? It runs the production pass in dry_run (intake_pass.run_once: "composes and
reports; sends nothing, writes nothing, moves nothing") against the LIVE fetch and the LIVE durable
cursor, with a send stub that raises if it is ever called. It never reads the gateway token, so it
works while the pin is still the unsatisfiable name.

Prints COUNTS ONLY -- never a ticket's text (client content does not go into a committed record).
Run from the repo root: python org/tier1_exec/2.0.0_SA_COO~ZB/deliverables/z6_checks/r4_backlog_read.py
Exit 0 = backlog is ZERO; exit 1 = backlog above zero (the cell stops; the call is Andrew's);
exit 3 = the read did not answer (FETCH_FAILED / config / cursor refusal) -- UNKNOWN, never a zero.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))

from integrations.ticketing.intake import runner  # noqa: E402
from integrations.ticketing.intake.intake_pass import run_once  # noqa: E402

SINCE = "2026-09-03"


def _never_send(_b):
    raise RuntimeError("send called in a dry-run backlog read -- refusing")


def main() -> int:
    try:
        cfg = runner.load_config()
        store = runner.ProdStore(cfg)
        cur = store.load_cursor()
    except SystemExit as e:
        print(f"BACKLOG: UNKNOWN (config/cursor refusal, exit {e.code})")
        return 3
    print(f"cursor: created_at={cur.created_at!r} ticket_id_present={bool(cur.ticket_id)}")
    sink: dict = {}
    fetch = runner.svc_fetch_factory(cfg, sink)
    rows_seen = []

    def counting_fetch(c):
        rows = list(fetch(c))
        rows_seen.extend(rows)
        return rows

    rep = run_once(counting_fetch, _never_send, store, str(cfg["portal_base"]), dry_run=True)
    if getattr(rep, "fetch_status", "") == "FETCH_FAILED":
        print("BACKLOG: UNKNOWN (FETCH_FAILED -- no row examined; this is not a zero)")
        for line in rep.lines:
            print(line.splitlines()[0][:200])
        return 3
    since = sum(1 for r in rows_seen if str(r.get("created_at", "")) >= SINCE)
    print(f"open tickets fetched: {len(rows_seen)} (denominator); opened since {SINCE}: {since}")
    print(f"dry-run pass: would_buzz={rep.buzzed} skipped_not_newer={rep.skipped_not_newer} "
          f"skipped_not_form={rep.skipped_not_form} refused={rep.refused}")
    if rep.buzzed == 0:
        print("BACKLOG: ZERO -- the first good pass posts nothing; the pin fix may land")
        return 0
    print(f"BACKLOG: {rep.buzzed} -- the first good pass would post {rep.buzzed} ticket(s) into the "
          "client ticket channel; STOP, the call is Andrew's")
    return 1


if __name__ == "__main__":
    sys.exit(main())
