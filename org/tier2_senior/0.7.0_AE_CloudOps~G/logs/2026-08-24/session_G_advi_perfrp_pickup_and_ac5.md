# Pickup falsified two spec premises and the gate that checks them — 0.7.0_AE_CloudOps~G

**Date:** 2026-08-24
**Task Order:** ADVI_PERFRP.TO-R1-AE (publisher keys · scoped route · chain stage · IAM)
**Status:** IN PROGRESS — AC5 PASS, five criteria UNCOMPUTABLE, start condition unmet
**Archetype:** AE (cloud/infra)

---

## Objective

Seat `0.7.0_AE_CloudOps~G` on ADVI_PERFRP round 1 — one project, base heap and the
OPAL_KIMIPIPELINE-S1 disarm explicitly excluded — run the TO's mandated SPEC-AT-PICKUP
falsification table as the first act, then hold at the start condition (the DS lane's first local
emission of a PERFRP leaf). AC5 was executed ahead of that condition under an explicit issuer
run-ahead grant.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 exercise half — a forwarder RAN (own banner), not merely resolved. PATH 97 of 102 bare. |
| comp-trigger | `comp-trigger advi-49f-gold-floor` | PARTIAL | Confirmed `[scheduler] ENABLED` against a printed denominator (136 events-rules + 18 schedules, us-east-1) and named the TF file. Printed `schedule: -` and did NOT carry the cron expression, so the APPLIED value had to come from `aws scheduler get-schedule`. Correctly labels itself declared-ness only. |
| comp-iam | `comp-iam role bd-exporter-ec2-role` | PASS | DESIRED plane, 33 statements. Found Statement 32 (Allow PutObject on the 49F platinum prefix) and Statement 18 (the only Deny, `s3:*` on `opal-data-cot`). Its own header disclosed `DENY-OVERLAY INCOMPLETE: 2 deny statement(s) unparsed` + `24 policy blocks NOT ATTACHED` — the disclosure is why the live simulate was treated as the verdict and comp-iam as corroboration. |
| comp-find | `comp-find --name 'chain_49f_entrypoint.py'` · `comp-find --name 'P4E1_FROZEN_SERVED_KEY_LIST_49F_20260818.md'` | PASS | 1 hit / 28,164 files scanned, and 1 hit; both banded `[HEAD]`. The second lookup is what turned the "11 twins" correction from a bare disagreement into a drift explanation with a dated provenance. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance> PRFR1AE-AC1,...,AC6` | FAIL (defect in the tool, not the instance) | rc=1. Its alignment frames printed correctly (36-cell decomp id space, 6/6 criteria carry a cell_ref, 5/5 cell_refs resolve) and then faulted the TO for a cell it does not claim. See Decisions §3. |

**What worked:** `comp-find --name` twice located a single file out of 28k with its denominator
printed, and the frozen-list lookup supplied the *provenance* of the stale number rather than just
its refutation. `comp-iam` was most useful for what it *disclosed about itself* — its unparsed-Deny
warning is the reason the `explicitDeny` verdict rests on the live simulate.

**What failed:** `comp-trigger` reported the schedule ENABLED but printed `schedule: -` instead of
the cron expression, so the single most decision-relevant field of a schedule query was absent from
a query about that schedule. Not wrong, but it forced a second tool for the primary fact.

**Gap found:** `proof-of-spec-check.py:259` harvests every cell id in the whole `<decomp_ref>`
element and treats all of them as cells the TO CLAIMS — it cannot distinguish an owned cell from a
read-dependency or from an explicitly disowned one. Measured across all three round-1 TOs; routed
as BLOCKING × INERT (66872). Details in Decisions §3.

---

## Work Completed

### 1. Startup + SPEC-AT-PICKUP (the TO's mandated first act)

Registered `0.7.0_AE_CloudOps~G` (PID 15652), armed the persistent inbox Monitor (task `bd1f1mb0w`,
`/cygdrive/c` prefix resolved rather than hardcoded, confirmed `running` via `TaskOutput`), session
serial file written, owned-paths hook verified, `comp-to ADVI_PERFRP.TO-R1-AE` set.

Five oracles run: **4 CONFIRMED, 1 FALSIFIED, 1 not-yet.**

| oracle | verdict |
|---|---|
| O-2 the 49F chain schedule | CONFIRMED both planes — DESIRED `comp-trigger` ENABLED (denominator printed); APPLIED `aws scheduler get-schedule` → `cron(45 12 * * ? *)` UTC, ENABLED, target `advi-49f-gold-dispatch` |
| O-3 the scoped router | CONFIRMED at source — `advisor-intelligence.ts:614` |
| O-5 the 49F switch HELD | CONFIRMED — portal `origin/PROD` = `8a96c91654…` (recorded as baseline); `ADVI_49FSRC` reads PARKED + HELD-ON-MIKE |
| O-4 DS first emission | NOT YET — the start condition |
| **O-1 publisher twin count** | **FALSIFIED on the count**, mechanism confirmed |

### 2. The "11 twins" premise, on three grains

Mechanism of O-1 confirmed: `EMITTERS` drives publication, D5 no-write via a `body-sha256` object
metadata compare, manifests under `_manifests/`, and `publish_one` hard-asserts the
`platinum/advi/49financial/` prefix (`d_publisher_port.py:422`). The **number** was wrong:

| grain | measured | how |
|---|---|---|
| emitter **entries** | **12** | AST over the `EMITTERS` literal — also what the TO's named `grep -c '"script":'` oracle returns |
| declared EMIT **twin objects** | **15** | 10 single-leaf + `timeseries_chart` pair (2) + `partner_analytics` multi (3) |
| **live** objects | **10** | `list-objects-v2` materialized, `IsTruncated=None` (12 total incl. 2 manifests) |

Provenance of the 11: the 2026-08-18 frozen served-key list, whose DENOMINATOR STATEMENT reads
"12 legacy keys → 11 advi twin objects". Two determinations recorded *inside `d_publisher_port.py`
itself* have landed since and both add leaves — the d12 un-collapse and the d13 trio. The file's
line-90 comment still quotes the frozen list while the dict beneath it derives 15.

**The load-bearing half was the grain error, not the arithmetic.** DS-AC13 read "count = 11 + N"
with an oracle that counts *entries* against a criterion worded in *twins* — Rule 24(ii), two grains
on one axis. Reported that way it **would have passed a mechanical check while being false.**

### 3. AC5 — the firm pin at IAM (the one cell executed)

Run under COO's explicit run-ahead grant (66725 item 4). Principal resolved by reading
`advi_49f_floor.tf:44-46`, which states the data-plane surface landed on **`bd-exporter-ec2-role`**,
not on either of the floor's own roles.

All three of `simulate-principal-policy`'s false-deny modes closed *before* reading any verdict:
one `--resource-arns` per call with the positive control in a separate invocation (mode 1); a
Condition census over all 15 inline policies establishing that the only PutObject-granting statement
and the only S3 Deny are both unconditioned (mode 2, clearance scoped to PutObject — a future
ListBucket test *will* need `--context-entries s3:prefix`); action-name validity taken from
`accessanalyzer validate-policy` with a planted bogus action that returned `INVALID_ACTION`, never
from simulate (mode 3).

| test | decision | matched |
|---|---|---|
| POSITIVE CONTROL — own 49F twin key | **allowed** | 1 — `advi-49f-publisher-platinum-put` |
| cross-firm **cot** | **explicitDeny** | 1 — `cross-firm-bucket-deny` |
| cross-firm **inf** | **implicitDeny** | **0** |
| scoping control — same bucket, `platinum/mdpf/` | **implicitDeny** | **0** |

Three distinct answers across four inputs: the instrument discriminates. Determinism STABLE
(test 2 re-run, identical decision *and* matched-statement identity). Full record:
`org/tier2_senior/0.7.0_AE_CloudOps~G/deliverables/ADVI_PERFRP.TO-R1-AE_AC5_IAM_FIRM_PIN_EVIDENCE.md`.

---

## Decisions Made

**1. Reported the cot delta against my own criterion rather than quietly passing it.** AC5 expects
`implicitDeny`; measured `explicitDeny`. The estate's posture is *stronger* than specified — an
explicit Deny cannot be overridden by any later Allow. A literal reviewer could have recorded a FAIL
on a control that is better than written, so the wording is what needs correcting.

**2. Surfaced the cot/inf asymmetry; changed nothing.** `PRF-inv-5` names "a cot/inf key" as one
phrase. cot is held by an explicit Deny belt; **inf is held only by absence of grant** — zero matched
statements on the APPLIED plane and no inf Deny in Terraform either (comp-iam: 33 statements, exactly
one Deny). NEVER#2 states the bd↔cot↔inf prohibition is "gate-blocked at commit **and IAM Deny at
runtime**"; on this role that second half holds for cot and does not hold for inf. Whether to add an
inf belt is an IAM change and a law question — routed, not acted on.

**3. Did NOT edit a frozen TO to satisfy a parser.** The proof-of-spec gate failed my instance for
"declared cell `PRF-b-1` … the TO claims a cell it never discharges". My TO does not claim it — its
decomp_ref says "**Reads** PRF-b-1's contract". Source-confirmed at `proof-of-spec-check.py:259`
(`CELL_ID_RE.findall(blob)` over the entire element). Measured across all three round-1 TOs:

| TO | harvested | criteria reach | TO's own stated count | unreached → one violation each |
|---|---|---|---|---|
| AE | 6 | 5 | 5 | `PRF-b-1` |
| DE | 13 | 10 | 10 | `PRF-b-1`, `PRF-g-1`, `PRF-g-4` |
| DS | 22 | 18 | 18 | `PRF-c-2`, `PRF-e-1`, `PRF-f-1`, `PRF-g-1` |

**3 of 3 fail; every TO internally correct.** The DS case is an *inversion*: three of its four
flagged ids come from its own "NOT in this TO:" exclusion clause, so the gate converts an explicit
disclaimer into a claim and faults the TO for not discharging it.

The cheap fix — deleting the cross-references from decomp_ref prose — was named and refused: those
sentences are the only record of what a TO reads and what it deliberately excludes, and removing them
would destroy real information to silence an instrument, on a spec frozen mid-round.

**4. Held the commit rather than landing a known-INVALID instance and calling it a flip.** AC6 names
a VALID instance. Told COO plainly and asked for the word; not reversing that unilaterally.

---

## Files Modified

| Path | State |
|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~G/deliverables/ADVI_PERFRP.TO-R1-AE_AC5_IAM_FIRM_PIN_EVIDENCE.md` | written, UNCOMMITTED |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ADVI_PERFRP.TO-R1-AE_PROOF_OF_SPEC.json` | written, UNCOMMITTED — at the TO's declared base path, flagged as a lane/base discrepancy |
| this log | written, UNCOMMITTED |

**No infrastructure touched.** No Terraform, no policy edit, no deploy, no ledger entry opened, no
tag. AC5 was read-only throughout.

---

## Blockers

**None that are mine to clear.** Two things I am waiting on, neither a hold on anyone:

1. **Start condition unmet** — the DS lane's first local emission of a PERFRP leaf. Verified at this
   seat, not taken on announcement: DS~G's only commit is `068ca0bebf` (PRF-a-1 column audit), which
   is neither the b-1 contract skeleton nor an emission. A single-shot background wait is armed on
   DS~G's next commit so I start at the event rather than at a message. **NOT YET STARTED is not
   BLOCKED.**
2. **The gate defect (66872)** — blocks AC6-class completion for all three round-1 lanes until the
   extraction is scoped or an interim disposition is ruled. Routed to the issuer; the gate belongs to
   the tooling lane.

---

## Current State

AC5 PASS on all three planes with its controls run. AC1–AC4 and AC6 UNCOMPUTABLE, each with a stated
reason rather than a blank. Proof instance and evidence written, uncommitted pending COO's word.
Inbox Monitor live; four messages received, read and ACKed this session (66637, 66725, 66744, 66804).

Known-relevant intelligence received and not re-derived: DS~G's `twr_daily` finding (returns refused
at the frontier) as strengthened by CVO — the refused partitions carry **9 columns, not 13**, with
`bmv/emv/cf_net/cf_gross` absent. Bearing on my lane is narrow and already stated by DS: the first
PERFRP leaf will carry all-null returns and that is **not** a broken emission; my chain-stage wiring
is unaffected.

---

## Next Steps

- [`0.7.0_AE_CloudOps~G`] On DS~G's contract-skeleton commit: begin the read-ahead the seating trigger
  permits (contract + IAM/TF preparation only).
- [`0.7.0_AE_CloudOps~G`] On DS~G's first leaf emission: AC1 (EMITTERS wiring, derived denominator
  printed before/after, D5 no-write exercised), then AC2 (one simulate per NEW key — the AC5 positive
  control used an existing twin and that gap is declared, not glossed).
- [`0.7.0_AE_CloudOps~G`] AC4 per the ruled placement: the stage runs **after** the c04 battery, and
  the criterion now requires exercising a forced c04 failure to show the projection UNRUN.
- [`2.0.0_SA_COO`] Two words wanted: the gate-defect interim disposition, and the proof-instance
  lane-vs-base path.
