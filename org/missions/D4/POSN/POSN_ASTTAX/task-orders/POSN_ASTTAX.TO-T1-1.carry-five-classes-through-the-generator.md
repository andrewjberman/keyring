# TO POSN_ASTTAX.TO-T1-1 -- make the positioning generator CARRY all five ratified asset classes end to end, so a correctly-tagged ticker renders under its own label with its weight intact (AT3-s-1, FWD-1/FWD-2)

<to_id>POSN_ASTTAX.TO-T1-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~10</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-1` · **Issuance:** round 3. **CHAIN HEAD -- `AT3-s-5` and
everything behind it depend on this.**

---

## THE CELL

`C-RETAG-SAFETY`, re-founded. The constraint's LIVE mechanism is **SILENT ZEROING, NOT BLANKING**:
`AT2-s-6` killed the KeyError, so a retag no longer crashes the generator. Instead the served output
maps hold FOUR keys and `.get(asset_class_raw, 'Unknown')` everything else, and the allocation
`if/elif` chain has **no `else`** -- so a `Commodities` or `Structured` value renders as the literal
string `'Unknown'` and its weight accumulates to 0.000.

⛔ **THE HAZARD GOT QUIETER, NOT SAFER.** A blank page is noticed in seconds; a zeroed allocation line
looks like a real allocation. This cell removes that.

⚠ **DO NOT INHERIT THE 17/3/14 COUNT.** Those figures are pinned to `TO-S7-1`'s run and
`3.0.0_SA_CVO~Z` records that `AT2-s-1` has since repaired a benchmark hop. **Re-measure the hop set at
your own vintage and print your own denominator.** The VERDICT is current (both classes still display
as `Unknown`); the RATIO is history.

## THE ACT

1. **Re-measure the hop set** (`T1-AC1`): every site where an `asset_class` value is mapped, branched,
   bucketed or rendered on the served path. Your denominator, not round 2's.
2. **Make every one of them carry all five ratified classes** -- Fixed Income/Cash, Equity, Structured,
   Commodities, Alternatives -- so a value outside the legacy four renders under its own label rather
   than collapsing to `'Unknown'`.
3. **Give the allocation chain an explicit `else`** so an unmatched value can never silently zero a
   weight. ⛔ It must be LOUD: a WARN naming the value, not a silent bucket.
4. **Prove it with a before/after that FAILS on the old bytes** (`T1-AC3`).
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **DO NOT RETAG ANY REGISTRY ROW.** This cell changes how a value is CARRIED, never what any row is
  TAGGED. `AT3-s-6` owns the retag and is gated behind the bar.
- ⛔ **DO NOT DEPLOY.** Source change only; `aws lambda update-function-code` is forbidden estate-wide.
- ⛔ **DO NOT MINT A SIXTH CLASS.** The five are ratified. If you find a served value outside them, that
  is a ROW, not a new key.
- ⚠ `AT2-s-1` added a sentinel (`UNCLASSIFIED_ASSET_CLASS = 'unclassified'`) and the
  `asset_class_recognized` / `assetClassRecognized` flags. **Do not remove or duplicate them** -- an
  unrecognised value and a real-but-uncarried class are DIFFERENT states and must stay distinguishable.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W10-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T1-AC1" cell_refs="AT3-s-1"><invocation>timeout 120 comp-read infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py --enumerate 'asset_class'</invocation><expect>the enumerate DENOMINATOR at THIS vintage and every banded hit, each classified as dict-key construction, subscript, comparison branch, output field, or mention; and the subset that is a SERVED-PATH hop named with file:line. The count is yours, not TO-S7-1's.</expect></criterion> `T1-AC1` -- THE HOP SET, RE-MEASURED AT YOUR OWN VINTAGE.

<criterion id="T1-AC2" cell_refs="AT3-s-1"><invocation>timeout 120 python -c "import ast; src=open('infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py',encoding='utf-8').read(); ast.parse(src); print('AST-OK', len(src.splitlines()),'lines')"</invocation><expect>AST-OK with a line count, proving the edited file still parses.</expect></criterion> `T1-AC2` -- IT STILL PARSES.

<criterion id="T1-AC3" cell_refs="AT3-s-1"><invocation>timeout 180 python &lt;your before/after harness&gt;</invocation><expect>for EACH of Commodities, Structured and Alternatives, two runs side by side on the SAME input: BEFORE (old bytes) the served asset_class reads the literal 'Unknown' AND the weight is 0.000; AFTER it reads the class's own label AND the weight is non-zero and equal to the input weight. Both outputs pasted verbatim, and a FALSIFY arm running the old bytes in BOTH positions that must FAIL.</expect></criterion> `T1-AC3` -- ⭐ **THE CONTROL THAT MUST FAIL ON THE OLD BYTES.** A five-class value that renders is not enough: the WEIGHT is half the defect and the half that hides.

<criterion id="T1-AC4" cell_refs="AT3-s-1"><invocation>timeout 120 python &lt;your no-else probe&gt;</invocation><expect>an unmatched/garbage asset_class value fed through the allocation chain: it must NOT silently accumulate to 0.000 and must emit a WARN naming the value. Paste the WARN verbatim. State what the value does to the totals.</expect></criterion> `T1-AC4` -- THE SILENT-ZERO PATH IS CLOSED AND SAYS SO OUT LOUD.

<criterion id="T1-AC5" cell_refs="AT3-s-1"><invocation>timeout 120 git -C . diff --stat HEAD -- infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>the diffstat verbatim, showing no registry, infrastructure or portal path was touched.</expect></criterion> `T1-AC5` -- THE WRITE SURFACE STAYED INSIDE THE CELL.

<criterion id="T1-AC6" cell_refs="AT3-s-1" judgment="true"/> `T1-AC6` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the five classes are now carried at the SERVED grain end to end, or only at the hops this cell happened to enumerate. **Record the readings and offer NO verdict.**

<expected_criteria>T1-AC1, T1-AC2, T1-AC3, T1-AC4, T1-AC5, T1-AC6</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T1-1.carry-five-classes-through-the-generator.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~10/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-1`.
<owned_cells>AT3-s-1</owned_cells>
Read-dependencies, NOT claimed: `AT3-s-5` measures the bar this cell makes meetable; `AT3-s-6` retags only after that bar reads GO. Neither is yours.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, Terraform or AWS write; source change only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied: the issuer did NOT re-measure the hop set after `AT2-s-1`'s benchmark-hop repair, so the
round-2 ratio is known-historical and AC1 is this round's first independent count.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~10/POSN_ASTTAX.TO-T1-1.carry-five-classes-through-the-generator.proof_of_spec.json
</proof_of_spec>
