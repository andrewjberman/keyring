# TO IRPT_DASHBD.TO-DB-b-115 -- defect W88-S3: the reporting-gold handler passes the firm's declared source entry to every emit_day call, so the returns manifest states method row 2 and its three method fields and never the literal absent -- with a test; no deploy

<to_id>IRPT_DASHBD.TO-DB-b-115</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~90</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>59</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the issuer's ruling on row IRPT_DASHBD-D2-W88-S3 (DB-b-113's measured manifest regression), under 1.0.0_SA_CTO~DELL2's msg 3999 (four members acceptable only with method_version 2 included) | **Decomp cell:** `DB-b-115` (decomposition section 61) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-96, DB-b-102, DB-b-113 (all drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-90`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~90/`.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit message, a record, a row or a report. Test fixtures
are synthetic.

**The cell (`DB-b-115`).** DB-b-96 and DB-b-102 made `account_return_daily.py` read the returns manifest's `method_version` and its three method fields
(`valuation_source`, `fee_treatment`, `price_basis`) from the source entry passed as `src`. The reporting-gold handler never passes it:
`infra/aws/lambda/investor-reporting/reporting-gold/handler.py` calls `ard.emit_day(...)` three times (lines ~430, ~579, ~620) without `src=`.
DB-b-113 MEASURED the result (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/R45_REFRESH_DELTA0.json`, `manifest_method_fields`;
row `IRPT_DASHBD-D2-W88-S3`): the live manifest states `method_version` 2, and the handler at HEAD would state the literal `absent` for all four. A served
manifest that drops its method claim is a regression, so the R45 release cannot be signed until this is fixed.

In `C:/dev/wk-irpt-dashbd-90`:
1. **Read** `emit_day`, `build_manifest`, `method_fields_of`/`method_version_of` and `source_entry` in
   `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, and in the handler `compute()` (it already resolves `src` at ~line 225) and the
   three `emit_day` call sites. Read DB-b-113's probe `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~88/manifest_probe.py`.
2. **Fix, in the handler only:** every `ard.emit_day(` call passes `src=` the firm's declared source entry, the SAME entry `compute()` resolved for
   that run (carry it out of `compute()` or resolve it once by the same rule; never a second, differently-derived entry and never a typed key). Change
   no producer file. Check whether the handler writes `dim_return_method` or any other artifact that takes `src`, and say what you found with file and line;
   fix it only if it has the same defect, and say so.
3. **Test** in `infra/aws/lambda/investor-reporting/reporting-gold/tests/`: on a synthetic fixture, the manifest the handler's own call writes states
   `method_version` 2 and the three fields exactly as the 49F custody entry in `sources.json` declares them, and none is `absent`. The test fails on
   the handler before your fix. Keep every existing test in that folder and in `data/assets/scripts/gold/irpt_reporting/tests/` passing.
4. **Record** `HANDLER_SRC_FIX.json` {call_sites: [{line, passes_src}], manifest: {method_version, valuation_source, fee_treatment, price_basis}
   (as written by the fixed handler's call on the fixture), other_src_consumers: [...], tests: {passed, failed, new_test}}.

**No deploy, no AWS call.** The bytes ride the R45 gold release after its packet is refreshed again.

<criterion id="DB59-1-AC1" cell_refs="DB-b-115"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r59/p59_round59.py" . DB59-1-AC1</invocation><expect>DB59-1-AC1 PASS</expect></criterion>
`DB59-1-AC1` -- every emit_day call in the handler passes src, and the manifest it writes states row 2 and the entry's three method fields, tested. Base: FAIL.

<expected_criteria>DB59-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/` or `portal/`, and under `infra/` only the two paths in the grant.
- **This order's exception:** you edit the reporting-gold `handler.py` and its tests. No deploy.
- **AWS:** none. NO Black Diamond or vendor call, no secret read, no S3 read or write, no deploy, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~90/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~90/
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-115.handler-passes-src.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 61 (round 59), cell `DB-b-115`.
<owned_cells>DB-b-115</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB59-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~90/IRPT_DASHBD.TO-DB-b-115.handler-passes-src.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB59-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, the criterion's last line, the three call sites before and after, the manifest fields the fixed call writes, other src consumers found, test counts and the new test's name, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the gold Lambda's handler; the returns manifest is its only output this cell changes; ships later under the R45 pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no new call, key or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB59-1-AC1 FAIL at base (3 of 3 emit_day calls lack src=). Row IRPT_DASHBD-D2-W88-S3.
lane: the <paths> block IS the grant.
</preflight>
