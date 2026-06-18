# MOLECULE + SEAM: advisor_nna_canonical.json (per-advisor fee_paying/no_fee split)   (scale: MESO)
**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, TRACE

**Agent:** 0.4.0_DE_ClientPlatform · **For:** ADVI_NNAATTR.TO-2 FE all-fee-views repoint pre-build grounding · **Ground-truthed against the SERVED S3 objects (boto3), not source/self-report.**

## Unit + expected role
The firm-scoped served JSON `platinum/firm/advisor_nna_canonical.json` -- the canonical advisor-NNA contract TO-2 repoints the ADVI NNA surfaces onto. Per-firm-pipeline producers (firm-separated): `data/black_diamond/scripts/gold/D_00f` -> `opal-data-bd` (49F); `data/inf/scripts/gold/INF_D_00f` -> `opal-data-inf` (Inflection). Expected contract (brief advi-infmvp-f5-...-20260528): `{firm,advisors:{windows:{QTD,YTD,MAX,1Y,3Y,q_current,q1,q2,q3 -> {nna,inflows,outflows,account_count,fee_paying:{...},no_fee:{...}}}, series:{weekly,monthly,quarterly}}}`, fee_paying+no_fee==total (F4 tie-out). **The per-advisor `windows[w].fee_paying`/`no_fee` is the load-bearing repoint target.**

## 1. Composition (vs declared)
Producer code computes the per-window fee_paying/no_fee split (F4); FE type `AdvisorNnaLeaf` (types.ts:2173) carries `fee_paying:{nna,inflows,outflows,account_count}` + `no_fee:{...}` -- so the repoint to `canonicalFlows.fee_paying.nna` is TYPE-SUPPORTED (mechanical-OK). Matches the brief contract.

## 2. State (LIVE served snapshot -- the crux)
| Firm | served object | LastModified | data_as_of | encoding | advisors | per-advisor fee-split |
|---|---|---|---|---|---|---|
| **bd/49F** | opal-data-bd/...advisor_nna_canonical.json | **2026-06-17 05:04Z = STALE** | 2026-06-15 | **gzip** | 61 | **NULL** (Travis QTD nna=$4,139,233.58 present; fee_paying.nna=None, no_fee.nna=None for QTD/YTD/MAX) |
| **inf/Inflection** | opal-data-inf/...advisor_nna_canonical.json | 2026-06-18 14:43Z = FRESH | 2026-06-17 | plain | 4 | **POPULATED** (all 4 advisors non-zero QTD+MAX; firm QTD fee_paying −3,520,855.93 + no_fee 3,703,454.63 = 182,598.70 = nna -> F4 tie-out holds LIVE) |

The 49F (bd) served artifact is STALE -- the 06-18 nightly D_00f run silently no-wrote (= CVO P1, DS owns; rc=0 no-write, runtime error in the new F-0/F-1a path). **The per-advisor fee-split -- exactly the TO-2 repoint target -- is NULL in the current 49F served vintage.** Inflection's fresh artifact proves the post-fix shape (per-advisor split populated + tie-out).

## 3. Position in the chain
Producers D_00f(bd)/INF_D_00f(inf) -> served opal-data-{bd,inf}/platinum/firm/advisor_nna_canonical.json -> FE `getAdvisorNnaCanonical` -> AdvisorPublicProfile (L320, feeView='all'-gated override), AdvisorAnalytics (L207, already canonical-primary), DistributionTab (L925/L2595, cohort='adv'-gated donut override). Seams to /seams: producer->served (the write), served->FE (the read+repoint).

## 4. Behavior (deployed/evidenced)
bd D_00f 06-18 ran 6.1GB/fresh inputs but the WRITE silently didn't land (LastModified stuck at 06-17; the "never trust rc=0" class). inf INF_D_00f wrote fresh 06-18 14:43Z. comp-pipescript io reports "WRITES: (none detected)" for BOTH producers -- the I/O manifest can't see the dynamic S3 write (a detection gap relevant to the silent-no-write).

## 5. Semantic quality (sharp)
inf: fee-split non-degenerate (4/4 advisors non-zero) + F4 tie-out exact LIVE. bd: per-advisor fee-split NULL (stale vintage); Travis canonical QTD = $4.14M (the correct side of the $4.14M-vs-$6.95M divergence). `comp-validate` finds NO value-config for either producer -> the artifact is **value-ungated** (NO_CONFIG/UNVALIDATED) -- which is why the stale/null-split slipped past with no alarm.

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| 49F served STALE + per-advisor fee-split NULL | DIG (CVO P1, DS-owned) | LastModified 06-17; Travis fee_paying.nna=None | the repoint target is null on 49F until tonight's D_00f fix lands |
| per-advisor fee-split null on bd but populated on inf | DIG -> repoint design | served reads | repoint MUST null-coalesce during the stale->fresh window or 49F fee-views render blank |
| bd gzipped, inf plain JSON | WATCH | ContentEncoding: gzip (bd) vs none (inf); both <10MB | cross-firm encoding asymmetry (CloudFront-10MB pre-gzip class) -- not size-forced; why divergent? |
| producer has NO comp-validate value-config | WATCH | comp-validate no-match both | silent stale/null-split was value-ungated; DS's write-success-sentinel catches no-write but not a populated-fee-split assert |
| comp-pipescript io "WRITES: (none detected)" | NOTE | both producers | manifest blind to the dynamic write -- relevant to silent-no-write detection |

## SEAM verdict: producer -> served -> FE consumer (fee-split)   (scale: MESO)
| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL | PASS | FE path resolves to the served key; FE type AdvisorNnaLeaf carries fee_paying/no_fee; field physically crosses | -- |
| DECLARATIVE | FAIL (= CVO P1) | believed (TO-2/brief): "F-1a deployed, all-roles canonical field exists SERVED"; actual: bd SERVED stale 06-17, per-advisor fee-split NULL (06-18 write silently failed) | true for code + inf-served; NOT for bd-served |
| SEMANTIC | PASS (inf) / STALE-FAIL (bd) | inf: fee-split populated + F4 tie-out live; bd: stale vintage + per-advisor fee-split null | bd resolves on tonight's D_00f redeploy + nightly |

**Verdict:** inf seam SOUND; **bd/49F seam BROKEN@DECLARATIVE+SEMANTIC** (stale, known CVO P1, fix lands tonight -> re-verify tomorrow-AM on the fresh 49F served artifact).

## Assessment + opinion (-> CVO to validate)
1. **TO-2 FE repoint is SAFE TO BUILD now** -- the fee-split target is structurally present + type-supported; AdvisorAnalytics is already canonical-primary; the AdvisorPublicProfile `feeView==='all'` gate + DistributionTab `cohort==='adv'` gate generalize cleanly to canonical-primary across fee-views.
2. **The build MUST keep a null-safe fallback** (canonical fee_paying.nna null -> fall back to legacy `entry.fee_breakdown` / aggregate), because the 49F served vintage has per-advisor fee-split = NULL until tonight's fix. FE-on-DEV + DT-batched PROD-promote bounds the exposure, but the null-coalesce is the correct defensive measure regardless.
3. **The cross-route-identity + fee-split-populated VERIFY runs on tomorrow's FRESH 49F served artifact** (the TO-2 gate, as specified) -- NOT today's stale vintage. inf is already verifiable now (fresh).
4. **Gap to consider:** the producer is value-ungated (no comp-validate config). DS's write-success-sentinel catches the no-write; a populated-fee-split / F4-tie-out value assert would catch a null/degenerate split that lands successfully. Recommend CVO weigh a value-config (the RIGID empirical gate: Peter + a 49F control, identical per window x fee_view across surfaces) on tomorrow's fresh artifact.

## Knowledge-parity delta + residual
BELIEVED (TO-2 premise): the all-roles canonical field is deployed + served. TRUE: deployed in CODE + served-fresh for inf; bd-served is STALE (06-17) with per-advisor fee-split NULL (CVO P1, DS fix tonight). Residual NOT exercised: tomorrow's post-fix 49F served artifact (the populated per-advisor fee-split + cross-route identity) -- the TO-2 served-verify, fires tomorrow-AM.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-which | "what produces/serves/consumes advisor_nna_canonical" | -> comp-pipescript io / pipescript --resource |
| comp-pipescript io | D_00f, INF_D_00f | READS mapped; WRITES (none detected) -- dynamic-write blind spot noted |
| comp-validate | D_00f / INF_D_00f | NO match -> value-ungated (NO_CONFIG) finding |
| comp-transform schema-check | DistributionTab/AdvisorAnalytics/AdvisorPublicProfile | canonical reads present; AdvisorPublicProfile getAdvisorNnaCanonical 8 fields |
| boto3 head/get + gzip | served opal-data-bd / opal-data-inf objects | bd STALE 06-17 (gzip, per-advisor fee-split NULL); inf FRESH 06-18 (fee-split populated, F4 tie-out live) |
