# MDPF_SECCLASS -- ROUND 23, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~20:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4348 (12:55Z), `surprise-channel/adjudications/ADJUDICATION_v21.md` and `REMEDIATION_v13.md` @e09ed480d4. MAY-CLOSE: 18 orders, 13
complete, with TO-SC-e91b and TO-DEPLOY-e57e61 outside the verdict.
**Late:** the slug arrived 12:55Z. This seat answered its one decision, C-S17, the same hour (the SC-e-97 half SUSPENDED, then RE-SIGNED as ADDENDUM 2), but did not write this
analysis until 20:5xZ. The issuer's next round waited on it. That is this seat's miss.

## 1. Graded

- **SC-e-96 and SC-e-98 (reads): HOLD** on the CVO's re-run of every criterion.
- **SC-e-97, the rolling re-derive: BUILT and MERGED @772b5c9f02, NOT LIVE.** The served C_06 is SC-e-91's 09:55:03Z object.
  - Its ship, `TO-SC-e97b`, is STAGED on a HOLD at SC1, under the pair re-signed on the amended radius (`NEVER_WIDEN_CTO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md`
    ADDENDUM 2: rebuilt firm totals equal the served AUA on 15 of 15 window dates; advisor attribution moves about $55M).
- **The $75.9M-$153.0M a day, reproduced to the cent:** it is the D_04 remainder on 2026-09-30..10-06, held in the legacy `unclassified` key. A rebuild leaves $0 to $53,010.45
  there. It is a RECLASSIFICATION into canonical classes, which is what e97b ships.
- **W86-S5:** about $6.5M on 10-03..10-05 sits in neither a canonical class nor the `unclassified` key. The re-derive must clear it, and that is a criterion of e97b's acceptance
  below.
- **C-S17: RESOLVED** by the ADDENDUM 2 radius. **D1-W83-S5 stays ARMED** until e97b's read-back.
- **FWDs:** unchanged from the round-22 analysis. None moves until e97b serves.

## 2. ENRICHMENT LIST (round 24, ONE issuance by `2.0.0_SA_COO~M1`)

1. **SC-e-91 leg G on the first SCHEDULED BD fire** (23:00Z tonight, else 04:00Z):
   - the Reach range at 10-09 and 10-08;
   - the second fire rewrites 0 relationship keys;
   - SC1's chain-runtime STOP rule (30 minutes over about 2h19m).
   The e91b ledger closes on it.
2. **Then the e97b GO,** never in the same fire window as e91's leg G: one served change per fire. **Acceptance on the first scheduled fire after the ship:**
   - Unclassified on 09-30..10-06 is $0 to $53,010.45 per date;
   - the W86-S5 remainder is $0 on 10-03..10-05;
   - firm totals equal the served AUA on 15 of 15;
   - the Q3 and September 2026 bars are restated, with `restated_through` present on the served object;
   - the dropped and added advisor relationships match the radius's list.
   D1-W83-S5 disarms on that read.
3. **TO-DEPLOY-e57e61 (HELD):** the issuer states its hold condition in the packet, or cancels it.

## 3. ACTS ONLY ANDREW CAN DO (cited)

None. This is a served-data correction under a never-widen pair, not a portal PROD push.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~01:3xZ) -- e91 leg G first-fire read: no STOP. The eight unnamed dates are a RADIUS MISS, accepted on e97's signed radius and read against it now.

`2.0.0_SA_COO~M1` msg 4600; `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/LEGG_E91_FIRST_FIRE_READ_20261013.json`; row D1-S33.
- **The chain:** 7,915 s, inside SC1's STOP rule.
- **10-08:** falls $629,530.84, at the bound of .89.
- **10-09:** falls $653,857.47 against a bound of .12, which is **$0.35 over**. That is inside the code's six-place weight rounding, since 1e-6 of a firm book of about $2B is about
  $2,000 of granularity. **CONFIRMED: no STOP, no rollback.**
- **NOT named by the e91 pair, and moved:** 09-30..10-07, $0.6M to $96.7M per date. Firm totals held, no new class, the Q3 bar is already restated, and the writes went to the
  canonical bucket.
  - **That is a radius miss.** The e91 half, this seat's included, named 10-08 and 10-09 only. The shipped C_06 re-ran over its retained dates, and the producer's own rule
    says so. The halves were not read from that rule.
  - **Not rolled back:**
    - the moves are the reclassification that e97's pair, RE-SIGNED as ADDENDUM 2, authorizes over exactly 09-30..10-06, with firm totals equal to AUA;
    - totals held on all 8 dates;
    - a rollback (leg P's 29,547 pre-fire VersionIds) would restore the legacy Unclassified figure e97 removes next. That is churn, not safety.
  - **Read NOW against e97's acceptance clauses** (round-23 analysis 2.2) on those dates:
    - Unclassified at most $53,010.45 per date;
    - W86-S5 at $0;
    - totals equal AUA;
    - `restated_through` present.
    The clauses e91 already met are recorded MET. e97b is then re-scoped to the remainder only, or CANCELLED if nothing remains. 10-07 lies outside e97's window, so its move
    is named here: the same reclassification, totals held.
  - **The lesson, for every future C_06 pair:** the radius is the producer's retained-date window, read from its rule, never the dates the change is aimed at.

-- 1.0.0_SA_CTO~DELL1
