# LGIC_ENFORCE — DECOMPOSITION (L5)

```json
{
 "project": "LGIC_ENFORCE",
 "directive": "D14",
 "macro": "LGIC",
 "fabric": "laptop",
 "decomp_version": "v1.1",
 "step": 5,
 "prd_ref": "org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md@78128f29ea",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO @daeeb1f437 (review @9879d45fdc)", "brief": "SIGNED 4.0.0_SA_CRO @bb99f5f03f (review @93b7a4664e)"},
 "author": "2.0.0_SA_COO~G",
 "cells": 22,
 "dag_levels": 7,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~G`, the lane that leads the sequence. Authority: Andrew-direct 2026-09-14 ~16:3xZ at the
`1.0.0_SA_CTO` terminal, VERBATIM *"The issue I need from you is to handle the larger scale work of sequence.yaml, which
COO~G is going to be leading ... instruct COO~G to essentially run /canonical-drive on those sequence.yaml sequenced
projects"*. It is recorded at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_163xZ_SEQUENCE_LED_BY_COO_G_ON_CANONICAL_DRIVE_CTO_OVERSEES.md`
@`507864b842` and in the DIRECTED Step 1b-F row in `org/XXX.md`. `1.0.0_SA_CTO` set the L5 order in msg 96640:
LGIC_ENFORCE first. L5 is the COO's; no seat certifies this document before L6.
**Input:** the PRD's SURFACE MANIFEST at v1.1 @`78128f29ea`, ADMITTED on both halves.
**Sequence:** stage 1 of `org/missions/SEQUENCE.yaml`. `sequence-check --project LGIC_ENFORCE` (17:06Z) reads `waits_on MET`
(LGIC_NAMING's PRD admitted) and flags NEEDS-SLOT, which this cut and its row flip answer. This project's cell `EN-f-2` is the
**manual gate on `ADVI_FIRMBKTS`** (hold `max_dep_stage: DECOMP`), so the fence chain is this decomposition's critical path.
**Frozen at the cut.** A cell that looks wrong mid-round is a **surprise row, never an edit**
(`org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`, which the first row mints).

**v1.1 (2026-09-14, before any order was issued).** Only the ten citations of LGIC_NAMING's cells changed: each is written
`LGIC_NAMING cell <x-n>` (its id there is `LN-<x-n>`) instead of in the cell-id form. The L6 coverage limb of
`.tools/to-pipeline-gate.py` reads every cell id in this document as one of this project's own (`_coverage_gap`,
`:414-419` @`a67425668b`), so it refused the issuance for four LGIC_NAMING cells that no LGIC_ENFORCE order owns. No cell,
edge, gate, criterion or count moved: 22 cells, 7 levels. The freeze above binds from the issuance, which had not happened.

**The rulings every cell carries, from the PRD preamble:** the SOURCE-FIRST key string
`{source}/{scope}/{tier}/{table}/{partition}`, with the bucket as container and never a segment; the short forms `49f`, `inf`
and `cot` beside the long forms, with `bd` refused in every slot; remediation shape (a): D14 owns the rule, the registry, the
builders and the flagger, and every fix goes where the resource lives; and THE FENCE's three conditions as ACCEPTANCE (DEC-4).
**DEC-11 binds every cell:** no live rename or move; no runtime interceptor; no alarm, monitor or notification; no tags; no
Terraform labels before the label census. The only applied-plane acts in this project are `EN-f-2`'s bucket policy and three
transient probe roles.

---

## 0. WHAT L5 READ THAT THE PRD LEFT TO IT

The PRD defers four reads to L5 by name. Each was read at this cut, and the result is written into the cells it reaches.

1. **The commit limb's insertion point** (DEC-6: *"The exact insertion point is L5's read"*). `.tools/safe-commit.sh`
   @`60fc168527` runs its gates as stages, in this order:
   - `commit-gate.sh` at `:652`, over `.py`, `.sh`, `.tf` and `org/projects/*.json` only;
   - `to-pipeline-gate.py` at `:686-688`, over task orders;
   - `surprise-row-gate.py` at `:708-731`.

   The flagger grades Python, JavaScript, Terraform, JSON and YAML, and `commit-gate.sh` never sees JavaScript, JSON or YAML.
   So the limb is **a new fail-closed stage in `safe-commit.sh`, placed after the commit-gate stage (`:652`) and before the
   to-pipeline stage (`:686`)**. It calls a new `.tools/naming-gate.py` over the staged graded files. It is not an edit to
   `commit-gate.sh` or `ds-precommit-check.py`. → `EN-g-1`.
2. **`.tools/safe-apply.sh`** (DEC-6: *"not read at L4"*). Read at 291 lines. It gates `apply` only. The halt checkpoint runs
   at `:72`, and a tag-authorization gate that produces a plan runs from `:80` to `:205`. *"Before plan"* therefore means **a
   new stage between `:72` and `:80`**, grading the resource-name attributes of the tree's `.tf` files before any plan runs.
   → `EN-t-2`.
3. **The carrier set (DEC-5), re-measured at HEAD** by definition-pattern search: all 8 definitions stand at the PRD's lines:
   - `infra/aws/lambda-edge/_shared/firm-config.mjs:65`
   - `data/assets/scripts/gold/investor_reporting/directory_runner.py:170`
   - `holdings_snapshot.py:145`, in the same directory
   - `infra/aws/lambda/investor-reporting/_authz/loaders.py:43`
   - `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py:57`
   - `.tools/ds-precommit-check.py:68` and `:110`
   - `data/firm_registry.json`, which exists

   This is a SCOPED read. The unscoped population is `EN-c-1`'s job, by DEC-5's own text.
4. **The fence at HEAD.** `infra/aws/terraform/shared-infra/s3-49financial.tf`:
   - `DenyForeignFirmPrincipals` is now at `:98`, not the PRD's `:93`;
   - its four enumerated patterns sit at `:109-112`;
   - `bd-gold-layer-runner` is named at `:76`.

   The 5-line shift is LGIC_NAMING cell l-1's replacement notice at `:16-20`, merged @`4d8219e3e6`. That is gate G-D of
   LGIC_NAMING's decomposition, now read: its hunk and `EN-f-1`'s policy lines are disjoint.

**Two measurements at this cut change what E5 is, and neither is in the PRD:**

- **Writes to the firm buckets are not observed by the trail.** The org trail logs firm-bucket data events as
  `read_write_type = "ReadOnly"` (`infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf:73`). The only write
  logging is `infra/aws/terraform/globgrph/item2e_served_write_trail.tf`, which is WriteOnly on `platinum/firm/` of three
  served buckets. So DEC-4 (ii)'s *"every principal that read or wrote each firm bucket ... from the CloudTrail data events"*
  can observe READERS but not WRITERS. **`EN-c-2` therefore takes the writer population from GRANTS** (identity policies, the
  bucket policy and the role-side belts), UNIONED with the reads and the served-prefix writes the trail does see. Andrew's
  ruling 6 (write logging on `opal-data-bd`, `-inf` and `-cot`) is routed to `0.0.0_AB_MSTR`'s infra lane and is not live;
  that is gate G-W.
- **Most live firm principals would be DENIED by a scope-derived fence.** LGIC_NAMING's cell f-1 (merged @`d9ccd9babd`,
  `exercises/n4-firm-patterns.md`) measured this: of 240 live IAM roles, 69 carry a firm alias token, and the canonical
  patterns catch only **12 of the 68** attributed live roles. The rest put the firm first, or do not end in `-role`. A fence
  derived from scope slots therefore denies roughly 56 live firm principals unless each is named in `exemptions.json`. That
  is exactly DEC-4 (ii)'s condition, and it sizes `EN-f-1`.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  SURFACE MANIFEST rows at 78128f29ea ................................ 12  (denominator, parsed)
  minus the row marked "excluded" .................................... -1  (live rename/move, runtime interceptor,
                                                                              alarm/monitor, tags, the D12 question)
  minus the row whose kind is "read only" ............................ -1  (the schema, N2/N6, infra/logic/*,
                                                                              CloudTrail events, the live plane)
  ------------------------------------------------------------------
  WRITE / EXECUTE SURFACES FOR THIS ROUND ............................ 10
     S1   infra/logic/registry/*.json                            new data                 EN-r-1 (+ EN-f-1 exemptions rows)
     S2   lib/opal_naming.py, lib/tests/test_opal_naming.py      new code                 EN-r-1, EN-b-1, EN-s-1
     S3   infra/aws/terraform/modules/opal_name/                 new module, no resources EN-m-1
     S4   s3-49financial.tf, the bucket policy only              APPLIED                  EN-f-1 (authored), EN-f-2 (applied)
     S5   three transient probe IAM roles                        APPLIED, transient       EN-f-1 (authored), EN-f-2 (applied, removed)
     S6   the six carrier paths + ds-precommit-check.py's two lists   generated, DELTA=0  EN-v-1..EN-v-6
     S7   the safe-commit path and .tools/safe-apply.sh          gate limbs               EN-g-1, EN-t-2
     S8   org/mcp/naming-gate.enforce and its verdict log        kill switch + audit      EN-g-1
     S9   org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/       records                  EN-c-1, EN-c-2, EN-t-1, EN-s-1, EN-s-2,
                                                                                          EN-f-1, EN-f-2, EN-p-1, EN-d-1, EN-d-2, EN-x-1
     S10  practice copies (linked worktrees, scratch branches, never pushed)   exercises  EN-g-1, EN-p-1, EN-d-1, EN-x-1
```

The project's surprise channel (lane ANY, append-only) is a carrier, not a deliverable surface. Every task order names it in
`<paths>`. So do the change-management ledger entry and its `.open_deploys/` sentinel, for the two fence cells only (the
dispatch skill's sentinel rule).

**Falsifier 1: the domain against every path the PRD cites.** `comp-adversary compose` over the PRD (read-vintage HEAD
@`4d8219e3e6`, 2026-09-14T17:12:55Z; artifact-vintage `78128f29ea`) returned:
- **15 of 15** cited commits verified;
- **19** cited paths, **12 stable and 7 flagged**:
  - **4 GONE, correctly.** `infra/logic/registry/systems.json`, `deliverables/CARRIER_CENSUS.md`,
    `deliverables/NAMING_CENSUS_REPORT.md` and `deliverables/TF_LABEL_CENSUS.md` are all this project's to mint.
  - **3 MOVED:**
    - `s3-49financial.tf`: re-measured in §0.4.
    - `SEQUENCE.yaml`: v2 capacity and v3 IRPT placement; no gate on this project moved.
    - `NAMING_SCHEMA.json`: v1.2 to v1.4, via LGIC_NAMING's v1.3 and v1.4. The move is **load-bearing** and is handled in §2
      row 2.

No flagged path falls outside the manifest.

**Falsifier 2: the carrier domain.** DEC-5's eight definitions stand at HEAD (§0.3). The unscoped re-derivation is
`EN-c-1`'s first act. A carrier it finds outside the eight is a row, and never a silent extension of `EN-v-*`.

**Status vocabulary.** Four values. NOT-EVALUATED is one of them, so non-evaluation cannot be encoded as a verdict:

| value | meaning |
|---|---|
| `MEASURED` | evidence in hand at the cut, instrument named |
| `DECLARED` | the PRD or a record asserts it; not independently measured here |
| `NOT-EVALUATED` | not looked at. Not a pass, not a fail. |
| `N/A` | the field does not apply to this surface |

---

## 2. THE RECTANGLE

| # | surface | current state | target state | collision set | evidence at cut | cells |
|---|---|---|---|---|---|---|
| 1 | S1 `infra/logic/registry/*.json` | `MEASURED` absent (comp-adversary GONE) | five JSON files per DEC-1, seeded from `infra/logic/05_IDENTITY_SPINE.md`; a validator refusing the planted bad rows | **two writers, serialised:** `EN-r-1` mints all five; `EN-f-1` appends `exemptions.json` rows (edge r-1 → f-1). Practice-copy plants (`EN-p-1`, `EN-d-1`) never merge | `MEASURED` | EN-r-1, EN-f-1 |
| 2 | S2 `lib/opal_naming.py` + tests | `MEASURED` absent | `key()`, `address()`, `name()`, `grade()` (DEC-2), `generate` (DEC-5), `census` (DEC-7); stdlib only | **three writers of one file, serialised by edges** r-1 (`generate`) → b-1 (builders, `grade`) → s-1 (`census`). ⚠ The schema they execute is **v1.4 at HEAD** (entity partition, code tier, legacy served paths, `LEGACY_SERVED_PATHS.json` as data). The PRD cites v1.2 as "the schema this project executes", but CONTRACTS row 1 says the builders *"read it at run time and never copy it"*, so v1.4 is what they execute. `grade()` must agree with LGIC_NAMING cell g-1's written rule | `MEASURED` (absent); `DECLARED` (behaviour) | EN-r-1, EN-b-1, EN-s-1 |
| 3 | S3 `modules/opal_name/` | `MEASURED` absent | a generated locals file (DEC-3) and a `format()` name output; no `external` data source; vectors match `name()` | none; sole writer | `MEASURED` | EN-m-1 |
| 4 | S4 `s3-49financial.tf` policy `:98-112` | `MEASURED` enumerated Deny on 4 patterns; LGIC_NAMING cell l-1's notice at `:16-20` (disjoint) | the scope-derived Deny with a generated exemption list, applied, and proved by real probes | **three writers of one file:** `0.7.0_AE_CloudOps` (landed `:17-19`, `:24-38`), LGIC_NAMING cell l-1 (landed `:16-20`), EN-f-1 (`:98-112`). Disjoint line ranges. Only EN-f-2 applies | `MEASURED` | EN-f-1, EN-f-2 |
| 5 | S5 three probe roles | `MEASURED` absent. **13** IAM roles match `mdpf` in the live plane (`comp-find --corpus aws 'mdpf' IAM_ROLE`: 13 hits across 240 nodes, vintage 2026-09-14 12:13:53 UTC, manifest `b578e47d733f`). The **10** `mdpf`-named ones carry no firm token; **3** roles owned by the MDPF pipeline DO carry one (`wp5-49f-feeder-scheduler-role`, `wsb-49f-model-aua-daily-role`, `wsd-49f-partner-held-etf-daily-role`) | `mdpf-49f-fenceprobe-role`, `mdpf-cot-fenceprobe-role`, `mdpf-fenceprobe-role`, named by the module, each able to read only the probed bucket; created, probed, removed | none | `MEASURED` | EN-f-1, EN-f-2 |
| 6 | S6 the carriers | `MEASURED` 8 definitions at HEAD (§0.3) | each a generated file headed GENERATED with its registry hash; exports byte-equivalent (DELTA=0) | one writer each; none shares a file with another cell. `.tools/ds-precommit-check.py`'s two lists (EN-v-6) and the commit limb (EN-g-1, in `safe-commit.sh`) do not share a file, per §0.1 | `MEASURED` | EN-v-1..EN-v-6 |
| 7 | S7 `safe-commit.sh`, `safe-apply.sh` | `MEASURED` stages at `:652`, `:686`, `:708`; `safe-apply.sh` `:72`, `:80` | a naming stage in each at the §0 insertion points | none inside the project. ⚠ **`safe-commit.sh` is on EVERY seat's commit path**, so the limb's WARN mode must never change its exit code (§8 choice 5) | `MEASURED` | EN-g-1, EN-t-2 |
| 8 | S8 kill switch + log | `MEASURED` absent | `org/mcp/naming-gate.enforce` (present = enforce), verdict log | none | `MEASURED` | EN-g-1 |
| 9 | S9 deliverables | `MEASURED` only `prd/` and `project.json` in the project tree | one record per cell, named in §3 | none: no file has two writers | `MEASURED` | 11 cells |
| 10 | S10 practice copies | N/A | one scratch branch per exercise cell, its commits cited by hash in that cell's record; the branch stays and the worktree is removed | none | N/A | EN-g-1, EN-p-1, EN-d-1, EN-x-1 |

**Worker admission is `NOT-EVALUATED` and is load-bearing.** Rows 1 to 8 sit in lanes that refuse a worker by lane. A
worker is admitted only by the `<paths>` block of its non-terminal order at HEAD. That is exercised at L6, on HEAD bytes, after
the issuance commit (G-C, carried from LGIC_NAMING's practice).

---

## 3. THE CELLS — 22

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, prefix `EN`. Axes:
- `c` the censuses
- `r` the registry
- `b` the builders
- `m` the module
- `f` the fence
- `v` the generated views
- `g` the commit gate
- `t` the Terraform-label census and the apply limb
- `s` census mode
- `p`, `d`, `x` the practice-copy and real-resource exercises

Every deliverable path is under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/` unless it is a code or infra path.
Each acceptance line below is **one criterion**. `J` marks a judgment criterion, graded by `3.0.0_SA_CVO` at L9, never at L7.

| cell | what it is | PRD cand. | serves | writes | acceptance, one clause per line |
|---|---|---|---|---|---|
| `EN-c-1` | the carrier census | E1 (half) | FWD-3 | `CARRIER_CENSUS.md` | an unscoped read over the repo of every firm long form, short form and legacy bucket name, with the denominator printed · every hit is listed as a carrier (with file:line) or excluded with a reason · the 8 DEC-5 definitions are present in the list · a carrier outside the 8 is listed AND filed as a row · `J`: every exclusion's reason holds |
| `EN-c-2` | the fence-writer census | E1 (half) | FWD-2 (DEC-4 ii) | `FENCE_WRITER_CENSUS.md` | for each of the four firm buckets, every principal GRANTED read or write (identity policies, the bucket policy, the role-side belts), with its grant line · every principal SEEN reading (the ReadOnly trail) or writing `platinum/firm/` (the item2e trail) in the stated window, with its evidence line · each principal's firm scope token, or `none` · the census states it cannot observe writes outside `platinum/firm/` (§0) · denominators printed per bucket and per source |
| `EN-r-1` | the registry rows, the validator, the generator | E2 | FWD-3, FWD-7 | `infra/logic/registry/{systems,scopes,tiers,exemptions,remediations}.json`; `lib/opal_naming.py` (`generate`, `validate`) | every file parses · the validator refuses a planted systems row missing `owner_directive` · the validator refuses a planted systems row whose key is a firm · every scope row carries long, short, tenancy and bucket · `bd` appears only as an alias or a refused token · `generate` reproduces each carrier in CARRIER_CENSUS.md byte-for-byte in its exported content (DELTA=0), into a scratch location, never over the carrier |
| `EN-b-1` | the builders | E3 | FWD-1, FWD-2, FWD-4, FWD-5 | `lib/opal_naming.py` (`key`, `address`, `name`, `grade`); `lib/tests/test_opal_naming.py` | `key("orion","inflection","bronze","positions","date=2026-09-13")` returns exactly `orion/inflection/bronze/positions/date=2026-09-13` · `address()` over the same arguments returns it under the bucket the tier home rule and tenancy give · neither `key` nor `address` has a bucket parameter · `name("mdpf","cottonwood","publisher","role")` returns `mdpf-cot-publisher-role` · IV.3's four controls return their stated verdicts, with `{source}` named as unfilled on `opal-data-inf/silver/x` · a test a `\b`-style regex would fail passes · `grade()` agrees with every worked case in LGIC_NAMING's `GRADING_RULE.md` (§3a.2), disagreements printed with the rule line |
| `EN-m-1` | the Terraform module | E4 | FWD-2 | `infra/aws/terraform/modules/opal_name/` | the module contains no `external` data source · every vector in the file the Python builder generates matches the module's output (`terraform console` or a plan output, no apply) · the locals file carries the GENERATED header with the registry hash |
| `EN-f-1` | the fence, authored | E5 (half) | FWD-2; the sequence gate | `s3-49financial.tf` (`:98-112` region, and the three probe-role resources); `infra/logic/registry/exemptions.json` (rows); `FENCE_PLAN.md`; the ledger entry + sentinel | every principal in FENCE_WRITER_CENSUS.md either matches its firm's derived pattern or has an `exemptions.json` row with reason and sign-off reference · the policy's pattern and exemption lists are produced by the generator, not typed (the diff's list lines equal the generator's output) · a `terraform plan` on the tree shows ONLY the policy change and the three probe roles · the ledger entry is opened and holds the prior policy verbatim, every principal whose access changes, and the rollback |
| `EN-f-2` | the fence, applied and proved | E5 (half) | FWD-2; the sequence gate | the ledger entry + sentinel (closed); `FENCE_PROBES.md` | the entry carries both never-widen sign-off halves (`1.0.0_SA_CTO`, `2.0.0_SA_COO~G`) before the apply (gate G-E) · `safe-apply` applies exactly the planned change · `mdpf-49f-fenceprobe-role` reads `opal-data-49financial` · `mdpf-cot-fenceprobe-role` is denied · `mdpf-fenceprobe-role` (unscoped, non-exempt) is denied · a principal `exemptions.json` names is allowed · the three probe roles are removed and the entry is closed |
| `EN-v-1` | view: `data/firm_registry.json` | E6 | FWD-3 | `data/firm_registry.json` | the file carries the GENERATED header with the registry hash · its exported content is byte-equivalent to the pre-image (DELTA=0) · its consumers' existing tests pass |
| `EN-v-2` | view: `firm-config.mjs` `FIRM_CONFIG` | E6 | FWD-3 | `infra/aws/lambda-edge/_shared/firm-config.mjs` | as EN-v-1, for this file |
| `EN-v-3` | view: the two IRPT `firm_bucket_map()` | E6 | FWD-3 | `data/assets/scripts/gold/investor_reporting/{directory_runner,holdings_snapshot}.py` | as EN-v-1, for these two definitions · both files pass `.tools/commit-gate.sh` |
| `EN-v-4` | view: IR authz `bucket_for` | E6 | FWD-3 | `infra/aws/lambda/investor-reporting/_authz/loaders.py` | as EN-v-1, for this definition · the file passes `.tools/commit-gate.sh` |
| `EN-v-5` | view: `resolve_firm` | E6 | FWD-3 | `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py` | as EN-v-1, for this definition · the file passes `.tools/commit-gate.sh` |
| `EN-v-6` | view: the precommit's two cross-firm lists | E6 | FWD-3 | `.tools/ds-precommit-check.py` (`:68`, `:110` only) | as EN-v-1, for these two lists · the precommit's own self-test (or its existing tests) passes |
| `EN-g-1` | the commit limb, the kill switch, the WARN window | E7 | FWD-4, FWD-7 | `.tools/naming-gate.py`; `.tools/safe-commit.sh` (one new stage, §0.1); `org/mcp/naming-gate.enforce` (absent: the shipped state); the verdict log path | on a practice copy with the enforce file present: a commit adding `opal-data-inf/silver/...` is refused, the canonical printed · the canonical form passes · an existing permitted alias passes with the canonical printed beside it · a NEW hand-kept firm mapping (a long form as a dict key in Python or JSON) is refused, the registry lookup printed · the same value read through the lookup passes · a NEW resource-name literal the builder would not produce is refused, the canonical printed · `name()` producing it passes · a long form passed as `key(scope=...)` passes · a hand edit to a generated view is refused · with the enforce file ABSENT, the same refused commit exits 0 with the WARN line printed · with the enforce file absent, an internal error in the limb prints `NAMING ERROR` and exits 0 · every verdict is logged |
| `EN-t-1` | the Terraform-label census | E8 (half) | FWD-4 | `TF_LABEL_CENSUS.md` | every resource-name attribute and every resource label in `infra/aws/terraform/**/*.tf` is listed with its grade, denominator printed · labels and name attributes are reported apart |
| `EN-t-2` | the safe-apply limb | E8 (half) | FWD-4 | `.tools/safe-apply.sh` (one new stage, §0.2) | on a practice copy: an `apply` over a tree adding a resource whose name the module would not produce is refused before any plan runs, the canonical printed · the same tree with the module-produced name passes the stage · the existing halt and tag-authz stages still run, in order |
| `EN-s-1` | census mode, the run | E9 (half) | FWD-5 | `lib/opal_naming.py` (`census`); `NAMING_CENSUS_REPORT.md` | the run covers the repo (Terraform, `lib/config.py`-class files, Lambda sources) and the live plane (`comp-find --corpus aws`, vintage printed) · every nameable live name is judged, denominator printed · each row is (current, canonical, verdict, type, plane) · a RAISE stops the run with the string printed |
| `EN-s-2` | census mode, the comparison | E9 (half) | FWD-5 | `NAMING_CENSUS_COMPARISON.md` | the report's totals are set beside LGIC_NAMING's worked cases (N2), its two-grader sample (N6, LGIC_NAMING cell h-3) and the census's IV.7 ranking, each with its denominator · every disagreement names the name and the two verdicts · `J`: the totals agree with the hand ranking, or every difference is explained |
| `EN-p-1` | FWD-6 on a practice copy | E10 | FWD-6 | `EXERCISE_FWD6.md` | on a practice copy, a planted `remediations.json` row owns one surface holding an OUT-OF-PATTERN name (§3a.4) · a change touching that surface without removing the name is refused · the change removing it passes · the scratch branch's commits are cited by hash |
| `EN-d-1` | FWD-7 and FWD-1 on a practice copy | E11 (half) | FWD-7, FWD-1 | `EXERCISE_FWD7.md`; the expected-diff file | the expected diff set is committed BEFORE the generator runs (two commits, in that order, cited) · one fictitious firm row (§3a.3) is added, and the generator's actual diff equals the expected set · a hand-typed address for that firm is refused · a hand-typed occurrence of the firm's long or short form in an ordinary config carrier is refused · a new pipeline for the firm is written holding no storage-location literal |
| `EN-d-2` | the second worker's search | E11 (half) | FWD-1 | `EXERCISE_FWD1_SEARCH.md` | a search of EN-d-1's new pipeline for every storage-location literal (bucket names, `s3://`, key prefixes), denominator printed, returns zero · the search's own positive control (a planted literal on a scratch copy) returns one |
| `EN-x-1` | FWD-2 on a real resource | E12 | FWD-2 | `EXERCISE_FWD2.md` | a real resource named by the module lands in a plan on the real Terraform tree (§3a.5) · its firm's fence pattern comes from the same registry row · on a practice copy, one change to that firm's short form moves the resource's name and the fence pattern together (both diffs non-empty and consistent) |

**Coverage of the PRD's candidates: 12 of 12.**
- E1 → EN-c-1, EN-c-2
- E2 → EN-r-1
- E3 → EN-b-1
- E4 → EN-m-1
- E5 → EN-f-1, EN-f-2
- E6 → EN-v-1..6
- E7 → EN-g-1
- E8 → EN-t-1, EN-t-2
- E9 → EN-s-1, EN-s-2
- E10 → EN-p-1
- E11 → EN-d-1, EN-d-2
- E12 → EN-x-1

**Coverage of the outcomes: 7 of 7.**
- FWD-1: EN-b-1, EN-d-1, EN-d-2
- FWD-2: EN-b-1, EN-m-1, EN-c-2, EN-f-1, EN-f-2, EN-x-1
- FWD-3: EN-c-1, EN-r-1, EN-v-1..6
- FWD-4: EN-b-1, EN-g-1, EN-t-1, EN-t-2
- FWD-5: EN-b-1, EN-s-1, EN-s-2
- FWD-6: EN-p-1
- FWD-7: EN-r-1, EN-g-1, EN-d-1

### Why the re-cuts

- **E1 → two cells.** A repo text census and a principal census over grants and trail events are two instruments, and they
  feed two different chains (the registry and the fence).
- **E5 → two cells around a gate.** The apply needs the never-widen sign-off of two seats in between, and a seat act cannot
  sit inside a worker's cell. EN-f-1 produces the plan and the sign-off packet; EN-f-2 applies, probes and closes.
- **E6 → six cells.** Six independent files in five lanes, each with its own consumers' tests. They share only the generator,
  which is EN-r-1's.
- **E8 → two cells.** The PRD itself orders the census before the limb.
- **E9 → two cells.** The comparison half waits on another project's order (G-B); the run does not.
- **E11 → two cells.** FWD-1's *"by a second worker's search"* requires a different worker.
- **E2, E3, E4, E7, E10 and E12 stay whole.**

### 3a. THE FIXED INPUTS L6 CUTS INTO THE FACES

Decided here, so no worker chooses its own test.

1. **EN-c-2's window and sources.**
   - Window: from the moment read logging went live on the four firm buckets (validated @`231cd62ec5`) to the L6 cut, stated
     in UTC in the face.
   - Sources: the org trail's ReadOnly data events; `item2e`'s WriteOnly events on `platinum/firm/`; the identity policies
     granting `s3:*` on each bucket (through `comp-iam role <name>` over the Terraform-declared roles and the live census); the
     bucket policy's named principals; and the role-side belts.
   - The face states in plain words that writes outside `platinum/firm/` are not observed (§0).
2. **EN-b-1's agreement set.** Every worked case in
   `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` @`ce7349b7cc` (**43 cases**), with
   `LEGACY_SERVED_PATHS.json` @`ce7349b7cc` (**39 templates**). A disagreement is graded against N2 (CONTRACTS row 2): it is
   a row naming the case and the rule line, never a silent fix to either side.
3. **EN-d-1's fictitious firm (DEC-9).** It is never `demo` and never pushed: long form `quillwater`, short form `qwt`. L6
   confirms before cutting that neither string occurs as a whole segment in the repo or the live plane (one `comp-find`
   read each, denominator printed). If either occurs, L6 picks the next unused pair and records why.
4. **EN-p-1's planted surface, by rule, because L6 precedes EN-c-1's run.** The first file in byte order in
   `CARRIER_CENSUS.md`'s carrier list that `grade()` marks OUT-OF-PATTERN is the surface the planted row owns. The worker
   applies the rule and states the file.
5. **EN-x-1's real resource.** A resource whose name `opal_name` produces for `49financial`, planned on
   `infra/aws/terraform/shared-infra/` and not applied. The face names no bucket, because the fence's target is the same row.
   ADVI_FIRMBKTS's new buckets (DEC-10's first candidates) are not used: that project is HELD at DECOMP behind this project's
   fence.
6. **The applied cells' tool pins.** EN-f-1 (plan) and EN-f-2 (apply) export `OPAL_AGENT_SERIAL` at spawn, per the two
   identity gates `safe-apply` carries. They set `SAFE_APPLY_TERRAFORM` to the MAIN workspace's `.tools/terraform.exe`,
   because a fresh worktree carries no copy of that gitignored binary and the PATH fallback repins remote state. L6 measures
   that the binary exists before cutting.

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP.** D14 is placed LAPTOP (Andrew-direct 2026-09-12 ~17:2xZ, the tree row's
`fabric_ruling`). The two applied acts (EN-f-2's apply and probe-role lifecycle) run through `.tools/safe-apply.sh` on this
device, which owns the work (Rule 26). **No cell is owned by a seat.** Every cell is served by a worker at L7
(`0.9.0_WK_LGIC_ENFORCE~<n>`). The PRD's *"applied by the infrastructure lane"* is read as the lane grant the order's
`<paths>` carries (RULING 1). If `1.0.0_SA_CTO` reads it as a seat, that is a spec question and a row, not an edit here.

---

## 5. DEPENDENCY EDGES, LEVELS, AND THE DISTINCT-WORKER CONSTRAINT

Edges are keyed to **observed completion**: `A -> B` means B's acceptance cannot be evaluated until A's artifact is at HEAD.

```
  EN-c-1 --> EN-r-1 --+--> EN-b-1 --+--> EN-m-1 --+--> EN-f-1 ==[G-E sign-off]==> EN-f-2 --> EN-x-1
                      |             |             |       ^                                   ^
  EN-c-2 -------------|-------------|-------------|-------+                                   |
                      |             |             +--> EN-t-2 <-- EN-t-1                      |
                      |             |             +-------------------------------------------+
                      |             +--> EN-g-1 --+--> EN-p-1
                      |             |             +--> EN-d-1 --> EN-d-2
                      |             +--> EN-s-1 --> EN-s-2 <== [G-B: LGIC_NAMING cell h-3 merged]
                      +--> EN-v-1 .. EN-v-6 --> EN-d-1
                      +--> EN-f-1, EN-g-1, EN-p-1, EN-d-1   (the registry rows; drawn once)
```

**The levels (longest path from a root):**

| level | cells | width |
|---|---|---|
| 0 | EN-c-1, EN-c-2, EN-t-1 | 3 |
| 1 | EN-r-1 | 1 |
| 2 | EN-b-1, EN-v-1, EN-v-2, EN-v-3, EN-v-4, EN-v-5, EN-v-6 | 7 |
| 3 | EN-m-1, EN-g-1, EN-s-1 | 3 |
| 4 | EN-f-1, EN-t-2, EN-p-1, EN-d-1, EN-s-2 (also waits on G-B) | 5 |
| 5 | EN-f-2 (waits on G-E), EN-d-2 | 2 |
| 6 | EN-x-1 | 1 |

**The critical path is the fence:** EN-c-1 → EN-r-1 → EN-b-1 → EN-m-1 → EN-f-1 → [G-E] → EN-f-2. EN-f-2's close is the
evidence `1.0.0_SA_CTO` confirms the ADVI_FIRMBKTS manual gate on (msg 96640: *"Pitch the ADVI_FIRMBKTS fence confirmation
to 1.0.0_SA_CTO with the .tf evidence when LGIC_ENFORCE lands it"*).

**The chain count.** Every cell is one connected component with EN-r-1, except that EN-t-1 joins only through EN-t-2. So
"M = connected components" would read 1 and serialise 22 cells, which the spine's own words do not ask for: *"a maximal
path through them is a chain, and two cells on one chain never run at once."* Cells at the same level lie on different
maximal paths, so the fan-out is the level width, capped.

**The distinct-worker constraint** (only one pair binds):

| cell | must not share a worker with | why |
|---|---|---|
| EN-d-2 | EN-d-1 | *"by a second worker's search"* (E11, FWD-1) |

As in LGIC_NAMING, a cold start is a fresh context, so a slot's continuation may serve EN-d-2 only if it is a new spawn.

**The fan-out this decomposition supports: up to 8 concurrent workers, the level-2 width of 7 plus one.** `1.0.0_SA_CTO`'s
rec (96626) is one fan-out across the whole sequence at the default cap of 8. LGIC_NAMING round 1 holds one live worker at
this cut, so L6 states N against the live count at issuance. A slotting that satisfies every constraint (L6's to choose and
defend):

| slot | cells, in order | spawned |
|---|---|---|
| 1 | EN-c-1, EN-r-1, EN-b-1, EN-m-1, EN-f-1, EN-f-2, EN-x-1 (the critical path) | at issuance; each next one after its inputs drain; EN-f-2 after G-E |
| 2 | EN-c-2, then EN-g-1, then EN-p-1 | at issuance |
| 3 | EN-t-1, then EN-t-2 | at issuance |
| 4 | EN-v-1, EN-v-2 | after EN-r-1 |
| 5 | EN-v-3, EN-v-4 | after EN-r-1 |
| 6 | EN-v-5, EN-v-6 | after EN-r-1 |
| 7 | EN-s-1, then EN-s-2 | after EN-b-1; EN-s-2 after G-B |
| 8 | EN-d-1; then EN-d-2 in a NEW spawn | after EN-g-1 and EN-v-1..6 |

**Disk.** A worker worktree costs about 1.4G, and so does each practice copy (EN-g-1, EN-p-1, EN-d-1, EN-x-1). This lane's
10G stop line binds at every spawn (C: read 36G free at this cut). Each face instructs:
- commit the exercise on its scratch branch, so the evidence survives;
- then `git worktree remove` the clean practice copy;
- the scratch BRANCH stays, because deleting an unmerged branch is destructive git.

---

## 6. BATTERY DISPOSITION

### `comp-adversary`: RUN

`comp-adversary compose org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md` (read-vintage HEAD @`4d8219e3e6`,
2026-09-14T17:12:55Z, artifact-vintage `78128f29ea`):

| source | denominator | result |
|---|---|---|
| cited-commit verification | 15 attempted | **15 verified, 0 unverifiable** |
| cited-path vintage | 19 attempted | 12 stable, 3 MOVED-SINCE-AUTHORING, 4 GONE |

All seven flags are resolved in §1. **Blindness, stated because the tool states it:** `T11: decomposition neighborhood NOT
RESOLVED (artifact carries no <decomp_ref>)`. The uncited-neighbourhood complement is therefore filesystem adjacency, not the
dependency chain. Re-running against a task order at L7 resolves T11; this cut does not rely on it.

### `comp-schedule`: RUN, and APPLICABLE

`comp-schedule --budget 540` scanned **5 of 5 carriers** within budget (351.5 s used). Reached denominators: C1 230, C2 6,
C3 12, C4 21, C5 334. **25 gates armed.** C4 (scope guards) and C5 (project blocking) are PARTIAL_OR_BLIND by their own
decidability. **0 lines of the report name LGIC_ENFORCE, `s3-49financial.tf`, `opal-data-49financial`, ADVI_FIRMBKTS or any
other sequenced project.**

**The promises-to-check-later this project creates, registered here:**

| gate | owner | the condition that clears it |
|---|---|---|
| **G-B** (carried from LGIC_NAMING) | this project's COO lane | LGIC_NAMING cell h-3 merged. **Its first half is DISCHARGED:** LGIC_NAMING cell g-1's rule and list merged @`ce7349b7cc`, which EN-b-1 reads. Only EN-s-2 waits on the second half. |
| **G-C** worker admission | `2.0.0_SA_COO~G` | after the issuance commit, `owned-paths-validate --check-agent` on HEAD bytes PERMITs each slot on a path its order names and REFUSES it on one it does not |
| **G-E** never-widen sign-off | `1.0.0_SA_CTO` and `2.0.0_SA_COO~G` (NEVER #1) | both halves written on EN-f-1's ledger entry, naming the act's blast radius (every principal whose access changes, the rollback per key), with both branches covered. Only then is EN-f-2 spawned |
| **G-F** the live REFUSE flip | this project's COO lane, announced to live seats | 7 days AND at least 200 graded strings in WARN mode (DEC-6), the false-refusal count printed with its denominator. **Outside this round's acceptance:** FWD-4 is exercised on a practice copy, so no FWD waits on the window |
| **G-S** the sequence's manual gate on ADVI_FIRMBKTS | `1.0.0_SA_CTO` confirms it on SEQUENCE.yaml | EN-f-2 closes with its probes passed; this lane pitches it with the `.tf` evidence (96640) |
| **G-W** write-event logging (ruling 6) | `0.0.0_AB_MSTR`'s infra lane | write data events live on the firm buckets. **Not a gate on this round:** EN-c-2 takes writers from grants (§0). Recorded because a writer census by grant is weaker than one by observation, and says so |

### `comp-iam`: RUN, and APPLICABLE (unlike LGIC_NAMING's)

`comp-iam stats` (this cut) reads: **209** IAM roles parsed, **189** services (168 Lambda, 21 EC2), **1,091** operations,
**310** permission gaps. APPLICABLE, because EN-f-2 applies a policy change and three roles, and EN-c-2's writer census is a
grant census.

**Blindness, stated.** `comp-iam` cross-references code operations against Terraform IDENTITY policies. It does not evaluate
a bucket (resource) policy, and neither does `simulate-principal-policy` (DEC-4: *"never by simulate-principal-policy"*). So
the fence's effect is outside its plane. EN-f-2 proves the fence by REAL probes; EN-c-2 uses `comp-iam role <name>` per
principal for the grant half of its census.

### Beyond the core

`comp-find --corpus aws` is an instrument inside cells (EN-c-2, EN-s-1, §3a.3), and at this cut it measured §2 row 5. No lens
of the admitted catalogue is claimed beyond the three above.

---

## 7. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is §1's subtraction: 12 manifest rows, each placed exactly once (1 excluded,
1 read-only, 10 surfaces), with two falsifiers run before use. **Exhaustive:** 12 of 12 candidates and 7 of 7 outcomes are
covered (§3). **Mutually exclusive on files:** yes, except the two serialised multi-writer files in §2 rows 1 and 2, each
ordered by an edge. Deliberately NOT mutually exclusive on outcomes: FWD-2 is served by six cells.

**(ii) SAME GRAIN.** Every cell is one act by one worker producing one record or one code surface, graded by a match or by a
CVO judgment. The re-cuts in §3 restore that grain where a candidate bundled two instruments, a seat act or a second worker.

**(iii) INTENT COHERENCE.** One axis: **make the schema mechanical at authoring time**: one registry, the builders, the
generated lists, and the gates that refuse what the builder would not produce. No cell renames a live name, and no cell
repoints a consumer (ADVI_FIRMBKTS FWD-3's). The applied-plane acts are the fence and its probes, and nothing else.

**(iv) STATE COHERENCE, and what each remedy does NOT move:**
- EN-r-1 moves the registry. It does **not** move any carrier; the carriers move in EN-v-*, byte-equivalent.
- EN-v-* move carrier FILES to generated form. They do **not** move served behaviour (DELTA=0), and they do **not** deploy:
  a deploy rides each owner's path (Rule 13).
- EN-f-1 moves the policy TEXT and the exemption rows. It does **not** move AWS; only EN-f-2 applies.
- EN-f-2 moves `opal-data-49financial`'s policy. It does **not** move `opal-data-bd`, `-inf` or `-cot`, whose policies are not
  in this tree, and it does **not** move ADVI_FIRMBKTS's hold; the CTO confirms that on SEQUENCE.yaml.
- EN-g-1 ships the limb in WARN mode. It does **not** refuse any live commit until G-F.
- EN-s-1 moves the census report. It does **not** mint a remediation (ruling (a): D8 and D12 mint where the resource lives).

---

## 8. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

Each is this seat's call at L5, stated so it can be argued with, and revertible at the round-N analysis.

1. **The commit limb is a new `safe-commit.sh` stage calling a new `.tools/naming-gate.py`**, not an edit to `commit-gate.sh`
   or `ds-precommit-check.py` (§0.1: those two do not see JavaScript, JSON or YAML).
2. **The safe-apply limb sits between the halt checkpoint and the tag-authz plan** (§0.2).
3. **EN-c-2 takes writers from grants**, unioned with what the trail observes, because the trail does not log writes
   (§0; G-W).
4. **E1, E5, E6, E8, E9 and E11 are re-cut** (§3). E6's six-way split buys width at level 2.
5. **The WARN mode never changes `safe-commit.sh`'s exit code, including on the limb's own internal error**, which prints
   `NAMING ERROR` and passes. ENFORCE mode fails closed. The reason: the limb sits on every seat's commit path, and a
   fail-closed bug in a WARN-only window would halt the fabric while protecting nothing. EN-g-1's last two criteria prove it.
6. **The generated views are written by EN-v-*, not by EN-r-1.** EN-r-1 proves `generate` reproduces each carrier into a
   scratch location. Each carrier file then has exactly one writer.
7. **EN-s-2 writes a separate comparison record**, so NAMING_CENSUS_REPORT.md has one writer.
8. **EN-x-1 does not use ADVI_FIRMBKTS's buckets** (DEC-10's first candidates), because that project is held behind this
   one's fence (§3a.5).
9. **The fictitious firm is fixed here** (§3a.3), with a collision check at L6.
10. **The builders execute NAMING_SCHEMA.json v1.4**, the schema at HEAD, per CONTRACTS row 1's *"read it at run time"*,
    although the PRD's preamble names v1.2 (§2 row 2).

---

## 9. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **The carrier set is re-measured only by definition pattern** (§0.3). The unscoped population is EN-c-1's.
2. **No principal census was run at L5.** The ~56 figure in §0 is LGIC_NAMING cell f-1's measurement over IAM roles carrying a firm token,
   not a census of opal-data-49financial's actual readers and writers. That is EN-c-2's.
3. **Worker admission is not exercised** (G-C). It cannot be until an order is at HEAD.
4. **The WARN window is not part of this round** (G-F). FWD-4's DONE WHEN is exercised on a practice copy.
5. **`comp-iam` cannot see the fence** (§6). A green `comp-iam` says nothing about DEC-4's three conditions.
6. **The chain reading and the levels are this document's readings of its own declared edges.** They are written out so they
   can be argued with.
7. **No cell has been exercised.** Every target state is a specification. No effort or duration estimate appears here,
   deliberately.
