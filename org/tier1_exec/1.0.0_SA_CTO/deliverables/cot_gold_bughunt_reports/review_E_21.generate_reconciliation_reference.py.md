# REVIEW -- E_21.generate_reconciliation_reference.py

- script: `data/cot/scripts/gold/E_21.generate_reconciliation_reference.py`
- verdict: **issues-found**
- runs_in_incremental: False
- findings: 6

## Finding 1 -- [high/other/full]
- **Location:** `E_21.generate_reconciliation_reference.py:113-117 (nna_day selection) -> :137-140 (firm NNA) + :168-174 (advisor NNA)`
- **Mechanism:** nna_day is set to _latest_partition(CANONICAL_NNA_PREFIX) (the lexicographically-last gold/canonical/nna/{date}.parquet) with NO filter tying it to target_date. The comment 'latest partition IS one date' only holds when the operator did NOT pass --date and the nightly is coherent. C_01 confirms canonical/nna is per-date-partitioned with nna_txn/daily_inflow/daily_outflow, so the branch executes. Every firm.*_canonical and per-advisor NNA field is stamped as target_date but is actually sourced from whatever the newest nna partition is.
- **Failure scenario:** Run the documented historical form `python3 E_21... --date 2026-04-01 --upload` while the latest gold/canonical/nna partition is 2026-04-07. reference.target_date is written as 2026-04-01, but firm.nna_txn_canonical / daily_inflow_canonical / daily_outflow_canonical (and each top-advisor's nna_txn/daily_inflow/daily_outflow) report 2026-04-07's flows. DE/RD comparing the portal's 2026-04-01 NNA against this 'authoritative' reconciliation_reference.json see a false discrepancy, or a genuine portal error on 04-01 is masked by the coincidentally-close 04-07 number. Same corruption occurs any night NNA (C_01) lagged while client_performance (C_02) advanced, since target_date follows client_performance's max date.
- **Proposed fix:** Read the exact-date partition: nna_key = canonical_nna_key(str(target_date.date())) (import it from lib.s3_layout). If that key does not exist, set nna_day=None and leave the *_canonical fields absent (or None) with a logged WARN, rather than silently substituting _latest_partition's date.

## Finding 2 -- [medium/empty-null-handling/full]
- **Location:** `E_21.generate_reconciliation_reference.py:148-179 (advisor block; anchor :150)`
- **Mechanism:** For COT, account_team's architect column exists (C_07 writes it) but every value is Unassigned/Unresolved because cot silver produces no role columns. The left-merge + fillna('Unassigned') collapses every account into a single architect group, so groupby('architect') yields one bucket carrying the entire firm AUA. team.empty is False (C_07 still produces rows), so the block runs and emits a single meaningless 'top advisor'.
- **Failure scenario:** A normal COT run produces top_advisors = [{'advisor':'Unassigned','aua':<entire firm AUA>,'account_count':<all accounts>,'client_count':<all clients>}]. The reconciliation reference then asserts one 'advisor' named Unassigned holds 100% of firm AUA. Any DE/RD per-advisor portal validation against this reference is misleading/useless, and it can mask a real per-advisor rendering bug.
- **Proposed fix:** Detect the no-role-data case (architect all in {Unassigned,Unresolved} or single distinct value) and emit top_advisors: [] plus a note (e.g. 'advisor breakdown N/A: firm has no role attribution'), rather than a single Unassigned bucket. Cleaner: gate the advisor section off for cot since the 49F role model does not apply.

## Finding 3 -- [low/unguarded-read/full]
- **Location:** `E_21.generate_reconciliation_reference.py:83 (CLIENT_PERFORMANCE) and :102 (ACCOUNT_PERFORMANCE) via _read_s3 :49-51`
- **Mechanism:** _read_s3 issues a bare s3.get_object + read_parquet with no error handling. The author guarded the ACCOUNT_TEAM read (try/except -> empty DF, :107-110) and the NNA read (None-guard, :114-115) but NOT the two primary reads. NoSuchKey/FileNotFound propagates uncaught and exits E_21 non-zero. NOTE: E_21 is NOT in the dispatcher catalog or any chain (full/incremental/canonical/downstream), so this aborts only the standalone diagnostic run, NOT the nightly gold chain.
- **Failure scenario:** On a first-run or partial-rebuild firm state where gold/timeseries/client_performance.parquet (or account_performance.parquet) does not yet exist, _read_s3 raises botocore NoSuchKey -> uncaught -> E_21 exits 1 with a raw stack trace instead of a clear 'input missing' message.
- **Proposed fix:** Not required for chain safety. If hardening, wrap the two primary reads with a clear 'required input <key> missing' message and return 1; or mirror the team try/except pattern.

## Finding 4 -- [low/empty-null-handling/full]
- **Location:** `E_21.generate_reconciliation_reference.py:94-96`
- **Mechanism:** When cp is empty, target_date resolves to NaT, cp_day is empty, available = cp['date'].unique() is a zero-size datetime64 array, prior is empty, and the else-branch calls available.min() on the empty array, which raises numpy ValueError 'zero-size array to reduction operation minimum which has no identity'.
- **Failure scenario:** client_performance.parquet exists but has 0 rows (e.g. a botched/partial C_02 write) -> E_21 crashes at pd.Timestamp(available.min()) with a numpy ValueError rather than reporting 'no client_performance data'.
- **Proposed fix:** Guard before the fallback: `if len(available) == 0: print('ERROR: client_performance is empty'); return 1`.

## Finding 5 -- [low/schema-column/full]
- **Location:** `E_21.generate_reconciliation_reference.py:125-129`
- **Mechanism:** relationship_id, num_accounts, cum_inflows, cum_outflows, and nna are read from cp_day WITHOUT the `if 'col' in cp_day.columns` guard that the author applied to aua_taxable/aua_tax_deferred/aua_tax_exempt (:122-124). C_02.client_performance is absent from the local tree, so COT's client_performance schema cannot be confirmed here.
- **Failure scenario:** If COT's client_performance omits any of these columns (e.g. 'cum_outflows' or 'nna' not computed for this firm) -> KeyError at firm-metric construction -> E_21 aborts. Lower confidence because the same cloned C_02 likely emits them, but the asymmetric guarding shows the author already knows some columns are firm-optional.
- **Proposed fix:** Apply the same `round(float(cp_day['col'].sum()), 2) if 'col' in cp_day.columns else None` guard used for the tax-bucket columns to cum_inflows/cum_outflows/nna/num_accounts/relationship_id.

## Finding 6 -- [low/type-issue/full]
- **Location:** `E_21.generate_reconciliation_reference.py:149 (merge) and :170 (isin)`
- **Mechanism:** account_id is assumed to have an identical dtype across account_performance (ap_day), account_team (team), and canonical/nna (nna_day). If team's account_id is object and ap_day's is int64, the line-149 merge raises pandas ValueError ('trying to merge on object and int64 columns'). On line 170, arch_accounts (a set of team account_ids) .isin() against nna_day['account_id'] with a str-vs-int mismatch silently returns all-False, so the advisor NNA fields are silently omitted (no crash). Provenance suggests all three share an object account_id (C_07/C_01 both build from the same account universe), so this is lower-likelihood.
- **Failure scenario:** If a future silver/gold change makes account_team.account_id object 'ACC123' while account_performance keeps int64 -> line-149 merge ValueError aborts E_21. If instead nna_day.account_id is int64 while team's is object -> line-170 .isin is all-False -> every top advisor's nna_txn/daily_inflow/daily_outflow silently dropped from the reference.
- **Proposed fix:** Normalize account_id to str on ap_day, team, and nna_day (e.g. df['account_id'] = df['account_id'].astype(str)) before the merge and the isin().
