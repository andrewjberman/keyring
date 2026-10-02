# ETFS_RIVALS round 5 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-02 ~13:25Z)

**Inputs:**
- the round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` @6dcb0074e4;
- the round-5 compile `surprise-channel/adjudications/ADJUDICATION_v5.Z.md` (part A @04a70a4241, part B with this slug);
- `remediations/REMEDIATION_v5.Z.md`;
- the FAST grades `deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md` (11 grades, @f751aac898 .. @5488015d8f);
- the drain handoff (COO~RV msg 28454);
- CRO~RV's rulings `org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md` (CALLs 1-12).

## 1. Round 5 as delivered

- **45 of 45 orders terminal:** 38 complete, and 7 superseded by the FAST lease from 05:08Z (the A1 cells pt/pg/rk/tb/ic/ai-1/ai-2,
  built by the seat and graded below). m-2, l-1 and s-6 drained at 13:0xZ (@e4e9eedfa9, @213540f408).
- **Suite:** this seat's run on CLOUD 383e989b95 reads 410 passed, 2 skipped, 0 failed.
- **Channel:** 133 rows, all dispositioned.
  - Part A: 6 dismissed.
  - Part B: 4 dismissed.
  - S13 and S14 graduate, both INERT.
  - W5-S21 and W3-S15 are REMEDIATED in place by m-2 and s-6; W4-S9 is REMEDIATED in code (part A). Rulings 8-12 closed five
    fabric items.
- **Still ARMED:**
  - W4-S9 (real; the disarm is COO~RV's): the windowed G1 code has been in every deployed package since 7aa0186d45, but no
    marker batch above 45 dates has run on the Lambda.
  - W5-S12: a census artifact (graduated without a disarm block; ruling 10 closed it).
- **Round-4 live proofs:**
  - S10 is proven by this seat's read of the vehicle log: `bbg_tplus1_20261002_070002.log:186`, enrichment exit 94 = landed,
    the meaning taken from `scheduled_daily_pull.cmd:406-407`.
  - W4-S10 is proven on the served 10-02 manifest (GQGU lag 0).
  - W4-S13 (G2 per-fund attribution at the 07:00 fetch) is reported OK by COO~RV. This seat did not read the G2 rows.

## 2. The FAST interval (05:08Z-13:0xZ) -- the section `/closer-drive` requires

- **10 graded served states, plus one offline grade:**
  - 6 states of the 10-01 page (1001 to 1001g);
  - 4 states of the 10-02 page (1002b to 1002e), the 10-02 page having first been published by the scheduled chain;
  - 11 applies (r1-r11), each after its never-widen pair. At each graded pin this seat checked the deployed bytes against the
    pin, with a positive control. r5's intermediate apply was superseded by r6 within 16 minutes and was not graded on its
    own.
- **One FAIL, grade 2:** ETFT's YTD contributions summed to -188.51%, because a zero valuation was read as a -100% day. The
  builder's own 12 A1 checks were 12/12 PASS on that code. It was fixed in 30 minutes (grade 3).
- **Findings raised and closed in the interval:**
  - F1-F4: ETFT, money-market lines in the rankings, missing data shown as "no trade", the sector panels;
  - G4-1: the split guard refused 7 real moves (CALL 8; this seat's own recommendation was weaker and CRO~RV corrected it);
  - G6-1: the trend sector guard;
  - G8-1: BASG false grounding FAILs (CALL 11 re-grade, verified 24/24 same text);
  - G8-2: phantom 0->0 exits (CALL 12);
  - G8-3: money-market lines in the trade log;
  - G10-1: CALL 12's notional clause.
- **Production evidence:** the scheduled chain (batch 096abf8e) published the 10-02 page with the three A1 tables at 11:04Z on
  its own.
- **Open after the interval (all P2, none on the served page's figures):**
  - F5: source identifiers in the AI prose (a1-chain/4 built, not yet run);
  - CGIC's stored AI text narrates money-market flows (the exclusion applies to future runs);
  - the CALL 2 floors;
  - the publish-page Lambda's bronze GetObject (parked by COO~RV);
  - the long census list.

## 3. Recommendations, per driver

**For CTO**
- **P1 -- a plausibility guard inside the A1 producers.** Grade 2's -188.51% passed every mechanical check the builder wrote.
  The page guardrails refuse bad holdings, but nothing refuses a bad ranking. Recommend a guardrail in `guardrails_config.json`
  (PROVISIONAL) that refuses a holding_contribution table when any fund's period total lies outside a stated band, or when a
  single holding exceeds a stated share. The next -188% then refuses instead of serving. It needs a judgment criterion in
  round 6's grading, not only mechanical ACs.
- **P2 -- the PRD carries CALLs 1-12 nowhere.**
  - The rulings live in a CRO deliverable and in code comments.
  - Recommend a PRD addendum that lifts the contract-level ones into the ratified text: the price-source order, the
    ratio-symmetric bands, refusal disclosure, the split rule, the GICS fallback and `sector_source`, the 0->0 and
    money-market display rules, and the re-grade rule.
  - The L4-R signer then reads the contract the code follows.

**For COO**
- **P1 -- the AI accounts are a seat act.** The 10-02 accounts exist because a seat ran them (CALL 5). Tomorrow's scheduled page
  carries none unless a seat runs the chain again. The parked Lambda wiring and the dedicated secret are what make FWD-16/17
  production; until then the page's AI section depends on a seat being awake.
- **P2 -- W4-S9's disarm needs one deliberate run.** Fire one marker batch above 45 dates against the deployed Lambda, the round-6
  backfills being the natural carrier, rather than waiting for an organic large batch.

**Deferred:** W3-S11 (dividend currency) and W3-S12 (child identity) stay round 6 as ruled. No change is recommended.

## 4. What you should have asked but did not

**Who graded the grader?** The FAST interval worked because every served state was read against the served bytes by a seat that
did not build it. Every defect this seat found had passed the builder's own checks: ETFT -188%, the 7 wrongly refused moves, the
false grounding FAILs, the phantom exits.

The interval's one structural weakness is the reverse case: this seat's own instruments. Twice today a check of mine returned a
confident number from an empty reference set:
- an invented-ticker check against a manifest with no G1 list read 82 of 82;
- a search for BASG's failing figures in the `text` field found none, because they sat in `observed`/`inferred`.

Both were caught by a positive control or by re-reading the source. The question for round 6's L5 is whether every judgment
criterion the CVO grades names its positive control in the order, so a grader's empty denominator fails loudly instead of
reading as a finding.

-- 3.0.0_SA_CVO~RV
