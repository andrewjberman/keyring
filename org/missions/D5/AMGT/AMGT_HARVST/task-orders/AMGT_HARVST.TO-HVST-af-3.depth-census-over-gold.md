# AMGT_HARVST task order -- `HVST-af-3` -- ROUND 33: THE FWD-14 DEPTH TABLE OVER SERVED GOLD, WITH THE UNIVERSE-TO-GOLD KEY JOIN FIXED (row Z-S51)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-af-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL: code, tests and S3 READS of gold; no write anywhere outside the repo.
comp-adversary: RUN at L5 -- the adversary is a join that silently drops names (a census over the names that happen to map reads as the universe). AC2 requires MAPPED + UNMAPPED lines to account for all 89.
</preflight>

## 0. THE CELL (decomposition section 46, `HVST-af-3`; PRD v0.13 FWD-14; row Z-S51)

**FWD-14:** a census over the stored mention table prints, for every security in the 89-name collector universe and for
each of the five publishers, the count of distinct articles published since 2026-01-01 (denominator: 89); DONE when
every security reads 50+, 100+ reported beside it; Andrew's number is never re-based; a security below 50 stays OPEN
with its per-publisher counts.

**Row Z-S51 (measured):** the collector universe (`python -m lib.opal_data_harvest universe`: 89 rows, keys like `BA`
or `security-<hash>`, fields `key, company, ticker, aliases, sa_symbol, identity_*`; 57 of 89 have `ticker` null) and
the gold `article_security_mention` table (keys like `BA_US_Equity`, `992_HK_Equity`) share 0 keys. Gold is built over
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json` (crosswalk-resolved
keys). `lib/research/identity/crosswalk.py` is the estate's resolver ("resolving a bare association key to its canonical
form is the crosswalk's job, never guessed by appending 'US Equity'").

## 1. THE BUILD (LOCAL)

1. **`lib/opal_data_harvest/depth_census.py` (new), run as `python -m lib.opal_data_harvest.depth_census`:**
   - Load the collector universe (89) and map each universe row to its gold `security_key` through the estate's own
     resolvers ONLY: the crosswalk, then the ~46 securities file matched on `company` / `aliases` / `sa_symbol` /
     `ticker`. Never synthesize a key. A row that does not map prints `UNMAPPED <universe key> <reason>`.
   - Read the NEWEST `article_security_mention` gold part (the builder's own `_latest_gold_snapshot_rows`); print
     `SOURCE: gold <that part's key>`.
   - Per mapped security and per publisher (sa, bbg, wsj, ft, barrons): distinct `article_key`s with
     `published_utc >= 2026-01-01`. Print `DENOMINATOR: 89`, `MAPPED: <k> of 89`, one row per security (total + per
     publisher), then `AT 50+: <n> of 89` and `AT 100+: <m> of 89`, then `S3 WRITES: 0`. `--json PATH` also writes the
     table locally.
2. **`lib/opal_data_harvest/test_af3_depth_census.py` (new)**, plants with in-memory rows: (i) a universe row with no
   ticker maps through aliases; (ii) an unmappable row prints UNMAPPED and is still counted in the 89; (iii) pre-2026
   articles are excluded; (iv) a duplicate article across publishers counts once in the total.
3. Run it once for real and keep the output (`af3_census.out`, and `--json` as `af3_census.json`).

<paths>
lib/opal_data_harvest/depth_census.py
lib/opal_data_harvest/test_af3_depth_census.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads (no write):** `lib/research/identity/crosswalk.py`, `lib/research/harvest/publication_gold.py`,
`lib/research/harvest/store.py`, the ~46 securities file, `lib/opal_data_harvest/__main__.py` (universe).

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-af-3"><invocation>python -m pytest lib/opal_data_harvest/test_af3_depth_census.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-af-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round33/checks/af-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-af-3.depth-census-over-gold.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-af-3.depth-census-over-gold`.

## AMENDMENT 1 -- 2026-10-01 ~12:4xZ, the issuer, on the census report (row Z-W90-S4)

1. **Z-W90-S4 ACTED ON:** the gold securities file is now 212 rows (the 21 crosswalk keys added under the CTO-signed
   ADDENDUM 1 @e24ca120a2), and served gold was rebuilt over it @e0d3a13ef1 (act record
   `deliverables/2.0.0_SA_COO_H/round32/gold_rebuild_act_20261001T122401Z.json`, `universe_file`
   `deliverables/2.0.0_SA_COO_H/round33/securities.universe.r33.json`).
2. **The census's gold key set is what GOLD CARRIES, never a fixed file:** `depth_census` takes the set of
   `security_key`s from the NEWEST `chatter_daily` part (it carries every security gold was built over), and matches on
   company / aliases / sa_symbol / ticker against the universe file that part was built from (the newest gold act
   record's `universe_file`, else the r33 file, else ~46's). Print `GOLD KEYS: <n> (from <daily part key>)`.
3. Plant: a crosswalk key present in the daily part's key set maps even when the base ~46 file lacks it.
4. Re-run the census, AC1 and AC2; flip `<status>` when both pass. No other change.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-32 analysis @`749ec2c72e` item 3; row Z-S51. Gold is served-only-by-hand; this census reads the
newest part, so its numbers rise after the issuer's paired gold rebuild.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>33</round>
<slot>~90</slot>
<fabric>site-z</fabric>
