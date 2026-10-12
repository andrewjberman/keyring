# TO MDPF_SECCLASS.TO-SC-e91 -- round 21 SC-e-91: C_06 revisits a retained date's unclassified holdings on every fire

<to_id>MDPF_SECCLASS.TO-SC-e91</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~80</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-91` (`decompositions/MDPF_SECCLASS_DECOMP_R21.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-20 analysis section 2 (D1-S30) and section 3 item 1, msg 4321

---

## WORKER FACE

### THE CELL

`SC-e-91`, row MDPF_SECCLASS-D1-S30. Round 20's SC-e-87 taught Black Diamond's three served classify sites to place a ticker-no-row
position by its `NAME::` row, and it shipped. The served effect did not follow at D_04: `platinum/firm/mix_summary.json` reads Unclassified
$1,846,332.73 at as_of 2026-10-09 BEFORE the ship and AFTER it, equal to the cent. Four facts at HEAD explain it, in
`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` (read them first):

1. **:274-275** `SERVED_HOLDING_CLASSES` contains `unclassified`, so **:278-311** `reclassify_retained(existing_mix, existing_conc, rebuilt_dates)`
   only revisits a retained holding whose class is OUTSIDE the set. A retained `unclassified` holding is never sent back through
   `classify_series`, so a better classifier never reaches a date C_06 already wrote.
2. **:694-696** `build()` returns early ("No new partitions -- artifacts are current") when no partition is newer than the watermark, so the
   retained pass does not run at all on a fire that builds no new date. Monday's fire read Friday's data and built none.
3. **:975** `existing.get('firm', {}).update(firm_daily_new)` replaces only the NEW dates in `mix_daily_summary.json`; a retained date's
   firm and advisor dollars by class are never adjusted by anything the retained pass changes.
4. **D_04.client_portal_summary.py :486** reads that `mix_daily_summary.json` for its firm mix (D_04's `Unclassified` is the firm total minus
   the six classes).

**Build (C_06 only; the lib and D_04 are READ ONLY):**
1. `reclassify_retained(existing_mix, existing_conc, rebuilt_dates, moved=None)`: keep the three positional parameters and add the optional
   `moved`. It also revisits a retained holding whose class is `unclassified`, through the same `classify_series` call new dates use (by
   ticker and name). A holding that resolves to a class in the six moves: its fields are rewritten as today and its own `pct` moves from
   `unclassified` to the new class inside that date's mix entry. A holding that still resolves to `unclassified` is left byte-identical and
   does not count as changed. An entry already inside the six is never touched. When `moved` is a list, append one tuple per moved holding:
   `(date, old_class, new_class, dollars)` with `dollars = pct * that date's total_mv`. The return stays `(entries_changed, holdings_changed)`;
   `holdings_changed` counts only holdings that moved, so a second pass over the same data returns 0 holdings and changes nothing.
2. The firm and advisor daily snapshots: wherever the pass moves holdings, adjust that date's class dollars in the firm snapshot (and, by the
   relationship's advisor, in the advisor snapshot) by the moved dollars: `old_class -= $`, `new_class += $`, `total` unchanged. Do this on a
   fire WITH new partitions (the retained dates' entries in the merged summary) and on a fire WITHOUT.
3. A fire with no new partition must run the retained pass instead of returning first: read the existing relationship JSONs, revisit,
   rewrite ONLY the relationships where at least one holding moved (their period views with them), adjust the snapshots, and write
   `mix_daily_summary.json` only if a date changed. State in your report how many relationship JSONs that read touches per fire; a second fire
   over unchanged data must write nothing.
4. Add `data/black_diamond/scripts/gold/tests/test_c06_retained_unclassified_r21.py`, a pytest in the style of the sibling
   `test_c06_retained_dates_six_class.py` (stub client, no AWS call), covering: the moved holding and its mix pct, the stays-unclassified
   holding, the in-six control byte-identical, the `moved` tuple, idempotence, and one snapshot adjustment. The sibling test must still pass.
5. Write the never-widen half request at
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md`, in the shape
   of `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_SERVED_PATH_REACH_20261011.md` (read it). Headings: **The act** (one C_06 file to
   `s3://opal-data-bd/code/gold/` by a CloudOps lane under a ledger opened at start, outside a BD gold run), **Blast radius** (objects the act
   writes: one code object; objects the next fire writes: the relationship JSONs and views where a holding moves, `mix_daily_summary.json`,
   then D_03 and D_04's outputs), **Writers** (count the writers of the served `platinum/firm/mix_summary.json`, of `gold/views/mix_daily_summary.json`
   and of the relationship JSONs, N printed, each by file:line), **Both branches of the expected outcome** (read from the code you wrote:
   a holding WITH a `NAME::` row moves; one WITHOUT stays `unclassified` and is listed; use the 23-security list
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D1W66S3_TICKER_NO_ROW_LIST_20261009.json` read against the live table with
   `get_item` only), **Rollback** (the prior C_06 object, ETag `1aa6e3b555815417bb90c65db3f2152f` VersionId `AREnJgLoyQnZ1zKwPan793py8CCkNHHA`, and the
   prior versions of every key the next fire rewrites, recorded by the ship's pre-act read). End with two lines left UNSIGNED: `COO half: UNSIGNED`
   and `CTO half: UNSIGNED`. Security-level fields only; no relationship id, account id or client name appears in it.

### ACCEPTANCE

<criterion id="SC21-e91-AC1" cell_refs="SC-e-91"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_retained_revisit.py revisit</invocation><expect>RETAINED-REVISIT ok=True</expect></criterion>
`SC21-e91-AC1` -- the module's own `reclassify_retained` moves a retained unclassified holding that has a `NAME::` row, leaves the one without and the in-six control byte-identical, hands back its `moved` tuple and is idempotent.

<criterion id="SC21-e91-AC2" cell_refs="SC-e-91"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_retained_revisit.py wiring</invocation><expect>RETAINED-WIRING ok=True</expect></criterion>
`SC21-e91-AC2` -- `build()` reaches the retained pass on a fire with no new partition and hands `reclassify_retained` a `moved` accumulator.

<criterion id="SC21-e91-AC3" cell_refs="SC-e-91"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_half_request_check.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md</invocation><expect>HALF-REQUEST ok=True</expect></criterion>
`SC21-e91-AC3` -- the half request exists with its five sections and both halves unsigned.

<expected_criteria>SC21-e91-AC1, SC21-e91-AC2, SC21-e91-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~09:3xZ): SC21-e91-AC1 FAIL as expected (`moved=0 mix_ok=False`; the stays and control arms read True); SC21-e91-AC2 FAIL as
expected (`early_return_runs_pass=False moved_passed=False`); SC21-e91-AC3 FAIL as expected (the file is absent). A minimally patched temp copy of C_06
(the retained filter widened, a `moved` parameter, one early-branch call) reads AC1 and AC2 `ok=True`, so both checks can pass.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan, DynamoDB get_item): no write to any table or bucket, no deploy, no invoke, no model call.
  Never push. The deploy is NOT part of this cell.
- **Never edit** `lib/etf_classifier.py`, D_04, D_03, `.tools/`, or any test other than the new file. The BD gold suite must stay green;
  run it once at the end and report the count.
- **Client data stays out.** Print no relationship id, account id or client name anywhere in the half request, the tests or the report.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-W80-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken any test.

<paths>
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/tests/test_c06_retained_unclassified_r21.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_RETAINED_UNCLASSIFIED_20261012.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R21.md</decomp_doc> (round 21), cell `SC-e-91`.
<owned_cells>SC-e-91</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC21-e91-AC1, SC21-e91-AC2, SC21-e91-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~80/MDPF_SECCLASS.TO-SC-e91.c06-retained-unclassified-revisit.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC21-e91-AC1,SC21-e91-AC2,SC21-e91-AC3`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, the number of relationship JSON reads a no-new-partition fire makes,
the writer counts, the BD gold suite count, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the ship is a later pair-gated act by a CloudOps lane, outside a BD gold run; this cell ships no key.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only get_item and head-object under the seat's role).
comp-adversary: RUN -- a function-level test standing in for the served path (round 16 and round 20 each passed that way and the served bytes did not move; AC1 drives the module's own function and AC2 reads the wiring of build()); a pass that rewrites an unchanged relationship every fire (idempotence is in AC1); a retained holding already in the six moved by the revisit (the control arm). BLIND: whether the moved dollars on retained dates are the right comparator for leg G (SC-e-94's read decides which dates are re-served).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-20 analysis section 2 (D1-S30 ruling) and section 3 item 1 (msg 4321); row D1-S30 @cf1dbb8d31; DECOMP_R21.
