# NFRA_CTLPLN decomposition -- workstream REMOTE, round 1: SSH over the tailnet (FWD-27) and the caller-tier fence (FWD-28)

**Issuer:** `2.0.0_SA_COO~C`. **Cut:** 2026-10-12. **Status: ISSUED in one issuance (seven orders: three build orders on two worker queues and four staged seat orders). FROZEN at the cut.**

**Input.** PRD v0.23 addendum (`prd/NFRA_CTLPLN_PRD.md` section "ADDENDUM v0.23"), `1.0.0_SA_CTO` msg 108406. Records:
- FWD-27: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_015xZ_SSH_OVER_TAILNET_EXECUTE_COO_C.md` and the plan
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/LD0644_ROLLOUT_PLAN_CLUSTER_REMOTE_ACCESS_TAILNET_20261011.md` sections 3 and 7.
- FWD-28: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_POST_OFFLINE_FIVE_CROSSBOX_CALLS_AND_TWO_SECURITY_CARRIES_20261012.md`
  section 3 (XB-20261011T194408Z-e588).

**Workstream.** This is a WORKSTREAM of NFRA_CTLPLN with its own write surface, disjoint from round 6 THREAD (which touches
`.tools/thread-trace.py`, `crossbox-matrix.py`, `box-sync-conflicts.py`, the census files and `org/devices/state/`). Same issuer, so no
two-issuers collision. E1-E8 stand; this workstream rides ahead of them on Andrew's word of 2026-10-12 ~01:5xZ.

## Measured at the base (issuer, 2026-10-12 ~02:3xZ, box/laptop)

1. Tailnet addresses and names are in `org/devices/DEVICES.json` (`tailnet_name`, `tailnet_address` per device); `lib/devices.py`
   `devices()` reads them. No ssh login name is in the register.
2. Plan wave 1 (section 7): all four boxes' agent sessions read `elevated=False`; sshd runs only on the laptop, whose :22 rule has
   `RemoteAddress = Any`; RDP is tailnet-scoped on all four.
3. The two functions: `opal-portal-data-proxy` source `infra/aws/lambda/portal_data_proxy/` (`lambda_function.py`, `session_tracker.py`;
   Terraform `infra/aws/terraform/market-overview/lambdas.tf`, resource `aws_lambda_function.portal_data_proxy`) and
   `opal-portal-content-api` source `infra/aws/lambda/portal_content/lambda_function.py` (Terraform
   `infra/aws/terraform/portal-content/main.tf`, `module.opal_portal_content_api.aws_lambda_function.this`).
   Neither reads `tier` today (grep of both source dirs for `tier`: only `portal_data_proxy` CORS text matched).
4. The reference helper is `_require_internal` in `infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/dashboard_api.py:42-60`
   with its tests in `.../tests/test_internal_only.py`. FWD-28 as ruled admits `tier == internal` only.

## The elevation fact (the one essential wait, qualified)

`Add-WindowsCapability`, `Set-Service`, `New-NetFirewallRule` and the key-file ACL need an ELEVATED session; every agent session is
unelevated (measured) and cannot answer a UAC prompt. So the enable run on each box is Andrew's one line, in an elevated PowerShell over
the RDP that already works. That wait is expressly qualified with Andrew's word: "I also want that tailnet port set up so that we can
ssh into the various devices as well as rdp ... perhaps COO~C can handle it" (2026-10-12 ~01:5xZ), and the CTO's record states the
elevated run is Andrew's. Everything around it is an act a seat takes on demand: the script, the printed line, the probe, the receipt.
The negative arm (a login by password, or from a non-tailnet address, is refused) is driven by the verify tool, not waited for.
If an elevated path the fabric already owns is found (a task registered to run as SYSTEM), it is listed as an option and NOT used
without Andrew's express word.

## Cells

| cell | what | serves | risk | issued to | status at cut |
|---|---|---|---|---|---|
| `CT-u-1` | `.tools/ssh-tailnet-enable.ps1`: idempotent plan section 3 A-D; `-PublicKey`, `-Plan` (non-mutating preview, runs unelevated), `-Rollback`, `-SelfTest`; refuses password-auth-off without a key; BEFORE/AFTER; receipt `org/devices/state/<device>/ssh_enable_<stamp>.json` | FWD-27 | LOCAL | `0.9.0_WK_NFRA_CTLPLN~61` | pending |
| `CT-u-2` | `.tools/ssh-tailnet-verify.py`: from the laptop, per box in the register: tailnet :22 open or closed, one `ssh -o BatchMode=yes ... hostname` answer, and the negative arms (password login refused, non-tailnet source refused) where the box lets them be driven | FWD-27 | LOCAL | `~61` (queue: after `CT-u-1`) | pending |
| `CT-u-3` | sitez: pull the merged script, print the one elevated line, after Andrew's run read `ssh-tailnet-verify.py` for sitez, commit the receipt | FWD-27 | WORLD | `0.7.0_AE_CloudOps~U3` (sitez) | staged; GO on CT-u-1 + CT-u-2 merged |
| `CT-u-4` | dell1: same | FWD-27 | WORLD | `0.7.0_AE_CloudOps~CT1` (dell1, the lane reseated for x-1) | staged; same GO |
| `CT-u-5` | dell2: same | FWD-27 | WORLD | `0.7.0_AE_CloudOps~U5` (dell2) | staged; same GO |
| `CT-u-6` | both functions read `tier` from the authorizer context and answer 403 unless `internal` (data-proxy: all 11 routes; content-api: GET only; PUT/DELETE keep the firm fence); unit tests with fake events | FWD-28 | WORLD by path floor (applies nothing) | `~62` | pending |
| `CT-u-7` | apply `CT-u-6`'s code by Terraform under a signed pair with a NEVER-2 ledger; exercise: one call to each function with a partner-firm token answers 403 and with an internal token answers 200 | FWD-28 | WORLD | `0.7.0_AE_CloudOps~U7` (laptop) | staged; GO on CT-u-6 merged and the pair signed |

The laptop's own enable (plan section 3 B and D only) is issuer act A1 below: Andrew runs the script elevated once here, and the probe
from a second shell is the proof. FWD-27's DONE WHEN needs the laptop itself answering, so A1 is in the endpoint's path.

## Rule 24

**Domain:** the two outcomes FWD-27 and FWD-28 and the four boxes.

| item | served by |
|---|---|
| FWD-27 script | `CT-u-1` |
| FWD-27 proof instrument (4 boxes + 2 negative arms) | `CT-u-2` |
| FWD-27 sitez / dell1 / dell2 | `CT-u-3` / `CT-u-4` / `CT-u-5` |
| FWD-27 laptop | issuer act A1 |
| FWD-28 code | `CT-u-6` |
| FWD-28 apply and the 403/200 exercise | `CT-u-7` |

No item is unowned. **Same grain:** one script, one instrument, one box or one function pair per cell. **State coherence:** no LOCAL
cell changes a live seat, applies, pushes or messages. The WORLD cells change one thing each: a box's sshd and firewall (rollback
block in the script), or two Lambda code packages (Terraform plan reading exactly two changed resources). RDP is untouched.

## Dependency chains and fan-out

- Chain A: `CT-u-1` and `CT-u-2` are independent builds (disjoint new files) but both feed `CT-u-3..5`, so they sit in one chain; one
  worker, `~61`, takes `CT-u-1` then `CT-u-2` as its queue. `CT-u-3..5` are seat orders that consume both.
- Chain B: `CT-u-6` (worker `~62`) then `CT-u-7` (seat order).
- M = 2 chains; N = 2 workers. The WORLD orders are seat orders, not workers.

`fanout: 2 of 2 chains, cap 8, reason: two builds with a shared consumer queue on one worker; the five WORLD orders are seat orders staged behind them`

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A1 laptop:** Andrew's one elevated line on the laptop; the issuer then runs `ssh-tailnet-verify.py` from a second shell and
  records the line.
- **A2 keys:** Andrew's public key(s) (his own and `muse`'s) are the input. They are pasted to the laptop manager and never leave it as
  private keys. The issuer asks for them in one message at the GO of the per-box cells.
- **A3 negative arms:** the verify tool's password-refused and non-tailnet-refused reads, once per box, are the difference control.
- **A4 FWD-28 exercise:** the partner-firm token comes from the `CT-u-7` seat's own read of how a partner login is made in the dev
  pool. If none can be had without minting a credential, the 403 arm is run through the real API with the dormant UI walker's
  service account only if that account is partner-tier; otherwise the issuer files a row and asks the CTO. No credential is minted.
