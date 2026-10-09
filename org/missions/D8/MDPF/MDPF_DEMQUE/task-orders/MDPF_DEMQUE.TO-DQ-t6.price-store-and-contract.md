# TO MDPF_DEMQUE.TO-DQ-t6 -- round 2 DQ-t-6: the queue's price store, per CUSIP, and the file contract ADVI_COTBKF reads
<to_id>MDPF_DEMQUE.TO-DQ-t6</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~5</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-6` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-1, FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-6`, hops 5-6 of the FWD-1 thread (PRD v0.3): a Cottonwood client's holdings are valued, on the client's pages, from prices this
queue pulled -- the valuing is done by dell2's ADVI_COTBKF, which READS a store this cell builds. The store is keyed by Commonwealth's
9-character CUSIP (Cottonwood's Black Diamond transactions do not carry most of these securities: 945 of 4,545 needed CUSIPs, measured).

**Inputs it receives (already built, read them, do not edit them):** `data/mdpf/scripts/demque/lock.py` -- `check()` returns a lock row
dict with keys `cusip, yahoo_symbol, valid_from, valid_to, method, observations_checked, observations_passed, median_abs_error, state,
claim, locked_at, run_id, supersedes` (`state` `LOCKED` or `REJECTED:PRICE_MISMATCH`; `claim` `measured` or `held`).
`data/mdpf/scripts/demque/yahoo_pull.py` -- `PullResult` with `symbol, status, http_status, prices` (DataFrame `date, close_served,
as_traded_close`; `date` tz-naive datetime64 midnights), `splits` (`date, ratio`), `dividends` (`date, amount`), `cells`.

**Build** NEW `data/mdpf/scripts/demque/price_store.py` with:

1. `write(root, lock_row, result) -> dict`: when `lock_row["state"] == "LOCKED"` and `result.status == "OK"`, writes under
   `<root>/cusip=<CUSIP>/` the files `prices.parquet` (`date, close_served, as_traded_close`, ONLY dates inside `[valid_from, valid_to]`),
   `splits.parquet`, `dividends.parquet` (whole history: a later correction is re-derived, never re-pulled) and `lock.json` (the lock
   row). Otherwise writes NOTHING and returns `{"written": False, "reason": ...}`. If the four files already hold identical content,
   it writes nothing and returns `{"written": False, "reason": "unchanged"}` (pull once, C-ONCE).
2. `index(root) -> DataFrame` and `write_index(root)`: one row per CUSIP in the store: `cusip, yahoo_symbol, valid_from, valid_to,
   rows, claim, method, as_of (the max date), run_id`, written to `<root>/index/index.parquet` and `<root>/index/index.csv`.
3. `root` is a local directory OR the S3 root printed by the builder: `lib.opal_naming.address("yahoo", "global", "silver",
   "price_history", "")` (strip the trailing slash). Never type an S3 address by hand: the commit gate refuses it. S3 writes go through
   boto3 `put_object`; tests use a local temp directory only.
4. NEW `data/mdpf/scripts/demque/test_demque_store.py` (pytest, synthetic frames, temp dirs, no S3) with exactly these names:
   `test_only_the_locked_range_is_written`, `test_rejected_lock_writes_nothing`,
   `test_served_and_as_traded_kept_apart_with_actions`, `test_index_row_per_cusip_carries_claim_and_range`,
   `test_second_write_of_unchanged_history_is_a_noop`.
5. NEW `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md` -- the file contract dell2's
   ADVI_COTBKF reads (one page, plain English): the per-CUSIP address and the index address, each copied EXACTLY from the builder's
   output (run `address("yahoo","global","silver","price_history","cusip=00162Q866")` and `...,"index")` and paste what they print); a
   line beginning `KEY NAMESPACE:` stating the key is Commonwealth's 9-character CUSIP as delivered; every file and column with its
   meaning (`date`, `close_served`, `as_traded_close`, splits, dividends, the lock row and its `claim`: `measured` = proved against the
   client's trade prices, `held` = not proved, a consumer may refuse it); which close to value a holding with (as traded, because
   Commonwealth quantities are as traded); and a worked example for CUSIP `00162Q866` (AMLP) using the shapes above (no account data).

Do NOT edit `demand_queue.py` (another cell's) and do NOT create `__init__.py`; the issuer wires the draw to `write` at the merge.

### ACCEPTANCE

<criterion id="DQ2-t6-AC1" cell_refs="DQ-t-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/dq_t6_tests.py</invocation><expect>STORE-OK</expect></criterion>
<criterion id="DQ2-t6-AC2" cell_refs="DQ-t-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/dq_t6_contract.py</invocation><expect>CONTRACT-OK</expect></criterion>
`DQ2-t6-AC1` -- the store, by the five named tests. `DQ2-t6-AC2` -- the contract carries the builder's two addresses verbatim, the key
namespace, the columns and the AMLP example (the real neighbour, dell2, is graded at the issuer's AMLP trace).

<expected_criteria>DQ2-t6-AC1,DQ2-t6-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `STORE-BAD no file ...`, `CONTRACT-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no vendor call, no deploy.** The first real S3 write of the store is the issuer's, at the drain.
- **No client data in any committed file.**
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W5-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/price_store.py
data/mdpf/scripts/demque/test_demque_store.py
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `DQ-t-6`.
<owned_cells>DQ-t-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ2-t6-AC1, DQ2-t6-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/MDPF_DEMQUE.TO-DQ-t6.price-store-and-contract.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ2-t6-AC1,DQ2-t6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the drain's first S3 write reads the dell1 user's PutObject first.
comp-adversary: DECLARED-NOT-APPLICABLE enrichment of LOCAL code.
risk: LOCAL -- code, tests and a contract document.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.3 FWD-1 (consumer (a)), C-PRICES, C-ONCE, C-HOMES; CTO adjudication 2026-10-09T0108Z acts 1-2; decomposition round 2.
