# TO IRPT_DASHBD.TO-DB-b-71 -- E2: FWD-11 Cottonwood -- its adapter's account_return_daily, offline on a sample, tied out against its own reported source (Commonwealth)

<to_id>IRPT_DASHBD.TO-DB-b-71</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~48</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-35 ADDENDUM 4 (on ADJUDICATION_v20 @e9d4ac3755; PRD v0.8 FWD-11 @e8b44a8379, amended @3eb7dbcf36 on CVO msg 2330), enrichment item E2 | **Decomp cell:** `DB-b-71` (decomposition section 38) | **outcome_ref:** FWD-11 | **depends_on:** none (offline; FWD-11 @e8b44a8379).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-48`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/`.

**The cell.** FWD-11 (Andrew-direct ~03:3xZ, PRD v0.8 @e8b44a8379, `prd/IRPT_DASHBD_PRD.md` lines 118-128 and the addendum
at line 492): Cottonwood (registry key `cottonwood`, short `cot`, master `z09`) gets the same daily account returns as 49 Financial, through its OWN adapter (C-ADAPTERS). This cell
builds that adapter's `account_return_daily` OFFLINE, on a sample, and ties it out. Nothing is served.

- **Read first.**
  - The 49 Financial producer: `C:/dev/wk-irpt-dashbd-48/data/assets/scripts/gold/irpt_reporting/account_return_daily.py`
    and its declaration `sources.json` beside it. Its `doc` field gives the adapter law: one entry per custody source, vendor codes only
    inside their own adapter, no firm token in the file.
  - The contract: `C:/dev/wk-irpt-dashbd-48/org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`. Your output
    carries exactly its columns.
  - The registry entry for the firm: `C:/dev/wk-irpt-dashbd-48/infra/logic/registry/scopes.json`.
  - The firm's own tree.
  - Cottonwood's only registered source is Black Diamond (master `z09`, 984 accounts measured 2026-09-24, registry note). Its tree is
    `data/cot/` (`data/cot/scripts/{silver,gold}`). Its prior state: `TO-IB-er-401_STEP0_DONE_COTTONWOOD_BLOCKED_20260929.md` (row
    IRPT_BCKEND-S203). Find both with Glob.
  - Build from the holdings, transactions and values Cottonwood already lands in its own bucket (the registry names its master `z09`
    as Black Diamond-issued ids). Name the system you read as `source`. Its vendor codes exist only inside this adapter (C-ADAPTERS).
  - PRD v0.8 @3eb7dbcf36 (CVO msg 2330): Cottonwood's reported returns are Commonwealth's, not Black Diamond's, because cot is not bd
    (CLAUDE.md rule 13: never mirror or sync). Find where Cottonwood's Commonwealth-reported returns land, and name it as
    `comparison_source`. If they are not on S3, file a row naming what is missing.

- **Isolation (CLAUDE.md HARD STOP).** This firm's data never meets another firm's in one reader, bucket or prefix.
  - Resolve every address with `lib/opal_naming.py` `lookup()` / `address()`. Never type a bucket or a firm token: the naming gate
    refuses it.
  - Your code lives in your folder only. Moving it into a pipeline tree is a later cell.
- **Sample.** At least one trading window over at least 10 accounts if the source holds them, or every account it holds if fewer.
  Print the denominator: account-days, or account-windows, whichever grain the comparison source reports.
- **Tie-out (C-TIEOUT).** PRD v0.8 @3eb7dbcf36: each firm ties out against its OWN reported source, which this cell's read names.
  Compare your `total_return_daily`, compounded over that source's own window, with its reported return for the same account and
  window, at 0.35 pp. For Cottonwood that is Commonwealth's reported return, not Black Diamond's. Every miss carries a class from a list you declare in the record
  (`classes`), with its evidence. "UNCLASSED" is not a class.
- **Record `COT_RETURNS_TIEOUT.json`:** `source` (the adapter's input system), `comparison_source` (the reported source tied out against), `accounts`, `denominator`, `within`, `tolerance_pp` (0.35), `classes`, `misses` (one entry per
  miss: a hashed account key, the window, both values, `class`), `output_columns` (read from the parquet you wrote), and `output_sha256`.
  Keep the parquet in `.scratch/`, never committed. No account number, name or balance goes in a committed `.md`.
- **If the source cannot supply a needed input** (a missing table, column or window), file a row naming exactly what is missing and keep
  going on what it does supply.

<criterion id="DB36-2-AC1" cell_refs="DB-b-71"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r36/p36_round36.py" . DB36-2-AC1</invocation><expect>DB36-2-AC1 PASS</expect></criterion>
`DB36-2-AC1` -- the sample's within-tolerance count at 0.35 pp printed with its denominator and account count, its source and comparison source named. Base: FAIL.

<criterion id="DB36-2-AC2" cell_refs="DB-b-71"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r36/p36_round36.py" . DB36-2-AC2</invocation><expect>DB36-2-AC2 PASS</expect></criterion>
`DB36-2-AC2` -- every miss classed in the record's declared classes, none UNCLASSED. Base: FAIL.

<criterion id="DB36-2-AC3" cell_refs="DB-b-71"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r36/p36_round36.py" . DB36-2-AC3</invocation><expect>DB36-2-AC3 PASS</expect></criterion>
`DB36-2-AC3` -- the adapter output carries exactly the returns contract's columns, its sha256 printed, and no S3 write call in the worker's code. Base: FAIL.

<expected_criteria>DB36-2-AC1,DB36-2-AC2,DB36-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-71.cot-adapter-returns.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 38 (round 36), cell `DB-b-71`.
<owned_cells>DB-b-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB36-2-AC1, DB36-2-AC2, DB36-2-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/IRPT_DASHBD.TO-DB-b-71.cot-adapter-returns.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB36-2-AC1,DB36-2-AC2,DB36-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the within count and denominator, the miss classes, the output columns and sha, and every row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an offline adapter run and records in the worker folder; nothing served, deployed or written to S3.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB36-2-AC1/AC2/AC3 FAIL at base (no record). Registry read @ad0dd17f7b: Cottonwood's only master is z09 (Black Diamond).
lane: the <paths> block IS the grant.
</preflight>
