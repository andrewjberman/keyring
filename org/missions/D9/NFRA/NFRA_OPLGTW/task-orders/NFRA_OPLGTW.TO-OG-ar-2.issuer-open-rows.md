# NFRA_OPLGTW task order -- `OG-ar-2` -- the issuer's seven OPEN remediation rows: who moves each, or why it closes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ar-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~21</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a record compilation; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- repo reads; live reads only to measure a remediation claim, read-only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-16 analysis s.4 item 6).
EGRESS CLASS, declared: NONE beyond read-only Opal AWS reads where a remediation must be measured.
</preflight>

## 1. THE CELL -- `OG-ar-2` (decomposition addendum R3-T.10, item 6)

Seven remediation rows owned by `2.0.0_SA_COO~O` are OPEN in
`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/remediations/REMEDIATION_v1-v3.md`:
- W6-S2: no carrier declares the three datasets' unique grain.
- W1-S9: the naming limb refuses the PRD-fixed role names.
- W2-S6: 8 synthetic probe items in the production access-state table.
- Z-W13-S5: the DATA_CATALOG.yaml line-ending renormalization never landed.
- Z-W12-S7: the operator's upload client has no live refresh family.
- S63: phase 1's committed seal lost its salt.
- Z-W15-S31: `tr.AC1.sh` arm 4 expects 48 `.env` keys while the host holds 50.

`deliverables/0.9.0_WK_NFRA_OPLGTW~27/AGED_ROW_TRIAGE.json` (OG-ar-1) triaged them at its pin. Start there and
RE-MEASURE: R9 (round 16) declared grains, so W6-S2 may now be remediated, or narrowed to `dim_balance`, which OG-gr-4
measures.

For EACH of the seven, write one entry in `ISSUER_ROWS_R17.json` (`{"rows": [...]}`): `{id, owner, mechanism_one_line}`
plus EXACTLY ONE of:
- `remediated_by: {pointer, measurement}`: the commit or order whose MEASURED result remediates it, and the measurement
  you took now.
- `moves_when: {condition, actor}`: the condition that moves it and who acts. **Z-W12-S7 is a dated act:** the operator
  re-authorizes the upload client before ~2026-10-18; say that date.
- `closure: {reason, pointer}`, where `reason` is one of `NOT_A_DEFECT`, `CARRIED_BY`, `IRREMEDIABLE`,
  `ACCEPTED_BY_RULING` (`docs/doctrine/THE_SURPRISE_CHANNEL.md`, "How a remediation row ENDS").

A row whose move needs the CTO's L4 (a PRD or ruling) says so in `moves_when` with the actor `1.0.0_SA_CTO~O`. Also write
a short `ISSUER_ROWS_R17.md`, grouped by kind.

You edit NO remediation row. The issuer decides from your file and `3.0.0_SA_CVO~O` writes the clocks (ruling
@cc05804f8f).

## 2. BOUNDS

- **Write:** your two deliverables (and rows) only. Read-only everywhere else.
- **Never:** push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor; delete the W2-S6 probe
  items (that is an act for its owner, not this record).

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W21-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ar-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/ar2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)rows 7; covered 7; missing 0 \[\]; malformed 0 \[\]; Z-W12-S7 dated True;.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-ar-2.issuer-open-rows.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once: per row the kind and its one-line basis.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 6). Alone.
- Pre-cut: `ar2.AC1` FAIL (the record is absent).

<status>pending</status>
<round>17</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
