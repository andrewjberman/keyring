# Deploy-Completion Ledger -- P0: inf ETFS producer canonical-holdings repoint

**Opened:** 2026-06-25T19:42Z | **Agent:** 0.5.0_AE_OpalETL | **Authority:** Andrew-direct P0 (DE-found, COO GO 194143Z)
**Status:** CLOSED -- the DEPLOY (producer repoint env+IAM+code) LANDED + live-verified 2026-06-25T19:56Z (tag inf-pipeline-v1.7.76). Backfill/dashboard-rerun = tracked follow-ons (gated on stray-delete confirm + DS completeness-floor decision), RAVC'd to COO/DS -- NOT a stranded deploy.
**Change:** Repoint inf-etf-ownership-daily Lambda env `HOLDINGS_PREFIX: gold/holdings/ -> gold/canonical/holdings_` (raw shared-Orion $377.6M/$83.3M-ETFs -> canonical Inflection-owned $202.3M/$42.16M-ETFs). Env-only (schema-compatible, no code/artifact change). + backfill the inflection daily slices + signal DS AVGCAP re-run + re-run the presentation dashboard.

## Grounding (Rule 22, done)
- RAW gold/holdings/2026-06-24: TOTAL $377,628,472 / Opal-ETFs $83,336,939 / 815 accts.
- CANONICAL gold/canonical/holdings_2026-06-24: TOTAL $202,321,763 / Opal-ETFs $42,164,129 / 792 accts. (ties DE's numbers + the PartnerAnalytics Total AUA.)
- Canonical has ticker/market_value/account_id/date -> env-only repoint works with the existing producer code.
- 49F W2 VERIFIED CLEAN separately (RPS book $1.63B ties canonical fact_position; no shared-account inflation).

## Plan
1. [x] Verify premise + canonical path/schema/sums (grounded above).
2. [x] Edit TF (HOLDINGS_PREFIX) + open ledger.
3. [ ] Commit; safe-apply HALTGT (targeted inf-etf-ownership-daily module -- env update, in-place).
4. [ ] 0-diff; backfill: re-invoke producer for the inflection slice history (corrected $42M); verify the corrected slice + tie-out.
5. [ ] Re-run the presentation dashboard (corrected platinum); signal DS (AVGCAP re-run).
6. [ ] CLOSE ledger; tag + push. RAVC COO. CVO verifies + builds the per-partner tie-out gate.

## Rollback
Env-only change; revert HOLDINGS_PREFIX + apply. The slices/dashboard are re-runnable. Low-risk.

## Log
- 19:42Z opened. TF repointed (env-only). Committing + applying next.
- 19:43Z apply-1 (env): 1 changed. Invoke 403 -> IAM gap (role granted gold/holdings/* only).
- 19:45Z apply-2 (IAM gold/canonical/holdings_*): 1 changed. Invoke OK value $42.16M BUT wrong key (holdings_{date}.json) -> code bug (part_date includes holdings_ prefix).
- 19:48Z code fix (strip holdings_) -> build (sha YeoQp6K...) -> apply-3: 1 changed. Re-invoke 06-24: key daily/inflection/2026-06-24.json, total $42,164,128.89, source canonical. CORRECT.
- 19:55Z backfill 41 dates: 06-08..06-24 CORRECTED ($39.7-42.2M); 05-15..06-07 SKIPPED no-valued-source (May canonical 35% non-zero-MV rows trip the DS COMPLETENESS_FLOOR though total value $203.8M is present -- floor mis-fire, DS-contract question, flagged DS).
- 19:56Z CLOSED (deploy landed+verified). Follow-ons RAVC'd: (A) stray daily/inflection/holdings_2026-06-24.json needs delete-confirm (COO); (B) dashboard re-run held on the stray; (C) AVGCAP June re-run signaled DS, May pending the floor decision.
