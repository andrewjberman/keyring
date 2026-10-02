# ETFS_RIVALS task order -- `RIV-st-1` -- ROUND 6 (ENRICHMENT): AN A1 TABLE FOLLOWS ITS INPUTS (RFW-D01, RFW-D02)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-st-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-st-1` -- an A1 table follows its inputs (RFW-D01 lead, RFW-D02)
- `publish_page.a1_stale(s, day, table) -> bool` is True when the newest G1 `canonical_shape` or G4 `security_market` object
  in the table's input window carries a revision timestamp (the `YYYYMMDDTHHMMSSZ` in its name) strictly later than the
  table's newest object's.
- `produce_a1` rebuilds a stale table without `refresh_a1`. The manifest's `a1_produced[<table>]` records
  `stale_rebuilt: true` and `stale_input` (the newer input's uri).
- A rebuild leaves the table NOT stale: its newest object's revision time is no earlier than the newer input's, even when its
  content is identical (today `write_unique` writes nothing on identical content).
- With no newer input, the table SKIPS as today.
- Shared fixture: `round6/checks/_d1_page.py`.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- Today `publish_page.produce_a1(s, sink_spec, day, refresh=False)` (~251) skips a table when an object for the date already exists (manifest '1 object(s) already at date=...'). On 2026-10-02 the A1 tables built at 11:03Z missed the 11:11Z G1 refresh and the 11:10Z G4 object (RFW-D01; the issuer refreshed today's page by hand, pair @c1bf9ac157).
- Object names carry the revision time: canonical_shape `holdings-<YYYYMMDDTHHMMSSZ>-<sha>.parquet`, G4 `market-...`, A1 `<table>-<YYYYMMDDTHHMMSSZ>-<sha>.parquet`; `revision.newest` orders them.
- `write_unique` writes nothing on identical content. A stale rebuild must still leave the table not stale (its newest revision time no earlier than the newer input's).
- 'later than' is strict; the checks keep a one-second margin on both sides.
- Shared fixture `round6/checks/_d1_page.py` (it stubs `market_context.read_context` to no readings so the census reads no S3).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6st1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/test_r6st1_*.py
data/etfs/scripts/rivalfunds/tests/test_a1_produce_wiring.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a planted newer G1 object makes the next publish (no refresh_a1) write a new holding_contribution object; the manifest reads stale_rebuilt true with stale_input (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/st-1.AC1.py`)
- **AC2** -- control: with no newer input a second publish SKIPS, as today (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/st-1.AC2.py`)
- **AC3** -- a1_stale exists and reads False for every table right after a rebuild; the census and the page read one G1 vintage (D02) (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/st-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-st-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/st-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-st-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/st-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-st-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/st-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-st-1.a1-follows-its-inputs.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-st-1.a1-follows-its-inputs`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~1`, slot `~1`, position 1 of 3 (st-1 -> ap-1 -> r-6). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
st-1.AC1 FAIL (2: no new object, manifest SKIPPED) as expected; st-1.AC2 PASS (control) as expected; st-1.AC3 FAIL (6: a1_stale missing; the D02 split reproduced) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>6</round>
<slot>~1</slot>
<fabric>site-z</fabric>
