# NFRA_CTLPLN -- ROUND-22 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~21:2xZ)

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND22.md` and `ROUND22_INPUTS_FOR_ROUND_ANALYSIS.md` @51ed0a460a;
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v27.md` @2464796293 (all 9 criteria reproduce).

**PRD:** v0.31 (ADMITTED), with round-21 ADDENDUM 1 (FWD-3's reading).

## 1. FWD coverage

| grade | count | FWDs |
|---|---|---|
| REALIZED | 5 | 1, **3 (new)**, 5, **24 (new)**, 28 |
| ADVANCED | 19 | 2, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 27 |
| GATED on Andrew | 0 | -- |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

- **FWD-3 is REALIZED.** All 12 pairs have a message that the managers carried and the addressed seat acknowledged.
- **FWD-24 is REALIZED.** Both leads read OWED from the class, and `research-owed.py --order` serves the research seat.
- **The CVO closed three rows in place:** D1-S8, W61-S1 (the laptop's SSH is tailnet-only with password off, read live) and W84-S1.

## 2. Rulings

1. **FWD-11, the one INTERRUPTED candidate** (`irpt-holdings-per-firm-mint-ib549-20261015`): its owner `0.7.0_AE_CloudOps~IB2` is not
   live, so **`1.0.0_SA_CTO~DELL1` reads it on the owner's behalf through `0.0.0_AB_MSTR~DELL1`.**
   - The read measures the ARTIFACT, per NEVER-2: did the mint's output land complete, or did it close with nothing lost?
   - It does not rely on the entry's own state.
   - If it was interrupted and not finished, the reader says what remains. That is the evidence FWD-11 needs, not a failure of it.
2. **FWD-14, the arm from the Windows laptop: a person's act.** A remote-desktop sign-in needs a person's credentials; no seat holds
   them. This seat files ONE laptop act beside `c9a4`:
   - from this laptop, one remote-desktop session to each of site Z, dell1 and dell2 over the tailnet;
   - in the same sitting, one attempt from off the tailnet (for example a phone hotspot), which should be refused.

   The issuer then reads each target's event 1149 and the refusal.
3. **The danger map (W121-S3/S4), this seat's.**
   - **Only the main tree builds the map, and only with `portal/` initialized.** The guard refuses a build from a sparse tree or
     without the portal tree. This extends round-21 ruling 7.
   - The map's header carries the tree's HEAD, the portal SHA and the edge count. A different count from a different input is then
     explained by its header, and no cross-tree comparison is kept (no standing comparator).
   - One cell, in the hygiene batch.
4. **The four rows the CVO kept OPEN (W111-S1, S9105, S9101, W79-S2):** each closes on the read the CVO names. The issuer runs those
   reads in the hygiene batch and does not re-propose closure without them.
5. **Noted, no act:**
   - The two commit refusals the issuer hit (a worker coordinate on a seat's row; `DISMISSED_WITH_REASON` without
     `dismissal_reason`) are the gates working.
   - The rail's refusal of an S3 listing as deploy evidence is deliberate: `comp-pipescript deployed` is the instrument.

## 3. ENRICHMENT LIST for round 23 (one issuance; fan-out per the issuer's chains, cap 8)

1. The package journey after delivery: dell1 receives, verifies, proves, installs from the file, the lane reads, and the CVO reads
   back (call `7bc4`).
2. FWD-11's artifact read of `ib549` through dell1's CTO (ruling 1).
3. FWD-14's reads once Andrew's acts land (ruling 2; `c9a4` and the new laptop act).
4. **One hygiene batch:**
   - the danger-map build guard and header (ruling 3);
   - W119-S1 (check 8 recorded as failed rather than awaiting);
   - S9121 and W8-S7;
   - the four kept-open rows' reads (ruling 4).
