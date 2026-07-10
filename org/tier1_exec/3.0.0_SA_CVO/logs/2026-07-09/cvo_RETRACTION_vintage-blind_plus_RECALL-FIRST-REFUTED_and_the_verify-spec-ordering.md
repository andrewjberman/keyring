# CVO — **RETRACTION** (I was vintage-blind) · **"recall before precision" REFUTED on the live tool** · the corrected verify-spec ordering · 32/60 tools have no test at all

**archetype:** VALIDATE

**Date:** 2026-07-10 ~02:10–02:20Z · **Agent:** 3.0.0_SA_CVO
**Retracts:** the "COO's P4 headline citation is WRONG" claim in `014cd9824` §7.
**Answers:** Andrew — *"the core element is essentially establishing recall first before precision."*

---

## 1. RETRACTION. My correction of COO was wrong, and it was wrong the way I have been correcting everyone else.

I wrote that `iam_cli.py:216` is role-listing code and that COO's citation was false. **Verified at source, with
retrieval controls** (`git show <ref>:<path>` → 416 / 1247 lines, so a real file, not a `fatal:` I would have grepped
zero from):

    @ ed415e268   iam_cli.py:216   granted = role.grants(action) if role else None     <- COO/CTO CORRECT
    @ HEAD        iam_cli.py:216   granted = role.grants(action) if role else None     <- STILL grants()
    @ worktree    iam_cli.py:216   return                                              <- what I read

`git log -S "def resource_verdict"` → **0 commits.** R2, the control on the control: `git log -S "def grants"` → **1
commit** (the recorder *can* see a one, so the zero is real); `-S "<never existed>"` → 0. Both files are `MM`.

> **`resource_verdict` exists in no commit. It is `0.8.0`'s UNCOMMITTED fix. I read the repaired tree and used it
> to adjudicate a claim about the broken one.**

My derived point survives and COO upheld it (post-fix, `iam_cli.py:578` still calls the resource-blind `grants()`
on the coverage surface, so the fixed tool answers one question at two arities). **The attribution does not.**

**COO's rule — "a line citation without a vintage is not a citation" — is right and I am sharpening it, from my own
error:** the axis was **not** HEAD-vs-old-commit. `git show HEAD:` would have shown me `grants()` and I would still
have been wrong about `resource_verdict`. **The axis is COMMITTED vs WORKING TREE.** Only `git status` (`MM`) would
have saved me.

> **A working tree is not a vintage. It is a superposition of a commit and another agent's uncommitted edits.**
> Nothing in `sed`/`grep`/`Read` carries a vintage field, so the subject and the instrument shared a frame — which
> is tonight's law, committed by the person enforcing it, for the third time.

## 2. "RECALL BEFORE PRECISION" — REFUTED, by exercising the tool that reopened this project

Ground truth read off the policy; the **real** resource-blind `grants()` (the function at `ed415e268`, still live on
the coverage surface):

    TP=3  FP=2  TN=2  FN=0
    RECALL    = 1.00     <-- PERFECT. It never misses a real grant.
    PRECISION = 0.60     <-- where the defect lives.

**A recall-first gate PASSES `comp-iam`.** It also passes COO's watcher counter, which returned `>0` for every
serial including `9.9.9_NOBODY` — **recall 1.00, and no information.** *A tool that always says YES has recall 1.0
by construction.*

**What is right in the instinct, and it is real:** *"0 hits and my file has lines"* IS a recall claim made with no
recall measurement. That is the **always-NO** class — the empty set read as a negative answer.
**What it misses:** `comp-iam` and the watcher counter are the **always-YES** class. Both classes occurred tonight.

| ordering | catches always-NO (vacuous empty) | catches always-YES (undiscriminating) |
|---|---|---|
| recall-first | **yes** | **no** |
| precision-first | no | yes |
| **discrimination-first** | **yes** | **yes** |

**The primary property is DISCRIMINATION: does the verdict CHANGE when the truth changes?** Recall and precision are
both downstream of it, and each alone is trivially gamed by a constant function. `comp-iam` read `GRANTED` before
and after the grant landed — that is zero mutual information between verdict and truth, and it is invisible to
either rate alone.

## 3. Recommended ordering for the comp-tool verify suite (recommendation to CTO/COO — I do not author the PRD)

    AC-0  DENOMINATOR     state the universe + the MATCH RULE. Print the LIST, never the count.
    AC-1  DISCRIMINATION  the verdict must FLIP when the underlying truth flips, on the SAME subject.
                          Mechanism: mutation / before-after pair. A tool that cannot emit its own negative
                          verdict on any input has not been tested -- it has been run.
    AC-2  RECALL          against a GENERATED oracle set (inject known-true facts). Empty result != negative answer.
    AC-3  PRECISION       against generated known-false facts.
    AC-4  PROVENANCE      every verdict names (a) which limbs of the contract it evaluated, and
                          (b) THE VINTAGE OF ITS SUBJECT -- commit-ish, and "working tree" is not one.

AC-1 is where every one of tonight's six defects lived. AC-4(b) is tonight's newest lesson, and it is mine.

## 4. The sweep cannot start with verification. 32 of 60 tools have nothing to verify against.

Rule: a test file must contain the **literal** tool name (`comp-X`) or import its module. **Controls printed before
any number** — positive `comp-iam` → 7 files (PASS); negative `comp-zzz-never-existed` → 0 (PASS); trap `comp-to`
(two-letter stem) → 3 (PASS).

    TOOLS WITH A TEST THAT NAMES THEM :  28 / 60
    NO TEST ANYWHERE                  :  32 / 60   (53%)

**Among the 32 with no test at all:** `comp-surface-check` (the SEV1 critical-surface gate), `comp-firmsep-sweep`
(the NEVER#1 firm-separation sweep), `comp-tagauthz`, `comp-denytest`, `comp-deadgrant`, `comp-tool-health`,
`comp-tool-health-gate`, `comp-routable-check`, `comp-coverage-check`, `comp-secrets`, `comp-xray`, `comp-honesty`.

**The tools that guard firm separation, IAM denies, secrets, and the SEV1 surfaces are the tools with no tests.**

## 5. And my FIRST census of that was garbage — third time tonight

My initial rule matched a bare stem. `comp-to` reported **569 test files** (of 658). The stem is `to`. It matched
every file containing the substring. It also inflated `comp-types`, `comp-diff`, `comp-build`, `comp-which`, and
would have shipped **"43 of 60 tested, all with negative assertions"** — a reassuring, false, and completely
plausible number.

Caught because I printed the counts beside the names and `569` is absurd on its face. **Same defect as the eleven
phantom tools; same defect as COO's `example:`/`rationale:`/`scope:`; in the instrument built to measure whether our
instruments can be tested.** The corrected run carries a positive, a negative, and a trap control, printed first.

## grounding

- **applied:** `git show ed415e268:{iam_cli,extract_iam}.py` (416/1247 lines, retrieval control); `git status` → `MM`
  both; `git log -S "def resource_verdict"` → 0 with R2 positive control `-S "def grants"` → 1
- **exercised:** the real `E.IamRole.grants()` over a 7-pair ground-truth set → recall 1.00 / precision 0.60;
  the test-census under a bare-stem rule (`comp-to` → 569) vs a literal-name rule (`comp-to` → 3), with
  positive/negative/trap controls
- **NOT established:** whether the 32 untested tools are untested-and-correct or untested-and-broken. **That is the
  point: nobody can say, and until AC-1 runs, neither can I.**

## What you should have asked but did not

**"Which of our tools has ever been observed to emit its own negative verdict?"**

Not "does it have tests." Not "does it pass." *Has anyone ever seen `comp-surface-check` say NO?* Has anyone seen
`comp-firmsep-sweep` flag a violation? `comp-denytest` produce a deny? If a tool has never once printed its own
failing verdict on any input in its lifetime, then **its GREEN is indistinguishable from `print("PASS")`** — and we
have thirty-two of those guarding firm separation, IAM denies, secrets, and every SEV1 surface.

That is not a testing gap. It is the discovery that our safety rail may be a constant function, and the only reason
we do not know is that **the estate has never been in a state that should have made it red.** The instruments were
never wrong. They were never *asked*.

— 3.0.0_SA_CVO
