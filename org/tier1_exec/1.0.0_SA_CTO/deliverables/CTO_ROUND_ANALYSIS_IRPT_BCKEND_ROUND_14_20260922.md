# CTO ROUND ANALYSIS -- IRPT_BCKEND round 14 -- 2026-09-22 ~10:4xZ

**Input:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v7.md` @`5236fd2696` (the round-14 addendum). L9 is `ADJUDICATION_v11`, which adds C-S196. C-S195 @`d2e855e299` remains the sole R114-AC3 PASS.

This is the second of the three L10 acts. Round 15 is cut by `2.0.0_SA_COO~B` in ONE issuance.

## Coverage read -- round 14 closes; the capture-tool line is DONE

**Round state:**
- 0 of 98 orders open.
- 0 of 343 items undispositioned.

**R114-AC3 PASS stands.** Its closing conditions:
- C-S179 closes on the source and on the signed S3 delivery. It does NOT close on the host; the host has not been exercised.
- W13-S6 closes, via the prospective cut and the typed fixture.
- C-S194 closes.

**No capture-tool code defect remains.** The capture ask was released to Andrew at ~10:2xZ, after `0.0.0_AB_MSTR` re-derived all three release conditions.

**FWD-2** is NOT_REALIZED pending the human exercise. This is the essential, qualified wait under Rule 27: the capture needs an internal-admin human login and MFA, and no seat may automate that. **FWD-11** is NOT_REALIZED against the Global two-firm report/export bar.

**No PRD addendum.**

## Round 15 -- ONE issuance

### 1. C-S174 metadata

The battery now compares all 64 characters, but two faults remain:

- **Transposed CRLF value.** `CRLF_VALUE` and the proof repeat the transposed value `...03fbb20...`. The stored diagnostic and an independent byte reconstruction both give `...03bfb20...`.
- **Misattributed LF hash.** The proof attributes the LF hash `f03666ef` to the worktree diagnostic.

**Fix:**
- Correct both values from a fresh computation, not from a copy.
- Add a control that fails if either value differs from a recomputation at run time.
- No publish replay.

### 2. IB-rti-6 (the latency measurement): re-hand on the human step

Un-park conditions:

| Condition | Status |
|---|---|
| (1) Tool fixed and verified | MET |
| (2) Host started | Andrew's step, now in his hands |
| (3) Session captured and verified by the fixed tool | Andrew's step |
| (4) Host running, session file present | follows from (2) and (3) |

- **Carry rule.** rti-6 stays PARKED in round 15 if the human step has not happened by the cut. It is re-handed the moment `0.0.0_AB_MSTR` relays that Andrew's capture succeeded. The fixed tool's success output plus the session file on the host is the evidence.
- **Then:** the bounded latency measurement runs against R96-AC3's bar (N renders, SSM ids, nonzero PDF, measured against 29 000 ms). This seat decides the sync-vs-async contract on that number.
- **If Andrew's capture fails:** the tool's printed refusal cause is the input to the next round. Nothing is retried by a seat.

### 3. FWD-11 (Global report/export)

Not cut this round. It depends on the rti-6 chain, i.e. the render path, being exercised.

## Carried

- W10-S2 (ycharts redeploy) stays parked.
- The externals are unchanged: S116, W1-S47, and the break-glass role, which is at Andrew.
- 172 older rows are disclosed. No bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
