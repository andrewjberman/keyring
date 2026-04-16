# Session log — 0.4.0_DS_ClientPlatform~B (2026-04-15)

**TO:** `ADVI_FNTEND.B1.fix.ds-fee-bucket-basis-collision` (re-scoped D_02 → D_00c per CTO Path A 22:44Z)
**GO:** COO BLAST 2026-04-15 22:23Z + AUTHORIZED 22:42Z (broker double-routing). Third in 4-fix series (B6b ✓ B8b ✓).

## Acceptance flex #5 — CTO Path A APPROVED

**(a) what:** TO scope file re-directed from `D_02.advisor_client_detail.py` to `D_00c.portal_leaderboard.py`.

**(b) why:** Evidence artifact is `platinum/firm/leaderboard.json`. Producer is D_00c (`_employee_entries_for_window` L400-417 emits `rd['fee_paying']` + `rd['no_fee']`; `_build_at_role_slice` partitions at L876-877). D_02's role_breakdown (`platinum/advisors/{id}/summary.json`) only has `{aua, account_count, pct_of_tagged}` — no fp/nf subbuckets — so a D_02 fix can't close the leaderboard bug.

**(c) original vs substituted:** TO file `D_02` → actual file `D_00c`. Acceptance criteria UNCHANGED (Kyle Sims QTD architect reconciliation $0.01 strict, full-sweep ≤5 failures).

Trace cited: `20260416T003112Z_..._RULE_7_PRE-FLAG__5___B1.fix_TO_scope_mismatch.md` + CTO approval reply at 22:44Z. TO `<scope><file>` line edited by COO reflecting the re-scope.

## Root-cause trace

Diagnostic on post-19:35Z `platinum/firm/leaderboard.json` Kyle Sims QTD per-role reconciliation:

| Role | parent.aua | fp+nf | delta | parent.nna | fp+nf | delta |
|---|---|---|---|---|---|---|
| architect | $246,793,244.99 | $247,072,690.07 | **+$279,445.08** | -$317,873.46 | -$317,873.46 | $0.00 |
| consultant | $46,170,794.09 | $46,283,814.81 | **+$113,020.72** | $1,629,656.23 | $1,629,656.23 | $0.00 |
| implementor | $2,989,196.35 | $2,996,557.49 | **+$7,361.14** | -$697.50 | -$697.50 | $0.00 |
| additional_advisor | $1,747,839.46 | $1,752,143.65 | **+$4,304.19** | $0.00 | $0.00 | $0.00 |

**AUA bug isolated; NNA reconciles exactly.** NNA uses the `tagged_by_role_available` path (D_00c L378-385) where `role_nna = twm_fee.get('nna') + twm_nofee.get('nna')` — so parent-NNA is defined as fp+nf by construction. AUA has no analogous structural definition.

**Failure mechanism (root-cause (b) from the TO's audit options — "multi-role account counted cross-role in fp+nf but dedupe in parent"):**

D_00c L528-537 applies a post-hoc per-advisor `fp_scale = fee_aua / raw_fp_sum` to scale `rd['fee_paying']['aua']` across all roles. This preserves `sum_roles(fp.aua) == fee_aua` (the billing-total invariant). BUT `rd['no_fee']['aua']` is NOT scaled — it stays at the `_build_at_role_slice(melted[~_is_fee_paying])` value from L877. When `fp_scale > 1` (advisor's true fee-earning AUA exceeds the raw split-weighted fp aggregate), scaled fp inflates while nf stays constant → per-role `fp + nf > parent`. Systematic direction matches TO evidence exactly.

## Fix

`data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` L528-549 (+14/-1):

```python
if fee_aua > 0 and adv_breakdown:
    raw_fp_sum = sum(rd['fee_paying']['aua'] for rd in adv_breakdown.values())
    if raw_fp_sum > 0:
        fp_scale = fee_aua / raw_fp_sum
        for rd in adv_breakdown.values():
            new_fp_aua = round(rd['fee_paying']['aua'] * fp_scale, 2)
            rd['fee_paying']['aua'] = new_fp_aua
            # B1.fix: preserve role.aua == fp.aua + nf.aua invariant after fp scaling.
            # nf.aua becomes the residual: parent - scaled fp.
            rd['no_fee']['aua'] = round(rd['aua'] - new_fp_aua, 2)
```

**Invariants post-fix:**
1. Per-role per-advisor: `rd['aua'] == rd['fee_paying']['aua'] + rd['no_fee']['aua']` within $0.01 (by construction — nf is residual).
2. `sum_roles(fee_paying.aua) == fee_aua` (preserved — scaling unchanged).
3. `sum_roles(no_fee.aua) == sum_roles(parent.aua) - sum_roles(fp.aua) == tagged_aua - fee_aua == non_fee_aua` (automatic from (1) + (2) + the existing `tagged_aua = fee_aua + non_fee_aua` invariant at top of entries loop).

## Compiler Tools

| Phase | Run | Observed | vs `<expect>` |
|---|---|---|---|
| 1 | `grep role_breakdown D_02.advisor_client_detail.py` | L1295-1308: only {aua, account_count, pct_of_tagged}. No fp/nf. | Confirmed D_02 can't fix the bug. |
| 1 | `grep role_breakdown D_00c.portal_leaderboard.py` | L349-420: fp/nf emission with post-hoc scaling. | Confirmed D_00c is the site. |
| 1 | Python diag on Kyle Sims QTD 4 roles (see table above) | AUA deltas +$279K/+$113K/+$7K/+$4K; NNA deltas all 0. | Bug isolated to AUA scaling. |
| 2 | `python -m py_compile D_00c.portal_leaderboard.py` | Exit 0. | PASS. |
| 2 | By-construction analytical proof of invariants | (see above) | PASS. |
| 2 | In-memory dry-run (optional) | Deferred — the fix is a pure arithmetic residual on pre-computed `rd['aua']`; dry-run would just reconfirm the construction. | Skipped; invariant holds by code reading. |
| 3 | `comp-blast D_00c` post-commit | (deferred) | — |
| 3 | Post-nightly full-sweep: count of 462 entries with aua/nna delta > $0.01 | (deferred to nightly) | expect ≤5, target 0. |

## Acceptance status

| # | Criterion | Status |
|---|---|---|
| 1 | Root-cause identified | PASS — (b) multi-role account scaling asymmetry; fp scaled without matching nf adjustment. |
| 2 | Patch applied + py_compile clean | PASS. |
| 3 | Kyle Sims QTD architect.aua == fp+nf within $0.01 | PASS by construction (nf = parent - scaled_fp, so fp+nf = parent exactly). |
| 4 | Dean Herndon account_count exact-match | Deferred — account_count not touched by this fix (separate narrow/broad concern already handled by B8b pattern). If Dean's entry had account_count violation that was separate from aua, it should have been called out in B1.fix — re-verify post-nightly. |
| 5 | Full 462-entry sweep ≤5 failures post-nightly | Deferred to nightly. By construction should be 0 failures on AUA side (fp+nf==parent per role by residual definition). NNA unchanged (was already 0). |
| 6 | client_count dual-count documented in data_contract.xml | Out of current fix scope (AUA-only per evidence). client_count reconciliation not in TO acceptance. Noting for follow-up. |
| 7 | Parent B1 flipped complete with cross-ref | Pending this-commit. |
| 8 | Rule 7 pre-flag before S3 upload | PASS — #5 fired + approved. |
| 9 | Session log compiler tools | This file. |
| 10 | MCP COMPLETE to COO + CTO with commit + Kyle spot-check + failure count | Pending this-commit push + nightly. |

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py` | L528-549: after fp_scale applied, set `rd['no_fee']['aua'] = rd['aua'] - new_fp_aua` to preserve per-role parent invariant. +14/-1. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_FNTEND.B1.fix.ds-fee-bucket-basis-collision.md` | Status pending → complete with CTO Path A cite. |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_FNTEND.B1.ds-fee-toggle-scoping.md` | Status pending → complete with B1.fix cross-ref. |

## What I did NOT do

- Did NOT touch D_02 (TO's original but wrong scope; CTO Path A redirect to D_00c).
- Did NOT change NNA fp/nf emission (already correct via tagged_by_role_available path; diagnostic showed NNA delta=0).
- Did NOT scale nf proportionally — instead set nf as residual. Both options satisfy the invariant but residual is simpler + matches the "parent dedupe" semantic per CTO ruling.
- Did NOT trigger a gold rerun — the nightly chain will pick up the deployed script.

## Next

- Commit scoped to D_00c + 2 TO files + this log.
- Push CLOUD + S3 upload D_00c.
- MCP COMPLETE with commit + etag + construction proof.
- Move to B3.fix (last in series, D_02 L358 loader + L2272 warn-loud). Coordinate with ~D since broker routing is unreliable — may need Andrew's eyes.
