# OPAL_ASSETS.P0-A -- DynamoDB schema + skeleton-emitter design (for CTO~B arch-gate BEFORE apply)

**Author:** 0.8.0_AE_CloudComp | **Date:** 2026-07-13 | **Status:** DESIGN -- awaiting CTO~B gate
(criteria msg 20260713T031139Z); row-shape CC to DS (0.4.0) for P0-B parity; stamp-alignment CC to
0.7.0~A (G6 owner). **Nothing applied.**
**Grounding:** TO `b9fafa92c` · PRD @ `79231da3e` · served artifact READ live
(`s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-07-10.json`) · G6 checker
`infra/aws/lambda/mdpf-pipeline/mdpf-freshness-checker/lambda_function.py:99-129` (EXPECTED_COHORTS)
· `alarms.tf` locals.g6_cohort_thresholds @ working-tree.

## 1. Table: `opal-assets-daily-aum`

| Element | Value | Why |
|---|---|---|
| PK | `cohort` (S) -- the G6 canonical id (`etf_divz` ... `49f_lt_aggressive`, 14 ids verbatim from alarms.tf) | CTO~B criterion 2: cohort history = ONE Query |
| SK | `bucket_date` (S, `YYYY-MM-DD`) -- the SNAPSHOT day; always advances | keyed by run-day NOT as_of (the AoR round-8 lesson, per your criterion 2) |
| GSI `by-day` | PK=`bucket_date`, SK=`cohort` (projection ALL) | a day's 14 rows = ONE Query |
| Billing | PAY_PER_REQUEST; PITR ON; no TTL | 14 rows/day; recovery > cost |

**Item attributes** (nullable = attribute ABSENT, never a fake value):
- `source_masters` (L of S) -- **multi-valued from day 1** (criterion 1). P0 population: 49f cohorts
  `["08242234"]`; `49f_schwab_custody` `[]` (nothing sourced) + `expected_masters ["08335338","08242234"]`
  (informational, the D1=SPLIT expectation) -- at P2 `source_masters` itself carries both.
- `value` (N) -- ABSENT when `state=missing` (a missing cohort carries NO number, never 0).
- `as_of` (S, ISO) -- the cohort's OWN-field as_of (criterion 3); ABSENT when missing.
- `state` (S) in `{fresh, rolled_forward, missing}`.
- `staleness_trading_days` (N) -- the G6 stamp mirrored (99 = missing sentinel, same as the checker's
  MISSING_STALENESS); NYSE-trading-day arithmetic identical to the checker.
- `partial` (S, optional) -- **criterion 4a home**: G4's interim flag lands as `partial="08242234-only"`;
  its removal at FULL dedup is a VALUE change (attribute absent), zero schema change.
- `ownership` (L of M `{firm_id, held, ownership_pct}`, optional) -- **criterion 4b home, my choice =
  NESTED attribute** (flagged per your ask): mirrors the served `etf_decomposition[].held_by_partner`
  shape VERBATIM so G4's fold writes 1:1; keeps the invariant "a day = exactly 14 items" (a companion
  item would break it); size is trivially inside the 400KB item cap. Companion-item alternative rejected
  for those two reasons -- overrule freely.
- `account_count` (N, optional -- by_model carries it), `source_artifact` (S, the exact served key read),
  `source_generated_at` (S), `emitted_at` (S), `methodology_version` (S) -- provenance per row.

**Write = idempotent UPSERT on (cohort, bucket_date)** (criterion 5): every re-run recomputes state/as_of
from the artifact -- a re-run cannot mask staleness because state is DERIVED at write, never carried.

**DS row-shape notes (0.4.0, 034120Z) -- ADOPTED, all three:**
1. **`state=missing` is an EXPLICIT ROW, never absence** (already the design; now stated as the rule): a
   day's census is ALWAYS exactly 14 rows -- so a MISSING ROW is a WRITER-failure signal, structurally
   distinguishable from data absence (the anti-silent-gap pattern; a missing row and a never-ran writer
   are otherwise byte-identical).
2. **rolled_forward provenance rule (verbatim-copy):** a `rolled_forward` row carries `value` + `as_of`
   VERBATIM from the last fresh observation, never re-derived -- inherited here by construction (the mdpf
   convergence gate performs the verbatim roll upstream; the emitter copies the served block as-is), and
   now BINDING on P0-B's emitter extension too.
3. **Upsert-on-rerun is the DELIBERATE choice** (idempotent daily series; contrast AoR round-8's
   append-only ledger, where overwrite collapsed history). Cheap insurance adopted: the write is
   UpdateItem with `first_written_at = if_not_exists(first_written_at, :now)` + `emitted_at = :now`, so
   a re-write is VISIBLE (first_written_at != emitted_at) without breaking idempotency.

## 2. State semantics -- ALIGNED TO G6 BY CONSTRUCTION (not re-derived)

The emitter mirrors the checker's EXPECTED_COHORTS extraction exactly (same per-cohort as_of source:
ETFs from `source_vintage.by_feeder.etf_net_assets`; partner cohorts from `as_of_by_partner[P]`;
by_model cohorts from their partner's as_of; cohort-8 = not-represented) and the SAME static
threshold map (alarms.tf locals: ETFs 3, partner cohorts 1):

- `missing`  <=> the cohort's expected source is NOT represented in the served partition (checker's 99).
- `rolled_forward` <=> represented AND (partner in `rolled_forward_partners` OR
  `staleness_trading_days >= g6_threshold(cohort)`).
- `fresh` <=> represented AND below threshold AND not rolled.

**Property this buys (AC4's cross-check, by construction):** a cohort whose G6 alarm is in ALARM can
NEVER read `fresh` -- both derive from the same inputs and the same thresholds. Parity is TESTED, not
assumed: acceptance includes a same-partition diff of my 14 rows vs the checker's structured-log
`cohort_freshness.cohorts[]` (state + staleness agree on all 14).
**Anti-fork note:** P0-A VENDORS the extraction with a cite + the parity test; lifting EXPECTED_COHORTS
into a shared module used by both lambdas is proposed to 0.7.0~A as the P0-B-adjacent refactor (his
artifact; his call).

## 3. Skeleton emitter -- `opal-assets-bucket-emitter` (Lambda, mdpf-pipeline family)

- **Reads ONE Opal-side served artifact:** the latest `platinum/mdpf/aggregate_aua/{date}.json`
  partition <= bucket_date on `opal-data-portal-v2`. It already folds EVERYTHING P0-A needs (verified
  live): `partners[].by_model` -> cohorts 5,6,10-14; `partners[49f].model_aua` -> cohort 9;
  `etf_decomposition[]` -> cohorts 1-4 (values + held_by_partner for the `ownership` home);
  inflection partner -> cohort 7; `as_of_by_partner` + `rolled_forward_partners` + `source_vintage`
  -> state derivation. Cohort 8 is absent -> `missing` (the honest row). Reading the ETF/inflection
  served outputs separately would DOUBLE-source what one served artifact already carries -- and the
  TO's comp-tools mandate forbids producer intermediates; this is the one true served surface.
- **bucket_date** = the UTC run day. Weekend/missed-run: rows still land for bucket_date, states/as_of
  derived truthfully from whatever partition is latest (e.g. today: latest = 07-10 -> ETFs would read
  rolled_forward at threshold, exactly what G6's alarms say).
- **Trigger:** EventBridge `cron(30 15 * * ? *)` (mdpf platinum lands ~14:53-15:04Z; 15:30Z = slack) --
  the sanctioned infra-schedule pattern (gold-run / comp_learns_producer / derive_runner precedent;
  LD-0175 governs agent loops, not infra). Manual invoke for the acceptance run.
- **IAM (new role, least-priv):** `s3:GetObject` on `opal-data-portal-v2/platinum/mdpf/aggregate_aua/*`
  + prefix-scoped ListBucket; `dynamodb:PutItem,Query` on the EXACT table + GSI ARNs; logs. Rule 22a:
  `simulate-principal-policy` on the exact ARNs WITH a positive control + a real DEPLOYED-role PutItem
  exercise (comp-iam DESIRED noted insufficient in the TO itself).
- **Zero sovereign surface:** one read, `opal-data-portal-v2` (Opal-side served). No bd/schwab/RPS/
  08335338/08242234 endpoints anywhere in the code path (AC6 grep will show zero).
- **Deploy:** code -> TF (mdpf-pipeline tree) -> source-map entry -> commit -> safe-apply -> 0-diff ->
  tag `mdpf-pipeline-v1.6.0` (or opal-assets-v0.1.0 -- COO/CTO~B naming call) -> push --follow-tags.
  Sized deliberately (256MB is fine here -- 10KB JSON + 14 puts -- but set 512MB/60s to clear the
  never-leave-defaults rule with margin).

## 4. Acceptance run (maps 1:1 to the TO's criteria)

1. safe-apply 0-diff; table ARN recorded.
2. Manual invoke -> 14 items for bucket_date; GSI Query(bucket_date) dump shows all 14 with
   distinct own-field as_of values (inflection 07-10 vs 49f 07-06 on today's data -- AC3's two-distinct
   check falls out of prod truth) + states {4-5 fresh-or-honestly-rolled ETFs+inflection, 8x
   rolled_forward @ 07-06, 1x missing (cohort-8)}.
3. Query(cohort=49f_intermediate) across >=2 bucket_dates (invoke twice / backfill yesterday) -> history
   in one query.
4. simulate-principal-policy evidence + positive control + deployed-role PutItem.
5. G6 parity diff (sec. 2). 6. AC6 sovereign grep. -> RAVC2 to COO.

## 5. Open items for the gate (explicit)

- `ownership` nested-vs-companion (sec. 1) -- my pick nested, flagged.
- Tag namespace (mdpf-pipeline-v1.6.0 vs opal-assets-v0.1.0).
- `expected_masters` informational field on missing cohorts -- keep or drop.
- EventBridge time (15:30Z) -- or event-driven off the platinum write (S3 event) if you prefer coupling
  to the artifact rather than the clock; S3-event is arguably cleaner (fires exactly when a new
  partition lands, no missed-run staleness window) -- **my actual recommendation**, flagged because it
  changes the trigger row in TF only.
