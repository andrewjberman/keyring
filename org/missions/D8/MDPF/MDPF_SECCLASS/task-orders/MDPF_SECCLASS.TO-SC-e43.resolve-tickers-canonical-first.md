# TO MDPF_SECCLASS.TO-SC-e43 -- round 9 SC-e-43: FWD-5 -- resolve_tickers.py resolves a name from the canonical table first

<to_id>MDPF_SECCLASS.TO-SC-e43</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~33</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-43` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none. Slot ~33's only order. `TO-SC-e45` waits for this cell.

---

## WORKER FACE

### THE CELL

`SC-e-43`: `data/black_diamond/scripts/classification/resolve_tickers.py` (770 lines; PRD surface S25) resolves a Black Diamond
`asset_name` to a ticker from the canonical table's `name` FIRST, with the old list (`bd-securities`) as the fallback; the attributes
the canonical table does not carry (`asset_name_raw`, `name_aliases`) are named and counted as the gap.

- Why: round 8's trace graded it NEEDS-OLD-LIST: methods 2 and 3 (`_resolve_bd_securities_exact` ~:191, `_resolve_bd_securities_prefix`
  ~:217) match on `asset_name_raw` from a full `bd-securities` scan (`_scan_bd_securities` ~:152); `etf-classifications` carries neither
  `asset_name_raw` nor `name_aliases`. FWD-5 and the round-8 analysis section 2.10: no writer stop until every real reader is canonical-first.
- **The switch:** before method 2, a new method matches the BD name (normalized with `normalize_asset_name` ~:114) against the canonical
  table's `name` field (normalized the same way), from a read-only scan of `etf-classifications` that keeps only rows carrying `name`;
  a hit resolves with its own method label and confidence 1.0; a miss continues to methods 2 to 6 unchanged. Record the method label in
  the output exactly as the existing methods are recorded. Change nothing else.
- **Vendor:** the file imports `yfinance` at module load and `sync_to_ticker_lookup` may call it. You make NO vendor call: tests stub it,
  and your dry run never reaches that code path (row S11 carries the vendor check for a real run).
- **Tests** in `data/black_diamond/scripts/classification/tests/test_resolve_tickers_canonical_first.py`, with S3, DynamoDB and yfinance
  stubbed: a name matching a canonical `name` resolves by the new method before the old list; a name matching only `asset_name_raw` still
  resolves by method 2; a name in neither falls through unchanged.
- **The gap record:** a read-only script `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/resolve_tickers_switch_check.py`
  (no upload; the held names come from the latest local holdings build, `inferred`, row W25-S1) and
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESOLVE_TICKERS_GAP_20261007.md` with:
  one `## ATTRIBUTE: asset_name_raw` and one `## ATTRIBUTE: name_aliases` section, each with an integer `OLD-LIST-ROWS:` line (rows of
  `bd-securities` carrying it, read-only scan), one `CANONICAL:` line (whether `etf-classifications` carries it: today no) and one `USED-BY:`
  line (the method, path:line); and one integer `CANONICAL-FIRST-HITS:` line (held names the new method resolves from the canonical `name`).

### ACCEPTANCE

<criterion id="SC9-e43-AC1" cell_refs="SC-e-43"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/classification/tests/test_resolve_tickers_canonical_first.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e43-AC1` -- a canonical name match resolves before the old list; an old-list-only name still resolves by method 2; a name in neither falls through.

<criterion id="SC9-e43-AC2" cell_refs="SC-e-43"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/issuer_check_sc_e43.py</invocation><expect>SC-E43-GAP ok=True</expect></criterion>
`SC9-e43-AC2` -- the gap record counts both missing attributes in the old list, names where each is used, and states the switch's canonical-first hits.

<expected_criteria>SC9-e43-AC1,SC9-e43-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=4`, no test file); AC2 FAIL as expected (`no RESOLVE_TICKERS_GAP_*.md`).
Issuer controls on AC2: a synthetic well-formed record read `ok=True attributes=2`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
  `R10_CHECKS/r10_pytest_ok.py` and `R11_CHECKS/issuer_check_sc_e43.py` are READ-ONLY to you.
- **Never run `resolve_tickers.py` with `--upload`.** No S3 or table write, no deploy, no vendor (yfinance) or model call.
- **NO package install and NO download of any kind** (row S49).
- Lint that predates your edit on a file you own: fix annotation- or comment-only, no runtime change; say so in a row.
- Your commit stays on your branch; never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W33-S<k>`), and do not weaken the test.

<paths>
data/black_diamond/scripts/classification/resolve_tickers.py
data/black_diamond/scripts/classification/tests/test_resolve_tickers_canonical_first.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/resolve_tickers_switch_check.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESOLVE_TICKERS_GAP_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-43`.
<owned_cells>SC-e-43</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e43-AC1, SC9-e43-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~33/MDPF_SECCLASS.TO-SC-e43.resolve-tickers-canonical-first.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e43-AC1,SC9-e43-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the new method's label and its place in the order, the two attribute counts, the canonical-first hits, whether
`resolve_tickers.py` has a scheduled caller (and so whether the switch needs an upload half at all), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing; the worker reports whether the script has any scheduled caller.
comp-iam: DECLARED-NOT-APPLICABLE the switch adds an etf-classifications read to a script with no deployed role in the repo; a real run's role is read at the run's own half.
comp-adversary: RUN -- the canonical table lacks asset_name_raw and name_aliases, so the switch is canonical-first for names only and the gap is counted, not hidden; yfinance is imported at module load (tests stub it; S11 carries the vendor check). BLIND: an out-of-repo caller of the script.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 @90f99888cd (FWD-5, surface S25); CTO round-8 analysis @1ca9e97fc9 sections 2.10 and 4 item 1; DECOMP_R9 @5d70aab6c9.
