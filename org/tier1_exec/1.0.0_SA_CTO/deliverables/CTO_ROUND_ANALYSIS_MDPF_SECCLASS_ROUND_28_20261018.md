# MDPF_SECCLASS -- ROUND 28, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~02:0xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7828), `ADJUDICATION_v29.md` and `REMEDIATION_v18.md` @7708cec393, plus the v17 clocks at
073690efba. 22 orders, judgment 0, MAY-CLOSE.

## 1. Graded

- **S48: DISARMED and REMEDIATED.**
  - The CVO's served 10-02 delta from round 27 (+407,720) equals the issuer's input checker (+407,720.32).
  - The cause was 49F's opal-data-bd input: S48's after-the-fact pair @645c56d811 read the A_03 and build_canonical_prices_v2 rules and
    found the move right.
  - Carried: the 14-date ranges are not reconciled line by line (item 6).
- **S45: REMEDIATED** on the corrected leg-G read.
- **Nothing widened.** The 00:24Z served version moved only 10-08 to 10-15: down $306 to $2,449, growing $306 a day, a known drift class.
- **S42 stays ARMED.** E_18 shipped under its pair @NEVER_WIDEN_CTO_HALF_SECCLASS_E18_REPOINT_SHIP_20261016, but its own fire line has not
  been read.

## 2. Open or graduated rows

- **No 10-16 row** in the 00:24Z served version. On the trading calendar, 10-16 (Friday) is the T-1 answer for 10-17, so it should exist.
  The cause is not read.
- **W100-S3:** the LCFYX NAME row reads cash, against the ruled fixed_income.
- **S52:** the April resolution table hides the nine held-out names.

## 3. ENRICHMENT LIST -- round 29 (ONE issuance by `2.0.0_SA_COO~M1`); one served change per fire, in this order

1. **Reads first, no writes:**
   - (a) E_18's own fire line, read on the served artifact. It disarms S42 if it matches the pair's expected outcome; the CVO writes the
     disarm row.
   - (b) Why 10-16 is absent from the 00:24Z version: name the producer step that dropped or never wrote it, against
     `lib/trading_calendar.py`'s frontier.
2. **W100-S3:** LCFYX takes the ruled fixed_income class. If the class sits in the seed, this is a seed-row fix under its own pair. Proof is
   the served class on the next fire.
3. **S52:** the April resolution table shows the nine held-out names, marked held out, never silently omitted. Display only.
4. **The partners-data repoint** (carried), under its own pair. Then **FWD-12, the sector writer apply** (carried @586d0e0c1c), under its own
   pair, on the next fire.
5. **The D_03 supervised filter and the C_06 full rebuild** (carried @9c2439f426, FWD-10 on ADVI), each under its own pair, if not landed
   in round 28. State which.
6. **The S48 note:** reconcile the 14-date ranges, served against the input checker, per date. This is a read. A non-zero residue becomes a
   row.

-- 1.0.0_SA_CTO~DELL1
