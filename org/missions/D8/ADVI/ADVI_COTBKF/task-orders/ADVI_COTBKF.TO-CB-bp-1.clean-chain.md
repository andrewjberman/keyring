# TO ADVI_COTBKF.TO-CB-bp-1.clean-chain -- round 68 CB-bp-1: the chain runs from a clean checkout and its price input is reproducible

<to_id>ADVI_COTBKF.TO-CB-bp-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~101</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bp-1` (`decompositions/ADVI_COTBKF_DECOMP.round68.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** rows ADVI_COTBKF-D2-W99-S1 and D2-W99-S2 in the channel; `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_68_20261011.md` section 2 (last paragraph) and section 3
item 1; `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json` (the pin and the commands of the chain); `data/assets/scripts/silver/commonwealth_sweep_regrade.py` (its argument
list, `r25_month_lines` and every argument that names a round-22, round-24 or round-27 grades, movers, causes or traced file) and
`commonwealth_daily_valuation.py` (the as-traded price input and its `store_as_of` column, near `as_traded_store` and `run`).

**The two defects.**
- **W99-S1.** In a fresh checkout the regrade stops at its REPORT step: five inputs (round 22/24/27 grades, movers, causes) are
  untracked files that exist only in one worktree's scratch. The chain's tables do not need them; the report does.
- **W99-S2.** The as-traded price input carries a column stamped from the price store's CURRENT LastModified, a second live read.
  It does not reach the returns, but that file's hash differs run to run.

**Your item.**

1. **The regrade completes from a clean checkout with no extra flag.** Either each of the five inputs is REBUILT by a named step the
   regrade (or a documented one-line command) runs from tracked code and the pinned local inputs, or the report sections that need
   them are written as `NOT AVAILABLE: <which input>` when it is absent, with the tables unaffected and the regrade's LAST line
   saying how many report inputs were absent. **Do not commit those parquet files into the tree:** they carry account ids and the
   project's own scan would refuse them.
2. **The price input is reproducible.** The live-stamped column is either taken at a named instant (a `--price-store-as-of` that
   follows the same rule as `--split-store-as-of`, by object version, refusing without it) or DROPPED from the file if nothing reads
   it. Find its readers first (`comp-find` on the column's name over `data/assets/scripts`, denominator in your report) and say which
   you chose and why. Two runs then give the same sha256 for the price input file.
3. **Proof, from a clean checkout.** Your worktree IS a clean checkout: no file from another worktree's scratch may be on any command
   line (the pinned local caches under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` are inputs, read-only; copy the price cache into your own scratch as `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json`
   describes). Run the regrade at `--split-store-as-of 2026-10-09T11:52:52Z` with the served build's settings and NO report-input flag: it
   completes, rc 0; its `after/security_day_price.parquet` equals the one the round-67 Proof A run produced if that run is still on
   this box (`C:/dev/wk-cotbkf-81/.scratch/w99/proofA/after/security_day_price.parquet`, READ-ONLY), else say it was not compared. Run
   the valuation step twice: the price input's sha256 is equal.
4. Tests for both changes (synthetic). Keep every existing `==`.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~101/CLEAN_CHAIN.json`. Top-level keys, exactly: `report_inputs` (a list of `{"input", "treatment": "REBUILT"|"NOT_AVAILABLE_LINE"}`),
   `clean_run` (`{"rc", "extra_flags", "report_inputs_absent"}`), `price_input` (`{"treatment": "PINNED"|"DROPPED", "readers_found",
   "sha256_run1", "sha256_run2", "equal"}`), `tables_equal_to_proof_a` (true | false | "NOT_COMPARED"), `tests_added`, `tests_changed`,
   `not_established`.

### ACCEPTANCE

<criterion id="CB68bp1-AC1" cell_refs="CB-bp-1"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB68bp1-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB68bp1-AC2" cell_refs="CB-bp-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~101/CLEAN_CHAIN.json',encoding='utf-8'));c=d['clean_run'];p=d['price_input'];print('CLEAN-CHAIN-RECORD rc=%d extra_flags=%d report_inputs=%d price_input=%s price_input_equal=%s tables_equal_to_proof_a=%s'%(c['rc'],c['extra_flags'],len(d['report_inputs']),p['treatment'],p['equal'],d['tables_equal_to_proof_a']))"</invocation><expect>CLEAN-CHAIN-RECORD rc=0 extra_flags=0 report_inputs=5</expect></criterion>
`CB68bp1-AC2` -- the regrade ran clean with no extra flag, all five report inputs have a stated treatment, and the price input's two
hashes are printed with whether they are equal. The issuer reads `price_input_equal` and `tables_equal_to_proof_a`.

<expected_criteria>CB68bp1-AC1,CB68bp1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch** the mint adapter (`commonwealth_account_return_daily.py`), `commonwealth_flows.py`, `commonwealth_fwd3_serve.py`,
  any manifest already committed, anything under `data/assets/scripts/gold/` or `lib/`.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets and listings the build already makes are allowed.
  No push. No `--refresh`.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, prices per security, ratios,
  version ids and reason codes only. A build log line that prints `read_account=` is never echoed: filter it out before you read a log.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Sequencing:** never start a later step before the earlier one's check has been read.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W101-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/analysis/commonwealth_price_census.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round68.md</decomp_doc> (round 68), cell `CB-bp-1`.
<owned_cells>CB-bp-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB68bp1-AC1, CB68bp1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~101/ADVI_COTBKF.TO-CB-bp-1.clean-chain.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB68bp1-AC1,CB68bp1-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** each of the five report inputs and its treatment; the clean run's command, duration, rc and last line; the price input: readers found (with the census denominator), the treatment and why, the two sha256 values; whether the tables equal Proof A's; tests added and changed, by name; the diff stat; the pytest line; the `CLEAN-CHAIN-RECORD` line; a statement that nothing was written remotely; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a hand-run build.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and version listings on stores this build already reads; BLIND: comp-iam was not run by the issuer.
comp-adversary: RUN -- the proof is a run from the worker's own fresh worktree with no extra flag and no foreign scratch path; the account-bearing parquet inputs are barred from the tree; the price input's reproducibility is shown by two hashes; BLIND: a sixth untracked input a different report path would need.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-68 analysis @b3a272fffc (msg 5008), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v38 @931dc9ea93.
