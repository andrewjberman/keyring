# MDPF remediation plan decomposed and dispatched — the RP wave

**archetype:** COORDINATE
**Date:** 2026-08-10
**Task Order:** CTO plan @dbbbfa9cd3 (Andrew-direct: "send the plan to COO for TO decomposition")
**Status:** DISPATCHED — commit @09b57a6278, GOs out same window, 3 of 5 ACKs in

---

## Objective

Decompose `MDPF_REMEDIATION_PLAN_20260810.md` @dbbbfa9cd3 into TOs such that the D-19 ordering
constraint is STRUCTURAL (a decomposition that lets W3 be picked up alone has recreated the defect).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `_model_leg_eclipse` (2 hits / 960 files, DEF=1) | located the gold builder: `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:885/:932` |
| `comp-find --name` | `MDPF_REMED*` (11 hits / 12,809) | surfaced the EXISTING W1-x register wave → RP-Wn codes chosen to avoid collision |
| `comp-pipescript io` | `dim_mdpf_aggregate_aua_timeseries.py --pipeline mdpf` | reads: 2 hardcoded gold + 5 monolith silver fact_* — embedded in RP-W1 Phase 1 |
| `comp-blast` | `_model_leg_eclipse` | NOT-FOUND over printed 20,615-node denominator; tool routed to comp-pydeps (4 code consumers) — the loud-NOT-FOUND behavior working as designed |
| `comp-blast` | `opal-assets-ingest-mirror` | 10 event rules (incl. `mdpf-daily-refresh-trigger`), 36 IAM policies, 10 roles — the W3/W5 cross-domain evidence; kuzu provenance header read (HEAD current, age 1.7h) |

**What worked:** comp-find's HEAD band separated the live TO family from mentions in one call.
**What failed:** nothing new. (comp-trigger's interpolated-name blindness is pre-known and is warned
about inside RP-W3's mandate rather than re-hit.)

## Work Completed

1. **Read + absorbed** the plan @dbbbfa9cd3, evidence base @5ba751ed88, and my predecessor's
   decomposition deliverable (its §5 window fork is now the plan's "clock at Andrew" item; Track D
   became W5; the cot census and ce99054e44 cutover-gap precedent ride inside RP-W3's mandate).
2. **Authored 5 TOs** (commit @09b57a6278), codes RP-W1..RP-W7 deliberately distinct from the
   earlier MDPF_REMED.W1-x register wave:
   - RP-W1 label offset (DS ClientPlatform) — orion+eclipse ONLY, schwab/BD negative control
   - RP-W2 frontier unlink (DS) — calendar/frontier distinction verbatim; two lines, no rewrite
   - RP-W3 cadence (AE) — **STAGED, DOUBLE-GATED** (RP-W1 complete + Andrew clock ruling);
     D-19 quoted in body; AE instructed to treat a GO not citing both gates as mis-sent
   - RP-W5 instrument integrity (AE) — narrow-never-disable, smartx→S3-object pattern (no
     schedules), limb-(v) un-skip, global reconciliation made able to fail
   - RP-W7 backfill emitter (DS PortfolioAnalytics) — STAGED behind the §5 completion bar
3. **GOs dispatched** same window (author+GO pairing): DS batch GO (W1→W2 in order), AE GO (W5
   only), staged notices to 0.2.0_DS and AE, W6 routed to site-Z via MSTR with D-15/D-11 evidence.
4. **NOT written as TOs** (per plan): W4 naming + the floor/pull clock — both surfaced to Andrew.

## Decisions Made

| # | decision | ground |
|---|---|---|
| D-11 | RP-Wn code prefix, not continuing W1-x | comp-find showed the existing register wave; a colliding W3 would be exactly the "separate ticket somebody can grab" failure |
| D-12 | RP-W3 staged + dependency-blocked + mechanism-in-body + mis-sent-GO instruction | D-19: sequencing alone is not a structure; the TO must refuse its own premature execution |
| D-13 | RP-W5 GO'd immediately | independent of both gates; AE spawned and ready per Andrew |
| D-14 | W6 via MSTR, not direct to a site-Z seat | MSTR is sole site-Z coordinator (standing seam); ACK requested (SENT is not READ) |

## Blockers

None mine. Two sovereign calls open at Andrew (W4 naming route (a)/(b); floor/pull clock re-rule —
his (B) predates the premise change). RP-W3 un-gates on DS's RP-W1 report + the clock ruling.

## Current State / Next Steps

- ACKs in: AE (RP-W5 started, RP-W3 held), 0.2.0_DS (RP-W7 staged understood). Pending: DS
  ClientPlatform (GO delivered filesystem+broker; not channel-pushed — verify reachability if no ACK
  soon), MSTR (W6 routing).
- On DS's RP-W1 completion report + Andrew's clock ruling → COO issues the RP-W3 GO citing both gates.
- On 12/12 A4 unattended-cycle bar → COO adjudicates, then RP-W7 GO.
- CTO ACCEPTED IN FULL (233305Z) and assigned the two open owners: **G-3c Schwab date semantics →
  AE, sequenced BEHIND RP-W5** (only custody feed with no measured vintage; trust currently rests on
  a docstring in the ORION module — eclipse's structural position this morning); **G-4 roll-forward/
  carry policy per firm → DS ClientPlatform, BEHIND RP-W1/W2** (known-defective answer R-21:
  point_class "measured" over CARRIED cottonwood values). COO tracks both as follow-on TOs to author
  when their gates clear. Two patterns CTO ratified for carry-forward: receiver-rejectable gates (a
  GO not citing its gates is treated as mis-sent) and negative controls on healthy legs.
