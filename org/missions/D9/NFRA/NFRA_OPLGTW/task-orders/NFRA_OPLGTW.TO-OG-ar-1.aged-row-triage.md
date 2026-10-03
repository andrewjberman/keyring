# NFRA_OPLGTW task order -- `OG-ar-1` -- triage every OPEN remediation row: owner and the condition that moves it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ar-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~27</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a record compilation; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- repo reads; live reads only to verify a remediation claim, read-only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-15 analysis s.4 item 5).
EGRESS CLASS, declared: NONE beyond read-only Opal AWS reads where a remediation must be measured.
</preflight>

## 1. THE CELL -- `OG-ar-1` (decomposition addendum R3-T.9, item 5)

The CVO's gate disclosed OPEN remediation rows that have not moved for two or more rounds. At the cut there were 41 rows
whose latest state is OPEN across `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/remediations/REMEDIATION_v1-v3.md`
(25 of them in v1). The check computes the live set. Many were already resolved by shipped work, for example:
- Z-S41 shipped in `4231bd2ddc`;
- Z-W15-S23 and Z-S34 in OG-rl-4 (`af2d762970`);
- W5-S6 pinned by OG-o-4;
- Z-W10-S1 adopted by R9.

For EVERY OPEN row, write one entry in `AGED_ROW_TRIAGE.json` with: `{id, round_graduated, owner, mechanism_one_line}`
plus EXACTLY ONE of:
- `remediated_by`: the commit or order whose MEASURED result remediates it, with the measurement. Re-measure where a
  cheap read exists; cite the proof instance where it does not.
- `moves_when`: the condition that moves it, and who acts. For example "G-E: Menachem's grant" or "the Research Meeting
  invitation (Z-S43)".
- `close_reason`: no condition moves it, with the reason.

Also write a short `AGED_ROW_TRIAGE.md`, grouped by the three kinds.

Then send nothing yourself. The issuer hands this file to `3.0.0_SA_CVO~O`, who owns advancing remediation rows. You edit
NO remediation row.

## 2. BOUNDS

- **Write:** your two deliverables only. Read-only everywhere else; no row is edited.
- **Never:** push, merge, rebase, stash, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~27/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W27-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ar-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/ar1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)missing 0; malformed 0;.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~27/NFRA_OPLGTW.TO-OG-ar-1.aged-row-triage.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If AC1 PASSes, edit this order's ONE `<status>` tag IN PLACE to `complete`. Never append a second tag.
4. Report once: the counts per kind, the literal AC output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 16 (addendum R3-T.9, item 5). Alone. Pre-cut 22:1xZ: `ar1.AC1` FAIL (remediation rows 66; OPEN 41; triage
  absent).

<status>pending</status>
<round>16</round>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
