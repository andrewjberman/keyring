# TO IRPT_DASHBD.TO-DB-b-323 -- C4 of the Cottonwood Performance read path: APPLY the signed pair (packet sha256 `07e9ab116825`): gates and live reads, ledger, ONE build of both function-map entries, ONE `safe-apply` of the new root `reporting-read-iso` (5 add), direct probes of the new function incl. a forged-forward event, ONE `safe-apply` of `reporting-read` (1 add, 1 change), probes through the live 49 Financial function, receipt (CTO ruling A, msg 10134) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-323</to_id>
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
<workstream>COTAPPLY</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the signed pair, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_COTTONWOOD_PERFORMANCE_READ_PATH_FORWARD_COO_HALF.md` @d242bc65d8 and CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_PERFORMANCE_READ_PATH_FORWARD_CTO_HALF.md` @b43bdc076f, both bound to the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_COTTONWOOD_PERFORMANCE_READ_PATH_FORWARD.md` (sha256 `07e9ab116825445bd7414e3963075be518036fe4eb209ceb93a7ede44d97cd87`; CTO msg 10262: Act 3 uses an OPAL_GLOBAL internal identity and the receipt names the class; Act 3 (c), the forged forward refused, runs BEFORE Act 4) | **Decomp cell:** `DB-b-323` (decomposition section 182).

**Risk class WORLD:** one new function, role and policies, and a code and environment change of the live 49 Financial read function. The Performance tab of a Cottonwood account viewed by Opal staff moves from "absent" to the published series. **Nothing is written to any data object.**

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`, FULL checkout, carrying the packet, both halves, the three landed cells and the read tools); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once and writes nothing further.** **No account id, no client name, no token and no response body appears in any file, commit message, row, log line you write or message you send: the client is the LABEL `cottonwood-client-1` (the same real client C0 used); ids live in memory only.** Counts, hashes, statuses, sizes and words only.

**What this order does, in one paragraph.** It lands the three cells of the Cottonwood read path (the forward code `3eb27c60c0`, the Terraform `10dac78f46`, the function-map `67cc230180`): one new function `irpt-cot-reporting-read-lambda` with its `-cot-` role, and the forward from `irpt-49f-reporting-read-lambda` to it. The Cottonwood function is proven alone BEFORE anything forwards to it.

**Terraform is available on this box** (`.tools/terraform.exe`, v1.15.8): the packet's sentence that the box has no terraform binary is wrong; it does not change an act or a gate. The issuer ran `terraform init -backend=false` and `validate` on both roots from the landed trunk: both read "Success! The configuration is valid", and `fmt -check` reported nothing. You run `fmt -check`, `validate` and the `safe-apply` plan step yourself, and the plan gates below stand exactly.

**Read first (all in your worktree):** the packet (whole), both halves; the two roots `infra/aws/terraform/investor-reporting/reporting-read-iso/` and `reporting-read/` (`forward.tf`, `lambda.tf`); the two entries `infra/aws/lambda/ci/function-map/irpt-cot-reporting-read-lambda.json` and `irpt-49f-reporting-read-lambda.json`; `infra/aws/lambda/ci/build-and-upload.sh`; `infra/aws/lambda/investor-reporting/_authz/served.py` (`handle`, `_forward`); your own C0 order `IRPT_DASHBD.TO-DB-b-318...` and its record `COT_READ_C0_RECORD.json` (the synthetic event shape and the client label); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p189_cot_read_apply.py` (the keys of your record). **Lessons applied here:** every invoke uses `--cli-read-timeout 0 --invocation-type RequestResponse --log-type Tail`; a lost client response is judged from the Lambda side (its log), never retried blind; an invoke response is read for its status, reason token, content-encoding and byte size only.

**Do, in this order. Record every value named in `COT_READ_APPLY_RECORD.json` as you go (keys exactly as the checker `p189_cot_read_apply.py` lists).**

0. **Gates, read only.** (a) `sha256` of the packet equals `07e9ab116825445bd7414e3963075be518036fe4eb209ceb93a7ede44d97cd87` (`gates.packet_sha256`); both halves read SIGNED at it (`gates.coo_half_signed`, `gates.cto_half_signed`). (b) The three landing commits are ancestors of HEAD (`git merge-base --is-ancestor <sha> HEAD` for `3eb27c60c0`, `10dac78f46`, `67cc230180`). (c) **One change at a time:** no ledger under `org/critical_paths/change_management/` and no `.open_deploys` marker at ANY live worktree (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`; print the denominator) names `irpt-49f-reporting-read-lambda`, `irpt-cot-reporting-read-lambda`, the roots `reporting-read` or `reporting-read-iso`, or the API `7k3ed8px20`'s Performance routes; other IRPT ledgers are other surfaces (`gates.one_change_at_a_time`: `worktrees_read`, `open_markers_naming_this_surface` = 0). (d) The live state equals the packet's section 2 (`gates.live_matches_packet`). Any mismatch: STOP.
1. **Open the NEVER-2 ledger BEFORE any write** with `python .tools/deploy_ledger.py open ...` under `org/critical_paths/change_management/`, slug `irpt-dashbd-cottonwood-read-path-forward-20261017`, **naming yourself (`0.7.0_AE_CloudOps~IB2`) as the applier**, legs: L1 git; L2 build; L3 terraform (two roots); L4 probes; L5 receipt. Commit its `.open_deploys` sentinel at once. Record `ledger_entry`, `applier`, and `probe_identity_class` (the class of the staff identity every staff probe below uses: it must be `OPAL_GLOBAL`, the internal identity class Andrew uses at Global).
2. **Before reads.** `before` {`cot_function_exists` false, `cot_role_exists` false, `cot_artifact_exists` false (the key `investor-reporting/irpt-cot-reporting-read-lambda.zip`), `read_artifact_version_id` (the 49 Financial artifact key's current version: expected `J9krUD0Qw3fz5QdcfYM4CRg7bYlHNigW`), `read_code_sha256` (the function's live CodeSha256: expected `z634S2QsrfCpY4c3cD2UGwicdmLDo6/Rmng8SrEskCQ=`), `prefixes` (the Cottonwood platinum reporting `account=` prefixes by one delimiter listing, auto-paginated, denominator printed: expected 939), `objects` and `versions` (client-side counts over `irpt/cottonwood/platinum/reporting/` in `opal-data-cottonwood`, every page), `bucket_policy_sha256` (sha256 of the bucket policy JSON canonicalised with sorted keys and compact separators) and `bucket_policy_statements` (7)}.
3. **Act 1 -- build and upload both entries.** (a) For each entry: `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <entry>` for `irpt-cot-reporting-read-lambda` and `irpt-49f-reporting-read-lambda`: **each base64 sha256 must equal the C3 record's `build_only_sha256`** (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~255/RD_COT_READ_FUNCTION_MAP_FACTS_R150.json`, `DhBc5TbOuUIdp70Op5MHpgCLq1TGnRC845ZwjEeQmoE=`, 32 members) **or STOP and say why**; record `build` {`cot_entry_sha256_b64`, `read_entry_sha256_b64`, `members`}. (b) The real `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <entry>` for each: a new key and a NEW VERSION of the existing key, and the entries' `artifact_sha256` updated; commit those two JSON fields with your receipt.
4. **Act 2 -- ONE `safe-apply` of `reporting-read-iso`.** `terraform fmt -check`, `validate`, `plan` through the `safe-apply` plan step. **The plan must read exactly 5 to add, 0 to change, 0 to destroy:** `module.irpt_reporting_read_iso.aws_lambda_function.this`, `module.irpt_reporting_read_iso.aws_cloudwatch_log_group.lambda`, `aws_iam_role.irpt_reporting_read_iso`, `aws_iam_role_policy.irpt_reporting_read_iso`, `aws_iam_role_policy.irpt_reporting_read_iso_service_profile`. Any other line STOPS. Then ONE `safe-apply`; a re-plan afterward reads No changes. Record `plans.iso` {`add`, `change`, `destroy`, `replan_no_changes`}.
5. **Act 3 -- the Cottonwood function, probed DIRECTLY (before Act 4).** Synthetic API proxy events built from the shape C0 used, with VERIFIED internal-staff headers of an OPAL_GLOBAL internal identity, the contract-version header, `selected_tenant=cottonwood`, for `cottonwood-client-1`: probe `cot-direct-manifest` (the manifest route; expect a served manifest), `cot-direct-series` (the series route; expect a gzip reply), `cot-direct-forged` (the SAME manifest request with the origin-verify header wrong and extra fields claiming a forward: **expect a refusal with a reason token and a body smaller than the served manifest; if it returns data, STOP before Act 4**). For every probe record `label`, `method` ("lambda-invoke"), `status`, `reason_code` (the refusal's token, else null), `content_encoding`, `size_bytes` (the payload length), `invoked_utc`, `request_id`. Also run the three simulations of the CTO's condition 3 now and record `simulate` {`invoke_new_function` (`iam simulate-principal-policy` of the 49 Financial role on `lambda:InvokeFunction` against the new function's ARN: the decision word, expected "allowed" AFTER Act 4, so run this one after Act 4), `invoke_other_function` ("implicitDeny" against one other function of the account), `s3_get_cottonwood_platinum` ("implicitDeny": `s3:GetObject` on a Cottonwood platinum key)}.
6. **Act 4 -- ONE `safe-apply` of `reporting-read`.** `fmt -check`, `validate`, `plan`. **The plan must read exactly 1 to add, 1 to change, 0 to destroy:** ADD `aws_iam_role_policy.irpt_reporting_read_forward`; CHANGE `module.irpt_reporting_read.aws_lambda_function.this` in place (code and environment: exactly one new variable `IRPT_FORWARD_COTTONWOOD_FUNCTION`). Any other line STOPS. ONE `safe-apply`; a re-plan afterward reads No changes. Record `plans.read`. Then the `invoke_new_function` simulation.
7. **Act 5 -- the probes through the live 49 Financial function** (`irpt-49f-reporting-read-lambda`, the same event shapes): `control-49f-manifest` (`selected_tenant=49financial`, the control account label `control-49f` as in C0: expect 200), `cot-via-49f-manifest` and `cot-via-49f-series` (the forward: expect the SAME status, content-encoding and byte size as the direct probes, the reply untouched), `inflection-via-49f` (`selected_tenant=inflection`: expect the refusal token `FIRM_BINDING`), `noninternal-cot-via-49f` (a non-internal caller selecting cottonwood: expect a refusal token). Record each as in step 5, in this order of labels: `cot-direct-manifest`, `cot-direct-series`, `cot-direct-forged`, `control-49f-manifest`, `cot-via-49f-manifest`, `cot-via-49f-series`, `inflection-via-49f`, `noninternal-cot-via-49f` (`probes`).
8. **Act 6 -- the after-read and the receipt.** `after` {`cot_function` {`code_sha256`, `memory_mb`, `timeout_s`, `env_keys` (sorted names only), `role` (the role NAME)}, `read_function` {`code_sha256`, `env_keys`, `forward_value` (the value of the forward variable: a function NAME)}, `read_role_policies` (the 49 Financial role's inline policy names), `bucket_policy_sha256`, `prefixes`, `objects`, `versions` (the same counts as before, read again)}; `ledger_closed` false (the issuer closes it after verification); `reads` {`vendor_calls` 0, `secret_reads` 0}; `notes` (words: counts, the memory and duration of the largest probe from its log REPORT line, the identity class, and the sentences "the page has not been looked at" and "advisor and client viewers of Cottonwood are not served until an ownership map exists"). Write `COT_READ_APPLY_RECORD.json` and flip this order's status to complete as your last commit.

<criterion id="DBC189-1-AC1" cell_refs="DB-b-323"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p189_cot_read_apply.py" . DBC189-1-AC1</invocation><expect>DBC189-1-AC1 PASS</expect></criterion>
`DBC189-1-AC1` -- the record: both halves signed at the packet's sha256, the ledger, both entries built to the C3 hash, the two plans at 5/0/0 and 1/1/0 with clean re-plans, the eight probes by label (the forward returns the reply untouched; the forged event and the unnamed firm refused), the OPAL_GLOBAL identity class, the three simulations, the counts equal before and after, no id. Base: FAIL (no record).
<criterion id="DBC189-2-AC1" cell_refs="DB-b-323"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p189_cot_read_apply.py" . DBC189-2-AC1</invocation><expect>DBC189-2-AC1 PASS</expect></criterion>
`DBC189-2-AC1` -- FRESH live reads: both functions run the bundle's code hash with the recorded environment keys (the new one without the forward variable), the new role carries `-cot-`, the 49 Financial role holds its three old policies byte-identical plus exactly the one forward statement. Base: FAIL.
<criterion id="DBC189-3-AC1" cell_refs="DB-b-323"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p189_cot_read_apply.py" . DBC189-3-AC1</invocation><expect>DBC189-3-AC1 PASS</expect></criterion>
`DBC189-3-AC1` -- FRESH live reads: the Cottonwood bucket policy equals the record's, the 939 prefixes, the three Performance routes still share one integration that invokes the 49 Financial function, and nothing routes to the new function. Base: FAIL.

<expected_criteria>DBC189-1-AC1,DBC189-2-AC1,DBC189-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the AWS acts the packet names and nothing wider. Everything else is read, never edited.
- **The signed acts, and nothing wider.** Writes to AWS: the artifact upload (a new key and a new version of one key), the TWO Terraform applies (`safe-apply`) of `reporting-read-iso` (5 add) and `reporting-read` (1 add, 1 change), and the synthetic invokes (read-only by construction). No `update-function-code`, no bare `terraform apply`, no delete of any object or version, no schedule change, no route change, no change to the Cottonwood bucket policy, no change to any staff profile row, no write to any data object. No act inside a weekday cache or fire window you know of.
- **Stop rules.** A `Task timed out`, an `AccessDenied` on a call this order names, a Max Memory Used above 80 percent of the function's memory, a probe above 20 s, a plan line outside a gate, a build hash that differs, a forged-forward event that returns data, a staff probe refused for a reason other than the map (for example the staff profile row lacks the firm: report the reason token and STOP; the row is NOT changed inside this order): STOP at once and report to the issuer. The rollback is the packet's section 6 (revert Act 4 first; the prior artifact version `J9krUD0Qw3fz5QdcfYM4CRg7bYlHNigW` through `safe-apply`).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB6-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-323.apply-cottonwood-read-path-forward.md
infra/aws/lambda/ci/function-map/irpt-cot-reporting-read-lambda.json
infra/aws/lambda/ci/function-map/irpt-49f-reporting-read-lambda.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 182 (round 150, workstream COTAPPLY), cell `DB-b-323`.
<owned_cells>DB-b-323</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC189-1-AC1, DBC189-2-AC1, DBC189-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-323.apply-cottonwood-read-path-forward.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC189-1-AC1,DBC189-2-AC1,DBC189-3-AC1` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line is the issuer's, so give yours: the plan lines, the eight probes' statuses and tokens, the identity class, and what is NOT proven. Counts, paths and words only. Tell the issuer at once when Act 6 is done.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the two Terraform roots are the writers of the changed properties; the two plan gates (5/0/0 and 1/1/0) are the blast bound; nothing else is written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the grants are new and explicit (the new role's statements and the one lambda:InvokeFunction statement, listed in the packet and checked by p189) and the issuer read the live role, its policies and the Cottonwood bucket policy.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; p189 re-reads the three routes and their one integration.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CDN or edge cache is touched by the applier; the page reads the live route.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the issuer's checker selftest is green on a synthetic record and red on 51 single-fault arms.
lane: the <paths> block IS the grant.
</preflight>
