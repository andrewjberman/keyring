# /self-drive D2 & D3 — tick 14 (2026-08-28 18:19Z) — state: ARMED

Covers tick 14 (tick 13 logged @20c0527041). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: the first ADJUDICABLE call pitched to
a live CVO this arm; row 14 executed; INSURE's reporting-pull side complete; a false-confession class
banked.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs **29**
(D2 22 — +1 = ADVI_INSURE.TO-A4-AEC; D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342,
0 claimed-not-member.

## Calls (§1-2)

**1 ADJUDICABLE, pitched to `3.0.0_SA_CVO` (live) with REC — 0 RESERVED.**
CALL: cut ADVI_PERFRP ROUND 2 (the DS b-series leaves) NOW, build-only, in parallel with the
campaign — or hold behind P1.5/P3? **REC (a) CUT NOW**: the leaves are the longest remaining pole
on D2; DE~D's 7 UNCOMPUTABLE criteria, BDPARITY's arming (first emission) and the serve gate's
source-gap half all wait on exactly this emission; nothing in it serves or egresses (08-19 ruling
#2 build-only caps inherit); a DS seat is free (DS~R released). Grounding on the card. The
ALL-RESERVED tell did not fire (queue of one, classified ADJUDICABLE — no NEVER line names this
sequencing).

## Verdicts / rulings since tick 13 (§3)

- **Row 14 CONSUMED by COO — EXECUTED 4 of 4 @6a634f2f6f:** INS-a-5 re-vehicled on the cell with
  his two words verbatim; TO-A3-AE (c′) at 0.6.0; **TO-A4-AEC cut to a FRESH lane
  `0.7.0_AE_CloudOps~K`** (seated 17:53:57Z pid 13944, 1pt/1b/1d clean) — my item-6 REC had named
  ~G, which COO had already killed at 16:46Z (a stale read of 78319; corrected on the record). ~K's
  seating ack (78541) reads the TO exactly as ruled: chain-wiring half only, no apply before this
  seat's GO on the SAVED -target'd plan diff, bd-49f-runner untouched, deploy order via exchanged
  timestamps. **Open gate at this seat: the plan-gate on the bd-49f-session-chain.tf IAM diff
  (one ARN on the session-trigger's invoke policy + the rule + the env var); ~K's first report
  precedes the diff.**
- **0.6.0 (c′) DEPLOYED @52ffb6c8a3, ledger 20260828T1807Z CLOSED 5/5 (78590/78593):**
  `INSURANCE_EGRESS=1` LIVE at 18:09:29Z, read from `get-function-configuration` (not the apply
  rc); gated at TWO chokepoints (`call_surface` + before `mint_both_authorities`, which reaches
  `veh._request` directly — one site would have left a vendor path open behind a closed gate); RED
  ARM 2 exercised (flag OFF → 0 http calls incl. the token mint); `.tf` TRIGGERS comment amended as
  ruled (replaces the blanket "WS-5 owns the trigger" that was being read as covering both payloads);
  two provenance one-liners fixed (the `to=` stamp had hardcoded TO-A1-AE into every object; the
  export key ended `.json` while carrying xlsx). Only `insurance_leg.py` moved. **Ordering
  dependency DISCHARGED — ~K is clear to fire after the gate.** 0.6.0's side is COMPLETE.
  Push-state self-correction: 22d029d7c8 ON origin (rode window 16), 52ffb6c8a3 LOCAL.
- **DE~D 78573/78596 — AC10 PASS @537de2bf75 (TO-R1-DE 6 PASS / 7 UNCOMPUTABLE), and how:** run 1
  FAILED on the spec's pinned baseline (528 px, both tabs); cropping and LOOKING showed a peer's
  nav-rail removal (18fd5b38, a DT seat) inside a 40-commit window — **a false confession averted**.
  Sound baseline = the merge's second parent (481a31c5^2 = 57701d5c; 9 of 9 commits the lane's;
  the peer change an ancestor by construction) → PASS, 0 px outside the mask. COO's issuer ruling
  (78582): the baseline is a RELATIONSHIP, never a ref; author census as the harness's first line;
  AC10(a)'s denominator re-measured at quote time (80/78, not the spec's 69/67 — the share GREW).
  DE~D transcribed it as a harness command with a NEGATIVE arm that reproduces the incident and
  refuses it (@a7924a327d) — "a warning is not a mechanism". **DE~D release-eligible** (no
  status-moving act left; AC3/4/5/6/11 verified producer waits on the DS b-series — the call above).
  Memory banked at this seat: `feedback_a_pinned_ref_decays_as_a_baseline_and_a_self_attributed_fail_is_unaudited`.
- **CVO base** live (seated by COO); the seven round-bank classes + the INS-a-5 re-cut cert pointer
  routed to it at tick 13; today's additions (false confession; pinned-ref decay; junction-lies-
  about-its-extent) are on COO's 78582.
- **MSTR window 16** (OPEN 18:01Z / CLOSED 18:04:06Z, per DE~D + 0.6.0): frames no longer routed
  to base seats (Andrew's word at the MSTR terminal); this seat read the CLOSE by the two-limb
  oracle (no MERGE_HEAD; origin f814126b59 → 537de2bf75).

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @537de2bf75, ls-remote read 18:19Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · `to-check --project
  ADVI_PERFRP` (roster only — 2 open, both R1; status grounded on faces per the tick-10 correction) ·
  brief `:55-75` read · ledger read · `git ls-remote` + MERGE_HEAD (the two-limb close oracle).
