# TO ADVI_COTBKF.TO-CB-br-1.open-corrections -- round 70 CB-br-1: the open corrections to the served table as ONE tracked list, each with its extent

<to_id>ADVI_COTBKF.TO-CB-br-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~111</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-br-1` (`decompositions/ADVI_COTBKF_DECOMP.round70.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This cell writes ONE tracked file from records already in the tree. It measures nothing new and changes no code.**

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` from the heading `## ADDENDUM v0.5` to the end (v0.5, v0.6, v0.7: v0.7 says one re-serve carries every open
correction when the list closes); `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_70_20261011.md` whole; and the records below.

**Why.** PRD ADDENDUM v0.7 un-parks the single re-serve of the served table when the list of open corrections CLOSES. No such list
exists. Each correction today lives in a different round's record.

**Your item.** Write `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json`: a JSON object with `as_of` (read from the clock), `served_method` (`method_r28`), `tree_default`
(`method_r29`), `pin` (the served instant's, from the round-67 record), and `corrections`: a list with ONE entry per open correction
to the served table. The analysis names five; add any other you find in the round 64 to 69 records and say where:

1. the 2 withholding account-days whose return moves and the 42 flow cells on blank days (records: round 68
   `deliverables/0.9.0_WK_ADVI_COTBKF~104/R28_VS_R29_AT_PIN.json`; round 69 `.../0.9.0_WK_ADVI_COTBKF~107/REMINT_FACTS.json`; the issuer's
   round-69 packet `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_69_DRAIN_END_20261011.md` section 1, which carries a second count
   of the flow change, 47 rows over 46 dates on the silver table, not reconciled with the 44 over 43);
2. the 41 withholding days blank under both rules for want of a price (they read under `method_r29` if priced later);
3. the mis-scaled price series (round 69 `.../0.9.0_WK_ADVI_COTBKF~108/CLOSE_VS_TRADE_SCAN.json` and `.csv`: seven series, 470
   measured account-days, NEVER stated without the 346 too-few, the 50 thin securities with a pair beyond 10 percent, and the 1,700
   with no close);
4. the 2022 spin-off factor for one security (rows ADVI_COTBKF-D2-S118, D2-W103-S1, D2-W103-S2; round 68
   `.../0.9.0_WK_ADVI_COTBKF~103/SPINOFF_CLAIMS.json`; the 30 drift account-days of round 67 `.../0.9.0_WK_ADVI_COTBKF~100/ADDED_SPLITS.json`);
5. the late-receipt rule, NOT adopted (round 69 `.../0.9.0_WK_ADVI_COTBKF~109/RESIDUAL_RECEIPT_PREDICATE.json`: 410 measured days if it is).

Each entry carries exactly these keys: `id` (a short slug), `what` (one plain sentence), `state` (`OPEN` | `NOT_ADOPTED` |
`UNDER_MEASUREMENT`), `extent` (`{"measured_account_days", "other_cells", "day_files", "silver_objects"}`; a number, or the string
`NOT_MEASURED`, never a guess), `evidence` (a list of `{"file", "what_it_says"}`; print the line or the key you quote before you write
it, and quote numbers exactly as the record has them), `unreconciled` (a list of strings: every place two records give different
numbers for the same thing, both numbers stated), `closes_when` (what must be true for this entry to leave the list: a ruling, a
measurement, an addendum), `owner` (the seat that must act: `1.0.0_SA_CTO~DELL2`, `2.0.0_SA_COO~C2`, `3.0.0_SA_CVO`).
Also a top-level `list_closes_when` (one sentence from PRD v0.7, quoted with its line number) and `not_established`.
Write a short `OPEN_CORRECTIONS.md` beside it: one table, one row per correction.

**Rules.** A number you cannot find in a record is `NOT_MEASURED`, with the record you looked in. Where two records disagree, both
numbers go in `unreconciled`; you do not pick one. You add no opinion on whether a correction should be made.

### ACCEPTANCE

<criterion id="CB70br1-AC1" cell_refs="CB-br-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/OPEN_CORRECTIONS.json',encoding='utf-8'));c=d['corrections'];k={'id','what','state','extent','evidence','unreconciled','closes_when','owner'};print('OPEN-CORRECTIONS-RECORD corrections=%d keys_complete=%s states=%s evidence_rows=%d unreconciled=%d served_method=%s tree_default=%s'%(len(c),all(k<=set(x) for x in c),','.join(sorted(set(x['state'] for x in c))),sum(len(x['evidence']) for x in c),sum(len(x['unreconciled']) for x in c),d['served_method'],d['tree_default']))"</invocation><expect>OPEN-CORRECTIONS-RECORD corrections=</expect></criterion>
`CB70br1-AC1` -- the list exists as one tracked file, every entry carries its eight keys, and the count of corrections, evidence rows
and unreconciled numbers is printed. The issuer reads each entry against its record.

<expected_criteria>CB70br1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (the deliverables folder, where the list sits at its top level, and your own NEW channel row)
  and the file of this order.
- **You change no code, test, config, manifest or registry, and no other seat's record.** Everything is local; no AWS call.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids and reason codes only. A build log line carrying `read_account=` is never echoed.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W111-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round70.md</decomp_doc> (round 70), cell `CB-br-1`.
<owned_cells>CB-br-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB70br1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~111/ADVI_COTBKF.TO-CB-br-1.open-corrections.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB70br1-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** each correction with its state, extent, evidence files, unreconciled numbers, what closes it and its owner; any correction you added beyond the five and where you found it; every number you wrote as NOT_MEASURED and the record you looked in; the `OPEN-CORRECTIONS-RECORD` line; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE one document compiled from records in the tree.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a number absent from a record is NOT_MEASURED, never estimated; two records that disagree both appear under unreconciled; each quoted number is printed from its record before it is written; the list states no opinion on whether a correction is made; BLIND: a correction recorded only in a message and in no file of the tree.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-70 analysis @991f749df1 (msg 5340), section 3 item 1; PRD ADDENDUM v0.7 @72d624cd26; `3.0.0_SA_CVO` REMEDIATION_v40 @90e1a7cbda.
