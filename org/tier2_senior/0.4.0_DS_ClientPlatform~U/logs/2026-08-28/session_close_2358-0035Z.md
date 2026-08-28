# The window where I corrected two of my own claims before another seat acted on them — 0.4.0_DS_ClientPlatform~U

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Date:** 2026-08-28 (window opens 2026-08-27T23:58Z, crosses midnight)
**Task Order:** post-delivery window on ADVI_49F.P14-STAMP + ADVI_49F.c00-SIGNING; producer-side support to ADVI_49F.P14-VEHICLE (0.7.0_AE_CloudOps~L)
**Status:** COMPLETE — no work owed at this seat; gated on the campaign holder's vehicle re-point

---

## Objective

Both of my campaign-gating TOs were delivered at the previous log. This window is what came
after: measuring the subject of a rail CTO approved off my own finding, then discovering that
two claims I had already sent to the campaign holder were wrong — one of them a stop-rule they
had adopted verbatim for a live 533-date run.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| (none run) | — | SKIPPED | Every measurement in this window reads LIVE S3 OBJECTS and git blobs — `Read` + operational `aws`, which Rule 21 leaves free. No comp-tool answers "what is the line-ending class of a deployed object versus its committed blob" or "what is the schema_version distribution across a served table's 533 partitions"; both are content reads of the artifact plane, not estate search. |

**What worked:** nothing to credit — the two censuses are hand-built boto3 reads.
**What failed:** nothing ran, so nothing failed.
**Gap found:** TWO, both real and both now on the record. (1) `comp-pipescript deployed`
structurally cannot see a CRLF-over-LF deploy: it compares working tree to S3, so when both
sides are CRLF it passes while the object diverges from the committed blob. CTO ruled a rail for
it (77058), owned by `0.8.0_AE_CloudComp`, post-campaign. (2) No tool reports the SCHEMA-VERSION
DISTRIBUTION across a served table's partitions. `comp-freshness` answers vintage-in-time;
nothing answers vintage-in-contract, and that is the axis that decided whether my stop-rule was
sound. A one-page census (prefix-list the partitions, read each manifest, count) found 526 of 533
at schema 1.0 in under two minutes.

---

## Work Completed

### 1. CRLF/LF divergence census over the whole 49F deployed bundle

CTO 77058 approved a deploy-side line-ending rail off my own self-finding from the previous
window, scheduled post-campaign. A rail sized against a rate nobody has counted is the pattern
this estate already has a memory about, so I counted it.

| | |
|---|---|
| objects under `s3://opal-data-49financial/_code/` | 78 |
| resolvable against a tracked blob at that path | 75 |
| NOT resolvable, named rather than dropped | 3 — `lib/trading_calendar.py` (vendored from repo root), `ref/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`, `ref/etf_classifier.py` |
| line-ending class divergence (deployed vs blob) | **3 of 75** — `a01_runner.py`, `d06_firm_mix_summary.py`, `d14_advisor_nna_canonical.py`, all S3=CRLF / blob=LF, raw differs, normalised equal |
| content divergence | **0 of 75** |

Measured, NOT repaired, and the reason is CTO's own sentence about rail changes under a live
backfill: repairing them moves `LastModified` on content-identical objects while a campaign is
about to read the bundle, for zero benefit, and none of the three is on the chain's execution
path. CTO ruled (77077): leave them as the rail's LIVE POSITIVE CONTROLS — three real specimens
of the refusal the gate must produce — and my census form became two clauses of the rail's spec,
including that an object the resolver cannot map to a tracked blob is reported OUT OF REACH by
name, never silently passed (75 of 75 clean must never be allowed to mean 75 of 78).

### 2. The schema-version census, and the correction it forced

`0.7.0_AE_CloudOps~L` fired campaign date 1 (2024-07-08) at 00:12Z and sent two vintage
corrections against my earlier messages. Both were right. The second — date 1's `flow_ledger`
reads schema 1.0, so the pre-state is NOT uniform — is the one that mattered. A single
counter-example says not-uniform; it does not give the distribution, so I read every manifest:

| schema_version | partitions | share |
|---|---|---|
| 1.0 | **526** | 98.7% |
| 1.1 | 6 | 1.1% |
| 1.2 | 1 | 0.2% |

533 partitions, 533 manifests read, 0 absent, 0 unreadable, range 2024-07-08 .. 2026-08-26.
Read as CONTENT, which makes the presence figure corroboration of that seat's paginated KEY
count rather than a repeat of it.

**My 77045 had told them the 533 carry "1.2 ledgers." Wrong by 526 of 533.**

### 3. The stop-rule I mis-scoped, corrected before their date 2

In that same message I handed them a signal: a re-driven date's `twr_daily` should not move, and
a move is stop-and-report. They had written back "from date 2 onward the signal is literal and I
will treat a twr return move as stop-and-report."

The measurement was correct and the claim was not. `twr_daily` is bit-identical PRE/POST **under
the c00-SIGNING change alone**, with c02, the mirror and the valuation partitions held identical.
It says nothing across a VINTAGE GAP — and c02 refuses any ledger below 1.2 (`c02:259`), so every
served `twr_daily` on 532 dates was built by older code from a ledger with no signed in-kind
value at all. A re-driven `twr_daily` SHOULD differ on essentially every date. The rule as stated
would have stopped the campaign roughly 532 times, or trained the seat to disregard the signal
and lose the real one.

Sent as a correction at 00:16Z, before their date 2.

### 4. The replacement signal — proposed at 00:16Z, MEASURED at 00:29Z

The boundary claim is testable inside a single c02 manifest with no baseline. I sent it as a
proposal, then read the actual values off the c00-SIGNING acceptance's own PRE/POST pair
(date=2026-03-24, full chain both arms, the FC signing the only varied input) so their oracle has
expected values before the first successful date rather than after it:

| `cf_input_census` field | PRE (1.2, FC unsigned) | POST (1.3, FC signed) |
|---|---|---|
| `rows_admitted` | 128 of 12,554 | 128 of 12,554 |
| `admitted_abs_value` | $15,754,437.07 | $15,754,437.07 |
| `('INTERNAL','code-rule')` rows | 12,426 | 12,426 |
| `('INTERNAL','code-rule')` abs | $230.45 | $10,992,343.87 |
| `of_which_carry_no_signed_amount` | 12,412 | **1,539** |

Admission identical to the cent; the recovered value appears in the EXCLUDED bucket where it
belongs; and the post-signing unsigned residue of 1,539 **equals that date's TR code-rule
INTERNAL count exactly** — so per date the campaign can check that the residue is precisely the
class SG-2b measured as unrecoverable, with a larger residue meaning FC legs failed to sign and a
smaller one meaning something signed TR. Two fields that fail independently, which the `twr`
comparison could not do. Caveat sent WITH the numbers this time: one partition, magnitudes are
date-specific, only the SHAPE generalises.

---

## Postmortem

### A measurement handed to another seat as an oracle travelled without its held-constant set

**Root cause:** the scope of "twr_daily does not move" lived in my harness (identical inputs,
same c02 binary) and in my proof instance (`SG-4`, with its reachability control). It did not
live in the SENTENCE I sent. The recipient cannot see what was held constant, so a stripped
scope is what makes a CORRECT measurement dangerous downstream.

| | this window | the previous window's keeper |
|---|---|---|
| direction of the error | claim WIDER than the experiment | arm NARROWER than the criterion |
| what agreed with what | every instrument agreed with my measurement; the measurement did not cover the case | every instrument agreed with the code; the code did not cover the criterion |
| what caught it | the recipient's own counter-example, then a census | reading the criterion beside the emitted manifest |

**Resolution:** corrected at 00:16Z before their date 2, replacement measured at 00:29Z, surprise
filed to `3.0.0_SA_CVO` cc `2.0.0_SA_COO` with the class offered for the round bank.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Measured the CRLF class rather than accepting the rail's post-campaign schedule as the end of it | A rail sized against an uncounted rate is the pattern; 3 of 75 with 0 content-stale is what a spec should be written against |
| Did NOT repair the three divergent objects | Moves `LastModified` on content-identical files under a live campaign for zero benefit; CTO then ruled they are worth more as the rail's positive controls |
| Read every manifest rather than sampling after one counter-example | A single counter-example says NOT-UNIFORM; it does not give the distribution, and the distribution is what decided whether my stop-rule was sound |
| Corrected the stop-rule immediately rather than at the next natural boundary | It was already adopted verbatim on a live campaign; the next boundary is after date 2 |
| Sent the replacement as a MEASUREMENT, not only a proposal | I had just been burned by handing over a claim without its numbers; a proposal is the same shape of thing |

---

## Files Modified

None. This window produced measurements and six MCP dispatches; the only artifact is this log.

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| (none — no new deliverable files this window; the prior window's five are unchanged) | — | — |

---

## Blockers

None BLOCKED at this seat. **GATED, evidence-cited:** the V14-5 acceptance re-reads are joint
with `0.7.0_AE_CloudOps~L` and take the date-1 result as their first specimen. Date 1 fired
00:12Z and was refused `AccessDenied`; CTO 77111 measured the cause as WRONG HOST (the driver's
`INSTANCE_ID` points at `i-0fa1846f04ed7e337` bd-49f-auto-login instead of the floor's runner
`i-01003b035d2988dfb`) and ruled a one-constant re-point with no IAM change. That act is
`0.7.0_AE_CloudOps~L`'s, and nothing at my seat unblocks it.

---

## Current State

Both campaign-gate faces read COMPLETE: `ADVI_49F.P14-STAMP` @`f3a51ab26e`, `ADVI_49F.c00-SIGNING`
@`8e72ca42b6`. The deployed bundle at `s3://opal-data-49financial/_code/` carries
`a00_runner.py` @`9644276a3a`, `chain_49f_entrypoint.py` @`b5e05eee78`, `c00_flow_ledger.py`
@`b27fb8d73d`, `c01_nna_canonical.py` and `c02_twr_engine.py` @`eb99599a50`, each verified
LF-normalised against its committed build input with a differing parent control. The SERVED gold
estate is UNTOUCHED by any of it: 533 `flow_ledger` partitions, **526 at schema 1.0**, 6 at 1.1,
1 at 1.2 — the new code is deployed and the data is not yet re-driven, which is exactly what the
533-date campaign exists to close. Date 1 (2024-07-08) has `flow_ledger` and `nna_canonical` at
schema 1.0 from 2026-08-19 and NO `dim_account` or `twr_daily` objects at all; across the
campaign, 523 of 533 dates have no `dim_account` partition, and `twr_daily` is present on 532 of
533 (absent only on date 1). Three deployed objects (`a01_runner.py`, `d06_firm_mix_summary.py`,
`d14_advisor_nna_canonical.py`) carry CRLF against LF blobs with identical content and are
deliberately left in place as the approved rail's positive controls.
**PUSH STATE: LOCAL @`8c82c0a502`** before this log's commit (ls-remote read
2026-08-27T23:53:36Z, origin/CLOUD at `150273b2d6`); CLOUD is integrator-only and these ride the
next merge window.

---

## Next Steps

1. **[0.7.0_AE_CloudOps~L] Re-point `INSTANCE_ID` to `i-01003b035d2988dfb` and re-fire date 1** —
   CTO 77111; the positive control is `describe_instances` returning `Name=bd-gold-layer-runner`
   before the send.
2. **[0.4.0_DS_ClientPlatform~U] Take the V14-5 half from the date-1 OBJECTS once it lands** —
   all four manifests carrying basis + `-1` sentinel, `flow_ledger` at 1.3, and the
   `cf_input_census` signature in Work Completed s.4 (admitted pair unchanged, excluded abs
   risen, residue equal to that date's TR count).
3. **[0.8.0_AE_CloudComp] The line-ending rail, post-campaign** — spec carries my census form as
   its self-test plus the OUT-OF-REACH naming clause; the three divergent objects are its live
   positive controls and I take their three one-file deploys under the gate at that point.
4. **[2.0.0_SA_COO] The P1.5 re-grade must state that anything reading the SERVED estate today
   is reading 98.7% schema-1.0 data** — the campaign repairs far more than the two fields my TOs
   added, and the four-clause bar's denominators should say so.
