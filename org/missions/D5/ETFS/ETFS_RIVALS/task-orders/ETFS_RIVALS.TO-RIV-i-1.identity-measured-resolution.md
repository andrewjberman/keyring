# ETFS_RIVALS task order -- `RIV-i-1` -- ROUND 3 (ENRICHMENT): IDENTITY -- MEASURED RESOLUTION IN THE CROSSWALK'S KEY GRAMMAR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-i-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~06:4xZ, --drift) -- 2 armed gates fabric-wide, none names rivalfunds/ or lib/research/identity/.
comp-iam: RUN at L5 -- no IAM change; this cell reads silver already in the canonical-shape Lambda's grant.
comp-adversary: RUN at L5 on the round-3 decomposition (3 of 3 cited commits verified) and DECLARED on this cell: the identity join is the round's highest-consequence inference (every trade matches by resolved identity, C-TRADE-SCHEDULE). Its check plants an ambiguous second candidate -- the refusal arm; the 2% tolerance and its denominators were measured at the cut (34/34 BASG joined, 0 ambiguous; exact equality 0/34).
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: rival active ETFs in two peer groups, each fund's trade schedule,
and a served page. Trades are matched by RESOLVED security identity; today almost nothing resolves (BASG issuer 0 of 34 positions).
**This cell resolves identity by measurement, never by guess.** It follows RIV-hp-1 on your slot; your worktree has CLOUD merged in
first. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-i-1` -- identity: measured resolution in the crosswalk's key grammar (rows W1-S4/S5; issuer ruling 2)

- **`identity.py` (new):** `bloomberg_key(bbg_id)` -> `'<ROOT>_<CC>_<YELLOW>'` for a `'<ROOT> <CC> <YELLOW>'` Bloomberg id (else
  None); `issuer_join(...)` -> for one issuer non-cash row, the unique Bloomberg silver row of the SAME fund at the same report
  date (or the nearest Bloomberg report date within 1 trading day) whose root ticker equals the issuer `security_ticker` and whose
  `POSITION` is within 2% of the issuer `quantity`; zero candidates = miss, two or more = AMBIGUOUS (UNRESOLVED, the note names every
  candidate).
- **`gold_canonical_shape.py`:** after `crosswalk.resolve()` misses, a Bloomberg row takes `bloomberg_key(id)`
  (`resolution_method = 'bloomberg-form'`, `resolution_source` stating it is not in the AMGT pool) and an issuer row takes
  `issuer_join` (`resolution_method = 'issuer-bloomberg-join'`, the share delta in `resolution_note`); `security_bloomberg` is set from
  the joined/own Bloomberg id.
- The measured fraction per fund is reported in the cell's deliverable (`i1_identity.json`); RIV-d-4 sets the publisher's
  `identity_coverage` floor from it.

## 1b. ISSUER AMENDMENT 1 (2026-10-01 ~07:4xZ, 2.0.0_SA_COO~RV) -- disarm row W1-S17 first

Row W1-S17 is ARMED. Today `home_producer.py` (RIV-hp-1, merged) finds the landing address by parsing
`integrations/bloomberg/pipeline/etf_constituents_pull.py` at RUNTIME. The stage Lambdas' bundle carries the `rivalfunds`
package and not `integrations/`, so on deploy `build-canonical-shape` and `build-coverage` would FAIL for every fund.
`home_producer.py` is granted to you. Fix it this way:
- module constants `BUCKET = "opal-data-etfs"`, `PREFIX = "bbg"`, `SUBFOLDER = "constituents"`, with a comment citing
  `etf_constituents_pull.py:53-55`;
- no runtime read of any file outside the package;
- a unit test in `tests/test_i1_*.py` that, when the producer file is present in the repo, asserts the three constants equal
  its module-level values, so drift is caught in the repo and never in production;
- record the disarm as the row's resolution.

Do this before the identity work. Your worktree has CLOUD merged in (hp-1's code is there).

## 1c. ISSUER AMENDMENT 2 (2026-10-01 ~09:1xZ, 2.0.0_SA_COO~RV) -- REOPENED: identity must never move a trade (row Z-S8, BLOCKING)

The issuer's served-delta dry run of the merged round-3 code (`deliverables/2.0.0_SA_COO~RV/round3/served_delta_r3.json`) found
that this cell's identity changes BASG's trade schedule:
- served 527 trade keys, new 1694 (322 removed, 1489 added);
- 922 exits and 638 entries against 224 adds and 261 trims;
- BASG G1 over 325 dates: 134 fully resolved, 7 zero, 184 partial.

`gold_trade_schedule` matches `q_{t-1}` to `q_t` on `security_id`. Where a window's two dates resolve a security differently,
the position reads as exited and re-entered, which C-TRADE-SCHEDULE forbids. TSEL +6, WCMG +1 and BIDD -2/+1 are the same
class.

- **The fix:** G5 matches positions within a fund's window on a WINDOW-STABLE key: the row's OWN raw identifier family.
  - For an issuer row: CUSIP, then ISIN, then SEDOL, then ticker, the first one the row carries.
  - For a Bloomberg row: its Bloomberg id.
  - For a home-landing row: its cusip.
  - `security_id` and the resolution fields ride along as LABELS.
  - A trade's `security_id` is the resolved key only when the window's two rows agree on it.
  - `data/etfs/scripts/rivalfunds/gold_trade_schedule.py` and its test files are granted.
  - Do NOT weaken identity in G1 to pass: i-1.AC1 must still PASS unchanged.
- **New criterion AC2** (`round3/checks/i-1.AC2.py`, bounded at about 30 s; it FAILs at CLOUD b780b4b8cb, with 31 removed and
  271 added in its window): BASG's trades in 2026-01-02..02-17, replayed by your branch over the served inputs, equal the
  served ones.
- **Report:** re-run `round3/served_delta_r3.py --out <your deliverables>/served_delta_after.json` once; it is long, about
  25 min, and is a report, not a criterion. Report its per-fund `g5_removed` / `g5_added`. Every non-home fund must read 0/0,
  or each difference must be named with its cause in a row.

## 2. THE RULING BEHIND IT (issuer ruling 2, inlined)

`lib/research/identity/` (the crosswalk object, `registrations.json`, `add_security`) is AMGT_RESAPP's and its rounds are live: you
WRITE NOTHING there. You CALL `crosswalk.resolve()` first, as G1 does today, and only on a miss apply the two MEASURED rules above.
Nothing is minted by appending a suffix (the crosswalk's own law, `crosswalk.py` docstring: "never made by appending US Equity or
stripping a suffix") -- a Bloomberg id is a form Bloomberg itself returned; the issuer join is a co-holding measured on the same fund
and day. Measured at the cut on 2026-09-28: BASG issuer `quantity` vs Bloomberg `POSITION` differ by ~0.1% (ABNB 70277 vs 70355,
GOOG 62241 vs 62309, AMZN 121244 vs 121376); root ticker + 2% joins 34 of 34 BASG non-cash rows, 0 ambiguous; exact equality joins 0.
Bloomberg ids of WCMG/TSEL/ETFT/PCLG on 2026-09-28 are 3-token `<ROOT> <CC> <YELLOW>` in 48/48, 28/28, 29/29, 29/29.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base 78167bb8fc)

- `gold_canonical_shape.py`: `_identity(row, cash, resolve, path, source_label)` (issuer rows; tries CUSIP, ISIN, SEDOL, ticker;
  ~line 190) and `_bbg_identity(sec, cash, resolve, path, source_label)` (Bloomberg rows). Identity columns: `security_id`,
  `raw_identifier`, `raw_identifier_kind`, `resolution_status` {RESOLVED, UNRESOLVED}, `resolution_method`, `resolution_source`,
  `resolution_note`, `security_bloomberg`. Issuer rows carry `fund_ticker` 'BASG' (their `fund_id` is the issuer's '4823'), plus
  `security_ticker`, `quantity`; Bloomberg silver rows carry `id`, `position`, `fund_ticker`. G1 already lists Bloomberg silver per
  report date (`_bbg_latest(s, rd)`), including for issuer_first funds.
- The crosswalk loads from the AMGT pool (237 records as_of 2026-09-29); a load failure FAILS the stage (keep that).

## 4. SURFACES AND BOUNDS

You READ (never edit): `lib/research/identity/` (all of it), `lib/trading_calendar.py`, the package's other modules,
`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3}/checks/`, the device-local captures under
`C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\` (the BASG issuer archive `amgt-reconn-daily-census-20260929\basg\` and the
PFOE-group BQL captures beside it).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`, where `i1_identity.json` goes). NEVER: anything
under `lib/`, any S3 write, any deploy, any Bloomberg or OpenAI call, any file another round-3 cell owns. Tests:
`tests/test_i1_*.py`.

<paths>
data/etfs/scripts/rivalfunds/identity.py
data/etfs/scripts/rivalfunds/home_producer.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_i1_*.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_g2_*.py
data/etfs/scripts/rivalfunds/tests/test_g52_*.py
data/etfs/scripts/rivalfunds/tests/test_g1_canonical_shape.py
data/etfs/scripts/rivalfunds/tests/test_g12_canonical_multi_source.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- on two real days, BASG's issuer rows resolve >= 95% by the measured join to BASG Bloomberg ids; a planted ambiguous
  candidate leaves ABNB UNRESOLVED with both candidates named; the four Bloomberg-sourced PFOE rivals resolve >= 95% in the key
  grammar (`.../round3/checks/i-1.AC1.py`)
- **Deliverable (not a criterion):** `i1_identity.json` records the measured fraction per fund over the same window (one object per
  fund: `resolved`, `non_cash`, `fraction`, `by_method`); RIV-d-4 reads it for the floor. AC1 prints the same fractions.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-i-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/i-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-i-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/i-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-i-1.identity-measured-resolution.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-i-1.identity-measured-resolution`, and `i1_identity.json` beside it. Report once: the verdict line with the output above it; the per-fund fractions; files written; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-2 analysis item 4 / ruling 6, narrowed by issuer ruling 2 (no AMGT pool write).
Check dry-run at base 78167bb8fc: i-1.AC1 FAIL (BASG 0/33 non-ABNB resolved; WCMG 8/48, TSEL 15/28, ETFT 14/29, PCLG 19/29) -- FAIL
as expected. Handed to slot ~1 after RIV-hp-1 merges (same file, gold_canonical_shape.py).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<completion_note>2026-10-01 ~09:5xZ drain by 2.0.0_SA_COO~RV after REOPEN (amendment 2): worker 0.9.0_WK_ETFS_RIVALS~1 @b74b0ec696 (fix 85f442ffe1); proof instance VALID; i-1.AC1 PASS, i-1.AC2 PASS (BASG window served 47 / branch 47, 0/0); full served-delta (served_delta_after.json): BASG 527/527 0/0, 7 funds 0/0; residual BIDD -2/+1 (newest of two captures for 2025-12-09 -- the supersede rule), TSEL +6 / WCMG +1 (fund's own prior report date paired -- the served daily stage pairs the global prior date; row W1-S27, to the round-3 analysis); suite 249 passed 0 failed; row Z-S8 disarmed (W1-S26).</completion_note>
<reopen_note>2026-10-01 ~09:1xZ REOPENED by 2.0.0_SA_COO~RV (amendment 2, row Z-S8 BLOCKING): identity moved BASG's trades; the prior completion stands for AC1 only.</reopen_note>
<completion_note>2026-10-01 drain by 2.0.0_SA_COO~RV: worker 0.9.0_WK_ETFS_RIVALS~1 @19b0e3889f (build 2dff1d32c1); proof instance VALID; i-1.AC1 PASS (BASG 33/33 by the measured join, ABNB ambiguity refused, PFOE rivals 100% in key grammar); i1_identity.json fractions 1.0 for BASG/WCMG/TSEL/ETFT/PCLG; W1-S17 disarmed (row S21). Drain suite 225 passed / 2 FAILED: the two RIV-hp-1 tests asserting the removed runtime read (row W1-S22) -- repaired under RIV-g-6 amendment 1.</completion_note>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
