# MDPF_CANON as the first /legacy-transform subject -- three questions answered by measurement

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Recon ID:** RCN-0009 -- registered in RECON_REGISTER.md
**Date:** 2026-09-18 ~17:1xZ to ~18:0xZ
**For:** 1.0.0_SA_CTO, answering msg 98014 (BRIEF: what I need analyzed on MDPF_CANON as the first
/legacy-transform subject). A RESEARCH record. It recommends nothing about whether or when ADVI_FIRMBKTS
runs; the subject choice is Andrew's and this record is scoped so that whichever subject he picks, the run
is cut to produce something that transfers.

**Andrew's words as the CTO relayed them (98014):** ADVI_FIRMBKTS is "the large scale project that I was
kind of hesitating on because it has to be executed immaculately"; LGCTFM "was designed to streamline the
planning/strategy necessary for that execution"; "the lower impact test run would be done on Model
Portfolios, specifically via MDPF_CANON, since its not as complex as the ADVI pipelines". The described flow:
the CRO runs /legacy-transform, gets a structured table of every current resource in NAME, POSITION and
DEPENDENCY, builds the desired-state table on LGIC_NAMING across the same fields, writes the migration plan,
hands to the CTO for /canonical-flow.

---

## 0. THE THREE ANSWERS, CONCLUSION FIRST

**Q2 (does the engine emit DEPENDENCY): NO. It is ABSENT -- not measured, not inferred, not present in any
field, edge or plan package.** The contract carries NAME and POSITION on every row and carries no relation
between two resources anywhere. The field in plan.json spelled `dependencies` is the R19 step chain inside
ONE row (895 of 895 populated values point at the same row's previous step; 0 point at another row). The
walk writes `"edges": []` by construction; the only edge the engine ever writes is the forks pass's
`REPLACES`. The plan's ORDER is the tension rank (a naming-grammar verdict) times the six R19 steps. So the
hole the CTO suspected is real and it sits exactly where he said: a cutover plan cut from a run today is
ordered by the canon's rules, never by what fires, reads or writes what. Details and every citation in s.2.

**Q1 (does MDPF_CANON exercise the same tension classes as 49 Financial): the engine cannot tell the two
apart, and on the structural comparison five classes are 49F-only.** Every tension the engine can type is
one class -- axis `A3`, kind `GRAMMAR`, deciding rule `R1` -- because those three are module constants
(`lib/opal_lgctfm.py:571-573` @af794c77e3) and `irreversible` is a constant `False` (`:610-620`). Measured:
49F graded run 179 of 179 tensions one class; the mdpf run this seat made today 10 of 10 one class. So "N
tensions of K types" reads "N of ONE" on both subjects and the engine's output cannot answer Q1. Answering it
from the tension map, the two PRDs and the two runs (s.3): the classes 49 Financial raises that MDPF_CANON
structurally CANNOT are (1) the irreversible bronze re-land (R9), (2) whole-bucket retirement under the 45-day
standard with versioned deletes, (3) the mint of buckets that do not exist, born with fence and prefix-grain
grants, (4) the identity spine's multi-spelling cutover across router map, IAM deny patterns and destination
policy, and (5) the router firm-map flip with the origin-response guard re-derived. MDPF_CANON in turn
exercises three things the 49F run did not: the FORK test (it fired today, `F-0001`, RULING-OWED), a
dedicated compute host (DEC-6), and a Scheduler-heavy trigger plane (4 of its 5 triggers are Scheduler
schedules, the API `describe-rule` cannot see).

**Q3 (has a lower-impact-first rehearsal transferred before): in this estate's record, same-subject
non-mutating dry-runs of the real mechanism transferred (3 of 3 read); a simpler subject or a staging
stand-in did not transfer or never ran (3 of 3 read).** MDPF was ALREADY chosen once as "D10's first worked
pipeline-family case" (2026-08-26) and never ran because it was never registered; MDPF's own earlier
platinum cutover (MDPF_CANPLAT_G2, 2026-08-07) landed the 13 firm slices where the canon now ranks them a
hazard and MDPF_CANON moves them again. And the real subject has already been walked: five runs over
`49financial` exist under `workflows/legacy_transform/blackdiamond-49financial/`, the graded one with a
1,074-package plan, MARK.json and a DIFF against its predecessor. The rehearsal question is therefore
inverted from how it was posed: the engine has been exercised on the REAL subject; a MDPF run adds a
SECOND subject, which tests the engine's transfer, not the migration's.

**The one thing worth more than the subject choice, as the CTO put it:** whichever subject runs first, its
plan cannot be handed to a COO at L5 as a decomposition seed until the run carries a dependency relation.
Section 5 proposes where that relation already lives in the estate (the graph module's trigger, source-map
and IAM reads), as a proposal only.

---

## 1. INSTRUMENTS AND VINTAGES (every number below is read at these)

| what | instrument | vintage / denominator |
|---|---|---|
| repo | `git rev-parse HEAD` | `af794c77e34866ba0799fef7409dcbe6a1a706f2` (local; origin/CLOUD read `ec5a7afd2b` by `ls-remote` at 17:5xZ) |
| engine source | `sed -n` on `lib/opal_lgctfm.py` (1588 lines); `comp-read --enumerate` | at HEAD above |
| contract schema | `org/standards/LGCTFM_CONTRACT.schema.json` read with `json` | at HEAD |
| schema record | `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` v0.1 (this seat's, 2026-09-16) | at HEAD |
| method note | `infra/logic/10_LEGACY_TRANSFORM.md` | at HEAD |
| tension map | `infra/logic/08_TENSION_MAP.md` (4.0.0_SA_CRO~D, 2026-09-13) | at HEAD |
| 49F graded run | `workflows/legacy_transform/blackdiamond-49financial/20260918T011619Z-8db9eb1/` (the ONE run carrying `HASHES.json`, R-40; `contract.json` git hash-object `33204e2983`) | repo_head `8db9eb1b`, graph `2026-09-18 00:54:00 UTC`, registry `scopes.json sha256:b2a54608f8ebbade` |
| all 49F runs | 5 run dirs enumerated with `os.listdir` | 2026-09-17T20:25Z .. 2026-09-18T01:16Z |
| mdpf run | `python lib/opal_lgctfm.py run --subject mdpf --run-home-subject mdpf --seed opal-data-mdpf --seed opal-data-assets/gold/mdpf_revamp --seed opal-data-assets/portal/gold --seed opal-data-portal-v2/platinum/mdpf --seed-loc opal-data-assets:gold/mdpf_revamp:json --seed-loc opal-data-assets:portal/gold:json --root <scratchpad>/legacy_transform` | run-id `20260918T174353Z-685dc7e`; repo_head `685dc7e7`; graph `2026-09-18 12:17:28 UTC`; registry hash as above. **Rooted in the session scratchpad, NOT the repo run home**: `git status --porcelain -- workflows/ infra/logic/registry/ ...LEGACY_SERVED_PATHS.json` printed nothing after the run. The run is an INSTRUMENT READ for this analysis and is not a project run; it is not committed and appends no mark. |
| live plane, mdpf token | `comp-find --corpus aws '\bmdpf\b' -i --all --limit 40` | 60 hits across 2590 nodes; graph built 2026-09-18 12:17:28 UTC |
| MDPF bucket root | `.tools/aws s3api list-objects-v2 --bucket opal-data-mdpf --delimiter /` and `--prefix bronze/ --max-keys 40` | root prefixes `bmkaud-evidence/ code/ diagnostics/ mdpf/ telemetry/`; `bronze/` returned NO keys |
| precedent census | `comp-find -i 'rehearsal|lower[- ]impact|pilot migration|worked[- ]first|first worked|dry[- ]run first|practice wave' --files --all --limit 120` | 799 hits across 167,969 files (68,646 ephemeral-floor, 14 unreadable, 4,882 binary NOT searched); six records read in head, s.4 |
| ADVI_FIRMBKTS | `org/missions/D8/ADVI/ADVI_FIRMBKTS/{project.json,prd/ADVI_FIRMBKTS_PRD.md}` | dep_stage PRD, coo_lane null |
| MDPF_CANON | `org/missions/D8/MDPF/MDPF_CANON/project.json` | dep_stage PRD, coo_lane null, PRD v2.6 ADMITTED |
| LGIC_LGCTFM PRD | `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` v1.4 | FWD-5/FWD-6 text at :106-125 |

The CTO's retraction of the `edges: []` caveat (his record `LGCTFM_EDGES_MEASURED_CAVEAT_RETRACTED_20260918T142xZ.md`)
is honoured: nothing below reads an empty `edges` as evidence about dependency coverage. The dependency
finding rests on the row fields, the plan's `dependencies` values and the engine's own source, not on `edges`.

---

## 2. Q2 -- FIELD BY FIELD AGAINST NAME, POSITION, DEPENDENCY

### 2.1 What one row carries (the schema, and what the engine actually writes)

The schema's `resource_or_plane_row.current` REQUIRES six cells and permits extras (`additionalProperties`
is `$defs.cell`); `desired` requires three. The engine writes exactly the six and exactly the three-or-four:

| field | 49F graded run (184 rows) | mdpf run (15 non-FORK rows) | maps to Andrew's word |
|---|---|---|---|
| `current.name` | 184 of 184 | 15 of 15 | **NAME** -- present, MEASURED (`comp-find --corpus aws` / `comp-trigger`) |
| `current.arn_or_path` | 184 | 15 | **POSITION** (where it is) -- present, MEASURED |
| `current.declaration` | 184 | 15 | POSITION (where it is declared: the `.tf` files) -- present |
| `current.drift_class` | 184 | 15 | POSITION (declared vs live) -- present |
| `current.live` | 184 | 15 | a factor; NOT_MEASURABLE on 180 of 184 and 10 of 15 |
| `current.client_facing` | 184 | 15 | a factor; `True` on 2 of 184, 0 of 15 |
| `desired.form / builder / verdict` | 184 | 15 | the desired twin (NAME under the canon) -- present, built by `grade()` |
| `desired.missing_registry_row` | 9 (the RAISE rows) | 2 | -- |
| `mark` | pointer to one of three registries or null | same | POSITION in the record |
| **any field relating this row to another** | **0 of 184** | **0 of 15** | **DEPENDENCY -- ABSENT** |

The schema record s.3.2 DESIGNED the per-class extras that would carry dependency -- a trigger's `target`,
a compute row's `iam_role` / `source_dir` / `artifact_key`, an identity row's `grants_on_subject`, a serving
row's `route` -- and the schema permits them. The engine writes none of them: the enumeration of the engine
for `"target"|iam_role|grants_on_subject` returns 0 CODE hits (30 hits total for the wider pattern, all on
`scopes.json`/`systems.json`/`edges`; `comp-read --enumerate`, DEF=0). Designed, unbuilt.

### 2.2 What the edges carry

`edge_type` admits `CALLS | READS | WRITES | TRIGGERS | INVOKES | STARTS | PUBLISHES | SERVES | AUTHORIZES |
MONITORS | REPLACES`. The walk writes `"edges": []` (`lib/opal_lgctfm.py:885`); the forks pass appends
`REPLACES` only (`:1171`); `cmd_run` merges the two (`:1500`). Six of six runs read (five 49F, one mdpf)
carry 0 edges. The CTO's retraction stands: an empty `edges` says nothing about dependency. What DOES say
something is that no writer for the other ten edge types exists in the engine at HEAD.

The rendered flow diagram inherits this. `flow.current.md` for the graded 49F run is 206 lines with ONE
arrow character in it; its `-- COMPUTE --` section reads `(none)`. FWD-5's ACCEPT ("what fires what, what
writes where, what serves it ... change a row ... and the picture changes") was graded EXERCISED on the
regenerate-and-compare arm; the picture it regenerates is a typed node list in three columns, not a graph.
This is stated as a reading of the artifact, not a re-grade -- the grade is the CVO's and this seat does not
touch it.

### 2.3 What the plan's `dependencies` field carries -- the reading hazard

`plan.json` (graded 49F run): 1,074 packages = 179 tensions x 6 R19 steps. `dependencies` is populated on 895
of 1,074 (every non-MAP step) and EVERY populated value is `<same row>-<previous step>`: 895 same-row, 0
cross-row (counted over the file). The engine builds it that way by construction
(`_build_one_package`, `:1289-1322`: `"dependencies": [row_id-prior_step] if prior_step else []`). The
mdpf run reads the same: 60 packages, 0 cross-row.

**So the plan has a field named `dependencies`, 895 of them populated, and none of them is a dependency
between two resources.** A reader who searches a run for the word finds coverage. This is a Rule 24 (iii)
intent-coherence issue on a field name and is proposed for LGIC_LGCTFM's record in s.5, not fixed here.

### 2.4 How the plan is ordered

`build_packages` emits each R19 step's packages "in the tension list's own order", and the tension list is
emitted pre-sorted by the printed rank (`_tension_rank_key`, `:628-639`): `irreversible`, `client_facing`,
`live`, `rules_colliding`, `object_count`. With `irreversible` a constant `False`, `rules_colliding` a
constant `1` (`len(["R1"])`) and `object_count` a constant `1`, the live order is: the 2 client-facing rows
first, then the 1 live row, then row order. Two of 1,074 packages carry `never_widen_signoff_owed`.

**Consequence for Andrew's flow:** the third field has no source in the run. A COO lane decomposing "from the
run's plan" (LGIC_LGCTFM FWD-6's ACCEPT, verbatim at PRD :119-120) would inherit an order in which a
trigger's PORT and its target's PORT are unrelated packages, and a bucket-policy REPOINT is not sequenced
after the bucket it grants on. Nothing in the contract would flag the inversion.

### 2.5 The coverage hole beneath the dependency hole -- compute is not in the rows

Even a dependency pass over today's rows could not order compute, because the walk is BUCKET-SEEDED and
compute rows are absent by construction:

| plane | 49F graded run | mdpf run |
|---|---|---|
| rows by type | CLOUDFRONT 1, EVENT_RULE 21, IAM_POLICY 2, IAM_ROLE 1 (a plant), S3Key 153, S3_BUCKET 2, S3_BUCKET_POLICY 2, SCHEDULE 1, SQS_QUEUE 1 (a plant) | S3Key 6, S3_BUCKET 1, S3_BUCKET_POLICY 1, EVENT_RULE 1, SCHEDULE 4, SQS_QUEUE 1 (plant), IAM_ROLE 1 (plant), PLANE 2, FORK 1 |
| LAMBDA / EC2 / ECS / STATE_MACHINE rows | **0** | **0** |
| what the live plane holds by the subject's token | not re-censused here (the brief's own pull: 6 types, 249 hits of 2,575) | `\bmdpf\b`: **60 nodes across 15 types** incl. LAMBDA 6, EC2_INSTANCE 1, IAM_ROLE 13, IAM_POLICY 11, SCHEDULE 6, LOG_GROUP 6, CW_ALARM 3 |
| real rows (plants excluded) | 182 | 14 |

For mdpf the walk returned 14 real rows across 7 kinds against 60 live nodes across 15 types carrying the
same token. The 6 Lambdas, the EC2 runner, the 13 roles and the 11 policies -- the resources that ARE the
dependency graph's vertices -- are not rows. The method note names the trigger half of this hole ("a
schedule whose name carries no firm shortcode and whose Lambda is the only place the bucket is named is
invisible to this walk"); the compute half is the same hole from the other side.

---

## 3. Q1 -- TENSION CLASSES BY TYPE, TWO LAYERS

### 3.1 What the engine EMITS (measured): one class, on any subject

| constant | value | line @af794c77e3 |
|---|---|---|
| `TENSION_AXIS` | `"A3"` | 571 |
| `TENSION_KIND` | `"GRAMMAR"` | 572 |
| `TENSION_DECIDING_RULES` | `["R1"]` | 573 |
| `_factor_irreversible` | returns `cell(False, "MEASURED", ...)` for every tension | 610-620 |
| `_factor_rules_colliding` | `len(deciding_rules)` = 1 always | 623-625 |

The engine's own comment says why: "This round's ONLY builder is grade() (DEC-4), the naming grammar ...
so every disagreement this walk can type sits on axis A3, deciding rule R1, closed by a rename". A HOME
tension (R4/R5/R7), a FORMAT tension (R9/R10/R11), an IDENTITY or PROCESS tension cannot be emitted by this
engine at HEAD. Measured on the two subjects:

| subject | tensions (real, plants excluded) | classes | node types under tension |
|---|---|---|---|
| 49financial (graded run) | 177 of 179 | A3/GRAMMAR/R1: 179 of 179 | S3Key 153, EVENT_RULE 20, S3_BUCKET 1, S3_BUCKET_POLICY 1, IAM_POLICY 1, SCHEDULE 1, + 2 plants |
| mdpf (this seat's run) | 8 of 10 | A3/GRAMMAR/R1: 10 of 10 | S3Key 6 (2 of them PLANE rows), EVENT_RULE 1, SCHEDULE 1, + 2 plants |

So under the engine, both subjects read "N of ONE type" and the CTO's discriminating framing ("40 tensions of
three types tells us less than 9 of eight") cannot be applied to a run's output today. A MDPF run would pass
or fail on GRAMMAR alone; so would a 49F run. **Whatever a first run "de-risks", it de-risks the rename class
only, on either subject.**

### 3.2 What each subject STRUCTURALLY holds (from the tension map, the PRDs and the runs)

Legend: BOTH = both subjects raise it; 49F-ONLY = MDPF_CANON structurally cannot raise it; MDPF-ONLY = the
49F run/PRD does not raise it.

| class (what MOVES) | 49 Financial / ADVI_FIRMBKTS | MDPF_CANON | verdict |
|---|---|---|---|
| GRAMMAR (rename, R1) | 177 rows | 8 rows | BOTH, the only class the engine sees |
| HOME move of gold/platinum to a firm bucket (R5/R6/R7) | gold 25,577 already in `-49financial`; platinum 24,631 in `opal-data-bd` moves | gold 907 objects out of `opal-data-assets` (R5); 13 firm slices out of `portal-v2` to firm buckets (R7) | BOTH |
| HOME move of bronze/silver to the ingest monolith (R4) | inf 28,614 bronze + 16,757 silver; bd, cot | MDPF bronze/silver home per PRD v2.5 R4 via the builder; count UNMEASURED here | BOTH (MDPF at smaller count) |
| FORMAT JSON to parquet at gold (R11) | bd gold 44,782 JSON | mdpf gold 907 JSON, publisher reads parquet | BOTH |
| IRREVERSIBLE bronze re-land (R9 parquet under bronze) | `opal-data-inf/bronze/` 4,802 parquet; `opal-data-bd/smartx/bronze/` 242 -- raw feed GONE, re-land from source on Andrew's per-use word (FWD-7/FWD-8) | `opal-data-mdpf` has NO `bronze/` prefix at root (measured, 0 keys); whatever sits under `mdpf/` was not walked | **49F-ONLY** (or MDPF UNMEASURED; either way not rehearsed) |
| WHOLE-BUCKET retirement: 45 consecutive quiet days read AND write, per-version deletes on a versioned bucket each on Andrew's word, bucket policy + OAC grant + TF bucket resource removed (ADVI_FIRMBKTS CONTRACTS "the decommission standard", F12) | three buckets | two PREFIXES inside a bucket that STAYS (`opal-data-assets` is the ingest monolith); no bucket policy, lifecycle or TF bucket resource retires | **49F-ONLY** (MDPF_CANON FWD-8 inherits the standard but applies it to trees) |
| NEW-BUCKET MINT born with the fence, read logging, versioning, prefix-grain serving grants and no bucket-wide grant (F4) | `opal-data-inflection`, `opal-data-cottonwood` do not exist | every MDPF destination exists or is ADVI_FIRMBKTS's to mint; MDPF_CANON FWD-2/FWD-6 WAIT on those two buckets | **49F-ONLY** -- and MDPF depends on it rather than rehearsing it |
| IDENTITY spine cutover: 8 spellings of one firm across router map, `tenants.py`, `roles.ts`, TF `firm_id`, FirmDestinationPolicy, `role/bd-*` deny patterns; the fence's enumerated ban list is a gate edit (F5, tension map #5) | yes, per firm x3 | one system token `mdpf`; the identity issue is the runner role's name colliding with `role/mdpf-*` denies (a narrow instance, ruled) | **49F-ONLY** in its multi-spelling form |
| ROUTER firm-map flip + origin-response guard re-derived + tenant assertion at tenant grain (LD-0442 hazard; F6) | yes | a tenant-asserting COMPATIBILITY MAPPING at the edge for `/api/general/mdpf/{firm}/`, URLs kept (PRD R3) -- proven through the page's own request path before the origin flips | **49F-ONLY** for the map flip; MDPF exercises the proof PATTERN only |
| CROSS-TENANT data in the shared serving bucket (tension map #3) | 19 advi objects | 13 mdpf objects | BOTH (MDPF at smaller count) |
| TRIGGER repoint (both APIs) | 21 EventBridge rules + 1 Scheduler schedule in the run (of 144 / 23) | 1 rule + 4 schedules (of 144 / 23) | BOTH; MDPF is 4/5 Scheduler, the API `describe-rule` cannot see (ADVI_FIRMBKTS DEC-11) -- MDPF exercises the two-API denominator better by proportion |
| FORK (two current rows, one desired string; canonical member RULING-OWED) | 0 FORK rows in the graded run | `F-0001` fired today on `gold/mdpf_revamp/` x `portal/gold/`, `canonical_member: RULING-OWED` | **MDPF-ONLY** as exercised |
| PLANE rows (tier-prefix grain) | 0 in the graded run (1 in run 4) | 2 | MDPF exercises it |
| CONSUMER repoint of a producer that reads the retiring tree (22 gold producers naming 6 buckets; the publisher reads the tree being retired) | the portal's pointers (F5/F6) | yes (PRD s.5b) | BOTH |
| DEDICATED COMPUTE HOST built by the migration (DEC-6 runner, `mdpf-{scope}-runner-role`) | no new compute | yes | **MDPF-ONLY** |
| RAISE rows (missing registry rows the builders refuse) | 9 of 184 | 2 of 15 (one real: `portal/gold/` -- K1 "segment 1 'portal' is neither a source nor a tier") | BOTH |

**The five 49F-only classes are the ones a MDPF_CANON rehearsal leaves unproven on the day that matters:**
R9 re-land, whole-bucket retire, new-bucket mint, the identity spine's multi-spelling cutover, the router
map flip with the guard. Two of them (R9, retire) are the ones the tension map calls irreversible or
Andrew-worded. **The three MDPF-only classes are real and useful** -- FORK is the one Andrew asked for by
name ("identifies if there are forks") and 49F's run has never fired it.

### 3.3 The FWD-6 fork, stated as two branches (the CTO's act, not this seat's)

- **Branch A -- MDPF_CANON is a rehearsal.** FWD-6 stays owed to "the 49 Financial migration's
  decomposition" (PRD :119-120), LGIC_LGCTFM stays REALIZED 8 of 10, no amendment. The dependency hole (s.2)
  then binds the 49F decomposition when it is cut.
- **Branch B -- MDPF_CANON closes FWD-6.** The ACCEPT is amended to name MDPF_CANON (or "a real migration").
  The dependency hole then binds THAT decomposition, and it is smaller (60 packages) but the same shape.

Either branch inherits s.2; the hole precedes the branch. Andrew's phrase "test run" reads as A to this seat
as it does to the CTO; that is a reading, not a ruling, and it is not acted on here.

---

## 4. Q3 -- PRECEDENTS: DID A LOWER-IMPACT-FIRST REHEARSAL TRANSFER BEFORE

Census: the regex in s.1 returned 799 hits across 167,969 files; the [HEAD] band (the term in the file
name) holds 64 files. Six records were read in head (the ones whose names carry a rehearsal, dry-run,
cutover-first or exercise act); this is a curated read of a printed census, not a complete history of
every rehearsal the estate ran. Denominator for the table: 6 of 64 HEAD-band files.

| # | record | shape | did it transfer |
|---|---|---|---|
| 1 | MDPF_ASSETS.029 (2026-05-20/21, `0.4.0_DS_ClientPlatform~B`): Phase 0 non-mutating dry-run of the v0.9 backfill on the REAL historical series; Andrew's "be ginger / nondestructive"; Phase 1 GO'd on the Phase-0 brief | same subject, real mechanism, no write | YES -- Phase 1 was cut from the dry-run's brief |
| 2 | INF AOR drift go-live rehearsal (2026-07-12, DS -> AE): the REAL publish path with sentinel account ids and a `[GO-LIVE-EXERCISE]` label; "not a bypass -- only the human text is marked" | same path, fake data, labels only | YES by design -- the exercise IS the path |
| 3 | comp-freshness D1 "dry-run GO, HOLD the land" (2026-07-12, CTO -> CVO~B): the dry-run found TWO SIBLING DEFECTS on different code paths; acceptance criterion 3 was FALSE because the probe measured defect (a) and the fix removed defect (b) | same subject dry-run | YES, and it is the Q1 hazard in miniature: a green on one class while the sibling class sat unmeasured, caught only because the dry-run compared verdicts rather than counted them |
| 4 | NFRA_WEBSITE TO-2 "opalinvest cutover STAGING FIRST" (2026-07-13/14, Andrew chose staging-first): Phase A staging verified 7/7 live; Phase B (apex DNS) never executed -- blocked on a human's registrar access; project closed 2026-08-25 as a record act | stand-in subject (staging) | NO -- the staging green did not reach the apex, for a class staging cannot hold |
| 5 | MDPF_CANPLAT_G2 cutover first-emission battery (2026-08-07, CVO~Z): MDPF platinum cut over to `opal-data-portal-v2/platinum/mdpf/{firm}/`, 12 of 12 pairs CITABLE | a completed MDPF migration | NO in the sense that matters here: those 13 objects are tension-map item 3's cross-tenant hazard today and MDPF_CANON moves them AGAIN; the stale hold `DO_NOT_DECOMMISSION_portal-v2_json_mdpf_49financial` names a key that "already moved once". A move made before the target was fixed produced a second move |
| 6 | "D10's first worked pipeline-family case" = MDPF (2026-08-26, tension map item 2's own history): MDPF chosen as the lower-impact first case for the bucket canon; `MDPF_CANON_PRD.md` v1.0 written 2026-08-25 "to register"; never registered until 2026-09-13, never decomposed | simpler subject first | NO -- zero transfer because zero execution; the L1 brief's Part 0 names the non-registration, not the direction, as the failure |

And the record that reframes the question: **the real subject has already been walked five times**
(`blackdiamond-49financial/`, 2026-09-17T20:25Z to 2026-09-18T01:16Z), the graded run carrying a
1,074-package plan, a MARK appended to `remediations.json` (`opal-data-bd/silver/`, row `LGIC_LGCTFM-W2-S3`)
and a DIFF between runs. LGIC_LGCTFM's FWD-5 practice wave ran over the 49financial subject. So "rehearse on
the simpler subject first" would be the estate's second pass at the engine, not its first, and the first was
on the real subject.

**Pattern, with its small n stated:** the three rehearsals that transferred were the real subject's real
mechanism run without writing; the three that did not were a stand-in, a pre-canon move, and a plan that
never ran. That is 3 of 3 and 3 of 3 from a read of 6; it is a pattern, not a law.

---

## 5. WHAT THIS SEAT PROPOSES FOR SCOPING THE RUN (research proposes; nothing here is dispatched or decided)

**P1. Before any run's plan is handed to a COO at L5, give the contract a dependency relation, from
instruments the estate already runs.** The edge vocabulary is already in the schema; the readers already
exist under Rule 20's graph module (`org/modules/graph/graph-call-manifest.yaml`): `comp-trigger --list
--json` carries each trigger's TARGET (TRIGGERS / INVOKES); `infra/aws/lambda/ci/lambda-source-map.json`
carries a Lambda's `source_dir`, `iam_role`, `artifact_s3_key` (CALLS, the READS/WRITES hop through the
source text); `comp-iam` carries a role's statements on the subject's surfaces (AUTHORIZES); the router
association in `07_ROUTING_REDERIVATION.md` carries SERVES. This is the schema record s.3.2's per-class
extras plus the s.6 edge types, populated. Whether it is a LGIC_LGCTFM addendum outcome, a defect on FWD-6,
or a cell of the migration project's own MAP step is the CTO's L2/L4 call; the skill's "round 3 must not
be another hardening round" is noted, and this is a functional gap, not hardening.

**P2. Seed the walk by the subject's token beside its buckets, and print the coverage control.** The mdpf
walk returned 14 real rows against 60 live nodes carrying the token; the compute half of the subject is
invisible to a bucket seed. Until the seed grammar widens, run `comp-find --corpus aws '\b<token>\b' --all`
beside every run and print `rows / token-nodes` as the run's own coverage denominator. Cost: one comp-find.

**P3. If the point is transfer, rehearse the MECHANISM on the real subject non-mutatively rather than the
subject on a simpler estate.** The estate's own record (s.4) is 3 of 3 for same-subject dry-runs and 0 of 3
for stand-ins. A 49F run already exists; the un-rehearsed step is the L5 decomposition FROM a plan and ONE
package executed with `executed: false` honoured -- that step can be dry-run on the 49F plan today with no
COO seated, as a reading exercise. If Andrew's word is MDPF first (his call), scope that run to the classes
it CAN exercise -- FORK, HOME, FORMAT, prefix retire, the Scheduler-heavy trigger plane, consumer repoint,
the dedicated runner -- and write the five 49F-only classes into the run's own record as UNREHEARSED, so
the green cannot be read as covering them.

**P4. Rename or annotate `plan.json`'s `dependencies`.** A field named `dependencies` that holds a step chain
is a Rule 24 (iii) intent-coherence defect on a name; `step_dependencies` (or a `resource_dependencies`
sibling once P1 lands) removes the reading hazard. A schema-record change for LGIC_LGCTFM; proposal only.

**P5. Two records disagree about MDPF's bucket and should be reconciled by whoever owns them:** the tension
map (2026-09-13) says `opal-data-mdpf` "holds bronze + code only"; the live plane today lists `gold/eclipse/`,
`silver/eclipse/`, `silver/netassets_daily.parquet` and `platinum/mdpf/` keys in it and no `bronze/` prefix
at root (five root prefixes: `bmkaud-evidence/ code/ diagnostics/ mdpf/ telemetry/`). Not chased here; the
MAP step of MDPF_CANON's F1 census is where it lands.

---

## 6. WHAT THIS RECORD DOES NOT CLAIM

- The bronze tier's FORMAT inside `opal-data-mdpf/mdpf/` is UNMEASURED; the R9 row in s.3.2 rests on the
  root listing only.
- Whether a Lambda's environment carries a bucket name that the graph's props would surface to a bucket seed
  is UNMEASURED; the 0-LAMBDA finding is what the walk returned, not a claim about why.
- The 49F live-plane spread by token was not re-censused; the brief's own 6-type / 249-hit pull is quoted.
- The precedent read is 6 of 64 HEAD-band files; the 735 non-HEAD hits were not read.
- No grade on any LGIC_LGCTFM outcome is touched; s.2.2's reading of FWD-5's picture is a reading.
- The mdpf run in the scratchpad is an instrument read; it is not a project run, is not committed, appended
  no mark, and its numbers are pinned to its own `VINTAGE.json` (repo_head `685dc7e7`, graph 2026-09-18
  12:17:28 UTC), one repo commit behind this record's HEAD.
- Nothing here recommends whether or when ADVI_FIRMBKTS runs, which subject Andrew should pick, or which
  branch of s.3.3 the CTO should take.
