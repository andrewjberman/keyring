# OPAL_ASSETS G4 + R-A/R-B LIVE; my aws-shim regression found + fixed; six false-greens

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE, COORDINATE

**Agent:** 0.8.0_AE_CloudComp | **Date:** 2026-07-13 | **Window:** post-reboot respawn (~0517Z) -> 0645Z
**Prior log:** `550eadfe6`

---

## Summary

Post-reboot respawn. Self-onboarded from `PRE_REBOOT_JOINT_NEXT_STEPS_20260713.md`. Priority was to
unblock `0.7.0_AE_CloudOps~A`, who was IDLE-gated on my G4 commit. Delivered that, then held the review
seat through R-A/R-B, then found and fixed a regression in my OWN aws shim that was silently breaking
Lambda deploys fabric-wide.

**Andrew can now run `SUM(value) WHERE additive` on `opal-assets-daily-aua` and get the right number.**
That is the deliverable. Before tonight a naive `SUM(value)` returned **$5.82B against a real ~$1.8B**
(COO-measured, ~3.3x) on a table Andrew queries directly.

---

## Work completed

### 1. G4 ownership fold -- LANDED, LIVE (`0105ef6e7` + `127e7dc0f`; applied by ~A at `opal-assets-v0.2.0`)
Per-(ETF,partner) held-ownership rows as ADDITIVE ROWS off the measured `opal-data-etfs/daily` source
(CTO~B-ratified canonical held-source; never mdpf `target_weight` -- intent is not observation).
- **Latent defect found + closed:** `value_class`/`source_field` were set INSIDE `if pb is not None:`
  (`lambda_function.py:176-190 @ d93c16661`), so a partition lacking a partner block would emit 9 of 14
  rows with NO `value_class` -- the exact unclassified-row defect CTO~B's condition-of-approval exists to
  prevent. **LATENT, NEVER FIRED** (every served partition carries its partner blocks -- which is why the
  live table honestly read 0-missing). Did not overstate it as live.
- **Fix MEASURED as free, not asserted:** ran HEAD's `build_rows` vs mine over the FULL enumerated
  denominator -- **427 served partitions / 5,978 base rows, 0 output changes** -> no re-backfill needed.
- **Decision reversal handled:** ~A first ruled an additive `record_type` classifier; his LATER message
  reversed it on LIVE STATE (deployed table already carried `value_class` on all 266 rows, 5 classes,
  0 missing). Backed `record_type` out fully rather than shipping both. Latest + most-restrictive binds.

### 2. The basis question -- GROUNDED, and it corrected CTO~B's own ruling
CTO~B asked for the basis question WITH EVIDENCE rather than a guess. Grounding it produced the session's
biggest find:
- **mdpf ALREADY computes, reconciles and SERVES the headline** (`aggregate.opal_aggregate_aua` =
  $1,758,111,296.54, with `headline_formula` + identity_1/identity_3 PASS) -- **and the emitter was reading
  that body and dropping the block on the floor.** The table held the ingredients while the answer sat in
  the source it already read.
- **R-B CORRECTED (CTO~B, on my grounding): CARRY-VERBATIM, never re-derive.** Re-deriving would mint a
  second source of truth for the number Andrew reads.
- **NEAR-MISS, on the record:** had I built the total the obvious way ("sum the disjoint basis") I would
  have emitted `partner_aua_subtotal` = **$1,823,572,303.03 -- $65,461,006.49 TOO HIGH** -- because the
  ratified headline EXCLUDES Inflection's non-model book as audit-only (mdpf PRD v0.9 / MDPF_ASSETS.028).
  Summable-looking, plausible, wrong. **You cannot get it right from the row data alone; the knowledge
  lives upstream.** That is the whole argument for producer-owned aggregation, made concrete.
- **The additive set, verified EMPIRICALLY (not from prose):** `{49f_schwab_custody, inflection_models}`
  reproduces the certified headline **427/427 partitions, residual $0.0000**. ~A independently re-ran it.

### 3. Review seat on ~A's R-A/R-B -- found the BLOCKER (`02ea149ba` / `opal-assets-v0.3.0`, LIVE)
- **BLOCKER: AC7 failed closed on the TOTAL and failed OPEN on the TABLE.** `lambda_handler` called
  `write_rows()` unconditionally, so on a detected inconsistency the mis-flagged `additive` rows STILL
  LANDED while the total sat blank -- and Andrew's *contracted* query would return the wrong number.
  **A guard that DETECTS but does not PREVENT is a witness, not a gate.** ~A gated the write (RAISE before
  every write path incl. backfill). Now: a partition that does not reconcile never lands, so **"it is in
  the table" IMPLIES "it reconciled."**
- **AC4 is UNSATISFIABLE BY CONSTRUCTION** (routed to CTO~B, RULED into G2): the only channel by which
  `08335338` can ever be OBSERVED is a body master-marker field. **mdpf has NEVER emitted one -- 0/427
  partitions top-level, 0 nested, `08335338` appears 0 times in any body.** So cohort-8's `incomplete` is
  correct today and **structurally UNCLEARABLE** -- it will NOT clear when G2 lands. Real hazard is not the
  stuck state but the fix someone reaches for: hard-wiring `fresh`, laundering the gap. -> mdpf must emit a
  per-cohort MASTER MANIFEST (CTO~B ruled it into G2's scope).
- **The PRD's own AC7 formula invited the edit that breaks the contract** (routed to CTO~B, RULED): a
  basis-scoped reading makes the 4 `etf_fund` rows `additive=true`, and a consumer who forgets
  `AND basis='partner_aua'` gets **$2,436,503,080.54**. CTO~B corrected his own spec: `additive` is GLOBAL,
  `basis` is DESCRIPTIVE ONLY. Pinned in `test_additive_is_GLOBAL_not_basis_scoped`.
- **Guard suite rewritten to v0.2** (landed inside ~A's commit so the tree never went red): retired
  `partial` into the folded `source_masters`/`masters_present` schema, added the adversarial AC7
  miswired-axis mutant. Suite **30/30**.

### 4. MY OWN REGRESSION -- the aws shim (`440471da4`, `29a7042b9`)
The `.tools/aws` PATH shim I landed at `19fde37de` **silently broke every bash -> powershell -> `aws` call
in the fabric.** A `powershell.exe` spawned from Git Bash inherits bash's PATH (`.tools` first) and resolves
the EXTENSIONLESS bash script as an Application -- **it HANGS rather than failing**, and with `--quiet` +
no rc check that printed a success line while S3 kept the OLD artifact.
- 4 call sites. `build-and-upload.sh` was guarded (base-AE's upload-verify gate -- **the only reason we
  learned any of this**). The **3 find-insure LAYER builds were UNGUARDED**: a silent no-op there ships a
  layer whose dependencies never updated, undetected.
- **FIX:** `.tools/aws.cmd` companion (PATHEXT makes Windows shells prefer it; bash keeps the MSYS guard).
  Exercised both directions. CTO then TRACKED both shim files (`789c291ba`) -- `.tools/` is a directory
  where tracked and invisible files are indistinguishable, and it holds fabric-critical executables.
- **CTO-ruled GO -> ported the upload-verify gate to all 3 layer builds** (`29a7042b9`), exercised 4 ways
  against a real 37MB artifact.
- **Struck 3 FALSE CLAIMS in my own brief**, incl. validation row T5 ("PowerShell unaffected") -- **the test
  was RIGGED, not passed: I ran it in an INDEPENDENT PowerShell, which has no `.tools` on PATH and therefore
  COULD NOT HAVE FAILED.** Corrected CLAUDE.md wording landed by CTO (`1925b9f9f`).

### 5. Fabric-wide instrument defect: `simulate-principal-policy` multi-ARN poisoning
Reported by ~A; **I independently REPRODUCED it before relaying** (3 calls, same role/action/ARNs, only the
batching differs): a HELD ARN reads `allowed` alone and **`implicitDeny` when batched with a not-held ARN.**
**CLAUDE.md Rule 22a MANDATES that exact combination** ("simulate the target WITH a positive control"), so an
agent following the rule the obvious way gets a false DENY and rolls back a CORRECT deploy. Root-causes
base-AE's unexplained false-deny. My own checks were sound only because I happened to issue separate calls.
Remedy: **one ARN per call, always.** -> CTO (Rule 22a defect).

---

## MCP traffic

~20 messages. Significant: COO `[DRIVE] GO` + RAVC2 gates; ~A's decision reversal, single-writer claim,
review-seat handoff, and LANDED+LIVE; CTO~B's G4 ACCEPT, R-A/R-B rulings, and BOTH-FINDINGS-ACCEPTED
(`9ab5488b7` -- both were defects in his own rules); CTO's 3 rulings on the shim + gate port.
**Two self-retractions issued by me in writing** (below).

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "which gold script produces the mdpf aggregate_aua served partition" | PASS | routed to `comp-pipescript io`; found the producer |
| `comp-iam service` | `opal-assets-daily-emitter` | **WARN** | returned **UNKNOWN / "role not mapped"** for both S3 ops -- SILENCE, not a green. Did not cite it as evidence either way. |
| `comp-blast` | `build_rows` | NOT-FOUND | honest NOT-FOUND -- the new opal-assets Lambda is not in the graph yet |
| `comp-aws` | `opal-assets-daily-emitter` | FAIL (usage) | my error: `comp-aws` takes subcommands, not a resource name |
| `comp-surface-check` | auto in `safe-commit` | PASS | 0 critical surfaces touched (x5 commits) |

**What worked:** `comp-which` routed correctly on a plain-English question.
**What failed:** `comp-iam` could NOT answer the one question that mattered -- a brand-new Lambda's IAM.
It returned `UNKNOWN / role not mapped` (its 21 NOT-ATTACHED policy blocks). Rule 20/22a had to be satisfied
entirely with live primitives (`simulate-principal-policy` + controls).
**GAP FOUND (worth a build):** the graph has **no coverage for the `opal-assets` module** -- `comp-blast`
NOT-FOUND on its functions, `comp-iam` role-not-mapped on its Lambda. A brand-new pipeline is exactly when
the graph is least useful and most needed. Routing as a coverage gap.

---

## Deployment / Verification (AE)

I authored + committed; **`0.7.0_AE_CloudOps~A` held the applier seat** (one applier, no TF race). I did not
apply. Verified independently rather than off his self-report:

```
G4:        opal-assets-v0.2.0 | 26 rows (14 base + 12 ownership) | value_class MISSING = 0
R-A/R-B:   02ea149ba | opal-assets-v0.3.0 | safe-apply 0/1/0 | 0-diff | invoke rc=200
           532 rows / 19 partitions / 28 each | MISSING additive: 0 | MISSING basis: 0
           SUM(value) WHERE additive == mdpf certified headline, EXACTLY, on every partition
           ledger 5/5 CLOSED; re-backfill ran in the SAME landing
Rule 22a:  opal-data-etfs GetObject -> implicitDeny (pre-apply, correct)
           POSITIVE CONTROL (mdpf key) -> allowed        <-- instrument HEALTHY, one ARN per call
           SOVEREIGN opal-data-bd      -> implicitDeny   (must stay; ~A re-verified post-apply)
Layer gate: exercised vs live 37,873,451-byte artifact -- control passes; size/sha/no-op/404 all FIRE
```

**Re-backfill was REQUIRED this time (unlike G4):** `basis`/`additive`/`masters_present` are new attributes
and a DynamoDB filter on a missing attribute **silently omits the row**, so a partial stamp would have made
the contract true for only the newest day. Flagged pre-landing; ran in the same pass.

---

## Blockers

**NONE.** Nothing outstanding with CTO, CTO~B, COO, or ~A (all confirmed closed in writing).

---

## Current State

- **OPAL_ASSETS G4 + R-A/R-B: LIVE and CLOSED on my side.** `opal-assets-daily-aua` carries 28 rows/day:
  14 base cohort + 12 ownership + 2 per-basis totals. Every row carries `value_class`, `basis`, `additive`,
  `source_masters` (DECLARED), `masters_present` (OBSERVED). `SUM(value) WHERE additive` (NO basis filter)
  is correct by construction and fail-closed: an unreconcilable partition never lands.
- **Guard suite:** `infra/aws/lambda/opal-assets/tests/` -- 30/30 (my classification/additivity guard +
  ~A's reachability). Outside the function dir, never packaged.
- **aws shim:** `.tools/aws` + `.tools/aws.cmd` -- **BOTH now TRACKED** (`789c291ba`). Provisioning is
  ATOMIC: both files or neither (`.tools/aws` alone IS the regression). Corrected CLAUDE.md rule landed
  (`1925b9f9f`).
- **Layer builds:** all 3 find-insure `build-layer.sh` now carry the fail-closed upload-verify gate.

## Next Steps

1. **[0.8.0_AE_CloudComp]** G5 convergence -- **HARD-GATED** on the PRD v0.2 §2 per-source `as_of`-SEMANTICS
   CENSUS of all six converging sources. Wiring six sources together before knowing what each means by
   `as_of` bakes the defect in. Not startable until the census exists.
2. **[1.0.0_SA_CTO~B]** owns the mdpf per-cohort MASTER MANIFEST requirement (G2 scope) -- until it lands,
   cohort-8's `incomplete` can never clear. `test_the_production_clearing_path_is_DEAD` asserts the gap on
   purpose; **when it goes RED that is GOOD NEWS.**
3. **[anyone building a find-insure layer]** the new gate is the **only** incidence measurement that will
   ever exist for the silent-no-op window. **If it fires, that is a finding, not an embarrassment.**
   Incidence remains **UNKNOWABLE** -- do not convert "no known incidents" into "no incidents."
4. **[0.8.0_AE_CloudComp]** graph-coverage gap: `opal-assets` module absent from the graph (`comp-blast`
   NOT-FOUND, `comp-iam` role-not-mapped). Route to CTO/COO.

---

## The pattern this session produced (six instances, five agents)

**A green that holds for a reason production does not supply.**
- My cottonwood fixture asserted absence for a partner that is LIVE (12 rows, not the 8 I predicted).
- ~A's reachability direction-2 passed only because his FIXTURE injected a marker field mdpf never writes
  -- it proved the CODE can not-fire, not that the SYSTEM can.
- `value_class` "always present" was true BY LUCK OF THE INPUT, not by construction.
- My shim's T5 test ran in the one shell that COULD NOT HAVE FAILED.
- AC7 detected a miswired axis but still WROTE the poisoned rows.
- **And while building the exercise harness for a gate against exactly this class, I wrote another one:**
  my positive control reported PASS off a **404** -- `head-object` failed, both sides of the comparison
  were the literal string `HEAD_FAILED`, **and I compared the garbage against itself.**

**Two lines landed as CLAUDE.md doctrine (CTO, `05d3c9b7a` / credited):**
- *A control that cannot fail is not a control.*
- *Knowing a failure mode by name does not immunize you against writing it.*

**Two self-retractions I issued in writing:** (1) I told ~A that AC7 could not catch the additive mis-flag
-- asserted from READING his code instead of EXERCISING it. Wrong. **Chasing the retraction is what surfaced
the write-gate hole**; had I quietly dropped the claim, that ships. (2) My characterization of
`model_value_sum` to COO was wrong (it is INFLECTION's model book, not a sum over rows already present) --
his arithmetic was right, his comparison crossed partners, and **my prose was the wrong thing**. It did not
propagate, because R-A was verified EMPIRICALLY on the full denominator rather than derived from my story
about it. *That is the value of grounding on the denominator instead of on a plausible narrative.*
