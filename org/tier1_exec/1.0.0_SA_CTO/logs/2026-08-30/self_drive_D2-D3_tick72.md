# /self-drive D2 & D3 — tick 72 (2026-08-30 02:44Z) — state: ARMED

Covers **ticks 71–72** (tick 70 logged @`9ed82980e8`, on origin). Cron `1c261f82` :07/:37 (both fires
delayed until idle — the seat was mid-act at each mark). Paired `/drive D2 & D3 @ 2.0.0_SA_COO`.

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 → 10 projects (1 complete). Open TOs **28 (tick 71) → 29 (tick 72)**; register ==
fresh `to-check` at BOTH ticks (28 = P2F-MARKER-DS closed; 29 = `ADVI_INSURE.TO-S1-AE` cut). Claims
342 of 342, 0 lag. Ledger **18 rows / 0 unconsumed** (row 17 consumed by COO on the hold read-back;
row 18 pre-filled on the CRO spawn). Population **20 of 20** (COO 84310) — the cap binds.

## Calls

- **Tick 71: zero new calls** (quiet; no pitch). R1/R2 carried.
- **Tick 72: CALL D2-T72-1 (pitched `20260830T024517Z`)** — RELEASE `4.0.0_SA_CRO` base now: its one
  allocated act (rider-4 selection) is delivered @`7cd0cc1200` and graded C3 PASS (84421); nothing
  CRO-class is reachable for hours (P3-EXACT's methodology limb sits behind P2-CENSUS ← the pull ← the
  reporting-pull deploy ~04:40Z); the cap is 20/20. Rec YES; re-spawn on demand. Asked of CVO because
  C4 of 84196 is CVO's own condition. R2 at Andrew is unchanged by it.

## Verdicts since last log

**0.** None pending at tick 72 (the T70-1 verdict was landed in the tick-70 cycle).

## Driver's own acts (ticks 71–72) — own lane, no TO, no dispatch, no apply

1. **org/mcp fix `f5836f8060` — `/ack-messages` recipient check** (MSTR 84328 diagnosis). Measured
   before the fix, live DB read-only: **341 of 22,596** acked rows `acked_by != to_serial` (two mine).
   Exercised on a scratch broker, baseline FIRST: HEAD acks B onto C's row (the defect, live); fix 4/4
   (own-row ok; foreign refused with ids, row untouched; audited override path kept; write-once skip
   distinct from refusal). **ON origin @`5a928adae7`.** Two live forgeries followed within 30 min
   (84265 by AE~X; 84598 by CTO~X, 84618) — the second is banked as the activation falsifier.
2. **org/mcp fix `ddbe7d1541` — `_broker_health` probe** (MSTR 83915 / 84511 step b). ⛔ The proposed
   refused-vs-timeout split was **unavailable on this host** — a closed loopback port TIMES OUT here
   (7891: raw 2.02 s / urlopen 2.04 s; live 7800: 0.00 s / 0.36 s); my first draft used it and the
   battery caught P1 "no listener" reading UNKNOWN (would never start a broker). Rewritten on the **OS
   port table** (exclusive-bind attempt: success = absent; EADDRINUSE = owned → HTTP decides ok/unknown);
   bounded retry on unknown; spawn only on absent. 6/6, baseline reproduces the P2 defect. Cost stated
   (~7.5 s worst case on a busy broker vs 2 s + a duplicate). **ON origin @`711a0717a0`** (02:44Z
   CLOSE; my own is-ancestor read).
   Activation = MSTR's restart at the 02:57–03:06Z tick gap with a listener census; CTO~X re-runs
   `ack_messages("84598")` as the post-restart control (must REFUSE).
3. **Per-apply gate rulings (84591):** reporting-pull deploy — CVO's member-sha condition adopted
   (`66f324ae…` LF, prior `4eaa66b0…` as the negative control — DS~C captured it before the deploy
   destroys it, 84637); apply BEFORE the 04:35Z production insurance fire accepted only on (i) zero
   insurance-path touches — **AE measured 0 of 8, PASS (84611)** — plus (ii) the three dispatch arms
   and (iii) a no-env-row plan, both still owed; gate also reads the **6-member census** (AE 84663: the
   packaging authority is `lambda-source-map.json files[]` = 6, the BUILD_MANIFEST's 3 is WRONG in the
   dangerous direction — filed, AE-owned). M-2 — COO's per-family-literal ruling confirmed, gate open on
   the two schwab rows.
4. **Deploy-gate CRLF one-liner answered for MSTR (84501):** rec = source the upload from the index blob
   (`git show HEAD:<path>`), queued at this seat as tooling item 3.

## In motion, not mine

c02 re-emission campaign **DRIVING** (COO 84671: R-1 accepted, 535 dates, ~8–10 s/date, ~40× margin to
the TUE lift-by; three special-date arms pre-registered; the 08-28 partition's flip is the round's
exhibit). Floor hold APPLIED (row 17). CRO selection delivered + graded. BDPARITY pull re-arms on the
reporting-pull deploy's member-sha read.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## RESERVED at Andrew

R1 `ADVI_49FSRC` close (rec: close) · R2 reach of the 21:23Z word (rec: YES; non-blocking; a YES also
releases the CRO slot if T72-1 has not already).

## Compiler Tools

`directives-check.py --json` ×2, `to-check.py --all` ×2 (per-project sums), claims scan (both `prds[]`
shapes), `comp-find` ×1 (locating 83915's carrier: 1 hit / 131,379 files), `commit-gate.sh` ×3 (all
clean), two scratch-broker exercises (session evidence, not committed). No comp-state (no record under
test).

state: ARMED · next log at a substantive delta (a verdict) or tick 78 (floor)
