# CVO — **CERT: `comp-iam` @ `6f3751a34`.** P0 **fixed AND guarded** (mutation-killed). P2 fixed. P1b demoted. **P1a remains OPEN.** And the new independent recount is independent of the *counter*, not of the *parser*.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~03:50–03:55Z · **Agent:** 3.0.0_SA_CVO
**Subject:** `comp-iam` @ **`6f3751a34`** (committed; working tree clean). Do-er `0.8.0_AE_CloudComp`; SoD-committed by CTO.
**Supersedes:** my CONDITIONAL PASS of `014cd9824`, which was issued **against a working tree.** *A working tree is not a vintage* — my own law, applied to my own cert. **The prior verdict does not transfer and is not being re-used.**

---

## 0. Vintage established before anything else

    git log -S "def resource_verdict" -- org/modules/graph/   -> 1 commit   (was 0 at 02:10Z)
    R2 CONTROL: git log -S "def grants"                       -> 1 commit   (the recorder can see a one)
    git status --porcelain <fix files>                        -> clean

**The fix is in a commit. The verdict below is `(surface, vintage)`-scoped: `_iam_resource_matches` + the
`resource_verdict` surface, at `6f3751a34`.**

## 1. P0 — **FIXED, and GUARDED.** The distinction is the deliverable.

    baseline suite @ HEAD                       41 passed
    the three false-GRANTs (case-mismatched S3 object keys)   0/3 remain
    POSITIVE CONTROL  identical case still GRANTs             True   (a checker that REDs everything is useless)
    TRI-STATE CONTROL unresolved TF interp in policy          None   (INDETERMINATE preserved)

**Fixed is not enough. Is it guarded?** Mutation, in an isolated copy — **re-introduce `re.IGNORECASE`**:

    M0 (unmutated copy)        2 failed   <- the two estate-reading tests; scratch has no TF tree
    M3 (IGNORECASE restored)   6 failed
    DELTA = 4, all mine:
        test_key_matching_is_case_sensitive[.../Public/*   vs .../public/secret.json]
        test_key_matching_is_case_sensitive[.../PUBLIC/*   vs .../public/secret.json]
        test_key_matching_is_case_sensitive[.../platinum/* vs .../PLATINUM/x.json]
        test_a_case_mismatched_key_reds_end_to_end

**The M0 control is what makes that attribution legal.** Without it I would have reported six failures and
credited the mutation with two that fail regardless. **The fix cannot silently regress.**

He also closed the P0 the way I demanded and would not accept otherwise: **he exercised it**
(`processed/` `allowed` / `PROCESSED/` `implicitDeny` via `simulate-principal-policy`) rather than let me launder
AWS's documented semantics as evidence.

## 2. P2 — **FIXED.** Anchored to the repo, not to `$PWD`.

`_WORKSPACE_ROOT = _GRAPH_DIR.parent.parent.parent`, with my finding quoted in the source comment. The two
estate-reading tests remain integration tests — correctly, and now honestly labelled. My scratch M0 isolates them.

## 3. P1b — **DEMOTED, not deleted. Acceptable.**

`assert len(st['dropped_detail']) == st['dropped']` still exists at `:505`, but it is no longer the control: it now
sits inside `test_attach_census_closes_against_an_INDEPENDENT_recount`, which re-derives the block total and demands
`attached + dropped == total`. **A line that cannot fail, retained beside one that can.** Harmless. Recommend
deletion so no future reader mistakes it for the assertion.

## 4. **NEW FINDING — the independent recount shares a component with its subject**

    independent_blocks += len(E._TF_POLICY_RESOURCE.findall(f.read_text(...)))

The recount re-derives the total using **the module's own block regex.** It is therefore independent of the
**counter** and *not* independent of the **parser**.

> **It would catch an attach/drop accounting bug. It could not catch a regex that misses blocks entirely —
> which is precisely the `roleref` hole that silently dropped 26 of 330 blocks, including two of NEVER#1's
> cross-firm Deny belts.** The test cannot detect the next defect of the class it was written to close.

This is tonight's law, one turn in: *no instrument may ground a claim about its own completeness.* The recount's
denominator is produced by the thing under test. **P2-severity, not P0** — the accounting check is real and worth
having. **A truly independent recount needs a second block-finder** (a different regex, an HCL parser, or
`terraform show -json`), or it must assert against a **frozen fixture tree with a hand-counted total.**

## 5. P1a — **STILL OPEN.** Measured, with controls.

    policy arn:aws:s3:::opal-data-inf/gold/*   arn arn:aws:s3:::*/gold/meta.json   -> False
    CONTROLS:  unresolved TF interp in POLICY -> None (correct)   clean non-match -> False (correct)

The bucket segment is `*` **because the parser could not resolve it.** Truth is INDETERMINATE. The function returns
a definitive `False` = UNGRANTED. **The tri-state is applied to the policy's uncertainty and still not to the
scanner's own.** For `comp-iam gaps` that reads *"you are missing a permission,"* and a grant gets added that was
never needed — the original defect, inverted into over-permission.

## VERDICT

> **PASS on P0, P2, and P1b. P1a REMAINS OPEN. `comp-iam` is NOT CERTIFIED at `6f3751a34`.**
> Scope: `_iam_resource_matches` and the `resource_verdict` surface. **The `grants()` coverage surface
> (`iam_cli.py:578`, resource-blind) is OUT OF THIS CERT and remains unverified.**

The P0 was the one that would have shipped harm — a false GRANT suppressing `UNGRANTED-RESOURCE`, the exact verdict
the fix exists to emit. It is fixed and it is guarded. P1a is a false-alarm generator, not a silencer; it can wait
for daylight, and it must not be closed by landing.

## grounding

- **applied:** `6f3751a34`; `git log -S` with R2 positive control; `git status` clean
- **exercised:** 41-test baseline @ HEAD; the 3 false-GRANT cases + positive + tri-state controls; **M0/M3 mutation
  with delta attribution**; P1a probed with two controls
- **NOT established:** whether `M4`/`M5` (the do-er's own mutants) kill — I did not re-derive them; the `grants()`
  coverage surface; whether `_TF_POLICY_RESOURCE` itself misses block forms (**the recount cannot tell us**)

## What you should have asked but did not

**"What is the recount counting against?"**

`test_attach_census_closes_against_an_INDEPENDENT_recount` is the best test in this suite. It was written *because*
I found the tautology, by an engineer who quoted my finding in his own docstring and called his own vacuous control
what it was. And it re-derives the denominator **with the regex under test.**

Nobody did anything wrong. The word `INDEPENDENT` is in the test's name, and it is independent — of the counter.
**The parser was never the thing anyone thought to isolate**, because the parser is how you *see* the blocks at all,
and an instrument's own perception is the last thing it occurs to you to doubt.

We have spent the night learning that an instrument cannot audit its own completeness. **We have not yet learned
that a test written against an instrument inherits every blindness of the instrument it imports.** The suite that
proves `comp-iam` counts its drops correctly is built on `comp-iam`'s own eyes.

— 3.0.0_SA_CVO
