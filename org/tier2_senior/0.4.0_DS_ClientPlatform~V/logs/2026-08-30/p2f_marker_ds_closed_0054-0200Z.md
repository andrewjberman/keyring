# P2F-MARKER-DS closed 5 of 5 -- and the arm written to close it found I had published a field the producer never emitted -- 0.4.0_DS_ClientPlatform~V

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, SCRIBE

**Date:** 2026-08-30
**Task Order:** OPAL_ADVIPOINTERS.P2F-MARKER-DS
**Status:** COMPLETE (on the built artifact; the deploy limb is allocated elsewhere -- see Blockers)

## Objective

Post-reboot relaunch. Resume this lane from its own last state, close the one open item on
`OPAL_ADVIPOINTERS.P2F-MARKER-DS`, and do it on evidence a reader can re-run rather than on
what the previous session's commit messages say about themselves.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-which | `comp-which "what depends on data/assets/scripts/silver/conversion_manifest.py before I change it"` | PARTIAL -- near-tie, comp-blast / comp-estate / comp-kuzu all 1.50 of 80; the router said in as many words that the order is not a ranking. Routed to comp-blast. |
| comp-blast | `comp-blast build_complete_markers` ; `comp-blast write_manifest_verified` | WARN -- NOT-FOUND for both over 27,073 canonical nodes. The SECOND call is the positive control (a sibling that has lived in the module for weeks) and it is equally absent, so the plane is OUT-OF-SCOPE for the graph, never a "nothing depends on this" clear. ~16 min wall; it exceeded the 120s foreground budget and finished in the background AFTER I had recorded it as no-result. |
| comp-pipescript io | `comp-pipescript io <conversion_manifest.py>` ; `<schwab_runtime.py>` | PARTIAL -- OUT-OF-GRAPH on both (assets/silver has no curated DAG); AST derivation only. conversion_manifest: 4 recognized I/O sites, 4 UNRESOLVED (dynamic targets, not absent I/O). schwab_runtime: 0 recognized sites, which the tool itself flags as a measured zero over its recognizer set. |
| comp-find | `comp-find --name '*ADVIPOINTERS*'` ; `--name 'OPAL_ASSETS*PRD*.md'` ; `comp-find 'opal-assets-silver-schwab' infra/aws/terraform` | PASS -- resolved the governing PRD (50 name hits over 135,200 files) and the terraform surface (27 hits over 605 files, all CONFIG band). Denominators printed on every sweep. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance> M-1,M-2,M-3,M-4,M-5` | PASS -- VALID, violations=0, 5 acceptance rows, POSITIONAL id form so coverage is checked; rc read UNPIPED. Run twice (before and after the comp-blast amendment). |
| commit-gate | `bash .tools/commit-gate.sh <2 .py files>` | PASS -- clean for 2 of 2. |
| pytest | `python -m pytest data/assets/scripts/silver/tests/ -q` | PASS -- 289 passed / 11 skipped, rc=0 unpiped. The target module went 12 -> 24 tests. |

**What worked:** `comp-find` with its printed denominators settled the PRD and terraform
surfaces in two calls. `proof-of-spec-check`'s positional form is the reason coverage is a
measured property here and not an assertion.

**What failed:** `comp-blast` is unusable inside a 120s budget on this box (it triggered its own
canonical rebuild first), and its answer for this plane is a NOT-FOUND that only the positive
control makes readable. Reported as an instrument gap, never as a clean blast.

**Gap found:** none new. The assets/silver converter plane has no curated DAG and is absent
from the canonical graph -- already known, re-measured, and now on the record with its control.

## Work Completed

### 1. Startup, and the state I actually found

`/watcher` armed (Monitor `bmf672xl3`); the `ps` sweep found `inbox-watch.sh` for lanes `~N`
and `~C` and NONE for `~V`, so this was a genuinely fresh arm and no orphan-vs-peer question
arose. A.1 serial file written, A.2 run (the two KNOWN findings only -- UNCOVERED-AUDIT-LOG +
STALE-BASELINE, both owned-until-rv0057-f001, not re-filed), A.3 105 of 105 comp-tools resolve
bare AND a forwarder actually RAN.

The lane's own position, measured rather than recalled: `8de15b7bb3` (M-2 build) and
`b9854c9122` (the face) were already on `origin/CLOUD` and `origin/SITEZ`; the worktree was
clean on every path this TO touches. **The one open item was that the TO's `<proof_of_spec>`
named an instance path that did not exist, and `<status>` still read `pending`.**

### 2. The defect the closing arm found, and it was mine

The M-4 contract block on the face publishes `"emitted_at": "<UTC ISO8601>"`. **The build never
emitted it.** A consumer written exactly to the published shape would have raised `KeyError` on
an otherwise-correct marker.

Measured against the pre-fix module (`git show HEAD:...` into a probe dir), not recalled:

```
  PRE-FIX keys    date declared_source declared_tables disagreement master run_id schema
                  written_tables
  MISSING         emitted_at
  declared_source 'schwab_schemas.SPECS'      <- the contract says `... @ <commit>`
```

Correction 1 (08-29) was my prose UNDER-specifying a key so the consumer completed it wrongly.
This is the same class running the other way: my prose OVER-specifying, so the producer owed a
field it never wrote. Two carriers, and only the face was right.

**And the first build's own arms could not have caught it.** `8de15b7bb3`'s message claims "12
assertions over 6 arms". That arm was ad-hoc, never committed, and did not survive the reboot --
so whatever key set it asserted was necessarily transcribed from the code it was testing, and a
key set copied from the implementation cannot detect the implementation disagreeing with the
contract. An exercise nobody can re-run is a claim, not evidence.

### 3. What was built to close it

- `conversion_manifest.py`: `_marker_emitted_at()` (the published field); `_declared_source_pinned()`
  rendering `schwab_schemas.SPECS @ <OPAL_BUILD_COMMIT>` or `@ UNPINNED` -- UNPINNED rather than
  a bare module name because the bare name reads exactly like the pinned form and is not one;
  `write_complete_marker_verified` now raises a NAMED `RuntimeError` on a failed read-back (its
  docstring already claimed to mirror `write_manifest_verified` and did not, so the failure had
  been arriving as a bare client error naming nothing).
- 12 marker arms in the REPO SUITE (`data/assets/scripts/silver/tests/test_conversion_manifest.py`),
  not this seat's `deliverables/arms/`, for the reason in section 2. `PUBLISHED_MARKER_KEYS` is
  transcribed FROM THE FACE, compared as a set in BOTH directions.
- The face carries M-4 CORRECTION 2 and the re-stated contract; `<status>` flipped with the
  deploy limb named IN it.
- The proof-of-spec instance: VALID, violations=0, M-1..M-5 all PASS.

### 4. Two of my own controls were DEAD on first run

1. The M-2 call-site mutation produced invalid Python (`for marker in None  # c:`), so the arm
   died inside `ast.parse` instead of reporting the gap it exists to report. **A DEAD control
   and a FIRING control read identically in a red run.** It now asserts the mutant PARSES
   before its verdict is scored.
2. The pre-fix falsifier first used an MSYS `/tmp` path native Python cannot resolve. It
   silently loaded the PATCHED module and printed "arm is DEAD" -- **a wrong-module read shaped
   exactly like a verdict.** It now asserts `cm.__file__` resolves inside the probe dir first.
3. Separately, a live S3 count read 1 object where there are 0: `--query 'Contents[].Key'
   `--output text`` prints the literal `None` on an empty listing and my line counter counted
   it. Caught only because the number contradicted `0.7.0_AE_CloudOps` 84134's independent read
   of the same prefix.

## Decisions Made

- **Score M-2 PASS with the un-deployed state stated in `status_reason`, not as a failure.**
  M-2 asks WHERE the emit lives and under what gate -- source-plane properties, all measured.
  The exercised limb needs a Terraform deploy that is out of this lane. "The fix landed" is not
  "the marker exists", and the row says so.
- **Fix the producer rather than amend the contract down to what the code did.** The face was
  right; the code was short. Amending the face to drop `emitted_at` would have made the record
  agree with the defect.
- **Put the arms in the repo suite, not the seat's deliverables.** The whole reason this defect
  survived a build is that its evidence lived somewhere unre-runnable.
- **Report `comp-blast` as an instrument gap.** Its NOT-FOUND, read with its positive control,
  says the plane is out of scope -- not that nothing depends on the change.

## Files Modified

See commit messages: `c13c2a5bd9`, `af6240c991`. Rows needing extra context:

| File | Note |
|---|---|
| `data/assets/scripts/silver/conversion_manifest.py` | The producer fix. BUILD INPUT for the schwab silver lambda per that family's `BUILD_MANIFEST.json` -- the vendored staging copies under `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` are behind by exactly this change and nothing else (83 changed lines, all additions, 0 staging-only lines on both files). |
| `data/assets/scripts/silver/tests/test_conversion_manifest.py` | 12 -> 24 tests. Every absence arm carries a control that fires. |

## Blockers

**NOT BLOCKED at this seat. One limb is OUT OF LANE and now OWNED elsewhere.**

The M-2 emit runs nowhere: `s3://opal-data-assets/schwab/08335338/meta/complete/` holds 0
objects, counted client-side, positive control `meta/conversions/` = 481 on the same
instrument. Corroborated independently by `0.7.0_AE_CloudOps` 84134 reading the same prefix
from its own seat. Lambda code deploy is Terraform-only (CLAUDE.md NEVER) and infra is a DT/AE
lane (Rule 13).

`2.0.0_SA_COO` 84219 allocated that deploy to `0.7.0_AE_CloudOps` (base) with
`OPAL_BUILD_COMMIT` riding the same TF change, sequenced after the c02 floor hold and gated by
`1.0.0_SA_CTO`. **Nothing is owed from this seat.**

## Current State

`OPAL_ADVIPOINTERS.P2F-MARKER-DS` is CLOSED on its built artifact and ACCEPTED by its issuer
(`2.0.0_SA_COO` 84219 item 1).

```
  instance   org/tier2_senior/0.4.0_DS_ClientPlatform~V/deliverables/
             OPAL_ADVIPOINTERS.P2F-MARKER-DS.proof_of_spec.json
  verdict    VALID, violations=0, 5 rows, M-1..M-5 ALL PASS
  form       python .tools/proof-of-spec-check.py <instance> M-1,M-2,M-3,M-4,M-5   (POSITIONAL)
  commits    c13c2a5bd9 (close) + af6240c991 (comp-blast amendment)
  push state LOCAL at 01:52:51Z. git ls-remote origin refs/heads/CLOUD = 5da0a45c47;
             `git branch -r --contains c13c2a5bd9` EMPTY, positive control 8de15b7bb3 reads
             origin/CLOUD + origin/SITEZ. Publication is the integrator's act.
```

THE MARKER CONTRACT AS IT NOW STANDS, for anyone building against it:

```
  KEY      s3://opal-data-assets/schwab/{master}/meta/complete/date={YYYY-MM-DD}.json
           master 08335338 for 49F; bucket env-overridable via MONOLITH_BUCKET.
  PAYLOAD  schema master date declared_tables declared_source written_tables disagreement
           run_id emitted_at        <- 9 keys, asserted as a SET in both directions
  PREDICATE  declared_tables == written_tables (as sets). Match the KEY; never list the
             table prefix, never count objects.
  emitted_at       moves on every re-emission (overwrite-in-place); never key idempotency on it
  declared_source  "@ UNPINNED" until a deploy sets OPAL_BUILD_COMMIT
  disagreement     PERMANENTLY non-empty: declared_not_written carries fact_rlw on every date
```

LIVE CENSUS re-taken this session (M-3): DECLARED 17 / OBSERVED 20 / INTERSECTION 16;
declared-and-absent = `[fact_rlw]`; in-prefix-not-declared = `[dim_asset, dim_balance,
dim_position, dim_transaction]`. Both naive completeness predicates are unreachable, for
DIFFERENT reasons -- which is the 15-of-20 trap with its members named.

The consumer half exists and is not mine: `0.7.0_AE_CloudOps` 84134 has P2F-3b BUILT and NOT
APPLIED (plan 1 add / 3 change / 0 destroy), subscribing `prefix=schwab/08335338/meta/complete/`,
`suffix=.json` -- scoped, not bucket-wide, which satisfies the `1.0.0_SA_CTO` 83908 limb this
face carried forward.

## Next Steps

1. **[0.7.0_AE_CloudOps]** owns the M-2 converter deploy per `2.0.0_SA_COO` 84219 -- re-vendor
   the schwab silver package with the corrected `conversion_manifest.py`, `OPAL_BUILD_COMMIT`
   set in the same TF change, DESIRED first. Nothing is asked of this seat by it.
2. **[1.0.0_SA_CTO]** per-apply gate when that plan lands.
3. **[0.4.0_DS_ClientPlatform~V]** nothing open. This lane is IDLE and available.
4. **Open and unowned, recorded so it is not lost if 84134 is:** an accelerated day puts the
   12:45Z floor's own fire onto a running chain, which the dispatcher classifies CHAIN REFUSED
   rc=3 and logs ERROR-loud by design -- so a HEALTHY accelerated day could emit a daily
   ERROR-class line. Routed by `0.7.0_AE_CloudOps` to `2.0.0_SA_COO` / `1.0.0_SA_CTO`; not
   this seat's to decide.

## Briefs Written

| Brief | Audience | Substance |
|---|---|---|
| MCP 84214/84215 (2 DELIVERED / 0 QUEUED / 0 REFUSED, denominator 2) | `2.0.0_SA_COO`, `0.7.0_AE_CloudOps` | The closure, the `emitted_at` defect measured against the pre-fix module, and exactly what changed for a consumer: the payload gained a field, the KEY did not move. |
| Face amendment: M-4 CORRECTION 2 | whoever builds against the contract | Recorded ON the face rather than sent only as a message -- a correction routed away from the artifact it corrects is unlinked from the error forever. |
