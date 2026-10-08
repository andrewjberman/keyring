# TO MDPF_SECCLASS.TO-SC-e76 -- round 15 SC-e-76: BD's classify_with_identity reads the NAME:: row when the identity chain cannot place a blank-ticker position

<to_id>MDPF_SECCLASS.TO-SC-e76</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~66</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-76` (`decompositions/MDPF_SECCLASS_DECOMP_R15.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-76`, row D1-S11. BD's firm mix serves 6.94 pct unclassified. The trace `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.md` puts
$133.58M (796 securities, group A) on blank-ticker positions that already have a canonical `NAME::<normalized name>` row in
etf-classifications. `data/black_diamond/scripts/gold/lib/etf_classifier.py` `classify_with_identity` (:207-230) tries only the identity
chain (`IdentityResolver.resolve`, :324-358: CUSIP and ticker keys) and stops with reasons like "name-carries-several-cusips".

**Build:**
1. In `classify_with_identity`, ONLY when the chain returns no key or a key with no row, read
   `'NAME::' + ETFClassifier.normalize_name(asset_name)`. If that row exists, return its class and sub-class with class_source
   `etf-classifications` and identity_hop `name-key`. Keep the existing order: a ticker, or a chain that already places the position,
   is never changed. Confirm the key form against the trace's `name_key` values before writing the code.
2. Write `data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py` with the table client stubbed. It must cover:
   - a blank-ticker name whose chain fails resolves through the NAME:: row;
   - a ticker position and a chain-resolved position return exactly what they return today (the controls);
   - a name with no NAME:: row stays unclassified.
3. Check whether `data/cot/scripts/gold/lib/etf_classifier.py` carries the same gap; if it does, file a row. Do not edit it.
4. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_KEY_LOOKUP_20261008.md`. Shape it like the other half requests in that folder,
   with `## The act`, `## Blast radius` and `Rollback per key`. It must name:
   - the act: deploy the lib file to `s3://opal-data-bd/code/gold/lib/`;
   - the shipped-bundle members safe-deploy also re-ships, each with a byte diff against what is served (row D1-S12);
   - the blast radius: the BD served mix moving $133.58M out of unclassified, by class, as a candidate diff from the trace;
   - the rollback per key: the current lib VersionId.
   Leave both halves unsigned.

### ACCEPTANCE

<criterion id="SC15-e76-AC1" cell_refs="SC-e-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/sc_r15_name_lookup.py</invocation><expect>NAME-LOOKUP ok=True</expect></criterion>
`SC15-e76-AC1` -- at least 99 pct of the 796 group-A securities resolve to their NAME:: row's class (live read-only get-item).
<criterion id="SC15-e76-AC2" cell_refs="SC-e-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_KEY_LOOKUP_20261008.md</invocation><expect>HALF-READY</expect></criterion>
`SC15-e76-AC2` -- the half request carries the act, the blast radius with a candidate diff, and the rollback per key.
<criterion id="SC15-e76-AC3" cell_refs="SC-e-76"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC15-e76-AC3` -- the whole BD gold suite passes, the new pin included.

<expected_criteria>SC15-e76-AC1,SC15-e76-AC2,SC15-e76-AC3</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~19:2xZ):
- SC15-e76-AC1: FAIL, as expected (resolved=5 of 796).
- SC15-e76-AC2: FAIL, as expected (the half is absent).
- SC15-e76-AC3: PASS, as expected (control, 82 passed).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan): no write to any table or bucket, no deploy, no invoke, no model call. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W66-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_NAME_KEY_LOOKUP_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R15.md</decomp_doc> (round 15), cell `SC-e-76`.
<owned_cells>SC-e-76</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC15-e76-AC1, SC15-e76-AC2, SC15-e76-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~66/MDPF_SECCLASS.TO-SC-e76.bd-name-key-lookup.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC15-e76-AC1,SC15-e76-AC2,SC15-e76-AC3`. Record a judgment criterion as
`UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming 3.0.0_SA_CVO, never as PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the lib deploy is the issuer's act under the pair, before a BD gold fire.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only get-item under the seat's role).
comp-adversary: RUN -- a chain-resolved or ticker position moved (controls); a NAME:: key form that differs from the trace's; BLIND: COT's lib copy (step 3) and the shipped-bundle refresh (row D1-S12).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL1 msgs 1061, 1066, 1071; Andrew-direct 2026-10-08 ~19:0xZ (alternatives rule); trace @3d9077bdc5; DECOMP_R15.
