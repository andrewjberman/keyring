# AMGT_RESAPP task order -- `AMGT-rk-33` -- C-PRODUCTION-HOME: the unit map to config beside its producer; the SEC cache and the peer candidate universe to builder-made pool addresses; a dry run writes nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-33</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~37</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected; no schedule is read or written.
comp-iam: RUN -- (comp-iam ran at the cut, 2026-09-18 19:5xZ, stats saved by the issuer) this order writes ONE new object family into the standing shared bucket
  s3://opal-data-harvest (Andrew's designated home, at the canon's bronze prefix; registry-gated, see the issuer amendment) at an address lib/opal_naming.py
  builds, under the device's EXISTING credentials; it grants no permission, provisions no bucket, no role and
  no policy, and touches no Terraform except the two GENERATED naming-module test files it REGENERATES
  (never hand-edits). A permission refusal on the put is recorded as a row and the SEC half stays at its
  current path with a printed WARN; it is never worked around.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~37`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`,
`lib/opal_naming.py`, `infra/logic/registry/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~37;`. **NEVER RUN AN
INSTALL.** **YOU ARE STEP 1 OF A TWO-STEP SEQUENTIAL QUEUE ON `lib/research/identity/build_universe.py`:**
`AMGT-rk-32` (chain I, slot ~36) edits the SAME file after you and its first act verifies that this order
landed. Drain fully before it starts; the interface names in RULED 3 are what it cites -- keep them exactly.

## 1. THE CELL, inlined in full -- `AMGT-rk-33` (R14-H1; S-W32-S4, M1, V7/D24; co-sign NO)

**The analysis row, verbatim (ROUND_ANALYSIS.round13.md s.4 @9c8e04cd9a, :123):** `C-PRODUCTION-HOME`: the
unit map to config beside its producer; the SEC cache and the peer candidate universe to the pool at
builder-made addresses; **a dry run writes nothing**. Ruling s.3.6 (:98): the peer universe cache (W32-S4,
OPEN) is RULED under `C-PRODUCTION-HOME`, this cell. The root cause it retires (s.2, :55-61): three production
code paths read or write a WORKER'S deliverables folder, which is the proof artifact of ONE task order and covers
only the names that worker handled.

**The constraint -- `C-PRODUCTION-HOME` (PRD v0.13 @1699960261, :1643-1650), verbatim:** A production code path
never reads or writes a WORKER'S deliverables folder -- that folder is the proof artifact of one task order and
covers only the names that worker handled. Configuration (for example the unit map) lives under version control
beside the producer that reads it; cached data (for example the SEC ticker table and the peer candidate
universe) lives in the pool at an address built by `lib/opal_naming.py` (Rule 30). A dry run writes nothing,
anywhere. Measured instances this clause retires: the unit map (`integrations/bloomberg/research/
model_block_pull.py:286-288`, worker ~1), the SEC ticker cache (`lib/research/identity/build_universe.py:503-507`,
worker ~19, whose miss is reported as absence from the full table), and the peer candidate universe
(`lib/research/peers/universe.py`, worker ~21, rewritten even under `--dry-run`).

**THE MEASURED STATE (code @075227f4c0; the validation @b527b93214).**
- *Unit map.* `model_block_pull.py:286-288` `_FIELD_MAP_PATH` = `deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json`,
  cwd-relative; read by `_field_map()` :292-299, `_resolved_unit()` :302-318, `_resolved_sign()` :321-336,
  `_currency_caveat()` :352-366. The file carries 3 securities and 36 fields (`field_map.json:2-6`). In the
  SAME file, the SAME class: `_pull_log_path()` :464-467 WRITES `deliverables/0.9.0_WK_AMGT_RESAPP~1/pull_log.json`
  from `cmd_pull()` :470-485 (:482-483), while the input ledger already records every pull (:246).
- *SEC cache.* `build_universe.py:450-453` `SEC_CACHE_DEFAULT` = `deliverables/0.9.0_WK_AMGT_RESAPP~19/sec_ticker_cik_cache.json`;
  `ENV_SEC_CACHE` :454; `load_sec_cache()` :478-484 opens it; `filing_identity_for()` :491-539 reads `rows`
  (:503), the table block (:497, :505-507) and `submissions.by_cik` (:518-520); `union_main()` :849 passes it in;
  `--sec-cache-path` :929. The document (`sec_ticker_cik_cache.json`) is a PROJECTION of the SEC table: 33 roots
  probed, 15 present, 18 absent (:15-20) over a 10,422-row delivery whose sha256, bytes, retrieval time and
  `source_last_modified` it records (:5-14), plus EDGAR submissions measurements for 15 CIKs (:188-192). Its
  miss message reports the DELIVERY's row count, not the projection's (validation D1 :174-176; Caterpillar).
  The READ semantics (full table, honest miss) are `AMGT-rk-32`'s; the HOME is yours.
- *Peer candidate universe.* `peers/universe.py:81-86` `CACHE_DIR_DEFAULT` = `deliverables/0.9.0_WK_AMGT_RESAPP~21/`,
  `CACHE_NAME` `candidate_universe.json`, `ENV_CACHE` :89, `cache_path()` :141-147; `fetch_factor_metadata()`
  :169-179 WRITES `scanner_factor_metadata.json` beside it (:178); `load_candidate_universe()` :558-582 REBUILDS
  and WRITES the cache when it is absent or lacks `preset_value_codes` (:568-580) -- reached from
  `engine.py:1453` (the `--security-key` path, BEFORE its own `--dry-run` branch at :1463) and `engine.py:1249`
  (the batch). Validation D24 :230-232: a `--dry-run` rewrote the tracked cache (restored; committed blob
  1,000,578 bytes, :20-22). The model-block half reads worker ~1's `model_block_*.json` (`MODEL_BLOCK_DIR_DEFAULT`
  :68-72, `_model_block_files()` :182-197, used at :417) -- the same class, NOT this order's write (see BOUNDS).
- *The builder.* `lib/opal_naming.py` `key()` :1542-1555 (source must be a `systems.json` key :1548-1549; scope a
  `scopes.json` LONG form :1550; never a product beneath itself :1551-1552; tier from the schema :1553-1554),
  `address()` :1558-1571 (the bucket from `tiers.json` homes via `_home_bucket()` :249-261 -- `shared` names a
  standing bucket, `scope` the scope row's bucket, `source` the SOURCE's own scope row :256-260; a KeyError or
  RegistryError becomes ValueError "no home bucket for tier ..." :1562-1565). The registry today:
  `systems.json` has NO `sec` row (VENDOR rows :64-212: schwab, blackdiamond, orion, eclipse, smartx, pathfinder,
  trueshares, ycharts, fred, seeking-alpha, bloomberg, msci) and lists `harvest` UNRESOLVED (:339-342);
  `scopes.json` has NO `amgt` and NO `harvest` scope (rows: 49financial, inflection, cottonwood, demo, global,
  08242234, 08335338, mdpf, etfs); `tiers.json:26-33` COMPOSITE tenancy (the `global` scope): bronze and silver
  -> `opal-data-assets` (:27-28), gold -> `source` (:29). `opal-data-harvest` (the pool) is in no registry row
  and no standing-shared list (`05_IDENTITY_SPINE.md:77` marks it UNRESOLVED, tick-list row 18). The doctrine:
  R4 bronze/silver have ONE home (`02_DOCTRINE.md:336-346`); R9 bronze is the delivery byte-for-byte
  (:402-409); N1 the key grammar with `source` a VENDOR key for a feed (:205-224, :210); a scope not on the
  tick-list returns to Andrew (:589-591); R20 an undeclared departure is a violation (:534-545). The checklist:
  `python lib/opal_naming.py validate` must print `VALIDATE: OK` (`10_ONBOARDING_CHECKLIST.md:90`); `address()`
  is the ONE source of an S3 address (:241-242, :261-262).

**RULED -- what you build, in this order.**
1. **FIRST ACT: run the builder and RECORD its answer** (AC1) for both datasets BEFORE any code edit, verbatim,
   into your deliverables folder. The two calls and their EXPECTED answers at the cut, from the code lines above:
   - `address("sec", "harvest", "bronze", "company_tickers", "date=2026-09-15")` -> REFUSED, `source 'sec' is not a
     systems.json key` (:1548-1549). **This refusal named a missing VENDOR row -- LANDED before spawn by `1.0.0_SA_CTO~Z` @e44380a9d1 (with `lusha`,
     `bright-data` and the `harvest` scope row). You do NOT add or edit `infra/logic/registry/systems.json`: VERIFY the `sec`
     row is present in YOUR worktree (`python -c` read of the file, key printed) and STOP with a row if it is not. The row's
     shape as landed supersedes the draft below, which read (Rule 30, at the cut):**
     `infra/logic/registry/systems.json` gains `{"key": "sec", "class": "VENDOR", "long": "sec", "owner_directive":
     "D8", "owner_claim": "inferred", "owner_basis": "a feed no directive names as its own is read as D8's
     (title 'Data Pipelines'), the same inference the other feed VENDOR rows carry; the SEC ticker table
     (https://www.sec.gov/files/company_tickers.json) and EDGAR submissions are consumed by D5's AMGT_RESAPP
     (lib/research/identity/build_universe.py, lib/research/filings/fetch.py)"}`, in the vendors' position.
     Then `python lib/opal_naming.py validate` prints `VALIDATE: OK`, and the builder returns
     `s3://opal-data-assets/sec/harvest/bronze/company_tickers/date=2026-09-15` (tiers.json:27). The registry
     change moves the marks of two GENERATED files (opal_naming.py `TARGET_REGISTRY_KEYS` :97-108 name
     `systems` for `infra/aws/terraform/modules/opal_name/tests/vectors.json` and `opal_name.tftest.hcl`):
     REGENERATE both with `python lib/opal_naming.py generate --out . --target <path>` -- if anything beyond
     the mark line changes, STOP and file a row (a `sec` VENDOR row adds no vector: `_VECTOR_SHAPES` :1613-1614).
   - `address("amgt", "harvest", "gold", "candidate_universe", "date=2026-08-06")` -> REFUSED, `scope 'harvest' resolves to no scopes.json row` (:1551-1565; MEASURED by the issuer at the cut,
     2026-09-18 23:0xZ, on HEAD bytes -- under the L4 ruling @2560e04f46 the missing row is the `harvest` PRODUCT scope,
     bucket opal-data-harvest). **This refusal names a missing SCOPE row -- the `harvest` PRODUCT scope whose bucket
     is `opal-data-harvest` (CTO L4 ruling @2560e04f46; validate :342-343) -- and WHICH scopes exist and how they are shaped is
     Andrew's per-scope call (`02_DOCTRINE.md:589-591`), NOT yours.** Do NOT add it. Do NOT hand-type
     `opal-data-harvest` anywhere. File ONE row (`spec_asserts`: C-PRODUCTION-HOME's "in the pool at an address
     built by lib/opal_naming.py"; `world_is`: the refusal verbatim, the row it names, the address the builder
     would give once the row exists, and `head_bucket` on that bucket) -- and proceed with RULED 4.
   - **The negative arm, both datasets:** if the builder RETURNS an address whose bucket EXISTS (the registry
     moved under you), the move in RULED 3/4 lands there and no row is filed for that dataset.
2. **The unit map -> config beside its producer.** Copy `deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json`
   BYTE-FOR-BYTE to **`integrations/bloomberg/research/field_map.json`** (THE config path this order establishes;
   `AMGT-rk-34` rebuilds the map for every name and WRITES this path -- keep the name exact). `_FIELD_MAP_PATH`
   :286-288 becomes `Path(__file__).resolve().parent / "field_map.json"` (beside the producer, never cwd-
   relative). The pull log (:464-467, :482-483) is the same class in the same file: it becomes ONE object per pull
   beside the raw landing it records, `raw/bloomberg/<KEY>/<stamp>/pull_log.json` (the EXISTING raw family,
   put-if-absent as :184-198; Rule 30 does not bind an existing family), and the cumulative repo file is no
   longer written. Do NOT touch `SECURITIES` :53, `HIST_END` :101 or the field lists -- those are chain M's.
3. **The SEC cache -> its bronze home, the interface `AMGT-rk-32` cites (names EXACT):**
   - `build_universe.sec_table_address(partition_date: str, object_name: str) -> str` returns
     `opal_naming.address("sec", "harvest", "bronze", "company_tickers", "date=" + partition_date,
     object=object_name)`; `build_universe.sec_table_prefix() -> (bucket, key_prefix)` derives the listing prefix
     from that address by splitting at `/date=` (a derivation from builder output, never a typed literal).
     `opal_naming` is loaded by PATH (`lib/` has no `__init__.py`, opal_naming.py:27-28) exactly as
     `.tools/naming-gate.py:123-125` does, or by namespace import if `from lib import opal_naming` resolves --
     prove one in a one-liner and use it.
   - The existing document is LANDED unchanged (bytes identical, sha256 printed both sides) at
     `sec_table_address("2026-09-15", "sec_ticker_cik_cache.json")` -- `2026-09-15` is the document's OWN
     `retrieved_at` date (:8) -- with `crosswalk.write_pool(key, payload, bucket=<the address's bucket>)`'s
     discipline (put with `document-sha256` metadata, head read-back; `crosswalk.py:609-657` takes a bucket).
     NAME the residue in your report and on the object's provenance note: this object is the 2026-09-15
     delivery's PROJECTION (33 of 10,422 rows) with the delivery's own sha256/bytes/retrieval time, not the
     delivery's bytes; `AMGT-rk-32` lands the full delivery `company_tickers.json` beside it, after which only
     this object's `submissions` block is read.
   - `load_sec_cache(path=None)` reads the NEWEST partition under `sec_table_prefix()` (an object named
     `sec_ticker_cik_cache.json`) and returns the SAME document shape as today (`rows`, `ticker_to_cik_table`,
     `submissions`) with one added key `ticker_to_cik_table.object` = the address read; `AMGT_SEC_CACHE_PATH`
     (:454) stays as the LOCAL override for tests and the `--sec-cache-path` flag (:929) stays; `SEC_CACHE_DEFAULT`
     (:450-453) is REMOVED, and no `~19` literal survives in the file. An absent pool object REFUSES LOUDLY
     naming the address (never a fallback to any repo path). `filing_identity_for()` :491-539 is NOT edited by
     you (its read semantics are `AMGT-rk-32`'s).
   - The `--dry-run` of `python -m lib.research.identity.build_universe --as-of <date> --dry-run` (:854-860)
     still writes nothing anywhere: reading the pool object is a read.
4. **The peer candidate universe.** (a) **A READ NEVER WRITES:** `load_candidate_universe()` :558-582 rebuilds a
   stale or absent cache IN MEMORY and returns it, with `cache_path` reported and NO `_write_json` (:578-580
   retired); `fetch_factor_metadata()` :169-179 likewise never writes on a read. The ONLY writer is
   `python -m lib.research.peers.universe --refresh` (`main()` :661-689), which writes and READS BACK. `engine.py`
   is NOT edited: its :1453 and :1249 calls become read-only by this module's contract (chain P owns engine.py).
   (b) **The home:** `universe.candidate_universe_address(vintage: str) -> str` returns
   `opal_naming.address("amgt", "harvest", "gold", "candidate_universe", "date=" + vintage,
   object="candidate_universe.json")` -- it RAISES the builder's own refusal today (RULED 1) and never a typed
   string. Under the refusal: `cache_path()` :141-147 keeps its current default, and EVERY load prints ONE
   `WARN: C-PRODUCTION-HOME: candidate universe read from a worker folder; home blocked on <the row id>`
   line (a log line, not a monitor), so the departure is never silent. Under the negative arm (an address in an
   existing bucket): the cache moves there (`--refresh` writes + reads back), `cache_path()` reads it, `ENV_CACHE`
   stays the test override, and the `~21` literal goes.
5. **Tests stay green and grow:** `lib/research/identity/tests/test_union_universe.py` (its fixture at :30
   already passes a document directly to `filing_identity_for()`) gains an arm that `load_sec_cache()` refuses
   loudly on an absent object and honours the local override; `lib/research/peers/tests/test_peers.py` gains
   the arm AC4 exercises (a stale cache file is NOT rewritten by a load).

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c (round-14 block), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis s.2 (:55-61),
s.3.6 (:98, W32-S4 RULED here), s.4 row R14-H1 (:123) @`9c8e04cd9a`; PRD v0.13 @`1699960261` s.10:
`C-PRODUCTION-HOME` :1643-1650 (and `C-UNIT-MAP-MEASURED`'s pointer at :855), `C-VALIDATION-NAMES` :1652-1658;
the validation @`b527b93214` D1 :174-176, D5 :185-186, D7 :189-190, D24 :230-232, the limit note :19-22;
CLAUDE.md Rule 30 and `infra/logic/02_DOCTRINE.md` v1.1 (R1, R4, R9, R20; N1 :205-224; s.6 :589-591).

**ISSUER AMENDMENT -- THE REGISTRY GATE (`2.0.0_SA_COO~Z`, 2026-09-18 ~21:3xZ, on Andrew's words relayed by
`1.0.0_SA_CTO~Z` msg 23778):** Andrew, VERBATIM: *"Yeah i hope its clear and foundational in all associated AMGT_RESAPP art
that the opal-data-harvest bucket is the designated folder for all RESAPP data content/pipelines"* and *"then it has to be
structured in said bucket in proper form"*. So: EVERY AMGT_RESAPP byte this order lands -- bronze raw included -- lands in
`opal-data-harvest`, at an address PRINTED BY `lib/opal_naming.py address()`, never typed. MEASURED at the cut: the registry
(`infra/logic/registry/tiers.json:27`) still homes bronze/silver in the shared `opal-data-assets`; the two registry rows that
re-home this project (the home registration + the R20 departure entry) are being placed by `0.0.0_AB_MSTR~Z` on the laptop
fabric and land here by merge. THE RULE, replacing every literal bucket in this order: before ANY live write at a builder
address, print the builder's output for the address the order names with the scope token `harvest` (the L4 RULING,
`1.0.0_SA_CTO~Z` @2560e04f46: vendor bronze is `<vendor>/harvest/bronze/<table>/<partition>/<object>`, our own derivations
`amgt/harvest/<tier>/<table>/...`; NO `global` route and NO `amgt` scope row -- a scope spelled `amgt` is refused by the
builder, and `global` is not this project's route; where this order's older text says `global`, read `harvest`); the naming gate at commit is ENFORCING and its grader is WIDER than the builder, so a
hand-typed key can pass the commit and resolve nowhere -- never type one); the live
arm is LIVE iff that address's bucket is `opal-data-harvest`. If the builder REFUSES or returns any other bucket, DO NOT
WRITE THERE: the offline, read-only and dry-run criteria run in full; each live criterion is recorded with the builder's
printed line as its output and the verdict REFUSED-BY-REGISTRY; ONE surprise row carries it (`spec_asserts`: Andrew's words
above and CTO msg 23778; `world_is`: the builder's exact output at spawn), and the worker keeps working. A write to
`opal-data-assets` of any AMGT_RESAPP object is NOT AUTHORIZED by this order under any branch. Where this order's text below
reads `s3://opal-data-harvest/...` for a builder address, that is the EXPECTED bucket once the rows land, and the address is
still read from the builder's print, never from this text.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/field_map.json
lib/research/identity/build_universe.py
lib/research/identity/tests/test_union_universe.py
lib/research/peers/universe.py
lib/research/peers/tests/test_peers.py
infra/aws/terraform/modules/opal_name/tests/vectors.json
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~37/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-33.production-home.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (`lib/opal_naming.py`, the registry's
  other files, `tiers.json`, `scopes.json`, `engine.py`, the worker folders ~1/~19/~21 you copy FROM). The two
  `opal_name/tests/` files are GENERATED: regenerate only, never hand-edit (the naming gate refuses a hand edit,
  `.tools/naming-gate.py:775-797`). `infra/logic/registry/` is lane PLATFORM_LOGIC_DOCS and `infra/aws/**` is
  CLOUD_OPS_OR_ETL: your grant is this `<paths>` block; if the commit gate REFUSES either path, do not force it --
  file a row naming the refused path and the exact row/regeneration owed, and the SEC half then reads the pool
  only once the row lands (the loader refuses loudly meanwhile; nothing falls back to `~19`).
- **NOT your write:** `filing_identity_for()`'s body (rk-32); `engine.py` and everything else under `peers/`
  except `universe.py` (chain P); `model_block_pull.py`'s `SECURITIES`/`HIST_END`/field lists (chain M);
  `MODEL_BLOCK_DIR_DEFAULT` :68-72 and the model-block half of `build_candidate_universe()` :417-423 (the same
  class -- it goes in AC6's census and your row, not in your diff); the coverage list's worker-folder home
  (`build_universe.py:79-81` OUTPUT_PATH, `crosswalk.py:71-74`, validation D2) -- same treatment.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~37 <0.9.0_WK_AMGT_RESAPP~37@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Every `.py` passes `.tools/commit-gate.sh`. Never push, merge,
  rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or
freshness checker** (the WARN line in RULED 4 is a print on a read path, not a checker). Secrets through
`comp-secrets` only. No non-ASCII in anything you write. **PUSH: never.** LD-0522 puts the push with
`0.0.0_AB_MSTR~Z`. **NO VENDOR CALL of any kind** -- no Bloomberg, no sec.gov GET (that is `AMGT-rk-32`'s), no
web; this order moves bytes that already exist and edits readers. **NO FLEET RUN, NO RE-RUN**; no producer is
run (`model_block_pull.py pull/derive` is never invoked; `engine.py --write-pool` never). **A dry run writes
nothing, anywhere** -- AC4 plants the stale-cache negative that used to write.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name -- and a builder refusal is NEVER
answered with a typed address.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** (the census in AC6 is the
denominator the CTO's next L4 reads; print every hit).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W37-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import importlib.util, os
spec = importlib.util.spec_from_file_location('opal_naming', os.path.join('lib', 'opal_naming.py')); nm = importlib.util.module_from_spec(spec); spec.loader.exec_module(nm)
for args in (('sec', 'harvest', 'bronze', 'company_tickers', 'date=2026-09-15'), ('amgt', 'harvest', 'gold', 'candidate_universe', 'date=2026-08-06')):
    try: print('ADDRESS', args, '->', nm.address(*args))
    except Exception as exc: print('REFUSED', args, '->', type(exc).__name__, str(exc))
refusals, warnings = nm.validate(); print('validate_refusals', len(refusals), 'warnings', len(warnings))
"</invocation><expect>ONE RUN at spawn, both lines PRINTED BY THE BUILDER and recorded verbatim (measured by the issuer on HEAD e44380a9d1, 2026-09-18 23:3xZ, after the registry rows landed): line 1 ADDRESS ... s3://opal-data-assets/sec/harvest/bronze/company_tickers/date=2026-09-15 -- BUILT, and its bucket reads opal-data-assets, so under the REGISTRY GATE the SEC table's live write is DEAD (REFUSED-BY-REGISTRY; the dry-run half, the row and the code that calls the builder are the cell; NOTHING is written to opal-data-assets); line 2 ADDRESS ... s3://opal-data-harvest/amgt/harvest/gold/candidate_universe/date=2026-08-06 -- BUILT into opal-data-harvest, so the gold move's arm is LIVE (AC5's negative arm fires: the cache moves there with the --refresh receipt and read-back); validate_refusals 0. If line 1 prints an opal-data-harvest bucket at spawn (the tenancy shape landed), the SEC arm is LIVE too and AC2 runs its landing; if either line REFUSES, record the builder's text and file the row -- never a typed address</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import hashlib, json, sys
from pathlib import Path
old = Path('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json').read_bytes()
new = Path('integrations/bloomberg/research/field_map.json').read_bytes()
print('old_sha', hashlib.sha256(old).hexdigest()[:16], 'new_sha', hashlib.sha256(new).hexdigest()[:16], 'byte_identical', old == new, 'fields', len(json.loads(new)['fields']), 'securities', len(json.loads(new)['securities']))
src = Path('integrations/bloomberg/research/model_block_pull.py').read_text(encoding='utf-8').split('\n')
print('worker_folder_literals_in_model_block_pull', [i + 1 for i, l in enumerate(src) if '0.9.0_WK_AMGT_RESAPP~' in l])
sys.path.insert(0, 'integrations/bloomberg/research'); import model_block_pull as m
print('field_map_path', m._FIELD_MAP_PATH, 'exists', m._FIELD_MAP_PATH.exists(), 'beside_producer', m._FIELD_MAP_PATH.parent == Path(m.__file__).resolve().parent)
print('unit CAPITAL_EXPEND SAP', m._resolved_unit('CAPITAL_EXPEND', 'SAP GY Equity'), '| sign BOOK_VAL_PER_SH BA', m._resolved_sign('BOOK_VAL_PER_SH', 'BA US Equity', -0.3772))
"</invocation><expect>byte_identical True with 36 fields and 3 securities (the map MOVES, it is not rebuilt -- rk-34 rebuilds it for every name at THIS path); worker_folder_literals_in_model_block_pull [] (the :286-288 read AND the :464-467 pull-log write both retired; the :49 comment naming select_securities.py may stay only if it is a comment -- print the list either way); field_map_path resolves beside the producer with exists True; the unit for CAPITAL_EXPEND on SAP reads MILLIONS and the sign for BOOK_VAL_PER_SH on BA reads NEGATIVE -- the same MEASURED values the worker-folder copy served (field_map.json:12-16, :48), read from the new home</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, hashlib
from lib.research.identity import build_universe as bu
addr = bu.sec_table_address('2026-09-15', 'sec_ticker_cik_cache.json'); print('address', addr)
bucket, key = addr[5:].split('/', 1)
s3 = boto3.client('s3', region_name='us-east-1')
head = s3.head_object(Bucket=bucket, Key=key); body = s3.get_object(Bucket=bucket, Key=key)['Body'].read()
old = open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/sec_ticker_cik_cache.json', 'rb').read()
print('ContentLength', head['ContentLength'], 'metadata', head.get('Metadata'), 'pool_sha', hashlib.sha256(body).hexdigest()[:16], 'repo_sha', hashlib.sha256(old).hexdigest()[:16], 'byte_identical', body == old)
cache = bu.load_sec_cache()
print('loader_object', cache['ticker_to_cik_table'].get('object'), 'rows', len(cache.get('rows') or {}), 'denominator_claimed', cache['ticker_to_cik_table'].get('row_denominator'), 'submissions_ciks', len((cache.get('submissions') or {}).get('by_cik') or {}))
print('SEC_CACHE_DEFAULT_present', hasattr(bu, 'SEC_CACHE_DEFAULT'), 'prefix', bu.sec_table_prefix())
src = open('lib/research/identity/build_universe.py', encoding='utf-8').read().split('\n')
print('tilde19_literals', [i + 1 for i, l in enumerate(src) if '0.9.0_WK_AMGT_RESAPP~19' in l], 'all_worker_literals', [i + 1 for i, l in enumerate(src) if '0.9.0_WK_AMGT_RESAPP~' in l])
"</invocation><expect>address printed from the builder (s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=2026-09-15/sec_ticker_cik_cache.json); the object exists with metadata document-sha256 and byte_identical True against the ~19 file (a MOVE of the existing document, sha256 printed both sides); load_sec_cache() reads it from the pool (loader_object == the address; rows 33, denominator_claimed 10422, submissions_ciks 15 -- unchanged semantics, the honest read is rk-32's); SEC_CACHE_DEFAULT_present False; tilde19_literals []; all_worker_literals lists only the coverage list's own lines (:56 docstring, :79-81 OUTPUT_PATH -- D2, not this order's), printed</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import hashlib, json, os, subprocess
from lib.research.peers import universe as u
src = json.load(open(u.cache_path(), encoding='utf-8')); src.pop('preset_value_codes', None)
os.makedirs('.scratch', exist_ok=True); p = os.path.abspath('.scratch/stale_candidate_universe.json')
open(p, 'w', encoding='utf-8').write(json.dumps(src, sort_keys=True))
before = hashlib.sha256(open(p, 'rb').read()).hexdigest(); mtime = os.path.getmtime(p)
os.environ[u.ENV_CACHE] = p
doc = u.load_candidate_universe()
after = hashlib.sha256(open(p, 'rb').read()).hexdigest()
print('stale_copy', p, 'rebuilt_in_memory', bool(doc.get('preset_value_codes')), 'database', doc['denominators'].get('database'), 'files_read', doc['denominators'].get('files_read'), 'of', doc['denominators'].get('files_expected'))
print('stale_file_unchanged', before == after and mtime == os.path.getmtime(p), 'cache_sha256_written', 'cache_sha256' in doc)
print(subprocess.run(['git', 'status', '--porcelain', '--', 'org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/'], capture_output=True, text=True).stdout or 'GIT CLEAN under ~21')
"</invocation><expect>THE PLANTED NEGATIVE, run BEFORE and AFTER the fix and both recorded: before, stale_file_unchanged False (the load rewrote the stale copy -- validation D24, universe.py:578-580); after, rebuilt_in_memory True with database and files_read N of 6 printed (the six scanner files are read, the fold happens in memory), stale_file_unchanged True, cache_sha256_written False, and GIT CLEAN under ~21 -- a READ never writes; the only writer is `python -m lib.research.peers.universe --refresh`</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.peers import universe as u
try:
    addr = u.candidate_universe_address('2026-08-06'); print('ADDRESS', addr)
    import boto3; b = addr[5:].split('/', 1)[0]
    try: boto3.client('s3', region_name='us-east-1').head_bucket(Bucket=b); print('bucket_exists', b, True)
    except Exception as exc: print('bucket_exists', b, False, type(exc).__name__)
except Exception as exc:
    print('REFUSED', type(exc).__name__, str(exc))
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf): u.load_candidate_universe()
warns = [l for l in buf.getvalue().split('\n') if 'C-PRODUCTION-HOME' in l]; print('warn_lines', len(warns), warns[:1])
text = open('org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md', encoding='utf-8').read()
print('rows_W37', sorted(set(__import__('re').findall(r'AMGT_RESAPP-Z-W37-S[0-9]+', text))))
"</invocation><expect>EITHER: REFUSED with the builder's own text (the `amgt` scope row, Andrew's call -- 02_DOCTRINE.md:589-591), warn_lines 1 naming C-PRODUCTION-HOME and the row id, and rows_W37 listing that row (it carries the refusal verbatim, the row it names, the address the builder would give and head_bucket's answer); OR, the negative arm, ADDRESS ... with bucket_exists True, warn_lines 0, and the cache moved there (the --refresh receipt with read-back in the instance, cache_path() reading the pool, the ~21 literal gone). Never a typed address, never opal-data-harvest by hand</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import os
hits = []
for root, dirs, files in os.walk('.'):
    r = root.replace(os.sep, '/')
    if any(s in r for s in ('/.git', '/org/', '/node_modules', '/.scratch', '/portal', '/tests', '/.runtmp', '/data/')): dirs[:] = []; continue
    for f in files:
        if not f.endswith('.py'): continue
        p = os.path.join(root, f).replace(os.sep, '/')[2:]
        try: lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
        except OSError: continue
        hits += [(p, i, l.strip()[:90]) for i, l in enumerate(lines, 1) if '0.9.0_WK_AMGT_RESAPP~' in l]
print('production_py_lines_naming_a_worker_folder', len(hits))
for h in hits: print(h)
"</invocation><expect>THE CENSUS (the denominator the CTO's next L4 reads): every remaining production line naming a worker folder printed with file:line; the three lines the PRD names (model_block_pull.py:286-288, build_universe.py:450-453 with :503-507's read, peers/universe.py:81-86) are ABSENT from the list; the remainder measured at the cut (crosswalk.py:72, build_universe.py:56/:80, peers/universe.py:19/:68-72, price_axis_pull.py:24, model_block_pull.py:49, chatter_axis.py:138, harvest/lambda_src/build_zip.py:91, social/collect.py:256, posture/packs.py:13, freshness/build_view.py:67, coverage_pass.py:58-60 -- re-measure) is listed in ONE row AMGT_RESAPP-Z-W37-S<k> as the class's residue, not edited here</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-33"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest discover -s lib/research/identity/tests -p "test_*.py" -q 2>&1 | tail -3 && python -m unittest discover -s lib/research/peers/tests -p "test_*.py" -q 2>&1 | tail -3 && python lib/opal_naming.py validate 2>&1 | tail -3 && python lib/opal_naming.py generate --out .scratch/gen --target infra/aws/terraform/modules/opal_name/tests/vectors.json --target infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl 2>&1 | tail -3 && python -c "
from pathlib import Path
for t in ('infra/aws/terraform/modules/opal_name/tests/vectors.json', 'infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl'):
    a = Path(t).read_bytes(); b = Path('.scratch/gen', t).read_bytes(); print(t, 'tree_equals_generator', a == b, 'bytes', len(a))
"</invocation><expect>both unit suites OK (counts printed, 0 failures, 0 errors -- including the new arms of RULED 5); validate prints VALIDATE: OK with the `sec` VENDOR row in place; the generator's fresh output for the two GENERATED files equals the tree byte-for-byte (tree_equals_generator True for both -- the marks moved with systems.json and nothing else changed) ISSUER REPAIR (2.0.0_SA_COO~Z, on rows W37-S4 and W37-S1): the `harvest` scope row landed @e44380a9d1 BEFORE the `etfs` row and shifted the generated `refuses_product_scope` vector (etfs -> harvest) -- a registry-induced drift the registry commit did not regenerate. Running `python lib/opal_naming.py generate` and committing BOTH generated files is the SANCTIONED regeneration (the naming gate accepts generator output; a hand edit is what it refuses): do it, and AC7 is met when `tree_equals_generator True` for both files after your regenerate with the diff against HEAD confined to the mark line plus that one vector's scope token; STOP with a row only on any OTHER difference. And on AC3: a live criterion recorded REFUSED-BY-REGISTRY with the builder's printed line (the REGISTRY GATE amendment) is the designed branch, not a FAIL -- it does NOT hold this order open; the order flips complete when every other mechanical criterion passes, and L9 grades the refusal as recorded</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. AC1 and AC4 are each run TWICE (before and after) and both runs are recorded -- the before run is the
discriminator.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~37/AMGT_RESAPP.TO-AMGT-rk-33.production-home.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once, and name in the report: the config path
(`integrations/bloomberg/research/field_map.json`), the SEC address the builder returned, the `sec` row's
commit, the peer-universe outcome (row id or address), and AC6's census count. `AMGT-rk-32` starts only after
this report.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~37</slot>
<fabric>site-z</fabric>
