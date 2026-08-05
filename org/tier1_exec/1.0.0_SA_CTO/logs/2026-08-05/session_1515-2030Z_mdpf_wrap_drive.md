# Session 2026-08-05 1515–2030Z — the MDPF wrap drive, and four instances of one failure family

**archetype:** MIXED (DIAGNOSE + COORDINATE + SCRIBE)
**Serial:** 1.0.0_SA_CTO

## Window summary

Andrew re-opened MDPF ("I want MDPF totally wrapped"), asked three named questions, then asked one
more that dissolved the fork I had put to him. Most of this window is his questions doing more work
than my analysis.

## His three questions, answered

1. **The `~F` kill** — census complete (17 rows), nothing killed, gated C1+C2. **C2 verified
   discharged** at source. **C1 was a CTO ruling sitting at my desk since 08-03** — ruled
   NOT-DROPPABLE: the runner's partition is the sole producer of MODEL-grain (7×49F) and ETF-grain
   (`etf_decomposition`) cohorts; the emitter re-sources only 3 of 14 and skeleton-fills the rest.
   The spine does **not** cover them — it emits FIRM-grain, a different grain, so finishing CANRTE
   does not discharge C1 for free.
2. **Routes + spine** — spine production and verified clean on its first full scheduled cycle;
   **canonization NOT finished** (W-3 unseated, W-5 held, two producers still writing).
3. **The roll-forward** — scoped but unseated; DS delivered during the window and the implementation
   surface came back **one producer, not three**.

## The question that changed the answer

> *"where does this `gold/mdpf_aggregate_aua.py` differ from the platinum publisher lambda? It seems
> like the publisher lambda should be running this script, not some ec2."*

Grounded: the publisher (230 lines) **computes nothing** — read gold, stamp, write served, verify.
`mdpf_aggregate_aua.py` is 1,446 lines of pandas. So the publisher should not *be* that script — but
his instinct found the real defect: **WS-A writes DIRECTLY to the served bucket, bypassing the
publisher**, while all 12 served keys go gold→publisher→platinum with a stamp. And **WS-A runs in 3
seconds** (whole chain ~3.5 min), so the EC2 is inertia, not capacity. That became option **(c)** —
port, re-point to gold, kill the chain — which he GO'd.

## Two corrections I owed, both mine

- **I mis-sized (c).** I pitched "kill the EC2 whole." The box runs **ten scripts**, and
  `build_mdpf_spine.py` — *the canonical spine itself* — is one of them. Porting WS-A relocates 1 of
  11. Corrected to him and to COO before anyone built against the number.
- **I minted an undefined identifier.** I wrote "6b/6c/6e" into a governance record twice; COO
  repeated it into a GO; DS refused to build on it and was right. Traced: 6a–6e are stage-6 sub-legs
  defined **only in the EC2 dispatch script**. My subset silently dropped **6d (Cottonwood)** — not
  by reasoning, by recollection written as if it were an enumeration. DS's tell: *"the letters skip
  6d,"* and they declined a three-letters/three-components match that looked "suspiciously neat."

## The finding his last question produced

**The live serving path is three hops and the EC2 is in it TWICE:** 09:00 chain (compute) → **09:40
accrual bridge, same EC2 via SSM (promotes spine output into `portal/gold/mdpf/{scope}/{type}/{date}`)**
→ 09:50 publisher → the 12 served keys. Bytes tie end-to-end (342,738B).
**The promotion step appears in NO teardown artifact** — not in the 17-row census, not in the (c)
decomposition. And it is a **redundant hop**: the same bytes written twice in two grammars 40 minutes
apart, because the spine was built as a swap-in and never had its output grammar aligned. Align it and
the hop disappears — a better target than porting ten scripts.
Also corrected in the record: `publisher OFF (publish HELD)` means the *chain* does not invoke the
publisher, **not** that serving is held. I had read it the stronger way.

## The gate I caught

COO's W1 re-pointed the **writer** and left the **reader** on the old prefix. `_latest_key()` returns
`max(keys)` and raises only on a **fully empty** prefix — and we are not deleting history. So it would
have locked onto the last partition ever written and emitted that day's values stamped with today's
date **forever**, for the same 11 cohorts. No exception, no rc≠0, no missing file.
Amended to atomic-over-producer-and-consumer with **consumer-side acceptance**. Then the consumer set
closed at **five**, including an IAM `ListBucket` with a `StringLike s3:prefix` **condition** — a
second independent pin that a bucket-ARN edit does not touch, and it denies the **LIST**, not the GET.
Re-gated: W-1 splits, **IAM leads and lands additively**.

## Rulings issued

| To | Ruling |
|---|---|
| DS | GRF count-carry is an **EXTENSION** of 051427Z, four conditions, cond-4 (*structural lag, not a gap*) is the test. Plus: stale sidecar must fail as loudly as a missing one |
| CVO | Gate roster 11-of-90 is **decay** — but print the denominator FIRST, triage, widen LAST (widening blocks the tree on a pre-existing break) |
| CRO | **Declare the 3/2 split**, do not re-cut the axis — re-cutting to look complete deletes evidence of a real sensor gap |
| MSTR | comp-find: 5 steps, **law LAST**. Registration canon: assert on the **delta between surfaces** |
| COO | 6a–6e defined; W-3 scope is **four legs**; the wider stale-plan sweep is mine |

## The family — four instances measured in one day

> **The defect was never the wrong number. It was that a scope change was SILENT.** (0.7.0_AE~A)

A writer re-pointed without its reader (freezes, never errors) · a stale **plan** vs a stale fact
(*a plan is an instruction — it gets executed*) · `_provenance.written_by` showing the last write and
unable to see a second writer · a derived predicate whose population moves at constant vocabulary.
**In every one the system stayed internally consistent while the thing it described had moved.**

And twice today a remedy grew the disease it treats: the phrase "producer AND consumer" (introduced to
fix leg 1) **concealed leg 4**, the producer's own self-read; and my two-clause derived-universe
amendment contained an instance of the exact failure it was written to close — caught by
`0.7.0_AE_CloudOps~A`, who then declined credit for foresight because both clauses came from a
measurement.

## Compiler Tools

| tool / probe | result | note |
|---|---|---|
| `comp-grep` ×6 | PASS | denominators printed; the stale-plan sweep returned 1 real instance + 1 false positive (`constant-shadowing` = variable scoping, different sense) |
| `comp-pipescript deployed --pipeline mdpf` | STALE (finding) | the Stage 3.5 committed-but-never-deployed |
| live AWS primitives (`s3api head-object`, `scheduler get-schedule`, `logs filter-log-events`, `lambda get-function-configuration`) | PASS | the serving-path map is APPLIED+EXERCISED, not TF-read |
| `owned-paths-validate.check_agent` | 9/9 both controls | **first run was undiscriminating** — see below |

**What worked:** grounding Andrew's questions at source rather than answering from the records — the
records were wrong twice (CANRTE phase, WSE_COTMDL blocker) and the code was right both times.

**What failed (mine), continuing this morning's streak:** a 4th self-inflicted retrieval error — I
truncated CRO's message with `head -40` and missed a direct ask, then had to disclose it. And my first
verification of the CRO grant returned **all False including a positive control that cannot be False**,
which is the undiscriminating-result class: consistent with "the grant failed" AND "the harness is
broken." Only the positive control separated them.

## Blockers

**OPEN AT ANDREW:** the W-3 appetite call — narrow (port WS-A, EC2 survives), full (relocate ~11
producers), or the third option his last question surfaced (align the spine's output grammar, delete
the promotion hop). Nothing is blocked behind it; W-1 proceeds either way.
