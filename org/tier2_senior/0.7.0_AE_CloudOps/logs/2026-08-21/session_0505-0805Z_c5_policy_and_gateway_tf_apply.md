# 0.7.0_AE_CloudOps session log -- 2026-08-21 0505Z -> 0805Z (C5-POLICY phases 1-3 + the opal-gateway TF fix APPLIED)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE
**window:** delta since `session_close_0216-0505Z.md` @dffa4a0dfc. 7 commits.

> **RELAY REQUESTED (Andrew-direct, this window): `0.0.0_AB_MSTR` to carry this to `0.0.0_AB_MSTR~Z`
> and the relevant parties, so the gateway question stops being re-asked.** The short answer for a
> relay reader is in "THE ONE-PARAGRAPH ANSWER" below.

## THE ONE-PARAGRAPH ANSWER (for the relay -- read this if you read nothing else)

**The opal-gateway Terraform user_data path defect is FIXED, APPLIED, AND VERIFIED. It is closed.**
`main.tf:191` created `/opt/m365-mcp-gateway` -- a directory deleted in the 08-15 cutover -- and
`:193` cited a service file that no longer existed. Both corrected, applied through `safe-apply`,
and verified on the box. **The instance was NOT replaced** (in-place, `0 to destroy`); it was
stopped and started, ~100s, and came back on its own because the unit is `enabled`. **Its public IP
changed: `3.83.108.63` -> `13.221.151.249`** (auto-assigned, no EIP) -- if anything anywhere pins
that address, that is the one thing to check. Terraform re-plan is clean. **Nothing is outstanding
and nothing needs deciding.**

## Work completed (newest first)

### opal-gateway Terraform user_data fix -- APPLIED + VERIFIED, ledger CLOSED 4/4
Two Andrew-direct acts drove this, both quoted in the commits: **"fix it now, you have my sovereign
approval"**, then -- after I stopped at the commit to surface a cost he had not been told about --
**apply now and accept the bounce.**

- **Fix @5b5e99fadb.** `:191` `/opt/m365-mcp-gateway` -> `/opt/opal-gateway`; `:193` ->
  `infra/aws/ec2/opal-gateway/deploy/opal-gateway.service`. New citation target verified to EXIST
  (950 B) against a control showing the old path returns "No such file or directory" -- the dangling
  half is closed, not renamed.
- **Why it mattered:** `user_data` runs ONLY ON FIRST BOOT and the 08-15 cutover deliberately did
  NOT replace the instance, so the one block the rename left stale was the one block its own
  execution model could never exercise. Live AWS, the running box and the plan all agreed because
  none of them executes user_data on a running instance. A future REPLACEMENT would have re-created
  the deleted path and re-opened the contested-directory question LD-0428 settled.
- **The replacement risk was LIVE, not a formality.** `lifecycle { ignore_changes = [ami] }` covers
  `ami` ONLY, not `user_data`. A replacement would have DESTROYED a persistent always-on production
  auth gateway and cascade-replaced the ALB target-group attachment. **The plan answered it before
  anything irreversible ran: `0 to add, 1 to change, 0 to destroy`, `~ updated in-place`.**
- **I stopped at the commit and surfaced the cost.** The same plan showed `public_ip`/`public_dns`
  -> `(known after apply)`: an in-place `user_data` modify requires the instance STOPPED, so the
  apply bounces a live auth gateway and changes its IP. Andrew's approval covered FIXING THE
  TERRAFORM; the outage was a cost neither of us knew about until the plan came back. He ruled apply.
- **Applied @ad38fded65** via `safe-apply.sh apply` (Rule 18, `HALT_ACK=1` for a routine pending
  message), rc=0, ~1m40s modify.

### NFRA_EPISTEMY.C5-POLICY -- phases 1, 2 and 3 complete; proof VALID
Activated 0620Z by COO GO 64596 (precondition: C6-KERNEL closed + validated). COO corrected their
own GO within five minutes (64604) -- they had written "no cert, no arch gate", and both stand at TO
:74-75. **I measured that I had not propagated the wider reading: 0 occurrences across both landed
artifacts, against a control of 1 for a phrase I did write.**

- **Phase 1 @f3c40cd923 -- the motivating measurement.** `.owned-paths.yaml` is PRD sec.2.5's law in
  production, and **its two axes sit at opposite ends of it**: WHAT (paths) 250 rules / 74% PREDICATE;
  WHO (principals) 518 entries / 58 lanes / **99.8% ENUMERATION, exactly one pattern (`ANY: *`)**.
  **A newly spawned seat is covered by exactly ONE lane and no other.** That is the conservative
  direction and not a defect; the finding is the ASYMMETRY -- a scope engine modelling only the path
  axis describes the permissive three quarters and misses the axis that gates a new principal.
- **Phase 2 @e5acee14e0 -- objects + battery 10/10.** `Scope_Declaration` carries the WHAT/WHO split
  per CRO's cert-shaping note 64627 rather than one grammar with a mode flag, because the two planes
  FAIL DIFFERENTLY (a predicate over-includes readably; an enumeration under-includes SILENTLY via
  dead members). The engine is **INERT BY CONSTRUCTION, NOT BY CONFIGURATION** -- public surface is
  exactly `evaluate`, and **no constructor flag is accepted** (EXERCISED: 4 flag shapes attempted,
  4 TypeError). **Clause independence DEMONSTRATED** by adopting COO's C6 method: control first, then
  disarming the epoch clause kills exactly m3.
- **Phase 3 @b37cfbe1ad -- read-only snapshot.** `.owned-paths.yaml` opened `'r'`, 0 writes.
  `plane=DESIRED substrate=codebase` -- the DECLARED config, never the applied hook.
- **Proof @c93fccb09c / pins corrected @ed63555d85.** VALID rc=0; **5 PASS, P1+P6+P7 honest FAIL.**
  P6's battery/determinism halves pass but its EMISSION half is PARTIAL (prints the record shape,
  does not emit through the C1 envelope with validation) -- not reported as met.

### The dead-principal finding, and CTO's ruling on it
Phase 3 found **6 dead principals across 3 lanes**. **My first run said 14 and was FALSE-POSITIVE on
two REAL seats** -- the resolver sourced existence from spawn-audit + inbox dirs only, and
`0.1.2_RD_CausalityEngine` / `0.3.3_RD_DataRefresh` have agent folders. Adding folders as a third
source moved the union 128 -> 140 and the count 14 -> 6.

**CTO ruled (64641), verifying the correction at their own seat first, and named the kinds:**
- **MALFORMED (4) = DEAD** -- unsatisfiable BY CONSTRUCTION. CTO's citation, which I did not have:
  `owned-paths-check.sh:37-38` passes the serial **VERBATIM**, no normalisation, so an underscore can
  never match. **KEEP unmarked** as C5's specimen; cleanup after C5.
- **UNSPAWNED (2) = DORMANT** -- not-yet-satisfied; they WILL match the day that seat spawns.
  **KEEP as a declared dormant grant. Do NOT withdraw.** Rule 25: dormant is not a deletion warrant.
  **The POD4 lane description records that exact tilde-lane gap biting FOUR times already** -- a
  cleanup sweep would re-create by tidying the defect the file has been patched for four times.

## Deployment Sequence + Verification (AE role requirement -- ACTUAL output)

```
commit-before-apply   @5b5e99fadb                                    (Deployment Rule 2)
plan                  Plan: 0 to add, 1 to change, 0 to destroy
                      ~ aws_instance.gw will be updated in-place
                      ~ user_data e30a45cb126fbf7f... -> 8b3d8fe1a8ab9556...
apply                 safe-apply.sh apply (Rule 18, never bare), rc=0, ~1m40s modify
applied truth         aws ec2 describe-instance-attribute --attribute userData
                      -> install -d ... /opt/opal-gateway
                      -> infra/aws/ec2/opal-gateway/deploy/opal-gateway.service
0-diff                "No changes. Your infrastructure matches the configuration."  TRUE rc=0 UNPIPED
on-box (SSM)          systemctl is-active   -> active
                      systemctl is-enabled  -> enabled     <- why it came back unattended
                      MainPID cwd           -> /opt/opal-gateway
                      on-box /health        -> 200
                      uptime                -> up 4 minutes
                      /opt/m365-mcp-gateway -> No such file or directory (still absent)
through the ALB       /mcp 401 x3 (auth enforcing, IDENTICAL to the pre-state captured pre-bounce)
                      ALB target i-07dccb1615503ac99:8080 -> healthy
what moved            public IP  3.83.108.63 -> 13.221.151.249
                      LaunchTime -> 2026-08-21T07:58:44Z
                      instance ID UNCHANGED (i-07dccb1615503ac99) -- stopped/started, NOT replaced
ledger                20260821T0755Z_opal-gateway-userdata-path-fix -- OPENED at deploy-start,
                      CLOSED 4/4 in-session @ad38fded65 (NEVER#8 satisfied)
```

**Honest note on that verification:** the post-apply SSM invocation reported `status=Failed`. **That
is MY probe's artifact** -- its last command was `ls` on a deliberately-absent path, which exits
non-zero and fails the whole invocation. Every command's output is correct. Recorded because a
"Failed" status line on a healthy verification is exactly what gets quoted later as an incident.

## MCP traffic
~20 messages, all ACKed. Significant: **Andrew-direct x2 at my terminal** (the fix approval, then
the apply-now ruling) -- recorded + broadcast same turn to COO/CTO/MSTR (64642-64644). COO 64596
(C5 GO) + 64604 (their own GO correction) + the C6 validation; CTO 64641 (DEAD/DORMANT ruling) and
the reframe that not-applying leaves a pending stop/start bundling into the next apply; CRO 64627
(cert-shaping note, sent BEFORE my schema landed so it cost nothing).

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| `terraform plan` (via `.tools/terraform.exe`) | opal-gateway, pre-apply + 0-diff | **PASS** -- pre-apply proved in-place/0-destroy BEFORE anything irreversible; post-apply "No changes", rc=0 unpiped |
| `safe-apply.sh` | `apply -auto-approve`, `HALT_ACK=1` | PASS rc=0 -- **and it refused my first invocation** for omitting the `apply` subcommand, which is the wrapper doing its job |
| `deploy_ledger.py` | open 4 legs at deploy-start, close-leg x4, close | PASS -- opened BEFORE the apply, closed in-session |
| `aws ec2 describe-instance-attribute` / `elbv2 describe-target-health` / SSM | applied-truth + behavioural verification | PASS -- applied user_data read back from AWS, not from my file |
| `commit-gate.sh` | policy_objects.py, exercise_policy.py, phase3_snapshot.py | PASS rc=0 UNPIPED after catching 5 lint defects |
| `proof-of-spec-check.py` | C5 instance, positional P1-P7 | VALID rc=0, rows=7, violations=0 |
| `comp-state --self-test` | drift-instrument gate | **PASS 4/4** ("the instrument discriminates") |

**What worked:** stopping at the commit to surface the outage cost. The plan is what turned "a
two-line doc fix" into "this bounces a live auth gateway and moves its IP" -- and that only surfaced
because the plan was READ rather than piped into an apply.
**What failed:** (1) my Phase-3 resolver's 14-vs-6 false positive, **where my own written caveat
named the exact failure and did not prevent it** -- CTO's framing: declaring a limit documents it, it
does not bound it; (2) a charmap crash from a non-ASCII character in a print path -- **my own
CLAUDE.md Code Quality rule**, and the runtime crash was the only detector; (3) two heredoc escaping
attempts mangled a string literal before I used ruff's own fixer.
**Gap found:** **`commit-gate.sh` does NOT check for non-ASCII.** `py_compile` and ruff will not flag
a string literal. Anyone treating the gate as a non-ASCII guard is mistaken -- worth knowing given
the rule exists precisely because non-ASCII breaks charmap/CloudWatch.

## Files Modified
See commit messages: f3c40cd923, e5acee14e0, b37cfbe1ad, c93fccb09c, ed63555d85, 5b5e99fadb,
ad38fded65. Infra touched: `infra/aws/terraform/opal-gateway/main.tf` (2 lines). New deliverable
tree: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_EPISTEMY.C5-POLICY/`.

## Blockers
None. C5's P1 awaits CRO spec cert then CTO arch gate -- **neither has been requested yet, which is
why P1 reads FAIL; that is a request I initiate, not an approval anyone is withholding.**

## Current State
- **opal-gateway TF: CLOSED.** Config and box agree. `/opt/opal-gateway` is the deploy destination
  (matches `EC2_MANIFEST.json` `remote_path`); `/opt/m365-mcp-gateway` absent on the box AND no
  longer created by user_data. **The fix does NOT take effect on the current instance and never was
  going to** -- user_data is first-boot-only; what it buys is that a FUTURE REBUILD creates the right
  directory. Ledger closed 4/4.
- **⚠ THE ONE THING A RELAY READER SHOULD CHECK: the gateway's public IP changed to
  `13.221.151.249`.** ALB routing targets the instance by ID and survived (verified healthy). Any
  external allowlist, firewall rule, or doc pinning `3.83.108.63` is now stale.
- **C5-POLICY:** phases 1-3 done, proof VALID rc=0 @ed63555d85, 5 PASS / P1+P6+P7 FAIL. Engine
  imported by NOTHING on a live path. **Activation on any real class remains Andrew's worded act.**
- **C6-KERNEL:** COMPLETE @e3c092e472 (prior window), cert + gate + COO validation.
- Watcher live (`brukpg68f`). safe-commit free. 22 + 7 commits this session.

## Next Steps
- [0.0.0_AB_MSTR] **RELAY THIS (Andrew-direct):** carry the gateway close to `0.0.0_AB_MSTR~Z` and
  relevant parties. The one-paragraph answer at the top is the relay payload; **the IP change is the
  actionable half.**
- [0.7.0_AE_CloudOps] wire C5 P6's C1-envelope emission, then REQUEST CRO spec cert -> CTO arch gate.
- [0.7.0_AE_CloudOps] **by 10:30Z:** if no PartnerETL seat is live, take the verify+close leg of
  `COT_SUPERVISED.G4-ACCEPT-HANDOVER` (read-only on cot). Compare sha256, not LastModified.
- [1.0.0_SA_CTO] the DEAD (4) cleanup is a one-line act AFTER C5; the DORMANT (2) stay untouched.
- [0.7.0_AE_CloudOps / any seat] C11 rider: one `bloomberg_historical_data` call with
  `max_data_points=2` at the next Bloomberg terminal login.
