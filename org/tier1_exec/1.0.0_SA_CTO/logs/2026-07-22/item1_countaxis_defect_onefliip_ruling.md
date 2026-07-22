# 1.0.0_SA_CTO -- Andrew Item-1 investigation -> count-axis defect INSIDE the frozen-9 -> co-sign VOID; ONE-FLIP ruling; doctrine banked

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE
**Window:** 2026-07-22 ~1202Z (session start, post-crash) -> ~1345Z | **Serial:** 1.0.0_SA_CTO (main-fabric CTO)

## Summary
Session opened on a crashed fabric with the MDPF re-land co-signed 2-of-3 and held for Andrew's sovereign
limb. Re-grounded the whole gate from scratch (pin, live CF, ledger, FE payload) rather than trusting the
handoff. Andrew re-scoped to TWO named items instead of granting the limb. Investigating item 1 found a
**real defect inside the frozen-9 on Andrew's exact dates** -> **voided the 2-of-3 co-sign**, ordered a
fix-before-flip. Andrew then ruled **ONE FLIP with Cottonwood inside the gate**, overruling the joint
CTO+COO+MSTR two-flips recommendation. Banked the session's principles as a new doctrine file. 5 commits.

## Key rulings issued this window
- **COUNT IS IN CUTOVER SCOPE -> FIX BEFORE FLIP.** Ship-with-it-NAMED **refused** -- the defect sat on the
  highest-visibility dates on the board.
- **FLAG-2 preserve-tie to the served count BREAKS.** *Parity with a known defect is not a virtue.* Changes a
  CTO+Andrew co-signed decision; I own it and named it to Andrew.
- **2-of-3 never-widen co-sign VOIDED** -> fresh pin + fresh 3-pass + fresh 3 limbs. COO's custody rule bound
  me exactly as she wrote it.
- **ONE FLIP (Andrew-direct, VERBATIM "Let's push everything with Cottonwood")** -> no intermediate pin;
  supersedes my own ruling that the Cottonwood Global fold needed a *separate* co-sign (one-flip makes it
  THE co-sign); critical path moved DS -> DE.
- **Global gate: `same_source=TRUE` with an ENUMERATED 20-date exemption** -- refused BOTH options offered
  (a flag flip disables detection forever; permanent-RED turns a gate into an ignored alarm). **The exemption
  is a LIST, not a FLAG**, and a 21st date must go RED.
- **STOP-WORK on widening clause (vi)** after CVO proved per-band finds the same single date.
- **Standing order: the source cross-reference becomes a RECURRING PER-CYCLE AUDIT** -- artifact-internal
  checks are structurally blind to this class, so a one-time sweep gives zero ongoing assurance.
- **Trigger shape: `on_success`, not a completion-stamp S3 event** (Door-6 forgeability + a self-sustaining
  trigger loop). **My own "mirroring eclipse/smartx" order was AMBIGUOUS** -- it named two precedents that
  resolve oppositely; 0.6.2 correctly refused to guess.
- **Firm-separation word GIVEN (conditioned)** for Cottonwood -> MDPF: reads only
  `opal-data-assets/blackdiamond/cottonwood/**`, never `opal-data-cot`/`opal-data-bd`, stated in the ledger.
- **4th silver table + all 60 models / 911 accounts with `is_opal` as a LABEL: APPROVED** (Rule 17 forbids the
  business-row-filter alternative; *you cannot prove 296 of 911 from a table that only kept 296*).
- **AE spawn approved onto the critical path**; WS-5 re-scoped and its date moved rather than squeezing a lane
  to close a gap it does not own.

## The defect (the substance of the window)
The revamp producer reads its **VALUE** axis from eclipse (correct) but **IMPORTS `account_count` from the
LEGACY served artifact by date-join** (`dim_mdpf_aggregate_aua_timeseries.py:476-500`, wired `:812`),
discarding the count it already computes at `:427`. Legacy's date axis is itself broken. **Two axes of one
artifact, read from different days.** Observable: frozen-9 inflection COUNT `07-02 474 -> 07-06 540 ->
07-07 474` (+66 then revert) while VALUE 07-06 was correct -- **Andrew's sentence, reproduced by the revamp.**
Found by `0.4.0_DS_ClientPlatform` **in its own producer, brought not fixed**; **independently reproduced by
me before acceptance** with a separately-run positive control.

**Root cause (CVO, supersedes my "five separate defects" framing): THE LEGACY DATE AXIS IS NOT A TRADING-DAY
AXIS** -- 21 of 429 points on market-closed days, 20 real trading days omitted. Unifies 5 of 6 spikes. This
is CLAUDE.md NEVER#1 one level up: not *is the data stale on this axis* but *is this a trading-day axis at all*.

## Compiler Tools
| Tool | Where | Result | Note |
|---|---|---|---|
| `aws s3api list-objects-v2` (listing-based acceptance per OPAL_ASSETS ruling) | `gold/mdpf_revamp/` x4 runs | PASS | pin re-verify at 1205Z (9/9 unchanged, denominator 10 incl `precutover_frozen`) and post-rebuild (10 objects / 3 moved / 7 unchanged) -- independently, not from producer reports |
| `aws cloudfront get-distribution-config` (APPLIED truth, Rule 22a) | `EVTSA9VEHNZVH` | PASS | 24 behaviors / 7 origins / no assets origin / zero exact-9 -- rollback landed, verified not assumed |
| python/boto3 artifact diffs (legacy vs revamp) | inflection + global + 49F aggregates | PASS | DoD sweeps at total + band + non_model grain; mechanism test (model vs non_model vs custody vs count) separating reclassification from new assets |
| `lib/trading_calendar` + day-of-week resolution | Saturday-07-18 finding | PASS | NEVER#1 resolved BEFORE calling the datapoint a defect |
| `safe-commit.sh` (surface-check + comp-pulse risk-reflex) | 5 commits | PASS/CLEAN | 1 file vs 1239 danger nodes each; danger map STALE 198h (noted, not blocking) |
| `git merge-base --is-ancestor` + `git show origin/CLOUD:<path> \| wc -l` | push verification x3 | PASS | verified commits landed ON ORIGIN with a positive control, not from push output |

**What worked:** refusing to accept any producer's self-report -- every finding (DS's defect, DS's global
inheritance, COO's pin, CVO's bound) was independently reproduced before I ruled on it. Stating denominators
on every scan. **What failed:** my first pass was `model`-axis and inflection-only; the corrected claim then
generalized again across the value/count axis and was wrong the same way. **Gap found (fabric-wide, affects
every agent): `git log --since='<today>'` returns 0 ACROSS ALL AUTHORS** while the newest commit carries that
date (`--since='2026-07-21'` -> 289). **The /log skill Step-1 gathering command silently under-reports.**
Caught only because I positive-controlled a zero. Also: **the streak tracker has been INVALID JSON at HEAD**
(unescaped verbatim Andrew quote in `census_gate`) -- the durable record the cutover trigger is specified to
READ was not machine-parseable; repaired @346ed92fe with verbatim quotes preserved byte-intact.

## MCP traffic
~30 dispatches, hub for the item-1 investigation. Significant: the co-sign VOID + [STOP] to COO; the
fix-before-flip ruling + 3 binding conditions to DS; the class-sweep order and its retraction-acceptance; the
ONE-FLIP Andrew-direct broadcast (COO/MSTR/DS/DE, same turn per XXX.md); the enumerated-exemption ruling to
CVO; the `on_success` ruling + my own ambiguity admission to 0.6.2 and 0.7.0; the WS-5 re-scope; DE's two
blocking answers (revamp producer / flat shape / 4th firm leg, and build-independent-of-the-axis-advancing).

## Blockers
None self-blocking. **Held on Andrew (2 open):** (1) is day-one Cottonwood as two dots under building-block
names what he meant (288 of 296 accounts render under names their advisors do not use -- spec-correct, first
time seen with real numbers); (2) the `portal-v2 json/mdpf/**` bucket-policy Deny vs his 07-17
alert-suspension order (my read: a preventive control, not an alert -- but not built without his word).

## Current State (zero-context handoff)
- **SERVED = legacy portal-v2, known-good, de-widened.** Live CF `EVTSA9VEHNZVH` = 24 behaviors / 7 origins /
  no assets origin. **Nothing applied, nothing served, nothing stranded** this window.
- **CO-SIGN = 0 of 3.** Both limbs withdrawn; item-1 discharge REVOKED; item-2 re-arm STANDS.
- **STAGED (CHECKPOINT, NOT A PIN -- Cottonwood rewrites global again):** inflection `5e7b684dbc141eeff...`,
  global `08f9720ef2056fd0...`, A2 `ca0c6d1c57be0a70...`; 49F `aa5c5b85...`, A1 `529b7c21...`,
  A4 `8a195549...`, account_dist x3 all UNCHANGED. Verified by me at 1343Z.
- **49F: KNOWN DEFECT, NOT RETAINED EXPOSURE.** Prospective roster audit found **07-17 off by -10 accounts**
  (07-16 exact). Mechanism **UNDETERMINED** (not a mis-stamp, not a duplicated roster -- distributed across
  4 of 7 bands). **No rate may be quoted off n=2.** Count axis has **NO assurance instrument at all** --
  no source cross-reference exists historically and artifact-internal checks are structurally blind.
- **Per-cycle source audit LIVE** @b8efd3214: inflection 0 of 37 audited (389 dates UNAUDITABLE, not clean);
  49F 1 of 2. Hit count + denominator, never a percentage. DS caught its own frontier false-alarm pre-ship.
- **Enumerated 20-date exemption** @77d297819, all 4 CVO controls correct incl remove-a-date -> RED.
- **Doctrine banked:** `docs/doctrine/INSTRUMENTS_AND_AXES.md` @8650c448c + @39284dafc (9 sections + a
  7-question pre-PASS check), sibling to CONTROLS_OVER_CARE.
- **In flight:** DE folding Cottonwood (4th FIRM LEG on the revamp flat shape, NOT a `partners{}` entry);
  0.6.2 building the rebalancer converter half; 0.7.0 on IAM + exercise + the held Deny draft.

## Next Steps
- [1.0.0_SA_CTO] Gate the fresh 3-pass on the nightly-emitted Cottonwood-inclusive set; take the single
  binding pin THEN. Carry Andrew's 2 open questions. Re-verify AE/0.6.2's event+sweep landing together.
- [0.4.0_DE_ClientPlatform] Land the fold before tonight's fire; assert pre-07-21 byte-identity vs the
  Cottonwood-absent build (the (A) bound is true BY CONSTRUCTION -- make it a gate, not a claim).
- [0.6.2_AE_PartnerETL~A] Converter half + `on_success` + extend `expected_partitions` (event and sweep land
  TOGETHER); amend the stale `silver_registry.py:23` hyphen/8-digit declaration in the same commit.
- [0.7.0_AE_CloudOps] IAM + exercise-(a) with a real object; Deny HELD for Andrew.
- [3.0.0_SA_CVO] Exercise the enumerated exemption (4 controls) on DS's landed commit.
- [ANDREW] day-one Cottonwood rendering question; bucket-policy Deny vs the alert-suspension order.
