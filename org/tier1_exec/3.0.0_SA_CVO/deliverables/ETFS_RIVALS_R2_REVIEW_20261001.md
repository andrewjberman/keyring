# ETFS_RIVALS round 2 -- CVO review and L10 slug basis

**Seat:** 3.0.0_SA_CVO~RV (Andrew's pairing with 2.0.0_SA_COO~RV). 2026-10-01 ~05:5xZ.
**Packet:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round2/DRAIN_END_READ_ROUND2.md` @d152231e55 (msg
27541, acked). 9 of 9 orders terminal; ledger `etfs-rivalfunds-round2` CLOSED.
**Carriers:** `surprise-channel/adjudications/ADJUDICATION_v2.Z.md` (4 rows, 29 items) and
`surprise-channel/remediations/REMEDIATION_v2.Z.md` (8 items, W2-S4 ARMED). Round 1's eight graduations
(`REMEDIATION_v1.Z.md` @7d90d0bfd8) stay OPEN beside them: **16 OPEN remediation items in all**, every one owned by
1.0.0_SA_CTO~Z.

## Denominator

The channel holds 66 rows. Round 1 compiled 29 (watermark 2026-09-30T15:35Z). Round 2 covers the 37 surfaced after
that, through Z-S3 at 05:09Z. The reconciliation script reads 29 dismissed + 8 graduated = 37, 0 missing, 0 extra.

## Measured by this seat (not taken from the packet)

| claim | read | result |
|---|---|---|
| W5-S24 disarmed | silver_bloomberg.py at HEAD; state/build_bloomberg_silver/ | no delete call (the one match is the :13 docstring); markers import-r2-07 04:16Z and -08 04:20Z, after the 04:10Z apply |
| residue of W5-S24 | marker census per stage | import-r2-04/-05 have no silver marker under date=2026-09-30 but do have gold and page markers; run_dag walks only its own day, so this stays a permanent gap in the marker record, not a re-run hazard |
| W5-S26 / W5-S19 | pytest | the named test: 1 passed; the package: 189 passed, 2 skipped, 0 failed |
| W3-S13 | sweep.py | enrichment_gate :232, applied to GATED stages in run_dag :324-328 |
| W2-S4 exposure | issuer silver key census | 325 objects, 325 dates, 325 old-format, 0 new-format: still ARMED |
| W3-S8 | git show ef6e9eb88d | all 13 raw types ruled before g-4 spawned, so this is dismissed, not graduated (my first draft graduated it; the amendment corrected me) |

## Recommendations by driver

**For CTO (1.0.0_SA_CTO~Z), the round-2 analysis**
- **P0 -- W2-S4 first.** It is the one live-correctness hazard: any re-capture of a landed BASG date silently keeps the
  old rows. The remedy is a one-line `_capture_id` change to a live Lambda (WORLD), so it needs a pair. Cut it as round
  3's first cell, with a re-capture of one landed date as the positive control.
- **P1 -- decide what a signed-out morning means.** W5-S23 (accepted Branch B): with no pull-enrichment marker, the
  W3-S13 gate builds no new G5 for ANY fund, BASG included. Round 1 built BASG daily without the Terminal; round 2 made
  every fund's daily trade schedule depend on the 08:03 leg's sign-in. The last Terminal health read was ok=false
  (2026-09-30 20:08 ET, packet :38). If that is the intended trade, say so in the PRD. If not, gate only the funds whose
  window touches a corporate action.
- **P1 -- W1-S8 (home-producer reader) and W5-S28 (freshness threshold 0).** Together they are why the served page
  reads `not-updated` with 6 of 13 funds. Neither is a defect, but FWD-1 for Andrew is "his fund beside its rivals", and
  today both home funds read ABSENT.
- **P1 -- round 1's S1, W1-S4, W1-S5 are still open.** S1 (GICS vs sub_asset_class) must be ruled before G4 lands.
- **P2 -- W1-S11, W3-S11, W3-S12, W5-S21.** The revision tie, dividend currency (DVD_CRNCY), child-line identity (your
  issuer's own ruling says a new line from an entitlement is not a trade, and the build cannot honour it), and the
  quadratic dedup before any backfill.
- **P2 -- S2, fabric.** Gateway deploy lease and route preservation; see the round-1 review's last section.

**For COO (2.0.0_SA_COO~RV)**
- **P2 -- W2-S4's disarm stays yours.** It is ARMED with you as disarm owner until the round-3 cell ships it. Until
  then, a manual re-fetch of a landed BASG date is the act that triggers it: don't run one.

## Deferrals and close-reads still owed (not graded here)

- FWD-1's acceptance needs two acts no seat can do on demand: the signed-in /rivalfunds read (a human; round 1's W5-S13)
  and the first live 08:03 leg after Terminal sign-in (packet :37-39, ABSENT until read). L10 cannot grade FWD-1
  REALIZED without both.
- GQGU is absent from the page input and no row explains it (packet :33, :73). This is unmeasured, not dismissed.
- W3-S10's later-window branch and W1-S14's periodic rule are proven on synthetic data only.

## What you should have asked but did not

Whether round 2 made the product more fragile than round 1. Round 1's thread needed AWS and the issuer's website.
Round 2's daily page needs those plus a signed-in Bloomberg Terminal on one machine for every fund's trades (W5-S23),
and it publishes `not-updated` whenever a Bloomberg-fallback fund lags one trading day (W5-S28). Every check passed,
and the served page tonight says not-updated. Measured against "Andrew does nothing by hand on an ordinary day" (PRD
`ETFS_RIVALS_PRD.md:68`), the thread's ordinary day now includes a manual Terminal sign-in. That is an endpoint question, not
a defect, so it is the CTO's to put to Andrew, not this seat's to grade.


## Addendum (2026-10-01 ~06:0xZ): W5-S12 disarm record

`1.0.0_SA_CTO~Z`'s round-2 analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round2.md` @01114ae8a8,
ruling 9, IS the disarm record for `ETFS_RIVALS-Z-W5-S12`. The hazard ended at the thread-r1 ledger close, 2026-09-30
15:33:58Z. The mechanism stays OPEN in `REMEDIATION_v1.Z.md`. `comp-surprise` keeps listing the item ARMED because its
round-1 graduation row carries no `disarm` block and the gate refuses adding one in place. Read that listing against
this addendum. The round-3 compile (ADJUDICATION_v3.Z) cites ruling 9 again.

-- 3.0.0_SA_CVO
