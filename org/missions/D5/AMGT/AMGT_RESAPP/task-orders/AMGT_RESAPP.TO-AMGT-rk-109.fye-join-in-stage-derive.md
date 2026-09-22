# AMGT_RESAPP task order -- `AMGT-rk-109` -- L-0c: `model_block_pull.stage_derive` uses the existing `fye_join.fiscal_period_join` for a NON-December fiscal year end (31 March), and leaves every December name's derived block byte-identical; CODE ONLY, stub reads, no pull

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-109</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~109</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits one producer module and adds one test file; arms nothing; runs no pull.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every S3 read in the tests is a STUB (monkeypatched readers).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~109`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that `org/`, `.tools/` and the
existing paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~109;`. **NEVER RUN AN INSTALL. NEVER CALL BLOOMBERG OR S3.** Never read,
show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-109` (round 28, the Lenovo trial's wave 0)

**The governing text, verbatim** (PRD v0.22 s.12 @`d0597e7e0a`, Preconditions): *"**Fiscal-year pairing.** The model
block for a 31 March year-end is graded only with the fiscal-year join wired (field map s.3 item 2, `fye_join.py`)."*

**THE MEASURED STATE at SITEZ `96cc4dae9d` (re-read at your branch HEAD before editing):**
- `integrations/bloomberg/research/model_block_pull.py:965-977` `stage_derive` calls `merge_by_fiscal_year(hist_rows)`
  (`:508-526`). That function groups by the CALENDAR year (`date[:4]`) and merges every row of a year into one group,
  with a `_dates` list.
- For a 31 March filer, it pairs the March fundamentals with the SAME calendar year's December price and ratios, about 9
  months off. Measured on Lenovo's held histdata: fundamentals dated 03-31, prices dated 12-30.
- `integrations/bloomberg/research/fye_join.py:83-129` `fiscal_period_join(hist_rows, dense_price_rows=None)` anchors on
  fundamentals rows only (`FUNDAMENTAL_FIELDS`, `:43`). It pairs `PX_LAST` at or nearest ON/BEFORE the period end (never
  after, `:69-80`) and returns `price`, `price_date` and `gap_days` per group.
- Its only caller today is `derive_fye_fixed.py:115`, the round-1 BABA re-derive. `model_block_pull` does not use it.
- `stage_derive` then reads each closed group's `HIST_FIELDS` (`:1023-1046`) into figures.
- Tests: `integrations/bloomberg/research/tests` does NOT collect as a directory; 2 collection errors are pre-existing
  (`test_consumer_wiring.py` and `test_unresolved_overlay_renders_marked.py`, both importing
  `render_pack.load_model_block`, which no longer exists). So bars here are PER FILE.
- `test_fye_join.py` reads 3 failed / 2 passed, pre-existing: its 3 failing arms list a retired bucket (NoSuchBucket).
- `test_vintage_derivation_identity.py` **4 passed**; `test_latest_stamp_raw_pair.py` **1 failed / 5 passed**
  (pre-existing).

**RULED, what you build** (in `model_block_pull.py` only):
1. A pure helper `_is_december_fye(hist_rows)`: True when EVERY row carrying a `fye_join.FUNDAMENTAL_FIELDS` member is
   dated in month 12, or when no such row exists. Load `fye_join` by path, the same way the module loads its other
   siblings (`_load_sa_forecast_fallback`, `:282`).
2. In `stage_derive`:
   - If `_is_december_fye(hist_rows)`, call `merge_by_fiscal_year` EXACTLY as today. The December path's output is
     BYTE-IDENTICAL.
   - Otherwise, group with `fye_join.fiscal_period_join(hist_rows)`, with no dense series in this cell (the daily price is
     stage 11, a later cell). Then:
     - (a) each group's `PX_LAST` is the paired `price`, and the group records `price_date` and `gap_days`;
     - (b) a `HIST_FIELDS` member that exists ONLY on a non-anchor (price-only) row is NOT merged, because it would be
       mis-dated. It is recorded in `unresolved` with the reason `"not dated at the fiscal period end (non-December FYE,
       fye_join)"`;
     - (c) the block gains a top-level `"fiscal_year_join": {"method": "fiscal-period (fye_join)", "max_gap_days": <int|None>}`.
       The December path writes `{"method": "calendar-year (merge_by_fiscal_year)", "max_gap_days": None}`, and so is NOT
       byte-identical once the key exists. **So write this key ONLY on the non-December path.** The December block stays
       byte-identical.
3. New test `integrations/bloomberg/research/tests/test_stage_derive_fye.py`, stubbing `_read_json_from_s3`,
   `_latest_stamp`, `_ensure_unit_map`, `_end_requested_from_pull_log` and any other S3 touch, with arms:
   - `test_march_fye_pairs_price_on_or_before_period_end`: a 992-shaped fixture, fundamentals 03-31 for 3 years and
     PX_LAST rows on 12-30. Each FY's PX_LAST figure is the price dated ON OR BEFORE that 03-31, and its `gap_days` is
     recorded.
   - `test_march_fye_price_only_ratio_is_unresolved`: a ratio present only on the 12-30 row lands in `unresolved` with the
     named reason, never as a figure.
   - `test_december_name_byte_identical_to_pin`: a December fixture's derived block equals, byte for byte after dropping
     only the fields that carry the run's own clock (`vintage`, and any `derived_at` or stamp field; NAME each in the
     test), the block from the PINNED module loaded from `git show 96cc4dae9d:integrations/bloomberg/research/model_block_pull.py`
     into a temp file.
   - `test_is_december_fye`: all-December is True, any March is False, and no fundamentals is True.

**What this cell does NOT change:**
- `fye_join.py`, `derive_fye_fixed.py` and `merge_by_fiscal_year`;
- the pull stage;
- any S3 object, served block or currency label (that is rk-112, chained after this cell).

## 2. WHERE THIS CAME FROM

**ROUND 28**, decomposition s.36: the Lenovo trial's wave 0. rk-112 (currency) edits the SAME module and is CHAINED after
this cell.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_stage_derive_fye.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~109/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-109.fye-join-in-stage-derive.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch is `<your worktree>/.scratch/r109/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~109 <0.9.0_WK_AMGT_RESAPP~109@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY**; tests stub every S3 read. **Run test FILES in this directory one pytest call each** (the directory does not
  collect).
- **A script that carries a backslash is a FILE** (W84-S1).
- **The pin is `96cc4dae9d`.**
- **THE REFUSAL CLAUSE** applies. The pre-existing failures (`test_fye_join.py` 3, `test_latest_stamp_raw_pair.py` 1, and
  the 2 collection errors) are NOT this cell's to fix. Their counts must not GROW.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W109-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

`.scratch/r109/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "96cc4dae9d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-109"><invocation>cd "$(git rev-parse --show-toplevel)" && sed -n '965,978p' integrations/bloomberg/research/model_block_pull.py && for t in test_fye_join test_vintage_derivation_identity test_latest_stamp_raw_pair test_forecast_fallback; do echo "$t $(python -m pytest integrations/bloomberg/research/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit: stage_derive calling merge_by_fiscal_year; then four per-file baselines, recorded (measured at the cut: 3 failed 2 passed; 4 passed; 1 failed 5 passed; 13 passed)</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-109"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_stage_derive_fye.py -v --color=no -p no:cacheprovider 2>&1 | tail -7</invocation><expect>"4 passed" and 0 failed -- the March pairing, the price-only ratio going unresolved, the December name byte-identical to the pinned module, and the helper</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-109"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_fye_join test_vintage_derivation_identity test_latest_stamp_raw_pair test_forecast_fallback; do echo "$t $(python -m pytest integrations/bloomberg/research/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each of the four lines EQUALS its AC0 line: no new failure, and no pre-existing failure removed or added</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-109"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r109/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY integrations/bloomberg/research/model_block_pull.py and integrations/bloomberg/research/tests/test_stage_derive_fye.py; each "compiles True crlf 0" and non_ascii_chars equal to the value at the pin (measure the pin's model_block_pull.py in AC0's spirit and record it)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~109/AMGT_RESAPP.TO-AMGT-rk-109.fye-join-in-stage-derive.proof_of_spec.json`.
Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0), flip to `complete` only if every
criterion passes, commit with `--only`, and report once.

**MUTATION DISCIPLINE:** snapshot working-tree bytes to `.scratch/r109/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5):**
1. **December byte-identity** is the non-regression guard for 37 served blocks. That is why the new block key is written
   only on the non-December path.
2. Without the daily price series (stage 11, later), Lenovo's nearest on/before price may sit about 3 months before
   03-31, from the prior December. `gap_days` records it honestly. L-PX later supplies the dense series.
3. A price-only ratio is refused, not re-dated. Re-computing a ratio from the paired price is a design choice for the trial
   report, not this cell.
4. CHAINED: rk-112 edits this same module and is spawned only after this cell drains.
5. No new security_key dependency.

<status>pending</status>
<round>28</round>
<slot>~109</slot>
<fabric>site-z</fabric>
