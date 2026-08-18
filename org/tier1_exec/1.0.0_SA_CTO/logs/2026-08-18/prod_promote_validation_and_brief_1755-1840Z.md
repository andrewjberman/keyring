# PROD Promote Request, Independent Validation, Brief -- 1.0.0_SA_CTO~X

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE

**Date:** 2026-08-18 (~1755-1840Z)
**Task Order:** ad-hoc, Andrew-direct at this terminal: "issue a request to 0.4.0_DT_ClientPlatform
for a /prod-deploy . THen when that is done and validated, and the VUG issue is fixed, i want you to
write a brief on what was done including architectural info, then finally a /log on this process."
**Status:** COMPLETE

---

## Objective

Get the naming-centralization frontend legs (portal DEV commits 8dbaf56b + 12058841) promoted to
PROD through the DT lane, validate the promote and the VUG fix independently, then deliver the brief
and this log.

---

## Compiler Tools

No comp-* runs this window, deliberately: the window was a cross-agent promote request, live
served-bytes validation (curl sweeps of the PROD bundle -- live-primitive reads, not repo searches),
and brief authorship; no code or infra changed from my seat. Rule-20 checks for the promoted code ran
in the prior windows (see d721153f10's log).

**What worked:** the pre-staged bundle-marker script made post-promote validation a one-command act.
**What failed:** nothing. **Gap found:** none.

---

## Work Completed

### 1. /prod-deploy request to [0.4.0_DT_ClientPlatform]
Broker liveness checked first (DT LIVE, idle). Request sent 175947Z with: Andrew's verbatim
authorization, the exact 2-commit payload, the verification already banked on DEV, and three asks
(ACK; run /prod-deploy per skill; completion data for my independent validation). Sender-unverified
flag noted by the broker (session unregistered per Andrew's startup word; serial stamped per LD-0290,
identity_override documented).

### 2. DT ACK (180140Z) -- evidence-verified, not from-line-trusted
DT independently confirmed from disk: payload exactly my 2 commits ahead of origin/DEV, tree clean,
origin/PROD..origin/DEV otherwise empty. Pushes routed to [0.0.0_AB_MSTR] per LD-0367/0368 (standing
posture) -- no override, no manufactured gate.

### 3. PROMOTE COMPLETE (181624Z) + my independent validation
DT's completion: origin/PROD = e27dd5fa (merge; parents 449a6a0e + 12058841; parity diff 0), tag
portal-v2.1.163 peels to PROD head, CI run 32169492889 'Deploy to Production' conclusion=success by
headSha, DECLARED rider edcc503e (DE's MDPF_PROVENANCE.T-A, already on origin/DEV, COO-concurred
180718Z), rollback base 449a6a0e in the merge message. DT ran its own served-bytes read (44/44
chunks, negative+positive controls).

MY validation, independent derivation:
- Bundle markers, proven discriminating PRE-promote (old CLIP-name string located in live chunk
  assets/index-DA-bY7bE.js): post-promote sweep of the NEW entry (index-DyUJgWOr.js, hash changed)
  + 43 chunks = 'Invesco Variable Rate Preferred ETF' 0 hits, 'ProShares Ultra Russell 2000' 0
  hits, NEW-code marker 'Quarterly bear hedge ETF' 1 hit (fresh-deploy vs cache discriminator).
  VERDICT: PROD BUNDLE VALIDATED.
- Git cross-check from my seat: origin/PROD fetch = e27dd5fa; tag peel matches.
- VUG fix on PROD: served holdings_attribution_data.json carries 'Vanguard Growth ETF' in all
  periods (verified at regeneration); old FE fell through to h.name (VUG never in the fallback map),
  new FE reads h.name directly -- fixed under BOTH frontend vintages, so the promote carried the
  decommission legs, not the fix's liveness.

### 4. Brief delivered
FILE docs/briefs/security-naming-centralization-brief-20260818.md @168a5a2352, also published as a
private artifact: https://claude.ai/code/artifact/d82f1dd0-9466-4986-9286-30fd34e4bdf6 -- defect
anatomy (3 stacked causes), before/after architecture (8 naming surfaces -> 1 canon), changes by
layer, verification record, residuals.

## MCP Traffic
3 total: 1 sent (the request), 2 received (DT ACK; DT PROMOTE COMPLETE). Both received messages
archived to read/ on disk (broker mark_read refused for the unregistered session -- filesystem
archive used, self-scoped).

## Blockers
None.

## Current State (zero-context handoff)

- PROD portal = e27dd5fa / tag portal-v2.1.163 / CI 32169492889 success; rollback base 449a6a0e.
- Naming architecture: ONE canon (FILE infra/aws/lambda/v2_portal/_shared/etf_classification.py ->
  DynamoDB etf-classifications, 116 rows, 0 placeholders) -> both yang positioning Lambdas
  (yang-pipeline v1.5.7 deployed) -> served JSON -> portal renders h.name directly. All shadow
  naming surfaces decommissioned (details + hashes: the brief and d721153f10's log).
- Deploy ledgers CLOSED in DIR org/critical_paths/change_management/ (20260818T1710Z_vug-naming-*,
  20260818T1845Z_naming-centralization-*).
- Workspace CLOUD commits + yang tags v1.5.4..v1.5.7 ride the integration window (lanes commit,
  integrators push); portal pushes already executed by MSTR during the promote.

## Next Steps

- [ANDREW] Residual rulings, each now a one-place fix: ICSH name (iShares vs BlackRock vintage);
  GO/no-GO on routing yang-generate-positioning's inline CLASSIFICATION dicts (asset class/style/
  sector) through the registry; tickerRegistry description-field cleanup.
- No agent handoffs outstanding; [0.4.0_DT_ClientPlatform]'s asks all discharged.
