# AMGT_CORPUS round 37 -- CRPS-am-2 never-widen pair, CTO half (re-derive of the 96 with a currency on every money figure + re-pin)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~00:5xZ. **COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND37_AM2_SERVED_ACT.md`
@7c72c86057 (msg 29354). **Authority:** round-36 analysis @4c3e3755a7 ruling 1. The producer is am-1 @3ffe37a57a.

## What I read

- **The rule is the producer's own.** One writer of the served block (`stage_derive`, reached by `cmd_derive`, `cmd_admit`,
  `cmd_refresh` and this loop) and one writer of a figure's currency (`_figure_currency` at `<p>`). N = 1 in both cases, and printed.
- **The dry run on the act's exact path** (the real `stage_derive`, `sa_fallback=False`, 96 puts captured and not sent):
  - unlabelled money 23,365 -> **0** over 31,985 money figures;
  - reasoned 42 -> 51; the +9 is `CRNCY_ADJ_MKT_CAP` inheriting `CUR_MKT_CAP`'s measured held-out null on the same 9 names,
    verified on 3;
  - **values moved 0, labels changed 0.**
  - The census control the round-36 analysis asked for is the dry run's own before/after, so it discriminates.
- **Branches:** A (all derive), B (a name fails: it keeps its block and is listed) and C (the re-pin is refused: STOP before (r)).
  All three are covered.
- **Timing is a real dependency, not a wait.** The 2026-10-05 13:00Z fire runs on the old pin. A re-derive before it would be undone
  (served churn), and a re-pin before it would put new code under the fire am-5 reads. The legs run after am-5's read.
- **Blast radius:** up to 96 new write-once block keys where only `currency`/`currency_basis` differ, plus the task's Start In.
  Rollback is forward (re-derive from the same raw under the old producer) plus `-Register -Commit 74e00624b0`. Nothing is deleted.

## Conditions

1. **Gate 0 exactly as written:** am-5's read of the 10-05 fire is done; the dry run re-run at `<p>` on the post-fire raw shows after 0,
   values moved 0 and labels changed 0; `-Plan` names Python311 from the live task. Any deviation is a STOP.
2. **No vendor call.** The re-derive reads landed raw only (`sa_fallback=False`). Any Bloomberg or Seeking Alpha request during the
   act is a STOP.
3. **Branch C** re-pins back to `74e00624b0`, and the label loss the next old-pin fire would cause is named in a row, never hand-patched.
4. One NEVER-2 entry, `amgt-corpus-r37-am2`, opened before leg d.

**CTO HALF: SIGNED** for CRPS-am-2 legs 0, d, r and v under conditions 1-4.
