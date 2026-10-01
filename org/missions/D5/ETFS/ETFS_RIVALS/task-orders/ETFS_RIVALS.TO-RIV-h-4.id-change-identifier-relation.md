# ETFS_RIVALS task order -- `RIV-h-4` -- ROUND 5 (ENRICHMENT): AN ID-CHANGE NEEDS AN IDENTIFIER RELATION; CUSIPS ZERO-PADDED AT SILVER (HOP-9 a)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-h-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-5 decomposition; declared on RIV-b-2 and RIV-l-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-h-4` -- an ID-CHANGE needs an identifier relation; CUSIPs zero-padded at silver (hop-9 ruling a)

**When an exit and an entry pair as ID-CHANGE.** Only when one of these holds:
- a G3 or issuer-published identifier event names both;
- a crosswalk hit (ISIN, SEDOL or FIGI) maps one to the other;
- the two CUSIPs are equal after normalisation.

A shared CUSIP-6 qualifies only alongside a G3 event. Equal value alone stays an exit plus an entry, with real share counts.

**Normalisation.** `silver_issuer.parse_capture` zero-pads a CUSIP of 1-8 characters to 9 (BP `55622104` -> `055622104`).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- `gold_trade_schedule._id_changes` (~315-331) greedily pairs exits to entries when `abs(va - vb) <= ID_CHANGE_TOL *
  max(va, vb)` (`ID_CHANGE_TOL` 0.01, ~105) -- no identifier test; called ~463; emitted as ONE row of action `exit`, confidence
  `ID-CHANGE`, `counterpart_security_key` the new key (~522-525). `stable_key` (~223-241) takes `security_cusip` first.
- Nothing normalises a CUSIP: `silver_issuer.parse_capture` (~55-89) keeps identifier columns verbatim (`STRING_COLS` ~42);
  G1 `_identity` only strips.
- Measured on served G1: PFOE's window 2026-09-25 -> 2026-09-28 pairs Universal Music Group `91377B109` -> Quanta Services
  `74762E102` as an ID-CHANGE (the CTO's ruling (a) acceptance case).
- Existing tests that assert a value-only ID-CHANGE and must flip: `test_g2_trade_schedule.py` ~78-90,
  `test_i1_trade_stable_key.py` ~90-92.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5h4_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/silver_issuer.py
data/etfs/scripts/rivalfunds/tests/test_r5h4_*.py
data/etfs/scripts/rivalfunds/tests/test_g2_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_i1_trade_stable_key.py
data/etfs/scripts/rivalfunds/tests/test_s1_silver_issuer.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- silver pads 55622104 -> 055622104; equal value alone infers an exit plus an entry (no ID-CHANGE); control: an 8/9-char CUSIP pair never splits (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-4.AC1.py`)
- **AC2** -- on SERVED G1 (READ-ONLY), PFOE's window to 2026-09-28 reads UMG 91377B109 as an exit and PWR 74762E102 as an entry, no ID-CHANGE (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-4.AC2.py`)

**Time bound (fabric ruling 9):** `h-4.AC2` read a whole window or a 50-date fixture: run it under `timeout 600`, not 120. rc 124 is a timeout, never a FAIL; report it as such.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-h-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-4.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-h-4"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-4.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-h-4.id-change-identifier-relation.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-h-4.id-change-identifier-relation`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: h-4.AC1 FAIL, h-4.AC2 FAIL -- each FAIL as expected, each control PASS.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>5</round>
<slot>~3</slot>
<fabric>site-z</fabric>
