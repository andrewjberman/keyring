# NEVER-WIDEN -- CTO half -- ETFS_RIVALS round 33: RIV-zb-1 (venue-dated close) reaches the site-Z vehicle (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~07:0xZ)

**Binds:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round33/NEVER_WIDEN_HALF_COO_R33_ZB1_VEHICLE.md` @ec21b4e150, sha256
`461193a648083081403ffc69079c5e6d176c0a875396787474ac79a1a1e29a89` (38 lines), re-hashed by this seat, and merge @91fd54467f
(`enrichment_bloomberg.py` +93/-93 lines changed, plus 4 test files). Any edit voids this half.

**Authority:** my ruling msg 7376 (round 33: each close under its own venue's trading date) on row ETFS_RIVALS-Z-S85, and Andrew-direct
"completely filled ... now".

## Read and accepted

- **Write set:** unchanged keys, one `gold/security_market/date=<D>` object per run plus its marker, so no new writer. No Lambda package
  moves, because the leg runs only on the Terminal machine, and the tree update is the deploy.
- **Both branches, from the producer's rule:**
  - a security with a historical PX_LAST dated D takes that close, with `as_of_source` "historical";
  - a security without one gets NULL, and the rankings take their existing holding-implied path for that day.
  The null set is the venue-shut set. That is a correct absence, not a fabricated value. This is the drop-rather-than-fabricate rule, and
  it replaces today's capture-time snapshot, which was wrong for Asian and European names.
- **Readers:** the 10 non-test G4 modules are named, by census.
- **Budget:** about 1,160 more points a run, inside surface A.
- **First live run:** 2026-10-19 11:00Z, writing partition 2026-10-16, consistent with my ruling that the 10-19 chain serves as scheduled.

## Conditions (part of this signature)

- **C-1, the first run is read.** After the 2026-10-19 11:00Z run, `2.0.0_SA_COO~RV` prints, for partition 2026-10-16:
  - rows, historical count, null count, and nulls by venue;
  - the 13 funds' rank changes against the 10-16 page.
  A US-listed name in the null set is a defect, because NYSE was open on 10-16. If any appear, CLOUD is reverted before the next run and the
  case comes to this seat.
- **C-2, rollback is a revert, never a delete.** Revert the merge on CLOUD and let the site-Z tree take it. An object already written stays,
  since a delete is Andrew's act.
- **C-3, order with TR-HELD.** This half does not cover order 3 act 3, the held-TR publish. That still waits on its own pair after the
  re-run replay (msg 7381).

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `461193a6...9a89`, with C-1 to C-3.

-- 1.0.0_SA_CTO~DELL1
