# TO MDPF_DEMQUE.TO-DQ-t61 -- round 9 DQ-t-61: the 14 daily-tier names whose Yahoo identity lock fails are priced by Bloomberg under surface B (depth c, V2 active-Cottonwood windows): the B1 builder takes a named CUSIP list
<to_id>MDPF_DEMQUE.TO-DQ-t61</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~53</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>YAHOOFAILED14</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-61` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 24) |
**outcome_ref:** C-QUOTE, C-PRIORITY, C-IDENTITY, FWD-3, FWD-5 | **depends_on:** DQ-t-50, DQ-t-57, DQ-t-60 (merged)

---

## WORKER FACE

### THE CELL

CTO msg 5411 (ruling on the 2026-10-13 22:30 ET Yahoo run): **14 daily-tier names do NOT get a looser identity rule; they leave Yahoo and are priced by Bloomberg under surface B, depth c, clipped to the active-Cottonwood windows, priced and quoted first.** The 14 are in
[YAHOO_FAILED_14_NAMES.json](file:///C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/YAHOO_FAILED_14_NAMES.json) (repo-relative `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/YAHOO_FAILED_14_NAMES.json`):
CUSIP, symbol and the observation counts of their failed lock (9 mutual funds and 5 ETFs; all `REJECTED:LOW_TRADE_AGREEMENT`; stored at 2026-06-23, 78 trading days stale). None of them is in the filed B1 request, because B1 is built from `card_a_slice.card_a_cusips()`.
**This cell makes no vendor call and draws nothing; it only teaches the builder to take a named CUSIP list.**

**Build** (read `b1_request.py` in full (`main`, `build_request`, `quote_summary`, `excluded_names`), `card_a_slice.py` `build` / `write_request` / `card_a_cusips`, `active_set.py`; import, do not copy):
1. **`b1_request.py --build --names PATH --request-id ID --out PATH`**: two NEW optional flags. `--names` reads the JSON file's `names` list (each `{cusip, symbol, ...}`); the request is built over EXACTLY those CUSIPs through `card_a_slice.build("P1", <those cusips>, crosswalk, transactions, today=...)`
   (the same P1 window rule as B1: start the later of the first trade and 2012-01-01; end the frontier when held, else the last trade), then the same pipeline as the default build: the `$1.00` money-market rule, `option_c_entries` at depth c, the TR rule, the priority gate (`excluded_names`, fail closed), the V2 active-set clip, `held_back` and `emptied`. **The funds join step (`_fund_rows`, `FUND_SYMBOLS`, `FUND_FLOOR`) does NOT run in this mode:** these names are not part of the 15-fund request.
   `--request-id` overrides the request's `request_id` (default unchanged, the B1 id); with `--names` it is REQUIRED, and a `--names` build refuses to write over the default B1 request path or id.
2. **Output.** The same one-line JSON as the default build; `priced_names` is the count of CUSIPs built (14 for the real file); `securities` counts those left in the request. Deterministic: two builds write byte-identical files. The default build (no flags) is byte-identical to today's output.
3. **Tests** in a NEW `test_demque_b1_names_mode.py` (pytest; stub frames as `test_demque_b1_request.py` builds them, no network) with exactly these names:
   `test_a_named_cusip_list_builds_the_option_c_request_over_those_names_only`,
   `test_the_named_request_carries_its_own_request_id_and_the_default_b1_request_id_is_unchanged`.
4. **Report, do not file.** Run the real build once into `.scratch/` and report its line; the issuer files and quotes the request on the merged bytes.

### ACCEPTANCE

<criterion id="DQ9-t61-AC1" cell_refs="DQ-t-61"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t61_tests.py</invocation><expect>NAMES-OK</expect></criterion>
<criterion id="DQ9-t61-AC2" cell_refs="DQ-t-61"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t61_real.py</invocation><expect>NAMES-REAL-OK</expect></criterion>
`DQ9-t61-AC1` -- the two named tests. `DQ9-t61-AC2` -- on the REAL names file (S3 and the V2 active set read only): securities 1 to 14, `priced_names` 14, held_back + securities + emptied == 14, cells above 0 and below 20,000, a finish date, only the 14 CUSIPs, nothing before 2012-01-01, valid, deterministic, no account key, zero account-id oracle hits.
The check runs two builds (about 60 s each): invoke it under `timeout 260`. Report the whole folder `pytest data/mdpf/scripts/demque` once and the build line verbatim.

<expected_criteria>DQ9-t61-AC1,DQ9-t61-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `NAMES-BAD no file ...test_demque_b1_names_mode.py`; `b1_request.py: error: unrecognized arguments: --names ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue or any pacer state; do NOT write a request into `org/missions/.../requests/`**; no AWS write; no deploy; no timer. Never print an account number (the build reads the transactions to rank and window; its output holds CUSIPs, symbols and dates only). Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W53-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/b1_request.py
data/mdpf/scripts/demque/test_demque_b1_names_mode.py
data/mdpf/scripts/demque/test_demque_b1_request.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-61`.
<owned_cells>DQ-t-61</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t61-AC1, DQ9-t61-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~53/MDPF_DEMQUE.TO-DQ-t61.yahoo-failed-14-bloomberg-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t61-AC1,DQ9-t61-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the build line verbatim, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a request builder over S3 reads; no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a builder; nothing is drawn or served.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO ruling msg 5411; the 2026-10-13 22:30 ET run's receipt; decomposition round 9.
