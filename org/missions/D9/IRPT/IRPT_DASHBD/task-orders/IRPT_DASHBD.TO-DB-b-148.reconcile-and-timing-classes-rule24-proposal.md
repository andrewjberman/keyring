# TO IRPT_DASHBD.TO-DB-b-148 -- the tie-out's class set as two questions -- does the segment reconcile, and which timing did the other system use -- returned as a Rule 24 proposal: four postulates, a word-boundary census of each new token, the 51 placed by subtraction

<to_id>IRPT_DASHBD.TO-DB-b-148</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~121</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5835 (2026-10-11 ~20:55Z) | **Rows:** IRPT_DASHBD-D2-W108-S2 | **Decomp cell:** `DB-b-148` (decomposition section 80) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-147 (drained @bbe07f54e7).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-121` (branch `wk-irpt-dashbd-78-121`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**The ruling this answers (CTO msg 5835), verbatim in part.** "The 51 are called contested for two different things, and only one is a
disagreement. Ruled: 1. Does the segment reconcile? Yes when its return closes within tolerance under at least one admitted timing,
with the dollars and flow days tying. Measured, not contested. 2. Which timing did the other system use? Classed only where EXACTLY ONE
timing closes: the 4, as START or MID, claim inferred, since a fit is evidence and not the custodian's statement. Where more than one
closes (32, 11, the fee-row day), the data cannot say, and that is the final answer: timing not determined. Not contested, not classed.
3. The 3 within 0.35 points: say first whether any closes. If none, they alone stay contested. That changes the class set, so it
returns as a proposal under Rule 24: four postulates and a word-boundary census of each new token. I rule on that record."

**The cell (`DB-b-148`).** You PROPOSE; you apply nothing, move no segment in any record, and edit no other worker's file. Read first:
`CLAUDE.md` rule 24 (TAXONOMY LAW) and `docs/doctrine/CLAUDE_ANNEX.md` on it; `rcg/rulings/RULINGS.jsonl` R-0006 and R-0009 (what a
value-enum proposal must carry); `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~120/CONTESTED_51_MEANING.json` and its tracked script
`x1_crosstab.py`; and how the tie-out's classes are spelled today in the records (`~104/UNEXPLAINED_244.json`,
`~108/UNCLASSED_90.json`, `~111/CONTESTED_51.json`) and in any code or contract that names them.
1. **Two axes, not one.** `axes`: (a) RECONCILES, over the declared domain "tie-out segments whose dollars and flow days were read on
   both sides", with its values; (b) TIMING, over the declared domain "segments that reconcile", with its values (a timing classed with
   its claim `inferred`, and the value for "more than one timing closes, the data cannot say"). Name each value in the project's
   existing spelling style. State the claim each carries (`measured`, `inferred`, ...) in a field a consumer can reject on.
2. **The four postulates**, each {finding, evidence}: MECE over the declared domain (hunt the uncovered member BY SUBTRACTION from the
   printed 51, and from the 244, not by a forward list; say where the 185 classed and the 8 unclassed sit on each axis, or that the
   axis does not apply to them and why); SAME GRAIN (every value is a property of one segment); INTENT COHERENCE (one axis, one
   intent: a value never answers the other axis's question); STATE COHERENCE (name which values one remedy does NOT move: for example,
   a custodian statement of its convention moves the "cannot say" value and not a reconciliation).
3. **A word-boundary census of each NEW token** (`new_tokens`, `token_census`: [{token, pattern (the word-boundary regex), files_scanned,
   hits, what_the_hits_are}]): one unscoped read per token over the corpus with its denominator (`comp-find -i` with word boundaries,
   or the native Grep tool over the tracked tree; never a census cut by `head`). A token already used with another meaning is a
   collision: say so and propose another.
4. **Place all 51** (`placement` {total: 51, cells: [{reconciles, timing, segments}], uncovered: 0}) from DB-b-147's cross-tabulation,
   re-derived with its script from the private tables (read in place under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~120/`).
5. **The three within 0.35 points** (`the_three` {segments: 3, any_timing_closes, per_segment: [{start_closes, mid_closes, end_closes}],
   stay_contested}): the CTO asked this FIRST. Read it from the per-segment table: for each, does START, MID or END close the return
   within the tolerance? If none closes for a segment, it stays contested; if one or more closes, place it by the rule.
6. `is_a_proposal: true`. State what the proposal does NOT decide (the 185, the 8, any served label). Counts and class names only:
   no account id, no client name, no amount. Record `TIMING_CLASSES_PROPOSAL.json`.

<criterion id="DB78-1-AC1" cell_refs="DB-b-148"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r78/p78_round78.py" . DB78-1-AC1</invocation><expect>DB78-1-AC1 PASS</expect></criterion>
`DB78-1-AC1` -- the class set is proposed over two axes with its four-postulate record, each new token is censused by word boundary with its denominator, all 51 are placed, and for the 3 it is said whether any timing closes. Base: FAIL.

<expected_criteria>DB78-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all. Everything is taken from DB-b-147's record and the private per-segment tables behind it.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~121/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W121-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-148.reconcile-and-timing-classes-rule24-proposal.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 80 (round 78), cell `DB-b-148`.
<owned_cells>DB-b-148</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB78-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/IRPT_DASHBD.TO-DB-b-148.reconcile-and-timing-classes-rule24-proposal.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB78-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the two axes, their declared domains and values; each postulate's finding in a line; the token census (token, pattern, files scanned, hits, and what each hit is); the placement table summing to 51; the three: whether any timing closes for each and whether they stay contested; what the proposal does NOT decide; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a proposal record; no class is applied anywhere until the CTO rules on it.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
