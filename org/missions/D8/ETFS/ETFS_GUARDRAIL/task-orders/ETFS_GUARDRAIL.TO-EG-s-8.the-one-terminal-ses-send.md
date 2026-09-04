# TO ETFS_GUARDRAIL.TO-EG-s-8 -- the ONE terminal SES send: when a gap survives every rung, Andrew receives an urgent, structured message naming each missing date, its partner and its provider -- from the orchestrator's existing send path, on the terminal failure path only, never on a schedule

<to_id>ETFS_GUARDRAIL.TO-EG-s-8</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct 2026-09-02 (PRD s.0 ruling (3), the SES carve-out) and 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S8; s.7.4 the home; s.0 MORATORIUM CARVE-OUT; s.6 ruling 7; s.4 property 8) | **Decomp cell:** `EG-s-8` | **outcome_ref:** FWD-7 | **verb:** wire | **depends_on:** `EG-sb-7` (your previous order)

---

## THE CELL

`EG-s-8` (PRD s.7.2 S8): NEW in `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py` (375 lines at HEAD), *"reusing the existing SES path"*. Bound: *"ONE send, terminal path only. Not a monitor, no schedule, no polling. Fires only when EVERY rung failed."* Property 8: *"When every rung fails, exactly one urgent message reaches andrew@opalinvest.com naming each missing date, its partner, and its provider -- and it does not fire when the ladder resolved the gap."*

**THE CARVE-OUT'S WIDTH, verbatim from PRD s.0, and it is the only thing a reader must not widen:** AUTHORIZED: *"ONE SES send, on the TERMINAL FAILURE PATH ONLY ... emitted by the remediation ladder when the ladder terminates unresolved -- the same act that already writes the refusal."* STILL BANNED: *"a new monitor, a new alarm, a new SNS topic, a standing freshness service, or any send on a SCHEDULE rather than on the terminal failure of the ladder."* Andrew's own words: *"This email must be a last resort, the backfill strategy must be effective enough that it doesnt happen."*

**How the terminal path reaches the orchestrator (the seam `EG-s-6` produces):** the renderer's gate, on a REFUSE verdict after the ladder ran, writes `platinum/reports/<month>/coverage_verdict.json` (always), `platinum/reports/<month>/coverage_unresolved.json` (only when unresolved days remain: `{"month", "unresolved": [{"date","partner","provider","class","reason"}...]}`) and `coverage_egress_ask.json` (rung 3's ask, `EG-sb-7`), and exits NON-ZERO without writing `etf_ownership.pdf` at the publish key. The orchestrator's `_run` already alerts on a non-Success SSM status and on the absent report object (`_alert` -> the EXISTING `REPORTS_SNS_TOPIC`, `lambda_function.py:79-87`). This order adds, INSIDE that existing refusal handling: (1) read the verdict/unresolved/ask objects if present and carry their content into the EXISTING alert's message (the refusal is visible and says why -- property 5); (2) if `coverage_unresolved.json` exists for the month, send ONE `_ses.send_raw_email` from `SES_SENDER` to `Destinations=["andrew@opalinvest.com"]` (andrew@ ONLY; the JOIN list of `EG-s-9` is the monthly report's, not this message's) with Subject `URGENT: ETF month-end <month> -- <n> date(s) unresolved after remediation` and a plain-text body listing each `date | partner | provider | class | reason` plus the egress ask if present -- exactly once, from `_run`'s refusal branch, never from a timer, never from `absence_check`; (3) a SEND-FREE rehearsal mode `terminal_qa` (mirroring the existing `email_qa` pattern at `:349-358`): builds the exact MIME from a given month and returns `{"subject", "to", "body_head"}` with no SES call reachable. No new mode sends. No new topic, alarm, schedule or env var.

**Deploy:** the orchestrator is `archive_file` (inline zip from `lambda_function.py`; NO `build-and-upload` step -- the source map says so). `terraform plan` in `infra/aws/terraform/etfs-reports` shows `aws_lambda_function.orchestrator` changing (the source hash); apply through `safe-apply` under a NEVER-2 ledger entry; 0-diff after; served `CodeSha256` compared to the built zip's base64 sha256 (`data.archive_file.orchestrator` writes `.build/etfs-reports-orchestrator.zip`; hash that file's bytes with sha256 -> base64); `record-terraform-deploy.sh` with `--function etfs-reports-orchestrator --author "0.9.0_WK_ETFS_GUARDRAIL~1 <0.9.0_WK_ETFS_GUARDRAIL~1@opal.agent>"` updates the source map.

## DELIVERABLE

1. The code in `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py` as specified (a function `_send_terminal_unresolved(month, unresolved, ask)` = the third and only new send call site; `_read_coverage_artifacts(month) -> dict`; the refusal branch of `_run` enriched; the `terminal_qa` mode).
2. `infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py` (NOT packaged: `archive_file` zips only `lambda_function.py`) -- boto3 clients stubbed at module level; arms: (a) unresolved present -> exactly ONE `send_raw_email`, `Destinations == ["andrew@opalinvest.com"]`, body names every date/partner/provider; (b) unresolved absent -> ZERO sends and the ordinary alert text unchanged; (c) `terminal_qa` makes no SES call; (d) `absence_check` makes no SES call; (e) the handler's mode table has no new sending mode besides the existing `send_correction`.
3. The ledger entry `etfs-guardrail-eg-s-8-orchestrator-terminal-send` opened with `--lambda etfs-reports-orchestrator` BEFORE the apply and closed with proof after; entry + sentinel COMMITTED.
4. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/the-one-terminal-ses-send.result.md` -- criteria verbatim with rc and denominator; the plan summary; the served-vs-built hash pair; the `terminal_qa` rehearsal output for 2026-08 (send-free).

## ACCEPTANCE

<criterion id="S8-AC1" cell_refs="EG-s-8"><invocation>python -m pytest infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py -q</invocation><expect>passed</expect></criterion>
`S8-AC1` -- the five-arm battery is green (record N passed).

<criterion id="S8-AC2" cell_refs="EG-s-8"><invocation>python -c "import re; s=open('infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py').read(); print('SEND_CALL_SITES=%d NEW_TOPICS=%d' % (len(re.findall(r'send_raw_email\(', s)), len(re.findall(r'create_topic\(', s))))"</invocation><expect>SEND_CALL_SITES=3 NEW_TOPICS=0</expect></criterion>
`S8-AC2` -- exactly three send call sites exist after this order (the two existing plus the terminal one) and the file creates no topic.

<criterion id="S8-AC3" cell_refs="EG-s-8"><invocation>bash .tools/commit-gate.sh infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S8-AC3` -- the commit gate is clean.

<criterion id="S8-AC4" cell_refs="EG-s-8"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false</invocation><expect>1 to change</expect></criterion>
`S8-AC4` -- the plan changes EXACTLY `aws_lambda_function.orchestrator` (source hash): `0 to add, 1 to change, 0 to destroy`. Any other resource in the plan -> do NOT apply, BLOCKING row. (`init -input=false` first if `.terraform/` is absent.)

<criterion id="S8-AC5" cell_refs="EG-s-8"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false -detailed-exitcode; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`S8-AC5` -- 0-diff after the apply (`HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-reports apply -input=false -auto-approve`, run only after AC4 read exactly one resource).

<criterion id="S8-AC6" cell_refs="EG-s-8"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/orchestrator_served_vs_built.py</invocation><expect>VERDICT: MATCH</expect></criterion>
`S8-AC6` -- the served `CodeSha256` (`.tools/aws lambda get-function-configuration --function-name etfs-reports-orchestrator --query CodeSha256 --output text`) equals the base64 sha256 of the zip Terraform built (`infra/aws/terraform/etfs-reports/.build/etfs-reports-orchestrator.zip`); your script prints the two values and the one verdict line.

<criterion id="S8-AC7" cell_refs="EG-s-8"><invocation>.tools/aws lambda invoke --function-name etfs-reports-orchestrator --cli-binary-format raw-in-base64-out --payload "{\"mode\":\"terminal_qa\",\"month\":\"2026-08\"}" /dev/stdout</invocation><expect>"mode": "terminal_qa"</expect></criterion>
`S8-AC7` -- the deployed function's SEND-FREE rehearsal runs live and returns the built message's fields (no email is sent; the `.tools/aws` shim is CLI v1 -- if `--cli-binary-format` is refused as unknown, drop the flag and pass the payload as a plain JSON string; record the exact form that ran).

<criterion id="S8-AC8" cell_refs="EG-s-8" judgment="true"/>
`S8-AC8` -- graded by the CVO at L9: the send fires only from the terminal failure branch, exactly once, to andrew@ only, with dates/partner/provider a person can act on without a follow-up; no schedule, no topic, no alarm, no polling was added; the carve-out's width is not exceeded. FWD-7's EXERCISED grade needs a REAL terminal failure, which by the PRD's own design should almost never happen -- record the rehearsal and say so. RECORD; NO VERDICT.

<expected_criteria>S8-AC1, S8-AC2, S8-AC3, S8-AC4, S8-AC5, S8-AC6, S8-AC7, S8-AC8</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override.
- **THE CARVE-OUT'S WIDTH IS ABSOLUTE:** one send, terminal path, no schedule, no new topic/alarm/monitor/env var. A test send to Andrew's inbox is NOT authorized by this order (his word authorizes the last-resort message, not rehearsals in his inbox); the rehearsal is send-free.
- **NEVER-2 / NEVER-9:** Terraform through `.tools/safe-apply.sh` only; `aws lambda update-function-code` is FORBIDDEN; the ledger entry opened before and closed after; plan read before apply; 0-diff after.
- **`EG-s-9` (JOIN) is your NEXT order, not this one:** leave the four recipient sites (`:158 :189 :221 :277`) exactly as they are.
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
infra/aws/lambda/etfs-reports-orchestrator/
infra/aws/terraform/etfs-reports/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/record-terraform-deploy.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-8`.
<owned_cells>EG-s-8</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or etfs-reports-orchestrator.
comp-iam: RUN at L5 on etfs-reports-orchestrator -- 16 calls / 9 statements; ses:SendRawEmail GRANTED-BROAD (Resource * with ses:FromAddress pinned to *@opalinvest.dev, orchestrator.tf:88-96) at :189 and :277 -- the terminal send needs NO IAM change; sns:Publish on the existing topics already granted.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); the ledger directory and the sentinel are named so the NEVER-2 entry can be COMMITTED.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S8-AC1` .. `S8-AC8`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-8.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> S8-AC1,S8-AC2,S8-AC3,S8-AC4,S8-AC5,S8-AC6,S8-AC7,S8-AC8` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
