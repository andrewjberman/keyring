# TO IRPT_DASHBD.TO-DB-b-318 -- C0 of the Cottonwood Performance read path: a READ-ONLY trace of the live 49F read function with synthetic staff requests for the firm cottonwood, the existence of the Cottonwood ownership-map and directory objects, and the API authorizer's firm handling (CTO ruling A, msg 10134) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-318</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTREAD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/RULING_COTTONWOOD_READ_PATH_OPTION_A_20261017.md` @6bfcbcf2cc (A ruled, C0 authorized, "run C0 now") and the plan `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/COTTONWOOD_READ_PATH_PLAN_20261017.md` @bba0548150 | **Decomp cell:** `DB-b-318` (decomposition section 178).

**Risk class WORLD, read only:** a synthetic invoke of a live function and reads of objects. **Nothing is written, deployed or changed**; no ledger is opened (no write leg).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`). Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once.** **No account id, no client name and no token appears in any file, commit message, row, log line you write or message you send: the client is the LABEL `cottonwood-client-1`; the ids live in memory only** (the CTO's conditions on the earlier trace ruling, XA-20261016T213506Z-8db5, apply).

**What this order answers.** Andrew's smoke showed the Cottonwood Performance tab empty. The CTO traced it to the live 49F read function's directory bucket map (`{49financial}`). Before any code is cut we need: (1) what the live function says today to a synthetic staff request for the firm cottonwood and to a 49F control, at the function (not at the API); (2) whether the Cottonwood ownership-map objects and the directory pointer exist; (3) where the API authorizer `naqxlm` keeps its firm handling.

**Do, in this order. Record every value named in `COT_READ_C0_RECORD.json` as you go (keys exactly as the checker `p184_cot_read_c0.py` lists).**

1. **Read first:** the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p184_cot_read_c0.py`; `infra/aws/lambda/investor-reporting/_authz/served.py` (`handle`, lines 1195 to 1270: how the firm, the internal subject and the selected tenant are decided; `event_headers`, `check_contract_version`, `selected_tenant`) and its tests under `_authz/tests/` (find how a test builds a synthetic proxy event with verified internal-staff headers; reuse that shape, never invent a header); `infra/aws/terraform/investor-reporting/reporting-read/api.tf` (the three routes and the authorizer `naqxlm`).
2. **The client by label.** Read the Cottonwood directory object (the registry bucket's `investor-reporting/directory/latest.json` for the firm cottonwood, as `reporting-publish`'s `read_directory(s3, directory_bucket("cottonwood"))` does) and pick the entry whose display name starts with "Thiessen"; take its first account id and map it to the published raw key through the platinum prefix (`irpt/cottonwood/platinum/reporting/account=<raw>/`) exactly as `reporting-publish/handler.py` `_published_map` does. Name this client `cottonwood-client-1` everywhere you write. For the control take the first sorted account of the 49 Financial published prefix, label `control-49f`.
3. **The three probes** (`lambda invoke --invocation-type RequestResponse --cli-read-timeout 0`, the function `irpt-49f-reporting-read-lambda`, a synthetic API proxy event built from the test shape of step 1 with VERIFIED internal-staff headers as the tests build them, the contract-version header the function requires, and `selected_tenant` as a query parameter): (a) `cottonwood-client-1-manifest`: the manifest route for the cottonwood client's account with `selected_tenant=cottonwood`; (b) `cottonwood-client-1-series`: the series route, same; (c) `control-49f-manifest`: the manifest route for the control account with `selected_tenant=49financial`. Record, for each, `status` (the proxy response's `statusCode`), `reason_code` (the refusal's public reason token such as `FIRM_BINDING`, else null), `content_encoding` (the response header, else null), `invoked_utc` and the Lambda `request_id`. **Never record or print a response body.** The control must answer 200; if a probe cannot be built without writing or without a real token, STOP and say what blocks.
4. **Existence reads (head only).** In the bucket `opal-data-cottonwood` head the two keys `platinum/cottonwood/ownership_map.json` and `advi/cottonwood/platinum/cottonwood/ownership_map.json` (a 404 is "absent"; any other error is a STOP). Read `directory/latest.json` for cottonwood and record whether it exists and its entry count. Record only the booleans and the count.
5. **The authorizer.** `aws apigatewayv2 get-authorizer` for `naqxlm` on API `7k3ed8px20`: record its id, its type and the Lambda function it calls (its name); then find in the repo where that function's source keeps its handling of the firm or of a permitted-firm list (a repo path, or `none`), and whether it lists firms (a boolean). One path and one boolean only.
6. **The function record.** `function` {`name`, `code_sha256_before`, `code_sha256_after` (the live `CodeSha256` read before step 3 and again after step 5: equal), `directory_bucket_map` (the sorted firm tokens of the live `IRPT_DIRECTORY_BUCKET_MAP` environment variable)}.
7. **Record** `COT_READ_C0_RECORD.json` with `claim` "measured", `applier`, `no_write` true, `probes`, `ownership_map` {`bucket`, `legacy_key_exists`, `canonical_key_exists`}, `directory` {`latest_json_exists`, `entry_count`}, `authorizer`, `function`, `notes` (one paragraph in words: what the function answered to cottonwood and why you think so, what you could not establish) and `reads` {`vendor_calls` 0, `secret_reads` 0}. Flip this order to complete as your last commit.

<criterion id="DBC184-1-AC1" cell_refs="DB-b-318"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p184_cot_read_c0.py" . DBC184-1-AC1</invocation><expect>DBC184-1-AC1 PASS</expect></criterion>
`DBC184-1-AC1` -- the record: three labelled probes (statuses and reason codes only, the 49F control 200), the ownership-map and directory existence flags, the authorizer's identity and firm-handling location, the function unchanged, no write, no id. Base: FAIL (no record).
<criterion id="DBC184-2-AC1" cell_refs="DB-b-318"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p184_cot_read_c0.py" . DBC184-2-AC1</invocation><expect>DBC184-2-AC1 PASS</expect></criterion>
`DBC184-2-AC1` -- FRESH live reads: the ownership-map flags equal the record's, the 49F read function runs the recorded code hash and bucket map (nothing was written). Base: FAIL.

<expected_criteria>DBC184-1-AC1,DBC184-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the read-only AWS calls this order names and nothing wider.
- **Reads and writes.** Writes to AWS: NONE. Allowed: `lambda invoke` of the one function (the three probes), `get-function-configuration`, `s3api head-object` and `get-object` of `directory/latest.json`, `apigatewayv2 get-authorizer`. No `update-function-code`, no `put`, no Terraform command.
- **Stop rules.** A probe that needs a real token, a write of any kind, a head error other than 404, or a response that carries client data into a log you cannot avoid: STOP at once and report to the issuer.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB5-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-318.cottonwood-read-path-c0-readonly-trace.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 178 (round 150, workstream COTREAD), cell `DB-b-318`.
<owned_cells>DB-b-318</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC184-1-AC1, DBC184-2-AC1 (mechanical, WORLD read only). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-318.cottonwood-read-path-c0-readonly-trace.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC184-1-AC1,DBC184-2-AC1` BEFORE the flip (the ids as ONE comma-joined argument).
</proof_of_spec>

**REPORT:** once, under 150 words: the two criteria's last lines; the three probes' status and reason code by label; the two ownership flags; the authorizer's firm-handling location; what you could not establish.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read only; nothing is planned, applied or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant changes; the applier's own read access is used.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the authorizer is read, not edited.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the checker's selftest is green on a synthetic record and red on 16 single-fault arms.
lane: the <paths> block IS the grant.
</preflight>
