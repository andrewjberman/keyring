# TO MDPF_DEMQUE.TO-DQ-t28 -- round 8 DQ-t-28: the 32 served price files still on three columns are listed, reset in the pacer and re-drawn
<to_id>MDPF_DEMQUE.TO-DQ-t28</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~22</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-28` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 8 -- CUT) |
**outcome_ref:** C-PRICES | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-28` (PRD ADDENDUM v0.5, C-PRICES: total return on every price table; CTO round-7 analysis
`org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round7.md` section 2 "D1-S8 placed", read it; row `MDPF_DEMQUE-D1-S8`). The served price
store (`price_store.s3_root()`, one `cusip=<CUSIP>/prices.parquet` + `lock.json` per name) holds 141 files; 109 carry the seven columns and 32 still
carry the original three (`date, close_served, as_traded_close`; all last-modified 2026-10-09). The store writes a file only when the Yahoo pacer
re-draws its symbol (`daily_draw.py`), and a three-column file holds no dividend or split data, so total return cannot be derived from it: the 32
symbols are RE-DRAWN, not re-written from stored rows. This order builds the tool; running it with `--apply` and the draw that follows are the
issuer's acts at the drain.

**Build** (NEW `data/mdpf/scripts/demque/redraw_stale.py`; read `price_store.py`, `yahoo_pull.py` `Pacer`, `demand_queue.py` `validate` and `daily_draw.py`
first; import them, do not copy them):
1. `stale(root=None) -> (total, rows)`: for every CUSIP the store lists (`price_store._Store(root).cusip_dirs()`, root defaulting to
   `price_store.s3_root()`) that has a `prices.parquet`, a file is STALE iff its column list equals `price_store.PRICE_COLS` exactly. `total` counts
   CUSIPs with a `prices.parquet`. Each stale row is `{"cusip", "symbol", "start", "end"}`: `symbol` is `lock.json`'s `yahoo_symbol`, `start` and
   `end` the ISO min and max of the file's `date` column. Read only.
2. `reset_pacer(state_path, symbols) -> int`: removes ONLY the named symbols' entries from the pacer state file's `symbols` map (read the JSON,
   write it back atomically as `Pacer._save` does) and leaves every other key (`day`, `count`, `factor`, `pushback`, the other symbols) as it was;
   returns how many entries it removed. A missing state file is a state with no symbols (returns 0, writes nothing).
3. `enqueue(queue_dir, rows) -> str | None`: with rows, writes ONE request file `DEMQUE-S8-REDRAW-<YYYYMMDD>.json` that passes
   `demand_queue.validate`: `tier` 2 (current clients; ADVI_COTBKF reads these files), `reason` "C-PRICES total return on every price table (row
   D1-S8)", `page` "price store (C-PRICES)", `securities` `[{cusip, symbol}]` in the listed order, `fields` `["close"]`, `start` the earliest and `end`
   the latest of the rows' windows. It is idempotent: when that file already exists it returns its path unchanged; with no rows it writes nothing
   and returns None.
4. CLI: `--list` prints ONE JSON line `{"total": N, "stale": [rows]}` and writes nothing. `--apply [--root R] [--state PATH] [--queue DIR]` runs
   stale -> reset_pacer -> enqueue and prints `{"stale": n, "reset": m, "request": path or null}`; `--state` and `--queue` default to the daily
   draw's home exactly as `run_daily_draw.sh` derives it (`$OPAL_DEMQUE_HOME` or `~/.opal/demque`, files `pacer.json` and `queue/`), never typed.
   You do NOT run `--apply` against the real home: it is the issuer's act.
5. NEW `test_demque_redraw_stale.py` (pytest; a LOCAL store root under `tmp_path` built with `price_store.write`-shaped files or hand-written
   parquet, a pacer JSON in `tmp_path`, no network, no S3) with exactly these names:
   `test_lists_only_files_with_the_original_three_columns`,
   `test_resets_exactly_those_symbols_in_the_pacer_and_enqueues_one_request` (the other symbols and `day`/`count` unchanged; the request validates;
   a second `enqueue` returns the same path) and `test_second_run_with_no_stale_files_enqueues_nothing`.

### ACCEPTANCE

<criterion id="DQ8-t28-AC1" cell_refs="DQ-t-28"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t28_tests.py</invocation><expect>RDS-OK</expect></criterion>
<criterion id="DQ8-t28-AC2" cell_refs="DQ-t-28"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t28_stale.py</invocation><expect>STALE-OK</expect></criterion>
`DQ8-t28-AC1` -- the three named tests. `DQ8-t28-AC2` -- `redraw_stale.py --list` on the REAL served store (S3 read only): its stale set and its
total equal the check's own read of the parquet footers (32 of 141 at 2026-10-11 ~04Z).

<expected_criteria>DQ8-t28-AC1,DQ8-t28-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `RDS-BAD no file ...`, `STALE-BAD no file ...redraw_stale.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served price store (local or S3), no write to the real pacer state or queue, no AWS write, no Bloomberg call, no deploy.**
  The S3 read in AC2 is the seat's existing read. The re-draw reaches the store at the next scheduled draw; that run is the issuer's.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W22-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/redraw_stale.py
data/mdpf/scripts/demque/test_demque_redraw_stale.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 8), cell `DQ-t-28`.
<owned_cells>DQ-t-28</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ8-t28-AC1, DQ8-t28-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~22/MDPF_DEMQUE.TO-DQ-t28.redraw-stale-price-files.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ8-t28-AC1,DQ8-t28-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--list` line (count and first three rows), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the existing daily draw (22:30 local) writes the seven columns from its next run after the issuer's `--apply`.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by the worker; the S3 reads use the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE a list/reset/enqueue tool; the served write is the existing price_store.write (t21's contract: the existing three columns byte-identical).
risk: LOCAL -- code and tests. The issuer's `--apply` and the draw that follows are SERVED under a never-widen pair (CTO half: round-7 analysis item 3; COO half: decomposition round 8), blast radius the 32 listed CUSIP prefixes' `prices.parquet`, rollback per key the object's prior S3 version.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-7 analysis @f5553ca3d5 section 2 D1-S8 and section 3 item 3; row D1-S8 (REMEDIATION_v6); TO-DQ-t21 (the column); decomposition round 8.
