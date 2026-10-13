# NFRA_OPLGTW -- ROUND-36 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-13 ~20:3xZ.
**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33733, `remediations/REMEDIATION_v19.md` @0ee8fa74cf. L8:
`adjudications/ADJUDICATION_v27.Z.md`.
**Issuer:** `2.0.0_SA_COO~O`.
**Direction:** cross-box ORDER XB-20261013T185926Z-4d72, outcomes Z3 and Z5. Andrew named this project one of "the three
that matter". Its next round serves the MC Portal panel instead of upkeep.

**Standing:** the project stays OPEN until Andrew has read NFRA_MCPORTAL FWD-20 (Andrew-direct 2026-10-12 ~20:5xZ,
item 2).

## 1. Round 36, as read

MAY-CLOSE, 4 of 4 complete, nothing deployed. 4 rows dismissed.
- **Z-S101 graduates:** r30 + bd-2 + sh-1 are built but not served. Ruled YES as one release @8f236865cc.
- **Z-S95 is partly met:** the 502s are localised to the ALB/target connection, with the cause inferred, and still
  recur (2 of 1440 polls).
- **Z-S100 and Z-S91 are built, not met:** they wait on the per-family releases.

## 2. Rulings

| item | ruling | cell |
|---|---|---|
| **Z-S101, the r30 release** | One gateway release on the live ref, after MP-z-5's ledger closes. It carries OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1, a pair naming all four, and every other unreleased `app/` diff listed as excluded. The grant writes are a separate act. The CVO's cut-template rule is adopted: a deferred-release build cell names the release order it rides. | **R1** |
| **Z-S91 / Z-S100, the per-family drains (OG-fd-2)** | They ship on their own per-family releases. They are not added to R1, because R1's scope is the four cells above. The pair for those releases must disclose that OG-fd-2 also moves schwab's drain ahead of the lanes (CVO note, REMEDIATION_v19). | **R2** |
| **Z-S95, the Teams 502** | No cell this round. The row stays open in this channel. Per the direction, it goes to the laptop as an FYI only if it blocks COMM_ASSIST, which now owns the Teams consumer. The host-journal read comes first if it does. | -- |
| **FWD-20 (v2.6), cadence and depth** | One read lists, per served family: the live schedule, the last sweep, and the history depth from `backfill-status` and the served earliest date, each with its claim. NFRA_MCPORTAL displays it. Read only. Its code rides a release behind R1. | **R3** |
| **FWD-21 (v2.6), harvest for Opal asset managers** | Name the asset-manager principals from the grant store, with the denominator printed. Grant Opal principals read on all 24 prefixes of list v4 @7e0da2dfee (Andrew call 8) through the existing grant writer; non-Opal principals are refused on every prefix. Proof: one real asset manager's driven call returns a pack and chatter; a non-Opal principal is refused on `packs/` and `wsj/harvest/`. An asset manager without a work Claude account goes on the site Z open-calls list as Andrew's act. NFRA_MCPINDEX catalogs the prefixes (its rows Z-S105 and round 11). | **R4** |
| **GRADE FWD-1..8** (direction Z3) | One READ cell. For each of FWD-1 to FWD-8, run that outcome's PROOF as the PRD writes it (`prd/NFRA_OPLGTW_PRD.md` :55-133) against live state, and record the evidence with its claim. Where a proof needs Andrew's or a named user's act, record which act and that it is owed. This seat grades each outcome REALIZED / NOT_REALIZED at the round-37 analysis, from that record. | **R5** |
| **dell2 convenience cells** | None taken this round unless dell2 is blocked this week (direction Z3). | -- |

## 3. ROUND 37 -- cut in ONE issuance

**Cells:**
- **R1:** the r30 release.
- **R2:** the per-family drain releases.
- **R3:** the FWD-20 read.
- **R4:** the FWD-21 principals and grant.
- **R5:** the FWD-1..8 grade read.

**Prerequisites and sequencing:**
- PRD v2.6 must read ADMITTED before R3 and R4 are cut (LIMB 6).
- Gateway releases go one at a time: MP-z-5, then R1, then whichever of R2/R3 the decomposition orders.
- R5 is read only and runs in parallel.
- Every WORLD cell carries its never-widen pair.

-- 1.0.0_SA_CTO~Z
