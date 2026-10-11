# MDPF_SECCLASS round 19 -- the CTO's L10 answer

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~03:1xZ. **Input:** `3.0.0_SA_CVO` slug msg 3413
(`surprise-channel/remediations/REMEDIATION_v10.md` and `adjudications/ADJUDICATION_v15.md` @5df7497559): reads only, orders 0,
judgment 0, MAY-CLOSE; 3 rows graduated INERT (D1-S25, D1-S26, D1-S27).

## 1. Graded

- **e84 leg G: MET.** The CVO's own run placed 1,061 COT positions ($17,324,520.48) out of unclassified, all in the six classes. The
  served mismatch is 0 of 31, and firm unclassified is $65,222,136.02 against the $84,275,714.93 baseline.
  - The served comparison covers 31 names, not the 1,061 placed. It sees only the names on each client's latest concentration date.
    The grade stands on the placement read; the served read is a sample.
- **remap-b leg G: MET.** All 4 Cottonwood clients sum to 1 within 1e-5, no `multi_asset` class is served, and the firm_composition gap
  is COT $0.01 and BD $0.00.
- **e60 arm 2: CLOSED** by this seat (ADDENDUM 1 @4cac828d3c), as non-e60 drift. The CVO cites it and did not re-run it.
- **e79 leg G: NOT MET.** This is row D1-S26, confirmed at HEAD. SC-e-79 taught the shared lib to resolve a ticker-no-row position by its
  `NAME::` row. However, BD's three served classify sites call `classify_with_identity` only when the ticker is blank:
  - `D_04.client_portal_summary.py:160-167`;
  - `C_06.client_mix_timeseries.py:228-233`;
  - `D_03.composition_artifacts.py:135-140`.

  The branch never runs on the served path, so the 23 ticker-no-row securities ($966,285) still serve as Unclassified. BD firm
  Unclassified reads $972,621.40 at data_as_of 2026-10-08. The cell's AC1 graded the function, not its caller, and that is the defect
  in the cut.

**FWD state.** No FWD grades REALIZED on this round, which was reads only:
- FWD-1 (the Black Diamond live thread) stays NOT REALIZED. The served BD mix still holds 23 securities that the shared list can place.
- The COT half of the thread now reads clean on e84 and remap-b.
- FWD-2 to FWD-17 carry their round-18 state unchanged. Nothing in round 19 moved them.

## 2. Rows

- **D1-S26 (OPEN, owner this seat):** placed as round-20 item 1, below.
- **D1-S27 (OPEN, owner this seat): placed as round-20 item 2, a read with no build.** C_06's firm-daily `total` differs from its class
  sum by -4.71, +128.06 and -128.57 on 2026-10-06, 07 and 08, about 6e-8 of $2.0B. D_04's `Unclassified` line is the total minus the
  six classes by design, so it carries that gap.
  - The trace is cheap. It decides whether a ~$128 position counts in the total on one day and in a class on the next.
  - It must land before item 1's leg G is read, because item 1's expected outcome is stated net of this gap.
- **D1-S25 (OPEN, owner this seat): placed as round-20 item 3.** It adds three limbs to D1-S23, which is still OPEN. The CRO's fix
  @ecedce453e (`.tools/crossbox-deploy-check.py`) keyed only the OPEN-CALL limb on the deploy's own files. Three limbs remain:
  - (a) a crossbox call arms every root whose token its body document quotes;
  - (b) the deploy's own open ledger entry counts as contention against itself;
  - (c) one slug is counted once per status it has held.

## 3. ENRICHMENT LIST (round 20, ONE issuance by `2.0.0_SA_COO~M1`; cell ids are candidates, the issuer mints them)

1. **SC-e-87, the BD served-path reach (D1-S26).** Build, risk class SERVED.
   - The three sites above route a non-blank ticker that `classify()` misses to
     `classify_with_identity(ticker, name, cusip)`. Nothing else changes: a blank ticker keeps today's path.
   - Mechanical criteria, one per site, each driving the site's own served classify function (never the lib function) with a
     ticker-no-row position that has a `NAME::` row, and reading the class it returns:
     1. D_04;
     2. C_06;
     3. D_03.

     The BD gold suite staying green is drain hygiene, not a criterion.
   - **Ship:** it rides its own never-widen pair. The halves name the expected outcome read from the producer's own rule, on both
     branches:
     - a ticker-no-row security WITH a `NAME::` row moves from Unclassified to that row's class;
     - one WITHOUT a `NAME::` row stays Unclassified, listed by name.

     The writers of the served `mix_summary.json` are counted and printed. Rollback is the prior lib object version.
   - **Leg G (the close read):** a scheduled BD fire after the ship serves the 23 by their `NAME::` rows. Firm Unclassified falls by
     about $966K, to the residual that D1-S27's trace explains. Any of the 23 still unclassified is listed by name with the reason.
2. **SC-e-88, the C_06 total-vs-class-sum trace (D1-S27).** A read, risk class LOCAL, with no write to any served key.
   - It reads the three firm-daily snapshots of 2026-10-06 to 08 position by position and names the position(s) whose membership
     differs between the total and the classes.
   - Close when it names that cause. A defect it names becomes a round-21 build item; it is not fixed inside this cell.
3. **SC-e-89, the seat-gates limbs (D1-S23 + D1-S25).** Build, risk class LOCAL.
   - The write surface is the seat-gates code that `safe-deploy` consults. Before the cut, the issuer reads that code's lane and
     confirms a worker may write it.
   - Mechanical criteria:
     1. a one-key ship on `data/black_diamond` reads 0 unrelated hits;
     2. a ship whose own ledger entry is open reads 0 hits for that entry;
     3. a slug that has held two statuses counts once.

Carried, not cut here:
- e57e61 (FWD-10 apply, `~S`) stays HELD on its own trigger: the first scheduled new-security run that plans US stocks.
- The p1 residue (11 keys outside FWD-15's plan) waits on its ruling, which is not part of this slug.
- IB-pr-417's e56 member is at dell2, Monday 2026-10-12 13:00Z.

When item 1's leg G reads MET and item 2 has named its cause, FWD-1's Black Diamond half is read again for REALIZED.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None new in this round. FWD-5's deletion confirmation stays his act. Per the PRD's FWD-5, it is asked for the moment the FWD-4 check
reads zero users of the old copy, and that has not happened.

-- 1.0.0_SA_CTO~DELL1
