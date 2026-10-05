# AMGT_HARVST task order -- `HVST-as-1` -- ROUND 46 CHAIN A (round-45 analysis ruling 1; CTO ruling @a142505a06): THE COLLECTION RUN'S UNIVERSE IS THE RANK'S 191 NAMES, EACH CARRYING THE DECLARED-SET JOIN KEY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-as-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~94</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched; the collector's recurring schedule stays disabled.
comp-iam: RUN at L5 -- LOCAL code, config and plants, plus ONE read of the pool universe object in S3. NO publisher request of any kind, NO collection run, NO upload, NO vendor call: the run itself is the issuer's act after this merges, under its own pair.
comp-adversary: RUN at L5 -- the adversary is a universe whose `security_key` is not the pool key (so the declared-set reader never matches a job), a resolution step that calls a publisher or vendor to find a symbol, a silently dropped name (the count is 191 or the cell has not landed), a broken pilot-securities path, or a dry run that touches the network.
</preflight>

## 0. THE CELL

**Why:** FWD-7's served chatter rank needs a NON-EMPTY declared publisher set.
`lib/research/metrics/chatter_axis.py` `publisher_universe_verdicts` admits a publisher only when its CONCLUDED jobs cover
EVERY key of the rank's universe, joining each job on `gold_security_key`. `lib/opal_data_harvest/worker.py:467` stamps
`gold_security_key` from the collector security's `security_key` field.

**What the collector runs today:** `lib/opal_data_harvest/__main__.py` `universe(config)` builds its securities from
`config.json` `universe_source` (RESAPP's 89-name `universe.json`) and `symbol_resolution_source`
(`SA_SYMBOLS_MERGED_89_20260927.json`). Each entry is `{key: "security-<hash>", company, ticker, aliases, sa_symbol, ...}`, with
NO `security_key`. So 0 of the rank's 191 names can ever match a job.

**The rank's universe:** `chatter_axis.read_universe_names()` reads the pool object `universe/v1/2026-09-16.json` (bucket
`opal-data-harvest`). It returns 191 names, each `{security_key, identity, identity_status: MEASURED, name, ticker,
resolution}`, out of 250 read (59 without an identifier are not ranked).

The CTO ruling's condition 1, verbatim in substance: resolve all 191 names to the collector's job keys (the same
`gold_security_key` the declared-set reader joins on) and print 191 of 191. A name that cannot be resolved is a STOP before the
run, named in a row.

## 1. THE BUILD (LOCAL; one pool read; no publisher or vendor request)

1. **Snapshot the rank universe into the repo:** write
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/rank_universe_20260916.json`. It holds the 191
   entries exactly as `read_universe_names()` returns them, plus the source key and its meta (`names_read`,
   `names_considered`, `denominators`).
2. **Resolve the search identities with NO vendor call**, and write
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/rank_universe_identity_20260916.json`.
   - Per name: `company` (the pool `name`, cleaned of any trailing ticker), `ticker` (pool), `aliases`, and `sa_symbol`.
   - Each value records its status (`MEASURED` / `DERIVED` / `UNRESOLVED`) and its evidence.
   - For `sa_symbol`, reuse the 89-name resolution file where the company matches. Otherwise derive it from the ticker only by a
     rule you state (for example, a US-listed ticker is its own SA symbol). Mark every derived value `DERIVED` and never guess
     silently.
   - Print the per-identity coverage over 191.
3. **Point the collector at the rank universe:** `config.json` `universe_source` and `symbol_resolution_source` point at the two
   files above. `universe(config)` reads that shape and gives every security `security_key` = the pool key, keeping
   `key`/`company`/`ticker`/`aliases`/`sa_symbol` for the publishers.
   - The pilot-securities path keeps working.
   - The denominator and unique-key check reads 191.
   - `backfill_driver` plans from the same `universe()`; if it reads the universe another way, make it read this one.
4. **A name lacking an identity a publisher needs to search** (for example, no `sa_symbol` for sa) is NOT dropped. List it per
   publisher in your report, and file ONE surprise row (class BLOCKING, disarm owner the issuer) naming those names. The issuer
   rules on it before the run.
5. **Plants** in `lib/opal_data_harvest/test_as1_rank_universe.py`, no network:
   - `universe(<shipped config>)` returns 191 securities, each `security_key` in the snapshot's keys, all distinct;
   - a security's `security_key` reaches `worker.run_job`'s result as `gold_security_key` (a stub publisher; no request);
   - `chatter_axis.publisher_universe_verdicts` over synthetic concluded jobs, one per security from `universe()`, reads
     UNIVERSE_SCOPE 191 of 191 for that publisher;
   - a mutant that omits `security_key` reads `PER_NAME_TRIALS_ONLY` or `NO_JOB`;
   - the pilot path is unchanged.
6. The collector suite stays green: `python -m pytest lib/opal_data_harvest -q`. Report the count.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r46-94`, branch `wk-AMGT_HARVST-94-r46a`, cut from CLOUD at the issuance commit
(sparse cone, decomposition section 50). Do not touch any `.runtime` directory. Do NOT run the collector, the driver without
`--dry-run`, or `upload-harvest`.

<paths>
lib/opal_data_harvest/__main__.py
lib/opal_data_harvest/config.json
lib/opal_data_harvest/backfill_driver.py
lib/opal_data_harvest/test_as1_rank_universe.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-as-1"><invocation>python -m pytest lib/opal_data_harvest/test_as1_rank_universe.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-as-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round46/checks/as-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-as-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round46/checks/as-1.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 prints the per-identity coverage beside the join-key count.
- AC3 runs the driver ONLY with `--dry-run`, and it must read NETWORK CALLS 0.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~94/AMGT_HARVST.TO-HVST-as-1.rank-universe-run-input.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-as-1.rank-universe-run-input`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-45 analysis @4f01f5ab8d ruling 1 and enrichment item 1; CTO ruling @a142505a06; decomposition section 59.
as-1b (the run) follows the merge under its own never-widen pair, and it opens a NEVER-2 entry before the first request.

**COMPLETE 2026-10-05 ~01:3xZ (issuer):**
- **Built and merged:** worker ~94 built @3a93a33849. The slot was re-seated to apply the Z-W94-S1 ruling, @e379f86719. Merged
  @dfd3ce3498 (12 files, dropped 0, foreign 0).
- **AC1 PASS:** 6 of 6.
- **AC2 PASS:** 191 of 191 rank names carry `security_key` = the pool key. sa_symbol is present for 191 of 191 (INFERRED 23,
  MEASURED 14, DERIVED 153, ISSUER 1).
- **AC3 PASS:** UNIVERSE 191, 955 PLAN lines, NETWORK CALLS 0.
- **Collector suite on CLOUD:** 647 passed, 3 skipped.
- **Ruling Z-W94-S1** (row Z-W94-S2):
  - TPG Inc = TPG (ISSUER);
  - the nine R2 symbols stand, because the pool keys are those US listings;
  - the 153 unprobed symbols are accepted, and the run is their probe.
- **Gate limb:** proof-of-spec-check graded the flip.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>46</round>
<slot>~94</slot>
<fabric>site-z</fabric>
