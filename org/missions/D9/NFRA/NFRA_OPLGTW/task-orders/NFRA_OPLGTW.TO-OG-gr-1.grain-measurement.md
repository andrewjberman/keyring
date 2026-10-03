# NFRA_OPLGTW task order -- `OG-gr-1` -- the Schwab position/asset grain over every qualified snapshot: adopt the candidate or the C3 refusal stands

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~22</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads with existing access; nothing written to AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the adopt/refuse rule is the CTO's (analysis round 12 s.3a, row Z-W10-S1).
EGRESS CLASS, declared: NONE beyond Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `OG-gr-1` (decomposition addendum R3-T.7, item 7)

Row Z-W10-S1: `dim_position` and `dim_asset` COLLIDE under the declared grain on all 8 snapshots measured by OG-v-6
(`deliverables/0.9.0_WK_NFRA_OPLGTW~10/GRAIN_DECLARATION.json`; declared grain dim_position `[account_id, cusip, l_s]`,
dim_asset `[cusip]`, from `infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py:136-140`). A CANDIDATE superset
made each of those 8 unique (dim_position + `quantity_settled_unsettled` -- a QUANTITY, not an identifier, with 3 equal
alternatives at that size; dim_asset + `security_description_line_1`). Eight snapshots are a sample: 2,395 exist under
`s3://opal-data-assets/schwab/<master>/silver/<dataset>/date=YYYY-MM-DD/data.parquet` (masters `08242234`, `08335338`).

1. **Denominator.** The QUALIFIED dates: those with a closure marker `schwab/<master>/meta/complete/date=<d>.json`
   (OG-v-6's `latest_markers()` basis). Print the count per master and dataset, and say if you bound it further and why.
2. **Measure** each qualified `dim_position` and `dim_asset` snapshot with OG-v-6's instrument
   (`deliverables/0.9.0_WK_NFRA_OPLGTW~10/measure_grain.py` + `og_v6_common.py`; pinned VersionId reads): declared grain
   unique or not; candidate grain unique or not; how many rows have the candidate's ADDED column blank.
3. **Read why** the colliding keys carry a blank component (5 of 10 in OG-v-6): which column, which rows, a count.
4. **Verdict by the ruling:** ADOPT only if the candidate is unique on EVERY measured snapshot AND its added column is
   never blank; otherwise REFUSE (the C3 refusal stands and FWD-2's quantity-against-value question is answered as a
   refusal). Do not choose a different candidate to make ADOPT true; report any column that would, as a note.
5. Write `deliverables/0.9.0_WK_NFRA_OPLGTW~22/GRAIN_R13.json`: `{"denominator": {"qualified_snapshots": N, "basis",
   "per_master_dataset"}, "snapshots": [{"master", "dataset", "date", "declared_unique", "candidate_unique",
   "candidate_blank"}], "candidate": {...}, "blank_component_reason", "verdict": "ADOPT"|"REFUSE"}` -- counts and column
   names only, no row values, no account numbers.

## 2. BOUNDS

Read only. No contract or code change (an ADOPT goes to the CTO as an addendum, not edited here). Never push, merge,
rebase, stash, `checkout --` or `clean`; never override a gate.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W22-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/gr.AC1.sh; echo "exit=$?"</invocation><expect>(?s)verdict (ADOPT|REFUSE) \(rule says \1\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record covers its printed denominator (more than 8), one row per snapshot, and its verdict follows the rule.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/NFRA_OPLGTW.TO-OG-gr-1.grain-measurement.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if it PASSES, append a `complete` status tag after the
order's last status line in the same commit. Report once: denominator, collision counts, verdict, the blank reason.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 7). Pre-cut: `gr.AC1` FAIL (absent); a synthetic record PASSes it and a
  planted blank flips ADOPT to "rule says REFUSE" (FAIL).

<status>complete</status>
<round>14</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
