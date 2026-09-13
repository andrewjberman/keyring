# TO POSN_ASTTAX.TO-T3-1 -- HOP-TEST the two sibling consumers `TO-S7-1` enumerated but never tested, so a shared-shape INFERENCE becomes a measurement (AT3-s-3, FWD-1)

<to_id>POSN_ASTTAX.TO-T3-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~12</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-3` · **Issuance:** round 3. **GATES `AT3-s-6` (the retag).**

---

## THE CELL

`TO-S7-1` enumerated two sibling consumers of the same classification vocabulary and **did not hop-test
either**, declaring the shared-shape assumption as INFERENCE rather than measurement:

```
  yang-generate-allocation-summary        67 hits
  yang-generate-holdings-attribution      32 hits
```

⭐ **THAT DECLARATION IS WHY THIS CELL EXISTS, AND IT IS THE RIGHT KIND OF DISCLOSURE.** "They likely
share the shape" is a hypothesis. If either buckets `asset_class` into its own fixed-key structure,
the retag silently zeroes or mislabels there too -- in a surface nobody has looked at.

## THE ACT

1. **Enumerate each consumer's `asset_class` hops** (`T3-AC1`) with a printed denominator per file.
2. **Hop-test both against a five-class value** (`T3-AC2`): does `Commodities` SURVIVE, RAISE, or get
   SILENTLY DROPPED at each hop? ⛔ **"SILENTLY DROPPED" IS A FAILURE, not a pass** -- the same bar
   `TO-S7-1` used, because the same defect hides the same way.
3. **State whether the shared-shape inference held** (`T3-AC3`) -- named either way. A confirmed
   inference is a result; so is a refuted one.
4. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **READ-ONLY ON BEHAVIOUR; NO FIX.** If a consumer drops the value, that is a FINDING and a later
  cell, not an act here. A cell that fixes what it is measuring cannot report on it cleanly.
- ⛔ **DO NOT RETAG AND DO NOT DEPLOY.**
- ⛔ **DO NOT CONCLUDE FROM A PAGE.** `--all` or paginate.
- ⚠ These two consumers are OUTSIDE `AT3-s-1`'s write surface. If `AT3-s-1`'s fix does not reach them,
  say so plainly -- that is exactly the finding this cell exists to produce.
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W12-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T3-AC1" cell_refs="AT3-s-3"><invocation>timeout 180 comp-read infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-allocation-summary/lambda_function.py --enumerate 'asset_class'</invocation><expect>the enumerate DENOMINATOR and every banded hit for this consumer, each classified as dict-key construction, subscript, comparison branch, output field, or mention. Repeat the same read for yang-generate-holdings-attribution and paste both denominators. If either path differs from the one named here, state the path you actually read.</expect></criterion> `T3-AC1` -- THE HOPS IN BOTH SIBLINGS, WITH THEIR OWN DENOMINATORS.

<criterion id="T3-AC2" cell_refs="AT3-s-3"><invocation>timeout 180 python &lt;your hop-by-hop harness&gt;</invocation><expect>a table, one row per hop per consumer: file:line and whether "Commodities" SURVIVES, RAISES, or is SILENTLY DROPPED. Hops tested == hops enumerated in AC1, stated as a count. Every drop site named.</expect></criterion> `T3-AC2` -- ⭐ **THE DECISIVE TEST, AND SILENTLY DROPPED IS A FAILURE TOO.**

<criterion id="T3-AC3" cell_refs="AT3-s-3"><invocation>timeout 120 python -c "print('INFERENCE VERDICT RECORDED IN THE INSTANCE')"</invocation><expect>a stated verdict on whether TO-S7-1's shared-shape inference HELD or was REFUTED, with the evidence named; and whether AT3-s-1's generator fix reaches these two consumers or stops short of them.</expect></criterion> `T3-AC3` -- THE INFERENCE, NOW MEASURED, NAMED EITHER WAY.

<criterion id="T3-AC4" cell_refs="AT3-s-3" judgment="true"/> `T3-AC4` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether these two are the whole sibling set or whether a third consumer exists that neither round enumerated. **Record the readings and offer NO verdict.**

<expected_criteria>T3-AC1, T3-AC2, T3-AC3, T3-AC4</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T3-1.hop-test-the-two-sibling-consumers.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~12/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-3`.
<owned_cells>AT3-s-3</owned_cells>
Read-dependency, NOT claimed: `AT3-s-6` (the retag) waits on this cell being terminal.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied: the issuer inherits `TO-S7-1`'s hit counts (67 and 32) as ITS figures at ITS vintage and has
not re-derived them; AC1 re-takes both denominators independently.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~12/POSN_ASTTAX.TO-T3-1.hop-test-the-two-sibling-consumers.proof_of_spec.json
</proof_of_spec>
