# NFRA_OPLGTW task order -- `OG-rz-2` -- APPLY: resize the gateway host `i-07dccb1615503ac99` from `t4g.small` to `t4g.large`, then release the raised memory limits (round 46; Andrew-direct ~18:3xZ 2026-10-19, "lets raise it to large"; STAGED, Phase A now, Phase B on the issuer's GO in an off-hours window)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rz-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rz-2</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or cadence is added or changed; you still run `comp-schedule --drift` at each phase and record what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: `ec2:StopInstances`, `ec2:StartInstances`, `ec2:ModifyInstanceAttribute` and `ec2:DescribeInstances` on `i-07dccb1615503ac99` are the actions `safe-apply` of `infra/aws/terraform/opal-gateway` makes for an in-place `instance_type` change; you simulate them in Phase A as the identity that will apply and record allowed/implicitDeny. An implicitDeny is a STOP and a BLOCKING row. No IAM resource changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew-direct ~18:3xZ (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_183xZ_GATEWAY_EC2_RESIZE_TO_T4G_LARGE.md` @439343a969: "lets raise it to large") and `0.0.0_AB_MSTR~Z` msg 36070 ("we need to get it up to a larger EC2 because it's choking on large requests on small"); the 2026-10-19 hang read `MemoryCurrent` 1.28 GB against `MemoryHigh` 1.26 GB on the 2 GiB host.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-rz-2` (decomposition addendum R3-T.123 amendment A5, round 46, workstream ENRICH-R46-E)

**METHOD = `OG-cd-3`'s (a Terraform apply through `safe-apply`, targeted, with its own never-widen ask and three halves) for the instance change, then `OG-ap-50`'s (one batched release, ledger, read-back) for the limits;** read both orders and their amendments and follow them step by step; this order states only what differs. The hard-guard rule, the live-ref re-read on the host, the ledger with entry AND sentinel first, and the host md5 walk all apply as they did there.

**Two acts, in THIS order, in one ledger `nfra-oplgtw-gateway-resize-t4g-large` (legs `instance`, `release`, `read-back`):**
1. **`instance`:** `infra/aws/terraform/opal-gateway/main.tf` line 172, `instance_type = "t4g.small"` becomes `"t4g.large"`; apply through `safe-apply`, TARGETED at `aws_instance.gw` (the plan must read `1 to change, 0 to add, 0 to destroy`, an in-place update: the instance stops and starts; **a plan that replaces the instance is a STOP and a BLOCKING row**). Andrew's word confirms the stop/start.
2. **`release`:** only AFTER the host reads `running`, `/health` 200 and the marker unchanged on the new size, ONE code release carrying the worker commit of `OG-rz-1` (three files: `deploy/opal-gateway.service` with `MemoryHigh=5600M` and `MemoryMax=6400M`, `tests/test_og_un1.py`, `deploy/NFRA_OPLGTW_CONTRACT.json` with `target_instance_type` `t4g.large`), cut on the live ref and deployed through `infra/aws/ec2/safe-ec2-deploy.sh` under the stale-base guard. **The limits MUST NOT be released before the resize:** `MemoryMax=6400M` on a 2 GiB host would invite the kernel OOM killer.

**AMENDMENT A1 (issuer, 2026-10-19 ~20:2xZ; CTO ruling (B) msg 36104): the release is BATCHED.** `rel-nfra-oplgtw-batch15` carries TWO worker commits whole: `OG-rz-1` (commit `5807068e367`, drained as `97ec4f8c60a`: the unit limits, `test_og_un1`, the deploy contract's `t4g.large`) AND `OG-ms-1` (worker `~165`: registers Schwab master `08403355` in `app/data_entitlement.py` `MASTERS`, `app/schwab_audit.py` `_MASTERS` and both contract copies, plus `tests/test_og_ms1.py`; I send its hash when it drains). **DO NOT cut batch15 until I send the `OG-ms-1` hash**; steps 3-4 stand as done. The ask names the master registration plainly: `08403355` becomes a legal master for a grant (no grant names it in this order), the `data_entitlement` constant is read at import (state the `process-wide state` line for it), and the reader IAM prefixes for `08403355` (`schwab_reader_iam.tf` lines 72-78) are read LIVE in Phase A (`simulate-principal-policy` on `gateway-schwab-read-role` for `s3:GetObject` and `s3:ListBucket` on one `schwab/08403355/silver/dim_balance/` key and the `meta/complete/` prefix: allowed or implicitDeny; an implicitDeny is reported to me, not fixed by you). The Alyssa grant write that gives her the master is a LATER order (`OG-ms-2`) after this release is live.

### PHASE A -- read, plan, measure, ask. NO apply, NO deploy, NO restart (start on the issuer's GO for Phase A)

3. **Before-record** `W/RZ2_BEFORE.json`: the instance (id, `instance_type` as `describe-instances` reads it, state, availability zone), whether an Elastic IP is attached (`describe-addresses`) and **whether the public IPv4 will CHANGE on stop/start** (it does unless an EIP is attached; print the answer, never the address), the target group health, `NRestarts`, the unit's live limits, host memory total (MB), the live ref and marker. Then **the public-IP residual:** read what in Opal's own estate names the gateway's public egress address (security groups, WAF, Terraform, the runbooks; `comp-find` for the denominator) and write the count and the surfaces by name; a VENDOR-SIDE allowlist (a vendor that admits only a listed source address) cannot be read from here: say so as NOT CLAIMED in the ask.
4. **The plan** `W/RZ2_PLAN.json` from `safe-apply`'s targeted plan: `{"add", "change", "destroy", "replace": false}` and the changed attribute named (`instance_type`). Also record the plan's stated downtime behaviour (stop/start) and the expected downtime (measure the last stop/start of any seat's box if you know it, else say unknown).
5. **The release cut:** branch `rel-nfra-oplgtw-batch15` on the LIVE ref read on the host, taking the three files of the worker commit whole; run the window tests as `OG-ap-50` did (`test_og_un1` included; the carried-red set must equal the live ref's); host measurements are read-only here.
6. **The ask** `W/NEVER_WIDEN_ASK_OG-rz-2.md` for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word. It carries: the downtime (the gateway is DOWN for every user during the stop/start; the other boxes and sessions must be told the window), the public-IP finding and its vendor-side residual, **the rollback in the SAFE order** (redeploy the live ref's tarball FIRST so the limits return to 1200M/1400M, THEN apply `t4g.small`; the reverse order would put `MemoryMax=6400M` on a 2 GiB host), the process-wide-state line (CVO verdict 35844: `process-wide state this change touches: <list>, or none, read`), and the window you propose.

Run AC1, commit, REPORT, STOP.

### PHASE B -- only on the issuer's GO, which names all three halves signed and the WINDOW

7. Open the ledger (entry AND sentinel); re-read the live ref, the unit's limits, target health and host md5; any change since Phase A re-cuts Phase A once. Tell `0.0.0_AB_MSTR~Z` (the one message names the window) before the stop.
8. `instance` leg: `safe-apply` targeted; read `describe-instances` until `running` and the target group healthy; record the downtime in seconds (first failed health read to first 200).
9. `release` leg: deploy `rel-nfra-oplgtw-batch15` through the wrapper (the service restarts once); read back against the ask's triggers.
10. **Read-back, 30 minutes, UNARMED ONLY:** `/health` 200; marker equals the release sha; host memory total reads at least 7,000 MB; the unit's live `MemoryHigh` 5600M and `MemoryMax` 6400M; `tools/list` 103; the 27-tool read passes 27 of 27 under the hard guard; `NRestarts` 0 after the deploy's own restart; **the large-reply test, ONE call at a time, never concurrent:** `mdpf_get_aggregate_aua` (about 743 KB) and `opal_discover` (about 585 KB) each complete, with the service's `MemoryCurrent` before and after each recorded as counts, and the peak below `MemoryHigh`; the journal `POST /mcp` count and the audit-lake count for ONE window (`OG-ap-50`'s dual count; journal 0 against a non-zero lake does not grade); `audit_failure_counter` 0.
11. Write `W/RZ2_SERVED.json` with the fields the check reads (below), close the ledger, run AC2, and report the CLOSED time and the final live sha to `2.0.0_SA_COO~O`, `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z` in one message. The landing on the sitez lineage is a separate order.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`.

## 2. BOUNDS

- ONE instance-type change on ONE instance, ONE release of three files; no IAM, SG, ALB, listener, EIP or other Terraform change; no env key; no `HALT_OVERRIDE`; no arming and no SSM parameter write.
- No tid, oid, e-mail, account id, ARN, account number or public IP address in any repo file, row or report: counts, hashes and statuses only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; a delete action; override a gate. A plan that replaces or destroys anything is a STOP.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/main.tf
infra/aws/terraform/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-resize-t4g-large.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rz-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/rz2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)before-record: instance, type, state, EIP answer, public-IP-changes answer, target health, limits, memory total: yes.*plan: change 1 add 0 destroy 0 replace False attribute instance_type: yes.*ask: three halves yes; process-wide state line yes; downtime and safe rollback order named yes; public IPv4 addresses 0 \(want 0\); runs of 9\+ digits 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rz-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/rz2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)status CLOSED=yes; sentinel at HEAD=no.*live instance type t4g\.large state running: yes.*health 200: yes; marker equals the release: yes; unit limits 5600M and 6400M: yes; memory total >= 7000 MB: yes; tools/list 103: yes; 27 of 27: yes; NRestarts after the deploy 0: yes.*large replies one at a time: 2 of 2 complete, peak below MemoryHigh: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the before-record names the instance, its EIP and public-IP answers, the plan changes one attribute in place, and the ask carries the downtime, the safe rollback order, the public-IP residual and the three halves.
- `AC2`: the live instance is `t4g.large` and running; the service answers with the raised limits, 103 tools and 27 of 27; the two large replies complete one at a time under `MemoryHigh`.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rz-2.round-46-resize-the-gateway-host-to-t4g-large.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE `<status>` tag to `complete` only if AC1 and AC2 PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, a mid-round cell on Andrew-direct via the CTO and `0.0.0_AB_MSTR~Z` (msg 36070), amendment A5 of R3-T.123. Two cells: the worker's code (`OG-rz-1`) and this applier cell; STAGED because the resize is off-hours and after Alyssa's 19:00Z session (the CTO's routing).
- The order of the acts is the safety property: the new limits only after the resize; the rollback the other way round.
- Pre-cut: `rz2.AC1` and `rz2.AC2` base FAIL as expected (records absent; the live type reads `t4g.small`).
- Z-S420 (the CRO's row on the outage) is disarmed by this issuer when the `read-back` leg shows the two large replies complete under the limit.

<status>staged</status>
- A1 (issuer, 2026-10-19 ~20:2xZ): the release is batched with `OG-ms-1` (master `08403355`), CTO ruling (B) msg 36104; step 5 waits for its hash; the ask carries the master registration and the live reader-role read. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>46</round>
<workstream>ENRICH-R46-E</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
