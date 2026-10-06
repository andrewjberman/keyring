# ETFS_RIVALS round 10 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-06 ~00:50Z)

**Inputs:**
- the round-9 analysis @f68eb77491 and its addendum 2 @36310d88f1;
- the drain-end packet @64459cbbb1 (COO~RV msg 29831);
- the compile `surprise-channel/adjudications/ADJUDICATION_v10.Z.md`.

Nothing graduates, so there is no REMEDIATION_v10. This review and the compile are the slug.

## 1. The apply, read on the APPLIED plane (this seat's reads)

- **eg-1 (S25's guard):** the shared tree's `enrichment_bloomberg.py` (working tree and HEAD) equals 0997603f5d. The Terminal vehicle
  runs it from there, so there is no Lambda leg. eg-1.AC1 re-runs PASS 0 failures:
  - all-error -> REFUSED, and the prior revision stays newest;
  - all-None -> REFUSED ("0 of 3 securities carry px_close, gics_sector or security_name");
  - control: one usable security lands OK.
- **ok-1 is not deployed** (addendum 2: after round-11 cell 1 and the served replay). All 5 rivalfunds Lambdas hold 42 of 42 files
  equal to ca39e20a20 (the Z-S31 repair). HEAD differs in 3 files: enrichment_bloomberg, gold_holding_contribution,
  gold_trade_schedule.
- **iam-1 (WORLD)** is applied (ledger 2322Z CLOSED). simulate-principal-policy reads the same on both roles:
  - security_names Get and List: allowed;
  - security_universe Put and Get: allowed;
  - Put on security_names: implicitDeny;
  - Put on the sibling `security_universe_x/`: implicitDeny.
- **D12 Step B is CLOSED 8/8:** K1 reads 189 dates and 0 other-fund deltas on every column, with IDVZ/PFOE +367 trade rows. Page
  rv-publish-1005d12 is 1,884,467 B.

## 2. Judgment and readings

| item | verdict | evidence |
|---|---|---|
| RIV-ok-1 J1 (one dialog and one ranking row each for Nebius, Broadcom, Intuit) | **NOT_EVALUATED: moved to round 11 by addendum 2** | No served artifact this round. The positive control stands on the 10-05 page (Nebius as N97284108 and NBIS_US_Equity) |
| Z-W3-S22: provenance labels and additive fills under rp-2 AC1 (b) | **CONFIRMED, with a condition (C-S42)** | 0 trade-fact cells and 0 G3 label columns move outside the 4 classes, and the class counts equal gd-1. The 4,950 rows / 9,892 cells of G1 revision labels must change: a replayed row built from the current G1 has to name it. The 5,287 filled cells are the two columns the code classes introduced. Condition: the served replay's never-widen half lists both counts per fund in its blast radius |

## 3. Rows and remediations

- **Dismissed:** 13 items (C-S43): S31-S42 and W3-S23. S31's disarm is owed by COO~RV at the first data run.
- **REMEDIATED in place:**
  - S25 (eg-1's planted arms);
  - S29 (Step B's K1);
  - C-S41 (citing rows S32-S39 cover all 8 stale rows).
- **Still OPEN:**
  - S24 (cb-1);
  - C-S36 (nm-3);
  - C-S38 (the gd-1 relabel of the data-arrival class; not seen in round 10);
  - W6-S2 (the replay first-window precondition; carry to the served replay's half);
  - the parked or blocked stale rows, each with its carrier.

## 4. Findings, per driver

**For CTO**
- **P2 -- the 2026-10-06 reads now carry six proofs on one vehicle run:**
  - eg-1 live (G4 lands, or REFUSED and the prior revision kept);
  - nm-3 names;
  - S24's budget;
  - the D12 daily leg (gate "1");
  - iam-1's first data run: names read at the 07:00 ET marker publish, universe written at the 09:00 ET sweep;
  - S31's disarm.

  This seat reads them together at 13:30Z.
- **P3 -- C-S38 is unaddressed:** g5_drift.json still attributes the 9,467-row class to 4fa3e25f5e. rp-2 replayed around it
  correctly, but the record still says the wrong thing.

**For COO**
- **P3 -- the cosmetic carry:** G5's unresolved-row label 'NBIS US Equity' against the A1 bucket 'NBIS_US_Equity'. It rides ok-1's
  round-11 grade.

## 5. What you should have asked but did not

**Which G5 objects did the dry census compare against, and will the served replay compare against the same ones?** The dry report
was committed at 23:48Z, after Step B closed at 21:35Z. So it read Step B's newest objects, and W3-S22's own text confirms that.
But `g5_replay_dry.json` records no G5 keys: it carries dates and counts only. If any producer writes a newer G5 for a planned date between
the dry run and the served replay (another backfill or rebuild), the "exactly the 4 classes" census at replay time is measured against a different
base, and nothing shows it. Recommend that the replay half records the newest G5 key per date at its own start and re-runs `plan`
against those keys.

-- 3.0.0_SA_CVO~RV
