# AMGT_CORPUS task order -- `CRPS-e-2` -- ROUND 3: the Model-block pull's field lists gain the 22 added mnemonics the team's own sheets call, with basis text; the dry run shows them; NO vendor call in this cell

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-e-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~4</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 and calls no vendor; the pull is the issuer's drain act under Andrew's word.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~4`**, slot `~4` of round 3. Serves **FWD-12** (the Model tab's rows carry figures for the 22 added
mnemonics). **First read `integrations/bloomberg/READ_HERE.md`.** NEVER call Bloomberg, NEVER import or exercise the blp client, NEVER
run the puller without `--dry-run`: the dry run stops before the client and writes nothing, and that is the only run you make.

## 1. THE CELL -- `CRPS-e-2`

**Where this came from.** `integrations/bloomberg/research/model_block_pull.py` pulls a fixed field set (header 18, history 23,
forecast 5) and lands raw bronze per security. The corpus's typecast (`research-model-typecast`, 96 workbooks) measured the team's
own mnemonic core; 22 of those mnemonics are absent from the pull, so the dossier's Model rows read ABSENT-with-reason for them
(brief `docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md` VIII-4; sizing `deliverables/2.0.0_SA_COO~X/FWD12_PULLER_SIZING_20260924.md`).

**RULED -- what you build (`model_block_pull.py`, one new test file):**
- The 22, exactly and only these, join the request lists: history (into `HIST_FIELDS`): `EQY_SH_OUT_TOT_MULT_SH EQY_RAW_BETA
  BS_CASH_NEAR_CASH_ITEM BS_TOTAL_LIABILITIES IS_ADJUSTED_GROSS_PROFIT IS_ADJUSTED_OPERATING_INCOME IS_COMP_EPS_ADJUSTED NET_INCOME
  EQY_DPS IS_DIL_EPS_CONT_OPS PX_TO_FREE_CASH_FLOW GROSS_MARGIN EBITDA_TO_REVENUE RETURN_ON_CAP RETURN_ON_INV_CAPITAL
  RETURN_ON_TANGIBLE_ASSETS` (16); estimates (into `FORECAST_FIELDS`, requested with the same `BEST_FPERIOD_OVERRIDE` shape as
  today's five): `BEST_DIV_YLD BEST_EBIT BEST_NET_INCOME BEST_CAPEX BEST_ESTIMATE_FCF BEST_BPS` (6).
- Each gains a `FIELD_BASIS` entry in the module's existing plain grammar (Bloomberg's own definition, no other vendor's name);
  no existing field, basis text, cap (`--securities` at most 3), landing address or derive rule changes.
- `test_model_block_22_fields.py`: asserts the 22 are present exactly once each across the request lists, that the lists carry
  46 + 22 distinct names, that every one of the 22 has a basis entry, and (a fixture, no network) that `cmd_pull(dry_run=True)`'s
  printed request lines carry them; the module imports without blpapi.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_model_block_22_fields.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-2.model-block-22-mnemonics.md
</paths>

READ-ONLY: everything else under `integrations/bloomberg/`, `lib/research/harvest/`, `lib/research/corpus/`. Scratch `.scratch/e2/`.
Your deliverables dir: `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/`. The module runs as a script with the
repo on `PYTHONPATH` (no package marker in its directory).

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO vendor call, NO S3 write, NO change to any cap or existing basis text.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W4-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-e-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e2_AC1.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-e-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e2_AC2.sh</invocation><expect>(?s)DRY-RUN PULL: ASML_NA_Equity.*EQY_SH_OUT_TOT_MULT_SH.*RETURN_ON_TANGIBLE_ASSETS.*BEST_ESTIMATE_FCF.*DRY RUN PULL DONE: 1 of 1 securities planned, 0 written</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-e-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e2_AC3.sh</invocation><expect>REFUSE: more than 3 securities requested</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the module's own dry run (no client, no write) states the 22 in its request lines;
  AC3 the bound: the 3-security cap stays (the drain runs batches of 3).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~4/AMGT_CORPUS.TO-CRPS-e-2.model-block-22-mnemonics.proof_of_spec.json`
   (shape: any round-2 instance under `deliverables/0.9.0_WK_AMGT_CORPUS~2/`).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the AC2 request lines' field counts (header / history / forecast), and the AC3 refusal line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the PULL is the issuer's drain act under Andrew's per-use word (record `org/tier1_exec/2.0.0_SA_COO~X/deliverables/
ANDREW_DIRECT_20260924_132xZ_OPEN_CALL_APPROVED_ALL_OPTIONS_IN_ORDER.md` @`16ee7f6373`, CTO R-70 + msg 25701: ONE use, the 22 only,
Bloomberg only, scripted per R-21). Class WORLD by the CTO's read (the run leaves Opal infrastructure): the drain opens a
change-management entry, runs `READ_HERE` s.2 + `bloomberg_health`, then the pull over the resolved keys in batches of 3 and
`derive` per security, read-back recorded; the CTO's exercised read follows. The file is the Bloomberg lane's; granted to this
worker by `<paths>` for this order only. Checks dry-run at the base: AC1 FAIL (no such test file), AC2 FAIL (fields absent),
AC3 PASS (the cap) -- recorded in the issuance commit.

<risk>WORLD</risk>
<status>pending</status>
<round>3</round>
<slot>~4</slot>
<fabric>site-z</fabric>
