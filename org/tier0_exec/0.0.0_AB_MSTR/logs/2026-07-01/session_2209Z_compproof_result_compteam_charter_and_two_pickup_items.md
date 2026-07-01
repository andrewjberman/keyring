# MSTR Session — COMPPROOF benchmark result + NFRA_COMPTEAM charter + 2 pickup items (post-reboot ~0307Z -> ~2209Z)
**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, DIAGNOSE

Long post-reboot operating session. Startup + a full run of the NFRA_COMPPROOF benchmark (the program
proving itself), a new NFRA_COMPTEAM charter, ~10 Andrew-direct/COO spawns across SCTY + INFREF + MDPF,
and — the reason for this log — TWO design items Andrew raised that we pick up TOMORROW (captured in full below).

## THE TWO PICKUP ITEMS (Andrew-direct, discuss tomorrow) -- primary handoff surface

### ITEM 1 -- Assess consistent + correct comp-tool usage from real agentOps; is it a queryable learning loop?
Andrew's Q: now that comp-tools are hammered in, how do we assess from real-life agentOps that they are
used CONSISTENTLY + CORRECTLY, and is that tracked in an easily-queryable mechanism for an effective
learning loop?

GROUNDED STATE (verified live this session):
- FOUR live telemetry streams exist + are queryable:
  - `org/compiler-tools-log.md` (12,413 lines, live) = every comp-tool run (tool/result/TO/agent) -> VOLUME.
  - `org/mcp/comp-which-rail.log` (3,263 lines, live) = rail route-vs-run + every `# rail-checked` override -> CONSISTENCY (comp-tool vs raw-grep/aws bypass rate).
  - `org/mcp/comproute-routing.jsonl` (622 lines) = router's tool pick per query -> CORRECT ROUTING.
  - `org/mcp/agent_telemetry/*.jsonl` (69 files) = PostToolUse work stream, archetype-tagged -> SHAPE/COST.
- These federate into Trino as the `tool_activity` catalog (NFRA_COMPLEARN P0-P1); `org/modules/graph/comp_learns_score.py` = the value-anchored scorer (scores VALUE not usage; 241 inversions caught, Goodhart-resistant).
- Mapping to the question: "consistently used" = directly measured by the rail-log override rate. "correct tool" = routing.jsonl + COMPROUTE C1 eval (precision@1). "actually solves" = what NFRA_COMPPROOF just measured (5/6 blind).
GAPS (honest):
  (a) the LEARNING LOOP is ACCUMULATES-BUT-INERT (COMPLEARN D1 finding) -- data collected + queryable, but not yet autonomously consumed-and-improved; needs the 2-stage close (DRV default-router flip [DONE] + affinity w_h activation [data-accruing over days]).
  (b) "correct in the wild" is measured thinner than "used in the wild" -- effectiveness is only a periodic blind-run (COMPPROOF), not continuous.
PROPOSED CHARTER CANDIDATE (tomorrow's decision): a unified **"comp-tool health" view** fusing per-tool
USED (compiler-tools-log) x RAIL-PREFERRED-OVER-RAW (rail-log) x EFFECTIVE (recurring COMPPROOF-style blind
probe). One query -> per tool: used+effective (keep) / used-ineffective (fix) / effective-ignored (promote) /
dead (retire). = the effective learning loop; mostly a FUSION of existing streams + COMPLEARN activation +
COMPPROOF as the recurring effectiveness probe. Frame as extending COMPLEARN.

### ITEM 2 -- Cross-Opal-employee agent collaboration over an SQS queue/thread; meter + secure it?
Andrew's Q: can we make an SQS queue + thread where MY agents talk to another Opal employee's agents,
even collaborating in parallel? How to METER + SECURE it?

ARCHITECTURAL READ: it is the MULTI-TENANT extension of the opal-agent-comms broker (today port-7800 +
inbox = single-user/single-workspace). Cross-EMPLOYEE = a new inter-principal bus, and it rides directly on
the just-chartered NFRA_COMPTEAM (onboarding) + SCTY (entitlements/guardrails).
- TRANSPORT = SQS (durable, decoupled, AWS-native, CloudWatch-metered). Shared queue / queue-pair per
  collaboration between fleet-A and fleet-B. Parallel collab works because both fleets read their scoped
  slice of the shared graph (COMPTEAM Component-B read-partitions) + coordinate via the queue.
- METER (2 layers, cheap): (1) SQS-native CloudWatch (MessagesSent/Received/Deleted, AgeOfOldest, per-queue).
  (2) app-layer broker logs every cross-employee message (from_employee/from_agent/to/subject/size/ts) into
  the SAME tool_activity telemetry substrate -> cross-employee collab metered exactly like tool-use, one query surface.
- SECURE (5 controls; cross-PRINCIPAL comms is a real attack surface):
  1. IAM-scoped per employee (send to shared queue; read ONLY own partition; SQS+KMS+message-group).
  2. SCTY-guardrail gated -- an ACTION-request (vs DATA-share) crosses a trust boundary -> the SCTY entitlement/tier authz gate (different trust classes).
  3. Verified attribution -- SIGNED from_employee+from_agent identity (not a claimed serial; hardens exact-serial discipline vs spoof).
  4. Egress content-strip/DLP -- no secrets/PII/creds cross the employee boundary (same strip-list as the COMPTEAM kit).
  5. Default read-only/propose -- an incoming cross-employee message can REQUEST not MUTATE; receiving fleet's own agent / human-tier adjudicates anything actionable.
PROPOSED SHAPE (tomorrow's decision): most naturally a COMPTEAM SIBLING (a "Workstream C -- inter-principal
agent bus") on SCTY -- not a new stack; = COMPTEAM(onboarding) + SCTY(entitlements) + one SQS bus + the
metering fold-in.

## Other work this window (concise)

1. **STARTUP (COORDINATE).** Post-reboot: /watcher re-armed Monitor `bhxjr330e`; re-registered PID 11200; Art. XII all 3 Tier-0 law docs re-read (Const v1.5/Stakes v1.5/Directives v1.12, unchanged). Base-CVO + CTO + COO + COO~B all self-came-up (reboot respawn window).

2. **NFRA_COMPPROOF -- chartered -> PRD -> RAN -> 5/6 (COORDINATE+VALIDATE+DIAGNOSE), the session's spine.** LD-0234 charter + brief (94b60a27f); B-corpus CAPPED at top-20-by-severity/2026/cited (LD-0235, 5402f130b); the "success-shaped-but-wrong" class pinned as B's 3rd scorer axis GROUNDING-RESILIENCE (LD-0236, ad001b875). CTO PRD 3d78e1f5b + B-harness 1315f9a03. FULL ISOLATION SAGA (airtight took a /seams + a false-alarm I caught by grounding + a hardening chain): answer-free payload -> clean-room context-suppress -> true-sandbox (build_sandbox.sh, forbidden absent-by-construction). RAN the 20 blind solvers (bare `claude -p` per case). RESULT (CVO~B B2 independent judge, b98a06197): **5/6 SOLVED first batch** (B-03 fair fixed-incident MISS; B-05 out-grounded the corpus). B-01 + B-08 DROPPED (Andrew corpus-validity doubt). B-09..B-20 banked, CVO~B judging -> full B-02..B-20 aggregate IMMINENT.
   - **FINDING B (load-bearing, reconciled + owned):** solvers cd'd OUT of the sandbox into the REAL ws (B-02 x42) -> the by-construction sandbox was BYPASSED; isolation held via payload+content-audit (detective), NOT the certified preventive sandbox. Result VALID (content-audit CLEAN), but certified != executed. Root: sandbox-cwd is FUNDAMENTALLY incompatible with a tool-substrate on the real estate (comp-tools need the real ws). CTO WITHDREW confinement; refined principle: "prevention > detection ONLY where prevention doesn't break the measured substrate." Standing-suite fix = returned-content-audit (CVO~B) + optional uid-ACL; ~A runs an EMPIRICAL container-as-root test (does comp-kuzu/comp-freshness FUNCTION in-container) to decide preventive-vs-detective.

3. **NFRA_COMPTEAM -- chartered -> PRD landed + verified (COORDINATE).** LD-0237 + brief (7e57d4b0b). Andrew-direct: onboard the team to the MCP server -- (A) refresh the Desktop agent_org_blueprint_v1 kit w/ current CLAUDE.md + comp-which rail + the COMPROUTE/COMPUNIFY/COMPLEARN ranking (NO git functions); (B) partitioned kuzu/nessie/iceberg READ-areas via TSGRAPH portal-surface panel-clusters. CTO PRD 58a1f8738 (verified against artifact: strip-list gate, SCTY-entitlement read-scope, same-estate, COMPLEARN cold-start, no-git all bound). ONE macro (A+B workstreams), paired w/ SCTY (enablement x security). DIRECTIVE JUDGMENT: CTO + MSTR concur it warrants a dedicated Directive (new standing access class) -- SURFACED to Andrew, PENDING his elect (PRD proceeds under Andrew-direct-auth now).

4. **SES/CW alarm noise (carry from pre-reboot):** email muted (7 subs off) + AE TF-purge brief; COO stripped the critical-surface SQS poll from /drive (Andrew-direct, grounded) -- acknowledged as authorized, not drift.

5. **SPAWNS this session (creator/destroyer, all LD-0042/Andrew-direct, all RAVC'd COO):** CVO~B (COMPPROOF judge) + 5 AE ~A-~E (NFRA_COMP fleet) + 0.6.1_AE (INFREF v3) + base-DS (TAGATTR) + DT (49F DEV push, shipped v2.1.129 then idle-died) + DS~A (INFREF ROOT-2, then MDPF WS-E) + base-CVO (SCTY cert) + base-0.8.0 (SCTY corroborator) + 0.7.0~A (SCTY deploy) + 0.7.0 (SCTY sync). COTMVP-B FOLDED then found phantom (D1 stood-down 06-26; real target = client_directory emit) -- base-DS grounded it, I owned my stale-premise carry.

## MCP traffic (this window)
~60+ messages. Significant: COMPPROOF charter/PRD/verdict chain w/ CTO+COO~B+CVO~B (the isolation-mechanism debate + the 5/6 reconcile); NFRA_COMPTEAM charter->PRD->Directive-surface w/ CTO; ~11 LD-0042 spawn-requests from COO/COO~B (SCTY + INFREF + MDPF fleet) all executed+RAVC'd; the phantom-COTMVP grounding + ownership.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| registry-check.py (-all) | PASS | HOT+COLD project view for the NFRA_COMP* family assessment (Andrew ask) |
| build_sandbox.sh (COMPPROOF) | PASS | independently built+verified the true-sandbox (VERIFY PASS, forbidden absent, 20 citations scrubbed) before firing |
| harness.cheat_check / content-audit | MIXED | my run_meta audit false-positived (naive substring on 'true_root_cause') -- blind_run.py authoritative CLEAN 6/6; noted my audit tool = the success-shaped-wrong class again |
| tool_log ground-truth grep | PASS | grounded Finding B (B-02 cd-to-real-ws x42) -- disproved my own "from-sandbox" report |

**What worked:** grounding the tool_log / build_sandbox verify directly (not self-report) caught every wrinkle incl. my own false-alarm + the sandbox-bypass. **What failed:** my content-audit substring matcher over-fired (false-positive VOIDs); a Python cp1252 charmap crash on solver-output arrows (fixed w/ PYTHONIOENCODING=utf-8). **Gap:** none of the comp-tools front a "cross-run benchmark-result aggregate" -- COMPPROOF's blind_run.py is the bespoke one; also no comp-tool for disk/estate-storage pressure (surfaced: C: at 4.1% free).

## Current State (handoff -- zero prior context)
- **Watcher:** Monitor `bhxjr330e` live. Serial 0.0.0_AB_MSTR PID 11200.
- **Tier-0 law:** Const v1.5 / Stakes v1.5 / Directives v1.12; ledger at **LD-0237**, cycle CY-0128.
- **NFRA_COMPPROOF:** 5/6 first batch (CVO~B b98a06197); B-09..B-20 banked, judging -> full B-02..B-20 aggregate IMMINENT (surface to Andrew when it lands). B-01+B-08 dropped (Andrew doubt; CVO~B running a diagnostic on them out-of-band). Standing-suite isolation fix (returned-content-audit vs container-as-root) = ~A empirical test -> CTO ruling; THIS run stands.
- **NFRA_COMPTEAM:** PRD 58a1f8738 landed+verified, decomposing at COO (A1+B1 parallel, B2 gated on SCTY entitlements). **Directive elect PENDING Andrew.**
- **SCTY GO-live:** fully staffed (0.7.0~A deploy + base-CVO cert + base-0.8.0 corroborator); COO drives ledger close.
- **INFREF ROOT-2 / MDPF WS-E:** DS~A live (P1 cutover pace-setter, straight-RPS basis-switch w/ 0.5.0).
- **DISK:** C: 9.7GB free / 4.1% -- LOW. Likely culprit = /tmp/compproof_* sandbox copies (per-case filtered-repo cp). RECLAIM once the aggregate lands (Andrew-ok pending; recursive-delete = confirm-first).

## Next Steps
- **[0.0.0_AB_MSTR tomorrow]** pick up the TWO ITEMS above (comp-tool-health learning-loop view; cross-employee SQS bus) -- both are charter-candidates awaiting Andrew's go on shape. Also: relay Andrew's NFRA_COMPTEAM Directive elect; surface the full COMPPROOF aggregate; reclaim /tmp disk.
- **[2.0.0_SA_COO~B]** deliver the full B-02..B-20 aggregate + fold Finding-B into the program ledger.
- **[1.0.0_SA_CTO]** rule the standing-suite isolation fix on ~A's container-test; ready to scribe the COMPTEAM Directive on Andrew's elect.
- **[0.8.0_AE_CloudComp~A]** run the empirical container-as-root tool-function test.
- **[2.0.0_SA_COO]** SCTY deploy-ledger close (0.7.0~A + base-CVO cert); MDPF P1 cutover on DS~A's WS-E.

## Blockers
None blocking MSTR. NFRA_COMPTEAM Directive is an Andrew-elect (not a blocker -- PRD proceeds under Andrew-direct-auth). Disk-at-4% is a WATCH (reclaim on aggregate-land), not yet a block.
