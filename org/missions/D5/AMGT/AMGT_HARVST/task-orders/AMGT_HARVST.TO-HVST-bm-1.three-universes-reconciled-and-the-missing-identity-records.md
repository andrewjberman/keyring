# AMGT_HARVST task order -- `HVST-bm-1` -- ROUND 68 (`1.0.0_SA_CTO~Z` msg 31637 (R19, R20), on `4.0.0_SA_CRO~Z`'s research `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_STANDING_COLLECTION_AND_DAILY_SWEEP_RESEARCH_20261008.md` @2394cfc3d8): THE THREE UNIVERSES RECONCILED (LIST 242, CROSSWALK 237, COLLECTOR 234) AND THE MISSING IDENTITY RECORDS WRITTEN AS NEW FILES -- NOTHING FETCHED, NO CONFIG CHANGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~120</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL files and scripts, plus READ-ONLY reads (S3 GET of the pool universe and the crosswalk object). NO put, NO delete, NO job, NO collector, backfill_driver or emitter run, NO vendor, publisher or Bloomberg call. `lib/opal_data_harvest/config.json` is NOT changed: one collection leg is LIVE and reads the two round-47 files it names. `.runtime` is not read.
comp-adversary: RUN at L5 -- the adversary is a round-47 file edited in place, a config pointer moved, a name completed by guessing, a record added from a source that does not carry it, or a job run to test the result.
</preflight>

## 0. THE CELL

Three sets of securities are in use and they do not agree:
- the SERVED GOLD LIST, 242: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json`, built by `lib/research/harvest/universe_securities.py` `build()` from the pool
  universe (`s3://opal-data-harvest/universe/v1/2026-10-06.json`, 302 records);
- the CROSSWALK, 237 records: `lib/research/identity/crosswalk.py` (read its docstring for where the object lives and how
  it is loaded);
- the COLLECTOR'S UNIVERSE, 234: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_20261005.json` (`entries`) with its search identities
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/rank_universe_identity_20261005.json` (`records`). `lib/opal_data_harvest/config.json` names these two files as
  `universe_source` and `symbol_resolution_source`. The collector only ever asks for a security that has a record there.

Three keys are already known to be on the list and absent from the collector's files: `CAT_US_Equity`, `CSL_AU_Equity`,
`6861_JP_Equity`. So Caterpillar, CSL and Keyence have never had a collection job. The builders of the two collector files
are `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/at-5.widen_universe.py` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/build_rank_identity.py` (the identity file's `rules` field states its
rules). Read both before you write.

**A run for any added name waits on Andrew's per-use word. This cell fetches nothing and changes no pointer.**

## 1. THE BUILD (LOCAL)

1. `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/bm1_three_universes.py` prints `DENOMINATORS: gold list <a>, crosswalk <b>, collector universe <c>, collector
   identity records <d>` and the join key it used for each, then the seven regions of the three-set comparison as counts,
   and for every region that is not "in all three" EVERY key with its company name where a source gives one:
   `ON THE LIST, NOT IN THE COLLECTOR: <n>` (expected to include the three above), `IN THE COLLECTOR, NOT ON THE LIST: <n>`,
   `IN THE CROSSWALK ONLY`, and so on. For each key say which stored source carries it (pool record, registry entry,
   crosswalk record).
2. **The new files, beside your script, NOT in round 47:** `rank_universe_20261008.json` and
   `rank_universe_identity_20261008.json`: byte-for-byte the round-47 files' content for every existing entry and record,
   plus ONE entry and ONE record for each key that is on the gold list and absent from the collector, built by the SAME
   rules the two builders apply, from STORED sources only (the pool record, `lib/research/identity/registrations.json`, the
   crosswalk). Where a field's stored source does not carry a value, the field says so in the form the file already uses
   for an unmeasured value; nothing is guessed and no vendor is called. `snapshot`, `author` and the denominator fields
   are updated to say what the new files are and what they were made from.
3. Print `ADDED: <n>` and each added record's key, company, ticker and search forms with the source of each; and
   `EXISTING RECORDS CHANGED: <c>` (must be 0), checked by comparing every pre-existing entry and record with the round-47
   files.
4. Do NOT edit either round-47 file and do NOT change `lib/opal_data_harvest/config.json`. Run no job.
5. **Plants** in `lib/opal_data_harvest/test_bm1_identity_records.py` (no network), reading your two new files: (i) every
   round-47 record is present and equal; (ii) `CAT_US_Equity`, `CSL_AU_Equity` and `6861_JP_Equity` each have a record
   with a non-empty company; (iii) the collector's own loader accepts the new identity file (call the function that loads
   `symbol_resolution_source`, pointed at your file by argument or a patched config, not by editing the config);
   (iv) THE NEGATIVE CONTROL: the round-47 identity file has no record for those three keys.
6. Last line of the script's output: `RECONCILE OK` only if all four denominators are above 0, the regions sum to the union,
   ADDED is at least 3 with the three named keys among them, and EXISTING RECORDS CHANGED is 0. Otherwise `RECONCILE FAIL`
   and the failing line. Write the output as `bm1_three_universes.out`.

Change an existing test assertion only where this cell's rule is the reason, and list each in your report.

<paths>
lib/opal_data_harvest/
lib/research/identity/
lib/research/harvest/universe_securities.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round64/securities.universe.r64.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round47/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bm-1"><invocation>python -m pytest lib/opal_data_harvest/test_bm1_identity_records.py -rA --tb=line -p no:cacheprovider</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bm-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/bm1_three_universes.out</invocation><expect>RECONCILE OK</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing; your next row id is `AMGT_HARVST-Z-W120-S1`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~120/AMGT_HARVST.TO-HVST-bm-1.three-universes-reconciled-and-the-missing-identity-records.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-bm-1.three-universes-reconciled-and-the-missing-identity-records`. Pin every artifact row to the commit that carries it.
- Run every script from the repo root of YOUR worktree as `PYTHONPATH=. python <file>`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~Z` msg 31637 (R19, R20), on `4.0.0_SA_CRO~Z`'s research `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/HARVST_STANDING_COLLECTION_AND_DAILY_SWEEP_RESEARCH_20261008.md` @2394cfc3d8. Decomposition section 82.
- R20 (a): "reconcile the three universes, list 242, crosswalk 237, collector 234, and add the missing identity records (CAT_US,
  CSL_AU, 6861_JP named so far)". R19: no sweep is built or scheduled. "A run for any of them waits on Andrew's per-use word."
- **Issuer ruling inside the decomposition** (no gate limb graded it): the records are added as NEW dated files beside the
  worker's script and the config pointer is not moved, because one collection leg is reading the round-47 files now and a
  pointer move is what would make the collector ask for the new names. Moving the pointer is a later act, with
  `1.0.0_SA_CTO~Z`'s word and Andrew's per-use word for the run it enables.
- `HVST-bl-1` (round 67, in flight) is the read behind this cell: the securities that never had a job.
- Slot ~120's queue: `bm-1`, then `bm-2`. **Checks dry-run at the base:** AC1 base FAIL as expected (the test is absent); AC2
  base FAIL as expected (no such file).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>68</round>
<slot>~120</slot>
<fabric>site-z</fabric>
