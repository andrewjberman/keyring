# TO MDPF_SECCLASS.TO-SC-e42 -- round 9 SC-e-42: FWD-5, FWD-2 -- A_07 (the Advisor Intelligence classification dim) reads the canonical table first

<to_id>MDPF_SECCLASS.TO-SC-e42</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~32</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-42` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-5, FWD-2 | **depends_on:** none. Slot ~32's only order. `TO-SC-e45` (the writer stops) waits for this cell.

---

## WORKER FACE

### THE CELL

`SC-e-42`: `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py` (617 lines) reads `etf-classifications` FIRST and falls
to the old list (`bd-securities`) only on a miss; the switch's before and after per held key is listed, with every changed class named.

- Why: round 8's trace (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_20261007.md`) graded a07
  NEEDS-OLD-LIST: it never reads `etf-classifications`. a07 is the Advisor Intelligence mix feed (49 Financial and Cottonwood mix
  artifacts); a security first held after the old-list writers stop gets equity if its ticker is 1-5 letters, a class by name
  pattern, or UNCLASSIFIED-LOUD. FWD-5 (PRD v0.13) and the round-8 analysis section 2.10: no writer stop until every real reader is
  canonical-first.
- **Read a07 first, in full.** Its header: classification is an ASSET-TRUTH; `_load_ddb()` (~line 198) materializes `bd-securities`
  at BUILD time into a ticker map and a name map (from `name_aliases` and `asset_name_raw`); `classify()` and `normalize_name()` are
  ported VERBATIM from `data/black_diamond/scripts/gold/lib/etf_classifier.py`, and `--parity-control` diffs the port against that
  original lib on the full population. **A canonical-first switch is a DELIBERATE reclassification**: the parity control will report
  the switch's deltas. Do not weaken or remove it: the set of keys parity reports as changed must equal the set your before/after file
  names as changed, and you say so in your report.
- **The switch:** load `etf-classifications` (consistent reads or a scan, at build time, in the same one sanctioned scan site) and, per
  held key, take its `asset_class` (and `sub_asset_class` where a07 uses it) from the canonical row when one exists; only a key with no
  canonical row falls to the old-list maps; a key in neither stays on a07's existing fallback. The canonical table's keys are bare tickers,
  `CUSIP:<9>` and `BBG:<ticker>:<exch>`; resolve a held security through those forms in that order. Six classes only (cash, fixed_income,
  equity, structured, alternatives, commodities); no `multi_asset`.
- **Tests** in `data/assets/scripts/gold/runners_49f/tests/test_a07_canonical_first.py`, with DynamoDB stubbed: a key in both tables takes
  the canonical class; a key only in the old list keeps the old class; a key in neither takes a07's fallback; the six-class bound.
- **The before/after:** a script `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/a07_switch_before_after.py` runs
  a07's classify over the held population read-only (a local build; nothing uploaded; the held set is `inferred`, row W25-S1) with and
  without the switch, and writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/A07_SWITCH_BEFORE_AFTER_20261007.json`:
  `{"as_of", "held_source": "... inferred", "denominator": <rows>, "rows": [{"key", "before_class", "after_class", "source": "canonical"|"old_list"|"unclassified"}]}`.
- **The half request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_A07_CANONICAL_FIRST_20261007.md`
  with `## The act` (upload the changed a07 through `.tools/safe-deploy.sh` -- a shared repo home, the S3-membership guard), `## Blast radius`
  (the changed keys and their dollars on each firm's mix, a local candidate diff), and `Rollback per key` (the S3 VersionId of the live
  a07 copy, read with `list-object-versions`). Both halves UNSIGNED; the issuer signs.

### ACCEPTANCE

<criterion id="SC9-e42-AC1" cell_refs="SC-e-42"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/assets/scripts/gold/runners_49f/tests/test_a07_canonical_first.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e42-AC1` -- a07 takes the canonical class first, keeps the old class only on a canonical miss, keeps its fallback for neither, six classes only.

<criterion id="SC9-e42-AC2" cell_refs="SC-e-42"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/issuer_check_sc_e42.py</invocation><expect>SC-E42-SWITCH ok=True</expect></criterion>
`SC9-e42-AC2` -- the before/after file numbers its denominator, and every key it marks canonical carries the class the live table holds.

<criterion id="SC9-e42-AC3" cell_refs="SC-e-42"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_A07_CANONICAL_FIRST_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC9-e42-AC3` -- the half request carries the act, the blast radius with a local candidate diff, and the rollback per key.

<expected_criteria>SC9-e42-AC1,SC9-e42-AC2,SC9-e42-AC3</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=4`, no test file); AC2 FAIL as expected (`no A07_SWITCH_BEFORE_AFTER_*.json`);
AC3 FAIL as expected (`NOT-READY: ... absent`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
  The issuer checks under `R10_CHECKS/`, `R11_CHECKS/issuer_check_sc_e42.py` and `IRPT_MVP_M/R20_CHECKS/` are READ-ONLY to you.
- **SHIPPED FILE.** `data/assets/scripts/gold/` is a shipped shared home: the pre-push deploy gate uploads a changed script in it at the
  push. Your commit stays on YOUR branch; the issuer holds it off every pushed range until both halves sign. Never push.
- **No deploy, upload, table or S3 write, no model or vendor call.** The before/after is a local build with nothing published.
- **NO package install and NO download of any kind** (row S49).
- Lint that predates your edit on a file you own: fix annotation- or comment-only, no runtime change; say so in a row.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W32-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py
data/assets/scripts/gold/runners_49f/tests/test_a07_canonical_first.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/a07_switch_before_after.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/A07_SWITCH_BEFORE_AFTER_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_A07_CANONICAL_FIRST_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-42`.
<owned_cells>SC-e-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e42-AC1, SC9-e42-AC2, SC9-e42-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~32/MDPF_SECCLASS.TO-SC-e42.a07-canonical-first.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e42-AC1,SC9-e42-AC2,SC9-e42-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** counts per source in the before/after, the changed keys with their dollars per firm, whether `--parity-control`'s changed set
equals the before/after's, the S3 key and VersionId of the live a07, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing; a07's scheduled runs are read, not changed.
comp-iam: RUN -- a07 already scans bd-securities at build time; the switch adds an etf-classifications read; the worker names the role a07 runs under and whether it grants dynamodb:Scan/GetItem on etf-classifications (a missing grant is a row and part of the half).
comp-adversary: RUN -- a07's parity control is designed to refuse a reclassifying port; this switch reclassifies on purpose, so the face requires the parity's changed set to equal the before/after's rather than letting either be weakened. Shipped shared home: held off pushed ranges. BLIND: the served mix bytes (firm buckets deny dell1, W25-S1; the dollars are from a local build, inferred).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 @90f99888cd (FWD-5, FWD-2); CTO round-8 analysis @1ca9e97fc9 sections 2.10 and 4 item 1; DECOMP_R9 @5d70aab6c9; R8 trace TO-SC-e38.
