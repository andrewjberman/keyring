# CVO /molecule + /seams validation — ADVI_NNAATTR F-0/F-1a deployed code — 2026-06-17 ~20:30Z

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, TRACE

Andrew-directed validation of the deployed NNA-remediation work (F-0/F-1a, commits 0bca5a46a + 98ff87c6d).
TIMING: code DEPLOYED + md5-matched on S3, but the SERVED artifacts have NOT regenerated (C_07's
`architect_no_infer` column is absent from the current served `account_team` -> the nightly hasn't run the
fix). So this is a DEPLOYED-CODE/LOGIC validation; the SERVED-number close-gate (cross-route byte-equality)
remains pending the 06-18 nightly (#9, validate-on-scheduled-nightly).

## /molecule 1 — lib/advisor_nna_attribution.py (the shared helper) [MICRO/pure]
COMPOSITION (deployed = committed, read): SOUND. Pure (no I/O). `build_account_advisor_map` melts the 5
roles, detects 49F House (architect-role only) + the broad `_ROLE_NULLS`, emits (account, advisor_key,
is_bucket): individuals (any role) + 49F House bucket (architect_no_infer) + Unassigned (no real advisor +
not house). `attach_advisor_allroles` LEFT-joins atomic NNA with BUCKET-ONLY fallback for not-in-account_team
accounts (49F House if atomic architect is house, else Unassigned; NEVER an individual) -- the close-gate fix
(98ff87c6d). `advisor_account_pairs(include_buckets=False)` drops buckets for the leaderboard. Matches the
Andrew-decided model exactly (all-roles, buckets preserved, snapshot tenure, individuals account_team-only).

## /molecule 2 — C_07.resolve_architect_no_infer (the attribution column) [MICRO]
COMPOSITION: SOUND + faithful to Andrew's F-0 asymmetry. 49F House -> preserved literally (NEVER resolved);
real -> Layer-1; blank/Unassigned -> Layer-2 modal REAL sibling architect (architect_rel excludes
house+blank, so a blank never inherits 49F House or an impl-pairing guess); residual -> Unassigned. Layer-3
(impl-pairing inference) DISABLED. ADDITIVE column (the 14 other account_team consumers keep legacy
`architect` unchanged -> zero blast). Correct.

## /seams (4 edges)
| Seam | MECH | DECL | SEM |
|---|---|---|---|
| C_07.architect_no_infer -> helper.build_account_advisor_map -> D_00f | PASS (D_00f imports+calls the helper, L83/533-534) | PASS | PASS (one shared map) |
| atomic gold/canonical/nna -> attach_advisor_allroles | PASS (LEFT-join + bucket-only fallback) | PASS | PASS (bucket-only preserves 49F House MAX + all NNA visible) |
| C_07.architect_no_infer -> D_00c (leaderboard individuals) | PASS-mechanically | **FAIL (drift)** -- see F-1 below | **WATCH** -- two parallel melts, narrower null-set; agree TODAY (0 divergence) |
| D_00f individuals == D_00c individuals (cross-route identity / AC1) | PASS empirically-today | n/a | rests on two-melts-agreeing, NOT one-helper-by-construction |

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| D_00c re-implements the melt inline -- does NOT use the shared helper's map; imports only `BUCKET_KEYS` (D_00c:48). The helper docstring claims "imported by BOTH D_00f AND D_00c ... not two parallel computations" (advisor_nna_attribution.py:4-7) -- FALSE for the map. | **DIG** | D_00c:48 import; D_00c:840-858 inline melt + own filter | The cross-route identity (F-1a's whole point) is NOT "by construction" -- it's two parallel computations that happen to agree. The helper's central claim is a DECLARATIVE overclaim. |
| Null-set divergence: helper `_ROLE_NULLS` excludes {none,nan,null,na,n/a,unknown,'No <role> value assigned',...}; D_00c inline excludes only {blank,49f house,unassigned,unresolved}. | **WATCH** | helper:44-49 vs D_00c:851-854 | If a role col ever carries 'No implementor value assigned'/'none'/'n/a', D_00c mints a PHANTOM individual D_00f excludes -> identity breaks silently. **Empirically 0 such rows in the current served account_team (all 5 roles clean)** -- latent, not active. |
| `is_house` is architect-role-only; a '49F House' in a non-architect role would mint a phantom individual (is_bucket=False wins the dedup). | **NOTE** | helper:91 | Benign now (49F House is an architect designation; 0 occurrences), but a non-architect '49F House' would leak. |
| Served account_team has NO `architect_no_infer` column yet (pre-nightly). | **NOTE** | account_team.parquet cols read 20:25Z | Expected -- C_07 runs on the nightly. D_00c's elif WARNs + uses legacy architect until then -> identity NOT live pre-nightly (correct; close-gate is post-nightly). |

## State (Dimension 2)
Served `advisor_nna_canonical.json` + `leaderboard.json` are STILL pre-fix (06-17 nightly, the divergent
$4.14M/$6.95M Travis numbers). The deployed code activates on the 06-18 nightly when C_07 regenerates
account_team with `architect_no_infer`. So the served close-gate is correctly pending (#9).

## Assessment
The deployed CODE is largely SOUND and faithfully implements Andrew's F-0 decisions (49F House preserved,
Layer-3 off, all-roles, bucket-only fallback, snapshot tenure) -- the helper + C_07 column are clean. The
ONE real finding (DIG): cross-route identity, the central F-1a guarantee, is NOT realized "by construction"
-- D_00c re-implements the per-advisor melt inline (imports only BUCKET_KEYS) with a NARROWER null-set than
the shared helper, so identity rests on two parallel melts that agree on TODAY's data (0 phantom-divergence
rows verified) but would silently diverge under drift (a placeholder string in a role col, or a one-sided
edit). Route to DS: have D_00c consume the helper's `advisor_account_pairs()` (or at minimum its `_ROLE_NULLS`)
so identity is genuinely single-source; and correct the helper docstring's "imported by BOTH" overclaim.
NOT close-gate-blocking (empirically clean today) -- but an F-1a-completeness gap to close before the
close-gate locks "done."

## Knowledge-parity delta + residual
BELIEVED: "one shared helper -> identity by construction, both routes." TRUE: D_00f uses the helper; D_00c
re-implements with a narrower null-set (agree today, fragile). Routed to DS (finding). Served-number
close-gate (Travis+2 byte-equality, 49F House ~$357.6M preserved, Unassigned composition) UNVERIFIED until
the 06-18 nightly -- by design (validate on scheduled nightly).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| Read (deployed lib/advisor_nna_attribution.py + C_07 + D_00f/D_00c call sites; md5==S3) | molecule composition of the helper + column | SOUND |
| Grep (helper imports/calls across D_00f/D_00c) | seam: does D_00c use the helper? | NO -- imports only BUCKET_KEYS, inline melt (the DIG) |
| python/pandas (served account_team.parquet, 6370 rows, role-col placeholder scan) | semantic: do the two null-sets diverge on real data? | 0 phantom rows -- latent not active; + architect_no_infer absent (pre-nightly) |

— 3.0.0_SA_CVO
