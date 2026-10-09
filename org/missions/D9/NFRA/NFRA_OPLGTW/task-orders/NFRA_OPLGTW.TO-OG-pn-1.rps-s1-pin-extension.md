# NFRA_OPLGTW task order -- `OG-pn-1` -- extend the Schwab converter's RPS section-1 pin for the 28 columns 08403355 carries on six held dates

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pn-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pn-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~50</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the converter `opal-assets-silver-schwab` fires on bronze ObjectCreated for three masters and on the 12:15Z sweep; this cell builds and asks, it deploys nothing. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- code and tests only; the converter's role is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s AMENDMENT 1 on OG-bh-1 (msg 32826, half @f77e32d7c3) and the COO's (@eea4aebe10): "the pin-extension cell to AE~Z re-runs only the held dates, under its own pair", on row NFRA_OPLGTW-Z-W46-S3.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (reads of held bronze objects and converter logs).
</preflight>

## 1. THE CELL -- `OG-pn-1` (decomposition addendum R3-T.38)

The Schwab silver converter (source `data/assets/scripts/silver/`, packaged byte-equal into
`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`) refuses a partition that carries columns its pin does not
know, with `SchemaDriftError` and the message "vendor drift is a finding: measure, extend the pin, never silently absorb".
For six 08403355 dates (2025-12-12, 2025-12-15 .. 2025-12-19), the RPS section-1 zip carries 28 columns the pin does not
know (`account_title_line_1` .. `account_title_line_3`, `acct_regis`, `acct_type`, `net_credit_debit`, `margin_balance`,
... -- the full list is in the converter's CloudWatch error, row Z-W46-S3). Those dates have no `fact_rps`,
`fact_rps_s2`, `dim_position` or `dim_balance`, so their records read incomplete. The same dates convert for 08335338
and 08242234.

### PHASE A -- measure, build, ask; NO deploy, NO re-run

1. **Measure.** Read one held file's section-1 header (S3 read of
   `schwab/08403355/bronze/rps/20251212/08403355.CRS20251212.RPS.zip`, no write) and list the 28 columns exactly. Check
   whether the other five held files carry the same 28, and whether any 08335338/08242234 RPS file in the window
   carries any of them. Record `W/pn1_measure.json` (column list, per-file match, the 3-master comparison). If the six
   files do not carry ONE identical extra set, STOP and report.
2. **Build, in the source** (`data/assets/scripts/silver/`; the Lambda folder's copies must stay byte-equal to the
   source -- copy them, never hand-edit both). Extend the RPS section-1 pin EXPLICITLY with the 28 columns (names and
   types as the vendor file carries them), following how the pin declares columns today. Decide, from the existing
   projections, whether any of the 28 belongs in a served table; default: carried in the bronze-faithful fact layer only,
   and no served dimension changes. Say which, with the reason. Do not loosen the drift guard: an unknown column outside
   the extended pin must still raise.
3. **Tests**, `data/assets/scripts/silver/tests/test_ogpn1_rps_pin.py`, named exactly `test_ogpn1_ac01..03`, as
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/pn1.AC1.sh`'s header states (the held
   header committed as a small fixture, no account numbers -- mask the account fields). The four existing suites must
   pass whole.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-pn-1.md`, two halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`): the code change; the
   one Lambda it deploys to and its build/deploy path (Terraform, by `0.7.0_AE_CloudOps~Z`, never
   `update-function-code`); what moves for each of the THREE masters (both branches: a file with the 28 columns now
   converts; a file without them converts exactly as before); whether any served table's schema changes; the rollback
   (prior artifact version); then the re-run of ONLY the six held dates' RPS events (how: the sweep, or re-emitting the
   six bronze events), with what each writes and its rollback per key.
5. Run AC1, commit, REPORT, STOP. The issuer cuts the applier's order after the halves.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~50/`.

## 2. BOUNDS

- No deploy, plan, apply, upload, invoke or re-run. S3 READS only.
- The drift guard is not loosened; no column is absorbed without being named.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into your branch (row Z-W41-S5); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
data/assets/scripts/silver/
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~50/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W50-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pn-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/pn1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pin tests: pytest rc=0; named tests passed 3 of 3.*test_conversion_manifest\.py: pytest rc=0.*test_schwab_conversion\.py: pytest rc=0.*test_schwab_projections\.py: pytest rc=0.*test_schwab_schemas\.py: pytest rc=0.*regression suites run: 4.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the 28 columns are named in the pin, a held file converts, an unchanged file converts as before, and the
  guard still refuses an unknown column.

## 5. WHEN YOU ARE DONE

Phase A ends at the ask; the order stays `pending` until the applier's deploy and the held dates' re-run (a later
continuation). Report once: the measured column list, the served-table decision and reason, AC1's literal output, the
ask's path, commits, rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- From both halves' AMENDMENT 1 on OG-bh-1 (CTO @f77e32d7c3, COO @eea4aebe10); row Z-W46-S3.
- Pre-cut: pn1.AC1 base FAIL as expected (test file absent); the four regression suites at base pass 36 / 10 / 20 / 37.

- A1 (issuer, 2026-10-09 ~17:1xZ, on rows Z-W50-S1 and Z-W50-S2): (a) the premise is corrected -- the six held files carry
  ONLY a D2 balance table (no D1 positions section), graded against the section-1 pin by file position; extending the
  section-1 pin would have written balances into fact_rps/dim_position. The cell's change is the worker's: a scanned
  table is graded by its own D-tag (else file position), and the absent section lands its pinned 0-row partition as
  the existing shell branch does; pins, projections and the drift guard are unchanged. (b) AC1's <expect> listed the
  suites in a different order than `ls` prints them; the expect now matches the printed order (issuer's defect, the
  check unchanged). Graded by GATE (viii) on the modified order (<placeholders>NONE</placeholders>).

<status>pending</status>
<round>33</round>
<workstream>RPS-PIN</workstream>
<slot>~50</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
