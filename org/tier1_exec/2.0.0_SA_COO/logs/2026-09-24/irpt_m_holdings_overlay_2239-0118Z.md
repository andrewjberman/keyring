# Holdings end to end with the snapshot model overlay - 2.0.0_SA_COO~M (Claude)
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE

**Date:** 2026-09-24
**Task Order:** Andrew-direct goal (record 6890584d29; Step 1b-F row landed by the CTO @d78fdb2f1c); CONTRACT v1.4 Holdings lane
**Status:** IN PROGRESS
**Window:** 2026-09-23T22:39Z (Codex-to-Claude handoff) -> 2026-09-24T01:18Z. Backend branch codex/irpt-m-completion: 9 commits by this seat; UI branch codex/irpt-m-ui: 1; workspace CLOUD: 1 record. Prior M log: irpt_m_holdings_runtime_coverage_checkpoint.md (2026-09-23).

## Objective

Holdings end to end for every 49 Financial and Inflection client, meshed across SmartX/Schwab and Eclipse/Orion, with a SNAPSHOT model overlay (which clients own which models, what assets are in those models; no time series), and a structurally correct Cottonwood pipeline bounded by Black Diamond's data window. Driven by /loop 20m (cron fcf016cf). DONE = /verify SOUND on the signed-in journey at all three firms.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-iam | `comp-iam service irpt-holdings` | PARTIAL | Printed the six statements but no Resource ARNs for the S3 grants; the exact key grants came from the live policy document (rail-checked) and simulate-principal-policy one decision at a time. |
| commit-gate | `.tools/commit-gate.sh` over every .py touched | PASS | py_compile + ds-precommit + ruff clean on each commit (one E702 and one F401 caught and fixed before commit). |
| naming-gate (in safe-commit) | every backend commit | PASS/WARN | Refused twice on new hand-kept carriers (firm literal; two pre-LGIC INF prefixes); both resolved by reading the names through lookup() and the producers' own key builders, never by waiver. The SmartX prefix RAISE was closed by 0.0.0_AB_MSTR at the gate (c49325f3d4, RAISE-EXISTING / WARN). |
| comp-which | not run | SKIP | The session's searches were single-file reads and rail-permitted pipe receivers; one raw `find` and one raw `aws s3 ls` were denied by the rail and re-run as `ls -R` and rail-checked listings. |

**What worked:** The publisher's own contract (bases never spliced, per-parent partitions, difference control) shaped every builder; each refusal it produced on real data was a real defect (nullable-int ids rendered as '44.0'; Opal model names in the composition table; the timestamp in the body making a rebuild a new revision).
**What failed:** My first COT membership GO request carried the prior candidate's part count (18) instead of measuring the new body's plan (20); disclosed the same turn, accepted by the CTO, and every later request prints the publisher's measured plan.
**Gap found:** served.py discards every internal error record (found by 2.0.0_SA_COO~P), so the deployed reader's NOT_READY for Andrew's Anna selection carries no reason; the sink is P's next code-only apply.

## Work Completed

1. SEAT TRANSITION. Measured the Codex M seat dead (no resume process, launcher parent gone, bridge log ending in cancelled turns), stopped its heartbeat/bridge/monitor/app-server and 600 s driver (0 of 6 remaining), registered this session, armed the inbox Monitor (re-armed on each 30-minute expiry), read and acked every queued broker message, recorded the two Andrew-directs verbatim (6890584d29) and armed /loop 20m.
2. COTTONWOOD PUBLICATIONS (two, both under CTO GOs, both CTO-verified): the 841-account expanded publication 93f930c265 (GO d940022b06; index grwnbLkeu; 18 creates + CAS; receipt COT_EXPANDED_PUBLICATION_RECEIPT_20260923.json) and the membership publication ac3adb97f5 (GO 99856; index XbWnSWxMFRs9; 20 creates + CAS, the 20-vs-18 deviation disclosed and accepted; receipt COT_MEMBERSHIP_PUBLICATION_RECEIPT_20260923.json). Deployed-reader matrix through the Lambda's own module: 0698 / d486 / combined READ_OK, 2026-09-23 refused, excluded account refused (CTO-accepted as the hop-3 library proof).
3. 49F MESHED BUILDER holdings_49f.py: Schwab 0833 custody as population and value (7,522 accounts), SmartX as model authority, Tax SMA workbook accounts under SMA > ALT Strategies > Tax-Managed SMA, Client as the plug; SmartX model leaves as the ASSIGNED pie (single model measured, several apportioned and claimed inferred), SmartX positions as a TARGET pie at the overlay clock; non-tying drills withheld. CTO findings 49F-TAX-CONFLICT-01 and TAXONOMY-PATH-01 closed (conflict carried in Client; taxonomy_path() from the registry).
4. INF MESHED BUILDER holdings_inf.py: validated Orion custody (876 of 876 tie) with Eclipse membership at its measured grain (whole-account leaves, managed/excluded splits with the drill withheld, Client with reasons); the COT-style currency modes in inf_positions.py; INF-CLOCK-01 closed (prior trading day of the Orion key); the CRO's retained Eclipse membership capture (138fad2935) consumed for the 74 sleeve accounts the export never exposed.
5. SNAPSHOT MODEL OVERLAY for all three firms: model_snapshot() (49F 7 SmartX models; INF 18 Eclipse models) and holdings_membership.cottonwood_model_snapshot() (46 Rebalancer models over the accepted publication, single-account custom names withheld); then the COT tree change (measured whole-account MODEL_LEAFs) published as item 2.
6. UI (codex/irpt-m-ui e7e6eaea): the Holdings tab renders a sleeve's taxonomy path, a model node's name and the producer's facts when the adapter carries them; the exact additive adapter patch for the shared client surface is with P (HOLDINGS_ADAPTER_PATCH_20260924.md).
7. ATTESTATION + GO REQUESTS: Andrew attested 49F and INF USD through the CTO; P's records (815dbc5507) read from P's branch into this worktree's untracked copy; both candidates prepared as exact bytes with 8 receipts each (49F 7c0e7ce3, 159 creates + index create; INF 1ebc7696, 34 + index create), zero-write checks PASS, GO requests with the measured plans sent (01:10Z).
8. ANNA NOT_READY (Andrew's re-test): the deployed bytes run outside the repo read all three selections; the role's exact S3 decisions are allowed for the capture path (versioned read of the index denied but unused there); the portal sends no as_of; the runtime binds the registry tenant. Differential routed to P/CTO: the request context under the role, readable only once P's served.py sink deploys.

MCP traffic: 31 inbound messages read and acked; significant: 3 CTO GOs/acceptances (d940022b06, 99856, 99866), CTO batches 3/5/7/9-10 (findings, acceptances, Step 1b-F rows), Andrew-directs relayed (hold off, currency attestations, Anna re-test), CRO capture 138fad2935, P's apply and attestation receipts. Outbound: 13 (record broadcast, 6 review handoffs / GO requests to the CTO, 2 interface messages to P, 1 reply to Y, 1 measurement to CTO+P).

## Decisions Made

| Decision | Rationale |
|---|---|
| Custody dollars only from the custodian, membership only from the model platform | SmartX valuations never tie to Schwab to the cent (0 of 5,912; different clocks); Eclipse managed values sit on their own clock. |
| Model assets: 49F as a TARGET pie at SmartX's clock; INF and COT as the member accounts' OBSERVED positions | TARGET is outside custody reconciliation by contract; Eclipse composition has no security rows; COT positions are validated custody. |
| Withhold a drill that does not tie, never patch it | 8 Schwab accounts, 71 INF split accounts: the account value stands, the rows do not. |
| Publish exact retained bytes, never a rebuild | clocks.as_of_timestamp is in the body, so a rebuild is a new revision; a GO names bytes. |
| No naming-gate waiver, no workaround | Names through lookup() and the producers' own key builders; the registry defect went to the gate owner. |

## Files Modified

See commit messages: 5f3651db41, 21f696e19a, a700417729, be672a40d8, a0f3f141ed, 26a04257bf, e9429899fe, da62651ff5, de804c65e9, 19b0f1f268 (backend, codex/irpt-m-completion); e7e6eaea (portal, codex/irpt-m-ui); 6890584d29 (workspace CLOUD, on origin @69e36619ae). Deliverables under org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/ (STATUS.md overwritten in place per the closer template).

## Blockers

None BLOCKED. Gated: the 49F and INF publications on the CTO's two GOs (requested 01:10Z); the screen on the runtime's error sink (P) and Andrew's re-test. Both are peer or Andrew acts, evidence-cited above.

## Current State

Base C:/Users/AndrewBerman/Desktop/ajb_workspace (CLOUD, origin @69e36619ae). Backend worktree C:/Users/AndrewBerman/Desktop/ajb_irpt_m on codex/irpt-m-completion, HEAD 19b0f1f268 (LOCAL, never pushed). UI worktree C:/Users/AndrewBerman/Desktop/ajb_irpt_m_portal on codex/irpt-m-ui, HEAD e7e6eaea. P integration portal C:/Users/AndrewBerman/Desktop/portal-local-live-20260923 @c1ac41ec (the 5174 screen). Untracked in the backend worktree: P-owned docs/contracts/investor-reporting/v1/CurrencyAuthorities.json (copied from P's 815dbc5507) and infra/aws/lambda/investor-reporting/reports/; do not commit either as M.
Live S3: opal-data-cottonwood index XbWnSWxMFRs9 -> revision ac3adb97 for 2026-09-22 (membership in the tree), prior grwnbLkeu / JhtDD retained. 49F and INF firm homes carry no index. Prepared bytes + receipts: .runtime/holdings-journey-20260923/prepared_49f and prepared_inf; publisher .runtime/holdings-journey-20260923/publish_candidate_live.py <firm> <revision> <go> check|publish.
Deployed irpt-holdings CodeSha l/GQrFcE... (repaired loader), role irpt-holdings-role; Andrew's last re-test: NOT_READY / No source age yet (00:5xZ), reason unrecorded by the runtime.

## Next Steps

1. [2.0.0_SA_COO~M] On each CTO GO: `publish_candidate_live.py <firm> <revision> <go> publish`, read back, reader matrix, receipt to the CTO; then the snapshot overlay artifacts on the published revisions.
2. [2.0.0_SA_COO~P] served.py error sink as the next code-only apply on irpt-holdings; the Holdings adapter patch on the live branch; confirm which publisher path (load_snapshot / load_pinned) the live request takes.
3. [1.0.0_SA_CTO] Rule the two GO requests; review of e7e6eaea and the adapter patch when P lands it.
4. [Andrew] Re-test Anna at localhost:5174 after P's sink deploys; the reason will then be one log line.
5. [2.0.0_SA_COO~M] /verify at completion; a card to Andrew before adding the Eclipse membership call to the scheduled pull (pipeline change).
