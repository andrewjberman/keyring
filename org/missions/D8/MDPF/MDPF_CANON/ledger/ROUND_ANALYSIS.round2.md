# MDPF_CANON -- ROUND 2, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~02:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3349 @0477bdd2dc; `surprise-channel/adjudications/ADJUDICATION_v2.md`;
`surprise-channel/remediations/REMEDIATION_v2.md` (D1-S9, C-S12, S8). Issuer packets:
`deliverables/2.0.0_SA_COO~D1/round2/ROUND2_CLOSE.md` and `DAILY_READ_20261010T1330Z.md` (row D1-S9 @69507b5493).
PRD v2.10 @fa51c1f544.

## 1. Graded

- **CN-b-1, the reader census (M1): MET.** 51 rows, and every reader the CVO's own unscoped read finds is cited or excluded
  with a reason. The portal limb is closed by row S8.
- **CN-b-3, the publisher runtime (M5 prerequisite): MET.** python3.11 with the pyarrow layer; 36,272 of 36,272 served values
  equal on the organic 2026-10-10 13:50Z run. FWD-4 is not graded by this: the publisher still reads the legacy trees, and
  its switch to `opal-data-mdpf` comes last in the arc.
- **CN-b-4, the composite grant on builder output (W1-S1): MET.** The live policy equals the render from
  `scope_bucket["mdpf"]`.
- **CN-b-2, the combined slice's basis (M7): NOT MET.** The basis asserts a minimum of 2 firms. The producer's own global
  output on 2026-10-08 carries 12 by_model entries held at one firm (6 of them at 3 or fewer accounts, each value equal to
  that firm's) and two series that are one firm's alone (`non_model_aua`, `inflection_non_model_aua`). The written reason
  does not match what is emitted.
- **CN-a-2, the one parquet writer: still NOT MET (ungraded).** See section 2.

**FWDs:**

| FWD | Verdict | Why |
|---|---|---|
| FWD-1 | PARTIAL | The thread works on the backfilled tree. The first scheduled daily write (2026-10-10 13:30Z) built 12 of 16; no scheduled fire has yet been read 16 of 16 at `address()` with the as-of at the T-1 frontier. |
| FWD-2 | not started | M9 waits on `ADVI_FIRMBKTS` per firm. |
| FWD-3 | NOT REALIZED | The reason is written but is not true of the output (CN-b-2). Section 3 holds the call. |
| FWD-4 | not started | M5's switch is last. The runtime prerequisite is met. |
| FWD-5 | not started | M1 is done; M4 and M6 have not run. |
| FWD-6 | not started | M10 waits on `ADVI_FIRMBKTS` and `LGIC_ENFORCE` E5. |
| FWD-7 | not started | M8 waits on `LGIC_ENFORCE` E3. |
| FWD-8 | not started | M11, M17. The instrument for `opal-data-assets` is still an open call (PRD DEC-9). |

## 2. Ruled here

### D1-S9 -- the 2026-10-10 fire built 12 of 16. Ruled: the writer is not defective; the input lagged

Read from the producer's source at HEAD (`data/mdpf/scripts/gold/mdpf_gold_consolidator.py`,
`emit_gold_parquet` :2187 and `mdpf_gold_parquet.write_partition` :217), beside the Lambda log the COO and the CVO read:

- A parquet partition's date is the **as-of the document carries** (`derive_as_of`), never the run date. `write_partition`
  is create-only: an existing partition returns `unchanged` (same bytes) or `conflict` (different bytes), with no put.
- The value leg (`aum_daily`) ended 2026-10-08 while the count leg reached 2026-10-09. So for 49financial and
  inflection, the value-bearing types carried as-of 2026-10-08. That date already held a partition from the 2026-10-09 fire,
  so nothing new was written, by design ("one addition per day; no date is rewritten"). The legacy JSON at the same date
  differed (a newer count against an older value), so the JSON guard recorded CONFLICT and overwrote nothing.
- For global, the cross-axis coherence gate refused to emit: 5 models had a count on 2026-10-09 with no value.
- Every one of these is the producer **failing closed on a lagged input**. No wrong figure was written or served. Platinum
  for global and 49financial served as of 2026-10-08, one trading day behind the T-1 frontier (Friday 2026-10-09).

**The mechanism that remains unread is the value leg's clock.** On the 2026-10-09 fire both legs agreed. On Saturday
2026-10-10 the count leg carried Friday and the value leg did not. Whether the value feed delivers Friday's data only on
the next trading day (a weekend clock mismatch that recurs every Saturday fire) or missed once is not measured. The next
trading-day fire is Monday 2026-10-12 13:30Z. The scheduled fire is the producer's own clock, the organic arm; an ad-hoc
gold run is QA only and never production evidence (CLAUDE.md section 5).

**The issuer's instrument needs one change.** `r2_daily.py` arm 1 (WRITTEN) counts partitions written at or after the fire.
A fire whose data as-of did not advance writes no new partition by design, so arm 1 fails on a correct producer. The arm
should grade, per scope and type: the partition at the scope's own data as-of exists at `address()` (written or unchanged),
and that as-of equals the T-1 frontier from `lib/trading_calendar.py`. The issuer amends its own instrument (rule 27 L6).

### W1-S1 -- closed for this project

The round-1 ruling asked for a registry row. CN-b-4 found the builder already carries `scope_bucket["mdpf"]`, and the grant
now reads it. The residue is that `scope_bucket["global"]` still gives the platinum bucket `opal-data-portal-v2`, so a future
consumer keying the gold composite by `"global"` would get the wrong bucket. That is a property of the builder map
(`LGIC_ENFORCE` / `LGIC_NAMING`), not of MDPF_CANON, and is not cut here.

### S8 -- carried

The stale served key's dead portal readers are removed at the key's retirement (M12). Not a round-3 cell.

## 3. ENRICHMENT LIST (round 3, ONE issuance by `2.0.0_SA_COO~D1`)

1. **D1-S9: read the value leg's clock, then the Monday fire** (issuer acts, not cells).
   - Before 2026-10-12 13:30Z: name the `aum_daily` producer and its delivery schedule, and read whether its 2026-10-09
     rows have landed. State whether the value leg structurally lands a day behind the count leg on a weekend fire.
   - After the 2026-10-12 13:30Z fire: run the amended `r2_daily.py` (section 2). CN-a-2 AC3 and FWD-1 grade on it.
   - If that fire also refuses with both legs at the T-1 frontier at input time, the defect is in the producer, not the
     input, and a cell is cut at the next analysis. If the value leg is structurally late on weekend fires, file it as a
     row against the value feed's owner. The gate's refusal is correct and is not loosened.
2. **CN-b-2 recut: M7, the basis made true** (one cell, at most 3 mechanical criteria):
   - AC1: `X2_GLOBAL_BASIS.md` states the minimum firm count per field family (headline sums; by_model; the two
     single-firm series), each read from the producer's global output at a named as-of with the denominator printed;
   - AC2: it lists every global entry that is one firm's value, with that entry's account count;
   - AC3: the ledger X2 row still cites it, and a seat that did not write it reads the counts back equal.
   This makes the reason true. Whether FWD-3 can be REALIZED on it is the call in section 4.
3. **M4, the repoints and seams, first slice.** Cut from `READER_CENSUS.md`: one producer reader at a time, each seam
   read on `/seams` (MECHANICAL, DECLARATIVE, SEMANTIC) against the deployed artifact. The issuer picks the first reader
   and the fan-out from the census's dependency order.
4. **M8, the bronze move,** only if `LGIC_ENFORCE` E3 reads applied at the cut. The issuer reads it; if it is not applied,
   M8 stays parked on E3.

Unchanged from round 1: M3's full-history clause, M6 (HELD on `LGIC_NAMING-S7`), M11-M17 follow the arc; M9 and M10 wait on
`ADVI_FIRMBKTS` (round 1 FWD-1 PARTIAL, round 2 pending issuance by `2.0.0_SA_COO~F1`).

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **FWD-3: may the combined all-firms figure carry single-firm, small-count entries?** (row C-S12)
   - The producer's global output carries 12 by_model entries held at one firm. 6 are at 3 or fewer accounts, so one entry
     is one or two accounts' holding value under a model name. It also carries two series that are one firm's alone.
     No account identifier is present.
   - FWD-3's ACCEPT requires a written reason why the figure "reveals nothing about any single firm's clients". A true
     basis (item 2) cannot say that while these entries are emitted.
   - **Option A (recommended): suppress in the global fold.** A by_model entry held at fewer than 2 firms is folded into
     one "other models" line, and the two single-firm series are left out of global (each firm keeps them in its own
     scope). The headline sums are unchanged. This moves served output, so it is a cell under never-widen sign-off
     (CTO and COO), with the before-and-after of every global leaf read.
   - **Option B: accept the disclosure.** Rewrite FWD-3's ACCEPT to state what single-firm entries reveal. That is an
     ENDPOINT change, so `3.0.0_SA_CVO` re-signs the ratified-text half.
   - Until he answers, FWD-3 stays NOT REALIZED and the basis cell (item 2) proceeds: it is needed under either option.

-- 1.0.0_SA_CTO~DELL1
