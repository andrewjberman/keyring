# TO-AR-g-80 -- the total-return level helper: one pure module that turns a source's daily total-return fractions (or a served cumulative level) into the one [date, level] series every price adapter hands the chain

<to_id>IRPT_ANLREQ.TO-AR-g-80</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~180</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-80` (`decompositions/IRPT_ANLREQ_DECOMP_R11_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES) | **depends_on:** `AR-g-69` (merged `d1de2f0cd6`, the read that fixed the one formula).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~180`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-180` (branch `wk-IRPT_ANLREQ-180`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~180 <0.9.0_WK_IRPT_ANLREQ~180@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W180-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-180/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `portfolio_series.py` and `price_source.py` (merged; the module style and how dates are validated) and their tests under `tests/`.
- The formula this cell implements is in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~176/r9/PRICE_ADAPTER_FACTS.json` (`q2.one_formula`).

### THE CELL (`AR-g-80`, inlined)

Andrew's rule: prices are TOTAL RETURN. Each price source gives a different thing (a stored daily total-return fraction, Bloomberg's daily total return in percent, Yahoo's Close with dividends and splits, YCharts' served cumulative level). The read fixed ONE formula so every
adapter yields a total-return level series on the same footing: `level_0 = 100` at the first retained date and `level_t = level_(t-1) * (1 + r_t)` where `r_t` is that source's daily total-return FRACTION. This cell builds that formula as one pure module that the four adapters
(later cells) import. It reads no store and calls no vendor.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tr_level.py`** with exactly this contract.

1. `chain_levels(daily_returns, base=100.0)`: `daily_returns` an iterable of `(date_str, r)` (or two-item lists), `r` a daily return FRACTION (0.01 is one percent). Returns `[[date_str, level], ...]` ascending by date, every `level` a `float`.
   - A row is kept only if `date_str` is a `str` matching `YYYY-MM-DD` AND a real calendar date, and `r` is an `int` or `float` (not a `bool`), finite, and `> -1.0`. Every other row is dropped (a date with no usable return never seeds the level).
   - If a date repeats, the LATER value given wins.
   - The FIRST retained date has `level == float(base)` and its own `r` is NOT applied (that return is the move into the first date from a day the series does not hold). Each later retained date has `level = previous level * (1 + r)`.
   - `None` or an empty iterable returns `[]`. The input is not changed.
2. `returns_from_levels(pairs)`: `pairs` an iterable of `(date_str, level)` (a served CUMULATIVE level series). Returns `[[date_str, r], ...]` ascending, with `r = level_t / level_(t-1) - 1` for every retained row after the first. A row is kept only if the date is valid (as above) and the level is an `int`/`float` (not a `bool`), finite, and `> 0`; the later value of a repeated date wins; the first retained row has no return and is not listed.
3. **The module is pure and stdlib-only:** it imports nothing but `math`, `datetime`, `re`, `collections`, `typing` (and `__future__`); it opens no file, makes no connection, reads no environment variable, and has no `print`.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_tr_level.py` with at least 6 tests, offline, with hand-computed values: the chain from the base (returns 0.10, -0.05, 0.0 give 100, 110, 104.5, 104.5); a custom base; unusable returns dropped and never seeding the base; sorted output with a repeated date keeping the later value; bad dates dropped; `returns_from_levels` including a zero level skipped; and the round trip from levels to returns and back.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR80-g-AC1" cell_refs="AR-g-80"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g80_checks.py g80</invocation><expect>^AR-G80-OK</expect></criterion>

<criterion id="AR80-g-AC2" cell_refs="AR-g-80"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g80_checks.py hygiene</invocation><expect>^AR-G80-HYGIENE-OK</expect></criterion>

<expected_criteria>AR80-g-AC1,AR80-g-AC2</expected_criteria>

- AC1 imports `tr_level`, asks it ten cases with hand-computed values (the contract above, item by item), then runs your test file (0 failed, at least 6 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, only the allowed imports, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/tr_level.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_tr_level.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~180/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-80.total-return-level-helper.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R11_G.md</decomp_doc> round 11, workstream ~G, cell `AR-g-80`.
<owned_cells>AR-g-80</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR80-g-AC1, AR80-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~180/IRPT_ANLREQ.TO-AR-g-80.total-return-level-helper.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-80`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR80-g-AC1,AR80-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the module's function names with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the module is NEW and imported by nothing; the four adapter cells of the next round are its first importers. Nothing deployed, so no edge is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the price-adapter facts record (q2: a daily return read as a cumulative level, or the reverse). Traps: returns added instead of compounded; the first row's own return applied to the base; a null return seeding the level; a return of -100 percent or worse accepted (level zero); a percent passed where a fraction is meant (the adapters divide Bloomberg's percent by 100 before the call). The checker feeds a green arm (a reference build passes all ten cases) and a mutant arm (additive instead of compounding fails three cases).
</preflight>

- Cut on the AR-g-69 record (`q2.one_formula`) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR80-g-AC1` and `AC2` FAIL as expected (no module).
- The four adapter cells (`AR-g-81` to `AR-g-84`) are cut after this merges: each imports `tr_level`.
