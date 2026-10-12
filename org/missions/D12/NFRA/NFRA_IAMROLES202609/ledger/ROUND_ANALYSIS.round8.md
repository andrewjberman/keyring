# NFRA_IAMROLES202609 -- ROUND-8 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~18:3xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33357,
`surprise-channel/remediations/REMEDIATION_v8.Z.md` @28b6af06ae. **Recut by:** `2.0.0_SA_COO~ZI`, in ONE issuance.

## Round 8, as read

2 of 2 orders are complete (`ledger/COMPLETION_REPORT.round8.json` @be0536cad9), MAY-CLOSE.
- **y-1 FAIL, narrow (Z-C-S42):** `/cloud-ops` 18a's fallback counted `2026*.md`. **Fixed by this seat @f326f70e16:** the
  pattern is now the filename grammar `[0-9]{8}T*.md`, exercised on a planted inbox (one 2026 message, one 2027 message,
  one in `read/` and one dotfile give `unread=2 state_markers=1`). Z-C-S42 is met, for the CVO's next compile.
- **y-2 PASS:** the sweep's three classes are exercised; 7 ABSENT names re-read at 404, and 2 foreign names at 403.

## Rulings on the sweep's findings

| finding | ruling | cell |
|---|---|---|
| **5 ABSENT names with live Allows nobody decided:** `ajb-workflow`, `opal-data-portal-s3`, `opal-data-smartx-v2`, `opal-market-update`, `opal-data-smartx` | **NARROW, resource grain**, the x-2/x-5 shape: per role, a reference census (env and deployed code, positive control), then remove only the dead ARNs. Write-bearing grants go first. One pair per module or IAM-API act | **E1** |
| **`opal-data-schwab` (404) -- a READER, not just a grant.** `/49-schwab-conv` marks `s3://opal-data-schwab/01_raw/` DEAD (frozen 2026-07-15), yet `data/canonical/schwab/build_canonical_daily.py:154-156` STILL enumerates it, by the skill's own note | **Higher stakes than a dead grant: whoever claims the name could feed bytes into the canonical Schwab build.** Two acts in one cell. (a) The canonical builder stops enumerating the dead bucket: its owner removes the read, and this project routes it through `0.0.0_AB_MSTR~Z` if the owner is off site Z. (b) Then the Allow is narrowed. **Order: (a) before (b)**, because narrowing first would turn a silent dead read into a loud AccessDenied that the builder might not handle. Also correct the skill's description line naming `opal-data-schwab` as the sync target | **E2** |
| **Z-S43:** `opal-market-data-v2`, deleted on Andrew's ruling (2026-07-30) and tombstoned, still has its Terraform declaration and one live Allow with write | **One pair:** remove the declaration (TF-debt A7) and the Allow together. `safe-apply` already refuses the re-create. This also settles round 7's E2 market-overview read | **E3** |
| **3 wildcard grants** (`opal*`, `opal-*`, `opal-data-*`) skipped by the sweep | **READ-ONLY census first:** for each grant, its role, actions, and the concrete buckets that role actually addresses (env, deployed code, and the bucket list under our account that matches). A wildcard is replaced by that explicit list next round. A wildcard has no single name for `head-bucket` to classify, so it is graded by what the role actually uses | **E4** |
| R20 bridge (Z-S34, cutoff 2026-12-31) | Carried. Retire it when dell1's FWD-8 is in `box/sitez` | this seat |

## ENRICHMENT LIST -- round 9 (cut in ONE issuance)

E1 (narrow 5), E2 (schwab: reader out, then grant), E3 (market-data-v2 declaration plus Allow), E4 (wildcard census,
read-only). The Z-S40 and Z-C-S36 standing clauses apply to every pair and table.

-- 1.0.0_SA_CTO~Z

## Addendum 1 (2026-10-12 ~02:2xZ) -- a cross-fabric assignment: the dell agents' standing `lambda:InvokeFunction` on the portal-fronted functions. It is FIRST in round 10

**Source:** the laptop CTO's ruling on XB-20261011T232055Z-c404, section 4 of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_POST_OFFLINE_FIVE_CROSSBOX_CALLS_AND_TWO_SECURITY_CARRIES_20261012.md` @8424b373f2.
It places the control in THIS project, the estate's least-privilege project.
- `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` are each allowed `lambda:InvokeFunction` on **7 of 7** functions
  behind the shared portal API: `opal-data-refresh-api`, `opal-partners-data`, `opalinvest-auth-handler`,
  `trade-dashboard-api`, `trade-identifier-cache`, `trade-submission-handler` and `trade-workflow-handler`.
- A direct invoke bypasses the portal authorizer, and each handler trusts the event it is handed. dell2's row
  TCKT_VNEXT-D2-S46 is ARMED on it.

Round 9 is mid-round and its decomposition is frozen, so this is round 10's first cell, ahead of every other enrichment.

| # | cell | done when |
|---|---|---|
| R10-E1a | **READ-ONLY census, one pass:** for both agent users, every `lambda:InvokeFunction` Allow and its source policy (inline, group or managed); the full set of functions behind EVERY API root that uses authorizer `naqxlm` (the portal, ticket, IRPT, harvest and data-proxy roots; the laptop census covered only the portal's 7); and, from 90 days of CloudTrail, which of those functions each agent actually invoked, and when | a per-function table: grant source, invoked yes or no (date), and the cell or order that needs it, with denominators printed |
| R10-E1b | **NARROW under a pair:** remove every authorizer-fronted function from the agents' standing invoke grant. A function that a named dell cell deploys or tests is re-added only for that cell's window, under its own pair, never standing | `simulate-principal-policy` for each agent on each fronted function reads implicitDeny, with a positive control (one function the agent legitimately keeps) reading allowed; the receipt goes to `1.0.0_SA_CTO~DELL2`, who disarms D2-S46 |

**Cross-fabric note:** the dell agent users' grants may sit in a dell-owned policy. If E1a finds the Allow in a policy another
fabric generates, as OG-tb-1 found for NFRA_CTLPLN, the cell gets that fabric's consent first, in the XB form.

## Addendum 2 (2026-10-12 ~21:0xZ) -- Addendum 1 is WITHDRAWN; there is no round 10; the project closes at round 9's L10

**Source:** Andrew-direct ~20:5xZ, item 1, VERBATIM: *"Dell boxes should not be curtailed. Is there further work slated on
this project? I think this one can be wound down/closed."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`.

- **R10-E1a and R10-E1b are withdrawn.** No act narrows the dell agent users' grants. dell2's row TCKT_VNEXT-D2-S46 is told,
  through `0.0.0_AB_MSTR~Z`, that this project will not take it.
- **No round 10 is cut.** Round 9's one non-terminal order, IAM-z-2, stays. Its only remaining leg is a READ: does the first
  real bd run after the APPLIED delete (~2026-10-13 04:00Z) complete? If it fails, the rollback is the saved policy document.
  Leaving a live narrowing ungraded would leave the act half-checked.
- **The close.** When the CVO's round-9 slug arrives, this seat answers with the CLOSE, not an enrichment list. FWDs it has
  not realized are graded as they stand and recorded as not pursued, on Andrew's word. Nothing is re-cut.
