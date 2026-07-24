# 0.6.2_AE_PartnerETL~C — CI-C1C2 contract census, 2026-07-24T17:27Z .. 18:35Z

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE, COORDINATE

## Summary

P0 dispatch to build two event contracts. **Grounded before building, and the ground moved the program:
CONTRACT C1 ALREADY EXISTS, IS WIRED ON 8 OF 8 FEEDS, AND FIRED EVERY TRADING DAY OF THE "FREEZE" I HAND-FIXED
FOUR HOURS EARLIER.** MDPF reads a *second*, unwired silver lineage. So today's P0 was a **lineage** problem,
not a conversion failure — CTO accepted it and is correcting a diagnosis he gave Andrew twice.

Then followed row 2 down and found **C2's writer already exists and already reads the correct lineage** — it is
**schedule-only**. The residual is a notification, a permission and an idempotency test, not a build.

**Nothing was built and nothing landed.** One scope ruling sits at CTO. **Five corrections to my own work today,
the fifth in this window** — a false `does-not-fire` that three independent signals agreed with.

## Work Done

1. **ACK + TENSION NAMED UP FRONT (17:27-17:28Z)** — acked P0, flipped to pending, and stated *before starting*
   that acceptance 1+2 are exercise-shaped while the deploy leg was (then) believed blocked, so parts might be
   honestly `FIRES-BUT-UNEXERCISED`. Committed to reporting **EXERCISED-against-live** separately from
   **BUILT-but-unexercisable** rather than one blurred number.
2. **THE CENSUS (17:30-17:45Z)** — 8 live `LambdaFunctionConfigurations` on `opal-data-assets`, read from
   `get-bucket-notification-configuration`, all `ObjectCreated`, all bronze-prefixed. Cadence **proven per
   object**: bronze `08242234.CRS20260723.RPS.zip` 10:15:57Z -> silver `fact_rps/date=2026-07-23/` 10:16:04Z,
   **+7s**, and the same every trading day 07-16..07-23.
   >> **C1 never stopped. `opal-data-bd/schwab/silver/rps/` — what the mdpf gate reads — is a second lineage
      with no event wiring.** Reported to CTO *before* building anything.
3. **THE TWO-LINEAGE NON-EQUIVALENCE (17:40Z)** — 93,131 vs 93,126 rows (**5-row delta**), **63 vs 11 columns**,
   5 shared names, 6 renamed; bd-tree is a **Rule 17 field-slimming violation**. **Named the "just point it at
   the fresher one" option and explicitly refused to recommend it** — the same shape as my 0833->0824 error
   this morning. CTO made it a gate: no repoint until the 5 rows reconcile and the 11 names map.
4. **ASKED FOR A RULING RATHER THAN TAKING ONE (17:45Z)** — exercising C1's arbitrary-date property needed a
   **historical bronze landing** (Rule 17a territory). Asked CTO; **refused**, on 17a *and* on the sharper
   ground that it would not prove the property anyway. **Marked arbitrary-date `UNEXERCISED`** and kept the
   converter evidence separate from event-path evidence rather than merging them.
5. **FIFTH SELF-CORRECTION — A FALSE `does-not-fire`, RETRACTED BEFORE IT TRAVELLED (18:05-18:11Z)** — I
   reported `silver-etf-filepoint` as a dead contract. **False**: it is a **1->2 fan** writing
   `pathfinder/{PFDE,PFOE}/silver/`, current through 07-23 (bronze 22:00:10Z -> silver 22:00:16Z).
   **My census derived each feed's expected silver prefix FROM its bronze prefix**, so the one feed violating
   that assumption read **ABSENT** rather than **UNMEASURED**.
   >> **THREE SIGNALS AGREED WITH THE WRONG ANSWER** — empty silver prefix (my assumption), DLQ depth 0
      (nothing failed), log filter `"filepoint"` -> 0 events (**that lambda logs no application text at all**).
      Plus a near-miss: my first CloudWatch query used a **future-dated window** and returned 0, caught by a
      positive control rather than by the zero looking wrong.
      **Corroboration between instruments that share an assumption is not corroboration.** Reading the deployed
      converter source is what broke it — the one signal not derived from my model.
6. **§1 RE-ANCHOR, GROUNDED MYSELF (18:00Z)** — COO relayed CVO's finding and *asked me not to take it on
   relay*. Read it: `:541` is the spine gate; **`:562-589` is a separate, later fail-safe** that defers on a
   stale partner's unreadable roll-source **with `spine_fresh` TRUE**. Confirmed independently. **Struck any
   design justification of the form "this removes the all-or-nothing gate"** and restated C2's property
   positively instead.
7. **13th-ITEM EVIDENCE, NOT A FIX (18:10Z)** — `_roll_source_exists:354` classifies on **`head_object`**, so
   granting `s3:ListBucket` fixes the symptom and leaves the wrong instrument. **Listing is this estate's
   sanctioned landing-verification instrument and cannot collapse ABSENT into UNREADABLE.** Routed to CTO,
   untouched.
8. **ROW 2 FOLLOWED TO ITS MECHANISM (18:20-18:28Z)** — `opal-assets-daily-emitter` **already reads MONOLITH
   silver** (own header `:35-39`, *"Never `opal-data-bd`"*), writes `opal-assets-daily-aua` `{run_date,
   cohort_id}`, and is invoked by **EventBridge only** (`cron(15 17 * * ? *)`) with a resource policy holding
   **exactly one statement and no S3 principal**. **C2 = a correct writer that is schedule-only.**
   Recorded the inversion: **C1 has event+floor, C2 has floor only, C3 has neither.**
9. **STOPPED AT A SCOPE BOUNDARY (18:29Z)** — C2's trigger **modifies an existing bucket notification-config**,
   which the OPAL_ASSETS **NEW-TERRITORY RULE** may forbid. **No `terraform plan` run, nothing applied.**
   Routed to CTO: *"I could argue the permissive reading persuasively — and that is precisely why I am not the
   one who should."*

## Deployment Sequence + Verification

Ledger `mdpf-ci-c1c2-contracts-20260724` opened 18:16Z, **CLOSED 4/4 at 18:29Z, nothing stranded.**

| leg | verdict |
|---|---|
| L1 | C1 **fires 8/8**, denominator stated, per-object lag +7s, filepoint retraction folded in |
| L2 | C2 **does-not-fire**; 3/3 candidate buckets examined; target `opal-assets-daily-aua` |
| L3 | committed `1daa84d197` (+`475d40731`) — **commit only, push is COO's** |
| L4 | **NOT BUILT** — closed naming the real reason (**scope ruling at CTO**), *not* the CI block |

>> **L4 IS THE LEG WORTH READING.** COO's correction — *"do not land" was over-broad; an open ledger citing
   the billing block is only correct for a leg that genuinely needs a refused workflow* — **did not unblock
   work; it removed an excuse.** I verified their correction at source myself (`lambda-deploy.yml` is a drift
   check, no deploy verb) and then could no longer close L4 behind a blocker that was not mine.

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-which` ×2 | **honest no-match both times**; did not pick a fuzzy candidate |
| `comp-pipescript postdeps` / `io` | **GAP** — `data/canonical/schwab/` gold family invisible; sibling of the cot gap logged 07-23 |
| deployed-code pull + `md5sum` | PASS — `mdpf-daily-trigger` byte-identical to HEAD, so §1's line citations cite the **deployed** logic |
| `aws lambda get-policy` ×2 (live primitive) | PASS — ruled out permission as filepoint's cause **before** finding the real one; established C2's writer has **no S3 principal** |
| `filter-log-events` | **FAILED TWICE AS AN INSTRUMENT** — future-dated window; text filter on a log with no application text |

**What worked:** reading **deployed source** broke two of my own wrong conclusions (filepoint, and the C2
"build from nothing" framing). **What failed:** my own census script — it encoded the bronze->silver mapping it
was meant to measure.

## MCP Traffic

6 sent, 6 received. Significant: COO GO 172727Z -> my ACK-with-tension 172827Z; census 174500Z -> **CTO ACCEPTED
+ re-scoped row 1** 174616Z (bronze write REFUSED, migration REFUSED); COO TO-correction 174401Z (deploy
over-broad) — **verified at source myself**; COO `[STOP AND READ]` 180356Z (§1 gone) -> grounded at `:541`/`:562`
myself; my filepoint retraction 181155Z; delivery to CTO 182929Z + COO 182954Z.

## Blockers

**BLOCKED-AT-CTO (routed, not stalled):** the notification-config **scope ruling** under the OPAL_ASSETS
NEW-TERRITORY RULE — the only thing between here and C2's trigger. Everything else in my lane is delivered.
Nothing pending at Andrew from this arc.

## Current State

Serial live (PID 29064), Monitor `bdkllgl7g`. Deliverable
`org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/CI_C1C2_contract_census_and_verdicts_20260724.md`
@`1daa84d197` + `475d40731`, written for CVO. TO `MDPF_CHANNEL_INDEPENDENCE.CI-C1C2` — rows 1+2 reported,
**C2 implementation NOT built**. Ledger CLOSED 4/4.

**NINE COMMITS UNPUSHED, held for COO** (`dff7849616` from the GC-BF1 block, plus `1daa84d197`, `475d40731`).

**Estate facts established this window, for whoever picks this up:** C1 fires on all 8 wired feeds; the MDPF
gate reads an unwired second lineage; the two lineages differ by 5 rows and 52 columns; `opal-assets-daily-aua`
has **no DDB stream** (blocks C3); `opal-assets-daily-emitter` is schedule-only.

## Next Steps

1. **[1.0.0_SA_CTO]** the **scope ruling**: does a 9th `LambdaFunctionConfiguration` on `opal-data-assets`
   clear the NEW-TERRITORY RULE's "no modifying existing notification-configs / pure to-add only"? **C2's
   trigger is blocked on exactly this and nothing else.**
2. **[CTO -> a lane]** the **two-lineage reconciliation** — 5 rows and 11 name mappings. Until then the
   migration stays REFUSED, and **MDPF keeps reading the hand-run lineage**, which means today's freeze can
   recur.
3. **[0.7.0_AE_CloudOps]** `opal-assets-daily-aua` has `StreamSpecification: null` — **C3 has no stream to
   subscribe to.** Belongs at the top of their sequence, not the bottom.
4. **[3.0.0_SA_CVO]** row 4, the sever exercise — **must sever a HEALTHY channel**; cottonwood would pass for
   the wrong reason.
5. **[1.0.0_SA_CTO]** 13th item: prefer **listing** over `head_object` in `_roll_source_exists` — the grant
   alone leaves the instrument that conflates ABSENT with UNREADABLE.
6. **[COO]** TOs should cite a rule's **CONTENT, not its number** — criterion 6 cited "NEVER#4" while that rule
   was being replaced under me. CTO is raising it.
