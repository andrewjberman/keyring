# TO MDPF_SECCLASS.TO-SC-e116.e18-held-out-display -- round 29 SC-e-116: E_18 prints the real-ticker pairs it skips as "already resolved" while their ticker is absent from the canonical table, marked held out (a log line only; nothing is deployed)

<to_id>MDPF_SECCLASS.TO-SC-e116</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~105</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-18</issued_date>
<status>complete</status>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-116` (`decompositions/MDPF_SECCLASS_DECOMP_R29.md`) |
**outcome_ref:** S52 (row MDPF_SECCLASS-D1-S52) | **depends_on:** none | **source:** CTO round-28 analysis section 3 item 3 (msg 7829): "the April resolution table shows the nine held-out names, marked held out, never silently omitted. Display only."

---

## WORKER FACE

### THE CELL

`SC-e-116`. `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` skips a holdings pair when its asset name is in the resolution table `gold/dimensions/ticker_resolution.parquet` (a name-to-ticker table written once, on 2026-04-07), counting it only as `already_resolved += 1` (the branch at about lines 217-220, the `if norm_name and norm_name in resolved_names:` block). The nine held-out tickers (BALCX, CIMAX, DODBX, FSNQX, HBLFX, JBAWX, KAMIX, PCEF, TRRNX) are hidden this way although none is in the canonical table `etf-classifications`, and no run shows their names. You make E_18 SHOW them. This is a log line only: no count, branch, write or return value changes.

**What you build, in `E_18.detect_new_securities.py` only:**
1. Next to `already_resolved = 0` add `held_by_resolution = []`.
2. In the `if norm_name and norm_name in resolved_names:` branch, before the existing `already_resolved += 1`, append `(pk, str(asset_name))` to `held_by_resolution` when `pk` does NOT start with `NAME::` (a real ticker). Keep `already_resolved += 1` and the `continue` exactly as they are.
3. After the existing `Already resolved (in resolution table):` summary line, print one line `    Held out by the resolution table (real ticker absent from the canonical table): <n>` where `<n>` is `len(held_by_resolution)` formatted like the neighbouring lines, then one line per pair, sorted, at most 50: `      <ticker>  <asset_name>  -- held out`; if there are more than 50, one last line `      (+<k> more)`.
Change nothing else in E_18.

**A new test** `data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py`. Read the sibling `data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py` FIRST: it shows how E_18 is loaded without side effects (S3 client stub serving a small holdings parquet, a dynamodb recorder, a fake scheduled module, `boto3.client` and `boto3.resource` patched while E_18 loads) and how stdout is captured; reuse that pattern (copy the helpers, do not import them from the other test). The test must show: (a) a real-ticker pair whose key is NOT in the stub canonical set and whose normalized name IS in the stub resolution table is printed under the held-out header with the count 1 and a line holding its ticker and `held out`; (b) the existing counts are unchanged for that run (`Already resolved ... 1`, `Scheduled-classification candidates ... 0`); (c) the difference control: the same pair with its name REMOVED from the stub resolution table is not held out (the held-out count is 0) and is a candidate instead; (d) a `NAME::`-keyed pair that is hidden the same way is NOT listed; (e) with 51 hidden real-ticker pairs the output lists 50 lines and ends with `(+1 more)`.

Do not touch any other file (not the shared module, not `gold_dispatch.sh`, not the r27 test).

### ACCEPTANCE

<criterion id="SC29-e116-AC1" cell_refs="SC-e-116"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py -q --tb=short</invocation><expect>passed</expect></criterion>
`SC29-e116-AC1` -- the new test passes, including the difference control (c) and the cap (e).

<criterion id="SC29-e116-AC2" cell_refs="SC-e-116"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py -q --tb=short</invocation><expect>6 passed</expect></criterion>
`SC29-e116-AC2` -- the round-27 test still passes unchanged (a control: the display changes no behaviour).

<expected_criteria>SC29-e116-AC1, SC29-e116-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-18 ~02:0xZ): AC1 FAILS as expected (`no tests ran`: the file is absent); AC2 PASSES as expected (`6 passed`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind.** pandas, pyarrow and boto3 are already installed.
- **No AWS call of any kind.** Nothing is deployed; the ship of E_18 is a LATER order to a CloudOps seat under a signed never-widen pair.
- **Append to the surprise channel in BYTE MODE** (`open(path, 'ab')`), one new row only if you file one: never read and rewrite that file (it mixes CRLF and LF blocks).
- **Never edit** anything outside the `<paths>` block. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W105-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
data/black_diamond/scripts/gold/tests/test_e18_held_out_display_r29.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R29.md</decomp_doc> (round 29), cell `SC-e-116`.
<owned_cells>SC-e-116</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC29-e116-AC1, SC29-e116-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~105/MDPF_SECCLASS.TO-SC-e116.e18-held-out-display.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC29-e116-AC1,SC29-e116-AC2`.
</proof_of_spec>

**REPORT:** the exact diff of E_18, the new test's cases, each criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a test that passes against the old E_18 (the difference control (c) and the held-out header assertion fail there); a display that changes a count or a branch (AC2 and assertion (b)); a list that grows without bound (the cap (e)); a `NAME::` pair shown as a ticker ((d)).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-28 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_28_20261018.md`, msg 7829); DECOMP_R29; row MDPF_SECCLASS-D1-S52.
