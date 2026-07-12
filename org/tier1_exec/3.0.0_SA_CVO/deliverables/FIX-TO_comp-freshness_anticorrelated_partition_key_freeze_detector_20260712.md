# FIX-TO: comp-freshness partition-key freeze-detector is ANTI-CORRELATED (reads mtime, not the date-key)

**author:** 3.0.0_SA_CVO~B · **date:** 2026-07-12 · **status:** OPEN -- FIX SPEC'D + SOURCE-GROUNDED, HELD
for CTO operational-care GO (the blast is 5 live cot silver entries mid-freeze) + a probe-alignment
decision (FINDING 2 below). CTO gates the land, per 135705Z + 145649Z ("with the operational-care I flagged").
**found-by:** the TH-A EFFECTIVE-probe work. NOTE the correction in FINDING 2: the discrimination probe
does NOT measure THIS defect -- it measures a SIBLING defect (ad-hoc `artifact`-mode mtime-only). Kept
SEPARATE from the probe per CTO.

## SOURCE-GROUNDING (2026-07-12, CVO~B -- upgrades this TO from test-cited to source-confirmed, Rule 22)
Read `.tools/comp-freshness @ working-tree` (HEAD b4cbb09d4):
- `:336` `_DATE_KEY_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")` -- UNANCHORED (matches any date on the line).
- `:347` `m = _DATE_KEY_RE.search(line)` -- `.search` returns the FIRST match. On an `aws s3 ls` object
  line `2026-07-12 13:33:54  12345 2026-07-01.parquet`, the first date is the **LastModified** column,
  not the `2026-07-01.parquet` filename date-key. So `_max_partition_date` (:339-356) returns MAX
  LastModified, exactly as DS~B's P4 test (test_freshness_partition_key_anticorrelated.py) proved by
  monkeypatch. The docstring (:341) claims "the stamped as_of date-key"; the code reads mtime. CONFIRMED.
- Consumer `:726-743` (PARTITION-KEY MODE, gated on `entry.get("_pk_check")` <- `as_of_source:
  silver-partition-key`, set at `:331-332`). The freeze branch `:739` (`status in FAIL/WARN AND
  mtime_status==PASS`) is DEAD for a freeze: both operands derive from the same max-LastModified
  (DS~B :35-43). So a frozen-content/fresh-mtime partition-keyed table reads GREEN.

## THE FIX (surgical, one seam)
Parse the date-key from the OBJECT KEY (the last whitespace token of an `aws s3 ls` line -- the object
basename, or the `PRE <subprefix>/` common-prefix), NOT the whole line. `line.split()[-1]` isolates the
key from the LastModified column; `_DATE_KEY_RE.search` on THAT token yields the filename/subprefix
date-key. Preserves the Hive-`PRE snapshot_date=YYYY-MM-DD/` case (its only date IS the key) and correctly
yields None (not LastModified) for a non-date-keyed file. mtime stays a SEPARATE secondary signal.

## FINDING 2 (decision-changing -- surfaced to CTO/CVO-base 2026-07-12): the PROBE and this FIX target
## DIFFERENT freeze-blind paths. Fixing `_max_partition_date` will NOT flip the discrimination probe.
- The TH-A discrimination probe stages a FLAT single-file fixture (`_toolprobe_scratch/comp-freshness/
  frozen.json`) and runs `comp-freshness artifact <uri>`. That path (`cmd_artifact` :1014) looks up a
  config entry by exact prefix (:1039); an UNREGISTERED scratch key -> `entry=None` -> permissive-default
  GUESS (:1058, no `_pk_check`) -> PURE MTIME check (:695-711). It NEVER reaches `_max_partition_date`.
  Grounded live: the fixture returns STATUS=PASS, NOTE "default daily thresholds", rc 0 -- a genuine
  mtime-only false-GREEN (defect **a**), NOT a RAW non-verdict (`--raw` is opt-in, :1273). The keystone
  effective="no" is HONEST for defect (a) -- but it is a SIBLING defect, not the partition-key one (b).
- CONSEQUENCE: acceptance criterion 3 as originally written ("the discrimination probe flips comp-freshness
  effective no->yes") is FALSE. Fixing (b) leaves the ad-hoc `artifact` mtime path (a) unchanged.
- RECOMMENDATION (for CTO): to close the loop on defect (b) HONESTLY, add a SECOND probe case that
  exercises the partition-key mode -- i.e. a registered `as_of_source: silver-partition-key` fixture
  (`silver/<table>/<stale-date>.parquet`, fresh mtime), so pre-fix it false-GREENs via `_max_partition_date`
  (effective=no) and post-fix it CATCHES the freeze (effective=yes). That requires a registered cadence
  entry (comp-freshness only sets `_pk_check` for CONFIG entries), which is more invasive than the flat
  fixture -- hence a CTO design call, not a unilateral one. The current keystone (defect a) stays as-is.

## OPERATIONAL CARE (the blast, quantified -- why this is CTO-gated not unilateral)
- A `.tools/comp-freshness` change goes LIVE fabric-wide on commit (no separate deploy; agents run the
  working-tree tool). So committing == landing.
- LIVE affected set (DS~B P4 census, yaml.safe_load not grep): EXACTLY 5 entries, ALL cot --
  `cot_silver_{holdings,unrealized,allocations,transactions,realized}` under
  `data/cot/scripts/gold/gold_freshness_config.yaml`; 2 are severity=ERROR. **No bd/49F/Schwab entry is
  partition-key mode** per that census.
- I did NOT independently re-census the bd config (`data/black_diamond/.../gold_freshness_config.yaml` is
  under the SOVEREIGN-HELD path -- reading it is a bd read). So "no bd blast" rests on DS~B's P4 census,
  NOT my own read. FLAGGED, not asserted.
- The 5 cot silver entries are in an ACTIVELY-TRACKED freeze (the 07-09 zero-row freeze; the
  `bd-cot-silver-stale-*` alarm trigger due 07-14; "close nothing on cot's alarm state"). Post-fix,
  comp-freshness would start CORRECTLY reporting any currently-frozen cot silver entry as STALE/FAIL --
  wanted behavior, but a NEW live signal landing on a delicate, partly-Andrew-parked situation. That
  interaction is the operational care CTO flagged; the land needs his GO, and ideally a dry-run delta
  (old vs new verdict per cot entry) run first -- an IN-SCOPE cot read I can produce on request.
- TEST OWNERSHIP: inverting test_freshness_partition_key_anticorrelated.py touches DS~B's owned lane
  (NFRA_TOOLCHECK_P4, org/modules/graph/tests/**). The inversion + the fix must land ATOMICALLY (an
  inverted test on the unfixed tool goes RED for everyone). Coordinate with DS~B or have them invert.

## The defect (source-grounded)
comp-freshness's partition-key freeze-detector is meant to catch a daily-rewritten frozen table (fresh
mtime, stale content date-key). But its date reader is ANTI-CORRELATED:
- `_max_partition_date` reads the FIRST `YYYY-MM-DD` on an `aws s3 ls` line -- which is the object's
  **LastModified**, NOT the object's date-PARTITION-KEY (`silver/<table>/YYYY-MM-DD.parquet`), despite the
  docstring swearing it reads the date-key. (test_freshness_partition_key_anticorrelated.py:11-17.)
- CLASSIFIED ANTI-CORRELATED: "the two dates coincide EXACTLY when the pipeline is healthy and diverge
  EXACTLY when it is broken -- and the tool reads the WRONG one." (test :32-33.)
- Consequence: the freeze-detector branch (comp-freshness ~:721) "can NEVER fire on the freeze it names"
  (test :35-43, `test_freeze_detector_branch_cannot_fire_on_a_freeze`). So a frozen-content/fresh-mtime
  artifact reads FRESH -- the paradigm exit-0-while-lying the freeze-detector exists to prevent.

## The fix
Read the object DATE-KEY from the S3 KEY path (`.../YYYY-MM-DD.parquet` -> the partition date), NOT the
`aws s3 ls` line's LastModified timestamp. The max partition-KEY date is the content frontier; compare
THAT to the freshness ceiling. (mtime stays a SEPARATE, secondary signal -- a frozen table has a fresh
mtime, so mtime alone is exactly the wrong oracle for a freeze.)

## Acceptance (revised per FINDING 2)
1. `test_freshness_partition_key_anticorrelated.py::test_R1_*` + `::test_freeze_detector_branch_cannot_fire_
   on_a_freeze` INVERT: post-fix `_max_partition_date(FREEZE)` returns the date-KEY (2026-07-01), not
   LastModified (2026-07-09); the freeze branch CAN + DOES fire (DS~B :53-54 explicitly designates the RED
   as the acceptance signal). Land the fix + the inversion ATOMICALLY (DS~B-owned test).
2. A synthetic frozen-content/fresh-mtime PARTITION-KEYED artifact -> comp-freshness says STALE (not FRESH).
3. (CORRECTED) A NEW partition-key probe case -- NOT the existing flat-fixture discrimination probe (which
   tests defect a, mtime-only ad-hoc, and is UNAFFECTED by this fix; see FINDING 2) -- flips effective
   no->yes. Whether to add that case (vs. accepting a+b as two distinct catches) is a CTO design call.

## OPEN DECISIONS for CTO (surface, don't adjudicate)
- **D1 (operational-care GO):** DRY-RUN DONE 2026-07-12 (CTO GO) -- 0 of 5 cot entries flip verdict old->new;
  land is safe-but-not-urgent, HELD until post-07-14 cot-clarity + a FRESH dry-run at land-time (CTO 151616Z:
  the fix is ~24h STRICTER, a threshold change not a no-op). **LAND-TIME RE-CONFIRM TOOL:
  `cot_pk_dryrun_land_reconfirm.py` (this dir) -- run it immediately before landing; exit 0 + "0 of 5" = safe,
  any flip = STOP + surface.** bd blast rests on DS~B's cot-only census, not my read (sovereign).
- **D2 (probe alignment):** add a partition-key probe case to close the loop on defect (b), or accept
  defects (a) and (b) as two independently-caught misses (keystone catches a; this fix removes b)?
- **D3 (ownership + test):** I (CVO~B) can implement the one-seam fix; the inverted test is DS~B's lane
  (NFRA_TOOLCHECK_P4). Coordinate the atomic land with DS~B, or route the whole fix to DS~B?
The fix is a one-seam change (`line.split()[-1]` before the date regex) -- SPEC'D above, HELD uncommitted
until D1 (committing == landing live on the 5 cot entries). Not coupled to the keystone (already landed).
