# 0.4.0_DS_ClientPlatform -- DS-2 (advisor-AUA no_infer) rec -> toggle -> Andrew-shelve; leg-2 deconflict

**archetype:** COORDINATE (secondary: DIAGNOSE, SCRIBE)
**window:** 2026-07-01 ~1436Z -> ~1517Z (delta since session_1436Z)
**serial:** 0.4.0_DS_ClientPlatform | **branch:** CLOUD | **project:** ADVI_TAGATTR
**driver:** Andrew-direct (rec on the D_02/D_01 rollup finding -> "sure" -> "toggle?" -> "go on" -> "nobody uses this shit ... explainable").

## HEADLINE
Recommended + scoped the fix for the served advisor-AUA rollup finding (DS-2: D_02/D_01 -> architect_no_infer),
refined it to a shared 2-way toggle per Andrew, ran a preliminary dry-run magnitude, then Andrew SHELVED it
(low-usage surface + explainable). Stood it down cleanly. Separately: my ~A lane landed TAGATTR leg-2 (fee) ->
my leg-2 block cleared; git verified synced (no D_00c single-writer collision).

## The DS-2 arc (authored -> refined -> shelved, no code shipped)
- REC (Andrew "give me your rec"): migrate the 2 AUA-attributing consumers (D_02 book.json total_aua -> served
  leaderboard; D_01 PartnerAnalytics ADV) from the Layer-3-inferred architect to architect_no_infer -- extends the
  ratified ADVI_NNAATTR F-0 basis to the served advisor total_aua. Keep Layer-2 (real-sibling); don't bundle the
  stricter Layer-2-off. Staged as ADVI_TAGATTR.DS-2 (32d035b5b).
- TOGGLE (Andrew "keep it a toggle?"): refined to ONE shared, artifact-stamped, 2-way selector (no_infer default |
  inferred) read by all 4 advisor-AUA producers (D_00c/D_00f/D_02/D_01) -> single-sourced, no drift; flip = a gated
  deploy, never a runtime env-flip on a live financial number. Andrew picked 2-way (AskUserQuestion). Amended (955e76c23).
  CTO affirmed + made 2 hard adds gate-binding (flip-is-gated-deploy; D_00c/D_00f byte-unchanged proof).
- DRY-RUN (Andrew "go on"): offline recompute on bd account_team (both architect columns) -- NOT served. Result:
  ~$336.8M firm-wide de-attributes under no_infer; 30/163 advisors move; top = Kyle Sims $270.5M->$166.8M (-38.4%),
  Travis $440.0M->$358.3M (-18.6%), Greg Rosner $270.6M->$201.3M (-25.6%). Cross-check: Travis no_infer ($358.3M) ==
  his DS-1 split-weighted role-sum to the dollar (the House book overlaps both reductions) -> raised confidence.
- SHELVE (Andrew "nobody uses this shit ... explainable if anyone ever asked"): DEFERRED (bd40e393d, staged->deferred).
  Low-usage surface + inferred-basis is defensible (coverage attribution of House/orphan accounts to the modal advisor).
  Documented explainable known-gap (memory/reference_bd_architect_inference_no_infer_split.md updated). No toggle built,
  no numbers moved. Stood down CTO (gate moot) + COO (registry) + DE (number-move watch dropped).

## leg-2 (fee) deconflict -- ~A landed it; base synced clean
~A lane landed TAGATTR leg-2 (3ba105354): Andrew ruled fees = per-account ACTUALS, conserved/reconciled to C_08
canonical (NOT full-tagged like AUA -- the option-B I'd recommended to CTO). So leg-2 = fee_basis labeling +
a runtime conservation assert (sum_roles(fee_paying.aua)==fee_aua; role.aua==fp+nf), no fee-value change; ARCH-GATE 2
discharged. VERIFIED my base session is synced: local HEAD==origin/CLOUD, 3ba105354 in history, D_00c carries the
fee_basis label, working tree clean, 0 behind -- push-time merges reconciled us, no single-writer collision. DS-2
shelved -> no further base-lane D_00c edit coming, so D_00c contention is clear.

## Blockers
NONE. leg-2-on-CTO-fee-ADR block CLEARED (~A landed it). Remaining work is nightly-external, not blocked.

## Current State
- **DS-2:** deferred (Andrew-shelved). TO ADVI_TAGATTR.DS-2 status=deferred with deferred_note. Finding banked.
- **leg-1 (0ab172d3f, base):** role_breakdown AUA/NNA/flows full-tagged + non-additive labeling. Landed+deployed(MATCH).
  Validates on tonight's bd nightly (comp-validate Phase-3 + DE render + CVO).
- **leg-2 (3ba105354, ~A):** fee labeling + conservation assert. Landed+deployed. Effective next bd nightly.
- **COTMVP.B-DS (bb2d62ef8, base):** cot D_04 build_client_directory -> platinum/firm/client_directory.json (218 HH).
  Landed+deployed(sha256 MATCH). Validates on tonight's cot nightly (comp-validate + DE render + CVO count-verify 218).
- git: CLOUD @ bd40e393d, clean, synced with origin.

## Next Steps
- [0.4.0_DS_ClientPlatform] On tonight's bd nightly: comp-validate Phase-3 on served leaderboard.json (Travis architect
  full-tagged, not ~358M split-sum; total_aua ~439.97M unchanged); RAVC2 DE+COO+CVO. Co-gated with DE render + CVO.
- [0.4.0_DS_ClientPlatform] On tonight's cot nightly: comp-validate client_directory.json (218 HH, display_name+finite aua);
  RAVC2 DE+COO+CVO. Co-gated with DE render + CVO count-verify.
- DS-2 re-open trigger (documented): only if the advisor-total_aua surface's usage/importance changes.

## MCP (this window)
~18 messages handled (RAVC-heavy). Significant: Andrew rec->sure->toggle->go-on->shelve (5 directives); CTO DS-2
arch-gate approved-in-principle -> toggle-affirm -> stand-down ACK; COO DS-2 tracked -> stand-down; DE DS-2 heads-up ->
ACK-both-flags-preresolved -> shelve-ACK; ~A leg-2 deconflict (landed 3ba105354) -> my synced-ACK; CVO cot-directory
served-verify ACK (grounds 218-vs-217). No open loops requiring my action -- all parked on the two nightlies.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| git fetch/merge-base/status | PASS | leg-2 deconflict sync check: base==origin, 3ba105354 in history, D_00c label present, clean |
| (dry-run) offline python on bd account_team.parquet | PASS | DS-2 preliminary delta (inferred vs no_infer per-advisor total_aua); NOT a served run, NOT ad-hoc gold |
No gold-script CODE edited this window -- DS-2 was authored-then-shelved before any .py change, so no ds-commit-gate /
comp-pipescript / comp-validate this window (they ride the implementing code, which never landed). The dry-run was a
rail-checked offline account_team recompute (comp-tool gap: no comp-tool computes a hypothetical attribution-basis
delta -- an ad-hoc python recompute is the right instrument for a pre-serve magnitude preview). comp-tool discipline
for the SHIPPED work (leg-1/leg-2/COTMVP.B-DS) is in the prior two logs.
