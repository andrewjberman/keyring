# CTO~Z ACCEPTANCE — OPAL_ANALYST.W6-T1 (the F8 fence tightening, Andrew-direct "rec approved" @ad2585793c) — ACCEPTED-PENDING-LIVE-POSITIVE

**Gate owner:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~15:57Z · **Builder:** 0.5.0_AE_OpalETL~Z (@cde91ccd08 fence + ajb.ps1 + suite; RELAUNCH.md @6e7678f9a7; record + proof @fe8f68a168) · **TO:** OPAL_ANALYST.W6-T1 @59244d9ccb · **Origin:** W6 T-1 (D6), Andrew's explicit word for the gate tightening.

## VERDICT
**ACCEPTED-PENDING-LIVE-POSITIVE.** All six ids verified at this seat; the ONE remaining row-half is the LIVE positive on BG's next relaunch (MSTR~Z's act, drill-hold respected): expect the `[ajb] F8: BG identity bound at launch` line + one classed call observed ACTIVE. Design constraint met exactly: **no blanket block** — an unresolvable serial on a non-BG session is LOUD-PASS, never denied.

## Verified at this seat (independent, not from the report)
- **Suite RE-RUN here:** `.tools/hooks/tests/test_bg_concierge_gate.sh` → **60 passed, 0 failed (denominator 60)** — incl. the five F8-1 classed DENYs (closed means closed: even the G1-allowlisted own-logs write and a read-class `git log` deny under marker-without-serial), the full F8-2 four-class positive with all 33 pre-F8 cases byte-unchanged, F8-3's three permitted+loud calls (a blanket block would FAIL the suite), both F8-4 mutants + the marker-content control (a non-`bg-concierge` first line does NOT close).
- **Proof instance:** `OPAL_ANALYST.W6-T1_PROOF_OF_SPEC.json` → validator **rc=0, 6 rows, 0 violations** (positional F8-1..F8-6, no pipe; honest rc history 11→5→1→0, conformance only).
- **Mechanism read:** the launcher binds BG identity AT LAUNCH — `ajb.ps1`, BG-scoped, writes `<sid>.launch-path` (marker) FIRST and `<sid>.serial` SECOND with `--session-id` pinned, so a failure between the writes leaves marker-without-serial = **LOUD-CLOSED by construction**; BG itself cannot write either file (G1) — the launcher writing them is the design, not a bypass. `settings.json` untouched (wiring unchanged); the never-rules-gate's own matrix untouched (Phase-1 census: 65 `OPAL_AGENT_SERIAL` hits / 545 files, every reader classed, none changes behaviour).
- **Rule-24 outcome set (the widened law's arrival requirement):** the four-cell table over (serial-state × BG-path marker) — ACTIVE-ENFORCE / SILENT-PASS / LOUD-CLOSED / LOUD-PASS — with (i) MECE over the full cross-product, the layer statement (identity resolution of one PreToolUse call; not authentication, not the classes' content), and the token census (four minted UPPER-KEBAB tokens, 0/67 collisions). Read in the record §; conforms.
- **Instrument finding banked:** the pre-F8 suite's "unresolvable = passes" case had been MIS-MEASURED (the probe inherited the runner's own serial); the suite now unsets it by default — the exact anti-correlated-probe class this whole tightening exists to kill, found and fixed in the same change.

## Close condition
F8's LIVE positive on BG's next relaunch (MSTR~Z coordinates; the launch line + one ACTIVE classed call observed) → this acceptance upgrades to CLOSED; COO~Z validates. No monitor, no new gate beyond the one Andrew approved; the fence's deny is its own deny-JSON.

---

## CLOSED ~16:12Z -- the LIVE POSITIVE landed (BG 2503, relaunch 16:00:03Z session 00a52644): W6-T1 CLOSED at this gate

Three legs, each with its control, measured AT THE RELAUNCHED SEAT first turn (record `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/F8_LIVE_POSITIVE_20260820_1600Z.md`):
1. **Launch binding:** `<sid>.launch-path` = `bg-concierge 2026-08-20T16:00:03Z launcher=ajb.ps1 ...` + `<sid>.serial` = the BG serial, both written by ajb (G1 forbids BG org/mcp/** -- the launcher writing them IS the design). **Negative control not hand-chosen:** BG's own reaped prior session has NEITHER file. Estate denominator: `*.launch-path` = 1 (exactly the one launch path specified to mark), `*.serial` = 69 (the fabric-wide mechanism).
2. **Fence ACTIVE in the healthy cell:** settings.json matcher covers all four classes, mtime 2026-08-07 UNTOUCHED by F8; identity resolves positively from `<sid>.serial` -> ACTIVE-ENFORCE by construction.
3. **One classed call BLOCKED live:** Write to an off-allowlist path DENIED with the named G1 line, **effect verified not inferred** (the file does not exist); positive control same tool, same minute, allowlisted path PASSED (the deliverable itself). Closed-means-closed; no blanket block.

**W6-T1 -> CLOSED.** COO~Z validates; the TO flip rides the record lanes. With this, the F8 tightening Andrew approved ("rec approved" @ad2585793c) is BUILT, EXERCISED (60/60 + mutants), and LIVE-POSITIVE at the real seat. D6's remaining open item = OPAL_ANALYST.W5-V03 alone.
