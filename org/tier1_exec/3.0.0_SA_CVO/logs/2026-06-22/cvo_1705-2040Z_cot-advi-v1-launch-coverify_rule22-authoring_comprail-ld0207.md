# CVO 2026-06-22 ~1705-2040Z -- COT ADVI v1 launch co-verify (both gates CLOSED) + Rule 22 authoring complete + comp-rail course-correct -> LD-0207

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, TRACE

Window after the 1345-1705Z log (e101bc0ea). Five arcs; the headline is the COT ADVI v1 launch co-verify (caught + closed two real launch-gates). All grounded vs live/served (Rule 22), with one owned over-claim that became governance.

## 1. Rule 22 authoring COMPLETE
- grounding: emission-format DRAFT (788ffa3c0) -> CTO RATIFIED no-change -> skill-fold COMMITTED (e71e9d13e): the `grounding:` field folded into `.claude/skills/{molecule,seams,verify-channel}` (per-CAUSAL-claim SOURCE-CONFIRMED vs INFERRED, reserved-words gated, STATE-findings exempt), cross-tool lane granted + gate-note. TO-5 coverage-audit backstop = mine. Memory: feedback_two_grounding_modes_state_vs_mechanism.

## 2. COTETL/ETFS formal closes
- Explicit cert-all-5 verdict line issued (CTO won't infer it) -> CTO STAMPED ACCEPTED -> $24M AUA-freeze formal close. Both flags source-confirmed pre-existing (nna-anomaly = onboarding-recency not fix-introduced [git show 5c80bf6ca diff scope]; the $2M = D_00 707->694 relationship-filter).
- 13-unmapped CO-VERIFY (DS's quantitative investigation): VERIFIED, independently reproduced TO THE CENT -- holdings 707 minus transaction-derived dim 694 = exactly 13 unmapped = $2,013,374.15 (6 manual-asset + 7 empty-cash, all NEW accts ~06-11). Andrew's snapshot-vs-txn-delay hypothesis CONFIRMED + refined (per-NEW-account lag, not feed-wide). Closes confirm-the-13.

## 3. ADVI-COT backend audit + spec (bf9aa0926)
- Deeply-comprehensive audit (daily-ETL + backfill/artifact-store + FE integration). FINDING: COT ADVI v1 BUILT+WIRED+access-gated+data-fresh@06-18 = a Distribution-centric v1 (OUTCOME-B, advisor/Books deferred-by-design). Backend flags A (prices-stale doesn't hit AUA: B_00 snapshot uses BD-mv) + B (06-09-stuck account_gains/C_00/nna_validation NOT consumed by v1) resolved. MISS owned: did NOT verify the FE-fetched partner_analytics artifact EXISTS (arc 4).

## 4. COT ADVI v1 LAUNCH CO-VERIFY -- BOTH GATES CLOSED (the headline)
COO-driven launch (Andrew HIGHEST PRIORITY). Two gates, both mine to verify:
- **gate#1 cross-firm ISOLATION -- CLOSED, runtime double-confirmed (me + AE).** I exercised it MYSELF on the live portal (opalinvest.dev -- the live alias; portal.opalinvest.com is a STALE no-DNS value, AE's catch): logged in as the cottonwood smoke cred, ran 6 cross-firm vectors (header_metrics/cumulative_chart/mix_summary x ?firm=/?firmId= x 49financial/inflection) -> ALL firm_id=cottonwood, ZERO leak; no-token 401. Mechanism: firm JWT-PINNED (param ignored, tamper-immune) + is_authorized artifact-403 (opal-partners-data:271-285,1725). Did NOT cert on AE's report alone.
- **gate#2 partner_analytics -- CLOSED.** DE smoke surfaced the COT v1 Distribution body renders EMPTY (partner_analytics_quarterly ABSENT). My ruling: P1 SERVED GAP, source-confirmed end-to-end (FE no-fallback + router passthrough-404 [handle_scoped_partner_analytics:786-792] + artifact-absent). DS emitted (244974718 cot-runnability + c5bc7ba49 geo-reconcile); I live-200-cert'd (was 403, now 200, populated views, cross-firm no-leak holds). GEO-DISPLAY: my "Unassigned slice reconciles" was a DATA-layer over-claim (DE's render: donut showed %s-of-$370.8M under $395M label, $24.5M invisible). Andrew chose FIX-FIRST -> DS added the explicit "Not state-attributed" segment -> RE-CONFIRMED both layers: 15 segments incl $24,493,456.71/6.20%, sum=$395,300,238.06 exact, TX 82.0%, donut reconciles on-view (DE pixel + my live data). d01-launch-emit ledger CLOSED (0d8359230).

## 5. comp-which-first / Rule-22 directive (Andrew) -> my course-correct -> LD-0207
- Andrew-direct: "follow rule 22 + religiously use compiler tools when poking around." Honest self-assessment: I used comp-tools for estate/IAM/routes/blast but leaned RAW Grep/Read/Bash-grep for FE+lambda SOURCE-poking (HUD nudged, I proceeded raw; a couple gated Bash-greps w/o # rail-checked). The geo over-claim's ROOT = same miss (grounded the DISPLAY on the artifact-data layer, not the comp-transform render-path). Course-corrected IN ACTION: comp-which -> comp-transform schema-check DistributionTab (the canonical FE-source tool I should have led with). Memory: feedback_comp_which_first_for_source_poking_and_render_vs_data_layer. Relayed the directive to the team (COO enforcing across DS/DE/AE).
- **-> LD-0207 (Andrew-APPROVED, 3a383ffd5):** my raw-Grep'd-DistributionTab over-claim is the ANCHOR for a comp-rail HARDENING batch -- KEY INSIGHT "a comp-rail SKIP IS a Rule 22 grounding SLIP" (Rule 21=lookup, Rule 22=reasoning, one thesis; comp-transform/comp-blast ARE the mechanism-grounding tools). CTO proposes the 3-gate batch (broad-grep DENY / native Grep-Glob GATE on estate-coupled paths / comp-transform+comp-blast mandatory in grounding:) + COO decomposes the NFRA_COMPRAIL hardening TO + TO-5 measures.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| pipescript advi-cot | COT estate spine (producers->served->frontend) | the cot-pipeline map + the FE cottonwood tenant (mounted-reachable) |
| boto3 (operational) | artifact-store survey + served-state + the live authed curl exercises | all STATE grounded vs served/live |
| comp-blast canonical_prices | prices->AUA consumer check | B_00 consumes prices BUT snapshot path uses BD-mv (flag-A resolved) |
| comp-iam gaps | cottonwood serving cross-firm IAM | ALLOW+Deny-coexist = isolation guardrail (serving effective) |
| comp-routes | deployed portal/API URL discovery | d2n2nzpeqf34ge.cloudfront.net + auth-map |
| comp-which -> comp-transform schema-check DistributionTab | FE render-path (the course-correct) | canonical FE data-flow tool (vs my prior raw-Grep) |
| live authed curl (opalinvest.dev) | gate#1 isolation + gate#2 live-200 + geo re-confirm | runtime-confirmed: zero-leak, 200, reconciles $395,300,238.06 |

**What worked:** the LAYERED grounding (data-cert vs render-pixel) + the INDEPENDENT live re-exercise (not certing on AE's report) caught my OWN over-claim before launch + double-confirmed isolation. **What failed:** raw Grep/Read on FE/lambda source-poking instead of comp-which-first -> the geo-display over-claim (data inferred as display) -> DE's render caught it. **Gap found (institutionalized LD-0207):** the Rule21<->22 linkage was unenforced (raw-grep on estate-coupled source = ungrounded mechanism); comp-transform/comp-blast now mandatory in the grounding: field; broad-grep DENY. Andrew-approved.

## Blockers
None for CVO. COT go-live gated only on Andrew's user-list (provisioning, not a defect).

## Current State (handoff -- zero prior context)
- **COT ADVI v1 = TECHNICAL + DISPLAY READY (CVO-cert).** BOTH gates CLOSED: gate#1 cross-firm isolation (runtime double-confirmed me+AE on opalinvest.dev; firm JWT-pinned; 6 vectors zero-leak); gate#2 partner_analytics (DS 244974718 + c5bc7ba49; live-200 reconciles $395,300,238.06; geo donut 15 segments incl "Not state-attributed" $24.49M/6.2%, TX 82.0%; data + render-pixel confirmed). d01-launch-emit ledger CLOSED (0d8359230).
- **PENDING go-live:** Andrew's user-list -> COO/AE provision `opal-users-v2` firmId=cottonwood -> CVO runs the live-render + AC2 isolation spot-check on the FIRST REAL session (near-certain: same FE code + the live data I curl-confirmed) -> go-live.
- **Portal facts:** live alias = `opalinvest.dev` (API same-origin -> d2n2nzpeqf34ge.cloudfront.net); `portal.opalinvest.com` is a STALE no-DNS value. Smoke cred (user@cottonwood.com) reverted by AE post-exercise.
- **Rule 22 authoring COMPLETE:** emission-format CTO-ratified (788ffa3c0); grounding: field in .claude/skills/{molecule,seams,verify-channel} (e71e9d13e); TO-5 coverage-audit = CVO.
- **LD-0207 comp-rail hardening APPROVED** (3a383ffd5): CTO proposes gate-batch (announce-then-enforce) + COO decomposes NFRA_COMPRAIL hardening TO + TO-5 measures. Anchor = my DistributionTab over-claim.
- **Open (non-blocking):** COTETL cleanup nightly-verify (DS confirms served partner_analytics reconciles fresh-date tonight; AE chained D_01 before D_04 in opal-cot-gold-run c19d40212 to avoid vintage skew); polish-backlog (the Unassigned slice "0 Accounts" relabel; state-attribution to shrink the 6.2%).

## Next Steps
- **[3.0.0_SA_CVO]** On provisioning: live-render + AC2 isolation spot-check on the first real cottonwood session -> go-live confirm. Verify the COTETL cleanup nightly (tomorrow's served partner_analytics reconciles fresh-date). TO-5 coverage-audit continues (now incl LD-0207 measures).
- **[2.0.0_SA_COO]** collect Andrew's user-list + provision -> trigger CVO spot-check; decompose the NFRA_COMPRAIL hardening TO (LD-0207).
- **[1.0.0_SA_CTO]** NFRA_COMPRAIL hardening gate-batch (LD-0207, announce-then-enforce); ETFS_AVGCAP PRD (gated on Andrew priority).
- **[0.4.0_DS_ClientPlatform]** COTETL cleanup nightly-verify; polish-backlog (0-accounts relabel, state-attribution).
- **[Andrew]** the COT user-list (go-live trigger); ETFS priority-call.

-- 3.0.0_SA_CVO
