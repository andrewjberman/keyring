# TO MDPF_SECCLASS.TO-SC-e117.april-table-candidacy -- round 30 SC-e-117: E_18 sends a real ticker that the April table resolves but the canonical table lacks to the scheduled classifier, tagged resolved_via = april_table (code and tests only; nothing is deployed)

<to_id>MDPF_SECCLASS.TO-SC-e117</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~107</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-117` (`decompositions/MDPF_SECCLASS_DECOMP_R30.md`) |
**outcome_ref:** S55 (row MDPF_SECCLASS-D1-S55) | **depends_on:** none | **source:** CTO round-29 analysis section 3 ruling and section 4 item 1 (msg 8326)

---

## WORKER FACE

### THE CELL

`SC-e-117`. E_18 (`data/black_diamond/scripts/gold/E_18.detect_new_securities.py`) reads the open holdings, and for each (ticker, asset_name) pair whose key is not in the canonical table `etf-classifications` it checks the April name table (`resolved_names`, from `gold/dimensions/ticker_resolution.parquet`). Today, if the normalized name is in that table, the pair is SKIPPED as "already resolved": a REAL ticker (not a `NAME::` pseudo-key) that the canonical table lacks is appended to `held_by_resolution` and printed `-- held out`, and is never classified. 14 real tickers are in that state in every scheduled fire since 2026-10-18 (BALCX, CIMAX, DODBX, FPE, FSNQX, HBLFX, JBAWX, KAMIX, PCEF, TRRJX, TRRNX, VTTVX, WTM, XPMIX). The CTO ruled (msg 8326): the April table's job is resolution, not gating. A real ticker it resolves that the canonical table lacks **enters candidacy through the classifier's normal path and its normal refusal rule**, and each written row carries `resolved_via = april_table`. A `NAME::` pair the table resolves stays skipped. A name the table cannot resolve stays as it is. A refusal is printed with its reason, never skipped silently.

**The change, in four parts (make exactly these, nothing else):**

1. **In the loop of `detect_new_securities()` (the block that starts `# Resolution-aware check: skip already-resolved names`):** keep `already_resolved += 1` for every pair whose normalized name is in `resolved_names`. For a `NAME::` pair keep the `continue`. For a REAL ticker pair (`not pk.startswith('NAME::')`) do NOT `continue` and do NOT append to `held_by_resolution`: record `(pk, str(asset_name))` in a new list `april_admitted`, append the same pair to `canonical_candidates`, and when `upload` is true add `pk` to `known` (as the existing candidate path does). `new_count`, `truly_unresolved_names` and `truly_unresolved_mv` are NOT touched for such a pair (it is not "truly unresolved"; the classifier decides). Leave `held_by_resolution = []` declared and its print block as it is; it will print `: 0`.
2. **After `plan, scheduled_unresolved, scheduled_seed_pending = plan_rows(...)`:** for every `row` in `plan` whose `row['ticker']` is in the set of `april_admitted` tickers, set `row['resolved_via'] = 'april_table'` (before any write). No other row gets the key.
3. **Print one outcome line per admitted pair,** after the existing `Scheduled-classification ...` lines and before the `Top 10` block, under the header `    Entered candidacy through the April table (resolved_via=april_table): <N>`, one line `      <TICKER>  <name>  -- <outcome>` per pair, sorted by ticker, at most 50 lines then `      (+<k> more)`. `<outcome>` is exactly: `written` (the put returned `written`), `refused (row already existed)` (the put returned `refused`), `unresolved (no input classified it)` (its name is in `scheduled_unresolved`), `seed_pending (the seed path owns it)` (its name is in `scheduled_seed_pending`), or `planned, not written (dry run)` (a row was planned and `upload` is false). A pair that matches none of these prints `no outcome recorded` (a defect you report, never a silent skip).
4. **In `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`:** add `"resolved_via"` as the LAST entry of the `_WRITE_FIELDS` tuple, with one comment line above it: `# resolved_via: claim field, 'april_table' only on a row E_18 admitted through the April name table (CTO ruling msg 8326); absent on every other row.` Change nothing else in that file (`plan_rows` and `write()` are untouched: `write()` already copies only the keys a row HAS with a non-None value, so a row without the key writes an unchanged item).

**Tests.** Create `data/black_diamond/scripts/gold/tests/test_e18_april_candidacy_r30.py` with EXACTLY these 7 cases (reuse the harness of `data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py`: a stub S3 serving a holdings parquet and a resolution parquet, a recorder DynamoDB, a fake scheduled module, `boto3` patched while E_18 loads; read that file, copy what you need, do not edit it except as step 5 says):
 (1) an April-resolved REAL ticker absent from the stub canonical set is passed to the fake `plan_rows` as a candidate (the candidate count line reads 1), and with `--upload` the row the fake `write` receives carries `resolved_via == 'april_table'`;
 (2) the same run prints `Held out by the resolution table (real ticker absent from the canonical table): 0` and NO line containing `-- held out`;
 (3) the outcome lines: a written pair prints `-- written`; a refused pair (fake `write` returns `refused`) prints `-- refused (row already existed)`; a pair the fake `plan_rows` returns in `unresolved` prints `-- unresolved (no input classified it)`;
 (4) a `NAME::`-keyed pair that the table resolves is NOT a candidate and is counted in `Already resolved`;
 (5) the difference control: a real ticker absent from the canonical set whose name is NOT in the resolution table is a candidate with NO `resolved_via` key on its planned row;
 (6) a dry run (no `--upload`) prints `planned, not written (dry run)` for the admitted pair, calls the fake `write` zero times;
 (7) the REAL shared module: put `infra/aws/lambda/v2_portal/_shared` on `sys.path`, `import etf_classification_scheduled as sched`; assert `'resolved_via' in sched._WRITE_FIELDS`; call `sched.write` with a recorder table (a class with `put_item(**kw)` that records `Item` and `ConditionExpression`) on two rows, one with `resolved_via='april_table'` and one without: the first item has `resolved_via == 'april_table'`, the second item has no `resolved_via` key, both calls use `attribute_not_exists(ticker)`.

5. **Trim `test_e18_held_out_display_r29.py`** to the cases that stay true: delete its cases (a), (b) and (e) (they assert held-out lines that the new behavior removes) and keep (c) and (d). Update its module docstring to say so in one sentence. After the trim it must hold exactly 2 test cases.

### ACCEPTANCE

<criterion id="SC30-e117-AC1" cell_refs="SC-e-117"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e18_april_candidacy_r30.py -q --color=no -p no:cacheprovider</invocation><expect>7 passed</expect></criterion>
`SC30-e117-AC1` -- the 7 new cases pass, including the difference control (5) and the real-module case (7).

<criterion id="SC30-e117-AC2" cell_refs="SC-e-117"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py -q --color=no -p no:cacheprovider</invocation><expect>6 passed</expect></criterion>
`SC30-e117-AC2` -- the control: the round-27 known-set test still passes unchanged (you do not edit it).

<criterion id="SC30-e117-AC3" cell_refs="SC-e-117"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py -q --color=no -p no:cacheprovider</invocation><expect>2 passed</expect></criterion>
`SC30-e117-AC3` -- the trimmed round-29 display test holds its 2 remaining cases and they pass.

<expected_criteria>SC30-e117-AC1,SC30-e117-AC2,SC30-e117-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-19 ~15:0xZ): AC1 FAILS as expected (no such test file), AC2 PASSES as expected (`6 passed`), AC3 FAILS as expected (`5 passed`). Repo-wide hygiene (py_compile, ruff) is the issuer's at the drain; do not add criteria.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind.** pandas, pyarrow, pytest and boto3 are already installed.
- **No AWS call of any kind.** Nothing is deployed; the ship of E_18 and the shared module is a LATER order to a CloudOps seat under a signed never-widen pair. The contract entry for `resolved_via` (`org/standards/MDPF_SECCLASS_CONTRACT.json`) is NOT yours; do not edit it.
- **Keep the file ASCII.** No non-ASCII character in the code, comments or test strings you write.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks).
- **Never edit** anything outside the `<paths>` block. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W107-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a test or a check.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
data/black_diamond/scripts/gold/tests/test_e18_april_candidacy_r30.py
data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R30.md</decomp_doc> (round 30), cell `SC-e-117`.
<owned_cells>SC-e-117</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC30-e117-AC1, SC30-e117-AC2, SC30-e117-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~107/MDPF_SECCLASS.TO-SC-e117.april-table-candidacy.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC30-e117-AC1` (and AC2, AC3).
</proof_of_spec>

**REPORT:** what you changed (files, line counts), each criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships in this cell.
comp-iam: DECLARED-NOT-APPLICABLE no grant changes; the ship is a later CloudOps order under a pair.
comp-adversary: RUN -- a test that passes against the old E_18 (cases (1), (2), (3), (6) fail there: the old code skips the pair and prints it held out); a candidate that reaches the write without the claim field (case (1)); a claim field leaking onto a row that did not come through the April table (case (5), the difference control); a NAME:: pair admitted by mistake (case (4)); a shared-module change that alters an unrelated row (case (7), the row without the key). BLIND: the real classifier's refusal and unresolved decisions on the 14 live names, which only the next fire (or the issuer's plan-form single at the ship) exercises.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-29 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_29_20261019.md`, msg 8326); DECOMP_R30; row MDPF_SECCLASS-D1-S55.
