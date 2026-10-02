# TO IRPT_BCKEND.TO-IB-pr-296 -- The installed render ports carry the retained-owner reader, and the print query takes the resolved kind

<to_id>IRPT_BCKEND.TO-IB-pr-296</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~101</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer, inside its decomposition (rows IRPT_BCKEND-W101-S7 and W101-S9, whose
remedy owner is 2.0.0_SA_COO~P; repairs batched into one cell) | **Decomp cell:** `IB-pr-296` (decomposition section 27 addendum note:
round 33, one cell; row IRPT_BCKEND-S267) | **outcome_ref:** FWD-9 (hop 12) | **depends_on:** IB-pr-293 (merged @88480ab9d8), IB-pr-294
(merged @1572729cfd)

---

## WORKER FACE

**The cell.** Two repairs on the export path to the served Analysis export (E4).
1. Row W101-S7: the Enforcer's prospect branch reads the report's RETAINED owner through the optional port `load_report_owner(tenant,
   report_id, report_revision)` (`_authz/enforce.py:282`, `:654-659`), and `_render_identity/grant.py` `render_ports(...,
   report_owner=None)` (`:277-311`) returns it as a third port. But `_authz/served.py` `render_ports_from_env` (`:1155-1169`) calls
   `_grant.render_ports()` with no reader, so every served prospect render refuses fail-closed. Wire the reader.
2. Row W101-S9: `export/retained_export.py` `print_query` decides "analysis" by report SHAPE (`_is_analysis`: no `dates` dict), not
   by the resolved kind the submit already holds. Make it take the resolved kind.

**What exists (read first).** `_authz/served.py` (`render_ports_from_env`, and how `Entry` unpacks the ports at `:754-756`);
`_render_identity/grant.py` `render_ports`; `_authz/enforce.py` `_resolve_prospect_render` (what the owner record must carry: firm,
principal, class, advisor, home firm, prospect input id); `reports/repository.py` (`ReportRepository.persist` writes the owner into
the index; `_key` `:66`; `_storage_firm` `:81`; `DynamoReportIndex.get(tenant, key)` `:415`, the irpt-requests table);
`reports/composition.py`; `ops/entry.py:224` (irpt-status installs `render_ports_from_env()`); `export/retained_export.py`
(`print_query`, `_is_analysis`, `resolve()` returns `kind`); `export/submit_service.py` (calls `print_query`).

**What you build.**
- `render_ports_from_env` passes `report_owner=` a READ-ONLY reader of the retained owner by (tenant, report id, revision), from the
  same retained report index the function already reads (environment, never a typed table name). The reader resolves the SAME key
  the writer used (`_key`, the storage firm), returns the stored owner record, and returns None for a missing item. It never writes,
  and an unset index refuses (fail closed). A tenant/storage-firm key the writer and reader cannot agree on is a row, never a guess.
- `print_query` takes the resolved kind (ANALYSIS | PERFORMANCE) from its caller; `submit_service` passes it. PERFORMANCE prints
  exactly as today.
- Tests: `_authz/tests/test_render_ports_report_owner.py` (at least 3, through `served.Entry` with `render_ports_from_env` and a
  fixture index: a prospect render admitted when the stored owner matches the grant; refused when it differs; refused when the index
  is unset or the item missing -- name `report_owner`, `Entry`, `render_ports_from_env`, "refused");
  `export/tests/test_print_query_kind.py` (at least 2: an ANALYSIS record with a stray `dates` dict prints as analysis; a PERFORMANCE
  print query is unchanged -- name ANALYSIS, PERFORMANCE, `dates`).

<criterion id="IB33-1-AC1" cell_refs="IB-pr-296"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r33/p33_1_ac1_render_ports_owner.py" .</invocation><expect>IB33-1-AC1 PASS</expect></criterion>
`IB33-1-AC1` -- the owner-reader tests pass through `served.Entry` (at least 3, none failing). Base: FAIL (no file).

<criterion id="IB33-1-AC2" cell_refs="IB-pr-296"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r33/p33_1_ac2_print_query_kind.py" .</invocation><expect>IB33-1-AC2 PASS</expect></criterion>
`IB33-1-AC2` -- the print-query kind tests pass (at least 2, none failing). Base: FAIL (no file).

<criterion id="IB33-1-AC3" cell_refs="IB-pr-296"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r33/p33_1_ac3_suites_unchanged.py" .</invocation><expect>IB33-1-AC3 PASS</expect></criterion>
`IB33-1-AC3` -- `_authz`, `reports`, `export`, `ops`, `_render_identity` and `directory` suites fail only their listed baseline ids
(each suite in its own process). Base: PASS (a regression guard).

<expected_criteria>IB33-1-AC1,IB33-1-AC2,IB33-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. `reports/repository.py` and
  `reports/composition.py` are read only: reuse them; a change they need is a row.
- **AWS:** none. Offline, fixtures only. No deploy: the served move is E4 (IB-pr-282), the issuer's packet.
- **Refusal clause.** An existing test that moves is a defect: stop and file a row, never edit the test. A PERFORMANCE print or an
  account-scoped render that moves is a defect, stopped with a row.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_render_identity/grant.py
infra/aws/lambda/investor-reporting/_render_identity/report_owner.py
infra/aws/lambda/investor-reporting/export/retained_export.py
infra/aws/lambda/investor-reporting/export/submit_service.py
infra/aws/lambda/investor-reporting/_authz/tests/test_render_ports_report_owner.py
infra/aws/lambda/investor-reporting/export/tests/test_print_query_kind.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r33/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/` (all of it), `docs/contracts/investor-reporting/v1/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 27 addendum note (round 33, workstream ~P), cell `IB-pr-296`.
<owned_cells>IB-pr-296</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB33-1-AC1, IB33-1-AC2, IB33-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~101/IRPT_BCKEND.TO-IB-pr-296.render-owner-reader-print-kind.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IB33-1-AC1,IB33-1-AC2,IB33-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the reader (file:line) and the index key it reads, the
environment variable it uses, and any surprise row id (`IRPT_BCKEND-W101-S<k>`, k >= 11).

---

## RECORD FACE

<preflight>
comp-blast: RUN -- `render_ports_from_env` is installed by every read function that sets IRPT_EVIDENCE_BUCKET (irpt-status at ops/entry.py:224); the reader is consulted only on the prospect branch (a stored prospect scope), so account-scoped renders are untouched; AC3 holds six suites; 0 served bytes move in the cell.
comp-iam: DECLARED-NOT-APPLICABLE in the cell -- no role changes; whether each installing function's role reads the report index is E4's packet's question.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: request-driven ports and a print query; no schedule, trigger or cron is created or moved.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB33-1-AC1 base FAIL (no file), IB33-1-AC2 base FAIL (no file), IB33-1-AC3 base PASS (regression guard: _authz 189 + 6 baseline, reports 88 + 1 baseline (row S268), export 153, ops 224, _render_identity 45, directory 171), dry-run at the base 2026-10-02 ~12:3xZ.
lane: the <paths> block IS the grant.
</preflight>
