# TO ADVI_BILLING.TO-AB-r-2 -- D2-S3: one exercised cross-firm probe -- an other-firm admin token with complete claims against a 49 Financial household, refused by the firm binding

<to_id>ADVI_BILLING.TO-AB-r-2</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.7.0_AE_CloudOps~AB2</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>EDGEPROBE3</workstream>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-r-2` (decomposition section 4, round 3) | **outcome_ref:** FWD-1 (D2-S3) | **depends_on:** none. **Authority:** CTO ADDENDUM 3 @7f414eb19e (msg 3004); probe terms of ADDENDUM 2 @abbf204c7e.

---

## WORKER FACE

Your folder is `org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/`.

**The cell.** Round 2's `other_firm` probe was refused at the edge's "missing identity claims" (`infra/aws/lambda-edge/auth-validator-edge/index.mjs:478-492`)
before any firm logic, so the cross-firm arm is ABSENT, not exercised (your row ADVI_BILLING-D2-S3). Exercise it: a token from ANOTHER firm with
COMPLETE claims, whose `firmRole` is `admin` so the edge's book check is bypassed and only the firm binding stands between it and a 49 Financial
household's fee. Expected: the read route `advi-49f-billing-read-lambda` refuses it with its firm-binding refusal (round 1 measured
`401 {"error": "Access denied to this firm"}` for a non-49F firm, `infra/aws/lambda/advi/billing-read/entry.py:113-158`).

1. Open the ledger `advi-billing-crossfirm-probe-r3-20261009` FIRST (one verify leg); commit after `open`, after the leg and after `close`.
2. Mint ONE synthetic 10-minute token with `opal/auth/jwt-private-key` (your round-2 path), in the auth handler's claim shape
   (`infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:168-185`): `sub`/`email` `advi-billing-probe-6@example.invalid`, `firmId` = a real
   firm other than 49financial that has a `FIRM#<id>` row in `opal-users-v2` (prefer `inflection` or `cottonwood`), `role` user, `firmRole`
   admin, `advisorId`, `advisorKey`, `userType` and every other claim the edge requires present.
3. ONE GET through `https://opalinvest.dev/api/scoped/partners/books/relationship/z08219260/fee-quarter/2026Q3`. Record the status and the
   first 80 characters of the error body. Classify `refused_by`: `firm_binding` (the Lambda's firm refusal), `edge_claims` (the edge's missing-claims
   refusal), `edge_book` (the edge's not-authorized refusal), or `other`; read the edge and Lambda source to classify, and if the edge refused,
   name the line.
4. Never store or log a token or key byte. Record `AB_R2_CROSSFIRM_PROBE.json`: `ledger_slug`, `minted_at`, `minted_by`, `key_read_at`,
   `probe` = `{method: "GET", route, via: "cloudfront", firm_id, status, error_head, refused_by, refusing_line}`.

<criterion id="AB3-2-AC1" cell_refs="AB-r-2"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB3-2-AC1</invocation><expect>AB3-2-AC1 PASS</expect></criterion>
`AB3-2-AC1` -- one GET probe recorded, status 401/403, refused_by firm_binding, no token bytes, ledger closed. Base: FAIL.

<expected_criteria>AB3-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- GET only; ONE probe; one read of the signing secret (time and actor recorded, never bytes); no write to any AWS resource, user, role or table.
- **Refusal clause.** An edit outside the grant, a write or deploy the face does not name, a vendor call, or an account number, name
  or dollar figure in a committed file is a defect: stop and file a row.

<paths>
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/
org/critical_paths/change_management/advi-billing-crossfirm-probe-r3-20261009.md
org/critical_paths/.open_deploys/advi-billing-crossfirm-probe-r3-20261009.json
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-r-2.crossfirm-probe.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 4 (round 3), cell `AB-r-2`.
<owned_cells>AB-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB3-2-AC1. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.7.0_AE_CloudOps~AB2/ADVI_BILLING.TO-AB-r-2.crossfirm-probe.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB3-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured, and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- nothing live moves in the cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB3-2-AC1 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
