# TO IRPT_DASHBD.TO-DB-b-102 -- E4: build_manifest takes method_version from the firm's sources entry -- a positions-based entry names its own method row with its rule-24 record, a firm with none writes absent, the custodian firms keep 2 explicitly

<to_id>IRPT_DASHBD.TO-DB-b-102</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~77</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>49</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 15 (msg 3492, @74243ee7c8) and ADDENDUM 13.2 (msg 3501), enrichment item E4 | **Decomp cell:** `DB-b-102` (decomposition section 51) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-96 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-77`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/`.

**The cell (`DB-b-102`).** In `C:/dev/wk-irpt-dashbd-77/data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, `build_manifest()` writes
`method_version: METHOD_VERSION` (2, the custodian-equity method row) into every manifest, whatever the source entry says (around line 1756). It does
the same in the row frame (around line 1278) and in `dim_return_method` (around line 1795). ADVI_COTBKF's CB-aq-1 built 3,325 Cottonwood days with
positions-based fields, and every manifest claims method 2. The CTO ruled (ADDENDUM 13.2) that this is the default claim ADDENDUM 13.1 forbids, and
that this producer cell comes first.

1. Each custody source in `sources.json` carries `method_version`. The existing custodian channel keeps `2` explicitly.
2. `build_manifest()` (and the row frame and the method dimension, where they state it) takes `method_version` from the entry:
   - an entry without one writes `absent`, never 2;
   - a positions-based entry (`valuation_source` not `custodian_reported`) must name its OWN method row, never 2.

   Add that row's definition to the method table's source in this file, with a rule-24 record `METHOD_ROW_RULE24.md` in your folder. Declare no
   Cottonwood entry yourself, since none is at your base.
3. Tests:
   - the custodian entry's manifest reads 2;
   - NEGATIVE arm: a positions-based entry's manifest never reads 2;
   - an entry with no method writes `absent`;
   - every existing producer test still passes.
4. Record `METHOD_FROM_SOURCE.json` {tests: {passed, failed, new_test, negative_test}, method_rows}.

No deploy and no AWS call. ADVI_COTBKF's CB-al-2 mint waits on this drain.

<criterion id="DB49-4-AC1" cell_refs="DB-b-102"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r49/p49_round49.py" . DB49-4-AC1</invocation><expect>DB49-4-AC1 PASS</expect></criterion>
`DB49-4-AC1` -- build_manifest takes method_version from the source entry, never a default 2, tested with a negative arm. Base: FAIL.

<expected_criteria>DB49-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the returns producer, its sources.json and its tests. No deploy.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/sources.json
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-102.method-version-from-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 51 (round 49), cell `DB-b-102`.
<owned_cells>DB-b-102</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB49-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~77/IRPT_DASHBD.TO-DB-b-102.method-version-from-source.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB49-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the method rows, the tests, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the returns producer; a fix reaches served output only through a later release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no role change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB49-4-AC1 FAIL at base (build_manifest writes METHOD_VERSION directly; no record). CTO ADDENDUM 13.2.
lane: the <paths> block IS the grant.
</preflight>
