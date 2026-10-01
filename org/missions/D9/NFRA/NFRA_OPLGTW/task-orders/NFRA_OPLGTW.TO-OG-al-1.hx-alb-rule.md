# NFRA_OPLGTW task order -- `OG-al-1` -- the ALB rule that lets the two headless prefixes reach the gateway

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-al-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~18</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one listener rule, created once; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; an ALB listener rule only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the pattern is the existing ms_ingest_capability rule (infra/aws/terraform/opal-gateway/ms-ingest.tf); the route's own bearer is the gate (PRD v1.3 C7 "Headless content routes").
EGRESS CLASS, declared: NONE beyond Opal's own AWS (ELBv2 via safe-apply) and unauthenticated GETs to the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-al-1` (decomposition addendum R3-T.2)

The gateway's public HTTPS listener (`infra/aws/terraform/opal-gateway/alb.tf`, `aws_lb_listener.https`) signs every
request in through Entra OIDC by default. A machine caller with a static bearer reaches the gateway only through a
listener rule that FORWARDS its exact paths without that sign-in: `/ms/*` uses `aws_lb_listener_rule.ms_ingest_capability`
(priority 31, `ms-ingest.tf`), `/otp/*` and `/graph/*` the same way. The headless routes `/hx/transcripts` and
`/hx/mail` (PRD v1.3 C7; built by `OG-hr-1` and `OG-hr-2`, released by `OG-rl-1`) have no such rule, so today an
unauthenticated request on them is redirected to the sign-in (measured: 302 to `login.microsoftonline.com`).

### PHASE A (no AWS write)

1. Write `infra/aws/terraform/opal-gateway/hx-capability.tf` on the `ms_ingest_capability` pattern: ONE
   `aws_lb_listener_rule` on `aws_lb_listener.https.arn`, ONE `forward` action to `aws_lb_target_group.gw.arn`, ONE
   `path_pattern` condition with exactly `/hx/transcripts/*` and `/hx/mail/*`, and a priority that is unused on the
   live listener (live priorities at the cut: 10, 20, 30, 31, 32, 33, 34; re-read with `aws elbv2 describe-rules` and
   name the one you take, 35 if still free). A header comment states why (the C7 bearer is the gate, as `/ms/*`), and
   the post-apply verify. No other resource. Any name or `Name` tag you give it is `lib/opal_naming.py` `name()`
   output (rule 30); a builder refusal is a BLOCKING row, never a typed name.
2. A TARGETED plan of that one resource, fed as `OG-pr-1` A1 feeds its plan (owner-key variables from the live
   grant-writer Lambda into `TF_VAR_*`, never printed; the grant writer's staged build and the deps-layer zip). It
   must read exactly 1 to add, 0 to change, 0 to destroy.
3. Write `ANNOUNCE_OG-al-1.md` in your deliverables: the file, the priority, the plan reading, and the rollback (remove
   the rule by Terraform; the paths then return to the sign-in). Commit it and report. STOP for the issuer's GO.

### PHASE B (on the issuer's GO)

4. Open the NEVER-2 ledger, slug `nfra-oplgtw-hx-alb-rule`, with `python .tools/deploy_ledger.py open ...` (legs:
   rule, probe). Commit the entry AND its sentinel BEFORE the act.
5. TARGETED `safe-apply` of that one rule, fed as in step 2. The plan must read 1 / 0 / 0, or you do not apply.
6. Run AC2. Close every leg with its proof and commit.

## 2. BOUNDS

1. One listener rule, nothing else: no change to `alb.tf`, `ms-ingest.tf`, the listener's default action, the target
   group, any security group, IAM or the instance. No gateway release.
2. Never print a variable value. Work in the worktree named in your identity line. Never push, merge, rebase, stash,
   `checkout --` or `clean`. REFUSE a criterion you cannot meet as written.
3. Commit with `.tools/safe-commit.sh` under your serial; every `.py` passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/hx-capability.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-hx-alb-rule.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W18-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-al-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/al.AC1.sh; echo "exit=$?"</invocation><expect>(?s)listener rules 1 .*path patterns \['/hx/mail/\*', '/hx/transcripts/\*'\].*action types \['forward'\].*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-al-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/al.AC2.sh; echo "exit=$?"</invocation><expect>(?s)live rules carrying /hx/: 1 .*probe control: status 302, redirects to sign-in True.*probe root: status 302, redirects to sign-in True.*probe mcp: status 401, redirects to sign-in False.*both /hx/ probes refused BY THE APP \(4xx, no sign-in\): True.*sentinel at HEAD=no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: one forward-only rule, exactly the two `/hx/` patterns, nothing else declared.
- `AC2`: APPLIED and EXERCISED: the live listener carries it; both `/hx/` prefixes reach the gateway and are refused
  BY THE APP (4xx; 404 before `OG-rl-1` mounts the routes, 401 after), not by the sign-in; the negative arms: a
  non-`/hx` path and `/` still 302 to the sign-in, `/mcp` is unchanged (401 from the app); NEVER-2 closed.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/NFRA_OPLGTW.TO-OG-al-1.hx-alb-rule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Cut 2026-10-01 ~07:3xZ on the issuer's finding while answering the laptop CTO's order 103564 (relay
  @cca5146909): `OG-rl-1` (ALB untouched by its bounds) would have released `/hx/*` behind the OIDC sign-in, so the
  laptop could not reach it and `rl.AC1.sh` (public URL) could not pass. Negative control run at the cut: `al.AC2.sh`
  reads 0 `/hx/` rules and 302-to-sign-in on all three probes.
- Its own one-cell issuance, round label 10. Slot `~18` after `OG-pr-1` (same Terraform root; never concurrent, C4).
  Edge `OG-al-1` -> `OG-rl-1` PHASE B. Before `OG-rl-1` serves, a forwarded `/hx/*` request reaches the app and gets its
  404 (no route mounted); after, the route's bearer refuses.
- Blast radius for the GO: one listener rule; two path patterns move from the sign-in to the app's bearer.
- `<risk>` WORLD: a public-surface rule.

<status>pending</status>
<status>complete</status>
<round>10</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

## AMENDMENT A1 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~07:3xZ; CTO 27605's four conditions)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). `1.0.0_SA_CTO~O`
confirmed this cell as train Terraform act #2b (after OG-pr-1, before MS-dn-1) on four conditions: exact two patterns,
no catch-all (AC1 already); a priority that shadows no rule, plan 1/0/0 (step 1-2 already); a builder name (A2 of
OG-pr-1's lesson, already in step 1); negative arms after the apply. Condition 4 is encoded AS MEASURED at the cut:
`/` 302s to the sign-in, but `/mcp` answers 401 from the app (its priority-10 forward rule), so the arm is "`/mcp`
unchanged", not "redirects". AC2's expect and `_al.py`/`_al_probe.py` now carry `/` and `/mcp` and require both `/hx/`
probes to be refused by the app.
