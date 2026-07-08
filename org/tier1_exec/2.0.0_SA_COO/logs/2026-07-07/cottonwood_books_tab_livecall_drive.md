# COO Session Log -- Cottonwood Books-tab live-call drive + cot-incident coordination (2026-07-07T18:22Z -> 2026-07-08T03:20Z)

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE

## Window

Restart after the Huntress/Rio reboot (post `session_close_handoff_COO_1822Z.md`) through the ADVI_COTPPLADVFIX Cottonwood Books-tab live-call delivery drive. ~9h wall, much of it event-gaps.

## Summary

Restarted the COO session (watcher + /drive, then /drive PAUSED per Andrew). Coordinated the cot DATEMODE incident into a clean HOLD (Andrew took the thread + authored a PRD). Decomposed ADVI_COTPPLADVFIX (Andrew-direct P0). Then drove the LIVE-CALL delivery of the Cottonwood single-synthetic-advisor Books tab through a multi-fix fire-drill (DS 3 durable producer fixes + DE frontend wiring + a source-grounded L3 registry-hole fix). Data leg + L3 fix landed + durable; **the PROD promote was GO'd by Andrew but never executed by DT (stranded -- see Current State).**

## Work done

- **Startup:** /watcher (registered 2.0.0_SA_COO PID 10284, Monitor bmb287xri), org/XXX.md protocol, committed the reviewed AE~B SCTY secrets-rotation-runbook closure (c1e87f4be). Armed /drive (cron 720b3631) then CANCELLED it per Andrew ("hold" on the cot thread).
- **cot DATEMODE incident (HELD):** Andrew took the whole bronze/holdings-freshness thread + is authoring a PRD; directed HOLD on all driving. Reconciled the cross-agent state cleanly: CTO issued a source-grounded per-table ruling (INPUT to Andrew's PRD, not a work order) + held its AE re-provision GO; CVO stayed verifier-only; closed the CTO<->COO B_01/AE-GO seam CVO flagged. No cot code moved. AE never respawned (Andrew-direct "no AE live").
- **ADVI_COTPPLADVFIX decomposed + driven (Andrew-direct P0 via CTO GO):** authored TO-1 (DS synthetic-advisor inject), TO-2 (DE Books-tab wiring), TO-3 (doc), + project JSON; commit 77f7414b4, pushed CLOUD. Q1 RESOLVED = SUPERSEDE COTMVP-B (complete, Books-disabled, no conflicting view). Respawn-requested DS + (later) DE + DT via MSTR.
- **Live-call fire-drill (the bulk):** re-scoped from nightly-validate to an Andrew-authorized ad-hoc gold recompute (~74s chain). Drove through, in order:
  1. DS injected the single "Cottonwood Capital Advisors" advisor at A_01 (0bb589a29) -- but D_02 (49F clone) crashed exit-1-optional on a missing 49F `implementor` col -> DS fixed D_02/D_03/D_04 schema-drift tolerance -> book.json served ($434.17M / 220 clients / 825 accts).
  2. Card blocker: dashboard.json employee_leaderboard=null (fee-gated off C_08 cot has none of) -> DS synthesized the single advisor in D_04.build_firm_dashboard (442b00a17).
  3. Drill hang: platinum/firm/leaderboard.json never emitted for cot -> DS emitted it in D_04.build_leaderboard (f75998b62). All 3 fixes DURABLE (nightly-reproducing, self-limiting to cot's null case).
  4. DE: found the PRD's "flag flip" is a no-op (cottonwood uses a bespoke dispatcher, never reads layout flags) -> wired the shared BooksTab into cottonwood/index.tsx config-driven, 0109fecb (tsc/eslint/schema-check clean, cottonwood-scoped, zero 49F/inf blast).
  5. **L3 (client-click) diagnosed to a 1-attribute registry hole (source-grounded):** opal-partners-data lambda get_firm_bucket -> DynamoDB opal-users-v2 FIRM#{firm}/META.s3Bucket; FIRM#cottonwood was MISSING s3Bucket (inf=opal-data-inf, 49f=opal-data-bd have theirs). Handler reads gold/entities/clients/{bare-z-key}/detail.json (exists for cot); DE confirmed bare-key-consistent end-to-end (220/220 match, no rel_ prefix). Fix = necessary+sufficient.
- **Andrew "A, go":** WROTE s3Bucket=opal-data-cot onto FIRM#cottonwood/META (additive, verified, guarded attribute_exists(PK)); GO'd DT to promote 0109fecb -> v2.1.133 present-as-is.
- **Side:** answered Andrew's cot-gold runtime question (chain ~74s SSM RunCotGoldChain; ~2-4min cold-boot incl. pip-install). Grounded the "Group B / 49F transaction-engine is dead weight for cot" architecture hypothesis (comp-pipescript io on B_00-B_03 + canonical_prices) -- validated the direction; routed to CTO's gold-review (17 defects catalogued). Held the COO~B NFRA lane carve-out (protected 0.4.x base lanes DE/DS/DT from NFRA respawn collision -- COO~B fully compliant, held its respawns).

## MCP traffic

~35 messages handled (heavy fire-drill coordination). Significant: HOLD-reconcile to CTO+CVO (cot DATEMODE); ADVI_COTPPLADVFIX TO-1 GO (DS) + TO-2 GO (DE); 3 MSTR respawn-requests (DS, DE, DT -- all provisioned); the live-call fast-track re-scope + 3 producer-fix RAVC loops (DS); DE render-verify BROKEN-CORE catch (held the promote correctly) + the complete drill-chain map; DT warm-readiness + promote GO; COO~B lane carve-out (ACK'd + compliant).

## Compiler Tools

| Tool | Where | Result |
|---|---|---|
| comp-which | routed the runtime + architecture questions | PASS (near-tie -> chose by concern; confirmed no tool covers runner exec-duration) |
| comp-pipescript io | B_00/B_01/B_02/B_03 + build_canonical_prices | PASS (Group B DAG + consumers; bd-graph -- cot under-instrumented, grounded cot-actual on source) |
| deploy_ledger check --red | /drive cycle | PASS (2 OPEN AE legs: globgrph-stitch PAST-WINDOW [Andrew-only PAT], scty-premcp in-window) |
| fabric-check | /drive 2b.0 | PASS (post-reboot Tier-1-only; drove worker respawns) |

**What worked:** comp-pipescript io cleanly enumerated the Group B transaction-engine consumers for the architecture question. **What failed:** none blocking. **Gap found:** cot is under-instrumented in the estate graph (advi-cot = 1 pipescript thread) -- the cot-actual consumer + L3-lambda + registry questions all had to be source/live-grounded (comp-tools read the bd graph). Also no comp-tool surfaces runner EXECUTION duration or a lambda's internal firm->bucket registry lookup (both rail-checked to raw aws).

## Files modified

- see commit messages: c1e87f4be (SCTY closure), 77f7414b4 (ADVI_COTPPLADVFIX 3 TOs + JSON + MDPF_COTMDL.TO-1 close).
- **Non-commit live change:** DynamoDB opal-users-v2 FIRM#cottonwood/META -- ADDED s3Bucket="opal-data-cot" (the L3 lambda-routing fix; verified persisted at 03:20Z).

## Blockers

- **STRANDED PROD PROMOTE (evidence-cited):** Andrew GO'd "A, go" (~00:40Z); I dispatched the promote GO to 0.4.0_DT_ClientPlatform (0109fecb -> v2.1.133). DT was STALE at dispatch. As of 03:20Z: origin/PROD still = f3ce600c (v2.1.132), NO portal-v2.1.133 tag, NO DT promote-result message. => DT never executed /prod-deploy; the promote is stranded (GO'd-but-not-started -- NOT half-landed; PROD is cleanly at v2.1.132). Per the NEVER-half-deploy discipline this is surfaced loud, not silent.

## Current State (handoff -- zero prior context)

- **ADVI_COTPPLADVFIX Cottonwood Books tab -- DATA + L3 fix DONE + DURABLE; PROD promote NOT done:**
  - Served (opal-data-cot), all nightly-reproducing: gold/entities/advisors/cottonwood_capital_advisors/book.json (220 clients / 825 accts / $434,165,337.25 == firm headline); platinum/advisors/cottonwood_capital_advisors/summary.json; platinum/firm/dashboard.json employee_leaderboard[0] (the N1 card); platinum/firm/leaderboard.json (the drill); gold/entities/clients/{z-key}/detail.json (L3). Producer commits (DS, deployed to opal-data-cot/code/gold/): D_02 crash-fixes + D_04 build_firm_dashboard (442b00a17) + D_04 build_leaderboard (f75998b62). TO-1 CTO-closed.
  - L3 lambda routing FIXED + live: opal-users-v2 FIRM#cottonwood/META.s3Bucket = opal-data-cot (affects DEV + PROD -- shared registry).
  - Frontend code (0109fecb, the config-driven BooksTab wiring, Books admin-gated) is on origin/DEV (deployed to the DEV env) -- so the FULL tab incl. L3 works on the DEV portal. **It is NOT on opalinvest.dev PROD** (promote stranded).
- **cot DATEMODE / holdings-freshness:** HELD -- Andrew's PRD in flight. Nothing moving. The nightly gold chain runs exit-0-but-degraded (allocations 0-rows -> zeroed fee/tax detail panels; the A_00 incremental corruption -> 12% null names / 100%-taxable). Present-as-is (Option A) was chosen for the call.
- **cot A_00 + 17-defect gold-review:** CTO catalogued (org/tier1_exec/1.0.0_SA_CTO/deliverables/cot_gold_bughunt_reports/, 68dfcd87d) -- the cot gold runner is a 49F clone actively corrupting served data; awaiting Andrew's container/priority ruling (dedicated hardening project vs fold). DS lane.
- **MDPF_COTMDL:** firm HOLD (Andrew: "nothing to do with model portfolios at this time" -- cot runs no model program, 0% strategy_id).
- **Fabric:** COO~B running the NFRA full-program (Batch-A fleet spawned, 8 workers up); 0.4.x base lanes (DE/DS/DT) idle-STALE, TO-1/TO-2 closed on their side. /drive cron PAUSED per Andrew.

## Next Steps

- **[Andrew / 0.4.0_DT_ClientPlatform] Decide + finish the stranded PROD promote.** The live call is long over (~7h), so re-confirm whether to promote 0109fecb -> opalinvest.dev (v2.1.133) NOW. If yes: respawn DT (STALE/idle) + run /prod-deploy (rollback base v2.1.132 / f3ce600c). Everything works on DEV; only the PROD promote remains. If no: the tab stays DEV-only until Andrew calls it.
- **[Andrew] cot container ruling** for the A_00/17-defect gold-review systematic hardening (DS lane).
- **[0.4.0_DE_ClientPlatform] Post-call harden** ClientsTab:760 (infinite spinner on any leaderboard 404 -- all tenants, shared-component, needs 49F/inf regression).
- **[COO] Bank** the SCTY rotation-runbook coupling note: AGENTBUS-S3 now reads the SCTY RS256 identity root -> list it as a downstream consumer on key rotation.
