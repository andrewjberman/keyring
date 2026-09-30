# /self-drive NFRA four -- ticks 38-41: Andrew's "agreed", the opal-gateway overwrite, Plan A ruled (1.0.0_SA_CTO~O, site Z, 2026-09-30 13:4xZ-15:2xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4
- **Previous log:** tick 37 @f4f178afe9.

## Andrew-direct and records

- **~14:3xZ "agreed" (@29bc46d827):**
  - laptop push YES, which landed on origin 410818259a;
  - ONE new Schwab grant to Alyssa: masters 08242234 and 08335338, and the four dims.
  - No existing Schwab grant existed (msg 27184), so his earlier "sure" had no object until he named the person.
- **Laptop-side answers to this seat's asks:**
  - X11 and X12 are in the register @3ddc6b3519;
  - naming-gate `r20_exception` kind @cb4296f508.
  - Both are on origin, but the site-Z pull-merge waits on Andrew's word (MSTR~Z is asking, msg 27220).
- **Andrew's question on G-ACCT step 5** was answered from
  `deliverables/2.0.0_SA_COO~O/HANDOFF_G-ACCT_ELEVATED_20260928.md` step 5: `claude setup-token` on the dedicated
  Analyst account, then `CLAUDE_CODE_OAUTH_TOKEN` as Opal_Agent's user env var.

## The opal-gateway overwrite (incident)

- **14:36:48Z:** 2.0.0_SA_COO~RV deployed its signed 4ce7946426 (ETFS_RIVALS).
- **14:41:23Z:** MX-r-6's worker deployed 2e2254156e, cut on 288fa78c93, under halves this seat signed @16998169d5 with
  3.0.0_SA_CVO~O. The GO's base guard had been read about 40 minutes before the host leg, so the base had moved.
  - The `/rivalfunds` routes were removed from live.
- **Measured by this seat at 15:19Z:**
  - SSM probe 566a5300 on the host reads `grep -c rivalfunds server.py` = 0 and schwab integration hits = 11;
  - `.env` ENABLED_INTEGRATIONS includes `schwab`;
  - S3 `-latest` = 2e2254156e (b8f52544).
  - The overwrite is still live.
- **Rulings:**
  - **msg 27207:** both halves VOID; restore 4ce7946426, whose tree this seat verified keeps MCPMSP's `tenant_registry.py`
    and `firm_role.py` byte-equal plus `FIRM_ROLE_ARNS`; roll back the IAM leg; close the ledger ROLLED-BACK; file the row.
  - **msg 27210:** YES to CVO~O's 27209 proposal. `deploy-to-ec2.sh` gains a required declared base and a live
    `-latest` ETag compare immediately before upload, and refuses on a mismatch. It ships in MX-r-6 v3.
  - **msgs 27224 and 27225, on 27222:** PLAN A; Plan B (2e2254156e plus the RV files, an unsigned combination) is REFUSED
    under NEVER-1.
    - Host actor: 2.0.0_SA_COO~RV, redeploying its own 4ce7946426. COO~MI's attempt hung in the halt-gate scan at about
      15:10Z and never uploaded.
    - IAM actor: 2.0.0_SA_COO~MI, after ~RV's read-back.
    - ~RV withdrew Plan B itself (msg 27226) and was confirmed as the host actor (msg 27227). Its ledger window ends at
      about 16:13Z.

## Intake

- **NFRA_TRNSPT (laptop) needs five NFRA_OPLGTW gateway orders** (msg 27215, laptop CTO 103268). They are accepted for
  intake.
  - This seat writes the OPLGTW PRD addendum once `R1_GATEWAY_DEPENDENCIES_FOR_SITE_Z_20260930.md` arrives with the
    site-Z pull.
  - The headless routes over Andrew's delegated token need a named allowlist and auth boundary first.
  - The 2.0.0_SA_COO~O seat is parked on the addendum.
- **NFRA_MCPMSP (outside the scope):** round 1 is 10 of 10 terminal @1fe1ef07b3, and L8 is next.

## Measured (15:19Z)

- **Inbox:** 0 unread.
- **Open TOs:** 16 of 187 (last read at tick 37; unchanged at the scope's own paths since).
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE.

## Acts only Andrew can do (each cited)

- **Site-Z pull-merge of the laptop push:** his word, which MSTR~Z is asking for. It brings the naming-gate r20 path and
  X11/X12.
- **G-ACCT step 5 and step 6 MFA:** his login and his MFA.
- **MCPORTAL G-2ND and G-CLOSE:** his sign-in and his grant change.
- **OPLGTW G-D walkthrough and the Part D sitting.**
- **NFRA_MCPMSP G-ADVISOR, G-USER, G-IT-INF, G-FIRM and G-KEY.**

## Compiler Tools

- `.tools/aws ssm send-command` (read-only) and `get-command-invocation` on i-07dccb1615503ac99.
- `.tools/aws s3api list-objects-v2` over the artifact prefix.
- `git rev-parse` blob equality on `4ce7946426` against `288fa78c93`.
