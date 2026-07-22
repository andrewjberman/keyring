# ANDREW-DIRECT 2026-07-22 ~20:50Z — THE CUTOVER CARRIES THE B7 FIX. NO LEGACY STAMP PATCH.

**Channel:** Andrew direct at the `2.0.0_SA_COO` terminal (this session), 2026-07-22 ~20:50Z.
**Context:** decision on the ONE open item from the completed 3F-B7 verdict (@`dfa42659f`) — how to cure
the axis mis-stamp that produces the wrong July 6 point on his own MDPF chart.
**Recorded same-turn per `org/XXX.md`.** Broadcast: MCP to `1.0.0_SA_CTO` + `0.0.0_AB_MSTR`.

---

## VERBATIM

> **"Let the cutover carry, go with your recommendation"**

**The recommendation he is accepting, stated so the referent is unambiguous** (COO to Andrew, same turn):

> *"Two ways to fix it: land the cutover to the trading-day-clean artifact — which is already built and
> verified, and governed by the existing one-flip gate — or have CTO patch the legacy stamp in place.
> The first is already on the roadmap; the second is a detour. My recommendation is to let the cutover
> carry it rather than repair something we're replacing."*

---

## What it establishes

1. **THE LD-0330-GOVERNED CUTOVER CARRIES THE FIX.** The already-built, already-verified trading-day-clean
   staged artifact is the cure. It ships through the existing one-flip gate (3F-F1).
2. **NO LEGACY STAMP PATCH.** `mdpf_aggregate_aua.py:1176-1179 @ed415e268` (the
   `overall = min(as_of_by_partner)` rule, stamped at `:1150`) is **NOT to be repaired in place.** We do
   not fix what we are replacing.
3. **AN ACCEPTED COST, STATED PLAINLY SO NOBODY RE-OPENS IT AS A DEFECT:** **Andrew's chart continues to
   display the wrong July 6 point until the cutover lands.** He has been told this and has accepted it.
   **A future agent rediscovering the mis-stamped 07-06 value must NOT treat it as a new finding or an
   unactioned P1** — it is a known defect with a ruled remedy and a scheduled carrier.
4. **The 3F-B7 repull NO-GO stands and is now doubly settled** — a repull fixes nothing observed, and
   the remedy is the existing roadmap rather than any new data operation.

---

## Second Andrew-direct in the same window (relayed by `0.5.0_AE_OpalETL`, his terminal ~20:47Z)

> **"I dont care about fucking alarms, I care about making sure that eveyrthing is working. we can fuck
> around with alarms later."**

- **Consistent with the 07-17 standing no-alarms word.** "later" reads as DEFERRED-not-banned, but the
  standing order governs until Andrew says otherwise. **Surfacing, not adjudicating** — 0.5.0 recorded
  and broadcast it himself.
- **THE OPERATIVE DEMAND IS WORKING-STATE VERIFICATION, EXERCISED** — not configuration reads, not
  alarm wiring. This is CLAUDE.md Rule 22a's behavioral-grounding requirement restated by the sovereign
  in his own terms.
- 0.5.0 ran it immediately on the whole SmartX leg and it came back WORKING end-to-end: trigger fired
  on schedule (13:30:50Z = 09:30 ET); **fail-loud + retry EXERCISED NATURALLY** (attempt 1 raised
  `DirtyRunError` on a feed9 identity-table mismatch, async retry at 13:38:34Z converged in 58s, no
  second error); silver chained on OnSuccess; DLQ 0 messages ever; sweep ran 16:00:12Z; content
  reconciles to $1,434,172,228 across 7 live models on the correct D-1 date — on Andrew's ~$1.4B ground
  truth. The 8th model went to $0.00 on 07-20 and stopped advancing: **de-funded, benign, not a defect.**

---

## Consequences for live work

| Item | Disposition |
|---|---|
| Legacy stamp fix | **NOT DONE, by ruling.** Do not open a TO for it. |
| 3F-F1 (the one flip) | Now additionally carries the B7 cure. Its value to Andrew is higher than "consolidation" — it is the fix for a wrong number on his screen. |
| 3F-B7 | Verdict stands; repull NO-GO affirmed; pending CVO independent read. |
| The wrong 07-06 point | **KNOWN + ACCEPTED until cutover.** Not a new finding. Not an unactioned P1. |
| Alarms / sentinels | Still OFF the work list. Verification-by-exercise is the demand. |

-- `2.0.0_SA_COO`
