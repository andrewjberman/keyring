# PRD REVIEW -- LGIC_NAMING v1.0 @c65a169ba0 -- the BRIEF half (L4-R, spine v3.15) -- 4.0.0_SA_CRO~D

**archetype:** VALIDATE
**Reviewer:** `4.0.0_SA_CRO~D` (the brief's author; the brief half is the CRO's by Rule 27).
**Read:** `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md` v1.0 @`c65a169ba0` in full (240 lines) and
`org/standards/NAMING_SCHEMA.json` v1.0 (100 lines), against `docs/briefs/d14-naming-schema-brief-20260913.md` @`1b42dbe758`
and `infra/logic/09_NAMING_CENSUS.md` @`bf21181208`. UTC 2026-09-13 ~22:4xZ.
**Half reviewed:** everything except ENDPOINT + CONTRACTS (the CVO's half): SCHEMA S1-S13, PROJECT ARC, CELL CANDIDATES
N1-N7, PATHS, BRIEF COVERAGE, SURFACE MANIFEST.

## VERDICT: REFUSE -- one exact defect in the data the PRD lands at L4, two lines to fix; everything else SIGNS as read

The refusal is narrow and names its bump. It is NOT about the brief's consumption (22 of 22 entries mapped, no outcome
narrowed, no bar moved, the three L4 decisions each stated with their authority) and NOT about the per-slot split (its
label is now correct: L4-ratified, revertible on Andrew's word).

### R1 (the refusal) -- `NAMING_SCHEMA.json` `kind.by_type` keys do not match the type vocabulary the graders will use
`grade(name, type)` (S11) takes a `type`. N2's worked cases and N6's hand-grading draw their names "across every
resource type" from `comp-find --corpus aws`, whose node types are the CloudNode DB's -- the census (`09_NAMING_CENSUS.md`
§2, measured from the same DB) uses them verbatim: `CODEBUILD_PROJECT` (5), `ECS_TASK_DEFINITION` (9), `STATE_MACHINE` (1),
`API_GW`, `CW_ALARM`, `SSM_DOCUMENT`, ... The data file's `by_type` carries **`CODEBUILD`** and **`ECS_TASK`** -- neither is
a node type the instrument returns. A hand-grader handed `ECS_TASK_DEFINITION` finds no row and must either guess
(`task`) or RAISE -- and S11 says an unplaceable input RAISES as a defect in the rule, so with the file as landed, nine
task definitions and five CodeBuild projects raise by construction at N2/N6.
**THE BUMP (v1.1, touches only this):** rename the two keys to the DB's strings -- `CODEBUILD_PROJECT`, `ECS_TASK_DEFINITION`
-- and add one line stating that `by_type` keys ARE CloudNode `node_type` values (so the vocabulary has one owner). S7's
sentence "ECS task definitions -> task, state machines -> sfn" already says the right thing in prose; the data disagreed
with it.

### R2 (carried with the bump, same file) -- the types that are NOT graded by kind are implicit
The census's 33 node types minus `by_type`'s 16 leaves 17 unnamed. Some are covered elsewhere in the file (`EVENT_RULE`,
`SCHEDULE` -> cadence last; `LOG_GROUP` -> derived; `S3_BUCKET` -> bucket grammar; `SECRET` -> secret grammar; `IAM_USER`,
`S3_BUCKET_POLICY` -> follow their resource), some are excluded by `not_covered` (KMS ids, distribution ids, service
principals, API routes), and some are neither listed nor excluded (`EVENT_SOURCE`, `ROUTE53_RECORD`, `VPC_ENDPOINT`,
`LOAD_BALANCER`, `ECS_CLUSTER`, `S3Key`). A grader handed one of those has no rule and no exclusion. **Add a
`types_not_graded_by_kind` block enumerating them by subtraction from the census's 33** (Rule 24 (i): the domain is the
DB's type list; the subtraction is printed, not recalled). Two lines of data; no prose change.

### Signed as read (no correction) -- stated so the bump does not widen
- S1-S6, S8-S13: each matches the brief's IV.2/IV.6 or a ruling, with the authority named. S4's inclusion of secret
  paths in the SHORT form matches the census's measured shape (`blackdiamond/49f/credentials`, §2).
- S7's three L4 decisions (add `task`, `sfn`; drop `secret`; `-trigger/-publisher/-scanner` are functions) are correct by
  subtraction from the census and I would have made them.
- N1-N7: the arc proves the schema by hand before the machine exists (LGIC_ENFORCE's) -- right, and it avoids the "bar
  only another project can meet" pattern for FWD-1/2/3/5/6. **N5 is the one cell that depends on another project's
  act** (MDPF_CANON's L4 edits its own §3): FWD-4 cannot grade REALIZED until that PRD lands -- carried as a NOTE, not a
  refusal; the PRD says so itself in PATHS and the manifest.
- BRIEF COVERAGE 22/22: entries 20 and 22 NOT CONSUMED with correct reasons.
- SURFACE MANIFEST: nothing deployed, no rename, no registry row, no IAM -- consistent with S13 and ruling (a).

## WHAT THIS REVIEW DOES NOT DO
No edit to the PRD or the data file (the CTO's surfaces). No comment on ENDPOINT/CONTRACTS (the CVO's half). No claim
that the 22-entry coverage was re-diffed against the brief byte-by-byte: it was read entry by entry against the brief's
headings and found complete.
