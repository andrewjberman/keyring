# Semantic notes — S3 buckets, in Andrew's words

**Capture protocol:** Andrew narrates what each resource IS and MEANS "at this time"; recorded
same-turn, verbatim-anchored (the phrasing is the record), then normalized. Canon position:
these are **legislation events** (vertical-overlay / D3-contract declarations). Deltas vs the
blind instrument pass are called out — they are the program's product.
**Session:** 2026-07-30, batch-1 buckets (the 7 largest pipeline estates).

---

## THE ARCHITECTURE LEGISLATION (stated across notes 1/2/3/5/7 — the load-bearing declaration)

**Target state, Andrew-direct 2026-07-30:** `opal-data-assets` is to become **"the canonical and
singular source of truth for all partner data"** — consolidated taxonomy, resource design, and
processes. The per-partner original buckets (`bd` = 49 Financial, `inf` = Inflection, `cot` =
Cottonwood) all migrate their business functions INTO assets. **"We are mid-migration in doing so
as of today."** Medallion contract, his words: assets houses **`/bronze -> /silver -> /gold`
("raw -> parquet structured/cleaned -> logic/derived/analytical")**, which is the prerequisite for
**`/platinum` serving artifacts living in the portal bucket** (`opal-data-portal-v2`).

Canonically: a **D3 canonical-source contract** declared for the partner-data domain, with a
lifecycle consequence — three healthy-looking estates are SCHEDULED TO CONVERGE, which no
instrument can see (their writes are green daily; their future is decommission-by-migration).

---

## 1. opal-data-bd — "the 49 Financial original data bucket"

**Verbatim:** "It is named opal-data-bd because it is the first bucket we ever made for partner
data and was from black diamond, hence it's related process 'bd-pipeline'. This is 49 Financial
and should not be confused for a general black diamond bucket, it is just poor naming. We really
want to migrate the functions of this bucket to opal-data-assets... We are mid-migration in doing
so as of today."
**Normalized:** business_function=49-Financial partner data (original estate) ·
target_state=migrate-into-assets, mid-flight · naming=historical fossil (Black Diamond was the
custodial SOURCE of the first feed, fossilized into the bucket name and the bd-* fleet names).
**Instrument delta:** the instruments (and my own card) read "bd" as a Black-Diamond estate
generally; the name encodes the FIRST USE, not the function. → class: **name-encodes-history**.

## 2. opal-data-assets — "the consolidated bucket"

**Verbatim:** "we want this to become the canonical and singular source of truth for all partner
data."
**Normalized:** business_function=canonical partner-data SSOT (target) · target_state=THE
convergence point · status=receiving migrations now (its per-custodian prefixes wrote today).

## 3. opal-data-inf — "the inflection wealth management bucket"

**Verbatim:** "it was designed in the same style as opal-data-bd but like that bucket, we want to
migrate all of the business needs for inflection assets to the opal-data-assets bucket."
**Normalized:** business_function=Inflection partner data · target_state=migrate-into-assets.
**Instrument note (INFERRED, unconfirmed):** the five cold silver categories found in the walk
(accounts_dim / orion-rest / api_dims / transactions / performance_dim, Apr–May) may be the
already-migrated-away portion of this estate's needs. Flagged as hypothesis, not fact.

## 4. opal-data-demo — "just demo data for advisor intelligence"

**Verbatim:** "it can be left alone."
**Normalized:** business_function=Advisor Intelligence demo prop · target_state=as-is.
(Confirms the earlier KEEP ruling; class demo-prop already captured.)

## 5. opal-data-portal-v2 — "the serving bucket for the opal frontend product"

**Verbatim:** "the 'portal' or 'dashboard' as it is known. The plan for this is that /platinum
files, the serving layer artifacts for that portal/dashboard product live here. Any partner data
required for this, namely in Model Portfolios or Advisor Intelligence should be coming from
opal-data-assets, which will house the /bronze -> /silver -> /gold (raw -> parquet
structured/cleaned -> logic/derived/analytical) which is the prerequisite for the /platinum
artifacts in the portal bucket."
**Normalized:** business_function=portal serving bucket · target_state=/platinum-only for
serving artifacts; partner-data inputs sourced exclusively from assets' medallion.
**Instrument delta:** current layout has 27 top prefixes (json/, cache/, benchmarks/, canon/,
macro/...) — the target-vs-current gap is large and now MEASURABLE against a declared target.

## 6. opal-data-imo — "a source bucket for developing a business development pipeline"

**Verbatim:** "...for insurance sales companies that we may attempt to solicit business from for
asset management."
**Normalized:** business_function=business-development prospecting estate (insurance-sales
targets for asset-management solicitation) · target_state=parked, keep.
**Instrument delta:** instruments saw "FIND_INSURE crawl, dormant 59d." The function is
PROSPECTING — value realized in future solicitation, not in pipeline freshness. Dormancy is the
wrong axis entirely for a prospecting asset.

## 7. opal-data-cot — "the partner data bucket for cottonwood capital advisors"

**Verbatim:** "another opal partner. Again, we want this functionality to all be transferred to
opal-data-assets."
**Normalized:** business_function=Cottonwood partner data · target_state=migrate-into-assets.
(Firm-separation gates continue to bind bd↔cot↔inf until migration design says otherwise —
migration INTENT does not lift the separation LAW.)

---

## New ontology classes from this pass

- **name-encodes-history** — a resource name fossilizes its first use and misleads every later
  reader (bd ≠ Black Diamond-general; it's 49F). Instruments read names as semantics; names lie
  with authority.
- **migration-in-flight** — an estate can be healthy on every instrument (daily writes, full
  event spine) while sovereignly scheduled to disappear into a successor. Target state lives
  ONLY in declarations like this file; no measurement reaches it. (Phase-inverse of
  superseded-in-place: smartx-v2 is post-migration debris, bd/inf/cot are pre-migration
  sources.)

---

# Batch 2 (2026-07-30, cards 8-14)

## 8. opal-data-mdpf — "very questionable and probably should not exist"

**Verbatim:** "This bucket should be already represented as a subbucket contained within
opal-data-assets (for bronze silver gold) and within opal-data-portal-v2 (for platinum). This
will need to be investigated explicitly."
**Normalized:** business_function=Model-Portfolios feed data · target_state=DISSOLVE into
assets(medallion)+portal(platinum) · action=EXPLICIT INVESTIGATION ordered.
**Delta:** created 2026-05-18 — AFTER assets existed. A canonical location existed and the
resource was created beside it. → new class: **canon-bypass-creation** (the founding-diagnosis
specimen: generation without situational awareness).

## 9. opal-data-etfs — mission-critical, migrate-with-assessment

**Verbatim:** "Ultimately this should be migrated to opal-data-assets, but because it is very
important, it has to be assessed for robustness of data ingestion/storage as the function which
it supports (ETF rebate ops) is mission critical. Nevertheless, I think there is a lot of
overlap within opal-data-assets for this function and that will need to be reviewed so there
are not clashing definitions/functions/pipelines."
**Normalized:** business_function=ETF rebate ops basis (mission-critical) · target_state=
migrate-into-assets GATED on robustness assessment + overlap/clash review (definitions,
functions, pipelines).

## 10. opal-data-astn — CEO morning-update emails

**Verbatim:** "This is a function for generating morning update emails for our CEO from
Financial Times and WSJ. We will want to review the quality of the outputs of this at some
point. There is a project attached OPAL_ASTNWSJ or something similar."
**Normalized:** business_function=CEO morning digest (FT+WSJ) · target_state=as-is ·
open=output-quality review; project code to reconcile.

## 11. opal-data-schwab — "should not even exist anymore"

**Verbatim:** "the opal-data-assets/schwab/ sub-bucket should cover all of this and more. Worth
exploring the autoschwab ec2 box and making sure there is no connection to this thing and if
so, it should be summarily deleted."
**Normalized:** business_function=NONE intended (superseded by assets/schwab/) · target_state=
DELETE, gated on the autoschwab-EC2 connection check + live-writer census.
**Delta:** instruments show LIVE writers as recent as 07-16 (bronze/rps) and _ops/ SI2 pull
scripts 07-15 — the connection check is not a formality.

## 12. opal-data-smartx-v2 — delete after validation, archive the code

**Verbatim:** "This bucket is also superseded by opal-data-assets/smartx/, should be deleted
upon validating the content in the opal-data-assets/smartx/ bucket. The only thing I'd want to
make sure here is that the code is archived somewhere, maybe in an archive /code folder in the
opal-data-assets/smartx/ bucket."
**Normalized:** target_state=DELETE, gated on (a) assets/smartx/ content validation,
(b) code archived to an assets smartx archive location. Confirms superseded-in-place.

## 13. opal-data-news-v2 — delete if nothing surfaces on the portal

**Verbatim:** "Need to check dataflow and see if any artifacts from this go anywhere, I'm
guessing they have no consumers that surface on the portal frontend and if so this should be
deleted."
**Normalized:** target_state=DELETE, gated on a dataflow trace to portal-frontend surfaces.

## 14. opal-data-trade-submissions — live product infra, one deprecated leg

**Verbatim:** "The trade parquet batch export looks deprecated, but we do use trade submission
handlers and infra for the portal's 'Trade Submission' page (C4 'Interactive Product' segment).
Worth review as well."
**Normalized:** business_function=Trade Submission page backing store (C4 interactive-products
segment — Andrew routing in canon vocabulary) · target_state=KEEP · review=parquet batch leg.


---

# Batch 3 (2026-07-30, cards 15-21)

## 15. opal-data-news-av — "almost surely all ready for deletion"

**Verbatim:** "This bucket and associated resources are almost surely all ready for deletion."
**Normalized:** target_state=DELETE (bucket + associated resources), gated on the live-vein
check: seeking-alpha/ wrote TODAY 14:00 (the scraper pair lands there daily) -- the gate must
trace where that flow goes and enumerate the associated-resource set (scrapers, their AMI
rotation slots, the lambda family) before execution.

## 16. opal-data-pm — Portfolio Management backend

**Verbatim:** "This is an 'Interactive Product' C4 backend, for the Portal 'Portfolio
Management' tool."
**Normalized:** business_function=Portal PM tool backend (C4 interactive-products) ·
target_state=KEEP.

## 17. opal-data-portfolio — twin investigation ordered

**Verbatim:** "We will need an investigation into this and 16 to identify if there are
essential functions in both or if one is purely deprecated twin."
**Normalized:** target_state=INVESTIGATE (queue Q-4, to 0.7.0 at completion).

## 18. opal-market-data-v2 — "looks like delete"

**Normalized:** target_state=DELETE, gated on the origin trace (frozen-at-creation-day estate;
shared-reader caveat applies).

## 19. opal-market-update — "very likely delete"

**Normalized:** target_state=DELETE, gated on consumer trace.
**Delta -- THE INVERSE DIRECTION, first clean specimen:** instruments read ALIVE (fred/ wrote
TODAY, daily lambda writer) and the sovereign reads DELETE. A producer can keep a corpse warm
indefinitely: activity is not purpose. -> new class: **zombie-flow**.

## 20. opal-313476888478-lambda-artifacts — keep, investigate later

**Verbatim:** "This is likely a keep, will want to investigate later but low priority."
**Normalized:** target_state=KEEP · queue Q-5.

## 21. opal-313476888478-globgrph — essential infrastructure

**Verbatim:** "This is essential infrastructure 'Estate Infrastructure' C4 material. Also to
your point, we want to make a note to investigate all these shared readers, it seems to me
like this should be a lot more organized and defined."
**Normalized:** business_function=world-model substrate (C4 estate-infrastructure) ·
target_state=KEEP · shared-reader organization -> queue Q-6.
**Process directive (standing):** "Items like this that we mention will require investigation
later will be assessed at the completion of our work and issued to 0.7.0" -> INVESTIGATION_QUEUE.md.


---

# Batch 4 (2026-07-30, cards 22-28) + the mdpf condemnation

## 22-25. cloudtrail-logs / cur / mcp-audit / mcp-athena-results — KEEP (cohort)

**Verbatim:** "buckets 22-25 all look good, i dont ever really look into these but i think they
are all valid for their purposes."

## 26. opal-schwab-d4-access-logs — purpose unknown to Andrew; INSTRUMENT FOUND

**Verbatim:** "i do not know the purpose of bucket 26, that looks like random agent idea that
may or may not have ever been allocated under a defined project, likely decomission/delete."
**Instrument finding (post-ruling):** opal-data-schwab has server-access-logging ENABLED
targeting this bucket -- it is an ARMED READER-CENSUS INSTRUMENT on the very bucket ruled
should-not-exist. Its quiet-since-07-23 IS the census answer (near-zero access for a week).
**CTO recommendation surfaced:** harvest its logs as the Q-17 opal-data-schwab deletion-gate
evidence, then delete BOTH together. Armer unknown (created 07-17, not in TF, no project tag).

## 27. opal-served-key-write-trail-logs — explained (Andrew: "definitely want to know more")

Dedicated CloudTrail `opal-served-key-write-trail`: Data events, WRITE-ONLY (readOnly=false),
scoped to arn:aws:s3:::opal-data-{inf,bd,cot}/platinum/firm/* -- the write-provenance black box
for every client-served firm artifact: who wrote a served file, when, with what identity.
**Migration note:** its selectors encode the CURRENT serving layout; when platinum moves to
portal-v2 per the target architecture, the trail's selectors must move WITH it or it silently
watches empty prefixes (applied-despite-hold cousin, pre-flagged).

## 28. terraform-state — KEEP ("yeah this is a keep")

## opal-data-mdpf — CONDEMNED (hardens the batch-2 #8 ruling)

**Verbatim:** "yeah this whole bucket is garbage, this is agents just making duplicate
resources, i would never ask for an 'estimate' for a surface like ETFs that absolutely need to
be exact and we have the resources to be exact. there should be a daily writer for etf ACTUAL
holdings, which i think has nothing to do with any of these resources, prime example of cruft
and agentic slop."
**Normalized:** the ESTIMATE MECHANISM itself is condemned, not just the bucket location. The
estate already measures ETF holdings EXACTLY (the {bd-49f,inf,cot}-etf-ownership-daily writers
into opal-data-etfs daily/). Consequence for the wsd-49f frozen-frontier decision: DO NOT
re-point the estimate feeder -- RETIRE the estimate leg and wire MDPF's etf decomposition to the
ACTUAL-holdings source (design task, folded into Q-2 dissolution).
**CAUTION carried from the estate record (2026-07-29 teardown doctrine):** identity_2 is a LIVE
GATE fed from etf_decomposition -- the unit of retirement is the WRITE, not the producer;
preserve the gate's input before deleting anything in this chain.


---

# Batch 5 — FINAL (2026-07-30, cards 29-35). THE S3 LAYER IS FULLY WALKED.

## 29. lambda-layers — KEEP-presumed (not explicitly ruled; deploy-plane sibling of artifacts)
## 30. ci-staging — "looks dead but id check on the lambdas aspect" -> CHECKED -> DELETED
Gate result: lambdas/ held ONE stale staging zip (seeking-alpha-news-scraper.zip, Feb 20, Q-15
teardown family); rest = news-experiment deploy zips + a moltbot credential helper. All contents
archived; deleted; 404-verified.
## 31. runner-shared — "check on this further" -> CHECKED -> KEEP, GROUNDED
It is the EC2 telemetry bootstrap kit (opal-telemetry.sh/py, telemetry-sync units, gold_prof.py);
data/inf/scripts/gold/orion-gold-dispatch.sh:95-96 pulls it at every inf gold dispatch (ran today).
## 32. infrastructure-snapshots — KEEP + Q-20
**Verbatim:** "keep but will need to be investigated because that daily report is a mess we meant
to clean it up with INFRPT project but havent had time to do it."
## 33. crawl-catalog — "used for DATA_PLATFORM and maybe DATA_ANALYTICS ... probably done for
now and delete" -> DELETED (archived 20 objs incl. version history purge 41; 404-verified).
Associated resource NOT ruled: orion-crawl-harness EC2 (its writer) still exists -> Q-22.
## 34. website-backups — KEEP ("34 is a keep")
## 35. opalinvest-portal — delete-instinct REFUTED by the gate; Q-21 consolidation instead
**Verbatim:** "really loooks like a delete will definitely want an investigation into that and
any associated resources, if opal-data-portal-v2 or something is actually pulling info from here
(possible) then those assets should just be in the portal not in whatever this thin little thing
is."
**Gate:** comp-routes = it is the DEFAULT (SPA) CloudFront behavior origin (shared-advisor-router
edge chain in front); root holds index.html/favicon/vite.svg (the app shell); portal deploy wrote
07-29 18:01. Deleting it removes the dashboard's front door. Andrew's architectural intent
(assets belong IN the portal serving bucket) becomes Q-21: a CF re-origin consolidation design
(merge shell+assets into portal-v2, one origin), not a bucket delete.

## S3 LAYER CLOSE-OUT
39 -> 32 buckets. 7 DELETED this session (ajb-workflow, cloudfront-logs, aaii-v2,
analytics-dashboard, market-data-v2, ci-staging, crawl-catalog) -- every one archived
pre-delete, 404-verified, positive-controlled. Every surviving bucket carries a sovereign
business-function record. Delete-gated pending elsewhere: schwab (migration), smartx-v2
(validation), news-v2 (final trace), news-av (Q-15), market-update (Q-16), mdpf (Q-2/Q-18
condemned). 25 ontology classes; consequences C-1..C-12; queue Q-1..Q-22.
