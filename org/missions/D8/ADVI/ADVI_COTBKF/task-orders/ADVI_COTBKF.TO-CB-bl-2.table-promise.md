# TO ADVI_COTBKF.TO-CB-bl-2.table-promise -- round 64 CB-bl-2: what the PRD promises for the returns table: is income part of it

<to_id>ADVI_COTBKF.TO-CB-bl-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~91</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>64</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bl-2` (`decompositions/ADVI_COTBKF_DECOMP.round64.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ. You change nothing.** Read `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_64_20261011.md` section 2 item 1 and section 4 item 2 first.

**Why.** Every one of the 1,691,729 minted rows of Cottonwood's `account_return_daily` has `income_received` and `income_return`
null. Another project's publisher refuses a row with null income. Before anyone calls that a defect, the CTO wants to know what this
project's PRD PROMISES for that table.

**Your item.**

1. Read `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` in full. Find every sentence that states an outcome for Cottonwood's
   daily returns or for the table `account_return_daily` (the ENDPOINT outcomes, FWD-3 in particular, the contracts C-DAILY and any
   other that names returns, the manifest rows, and every ADDENDUM that names the mint). Quote each with its line number, read by
   printing the line, not by searching for words you expect.
2. Read what the mint says about income: the adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` (its header
   docstring and the dict near line 137 that explains the null columns), with line numbers.
3. Answer ONE question: **does this project's PRD include income in the outcome for that table?** `YES` (quote the sentence), `NO`
   (the outcome is stated and does not include it; quote the sentence that states it), or `NOT_STATED` (no sentence states an outcome
   for the table at all; say where the mint's requirement came from instead, with its citation).
4. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~91/TABLE_PROMISE.json` with exactly these keys: `income_in_outcome`, `paragraph` (one paragraph, plain words), `citations` (a
   list of `{"file", "line", "text"}`), `who_asked_for_the_table` (a citation), `not_established` (a list).

### ACCEPTANCE

<criterion id="CB64bl2-AC1" cell_refs="CB-bl-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~91/TABLE_PROMISE.json',encoding='utf-8'));assert d['income_in_outcome'] in ('YES','NO','NOT_STATED');print('TABLE-PROMISE-RECORD income_in_outcome=%s citations=%d paragraph_chars=%d'%(d['income_in_outcome'],len(d['citations']),len(d['paragraph'])))"</invocation><expect>TABLE-PROMISE-RECORD income_in_outcome=</expect></criterion>
`CB64bl2-AC1` -- the record exists with one of the three answers, its citations and its paragraph. The CTO reads the paragraph.

<expected_criteria>CB64bl2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** You READ local data under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` (the base checkout; never write
  there) and write scratch under your own worktree `.scratch/` only (never committed).
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. A commonwealth script you run carries
  `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round64.md</decomp_doc> (round 64), cell `CB-bl-2`.
<owned_cells>CB-bl-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB64bl2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~91/ADVI_COTBKF.TO-CB-bl-2.table-promise.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB64bl2-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the `TABLE-PROMISE-RECORD` line; the answer and the paragraph; each citation with its line; who asked for the table; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of two documents.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the answer set admits NOT_STATED so an absent sentence is not forced into YES or NO; each quote is read by printing its line; BLIND: an outcome for the table stated outside the PRD and its addenda.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-64 analysis @5cc2574c67 (msg 4579), section 4 item 2; `3.0.0_SA_CVO` REMEDIATION_v36 @877c95fb20.
