# TO ADVI_COTBKF.TO-CB-bw-5.nine-accounts -- round 75 CB-bw-5: the nine accounts the changes sit in: funds, trade days and the share of each account's served days that change; counts only, no id

<to_id>ADVI_COTBKF.TO-CB-bw-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~136</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bw-5` (`decompositions/ADVI_COTBKF_DECOMP.round75.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a COUNT on copies. You change no code. Nothing is served or fetched. NO ACCOUNT ID LEAVES YOUR SCRATCH.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` section 1 ("changes on 1,577, all of them in 9 accounts") and section 3 item 5 ("The nine accounts: how
many funds, how many trade days, and what share of each account's served days change. Counts only; no account id leaves the worker's
folder."); row ADVI_COTBKF-D2-S127 in the channel (554 dates and 9 accounts); the round-74 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`.

**The two builds of round 74 are your input, READ ONLY:** `C:/dev/wk-cotbkf-83/.scratch/w129/fwd3_baseline/` and `C:/dev/wk-cotbkf-83/.scratch/w129/fwd3_variant/` (each:
`daily_returns.parquet` with account, date, value, flow, return, blank_reason; `account_day_value.parquet`), and
`C:/dev/wk-cotbkf-83/.scratch/w129/baseline_out/` and `C:/dev/wk-cotbkf-83/.scratch/w129/variant_out/` (the valuation's own tables, the security-day prices among them). The baseline
equals the served table; the variant differs in the price of 19 validated funds alone (record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`). You modify nothing in that
folder and build nothing new: no S3 read, no fetch.

**Your item.**

1. **Reproduce the nine:** the changed account-days at a floor of 1e-12 (1,577) and of 1e-9 (1,575), the distinct dates, the distinct
   accounts. If the account count is not 9, say what it is at each floor and carry on with what you measured.
2. **Label them `A1` to `A9`** in descending order of changed account-days (ties by first changed date). The mapping stays in your
   scratch. Per label, counts only: changed account-days, by band (under 1, 1 to 10, over 10 basis points); the account's served
   measured days and the share of them that change; how many of the moved validated funds it holds on a changed day, and which (by
   ticker: a fund is not client data); days with a share-moving row in one of those funds (purchases, sales, reinvestments,
   transfers, each counted); first and last changed date; higher and lower.
3. **Concentration:** the share of all changed account-days, and of all changes over 10 basis points, in the top one, two and three
   accounts. Whether any account's changes are all one fund.
4. **Accounts that hold a moved fund and do NOT change:** how many accounts hold one of the 19 moved funds on a day both builds
   price, and how many of those have no measured day at all on such days (the table is about 94 percent blank). So the reader can
   see whether nine is small because the defect is small or because few holders are measured.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~136/NINE_ACCOUNTS.json` and a short `.md`. NO per-account value, flow, return or balance; no id. Top-level keys, exactly:
   `changed` (`{"floor_1e12", "floor_1e9", "dates", "accounts"}`), `accounts` (a list of nine objects keyed by `label`),
   `concentration` (`{"top_1", "top_2", "top_3", "over_10bp_top_1"}`), `holders_of_a_moved_fund` (`{"accounts", "with_a_measured_day",
   "without"}`), `labelling_rule`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB75bw5-AC1" cell_refs="CB-bw-5"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~136/NINE_ACCOUNTS.json',encoding='utf-8'));c=d['changed'];a=d['accounts'];h=d['holders_of_a_moved_fund'];print('NINE-ACCOUNTS changed=%d/%d dates=%d accounts=%d labels=%s per_account_sum=%d top_1=%s holders=%d with_a_measured_day=%d without=%d'%(c['floor_1e12'],c['floor_1e9'],c['dates'],c['accounts'],','.join(x['label'] for x in a),sum(x['changed_account_days'] for x in a),d['concentration']['top_1'],h['accounts'],h['with_a_measured_day'],h['without']))"</invocation><expect>NINE-ACCOUNTS changed=1577/1575</expect></criterion>
`CB75bw5-AC1` -- the changed account-days are reproduced at both floors and split over labelled accounts whose counts sum to the
total. The issuer reads the account count, the concentration and the holders with no measured day.

<expected_criteria>CB75bw5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call, no new build.
- **Accounts.** Inside your own scratch you work with account ids as the tables hold them. NOTHING you commit, print in your report
  or write to the channel carries an account id, or an account's value, flow, quantity, balance or return. Where accounts must be
  told apart, label them `A1` to `A9` by a rule you state, and keep the mapping in your scratch only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W136-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round75.md</decomp_doc> (round 75), cell `CB-bw-5`.
<owned_cells>CB-bw-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB75bw5-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~136/ADVI_COTBKF.TO-CB-bw-5.nine-accounts.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB75bw5-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the changed account-days at both floors, the dates and the accounts as reproduced; the labelling rule; per label, the counts; the concentration; the holders of a moved fund with and without a measured day; the headline; the `NINE-ACCOUNTS` line; the account-id scan's DENOMINATOR line; a statement that no account id, value, flow or return left the scratch; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the reviewer's 1,577 and nine accounts are the positive control; accounts are labelled by a stated rule and the mapping never leaves the scratch; the cell counts the holders who are never measured, so a small account count is not read as a small defect; BLIND: an account whose only holding day is blank in both builds.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-75 analysis @cd481e59d2 (msg 5920), section 3 item 5; `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
