# Broker queue-duplication finding, two-seat confirmed (2350Z -> 0020Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE

**Serial:** `0.4.0_DS_ClientPlatform~B` | **Window:** 2026-08-19 2350Z -> 2026-08-20 0020Z
(follows `2026-08-19/session_close_2325-2350Z.md`)
**Commits this window:** ZERO. All output was measurement + MCP; no code, no artifacts, no deploys.

---

## Summary

Board was already closed. This window is one unplanned finding, surfaced through the surprise
channel, plus the RAVC close-outs on both TOs.

**A heartbeat return exceeded the tool's token limit** (164,319 chars, spilled to a file rather than
returning). Measuring the spill: the payload claimed **"46 messages received while idle"** but held
**4 distinct messages**, three of them repeated **15x**. All four were already read and acted on.

**Localised, not just reported:** the filesystem clocks are CLEAN -- `.unread-deliveries` carries one
entry per real send (DROPPED 1, IDENTITY_RUN 1, RELEASE 3 for 3 genuine sends), top-level unread 0,
all four in `read/`. So the multiplication is **broker-side, in the queued-message return path** --
not the `inbox-watch` path. That half is what made it actionable rather than alarming.

## Outcome -- confirmed at a second seat, and it caught a live error

`2.0.0_SA_COO` re-measured their own payload after reading mine: **stated 72, DISTINCT 12**,
multiplicity 9,8,8,7,7,7,6,6,5,4,3,2. Base inbox and `~lane` inbox, two seats, same class -- not
lane-specific, not one seat's artifact.

**It reached a number already travelling.** Forty minutes earlier they had told `0.8.0` their
"72-message batch" was un-ackable and recommended flooring a metric to exclude ~72 rows. The scale was
**6x overstated**; the exclusion would have carved a hole six times too large. Their own words on how
it passed: they had "verified" the 72 by counting message BLOCKS -- **not an independent check,
because the duplication is in the blocks.** Correction sent; routed to `0.8.0` with both seats'
measurements.

## The precision I sent back on my own half

COO characterised my `[15,15,15,1]` as fitting their age-monotonic gradient. **It does not do that
work.** Mine is **flat-then-step**, not a descent:

| arrival | subject | copies |
|---|---|---:|
| 233839Z | `[RELEASE]` | 15 |
| 233922Z | IDENTITY RUN | 15 |
| 234307Z | DROPPED | 15 |
| 000411Z | RETRACTION ACCEPTED | 1 |

Both are compatible with a re-append-per-queue-event accumulator, but **only their 9..2 is evidence
of monotonicity.** Mine is equally explained by my three oldest arriving within 4.5 minutes and so
surviving the same subsequent events. Sent before `0.8.0` debugs against it -- and my flat 15 is
arguably the *cleaner* test of their hypothesis, since messages surviving identical events should show
identical counts.

## The one that bit me

**My first re-measurement used `grep -c` and returned 1 for all four subjects.** The payload is a
**single line of JSON** (`wc -l` = 0), so `grep -c` counted matching LINES, not matches -- reading as
"no duplication at all," flatly contradicting what I had already measured and reported. Correct form
is `grep -o ... | wc -l` -> 15/15/15/1, summing to the stated 46.

**Caught only because the sum did not reconcile.** This is the estate's printed-denominator rule
biting me *inside the message where I was being careful about someone else's denominator*. Passed
onward to `0.8.0`, since anyone measuring these payloads hits the same single-line JSON and can
silently read every count as 1.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `grep -o ... \| wc -l` over the spill file | per-subject copy counts | PASS -- 15/15/15/1, sum reconciles to the stated 46 |
| `grep -c` (same target) | first attempt at the same counts | **FAIL** -- returned 1 for every subject; single-line JSON, counted lines not matches |
| `wc -l` on `.unread-deliveries` + per-pattern counts | localise the fault | PASS -- one entry per real send; ruled OUT the inbox-watch path |
| `ls read/` + top-level count | read-state check | PASS -- 0 unread, all four delivered |

**What worked:** reconciling the parts against the stated total. The sum is what exposed the bad
measurement -- no individual count looked wrong. **What failed:** `grep -c` on single-line JSON, above.
**Gap found:** none tool-side; the defect is in the broker's queued-message return path, routed to
`0.8.0` and not my lane.

*(No comp-* tools this window: no repo search, no code, no infra change -- the subject was a runtime
payload and two inbox directories.)*

## MCP traffic

4 sent, 3 received (excluding broker re-surfaces of already-handled messages). Significant:
RAVC close on both TOs (ACK to COO); surprise-channel item raised; COO confirmation + their
self-correction; my precision correction on the gradient characterisation.

## Blockers

**None.** `dim 436` remains at Andrew via COO -- a template write is not a bigger read, so the 49F-BD
scanning grant does not cover it. Nothing I built depends on it arriving.

## Current State

- **T1-ORACLE** and **T2-DIMS** both COMPLETE and accepted; retraction of the 90.8% split accepted and
  **contained** (never reached CTO or Andrew). Both proofs VALID rc=0.
- **9 commits, 6 session logs**, all unpushed per lanes-commit-integrators-push.
- T2 gold live at
  `s3://opal-data-49financial/gold/advi/dimensions/{dim_portfolio_group,bridge_group_account}/date=2026-08-18/`;
  `platinum/advi/49financial/` still **0 keys**.
- Broker duplication routed to `0.8.0`; both seats' measurements attached; spill file path given.

## Next Steps

1. [`0.8.0_AE_CloudComp`] Broker queued-message duplication -- deterministic accumulator signature,
   two-seat data, plus the `grep -c` single-line-JSON caveat for anyone re-measuring it.
2. [`2.0.0_SA_COO`] `dim 436` at Andrew; the AE publisher invocation contract still unanswered.
3. [`0.4.0_DS_ClientPlatform~B`] Nothing owed. Event-driven; T2-3 closes with no further build the
   moment 436 lands.
