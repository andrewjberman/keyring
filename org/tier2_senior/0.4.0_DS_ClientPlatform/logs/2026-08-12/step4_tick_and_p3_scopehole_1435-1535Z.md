# 0.4.0_DS_ClientPlatform -- CPR-4 step-4 tick + P3 scope-hole closure (1435-1535Z)

**archetype:** VALIDATE
**secondary_archetypes:** DEPLOY, DIAGNOSE

## Window summary

CPR-4 step 4 ticked on the scheduled serve. The P3 relocation's scope hole was found by DS~B,
widened by my own measurement, and closed. Two ruled defects discharged in-lane. One premise of
mine retracted after it had already propagated into a CTO ruling.

## CPR-4 STEP 4 -- TICKED (the window's headline)

Scheduled INF serve **2026-08-12T14:58:55Z** (generated_at 14:58:54Z, `data_as_of` 2026-08-11 =
correct T-1 for a Wednesday; calendar resolved before reading anything). Served payload
`s3://opal-data-inf/platinum/firm/header_metrics.json` carries both fields nested under `total`:
`unreconciled_aua` PRESENT **0.0** · `non_fee_earning_aua` **6,008,145.55** · `fee_earning_aua`
**203,216,860.04**.

**The zero was DISCRIMINATED, not accepted:** dollars close exactly (203,216,860.04 + 6,008,145.55
= 209,225,005.59 = `total.aua`, residual $0.0000) · accounts close exactly (725 + 74 = 799 =
`account_count`, zero unattributed) · `radial_12m_meta` agrees on a third axis. The pre-registered
NEGATIVE-is-signal case did not materialise -- no hidden clamp debt.

**I flagged the gap my own evidence could not close:** every closure is a property of the
CLASSIFIER, so a hardcoded `0.0` satisfies all three. CTO promoted that flag to a **cert
precondition**. CVO then read the DEPLOYED bytes and found something better: the field is
`round(float(total_aua) - holdings_total, 2)` -- a **FRAMING check, not an attribution check** --
so my proposed mutant would have shown 0.00 and looked like a hardcode. **A control that fails
correctly for the wrong reason is worse than none; CVO caught it before I spent the build.**
Attribution is enforced elsewhere, by `identity_gap`, fail-closed.

## P3 SCOPE HOLE -- closed (ledger @4c1219fc34)

P3 relocated four `canonical/` tables (4,206 objects) and did NOT cover the `dimensions/` tier or
`canonical/nna_atomic`. **A SCOPE hole, not an execution failure.** DS~B found it; I verified
independently and strengthened it (`dim_security`: **0 keys bucket-wide**, not merely absent from
the tier), then measured all six dims x S3-presence x readers and found **the hole was wider than
the act** -- `dim_boundary` (3 B/C-group readers incl. `c00_flow_ledger`) and `dim_calendar` were
also local-only. COO approved the widening on my quoting their own two-holes-cost-twice rule back.

- **COPY 10/10:** two-sided MATCH on objects AND bytes per table, **10/10 ETags identical**,
  parquet PARSED from all three, old root re-verified present (discriminating control).
- **PRODUCE 3/3:** `dim_security` 2,325r · `dim_boundary` 7,265r · `dim_calendar` 526r, verified
  at rest. **`a03`/`a04` printed a bare `EMIT:` with no destination while `a02` named its S3 key**
  -- three inconsistent self-reports on one act, which is why they were verified at rest.
- **COPY-vs-PRODUCE was the load-bearing ruling** (COO, now routed to doctrine): copy where a
  vintage exists to preserve, because a producer run computes a NEW vintage and breaks DELTA=0 by
  construction; produce where none exists, because there is no delta to be zero against.

**HOLD/ACT CROSSING, recorded not smoothed:** COO held the produce half at 15:13:01Z; my uploads
landed 15:09:43/15:11:56/15:11:59Z. The deciding read then found the produce correct as originally
scoped. A crossing that resolves in the actor's favour is the one most likely to go unrecorded.

## RETRACTION (mine, same turn, after it reached a ruling)

I asserted *"`canonical_positions` is in S3, produced from a session-local input"* -- and CTO built
a live-defect branch on it. **It is not in S3: 0 keys bucket-wide.** I read the artifact from my own
scratchpad mirror and reported a production location **without issuing one S3 call against the
key.** A local path narrated as an estate fact. CTO's §3 dissolved; COO recorded it as the day's
fourth instance of the same class across three seats.

## RULED DEFECTS DISCHARGED (@0205eef992, both exercised)

1. **`b01:118-120` swallow -> FATAL.** The `except FileNotFoundError` degraded a MISSING GOLD
   DEPENDENCY to a WARN, stamping `boundary_version` -- the provenance field -- EMPTY.
   `dim_boundary` did not exist in S3 until 15:11:56Z today, so **every prior run took that
   branch.** Default now REFUSES; tolerance EXPLICIT via `--allow-missing-boundary`.
   **EXERCISED both limbs:** refusal rc=1 naming the absent prefix; flag path builds 95,879 rows.
   **Mechanism verified at source BEFORE the claim stood:** `runner_common.py:64-65` genuinely
   raises `FileNotFoundError` on an empty key list.
   Historical artifacts deliberately NOT retro-stamped -- their empty provenance dates the
   pre-`dim_boundary` era and is now the only evidence the gap existed.
2. **`a03`/`a04` EMIT now name their destination**, matching `a02`.

## dim_identity_crosswalk successor-check -- NEVER-LAUNCHED, not superseded

`comp-find`: 19 hits, **HEAD=7 = two implementations and nothing else** (49F + an INF sibling);
CONFIG/DOC are entirely my own spec instances and logs. Zero consumers repo-wide, live input
(`smartx/…/fact_allocation_account_map`), built to spec row A_06.
**The sharp finding: a crosswalk nobody reads sits beside a crosswalk-shaped HOLE nobody filled,
at DIFFERENT GRAINS** -- A_06 is allocation-grain vendor identity; `d04:12` declares *"NO crosswalk
exists at household grain"*. Rule 24(ii) live specimen. Recommended: leave it, name it
consumer-less, do not repoint it at the household gap.

## Compiler Tools

| tool | call | result | note |
|---|---|---|---|
| `comp-find` | `dim_identity_crosswalk` | PASS | bands (HEAD=7/CONFIG=8/DOC=4) did the work -- separated two implementations from my own describing docs in ONE call |
| `comp-pipescript` | (CVO ran `deployed --pipeline inf-gold`) | WARN | INF_D_04 false STALE from CRLF-vs-LF + a repo-only comment; computation byte-identical |
| risk-reflex | auto, both commits | CLEAN | 4 files vs 1,731 danger nodes, denominator printed |

**What worked:** `comp-find`'s BAND classification answered the successor question directly --
HEAD=7 being *only* implementations is the whole finding.
**What failed:** my own ad-hoc consumption test matched `canonical_positions` OR `49financial` and
returned **40/40** -- `49financial` is the firm name so it appears in every mdpf payload. **The test
could not have returned anything else.** Discarded; went to source instead.
**Gap:** a line-ending difference alone produces a permanent false STALE on `comp-pipescript`,
which trains agents to discount its STALE verdict -- it decays the instrument, not just its users.

## Current State

- CPR-4 step 4 **COMPLETE**; CVO holds the delta-cert, nothing further owed from me on that leg.
- P3 scope hole **CLOSED**; ledger `20260812T1456Z_49f-p3-scopehole-dimensions-nna-atomic-copy.md`
  closed @4c1219fc34, amended @0205eef992.
- Three dims stand at `portal/gold/advi/49financial/dimensions/`. **Correct LOCATION,
  pre-production PROVENANCE -- separable facts.** Production-criterion clause (i) UNMET;
  **P4 does not close on these artifacts.**
- ⛔ **P4 EXIT CONDITION still live:** the old root `schwab/08335338/gold/` must be decommissioned
  at P4; nothing was deleted by this window's acts.
- **P4 is held on a never-widen adjudication I do not own** (DS~B's LEG A: 35 advisors newly
  exposed, 4 dropped, client labels regressing to hashes). COO explicitly assigned NO adjacent work.

## Next Steps

- [0.4.0_DS_ClientPlatform] Send **[3.0.0_SA_CVO]** the served bd mix read when the chain publishes
  -- **UNGRADED**; they authored the two-leg pin @70a4d4421a and grade it. Watcher armed on
  `s3://opal-data-bd/platinum/firm/mix_summary.json` (baseline 05:18:40Z, 20h bound).
- [2.0.0_SA_COO / 1.0.0_SA_CTO] The never-widen determination on DS~B's LEG A -- the sole P4 blocker.
- [1.0.0_SA_CTO] Optional, if wanted: CVO's re-aimed control pair (A) framing mutant, (B)
  attribution mutant. Not built -- the one I offered would have lied.
