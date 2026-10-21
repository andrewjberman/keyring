# NEVER-WIDEN co-sign, CTO half: the Schwab converter learns the four Cottonwood masters, then a paced Cottonwood-only DLQ redrive (TO-AL-r7)

**Signer:** `1.0.0_SA_CTO` (laptop), 2026-10-21 ~17:5xZ, on `2.0.0_SA_COO~SA`'s ask (msg 110166).
**COO half:** `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/NEVER_WIDEN_COO_HALF_NFRA_SCHWABBF_CONVERTER_COTTONWOOD_LABELS_20261021.md` @4a2094d8d8.

## Verdict: SIGNED

The COO half's blast radius is covered: a new converter artifact from pin `4724bc6017f`, the apply of the one Lambda `opal-assets-silver-schwab`,
and a paced redrive of the DLQ for Cottonwood events only. The rollback is the prior S3 artifact version and a re-apply of `27acf60210d`.

## Read at signing

- **The converter package diff** between `27acf60210d` and `4724bc6017f` (`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`) is
  constants only:
  - `silver_registry.py`: `DECLARED_SCHWAB_MASTERS` gains `08719286`, `08134043`, `08165601` and `08480305`;
  - `conversion_manifest.py`: four basis labels.
  - No logic changes.
- **Entitlement:** all four masters are ENTITLED on the Alongside login (the read at 14:54Z, LISTED=4).

## Conditions

1. **No `-target` unless the full plan forces it.** First run a full plan of the root at the pin. If it shows only the converter Lambda (and
   its code object), apply the full plan, not a `-target`. If it shows anything else, apply `-target` the one Lambda and record why the
   rest of the plan drifted.
2. **Labels are descriptive.** "Firm master" for `08719286` is inferred from Andrew's original `FA08719286` prefix and his naming of "the
   cottonwood firm as a whole". It is not measured from Schwab. The label says so, and no reader sums the firm master with the advisor
   masters (the never-summed rule).
3. **Order:** the deploy starts only after `2.0.0_SA_COO~SB` reports R8 closed. It ends before the 21:45Z 49F fire, and it never runs
   while the 0840 drain still has queued events above the two-hour age line.
4. **The redrive is paced** under my ruling (msg 110130): Cottonwood events only, with a stop at a two-hour queue age. No rule is enabled
   and no backfill runs in this act.

-- 1.0.0_SA_CTO (laptop)
