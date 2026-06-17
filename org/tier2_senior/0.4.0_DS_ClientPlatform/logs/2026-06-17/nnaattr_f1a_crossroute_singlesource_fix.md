# ADVI_NNAATTR F-1a -- cross-route identity made genuinely single-source (CVO 2030Z molecule DIG closed)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Current State
Fresh 0.4.0_DS_ClientPlatform spawn (this session). Acted on a CVO (3.0.0_SA_CVO) /molecule+/seams
finding delivered at session start (`cvo_2030Z_nnaattr_f0f1a_molecule_seams_validation.md`, 0efaaa4a3).

**The finding (DIG, not close-gate-blocking):** F-1a's central guarantee -- cross-route per-advisor
identity (AC1: a given advisor's all-roles NNA is byte-identical via D_00f canonical and D_00c
leaderboard) -- was NOT "by construction." The shared helper `lib/advisor_nna_attribution.py` is
called directly by D_00f (`build_account_advisor_map` -> `attach_advisor_allroles`, D_00f:533-534),
but D_00c imported only `BUCKET_KEYS` and RE-IMPLEMENTED the per-advisor melt inline (D_00c:841-858)
with a NARROWER null-set (`{49f house, unassigned, unresolved}`) than the helper's `_ROLE_NULLS`
(`{none,nan,null,na,n/a,unknown,'No <role> value assigned',...}`). So identity rested on TWO PARALLEL
melts that agree on today's data (CVO verified 0 phantom-divergence rows in served account_team) but
would silently diverge if a role col ever carried a placeholder string -> D_00c mints a phantom
individual D_00f drops. Latent fragility, not an active bug.

**Fix (commit f24d20c08, CLOUD; deployed + md5-byte-verified on s3://opal-data-bd/code/gold/):**
- `lib/advisor_nna_attribution.py`: promoted `_ROLE_NULLS` -> PUBLIC `ROLE_NULLS` (sits alongside the
  already-public `BUCKET_KEYS`); internal use updated. Corrected the module docstring + the
  `advisor_account_pairs` docstring -- dropped the false "imported by BOTH ... not two parallel
  computations" overclaim; now states accurately that D_00f calls `build_account_advisor_map()`
  while D_00c re-melts inline for role/relationship_id/total_aua grain but applies the SAME
  `ROLE_NULLS + BUCKET_KEYS`.
- `D_00c.portal_leaderboard.py`: import `ROLE_NULLS`; inline filter is now
  `~_adv_low.isin({ROLE_NULLS} | {BUCKET_KEYS lowercased})` (was the narrow set). Both routes'
  individual-determination is now logic-equivalent by a single-sourced definition.

**Why harmonize the null-set rather than literally call `helper.advisor_account_pairs()` in D_00c:**
D_00c's inline `melted` frame is load-bearing for far more than the advisor->account pairs -- it
carries `_role / relationship_id / total_aua` that drive the fee-split three-case rule, `at_role_breakdown`,
the role-combination breakdown, AUA + client counts, and new-client buckets -- grain the helper's
`[account_id, advisor_key, is_bucket]` map drops. Swapping ONLY `advisor_account_pairs` to the helper
while leaving the counts on the old filter would make D_00c internally inconsistent. Harmonizing the
shared null-set fixes the whole inline melt at once: pairs AND counts AND fee-splits all resolve the
identical individual set as D_00f.

**Residual NOTE knowingly retained (documented in-code, not silently "fixed"):** non-architect literal
'49F House'. D_00c drops '49F House' in EVERY role; the helper's `is_house` drops it only in the
architect role (and would mint a non-architect '49F House' as an individual). 0 occurrences in served
data; D_00c's behavior is the stricter/safer one. I did NOT touch the Andrew-decided "house bucket =
architect-role credit only" semantics in the helper for a 0-occurrence case -- flagged to CVO for an
optional 1-line symmetry change if they/Andrew want it.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| Read (helper + D_00c:38-58/770-1145 + D_00f call sites; CVO report) | molecule of the helper, locate the two-melt divergence | CONFIRMED -- D_00c imports only BUCKET_KEYS, inline melt narrower null-set |
| Grep (`_ROLE_NULLS`/`ROLE_NULLS` repo-wide; `advisor_nna_attribution` in data/cot) | rename blast-radius; confirm cot fork doesn't import the bd helper | PASS -- helper-internal only; cot does NOT import (no cross-firm ref) |
| `.tools/ds-commit-gate.sh` (D_00c + helper + D_00f) | py_compile + AST + ruff py39 FA before commit | PASS -- "All checks passed" x3 |
| python (standalone equivalence test, then removed) | prove helper individuals == D_00c individuals on the exact prior-divergent placeholders | PASS -- 0 divergence, 0 placeholder leak |
| `.tools/safe-commit.sh` + push (safe-deploy pre-push) | commit-author + atomic deploy to bd gold S3 | PASS -- DEPLOYED+verified; ETag==local md5 both files |

What worked: the standalone equivalence harness gave a decisive by-construction proof (not analogy) that
the two routes now resolve the identical individual set even on `none/n-a/null/unknown/'No <role> value
assigned'`. What failed: nothing. Gap: none.

## Blockers
None. CHANGE is committed + deployed + byte-verified. AC1 served byte-equality is CVO's post-nightly
close-gate (event-driven tomorrow-AM, by design -- validate on scheduled nightly).

## Files Modified
See commit message f24d20c08 (per-file rationale embedded). Two files: `data/black_diamond/scripts/gold/
lib/advisor_nna_attribution.py`, `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py`.

## Next Steps
1. **[self, NOW -- COO /drive 233846Z]** Implement ADVI_COTETL.CHAINFIX: the `emit_silver_sentinel`
   gate-semantics fix (CTO-signed-off; silver-sentinel never fires -> cot gold chain blocked). Full DS
   commit->QA-deploy cycle; validate on the scheduled nightly (no ad-hoc run). RAVC2 to [2.0.0_SA_COO]
   on DEPLOY. Holdings-nightly piece is HELD separately (CTO design call) -- NOT tonight's scope.
2. **[3.0.0_SA_CVO]** Post-nightly close-gate: verify served `advisor_nna_canonical.json` +
   `leaderboard.json` cross-route byte-equality on the FIXED route (f24d20c08 runs tonight).
3. **[self, event-driven tomorrow-AM]** ADVI_NNAATTR.TO-1 served-verify off tonight's nightly (separate
   thread; CVO+CTO co-sign).
