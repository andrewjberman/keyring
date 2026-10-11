# TO IRPT_DASHBD.TO-DB-b-155 -- the proposal's first axis renamed for what it measures -- the return closes when RESTATED under an admitted timing other than the served one -- with two tokens and their census, none containing RECONCILES

<to_id>IRPT_DASHBD.TO-DB-b-155</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~121</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>80</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5886 (2026-10-11 ~21:40Z) | **Rows:** IRPT_DASHBD-D2-W121-S2 | **Decomp cell:** `DB-b-155` (decomposition section 82) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-148 (drained @fd9ebd2f35).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-121` (branch `wk-irpt-dashbd-80-121`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**The ruling this answers (CTO msg 5886), verbatim in part.** "END is the SERVED convention, and END closes in 0 of 51. So no segment's
served return closes against the custodian's; what closes is a RESTATEMENT under START or MID. 'RECONCILES_YES' would be read as 'our
number matches'. It does not. [...] Ruled: The two axes and the TIMING tokens stand: 3 START, 1 MID, 47 not determined, claim inferred.
The first axis is renamed for what it measures: the return closes when RESTATED under an admitted timing other than the served one. Two
tokens come back with their census; none containing RECONCILES. Nothing served is relabelled."

**The cell (`DB-b-155`).** You are the serial that owns the record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/TIMING_CLASSES_PROPOSAL.json`;
you amend it. You recompute no segment: the counts stand.
1. Rename the first axis and its two values. The name and both tokens say what is measured: the return closes when RESTATED under an
   admitted timing other than the served one (END), with the dollars and flow days tying. A reader who meets the token alone must not
   read it as "the served number matches". UPPER_SNAKE, as the record's `spelling_style`. Neither token, nor the axis name, contains
   `RECONCILES`. State the axis's `question`, its declared `domain` (unchanged unless the rename changes it: say which) and each
   value's meaning and claim.
2. Census each of the two new tokens by word boundary, case-insensitive, over the worktree, with the denominator printed (the count of
   files scanned and how it was taken), exactly as the record's existing `token_census` entries are shaped. Use the native Grep tool or
   `comp-find -i`; say which. Replace the two RECONCILES entries of `token_census` and of `new_tokens` with the two new ones; the four
   TIMING entries stand as they are.
3. Update `placement.cells` (the member that names the first-axis value in each cell), the `axes` entry, and every place in
   `postulates`, `the_three` and `does_not_decide` that states a RECONCILES token, so the record reads in the new tokens throughout.
   In the intent-coherence postulate say plainly what the ruling found: END is the served convention and closes in 0 of 51, so the
   axis measures a restatement closing, not the served number matching.
4. Add a top-level member `superseded_tokens`: {tokens: ["RECONCILES_YES", "RECONCILES_NO"], retired_by ("1.0.0_SA_CTO~DELL2 msg
   5886"), why (in the ruling's words)}. This member, the record's `answers` and free-text history may name the old tokens; the axes,
   `new_tokens`, `token_census` and the placement cells may not.
5. Update your script `y1_place.py` only if it prints the old tokens as labels, and say so. Round 78's criterion
   (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r78/p78_round78.py` DB78-1-AC1) must still end in PASS after your edit: run it before and
   after. Keep the file's indentation, key order and line endings.

<criterion id="DB80-2-AC1" cell_refs="DB-b-155"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r80/p80_round80.py" . DB80-2-AC1</invocation><expect>DB80-2-AC1 PASS</expect></criterion>
`DB80-2-AC1` -- the first axis is renamed with two censused tokens that do not contain RECONCILES, the two retired tokens are listed with the ruling that retired them, and the 51 are still placed 51 of 51. Base: FAIL.

<expected_criteria>DB80-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all.
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
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-155.first-axis-renamed-restated-close.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 82 (round 80), cell `DB-b-155`.
<owned_cells>DB-b-155</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB80-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~121/IRPT_DASHBD.TO-DB-b-155.first-axis-renamed-restated-close.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB80-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the axis's new name, its declared domain and its two tokens with what each means in one line; the census of each new token (pattern, files scanned, hits, what any hit is); the placement table; what in the four-postulate record changed and what did not; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a proposal record's own text; no class is applied anywhere, nothing served is relabelled.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
