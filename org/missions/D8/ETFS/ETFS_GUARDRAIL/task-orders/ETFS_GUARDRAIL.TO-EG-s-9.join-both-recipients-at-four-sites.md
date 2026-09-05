# TO ETFS_GUARDRAIL.TO-EG-s-9 -- Andrew AND AJ both receive the monthly report: JOIN, not replace, as a TYPE decision at FOUR sites across TWO paired send paths -- header keeps the joined string, envelope takes a list -- plus the variable, verified as delivery-capable

<to_id>ETFS_GUARDRAIL.TO-EG-s-9</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- proof-of-spec instance `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-9.join-both-recipients-at-four-sites.proof_of_spec.json` VALID (rc=0). All 8 criteria PASS by output (S9-AC2 amended by the issuer's ruling on row W1-S9 to HEADER_SITES=3; the JOIN variable applied BY TARGET across two applies -- the second for the email_qa To-header addition, its own ledger sequencing gap surfaced and remediated same-turn on row W1-S10 -- served CodeSha256 MATCHES the built zip; both live rehearsals confirm the join and the terminal path's isolation). Rows W1-S9 and W1-S10 filed, both dispositioned by this order's own remediation/the issuer's ruling. Flip made by the assignee per the tree-convention grant. LAST ORDER OF THE ROUND. Prior: pending -- GO paired at cut (the spawn IS the GO); HANDED to the slot only after EG-s-13's proof instance is VALID at HEAD (PRD ruling 5: alignment gates the automated send). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct 2026-09-01 ruling card 3 (JOIN) and 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S9; s.7.3 and s.7.3a; s.0 rulings table card 3; s.6 ruling 3; s.4 property 7) | **Decomp cell:** `EG-s-9` | **outcome_ref:** FWD-5 | **verb:** wire | **depends_on:** `EG-s-13` (slot 3; the COO hands this order only after it merges), `EG-s-8` (your previous order; same file, same deploy)

---

## THE CELL

`EG-s-9` (PRD s.7.2 S9): `infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:49,158,189,221,277`, claim MEASURED by the CTO. Bound: *"A VARIABLE-ONLY CHANGE CANNOT DELIVER FWD-5 -- see 7.3"*. Ruling card 3, an OVERRIDE not an approval: *"ALso I want to be on the email as well as aj@opalinvest.com should be him and me at andrew@opalinvest.com"* -- JOIN, both addresses. Ruling 3 (s.6): *"a comma-separated variable so a future recipient is a variable change, not a code change."* Property 7: *"Both aj@ and andrew@ receive a real send, verified as delivery, not as a successful API call -- a comma-joined recipient string can be accepted and mis-delivered, and that failure is silent."*

**s.7.3a, the four sites and the two shapes (verbatim from the PRD, re-read at HEAD by the issuer):**

```
  _build_report_email      (145-183)   :158  msg["To"] = EMAIL_RECIPIENT        HEADER   (RFC 5322: a comma-joined STRING)
  _email_report            (186-190)   :189  Destinations=[EMAIL_RECIPIENT]     ENVELOPE (SMTP: a LIST of addresses)
  _build_correction_email  (213-270)   :221  msg["To"] = EMAIL_RECIPIENT        HEADER
  _send_correction_email   (273-278)   :277  Destinations=[EMAIL_RECIPIENT]     ENVELOPE
```
*"ONE VARIABLE CANNOT BE BOTH. The obvious fix -- make EMAIL_RECIPIENT a list, or .split(",") it at :49 -- repairs :189/:277 and SILENTLY DAMAGES :158/:221."* So: keep `EMAIL_RECIPIENT` the joined string from the environment; derive `EMAIL_RECIPIENTS = [a.strip() for a in EMAIL_RECIPIENT.split(",") if a.strip()]` once at module level; the two headers take `", ".join(EMAIL_RECIPIENTS)` (or the raw string, which is already a valid header); the two envelopes take `Destinations=EMAIL_RECIPIENTS`. The cosmetic sites `:325` (failure-alert text) and `:373` (handler return) may print the joined string; `EG-s-8`'s terminal send stays `Destinations=["andrew@opalinvest.com"]` and is NOT joined (property 8 names andrew@ alone). The variable: `EMAIL_RECIPIENT = "aj@opalinvest.com,andrew@opalinvest.com"` in `infra/aws/terraform/etfs-reports/orchestrator.tf` (the environment block, currently `"andrew@opalinvest.com"`) -- one line, the ONLY Terraform change besides the code hash.

**Delivery-capability, the silent-failure half (brief s.6 prerequisite):** the SENDER identity is `noreply@opalinvest.dev` (a verified domain identity, pinned by IAM condition). A send to `aj@opalinvest.com` fails at delivery, after the render succeeded, only if the SES account is SANDBOXED (recipients then must be verified). Read the account's production-access state BEFORE the deploy; if sandboxed, that is a BLOCKING row (a person verifies the identity or requests production access -- not you).

## DELIVERABLE

1. The code: the four sites and the module-level list, as specified; both send-path docstrings updated from *"to Andrew"* to the recipients (descriptive drift the PRD names).
2. `infra/aws/lambda/etfs-reports-orchestrator/test_recipients_join.py` (not packaged) -- SES stubbed; arms: (a) env `aj@opalinvest.com,andrew@opalinvest.com` -> BOTH build paths set `To` to a string containing both addresses, and BOTH send paths pass `Destinations` as a 2-element list in that order; (b) env with one address -> a 1-element list, header unchanged in meaning; (c) whitespace around commas tolerated; (d) `EG-s-8`'s terminal send still targets `["andrew@opalinvest.com"]` alone; (e) `email_qa` returns the attachment names with no SES call (the existing rehearsal still send-free).
3. The Terraform variable change; plan; apply through `safe-apply` under the ledger entry `etfs-guardrail-eg-s-9-orchestrator-join-recipients` (`--lambda etfs-reports-orchestrator`); 0-diff; served config read; `record-terraform-deploy.sh --function etfs-reports-orchestrator --author "0.9.0_WK_ETFS_GUARDRAIL~1 <0.9.0_WK_ETFS_GUARDRAIL~1@opal.agent>"`; entry + sentinel COMMITTED.
4. `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/join-both-recipients-at-four-sites.result.md` -- criteria verbatim with rc and denominator; the live `email_qa` rehearsal output for 2026-08 showing the To header (send-free).

## ACCEPTANCE

<criterion id="S9-AC1" cell_refs="EG-s-9"><invocation>python -m pytest infra/aws/lambda/etfs-reports-orchestrator/test_recipients_join.py -q</invocation><expect>passed</expect></criterion>
`S9-AC1` -- the five-arm battery is green (record N passed).

<criterion id="S9-AC2" cell_refs="EG-s-9"><invocation>python -c "import re; s=open('infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py').read(); print('ENVELOPE_LIST_SITES=%d HEADER_SITES=%d SINGLE_ELEMENT_ENVELOPES=%d' % (len(re.findall(r'Destinations=EMAIL_RECIPIENTS', s)), len(re.findall(r'msg\[\"To\"\]\s*=', s)), len(re.findall(r'Destinations=\[EMAIL_RECIPIENT\]', s))))"</invocation><expect>ENVELOPE_LIST_SITES=2 HEADER_SITES=3 SINGLE_ELEMENT_ENVELOPES=0</expect></criterion>
`S9-AC2` -- both report/correction envelopes take the list, the one-element-list shape is gone, and THREE `msg["To"]` header sites exist: the two of the PRD's four-site table plus the terminal email's from `EG-s-8` (`_build_terminal_email`, andrew@ alone, which arm (d) proves at the envelope). AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W1-S9: the cut's `HEADER_SITES=2` predated EG-s-8's third header site in the same file, so a CORRECT implementation of this order's own BOUNDS necessarily reads 3; the census counts sites, the four-site fix is the two envelopes and the two report/correction headers, and the terminal header is left as EG-s-8 shipped it.

<criterion id="S9-AC3" cell_refs="EG-s-9"><invocation>.tools/aws sesv2 get-account --query ProductionAccessEnabled --output text</invocation><expect>True</expect></criterion>
`S9-AC3` -- the SES account is OUT of the sandbox, so an unverified recipient does not fail silently at delivery (if the shim's CLI v1 lacks `sesv2`, use `.tools/aws ses get-account-sending-enabled` and `.tools/aws ses get-send-quota` and record what they say; a sandbox is a BLOCKING row before the deploy).

<criterion id="S9-AC4" cell_refs="EG-s-9"><invocation>bash .tools/commit-gate.sh infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py infra/aws/lambda/etfs-reports-orchestrator/test_recipients_join.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S9-AC4` -- the commit gate is clean.

<criterion id="S9-AC5" cell_refs="EG-s-9"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false -target=aws_lambda_function.orchestrator</invocation><expect>1 to change</expect></criterion>
`S9-AC5` -- the TARGETED plan changes EXACTLY `aws_lambda_function.orchestrator` (code hash + the one environment variable): `0 to add, 1 to change, 0 to destroy`. Anything else in the targeted plan -> do NOT apply, BLOCKING row. (AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W1-S7: the `aws_instance.reporter` `user_data` 'drift' rows W1-S7 and W1-S8 saw was a FALSE drift, corrected by the issuer on row ETFS_GUARDRAIL-S2: the live instance's user_data (sha1 e47b615c) is byte-identical to the LF rendering of `instance.tf` at HEAD, and the plan's 'new' hash 434774b5 is the CRLF rendering of the same heredoc -- a fresh worktree on this `core.autocrlf=true` box checks every `.tf` out with CRLF (no `*.tf` eol rule in `.gitattributes`), and Terraform hashes what it reads; the July commit @`1502fdd6f9` concerns `ami` and the public IP, not `user_data`. The issuer normalizes every `.tf` in your worktree to LF at hand-off (confirm: `file infra/aws/terraform/etfs-reports/instance.tf` reads `ASCII text` with no CRLF), after which the instance shows NO change in any plan. The by-target form stays as a precaution, and a `user_data` change on `aws_instance` remains a confirm-with-Andrew act if one ever appears for real; plan, apply and the 0-diff read BY TARGET to `aws_lambda_function.orchestrator` -- `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-reports apply -input=false -auto-approve -target=aws_lambda_function.orchestrator` -- state the target in the ledger entry, record the full untargeted plan's summary and its `aws_instance.reporter` line verbatim in the result.)

<criterion id="S9-AC6" cell_refs="EG-s-9"><invocation>.tools/aws lambda get-function-configuration --function-name etfs-reports-orchestrator --query Environment.Variables.EMAIL_RECIPIENT --output text</invocation><expect>aj@opalinvest.com,andrew@opalinvest.com</expect></criterion>
`S9-AC6` -- the APPLIED plane carries the joined variable (read after `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-reports apply -input=false -auto-approve` and a 0-diff plan, both recorded).

<criterion id="S9-AC7" cell_refs="EG-s-9"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/orchestrator_served_vs_built.py</invocation><expect>VERDICT: MATCH</expect></criterion>
`S9-AC7` -- served `CodeSha256` equals the built zip's base64 sha256 (the script from `EG-s-8`, re-run against the new build).

<criterion id="S9-AC8" cell_refs="EG-s-9" judgment="true"/>
`S9-AC8` -- graded by the CVO at L9: JOIN not replace at all four sites; Andrew is never dropped; the variable is the carrier for a future recipient; FWD-5's EXERCISED grade ("both people have actually received one") is the scheduled `etfs-reports-monthly-run` fire (`cron(0 10 1 * ? *)` America/New_York) read as DELIVERY at both inboxes -- this order does NOT send a report to AJ ahead of it (an outward-facing act on a report the alignment has only just landed). RECORD the `email_qa` rehearsal's To header; NO VERDICT.

<expected_criteria>S9-AC1, S9-AC2, S9-AC3, S9-AC4, S9-AC5, S9-AC6, S9-AC7, S9-AC8</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a BLOCKING row, never an override.
- **NO LIVE SEND OF ANY KIND in this order.** The rehearsal `email_qa` is send-free by construction; do not invoke `run` or `send_correction`.
- **NEVER-2 / NEVER-9:** Terraform through `.tools/safe-apply.sh` only; ledger before/after; plan read before apply; 0-diff after; `aws lambda update-function-code` FORBIDDEN.
- **Leave `EG-s-8`'s terminal send andrew@-only.**
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>`.
- **THE TERRAFORM BINARY (AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W1-S6):** `.tools/terraform.exe` (v1.9.8) is the estate's terraform and it is GITIGNORED, so a fresh worktree lacks it; the issuer provisions a copy into your worktree's `.tools/` at hand-off (confirm `.tools/terraform.exe version` before any plan). NEVER substitute the PATH `terraform` (v1.14.5) for an apply: a newer CLI re-pins the remote state's `terraform_version` and the estate's binary can no longer read that state. If the copy is absent, that is a BLOCKING row, not a substitution.
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
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-9`.
<owned_cells>EG-s-9</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or etfs-reports-orchestrator.
comp-iam: RUN at L5 on etfs-reports-orchestrator -- 16 calls / 9 statements; ses:SendRawEmail GRANTED-BROAD with ses:FromAddress pinned to *@opalinvest.dev (orchestrator.tf:88-96) -- a recipient change needs NO IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); the ledger directory and the sentinel are named so the NEVER-2 entry can be COMMITTED.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S9-AC1` .. `S9-AC8`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-9.join-both-recipients-at-four-sites.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S9-AC1,S9-AC2,S9-AC3,S9-AC4,S9-AC5,S9-AC6,S9-AC7,S9-AC8` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
