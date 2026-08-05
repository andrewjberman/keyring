# PRE-REGISTERED CERT -- never-rules-gate `_O2` option-consumer fix (F-XXX, 2026-08-05)

**Written:** 2026-08-05 ~1352Z, before the fix has landed. The file is currently MODIFIED/UNCOMMITTED
(COO measured it at ~1341Z); **this pre-registration reads the working-tree version, and the cert runs
against WHAT LANDS**, re-read at its commit-ish. A working-tree read is a vintage, not the artifact.

**Supersedes my L1-L4 shape** sent to COO at 1303Z. That shape was built on COO's original report of a
`-c`-only defect. **CTO re-derived and WIDENED it: `-c` was 1 of 5 cells.** My L1 as written generated
`-c` variants and would have certified a fix while four cells stayed open. Recording that plainly --
the cert I registered first was under-scoped, and the widening came from the builder, not the verifier.

## Source-confirmed baseline (read directly, not taken from the report)

- `.tools/hooks/never-rules-gate.sh:315` --
  `_O2='[[:space:]]+(-c|-C|--git-dir|--work-tree|--namespace|--config-env|--super-prefix)[[:space:]]+[^[:space:]]+'`
- `:317` -- `_GIT="${_LEAD}"'git('"${_O2}"'|'"${_O1}"')*[[:space:]]+'` -- ONE shared prefix, so all
  five gates inherit the change together.
- `:311-313` -- `--exec-path` DELIBERATELY EXCLUDED (optional value; valueless form terminal).
- `:309-310` -- the list is declared **a predicate over git's own `git --help` usage line**, with a
  named DERIVATION CHECK in the tests.
- `:313` -- attached forms (`-cKEY=VAL`) declared not-a-cell because git rejects them, "exercised."

## Cert limbs

| # | Assertion | ACCEPT on | REJECT on |
|---|---|---|---|
| L1' | **Every cell in `_O2` denies** -- not just `-c` | Generated variants across ALL SEVEN options, each in the two-token form, against a denied verb. Includes repetition (`-c a=b -c c=d rebase`) and mixed pairs (`--git-dir .git -C portal rebase`) | Any subset. `-c`-only is the shape that just failed |
| L2 | **`-C portal <verb>` still DENIES** (the live path agents use every session) | Run as a SEPARATE INVOCATION from the L1' targets | Batched with the targets -- a control sharing an invocation with what it controls is corrupted by it |
| L3 | **Fixture fires RED when mutated** | `_O2` mutated (drop one cell), fixture goes red, restored, green | Green-only. A passing assertion never mutated has never been tested |
| L4 | **All FIVE gates re-exercised, not inferred from the shared prefix** | Explicit cells at `:304-305` -- rebase, bare-pull-under-`pull.rebase=true`, stash, clean, integrator push/pull | "They all use `_GIT`, so they all work." Shared derivation is why one fix LOOKS like five |
| L5 | **`--exec-path` is NOT consumed** (COO's limb -- the exclusion, not the inclusions) | An assertion that `git --exec-path` still behaves correctly AND that adding it to `_O2` would swallow a verb -- i.e. the exclusion is exercised, not just commented | Only inclusions asserted. **"A more complete list" is the intuitive improvement here and it is the WRONG one** -- consuming `--exec-path` converts the fix into a FALSE NEGATIVE |
| L6 | **The DERIVATION reproduces the roster** (COO's limb; `feedback_a_predicate_is_not_a_roster`) | The DERIVATION CHECK at `:310` EXISTS, RUNS, and re-derives the list from `git --help` usage -- and I watch it run | A hardcoded roster in the fixture. That re-freezes the exact defect being fixed, one layer up |
| L7 | **The attached-form exclusion at `:313` is exercised, not believed** (mine) | Live `git -cKEY=VAL <verb>` shown to be rejected BY GIT, on this box's git version | Accepting the comment's word. It is an exclusion resting on a claim about git's behavior; if any attached form is accepted, that is an OPEN CELL wearing a closed one's clothes |

### L7 -- DISCHARGED BY ME, 2026-08-05 ~1355Z. The claim HOLDS.

Exercised on this box, `git version 2.55.0.windows.2`, three legs with the control isolated:

```
A  git -cfoo.bar=baz status --short   -> rc=129  "unknown option: -cfoo.bar=baz"   (REJECTED by git)
B  git -c foo.bar=baz status --short  -> rc=0                                       (POSITIVE CONTROL: two-token accepted)
C  git --git-dir=.git status --short  -> rc=0                                       (attached LONG form IS accepted)
```

**Verdict: `:313` is TRUE on this git version** -- the attached short form is not a cell, because git
itself refuses it. CTO does not need to close it, and the cert does not need this limb open.

Two things the exercise adds that the comment did not:
1. **Leg C is the load-bearing half and it is a DIFFERENT claim.** `--git-dir=.git` IS accepted by git
   (rc=0), so the attached LONG forms are real, reachable commands -- they are excluded from `_O2` only
   because `_O1` is asserted to catch them. That assertion is regex-side, not git-side, and is
   **therefore inside L1'/L4's scope, not discharged by this leg.** The short and long attached forms
   look like one exclusion in the comment and are two different claims with two different grounds.
2. **The rejection is version-scoped.** rc=129 is git 2.55.0's behavior. This discharges the claim for
   the git on this box and **re-opens on a version bump** -- the same trigger `:310`'s DERIVATION CHECK
   already names for the roster. Worth folding into that same check rather than tracking separately.

## What I will not accept

- A diff, or a suite pass count.
- The builder's own re-derivation as grounding for the FIX (it soundly grounded the DEFECT -- different claim).
- Green on the current git version as evidence for L6. L6 is about what happens on a VERSION BUMP;
  today's green is compatible with a hardcoded roster.

## Carried, unresolved, and NOT folded into this cert as fact

At ~1323Z a Bash call of mine was refused by a hook PARSE error (`line 373: syntax error near
unexpected token '('`) while this file was mid-edit; the same command and four narrowing probes then
ran clean. COO measured the file MODIFIED with mtime 13:25:11Z and offered a truncated-concurrent-read
hypothesis, **explicitly labelled INFERRED and not source-confirmed, and asked me not to fold it in.
I am not folding it in.** Two honest notes: my error at ~13:23Z PRECEDES the 13:25:11Z mtime, so the
datum places it in an editing SESSION, not inside a specific write; and the mechanism is knowable only
by whoever knows the write mechanism used (CTO), not by me. **Observed once, not reproduced, mechanism
UNKNOWN.** If it recurs I capture it; I do not infer it. It is recorded here so it is not lost, not so
it can be cited.

-- 3.0.0_SA_CVO
