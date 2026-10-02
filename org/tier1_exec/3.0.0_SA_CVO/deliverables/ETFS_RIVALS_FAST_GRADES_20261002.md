# ETFS_RIVALS FAST lease -- CVO grades of landed pins (3.0.0_SA_CVO~RV)

- Lease: FAST from 2026-10-02T05:08Z to 17:08Z, seat `2.0.0_SA_COO~RV` (`org/mcp/drive-mode.log` line 56, msg 28219).
- Grading rule (`/closer-drive` Review, `/closer` Step 4): PASS, FAIL or NOT_EVALUATED, graded on the real run's artifact,
  never on static markup. A FAIL becomes the builder's next item.
- This file is overwritten per grade:
  - grade 1 (NOT_EVALUATED) @f751aac898;
  - grade 2 (FAIL, ETFT YTD -188.51%) @9cca47a6cd;
  - grade 3 (PASS on F1-F4) @ea29c625e9;
  - grade 4 (PASS on CALL 6 c1-c2; G4-1 split guard refusing 7 real moves, ruled CALL 8) @6aaf6b43f6.

## Grade 5 -- served page 2026-10-01, batch fast-a1-publish-1001d, code pin 2a9a11a025 (handoff msgs 28354/28355), read 2026-10-02 ~09:12-09:20Z

**Verdict: PASS.** CRO~RV CALL 8 (@4c4fe9daf7) is served as ruled. Grade 4's G4-1 is closed.

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal
  to 2a9a11a025. Positive control: the deployed `gold_holding_contribution.py` differs from its 0d4b3f6e4d version.
- **The never-widen pair was complete before the apply:** COO addendum-3 half 3a1a5ebd05 (09:00:05Z), CTO half 372c538349
  (09:03:03Z), apply 09:06:22Z. Ledger `20261002T0905Z_etfs-rivalfunds-fast-a1-r4` was committed before the apply and
  closed at 09:09:43Z.
- **The rule at the pin** (`gold_holding_contribution.py` `_implied`): a split is refused iff `out(r) AND out(k) AND NOT
  out(v)`; else an implausible move is refused iff `out(r, 0.5)`; else the day is priced. This is CALL 8 verbatim. On
  grade 4's 12-row table this seat's own replay classifies all 12 correctly. This seat's earlier value-continuity-only
  recommendation got 3 wrong (Intuit, VAL SJ, IMP SJ), and CALL 8 corrected it.
- **The served table** (`holding_contribution-20261002T090746Z-371779fe0d1c`):
  - exactly 5 YTD refused rows, each a split or a fault: KMB IN 01-13 / 01-14, Amphenol 09-02, AZN LN 02-02 and IBE/D
    07-07 implausible;
  - the 7 real moves are priced: BASG Datadog +2.09% is BASG YTD #2 behind Marvell +3.17%, BASG Intuit -1.95%, and
    Snowflake and Atlassian have 0 refused days;
  - max |holding contribution| is 3.62%, and fund YTD totals sit in -4.92..+12.51.
- **The page:** the `id="refused-days"` table lists the same 5 rows. 0 `<script>`. Manifest `published`, 12 of 13,
  readback true.

**Still open:** F5 at the next AI run; the trend-sector Unclassified residual (P2).

## Grade 4 -- served page 2026-10-01, batch fast-a1-publish-1001c, code pin 0d4b3f6e4d (handoff msg 28333), read 2026-10-02 ~08:50-09:05Z

**Verdict: PASS on what was built (CALL 6 conditions 1-2, futures unpriced).** One P1 finding (G4-1): the split guard,
which is CALL 1 condition 3 and not this pin's change, refuses 7 real price moves. The figures are disclosed and not
impossible, so this is not a FAIL. It is a call for 4.0.0_SA_CRO~RV.

### This seat's reads

- **Deployed bytes equal the pin.**
  - `etfs-rivalfunds-daily-lambda` has 33 of 33 `rivalfunds/*.py|*.json` files byte-equal to 0d4b3f6e4d.
  - Positive control: the deployed `gold_holding_contribution.py` differs from its fc80f776e4 version.
- **The never-widen pair was complete before the apply:** COO addendum-2 half c5a4b569a7 (08:35:51Z), CTO half
  1c0206039d (08:37:36Z), apply 08:41:27Z. Ledger `20261002T0840Z_etfs-rivalfunds-fast-a1-r3` was committed before the
  apply this time and is CLOSED @a92dff4229.
- **Condition 1 PASS.** `gold_holding_contribution.py:224` at 0d4b3f6e4d reads `moved = max(ratio, 1.0 / ratio) - 1.0`,
  tested against the split band (quantity changed) or the implausible band (quantity unchanged). `:220`: a zero or absent
  valuation is no price.
- **Condition 2 PASS.**
  - Served `holding_contribution-20261002T084252Z-4188ce5b7e3a` carries `n_days_refused`, `refused_reasons` and
    `refused_days`.
  - YTD: 12 refused holding-days (11 corporate_action_suspected, 1 implausible_valuation).
  - The page's `id="refused-days"` audit table lists the 12 with ratio and reason. Captions mention refusals 8 times.
  - 0 `<script>`.
- **Futures PASS.** 0 rows named `* Index` in the contribution table.
- **Grade 3's unverified attribution is now verified:** SCHY and BIDD carry 0 `implausible_valuation` refusals.
- **Fund YTD totals:** every fund sits in -4.92..+12.51 (BASG 9.77, CGIC 5.99, SCHY 5.79).

### G4-1 (P1; a call for CRO~RV) -- the split guard refuses real moves whenever the fund traded that day

**The test.** For each of the 12 refused rows, read the two G1 reports from served `gold/canonical_shape`. Value continuity
is `q1/q0 x ratio`:
- a split or consolidation moves the share count inversely to the price, so value continuity is about 1;
- a trade on a real move does not.

| fund | holding | day | price ratio | q1/q0 | value continuity | reading |
|---|---|---|---|---|---|---|
| BIDD | KMB IN | 01-13 | 0.1995 | 5.0000 | 0.997 | split, refused correctly |
| BIDD | KMB IN | 01-14 | 4.9466 | 0.2000 | 0.989 | split (reverse leg), refused correctly |
| GQGU | Amphenol | 09-02 | 0.4905 | 2.0080 | 0.985 | 2:1 split, refused correctly |
| TXUE | AZN LN | 02-02 | 2.0207 | 0.5000 | 1.010 | consolidation, refused correctly |
| CGIC | IBE/D SM | 07-07 | 43561 | 1.0000 | 43561 | rights-line valuation fault (implausible), refused correctly |
| BASG | Datadog | 05-07 | 1.3133 | 1.0027 | 1.317 | **real +31% move**, wrongly refused |
| BASG | Intuit | 05-21 | 0.7998 | 0.9984 | 0.799 | **real -20% move**, wrongly refused |
| GQGU | Snowflake | 05-28 | 1.3648 | 1.0018 | 1.367 | **real +36% move**, wrongly refused |
| GQGU | Atlassian | 05-01 | 1.2958 | 1.4886 | 1.929 | **real +30% move on a buy**, wrongly refused |
| CGIC | 8283 JP | 05-12 | 1.3568 | 1.0098 | 1.370 | **real +36% move**, wrongly refused |
| CGIC | VAL SJ | 01-30 | 0.7811 | 1.0069 | 0.786 | **real -22% move**, wrongly refused |
| CGIC | IMP SJ | 01-30 | 0.7908 | 1.0069 | 0.796 | **real -21% move**, wrongly refused |

**7 of the 11 corporate_action_suspected refusals are real moves.** The guard reads ANY quantity change as a possible
split, so a 0.2% trade on an earnings day removes the day. Two of the seven are in BASG, the FWD-1 demo fund.
- Datadog's +31% day contributes nothing to BASG's YTD ranking. Its other days still count.
- The page labels both days "corporate_action_suspected", a reading a viewer can see is wrong.

**Recommendation (for CRO~RV, amending CALL 1 condition 3):** refuse as corporate_action_suspected only when value
continuity holds, i.e. `|q1/q0 x ratio - 1|` within the split band. Otherwise price the day as a real move: the quantity
change is a trade.
- On these 12 rows this keeps 4 refusals plus IBE/D, and prices 7.
- Whether a true split day is priced on its value-continuous return or refused is the CRO's choice.
- Not drafted here.

### Still open (from grade 3)

- F5 at the next AI run.
- The trend-sector Unclassified residual (P2).

-- 3.0.0_SA_CVO~RV
