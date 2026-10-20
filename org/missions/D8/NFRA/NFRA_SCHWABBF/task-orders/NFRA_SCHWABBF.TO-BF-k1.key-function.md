# TO NFRA_SCHWABBF.TO-BF-k1 -- thread hop 1: the one Schwab bronze key function, in the builder's form, both mirrors

<to_id>NFRA_SCHWABBF.TO-BF-k1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-k-1` (`decompositions/NFRA_SCHWABBF_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-k-1`, PRD contract C-KEYFORM. Andrew-direct 2026-10-19: Schwab files "should be organized in the opal-data-assets bucket in canonical LGIC_NAMING path form";
2026-10-20: the stored files move to that form (one cutover, no side-by-side copy). FWD-4 ACCEPT: "Someone who only knows the naming builder finds any stored Schwab raw file on the
first try, and never finds the same day stored two different ways."

**What exists (read it, then change only the two key-function files).**
- `data/black_diamond/scripts/bronze/_monolith_bronze.py` and `data/canonical/schwab/silver/_canonical_silver_lib.py` each carry `monolith_bronze_key(feed, date_compact, master)`
  and the partition-listing helpers (`list_bronze_dates` in the first, `latest_bronze_date` in the second). The first is MIRRORED, not imported (it deploys standalone to
  `s3://opal-data-bd/code/`): "Any change to the purpose law or the key grammar lands in BOTH files in one commit". Do exactly that: one commit, both files, byte-equal helpers.
- Today's grammar: `schwab/{master}/bronze/{feed}/{YYYYMMDD}/{master}.CRS{YYYYMMDD}.{FEED}.zip` (feed lower-case in the folder, upper-case in the file name).
- The builder: `lib/opal_naming.py` `address(source, scope, layer, ...)`. Measured 2026-10-20: `address('schwab','08403355','bronze','acc','date=2023-10-17')` returns
  `s3://opal-data-assets/schwab/08403355/bronze/acc/date=2023-10-17`; it accepts any type token and all three masters (08242234, 08335338, 08403355).
- The silver converter Lambda (`data/assets/scripts/silver/schwab_conversion.py`, deployed twin `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_conversion.py`) derives master
  from path segment 1 and the type and date from the FILE NAME (`scope_from_key`, `feed_from_key`, `date_from_key`). It is key-shape agnostic. READ ONLY; do not edit it.

**The new contract (fixed here so the other cells of this round build against it; do not rename).** Bucket stays `opal-data-assets`; every function below returns a KEY (no bucket, no `s3://`).
1. `bronze_partition_prefix(master, feed, date_compact) -> str` = the builder's address with the bucket removed: `schwab/{master}/bronze/{feed.lower()}/date={YYYY-MM-DD}` (no trailing slash).
   The ISO date is `date_compact[:4]-[4:6]-[6:8]`; a `date_compact` that is not 8 digits or not a real calendar date RAISES.
2. `bronze_key_for_file(master, feed, date_compact, filename) -> str` = `bronze_partition_prefix(...) + "/" + filename`, the vendor file name UNCHANGED (Schwab ships two name forms,
   `{master}.CRS{YYYYMMDD}.{TYPE}.zip` and `{master}.CS{MMDDYY}.{TYPE}.zip` for `fam` and `slm`; the key keeps whichever it is).
3. `monolith_bronze_key(feed, date_compact, master) -> str`: SAME SIGNATURE as today, now `bronze_key_for_file(master, feed, date_compact, f"{master}.CRS{date_compact}.{feed.upper()}.zip")`.
4. `parse_bronze_key(key) -> dict(master, feed, date_compact, filename)`: accepts the NEW form only; raises `ValueError` on anything else (including the old form).
5. `parse_legacy_bronze_key(key) -> dict(master, feed, date_compact, filename)`: accepts the OLD form only (`schwab/{master}/bronze/{feed}/{YYYYMMDD}/{filename}`); raises on anything else.
   The move script uses it. The master must be 8 digits; the feed and the date folder are taken from the PATH, the file name from the last segment.
6. The partition listers (`list_bronze_dates`, `latest_bronze_date`, in the files that carry them today) keep their signatures and their return type (compact `YYYYMMDD` strings) but read the NEW form:
   a partition token is `date=YYYY-MM-DD`; return it as compact. If the prefix holds no new-form token but holds old-form tokens (eight digits), RAISE `ValueError` saying the count of old-form
   objects seen and "not moved" -- an empty answer there would read as "nothing landed" when the truth is "not moved yet". During the days between the copy and the delete both forms coexist: ignore
   old-form tokens when at least one new-form token exists. No new-form and no old-form token: `list_bronze_dates` returns `[]`, `latest_bronze_date` raises as it does today.
7. Both files' docstrings say: this grammar supersedes `{master}/bronze/{type}/{YYYYMMDD}/` recorded in `docs/architecture/OPAL_ASSETS_CONSOLIDATION_PRD.md` (line 36 and 477) and
   `docs/architecture/OPAL_ASSETS_PRD.md` (line 494), by Andrew-direct 2026-10-19 and 2026-10-20 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_130xZ_NFRA_SCHWABBF_DONE_WHEN_CONFIRMED_PATH_MOVE_YES_210_MASTERS_OUT.md`).
   Do NOT edit those two documents.

Callers of these functions (the converters, `build_*`) are other cells' business or follow the function unchanged. Keep every existing public name working.

**Test (`data/canonical/schwab/tests/test_bronze_key_form.py`).** Load both files by path (the bd-tree file cannot be imported as a package module); stub `boto3` clients and the S3 listings (no network):
- PARITY: for 3 masters x 17 feeds (acc rps trn tnn sec uln ult rld rlu rly rtu rty fam slm upn upt trn_nna) x 2 dates (2023-10-17 and 2026-10-16): both files return the same string, and it equals
  `address('schwab', master, 'bronze', feed, 'date=YYYY-MM-DD')` with `s3://opal-data-assets/` removed, plus `/` plus the vendor name. Import `lib.opal_naming` from the repo root.
- ROUND TRIP: `parse_bronze_key(bronze_key_for_file(...))` returns the inputs; `parse_legacy_bronze_key` accepts an old-form key and refuses a new-form key, and the reverse for `parse_bronze_key`; the CS-form name survives.
- LISTERS: a stubbed listing with new-form partitions returns compact dates sorted; a listing with only old-form tokens RAISES with the count; a mixed listing returns the new-form dates only.
- CONVERTER SEAM (name the test function with the words `converter_seam`): import `data/assets/scripts/silver/schwab_conversion.py` by path and assert that `scope_from_key`, `feed_from_key` and `date_from_key`
  return master, feed and date for a NEW-form key built by `monolith_bronze_key` -- the neighbor that every copied object will wake up. That file does `import stream_parquet as sp` (line 66), and the module is tracked at `data/assets/scripts/lib/stream_parquet.py` (the Lambda package carries it beside the handler). Inside the test only, put `data/assets/scripts/lib` on `sys.path` before loading the converter by path. (Issuer ruling 2026-10-20 after row `NFRA_SCHWABBF-W1-S1`; no `<paths>` change, the directory is read-only.)

### ACCEPTANCE

<criterion id="BF1-k1-AC1" cell_refs="BF-k-1"><invocation>python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF1-k1-AC1` -- parity of both mirrors with the builder over 3 masters x 17 feeds x 2 dates, the parsers, and the listers including the refusal on a prefix that is only old-form. The bar is a pytest summary line that STARTS with the passed count, so a line that opens with a failed count does not match.

<criterion id="BF1-k1-AC2" cell_refs="BF-k-1"><invocation>python -m pytest data/canonical/schwab/tests/test_bronze_key_form.py -q -p no:cacheprovider --color=no -k converter_seam</invocation><expect>^1 passed[ ,]</expect></criterion>
`BF1-k1-AC2` -- the seam probe against the REAL neighbor: the silver converter's own key readers accept a new-form key.

<expected_criteria>BF1-k1-AC1,BF1-k1-AC2</expected_criteria>

Dry-run at the base 2026-10-20: AC1 and AC2 "file or directory not found" (rc 4) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named is READ and never edited.
- **LOCAL.** No S3 read or write, no deploy, no network. The deploy of the bd-tree copy to `s3://opal-data-bd/code/` is the issuer's release act R5.
- **The next orders in your queue (`TO-BF-m1`, then `TO-BF-r1`) import this contract.** Keep the six names and signatures exactly as written above.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing),
  and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/bronze/_monolith_bronze.py
data/canonical/schwab/silver/_canonical_silver_lib.py
data/canonical/schwab/tests/test_bronze_key_form.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP.md</decomp_doc> (round 1), cell `BF-k-1`.
<owned_cells>BF-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF1-k1-AC1, BF1-k1-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-k1.key-function.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> BF1-k1-AC1,BF1-k1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the six function names with their signatures, the pytest summary line for each criterion, the one commit hash covering both mirrors, and any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round.
comp-iam: RUN -- decomposition battery: new keys sit inside the box role's `schwab/<m>/bronze/*` grants (monolith-iam.tf:60-81); this cell touches no IAM and no network.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; findings 4, 5 and 6 of the decomposition battery (date from AsOfDATE not filename; address() accepts any type token; CRS-only name form) are inlined in the face above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-KEYFORM, C-NAMES; decomposition round 1 cell BF-k-1; CVO carried items 2 (supersession named in the docstrings) and 3 (not a cell matter).
