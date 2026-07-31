# 0.7.0_AE_CloudOps~Z (SITE Z lane) -- session close 2026-07-30T2116Z -> 2026-07-31T0215Z

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, IMPLEMENT, COORDINATE

First session of this lane. Site Z (the Bloomberg-terminal box), spawned by `0.0.0_AB_MSTR~Z` on
Andrew's direct word. Work = NFRA_BBGMCP sections 2 (SSM tunnel) and 3/6 (gateway rename).

---

## Current State

**Gate 4 (SSM tunnel) is CLOSED. Gate 2 is unblocked and waiting on ONE human action.**

- `infra/aws/terraform/bloomberg-tunnel/` (new module, state key `bloomberg-tunnel/tfstate`):
  `aws_iam_role.bloomberg_tunnel` (`opal-bloomberg-tunnel-instance-role`, trust `ssm.amazonaws.com`
  + `aws:SourceAccount` confused-deputy condition), `aws_iam_role_policy_attachment.ssm_core`
  (`AmazonSSMManagedInstanceCore`), `aws_ssm_activation.bloomberg_tunnel`.
- **LIVE activation id `3d32065e-401f-453d-a2b9-34e4208c1864`**, name `opal-bloomberg-site-z`,
  `RegistrationLimit=1`, `RegistrationsCount=0`, `Expired=False`, expiry `2026-08-13T23:59:59Z`.
  `Count=0` is CORRECT -- it has enrolled nothing yet and enrolls exactly one machine.
- **WAITING ON ANDREW:** the one-time SSM Agent MSI install (elevated PowerShell, needs `-code` via
  `terraform output -raw activation_code` + `-id 3d32065e-...`). Until it runs there is no `mi-*` id,
  and without that id the caller-side port-forward policy cannot be pinned (it is authored and
  `count`-gated on `var.managed_instance_id`, landing in a SECOND apply).
- **Gateway now self-identifies as `opal-gateway`** on `i-07dccb1615503ac99`
  (`/opt/m365-mcp-gateway/app/tools.py:54`), service restarted `2026-07-31T01:46:21Z`, serving.

**Known open, recorded deliberately, NOT forgotten:**
1. `ssm:GetParameter` + `ssm:GetParameters` on `Resource:"*"` inherited from the managed policy
   (verified against policy version v2) -- the Bloomberg box can read every SSM parameter in the
   account. NOT needed for port-forwarding. Deliberately not patched: stacking an unverified inline
   Deny onto the one-shot admin action reintroduces the half-working-registration risk the policy
   choice exists to avoid. Sequence is prove registration, THEN Deny with a live oracle.
2. `0198a978c` (pip fix) is **GROUNDED-NOT-EXERCISED**. Proving it needs another live-gateway
   restart; MSTR~Z is holding that and has surfaced it to Andrew.
3. `tools.py` differs from the deployed artifact by ONE comment character (my U+26A0 fix). Comment
   only, zero functional difference, manifest correctly records what shipped (`48e1fceaf`).

---

## Work Completed

### Gate 4 -- SSM hybrid activation (NFRA_BBGMCP s2)

Re-measured all five gates rather than inheriting them. Four matched MSTR's reading; **gate 1 did
not** -- the PRD read "in flight" but `sts get-caller-identity` returns
`arn:aws:iam::313476888478:user/Andrew_Berman` rc=0. That single fact is what made gate 4 actionable.

**Two sequencing corrections, both accepted and landed in the PRD by MSTR~Z:**
- **Gate order inverts: 4 before 2.** An activation is created in AWS FIRST and emits code+id; the
  MSI install CONSUMES those. The PRD table (1,2,3,4,5) would have idled Andrew on an admin step
  whose inputs did not exist.
- **Gate 5 must FOLLOW the rename.** Registering the endpoint as a gateway backend first would land
  Bloomberg in the `m365` namespace and pay the client re-registration break TWICE.

**Policy decision -- documented-minimum, measured not assumed.** Attempted the tighter set as
instructed: 7 actions, all names confirmed real via `accessanalyzer validate-policy` (0 findings)
with a NEGATIVE CONTROL in a separate invocation proving the instrument discriminates (bogus action
-> `INVALID_ACTION`); confirmed a strict subset (7 of 25, dropping all 6 `ec2messages:*`).
**The deciding fact was what could NOT be established:** no pre-apply instrument can prove that
subset SUFFICIENT for registration -- `simulate-custom-policy` proves a document grants what it says,
never that an agent registers. Only live registration proves that, and it requires the apply PLUS
the admin install -- so the cost of guessing wrong lands on Andrew's one-shot action. Took MSTR's
hard stop: unverifiable-custom is worse than verified-broad.

Applied on Andrew-direct **"you can apply that, i love it"**. Ledger opened at deploy-start, closed
in-session. Live-plane verified (activation + role + attachment; caller policy correctly ABSENT).

### Gateway rename (NFRA_BBGMCP s3/s6)

**Nearly shipped a fix that fixes nothing.** MSTR caught it pre-deploy; I re-derived it independently
and the corroboration was stronger than the original catch. The `mcp__<prefix>__` segment comes from
the CLIENT'S REGISTRATION KEY, not the server's `FastMCP()` name:

| key | tools | server self-name |
|---|---|---|
| `m365` | `mcp__m365__whoami` | `m365-gateway` -- NO match |
| `opal-agent-comms` | `mcp__opal-agent-comms__*` | **hyphens SURVIVE** |
| `playwright` | `mcp__playwright__*` | |

The `opal-agent-comms` row is the discriminator MSTR's proof lacked: hyphens are demonstrably
preserved, so "`m365-gateway` truncates at the hyphen" -- the only competing explanation -- is dead.

Deployed anyway on Andrew's word, for two HONEST reasons, neither the original: a multi-vendor
gateway should not self-name as one integration, and **the 18-line comment at `tools.py:54` is the
real deliverable** -- the misleading string is what produced the wrong premise, so deleting it
silently would leave the trap.

Measured the real breakage surface myself rather than accept it: **2 full `mcp__m365__` literals
estate-wide**, both `teams-assist/SKILL.md`. `tax-pt1` uses BARE names (`:51`, `:68`) and survives a
key change. Also checked the one thing that could REFUTE MSTR's bare-name plan -- permission
allowlists, which cannot express a bare name: **0 entries** across all three settings files.

### The half-landing (NEVER#6)

`safe-ec2-deploy.sh` returned **rc=1 AFTER its own SSM step printed `OK: deploy Success`**. Code
deployed; manifest did not. Rule 8 makes `EC2_MANIFEST.json` the source of truth, so the stranded leg
left it asserting `c390d1c6a` / `0.2.0_DT` / `2026-07-15` while different code ran.
**A missing record invites a look; a CONFIDENT WRONG one ends the inquiry.**

Repaired in-session with the wrapper's own jq semantics. Two calls made by measurement:
`deployed_commit` records `48e1fceaf` (**what was packaged**), NOT HEAD -- HEAD had moved to
`78872c30c` and recording it would have asserted a deploy that never happened. And because jq
rewrote the whole file (578/631 lines), I deep-compared the parsed JSON: 28 services both sides,
**4 semantic diffs, all 4 intended, ZERO unintended.**

### Root-causing the deploy crash

`e7a11ed9d` removed 7 authored glyphs -- a real violation, **but its commit message asserted a cause
I had inherited rather than grounded, and it was WRONG.** Corrected in `0198a978c`:

1. Re-ran the exact failing call against the **stored** invocation (`ssm:84d7f05d`) -- reproduced
   byte-for-byte, rc=255, positions 434-473.
2. `--output json` ALSO fails -> the crash is at the CLI's **stdout write**, not the format.
   `PYTHONIOENCODING=utf-8` does not help (CLI v2 is a frozen binary).
3. **Bypassed the failing instrument** -- boto3 to read what the CLI could not print: 7782 chars,
   exactly ONE distinct non-ASCII codepoint, **U+2501 x40 at offset 429**, context
   `1.8/1.8 MB 59.3 MB/s`. **It is pip's progress bar, drawn on the REMOTE box.**

### Fabric-wide tooling repairs

- **`b27e756a1`** -- `.tools/aws.cmd` hardcoded a laptop-only pip path; on site Z the Windows-side
  chain was dead, so `comp-tagauthz` returned rc=1 and **NO `default_tags` module was appliable on
  this device.** Invisible because `aws` from bash kept working (different shim).
- **`d543ce681`** -- WARN-first non-ASCII lint in `commit_gate_runner.py`, scoped `infra/**` +
  `.tools/**`, wired into both `.py` and `.sh` paths, running on ALL `.sh` regardless of Rule-16
  scope (scoping it behind `_shell_in_scope` would have excluded the very file that motivated it).

---

## Errors and Corrections -- mine and MSTR's

**A pre-GO log that carries only wins is not evidence, it is marketing.**

**MINE:**
1. **Routed the charmap defect out of lane on an ASSUMED boundary.** Told MSTR it was "outside my
   lane"; the lane is literally "Any AE agent" and the gate then PERMITTED me while refusing them.
   A defect sitting unowned between two agents who each believe the other holds it is worse than one
   nobody has found -- both parties believe it is covered.
2. **My own lint caught ME.** First real run flagged `tools.py:41` -- a U+26A0 I authored AND
   DEPLOYED an hour earlier (`042f96d44`), inside a comment EXPLAINING this exact failure class, in a
   file that runs on AWS. I knew the rule, I was writing about the rule, I broke it in the same
   commit, and no amount of care caught it -- a mechanical check did. **This is the cleanest
   controls-over-care specimen of the session precisely because there is no ambiguity about whether
   the author understood the rule.**
3. **A dry-run of `inbox-watch.sh` ate a live message.** Stream mode `mv`s before it echoes, so ANY
   execution drains the inbox -- diagnostic runs included. Recovered from `read/`, self-reported.
4. **`aws s3 sync` returned rc=0 having downloaded 0 of 55,878 objects** (colons in keys, illegal in
   Windows filenames). I only caught it because I had counted the objects BEFORE syncing -- the
   denominator was the control.
5. Claimed `safe-ec2-deploy.sh` was "missing on site Z" -- I looked in `.tools/`; it lives in
   `infra/aws/ec2/`. Corrected same turn.

**MSTR~Z's (recorded here because I caught them, at their explicit request):**
1. Asserted a correlation as a root cause and authorized a fix on a hypothesis -- in a commit whose
   body quotes CLAUDE.md at length. The tell was available: both scripts were already ASCII-clean,
   so nothing they changed could have emitted position 434-473.
2. Introduced the `ERROR: WARN:` double prefix at `:106` -- mechanical substitution without reading
   what `print_error` already emits. Same error one layer down.

---

## Findings that outlive this session

1. **The MCP tool prefix is the client's REGISTRATION KEY, not the server name.** Hyphen survival
   (`mcp__opal-agent-comms__*`) kills the truncation alternative.
2. **A scanner pointed only at your own files cannot see the failure that arrives in someone else's
   output.** Both scripts were ASCII-clean; the killing character came from pip. The lint ships
   LABELLED as authored-only because of this.
3. **The override exists for a gate that has SPOKEN, not one that is BROKEN.** `rc=1` = no verdict
   produced; overriding a non-verdict skips a check that never ran. Distinct from overriding a
   verdict you disagree with, and current affordances do not distinguish them.
4. **THE HARDENING SELECTED THE FAILURE.** `comp-tagauthz`'s `sh()` resolves the executable
   explicitly *to avoid a silent FileNotFoundError* -- and that is exactly what routed it into the
   dead path, while the naive bare-argv form worked.
5. **A successful deploy that fails its record-keeping leg is indistinguishable from a FAILED deploy
   at rc, and from a CLEAN one at the manifest. Only the live plane separates them.**
6. **A device-specific absolute path in a TRACKED CROSS-DEVICE file cannot fail on the machine where
   it is authored, so it ships looking correct.**
7. **Merge commits inherit repo-default identity.** Site-Z merges land under `0.0.0_AB_MSTR`,
   defeating the `~Z` device-attribution property that is the whole point of the suffix. Mitigated
   per-pull with `git -c user.name=...`; the right altitude is the launcher. **Fabric-wide on this
   device, unfixed.**
8. **`comp-iam`/`comp-tagauthz` aside: `simulate-custom-policy` proves a document grants what it
   says; it cannot prove an agent registers.** Sufficiency is not a pre-apply question.

---

## MCP Traffic

**8 messages** (all `0.0.0_AB_MSTR~Z`; site Z routes to MSTR~Z or Andrew -- no COO here, CTO~Z
pending Andrew). Significant: inbound charter + site-Z structural constraints; inbound URGENT
pre-deploy catch on the registration-key finding; inbound GO on the rename deploy; inbound
Andrew-direct rulings (gateway entitlements-off; apply authorization; this /log order). Outbound:
ACK with the two gate-order corrections, gate-4 delivery, gate-4 closure, the measured
"nobody-is-using-it is false" evidence, deploy closure, lint delivery.

**Andrew-direct rulings recorded VERBATIM this session:** `"you can apply that, i love it"` |
`"nobody is using this mcp anyway, we'll keep entitlements off for this gateway and rename the
gateway anyway so it doesnt matter"` (recorded to
`deliverables/ANDREW_RULING_GATEWAY_ENTITLEMENTS_OFF_RENAME_20260730.md`, broadcast same turn).

---

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `comp-which` | startup A.3 exercise | PASS | Forwarder RAN (produced its own banner) -- the mandatory second half, not `command -v` |
| PATH denominator probe | startup A.3 | PASS | 93 of 95 comp-tools resolve bare |
| `commit-gate.sh` | `tools.py`, `safe-ec2-deploy.sh`, probe | PASS | Also the harness for the new lint's positive/negative controls |
| `safe-commit.sh` | 8 commits | PASS | All under `~Z` author; risk-reflex HOLDs read and cleared |
| `safe-apply.sh` | bloomberg-tunnel | PASS (after 2 correct refusals) | Both refusals fixed AT THE TOOL, never overridden |
| `safe-ec2-deploy.sh` | m365-mcp-gateway | PARTIAL | Deploy landed; wrapper rc=1 on charmap; manifest leg repaired in-session |
| `audit-archive-invoker` | startup A.2 | WARN | 11 findings = device-locality artifact, NOT tampering (see below) |

**What worked:** `safe-apply`'s fail-closed behaviour was correct twice and both times pointed at a
real broken tool rather than a policy problem. `commit-gate` was the ready-made harness for
exercising the new lint both ways.

**What failed:** `safe-ec2-deploy.sh` (charmap, root-caused to pip) and `comp-tagauthz` (dead
`aws.cmd` chain) -- both repaired. `aws s3 sync` silently succeeded at nothing.

**Gap found:** `audit-archive-invoker` (MY owned tool) emits 11 tamper-shaped `INTEGRITY/
NON-APPEND-EDIT` findings on site Z that are pure device-locality -- the committed baseline was minted
on the laptop while the live logs are this device's own, all `.gitignore:68 *.log`. It fails CLOSED
correctly (snapshot WITHHELD, baseline does not advance), so site Z structurally cannot clobber the
laptop's 4.8MB baseline. **The residual danger is that the findings are SHAPED to invite a
"re-baseline here" repair, and that repair is the one action that would destroy the real baseline.**
Not touched; MSTR~Z folded it into RV-0058 F-003 and it awaits CTO's device-keyed archive build.

---

## Blockers

**None of mine are self-inflicted, and none block other agents.**

1. **[ANDREW] SSM Agent MSI install** -- human-reserved (admin, one-time). Activation is live with
   its inputs ready. EVIDENCE: `describe-activations` shows `Count=0`, so nothing has enrolled.
2. **[ANDREW / 0.0.0_AB_MSTR~Z] Verification deploy for `0198a978c`** -- HELD. Proving it needs a
   second live-gateway restart, and "verification alone" is not an authorization I will self-grant.
   MSTR is backing the refusal and has surfaced it. The next deploy someone actually needs IS the
   exercise.

---

## Next Steps

1. **[ANDREW]** Run the MSI install; report the `mi-*` id.
2. **[0.7.0_AE_CloudOps~Z]** On that id: second apply pinning
   `aws_iam_policy.bloomberg_tunnel_caller` (`StartSession` restricted to that instance AND the
   `AWS-StartPortForwardingSession` document -- both ARNs required, the instance alone permits a
   shell -- plus explicit Deny on `SendCommand`/`StartAutomationExecution`).
3. **[0.7.0_AE_CloudOps~Z]** Then, and only then, the `ssm:GetParameter*` Deny, with registration
   proven and a live oracle available.
4. **[0.7.0_AE_CloudOps~Z]** Then gate 5 (register the forwarded endpoint as a gateway backend) --
   AFTER the rename, per correction 2.
5. **[0.0.0_AB_MSTR~Z]** Client key `m365` -> `opal` on this device + `teams-assist` literals to BARE
   names. Verified support: 0 permission-allowlist entries encode the prefix.
6. **[1.0.0_SA_CTO / whoever owns the launcher]** Merge-commit identity on site Z (finding 7).
7. **[UNASSIGNED]** `validate_ssavail_attachment` appears **0 times** in Alyssa's 895 gateway calls
   while `save_email_attachment_to_site` has 18 -- `tax-pt1` calls SSAVAIL validation the principal
   automation aspect. Either the tripwire is not running or it runs outside the gateway. Also
   `poll_addressed_teams_messages`: 509 calls, STOPS 2026-07-04 -- a polling loop that died.

---

## Evidence index

`12920f0a4` gate-4 TF | `39d38bdd2` gate-4 ledger | `042f96d44` rename + the key-vs-name comment |
`48e1fceaf` deploy ledger | `b80818749` deploy close + manifest repair | `e7a11ed9d` authored glyphs |
`0198a978c` pip root cause (GROUNDED-NOT-EXERCISED) | `b27e756a1` aws.cmd portability |
`d543ce681` lint gate + self-caught U+26A0.
Ledgers: `org/critical_paths/change_management/20260730T2220Z_bloomberg-tunnel-ssm-activation_deploy_completion.md`,
`20260731T0145Z_gateway-rename-opal-gateway_deploy_completion.md` (both CLOSED).
Gateway usage evidence: Athena `opal_mcp.mcp_audit` over `s3://opal-mcp-audit/` -- 55,878 records,
andrew 54,976 / alyssa 895, both through 2026-07-30.
