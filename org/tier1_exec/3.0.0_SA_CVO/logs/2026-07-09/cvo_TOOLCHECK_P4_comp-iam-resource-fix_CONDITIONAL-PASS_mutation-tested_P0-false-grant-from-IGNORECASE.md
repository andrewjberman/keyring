# CVO — P4 verify: `comp-iam` resource fix. **CONDITIONAL PASS.** Mutation-tested: the controls are real. Three defects; the P0 suppresses the verdict the fix exists to emit.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~01:59–02:05Z · **Agent:** 3.0.0_SA_CVO
**TO:** `NFRA_TOOLCHECK.P4` §8 — *verifier != do-er.* Do-er: `0.8.0_AE_CloudComp` (handoff `015904Z`).
**Subject:** `org/modules/graph/extract_iam.py`, `iam_cli.py`, `tests/test_iam_resource_verdicts.py` (uncommitted).
**Scope:** verifier wrote nothing under `org/modules/graph/`. All mutation done in an isolated copy.

---

## 1. The do-er's central request, answered: **the control is NOT fake**

He wrote: *"I only proved the OLD function's invariance as a fixture. I have not mutated the source to prove they
fail. Mutation-test it."* That is the correct request, and nobody else in this fabric made it tonight.

| mutation | result |
|---|---|
| **M1** — neutralize `_iam_resource_matches` (always `True`) | **15 RED by name** — incl. all 4 params of `test_the_old_action_only_logic_would_have_passed_every_negative_control`, `test_the_invariance_is_gone`, `test_time_travel_the_original_incident_reds` |
| **M2** — collapse `INDETERMINATE` → covered (`None`→`True`) | **1 RED** — `test_unresolved_tf_interpolation_is_indeterminate`. Thin, but it bites. |

**The assertions fail when the property is false.** They are tests, not decoration. Baseline: 31 pass.

## 2. I attacked his declared weakest point (#2) and **failed** — recorded as a negative finding

    policy b/pub/*  vs  arn b/*     -> False   (does NOT over-cover)
    policy b/*      vs  arn b/x/*   -> True    (correctly covers)

The `fullmatch`-coverage rule is conservative, as he claimed. **His instinct pointed at the right line and was one
token off.**

## 3. P0 — **FALSE GRANT** via `re.IGNORECASE`

    return re.fullmatch(pat, arn, re.IGNORECASE) is not None      # extract_iam.py ~:505

S3 bucket names are lowercase by AWS constraint; **S3 object keys are case-sensitive, and IAM Resource-ARN matching
on the resource-id is case-sensitive.** Exercised against the live function — **3/3 false GRANTs**:

    policy .../Public/*     arn .../public/secret.json   -> True
    policy .../PUBLIC/*     arn .../public/secret.json   -> True
    policy .../platinum/*   arn .../PLATINUM/x.json      -> True

**Direction of harm:** a false GRANT **suppresses `UNGRANTED-RESOURCE`** — precisely the verdict this fix exists to
produce. The defect he repaired (output independent of the resource) survives, in the same expression, as *output
independent of the resource's case*.

**Grounding, stated honestly:** I **exercised** `_iam_resource_matches`; the three `True`s are fact. The claim that
**AWS** would `implicitDeny` them rests on AWS's documented ARN-matching semantics — **INFERRED, not exercised.**
Per Rule 22a that limb closes with a `simulate-principal-policy` run on a case-mismatched key, which is the do-er's
to run and which he already has standing. **I did not write "proof."**

## 4. P1 — the `None` discipline is asymmetric. Same sin, opposite direction, same function.

He refuses `None`→`True` (correct; M2 defends it). But the ARN is built by **his own parser**, whose comment says
`resource_arn may contain '*' where a segment could not be statically resolved`. Exercised:

    policy arn:aws:s3:::opal-data-inf/gold/*   arn arn:aws:s3:::*/gold/meta.json   -> False (UNGRANTED)

The bucket segment is `*` **because he could not resolve it.** Truth is INDETERMINATE; the function returns a
definitive negative. **The tri-state is applied to the policy's uncertainty and never to the scanner's own.**
For `comp-iam gaps` that reads "you are missing a permission" → a grant gets added that was never needed → his own
defect class, inverted into over-permission.

## 5. P1 — a vacuous control **inside the suite written to eliminate vacuous controls**

    assert len(st['dropped_detail']) == st['dropped']     # test_attach_census_is_populated_and_closes

`extract_iam.py:1485` → `dropped += 1`; `:1488` → `dropped_detail.append(...)`. **Unconditionally paired, same
branch.** The assertion compares a counter to the length of the list that produced it. **It cannot fail.**

He told me *"check the contents, not the count."* His own assertion checks the count against the length of the thing
that generated the count. And **no test asserts `26`, and none asserts that the NEVER#1 cross-firm Deny belts are
among the dropped** — the highest-stakes content in the entire finding is asserted nowhere. `deny_detail` /
`deny_unparsed` exist (`:1499-1501`, CTO arch-gate, today) and nothing tests them.

## 6. P2 — the census test is not hermetic

`test_attach_census_is_populated_and_closes` calls `E.build_iam_report(_P('.'))` — it reads the **live** terraform
tree from CWD. **It went RED on my unmutated scratch copy**, which is how I found it: my M0 control failed before I
had mutated anything. An integration test in a unit test's clothes; `tf_files > 0` / `attached > 0` are
estate-dependent thresholds whose meaning drifts silently as terraform changes.

## 7. Correction to the TO's own headline finding — and it changes AC-7

COO's P4 dispatch cites `iam_cli.py:216  granted = role.grants(action)  -- the resource is never passed`.
**That line is role-listing code, and the claim as stated is false.**

    extract_iam.py:669   def grants(self, action: str) -> bool     <- resource-BLIND. Callers: extract_iam.py:1743, iam_cli.py:557
    extract_iam.py:~692  def resource_verdict(self, action, arn, exact)  <- resource-AWARE. Callers: iam_cli.py:244, :429

**`comp-iam` is not uniformly resource-blind. It carries two functions answering the same question at different
arity, and the caller chooses.** That is worse than a missing limb and it is a different fix. **AC-7 as written
("run the OLD P1 method against comp-iam; it must pass; the NEW framework must reject it") does not bind until it
names WHICH surface** — `gaps`/coverage (`grants`, blind) or the resource surfaces (`resource_verdict`, aware).
I have **not** traced which surface produced the `GRANTED`-before-and-after table; that limb is unverified.

## Disposition

**CONDITIONAL PASS. NOT CERTIFIED.** The core claim — `comp-iam` now compares the resource, and the controls that
say so are real — is **CONFIRMED by mutation**. The P0 must close (case-sensitivity + the `simulate` exercise);
the asymmetric `None` and the tautological assertion are P1 and must land first. Verifier is not do-er.

**AC-0 cross-validation:** his `universe = 60` matches mine **exactly**, reached independently by a different match
rule (67 raw − 5 impl-twins − 2 test harnesses). **Two instruments, two rules, one answer** — the first number
tonight that cross-validated. His `40 UNRESOLVED` is not yet adjudicated.

## grounding

- **desired:** `extract_iam.py:492-508` (`_iam_resource_matches`), `:669` (`grants`), `:1485/:1488` (drop counters),
  `:1499-1501` (deny stats); `tests/test_iam_resource_verdicts.py`
- **applied:** baseline suite 31/31 green on the working tree
- **exercised:** M1 → 15 RED by name; M2 → 1 RED; attack-3 (over-coverage) → could not break; 3/3 false GRANTs from
  `IGNORECASE`; unresolved-bucket ARN → `False`; M0 control RED on an unmutated copy (non-hermetic census test)
- **NOT established:** that AWS `implicitDeny`s the case-mismatched keys (documented semantics, **not exercised**);
  which comp-iam surface produced COO's before/after `GRANTED` table; the `40 UNRESOLVED`

## What you should have asked but did not

**"Which of our passing assertions have ever been observed to fail?"**

Not "are they green" — every one of them is green, that is what shipping means. *Have they ever gone red?* An
assertion that has never failed has never been tested; it has merely been run, and it is indistinguishable from
`assert True` until the day you mutate the thing it guards. Tonight one suite in this estate had that question asked
of it, and it survived — **because the do-er asked the question about his own work, in writing, to the person
empowered to hurt him with it.**

The tautology at `len(dropped_detail) == dropped` is the counterexample sitting inside the same file: green since
the hour it was written, guarding nothing, and it would have stayed green through every future regression of the
census it claims to certify. It is the sixth vacuous control tonight and the second I have found in an instrument
built specifically to catch vacuous controls.

**Mutation testing is not a nicety. It is the only negative control we own that we did not choose ourselves** — and
choosing them is how five instruments passed, all night, on the night they were wrong.

— 3.0.0_SA_CVO
