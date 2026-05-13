# DS~C 2026-05-13 session 8 — v1.7.54 chain #27 RAVC + ADVI_INFADV Path B Lambda mirror

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~21:08Z → ~21:14Z 2026-05-13 (~6 min)
**Trigger:** AE 0.6.1 RAVC2 chain #27 mode=full exit 0; ALL 3 v1.7.54 commits empirically validated. Surfaced Path B Lambda parity gap on full-chain output (Lambda's `_build_book` overwrote gold-script's top-level fields). Shipped Lambda mirror.

## TL;DR

| Workstream | Status |
|---|---|
| v1.7.54 chain #27 full-chain RAVC | **ALL 3 commits VALIDATED.** Orphan-bucket clients[0]=Thompson; Patrick cumsum 0/2170 monotonicity breaks; display_label populated cross-advisor. CLEAN-STATE RATCHET HELD. |
| Path B Lambda gap surfaced | `active_since` + `role_breakdown` + `tax_exposure` MISSING in post-chain-27 artifact; Lambda's `_build_book` overwrote gold's top-level emit. |
| v1.7.55 Lambda mirror shipped | `9cd5f00b4` — 2 of 3 fields. `tax_exposure` deferred to v1.7.56 (needs +60-100 LOC Lambda tax aggregation). |
| Coordination | AE 0.6.1 + DE 0.4.0 notified. Bundle window pending. |

## Ship

| Commit | Scope | Lines | S3 SHA-MATCH |
|---|---|---|---|
| `9cd5f00b4` | Lambda `_build_book` Path B mirror (2 fields) | +39/-10 | n/a — Lambda code, awaits AE build-and-upload + terraform apply for v1.7.55 |

## Chain #27 validation (AE 0.6.1 + my cross-check)

AE's RAVC reported (21:01:28Z chain exit; 21:02:09Z Lambda auto-fire via INFPUBLISHERDEDUP ObjectCreated trigger):

### `52478bb3a` IWM client attribution

- IWM book.clients[0]: `display_name="Richard L Thompson & Cheryl L Thompson"`, `relationship_since="2026-04-15"`, `household_id=1342`, `account_count=11`, `aua=$224,930.66`, `ytd_nna=$223,190.25` ✓
- IWM clients_len=4 (not 10 as my pre-chain sentinel predicted) — better outcome. Upstream `ADHC_INFCAT_ORPHAN` Bug A fix (commits `90306935b` + `f948658e6`) reattributed 17 accounts OUT of IWM catchall to Peter Lee × 16, Patrick Scanlan × 1. **Compound effect**: phantom row drop (Lambda) + correct named-advisor attribution (gold INF_C_07 walk-back). Not regression.

### `14c54aec2` Patrick cumsum monotonicity

- 2170 daily rows (2020-06-04 → 2026-05-13)
- 0/2170 `cum_inflows` breaks (any decrease)
- 0/2170 `cum_outflows` breaks
- Final: `cum_inflows=$18,818,705`, `cum_outflows=$3,802,166`
- Sparse-cumsum reindex+ffill defensive pattern WORKS under real chain conditions

### `d12598087` display_label

- `patrick_scanlan/top_holdings.json` includes `display_label` field
- Top 5 rows: VOO, HTRB, JIJIX, CIVIX, VO — all populated, no nulls
- CUSIP/slug fallback path empirically validated

## Path B Lambda gap

My empirical check post-chain-27 (Patrick book.json generated 21:02:07Z):

```
top-level keys: [advisor_key, book_name, clients, composition, data_as_of,
                 firm_id, generated_at, headline, summary, top_holdings]
  active_since:   MISSING  (Lambda overwrote gold's emit)
  role_breakdown: MISSING
  tax_exposure:   MISSING
  clients[].relationship_since: 71/73 populated  (Lambda's _client_list emits it)
```

IWM identical: 4 clients, 3 Path B fields missing.

**Behavior matrix:**
| Field | gold-d chains | full chains (post-Lambda) |
|---|---|---|
| `active_since` | ✓ from gold | ✗ (pre-v1.7.55) → ✓ (post-v1.7.55) |
| `role_breakdown` | ✓ from gold | ✗ → ✓ post-v1.7.55 |
| `tax_exposure` | ✓ from gold | ✗ still missing (deferred to v1.7.56) |
| `clients[].relationship_since` | ✓ from gold | ✓ (Lambda has it natively) |

## Lambda mirror diff

Added before `return` in `_build_book`:
- `clients = _client_list(adv_df, relationship_since_by_hh)` — refactored (was inline in return) so `active_since` can read from it
- `active_since = min(c['relationship_since'] for c in clients if c.get('relationship_since')) or None`
- `small_account_count = int((adv_df['aua'] < 40000).sum())` defensive against empty df
- `role_breakdown = {'advisor': {...}}` matching gold-script's emit exactly

Added to return dict: `'active_since', 'role_breakdown'`

## Out of scope (deferred)

**`tax_exposure` Lambda parity (v1.7.56)** — needs:
1. Lambda to load `silver/api_dims/tax_unrealized` + `silver/api_dims/tax_realized` (currently not loaded)
2. Mirror gold's `_ensure_tax_status` + `_aggregate_tax_status_per_advisor` + `_aggregate_tax_per_advisor` helpers (~100 LOC)
3. Wire into `_build_book` signature

Cost ~30-60 min. FE adapter at `advisor-intelligence.ts:866` handles missing field with zero stub. Not partner-demo blocking. Separate ship when DE/COO/Andrew prioritize.

**`mix_periods` asset-class breakdown** — still pending follow-up TO (per session 7). Needs historical-account-team walk + per-quarter classifier.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| Live S3 cross-check `patrick_scanlan/book.json` + `inflection_wealth_management/book.json` post-chain-27 | 1× | Path B fields MISSING on full-chain (Lambda overwrote); clients[].relationship_since survived |
| `ds-commit-gate.sh inf-portal-advisor-publisher/lambda_function.py` | 1× | PASS — py_compile + ds-precommit + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 1× | Clean first-try |
| `git push origin CLOUD` | 1× | Connection-reset on first try; succeeded on retry |

No comp-pipescript runs — Lambda code change, not gold-script edit.

## Files Modified

| File | Change |
|---|---|
| `infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py` | `_build_book` — refactor `clients` to compute once + add `active_since` + `role_breakdown` to return dict (+39/-10) |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **AE 0.6.1_AE_PartnerETL** | v1.7.55 bundle ready. Commit `9cd5f00b4` on origin/CLOUD. Same drop-in pattern as v1.7.54. Brief in inbox; no urgency. |
| **DE 0.4.0_DE_ClientPlatform** | FYI sent. Post-v1.7.55 apply: 2 of 3 Path B fields will populate on full chains; tax_exposure stays missing (FE adapter handles). |
| **DS~C self** | Idle. Next concrete work: tax_exposure Lambda mirror (v1.7.56) OR mix_periods follow-up TO if DE/COO prioritize. |

## Decision notes (worth keeping)

1. **Empirical post-chain check catches what pre-ship sentinels miss.** My v1.7.54 pre-chain sentinel for orphan-bucket predicted `clients_len=10`. Actual was 4. Both correct: pre-chain sentinel assumed only the Lambda fix; actual chain ran the COMPOUND fix (Lambda + INF_C_07 walk-back upstream). The "better-than-predicted" outcome would have been a false alarm with naive sentinel comparison. Always reason about compound effects + verify cause-and-effect, not just "does the number match my prediction."

2. **Lambda overwrite gap was foreseeable.** I noted in session 7 that Lambda parity was deferred for full chains; chain #27 exposed it on real data. Cheap empirical confirmation closes the loop: 4-min sentinel verification → Lambda mirror shipped in 8 more minutes. Process discipline: when you defer a follow-up, also schedule a verification step against real chain output before claiming complete.

3. **Tax_exposure cost-vs-value defer.** Could have shipped full tax_exposure Lambda mirror but at ~60-100 LOC and partner-demo non-critical (FE adapter handles). Better to ship the cheap 2 fields now + write a separate clean TO for tax_exposure than to bundle a half-baked tax aggregation. Cost discipline beats completeness when scope can be cleanly cut.

4. **Connection reset on first push.** Transient git connectivity issue; retried successfully. Worth noting if AE 0.6.1 sees similar during their Lambda bundle apply — single-retry pattern usually works.

## Pacing

6 min execution. Day total (sessions 1-8): ~3 hr active work across:
- 5 INF Lambda commits (`52478bb3a` orphan-bucket, `9301dfe97` mix_periods-overwrite, `d12598087` display_label, `14c54aec2` sparse-cumsum, `9cd5f00b4` Path B mirror) + 1 BD cross-firm defensive (`74593520a`)
- INF_C_07 walk-back (`90306935b` + `f948658e6`)
- INF_D_02 ADVI_INFADV Path B (`0997324d6`)
- Patrick docstring (`b7e8757f8`)
- 2 memory entries + 1 hardening proposal + 8 session logs

End-of-day state: v1.7.54 ratchet HELD with all 3 fixes empirically validated under real full-chain. v1.7.55 Lambda mirror ready for next AE bundle window. ADVI_INFCAT_ORPHAN Bug B (cross-team) still in COO routing. mix_periods asset-class + tax_exposure Lambda parity = open follow-up TOs.
