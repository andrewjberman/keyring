# TO MDPF_DEMQUE.TO-DQ-t62 -- round 9 DQ-t-62: a share-class symbol without a dash (BRKB) is pulled from Yahoo in its dash form (BRK-B) and keyed as given
<to_id>MDPF_DEMQUE.TO-DQ-t62</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~54</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SYMBOLFORMS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-62` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 25) |
**outcome_ref:** C-YAHOO, C-PRICES, FWD-8 | **depends_on:** DQ-t-58 (merged @ea0dd99e4e)

---

## WORKER FACE

### THE CELL

CTO msg 5411: BRKB's lag is a symbol-form bug, "fix the symbol map and re-read, no rule change". Measured by the issuer on the 2026-10-13 22:30 ET run: the store's Berkshire B lock (CUSIP `084670702`) carries `yahoo_symbol` **`BRKB`** and sits at `valid_to` 2026-06-22 (79 trading days behind); the pacer records `BRKB` **FAILED_EMPTY** (7 attempts, row `UNRESOLVED:YAHOO_NO_DATA`) while `BRK-B` and `BRK-A` pull OK (the IRPT request carries `BRK-B`; the R4 slice and the store carry `BRKB`).
Of the 22 symbols that came back empty that night, `BRKB` is the only one whose dash form pulled OK; the rest are delisted, merged or money-market names and are NOT touched. **This cell changes only the symbol sent to Yahoo; the key everywhere else (the store's lock, the pacer, the ledger, the queue, the unresolved list) stays the symbol AS GIVEN.** No identity rule changes. **One live Yahoo request is allowed (the AC2 probe).**

**Build** (read `yahoo_pull.py` `_default_fetch` / `pull` / `_probe`, `daily_draw.py` `_yf_window`, `batch_pull.py` `_default_fetch_many`; import, do not copy):
1. **`yahoo_pull.yahoo_form(symbol) -> str`**: a module constant `SHARE_CLASS_FORMS = {"BRKB": "BRK-B", "BRKA": "BRK-A"}` and the function returning the mapped form, else the symbol unchanged. Nothing is derived by a rule (a symbol like `CTL` or `GOOGL` must never be altered).
2. **Every Yahoo fetch path sends `yahoo_form(symbol)`**: `yahoo_pull._default_fetch` (full history), `daily_draw._yf_window` (the stored-name window) and `batch_pull._default_fetch_many` (the batch). The result is attributed to the symbol AS GIVEN: `PullResult.symbol`, the pacer entry and the ledger row all read `BRKB`, never `BRK-B`. A test double passed as `fetch` receives the symbol as given (the mapping lives inside the default fetches, not in `pull`/`run`), so existing tests are unaffected.
3. **Tests**: NEW `test_demque_symbol_forms.py` (pytest; monkeypatched `yfinance.Ticker`, no network) with exactly these names:
   `test_a_class_share_symbol_without_a_dash_is_pulled_in_its_yahoo_dash_form_and_keyed_as_given` (all three default fetch paths send `BRK-B` for `BRKB`; the result and the pacer entry read `BRKB`),
   `test_a_symbol_with_no_override_is_pulled_unchanged_in_every_fetch_path` (`ACTSX`, `CTL`, `BRK-B` and `GOOGL` go to Yahoo exactly as given).

### ACCEPTANCE

<criterion id="DQ9-t62-AC1" cell_refs="DQ-t-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t62_tests.py</invocation><expect>FORM-OK</expect></criterion>
<criterion id="DQ9-t62-AC2" cell_refs="DQ-t-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t62_probe.py</invocation><expect>PROBE-OK</expect></criterion>
`DQ9-t62-AC1` -- the two named tests. `DQ9-t62-AC2` -- ONE live probe: `yahoo_pull.py --probe BRKB` reads `symbol=BRKB status=OK rows>=1000` (at the base it reads `status=FAILED_EMPTY rows=0`). Report the whole folder `pytest data/mdpf/scripts/demque` once and the probe line verbatim.

<expected_criteria>DQ9-t62-AC1,DQ9-t62-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `FORM-BAD no file ...test_demque_symbol_forms.py`; `PROBE-BAD symbol=BRKB status=FAILED_EMPTY rows=0`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **ONE Yahoo request (the AC2 probe, on its own scratch pacer); no other vendor call. NO write to S3, the real store, the queue, the ledger, the actuals or the shared pacer (`~/.opal/demque/pacer.json` is never touched); never run `daily_draw.py` against the real store or `--s3`.** Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W54-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1`; the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/yahoo_pull.py
data/mdpf/scripts/demque/daily_draw.py
data/mdpf/scripts/demque/batch_pull.py
data/mdpf/scripts/demque/test_demque_symbol_forms.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit; a test file outside it that fails is a surprise row asking for the grant.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-62`.
<owned_cells>DQ-t-62</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t62-AC1, DQ9-t62-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~54/MDPF_DEMQUE.TO-DQ-t62.share-class-symbol-forms.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t62-AC1,DQ9-t62-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the probe line verbatim, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS access.
comp-adversary: DECLARED-NOT-APPLICABLE the change is the string sent to Yahoo for two named symbols; the key everywhere else is unchanged.
risk: LOCAL -- code and tests. The first nightly run after the merge pulls BRKB through the wired incremental path (a gap pull, since its store sits 79 trading days behind), under the signed pair A; the issuer reads that receipt.
direct_act: false -- a worker order.
</preflight>

Source: CTO msg 5411; the 2026-10-13 22:30 ET run's pacer record; decomposition round 9.
