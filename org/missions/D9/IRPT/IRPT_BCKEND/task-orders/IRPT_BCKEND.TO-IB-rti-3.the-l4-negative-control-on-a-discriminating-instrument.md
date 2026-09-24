# TO IRPT_BCKEND.TO-IB-rti-3 -- THE L4 NEGATIVE CONTROL ON A DISCRIMINATING INSTRUMENT: ledger leg L4 (`org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md`) is the ONE open leg on the IB-rte-3 deploy ledger and is 0 of 2 exercised. The CTO's round-8 ruling REVISED its instrument: the old host (`i-02448edb624a7a7cf`) is `mdpf-daily-runner`, another project's runner, and a BARE `AccessDenied` from a principal whose own IAM does not grant the action proves only IAM, never the bucket-policy fence. A negative control is DISCRIMINATING only if the SAME attempt could have succeeded were the fence absent.

<to_id>IRPT_BCKEND.TO-IB-rti-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~11</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete -- R93-AC1 PASS-by-output, R93-AC2 non-verdict (no eligible principal, both buckets), R93-AC3 judgment recorded (0.9.0_WK_IRPT_BCKEND~11). Formerly: pending -- HANDED by 2.0.0_SA_COO~B 2026-09-21 ~22:3xZ (round 9, wave 1, chain C, decomp v0.13 s.R9.1). On the CTO's round-8 analysis @8e0f9a127e (msg 99299), his L4 INSTRUMENT RULING, and CVO~B's answer routing (ADJUDICATION_v4.md C-S124 / held question 3). READ-CLASS ACTIONS ONLY: no write of any kind to either bucket. No grant is widened, no host is started, no principal is created.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 9 (wave 1) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rti-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.13, s.R9.1) | **outcome_ref:** FWD-11 (the bucket program) | **Prior context:** `IB-rtf-5` (the original L4 design and its `R62-AC3` non-verdict vocabulary), `IB-rth-7`'s result (L4 UNEXERCISED, host stopped), `IB-rth-8`'s apply (the fence is live, both policies unchanged: sha 2d90b2f1a01bada3 / b095cbbfe6572ae6)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~11`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~11;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-9-11` on branch `wk-irpt_bckend-9-11`, cut from CLOUD HEAD AFTER this order's own commit lands and verifies THIS FILE is present in it before spawning. First act: `cd /c/tmp/wk-irpt-9-11`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-3.the-l4-negative-control-on-a-discriminating-instrument.md` -- absent means STOP and file a row as row `IRPT_BCKEND-W7-S1` did. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing `/c/tmp/wk-irpt-9-11/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~11 <0.9.0_WK_IRPT_BCKEND~11@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Capture `safe-commit.sh` output to a file; ask `git log` whether it committed, never read its prose.
- Python `py -3.12`; AWS via `.tools/aws`. **A raw `aws iam ...` read is rail-GATED and a denial aborts the WHOLE call: use `comp-iam` (`comp-iam live`, `comp-iam service <fn>`) for the census, and where no comp-tool fits the exact read, add the auditable trailing `# rail-checked: <why>` marker in its OWN call.** Use Read/Grep/Glob for files.

## THE CELL

- **(a) THE PRINCIPAL, per bucket, for BOTH `opal-data-inflection` and `opal-data-cottonwood`.** Census the account's IAM for an EXISTING identity that is NOT on the fence's exemption list (`infra/logic/registry/exemptions.json`, 3 of 3 rows per bucket: `Andrew_Berman`, `Andrew_Berman_Console`, `Opal_Terminal`, and not matching the fence's role patterns) and whose IAM ALREADY allows the exact action you will attempt on the exact key pattern. Name it with its ARN AND the policy statement that grants the action. **Print the census denominator** (users and roles examined) and the exemption-list check for every candidate you keep. The identity must be one the seat can act as with what it ALREADY holds -- an `sts:AssumeRole` that the role's EXISTING trust policy already permits for the seat's identity. A role whose trust does not admit the seat is INELIGIBLE; that is not a reason to change trust.
  **AMENDED AFTER HAND-OFF, ~22:3xZ, on the CTO's ruling (msg 99309, relaying `0.7.0_AE_CloudOps~V`'s 22:26Z measurement); the worker was CONTINUED with this text by the issuer because its worktree copy of this face cannot carry it, and THIS paragraph is the record.** (i) `user/Andrew_Berman` and `user/Andrew_Berman_Console` are EXEMPT from BOTH buckets' `DenyForeignFirmPrincipals` (`s3:*`, `ArnNotLike aws:PrincipalArn`) -- a success as an exempt identity proves the EXEMPTION, not that the fence is absent, so they are DISQUALIFIED as the negative-arm principal, as is any role matching the TARGET bucket's own pattern (`role/*-inf-*` on inflection, `role/*-cot-*` on cottonwood). (ii) The exemption list is read from the LIVE bucket policy of each bucket (`get-bucket-policy`, parsed) and the FULL, UNTRUNCATED `ArnNotLike` list is PRINTED per bucket BEFORE any principal is chosen -- not from `exemptions.json` alone (the live policy carries further ARNs, service principals among them; an earlier read of it was truncated and not enumerated). (iii) The discriminating principal is an existing identity NOT on that printed list whose IAM already grants `ListBucket`/`HeadObject` broadly enough to reach the target -- typically a role of a DIFFERENT firm; its granting statement for the exact action is printed beside EVERY attempt. (iv) None such => the non-verdict "cannot discriminate without a new grant", routed to `1.0.0_SA_CTO`. Criteria and expect tokens are UNCHANGED.
- **(b) THE ACTION IS READ-CLASS, on purpose.** Use a read-class action that can succeed on an EMPTY bucket, so a success proves the fence is absent and a denial proves it is present: `s3:ListBucket` on the bucket (both buckets hold 0 keys -- re-measure that at the event) and/or a `HeadObject`/`GetObject` on a key you know does not exist. **NO write-class attempt of any kind, ever, in this cell:** a write that succeeded would put an object in a fenced bucket, and this cell exists to prove the fence, not to test whether it can be breached.
- **(c) POSITIVE ARM.** The SAME principal, the SAME action, on a CONTROL target inside its grant but OUTSIDE the fence (a bucket the fence does not name), must SUCCEED. Print the identity, action and target. This proves the call can succeed at all.
- **(d) NEGATIVE ARM, ATTRIBUTABLE TO THE BUCKET POLICY.** The same action on the fenced bucket is denied, and the denial is attributed to the BUCKET POLICY by S3's own error context (a message naming an explicit deny in a resource-based policy) and/or the CloudTrail record (`errorMessage`, `eventName`, `requestParameters`) -- NEVER by the bare error code. Print, for every attempt, the actual identity, action, bucket/key and the verbatim error. If the attribution signal is not available for this action, say so: an un-attributable denial is NOT a discriminating control.
- **(e) THE HONEST RESULT WHEN NO PRINCIPAL QUALIFIES.** If, for either bucket, no existing principal satisfies (a) with an admissible identity, the cell's result for that bucket is **"L4 cannot be discriminatingly exercised without a new grant."** That is a FINDING routed to `1.0.0_SA_CTO`, recorded with the census denominator and the candidates rejected and why. It is NOT a PASS and it is NOT a reason to create, widen or borrow a grant.
- **(f) THE LEDGER.** Record the outcome on leg L4 in the ledger entry named above (the ledger tool's own verbs; the sentinel under `org/critical_paths/.open_deploys/`). **Close L4 ONLY if both buckets discriminated; otherwise leave it OPEN with the reason recorded.**

## DELIVERABLE
The principal table per bucket (ARN, granting statement, exemption check, census denominator); every attempt printed with identity, action, target and verbatim error; the attribution evidence; the ledger note; the result.md; the proof instance.

## BOUNDS
- **READ-CLASS ACTIONS ONLY. No object written, copied, tagged or deleted in either bucket by anyone. No host started or stopped. No principal created. No policy, trust policy or grant changed.** Assuming a role uses the trust it already has and nothing else.
- Nothing in `infra/logic/registry/`, `s3-lgic-firm-buckets.tf`, `fence_patterns()` or `exemptions.json` is touched (`fence_patterns()` is the CTO's lane; `S116`).
- The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event -- the bucket policy hashes are read at the event, never carried); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W11-S<k>` starting at 1, appended as a NEW fenced JSON block (CRLF, UTF-8, `grounding` AND `disposition` required, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); validate every fence still parses before committing; then keep working. Never edit this face, never widen the order.

<expected_criteria>R93-AC1, R93-AC2, R93-AC3</expected_criteria>
<criterion id="R93-AC1" cell_refs="IB-rti-3"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/battery_ib_rti_3.py --arm principal</invocation><expect>IBR93-PRINCIPAL-TABLE-COMPLETE-2-OF-2</expect></criterion>
**`R93-AC1` -- PASSES BY OUTPUT:** for EACH of the 2 buckets the table is complete: either an eligible principal (ARN, the granting statement, the exemption-list check, the assume route) or "NONE ELIGIBLE" with the rejected candidates and reasons -- and the census denominator printed in both cases. This criterion grades the census, not the outcome.

<criterion id="R93-AC2" cell_refs="IB-rti-3"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/battery_ib_rti_3.py --arm exercise</invocation><expect>IBR93-NEGATIVE-CONTROL-DISCRIMINATES-2-OF-2</expect></criterion>
**`R93-AC2` -- GRADED ON ITS OWN VOCABULARY (the `IB-rtf-5` `R62-AC3` shape):** for BOTH buckets a positive arm succeeded and the negative arm was denied WITH attribution to the bucket policy => the token prints, PASS. A negative arm that SUCCEEDED (the fence is not live) => FAIL and a BLOCKING row. Any bucket with NO eligible principal, or an un-attributable denial => NO token and the instance row carries the schema's non-verdict status (`UNCOMPUTABLE-BY-CONSTRUCTION`, `status_reason` = "L4 cannot be discriminatingly exercised without a new grant" plus the specifics and the owner, `1.0.0_SA_CTO`) -- neither PASS nor FAIL, and never a PASS by relaxing the bar.

<criterion id="R93-AC3" cell_refs="IB-rti-3" judgment="true"/>
**`R93-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED. THE BAR:** State for `3.0.0_SA_CVO~B`. Per bucket, PASS iff the record shows ALL of: the principal's granting statement for the EXACT action and key pattern; a SUCCESSFUL positive arm with the same principal and action on a control target; and a denial whose attribution is an explicit-deny-in-a-resource-policy signal read from S3's error context or the CloudTrail record. FAIL if the attribution rests on the error code alone, or the principal's own IAM would have denied the action anyway. NOT_EVALUATED where the non-verdict branch was taken -- that is the honest outcome and routes to the CTO, not to a grade. No verdict from the worker; every line citation carries `@<commit-ish>`.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rti-3.the-l4-negative-control-on-a-discriminating-instrument.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.13, cell `IB-rti-3` (s.R9.1).
<owned_cells>IB-rti-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: RUN by the assignee as arm (a)'s census -- BLIND until it runs: the issuer measured only that `exemptions.json` carries 3 of 3 rows for each bucket; the number of candidate identities in the account is UNKNOWN at the cut and is printed by arm (a) as its denominator.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R93-AC1, R93-AC2 (may carry the non-verdict status), R93-AC3 (judgment). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~11/IRPT_BCKEND.TO-IB-rti-3.the-l4-negative-control-on-a-discriminating-instrument.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT (commit the battery, output and result BEFORE the instance); a blob pin is written `blob <hash>`; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO~B`. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND `R93-AC1` PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together; `R93-AC2` may carry its non-verdict status without blocking that flip, because a control nobody could honestly run is a fact about the world, not a defect in the cell -- BUT the ledger's L4 then stays OPEN and the finding routes to the CTO.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why, and explicitly per bucket: discriminated, or cannot-discriminate-without-a-new-grant).
