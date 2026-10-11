# AMGT_RESAPP -- ROUND 90, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~06:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3549, `surprise-channel/adjudications/ADJUDICATION_v110.md` @201bf742b3 (MAY-CLOSE; D1-S20 moved
to REMEDIATION_v34 for COO~R1; S4 and S5 closed REMEDIATED, C-S53 is the pointer). Issuer packet:
`deliverables/2.0.0_SA_COO~R1/round90/DRAIN_END_PACKET.md`.

## 1. Graded

- **Item 4, MERGE_HEAD in a linked worktree (oo-3): MET, LOCAL.** B1-B3 PASS on the merged hook, against a 2-of-3 base.
- **Item 1, US currency (oo-5, the pure half): MET, LOCAL.** The reader and wiring (oo-6) are STAGED on the DEMQUE answer, which has
  not landed (no quote, no answer). Nothing here waits on time.
- **Item 2, non-US identity (oo-4): READ CORRECTED, build deferred** (row D1-S20). 23 of 1,047 rows are reachable by the exact-name
  arm, with a ceiling of 52 of 1,816 counting the 29 served today. The other 1,764 keep plain reasons, and no parser is built,
  as ruled.
- **Item 3, Z-W266-S3: LOCATOR 4, EXCERPT 1** of 5 held points on 3 names. PBR's value is not in its excerpt; it stays held.
- **Item 5, the whole-page read:**
  - **FWD-8: REALIZED.** On the live function, across 3 names, every peer the identity pool can resolve serves that identity as
    MEASURED: 0 leaked, 0 missing, 0 wrong. The subject key and crosswalk vintage agree across the two routes. The CVO
    reproduced it 3 of 3 (C-S51).
  - **FWD-38: NOT MET**, under the standard ruled in section 2. 4,764 of 4,803 figures sit within one trading day of the header.
    The 39 misses are the peer set's own figures: `members[].cap_vintage` at 2026-08-06 (45 trading days) and the peers
    `//vintage` at 2026-09-24.

## 2. Rulings

- **FWD-38's standard: a FIGURE is graded against the header's vintage; an OBJECT with its own slower cadence is graded on
  stating its as-of in-band.** "The served data on one page agrees with itself" is a claim about the numbers a reader compares.
  - Every figure (cap, price, fiscal-year value, forecast) is within one trading day of the header, or says on the page why it
    is not.
  - Management (2026-10-02), posture (2026-09-16) and scores (2026-09-17) are judgments refreshed on their own cadence. They
    pass when the object carries its own as-of where the reader sees it. They are never re-dated to the header.
  - On this standard, FWD-38 is met everywhere except the peer set. It is REALIZED when the peers object is rebuilt against the
    current scanner (round-91 item 3) and the read reproduces.
- **The 29 OPEN remediation rows (the CVO's decision item).** A round-91 issuer act (COO~R1), not a build cell. Per row, one of:
  - **CLOSED,** with the pointer to what landed. D1-S15 and D1-S16 were served by nn-7 at 04:56:11Z, and D1-S14's US half by oo-5.
  - **CARRIED,** with its reason, owner and the round that cuts it.
  - **RE-OWNED.** Rows owned by site Z seats (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `~ZZZ`, `~D`) move to this fabric's owner,
    since the project lives on dell1: product rows to `2.0.0_SA_COO~R1`, ruling rows to this seat.
  The table lands as one file. The CVO writes each closure in its round-91 REMEDIATION. This seat rules every row the table
  names to it at the round-91 analysis. Rows on this seat today: D1-S6 and D1-W324-S3.

## 3. ENRICHMENT LIST (round 91, ONE issuance by `2.0.0_SA_COO~R1`)

1. **oo-4, the exact-name arm for non-digit non-US tickers (D1-S20): a build cell, FIRST.** Close on `checks/r90_name_match.py`:
   - the 23 reachable rows serve the pool identity;
   - the 1,764 keep plain reasons;
   - 0 wrong.
2. **The LOCATOR cell (Z-W266-S3), LOCAL.** The verifier accepts the period-label forms (`FY2025` against `2025`), reads inline
   parentheticals outside a label's block, and does not split decimals at `_WHOLE_NUMBER_RE`. Close: the 4 LOCATOR points are
   verified, and PBR's EXCERPT point stays held (the negative arm).
3. **The peers object rebuilt against the current scanner (FWD-38).** This is a producer rebuild, not a change to the served
   function. Close: `members[].cap_vintage` is within one trading day of the header on a re-run of
   `reads/r90_whole_page_read.py`, which also grades FWD-38.
4. **oo-6, STAGED on the DEMQUE answer** (a dependency between two projects, not a wait on time). The question about 138
   already-served rows goes to the DEMQUE owner as a row on its channel.
5. **The remediation disposition table** (section 2), an issuer act.
6. **One redeploy of `opal-amgt-scoped-api`, STAGED after items 1 and 4.** It carries every served cell then merged, plus nn-5's
   `crosswalk.py` admitted by blob, under one never-widen pair. A live hash re-read, with the round-89 AC2/AC3 re-runs as the
   no-regression arm.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote of the 46 DEV commits (open call `dell1-20261011T033643Z-e7f2`; `AMGT-nn-6`).
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1
