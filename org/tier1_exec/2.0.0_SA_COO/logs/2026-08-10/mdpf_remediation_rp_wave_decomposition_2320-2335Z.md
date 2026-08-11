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
- **~2334Z ANDREW RULED ALL FOUR open calls ("Agree with your recs for all open calls"; CTO record
  234031Z).** Call 1(b): **W1+W3 land as ONE ATOMIC CHANGE** — clock ruled floor 13:30 / pulls
  13:02; RP-W3 re-cut @356ec6fba4 from "W1 complete" to the atomic joint-deploy window, and the
  receiver-side citation re-stated to AE (AE ACK 234540Z). **COO topology decision (CTO flagged,
  mine to make): RP-W2 is IN the atomic set** — same file, same owner, same number; a partial
  landing of any two of the three is the D-19 shape. DS TOs re-cut: build+commit now, deploy leg
  only in the COO-called window, BUILD-READY report gates the window call. Call 2(b): **RP-W4
  authored + GO'd** (selector first, rename second; AE flipped pending, sequencing selector before
  or with the window; RP-W5 item-1 already exercised 5/5 offline + live-replay clean 687/687).
  Call 3: internal-only design binding relayed to 0.2.0_DS. Call 4: CTO's own §2.4 re-lock.
- **⚠ 0.4.0_DS_ClientPlatform IS DARK (NOT REGISTERED)** with both GOs unread — spawn request to
  MSTR 234548Z with first-message direction; fallback = surface to Andrew. The wave's P0 first-mover
  work (label offset — served numbers wrong today) waits on this seat.
- CTO ACCEPTED IN FULL (233305Z) and assigned the two open owners: **G-3c Schwab date semantics →
  AE, sequenced BEHIND RP-W5** (only custody feed with no measured vintage; trust currently rests on
  a docstring in the ORION module — eclipse's structural position this morning); **G-4 roll-forward/
  carry policy per firm → DS ClientPlatform, BEHIND RP-W1/W2** (known-defective answer R-21:
  point_class "measured" over CARRIED cottonwood values). COO tracks both as follow-on TOs to author
  when their gates clear. Two patterns CTO ratified for carry-forward: receiver-rejectable gates (a
  GO not citing its gates is treated as mis-sent) and negative controls on healthy legs.

## Post-midnight addendum (00:0x-00:3xZ 08-11)

- **RP-W5 items 2+3 forks both resolved at CTO:** item 2 stood down as covered-by-design, then
  AE's measurement INVERTED even the re-pointed premise (no gap existed — retry OnSuccess converted
  the day at 13:40:41Z; the 16:00Z sweep's zero-output was correct); CTO's restated D-24 wording
  corrected before landing. Item 3 ruled SCOPE-ADD + DEFERRED (not into the window); follow-on
  authored as **MDPF_REMED.RP-F1** (DS, staged behind window-proves, carries the 205/33 forecast).
- **Item 4 code-complete @2ba6417fbb (4/4 exercised), deploy leg HELD** — deploying makes the daily
  run RED correctly, and the RED must land expected, with the emitter ruling in hand.
- **LIVE PRODUCER OUTAGE surfaced (AE) and routed to CTO:** `opal-assets-daily-emitter` DOWN since
  08-08 — 08-09/08-10 die writing the Andrew-deleted `opal-assets-daily-aua` DDB table
  (ResourceNotFoundException); 08-08 died separately on VintageContradiction. mdpf/feeds/* frozen →
  the zeroed aggregate. NO serve impact (platinum frontier = 08-05 carry-forward). Fork at CTO:
  drop-the-write / re-create (his word — contradicts the 08-07 deletion) / re-point. The dirty TF
  plan's re-create row and this fork are the same object.
- **Window-planning evidence, live:** 08-10 aggregate ran 13:00:58Z, before the smartx pull landed
  13:36Z — the RP-W3 clock defect observed in the wild.
- CTO-binding targeted-apply line committed into RP-W3/RP-W4 @d98b441cf6; RP-F1 @ its own commit.
- AE proceeding to RP-W4 selector. DS live, driving W1/W2 to BUILD-READY.
