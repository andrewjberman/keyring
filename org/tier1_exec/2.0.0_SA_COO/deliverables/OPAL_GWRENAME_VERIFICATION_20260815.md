# OPAL_GWRENAME -- COO independent verification record (TO-2)

**Verifier:** 2.0.0_SA_COO. **Executor:** 0.7.0_AE_CloudOps (TO-1). **Spec:** runbook @433454738b.
**TOs issued:** @8dfa20c274. **GW-6 cold-login amendment:** @8386ce43c3 (MSTR 015746Z, adopted 015822Z).
**Principle:** my verification shares no derivation with AE's. Live primitives only; AE reports are
claims, not evidence. Interpretation tables are pre-registered BEFORE the evidence exists.

## Pre-flip baselines (all 2026-08-15, BEFORE any live-plane change)

| # | What | By | When | Result |
|---|------|----|----- |--------|
| B1 | Warm whoami via mounted opal-gateway MCP (`mcp.opalinvest.dev/mcp/`) | COO (this session) | ~0156Z | PASS -- Graph payload: displayName "Andrew Berman", mail Andrew@opalinvest.com, odata context graph.microsoft.com/v1.0 |
| B2 | Warm whoami, same path | MSTR | 015830Z | PASS -- same payload shape. Full chain alive: ALB -> listener -> target -> gateway -> Graph |
| B3 | COLD OIDC mount, known-good state (positive control for the discriminator) | COO seat spawn ~0152Z; AE seat spawn ~0152Z | pre-flip | BOTH succeeded -- proves a cold mount PASSES when the gateway is healthy, so a post-flip cold-mount failure cannot be dismissed as "fresh mounts are flaky" |

Gateway is HEALTHY end-to-end going in: any post-flip failure is attributable to the cutover.

## GW-6 interpretation table (pre-registered, MSTR 015904Z, adopted verbatim)

| Post-flip observation | Verdict |
|---|---|
| Cold mount succeeds + whoami returns Graph data | H1 genuinely closed |
| Cold mount FAILS, or mounts but whoami errors | H1 LIVE -- OIDC secret not re-set on the recreated listener |
| Warm sessions still fine but cold fails | H1 LIVE and MASKED by pre-flip tokens -- the row the amendment exists to expose |

Warm-session calls post-flip are REGRESSION checks only, recorded as
"warm call OK (non-discriminating)". A warm PASS is never GW-6 evidence: warm sessions hold
bearer tokens minted before the flip, and H1 is exercised at LOGIN.

**Plan of record for the cold read:** MSTR spawns a throwaway fresh seat at S4-complete
(COO calls for it); the seat's cold MCP mount + first tool call is the acceptance instrument;
seat killed immediately after.

## Stage verification log (COO independent reads)

- S1 (additive): **VERIFIED-INDEPENDENT (COO), 0201Z.** GW-1: my own live read -- 4 of 4
  secret pairs sha256-MATCH (aws CLI pipeline, values never printed; my absolute hashes differ
  from AE's boto3-derived ones because the pipelines differ -- the old==new equality holds on
  BOTH instruments, and the differing absolutes evidence genuinely independent derivation).
  GW-2: my own recursive listings materialized client-side -- 38 of 38 relative keys present,
  size-identical, diff clean.
  **CENSUS ADJUDICATION (COO, acceptance-bar holder): 36 of 38 blobs inside the NEW prefix
  retain m365-*.tar.gz basenames (version history). DECLARED EXCEPTION -- retained, not pruned:
  (a) pruning inside the new prefix is NOT a runbook-named act and S3 object deletion is
  Andrew-reserved, so it is out of tonight's authorization; (b) the census surfaces are
  live-plane resource NAMES -- history blob basenames are content, not a live surface;
  (c) post-S4 they are dormant history (deploys mint opal-named artifacts). Will be surfaced
  to Andrew in the final report for an optional prune order.**
- S2 (plan-only): **VERIFIED-INDEPENDENT (COO), 0219-0222Z, against the @3e8c3522f1 tree.**
  My own read-only plan re-derivation (`terraform plan -lock=false`, 1,769 lines captured):
  Plan 40 add / 7 change / 35 destroy -- REPRODUCES AE's numbers exactly. STOP-CONDITION
  CLEAR on my instrument: "aws_instance.gw will be updated in-place" (:862), zero
  `forces replacement` lines in its block. 35 must-be-replaced 1:1 with destroys; the 5
  taxsma creates account for the 40-vs-35 delta; `aws_lb_listener.https must be replaced`
  (H1 exposure confirmed real); route53 alias updated in-place (follows new ALB). Diff
  checks: ART + latest literals now DERIVE from $SERVICE (source-read at @a7312b946b);
  producer-regression class closed. taxsma sweep-in: 5 resources enumerated at source,
  both role names ABSENT on my own live get-role reads. COO ruling: sweep-in ACCEPTED
  (additive-only IAM, committed CTO-gated config, -target surgery riskier).
  RESOLVED 022546Z (MSTR ruling, converged): (a) taxsma sweep-in CONCUR -- lands with the
  apply; (b) REVERT @3e8c3522f1 -- MSTR withdrew their 021548Z conditional on the record as
  malformed (a plan verb is a DESIRED-state statement and does not disclose the convergence
  mechanism; an EC2 stop is Andrew-reserved and the reservation binds on the ACT). Andrew's
  stop/start word sought in parallel, explicitly NON-GATING. Unified S3 GO issued to AE 0227Z.
  **CARRIED RESIDUAL (census + close report, verbatim):** "user_data still references m365
  paths; TRIP-CONDITION: any future instance replacement first-boots against the old /opt
  path and, post-S6, a DELETED S3 prefix -- must be fixed as part of any deliberate
  replacement act."
  **PRECONDITION recorded against any FUTURE approved stop act (MSTR 022546Z):** a stop/start
  assigns a new PUBLIC egress IP (no EIP); Entra Conditional Access has NOT been verified free
  of IP-restricted policies, so a new egress IP could break Microsoft auth in a way that
  MIMICS H1. Checking Entra CA is a precondition of the stop, not a follow-up. Scope note:
  tonight's reverted tree has no egress IP change, so this hazard CANNOT contaminate tonight's
  cold-login read.
- S3 (apply + H1 re-set): PENDING.
- S4 (on-box): PENDING -- on-box verification, never the wrapper rc (known charmap false-negative).
- S5 (verify): PENDING -- cold login per table above + section-2 census with denominators.
- S6 (retire): PENDING -- gated on S5; after S6 the rename is one-way.
