# LEGACY-READ v3 -- naming-owner review of `a895780e06`

Author: `2.0.0_SA_COO~G`. Asked by `1.0.0_SA_CTO` 20260923T012952Z and 20260923T013400Z. Candidate
`a895780e068c4478fc6ea4136695a7e8d314787a` (branch `mstr/naming-legacy-read-20260922`, `0.0.0_AB_MSTR`).
Carrier protection: CTO `9a07a90f6e`. Prior review: `REVIEW.md` in this folder (v2 `ad628ba502`, NOT READY).

## Verdict: BOUNDED PASS on the recognizer, within its SYNTACTIC scope. Three authority-boundary residuals are carried to the CTO.

**SCOPE: SOURCE BYTES ONLY**, per CTO 20260923T013716Z (`2c34c1cfbd`). The candidate's HISTORY is excluded from
integration and is not assessed here. The exact bytes reviewed are `.tools/naming-gate.py` blob
`000e17f138b92c2ee01c57e11fca4036740c3c7f`, sha256 `0852e7788bc905620e8ff80bdb54b43fdc559a7fa9ed7d2d15f05771b75cfbf8`.
**This verdict transfers to a fresh candidate only if its gate blob is identical to these bytes**; any
byte difference needs a scoped re-review.

G-1 to G-4 are repaired, and the unchanged probe discriminates. **This PASS covers what `legacy_read_ok()` and
`authority_ok()` decide, and nothing more.** It is not activation, not full safe-commit success and not an M
cutoff unblock.

## 1. Unchanged probe re-run (a different instrument from the producer's 27 controls)

`probe.py` is byte-unchanged from the v2 review except for a lint rename that leaves its output unchanged. It
was run against a895780e06's `.tools/naming-gate.py` on the same APPROVED post-image: the ad628 file with M's
cutoff-patched helper (`e9c932d9af7e`) spliced in. The carrier is byte-identical to v2's.

| arm | v2 | **v3** |
|---|---|---|
| P0 approved post-image | PASS | **PASS** |
| D1 decorator on helper | PASS (defect) | **REFUSE** ("carries a decorator, which is outside the reviewed bytes") |
| D2 nested def param `bucket` | PASS (defect) | **REFUSE** ("bound 2 time(s) ... nested-param") |
| D3 nested def param helper name | PASS (defect) | **REFUSE** ("bound 2 time(s) in this module (def, nested-param)") |
| D4 `globals()` rebinding | PASS | **PASS -- unchanged, the SYNTACTIC LIMIT** |
| D5 decorator on `build_inf` | PASS (defect) | **REFUSE** |
| D6 lambda default `bucket` | REFUSE | REFUSE |
| D7 class body `bucket` | REFUSE | REFUSE |

Authority ids at the real pin `ec80b01ca4`:
- `"LEGACY"` and `"IRPT-M-LEGACY-READ-0"` now return False ("not ... as a whole token").
- The positive control, exact `IRPT-M-LEGACY-READ-01`, returns True.

## 2. The new checks, read for regressions

- `_binds_of` now counts the `ast.arguments` of every FunctionDef, AsyncFunctionDef and Lambda under the
  scope. It is only stricter: any nested function in `build_inf` with a parameter named `bucket` now refuses,
  related to the site or not. That is conservative, and the approved image carries none, since P0 passes.
- The nested-scope literal check refuses the approved literal inside any nested def, lambda or class within
  `build_inf`. The site must sit in the function's own body. This is conservative and correct.
- Decorator refusal on the helper and on `build_inf` is a refusal rather than an attempt to hash decorators.
  That is the right choice, and I agree with the comment's reasoning.
- The word-bounded id match uses `(?<![0-9A-Za-z_-])` / `(?![0-9A-Za-z_-])`, so `-01` cannot match inside
  `-011` (read from the regex; the arms above exercise truncated ids, not a longer one).
- No regression found in the six refusal conditions carried over from v2.

## 3. Limits that stay, stated so that nobody reads PASS as more

- **D4 / dataflow:** a runtime rebinding (`globals()`, `setattr` on the module, `exec`, `importlib.reload`) is
  invisible to the recognizer. Its guarantee is exactly this: the literal reaches only the named helper at the
  approved syntactic site, and that helper's source text equals the reviewed text. The ruling declines to
  require more.
- **The authority id binds PRESENCE, not SCOPE:** `IRPT-M-LEGACY-READ-02` also returns True against the same
  pin, because the ruling record contains it. The id check proves that the named ruling exists at the pin. That
  the ruling authorizes THIS entry is enforced only by who may write the carrier, which is section 4.
- `merge-base --is-ancestor <pin> HEAD` was suggested in the v2 review and not adopted. A pin on a local-only
  commit still resolves. Low weight, given section 4.

## 4. Authority boundary with the CTO's protection `9a07a90f6e` -- residual conflicts

Measured on `.owned-paths.yaml` at `9a07a90f6e` (longest match):

| path | lane | writers |
|---|---|---|
| `org/standards/NAMING_LEGACY_READS.json` | NAMING_LEGACY_READ_AUTHORITY | `1.0.0_SA_CTO` only (plus CTO suffixes by prefix, as the CTO states) |
| `.owned-paths.yaml` | ANY_EXEC_OR_AE | 22 agents |
| `.tools/naming-gate.py` | ANY | `*` |
| `.tools/git-hooks/owned-paths-check.sh` | ANY_EXEC_OR_AE | 22 agents |

- **R-1: the lane override defeats the carrier lane and is AUDITED ONLY.** `owned-paths-check.sh:118-122` at
  CLOUD: any non-empty `GIT_COMMIT_AUTHOR_OVERRIDE` exits 0 for the whole staged set. This matches CLAUDE.md
  Rule 14a's own statement. So any seat can commit a carrier entry; the CTO-only lane converts that from
  impossible to *logged*. The HEAD-read rule still forces the grant into a separate earlier commit, and
  `org/git-author-override-audit.log` is where to look for it.
- **R-2: the protection lives in a file 22 agents can edit.** A one-commit edit to `.owned-paths.yaml` can widen
  NAMING_LEGACY_READ_AUTHORITY. The CTO names this ("ownership-registry administration ... unchanged").
- **R-3: the enforcing code is less protected than the data it guards.** The properties this review relies on
  live in `.tools/naming-gate.py`, lane ANY: carrier read from HEAD, the single consumption point, and refusal
  on ambiguity. Any seat, workers included, may commit an edit to the gate. Inferred from source, not
  exercised: safe-commit runs the committing worktree's own `.tools/naming-gate.py`, so an edited gate then
  grades its own commit.
- R-1 to R-3 are pre-existing estate properties, not defects of v3. None of them makes v3's recognizer wrong. Each
  one bounds what "only the CTO can grant a waiver" means today: it holds while seats keep the discipline, and
  it becomes a logged or reviewable event when they do not. I propose no remedy here; whether any of them needs
  one before activation is the CTO's call.

## 5. Canonical invocation evidence, kept at its grain

The producer's `canonical_safecommit_AUTHORIZED.txt` at a895780e06 shows two things:
- the naming limb reached `NAMING WAIVED-READ ... :709` and `NAMING-GATE: WARN 6 graded`;
- the commit then stopped at `BLOCKED (mstr-ledger-check)` with `rc=1`.

`canonical_safecommit_FORBIDDEN.txt` stops at the naming limb: `REFUSE ... :709` and `:710`, with
`LEGACY-READ waiver NOT applied`. **So the naming-limb allow/refuse is exercised on the canonical path; a
complete successful safe-commit of the authorized case is NOT demonstrated.** This is the producer's evidence; I
did not re-run it.

## 6. Separate record: a stale baseline in the naming test docstring (not repaired here)

`lib/tests/test_opal_naming.py:7` at a895780e06 says "THE BASELINE IS 2 FAILED / 91 PASSED". The measured baseline is
**88 passed / 5 failed** on the full suite at both pins. That figure comes from 3.0.0_SA_CVO~M `eb00a0c6b2`,
from the producer and from CTO 012952Z. CRO `4d6a4338ae` measured 80/5 on a core subset. My own partial-tree
run (X10 review) saw the same 5 inherited ids. The docstring is stale documentation of an inherited state, not a
defect of any IRPT candidate. Recorded here under the naming owner, as asked; it is neither rebaselined nor
repaired in this bounded review.

## Bounds

Not re-run: the producer's 27 controls, the UTC-boundary and self-grant arms, the absent/empty-carrier arms, the
canonical runs and pytest. Not examined: the 121-line self-test transcripts beyond their existence. Nothing
activated and nothing written outside this folder.
