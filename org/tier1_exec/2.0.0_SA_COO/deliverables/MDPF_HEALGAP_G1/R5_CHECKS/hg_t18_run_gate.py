"""MDPF_HEALGAP round 5, HG-t-18 criterion (a): run.py's FT same-day re-attempt, and the default 3 AM run left as it was.
Pure stub test: no AWS call, no network, no browser, no SES.

Module under test: tools/astn_wsjft/scripts/run.py (override with HG_T18_RUN to grade a control copy).

Contract (the order's worker face states the same). `run.ft_reattempt(date, now_utc, dry_run=False) -> {"verdict": ...}`:
  - store.try_load_digest(date + "-ftsup") is not None            -> SKIP-COMPLETE   (no fetch, no send)
  - today's digest absent, or total_articles_out <= 0             -> NO-PRIOR-DIGEST (no fetch, no send)
  - today's digest has no warning starting "FT fetch failed"      -> SKIP-COMPLETE   (no fetch, no send)
  - otherwise (an FT-failed day):
      window = hours since 07:00Z of the NEWEST earlier day (back to 7 days) whose digest has total_articles_out > 0 and no
               FT failure warning (ceil, at least 1, at most 168); no such day -> 12 hours.
      fetch_ft(date, persist=not dry_run) is called ONCE; a raise propagates and nothing is sent.
      kept = fetched articles fresh within the window (run._fresh) and whose store._id(url) is in NO known digest
             (today's, every earlier day's back to and including the last ok day, and any "-ftsup" supplement of those days).
      kept empty                                                  -> FT-REATTEMPT-NO-NEW (no analyze, no send)
      analyze.analyze_all(kept); 0 out                            -> FT-REATTEMPT-NO-NEW (no send)
      dry_run                                                     -> FT-REATTEMPT-DRY (no put_digest, no put_email, no send)
      else put_digest(date + "-ftsup"), put_email, send_ses.send(html, date, subject containing "FT supplement"),
      best-effort store.discard_raw(date)                         -> FT-REATTEMPT-SENT
  - run.run() (the 3 AM path) sends once with NO subject argument and writes the digest under `date`, exactly as before.
Last line: GATE-OK or GATE-BAD <reasons>. At the base this is GATE-BAD.
"""
from __future__ import annotations

import datetime
import hashlib
import importlib.util
import os
import sys
import types
from pathlib import Path

RUN = Path(os.environ.get("HG_T18_RUN") or "tools/astn_wsjft/scripts/run.py")
UTC = datetime.timezone.utc
DATE = "2026-10-13"
NOW = datetime.datetime(2026, 10, 13, 11, 0, tzinfo=UTC)


def _id(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:16]


def art(url: str, published: str, source: str = "FT") -> dict:
    return {"title": "t " + url[-6:], "url": url, "source": source, "text": "x", "published": published}


def digest(urls=(), out=None, warnings=()):
    arts = [{"url": u, "source": "FT", "section": "S"} for u in urls]
    return {"by_section": {"S": arts} if arts else {}, "total_articles_out": len(arts) if out is None else out,
            "total_articles_in": len(arts), "warnings": list(warnings), "date": DATE}


def main() -> int:
    if not RUN.is_file():
        print(f"GATE-BAD no module file {RUN}")
        return 1
    S = types.SimpleNamespace(digests={}, calls=[], fetch=None, fetch_raises=None, analyze_out=None, raw=[], put=[], sent=[],
                              discards=0, wsj=[], read_fails=False)

    store = types.ModuleType("store")
    store._id = _id

    def try_load_digest(d):
        S.calls.append(("try_load_digest", d))
        if S.read_fails:
            raise PermissionError("AccessDenied")
        return S.digests.get(d)

    store.try_load_digest = try_load_digest
    store.load_digest = lambda d: S.digests[d]
    store.put_digest = lambda d, dg: S.put.append(("digest", d, dg)) or d
    store.put_email = lambda d, h: S.put.append(("email", d, h)) or d
    store.put_raw = lambda d, a: S.put.append(("raw", d, a)) or d
    store.load_raw = lambda d: list(S.raw)

    def discard_raw(d):
        S.discards += 1
        return 0

    store.discard_raw = discard_raw

    config = types.ModuleType("config")
    config.AWS_REGION = "us-east-1"
    config.EMAIL_SUBJECT_PREFIX = "Opal Morning Brief"
    for k in ("SECRET_FT_SESSION", "SECRET_RESI_PROXY", "SECRET_BRIGHTDATA"):
        setattr(config, k, k)

    analyze = types.ModuleType("analyze")

    def analyze_all(arts):
        S.calls.append(("analyze_all", [a["url"] for a in arts]))
        out = len(arts) if S.analyze_out is None else S.analyze_out
        return {"by_section": {"S": [{"url": a["url"], "source": a["source"], "section": "S"} for a in arts][:out]},
                "total_articles_in": len(arts), "total_articles_out": out, "sections_order": ["S"], "dropped": 0, "clustered": 0}

    analyze.analyze_all = analyze_all
    compile_email = types.ModuleType("compile_email")
    compile_email.render = lambda dg, d: "<html>%s</html>" % d
    fetch_wsj = types.ModuleType("fetch_wsj")
    fetch_wsj.fetch_wsj = lambda d: list(S.wsj)
    send_ses = types.ModuleType("send_ses")

    def send(html, date, subject=None):
        S.sent.append({"html": html, "date": date, "subject": subject})
        return "id"

    send_ses.send = send
    refresh = types.ModuleType("refresh_holdings")

    def _boom():
        raise RuntimeError("no holdings source in the stub")

    refresh.refresh = _boom
    for name, mod in (("store", store), ("config", config), ("analyze", analyze), ("compile_email", compile_email),
                      ("fetch_wsj", fetch_wsj), ("send_ses", send_ses), ("refresh_holdings", refresh)):
        sys.modules[name] = mod

    try:
        spec = importlib.util.spec_from_file_location("hg_t18_run_under_test", str(RUN))
        run = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(run)
    except Exception as exc:  # noqa: BLE001
        print(f"GATE-BAD module does not import: {type(exc).__name__}: {exc}")
        return 1

    def fetch_ft(date, persist=True):
        S.calls.append(("fetch_ft", date, persist))
        if S.fetch_raises:
            raise S.fetch_raises
        return list(S.fetch or [])

    run.fetch_ft = fetch_ft
    run._run_date = lambda: DATE
    bad: list[str] = []

    def reset(**kw):
        S.digests.clear()
        S.calls.clear()
        S.put.clear()
        S.sent.clear()
        S.discards = 0
        S.fetch, S.fetch_raises, S.analyze_out, S.read_fails = None, None, None, False
        S.raw, S.wsj = [], []
        for k, v in kw.items():
            setattr(S, k, v)

    def n(kind):
        return sum(1 for c in S.calls if c[0] == kind)

    def go(tag, dry=False, expect_raise=False):
        try:
            res = run.ft_reattempt(DATE, NOW, dry_run=dry)
            if expect_raise:
                bad.append(f"{tag}: did not raise")
            return res or {}
        except BaseException as exc:  # noqa: BLE001 -- a SystemExit from a fatal path is a raise too
            if not expect_raise:
                bad.append(f"{tag}: raised {type(exc).__name__}: {exc}")
            return {"raised": exc}

    def expect(tag, res, verdict, fetch=0, analyze=0, sent=0):
        if res.get("verdict") != verdict:
            bad.append(f"{tag}: verdict {res.get('verdict')!r}, want {verdict!r}")
        if n("fetch_ft") != fetch:
            bad.append(f"{tag}: fetch_ft called {n('fetch_ft')}x, want {fetch}")
        if n("analyze_all") != analyze:
            bad.append(f"{tag}: analyze_all called {n('analyze_all')}x, want {analyze}")
        if len(S.sent) != sent:
            bad.append(f"{tag}: {len(S.sent)} send(s), want {sent}")

    FAILED = ["FT fetch failed (session expired? -> run harvest_ft_session): boom"]
    old_a = art("https://ft.com/old-aaa111", "2026-10-12T05:00:00Z")      # before the window (07:00Z the day before)
    dup_a = art("https://ft.com/dup-bbb222", "2026-10-12T20:00:00Z")      # in the window, already sent on D-1
    new_a = art("https://ft.com/new-ccc333", "2026-10-13T09:00:00Z")      # in the window, never sent
    new_b = art("https://ft.com/new-ddd444", "2026-10-13T08:30:00Z")

    # A: the default 3 AM path is as it was: one send with NO subject, the digest under the date itself
    reset(wsj=[art("https://wsj.com/x-eee555", "", "WSJ")], raw=[art("https://wsj.com/x-eee555", "", "WSJ")],
          fetch_raises=RuntimeError("ft down"))
    try:
        run.run()
    except Exception as exc:  # noqa: BLE001
        bad.append(f"A: run.run() raised {type(exc).__name__}: {exc}")
    if len(S.sent) != 1 or S.sent[0]["subject"] is not None or S.sent[0]["date"] != DATE:
        bad.append(f"A: the default run sent {S.sent!r}, want one send(html, date) with no subject")
    if not any(p[0] == "digest" and p[1] == DATE for p in S.put):
        bad.append("A: the default run did not write digest/<date>")
    dg = [p[2] for p in S.put if p[0] == "digest" and p[1] == DATE]
    if dg and not any(str(w).startswith("FT fetch failed") for w in dg[0].get("warnings", [])):
        bad.append("A: the FT failure warning text no longer starts 'FT fetch failed' (the re-attempt keys on it)")

    # B: the refill is already sent
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED), DATE + "-ftsup": digest(["https://ft.com/z"])})
    expect("B", go("B"), "SKIP-COMPLETE")

    # C, D: no usable digest
    reset()
    expect("C", go("C"), "NO-PRIOR-DIGEST")
    reset(digests={DATE: digest([], out=0, warnings=FAILED)})
    expect("D", go("D"), "NO-PRIOR-DIGEST")

    # E: a day whose FT fetch did not fail
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=[])})
    expect("E", go("E"), "SKIP-COMPLETE")

    # F: the FT-failed day with an ok day before it: window since D-1 07:00Z (28 h), dedup by id, one supplement
    prev = "2026-10-12"
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED),
                   prev: digest(["https://ft.com/dup-bbb222", "https://wsj.com/b"], warnings=[])},
          fetch=[old_a, dup_a, new_a])
    res = go("F")
    expect("F", res, "FT-REATTEMPT-SENT", fetch=1, analyze=1, sent=1)
    if res.get("hours") != 28:
        bad.append(f"F: window {res.get('hours')} h, want 28 (since 2026-10-12 07:00Z)")
    an = [c for c in S.calls if c[0] == "analyze_all"]
    if an and an[0][1] != [new_a["url"]]:
        bad.append(f"F: analyze_all got {an[0][1]}, want only the new article (old dropped by the window, dup by its id)")
    if S.sent and "FT supplement" not in (S.sent[0]["subject"] or ""):
        bad.append(f"F: subject {S.sent[0]['subject']!r} does not carry 'FT supplement'")
    if not any(p[0] == "digest" and p[1] == DATE + "-ftsup" for p in S.put):
        bad.append("F: the supplement digest was not persisted under <date>-ftsup")
    if not any(c == ("fetch_ft", DATE, True) for c in S.calls):
        bad.append("F: fetch_ft was not called with persist=True")
    if S.discards != 1:
        bad.append(f"F: raw discarded {S.discards}x, want 1")

    # G: no earlier ok day inside seven days -> the 12 h window
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED)}, fetch=[new_a])
    res = go("G")
    expect("G", res, "FT-REATTEMPT-SENT", fetch=1, analyze=1, sent=1)
    if res.get("hours") != 12:
        bad.append(f"G: window {res.get('hours')} h, want 12")

    # H: the last ok day is older than the cap -> never more than 168 h; an earlier day with an FT failure is not "ok"
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED),
                   "2026-10-12": digest(["https://wsj.com/b"], warnings=FAILED),
                   "2026-10-11": digest(["https://wsj.com/c"], warnings=[])}, fetch=[new_a])
    res = go("H")
    if res.get("hours") != 52:      # 2026-10-11 07:00Z -> 2026-10-13 11:00Z = 52 h
        bad.append(f"H: window {res.get('hours')} h, want 52 (the newest earlier day WITHOUT an FT failure is 2026-10-11)")
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED)}, fetch=[new_a])

    # I: everything fetched was already sent -> nothing analysed, nothing sent
    reset(digests={DATE: digest(["https://wsj.com/a", "https://ft.com/dup-bbb222"], warnings=FAILED)}, fetch=[dup_a])
    expect("I", go("I"), "FT-REATTEMPT-NO-NEW", fetch=1)

    # J: the FT fetch raises -> loud, nothing sent
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED)}, fetch_raises=RuntimeError("cookie dead"))
    go("J", expect_raise=True)
    if S.sent or n("analyze_all"):
        bad.append("J: a send or an analysis happened after the FT fetch raised")

    # K: dry run -> persist=False, nothing written or sent
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED)}, fetch=[new_a])
    res = go("K", dry=True)
    expect("K", res, "FT-REATTEMPT-DRY", fetch=1, analyze=1)
    if S.put or any(c == ("fetch_ft", DATE, True) for c in S.calls):
        bad.append(f"K: dry run wrote or persisted: put={S.put!r}")

    # L: nothing survives analysis -> no send, no supplement digest
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED)}, fetch=[new_a, new_b], analyze_out=0)
    res = go("L")
    expect("L", res, "FT-REATTEMPT-NO-NEW", fetch=1, analyze=1)
    if any(p[0] == "digest" for p in S.put):
        bad.append("L: a supplement digest was written for 0 surviving articles")

    # M: an unreadable digest is not an absent one (a read error raises; it is never read as NO-PRIOR-DIGEST)
    reset(digests={DATE: digest(["https://wsj.com/a"], warnings=FAILED)}, read_fails=True)
    go("M", expect_raise=True)
    if n("fetch_ft") or S.sent:
        bad.append("M: fetched or sent after an unreadable digest")

    if bad:
        print("GATE-BAD " + "; ".join(bad))
        return 1
    print("GATE-OK arms A(default run unchanged) B(supplement sent) C(no digest) D(empty digest) E(no FT failure) "
          "F(window 28h, dedup by id, one supplement) G(12h default) H(newest ok day) I(all dup) J(fetch raises) "
          "K(dry run) L(0 survive) M(unreadable digest raises)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
