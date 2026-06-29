# CVO Finding — EC2_MANIFEST + bd-49f TF "always-on proxy" stale-claim drift (49f native-IP)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 0.6.2_AE_PartnerETL (infra driver, grounded it) · cc 2.0.0_SA_COO · context 0.7.0 (box-owner) / 0.6.0 (build-lead)
**Verdict: DRIFT CONFIRMED — ground truth is NATIVE-IP (no proxy). Stale "always-on BrightData proxy" claim survives in 3 infra-lane files. Routed to driver (infra source-of-truth = outside CVO direct-fix lane).**

## Ground truth — independently verified (not relayed)
My own Andrew-direct decision **CVO 203246Z** dropped BrightData for 49f (datacenter-block premise was FALSE; native AWS IP reaches bd3). Applied + proven:
- Commits: `78cc4a435` (DROP BrightData, remove proxy grant, omit BD_PROXY_SECRET_ID from box env), `3e7246ab4` (proxy-drop ledger CLOSED, role re-slimmed), `b69a5faf6` (my log: durable auto-login PROVEN end-to-end on native AWS IP).
- **LIVE IAM role `bd-49f-auto-login-role`** (via instance-profile `bd-49f-auto-login-profile`), inline policy `bd-49f-auto-login`, GetSecretValue Resource set = `blackdiamond/49f/*`, `astn/kimi/api-key-*`, `blackdiamond/49f/session-*` — **NO `astn/brightdata/residential-proxy`.** The box cannot fetch proxy creds; native egress is structurally the only path. (Grounded on live `get-role-policy`, not comp-iam DESIRED, per CLAUDE.md fresh-IAM rule.)
- `infra/aws/terraform/bd-49f-auto-login/iam.tf:51-52` already documents the drop correctly.
- `astn/brightdata/residential-proxy` secret still EXISTS (intentional — held as a one-line revert if native-IP ever shows a BD connection-block at durable-port LEG2). Correct, not drift.

## The stale claim — 3 locations (all infra source-of-truth)
1. **`infra/aws/ec2/EC2_MANIFEST.json:58`** (CI/CD source-of-truth, Rule 8) — `"...egress only; ALL BD traffic via the ALWAYS-ON BrightData residential proxy)."` + IAM clause `"GetSecretValue blackdiamond/49f/*+astn kimi/brightdata"`.
2. **`infra/aws/terraform/bd-49f-auto-login/instance.tf:18`** — subnet description `"...all BD traffic is proxied through the always-on residential proxy."`
3. **`infra/aws/terraform/bd-49f-auto-login/instance.tf:26,30`** — SG comment/description `"reach BrightData residential proxy..."` / `"egress all (BrightData/Graph/Kimi/AWS/pkg)..."`

(The SG egress-all + public-subnet stay functionally correct — egress is needed for Graph/Kimi/AWS regardless. Only the narrative over-claims the proxy is in use.)

## Recommended corrections (exact, for the driver to commit)
- **EC2_MANIFEST.json:58** proxy clause -> `"...egress only; NATIVE AWS IP for BD (BrightData proxy DROPPED 2026-06-25, Andrew-direct via CVO 203246Z -- datacenter-block premise was false; resi-proxy secret retained as a revert-only)."` and IAM clause -> `"GetSecretValue blackdiamond/49f/* + astn/kimi/api-key (brightdata grant DROPPED 203246Z)"`.
- **instance.tf:18** -> `"...outbound reach to Graph/Kimi/AWS (BD egress is the box's NATIVE AWS IP -- BrightData proxy dropped 203246Z; public IP is IGW-reach only). Default-VPC public subnet..."`.
- **instance.tf:26,30** -> drop "BrightData residential proxy" from the reach list; keep `Graph/Kimi/AWS/pkg`. SG stays egress-all (functionally unchanged).

## Lane note
EC2_MANIFEST.json + instance.tf are infra authoring-lane / CI-CD source-of-truth — my `/spot-check` fix-authority is bounded to project-JSON/REGISTRY/TO-status and EXCLUDES code/infra/runtime, which route as a CVO finding to the responsible driver +CC COO. So this is a routed finding with the verified corrections, not a direct CVO edit. (If COO issues an explicit scope-grant to edit the manifest directly given it restores my own decision, I'll do it under audit.)

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| live `aws iam get-role-policy` (rail-checked) | bd-49f-auto-login-role GetSecretValue resource set | PASS | NO brightdata grant -> native-IP structurally enforced |
| live `aws ec2 describe-instances` | i-0fa1846f04ed7e337 state | PASS | stopped (transient box, expected) |
| git log/grep | 203246Z decision provenance + 3 stale-claim locations | PASS | iam.tf already correct; manifest + instance.tf narrative stale |

## Blockers
None. Finding routed; awaiting driver commit (or COO scope-grant).

— 3.0.0_SA_CVO
