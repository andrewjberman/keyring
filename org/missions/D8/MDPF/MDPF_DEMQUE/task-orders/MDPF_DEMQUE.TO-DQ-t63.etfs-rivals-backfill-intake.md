# TO MDPF_DEMQUE.TO-DQ-t63 -- round 9 DQ-t-63: the ETFS_RIVALS backfill gaps become seven priced Bloomberg demand requests (total return on held days and the close on dialog-curve days, in three newest-first stages, plus the dividend history for the securities with no corporate-actions row)
<to_id>MDPF_DEMQUE.TO-DQ-t63</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~55</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>ETFSINTAKE</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-63` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 26) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-NEED-CLASS, FWD-3, FWD-5 | **depends_on:** DQ-t-50, DQ-t-43, DQ-t-44 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-14 ~18:5xZ, relayed by the CTO (msg 5713): "ETFS_RIVALS is done now, all it needs is its backfill sorted out in DEMQUE." The ETFS_RIVALS issuer cited three measured gaps in
[BACKFILL_GAPS_FOR_DEMQUE.md](file:///C:/dev/ajb_workspace/org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/BACKFILL_GAPS_FOR_DEMQUE.md)
(repo-relative `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30/BACKFILL_GAPS_FOR_DEMQUE.md`). Read it first. This cell builds the requests; **it makes no vendor call, draws nothing and files nothing.**

**Build ONE new module `data/mdpf/scripts/demque/etfs_rivals_intake.py`** (read `bbg_quote.py` in full: `_validate`, `_entry_dates`, `_check_window`, `quote`; read `demand_queue.py` `validate`; read the filed precedent requests
`org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json` and `AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.json` for the request shape; import, do not copy). The derivation of the owed sets already exists as
read-only code in `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~V1/round30_prep/owed_size.py` (the method: `history_owed.owed`, the G1 held days, the dialog keys of the published page) and in
`data/etfs/scripts/rivalfunds/` (`history_owed.py`, `gold_holding_contribution.py`, `homes.py`, `sinks.py`). Reuse those functions by import; do not edit them.

CLI: `python etfs_rivals_intake.py --build --day YYYY-MM-DD --out-dir DIR` (both flags REQUIRED; no default day; a `--build` into a directory under `org/missions/` refuses and exits 2).
It writes exactly seven request files into DIR, prints ONE JSON line, and exits 0.

**The seven requests** (all `need_class` `non_client`, `need_date` = the day, `window_start` `2025-10-13`, `standing` false, `tier` 3, `vendor` `bloomberg`, `page` `rival funds (ETFS_RIVALS)`, `filed_by` `2.0.0_SA_COO~Q1`,
`filed_for` `ETFS_RIVALS`, a `reason` and an `authority` citing the two records above):
1. `ETFS_RIVALS-C1-TR-HELD-D30`, `-D90`, `-D365`: channel `history`, fields `["DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]`. Units = (security, trading day) pairs that the Rival Funds page's rankings read AND that have no stored close: the day after each report on which any of the
   13 funds holds the security (V1's set H; ACWI and IWM holdings are excluded, Andrew Z4). The as-of day is the previous trading day of `--day` (`lib/trading_calendar.py`). Stage windows by calendar days before the as-of day: D30 = the as-of day minus 30 days
   through the as-of day; D90 = the as-of day minus 90 days up to but NOT including minus 30; D365 = `2025-10-13` up to but NOT including minus 90. The stages are DISJOINT per (security, date) and together are the whole 365-day set (newest first: the queue draws D30 before D90 before D365).
2. `ETFS_RIVALS-C1-CLOSE-CURVES-D30`, `-D90`, `-D365`: channel `history`, fields `["PX_LAST"]`. Units = the owed (security, day) pairs of every security that gets a security dialog on the published page for `--day` (V1's set C: the `data-sec-dialog` keys of the
   page's `index.html`, matched to security ids; unmatched keys are counted in the build line and not requested), same three disjoint stage windows.
3. `ETFS_RIVALS-C1-DIVIDENDS`: channel `reference`, fields `["DVD_HIST_ALL"]`, no dates. Securities = the 70 names in
   [ETFS_RIVALS_DVD70_NAMES.json](file:///C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ETFS_RIVALS_DVD70_NAMES.json) (repo-relative `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ETFS_RIVALS_DVD70_NAMES.json`), each as `"<bloomberg>"` exactly as the file holds it.
   The source note's 71st key `nan` is a null security key, NOT a security; it is excluded and the build line says so. By `bbg_quote`'s reference rule this is 70 cells; DVD_HIST_ALL returns several rows per security, so that count is an UNDERCOUNT: put a `cells_claim_note` key in the request saying so
   (the live store holds 9,354 dividend event rows for 724 securities, about 13 each), and file one OBSERVATION surprise row naming the gap between the reference rule and a bulk field.

**Entry shape for requests 1 and 2:** one entry per security, `{"bloomberg": "<ticker> Equity" (as the owed set and the page's raw identifier carry it), "dates": [ISO trading days, strictly ascending]}`, exactly the per-entry dates shape `bbg_quote` documents (DQ-t-50). Every date is a trading day on or after `2025-10-13`.
If the owed set gives no Bloomberg ticker for a security, count it in the build line as `no_ticker` and leave it out; if MORE than 2 percent of the units have no ticker, STOP and file a BLOCKING surprise row naming it instead of building.

**The build line** (one JSON object): `day`, `asof`, `requests` (a list of `{request_id, cells, units, securities}`, in the order above, where `cells` is `bbg_quote.quote`'s own count for that request), `tr_union_units`, `close_union_units`, `dialog_keys`, `dialog_unmatched`, `no_ticker`, `dividend_securities` (70), `excluded_keys` (`["nan"]`).
Deterministic: two builds write byte-identical files. No key in any request names an account; the build reads fund holdings and writes tickers and dates only.

**Tests** in a NEW `test_demque_etfs_rivals_intake.py` (pytest; stub frames, no network, no S3), with exactly these names:
`test_the_three_stages_are_disjoint_and_newest_first_and_their_union_is_the_365_day_set`,
`test_a_unit_is_one_security_on_one_trading_day_and_dates_entries_validate_under_bbg_quote`,
`test_the_dividend_request_is_one_reference_cell_per_security_and_excludes_a_null_key`.

**Report, do not file.** Run the real build once into `.scratch/` and report its line; the issuer files and quotes the requests on the merged bytes.

### ACCEPTANCE

<criterion id="DQ9-t63-AC1" cell_refs="DQ-t-63"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t63_tests.py</invocation><expect>INTAKE-OK</expect></criterion>
<criterion id="DQ9-t63-AC2" cell_refs="DQ-t-63"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t63_real.py</invocation><expect>INTAKE-REAL-OK</expect></criterion>
`DQ9-t63-AC1` -- the three named tests. `DQ9-t63-AC2` -- on the REAL stores (S3 read only, page day 2026-10-13): seven files, every request valid under `bbg_quote._validate`, non-client tier 3, stage windows and trading days right, stages disjoint, the TR 365-day union within 1 percent of the measured 123,933 units and the close union within 1 percent of the measured 89,216, the dividend request exactly the 70 names as reference cells, the build line's cells equal `bbg_quote`'s own, byte-identical twice, no account key and zero account-id oracle hits.
The check runs two builds (each reads S3 and the published page; expect 1 to 3 minutes each): invoke it under `timeout 560`, and say so in your report. Report the whole folder `pytest data/mdpf/scripts/demque` once and the build line verbatim.

<expected_criteria>DQ9-t63-AC1,DQ9-t63-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `INTAKE-BAD no file ...test_demque_etfs_rivals_intake.py`; `INTAKE-REAL-BAD build rc=2 ... etfs_rivals_intake.py: No such file`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue or any pacer state; do NOT write a request into `org/missions/.../requests/`**; no AWS write; no deploy; no timer. S3 reads use the box's `cloudops-dell1-agent-user` profile as `owed_size.py` does. Never print an account number. Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W55-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/etfs_rivals_intake.py
data/mdpf/scripts/demque/test_demque_etfs_rivals_intake.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-63`.
<owned_cells>DQ-t-63</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t63-AC1, DQ9-t63-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~55/MDPF_DEMQUE.TO-DQ-t63.etfs-rivals-backfill-intake.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t63-AC1,DQ9-t63-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the build line verbatim, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a request builder over S3 reads; no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a builder; nothing is drawn or served.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct ~18:5xZ 2026-10-14 via CTO msg 5713 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_185xZ_ETFS_RIVALS_DONE_BACKFILL_TO_DEMQUE.md`, CLOUD @a9a7ed555a); `2.0.0_SA_COO~V1` msg 5716 and `BACKFILL_GAPS_FOR_DEMQUE.md` @c9e98081a6; staged order 30, 90, 365 on Andrew's "C1 yes, approved in that order" (`DEMQUE_QUEUE_FORM_ANDREW_20261013.md`); decomposition round 9.
Issuer finding: the source note's Row 3 list holds 71 keys and the last is `nan`, a null security key; the pinned names file holds 70.
