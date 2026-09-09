# TO ETFS_GUARDRAIL.TO-EG-s-15 -- THE SEPTEMBER-TO-DATE REFUSAL: the orchestrator's `run` mode taught to honor a `month` override (one line, deployed under NEVER-2), then started by hand for 2026-09 -- a partial month is incomplete by construction, so the refusal ladder runs on real data to its terminal email

<to_id>ETFS_GUARDRAIL.TO-EG-s-15</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- issued in round 2's ONE issuance on PRD v0.4 @`a830ea1cc0` (the manual-trigger addendum on Andrew's ~21:4xZ word), s.9 row S15; decomposition v0.2 s.8-s.11. SECOND on slot ~1, after EG-s-14 is terminal (same orchestrator, one deploy, one queue -- decomposition v0.1.1's rule). EG-s-16 reads this order's run.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.4 (s.9 row S15; s.0 the carve-out; s.7.2 S6/S7/S8 the ladder and the terminal send) | **Decomp cell:** `EG-s-15` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.2, s.8-s.11) | **outcome_ref:** FWD-2, FWD-7, FWD-8 | **verb:** verify (with ONE line of code and its deploy, stated below) | **depends_on:** `EG-s-14`

---

## THE CELL

`EG-s-15` (PRD s.9 S15): no real refusal has ever reached a person -- FWD-2 (the pre-publish gate refuses), FWD-7 (the one terminal SES send) and FWD-8 (the ladder's stop-and-ask) all graded NOT_EVALUATED because every prior proof was a fixture or a send-free rehearsal. A month that is INCOMPLETE BY CONSTRUCTION -- September, run today -- makes the refusal real: the gate (`EG-s-6`) classifies the missing days, the ladder (`EG-s-7`/`EG-sb-7`) runs its rungs and stops, the orchestrator writes the refusal HTML under `refused/`, leaves the 2026-09 publish key ABSENT, produces the alert text, sends the ONE terminal email to andrew@ (the carve-out's send, on a real refusal), writes `coverage_egress_ask.json`, and makes 0 vendor calls.

⛔ **THE ONE LINE, AND WHY IT IS THIS ORDER'S:** the handler's `run` mode renders `_last_month()` unconditionally (`infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:383`), while its QA modes already honor `(event or {}).get("month") or _last_month()` (`:476`, `:507`). The rule's target cannot be run for 2026-09 as deployed. The fix is that same expression at `:383` -- `month = (event or {}).get("month") or _last_month()` -- so the SCHEDULED payload `{"mode":"run"}` behaves exactly as before (no `month` -> last month) and a hand invoke `{"mode":"run","month":"2026-09"}` renders the month named. Same target, the scheduled payload shape plus one field, the OS-s-26 pattern. It is a code change on a served Lambda: deployed through Terraform under `safe-apply` with a NEVER-2 entry (the round-1 EG-s-8 shape: targeted plan, apply, 0-diff, served `CodeSha256` == the built zip), never `update-function-code`. The issuer stated this line to the CTO in the drive read that carried this issuance; it does not widen the row's claim.

⛔ **RULE (2), THE ENTRY, THE SIGN-OFF.** This run writes under the month prefix (`platinum/reports/2026-09/refused/…`, `coverage_verdict.json`, `coverage_unresolved.json`, `coverage_egress_ask.json`) and sends ONE real email; the 2026-09 publish keys are NOT written (that is the point). The CTO called it a real deploy act: the NEVER-2 entry is OPENED FIRST, covering both the one-line deploy and the run, quoting BOTH never-widen halves (the COO's = the hash of the issuance that created this file; the CTO's = the message id GIVEN IN YOUR PROMPT), naming what the run may write and the fact that no publish key is written; the entry + sentinel COMMITTED. Nothing is deleted.

⛔ **THE CARVE-OUT'S WIDTH IS ABSOLUTE (PRD s.0):** ONE SES send, on the terminal failure path, from the same act that writes the refusal, to andrew@ only -- the orchestrator's existing `_send_terminal_unresolved` (EG-s-8). You add no send, no topic, no alarm, no schedule, no env var. **A real refusal on real September data IS the authorized case.**

## DELIVERABLE

1. The one-line change at `:383` (and the arm in `infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py` proving `run` with `month` renders the named month and without it renders `_last_month()`).
2. The ledger entry + sentinel (opened before the plan/apply; the deploy legs and the run legs closed with proof), COMMITTED.
3. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs15_september_refusal.py` -- the refusal battery; `the-september-refusal.result.md` -- criteria verbatim with rc and denominator; the plan summary; the served-vs-built hash pair; the invoke's request id and UTC; every refusal artifact's key, size and UTC; the SES MessageId; the egress read with its denominator; any row filed.
4. The proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** A path you need that it does not name is a BLOCKING row, never an override.
- **YOUR AWS IDENTITY IS THE LAUNCHING SEAT'S** (decomposition s.3 decision 1); every invocation and its output recorded VERBATIM.
- **NEVER-2 / NEVER-9:** Terraform through `.tools/safe-apply.sh` only; `aws lambda update-function-code` is FORBIDDEN; plan read before apply; the TARGETED plan must change EXACTLY `aws_lambda_function.orchestrator` (source hash) -- any other resource in the plan -> do NOT apply, BLOCKING row; 0-diff after.
- **THE TERRAFORM BINARY:** `.tools/terraform.exe` (v1.9.8) is the estate's and it is GITIGNORED, so a fresh worktree lacks it; the issuer provisions a copy into your worktree's `.tools/` at hand-off (confirm `.tools/terraform.exe version` before any plan). NEVER substitute the PATH `terraform` (v1.14.5): a newer CLI re-pins the remote state's `terraform_version`. If the copy is absent, that is a BLOCKING row.
- **NO VENDOR EGRESS BY ANYONE** (ruling card 4, per-use only): rung 3 STOPS and names the dates and the provider; the run's egress read (the gateway's egress log + CloudTrail over the run window) must print 0 with its denominator.
- **NO SERVED SLICE IS TOUCHED.** The daily slices under `daily/<partner>/` are read by the gate, never written by this order; the September publish keys stay absent.
- **EVERY invocation is bounded.** `timeout 120` on reads; poll the refusal artifacts and the box state at most every 60 s for at most 30 minutes.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

## ACCEPTANCE

<criterion id="S15-AC1" cell_refs="EG-s-15"><invocation>python -m pytest infra/aws/lambda/etfs-reports-orchestrator/test_terminal_send.py -q</invocation><expect>passed</expect></criterion>
`S15-AC1` -- the existing battery plus your two arms (`run` with `month` -> that month; `run` without -> `_last_month()`) is green (record N passed, N >= the round-1 count + 2).

<criterion id="S15-AC2" cell_refs="EG-s-15"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false -target=aws_lambda_function.orchestrator</invocation><expect>1 to change</expect></criterion>
`S15-AC2` -- the TARGETED plan changes EXACTLY `aws_lambda_function.orchestrator` (source hash): `0 to add, 1 to change, 0 to destroy`. (`init -input=false` first if `.terraform/` is absent.) Then `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-reports apply -input=false -auto-approve -target=aws_lambda_function.orchestrator`, only after this plan read exactly one resource, under the entry.

<criterion id="S15-AC3" cell_refs="EG-s-15"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/orchestrator_served_vs_built.py</invocation><expect>VERDICT: MATCH</expect></criterion>
`S15-AC3` -- the served `CodeSha256` equals the base64 sha256 of the zip Terraform built (the round-1 script in your deliverables folder; re-run, do not rewrite), read AFTER the apply; a 0-diff targeted plan (`-detailed-exitcode` rc=0) recorded beside it.

<criterion id="S15-AC4" cell_refs="EG-s-15"><invocation>timeout 900 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs15_september_refusal.py</invocation><expect>EGS15-REFUSAL-LADDER-RAN</expect></criterion>
`S15-AC4` -- a battery you write, printing the token ONLY when every arm holds on REAL data: (a) the ledger entry opened BEFORE the plan and BEFORE the invoke, quoting both sign-off ids and naming what the run may write; (b) the invoke on the rule's target with `{"mode":"run","month":"2026-09"}` (request id + UTC recorded; CloudTrail `Invoke` initiator = the launching seat's user, not the scheduler role); (c) after the run: the ladder's rungs in `platinum/reports/2026-09/coverage_unresolved.json` (each rung's output present; rung 3 STOPPED naming the dates and the provider), `coverage_verdict.json` reading REFUSE with the month's classes, the refusal HTML under `platinum/reports/2026-09/refused/` (head-object 200, size, UTC), and the 2026-09 PUBLISH keys ABSENT (head-object 404 on each of `_report_keys("2026-09")`, printed beside the refused object's 200 -- the discriminating pair); (d) the alert text produced (the orchestrator's log line and/or the SNS publish to the existing `etfs-reports-alerts` topic, as already wired -- nothing new); (e) the ONE terminal email: the orchestrator's log shows exactly ONE `send_raw_email` on the terminal branch with `Destinations == ["andrew@opalinvest.com"]` and its SES `MessageId`; CloudTrail `SendRawEmail` count for the run's window == 1 for that branch (the ordinary monthly send does NOT fire on a refusal -- print its count, expected 0); DELIVERY at the inbox is the issuer's read; (f) `coverage_egress_ask.json` written with the dates and the provider named; (g) VENDOR EGRESS 0 over the run window, with the denominator (the gateway's egress log read for the window + CloudTrail for any provider-facing call), printed; (h) the run-id: the request id from (b) appears in the orchestrator's log for every artifact-writing step -- if the artifacts themselves carry no run-id field, PRINT `ARTIFACT-CARRIES-NO-RUN-ID` and file the row; (i) the box `stopped` at the read. Denominators on every list.

<criterion id="S15-AC5" cell_refs="EG-s-15" judgment="true"/>
`S15-AC5` -- graded by the CVO at L9: the ladder on real data rung by rung (what each rung found, what rung 3 named), the refusal's text as a person would read it (dates, partners, providers, no follow-up needed), that the send fired exactly once from the terminal branch and nowhere else, that the one-line change altered nothing on the scheduled path (the `month`-absent arm), and what this order could not see (the inbox). Evidence with vintage. NO VERDICT.

<expected_criteria>S15-AC1, S15-AC2, S15-AC3, S15-AC4, S15-AC5</expected_criteria>

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
The same grant EG-s-8 carried in round 1 (the orchestrator, its Terraform, the CI source map and the deploy recorder, both ledger folders): one file changes by one line; `data/etfs/scripts/` is READ, never edited (the gate and the ladder run as deployed).

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.2, cell `EG-s-15`.
<owned_cells>EG-s-15</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names ETFS_GUARDRAIL, etfs-reports-orchestrator, the reporter box or opal-data-etfs. BLIND SPOT, stated: the gate ledger cannot see a Lambda source change or a real send -- the NEVER-2 entry, the targeted plan and the CloudTrail reads are the controls, named in the accept.
comp-iam: RUN at L5 round 1 on etfs-reports-orchestrator -- 16 calls / 9 statements; `ses:SendRawEmail` GRANTED-BROAD with `ses:FromAddress` pinned (`orchestrator.tf:88-96`); the one-line change needs NO IAM change. Run `comp-iam refresh-census` before any APPLIED-plane read (24 h TTL); the four false-deny modes are live.
comp-adversary: DECLARED-NOT-APPLICABLE -- a verify cell with one line of code; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S15-AC1` .. `S15-AC5`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-15.the-september-refusal.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> S15-AC1,S15-AC2,S15-AC3,S15-AC4,S15-AC5` BEFORE the complete flip, which you commit yourself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row. The issuer hands you `EG-s-16` next by continuing you.
