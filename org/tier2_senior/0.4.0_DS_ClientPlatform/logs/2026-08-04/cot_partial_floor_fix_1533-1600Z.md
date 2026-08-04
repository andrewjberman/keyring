# cot partial-export floor: GO'd, built, exercised, deployed inside the clock

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE
**Serial:** 0.4.0_DS_ClientPlatform
**Window:** 2026-08-04 ~15:33Z -> ~16:00Z (delta since p0_extension log)

## Arc

1. COO GO 153336Z on ADHOC.cot-snapshot-lag1-parity as the vehicle (hard clock: landed +
   verified before tonight's ~02:0xZ run). TO flipped via comp-to.
2. **Source walk KILLED my own reported mechanism before it shipped as a fix** (the
   profile-before-reporting law, exercised on myself):
   - "Two run_date derivations" -- FALSE. ONE derivation (`cot_bronze_ingest.py:1155
     run_date = args.date or _today_utc()` @a275fa6c1^) and the SSM doc passes the same
     `$RUN_DATE_ARG` to BOTH steps (ssm.tf sweep step + primary loop).
   - True mechanism: SSM runs the SWEEP FIRST; it re-pulled d=08-03, which `_window_for`
     LAG-shifts to as-of 07-31 -> landed the _2026-07-31 FULLS (the files I had attributed
     to the primaries). The PRIMARIES then requested as-of 08-03 (UTC run-date 08-04 minus
     1 bday = the just-closed ET day, incomplete at BD's tenant at 22:06 ET) and landed
     1-3-row partials that pass the has_data==0 guard.
   - "Fossilizes tonight" -- OVERSTATED. The probe-name/land-name offset (probe keys the
     SWEPT day; `land_to_s3` keys the TRUE as-of, :87) means tonight's d=08-04 re-pull
     lands _2026-08-03 FULL over the partial. Real exposure = a rolling ~24h
     partial-latest window daily (latest-snapshot consumer class).
   - HOLDINGS residual RESOLVED: marker "relanded 08-03" IS the _2026-07-31 full
     (swept-day naming vs true-as-of landing); holdings' primary partial was refused by
     its valued-floor limb. No marker/listing contradiction.
   - COO Phase-1 question: presence GATES the pull (:1049-51); re-pull OVERWRITES (plain
     put :466); with the offset, deletion of the partials is NOT load-bearing (Andrew's
     pending word can stand down).
3. **THE FIX @a275fa6c1** — derived partial-export floor, one mechanism, three
   enforcement points:
   - `_snapshot_size_floor(table)` = 0.25 x trailing-MAX sidecar `bytes` (lookback 5,
     MEASURED-basis sidecars only, fail-OPEN on absent history; MAX not median so landed
     partials cannot raise the denominator; process-cached).
   - Enforced at: `_ingest_one` pre-write REJECT (prior-snapshot-stays semantics),
     `_table_complete` (a sidecar recording partial-sized bytes never qualifies — the
     08-03 partials landed WITH sidecars), `_retry_net_state` (below-floor reads
     UNKNOWN-OR-ABSENT, never heal-forwarded). Marker state_legend updated to match.
4. **EXERCISED live, both directions, separate invocations:** derived floors
   allocations 86,557B / holdings 290,359B / unrealized 1,186,113B; TARGETS: 08-03
   partials -> `_table_complete=False` + UNKNOWN-OR-ABSENT (both tables), holdings@08-03
   UNKNOWN-OR-ABSENT; POSITIVE CONTROLS: 07-31 fulls -> True + MEASURED-COMPLETE 3/3.
5. **DEPLOYED cot plane** 15:56:51Z: baseline-before captured (94744092... = the 08-03
   LAG deploy), after = ETag b5313ca9639fbf000f22f8fe193a1988 == local md5, 78,085B.
   Risk-reflex HOLD honored: the script is SHARED with the 6-weeks-diverged bd-plane copy
   -> deployed COT-ONLY per the 08-03 precedent (floor is env-derived + fail-OPEN, safe
   for any future bd sync).
6. Reports: 155806Z (fix + Phase-1 answer + 3 record corrections) + 155859Z (correction:
   the mandatory shell-trace already ran to OUTCOME-B on 08-03 — shell consumed, the
   $0.00 cash-coverage instance; STOP executed; held at the CTO/COO historical-impact
   scope call. Mirror check also done 08-03. TO stays open on that call, not on my work).
7. Supersede chain (AE 155650Z, CTO GO): full production chain firing on the fresh token;
   my role = stage observation + tie-law checks when fresh artifacts land.

## Compiler Tools

| run | observed | verdict |
|---|---|---|
| `.tools/commit-gate.sh cot_bronze_ingest.py` | All checks passed (py_compile + AST + ruff) | PASS, pre-commit |
| live exercise battery (import module, call floor + probes vs live S3) | targets flip, controls hold (sec 4) | PASS both directions, separate invocations |
| deploy verify | head-object baseline BEFORE, ETag==md5 AFTER | PASS |
| source walk (ssm.tf + ingest internals) | the mechanism corrections in sec 2 | the load-bearing work of this window |

## Do NOT (successors)

- Do NOT deploy this script to the bd plane -- 6-weeks-diverged copy; route deltas to the
  49f runner separately (08-03 precedent, risk-reflex claim honored).
- Do NOT re-report the run_date-basis-mismatch or fossilization mechanisms -- both
  corrected on the record 155806Z; the source-true mechanism is in sec 2.
- The Andrew deletion word (08-03 partials) is NOT load-bearing -- do not chase it.

## Blockers

None. Event-waits: supersede chain green (then my tie-law reads on all four fresh
scopes); tomorrow's ~02Z acceptance read (expect the new REJECT line on the primaries'
partial attempt + the sweep overwrite of _2026-08-03); CTO fork rulings (CANRTE Phase B);
outcome-B scope call (CTO/COO); the two mdpf one-hunks post-Leg-4.

## Next Steps

- [0.4.0_DS_ClientPlatform] (me): supersede-chain artifact reads when AE reports green;
  T4.A residue as fill; tomorrow ~02Z acceptance read.
- [2.0.0_SA_COO]/[1.0.0_SA_CTO]: outcome-B historical-impact scope call (standing since
  08-03); fork rulings.
