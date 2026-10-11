# TO ADVI_COTBKF.TO-CB-bq-5.store-label -- round 69 CB-bq-5: the price store called the custodian's mark is labelled as what it is: the portfolio system's snapshot price

<to_id>ADVI_COTBKF.TO-CB-bq-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~110</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>69</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bq-5` (`decompositions/ADVI_COTBKF_DECOMP.round69.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_69_20261011.md` section 2 item 2 (second bullet) and section 3 item 5; rows ADVI_COTBKF-D2-W103-S1 and D2-W103-S2 in the
channel; `data/assets/scripts/analysis/commonwealth_price_census.py` lines 50 to 75.

**The defect.** The code calls one price store "the custodian mark on a held position" (a comment at line 59 of the census script).
The reviewer found it is the PORTFOLIO SYSTEM'S snapshot price: its only `source` value is `bd_snapshot`, and its price is that
system's reported market value over units. "A value is not called the custodian's on a variable name."

**Your item. No AWS call.**

1. Correct the label wherever the code or its docstrings call that store's price the custodian's: the comment at line 59, and any other
   place. Find them: `comp-find -i "custodian mark|custodian's mark|custodian_mark"` scoped to `data/assets/scripts`, run alone and
   unpiped; quote its DENOMINATOR line. The new wording says what it is: the portfolio system's snapshot price (source `bd_snapshot`),
   its reported market value over units; whether it equals the custodian's own mark is not established.
2. **Change no behaviour and no identifier a reader depends on:** store ids, legacy address keys, column names and source values stay.
   If a NAME (a variable, a constant, a function) says "custodian" for this store and renaming it is contained in one file, rename it
   and its uses; if it crosses files or is written into data, leave it and list it in your report.
3. Do NOT touch a place where "custodian" means the custodian in fact (Commonwealth's own delivered files, the bond custodian price
   script): list the hits you left and why.
4. Run the suite.

### ACCEPTANCE

<criterion id="CB69bq5-AC1" cell_refs="CB-bq-5"><invocation>env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests -q</invocation><expect>passed</expect></criterion>
`CB69bq5-AC1` -- the silver suite passes with the variable unset: 0 failed, 0 errors, 12 skipped as before.

<criterion id="CB69bq5-AC2" cell_refs="CB-bq-5"><invocation>python -c "t=open('data/assets/scripts/analysis/commonwealth_price_census.py',encoding='utf-8').read();print('STORE-LABEL custodian_mark_hits=%d snapshot_label=%s bd_snapshot_named=%s'%(t.count('the custodian mark on a held position'),'portfolio system' in t,'bd_snapshot' in t))"</invocation><expect>STORE-LABEL custodian_mark_hits=0 snapshot_label=True bd_snapshot_named=True</expect></criterion>
`CB69bq5-AC2` -- the census script no longer calls the store's price the custodian's mark and says what it is.

<expected_criteria>CB69bq5-AC1,CB69bq5-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Comments, docstrings and contained names only.** No logic, no store id, no address key, no column or source value changes.
- **Do NOT touch** `commonwealth_daily_valuation.py`, `commonwealth_sweep_regrade.py`, `commonwealth_fwd3_serve.py`,
  `commonwealth_sweeps.py` (another cell edits them): if a hit sits in one of them, LIST it and leave it.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write.** Read-only S3 gets, heads and listings are allowed where the cell
  says so. No push. No `--refresh`. No vendor call (no Yahoo, no Bloomberg).
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids, ETags and reason codes only. A build log line carrying `read_account=` is never echoed: filter it out.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W110-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
data/assets/scripts/analysis/commonwealth_price_census.py
data/assets/scripts/analysis/
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round69.md</decomp_doc> (round 69), cell `CB-bq-5`.
<owned_cells>CB-bq-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB69bq5-AC1, CB69bq5-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~110/ADVI_COTBKF.TO-CB-bq-5.store-label.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB69bq5-AC1,CB69bq5-AC2` BEFORE the flip. Both are mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the census DENOMINATOR line; every hit changed, with file and line and the new wording; every hit left and why; names renamed or left; the pytest line; the `STORE-LABEL` line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE comments and docstrings.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- behaviour, store ids, address keys, columns and source values are barred from change; a hit where custodian means the custodian in fact is listed and left; hits in files another cell edits are listed, not edited; BLIND: wording outside data/assets/scripts (documents, the PRD) is not in scope.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-69 analysis @e0f9682779 (msg 5206), section 3 item 5, and PRD ADDENDUM v0.6 @df488019bf (msg 5217); `3.0.0_SA_CVO` REMEDIATION_v39 @22e2566c22.
