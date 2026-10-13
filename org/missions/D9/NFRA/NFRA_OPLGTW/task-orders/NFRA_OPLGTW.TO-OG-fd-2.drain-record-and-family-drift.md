# NFRA_OPLGTW task order -- `OG-fd-2` -- persist the sweep's DLQ drain record, and census every remaining family's package drift for its release ask (E2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-fd-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-fd-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~61</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source, tests and a read of the repo's packaged copies; no deploy. The release is a later order per family.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change. sqs:ChangeMessageVisibility on the DLQ is already live for all 7 converter roles (OG-ap-12).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-35 analysis E2 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round35.md @682d1ced78), rows Z-S91 and Z-S100.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-fd-2` (decomposition addendum R3-T.48, E2)

The per-family DLQ drain (OG-fd-1) is in source for every family and LIVE on schwab only. Every other silver converter's
16:00Z sweep still drains the WHOLE shared queue `opal-assets-silver-dlq`: on 2026-10-13 the blackdiamond sweep deleted an
eclipse record at 12:45:52Z (row Z-S91). And a scheduled sweep's drain report is a return value that EventBridge discards,
so no drain can be read after the fact (row Z-S100).

1. **Drain record (Z-S100).** In `data/assets/scripts/silver/`, make `run_sweep` write its DLQ drain dict (`drained`,
   `family`, `other_family_returned`, `unattributed`, `truncated`, and the drained message ids or bodies, capped) into the
   backfill-status section it already writes. Do it for the mirror families' runtime and for `schwab_runtime.py`.
   - The section must stay readable by its existing readers, so add a key and change no existing one.
   - Tests: `test_fd2_ac01` in `tests/test_mirror_conversion.py` and `test_fd2_ac02` in `tests/test_schwab_runtime.py`.
     Each asserts that after a sweep with a planted own message and a planted foreign message, the written backfill-status
     carries the drain dict, with the own message drained and the foreign one returned.
2. **Drift census (Z-S91).** Read the families from `infra/aws/terraform/opal-assets/silver.tf` `local.silver_families`;
   that is the denominator. For EVERY family but schwab, compare the packaged copy
   (`infra/aws/lambda/opal-assets/opal-assets-silver-<family>/`) with the source files it vendors.
   - Count the differing lines (`drift_lines`, an int).
   - Name who owns the drift (`drift_owner`): the author of the newest commit that changed the packaged copy away from the
     source (`git log` on the package path), with that commit's hash.
   - Write `W/FD2_DRIFT.json` = `{"denominator_source": "silver.tf local.silver_families @<HEAD>", "families": [{"family",
     "package_dir", "drift_lines", "drift_owner", "drift_commit", "files_differing"}]}`.
3. **Ask.** Write `W/NEVER_WIDEN_ASK_OG-fd-2.md` for the per-family releases. Per family, it names:
   - the drift and its owner;
   - whether the rebuild would ship the drain change ALONE or also carry the drift;
   - the blast radius: that converter's code;
   - the rollback: its prior CodeSha256 and pin.

   The releases are later orders.

## 2. BOUNDS

- Source and tests under `data/assets/scripts/silver/`, plus reads of the packaged copies. No package rebuilt, no deploy,
  no live queue read.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
data/assets/scripts/silver/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~61/`. Rows: id `NFRA_OPLGTW-Z-W61-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-fd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/fd2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)mirror rc=0; schwab rc=0; named tests passed 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-fd-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r36/checks/fd2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)families required ([1-9]\d*) \(from silver.tf\); covered with drift_lines and drift_owner \1; missing \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a drain is readable after the fact. `AC2`: every remaining family's release can be signed against named drift.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-fd-2.drain-record-and-family-drift.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the
ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 36, E2. Pre-cut:
  - fd2.AC1 base FAIL as expected: named 0 of 2, both suites rc=0, so the harness runs.
  - fd2.AC2 base FAIL as expected: the files are absent.

<status>complete</status>
<round>36</round>
<slot>~61</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
