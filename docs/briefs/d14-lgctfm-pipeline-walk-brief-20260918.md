# D14 -- LGIC_LGCTFM, THE PIPELINE WALK: THE RUN ENDS ONLY WHEN EVERY INVOLVED RESOURCE HAS A ROW, EVERY HOP HAS AN EDGE, AND EVERY FINAL ARTIFACT HAS A VIEWER VERDICT -- MIDSTREAM BRIEF

**Author:** `4.0.0_SA_CRO` . **UTC:** 2026-09-18 ~19:3xZ
**Mode:** MIDSTREAM. `LGIC_LGCTFM` (D14, `org/missions/D14/LGIC/LGIC_LGCTFM/`) is active: rounds 1-2 CLOSED, REALIZED
8 of 10 at the last analysis; the engine `lib/opal_lgctfm.py`, the contract schema and six runs exist. This brief is
authored blind to the open task-order set, per `/brief-create --midstream`; it adds outcomes, it retires none.
**Directive / macro:** D14 "Platform Logic", macro `LGIC`, project `LGIC_LGCTFM`.
**Commissioned by:** Andrew-direct 2026-09-18 at the `4.0.0_SA_CRO` terminal, two words, VERBATIM AND ENTIRE:

> ~18:2xZ: *"If we are missing lambdas/ec2/eventbridge rules or schedules/ddb/etc, any involved aws resources, then
> the workflow process is not done."* / *"that means that the workflow must be designed to create rows for these
> items"* (record @28a8ae74e3)

> ~18:3xZ: *"We want to work in all the comp-tools to this process so we adequately enumerate the true resources
> involved in a given production pipeline. CTO is currently looking through the comp-tools list i gave them to
> validate that they are in working order. Something I think that you can do in the interim is perhaps there should
> be a "change-management" comp-find scan, maybe a session-logs comp-scan too. I want to make sure that the process
> is athletic, and we don't miss some crucial resource and declare it real. As a result, I think the final step of
> the current resource/state manifest should include a walk of the pipeline, covering each resource/script/etc from
> start to finish to assess what exactly consumes the final artifacts (and if those artifacts are visible or
> invisible to a viewer on the portal). Is a process like this already established in the /legacy-transform
> operation? If not, I want you to give it a shot based on what youve already found via your MDPF_CANON
> /legacy-transform run, and identify as you do it what the efficient/generalizable rulesset is for
> walking/compiling this for the records so you can write a brief on the subject and that brief can be integrated
> into the LGIC_LGCTFM project."* (record @c9e54d5c0f)

**Standing law this brief executes, not re-argues:** the two words above; `1.0.0_SA_CTO` R-81 @4443e7308e (the
design requirement this brief lands into: RCN-0009's P2 promoted to FWD-1's acceptance arm per node_type against the
live plane; P3 the round's shape; P4 the `dependencies` rename owed; P1 adopted with the lambda-source-map leg
RE-POINTED to `comp-iam live / reconcile / simulate` and `comp-find --corpus aws`; hand surfaces carry the
`comp-lambdamap` guard or a dated declaration; SERVED_FROM lands on the wrong node class and is repaired BEFORE the
walk uses it; STORED_IN resolves 0 of 955; ROUTES_TO is sound; "a relation reading zero is a question, never an
answer"); the canon `infra/logic/02_DOCTRINE.md` R1-R21; CLAUDE.md Rule 22 (grain, coverage, state, discrimination;
a shared dependency beneath the members is checked on its own), Rule 24 (a taxonomy is MECE by subtraction over the
claim's population), Rule 30 (a builder refusal is a missing registry row); the standing moratorium on monitors
(nothing here is a monitor); `1.0.0_SA_CTO`'s comp-tool validation pass, which this brief consumes and does not
duplicate.
**Worked example this brief is extracted from:**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/LGCTFM_PIPELINE_WALK_MDPF_START_TO_FINISH_20260918.md` (RCN-0010, the
model-portfolio pipeline walked start to finish with the comp-tools that exist). Its predecessor is RCN-0009
@edcbe51fb4 (the engine's rows carry NAME and POSITION and never DEPENDENCY).
**Consumer:** STEP 2, `1.0.0_SA_CTO` `/endpoint --forward`; the integration carrier (an addendum outcome set, a round,
or cells of the migration projects' MAP step) is the CTO's at L2/L4 and this brief does not pre-decide it.

[!] **This brief authorizes no move, no rename, no retirement, no monitor and no gate.** It specifies what a RUN of
the instrument must contain before it may be called done, and the ruleset by which the run is compiled. Every act
the run's output names stays a separate R19 project under never-widen sign-off.

---

# PART 0 -- WHERE THE PROJECT STANDS, AND WHY THIS BRIEF EXISTS MIDSTREAM

- **What exists.** `lib/opal_lgctfm.py` (`walk`, `forks`, `plan`, `run`), `org/standards/LGCTFM_CONTRACT.schema.json`,
  the schema record `infra/logic/11_`, the method note `infra/logic/10_`, six runs under
  `workflows/legacy_transform/` (five over `49financial`, one instrument read over `mdpf` in a scratchpad). FWD-1..
  FWD-10 with 8 REALIZED at the last L10.
- **What was measured and not designed for.** The walk is BUCKET-SEEDED and returns 0 compute rows on both subjects
  (49F: LAMBDA 0 / EC2 0 of 184 rows; mdpf: 14 real rows against 60 live nodes carrying the token -- 0 of 6 LAMBDA,
  0 of 1 EC2, 0 of 13 roles, 0 of 11 policies). It writes `"edges": []`; the only edge writer is forks' `REPLACES`.
  `plan.json`'s field named `dependencies` is the R19 step chain inside one row (895 of 895 same-row, 0 cross-row).
  No consumer hop, no route, no component, no viewer verdict exists in any run. (RCN-0009 s.2.)
- **Andrew's word turns that measurement into a DONE condition:** a run that omits an involved resource is not a
  done workflow, and the remedy is DESIGN -- rows -- not a caveat.
- **What the walk found in one afternoon on the smaller subject** (RCN-0010): 6 Lambdas, 1 EC2 runner, 13 roles, 11
  policies, 7 triggers with targets, 3 alarms, 6 log groups, a layer, an SSM parameter and a secret path outside the
  33-type vocabulary, ~17 packaged scripts, ~30 storage locations, 3 routes, 1 component, and ONE CROSS-SYSTEM
  TRIGGER (`mdpf-feeder-accelerator` fires on `opal-data-inf`'s completion sentinel -- a bucket `ADVI_FIRMBKTS`
  retires) that neither subject's run can see. Every class Andrew named was missing, and the one that binds the two
  migrations together was missing twice.

---

# PART I -- THE OUTCOME TERRITORY

Each is one thing a named kind of person can DO that they cannot do today. Qualitative; every number a run prints is
measured at run time with its denominator.

### O1 -- A reader of a run sees every involved AWS resource of the subject as a row, and reads the run's own coverage per resource type against the live plane before reading anything else

Compute (Lambda, EC2, ECS, state machines), triggers (BOTH APIs), identity (roles, policies, profiles, secrets),
storage (buckets, policies, keys, planes, DynamoDB), observability (alarms, log groups), parameters -- each a row;
and at the top of the contract a table `rows / live-nodes` PER NODE TYPE for the subject's token, so a reader sees
"LAMBDA 6 of 6" or "LAMBDA 0 of 6" before any tension. A type the vocabulary does not grade is COUNTED and carried
(R-36), never dropped. **Bar:** the per-type coverage table is printed and every live node carrying the subject's
token is either a row or a named, classified non-row (O3). *(R-81: FWD-1's acceptance arm, promoted from RCN-0009
P2.)*

### O2 -- A migration engineer reads the dependency between any two rows as a typed edge with the instrument that measured it, and the plan's package order respects it

`TRIGGERS`, `INVOKES`, `STARTS`, `READS`, `WRITES`, `AUTHORIZES`, `SERVES`, `CALLS` -- the schema's own edge
vocabulary, populated: trigger -> target from Terraform target blocks (desired) and the live schedule/rule target
(applied); compute -> storage from grants (`comp-iam live / simulate`, applied) and from the writer census
(`comp-legacywriter`, source); route -> key -> component from `comp-routes` / `comp-platinum` (desired). Packages
that PORT or REPOINT a row are ordered after the packages of the rows it depends on, beneath the tension rank; a
cycle is printed, never broken silently. **Bar:** for the worked subject, the seven trigger -> target edges, the
two feeder -> feeds edges, the gold -> `portal/gold/mdpf/` edge, the publisher -> `platinum/mdpf/` edge and the
three route -> component edges are present with instruments, and the plan orders the publisher's REPOINT after the
gold Lambda's. *(R-81: P1 adopted in direction; the source-map leg re-pointed as that ruling states.)*

### O3 -- A reader sees every resource name the estate's own records carry for the subject, and each one that is not on the live plane classified as exactly one of five things, with MISSED the only one that fails the run

The change-management scan (`org/critical_paths/change_management/`) and the session-log scan (`org/**/logs/`)
run as a NAME census: files scanned, files with a hit, distinct names, printed. Every name absent from the live
plane is RETIRED (a record names the retirement), NEVER-BUILT, SCRIPT-NOT-RESOURCE, ALIAS, or MISSED. **Bar:**
on the worked subject, `mdpf-daily-trigger` reads RETIRED with the 2026-08-07 record as its evidence, the six
Lambdas read MISSED against the engine's run and PRESENT against the walk, and the run's own verdict on itself
is "0 MISSED" or it is not done. *(Andrew's two named scans, and the sentence "we don't miss some crucial
resource and declare it real".)*

### O4 -- A reader sees, for every FINAL artifact the subject produces, what consumes it and whether a viewer on the portal can see it, as one verdict from a closed set

The walk runs in the direction of data -- trigger, compute, script, artifact, consumer, route, component, viewer --
and ends at a per-artifact verdict: VISIBLE, CONSUMED-BY-FIELD-ROUTE-UNRESOLVED, ROUTED-FIELD-USE-UNMEASURED,
NO-ROUTE, NO-ENDPOINT, OPERATIONAL, INTERMEDIATE. The desired-plane instruments are `comp-routes trace`,
`comp-platinum reverse`, `comp-transform fields`; the applied-plane instrument is a `head_object` on the key and a
GET through the page's own request path; the graph's SERVED_FROM is not used until it lands on `S3_BUCKET`
(R-81). **Bar:** on the worked subject the four platinum keys carry four different verdicts today
(account-distribution VISIBLE; category-views consumed-by-field with the route unresolved; aum-metrics routed with
field use unmeasured; aggregate-aua-timeseries NO-ROUTE), and the run states which plane each verdict was read on.
*(Andrew: "what exactly consumes the final artifacts (and if those artifacts are visible or invisible to a viewer
on the portal)".)*

### O5 -- Where two instruments disagree about one row, a reader sees both and the row's population is their union

`comp-pipescript io` saw 0 writes on `mdpf_gold_consolidator`; `comp-legacywriter` saw nine write sites in the same
family. A run carries BOTH cells with their blind spots; it never elects one tool's zero. **Bar:** a row whose
instruments disagree renders both, and a criterion that grades "no writes" on one instrument's silence is refused
at the cut.

### O6 -- A reader of ONE subject's run sees the rows that belong to ANOTHER subject's migration, named as cross-system, so neither migration can retire what the other still fires on

A trigger whose pattern names another subject's bucket, a script that waits on another subject's sentinel, a role
that reads another subject's silver -- each is a row tagged with the other subject's registry key. **Bar:**
`mdpf-feeder-accelerator` (pattern on `opal-data-inf`) and the dispatch script's wait on the same sentinel appear
in the MDPF run tagged `inflection`, and the 49F/INF run carries them back as consumers of the bucket it retires.

### O7 -- A reader sees which of the run's facts came from a HAND-KEPT surface, with that surface's measured drift beside it

`lambda-source-map.json` (19 of ~216 names out of step with the live plane, R-81), `EC2_MANIFEST.json` (the MDPF
runner is absent from it), `route_bindings.yaml`, the ontology snapshot (last review 2026-07-30) -- any fact read
from one carries the `comp-lambdamap` guard result or a dated declaration (date, owner, un-defer condition).
**Bar:** no `source_dir`, `iam_role` or instance fact is presented as MEASURED when its only source is a hand
surface.

### O8 -- Any seat compiles the walk for any subject by the same printed ruleset, and a second seat's compile over the same subject at the same vintage produces the same rows, edges and verdicts

The ruleset is Part V; the engine's determinism test extends to the walk. **Bar:** two compiles by different
slots at one vintage diff to zero on the tension identity key AND on the edge set.

---

# PART II -- WHERE THE BOUNDARY SITS

**Inside:** the run's contract, edges, record-scan census, viewer verdicts, coverage table and plan ordering;
the ruleset for compiling them; the comp-tools each hop names; the two new scans.

**Outside, and whose:** validating that each comp-tool is in working order (`1.0.0_SA_CTO`, in progress); repairing
SERVED_FROM's node class and STORED_IN's grain (`NFRA_CLDGRPH`'s plane, R-81 names it as preceding the walk); any
move, rename, repoint, retirement or monitor (R19 projects; the moratorium); the migration projects' own MAP cells,
which CONSUME a run; the portal's sources as rows (a gitlink; consumer evidence only, unchanged from the first
brief); read-logging on `opal-data-assets` / `opal-data-portal-v2` (billed, Andrew's word; without it the
OBSERVED-reader axis of O4 stays out of coverage and the run says so).

---

# PART III -- THE QUALITATIVE BAR

- O1: coverage per node type is a printed table, never a sentence; a zero for a type is followed by the
  instrument and the positive control (R-81: a zero relation is a question).
- O2: an edge is `{from, to, type, instrument, plane, blind_spot}`; an edge with no instrument is not an edge.
- O3: the five classes are a closed enum; a run with any MISSED is NOT DONE and prints the names.
- O4: a verdict names its plane; a desired-plane VISIBLE is not an applied-plane VISIBLE and the run says which.
- O5: disagreement is a row state, not a choice.
- O6: a cross-system row is tagged with the OTHER registry key and appears in both subjects' runs.
- O7: a hand-surface fact is never MEASURED.
- O8: reproduction by a different slot, never the author.

---

# PART IV -- THE SUBSTRATE: FINDINGS, EACH WITH WHAT WAS MEASURED

### IV.1 -- The comp-tools already cover every hop of the walk; no run composes them

Measured on the model-portfolio subject 2026-09-18 (RCN-0010 s.1): triggers `comp-trigger --list --json` (167);
identity `comp-iam service|role`; script I/O `comp-pipescript io --pipeline mdpf`; writer census
`comp-legacywriter --json` (9,015 files, 586 locations); graph neighbourhood `comp-blast --direction both --json`
(28,123 nodes); storage `comp-keys prefix|partitions` (live s3api); serving `comp-routes trace|rewrites|endpoints`,
`comp-platinum reverse`, `comp-transform fields`; business chains `comp-estate --resource`; record scans
`comp-find` over `org/critical_paths/change_management/` and the log trees. 104 of 104 comp-tools resolve on this
box (A.3). The engine calls two of them (`comp-find --corpus aws`, `comp-trigger --list`).

### IV.2 -- `comp-trigger --list` carries no target; the trigger -> target hop is read from Terraform today

Its JSON keys are `arn, kind, name, pattern, schedule, state`. The seven MDPF targets were recovered from
`target {}` blocks in eight `.tf` files (desired plane). The applied-plane read (`get-schedule`, `list-targets-by-rule`)
is one call per trigger and was not run here. A run must carry both planes or say which it read.

### IV.3 -- The cross-system trigger is the resource that binds two migrations, and both runs miss it

`mdpf-feeder-accelerator`'s pattern: `Object Created` on bucket `opal-data-inf`, key `gold/meta/pipeline-complete.json`
(`feeder-trigger.tf:259-285`; live, ENABLED). The runner's dispatch script waits on the same key
(`mdpf-daily-dispatch.sh:283-301`). The MDPF engine run carried the rule as a GRAMMAR tension on its name; the 49F
run does not carry it. `ADVI_FIRMBKTS` retires `opal-data-inf`. This is O6's founding instance.

### IV.4 -- Two static instruments disagree on one script's writes, and each is right about its own blindness

`comp-pipescript io mdpf_gold_consolidator --pipeline mdpf`: READS 0 detected, 2 UNRESOLVED-PREFIX, WRITES 0
detected, and it says "manual review required". `comp-legacywriter`: write sites at
`mdpf_gold_consolidator.py:1460,1463,1691` and eight more in the family. O5.

### IV.5 -- Hand surfaces are wrong in both directions today and one of them omits the subject's only server

`lambda-source-map.json`: 216 entries against 217 live functions with 19 names disagreeing (R-81's measurement,
including a rename never followed). `EC2_MANIFEST.json`: one service (`consolidation-gold-runner`); the MDPF runner
`i-02448edb624a7a7cf`, live and declared, is absent. `ec2.tf`'s own comment names a retired starter
(`mdpf-daily-trigger`); the live starters are `mdpf-feeder-trigger` and `mdpf-accrual-trigger` (both hold
`ec2:StartInstances` + `ssm:SendCommand`, `comp-iam service`). O7.

### IV.6 -- The record scans turn absences into verdicts; the live plane alone cannot

change-management: 128 of 831 records, 112 distinct names. Session logs: 884 of 6,068 files, 299 distinct names.
Live plane: 60 nodes. `mdpf-daily-trigger` is in 15 records and 103 logs, in 0 live LAMBDA nodes, and the
2026-08-07 cutover bundle names its retirement -- RETIRED, not MISSED. `mdpf-freshness-checker` has a source dir,
no source-map entry, no live node, 24 log mentions -- UNMEASURED-WHICH, and a monitor of the class the moratorium
covers. `comp-blast` already reads the change-management directory for HOLD claims (74 on `mdpf-gold-lambda`); a
name census over the same directory is the second read it supports. O3.

### IV.7 -- The viewer verdict is four different answers on four sibling keys written in the same second

`platinum/mdpf/49financial/{account-distribution,category-views,aum-metrics,aggregate-aua-timeseries}.json`, all
LastModified 2026-09-18T13:50:49Z: VISIBLE (route + component + field), consumed-by-field with the route
unresolved (client-composed URL), routed with field use unmeasured (`comp-transform fields ModelPortfolios` lists
2 fields, neither from `getAUMMetricsByFirm`), NO-ROUTE (139,839 bytes written daily, no endpoint). Plus
`platinum/mdpf/global/*` with no endpoint (IN_REPO stitch) and `_manifests` operational. `comp-platinum reverse`
prints PRODUCER (empty) for a served key -- the serving tool cannot name the writer; the writer is known from the
publisher's source and grant. O4.

### IV.8 -- Two resource kinds on this subject fall outside the 33-type vocabulary the contract grades

SSM parameter `/mdpf/custody_source` (`lambdas.tf:25`; the vocabulary has `SSM_DOCUMENT`, not `SSM_PARAMETER`) and
the secret path `smartx/credentials/*` (a `SECRET` slash-path, graded as placement only). R-36 carries them in
`PLANT_UNTYPEABLE` and counts them; O1 requires the count to be a row-class of its own in the coverage table.

### IV.9 -- Bronze on this subject is JSON, so the canon's irreversible class is absent here; the tension map's line about the bucket is stale

`opal-data-mdpf/mdpf/bronze/orion_model_composition/{date}/model_*.json`, 89 partitions 2026-05-18 to 2026-09-18.
`08_TENSION_MAP.md` item 2 says the bucket "holds bronze + code only"; the live root has five prefixes and the
graph lists gold/silver/platinum keys in it. Lands in MDPF_CANON F1's MAP (RCN-0009 P5), not here.

### IV.10 -- The graph's consumer edges are usable in one direction and misaimed in the other, as R-81 measured

ROUTES_TO (route -> lambda) is sound; SERVED_FROM's 27 edges land on `S3_BUCKET_POLICY`; STORED_IN resolves 0 of
955 (ARN-grain targets against NAME-grain bucket identity). `comp-blast` on the gold Lambda reports a DynamoDB
table and a second Lambda at depth 2-3 through the CloudFront principal chain -- the graph's claim, not a grant
either role holds. The walk uses ROUTES_TO and the route tools for the consumer hop and treats depth >= 2 graph
consumers as claims until a grant or call site confirms them.

### IV.11 -- The prior answer stands beneath all of this: NAME and POSITION are carried, DEPENDENCY is not

RCN-0009 @edcbe51fb4 s.2: six `current.*` cells on 184 of 184 and 15 of 15 rows; `plan.json` `dependencies` 895 of
895 same-row; `"edges": []` at `lib/opal_lgctfm.py:885`. R-81 adopted that finding as the spine of its requirement.

---

# PART V -- WHAT MUST BE TRUE: THE WALK RULESET (named, NOT sequenced -- sequencing is step 5)

W1 **Seed by the subject's TOKEN and by its buckets; print `rows / live-nodes` per node type as the run's first
table.** (R-81, FWD-1's arm.) COST: one `comp-find --corpus aws`. NON-APPLICATION: none.

W2 **Walk in the direction of data, and name the hop's instrument, plane and blind spot on every edge:** TRIGGER
-> COMPUTE -> SCRIPT -> ARTIFACT -> CONSUMER -> ROUTE -> COMPONENT -> VIEWER. An edge is
`{from, to, type, instrument, plane, blind_spot}`. COST: one column. NON-APPLICATION: none.

W3 **Union, never election:** where two instruments disagree on a row, both cells stay and the population is
their union. COST: none. NON-APPLICATION: instruments whose domains do not overlap.

W4 **Trigger -> target is read from Terraform (desired) AND the live target (applied), both printed;** the list
census has no target field and a trigger with no target found is UNMEASURED, never "none". COST: one
`get-schedule` / `list-targets-by-rule` per trigger. NON-APPLICATION: a run that declares itself desired-plane only.

W5 **A cross-system row is tagged with the OTHER registry key and is emitted into both subjects' runs:** a
pattern, a sentinel wait, a grant or a read that names another subject's bucket. COST: one tag. NON-APPLICATION:
a subject with no such edge -- and the run prints that it looked.

W6 **Identity from the graph, grants from the live evaluator, the map for `source_dir` only and declared:**
function identity from `comp-find --corpus aws` with `drift_class`; grants from `comp-iam live / reconcile /
simulate`; `lambda-source-map.json`, `EC2_MANIFEST.json` and any hand surface carry the `comp-lambdamap` guard result
or a dated declaration (date, owner, un-defer condition). (R-81.) COST: one `comp-lambdamap check` per run.
NON-APPLICATION: a field with no hand-surface source.

W7 **Run the two record scans as a NAME census and classify every off-plane name into exactly one of RETIRED /
NEVER-BUILT / SCRIPT-NOT-RESOURCE / ALIAS / MISSED, printing files scanned, files hit and distinct names;** MISSED
is the only class that fails the run. COST: two scans, ~5 s each on this box. NON-APPLICATION: none -- a subject
with no records is itself a finding.

W8 **End at a VIEWER VERDICT per final artifact from the closed set** VISIBLE / CONSUMED-BY-FIELD-ROUTE-UNRESOLVED
/ ROUTED-FIELD-USE-UNMEASURED / NO-ROUTE / NO-ENDPOINT / OPERATIONAL / INTERMEDIATE, each naming its plane; desired
from `comp-routes trace` + `comp-platinum reverse` + `comp-transform fields`, applied from `head_object` + a GET
through the page's own route; SERVED_FROM unused until it lands on `S3_BUCKET`. COST: three tool calls per final
artifact + one GET. NON-APPLICATION: a subject with no served artifact, which the run states.

W9 **A relation reading zero prints its instrument and a positive control** (R-81; TRIGGERS read 0 estate-wide
until 2026-09-04). COST: one control per zero. NON-APPLICATION: a relation the run did not measure, which is
UNMEASURED, not zero.

W10 **A resource outside the 33-type vocabulary is a counted row-class, never dropped** (R-36; SSM parameters,
secret paths). COST: none. NON-APPLICATION: none.

W11 **Scripts enter through the compute row's package manifest and the runner's sync source, and a script the
manifest names that the repo lacks, or vice versa, is a drift row.** COST: one manifest read per compute row.
NON-APPLICATION: compute with no packaged code (a bare AWS-managed function).

W12 **Every count carries its denominator and vintage, and the run's own manifest lists per-hop instrument, plane,
denominator, blind spot;** a report to a decision-maker states "6 of 6", never "all". COST: none. NON-APPLICATION:
none.

W13 **The plan orders PORT and REPOINT packages after the packages of the rows they depend on, beneath the tension
rank, and prints any cycle;** `plan.json`'s step chain is renamed `step_dependencies` (R-81, P4 owed). COST: one
topological pass. NON-APPLICATION: a run with no edges, which under W1-W9 is not done.

---

# PART VI -- STATUS . [!] NOT OUTCOME-BEARING . measured 2026-09-18, clocks per line

- `LGIC_LGCTFM`: active; rounds 1-2 CLOSED; REALIZED 8 of 10; R-81 @4443e7308e is the standing requirement.
- The engine at HEAD af794c77e3 / 685dc7e7 (the mdpf run's vintage): bucket-seeded, `edges: []`, one tension class.
- RCN-0009 @edcbe51fb4; RCN-0010 (the walk) and this brief: LOCAL at commit time, push state in the delivery message.
- `1.0.0_SA_CTO`'s comp-tool validation: in progress on Andrew's list; this brief names tools by what they printed
  today and does not certify them.
- Neither `MDPF_CANON` nor `ADVI_FIRMBKTS` has a COO lane seated (both dep_stage PRD, coo_lane null).

---

# PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- Which carrier lands it (addendum outcomes, a round, migration MAP cells): the CTO's at L2/L4.
- That the comp-tools are in working order beyond what each printed on this subject today; the CTO's pass decides.
- Applied-plane viewer verdicts: none were exercised; every verdict in IV.7 is desired-plane.
- The OBSERVED-reader axis (who actually read `opal-data-assets` / `opal-data-portal-v2`): out of instrument coverage
  until read logging reaches those buckets, which is billed and Andrew's.
- That the record-scan classes are the final enum: they are Rule 24's first cut over the measured population
  (112 + 299 names); the four-postulate record for the enum is owed at L4 with its token census.
- Any effort estimate; Part III's bars are qualitative by Andrew's rule.

## REFS TO CARRY

- Andrew-direct records: @28a8ae74e3 (`..._182xZ_LGCTFM_WORKFLOW_NOT_DONE_...md`), @c9e54d5c0f
  (`..._183xZ_LGCTFM_ALL_COMP_TOOLS_PIPELINE_WALK_...md`), both under `org/tier1_exec/4.0.0_SA_CRO/deliverables/`.
- R-81 @4443e7308e, `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260917.md` (msg 98046).
- RCN-0009 @edcbe51fb4; RCN-0010 (the walk record named above); `RECON_REGISTER.md`.
- Engine and law: `lib/opal_lgctfm.py`; `org/standards/LGCTFM_CONTRACT.schema.json`; `infra/logic/10_`, `11_`, `08_`;
  `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` v1.4; `docs/briefs/d14-legacy-transform-brief-20260916.md`.
- Graph route law: `org/modules/graph/graph-call-manifest.yaml` (Rule 20; the repository is the denominator, the
  manifest one input).
- The worked subject's own records: `org/missions/D8/MDPF/MDPF_CANON/`, `infra/aws/terraform/mdpf-pipeline/`,
  `infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf`, `infra/aws/ec2/mdpf-daily-runner/`,
  `infra/aws/lambda/mdpf-pipeline/`, `org/critical_paths/change_management/20260807_mdpf_canplat_cutover_bundle_AE_Z.md`.
