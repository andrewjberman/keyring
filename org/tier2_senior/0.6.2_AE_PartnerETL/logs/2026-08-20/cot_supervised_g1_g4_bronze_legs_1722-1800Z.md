# COT_SUPERVISED G1/G4 bronze legs -- one-shot landed, daily belt amended in place

**archetype:** IMPLEMENT
**serial:** 0.6.2_AE_PartnerETL (PID 23176, Monitor bb5aiy7je)
**window:** 2026-08-20 1722-1800Z
**TO:** COT_SUPERVISED.G1-G7 (joint, 0.2.0_DS gold legs / 0.6.2 bronze legs G1+G4; COO GO 63323)

## Current State

**G1 COMPLETE (bronze half): the account-attributes one-shot is LANDED + verified on served
bytes.** `s3://opal-data-cot/forwardfill_v2/account_attributes/ACCOUNT_ATTRIBUTES_DAILY_2026-08-19.xlsx`
(24,906 B, sha256 f21eea8a..., sidecar basis=land_time_measured). Zero-measure qt4 run -- the
export is EXACTLY the five CTO-design columns: ["Portfolio Group", "AccountID", "Position Only",
"Account Supervised", "Account Billable"]. 943 rows / 942 distinct accounts (matches the served
dim universe); Supervised 820 / Unsupervised 123; 0/942 conflicting flags (account-clean holds
full-universe); books Rubottom 399 / Bass 232 / Shipley 231 / "No Advisor" 81. ONE two-book
duplicate (z0927448821 under Rubottom AND Shipley, attributes identical) -- reported to DS
verbatim with dedup consequences (63328 seam ACKed 173411Z, land report 173818Z). As-of
2026-08-19 = the HAR oracle date, so DS's G3 tie-out joins same-vintage. Commit @25ccb05301.
BD persisted template minted: **270648** (NOT 270650 -- that was the RUN id; misreported once,
corrected on the record in 63366-63368 + the script NOTE + the thin envelope).

**G4 COMPLETE (config half): daily holdings template 226355 amended IN PLACE per CTO pin (B)**
(63339; COO 63341/63345/63354 carried into the TO): +Account Supervised (id 33, level 7),
+Holding Supervised (id 45, level 9), inserted verbatim from the qt1 Query/DimensionsFacts
catalog. GET re-read diff: exactly the two additions, 15 -> 17 dims, nothing lost. Ad-hoc QA
read via the REAL production path: 21 cols incl both, 18,051 rows, 1,376,586 B -- run-and-read,
nothing landed. **REAL acceptance = tonight's scheduled run** (ad-hoc-runs law: an ad-hoc
artifact is never production evidence). Pre/post enriched bodies committed @17c38a26f2 +
@e398873d58; `--rollback` re-PUTs the pre-image (same-window rollback path).

**G4b (new, COO 63345 / CTO re-rule 63350): my halves DONE, DS holds the one-commit.** I
authored the thin envelope (`account_attributes_template_thin_FOR_DS.json`, cites 270648,
grain/overlap caveats + ratified snapshot semantics in-comment) and own the BD side (270648
reuse endorsed, no re-mint). DS lands TABLE_QUERY_TYPE/"account_attributes": 4 +
TABLE_DATE_MODE ("Custom", 14) + SNAPSHOT_TABLES membership (RATIFIED) + the JSON + their
TABLE_CONFIG in ONE commit. Acceptance BEHAVIORAL (dict entries + one observed scheduled run +
sentinel + silver consuming).

## Findings on the record (all surfaced same-turn, none held)

1. **The ingest's "config-driven table set" docstring is false at :1261** -- the nightly
   enumerates hardcoded TABLE_QUERY_TYPE; a dropped template JSON is INERT. Surfaced 63348/63349
   BEFORE the ruling baked it into the TO; CTO owned the correction (63350), G4b re-ruled from
   pure-config to DS-side code with behavioral acceptance.
2. **endpoints/README.md:59 is false at the wire**: POST /v1/template/ with a real templateId
   MINTS A CLONE (minted 270653, same-name "Assets_Dim"; DELETED same window via
   DELETE /v1/template/{id}; roster re-read = single Assets_Dim). The true update verb:
   **PUT /v1/template/ with the id in the BODY** (200, in-place, response carries NO id -- GET
   diff is the only sound verify); PUT with id-in-path 405s. Doc defect routed (bd-tree doc,
   0.6.0/CTO to land the fix), not cross-tree-edited.
3. **run_query's return is the RUN id, not the created template id** (270650 vs 270648) --
   NOTE added to the fetch script so the next reader does not re-quote a run id as a template id.

## Blockers

**NONE.** One external gate, stated plainly: the next SCHEDULED cot chain fire is the G4 belt
acceptance + the G4b behavioral acceptance. Not deferrable-by-choice -- the acceptance is
DEFINED as the scheduled run's output. My proof instance (bronze group G1-G4) mints after that
verification, then RAVC close to COO cc CTO.

> ⛔ **CLOCK CORRECTION 2026-08-20 ~2045Z, MINE, load-bearing.** This section originally read
> *"tonight's scheduled cot nightly (~02:00Z window)"*. **THAT IS WRONG AND I CARRIED IT INTO
> FOUR MESSAGES (63366/63367/63368 + the G4 landing report).** The cot chain was re-anchored to
> **7:30 AM America/New_York = 11:30Z** (Andrew-direct 2026-08-14, MDPF_TRGALN §3 row 4); the
> `cron(0 2)Z` Rule I was reasoning from was **DELETED in that same change**
> (`eventbridge.tf:43-45`). Read at BOTH planes: DESIRED `schedule-et.tf:90` cron(30 7)
> America/New_York; APPLIED `aws scheduler get-schedule cot-bd-session-daily-et` -> State
> **ENABLED**, same expression. **So the acceptance fire is FRIDAY 2026-08-21 11:30Z**, not
> "tonight". CTO (63716) and COO (63713) held the same stale fact from my reports and have
> corrected their own boards -- four seats, one unverified fact, propagated by citation.
> **THE CONSEQUENCE THAT MATTERS: today's fire ran 11:31Z, SIX HOURS BEFORE the 17:50Z template
> amendment, so today's 19-column extract is NOT a G4 failure** -- a stale clock does not merely
> delay a verification, it frames a correct artifact as a defect.

## Next Steps

1. **[me, on the FRIDAY 2026-08-21 11:30Z fire -- watch armed, Monitor bgx6dde2b on the exact
   key]** Run `verify_g4_belt_acceptance.py`: served-bytes verify of
   `HOLDINGS_DAILY_2026-08-20.xlsx` (expect 21 cols vs the MEASURED 19-col baseline, 18,051 rows
   unchanged), the belt's FIRST REAL TEST (per-row Holding-vs-Account supervised disagreement
   with its denominator), both sidecars, the bronze sentinel, and G4b's schedule-landed proof
   (a landing timestamp INSIDE the 11:3xZ window -- the G1 bootstrap was a 17:36Z hand-run, and
   the verifier discriminates the two). Then mint
   `COT_SUPERVISED_PROOF_OF_SPEC_062_20260820.json`, validate rc=0, RAVC close to COO cc CTO.
   *Pre-fire negative control RUN 2026-08-20 20:49Z: 8/12 PASS, failing on exactly the four
   not-yet-true cells -- the instrument can fail, and fails in the right places.*
   *Runtime prerequisites for G4b VERIFIED DEPLOYED (not merely committed): the deployed
   `code/bronze/cot_bronze_ingest.py` @18:06:50Z carries the account_attributes dict entries +
   SNAPSHOT_TABLES membership, and `code/bronze/templates/account_attributes.json` is live
   @18:06:01Z -- the S3 template is what `load_template` actually reads, and its absence would
   have failed the table and SUPPRESSED THE WHOLE CHAIN'S SENTINEL.*
2. **[0.2.0_DS]** G3 tie-out (HAR oracle, grain-collapsed) + G2 served-dim re-read + G4b
   one-commit + G5/G6. All inputs from my side are delivered.
3. **[0.6.0/CTO]** the endpoints/README.md:59 one-line doc fix (routed finding 2).

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-which | A.3 exercise ("how do I grep the repo") | forwarder RAN (banner) -- PATH healthy 97/99 |
| comp-find | --name cot_bronze_ingest* / *.json data/cot / merge-daily* / "v1/template" / "226355" | located ingest + 5 template JSONs + the update-endpoint doc + 226355 references; denominators printed per call |
| comp-to | COT_SUPERVISED.G1-G7.retroactive-filter-and-portfolio-group | session TO context set (race-free per-session file) |
| comp-pipescript | NOT RUN -- deliberate | my legs triggered no gold run and touched no gold script (io/deployed/postdeps are gold-script instruments; A_00 is DS's leg and DS ran their own Phase-1 io call per their 63328) |

Raw reads beside the tools: template JSON inspection + BD API endpoint doc reads (native Read /
pipe-safe python -c against repo files -- tool-first localization, raw drill-in per the
two-stage standing rule).

## Deploy/ledger note

No Terraform, no Lambda, no EC2 code, no served-key move. The two production mutations are
BD-side template config (226355 in-place, rollback pre-image committed) + one new bronze S3
object under a NEW prefix with zero existing consumers (DS's silver entry is the first consumer,
their commit). No deploy-completion ledger entry required; nothing half-landed.
