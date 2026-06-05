# ws-charter cycle:0032 — 2026-06-05 1312Z

**CLASS:** NOVEL (Andrew-direct PRD authoring)

## Trigger
Andrew-direct: "write a PRD that covers the fixes for all of these formally that we can send
to COO for decomposition. Use your recommendations." NOVEL authorized via Andrew direction
in inbox this cycle (/ws-charter Step 4b ladder). Not a new project — PRD for existing active
NFRA macro (had no formal PRD doc; prd was null). HARD-BLOCK check: clear (PRD doc, not new
project code / not REGISTRY Active addition / not destructive).

## Action
Authored docs/architecture/NFRA_COSTRED_PRD.md (v0.1) — the NFRA cost-reduction execution PRD
formalizing the 2026-06-05 AWS audit findings into 7 decomposable remediations (R1-R7) mapped
to NFRA W1/W3/W4, consolidating both halves of the CTO/COO de-dup split:
- R1 activate cost-allocation tags (root attribution blocker, forward-only, do-first)
- R2 opal-data-bd noncurrent 90d->14d (~$45/mo; 2.3TB version bloat; best risk/reward)
- R3 bd-gold c6i.16xlarge right-size (~$100-200/mo; validate-on-nightly; QA/Spot first)
- R4 leaked runners (demo-transform + inf-exporter) / R5 orphan EBS + idle EIPs + stopped fleet
- R6 inf-gold self-stop reliability (mostly done by enforcer) / R7 Secrets caching (optional)
Binding constraints baked in: C1 compute-discipline (no ad-hoc runs), C2 Andrew-gate on every
destructive apply, C3 idle-scoped caps, C4 TF/safe-apply + S3-artifact flow. Plausible total
~$230-410/mo (~40-65% of bill).

## Commits
- eb2f7fe9a feat(NFRA): PRD v0.1 + NFRA.json prds[] registration (pushed CLOUD)
- (prior this session) d9f2978a9 + bb2cf2835 = the audit brief + CTO deep-dive addendum

## Handoff / follow-on
- Routed to COO (msg 131213Z) for decomposition. Recommended first TOs: R1 + R2(a) + R5;
  R3 behind nightly-telemetry confirm; destructive applies stage to Andrew GO.
- Open (separate): v2.1.114 SERVED-PROD close — CVO verdict PASS-with-honest-limit; routed
  (a) Andrew pixel-glance / (b) accept-on-stability to Andrew; RAVC2 closes on his call.

## Next-cycle expected state
COO decomposes R1-R7 into TOs; CTO available for AC/scope questions + v0.2 amendment if needed.
