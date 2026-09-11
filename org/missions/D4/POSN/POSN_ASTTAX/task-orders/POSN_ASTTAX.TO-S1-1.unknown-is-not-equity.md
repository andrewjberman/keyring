# TO POSN_ASTTAX.TO-S1-1 -- make UNKNOWN distinguishable from `equity`: the registry cannot keep securities PROPERLY TAGGED while "properly tagged equity" and "not recognised" are the same string (AT2-s-1, FWD-1)

<to_id>POSN_ASTTAX.TO-S1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~6</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5** ·
**Decomp cell:** `AT2-s-1` · **Issuance:** round 2. **PRIMARY. Independent chain head; depends on `AT2-s-6`.**

---

## THE CELL

`C-CLASSIFIER-PURPOSE` **(c)**: `equity` is BOTH a ratified class AND the positioning lambda's
unknown-default. Andrew's purpose ruling is that the registry exists to keep securities **properly
tagged** -- and a bucket where "properly tagged equity" and "not recognised" are the same string is
precisely the thing that cannot be audited.

**MEASURED by round 1 (`S1a-AC8`), re-take it:** three unknown-default call sites in one file, and they
DISAGREE -- `:209` -> `fixed_income` ("Default to FI if unknown"), `:360` and `:520` -> `equity`.

⭐ **AND THIS IS THE ONE CELL WHOSE OUTCOME THE BROKEN SYSTEM ALREADY PASSES.** FWD-1's bar -- "every
holding lands in exactly one class" -- is satisfied today by a default that files everything unrecognised
as Equity. **Your criteria must assert the unknown case explicitly or they cannot grade the fix.**

## THE ACT

1. **Re-take the three sites** (`S1-AC1`) and state each one's default.
2. **Make an unrecognised ticker RENDER AS UNRECOGNISED**, not silently absorbed. ⚠ **The shape is yours
   to choose and to state**: a distinct sentinel class, a separate unclassified bucket, or an explicit
   flag alongside the class. **State which and why in the instance.**
3. ⛔ **DO NOT SIMPLY UNIFY THE THREE DEFAULTS.** Making all three default to the same class is a smaller,
   plausible change that leaves the defect exactly in place -- unknown would still be indistinguishable
   from a real class, just consistently so. If you conclude unification is nonetheless the right first
   step, say so explicitly and name what it does NOT fix.
4. **Prove with a negative control that fails on the old code** (`S1-AC3`): a ticker absent from the
   registry must be distinguishable from a genuine equity holding AFTER, and must NOT be before.
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RETAG ANY REGISTRY ROW.** This cell changes how an ABSENT ticker is handled; it does not
  reclassify present ones. `AT2-s-2` owns retagging.
- ⛔ **DO NOT DEPLOY.** Source change only; `aws lambda update-function-code` is forbidden estate-wide.
- ⚠ **YOU SHARE A FILE WITH `AT2-s-6`.** It hardens the allocation dicts and the default GUARD; you change
  what the default MEANS. Verify `AT2-s-6` is terminal first (`S1-AC5`) and do not re-do its work.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W6-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="S1-AC1" cell_refs="AT2-s-1"><invocation>timeout 120 grep -n "Default to\|registry_field(ticker, 'asset_class'" infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>every numbered line pasted verbatim, the `asset_class` subset separated from other fields, each with its default named, and the count of DISTINCT defaults across the asset_class sites only.</expect></criterion> `S1-AC1` -- THE THREE SITES AND THEIR DISAGREEMENT, RE-TAKEN. ⚠ The pattern also returns a `management_style` line; separate it, do not count it.

<criterion id="S1-AC2" cell_refs="AT2-s-1"><invocation>timeout 120 python -c "import ast; src=open('infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py',encoding='utf-8').read(); ast.parse(src); print('AST-OK', len(src.splitlines()),'lines')"</invocation><expect>AST-OK with a line count, proving the edited file still parses.</expect></criterion> `S1-AC2` -- THE FILE STILL PARSES.

<criterion id="S1-AC3" cell_refs="AT2-s-1"><invocation>timeout 180 python &lt;your negative-control script&gt;</invocation><expect>TWO runs side by side for a ticker ABSENT from the registry: BEFORE, it is indistinguishable from a genuine equity holding; AFTER, it is distinguishable, and the means of distinguishing is named. Both outputs pasted verbatim.</expect></criterion> `S1-AC3` -- ⭐ **THE CONTROL THAT MUST FAIL ON THE OLD BYTES.** The broken system passes FWD-1 already; only a before/after separates the fix from the status quo.

<criterion id="S1-AC4" cell_refs="AT2-s-1"><invocation>timeout 120 git -C . diff --stat HEAD -- infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>the diffstat pasted verbatim, showing no registry or infrastructure path was touched.</expect></criterion> `S1-AC4` -- THE WRITE SURFACE STAYED INSIDE THE CELL.

<criterion id="S1-AC5" cell_refs="AT2-s-1"><invocation>timeout 120 grep -n "<status>" ../task-orders/POSN_ASTTAX.TO-S6-1.harden-the-generator.md</invocation><expect>the status line pasted verbatim reading `complete`; if not, this order STOPS and files a row rather than editing the same file underneath an unfinished cell.</expect></criterion> `S1-AC5` -- THE SHARED-FILE PREDECESSOR IS DONE.

<criterion id="S1-AC6" cell_refs="AT2-s-1" judgment="true"/> `S1-AC6` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether "not recognised" is now genuinely distinguishable from a real class at the served grain, or only inside the generator. **Record the readings and offer NO verdict.**

<expected_criteria>S1-AC1, S1-AC2, S1-AC3, S1-AC4, S1-AC5, S1-AC6</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-S1-1.unknown-is-not-equity.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~6/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round2.md</decomp_doc> round 2, cell `AT2-s-1`.
<owned_cells>AT2-s-1</owned_cells>
Read-dependency, NOT claimed: `AT2-s-6` shares this file and must be terminal first (`S1-AC5`).
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, Terraform or AWS write; source change only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool; the three call sites are round 1's measured
finding (S1a-AC8, instance at HEAD) and AC1 re-takes them at this worker's vintage.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~6/POSN_ASTTAX.TO-S1-1.unknown-is-not-equity.proof_of_spec.json
</proof_of_spec>
