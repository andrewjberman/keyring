# 1.0.0_SA_CTO -- MDPF flip-gate (3-pass 3/3 CLEAN) + A2 Andrew-reversal + cot deploy COMPLETE + OPAL_PRISTINE

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, IMPLEMENT
**Window:** 2026-07-21 ~2114Z (last log @f5114d6d9) -> 2026-07-22 ~0028Z | **Serial:** 1.0.0_SA_CTO (main-fabric CTO)

## Summary
Drove MDPF_REVAMP from disposition-execution to the flip's final edge: **3-pass 3/3 CLEAN (data verification COMPLETE)**, routing mechanism fully gated, held on ONLY the DE render-check. Handled an Andrew mid-flight REVERSAL (A2 FE-derive -> canonical-produce), a DS crash+reload (A1/A4 survived, ~15min cost), and 4 parallel Andrew-spawned lanes (cot deploy DONE, Tax-SMA, 49F runner, BD-replacement, safe-commit fix) -- each gated or deferred without dropping the flip. Created OPAL_PRISTINE (Andrew-direct). 7 commits.

## Key rulings / gates this window
- **A2 REVERSAL X->Y (Andrew-direct @2210Z):** "including aum-metrics AND aum-timeseries, from the canonical location in opal-data-assets and associated strategy" -> reversed A2 from FE-derive to a CANONICAL PRODUCED artifact (off the revamp aggregate, symmetric with A1). DE reverted the FE-derive to a repoint-only canonical read (net-FE ZERO, content-A/B preserved); routing back to exact-9. Recorded @707adebad.
- **Content render mechanism:** connectNulls FAILS on Recharts stacked areas (spike artifacts) -> DE surfaced it -> DROP-WHOLE-DAY-NULL-ROWS (honest-None data, render-only bridge; guards: pre-onset not fabricated, monthly last-non-null). @a11a7027c.
- **cohort_provenance:** derive from the opal-data-assets SOURCE-PATH (Andrew-direct) -- 49F SmartX/Schwab, inflection Eclipse/Orion, global omits. @1cae2ed4c.
- **census CO-SIGNED** (@386e3717a, CTO+CVO two-independent) + re-affirmed A2=Y. @91b962cad.
- **Routing = Option-C exact-9 direct behaviors** GATED (clone-the-catch-all, no L@E swap, b1-proven OAC; -json-verified additive; (b) scope-isolate to keep 0.5.0~A's WS-R3 out of the MDPF apply). 9 path_patterns confirmed EXACT verbatim.
- **safe-commit -F-read fix:** build/apply SPLIT (Andrew override of the defer) -- 0.8.0 built + CVO verified strictly-additive; the LIVE-APPLY is my gate, HELD to a post-flip quiet window.

## Compiler Tools
| Tool | Where | Result | Note |
|---|---|---|---|
| CTO independent S3 re-verify (python/boto3) | coherent-9 (gold/mdpf_revamp/) | CLEAN | aggregate identities 3 firms + coherence 3 firms + A1/A2 field-identity + A2 freshness + A4 identity + cohort_provenance lineage; my check's dict-vs-list bug self-caught+resolved |
| safe-commit surface-check + comp-pulse | 7 commits | PASS/CLEAN | doc/tracker/PRD files, 1-file vs 1239 danger nodes each |
| get_live_agents / get_org_summary / query_project | DT-liveness, TAXSMA state, project census | PASS | grounded DT dead-then-respawned; TAXSMA owner 0.5.0~A; 270-project scan |
| aws s3 ls / s3 cp / s3api | pull coherent-9 + served for the re-verify | PASS | applied-truth pulls |

**What worked:** parallelizing the flip-gate (render + routing built against DT's leg, not serialized) -- shaved the assembly. The 3-pass rigor caught real things: my pin-catch (COO staged a STALE pre-provenance pin, 7-key not 9; my live S3 re-verify grounded the current ETags) and all-3-legs independently hitting+resolving the cohort_provenance new-root. **What failed:** my S3 re-verify's cohort_provenance check assumed a dict (cp is a list of 427) -> 2 false-fails, resolved by introspection. **Gap:** DT's harness lagged the ledger on the cohort_provenance root (fixed @93382362c) -- instruments lag new data-shapes; the exemption-that-still-fails-a-real-extra is the right fix.

## MCP traffic
~55 dispatches this window (flip-gate coordination hub). Significant: the A2-reversal redirects (DS/DE/AE/CVO), the 3-pass trigger + verdicts (CTO S3 CLEAN + CVO CLEAN + DT CLEAN = 3/3), the pin-discipline catch (COO re-pinned to the live 9), the exact-9 routing GATE + path-pattern confirm, the cot-runner apply-gate -> CO-SIGN -> L4 accept -> tag (Andrew URGENT deploy COMPLETE), the safe-commit build/apply split ruling, OPAL_PRISTINE handoff + the BD-replacement/TAXSMA/49F deferrals.

## Blockers
None. MDPF flip HELD (deliberate gate) on DE render-check (last input) -> co-sign -> apply -> flip. cot deploy COMPLETE. Others deferred post-flip.

## Current State (zero-context handoff)
**MDPF_REVAMP flip -- at the FINAL EDGE. Durable: `org/critical_paths/MDPF_REVAMP_streak_tracker.json` (single-writer CTO, @a3bfa612e).**
- **Data VERIFIED: 3-pass 3/3 CLEAN** on the coherent-9 (CTO S3 re-verify + CVO re-derive + DT date-joined, 0 unexplained). ETags (live, @233355Z): aggregate 49f=a2e87f31/inflection=7ab6e93e/global=1b52211f, A4=7ef32112, A1(aum-metrics)=d69ac96a, A2(aum-timeseries)=38e9e8d4, account_dist=865919f2/afb964c4/b946d836. Staged at s3://opal-data-assets/gold/mdpf_revamp/.
- **Mechanism = Option-C exact-9 direct CF behaviors** (@803f8b1e7, 0.7.0). portal-auth: +OAC +assets-origin +9 exact clones-of-catch-all (before behavior 8). opal-assets: bucket-policy +exact-9-key GetObject SourceArn=EVTSA9VEHNZVH + publisher retarget. -json-verified additive. Apply --target-isolated (2 MDPF resources only; NOT 0.5.0~A's WS-R3). Rollback = remove-behaviors -> portal-v2 (untouched shadow). Publisher HELD/manual through cycle-1.
- **REMAINING GATE (ordered):** (1) DE render-check on the real coherent-9 (6-cell Value+Count x3 + A1 cards + A2 trend + coherence + content-A/B) -- **DE just re-spawned by Andrew (was swept)**; (2) COO co-sign on the live 9 (STAGED, re-pinned); (3) AE opal-assets-targeted apply -> AE BRINGS me get-bucket-policy live-verify + C-pre-flight BOTH-shapes (200+neg403+failsafe) BEFORE portal-auth; (4) **portal-auth flip = my FINAL GO**; (5) verify-9-URLs-serve-JSON + rollback-tested; (6) verify-before-serve cycle-1 (CVO). Andrew PUSH-NOW GO already given.
- **FE done:** A2 canonical-read (@aa8c0420) + content-A/B drop-null-rows (@5b1e44dc) on portal DEV, net-FE-zero, DT-gated for promote.

**cot-rebalancer-runner (WS-E WS-1) -- DEPLOY COMPLETE** (Andrew URGENT @b5be0f680): apply 10-add/0/0 + 0-diff + Rule-22a isolated-1-ARN (GetSecretValue-only/PutSecretValue-deny/cottonwood-writes/49f-deny) + L4 no-stub live (5 distinct pages, 296-across-14 live, gates fired) + tag v0.1.0. CVO issued.

**OPAL_PRISTINE created** (@4e734f34f): PRD + JSON + registry; 5 WS (generator / gate-flips / burn-down / debt-score / sharpen-detectors); CVO verify leg. For COO decomposition POST-FLIP.

## Next Steps
- [1.0.0_SA_CTO] GATE the flip: DE render clean -> confirm COO co-sign covers the live 9 -> AE targeted apply -> verify get-bucket-policy + C-pre-flight -> **portal-auth flip FINAL GO** -> verify-before-serve.
- [0.4.0_DE_ClientPlatform] (re-spawned) run the 6-cell render-check on the coherent-9 staged real data -> report screenshots.
- [2.0.0_SA_COO] co-sign same-turn at the assembled gate (pinned to the live 9); decompose OPAL_PRISTINE + WS-E TOs post-flip.
- [1.0.0_SA_CTO] POST-FLIP: pivot DS to the 49F-runner (last-mile field-emit + D1 + N=3); ratify+register BD-replacement (D5/D2/D6); go-live the safe-commit fix (quiet window); gate the TAXSMA WS-R3 apply + the PFMG_TAXSMA banner; universal-calendar decompose.
- [ANDREW] pending: BD-replacement D1 (365-vs-252 business call); Bump/Macy TAXSMA egress.
