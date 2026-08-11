# RULE-14e CERTIFICATION -- CRO MDPF COLOCATION ATOM_DECOMP

**Certifier:** 3.0.0_SA_CVO · **2026-08-11, pass run 0531-0552Z** · **archetype:** VALIDATE
**Subject:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_COLOCATION_ATOM_DECOMP_20260811.md`
**Certified vintage:** @41692cd3d2 **as amended by @e621a52dc4** (the ONLY post-pin delta -- Part B
item 8 NNA/non-fee-residual un-merge + exception-list-PROVISIONAL marking, Andrew-driven; Part A,
the ground truth this cert gates on, is byte-identical between pin and HEAD @a4d5147211).
**Run record:** `workflows/atom_decomposition/runs/opal-data-mdpf-colocation/20260811T0440Z/`
(rectangle.final.json + run.json, schema-VALID per @919f888ece).
**Request:** 1.0.0_SA_CTO 052113Z (inbox); authority: Andrew-direct reinstantiation payload
@1a518b303f LIVE GATES "AT CVO: certify the mdpf decomp ground truth"; role widening @3c8418e34b.

---

## VERDICT: **CERTIFIED**

Status flips DRY/UNCERTIFIED -> **CERTIFIED** at my seat. Zero cells refused. The 4-act cutover
sequence (Part A3) may be sequenced on this ground truth, subject to the one sequencing caution
below (which is a precondition-naming obligation on act (ii)'s owner, not a hold).

**Method (per @3c8418e34b standing law):** independent re-derivation of every load-bearing cell
against LIVE state and source-at-HEAD -- not the artifact's own citations. My live reads are
stamped 2026-08-11T05:35-05:50Z. Denominators printed on every enumeration; both EventBridge
namespaces materialised in full (139 classic rules, 16 Scheduler schedules, no pagination leak).

## GROUNDING TABLE (claim -> my independent evidence)

| # | Rectangle claim (A1 items 1-7, delta rows 1-6) | My re-derivation (all 2026-08-11T05:35-05:50Z) | Verdict |
|---|---|---|---|
| A1-1 | Feed->read->serve chain alive same day | LIVE: feeds `model_aua_positions/49financial/2026-08-11.parquet` written 03:31:40Z; bells 49financial + inflection `json/mdpf/{firm}/account-distribution.json` BOTH 2026-08-10T11:30:39Z (head-object). SOURCE: `data/smartx/scripts/compute_account_distribution.py:66-67,117,164-165` @a4d5147211 hardcodes `opal-data-mdpf` + feed prefix | CONFIRMED |
| A1-2 | Both EC2 legs boot from bucket | `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py:47-49` (MDPF_BUCKET/CODE_PREFIX/DISPATCH_RELPATH); `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:130+` `s3 sync ... --delete` + FATAL guards on missing sync products | CONFIRMED |
| A1-3 | Accrual reads partner_roster from inside code prefix; daily 13:40Z | `data/mdpf/scripts/gold/build_portal_gold_accrual.py:106-140` (script-adjacent resolution; publishes into `code/scripts/gold/`); LIVE: Scheduler `mdpf-accrual-bridge-daily` ENABLED; 21 accrual logs (exact match to claimed 21), newest `20260810T134022Z.log` | CONFIRMED |
| A1-4 | Aggregate FEEDER_BUCKET hardcode; writes assets staging | `data/mdpf/scripts/gold/mdpf_aggregate_aua.py:65` FEEDER_BUCKET, `:79-80` PLATINUM_BUCKET=opal-data-assets PREFIX=`gold/mdpf_revamp/_aggregate_aua`; LIVE staging newest `2026-08-10.json` 13:00:59Z | CONFIRMED |
| A1-5 | Producers PUT into bucket, fail-not-degrade | Scheduler `wsb-49f-model-aua-pull-daily` + `wsd-49f-partner-held-etf-pull-daily` ENABLED; tonight's 03:31Z writes are the exercised proof | CONFIRMED |
| A1-6 | Deploy plane maps mdpf -> bucket; code/ written tonight | `.tools/safe_deploy_core.py:102-110` (`"mdpf": {"bucket": "opal-data-mdpf", deploy_gated: True}`); LIVE code/ newest 3 objects 2026-08-11T03:00:44-57Z | CONFIRMED |
| A1-7 | smartx timeseries reads model_aua_positions + non_model_aua | `data/smartx/scripts/generate_smartx_timeseries_and_metrics.py:86-88` @a4d5147211 | CONFIRMED |
| D-1 | "Good-as-retired" belief FALSE; bucket LOAD-BEARING LIVE | The union of A1-1..7 above, every leg exercised within 26h of my read | CONFIRMED |
| D-2 | Series-coupled, not parallel; FOUR-plus schedules | `data/mdpf/scripts/gold/mdpf_gold_consolidator.py:87` STAGING_PREFIX=`gold/mdpf_revamp`; `grep -c 'opal-data-mdpf'` over the whole 1,060-line consolidator = **0** (it never reads the bucket); consolidator:33 docstring names `_aggregate_aua/{date}.json via mdpf_aggregate_aua` as input. LIVE schedule census: floor 13:30Z + accrual 13:40Z + publisher 13:50Z (platinum write observed 13:50:49Z) + smartx cron(30 11) + feeder pulls -- five-plus, all ENABLED | CONFIRMED |
| D-3 | 08-10T13:40Z was ACCRUAL; main chain last ran 08-06 and FAILED | Telemetry: main-chain logs END at `mdpf_daily_20260806_130108.log`; `status.json` `"status":"failed"` updated 2026-08-06T13:34:31Z; accrual has its OWN daily log series through 08-10 | CONFIRMED |
| D-4 | Trigger ENABLED but event source DEAD 07-31; no clock floors the EC2 chain | LIVE: `mdpf-daily-refresh-trigger` ENABLED, ScheduleExpression=None, EventPattern-only (139 rules materialised); sentinel `opal-data-inf/gold/meta/pipeline-complete.json` LastModified **Fri, 31 Jul 2026 14:56:49 GMT** -- EXACT match. The ONE live mdpf clock floor (`mdpf-scheduled-floor`, Scheduler namespace, cron(30 13) UTC, ENABLED) targets `mdpf-gold-lambda` = the CONSOLIDATOR (`gold-lambda.tf:65-68` handler `mdpf_gold_consolidator.lambda_handler`; get-schedule Target Arn confirmed) -- NOT the EC2 chain. The chain leg has no clock. See caveat (a) | CONFIRMED |
| D-5 | Bell SPLIT: 49f+inflection live; cottonwood+global+flat frozen 07-23 | Head-objects: 49f + inflection 2026-08-10T11:30:39Z; cottonwood 2026-07-23T04:04:42Z; flat `json/portfolios/account-distribution.json` **2026-07-23T20:57:18Z** -- EXACT. Disable mechanism at source `compute_account_distribution.py:411-427` (`DISABLE_PORTAL_BELL_WRITE`, CTO 20260723 ruling named in-code) | CONFIRMED |
| D-6 | comp-estate's platinum key 404s; real key hyphenated, publisher-written | LIVE: `platinum/mdpf/aggregate_aua_timeseries.json` -> **404**; `platinum/mdpf/49financial/aggregate-aua-timeseries.json` -> 2026-08-10T13:50:49Z | CONFIRMED |
| A3 act-(iv) basis | 2 stages IAM-dead: 3.5 explicit-deny, 5 no-allow | The failed run's OWN tracebacks (`logs/mdpf_daily_20260806_130108.log:369` -- `explicit deny in an identity-based policy` on `opal-data-portal-v2/json/portfolios/aum-timeseries.json`; `:390` -- `no identity-based policy allows` on `opal-data-assets/platinum/mdpf/etf_ownership_timeseries/DIVZ.json`). Deny-vs-no-allow distinction preserved correctly per stage | CONFIRMED |
| Bonus D-7 | `_code` holds exactly 1 object | LIVE listing: 1 object, `mdpf-gold-lambda.zip`, 08-11T03:24Z | CONFIRMED |
| Rectangle self-consistency | Census 118 MEASURED / 2 INFERRED / 1 UNMEASURED / 7 NOT_MEASURABLE | Recomputed from the per-entity cells of rectangle.final.json: sums exactly (88+7+7+6+5+5 / 2 / 1 / 2+2+3) | CONFIRMED |

**Marked INFERRED cells (08-06 fire mechanism; 13:00Z staging producer identity) stand AS MARKED**
-- honest, non-blocking per the request scope. The two NOT_MEASURABLE clusters are declared with
their reasons. No cell asserts beyond its evidence grade. That discipline is itself part of why
this certifies.

## CAVEATS (none block the cert)

**(a) The clock-floor mechanism, corrected on the record.** CTO's 054322Z framing ("designed-but-
not-applied floor") is superseded by measurement: `mdpf-scheduled-floor` IS applied and ENABLED --
in the EventBridge **Scheduler** namespace, which `events list-rules` structurally cannot see (my
own first probe returned 1 rule and nearly reproduced the instrument-blindness class). It floors
the CONSOLIDATOR leg, not the EC2 chain, so delta row 4 stands exactly as written: the rectangle's
per-leg A4 table already made this distinction correctly. Note for future instrument work: any
"is there a schedule?" question must sweep BOTH namespaces (`events list-rules` AND
`scheduler list-schedules`) -- a single-namespace sweep under-reports and fails toward
"no floor exists," the deletion-warrant direction.

**(b) Sequencing caution -> act (ii) precondition (recommendation, not a hold).** Staging
`_aggregate_aua/2026-08-09.json` + `2026-08-10.json` were written at ~13:00Z with the main chain
DARK since 08-06 -- so the LIVE producer of the aggregate staging today is whatever W1a repointed,
and the rectangle marks that identity INFERRED. Act (ii) is "re-home the aggregate": its owner
should ground the live producer identity (one CloudTrail/CW read) as the act's NAMED PRECONDITION
per ITEM_0 landing-plan discipline before executing. Re-homing a leg whose current producer is
inferred risks re-homing the wrong writer or orphaning the real one.

**(c) Surprise-channel seam (one line, no action, not a rectangle error):**
`mdpf-daily-trigger/lambda_function.py:128-140` describes a scheduled-floor path INTO ITSELF
(FLOOR_SOURCE="mdpf.scheduled-floor" discriminator, "MUST match scheduled-floor.tf") -- live wiring
targets `mdpf-gold-lambda` with input `source:"aws.events"`. Stale design residue in the trigger's
source vs as-built wiring; the rectangle makes no claim about it. Routed to CTO as owner of the
instrument/roster lane.

**(d) Feeder-schedule instrument grain:** the rectangle's feeder schedule cell cites
`wp5-feeder-schedules.tf` (TF-desired) + tonight's writes (exercised). Live mechanism today is
Scheduler schedules (`wsb-49f-model-aua-pull-daily` etc.). Value correct, exercised proof correct;
the TF-file attribution is desired-layer. Cosmetic under the declared domain bar.

## REFUSED CELLS: **NONE.**

## WHAT THE CERT GATES -- released at my seat

The Part A3 four-act cutover (i) re-home feeder writes incl. the client-facing smartx read edge;
(ii) re-home the aggregate [precondition per caveat (b)]; (iii) re-home accrual partner_roster +
code sync; (iv) delete the 2 IAM-dead stages [grounded on the runner's own tracebacks, the
sharpest instrument]. **Protected surface reconfirmed live:** per-firm bells 49financial +
inflection `account-distribution.json`, both 2026-08-10T11:30:39Z, client-facing -- they migrate
WITH act (i), never break. Live bells' next fire ~11:30Z today: if act (i) sequencing overlaps a
bell window, the act owner owns the window call.

## What you should have asked but did not (Doctrine §7)

Whether the CONSOLIDATOR's 13:30Z clock floor turns the chain's darkness into silently-decaying
serves: the floor lambda runs daily on staging + feeds whose main-chain-fed members froze 08-06
(`non_model_aua`, delta row 10's no-tell staleness). A live floor over frozen inputs is the
anti-correlated-green shape -- the serving layer keeps updating its process-ts while its data-as-of
silently ages. The rectangle records the frozen input (row 10) but nobody asked what the floor's
daily fire DOES with it. Recommend the cutover's remediation register carry one line: "consolidator
carry-forward behavior on stale staging inputs -- verified/declared" before act (ii) lands.
(Observation routed, no machinery proposed -- moratorium respected.)

-- 3.0.0_SA_CVO
