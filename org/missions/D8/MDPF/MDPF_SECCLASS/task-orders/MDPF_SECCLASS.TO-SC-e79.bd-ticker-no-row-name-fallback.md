# TO MDPF_SECCLASS.TO-SC-e79 -- round 16 SC-e-79: BD's classify_with_identity falls back to the NAME:: row when the position's ticker has no row

<to_id>MDPF_SECCLASS.TO-SC-e79</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~69</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-79` (`decompositions/MDPF_SECCLASS_DECOMP_R16.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-79`, row MDPF_SECCLASS-D1-W66-S3. Round 15 (SC-e-76) made `data/black_diamond/scripts/gold/lib/etf_classifier.py`
`classify_with_identity` read the canonical `NAME::<normalized name>` row when the identity chain cannot place a BLANK-ticker position.
A position that CARRIES a ticker with no row in `etf-classifications` still stops at hop `ticker-no-row` and serves `unclassified`, even
when its `NAME::` row exists. Measured today: of the 36 trace securities in group A that carry a ticker, 23 have no ticker row and a live
`NAME::` row. Example: LBSAX, COLUMBIA DIVIDEND INCOME A, NAME:: row equity. The trace is
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.json`; rows whose `why` starts "A:" are
group A, and each carries `ticker`, `name`, `cusips` and `name_key`.

**Build:**
1. In `classify_with_identity`, when the position's ticker is non-blank AND has no row (the `ticker-no-row` hop), read
   `'NAME::' + ETFClassifier.normalize_name(asset_name)`, through the same lookup SC-e-76 added for the blank-ticker case. If that row
   exists, return its class and sub-class with class_source `etf-classifications`, and an identity hop that names the name key (the
   check requires the hop string to contain "name"). Reuse SC-e-76's code path; do not write a second lookup.
2. Keep every other answer exactly as today:
   - a ticker that HAS a row returns that row (the ticker is never overridden);
   - a chain that already places the position is unchanged;
   - a name with no `NAME::` row stays `unclassified` with hop `ticker-no-row`.
3. Extend `data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py`, with the table client stubbed, to cover:
   - a ticker-no-row position resolving through its `NAME::` row (hop names the name key);
   - a ticker-with-row position returning the ticker row (control);
   - a ticker-no-row position with no `NAME::` row staying unclassified (control).
   Keep the file's existing tests green.
4. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_TICKER_FALLBACK_20261009.md`,
   shaped like the other half requests in that folder (`## The act`, `## Blast radius`, `Rollback per key`). It must name:
   - the act: deploy ONLY `data/black_diamond/scripts/gold/lib/etf_classifier.py` to `s3://opal-data-bd/code/gold/lib/`, with
     `safe-deploy.sh <that path>` (the deploy core ships only named files);
   - the blast radius: the trace's ticker-no-row securities that move, with their dollars and class (a candidate diff from a local run of
     the new code over the trace);
   - the rollback per key: the current served lib VersionId (read it with `aws s3api head-object`, read-only).
   Leave both halves unsigned.

### ACCEPTANCE

<criterion id="SC16-e79-AC1" cell_refs="SC-e-79"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/sc_r16_ticker_no_row.py</invocation><expect>TICKER-NO-ROW ok=True</expect></criterion>
`SC16-e79-AC1` -- every ticker-no-row trace security with a live NAME:: row resolves to that row's class, with a hop naming the name key.
<criterion id="SC16-e79-AC2" cell_refs="SC-e-79"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_TICKER_FALLBACK_20261009.md</invocation><expect>HALF-READY</expect></criterion>
`SC16-e79-AC2` -- the half request carries the act, the blast radius with a candidate diff, and the rollback per key.
<criterion id="SC16-e79-AC3" cell_refs="SC-e-79"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC16-e79-AC3` -- the name-key test file passes, the new arms included.

<expected_criteria>SC16-e79-AC1,SC16-e79-AC2,SC16-e79-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:0xZ):
- SC16-e79-AC1: FAIL, as expected (ticker_no_row=23, resolved=0).
- SC16-e79-AC2: FAIL, as expected (NOT-READY, the half is absent).
- SC16-e79-AC3: PASS, as expected (control, 10 passed).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan): no write to any table or bucket, no deploy, no invoke, no model call. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W69-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_TICKER_FALLBACK_20261009.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R16.md</decomp_doc> (round 16), cell `SC-e-79`.
<owned_cells>SC-e-79</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC16-e79-AC1, SC16-e79-AC2, SC16-e79-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~69/MDPF_SECCLASS.TO-SC-e79.bd-ticker-no-row-name-fallback.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC16-e79-AC1,SC16-e79-AC2,SC16-e79-AC3`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the lib deploy is the issuer's act under the pair, by a CloudOps lane, outside a BD gold run.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only get-item under the seat's role).
comp-adversary: RUN -- a ticker with a row overridden (control arm); a chain-placed position moved (control); a NAME:: key form that differs from the trace's name_key; a hop string that hides the source (AC1 requires "name" in it)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO rounds 13-15 analysis section 3 item 1 (msg 2139); row D1-W66-S3; DECOMP_R16.
