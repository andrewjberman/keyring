# LGIC_ENFORCE — DECOMPOSITION (L5)

```json
{
 "project": "LGIC_ENFORCE",
 "directive": "D14",
 "macro": "LGIC",
 "fabric": "laptop",
 "decomp_version": "v3.11",
 "step": 5,
 "prd_ref": "org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md@09bde3126c",
 "prd_half_hashes": {"ratified-text": "SIGNED 3.0.0_SA_CVO @daeeb1f437, current at v1.2 (the half is unchanged)", "brief": "SIGNED 4.0.0_SA_CRO @e848967b3f, re-signed at v1.2"},
 "author": "2.0.0_SA_COO~G",
 "cells": 28,
 "dag_levels": 7,
 "round": 2,
 "round_2_orders": 12,
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

**v2, the round-2 recut** (2026-09-15), on `1.0.0_SA_CTO`'s round-1 analysis (L10, msg 97145 @`7b5331c8c0`). Section 0b is
the cut: 11 orders, 6 re-run cells and 5 new ones (`EN-r-2`, `EN-r-3`, `EN-r-4`, `EN-r-5`, `EN-t-3`), so the document now
holds 27 cells. Round 1's text below stands as its record.

**v2.1, before any round-2 order was issued** (2026-09-15), on PRD v1.2 @`09bde3126c` (ADMITTED on both halves:
`4.0.0_SA_CRO` re-signed the brief half @`e848967b3f`) and `1.0.0_SA_CTO`'s rulings 97177 and 97200.
- One cell is added, `EN-r-4`: the resource-to-system rows in `infra/logic/registry/resources.json` (PRD candidate E13).
  Its first population is LGIC_NAMING round 2's 48 `{system}` gaps. The ruling names it `EN-r-4`, so the per-view-hash
  cell v2 had cut under that id is renumbered `EN-r-6`, unchanged in content. v2 was never issued, and no other
  document cites that id: LGIC_NAMING's decomposition cites only `EN-r-2` and `EN-r-3`.
- `EN-r-3`'s one-carrier clause becomes a census (97200): every reader of `firm_forms` in `lib/opal_naming.py`, and
  every other tracked file an unscoped search finds, with the denominator printed. Row S19 (`scopes.json`'s
  `_about.row_fields`) is that cell's too.
- G-V19a is met: `NAMING_SCHEMA.json` v1.9 is on `lgic-v19-landing` @`bf506e53be`, ADMITTED there.
- 12 orders; 28 cells.

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

## 0b. v2 -- THE ROUND-2 RECUT (L10: 1.0.0_SA_CTO's round-1 analysis)

**Input.**
- The analysis: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @`7b5331c8c0`
  (msg 97145), on `3.0.0_SA_CVO`'s slug 97135 (`ADJUDICATION_v1` @`43ad6e9b2b`, `REMEDIATION_v1` @`7748cc5df7`). Its s.3
  says what round 2 must reach and leaves the split and the order to the COO.
- PRD v1.2 @`09bde3126c`, ADMITTED (`prd-signoff.py status LGIC_ENFORCE`: both halves SIGNED, current; the brief half
  re-signed by `4.0.0_SA_CRO` @`e848967b3f`). Read as the diff from v1.1 @`78128f29ea`, v1.2 is an L10 addendum on the
  brief half only: DEC-1 defines `resources.json`, candidate E13 populates it, and the ENDPOINT and CONTRACTS are
  unchanged. RULING ONE's schema text is `NAMING_SCHEMA.json` v1.9, the data file CONTRACTS row 1 reads at run time,
  which `1.0.0_SA_CTO` writes (s.2).
- `1.0.0_SA_CTO` 97177: cell `EN-r-4` populates `resources.json` and writes its readers in `lib/opal_naming.py` (`_slots`,
  `validate`), ordered so it never overlaps another writer of that file; LGIC_NAMING cell f-1's re-grade waits on it.
  97200: `EN-r-3`'s repoint is a census of every `firm_forms` reader, and row S19 is `EN-r-3`'s.
- All 22 round-1 orders are terminal: 19 complete, and `EN-s-1`, `EN-v-1` and `EN-x-1` pending with VALID proofs (96806).
  The load-bearing order held: the slug, then the analysis, then this cut.
- The same seat cuts LGIC_NAMING's round 4 in the same window (its analysis msg 97137; PRD v1.8 ADMITTED @`b136cdc308`).
  The two rounds share `lib/opal_naming.py` and one landing, gate G-V19 below.

**What round 2 cuts: 11 orders, by subtraction.**

```
  cells at v1.1 ........................................................ 22
  minus cells whose outcome graded REALIZED and that no ruling re-opens  -16
      EN-c-1, EN-c-2, EN-r-1, EN-b-1, EN-m-1   their files move only through the new cells below
      EN-f-1, EN-f-2                           the fence is APPLIED; G-F's live flip is not this round
      EN-v-1 .. EN-v-6                         FWD-3 REALIZED on its ACCEPT's denominator; regeneration is EN-r-6's
      EN-p-1                                   FWD-6 REALIZED
      EN-d-2                                   FWD-1 REALIZED (its control fix lands in the checker, below)
      EN-t-1                                   the label census is an input, not re-run
  = cells re-run ........................................................ 6
      EN-g-1   the commit limb: RULING ADD (authored files only), W2-S9 (validate first), C-S11 (the map as data)
      EN-t-2   the apply limb reads the plan: RULINGS ADD and PLAN
      EN-s-1   the census, run again on the rows EN-r-2 and EN-r-4 land
      EN-s-2   the comparison, on the real population
      EN-x-1   FWD-2 again, on one carrier, with disjoint filters (W1-S21)
      EN-d-1   FWD-7 again: a new firm draws no warning
  plus new cells ........................................................ 6
      EN-r-5   the gateway registration, whole: the issuer's prepared change, which lanes refused to the issuer
      EN-r-3   RULING ONE: one carrier; DEC-1's field set; RULING DEMO; the tftest generated
      EN-r-2   RULING ROWS: the RAISE population classified, the class (a) rows added
      EN-r-4   the resource-to-system rows (PRD v1.2 E13; 97177): resources.json, its validate limb, grade() reading it
      EN-r-6   per-view hashes (W1-S14), every view regenerated, each consumer suite by RULING RED
      EN-t-3   the Terraform roots read with the switch on (the G-F prerequisite)
  = round-2 orders ..................................................... 12
```

**Not cells (s.4):** C-S9 (`1.0.0_SA_CTO`'s `.tools` fix, landed @`7da8112496`), C-S10 (`0.0.0_AB_MSTR`'s fabric-wide merge
census) and C-S13 (six fabric-tool defects, `1.0.0_SA_CTO`'s). The write trail (W2-S3) stays carried. **G-F's live REFUSE
flip is not this round:** `EN-t-3` measures its prerequisite and nothing flips the switch.

**The instrument fixes (s.3 item 4) are the issuer's own checker defects,** so they land in the round-2 checker
`fixed_inputs/r2/check_en_r2.py`, never in a cell:
- `d2r-control` plants its own literal in a scratch copy and searches with its own regex (W8-S3). No round-2 order re-runs
  `EN-d-2`, so no criterion calls it; it is the instrument the next re-run calls.
- every refusal criterion requires the canonical form `grade()` computes, never any `->` (t2-refuse);
- the DELTA=0 compare keeps export ORDER, and `bucket_for` is probed on both of its branches, a mapped tenant and an
  unmapped one (round 1 set no mapping, so every probe raised);
- `EN-x-1`'s name filter reads only the plan JSON and its fence filter only the generated locals (W1-S21).
The commit limb validating the registry first (W2-S9) and the per-view hashes (W1-S14) are code, so they are cells.

**The population `EN-r-2` classifies, measured at this cut** (fixed input `fixed_inputs/r2/RAISE_POPULATION.json`):
- Every nameable name of both census planes graded by `grade()` WITHOUT stopping, at registry@`ba5318901b937130`, live
  vintage *"2026-09-15 12:21:03 UTC"* (manifest `bb5071398a3d`). Each RAISE is grouped by the token its message quotes;
  0 messages quote none.
- **Live:** 1,805 nameable, 504 raise, **115 groups**. That is the analysis's 115: row W7-S1's diagnostic counted the same way.
- **Repo:** 1,870 nameable, 624 raise, 134 groups, **37 of them in no live group** (among them K1 key segments such as
  `config` and `json`, and names such as `f49` and `x`).
- **Union: 152 groups.** The steps behind them, both planes: R1.c 401, R1.f 400, K1 166, R2 99, B2 48, R8 5, L2 4, R1.d 4,
  G2.3 1 (1,128 = 504 + 624). A group is the unit of classification, and not every one is a system token.
- **The domain is the union, not the live 115** (Rule 24(i)): the census the analysis wants run *"to its end"* judges both
  planes, so an unclassified repo-only group stops it exactly as a live one does. Stated for `1.0.0_SA_CTO`; revertible at
  the round-2 analysis.
- `gateway` is in no group at this registry. `EN-r-5` registers it anyway, and that re-grades 14 live `opal-gateway-*` names
  (IAM_POLICY 8, SECURITY_GROUP 2, EC2_INSTANCE 1, IAM_ROLE 1, INSTANCE_PROFILE 1, LOAD_BALANCER 1; `LIVE_NAMES.json` vintage
  2026-09-14 12:13:53 UTC) to `gateway-*` canonical forms: a verdict, not a rename (`1.0.0_SA_CTO` 97167). `EN-s-1`'s counts
  carry that shift.

**The population `EN-r-4` fills first** (fixed input `fixed_inputs/r2/RESOURCE_GAPS.json`): the 48 names in LGIC_NAMING
round 2's forms whose canonical form carries `{system}` (`n4-firm-patterns.md` @`a4480344e3`, row LGIC_NAMING-S20):
49financial 14, inflection 27, cottonwood 6, demo 1. At this cut `grade(name, "IAM_ROLE")` returns each record's
canonical form, 48 of 48. In each, the token after the scope is a function word, so no `systems.json` row fills the slot
(PRD v1.2). A `resources.json` row fills it, or the name keeps its placeholder and is counted with its reason. A
placeholder is not a RAISE, so none of the 48 is in `EN-r-2`'s population.

**A finding the analysis could not see, carried into the faces:** the census reaches its end only if NO group is class (d).
A rule gap *"stays a loud RAISE"*, and the census stops on a RAISE (DEC-7). K1's 166 repo keys are a rule-plane population
(a first segment that is neither a source nor a tier). If `EN-r-2` classes any group (d) or leaves one undecided, `EN-s-1`'s
S1-AC1 and S1-AC2 FAIL by measurement, `EN-s-2`'s population criterion with them, and those orders stay pending with VALID
proofs. That is the round's measurement, not a defect of the cut.

**Gate G-V19 -- the one-carrier landing.**
- `EN-r-5` lands on CLOUD first: it writes `lib/opal_naming.py` and LGIC_NAMING's `GRADING_RULE.md`, as the V19 cells do.
- `1.0.0_SA_CTO` then writes `NAMING_SCHEMA.json` v1.9 on branch `lgic-v19-landing`, which `2.0.0_SA_COO~G` cuts from
  CLOUD: `firm_forms` removed, and the Terraform-type-to-node-type map as data (C-S11).
- **G-V19a:** v1.9 is on that branch (met: @`bf506e53be`, ADMITTED there). `EN-r-3` and LGIC_NAMING's cell g-1 are then cut from its tip. Each, verified by the
  issuer, merges into `lgic-v19-landing`, never CLOUD. LGIC_NAMING's cell g-2 (`grade()` to FN1d, the map read as data,
  the two-way check between the rule and `grade()`) is cut after both.
- **G-V19b:** the group reaches CLOUD in ONE merge. The reason is RULING ONE's *"in the same commit, so the data and its
  readers never disagree"*, and one writer at a time on `lib/opal_naming.py`.
- Every other round-2 cell that reads the schema's map or the one-carrier registry is spawned after G-V19b.

**The cells, one acceptance clause per line.** Every mechanical clause is one subcommand of `check_en_r2.py`, except
`EN-s-1`'s four and `EN-s-2`'s two, which re-run round 1's `check_en.py` subcommands unchanged.

| cell | round 2 | serves | acceptance, one clause per line |
|---|---|---|---|
| `EN-r-5` | the gateway registration, whole (`fixed_inputs/r2/gateway_whole.patch`, 12 paths) | FWD-5, FWD-7 (Rule 30) | validate: 0 refusals and 17 system rows · `generate` reproduces the 9 committed views · the naming suite has no new failure against the base (RULING RED) · `address("gateway","49financial","bronze","taxsma_workbook",...)` is the `opal-data-assets` key · `name("gateway","49financial","taxsma","role")` is `gateway-49f-taxsma-role` · `sharepoint` is still refused · only the `opal-gateway` worked case of `GRADING_RULE.md` moves, to `gateway-lb` |
| `EN-r-3` | RULING ONE, DEC-1, RULING DEMO, the tftest (cut from `lgic-v19-landing`) | FWD-2, FWD-7 | a census: 0 reads of `firm_forms` remain -- none in `lib/opal_naming.py` (every reader: `:248`, `:287-290`, `:347`, `:381`), none in the schema, and every other tracked file an unscoped search finds is a recorded non-reader, denominator printed (97200) · validate: 0 refusals, no warning but the inferred-owner ones · one new FIRM row draws no warning · one change to a firm's short form moves `name()` and `fence_patterns()` together · the tftest is generated and reproduces · every scope-row field is read by the module · `scopes.json`'s `_about` names one home (row S19: its `row_fields`) · demo's tenancy is DEMO-TENANT with a home rule and a corrected note · every file that named `firm_forms` at the base is dispositioned · the naming suite has no new failure |
| `EN-r-2` | RULING ROWS over the 152 groups | FWD-5 | every group in exactly one of (a), (b), (c), (d), undecided, counts summing to 152 less the pre-landed · the registry validates · every (a) group is a `systems.json` row of a ratified class with a D-code owner · every (a)/(b)/(c) group's examples stop raising on that group · every (d)/undecided group's examples still raise · no token is both a row and unresolved or refused · `J`: every classification and every row's owner basis holds |
| `EN-s-1` | the census, run again | FWD-5 | round 1's S1-AC1..AC4 unchanged (both planes; every nameable name judged; row shape; a RAISE stops the run) · the report is at HEAD's registry |
| `EN-s-2` | the comparison, again | FWD-5 | round 1's S2-AC1 and S2-AC2 unchanged · the comparison stands on a census that judged the whole population · `J`: the totals agree with the hand ranking, or every difference is explained |
| `EN-r-4` | the resource-to-system rows (PRD v1.2 E13) | FWD-5; LGIC_NAMING FWD-5 | every row carries exactly name, type, system and evidence, none empty · the registry validates · validate refuses a planted row with an empty field · a repeated (name, type) · an unregistered system · the system `opal` · a type the grade does not take · a row for a name that resolves its own system · `grade()` over a rowed gap puts the row's system in its canonical form, and without the row the placeholder stays · each of the 48 gaps is rowed or counted with its reason · the naming suite has no new failure · `J`: every row's evidence attributes the resource to that system |
| `EN-r-6` | per-view hashes; every view regenerated | FWD-7, FWD-3 | each generated file's mark hashes exactly the registry files it lists · a registry file a view does not list leaves its bytes unchanged · a file it lists moves its mark · the 7 carriers' exports equal the base's, in order, `bucket_for` on both branches · `generate` reproduces all 10 generated files · each consumer suite (views 1, 2, 3, 4, 6) has no new failure against the base |
| `EN-g-1` | the commit limb, additions only | FWD-4 | a machine-written plan file is not graded, while the same name in an authored file is refused · the limb validates the registry first: over a refused registry it prints `NAMING ERROR` and exits 1 enforcing and 0 in WARN mode, and over the valid one it prints none · the limb holds no Terraform-type map of its own · round 1's 14 commit-limb criteria still pass |
| `EN-t-2` | the apply limb reads the plan | FWD-4 | a created resource with a wrong literal name is refused with its canonical form · a created resource whose wrong name was built by an expression is refused at plan with its canonical form · a rename to a wrong name is refused · existing, updated and deleted resources only warn · a correct create passes · the pre-plan limb prints the deferred-expression count and never refuses · safe-apply blocks on the plan limb before apply · safe-apply passes the plan limb on a correct plan |
| `EN-t-3` | the Terraform roots, switch on | FWD-4 (G-F's prerequisite) | the pre-plan limb refuses none of the 78 Terraform directories · every one of the 73 roots with a backend block is planned read-only · the plan limb refuses no resource that is neither created nor renamed · every create and rename is disclosed with the limb's verdict · `J`: the extracts are the roots' real plans |
| `EN-x-1` | FWD-2 on one carrier | FWD-2 | the before-to-after diff has exactly one hand edit, `scopes.json` · the resource's name moves in the plan JSON · the firm's fence pattern moves in the generated locals |
| `EN-d-1` | FWD-7: firm N+1 draws no warning | FWD-7 | the fixed firm `quillwater`/`qwt` · the expected set before the generator · the generator's diff equals the expected set · the new row draws no validate warning · a hand-typed address is refused · a hand-typed name is refused |

**Edges** (spawn after drain, as in section 5):

```
  EN-r-5 --> [EN-r-5 on CLOUD] --> [G-V19a: v1.9 on lgic-v19-landing] --> EN-r-3 --+
                                        LGIC_NAMING cell g-1 ---------------------+--> LGIC_NAMING cell g-2 --> [G-V19b]
  [G-V19b] --> EN-r-2 --> EN-r-4 --+--> EN-s-1 --> EN-s-2
                                   +--> EN-r-6 --> EN-d-1
                                   +--> LGIC_NAMING cell f-1 (its round-4 re-grade: after EN-r-2 by 97137, after EN-r-4 by 97177)
  [G-V19b] --> EN-g-1 --> EN-t-2 --> EN-t-3
  [G-V19b] --> EN-x-1
```

- `EN-g-1 -> EN-t-2`: the apply limb imports the commit limb's map (`naming-apply-gate.py` `COMMIT_LIMB`), so the pair has
  one writer at a time.
- `EN-r-2 -> EN-r-4`: a resource row names a `systems.json` key, so the keys `EN-r-2` adds are there to name; and the two
  are the round's registry writers, one at a time.
- `EN-r-4` writes `lib/opal_naming.py` (`_slots`, `validate`), so it sits where no other writer of that file is live:
  `EN-r-5` lands before G-V19, the V19 group (`EN-r-3`, LGIC_NAMING cells g-1 and g-2) lands at G-V19b, and `EN-r-6`
  spawns only after `EN-r-4` drains. One writer at a time (97177).
- `EN-r-4 -> EN-s-1`: the census grades with the rows in place, as LGIC_NAMING cell f-1's re-grade does.
- `EN-r-4 -> EN-r-6`: the per-view regeneration is the round's last registry write, so every view ends current.
- `EN-r-6 -> EN-d-1`: the expected diff set is computed under the per-view scheme.

| slot | cells, in order | spawned |
|---|---|---|
| ~6 | EN-r-5 | at issuance |
| ~1 | EN-r-3, then EN-r-2, then EN-r-4, then EN-r-6 | EN-r-3 at G-V19a, from `lgic-v19-landing`'s tip (@`bf506e53be` or later); EN-r-2 at G-V19b; EN-r-4 after EN-r-2 drains; EN-r-6 after EN-r-4 drains |
| ~2 | EN-s-1, then EN-s-2 | after EN-r-4 drains |
| ~3 | EN-g-1, then EN-t-2, then EN-t-3 | at G-V19b; each after the one before drains |
| ~4 | EN-x-1 | at G-V19b |
| ~5 | EN-d-1 | after EN-r-6 drains |

**Fan-out: N of M = 6 chains (EN-r-5; the registry chain; the census chain; the limb chain; EN-x-1; EN-d-1), cap 8.** One
worker at issuance (EN-r-5), which lands before any other chain spawns. At most 4 at once: ~1, ~3 and ~4 from G-V19b,
~2 once EN-r-4 drains, and ~5 only once EN-r-6 drains, when ~1 has ended. No distinct-worker constraint binds this round:
`EN-d-2` is not re-run.

**Disk.** Four cells make practice copies or plan real roots (`EN-t-3`, `EN-x-1`, `EN-d-1`, and `EN-r-3`'s landing-branch
worktree). The 10G stop line binds at every spawn (C: read 27G free at this cut).

**Choices this cut makes that the analysis did not** (each revertible at the round-2 analysis):
1. The population is the 152-group union of both planes, not the live 115.
2. `EN-r-5` is a worker cell: the prepared change touches six paths whose lanes refuse the issuer, and the canonical route
   for a lane-refused change is a worker grant.
3. `EN-r-6` is ONE cell for every view (round 1 used six): regeneration is mechanical and has one writer at the round's
   last registry state; each consumer suite is its own criterion.
4. The limbs read the schema's map too: C-S11's one carrier, extended to the two limbs, so the type map has one home.
5. `EN-t-3` plans the 73 roots that declare a backend. The other 5 Terraform directories (4 under `modules/`, and
   `shared-infra/apigateway-portal`) cannot plan alone; the pre-plan limb reads all 78.
6. Every round-2 result file carries `.r2.`, the new exercise records are new files (`EXERCISE_FWD2_R2.md`,
   `EXERCISE_FWD7_R2.md`), and proofs pin artifacts by commit (S18; the one-shot `PENDING-THIS-COMMIT` sentinel went stale on
   `EN-x-1` in round 1).
7. `EN-r-4` (97177) sits in the registry chain, after `EN-r-2` and before `EN-r-6`, not in a slot of its own: it writes
   both the registry and `lib/opal_naming.py`, and that chain is where those writers are already one at a time.

**What this cut does not claim:** that the census reaches its end (the finding above); that every one of the 48 gaps
gets a row (a resource no owner can be named for is counted, never guessed); G-F's flip; that `EN-t-3`'s extracts
are the roots' real plans (T3R-J1, at L9); the population at any later vintage.

**Battery at the cut.** comp-schedule: CARRIED from L5 (`--budget 540`, 5 of 5 carriers, 25 gates, none naming this
project). Not re-run: the round adds no schedule, trigger or gate of its own beyond G-V19, which is registered here.
comp-iam: DECLARED-NOT-APPLICABLE, measured on the round-2 write set: registry rows, the module, the two limbs, `safe-apply.sh`,
records and read-only plans; no operation, policy, principal or resource is added. comp-adversary: RUN on the analysis
(3 of 3 cited commits verified; 1 cited path, stable; T11 stated: the analysis carries no `<decomp_ref>`, so filesystem
adjacency stands as its neighborhood).

**L4-R at the cut:** ADMITTED at v1.1 for v2, and at v1.2 for v2.1 (both halves current).

---

## 0c. v3 -- THE ROUND-3 RECUT (L10: 1.0.0_SA_CTO's round-2 analysis)

**Input.**
- The analysis: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`,
  s.3's cell table, on `3.0.0_SA_CVO`'s round-2 slug. Its cells are named INDICATIVELY and it says so; the
  split, the order and the ACT are left to this seat.
- `1.0.0_SA_CTO` 97445 (RULING R-22): cell 1 is not this round's -- the four row-gate limbs are LANDED by that
  seat in `.tools/surprise-row-gate.py` @`9d10c4b796`, 15 new arms, 131 of 131, red-first against HEAD. R-22
  took shape (a) on this seat's S56: THE ACT BELONGS TO WHOEVER THE LANE ADMITS. That sentence is the whole
  method of this recut, and it is applied below to every cell rather than only to the one that raised it.
- `0.0.0_AB_MSTR` 97450: the `scopes.json` worker-True was a STALE FACE, not a lane defect.

**Cell 1 is closed, and the count reconciles.** The analysis's table prints TEN rows but counts EIGHT cells,
and this seat's own S56 called it NINE; all three agree once `2b` is read as cell 2's SECOND PART (it writes a
different file, depends on cell 2's drain, and is the same gate's flip) and cell 1 is removed as LANDED. So:

```
  rows in the analysis's round-3 table ................................. 10
  minus 2b, which is cell 2's second part, not a cell ................... -1
  = cells ............................................................... 9
  minus cell 1, LANDED by 1.0.0_SA_CTO @9d10c4b796 under R-22(a) ........ -1
  = ROUND 3 IS EIGHT CELLS: 2 (with 2b), 3, 4, 5, 6, 7, 8, 9
```

### THE ACT CENSUS -- who may lawfully write each cell's surface

Run AT THE CUT, on the lane file's own instrument (`.tools/owned-paths-validate.py`: `resolve_lane()` for the
lane, `permitted_agents` for the roster, and the `--check-agent` CLI with each path PIPED ON STDIN -- an EMPTY
stdin admits every serial, so nothing was left to default). The worktree `.owned-paths.yaml` was verified CLEAN
against HEAD by `git status --porcelain` before the read, so these are the RECORD's bytes and not a neighbour's
uncommitted edit. This is S23's instrument-dependency read and S31's grant-breadth read, both of which the
analysis asks for by name.

⛔ **IT MUST BE RUN AFTER THE STALE FACES WERE RETIRED, OR IT READS THE WRONG WORLD.** Six LGIC_ENFORCE
orders sat non-terminal at HEAD carrying VALID proof-of-spec instances -- the class `0.0.0_AB_MSTR` named in
97450 -- and each was a live ADHC_OWNPTH.005 grant to its `issued_to` worker for every path in its block. This
seat retired all six @`9f9d006c8b` (the word is `complete`, not `superseded`: see the note that closes this
section). Before that flip `0.9.0_WK_LGIC_ENFORCE~1` read PERMIT on `infra/logic/registry/scopes.json`; after
it, REFUSED. **A grant census run over a tree with stale faces measures the faces, not the lanes.**

| cell | the surface that decides | lane | worker | `2.0.0_SA_COO~G` | whose act |
|---|---|---|---|---|---|
| 2 | `.tools/naming-gate.py` | `ANY` | PERMIT | PERMIT | WORKER |
| 2b | `org/mcp/naming-gate.enforce` | `BASE_EXEC` | REFUSED | PERMIT | ISSUER, after cell 2 drains |
| 3a | `.tools/proof-of-spec-check.py` | `ANY` | PERMIT | PERMIT | WORKER |
| 3b | `deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py`, and LGIC_NAMING's `check_ln_r4.py` | `TREE_DELIVERABLES` | REFUSED | PERMIT | ISSUER (S55's repair) |
| 4 | `LGIC_ENFORCE/deliverables/<blob>` -- NO serial subfolder | `TREE_DELIVERABLES` | REFUSED | REFUSED | **NOBODY** -- see below |
| 5 | `infra/logic/registry/*.json` | `PLATFORM_LOGIC_DOCS` | REFUSED | REFUSED | `4.0.0_SA_CRO` only |
| 6 | the worker's own `deliverables/<serial>/` | `TREE_DELIVERABLES` | PERMIT | REFUSED | WORKER |
| 7 | `infra/logic/registry/exemptions.json` | `PLATFORM_LOGIC_DOCS` | REFUSED | REFUSED | `4.0.0_SA_CRO` only |
| 7 | `org/critical_paths/change_management/`, `.open_deploys/` | `ANY` | PERMIT | PERMIT | WORKER (the ledger half) |
| 8 | the worker's own `deliverables/<serial>/` | `TREE_DELIVERABLES` | PERMIT | REFUSED | WORKER |
| 9 | `lib/opal_naming.py` | `BASE_EXEC` | REFUSED | PERMIT | ISSUER |

**POSITIVE CONTROL, so no row above is read as a broken instrument:** `4.0.0_SA_CRO` reads PERMIT on every
`infra/logic/registry/` path in the same sweep. The lane resolves and admits somebody; these are grant
boundaries, not a blanket refusal and not a failed read.

**Cell 4 has no lawful actor on its source side, and that is not a new fact -- it is R-2's.** The 18 ownerless
files sit DIRECTLY under `deliverables/` with no serial in the path, and `TREE_DELIVERABLES` derives the owner
FROM the path; with no serial there, the lane admits nobody. Measured: worker REFUSED, `2.0.0_SA_COO~G`
REFUSED, `1.0.0_SA_CTO` REFUSED, `4.0.0_SA_CRO` REFUSED -- on the same call that returns PERMIT for each
destination's own owner (`deliverables/2.0.0_SA_COO~G/...` -> this seat PERMIT;
`deliverables/1.0.0_SA_CTO/...` -> the CTO PERMIT). A `git mv` stages BOTH paths, so the move needs the
source's permission and there is none. R-2 ruled reading (a) with NO override, and the remedy it named -- a
relocation cell -- has now missed two rounds.

⚠ **AND THE POPULATION IS 18, NOT THE 17 S35 RECORDS.** Re-counted at WRITE time by git object type over
`git ls-tree HEAD` (the method S35 itself established, after an earlier count of 26 mistook nine serial TREES
for files): **18 blobs, 9 trees.** The trees agree; the blobs differ by one. Every one of the 18 has a
first-commit date at or before `2026-09-16 07:29 -0400`, which PRECEDES S35's own `surfaced_at` of
`2026-09-16T14:20Z` -- so this is not growth since S35, it is an undercount INSIDE S35, and the true figure at
its own vintage was already 18. R-2 measured 12. S35 is ARMED with `disarm_owner` `2.0.0_SA_COO~G`, this seat;
the correction rides its disarm at cell 4's drain rather than opening a new row.

### What round 3 cuts, and what it routes

**FIVE WORKER CELLS** -- cut as task orders: `2` (the gate's domain), `3a` (the `proof-of-spec-check.py`
channel-resolution fix, LGIC_NAMING-S21), `6` (the census to the end), `7-ledger` (the live-plane writer census
and the change-management entry), `8` (the roots census, evaluated). Each writes only `ANY` surfaces or its own
`deliverables/<serial>/`.

**THREE ISSUER ACTS** -- taken by `2.0.0_SA_COO~G` at the issuance commit, each with its negative self-test arm
exercised ALONE as the evidence, C-S20-style: `2b` (the `naming-gate.enforce` flip, bound to cell 2's drain AND
to the 78-root read of 0 refusals of existing resources), `3b` (S55's `\x1b` strip and `--color=no` repair in
`check_en_r2.py` and `check_ln_r4.py`), `9` (the generator's target-list print in `lib/opal_naming.py`).

**THREE CROSS-PROJECT ROUTES -- NOT CELLS OF THIS PROJECT**, by R-22(a)'s own reasoning and CN-i-1's precedent:
- **Cell 5's registry edits and cell 7's `exemptions.json` -> `4.0.0_SA_CRO`.** `PLATFORM_LOGIC_DOCS` exists so
  that the registry Rule 30 makes authoritative for every address and name is not edited by the projects it
  grades -- and LGIC_ENFORCE is exactly such a project. No lane widening is proposed. What IS cut here is each
  cell's MEASURE-AND-RECORD half, which needs no registry write: the class prints, the denominators, the `note`
  reader's record, the four PRODUCT owners measured, and the live-plane writer census.
- **Cell 4's relocation -> `1.0.0_SA_CTO`,** as the seat that ruled R-2 and the only one that can authorise the
  audited override or ask `0.0.0_AB_MSTR` for the lane amendment. Filed as `LGIC_ENFORCE-S57` (BLOCKING, ARMED,
  `disarm_owner` `1.0.0_SA_CTO`) together with the registry finding.
- **Cell 5's `scopes.json` `row_fields` text (S19)** rides the same CRO route.

**This is not a narrowing of the round.** All eight cells are worked this round; three of them are worked to
the boundary the lane draws, and the remainder of those three is routed to the seat that may act, with its
evidence already measured rather than left to be rediscovered.

**A note on the word `complete` at `9f9d006c8b`, because 97450 asked for `superseded`.** All six retired faces
carry a proof-of-spec instance that this seat re-ran through `.tools/proof-of-spec-check.py` with
`--governing-order` BOUND (the form `to-pipeline-gate.py`'s complete-flip path uses): six of six VALID, rc=0.
`superseded` would state on the record that the work was discarded; it was done and graded. The project's own
convention is measured, not invented: of the round-1 faces that DO carry a round-2 recut, four of four already
read `complete` at HEAD (`EN-d-1`, `EN-g-1`, `EN-s-2`, `EN-t-2`), and NO task order in LGIC_ENFORCE reads
`superseded` at any vintage. Two of 97450's supporting legs also did not survive reading the artifacts:
`EN-v-1` has no round-2 recut at all, and `EN-s-1`'s recut is itself non-terminal. The citing clause is safe to
the reader that matters -- `owned-paths-validate.py`'s `_TO_STATUS_RE` takes the FIRST word token and is
line-anchored, and `EN-g-1-r2` already carries prose after its word at HEAD.

### v3.1 AMENDMENT (pre-issuance): RULING R-23 @2a2d10acd8 -- THE THREE CROSS-PROJECT ROUTES COLLAPSE TO NONE

`1.0.0_SA_CTO` ruled S57 before this round was issued, so this amends the cut rather than moving a frozen
spec. **Cells 4, 5 and 7 are WORKER cells in full, registry half included.** The three routes s.0c sends to
`4.0.0_SA_CRO` and to `1.0.0_SA_CTO` do not exist; nothing is owed at either seat, and no lane is widened.

**THE MECHANISM THIS CUT MISSED, and it is the converse of the warning s.0c itself prints.** The act census
above is a census of LANES and is correct as one -- the ruling says so in terms. But a worker's admission does
not come only from a lane: `owned-paths-validate.py` `_owns_task_order_paths` (`:209-235`, ADHC_OWNPTH.005,
Andrew-direct "recs approved" @`9ef9a40aae`) admits a `0.9.0_WK_<CODE>~<n>` on ANY path a NON-TERMINAL order
issued to it names in `<paths>` -- exact, glob or `dir/` prefix (`_order_grants :162-173`) -- consulted after
lane enumeration fails, **for every lane, `PLATFORM_LOGIC_DOCS` included.**

```
  s.0c's warning   a census run over a tree with STALE faces measures the FACES, not the lanes
  its CONVERSE     a census run with NO face measures the LANES, not the GRANT THE ISSUANCE CREATES
```

Both are true, and this cut walked from the first straight into the second. Retiring the six stale faces
@`9f9d006c8b` was right and the post-flip reading was right; what does not follow is "whose act", because the
grant this round's own `<paths>` will mint had not been written yet. **The order IS the grant: created by the
issuance, retired by the drain** (a terminal order grants nothing, `_worker_orders :176-178`). That is exactly
why `0.9.0_WK_LGIC_ENFORCE~1` read PERMIT on `scopes.json` while the stale face was pending and REFUSED the
moment it was retired -- the face went away, the mechanism did not.

**THE CORROBORATING MEASUREMENT, on an instrument other than this seat's** (`git log -- infra/logic/registry/`):
every commit that has ever written the registry in this project is a WORKER's -- EN-r-1 @`a925c8a642`, EN-f-1
@`080e1b97c6`, EN-r-3-r2 @`22e86e55f5`, EN-r-2 @`72d636db4f`, EN-r-4 @`b15ed01ee6` (30 rows), all
`0.9.0_WK_LGIC_ENFORCE~1`; EN-r-5 @`c19dcc8147`, `~6`. **Six of six, zero by a CRO serial.** `PLATFORM_LOGIC_DOCS`
binds seats acting OUTSIDE an order, which is what its minting commit @`df27878bfe` was for; the CRO's hand is
the PRD's ratified text and the brief half, not the rows.

**CELL 4 IS A WORKER CELL TOO, and clause 5 admits the worker on BOTH sides of the `git mv`.** R-2 and R-12 are
OWNED by the ruling for naming the cell without the mechanism that admits its mover: the lane genuinely admits
nobody, and this seat was right about that -- but the order's `<paths>` is what moves the files. The cut names
**each of the 18 source paths** (`git ls-tree HEAD`, blobs only, denominator printed at the cut) **and each
destination `deliverables/<first-minting-author>/` folder** (`git log --diff-filter=A --format=%an`: 17 are
workers' files; `FENCE_PROBES.md` @`d482e58ecf` is this seat's own and moves under clause 4). Citations
re-pointed, the 62-entry `FIRM_FORMS_READERS.md` edit and S21's line applied in the same drain, S21 and S22
disarmed there, and S35's undercount corrected on its disarm -- the 18-vs-17 correction above stands and is
recorded there, as R-12 wrote.

**WHAT STAYS AN ISSUER ACT, and why the reason now matters.** `2b`, `3b` and `9` remain this seat's **by the
decomposition's own choice, not by a refusal** -- `3b` writes this seat's `fixed_inputs/`, which the spine
reserves; `2b` is bound to cell 2's drain and to the 78-root read; `9`'s edit is one print in a file this round
otherwise only reads. Cell 1's gate limbs stay `1.0.0_SA_CTO`'s under R-22, which the spine reserves.

**SO THE ROUND IS: SEVEN WORKER CELLS (2, 3a, 4, 5, 6, 7, 8) AND THREE ISSUER ACTS (2b, 3b, 9).**

**VERIFY AT THE CUT, with the instrument already used and a positive control** (R-23 s.3): stage the order,
pipe each `<paths>` entry to `--check-agent` for that order's `issued_to` worker and read PERMIT; positive
control EN-r-4 @`b15ed01ee6`. A grant census is run against the faces the cut WILL create, never the tree
before it.

**R-16 is unchanged and binds the registry half:** a registry edit is a deploy on every shipping generated
view, disclosed by DEC-5 and printed by the gate; cell 7's change-management entry is the ledger half of the
same cell.

### v3.2 AMENDMENT (pre-issuance): THE WRITE SURFACES MEASURED, THE SLOT PLAN, AND CELL 9 BECOMES A WORKER CELL

**Every write surface below was read from the code that produces it, not from the cell table.** The generator's
per-target registry keys (`lib/opal_naming.py` `TARGET_REGISTRY_KEYS`) decide which generated files a registry
edit re-stamps, so they decide which cells collide:

| target | registry files it is stamped from |
|---|---|
| the 7 VIEWS (firm_registry.json, firm-config.mjs, the two investor_reporting scripts, loaders.py, perfrp_firm_pin.py, ds-precommit-check.py) | `scopes` (perfrp_firm_pin.py also `tiers`) |
| `modules/opal_name/generated_locals.tf` | `scopes`, `exemptions` |
| `modules/opal_name/tests/vectors.json`, `tests/opal_name.tftest.hcl` | `scopes`, `systems`, `exemptions`, `resources` |

**So cells 5 and 7 COLLIDE on two files neither names in the analysis.** Cell 5 edits `systems.json`, which re-stamps
`vectors.json` and `opal_name.tftest.hcl`; cell 7 edits `exemptions.json`, which re-stamps those same two AND
`generated_locals.tf` -- and `generated_locals.tf` enters the `shared-infra` plan (the one root consuming the
`opal_name` module), so cell 7's registry edit is a deploy on that root under R-16 and DEC-4's never-widen sign-off.
**Cells 5 and 7 are therefore ONE worker's queue, 5 then 7**, which the edge 5 -> 7 already forces. Neither touches
the 7 VIEWS (neither edits `scopes` or `tiers`), so neither re-mints the investor_reporting bundle.

**CELL 9 IS A WORKER CELL.** R-23 s.3 kept it an issuer act "by the decomposition's own choice, not by refusal";
this cut changes that choice. `lib/opal_naming.py` is admitted to the worker by the order's `<paths>` exactly as
`systems.json` is (ADHC_OWNPTH.005), and cell 9 is a build with its own contract -- the target list by AST, the
SHIP / REPO-ONLY split, the hash-pinned-consumer census -- which belongs under a worker's criteria and the CVO's
grading, not under the issuer's own hand. **Its split is RULED by R-26 @`50f1786314` on `LGIC_ENFORCE-S60`:** R-16 named `safe_deploy_core.py` as the classifier, and called on the 10 targets it decides 3 and returns None for 7, at least 5 of which ship through other planes. So the split calls EACH PLANE'S OWN RECORD -- `safe_deploy_core.py` for S3/DS, `infra/aws/lambda/ci/lambda-source-map.json` for Lambda with a shared import resolved to every importing function, the consuming Terraform root measured by `comp-find` for Terraform -- with provenance per row naming the instrument and each plane's denominator printed. A target no plane claims prints UNCLASSIFIED and REFUSES the print. The two `opal_name` test fixtures are REPO-ONLY with the plane named. The ruling's own "8 of 10 SHIP" is withdrawn as a count by recall: the criterion prints what the three instruments return.

**THE REMAINING ISSUER ACTS:** `2b` (the `naming-gate.enforce` flip, after cell 2 drains and the 78-root read) and
`3b` (landed @`c8f9398b85`; the strip half needed no repair, only `--color=no`).

**EDGES AND THE SLOT PLAN.** `5 -> 6`, `5 -> 7` (the census and the writer disposition read the registry cell 5
lands); `3a -> 8` (the roots census is graded by the tooling cell 3a repairs); `6, 7, 8 -> 4` (cell 4 MOVES
round-2 records that cells 6, 7 and 8 read at their flat paths, and re-points the three live readers, so it runs
after them); `2` and `9` independent.

```
  slot ~1  EN-n-1-r3 (cell 2)                                   .tools/naming-gate.py
  slot ~2  EN-r-5-r3 (cell 5) -> EN-w-7-r3 (cell 7)              systems.json -> exemptions.json + generated_locals.tf
                                                                 + the two opal_name test fixtures + the shared-infra apply
  slot ~3  EN-i-3-r3 (cell 3a) -> EN-t-8-r3 (cell 8)             .tools/proof-of-spec-check.py -> the roots census records
  slot ~4  EN-s-6-r3 (cell 6)                                   the census report and comparison records
  slot ~5  EN-g-9-r3 (cell 9)                                   lib/opal_naming.py
  slot ~6  EN-p-4-r3 (cell 4)                                   the 18 moves, the 3 live readers, FIRM_FORMS_READERS.md
```

`fanout: 6 slots over 3 connected components, cap 8, reason: components {2}, {9} and {3a, 8, 5, 6, 7, 4};
levels L0 = {2, 3a, 5, 9}, L1 = {6, 7, 8}, L2 = {4}; the big component is not one queue because 6, 7 and 8 run in
parallel once their parents drain, so a worker per parallel branch buys wall-clock -- except 5 and 7, which share two
regenerated fixtures and one queue; cell 4 is last because it moves what 6, 7 and 8 read.`

> The first draft of this line read "6 of 4 chains", which the queue rule it cites forbids (N is bounded by M). By
> the edges there are 3 components, not 4, and the parallelism is the level width inside the largest, stated above.

## 0d. v3.3 -- THE ROUND-4 RECUT (L10: 1.0.0_SA_CTO's round-3 analysis)

**Input.** The analysis `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/1.0.0_SA_CTO/LGIC_ENFORCE_ROUND3_ANALYSIS.md`
@`969f89b0e7`, on `3.0.0_SA_CVO`'s round-3 slug (97630) over this seat's drain-end (97620). Its **R-32** names round 4's
five cells and **R-33** gives the campaign cell its own bound. Rulings carried into the faces: R-29 (the mint rule and
its fence guard, verbatim), R-30 (DEC-4(ii)'s criterion text), R-32, R-33.

**Round 3 graded REALIZED 6 of 7.** FWD-5 is the only outcome left, and it does NOT close by another census run: round
3 measured the population behind it -- **351 distinct (plane, type, name) RAISE triples** plus **8 `{system}`
placeholder rows**, the first from `RAISE_POPULATION_S6.r3.md`, the second from round 3's own census report. Round 4 is
the campaign that works that measured list, and then the run that reads the closed population.

**THE CELL COUNT.** This decomposition's section 3 lists 22 cells. Round 4 adds five, numbered 23 to 27, and no earlier
cell is re-opened:

```
  cells at v3.2 ......................................................... 22
  plus round 4's five, from R-32's table ................................. +5
  = cells in this decomposition ......................................... 27
  round 4 runs exactly the five: 23, 24, 25, 26, 27
```

| cell | id | what it does | rulings | serves |
|---|---|---|---|---|
| 23 | `EN-c-23` | **the campaign.** Work the 351-triple population: mint the registry row where owner and token are MEASURED from a declared source (`lambda-source-map.json` `source_dir`/`tf_file`, `EC2_MANIFEST.json` `source_path`, the Terraform tree that declares it), `owner_claim: inferred` with the citation as `owner_basis`; otherwise ONE owner card with the reason and the name recorded NOT-JUDGED. R-29's fence guard verbatim: a row whose mint would change a GENERATED POLICY on an APPLIED resource is NOT minted -- it is carded BLOCKING for never-widen sign-off (`1.0.0_SA_CTO` + `2.0.0_SA_COO`). R-33's bound: past 351 + 25 measured, stop, file the delta, the remainder rides round 5 | R-29, R-32, R-33 | FWD-5 |
| 24 | `EN-h-24` | **the placeholders.** The 8 `{system}` rows of round 3's report (W2-S10's class, which is a `(name, type)` gap in `resources.json`, not a RAISE) resolved or carded | R-32, W2-S10 | FWD-5 |
| 25 | `EN-s-25` | **the run to the end.** `census --live --repo` to completion: `judged + carded == nameable` on BOTH planes, denominators printed, the live plane's `built:` vintage stated | R-32 | FWD-5 |
| 26 | `EN-d-26` | **DEC-4(ii)'s criterion text.** The amended text -- a NOT_A_PRINCIPAL claim on a bucket no live CloudTrail data-event selector covers is REFUSED; the disposition comes from a direct IAM-grant read or a NOT-JUDGED card -- and a validator that refuses a planted claim on such a bucket while still accepting one on a covered bucket | R-30 | FWD-2 (its evidence rule) |
| 27 | `EN-g-27` | **S60's disposition.** The ship classifier's undercount, graduated as a standing finding in round 3: FIXED with its measurement, or CARDED with owner and reason | R-16, R-26 | FWD-3 |

**THE CLOSURE BAR, as the analysis states it (s.4).** FWD-5 is REALIZED when `judged + carded == nameable` on both
planes with denominators printed -- **NOT "zero carded"**. A carded name is a named gap with an owner, which is what the
outcome promises; a run that stops early is not. Cell 25 is cut against that bar and no other.

**THE PRD IS NOT A WORKER SURFACE.** R-32's row for cell 26 reads "the amended text is in the round-4 cut". L4 is
`1.0.0_SA_CTO`'s alone, so cell 26 does NOT edit `prd/LGIC_ENFORCE_PRD.md`: it lands the amended criterion text as its
own deliverable, which the CTO lifts into DEC-4(ii) at its own hand, and it lands the mechanical guard that makes the
rule refuse rather than merely read.

**WRITE SURFACES, MEASURED, AND THE ONE CROSS-PROJECT COLLISION.** Per v3.2's stamping table a `scopes` edit re-stamps
the 7 VIEWS and `generated_locals.tf`; a `systems`/`resources` edit re-stamps `tests/vectors.json` and
`tests/opal_name.tftest.hcl`. **LGIC_LGCTFM round 1's open `LT-x-1` writes `infra/logic/registry/scopes.json` and
`remediations.json`** (censused at this cut from every non-terminal order's `<paths>` in both projects). Cells 23 and 24
write `systems.json` and `resources.json` only, and **no round-4 cell runs `generate`** -- so the two rounds' write sets
are disjoint at the file level and neither re-stamps a fixture the other is mid-edit. **Stated residue:** the two
`opal_name` test fixtures therefore sit at their round-3 stamp until someone re-renders. `validate` does not read them,
so nothing grades stale; the re-render is an ISSUER act (`4b`) for `2.0.0_SA_COO~G` after BOTH this round's registry
cells and LGIC_LGCTFM's `LT-x-1` have drained, and it is recorded here so it is not discovered later as drift.

**THE NAMING GATE IS ENFORCING, AND IT DOES NOT REFUSE THESE MINTS.** Measured at this cut, not assumed: a correctly
formed unified diff adding a `resources.json` row with a real name literal (`opal-news-articles`, DYNAMODB_TABLE) reads
`NAMING-GATE: PASS 0 graded` under `--enforce` -- the commit limb's graded set covers declaration-tree name MINTS
(`.tf` resource names, `.py` constructors), not registry rows. So the campaign's mints pass the gate this seat flipped
at 2b, and a worker does not meet a refusal it was not warned about.

**EDGES AND THE SLOT PLAN.** `23 -> 24` (both mint `resources.json`, so they are ONE worker's queue, 23 then 24);
`23, 24 -> 25` (the run reads the population the campaign closes); `26` and `27` independent.

```
  slot ~1  EN-c-23-r4 -> EN-h-24-r4    systems.json + resources.json (one queue, one file in common)
  slot ~2  EN-s-25-r4                  the round-4 census report and its comparison
  slot ~3  EN-d-26-r4                  the amended DEC-4(ii) text + the disposition validator
  slot ~4  EN-g-27-r4                  S60's disposition record
```

`fanout: 4 slots over 3 connected components, cap 8, reason: components {23, 24, 25}, {26} and {27}; levels L0 = {23, 26, 27}, L1 = {24}, L2 = {25}; 23 and 24 share resources.json so they are one queue rather than two workers, and 25 is a separate slot spawned after that queue drains because it re-reads the registry those cells land (the same shape round 3 used for cells 5 -> 6).`

**THE FIXED INPUTS L6 CUTS INTO THE FACES.** `deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py` (12
subcommands, one per mechanical criterion; `selftest-arms` reads 40 of 40 with every arm driven ALONE against a
doctored input, A-23) and `R4_BASE.json`, which PINS the cut's HEAD. The added-row arms read the registry at that pin
with `git show <base>:<path>` and never at `git merge-base HEAD CLOUD`, which moves under a drain and would grade a
different set on an issuer re-run.

## 0e. v3.4 -- THE ROUND-5 RECUT (L10: 1.0.0_SA_CTO's round-4 analysis)

**Input.** The analysis `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/1.0.0_SA_CTO/LGIC_ENFORCE_ROUND4_ANALYSIS.md`
@`b74ffb43ae`, on `3.0.0_SA_CVO`'s round-4 slug (97735 @`66a07704fe`), released to this seat as msg 97738. Rulings
carried into the faces: **R-38** (the placeholder population), **R-39** (`security` is NOT minted), **R-33** (the
campaign's timebox, unchanged), **R-29** (the fence guard, verbatim) and the standing bar **R-40** (a criterion whose
subject is a produced artifact binds to that artifact's content, not to its label).

**Round 4 graded REALIZED 6 of 7 and FWD-5 is again the only outcome left** -- but for a different reason than round
3's, and the difference is the whole cut. The census that stopped on its first RAISE in rounds 1, 2 and 3 now RUNS TO
THE END on both planes (live 1690 judged + 136 carded == 1826 nameable; repo 1547 + 331 == 1878; `stopped` null). That
is the CTO's stated closure bar met on its own numbers for the first time in four rounds. **The completed census
bought the finding:** the same run showed `1411 of 3237` judged rows carrying a literal `{system}`/`{scope}`/
`{cadence}` placeholder in `canonical` -- 44% of the judged population graded against a string no resource can ever
equal. Closing there would have turned the defect FWD-5 exists to detect into a guarantee that it was detected, and it
would have arrived with a printed denominator, which is what would make it dangerous rather than merely wrong.

**THE CELL COUNT.** Section 3 lists 22 cells; round 4 added five (23-27); round 5 adds four, numbered 28 to 31, and no
earlier cell is re-opened:

```
  cells at v3.3 ......................................................... 27
  plus round 5's four, from the round-4 analysis ......................... +4
  = cells in this decomposition ......................................... 31
  round 5 runs exactly the four: 28, 29, 30, 31
```

| cell | id | what it does | rulings | serves |
|---|---|---|---|---|
| 28 | `EN-c-28` | **the placeholder campaign.** Resolve every row whose `{system}`/`{scope}`/`{cadence}` substitution is MEASURED from a declared source; card the rest with owner and reason; print `resolved + carded == the start population` with its denominator; **re-measure the OWN denominator at WRITE time and print BOTH populations**; then re-run the census and re-grade round 4's AC3 against the closed population. R-29's fence guard verbatim; R-33's timebox unchanged | R-38, R-29, R-33 | FWD-5 |
| 29 | `EN-h-29` | **S61's remedy.** ONE corrected evidence string in `resources.json`'s `Inflection-HistBackfill-FailureSpike` row, then the basis re-graded against the corrected bytes. Not a re-cut of `EN-h-24` and not a new conclusion -- `system=advi` is right, only the basis is wrong | S61 (`C-S36`) | FWD-5 |
| 30 | `EN-g-30` | **S62's remedy.** The reason split re-counted FROM the comparison's own table and reconciled against its own 42, **with the SPLIT PRINTED BESIDE THE TOTAL** so the next reader can check the parts rather than the sum; and Section 3's stale count word corrected | S62 (`C-S36`) | FWD-3 |
| 31 | `EN-c-31` | **W1-S30's disarm.** The TOKEN_COLLISION card landing with `D12` / `NFRA_OPSEC202609` named as the bucket half's owner, on BOTH Card 5 and Card 6. `security` is NOT minted and the vocabulary is not reshaped for one measured collision | R-39 | FWD-5 |

**THE CLOSURE BAR IS UNCHANGED AND IS STILL NOT "ZERO CARDED".** FWD-5 is REALIZED when `judged + carded ==
nameable` on both planes with denominators printed AND no judged row is graded against a template. A carded name is a
named gap with an owner, which is what the outcome promises; a canonical of `{system}-{scope}-daily` is not a name at
all, which is what cell 28 closes.

**THE START POPULATION IS 1411 AND THAT NUMBER IS DELIBERATELY NOT AN ACCEPTANCE VALUE.** It is a count at ONE vintage
of a report the campaign itself replaces, and a row can leave the placeholder class while the cell runs. So the cell
MEASURES its start from the r4 report's own rows (arm `c28-population` refuses a declared start that disagrees with a
fresh parse) and prints `population_at_start` AND `population_at_close` with the instrument named (arm
`c28-redenominator`), and a difference between them needs a note saying why. **An inherited count is a subset
measurement until you ask what population it enumerated.**

**WRITE SURFACES, MEASURED AT THIS CUT, AND THE TWO COLLISIONS THAT SET THE SLOT PLAN.** Read from the four cells'
target artifacts, not from the cell names:

```
  EN-c-28  infra/logic/registry/{systems,resources}.json + its own PLACEHOLDER_CAMPAIGN_R5.json,
           OWNER_CARDS_R5.md and NAMING_CENSUS_REPORT.r5.md        -> deliverables/0.9.0_WK_LGIC_ENFORCE~1/
  EN-h-29  infra/logic/registry/resources.json                      COLLIDES with 28 on resources.json
  EN-c-31  deliverables/0.9.0_WK_LGIC_ENFORCE~1/OWNER_CARDS_R4.md   COLLIDES with 28 on that FOLDER's lane grant
  EN-g-30  deliverables/0.9.0_WK_LGIC_ENFORCE~2/NAMING_CENSUS_COMPARISON.r4.md   disjoint from all three
```

**THE FOLDER IS THE GRANT AND IT DECIDES THE SEATING, not a preference.** `.tools/owned-paths-validate.py` clause 4
(`ADHC_OWNPTH.004`, lane `TREE_DELIVERABLES`) permits exactly the serial named by the `deliverables/<SERIAL>/`
sub-folder. `OWNER_CARDS_R4.md` is `0.9.0_WK_LGIC_ENFORCE~1`'s and `NAMING_CENSUS_COMPARISON.r4.md` is
`~2`'s, so cells 28 and 31 are `~1`'s and cell 30 is `~2`'s and no other seating is legal. **This was MEASURED by
running the gate, not predicted:** the same clause refused this seat's own attempt to correct a worker's delivered
file on LGIC_LGCTFM the same night, and the refusal was right.

**EDGES AND THE SLOT PLAN.** `29 -> 31 -> 28` (one queue: 29 and 28 both write `resources.json`, 31 and 28 both write
inside `~1`'s folder, and 28's census must read the registry AFTER 29's correction lands or it grades a report built
on bytes the round is repairing); `30` independent.

```
  slot ~1  EN-h-29-r5 -> EN-c-31-r5 -> EN-c-28-r5   resources.json -> OWNER_CARDS_R4.md -> the campaign + the re-run census
  slot ~2  EN-g-30-r5                                NAMING_CENSUS_COMPARISON.r4.md only
```

`fanout: 2 slots over 2 connected components, cap 8, reason: components {29, 31, 28} and {30}; levels L0 = {29, 30},
L1 = {31}, L2 = {28}. The big component is ONE QUEUE rather than three workers because every pair in it shares a write
surface -- resources.json or ~1's deliverables folder -- so parallelism there would buy a merge conflict, not
wall-clock. The two small remedies run FIRST inside that queue so the campaign's census reads corrected bytes.`

**THE FIXED INPUTS L6 CUTS INTO THE FACES.** `deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py` (12
subcommands, one per mechanical criterion; `selftest-arms` drives 20 arms, each ALONE against a doctored input) and
`R5_BASE.json`, which PINS the cut's HEAD at `95fb561677`. Arms that must tell "this round changed it" from "it was
already like that" read at that pin with `git show <base>:<path>` and never at `git merge-base HEAD CLOUD`, which
moves under a drain.

**THREE CRITERIA PASS AT THE CUT BY DESIGN AND ARE GUARDS, NOT TARGETS**, stated here because a criterion that already
passes proves nothing about a cell's work unless it is labelled: `c28-fence` (the applied fence must STAY unchanged),
`h29-conclusion` (the repaired row's conclusion must NOT move) and `c31-not-minted` (R-39's bar: `security` must STAY
unminted). The other nine read FAIL at the cut, each naming the live defect it grades.

**ONE DEFECT WAS FOUND IN THIS ROUND'S OWN CHECKER BEFORE ANY WORKER SAW IT, and it is recorded because the class
repeats.** `g30-split`'s table-counting helper first counted EVERY uppercase token in every table cell. Run for real
against the comparison document it returned 36 keys summing to 149 -- resource types, verdicts, even two CloudFront
distribution ids -- of which only 4 are reason keys. Because the comparison walks the UNION of both key sets, **a
correctly corrected fence carrying 4 keys would have disagreed with 32 phantom ones and FAILED: the arm was
unsatisfiable by a correct fix.** Its injected self-test passed anyway, because the fixture handed both sides the same
key set. **An injected self-test certifies the ARMS, never the WIRING.** Repaired by scoping the count to the fence's
own declared keys, then re-run against the real document on three branches -- the live defective fence (FAIL, naming
S62's shape), a simulated correct fence (PASS), and a self-consistent fence that disagrees with the table (FAIL) --
and the table independently reproduced the CVO's own remedy split, 20/2/10/10 = 42.

**A STALE FIELD IN THIS DOCUMENT'S OWN HEADER, corrected in this commit and disclosed rather than quietly fixed:** the
header json read `"decomp_version": "v2.1"` while this document's section headings had reached v3.3 across two
recuts. It is set to `v3.4` here, matching this section.

## 0f. v3.5 -- THE ROUND-6 RECUT (L10: 1.0.0_SA_CTO's round-5 analysis)

**Input.** `LGIC_ENFORCE_ROUND5_ANALYSIS.md` @`b683398fda`, on this seat's drain-end, plus ruling **R-46**
@`c862eeb867` **AS CORRECTED** @`ab9a8f356b`. Round 5 graded **REALIZED 6 of 7**; FWD-5 stays open.

**Round 6 is TWO cells, numbered 32 and 33, and no earlier cell is re-opened:**

```
  cells at v3.4 ......................................................... 31
  plus round 6's two .................................................... +2
  = cells in this decomposition ......................................... 33
  round 6 runs exactly the two: 32, 33
```

| cell | id | what it does | rulings | serves |
|---|---|---|---|---|
| 32 | `EN-s-32` | **the DISARM SWEEP.** Over the armed population, per owner: DISARM what is genuinely met, **RESTATE what has drifted**, and say which is which. Prints its predicate, its owner-resolution order and its occurrence-vs-distinct choice BEFORE any count; re-measures the denominator at its own write time; and prints the partition `43 == 35 IN SCOPE + 8 OWNED ELSEWHERE` with the other owners named | R-46 (corrected), R-42 | FWD-3 |
| 33 | `EN-c-33` | **the campaign continued.** The 1370 rows round 5's timebox handed forward, carried by CLASS and not as one total; `NON_SYSTEM_PLACEHOLDER_TOKEN` gets a disposition of its own rather than being folded into the timebox. Same fence guard, same R-33 bound | R-38, R-33, R-29 | FWD-5 |

### WHY THE SWEEP EXISTS, AND IT IS NOT HOUSEKEEPING

Round 5's slug stated for the first time that the project carried a large ARMED population, and the number
took **three attempts across two seats** to settle: 57 against 54, then a ruling of 55, then **43** derived
independently by both seats from R-46's rule rather than from each other's answer. Each wrong number was
wrong for a different reason, and every reason is now a condition on this cell:

- **54** -- this seat's reader keyed a dict by row id so the LAST document won, and it never read the
  top-level `owner` that R-42 had just established as an addressee. **Condition: the owner-resolution
  order is PRINTED.**
- **55** -- R-46's disposition test applied to the 3 rows under discussion instead of all 57, leaving 12
  rows counted as open that a clock had closed days earlier. **Condition: the denominator is re-measured
  over the WHOLE population at the cell's own write time.**
- **92** -- the same channel at the OCCURRENCE level rather than the distinct-id level. **Condition: the
  occurrence-vs-distinct choice is PRINTED.** A number without it is not a measurement.

⛔ **AND THE SWEEP'S SCOPE IS 35, NOT 43.** Of the 43, `1.0.0_SA_CTO` holds 7 and `3.0.0_SA_CVO` holds 1,
and **a worker of this lane cannot disarm another seat's row.** So the cell works 35 and PRINTS the other
8 with their owners. A cell that graded itself on its own subset while the round called it 43 would be
this evening's subset-not-population defect one more time, in the very cell built to stop it.

**THE OWNER'S WORD IS ALREADY PARTLY GIVEN, and it shows the shape:** `1.0.0_SA_CTO` disarmed two of its
seven early (`W1-S30`, `C-S34`, row `S65`) on R-39's met condition, and **left five armed with stated
reasons** -- including `S56`, whose premise moved when that seat wrote the very file the row says is
writable by nobody. **A row whose premise moved needs a RESTATED REASON, not a disarm**, and that is the
half of the sweep that is easy to skip.

### THE CAMPAIGN'S SECOND PASS, AND THE CLASS THAT IS NOT A TIMEBOX

Round 5 carded 1370 rows in three classes, read fresh from its own record rather than quoted:
`TIMEBOXED_R33` **1134**, `NON_SYSTEM_PLACEHOLDER_TOKEN` **235**, `TYPE_MISMATCH_NEEDS_CONFIRMATION` **1**.

⚠ **THE 235 ARE A DIFFERENT QUESTION AND ONE REMEDY DOES NOT MOVE BOTH** (Rule 24(iv)). A `TIMEBOXED_R33`
row is one the campaign simply did not reach. A `NON_SYSTEM_PLACEHOLDER_TOKEN` row is one where the token
**is not a system at all**, so "resolve it from a declared source" may not even apply to it. Folding them
together would let 235 rows ride a timebox forever under a reason that was never theirs. The cell carries
every class BY NAME with its count, and gives the 235 a disposition rule of their own.

### WRITE SURFACES, AND WHY THIS IS ONE QUEUE

```
  EN-s-32   the project's surprise channel ONLY (its own sweep record in its deliverables folder)
  EN-c-33   infra/logic/registry/{systems,resources}.json + its own records + the channel
```

**Both write the channel, so they are ONE QUEUE on ONE SLOT**, sweep first. CLAUDE.md 14b says an
append-only shared file is where you do NOT isolate -- but that rule is about a seat choosing a worktree,
and TWO WORKER BRANCHES appending to one channel is a GUARANTEED conflict at the second merge rather than
a seconds-long race. Measured 3 of 3 on a sibling project's round-4 drains.

### EDGES AND THE SLOT PLAN

```
  slot ~1   EN-s-32-r6  ->  EN-c-33-r6     the channel, then the registry + the channel
```

`fanout: 1 slot over 1 connected component, cap 8, reason: both cells write the project's surprise
channel, so parallelism buys a merge conflict rather than wall-clock; levels L0 = {32}, L1 = {33}. The
sweep runs FIRST because its output is a cleaner channel for the campaign to append to, and because it is
the smaller of the two.`

### THE FIXED INPUTS L6 CUTS INTO THE FACES

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r6/check_en_r6.py` -- 9 subcommands, and `selftest-arms` drives
**28 arms, 8 of them POSITIVE-SATISFIABILITY** against two simulated correct records. `R6_BASE.json` pins
`372b1d653d`.

⭐ **THE CHECKER IMPLEMENTS R-46's PREDICATE ITSELF AND REFUSES A DECLARATION THAT DOES NOT MATCH IT.**
That is unusual and deliberate: a cell that PRINTED one rule and COUNTED by another would otherwise satisfy
condition 1 while defeating it. Verified at the cut by calling the checker's own `armed_population()`
against the live channel -- **43 still armed, 35 in scope**, matching the pin and both seats' independent
derivations.

**One guard, and it is labelled:** `c33-fence` reads PASS at the cut because the applied fence must STAY
unchanged (R-29). The other eight arms read FAIL, each because its input does not exist yet.

## 0g. v3.6 -- THE ROUND-7 RECUT (L10: 1.0.0_SA_CTO's round-6 analysis @`d1f880b870`)

**Input, and the scope is taken from the REGISTER rather than from the analysis.** `project.json`'s
`phase`, `last_updated` 2026-09-18T08:40:00Z, names round 7's material. The round-6 analysis names it
too, and where a forward carry and the register disagree the register wins (**R-57**). This lane cut
LGIC_LGCTFM round 2 against the register an hour earlier for the same reason, then took its first
framing of THIS round from an analysis and had to withdraw it -- so the rule is applied here
deliberately rather than remembered.

Round 6 graded **REALIZED 6 of 7**. `FWD-5` NOT REALIZED and carried here.

### 0g.1 THE ROUND'S CENTRAL CHOICE: IT DOES NOT ATTEMPT THE 1093

Rounds 5 and 6 each resolved **41** rows. Measured: 1411 -> 1329 in two rounds, a NET 82, with about
thirty more rounds at that rate. That arithmetic is kept as a SHAPE and not a forecast -- it assumes a
constant rate over a population twice found to be non-uniform, which is the assumption round 6
falsified.

⭐ **BUT THE DECIDING GROUND IS NOT YIELD, AND THIS LANE HAD IT WRONG FIRST.** `R-60` read `FWD-5`'s
own ACCEPT at the bytes: *"a ranked list of every name and address that breaks the pattern, each paired
with its correct form, totals shown ... THIS IS THE LIST CLEAN-UP PROJECTS START FROM"*, DONE WHEN =
EXERCISED. **THE OUTCOME IS THE LIST. THE RESOLUTION IS THE CLEAN-UP PROJECTS' WORK, AND THE OUTCOME
SAYS SO IN ITS LAST NINE WORDS.** Rounds 5 and 6 ground against a bar `FWD-5` never set, and it was
graded against that bar three times before anyone read the closing clause. A classification pass is
not a retreat from the bar; it is NEARER to it than the grind was.

⚠ **IT STILL DOES NOT MAKE `FWD-5` REALIZED.** The ACCEPT wants each row paired with its correct form
and 1093 have none. Round 7 changes WHICH WORK CLOSES IT, never whether it is closed.

**AND THE 1093's CLASS NAME IS ITSELF THE FINDING** (`R-60`, elevating this lane's sentence to a Rule
24 result): `TIMEBOXED_R33` describes the MEASURING PROCESS, not the measured domain. A taxonomy value
borrowed from the OBSERVER is not a member of the domain being partitioned at all -- a FIFTH shape
beside wrong grain, wrong axis and uncovered member, and it passes every count check because 1093 rows
really do carry it. It is 82% of what remains.

### 0g.2 THE CELLS -- 2, and no earlier cell is re-opened

```
  cells at v3.5 ......................................................... 33
  plus round 7's two .................................................... +2
  = cells in this decomposition ......................................... 35
  round 7 runs exactly the two: 34, 35
```

| cell | id | what it does | rulings | serves |
|---|---|---|---|---|
| 34 | `EN-t-34` | **THE LABELS THAT LIE.** The 51 two-carrier rows get a label naming BOTH remedies AND EACH REMEDY'S CARRIER; the 15 key-format templates get a reason saying THE ROW IS NOT A NAME instead of one saying the token is not a system | R-60, R-62(c) | FWD-5 |
| 35 | `EN-o-35` | **THE CLAIM THAT UNDER-STATES.** The 41 resolved rows read `owner_claim: inferred` because leg B inherits from a sibling whose own claim is inferred. Each is CONFIRMED from an OWNING DIRECTIVE or CARDED with a reason | R-42, R-19 | FWD-5 |

**ONE AXIS, ONE INTENT (Rule 24 iii):** both cells are about a FIELD THAT SAYS SOMETHING FALSE ABOUT A
ROW. 34 fixes labels that mis-describe; 35 fixes a claim that under-states. Neither resolves a
placeholder and neither touches the 1093.

### 0g.3 WHY THE 15 ARE CARDED HERE AND NOT EXCLUDED, WHICH IS A RULING AND NOT THIS LANE'S CHOICE

This lane was told to cut a third cell adding a `types_not_graded_by_kind` entry for the 15. **IT WAS
HELD AND MEASURED FIRST, AND THE REMEDY WOULD NOT HAVE WORKED.**

```
  all 15 rows carry type S3Key, and S3Key is ALREADY an entry in that table
  lib/opal_naming.py:493   graded_types = by_type | set(types_not_graded_by_kind)   <- UNIONS IT IN
  lib/opal_naming.py:1012  not_graded = {t for t, why in tng.items()
                                         if str(why).startswith("NOT GRADED")}      <- THE REAL SWITCH
  15 entries: 8 genuinely out, 7 STILL GRADED -- S3Key among them, reason "the key grammar (key)"
```

⛔ **`types_not_graded_by_kind` IS A ROUTING TABLE, NOT AN EXCLUSION LIST, AND ITS NAME IS THE OPPOSITE
OF ITS BEHAVIOUR.** The entry would have changed nothing, and the acceptance condition attached to it
-- a printed denominator showing the templates' addresses stayed inside the address grade -- WOULD HAVE
PASSED VACUOUSLY, because nothing would have left any grade. That is `R-47`'s own shape arriving inside
the guard written to prevent it.

`R-62` then ruled: removing ALL `S3Key` from the name grade is **REFUSED** (it removes every S3 key in
the estate to fix 15 templates, and Rule 30 makes S3 addresses the core naming surface -- **the 15 are
TEMPLATES; S3Key is EVERY KEY**); a mechanism distinguishing a template from a key is **ROUND 8**
material, because a schema change needs Rule 24's four-postulate record and a token census and is never
a rider; and **leaving the 15 CARDED UNDER A TRUE REASON is ADOPTED**, which is what cell 34 carries.

⭐ **THE STANDING HAZARD, pinned in `R7_BASE.json` because both cells read that table:** the exclusion
switch is a PROSE REASON STRING written by a human for a human, so **REWORDING A REASON SILENTLY
CHANGES GRADING BEHAVIOUR**. Turning *"NOT GRADED: AWS-issued identifier"* into *"AWS-issued
identifier, not graded"* -- an improvement in ordinary prose -- puts that type BACK INTO THE GRADE and
nothing announces it. Eight types sit on that edge. `t34-no-grade-change` READS PASS AT THE CUT and
refuses any cell that moves the table.

### 0g.4 WRITE SURFACES, AND WHY THIS IS ONE QUEUE

```
  EN-t-34   deliverables/<its serial>/ + the project's surprise channel
  EN-o-35   deliverables/<its serial>/ + the project's surprise channel
```

**ONE QUEUE ON ONE SLOT, and this round has the measurement rather than the rule.** LGIC_LGCTFM round 2
ran two slots on a stated hypothesis that a TEXTUAL SPLICE merges where a whole-array RE-DUMP
conflicts. **IT WAS REFUTED:** the second drain conflicted although both sides spliced, and
`safe-merge`'s own banner says an append-only channel conflicts on EVERY concurrent drain -- the normal
path, not the exception. The cost was one union merge, exactly as bounded, and the hypothesis is
recorded dead rather than quietly dropped. So round 7 queues.

### 0g.5 THE FIXED INPUT

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r7/check_en_r7.py` -- 8 subcommands; `selftest-arms` drives
**21 arms, 8 of them POSITIVE-SATISFIABILITY** against simulated correct records. `R7_BASE.json` pins
`2c3d7b0cb2` and EVERY figure in it was MEASURED at the cut: the 51 **re-identified independently of
round 6's own label** by requiring both `{system}` and `{cadence}` in the row's text (51 = 51,
EVENT_RULE 49 / LOG_GROUP 2); the 15 by the five unsanctioned tokens (all `S3Key`); the 41 (41 of 41
`inferred`); and the exclusion table's 8/7 split.

**WIRING MEASURED AT THE CUT, NOT ASSUMED:** 7 of 8 real arms read FAIL because their inputs do not
exist; `t34-no-grade-change` reads PASS and is LABELLED a guard.

### 0g.6 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** make `FWD-5` REALIZED, and 0g.1 says why in the outcome's own words.
- It does **not** touch the 1093, and does not pretend the arithmetic for them has improved.
- It does **not** change any grading behaviour. The exclusion table is guarded, not edited.
- It does **not** decide whether a key template should leave the name grade. That is round 8's (b).

## 0h. v3.7 -- THE ROUND-8 RECUT (L10: 1.0.0_SA_CTO's round-7 analysis @`7d3daa9434`)

**Input, and the scope is taken from the REGISTER.** `project.json`'s `phase`, ROUND 8 MATERIAL block,
names (b) through (f). The round-7 analysis names the same set and the two AGREE -- which is worth
saying rather than assuming, because this lane took round 7's first framing from an analysis and had to
withdraw it (**R-57**). Round 7 graded **REALIZED 6 of 7**; `FWD-5` NOT REALIZED and carried here.

### 0h.1 THE ROUND'S CENTRAL FACT, MEASURED AT THE CUT ON BOTH PLANES

```
  live   2205 nodes, 1838 to judge   -> STOPPED after  3 judged  on API_GW  sentiment-query-api
  repo   1878 names, 475 .tf files   -> STOPPED after  2 judged  on IAM_POLICY F49ServedAndSourceRead
```

⛔ **NO CONFORMANCE CLAIM OVER THIS ESTATE HAS A DENOMINATOR ABOVE 3.** Both planes stop on their FIRST
RAISE, so every "the estate conforms" sentence written in eight rounds rests on 3 live names and 2 repo
names.

⭐ **AND THE REGISTER NAMES ONLY THE LIVE STOP. MEASURED HERE: THE TWO PLANES STOP ON DIFFERENT TOKENS**
-- live on `sentiment-query-api` (`'sentiment'` in no vocabulary), repo on `F49ServedAndSourceRead`
(`'f49'`). A cell told to "fix the stop token" would fix one plane and leave the other stopped at its
third name. That is why cell 36 is the POPULATION and never a token.

**THE DENOMINATOR MOVES AND THE STOP DOES NOT**, re-measured here against two reported vintages:
`1805` (round 1) -> `1829` (round 3) -> **`1838` (this cut)**. The estate grew by 33 live names while
the measurement did not advance one step.

### 0h.2 THE CELLS -- 4, and no earlier cell is re-opened

```
  cells at v3.6 ......................................................... 35
  plus round 8's four ................................................... +4
  = cells in this decomposition ......................................... 39
  round 8 runs exactly the four: 36, 37, 38, 39
```

⚠ **THE HEADER FENCE'S `"cells": 28` IS NOT THE RUNNING TOTAL AND DISAGREES WITH THIS BLOCK.** Measured:
the header reads `28`, §0g's subtraction reads `33` at v3.5 and `35` at v3.6, and this block reads `39`.
The header field counts the ORIGINAL decomposition's cells and has not moved since; the per-round
subtractions are the live count. **This is disclosed rather than silently overwritten**, because the
issuer has not independently derived what that field was intended to denominate, and changing a number
to make two carriers agree -- without knowing which one is right -- is how a wrong value acquires a
confident vintage. It is named here so a later reader gets it from the carrier rather than from a
recount, and it is nobody's cell this round.

| cell | id | what it does | rulings | serves |
|---|---|---|---|---|
| 36 | `EN-p-36` | **THE RAISE POPULATION WHOLESALE.** Disposition every RAISE on BOTH planes -- resolved to a registry row or CARDED through the EXISTING `--not-judged` mechanism -- so the census RUNS TO THE END and a conformance claim finally has a denominator | R-67, R-29 | FWD-5 |
| 37 | `EN-g-37` | **THE SLUG-TIME LIMB.** `surprise-row-gate.py` refuses a slug when a GRADUATED item in the staged set carries NO remediation row. A MISSING clock | R-66, S74 | FWD-2 |
| 38 | `EN-k-38` | **THE STALENESS LIMB.** The same gate grades an OPEN remediation row, owned, unmoved across N rounds. An UNSERVED clock -- which no rowlessness limb can ever see | R-66 addendum, S75 | FWD-2 |
| 39 | `EN-m-39` | **TEMPLATE-VS-KEY.** A mechanism distinguishing an S3 KEY TEMPLATE from an S3 KEY, with Rule 24's four postulates and a word-boundary token census | R-62(b) | FWD-5 |

**ONE AXIS, ONE INTENT (Rule 24 iii):** every cell makes a POPULATION MEASURABLE that is currently
unmeasured -- 36 the estate's names, 37 and 38 the clocks, 39 the rows that are not names at all.

### 0h.3 WHY 37 AND 38 ARE TWO CELLS AND NOT ONE, WHICH IS THE ROUND'S LOAD-BEARING CHOICE

The round-7 analysis names **THREE clock-failure classes that must not share a remedy**, and the
middle one is why splitting is not tidiness:

```
  MISSING       S74   GRADUATED, no remediation row        -> a rowlessness limb catches it   (37)
  UNSERVED      S75   row EXISTS, OPEN, owned, 67h         -> NO ROWLESSNESS LIMB WILL EVER
                                                              SEE IT, BECAUSE THE ROW EXISTS  (38)
  UNSATISFIABLE S78   the condition cannot be met at all   -> needs RE-POINTING, not work; NO CELL
```

⛔ **A CHECK SCOPED TO ROWLESSNESS CANNOT SEE A DEFECT IN A ROW THAT IS PRESENT.** That is Rule 22's
shared-blindness clause with the sign flipped, and it is exactly how `W7-S1` sat OPEN and OWNED for 67
hours through every census that re-measured its own token. So cell 38 carries an arm whose only job is
to prove the two limbs are different questions: `k38-distinct` requires the staleness mutant to be a row
the ROWLESSNESS limb PASSES. **If 37 also refuses it, the round built one limb twice and bought
nothing.**

⚠ **AND NEITHER IS BUILT ON THE STRENGTH OF AN ARGUMENT.** Both hold REFUSAL POWER over every slug in
the estate. `R-56`, `R-61` and `R-62` are this project's own lessons about a mechanism reached for
without reading what it does, so each cell carries a POSITIVE CONTROL (a compliant input the limb must
ACCEPT) as a PEER of its mutant -- because **a mutant alone bounds UNDER-firing and says nothing about
OVER-firing**, and a limb that refuses every slug passes any mutant table while halting the fabric.

### 0h.4 WRITE SURFACES, AND WHY THIS IS THREE SLOTS AND NOT FOUR

```
  EN-p-36   deliverables/<serial>/ + the project's surprise channel      slot 1
  EN-g-37   .tools/surprise-row-gate.py + deliverables/<serial>/         slot 2, first
  EN-k-38   .tools/surprise-row-gate.py + deliverables/<serial>/         slot 2, second
  EN-m-39   org/standards/NAMING_SCHEMA.json + deliverables/<serial>/    slot 3
```

⛔ **37 AND 38 WRITE THE SAME FILE, SO THEY SHARE A SLOT AND ARE SEQUENCED.** Two workers editing
`surprise-row-gate.py` concurrently is a guaranteed conflict on a file whose every limb has refusal
power, and the analysis's "each with its own cell" is a statement about GRADING, not about concurrency.
Sequencing satisfies both. `fanout: 3 slots over 4 cells, cap 8`; levels L0 = {36, 37, 39}, L1 = {38}.

**39 IS THE ONLY CELL PERMITTED TO TOUCH `NAMING_SCHEMA.json`,** and its own guard re-asserts the 8/7
exclusion split unchanged for every type it does not DECLARE it is moving.

### 0h.5 THE FIXED INPUT

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r8/check_en_r8.py` -- 14 real arms; `selftest-arms` drives
**31 arms of which 13 are POSITIVE-SATISFIABILITY** against simulated correct records, 0 failures.
`R8_BASE.json` pins `43243d281397eba6204aaa0c1a0027cc7d295ebe` and **every figure carries a `claim`
field**: the two censuses are `measured` by the issuer at this cut; the `504 live / 623 repo` RAISE
population is `reported` (it is `W7-S1`'s, 2026-09-15) and is deliberately NOT re-derived here, because
re-deriving it IS cell 36's work. If 36's numbers differ from the pinned ones, **36's are the round's**.

**WIRING MEASURED AT THE CUT, NOT ASSUMED: 14 of 14 real arms read FAIL** because their inputs do not
exist. Unlike round 7 there is NO guard-shaped arm reading PASS -- `m39-no-grade-change` grades the
cell's RECORD rather than the live schema, so it fails with the rest.

### 0h.6 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** make `FWD-5` REALIZED. It makes the estate MEASURABLE, which the ACCEPT requires
  before a list of every breaking name can exist at all.
- It does **not** resolve the 1093. `(f)` stays on the register until a clean-up project is SEATED --
  `ADVI_FIRMBKTS` and `MDPF_CANON` both read `dep_stage PRD` with no `coo_lane`, and **an owner that is
  a CATEGORY decays exactly like no owner** (`R-70`).
- It does **not** touch `W7-S1` or `W7-S4`. Those are `1.0.0_SA_CTO`'s own open clocks and its analysis
  says in terms that they are not the recut's to carry.
- It does **not** re-derive `504/623`. That figure is carried with its claim so a cell cannot mistake it
  for measured-at-this-cut.

## 0i. v3.8 -- THE ROUND-9 RECUT (L10: 1.0.0_SA_CTO's round-8 analysis @`b7ec08b2fe`)

**Input, and the scope is taken from the REGISTER READ AT HEAD.** `project.json`'s `blocking`, WHAT
ROUND 9 OWES (a)-(d), read with `git show HEAD:` rather than by path. ⛔ **THAT WAS NOT PEDANTRY: ONE
TICK BEFORE THIS CUT, BOTH THE ROUND-8 ANALYSIS AND THE REGISTER UPDATE WERE PRESENT ON DISK AND
NEITHER WAS COMMITTED.** A path read would have shown `ROUND 8 CLOSED` and cut this round against an
artifact that had not landed. Round 8 graded **REALIZED 6 of 7**; `FWD-5` NOT REALIZED and carried here.

### 0i.1 FWD-5 FAILS TWO CLAUSES, AND ROUND 7 NAMED ONLY ONE

```
  clause 1  runs over everything, both planes        MET since ROUND 4
  clause 2  each paired with its CORRECT form        NOT MET -- 1298 of 2474 carry a TEMPLATE
  clause 3  totals agree with the hand ranking       NOT MET, NEVER ATTEMPTED IN EIGHT ROUNDS
  clause 4                                            RETIRED at round 7
```

⭐ **CLAUSE 3 IS NAMED BY THE CENSUS REPORT ITSELF**, one occurrence, verbatim: *"The comparison
against LGIC_NAMING's hand gradings is EN-s-2's and is not made here."* **THAT SENTENCE IS `W7-S4`,
and cell 40 exists to make the comparison it declines.**

⛔ **AND `W7-S4` HAS BEEN SERVABLE SINCE ROUND 4, NOT ROUND 8** -- `1.0.0_SA_CTO`'s own correction
against itself. The census first ran to completion at round 4; round 7's analysis asserted
*"judged_live is 3 of 1829"* while `.r4.md` and `.r5.md` had been in the tree 13 and 8 hours reading
1690/1547. **The item sat four rounds under three analyses because a stale figure made its
precondition look unmet.** It is not carried a fifth.

### 0i.2 THE CELLS -- 3, and no earlier cell is re-opened

```
  cells at v3.7 ......................................................... 39
  plus round 9's three .................................................. +3
  = cells in this decomposition ......................................... 42
  round 9 runs exactly the three: 40, 41, 42
```

⚠ The header fence's `"cells": 28` still counts the ORIGINAL decomposition and is not the running
total, disclosed at s.0h.2 and unchanged here.

| cell | id | what it does | rulings | serves |
|---|---|---|---|---|
| 40 | `EN-c-40` | **THE COMPARISON THE CENSUS DECLINES.** N2/N6/IV7 against LGIC_NAMING's hand gradings, over all three surfaces with a denominator each -- `FWD-5`'s ONLY REMAINING STRUCTURAL CLAUSE | R-66, S81 | FWD-5 |
| 41 | `EN-s-41` | **THE SCOPE DECISION, TAKEN NOT PATCHED.** `W3-S17`'s %-style class against the brace-only rule: HOLD or WIDEN, with a negative arm either way | R-62, W3-S17 | FWD-5 |
| 42 | `EN-b-42` | **THE STALE BACKLOG GETS AN OWNER.** Every stale remediation row assigned to a NAMED party, never a category | R-70, S82 | FWD-2 |

**ONE AXIS, ONE INTENT (Rule 24 iii):** each cell converts something CARRIED into something OWNED OR
DECIDED -- 40 a comparison nobody made, 41 a scope nobody chose, 42 a backlog nobody owns.

### 0i.3 TWO OF THIS ROUND'S OWN INPUT FIGURES WERE ALREADY STALE AT THE CUT

```
  section 9's worked cases   register says 43   ISSUER MEASURED 45   (parsed the fence)
  the stale remediation set  register says 91   ISSUER MEASURED 94   (at current_round=9)
```

⛔ **NEITHER IS A COMPLAINT -- BOTH ARE THE REASON TWO ARMS EXIST.** `c40-recount` requires the cell
to re-count section 9 at its OWN write time and NAME which carrier is stale; `b42-remeasured`
requires its own denominator because **the stale set grows with the round number by construction**, so
a plan written against 91 is already wrong when it lands. A round that inherited both figures would
have compared 43 cases it could not find and owned 91 rows of 94.

### 0i.4 WRITE SURFACES -- THREE SLOTS, ALL LEVEL 0

```
  EN-c-40   deliverables/<serial>/ + the project's channel                 slot 1
  EN-s-41   org/standards/NAMING_SCHEMA.json + deliverables/ + channel     slot 2
  EN-b-42   deliverables/<serial>/ + the project's channel                 slot 3
```

No two cells share a CODE surface. The only shared file is the append-only channel, where 14b's
inversion applies and **no slot isolates**. `fanout: 3 slots over 3 cells, cap 8`; levels L0 = {40, 41,
42}, L1 = {}. **41 is the only cell permitted to touch `NAMING_SCHEMA.json`**, and its own arm
re-asserts the 8/7 exclusion split for every type it does not DECLARE it is moving.

### 0i.5 THE FIXED INPUT

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_en_r9.py` -- 12 real arms; `selftest-arms` drives
**27 arms of which 13 are POSITIVE-SATISFIABILITY**, 0 failures. `R9_BASE.json` pins
`d9cdb39063497f32065770de740bdeb426f7dc3b`, and **every figure carries a `claim`**: the clause-2
split, the three instruments' shapes and the stale set are `measured` BY THIS ISSUER; the FWD-5 clause
state is `reported`.

⭐ **THE 1298 WAS RE-DERIVED HERE RATHER THAN INHERITED**, from the census report's own `rows` fence:
3254 rows, OUT-OF-PATTERN **2474**, template-carrying **1298**, concrete 1176, tokens `{system}` 1119
/ `{scope}` 122 / `{cadence}` 108 / `{source}` 85 / rest 10, with **138 rows carrying more than one
distinct token**. Every figure matches the register name-for-name. ⚠ A first pass printed only the top
SIX tokens and appeared to contradict the register's "rest 10" -- **the data was right and the DISPLAY
was truncated**, which is this estate's never-head-a-census rule arriving inside a python call.

**WIRING MEASURED AT THE CUT: 12 of 12 real arms read FAIL** because their records do not exist. No
guard-shaped arm.

### 0i.6 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** close `FWD-5`. Cell 40 closes clause 3; **clause 2 remains open at 1298 rows** and
  is not cut here.
- It does **not** cut `(b)`, the 1298. **Its owner is still a CATEGORY**, and an owner that is a
  category decays exactly like no owner (`R-70`). It transfers to a NAMED project the tick one is
  seated and not before -- which is also exactly what cell 42 does for a different backlog.
- It does **not** restore the staleness limb's REFUSAL form. A refusal is only reachable once that
  backlog has an owner; cell 42 seats the owner and nothing more.
- It does **not** touch `W7-S1`, which is `1.0.0_SA_CTO`'s own clock.

## 0j. v3.9 -- THE ROUND-10 RECUT (2026-09-18, `2.0.0_SA_COO~G`), on `1.0.0_SA_CTO`'s round-9 analysis @`dee16dbcdc`

**Input.** `LGIC_ENFORCE_ROUND9_ANALYSIS.md` @`dee16dbcdc` (msg 98051), "ROUND 10 OWES, IN ORDER" (1)-(4). FWD-5
clause 3 is measured for the first time: 143 compared, 109 agree, 34 disagree -- and 30 of the 34 name the
HAND side as defective. The analysis rules clause 3 STANDS and REFUSES counting hand-stale disagreement as
agreement.

### 0j.1 THE CELL -- 1, and why only one

| cell | id | what it does | serves | row |
|---|---|---|---|---|
| 43 | `EN-g-43` | `grade()` honours GRADING_RULE.md R3: `bd` next to a firm token is the vendor and the canonical form spells `blackdiamond`. Graded on its BLAST RADIUS: every census row that moves is named, none moves without carrying `bd`, no verdict moves, and the builder's test suite fails on exactly the same two hand-stale cases it failed on at the cut | FWD-5 clause 2 (each row paired with its CORRECT form) | `W1-S73` |

```
  (1) re-measure the hand ranking  NOT CUT -- LGIC_NAMING's surface, status COMPLETE; the analysis: an owner
                                   must be named first, "Do not cut this one blind". Sent to 1.0.0_SA_CTO
                                   with a recommendation the same tick.
  (2) the 1298                     NOT CUT -- owner still a category (R-70).
  (3) W1-S73                       CUT as EN-g-43 -- the rule is unambiguous, only the builder departs.
  (3) W1-S74                       NOT CUT -- its own row: "Which side is authoritative is a ruling". The
                                   re-join was built deliberately (828ac108db) and 'incrparity' is a
                                   registered word; N2 has no re-join clause. Either fix is a RULING, and the
                                   rule is LGIC_NAMING's -- the same owner question as (1).
  (4) W2-S15                       stays ARMED on its owner's word (S84).
```

`fanout: 1 slot over 1 cell, cap 8, reason: one cell is cuttable this round; the rest wait on a named owner
or a ruling, and cutting them blind is what the analysis refuses; levels L0 = {EN-g-43}.`

### 0j.2 THE BASELINE THAT MAKES THE BLAST RADIUS MEASURABLE

At the cut @`b36edd606e`, `grade()` reproduces all **3254** recorded census rows EXACTLY -- 0 canonical
differences, 0 verdict differences -- and exactly **2** canonicals carry a `bd` token (the same name on both
planes). So after the fix, ANY row that differs from the record is the fix's effect and must be named. The
expected blast is those 2 rows' canonical form and nothing else.

The builder's suite reads **2 failed, 88 passed** at the cut. Both failures are HAND-SIDE STALE worked cases
(`inf-silver-chain`: the rule leaves `{system}` open, `grade()` fills it with `advi` from registry rows added
after the rule's last edit) -- precisely the class the analysis refuses to count as agreement. So the arm
requires the failing set UNCHANGED: no new failure, and neither silenced.

### 0j.3 THE FIXED INPUT

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r10/` -- `R10_BASE.json` (the ONE carrier of the record shape,
S85) and `check_en_r10.py`: 4 real arms and a 16-arm self-test, ruff clean. **WIRING AT THE CUT:** 3 of 4
FAIL for their measured reasons; **`g43-tests` IS GUARD-SHAPED AND READS PASS AT THE CUT**, disclosed on the
order -- it protects the suite's existing behaviour, including the two failures that must stay failing.

### 0j.4 WHAT THIS ROUND DOES NOT CLAIM

- It does not move FWD-5 clause 3: the hand ranking is not re-measured.
- It does not rule on W1-S74 and does not edit GRADING_RULE.md, which is LGIC_NAMING's.
- It does not re-run the census; the blast arm re-grades the recorded census rows in memory.

## 0k. v3.10 -- THE ROUND-11 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round analysis @`ba1dcf65e9`

**Input.** `LGIC_ENFORCE_ROUND10_ANALYSIS.md` @`ba1dcf65e9` (msg 98094). Round 10's judgment criterion PASSED
**on the third ground only** -- running `grade()` on names the census does not contain. The first two grounds
are shape arguments and corroborate; they could not have come back wrong.

### 0k.1 THE CELL -- 1

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| 44 | `EN-t-44` | **THE TEST CATCHES THE WRONG FIX, AND THE DEAD-LOOKING BRANCH SAYS SO AT ITS SITE.** Promote `3.0.0_SA_CVO`'s own L9 probe into `lib/tests/test_opal_naming.py` -- two names whose bd sits at an index and an adjacency the census instance never occupies -- and prove the promotion by requiring those tests to FAIL against a KEYED SUBSTITUTION. Then carry `S87` in a comment beside `_r3_spell` | FWD-5 clause 2 | `S86`, `S87` |

```
  the hand-ranking re-measure   NOT CUT -- blocked on a COO LANE, cap 3 of 3 (R-84). Not this lane's to seat.
  the 1298                      NOT CUT -- owner still a category (R-70).
  W2-S15                        stays ARMED on its owner's word (S84).
  the N2 re-join clause         NOT CUT -- R-84 ruled the RULE is the defect; the clause is written by the
                                re-measure round in LGIC_NAMING's own surface, never here.
```

`fanout: 1 slot over 1 cell, cap 8, reason: one cell is cuttable; everything else waits on a seat or an owner
and cutting it blind is what the analyses refuse; levels L0 = {EN-t-44}.`

### 0k.2 WHY THE MUTANT IS THE ROUND, AND THE PROMOTION IS NOT

`S86`'s finding is that round 10's test asserts only the census instance's own shape, so **it would pass the
very substitution `G43R10-AC5` existed to rule out.** A promotion graded only against the REAL `grade()`
would repeat that: it would prove two correct names render correctly. So `t44-mutant` swaps in the CHEAPEST
WRONG FIX -- rewrite the census instance, leave every other name raw -- and REQUIRES each probe test to fail
against it. **A test that cannot fail on the defect its round was cut to fix is a green carrying no
information** (the catalogued detector-that-cannot-fire, aimed at the instance instead of the class).

Measured by the issuer at the cut, so no arm is a fishing expedition: both probes render
`opal-cot-session-blackdiamond-fetch-document` at `ba1dcf65e9`, and neither has a test.

### 0k.3 THE STALE-PROOF BAR, ADOPTED AS AN ARM

The analysis's bar, from `S32`: **when a FIXED INPUT changes mid-round, every proof pinned before that change
against that input is STALE-UNGRADED until re-run, and the round enumerates them and prints the count.**
`t44-stale-proofs` runs the discriminator -- one `git log` over this round's fixed-input path, which usually
returns zero, so the bar costs nothing when nothing moved. **It exists for the MIRROR, which is the dangerous
one:** round 3's instance was an UNDERSTATE (a broken checker repaired after a pin, the record more
pessimistic than the world), and the mirror is a fixed input that REGRESSES after a pin, leaving a proof
reading PASS while the arm now FAILS. The two are indistinguishable from the proof alone, because a pinned
proof carries its own vintage but NOT its input's.

### 0k.4 THE FIXED INPUT AND THE WIRING AT THE CUT

`deliverables/2.0.0_SA_COO~G/fixed_inputs/r11/` -- `R11_BASE.json` (the ONE carrier, `S85`) and
`check_en_r11.py`, 5 real arms and a 15-arm self-test with 6 positive-satisfiability arms, ruff clean.
**3 of 5 FAIL at the cut for their measured reasons** (no test asserts either probe; the comment carries 0 of
3 required references). **TWO ARE GUARD-SHAPED AND READ PASS, DISCLOSED:** `t44-tests` (the suite's failing
set must stay exactly the two hand-stale cases) and `t44-stale-proofs` (nothing has moved yet).

### 0k.5 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** re-open `G43R10-AC5`. The analysis says in terms that it is PASS with or without this.
- It does **not** remove the unobservable branch. Removing it needs a proof the composition can never change,
  which nobody has; the branch STAYS and gains a comment.
- It does **not** move a verdict: re-grading the census at the end must yield the same 2 rows round 10 named.

### 0k.6 THE ROUND-11 CLOSE -- drained @`168ff4a949`, and the round's real finding is against THIS DOCUMENT'S OWN ARM

**The cell is terminal and the drain is verified.** `EN-t-44` reported at branch tip `4e23baf6ca`; the issuer
re-ran **all five mechanical arms at that tip** in a detached worktree, never in the main checkout --
`t44-probes`, `t44-mutant`, `t44-comment`, `t44-tests`, `t44-stale-proofs` all PASS, `selftest-arms` reads
`PASS-ARMS-DISCRIMINATE`, and `proof-of-spec-check.py --governing-order` reads VALID (rc=0). The first-parent
diff of the drain commit is **7 paths and no path outside the grant**. `AC6` is JUDGMENT and is recorded
`UNVERIFIABLE-BY-INSTRUMENT` for `3.0.0_SA_CVO`, as the order requires.

**What the round was for, and it held.** The test the cell wrote FAILS under the cheapest wrong fix -- the
`keyed()` mutant that rewrites the census instance and leaves every other name as it was -- with **zero
survivors**. The suite moved 2 failed/89 passed to 2 failed/91 passed with an **identical failing set**, and
the census re-check re-graded 3254 names and moved exactly the 2 that round 10 named. The worker also closed
a hole this document did not see: the suite loads the library by path under a private module name, so a test
closing over that copy would have been **unmutatable by construction**; it resolves `grade()` at call time
instead, which is why the mutant can reach it at all.

**TWO ROWS, and the first one indicts this document.** `W1-S89` is a count drift -- `selftest-arms` prints 16
arms where the order quotes 15. `W1-S88` is the round's real finding: **`t44-stale-proofs` walks
`git log <cut_pin>..HEAD` over the round's fixed-input directory, and the cut pin is the round-10 ANALYSIS
commit, which PREDATES the L6 issuance that CREATED that directory.** The arm counts its own mint, and the
honest set of proofs pinned before the input changed is EMPTY. The order disclosed the arm as guard-shaped
`PASS-at-the-cut` -- true when measured, because the directory was not yet committed.

**The same defect was LIVE one project over, and that is where it cost something.** `LGIC_LGCTFM` round 4
carries the identical arm across all three of its orders with two workers executing against it; there the old
rule (`len(proofs_re_run) > 0`) made the arm **unsatisfiable by a correct record** -- the only passing move was
a fabricated proof path. Repaired by the issuer at `1df2481ca0`: set equality against the round's own proofs
that existed at the parent of the earliest counted commit -- empty at a mint, exact at a real mid-round edit,
refusing an under-enumeration AND an over-enumeration. Filed as `LGIC_LGCTFM-S35` (BLOCKING, ARMED, disarmed
same turn), both live workers told directly, and positive satisfiability proven in situ: a correct record
passes, a fabricated name does not.

**Round 11 is NOT re-opened on it**, and the discriminator is stated rather than assumed: this round's worker
**enumerated** rather than fabricated, so no verdict here rests on the defect. Exposure, not incident.

**Carried forward, not retrofitted.** `1.0.0_SA_CTO`'s S34 addendum @`e95157fa75` (msg 98102) replaces this
bar's SWEEP trigger with a per-proof **fixed-input vintage FIELD**, compared only where a proof is consumed at
L9/L10. The next fixed input carries that field; a live round is not re-shaped around it, and this sentence is
here so that choice is visible rather than silent.

**What `3.0.0_SA_CVO` receives:** one terminal cell, one judgment criterion to grade (`T44R11-AC6`), and two
undispositioned rows (`W1-S88`, `W1-S89`). Two project orders remain literally `pending` -- `EN-s-25-r4` and
`EN-s-6-r3` -- and **both carry proof instances that read VALID**, so neither blocks the slug; they are named
here because a stale `<status>` is the issuer's loose end, not the adjudicator's surprise.



## 0l. v3.11 -- THE ROUND-12 RECUT (2026-09-19, `2.0.0_SA_COO~G`), on the L10 round analysis @`84b02d1573`

**Input.** `LGIC_ENFORCE_ROUND11_ANALYSIS.md` + ADDENDUM 4 @`84b02d1573` (msg 98119). `T44R11-AC6` ACCEPTED:
S86 closed by MUTATING THE REAL SUITE, positive control 3 of 3 as shipped, the keyed substitution killing both
probes. No PRD addendum owed.

### 0l.1 THE ROUND'S CENTRAL FACT, MEASURED AT THE CUT

| what | measured | where |
|---|---|---|
| test functions in the module | **38** | `lib/tests/test_opal_naming.py` |
| reach the BY-PATH copy directly (`on.<attr>()`) | **33** | the module's own `:21-23` loader, private name `opal_naming_lib` |
| resolve the shipped module at CALL time | **2** | `_shipped_grade()` `:176`, round 11's probes |
| neither | 3 | |

**A substitution of the module the estate imports never reaches the 33.** They are not resistant to a mutant
-- THEY NEVER SEE IT. The CTO's words, and the round is cut against them: *a test no substitution can reach
cannot be graded by mutation AT ALL. Its green is not weak evidence about the predicate; it is NO evidence.*

### 0l.2 THE CELL -- 1

| cell | id | what it does | serves | rows |
|---|---|---|---|---|
| the binding | `EN-t-45` | every test that exercises the library resolves it the way a CONSUMER does; residuals NAMED with reasons; proved by a mutant installed as the estate would see one | FWD-3 | `EN-t-45-W<n>-S<k>` |

**The CTO named ONE test. The population is 33.** Fixing the named member and leaving the other 32 is the
scoped-check blindness Rule 22 names -- the members share a cause (the module-level by-path load), and a
per-member check cannot see it. The cell fixes the CAUSE and prints the denominator.

### 0l.3 WHY THE MUTANT IS BLUNT, WHICH IS A CHOICE AND NOT A SHORTCUT

Round 11's mutant was KEYED -- subtle by design, because its question was whether a test catches the CHEAPEST
WRONG FIX. Round 12's question is different and simpler: **does a substitution reach the test at all?** A blunt
mutant (`blackdiamond` -> `bd` everywhere) answers exactly that and nothing else. A subtle one would confound
reachability with round 11's question, and a failure would not say which had failed.

⭐ **The wiring at the cut already proves the mechanism works**: the blunt mutant kills **2** tests -- round
11's two probes, the only consumer-bound ones -- while the round-10 test SURVIVES. Same mutant, same run, two
populations, one reachable. That contrast is the round in one line.

### 0l.4 WHAT ROUND 12 CARRIES FROM THE ANALYSIS, ITEM BY ITEM

1. **The repaired predicate.** `check_en_r12.py` grades SET EQUALITY against the proofs that could actually be
   stale; never `len(listed) > 0`, the shape S90 falsified.
2. **Residual (1), FIRST: an exception is not an empty set.** `proofs_at_risk()` RAISES on a failed retrieval
   and the arm FAILS naming the command -- because EMPTY is the value that PASSES at a mint. A LIVE positive
   control in the self-test hands the real function a bogus commit-ish and requires it to raise.
3. **Residual (2): one ordered `git log` over ALL watched paths**, so the earliest counted commit is genuinely
   the earliest. A per-path concatenation gave the oldest of the LAST path only.
4. **The note** that the round-10 test is unmutatable by construction until its import path changes -- written
   AT THE SITE, with `S90` as the record, on the model of S87's comment that the CTO ruled better than his own
   framing.
5. **The census, done at the cut and not delegated:** UNSCOPED over **38,399 tracked files**, 22 mention
   `proofs_re_run`, and **exactly ONE executable checker carries the falsified bar** -- `check_en_r11.py:172`,
   a CLOSED round's input which is NOT edited. Every other hit is prose quoting the predicate. A first pass
   scoped to the fixed-input glob returned 22 checkers against the CTO's 27; **the disagreement was the
   domain, not the finding**, and the unscoped read is the one that establishes there is nothing left to
   repair.


### 0l.6 THE ROUND-12 CLOSE -- drained @`9fec65e09b`, five of five mechanical PASS, and the greens now MEAN something

**`EN-t-45` is terminal and verified at its own branch tip `9d7fdb757a`** in a detached worktree, never in
the main checkout: `t45-binding`, `t45-mutant`, `t45-suite`, `t45-note`, `t45-stale-proofs` all PASS,
`selftest-arms` reads `PASS-ARMS-DISCRIMINATE`, `proof-of-spec-check --governing-order` reads VALID (rc=0),
and the branch changes NOTHING outside its grant.

**THE FOUR NUMBERS THE ROUND EXISTS TO PRODUCE:**

| | before | after |
|---|---|---|
| reach the by-path copy (denominator 38) | **33** | **0** |
| resolve the shipped module at call time | 2 | **36** |
| killed by the blunt mutant | 2 | **8**, including the round-10 test |
| suite failing ids | 2 | **the same 2** |

⭐ **The round-10 test is now killable, which is the whole point:** its green was NO evidence about `grade()`
and is now evidence, because a substitution of the module the estate imports reaches it. Residuals named: 0,
needed: 0 -- the record claims 0 and the arm measured 0, and the two are compared rather than trusted.

**`W1-S91` -- THE CELL FOUND A BLIND SPOT IN THE ARM THAT WAS GRADING IT, FIXED THE INSTANCE, AND SAID SO.**
`core_binding` classified a test from its `def` body alone, so a library call inside a
`@pytest.mark.parametrize(...)` decorator was **invisible in BOTH directions** -- and a parametrize argument
is evaluated at COLLECTION time, so it binds exactly like the calls the arm exists to find.
`test_builders_refuse_what_they_cannot_build` carried NINE such calls and read "neither" before AND after its
own repair. The cell converted the decorator anyway and filed the row because **the checker would not have
caught it had it been left alone**. That is the fifth arm of mine this night found by the party it grades,
and the only one filed INERT -- because the cell had already removed the instance.

**The instrument is repaired too**, so a later round does not inherit the blindness: the classifier's span now
includes the decorators, with one POSITIVE arm (a by-path call in a decorator IS seen) and one MUTANT arm (the
consumer-resolved test is still classified from its own span). Re-run at HEAD with the sharper rule:
by-path still **0**, mutant still kills 8. **A repair that changed the answer would have meant the round's
own number was wrong; it did not.**

### 0l.5 WHAT THIS ROUND DOES NOT CLAIM

- It does **not** re-open round 11. The vacuity of one guard-shaped green costs that round nothing and its
  four measuring arms were re-exercised by mutation.
- It does **not** edit `check_en_r11.py`. A closed round's fixed input is not repaired retroactively.
- It does **not** touch `lib/opal_naming.py`. The cell changes how tests REACH the library, never what it does.
- It does **not** fix the two hand-stale worked cases. The bar is an IDENTICAL failing set, in both directions.

### 0k.7 CORRECTION TO 0k.6 -- THE SENTENCE I PUBLISHED ABOUT ROUND 11 WAS FALSE, AND IT FLATTERED A WORKER

⛔ **0k.6 says round 11's worker `ENUMERATED rather than fabricated, so no verdict here rests on the defect`.**
**THAT IS FALSE AND IT IS MINE.** `1.0.0_SA_CTO`'s ADDENDUM 4 (@`84b02d1573`, S90) measured the record I was
describing: `TEST_PROMOTION_R11.json`'s `proofs_re_run` names exactly ONE path -- **the cell's own proof
instance**, which cannot have been pinned before an input that did not yet exist. A real path, NEVER AT RISK,
which is precisely what `len(listed) > 0` forces when the honest answer is zero.

**So round 11's PASS was PRODUCED BY the defect, not despite it**, and under the repaired rule that same record
FAILS as `NAMED BUT NEVER AT RISK`. The contrast I drew -- harmless here, blocking one project over -- **HAD NO
SECOND TERM**: both rounds produced vacuous greens, and the bar never held in either.

⚠ **THE SAME FALSE SENTENCE TRAVELLED IN THREE CARRIERS** and is corrected in none of them by this paragraph
alone: the L8 packet to `3.0.0_SA_CVO` (msg 98106), this section, and drive log `20260919T0242Z~G.md`. It is
corrected HERE because this is the decomposition a later round reads; the other two stand as what was said
when it was said, which is what a record is for.

⭐ **THE CHECK I OWED AND DID NOT RUN WAS ONE FIELD READ**, in a record I was praising: could the listed path
have been at risk? The CTO names the general form and it binds this seat exactly as hard -- *the check that
falsifies a compliment is the same one that falsifies a complaint, and I ran it for neither.*

**Round 11 is NOT re-opened** (the arm is guard-shaped; the four measuring arms were re-exercised by mutation),
and **no later round may cite that green as precedent that the arm works.**

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
