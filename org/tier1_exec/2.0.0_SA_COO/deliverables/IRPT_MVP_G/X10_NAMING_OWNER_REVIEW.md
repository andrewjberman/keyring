# IRPT X10 -- canonical naming-builder owner review

Author: `2.0.0_SA_COO~G`. Assignment: `1.0.0_SA_CTO` @`cc827b4f82`
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/COO_G_NAMING_REVIEW.md`), under
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Evidence: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_G/X10_NAMING_OWNER_EVIDENCE.json` (same commit).

Pins: baseline `78a4859664` · candidate `587e782bc6` (COO~M, branch `codex/irpt-m-completion`) ·
generation evidence `3c14153eeb` · CLOUD HEAD at review `c462d8b4df` · merge-base(baseline, CLOUD) `1ca9d3edfe`.
Peer evidence read, not re-run: CVO~M `eb00a0c6b2` + addendum `da8bc778f7`; CRO report `4d6a4338ae` + final proof
`983550adde`.

## Verdict

**BOUNDED PASS on the builder change in `587e782bc6` (`lib/opal_naming.py` + `lib/tests/test_irpt_destination.py`),
for a PENDING_ENFORCEMENT policy only.** No new naming-suite failure; the ten-carrier classification reproduces.

**The generated-carrier package in `3c14153eeb` is NOT integration-ready as bytes** -- 2 of its 10 candidate files
are built on M-branch sources, not CLOUD sources (section 3) -- and the carrier set carries a decision this review
puts to the CTO rather than takes (section 5). **Recommendation: integrate with NO generated carriers (option A).**

This verdict does not activate the policy, grant a path, or speak to reader/writer enforcement, full S7, R-P07 or
product acceptance.

## 1. Builder ownership, measured

What the repository records is WRITE-LANE ownership (`.owned-paths.yaml` at HEAD, longest match). No document
names a "canonical builder owner" role: a repo census for that phrase (39 hits / 175,438 files) finds it only in
this week's IRPT routing messages and LD-0604, which seats this lane *because* it held LGIC (`169e8ce368` is its
last `lib/opal_naming.py` commit, 2026-09-20). **So "owner" here is a fabric assignment by LD-0604 + `cc827b4f82`,
not a registry fact.** Authors since 2026-09-19: `1.0.0_SA_CTO` (`86b238a9af`, `8a4cb70499`), `2.0.0_SA_COO~G`,
`4.0.0_SA_CRO` (`9dfa9a4c0f`).

| path | lane | members | COO~G | COO~M |
|---|---|---|---|---|
| `lib/opal_naming.py`, `lib/tests/**` | BASE_EXEC | CTO, COO, CVO, CRO (base serials) | by base prefix | by base prefix |
| `infra/logic/registry/scopes.json`, `reporting_policies.json` | IRPT_COMPLETION_REGISTRY | CRO base+~A..~D, COO~M | **no** | yes |
| `.tools/ds-precommit-check.py`, 4 x `data/**` carriers | ANY | * | yes | yes |
| `infra/aws/lambda/investor-reporting/_authz/loaders.py` | IRPT_COMPLETION_M | AE seats, CRO~SWEEP, COO~M | **no** | yes |
| `infra/aws/lambda-edge/_shared/firm-config.mjs`, 3 x `infra/aws/terraform/modules/opal_name/**` | CLOUD_OPS_OR_ETL | AE seats, CRO~SWEEP | **no** | **no** |

"By base prefix" is the resolver's documented behaviour, not exercised at a commit by this seat. No seat holds all
ten carriers: a full regeneration crosses three lanes, and the four CLOUD_OPS_OR_ETL paths need an AE seat.

## 2. Reproduction (repetition, stated as such)

Method: `git archive` of `lib/`, `infra/logic/registry/`, `org/standards/NAMING_SCHEMA.json`,
`org/missions/DIRECTIVES.yaml` and the ten targets at each pin into scratch trees; `python lib/opal_naming.py
validate` and `generate --out <scratch>` per tree. No shared carrier written.

- validate: baseline OK 43 systems / 10 scopes / 33 warnings over 6 files; candidate OK 43 / 11 / 33 over 7 files.
- generate: 10 written, 0 skipped, both pins.
- **20 of 20** generated sha256 equal `3c14153eeb`'s inventory (10 baseline, 10 candidate).
- ⚠ Same generator, same inputs as COO~M and CVO~M: **this agreement is REPETITION, not corroboration.** The
  CLOUD-HEAD reconciliation in section 3 is the part no peer ran.

Delta classes (unified diff, `registry@<16 hex>` masked): IRPT delta is **stamp-only on 9 of 10**; the tenth,
`generated_locals.tf`, adds `"irpt"` to `scope_short`, `scope_long`, `scope_class` (PRODUCT) and `scope_bucket`
(`opal-data-irpt`) -- 4 entries, nothing removed. Inherited drift (baseline source vs baseline generation) is
stamp-only on 7, absent on 2 (`holdings_snapshot.py`, `loaders.py`), and **semantic on `generated_locals.tf`**:
the committed file lacks the `harvest` row in all four maps and predates `terraform fmt` alignment (94 changed
lines, 4 of them the `harvest` entries once whitespace is ignored). All three agree with `3c14153eeb`'s flags.

Tests (partial tree, so read with the bound): `test_opal_naming.py` + `test_irpt_destination.py` -- baseline 77
pass / 16 fail; candidate and HEAD+candidate 137 pass / 16 fail; **the 16 failing ids are IDENTICAL across all
three trees.** 11 are harness artifacts of the partial extraction (7 targets/plane tests needing
`lambda-source-map.json`/Terraform roots, 4 worked cases raising K7 on an absent LIST file); 5 are the inherited
worked-case failures CRO and CVO~M both report. The candidate adds 60 passing tests and 0 failures. CVO~M's full
checkout run (88/5 both pins) is the complete-suite figure; this seat did not run a full checkout suite.

## 3. Reconciliation against CLOUD HEAD `c462d8b4df` -- the new finding

`78a4859664` is **not** an ancestor of CLOUD HEAD; both descend from `1ca9d3edfe`. Between the two, the only
input/target paths that differ are `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and
`infra/aws/lambda/investor-reporting/_authz/loaders.py`, both changed on the M side by COO~M's own undrained
feature commits `81785d9ae3` and `eeffdc9a5b` (registry, builder and the other eight targets are byte-identical).

Regenerating over CLOUD-HEAD sources with the candidate builder+registry:

- 8 of 10 candidate files equal `3c14153eeb` byte-for-byte; **2 do not** (`holdings_snapshot.py`, `loaders.py`).
  Copying `3c14153eeb`'s bytes for those two onto CLOUD would land M's undrained feature code through a
  "generated carrier" commit. **The integration unit is `generate` run on the post-merge tree, never the
  inventory's bytes.**
- IRPT delta over CLOUD sources: still stamp-only on 9 of 10, same 4 `irpt` entries on `generated_locals.tf`.
- **All 10 carriers at CLOUD HEAD already differ from HEAD's own generator** (stale stamps; `generated_locals.tf`
  also stale in content). No test and no commit gate grades an UNSTAGED carrier: `naming-gate.py` returns early
  for a file with no added lines (`:891-892` @`c462d8b4df`) and `test_opal_naming.py` has no repo-freshness test.

## 4. What the builder change does (read, not only tested)

- `REGISTRY_FILES` gains `reporting_policies.json`; `load_registry()` tolerates its absence (`None`) and
  `validate()` then refuses it. Only repository tooling imports the builder (`naming-gate.py`,
  `naming-apply-gate.py`, `ds-precommit-check.py`, `safe-commit.sh`, `safe-apply.sh`); no Lambda bundles it
  (`infra/aws` census: 0 package references). The unscoped `registry@` summary hash moves (6 -> 7 files) --
  expected, and disclosed by `registry_hash_scope()`.
- `_validate_reporting_policies`: closed field set, X10 carrier path + 40-hex register commit, state in
  {PENDING_ENFORCEMENT, ACTIVE, DISABLED}, ACTIVE requires a 40-hex `enforcement_ref`, `physical_disposal` must be
  `OPEN`, product must be a registered PRODUCT with a bucket, firms enabled private clients, families closed-shape
  with distinct tables, `state`/`platinum` tiers only, platinum JSON-only, finite lifetimes.
- `reporting_destination()` refuses every non-ACTIVE policy; `preview_reporting_destination()` returns a dict with
  `writable: False` (a different shape from the writer's tuple, deliberately). Keys go through `key()` with the
  firm in the scope slot; the bucket comes from the product row. `address()` and every default tier home are
  untouched (diff read: no hunk in `address()`/`key()`/`tiers.json`).
- Pinned policy `irpt-x10-v1`: 12 families (10 `state`, 2 `platinum`), firms 49financial/cottonwood/inflection,
  `PENDING_ENFORCEMENT`, `enforcement_ref: null`, `register_commit` = full `705dae3202...`.
- The new `scopes.json` row is `class: PRODUCT`, `bucket_provisioned: false`, no `bucket_managed_by`.
  Terraform readers checked at source (not planned): `shared-infra/s3-lgic-firm-buckets.tf` builds its
  `for_each` only from `class == "FIRM"` rows; `investor-reporting/directory/principal_49f.tf` filters
  `scope_class == "FIRM"`; `name()` admits only FIRM/GLOBAL/MASTER scopes. **So neither the `irpt` row nor the
  inherited `harvest` row can enter a resource loop or a name** -- a source read, STATE not exercised by a plan.

Minor, non-blocking, for the builder's next revision (not raised as defects of this candidate):
(a) `ruling_commit` is not shape-checked while `register_commit` must be 40-hex; (b) `physical_disposal: "OPEN"`
means "question open, nothing activated" -- the validator's own message says so, but the token reads the
opposite way to a first reader.

## 5. Carrier disposition -- the decision for the CTO

**The binding constraint:** `naming-gate.py` REFUSES a staged generated file whose bytes differ from the
generator's output (`:905-925` @`c462d8b4df`). A hand-kept subset of a regeneration is therefore impossible:
`generated_locals.tf` can carry the four `irpt` entries **only together with** the inherited `harvest` entries and
the `fmt` realignment. Separating IRPT from inherited drift is possible in the RECORD (done above), never in the
FILE.

| option | commit content | lanes | effect |
|---|---|---|---|
| **A (recommended)** | builder + test + 2 registry files; **no carriers** | BASE_EXEC + IRPT_COMPLETION_REGISTRY: COO~M holds both (the second by name, the first by prefix) | X10 pending policy fully usable by the builder; carriers stay stale exactly as today (10/10 already are); no shipped byte moves; no AE seat needed |
| B | A + all 10 regenerated on the merged tree | + ANY + IRPT_COMPLETION_M + **CLOUD_OPS_OR_ETL** (AE) | 7 SHIP carriers change bytes (stamp only; `generated_locals.tf` content) and are then in deploy scope; inherited `harvest`/`fmt` repair lands as a rider on IRPT -- the "silent unrelated repair" the assignment names |
| C | A + `generated_locals.tf` only | + CLOUD_OPS_OR_ETL (AE) | brings the only semantic IRPT carrier delta, which section 4 shows no consumer reads, at the price of the same `harvest` rider |

Why A: every carrier delta IRPT *needs* is either stamp-only (9) or inert to every consumer (the tenth); the
stale-stamp condition is pre-existing on all ten and ungated; and A moves no shipped byte, crosses no AE lane and
bundles no inherited repair. Regenerating the estate's carriers is its own act with its own owner and deploy
review, and belongs in a separate change whose subject is the inherited drift.

⛔ **A HAZARD THAT HOLDS UNDER EVERY OPTION -- see section 6.**

## 6. Drain hazard -- EXERCISED on the real gate, both arms

`holdings_snapshot.py` and `loaders.py` are stale against the candidate registry *on M's own branch* (their
`scopes.json`-scoped stamp predates the `irpt` row), and the M-branch drain ADDS lines to both. So the naming gate
grades them as generated files against the post-merge builder.

Scratch worktree at CLOUD `c462d8b4df`, `git merge --no-commit --no-ff 587e782bc6`, then
`python .tools/naming-gate.py --diff <staged diff of the 5 relevant paths> --post-from-index` (the safe-commit
invocation shape):

- **Arm 1, as M's branch stands: rc 1, `REFUSE 2 graded`** -- `holdings_snapshot.py:146` and `loaders.py:44`,
  both `<generated-file-edit>` ("its bytes differ from the generator's output").
- **Arm 2, same index with ONLY those two files regenerated by the merged builder** (each differs from the merged
  file by exactly 2 lines, the stamp): **rc 0, `WARN 1 graded`** -- the WARN is the pre-existing
  `holdings_snapshot.build_inf` alias at `:785`, unchanged by this act.

So the one thing that separates refuse from pass is the stamp on those two files. **This binds under options A,
B and C alike**, because the drain carries M's feature edits to both files whichever option is chosen. Remedy,
in M's own lanes (`data/**` = ANY, `_authz/**` = IRPT_COMPLETION_M): regenerate those two targets on the branch
(`python lib/opal_naming.py generate --out <dir> --target <path>`, copy, commit) before the drain. That is a
stamp-only change to files M already edits. It is not an inherited-drift repair and not a carrier integration.

Also seen in the same trial merge, outside this review's scope: an add/add conflict on
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (both sides created it).
Whoever drains will have to resolve it.

## 7. Commands (reproducible)

```
git archive <pin> lib infra/logic/registry org/standards/NAMING_SCHEMA.json org/missions/DIRECTIVES.yaml <10 targets> | tar -x -C <tree>/src
(cd <tree>/src && python lib/opal_naming.py validate && python lib/opal_naming.py generate --out <tree>/gen)
python -m pytest -q lib/tests/test_opal_naming.py lib/tests/test_irpt_destination.py    # in <tree>/src
```

Not done by this review: any shared-carrier write, any commit outside this folder, a full-checkout test suite, a
`terraform plan`, any grant or lane change, any activation.
