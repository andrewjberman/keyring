# ETFS_RIVALS task order -- `RIV-rk-2` -- ROUND 6 (ENRICHMENT): THE A1 PLAUSIBILITY GUARD (analysis cell 2, CRO~RV CALL 13 C1 amended)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rk-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-rk-2` -- the A1 plausibility guard (analysis cell 2; CRO~RV CALL 13 C1 as amended)
- `gold_holding_contribution.plausibility_guard(df, bounds=None) -> df`, applied in `handler_entry` before the write.
- Per fund x period, never the table, the rows give way to ONE row: axis "refused", bucket = the bound, contribution = the
  offending value.
  - (a) a total below -100% -> `total_below_minus_100pct` (hard), checked first;
  - (b) one holding with |c| above `contribution_single_holding_bound` (guardrails_config.json, value 0.25, status
    PROVISIONAL) -> `single_holding_above_bound`;
  - (c) NAV reconciliation where a NAV is on file, its tolerance from the residual distribution. It ships as a documented
    hook; no NAV is on file today.
- The page's refusal display is u-2's.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- CRO~RV CALL 13 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md` @6e3c94774a): refusal per fund x period, never the table; bounds STRUCTURAL, not from the peer distribution.
- Measured 2026-10-02 14:2xZ on the served 10-01 and 10-02 tables: lowest fund x period total -4.9%, largest single holding 3.6% -- the guard refuses nothing today.
- `guardrails_config.json` entries are `{value, status, note}`; read through `guardrails.load_config()`.
- The page's 'Rankings refused' display is cell ui-2's, not yours (render.py is chain ~6's).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6rk2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/guardrails_config.json
data/etfs/scripts/rivalfunds/tests/test_r6rk2_*.py
data/etfs/scripts/rivalfunds/tests/test_a1rk_contribution.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a planted -188% fund x period is ONE refused row naming bound (a); TXUE untouched; the served 2026-10-02 table refuses nothing (S3 READ-ONLY) (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/rk-2.AC1.py`)
- **AC2** -- the 0.25 PROVISIONAL single-holding bound is in guardrails_config; 0.31 refuses as bound (b), 0.24 passes (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/rk-2.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rk-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/rk-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-rk-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/rk-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-rk-2.a1-plausibility-guard.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rk-2.a1-plausibility-guard`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~2`, slot `~2`, position 1 of 2 (rk-2 -> sx-1). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
rk-2.AC1 FAIL (no plausibility_guard) as expected; rk-2.AC2 FAIL (no config entry, no guard) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>6</round>
<slot>~2</slot>
<fabric>site-z</fabric>
