# Session log — 0.7.0_AE_CloudOps~Z — 2026-09-10 0122–0200Z — SYSPARITY RB1 rule-bank drift

**Seat:** `0.7.0_AE_CloudOps~Z` · **Face:** `NFRA_SYSPARITY.TO-RB1-SITEZ` · **Issuer:** `2.0.0_SA_COO~Z` (GO msg 20707)
**Authority:** Andrew-direct 2026-09-09 ~22:3xZ, *"Yes agreed with COO~Z."* · **Branch:** `ae-cloudops-z-rb1-rulebank`

## The work, and it was small

Head is `v1.8`; eight SDK assertion sites across seven files still asserted `v1.2`. Moved them. The
whole face is 7 files, 8 insertions, 8 deletions — one token per site.

What made it worth care rather than speed was the **exclusion**: `infra/system/system_parity.py`
carries three more hits, and its `:676` `v1.1` is a **deliberate negative control** consumed by the
mutant at `:692`. "Fixing" it would make the mutant pass on a stale site and silently destroy the
discrimination the check exists for. So the edit script takes an **enumerated file list with an
explicit refusal guard on that filename** — not a glob, not a tree walk — with a per-file expected
count verified in a pre-pass before a single byte is written, and an assertion after each write that
reversing the substitution reproduces the original bytes.

`system_parity.py` appears **0 times** in the diff, measured on two tree states. Self-test **30/30**,
including `[PASS] 23 COVERAGE MUTANT (rulebank shape)`.

The **ratification pins did not move** — deliberately. That is `RB1-AC4`, a judgment criterion the
face reserves; bumping them would have been deciding it. Filed `UNVERIFIABLE-BY-INSTRUMENT` naming
the adjudicating seat, with the inputs assembled and **no verdict written in-lane**.

## The finding — row `NFRA_SYSPARITY-Z-S1` @`b441f6e2c4`

**`comp-find` run from a linked worktree censuses the MAIN tree, and fails as a confident MEASURED
ZERO.**

Found because `RB1-AC2`'s own named invocation **contradicted the bytes on disk**. In the worktree,
whose files carried `v1.8` (verified by direct read of four sites):

| invocation, same cwd | result |
|---|---|
| `comp-find 'rule-bank v1\.8' infra/system` | `0 hit(s) across 173 file(s)` — *"a MEASURED zero"* |
| `comp-find 'rule-bank v1\.2' infra/system` | 10 hits, the **pre-edit** content |

Same denominator both ways. The control that separates *wrong tree* from *broken pattern*: the
identical `v1.8` invocation from the **main** tree after merge-back returns **8 hits** over the same
173 files. Same pattern, same pathspec, opposite verdict; the only variable is which tree the shell
stood in. `pwd` and `git rev-parse --show-toplevel` both resolved to the worktree, so cwd was not the
confound.

**Why it matters beyond this face:** CLAUDE.md 14b *mandates* a worktree for anything bigger than a
one-file edit; Rule 21 *mandates* comp-find as the census instrument and gates raw grep. The mandated
instrument is blind to the mandated workspace, silently. The mirror case is the dangerous one — a
seat verifying a **deletion** from a worktree gets a clean PASS from a tree that was never edited.

**Mechanism stated only as far as it was established:** the `~/bin` forwarder ends `exec "$_t" "$@"`
with `_t` hardcoded to the main workspace, and `.tools/comp-find:73` resolves relative to its own
`__file__`. ⛔ The line that computes the corpus root was **not located** and the row does not assert
one. The behaviour is the claim.

## Errors and near-misses

- **The near-miss that became the finding.** Had I taken `RB1-AC2` at face value from the worktree, I
  would have reported my own landed edit as *not landed*. A criterion disagreeing with a direct read
  is what surfaced it.
- **Two rail gates fired correctly on me** — piping `comp-find`/`comp-read` into `head`/`grep` erases
  the denominator. Re-run with native flags both times.
- **Assumed a schema shape and was wrong**, cheaply: the flat channel didn't exist, so I read the
  `POSN_TENANCY` template and the item schema rather than inventing a header, and validated the row
  against `investigation_item.schema.json` **before** committing.

## Compiler Tools

| tool | invocation | what it decided |
|---|---|---|
| `comp-find` | `comp-find 'rule-bank v1\.' infra/system --limit 40` | RB1-AC1 in full: 11 hits / 173 files, and the **banding** (SURFACED=5 / CONFIG=6) is what partitioned 8 in-scope from 3 fixture in the tool's own output rather than by hand. |
| `comp-find` | `'rule-bank v1\.2'` then `'rule-bank v1\.8'` | The after **pair**, run as a pair deliberately: the zero-remaining half alone reads identically whether the edit landed or the instrument is blind — which is precisely the failure that then occurred. Arithmetic closes: 8 + 2 + 1 = 11. |
| `comp-read --enumerate` | `.tools/comp-find --enumerate 'show-toplevel\|__file__\|REPO_ROOT\|...'` | 1 hit / 725 lines, CODE=1: `:73` `sys.path.insert(...abspath(__file__))`. Also established the corpus-root line is **not** among those patterns — which is why the row declines to assert a mechanism it could not find. |

## State at close

- Proof-of-spec **VALID rc=0**, 0 violations, 8 artifacts resolved:
  `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_SYSPARITY.TO-RB1-SITEZ.rule-bank-version-drift.proof_of_spec.json`
  RB1-AC1/AC2/AC3 **PASS**, RB1-AC4 **UNVERIFIABLE-BY-INSTRUMENT** (judgment, reserved).
- Commits `5f90753a25` (bump), `cce83eae14` (drain), `b441f6e2c4` (row). Push state **LOCAL**.
- **Open:** RB1-AC4's pin question, and row Z-S1's remedy (`.tools` is `1.0.0_SA_CTO~Z`'s lane).
