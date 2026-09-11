# TO POSN_ASTTAX.TO-T5-1 -- MEASURE step (2)'s BAR against the SERVED artifact. It is a CONDITION, not a task: your verdict is what the world says, not that the harness ran (AT3-s-5, FWD-1/FWD-2). GATES THE RETAG

<to_id>POSN_ASTTAX.TO-T5-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~14</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-11</issued_date>
<status>staged</status>

**Directive:** D4 · **Macro:** POSN · **Fabric:** site-z · **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d` · **Decomp cell:** `AT3-s-5` · **Issuance:** round 3.
**DEPENDS ON `AT3-s-1`. GATES `AT3-s-6` (the retag).**

---

## THE CELL

PRD s.4 `C-RETAG-SAFETY`, step (2), **verbatim -- this is your bar and the whole of it**:

> for EVERY ticker in the retag set, the SERVED `asset_class` value equals its ratified five-class
> label AND its allocation weight is NON-ZERO and equal to its pre-retag weight, read from the served
> artifact.

⛔ **STEP (2) IS CURRENTLY *NOT MET*.** `TO-S7-1` measured it in round 2 and returned NO-GO. `AT3-s-1`
was cut to make it meetable. **You measure whether it now IS met.**

⭐ **THE PRD RE-WROTE THIS STEP FROM AN ACT INTO A CONDITION FOR A REASON, AND THAT REASON IS YOU.**
It used to read "verify the chain", and a reader -- `1.0.0_SA_CTO~Z`, who then withdrew it -- treated a
COMPLETED verification cell as a PASSED one. In the PRD's own words: *"A step that names a TASK is
satisfied by doing the task; a step that names a CONDITION is satisfied only by the world."*
⛔ **SO: RUNNING YOUR HARNESS IS NOT A RESULT. THE BAR HOLDING IS THE RESULT.** If it does not hold,
NO-GO is the correct, valuable output of this cell -- exactly as `TO-S7-1`'s NO-GO was round 2's most
valuable product.

## THE ACT

1. **Name the retag set by MEMBER** (`T5-AC1`), not by description, with its ratified target label per
   ticker. The set is the six Commodities moves plus VXX (Structured) -- **re-derive it, do not inherit
   it**, and say if your read differs.
2. **Read the SERVED artifact** (`T5-AC2`) -- `positioning_data.json`, not the generator's internals.
   The bar says "read from the served artifact" and that is the grain that binds.
3. **For every member, assert BOTH halves** (`T5-AC3`): served label == ratified label, AND weight
   non-zero AND equal to pre-retag weight. ⛔ **BOTH. The weight is the half that hides** -- a correct
   label on a zeroed weight is the exact failure the re-founding describes.
4. **State GO or NO-GO** (`T5-AC4`), naming every member that fails and on which half.
5. Instance, checker, `complete`, one commit, one report.

## BOUNDS

- ⛔ **READ-ONLY. CHANGE NOTHING.** No registry write, no code edit, no deploy, no retag. A cell that
  fixes what it is measuring cannot report on it cleanly -- and this is the gate cell for an
  irreversible act.
- ⛔ **DO NOT RETAG TO TEST.** The bar is measured on the CURRENT world. If the retag has not happened,
  measure what a five-class value does through the served path by the means `AT3-s-1` left available --
  do not move a live row to create your own test case.
- ⛔ **GO REQUIRES EVERY MEMBER TO PASS BOTH HALVES.** Not most. Not the held one. Every member.
- ⛔ **DO NOT CONCLUDE FROM A PAGE.**
- A divergence is a ROW at `../surprise-channel/investigations/INVESTIGATION_v1.md`, ids
  `POSN_ASTTAX-Z-W14-S<n>`, ONE new fenced ```json block appended at the END; then keep working.
- Commit under your own serial via `safe-commit.sh`, msgfile by the Write tool, PURE ASCII, never `-m`.
- Run `.tools/proof-of-spec-check.py` FROM INSIDE YOUR WORKTREE before flipping `complete`.

## ACCEPTANCE CRITERIA

<criterion id="T5-AC1" cell_refs="AT3-s-5"><invocation>timeout 180 .tools/aws dynamodb batch-get-item --request-items '{"etf-classifications":{"Keys":[{"ticker":{"S":"DBC"}},{"ticker":{"S":"GLD"}},{"ticker":{"S":"GSG"}},{"ticker":{"S":"IAU"}},{"ticker":{"S":"SLV"}},{"ticker":{"S":"USO"}},{"ticker":{"S":"VXX"}},{"ticker":{"S":"VIXY"}}]}}' --query 'Responses."etf-classifications"[].{t:ticker.S,a:asset_class.S,s:sub_asset_class.S,m:management_style.S}' --output json</invocation><expect>every key resolved and pasted verbatim, UnprocessedKeys named; then the RETAG SET stated BY MEMBER with each member's ratified five-class target label, and a one-line reason per member. If your derived set differs from the issuer's seven, say so and state yours.</expect></criterion> `T5-AC1` -- THE SET, BY MEMBER, RE-DERIVED.

<criterion id="T5-AC2" cell_refs="AT3-s-5"><invocation>timeout 180 python &lt;your served-artifact read&gt;</invocation><expect>the SERVED positioning_data.json located and read, with its S3 URI (or path), LastModified and byte size pasted verbatim as the vintage. Every retag-set member's served asset_class/assetClass value and its allocation weight, quoted from that artifact. The artifact NAMED -- not the generator's in-memory state.</expect></criterion> `T5-AC2` -- THE SERVED ARTIFACT, WITH ITS VINTAGE.

<criterion id="T5-AC3" cell_refs="AT3-s-5"><invocation>timeout 180 python &lt;your two-half bar harness&gt;</invocation><expect>one row per member with BOTH halves asserted separately: (a) served label == ratified label PASS/FAIL, (b) weight NON-ZERO and equal to pre-retag weight PASS/FAIL, with both numbers shown. A member passing (a) and failing (b) must read FAIL. Members tested == members enumerated in AC1, stated as a count.</expect></criterion> `T5-AC3` -- ⭐ **BOTH HALVES, SEPARATELY. THE WEIGHT IS THE HALF THAT HIDES.**

<criterion id="T5-AC4" cell_refs="AT3-s-5"><invocation>timeout 120 python -c "print('BAR VERDICT RECORDED IN THE INSTANCE')"</invocation><expect>GO or NO-GO for AT3-s-6, stated as the CONDITION's truth value and not as "the harness ran". GO requires every member to pass BOTH halves. If NO-GO, every failing member and the failing half named.</expect></criterion> `T5-AC4` -- THE GATE ON THE RETAG. A completed cell is not a passed one.

<criterion id="T5-AC5" cell_refs="AT3-s-5" judgment="true"/> `T5-AC5` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.** Whether the bar as measured here is the bar the PRD states, or a proxy that happens to be easier to read. **Record the readings and offer NO verdict.**

<expected_criteria>T5-AC1, T5-AC2, T5-AC3, T5-AC4, T5-AC5</expected_criteria>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~14/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round3.md</decomp_doc> round 3, cell `AT3-s-5`.
<owned_cells>AT3-s-5</owned_cells>
Read-dependencies, NOT claimed: `AT3-s-1` must be terminal first (it makes the bar meetable); `AT3-s-6` is gated on YOUR verdict and is NOT yours.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only; no job, monitor or alerting built or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; DynamoDB and S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- not run as a tool. NOT covered and stated rather than
implied: the issuer has NOT measured the bar at this vintage and is not predicting its answer. Round
2's 17/3/14 ratio is historical (`AT2-s-1` repaired a benchmark hop) and must not be treated as this
cell's starting point.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~14/POSN_ASTTAX.TO-T5-1.the-bar-step-2-measured-against-the-served-artifact.proof_of_spec.json
</proof_of_spec>
