# ADVI_NNAATTR.TO-2 -- DE-leg build (profile-leg) + pre-build grounding
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Agent:** 0.4.0_DE_ClientPlatform · **TO:** ADVI_NNAATTR.TO-2 (pending) · **Portal DEV commits:** `6e95f05c`, `b24cd040`

## Current State
TO-2 DE-leg: the FE NNA repoint to the all-roles `advisor_nna_canonical`. Built the profile-leg + bounded the rest; the verify-dependent piece rides CVO's #9 (tomorrow-AM). Ran the mandated pre-build grounding (CVO-validated) before touching the financial-display surface.

**Pre-build grounding (gated the build):**
- `/molecule` + `/seams` on `advisor_nna_canonical` fee-split, ground-truthed against the SERVED S3 objects (commit `c66b01c24`): **bd/49F STALE** (06-17, per-advisor fee_paying/no_fee = NULL -- = CVO P1, D_00f silent no-write, DS fix tonight); **inf FRESH** (06-18, fee-split populated, firm QTD F4 tie-out exact to the cent). CVO independently re-ground-truthed -> VALIDATED to-the-cent + GO'd build-with-PERMANENT-null-fallback (191618Z).
- Andrew routed the build-pacing decision to CVO -> CVO adjudicated (195352/195545Z): GO option-a (commit profile-leg now), defer override-removal to #9 (outcome-gated), scope-bound CONCUR (repoint NOT feature-add).
- FE sweep (comp-toolkit -- `pipescript advi-bd/advi-inf` + `comp-routes behaviors` + boto3 freshness sweep): the stale/silent-no-write class is ISOLATED to `advisor_nna_canonical` (all other bd/49F + all inf FE artifacts fresh). One new finding (ClientsTab `getHeaderMetrics` reads dead `artifacts/summary/` path, 404 both firms) -> routed to COO as a DE carry-forward (193344Z), NOT folded into TO-2.

**What landed (portal DEV):**
- **AdvisorPublicProfile** (`6e95f05c`) -- F-1b/F-1c + F-3 core. Generalized the ADVI_INFMVP.F5 `feeView==='all'`-only canonical override: `advisor_nna_canonical` is now the PRIMARY Exec-Summary-Flows source for **all|fee_paying|no_fee** (reads `canonicalFlows.fee_paying`/`no_fee`/total). **F-3:** inf's INF_D_00c never emitted per-advisor `fee_breakdown`, so inf fee-views fell back; canonical windows now carry populated inf fee_paying/no_fee (verified served) -> inf exec-flow fee-split renders from canonical. **PERMANENT null-fallback** (typed non-null but runtime-nullable -> null-coalesce to legacy/aggregate, never NaN/blank). `tsc --noEmit` clean.
- **DistributionTab** (`b24cd040`, comment-only) -- grep-documented the AC4 override deferral.

**Confirmed (not assumed, per CVO):**
- **AdvisorAnalytics** already canonical-primary: `pickNnaCanon`/`pickInflowsCanon`/`pickOutflowsCanon` handle all/fee_paying/no_fee (timeseries sub-streams + synthetic-ratio for inf, which lacks per-period timeseries fee-split -- a separate DS backfill-brief, NOT TO-2 FE scope, NOT regressed); `nnaPeriodData` prefers the bucket-summed canonical series. No change needed.
- **DistributionTab** has NO fee-view dimension (`feeView`/`fee_paying`/`no_fee` grep-empty) -> no fee-split repoint applies. Continuous already canonical-primary (60%-flow-loss fix landed P2.W2). The adv-donut INFMVP.F5 override sources canonical w.nna TOTALS (populated even in the stale vintage) + is null-guarded -> canonical-primary today; KEPT pending #9.

## Blockers
None. The override-removal (AC4) + cross-route-identity VERIFY ride **CVO's #9** on the fresh 06-19 bd artifact (outcome-gated: legacy `views.nna[period].adv` == canonical `w.nna` per window x advisor -> remove if equal, else override is load-bearing + finding). Cross-route identity is served-truth = CVO #9, not self-reported.

## Next Steps
- **[3.0.0_SA_CVO]** #9 tomorrow-AM: cross-route identity + the legacy==canonical totals-equality gate (AC4 folded in) + the F4 tie-out per window x fee_view (Peter + 49F control). On its outcome I do the override-removal post-pass (or it's a finding).
- **[0.4.0_DE]** post-#9: remove the override if #9 confirms equality; then RAVC2-close TO-2 (profile-leg + the verified DT cleanup).
- **[0.4.0_DE carry-forward]** the ClientsTab `getHeaderMetrics` dead-path fix (DE lane, post-TO-2, COO-queued; check headerTotal superseded-by-dashboardQuery -> remove, else re-path + retry:false).
- **[0.4.0_DE]** P2-1 close-verify still armed for AE's P2-2 materialize (event-driven).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-which | served/producer/consumer of advisor_nna_canonical | -> comp-pipescript io / pipescript --resource |
| pipescript | advi-bd (19 threads), advi-inf (14) | estate map; stale-class isolation confirmed |
| comp-routes behaviors | advisor-intelligence routes | artifacts/* -> opal-data-bd literal (no rewrite); confirmed the 404-key mapping (no false negatives) |
| comp-pipescript io | D_00f / INF_D_00f | READS mapped; WRITES (none detected) -- dynamic-write blind spot |
| comp-validate | D_00f / INF_D_00f | NO config -> value-ungated (gap routed to CVO/DS) |
| comp-transform schema-check | DistributionTab / AdvisorAnalytics / AdvisorPublicProfile | canonical reads present; type AdvisorNnaLeaf carries fee_paying/no_fee |
| boto3 head/get + gzip | FE-served firm artifacts, bd + inf | freshness sweep: advisor_nna_canonical bd STALE (isolated); inf all fresh + F4 tie-out live |
| tsc --noEmit (portal) | -p tsconfig.app.json after AdvisorPublicProfile edit | exit 0, clean |
