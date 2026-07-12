# NFRA_TOOLPASS sweep leg -- 4 tools fixed + 2 confirmed, a security-tool defect behind a benign drift -- 3.0.0_SA_CVO
**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), DIAGNOSE, IMPLEMENT, COORDINATE
**Date:** 2026-07-12
**Task Order:** NFRA_TOOLPASS (CTO front-passes -> CVO confirm/fix, gate-to-CTO, brief COO) -- in-session variation: CVO does the fixes directly (Andrew: keep the circle tight)
**Status:** COMPLETE (all dispatched items closed; reachable for next dispatch)

## Objective
Independently confirm-or-fix each comp-* tool CTO front-passes: reproduce every clean bill by an
independent EXERCISED method, hold the sovereign bd-hold, gate-before-commit, non-vacuous fixture +
sec.2a mutant-kill on every fix, own-mutant discrimination on every confirm.

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-which / comp-grep / comp-glob | routing audit + all searches (on-rail) | PASS | comp-grep correctly excluded 972 sovereign-held paths every call |
| comp-pii routes / fields | PII-DRIFT grounding + fix verify | PARTIAL->FIXED | reported cleartext as "hashed" (audited a retired mechanism); fixed 2094d30c9 |
| comp-routes (pii_cli routes) | auth:NONE census | PASS | post-fix 9 edge / 3 UNRESOLVED / 0 NONE -- discriminating |
| comp-learns-score --self-test | Goodhart invariant confirm | PASS | 8/8, goodhart.no_usage_proxy bites on my own pure-usage item |
| comp-xray freeze-monitor (source) | bd-DATA reader guard | PASS | held-target exclusion; 0 reads on opal-data-bd |
| comp-iam (implicit via source reads) | n/a | -- | not needed; all boto3/read targets source-verified |

**What worked:** comp-grep's sovereign-hold exclusion (972 paths) made CODE-ONLY grounding safe by
construction; comp-pii/comp-routes `routes` gave the exact auth-posture census the findings turned on.
**What failed:** comp-pii's OWN false-assurance (reported retired-hashing as live) -- the defect I fixed.
**Gap found:** a tool that audits a mechanism must first verify the mechanism is REACHABLE, else it
reports on a corpse (banked to memory; CTO-ratified doctrine).

## Work Completed
1. **comp-tooltip** c91aaa804 -- semantic false-positive: DataTooltip.tsx:22 (the canonical component's
   OWN render) flagged "migrate to <DataTooltip>". Exempted canonical def files from DRIFT; drift 6->5,
   migration 83%->86%. 6-test bidirectional fixture + sec.2a. CTO gate GREEN.
2. **comp-xray** 04de28c0b (AE-committed via the owned-paths lane gate; Co-Authored 3.0.0_SA_CVO) --
   `freeze-monitor` (agent CLI) auto-read opal-data-bd 49F served AUA. Held-target exclusion at the
   run_freeze_monitor chokepoint (pure-string _bucket_is_held, opens nothing); COMP_XRAY_INCLUDE_HELD=1
   opt-in for the deployed cron. 4-test fixture (non-vacuity via OVERRIDE control) + sec.2a. Closed the
   bd-reader DATA-tier. Lane gate blocked CVO from infra/aws -> correctly routed to AE~C.
3. **comp-which** 2777924da + scorecard 172b898c6 -- routing-quality scorecard 4/12->10/12 (83%). 5
   curated rules (kuzu / surface-check-via-launcher-pointer / validate / bare-gold-script / grep-fallback)
   + --json passthrough + grep-fallback-threshold fix. 18-test bidirectional fixture. comp-surface-check
   is deliberately non-routable (excluded_not_graph_use_cases) -> launcher POINTER, NOT _ROUTABLE_META_ROLES.
   Durable TO-8 scorecard handed to COO for the 0.8.0 corpus.
4. **comp-pii** 2094d30c9 -- PII-DRIFT (account_number/clientKey) grounded CODE-ONLY = NOT a leak;
   serve-time masking fully RETIRED 2026-04-15 (needs_pseudonymization->False + 2 filter early-returns).
   The REAL defect: comp-pii audited the retired _transform_field and reported cleartext PII as "hashed"
   (false assurance). Fix: AST reachability gate -> honest cleartext posture (redirects to upstream auth).
   4-test fixture + mutant-kill. DS_ClientPlatform (owner) retro-confirmed.
5. **comp-learns-score** 57488c961 (CTO's fix) -- CONFIRMED all 3 exercised: the re-anchor
   (low_confidence_routes) is not a Goodhart relaxation; my own pure-usage item flips goodhart.no_usage_proxy
   to FAIL while the real worklist passes. CLOSED (CYCLE-27).
6. **comp-routes** c9949dd3b (COO/worker fix) -- CONFIRMED all 3: discriminator sound, does NOT
   blanket-relabel (genuine-open getPlatinumFirmDashboard stays resolvable/NONE; client-composed
   getPlatinumAdvisorSummary->UNRESOLVED), my own bidirectional mutants both bite. Closed my own auth:NONE
   finding = a comp-routes resolution gap (Rule-22a caveat), gate actually SOUND.

## Decisions Made
- Sovereign hold held throughout: CODE-ONLY grounding, no served/client/bd payload read; never ran a
  producer; the (b) PII-tripwire correctly did NOT fire (cleartext is Andrew's deliberate 2026-04-15 model).
- comp-surface-check routed via a launcher pointer (respects the deliberate exclusion), not made routable.
- Deconfliction on crossed comp-xray routing settled by the owned-paths lane gate (objective arbiter);
  no --force bypass of infra/aws.

## Files Modified
see commit messages: c91aaa804, 2777924da, 172b898c6, 2094d30c9 (each carries per-file summaries).
comp-xray files landed under 04de28c0b (AE lane). 2 memory files written to ~/.claude memory (routing
mechanism; reachability-before-audit).

## Blockers
None. (Sovereign bd-hold is a standing CONSTRAINT, not a blocker -- all work routed around it CODE-ONLY.)

## Current State
All 6 dispatched items CLOSED. Every fix on origin/CLOUD, verified by hash, F-010-safe (-F), with a
non-vacuous fixture + sec.2a mutant-kill; both confirms exercised on my own mutants against the real code.
The auth thread I surfaced is fully resolved end-to-end: comp-pii not-a-leak + false-assurance fixed;
auth:NONE = a comp-routes resolution gap (fixed c9949dd3b); upstream-auth integrity EXERCISED + SOUND,
co-signed DS+COO, CLOSED (499cb50ef -- anon->401, 4 co-signed facts, no anon-200-with-body). comp-pii's
"pseudonymizer not-found" fallback residual is deferred to the DS_ClientPlatform retro (should also
fail-safe to cleartext). Not my lane: the sovereign_held C1-C8 consolidation (3.0.0_SA_CVO~B).

## Next Steps
- [1.0.0_SA_CTO] Reachable for the next front-passed tool dispatch (alphabetical sweep).
- [0.4.0_DS_ClientPlatform] Retro: confirm the comp-pii fix + the not-found fallback residual (own the
  pseudonymizer + comp-pii long-term).
- No open loops on my side.
