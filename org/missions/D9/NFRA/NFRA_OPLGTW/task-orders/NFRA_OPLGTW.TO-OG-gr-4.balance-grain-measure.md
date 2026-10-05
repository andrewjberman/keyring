# NFRA_OPLGTW task order -- `OG-gr-4` -- measure dim_balance's grain (account,) on every served snapshot; serve one page

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gr-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~26</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot read-only measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- reads through the gateway's own installed catalog and data roles; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-16 analysis s.4 item 3).
EGRESS CLASS, declared: NONE beyond read-only Opal AWS (SSM to the gateway host, S3 reads by its roles).
</preflight>

## 1. THE CELL -- `OG-gr-4` (decomposition addendum R3-T.10, item 3)

FWD-2 (accurate answers) is NOT_REALIZED because balance answers are unproven. `dim_balance` pages on the grain
`(account,)` (`infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py:160`), and that grain has never been measured
for uniqueness on a served snapshot. Served `4b6b823fae` makes 14 qualified days per master servable for every contract
dataset (r16 Phase B, `deliverables/0.9.0_WK_NFRA_OPLGTW~15/RL5_PAGING.json`, `census_after_other`).

READ-ONLY. On the opal-gateway host, through the installed engine and its venv, reuse the r16 helpers in
`deliverables/0.9.0_WK_NFRA_OPLGTW~15/`: `rl5_ssm.py`, plus `rl5_host_prelude.py.txt` and the census program pattern
`rl5_census_release_host.py.txt`.
1. **Census.** List every served `dim_balance` snapshot (both masters; print the denominator, expected 28 at the cut).
2. **Uniqueness.** For each, read its parquet and count rows and DUPLICATE `(account,)` keys, i.e. keys appearing more
   than once. When `account` is a column under another name, use the grain field the engine uses and say which.
3. **One page.** With a SYNTHETIC principal and an in-memory grant naming `dim_balance` (never a real identity, never a
   state-store write), request one `dim_balance` rows page (page size 5) on the newest qualified snapshot. Record `OK`
   with the row count, or `REFUSED <code>`.
4. Write `GR4_BALANCE_GRAIN.json`:
   - `served_snapshot_census`;
   - `snapshots: [{master, date, rows, duplicate_keys, grain_field}]`;
   - `page`;
   - `synthetic_principal: true`, `grants_written: 0`, `state_store_written: false`;
   - `row_id` when the grain is not unique.
5. **If ANY snapshot has duplicate keys:** paging refuses as designed. File a BLOCKING row (`spec_asserts` = the
   `(account,)` grain; `world_is` = which snapshots and how many duplicates, with two example duplicate keys REDACTED to
   their last 4 characters) and name it in `row_id`. The CTO rules a grain, as R9 did. Do NOT change the grain.

Remove every host scratch copy.

## 2. BOUNDS

- Read-only on the host and S3. No code, contract or grain change. No grant, no state-store write.
- Never print an account number, a CUSIP list, or any row value beyond counts and the redacted example keys.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor; source `.env`.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W26-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gr-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/gr4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)served census \d+; measured \d+;.*branch: (UNIQUE\+SERVED|NOT-UNIQUE\+REFUSED\+ROW).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/NFRA_OPLGTW.TO-OG-gr-4.balance-grain-measure.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once: denominator, duplicates per snapshot (counts), the page outcome, rows, commits.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 3). Alone; runs beside `OG-q-7`.
- AC1 passes on EITHER branch: the cell measures and does not decide. A not-unique result sends a grain ruling to the
  CTO.
- Pre-cut: `gr4.AC1` FAIL (the record is absent).

<status>pending</status>
<round>17</round>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
