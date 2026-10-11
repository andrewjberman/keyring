# TO ADVI_COTBKF.TO-CB-bq-1.price-cache-and-default -- round 69 CB-bq-1: the Yahoo close cache is given by a flag and named in the pin record; method_r29 is the default (PRD v0.6)

<to_id>ADVI_COTBKF.TO-CB-bq-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~106</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bq-1` (`decompositions/ADVI_COTBKF_DECOMP.round69.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** row ADVI_COTBKF-D2-W101-S1 in the channel; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_69_20261011.md` section 2 (item 1 and the last paragraph) and section 3 item 1;
`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` from the heading `## ADDENDUM v0.5` to the end; `data/assets/scripts/silver/commonwealth_daily_valuation.py` (`YAHOO_CACHE`
near line 202, `read_yahoo_close`, `as_traded_store`, `split_store_record`, `write_split_pin`, `main`);
`data/assets/scripts/silver/commonwealth_sweep_regrade.py` (how it calls the valuation and passes `--price-cache`);
`data/assets/scripts/silver/commonwealth_fwd3_serve.py` (where `fwd3_manifest.json` gets `split_store`);
`data/assets/scripts/silver/commonwealth_sweeps.py` lines 90 to 105 (`CASH_LEG_DEFAULT`).

**Two changes.**

**A. The Yahoo close cache is an input like any other (D2-W101-S1).** The as-traded basis reads 3,580 untracked files from a fixed
path, `<root>/.scratch/advi_cotbkf/yahoo_census`, with no flag and no record of what it read.
1. `--yahoo-cache <dir>` on every entry point that reads it (the valuation and the regrade). With the as-traded basis and no flag the
   run REFUSES: `REFUSED: the as-traded basis reads a Yahoo close cache; pass --yahoo-cache <dir>`. The fixed default path goes.
2. What was read is recorded: the pin sidecar (`split_store_pin.json`) and so `fwd3_manifest.json` gain a `price_caches` object with,
   for the Yahoo cache AND for the `--price-cache` directory: the path as given, the file count, and one sha256 over the sorted
   `(file name, file sha256)` pairs. The run prints one line beginning `PRICE-CACHE-PIN`.
3. Tests (synthetic directories): the refusal; the digest is stable across two reads and changes when one file's bytes change; a basis
   that does not read the Yahoo cache does not demand the flag.

**B. `method_r29` is the default (PRD ADDENDUM v0.5 as narrowed by ADDENDUM v0.6 @df488019bf: `method_r29` is `method_r28` plus one rule -- a federal or state withholding row (`ftax`, `stax`) on the cash line is an external outflow, with or without a same-day withdrawal; foreign tax (`frntax`) is NOT covered and stays inside the return).** `CASH_LEG_DEFAULT` becomes `method_r29`,
its comment cites "PRD ADDENDUM v0.6 @df488019bf"; the docstrings that say r28 is the default say r29; every test that asserts the
default is r28 asserts r29 (round 65 found five; name each you change). `method_r28` selected explicitly is unchanged.

**Proof.** From your worktree: the regrade at `--split-store-as-of 2026-10-09T11:52:52Z` with `--after-cash-leg method_r29`, the served
build's other settings, `--price-cache` and `--yahoo-cache` pointing at your OWN copies of the pinned directories
(`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3/price_cache`, `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census`), completes rc 0 and prints both pin lines; its
`after/security_day_price.parquet` has sha256 `3521815d...` (the value rounds 67 and 68 measured at this pin: read the full value from
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~101/CLEAN_CHAIN.json` or recompute it from that worker's record,
and say which).

Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~106/PRICE_CACHE_PIN.json`. Top-level keys, exactly: `flag`, `refuses_without_flag`, `price_caches` (the object the run recorded),
`default_leg`, `tests_changed_for_default` (names), `tests_added`, `proof` (`{"rc", "price_table_sha256", "equals_round_68"}`),
`not_established`.

### ACCEPTANCE

<criterion id="CB69bq1-AC1" cell_refs="CB-bq-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB69bq1-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB69bq1-AC2" cell_refs="CB-bq-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~106/PRICE_CACHE_PIN.json',encoding='utf-8'));p=d['proof'];c=d['price_caches'];print('PRICE-CACHE-PIN-RECORD refuses_without_flag=%s caches=%d default_leg=%s proof_rc=%d equals_round_68=%s tests_changed_for_default=%d'%(d['refuses_without_flag'],len(c),d['default_leg'],p['rc'],p['equals_round_68'],len(d['tests_changed_for_default'])))"</invocation><expect>PRICE-CACHE-PIN-RECORD refuses_without_flag=True caches=2 default_leg=method_r29 proof_rc=0 equals_round_68=True</expect></criterion>
`CB69bq1-AC2` -- the cache is given by a flag and recorded, the default leg is `method_r29`, and the run at the served pin gives the
price table rounds 67 and 68 measured.

<expected_criteria>CB69bq1-AC1,CB69bq1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** the mint adapter (`commonwealth_account_return_daily.py`), `commonwealth_flows.py`,
  `commonwealth_price_census.py` (another cell edits it), any manifest already committed, `data/assets/scripts/gold/`, `lib/`.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets, heads and listings are allowed where the cell
  says so. No push. No `--refresh`. No vendor call (no Yahoo, no Bloomberg).
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids, ETags and reason codes only. A build log line carrying `read_account=` is never echoed: filter it out.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W106-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/commonwealth_price_basis_census.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round69.md</decomp_doc> (round 69), cell `CB-bq-1`.
<owned_cells>CB-bq-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB69bq1-AC1, CB69bq1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~106/ADVI_COTBKF.TO-CB-bq-1.price-cache-and-default.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB69bq1-AC1,CB69bq1-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the flag, where it is accepted and the refusal text; the `price_caches` object and the `PRICE-CACHE-PIN` line; the default line and every test changed for it, by name; tests added; the proof run's command, duration, rc and price-table sha256; the diff stat; the pytest line; the `PRICE-CACHE-PIN-RECORD` line; a statement that nothing was written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a hand-run build.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and version listings on stores this build already reads; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- an as-traded run with no cache flag refuses, so the untracked fixed path cannot return as a default; the cache digest is over file bytes; the proof run must reproduce the price table two earlier rounds measured at this pin; the default move follows PRD ADDENDUM v0.6, and the issuance gate itself refuses these orders until its ratified-text half is signed; BLIND: a third untracked input another basis would read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-69 analysis @e0f9682779 (msg 5206), section 3 item 1, and PRD ADDENDUM v0.6 @df488019bf (msg 5217); `3.0.0_SA_CVO` REMEDIATION_v39 @22e2566c22.
