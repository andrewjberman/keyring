# TO MDPF_DEMQUE.TO-DQ-t49 -- round 9 DQ-t-49: the surface B porting test -- its Bloomberg request (at most 10 cells a security) and its comparator
<to_id>MDPF_DEMQUE.TO-DQ-t49</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~41</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>PORTING</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-49` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 14) |
**outcome_ref:** C-QUOTE, C-PRICES, C-ROUTE, FWD-6 | **depends_on:** DQ-t-44 (merged @900406e221), DQ-t-48 (merged @9de742d8f9)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-13 (Surface B, confirmed ~16:5xZ; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, section "Surface B", read it): **Bloomberg is the
default source for client history; a security uses Yahoo only after it passes a PORTING TEST**, and Yahoo-sourced client prices already stored read UNVERIFIED until they pass.
The test, as confirmed:
- Compare RETURNS, never levels. Yahoo interval return: `adjclose(end) / adjclose(start) - 1`, where the adjusted close is REFORMULATED from the store (stored as-traded close,
  split factors and stored dividends, gross dividends reinvested on the ex-date close: the same convention as Bloomberg's gross-dividends index). Bloomberg interval return:
  `TOT_RETURN_INDEX_GROSS_DVDS(end) / TOT_RETURN_INDEX_GROSS_DVDS(start) - 1`.
- **Pass:** the two returns differ by at most 10 bps on EVERY test interval; one miss fails the security.
- **Intervals:** 5 per security, a deterministic sha256 draw over the security's own held window, lengths 1 month, 1 quarter and 1 year plus 2 drawn lengths; no interval may start
  before the security's first held date.
- **Cost:** at most 10 Bloomberg cells a security (2 endpoints by 5 intervals). A pass ports the security; a fail keeps it on Bloomberg.

**This cell BUILDS the request and the comparator. It makes NO vendor call and draws nothing.**

**Build** (NEW `data/mdpf/scripts/demque/porting_test.py`; read `price_store.py` (`index`, the file layout, `prices.parquet`, `splits.parquet`, `dividends.parquet`, `lock.json`),
`bbg_quote.py` `_validate` and per-security windows, `lib/trading_calendar.py` first; import, do not copy):
1. **`--build --out PATH`** (S3 read only): over every security `price_store.index` lists (the Yahoo-sourced client prices landed today, 326 at the last count), take its held window
   `[valid_from, valid_to]` from the index row. Draw 5 intervals per security by `hashlib.sha256(("%s|%d" % (cusip, k)).encode()).digest()` (k 0 to 4): k 0, 1, 2 have lengths 1 month,
   1 quarter, 1 year (calendar, then each endpoint moved to a trading day on or before it); k 3, 4 take a length of 5 to 250 trading days drawn from the digest. Each interval's
   start is drawn from the digest inside `[window start, window end - length]`; an interval that does not fit is dropped and counted (`short_window_securities` counts securities with
   fewer than 5 intervals). The request: `{"request_id": "MDPF_SECHIST-CARD-A-PORTING-TEST", "channel": "history", "vendor": "bloomberg", "tier": 2, "need_class": "client", "window_start":
   <earliest endpoint>, "page": "client performance (Cottonwood), porting test", "fields": ["TOT_RETURN_INDEX_GROSS_DVDS"], "securities": [{"cusip", "start": D, "end": D}, ...]}` with
   one entry per endpoint (single trading day, `start` == `end`), CUSIPs and dates ONLY, no account number. It validates under `bbg_quote._validate`.
   Prints ONE JSON line `{"securities", "intervals_total", "cells", "max_cells_per_security", "short_window_securities", "need_class", "window_start"}`. Two runs write byte-identical files.
2. **`compare(bbg_rows, store_frames, intervals) -> verdict`** (pure function, no I/O): reformulates the adjusted close per rule above from the stored frames, computes both interval
   returns, and returns `{"cusip", "intervals": [{"start","end","yahoo_return","bbg_return","diff_bps","ok"}], "verdict": "PASS" | "FAIL" | "NO_BLOOMBERG"}`; PASS needs every
   interval within 10 bps. A missing Bloomberg endpoint is `NO_BLOOMBERG`, never a pass.
3. NEW `test_demque_porting_test.py` (pytest; stub frames, no network, no S3) with exactly these names:
   `test_the_five_intervals_are_a_deterministic_sha256_draw_inside_the_held_window_with_one_month_quarter_and_year_lengths`,
   `test_a_security_passes_only_when_every_interval_return_is_within_ten_basis_points_and_one_miss_fails_it`,
   `test_the_request_carries_at_most_ten_single_day_cells_a_security_on_trading_days_inside_the_window`.

### ACCEPTANCE

<criterion id="DQ9-t49-AC1" cell_refs="DQ-t-49"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t49_tests.py</invocation><expect>PORT-OK</expect></criterion>
<criterion id="DQ9-t49-AC2" cell_refs="DQ-t-49"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t49_real.py</invocation><expect>PORT-REAL-OK</expect></criterion>
`DQ9-t49-AC1` -- the three named tests. `DQ9-t49-AC2` -- on the REAL store: 300+ securities, at most 10 cells each, the declared client class, a deterministic file that validates under
the queue's rule, every entry a single day, no account key. The real check allows 55 seconds a run: read only the index and each name's own held range. Report the whole folder
`pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t49-AC1,DQ9-t49-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `PORT-BAD no file ...`; `PORT-REAL-BAD no file ...porting_test.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Yahoo call, NO Bloomberg call, no write to S3, the ledger, the queue or any pacer state, no AWS write, no deploy, no timer.** No file edits outside the grant.
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W41-S<k>`, `fabric` `dell1`, `surfaced_at` =
  `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY. Merge `box/dell1` into your branch (a merge,
  never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/porting_test.py
data/mdpf/scripts/demque/test_demque_porting_test.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-49`.
<owned_cells>DQ-t-49</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t49-AC1, DQ9-t49-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~41/MDPF_DEMQUE.TO-DQ-t49.porting-test-request-and-comparator.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t49-AC1,DQ9-t49-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--build` line verbatim, how the adjusted close is reformulated (the exact dividend and split rule), securities with fewer than 5
intervals, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder and a pure comparator; nothing is drawn or served.
risk: LOCAL -- code, tests and a priced request. The UNVERIFIED labelling of stored Yahoo prices is a separate SERVED cell under its own pair.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 (form Surface B, confirmed); CTO msg 4946; decomposition round 9.
