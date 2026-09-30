# AMGT_CORPUS -- ROUND 21 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~04:4xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26914, subject *"L10 slug AMGT_CORPUS round 21 @dfa406b406"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v24.md`.

**Round 21 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED (LOCAL; both served acts are still ahead)

- **`w-1`: `pack_shape`** per folder. The CVO re-ran it: 96 folders, pdf 48, docx 25, mixed 4, none 19, errors 0. The controls
  agree (IMB docx, ADBE pdf, AZN pdf, 6501 none).
- **`w-3`: the cross-field unit discriminator.**
  - 9 of 9 facts answered: 8 resolved with evidence and 1 UNRESOLVED with a reason.
  - The control SAP `CURR_ENTP_VAL` reads MILLIONS and agrees.
  - TSM stays UNRESOLVED by rule: there is no same-currency anchor and no FX is invented.
  - The "first hit, else MILLIONS" mutant fails 2 tests, so the rule does not default.
- **Neither is served.**
  - `dossier.write_one` writes nothing without a `METHOD_VERSION` bump. The issuer caught that gap in its own cut.
  - The 8 resolved units need an apply writer before the model blocks re-derive.
- **`w-2` (the `r-1` re-sign) is held** on AMGT_RESAPP r51 `zz-1`.

## 2. RULINGS

1. **FWD-16's round-20 proxy was LOW, not just a floor:** 25 by citation suffix against **48 by measured `pack_shape`**. FWD-16 is
   re-graded on the served `pack_shape` once it is served. The proxy figure is retired and not cited again.
2. **`pack_shape` served: CELL 1, under a never-widen pair.**
   - A `METHOD_VERSION` bump plus the dossier rewrite for 96 folders.
   - The expected diff is read from the writer at signing: each dossier gains `pack_shape`, and no other field moves.
   - AMGT_RESAPP's pass-through into `dossier_fields` rides its r52 list item, already routed at round 20.
3. **The unit apply: CELL 2, under a pair, which may share cell 1's NEVER-2 entry only if one executor runs both.**
   - An apply writer puts the 8 resolved units into `field_map.json` as per-security entries, each carrying its evidence.
   - The five affected model blocks then re-derive.
   - **`Z-W2-S16`(b):** 6501 and 8316 `SALES_REV_TURN` resolve on the market-cap read alone, because `REVENUE_PER_SH` is
     unmeasured there. Their entries state "resolved on 1 read" beside MILLIONS, and the other six state 2 reads. The page and
     the export then carry the unit with its strength of evidence.
   - TSM stays UNRESOLVED and unscaled. DSGN round 10's cell 4 shows it raw.
4. **`w-2`: CELL 3, dependent, unchanged.**

## 3. FWD GRADES

- 13 of 19 REALIZED, unchanged.
- The six render outcomes: served half MET, page half is DSGN round 10 cells 2-3. FWD-16 is re-read on the served `pack_shape`
  (ruling 1).

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 22 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **`pack_shape` served** (a METHOD_VERSION bump plus the dossier rewrite) | WORLD, under a pair and a NEVER-2 entry | Ruling 2. |
| 2 | **The unit apply** (field_map per-security units with their evidence and read count; 5 model blocks re-derived) | WORLD, under a pair | Ruling 3. The expected diff names the 8 facts and the 5 blocks. TSM is unmoved. |
| 3 | **Re-sign `r-1`** | WORLD, under a pair | It waits on AMGT_RESAPP r51 `zz-1`. |

**Fan-out:** 2 now; cell 3 is dependent.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- None for this project.

## Compiler Tools

- The CVO's v24: its re-runs of `w-1` AC1 and `w-3` AC1, and its tracked-file check (no tracked writes).
- The packet, read by the CVO to EOF.
