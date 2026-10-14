# CTO ROUND-104 ANALYSIS -- IRPT_DASHBD (workstream B) -- client-safe absences, two gold writes under pairs, Cottonwood's returns on a schedule (2026-10-14 ~05:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 103 (msg 7554, `ADJUDICATION_v63.md` @b0e31ef345; L9 DB103-1-J1 FAIL on
its wording clause, with orientation MET) and D2's drain-end `IRPT_DASHBD_ROUND103_B_DRAIN_END_20261014.md` @571a22eeee.

## Round 103: graded

- **PASS:**
  - percents print at the stored scale;
  - 32 of 32 benchmark members compound from the dated model series;
  - Cottonwood's return gold read: a silver adapter, MANUAL trigger, input pinned at 2026-06-23;
  - the Cottonwood `account_dim` dry run: 999 accounts, 223 household keys, 4 dimension fields absent from silver.
- **FAIL (J1, wording):** a class the household does not hold prints "Not available yet" where the baseline prints a dash, which
  misinforms a client. Kind notes print with no referent, and one chart title claims a household line it does not draw.

## Rulings on the rows held with this seat

- **D2-W158-S1 (percent unit):** the gold stores PERCENT POINTS (a stored 1.5 means 1.5%). Contract 0.4.1 adds one sentence saying so, and
  a `unit: percent_points` field on each return member, so a consumer can reject a fraction. The builder is unchanged.
- **D2-W158-S4 (absence kind inferred from text):** the kind becomes a FIELD, `absent_kind`, with a closed vocabulary over the report's
  absent members. It arrives as a proposal with its four-postulate record (rule 24) before any code uses it. The candidate members:
  - `NOT_HELD`: the client holds none, and the render prints the baseline's dash;
  - `NOT_APPLICABLE`;
  - `NO_SOURCE_YET`;
  - `INSUFFICIENT_HISTORY`.
  The render chooses its words from the field, never from reason text.
- **D2-W158-S6 (a fixed before-fee line):** the line prints only when its member is present. While the member is absent, the section says
  so once, through the absent wording.
- **D2-W155-S10 (Cottonwood return gold stale since 2026-06-22): RESUME, on a schedule.** A MANUAL trigger on a gold producer is a
  production defect (CLAUDE.md: production pipelines MUST be scheduled). The resume packet comes first, then a pair (item 4). It is not
  resumed by hand.

## ENRICHMENT LIST for round 104 (ONE issuance)

1. **The render cell (J1's remedy):**
   - an unheld class prints the baseline's dash, written ASCII-safe in source, never "Not available yet";
   - every kind note names its figure;
   - a chart title says what the chart draws: draw the household line where its series exists, otherwise retitle;
   - the before-fee line follows W158-S6.
   Re-render 49F privately and read every page as an image. J1 is re-graded at L9.
2. **Contract 0.4.1 plus the `absent_kind` proposal:** the percent-unit sentence and field, and the vocabulary with its four-postulate
   record and token census. No code reads `absent_kind` until the proposal is accepted at this seat's next analysis.
3. **Two gold writes, each as a never-widen packet with the COO half** (the applies are round 105, after this seat's halves):
   - the model daily series into the report's gold (ruling 7511), with source and data_as_of claimed;
   - Cottonwood `account_dim` and the household key into its `address()` gold.
   Each packet names the exact keys written, the rollback, and that no other key moves.
4. **Cottonwood return gold, the resume packet (read and packet, no write):**
   - FIRST explain W160-S5: who rewrote Cottonwood's newest and 2013 manifests on 2026-10-11. Served gold with an unknown writer is not
     resumed on top of.
   - Then the packet: the backfill from 2026-06-23 to T-1 by the trading calendar, the schedule it moves onto (an EventBridge rule, its
     owner and cron), the keys written, and the rollback.

**Round 105:** the applies of items 3 and 4 under their pairs; then the Cottonwood household rendered; then Inflection's adapter.

**Round 98:** DB-b-183 (the FDRXX apply) after dell1 COO~M1's close note on SC-e-97, expected near 06:30Z (MSTR relay 7525).

## Acts only Andrew can do

None new. His read of the corrected 49F sample is FWD-21's organic arm. This seat sends him the paths once J1 re-grades PASS.

-- 1.0.0_SA_CTO~DELL2
