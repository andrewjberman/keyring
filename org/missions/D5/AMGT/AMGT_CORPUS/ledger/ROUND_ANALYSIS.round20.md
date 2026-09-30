# AMGT_CORPUS -- ROUND 20 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~03:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26885, subject *"L10 slug AMGT_CORPUS round 20 @d581644aff"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v23.md`. Issuer packet: `ROUND20_DRAIN_END_PACKET.md` @`0f953c0312`.

**Round 20 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`v-1`:** the 3.9 floor. Ten `Path.write_text(newline=)` calls became `open()`. AC1 reads 0 calls over 96 files.
- **`v-2`:** the six render outcomes, measured on both halves.
  - **Served: MET.** IMB's `/thesis` carries `dossier_fields` (pillars, management, fund of record, last stated position).
    AZN's `model.team_cases` serves base, upside and downside.
  - **Page: 0 consumers.** The CVO read `git -C portal grep -l dossier_fields 29c8226a -- src` = 0 files, with the control
    `team_cases` = 3.
  - The page draws only the team's Base.
- **`v-3` (the `r-1` re-sign) is held.** AMGT_RESAPP round 51 is issued (@77712167dc), with `zz-1`, the `write_pool` union, first.

## 2. RULINGS

1. **The six outcomes (FWD-10, 11, 12, 15, 16, 18): NOT REALIZED, served half MET, page half ABSENT.** Round-19 ruling 2 applies
   as written.
   - **The page ask goes to DSGN_AMGTV1**, which owns the page. DSGN round 9 is issued (@27938c7a99), so this seat carries it into
     DSGN's round-9 analysis as that round's first enrichment cell. It renders:
     - `dossier_fields`: pillars with citation and terms; the management passage beside the roster; fund of record and last
       stated position on the posture line and the Posture tab;
     - the team's Upside and Downside from `model.team_cases`.
   - **The whose-case refinement (CVO v23 section 2) is part of that cell.** Opal's RULE cases are labelled as Opal's
     ("Opal's rule-based upside: the method is to be agreed"). A bare "Upside case: not in the pack yet" never sits beside a
     served team Upside. This extends DSGN `v-4`'s Base fix to Upside and Downside.
2. **`Z-W2-S15` (6501's `/thesis` serves no `dossier_fields` block, so no per-field ABSENT reason): routed to AMGT_RESAPP's next
   list.** A name with nothing to fold still serves the block, each field ABSENT with its reason, so the page can say why.
3. **FWD-16's floor (the worker's 25/25 "PDF-only" is a proxy, because no pack-shape field exists): CELL 1 here.**
   - The dossier records `pack_shape` (pdf / docx / mixed / none) per folder, from the files the fold actually read.
   - AMGT_RESAPP passes it in `dossier_fields`. That rides the same RESAPP list item as ruling 2, one producer ask.
   - Then the tab can "state which shape" as the DONE WHEN requires.
4. **FWD-15's "machine verdict byte-unchanged" clause is unexercised until a team posture renders.** It is graded at the page
   cell's walk and carried, not ruled away.

## 3. FWD GRADES

- 13 of 19 REALIZED, unchanged.
- The six: served MET, page ABSENT, **NOT REALIZED**, with the owner and act named (ruling 1).

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 21 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **`pack_shape` in the dossier** | LOCAL, then a served dossier rewrite under a pair if it moves served bytes | Ruling 3. The census prints the shape distribution over 96 folders. |
| 2 | **Re-sign `r-1`** (`v-3` carried) | WORLD, under a pair and a NEVER-2 entry | It waits on AMGT_RESAPP r51 `zz-1`. |

**Fan-out:** 1 now; cell 2 is dependent.

**Routed, NOT cells:**
- the page render of the six outcomes, to DSGN_AMGTV1 (ruling 1);
- 6501's empty-block reasons and the `pack_shape` pass-through, to AMGT_RESAPP (rulings 2-3).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None for this project. `wk-crps20-1/2` go under his 02:5xZ word to 2.0.0_SA_COO~X (@8c4f79e531), which the issuer applies to its
  own drained worktrees.

## Compiler Tools

- The CVO's v23: its portal grep (0 against the `team_cases` control 3), its `/thesis` reads for IMB and AZN, and its read of
  shot `089-AZN-LN-Model.png`.
- The packet's section 7.
- `git log` for the round-51 and DSGN round-9 issuance hashes.

## ADDENDUM (~03:5xZ, before the round-21 issuance, on 2.0.0_SA_COO~Z msg 26891, row AMGT_RESAPP `Z-S309`) -- CELL 3 ADDED

AMGT_RESAPP round-50 ruling 3 (the export resolves per-security units for 6 names) is RE-HOMED here. The row measured that the
export already prints the model block's per-security unit, and for the six names `field_map.json` itself holds the unit as
UNRESOLVED-ON ("sampled magnitude N does not discriminate absolute vs millions"). The affected facts are:
- `SALES_REV_TURN`: 6501, 8316;
- `CURR_ENTP_VAL`: 6501, 9433, 8035, 8766, TSM;
- `NET_DEBT`: 8316;
- the `BEST_SALES` scalar exception: 6501.

No RESAPP write can move them. The unit map is this project's artifact.

| # | cell | risk | note |
|---|---|---|---|
| 3 | **A unit-map discriminator that does not rest on magnitude alone** | LOCAL, then a unit-map commit and re-derive under a pair if served units move | It uses a cross-field consistency read, for example EV against price times shares from resolved fields, or revenue against resolved per-share figures times shares. The AC prints, per fact per name, the resolved unit with its evidence or UNRESOLVED with the reason, over the 6 names plus a MEASURED control. A name the read cannot decide stays UNRESOLVED and is never guessed. |

**Fan-out:** 2 now (cells 1 and 3); cell 2 is dependent.
