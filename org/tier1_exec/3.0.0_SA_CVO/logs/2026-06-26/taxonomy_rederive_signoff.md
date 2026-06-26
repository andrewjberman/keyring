# Follow-on 2026-06-26 ~22:45Z->23:35Z -- NFRA_MSGRAPH layer-taxonomy re-derive VERIFIED + SIGNED (permanent COND-A fix landed)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-26 | **Window:** since session_close_1925-2245Z (f4afb0ad0)

## TL;DR
Single-item delta after the session-close log: AE landed the layer-taxonomy relabel re-derive; I
ran the independent per-class acceptance verify and SIGNED. The permanent COND-A fix is now LIVE --
aws is a pure resource layer, my certified baseline byte-preserved, and my corrected per-class
COND-A is the STANDING definition (no more per-run adjudication). Closes the night's MSGRAPH arc e2e.

## Work done
- **Taxonomy re-derive acceptance** (315dfd410, appended to CVO_taxonomy_signoff_20260626.md):
  verified INDEPENDENTLY on snapshot 8308767746622328835 (queried the graph myself, not AE's report):
  - 3 layers exactly: aws=1442 / portal=11338 / ms=5423. 0 UNCATEGORIZED (COND-2 fail-loud cert held).
  - aws PURE: LEAK CHECK = 0 portal-code node_types in aws (the mislabel that polluted the count is gone).
  - COND-A baseline PRESERVED: all 9 certified per-class byte-match (IAM_POLICY=308, LAMBDA=177,
    IAM_ROLE=141, EVENT_RULE=112, API_ROUTE=77, SECRET=76, S3_BUCKET=35, DYNAMODB_TABLE=34, EC2_INSTANCE=29).
  - EXTERNAL_ENDPOINT=0 (Andrew dropped the 3 SNS-target PII nodes); reappearance is caught by COND-2.
- Accepted Andrew's sovereign 3-layer simplification (aws/portal/ms; dropped the external+pipeline I'd
  signed) -- doesn't touch the COND-A baseline; cleaner. RAVC SIGNED to 0.8.0 (CC CTO/COO/0.7.0).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-kuzu | re-derive acceptance: layer breakdown + aws portal-leak check + 9 per-class counts + UNCATEGORIZED/EXTERNAL_ENDPOINT | PASS | the independent-verify spine; confirmed aws-pure + baseline-preserved |

**What worked:** comp-kuzu per-class diff confirmed the relabel preserved the frozen baseline + purged the portal leak. **Gap:** none this delta.

## Blockers
None.

## Current State (handoff)
NFRA_MSGRAPH layer-taxonomy permanent fix LANDED + verified (snapshot 8308767746622328835): layer='aws'
is now the standing frozen COND-A baseline (28 resource types, the 9 certified per-class counts), portal
(11338) + ms (5423) drift freely. Ledger nfra-globgrph-layer-taxonomy CLOSED. The full MSGRAPH MS-estate
arc (COND-A adjudication -> 5422 sign -> taxonomy conditional-sign -> signed -> re-derive accepted) is
complete end-to-end.

## Next Steps (mine, event-gated -- unchanged from the session-close)
- **[3.0.0_SA_CVO]** M365 0-2 deploy smoke + Part-3 per-user-scope smoke (post-L6, when 0.8.0 deploys);
  DC1 post-crawl isolation-held verify (0.7.0 live artifacts); GCONTR --load-contracts pin verify + the
  joint BMKAUD replay; Decision-B federated-heat provenance verify when that phase builds.

## MCP traffic
~3 significant: AE re-derive hand-off (received), my taxonomy SIGNED (sent, CC CTO/COO/0.7.0), heartbeat.
Prior heartbeat re-surfaced 15 already-actioned messages (not re-counted).
