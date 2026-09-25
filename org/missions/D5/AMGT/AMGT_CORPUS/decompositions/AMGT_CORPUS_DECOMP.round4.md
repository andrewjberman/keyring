# AMGT_CORPUS -- L5 decomposition v4.0 -- ROUND 4 (the enrichment round after the round-3 analysis)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-25 ~03:0xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-3 analysis
`ledger/ROUND_ANALYSIS.round3.md` @`eaed38bac0` section 7 (the recut list) and sections 2-3 (its two rulings). Round 3's
decomposition is kept as `AMGT_CORPUS_DECOMP.round3.md`. PRD v0.6 @`031c3a3a3e`, both halves SIGNED current.

## 0. What this round IS, by subtraction from the analysis's list

Section 7 lists five items; this round cuts all five:
1. the denominators / universe-pin DISCLOSURE rebuild (section 2's ruling) -> cell `CRPS-f-1`;
2. the FWD-12 history request (`Z-S29`) -> cell `CRPS-f-2`, which states what it tests: the DROPPED ERROR is MEASURED (the
   client's handler returns on any message without `securityData`); the per-request FIELD LIMIT is INFERRED, and the cell's
   split guards against it without claiming to have measured it -- the drain's first batch measures it;
3. the dossier sequence blocked at extract (`Z-S30`) -> cell `CRPS-f-3`;
4. ONE JUDGMENT criterion (section 3) -> `CRPS-f-2` AC4, graded at L9 by `3.0.0_SA_CVO~Z` on the drain's real run;
5. the verify-leg CONTENT rule (section 6) -> every drain verify leg in section 5 names what it reads INSIDE the object and
   prints present-but-empty beside present.
Nothing else is cut. The goal clause still open is the backfill (section 8): FWD-12 and FWD-19.

## 1. The rectangle -- three cells `CRPS-f-<n>`, cut by WRITE SET (no two cells write one file)

| cell | serves (FWD) | `<risk>` | class | write set (`<paths>`, disjoint) | the build |
|---|---|---|---|---|---|
| `CRPS-f-1` | FWD-19 (the completion test's denominator, section 2) | SERVED (the drain's one re-mint moves the served pool) | worker | `lib/research/identity/crosswalk.py`, `lib/research/identity/add_security.py`, `lib/research/identity/tests/test_crosswalk_disclosure.py` (new) | the served document discloses the denominator it carries: `denominators.folders_in_records` (distinct `source_row.folder`) and `denominators.research_folders_live` (the live research directory's folder count at build time, with its root and read time) join the block; `coverage_vintage` gains `snapshot_stale_against_live` (bool) so the 89 reads as the SNAPSHOT it is; a new `research_universe` block names the live directory as the universe of record. No record, key or form changes. |
| `CRPS-f-2` | FWD-12 (the 22 mnemonics' figures) | WORLD (the drain's pull leaves Opal infrastructure: Bloomberg) | worker | `integrations/bloomberg/research/model_block_pull.py`, `integrations/bloomberg/mcp/blp_client.py`, `integrations/bloomberg/research/tests/test_hist_request_chunks.py` (new) | the historical request is split into requests of at most 25 fields and the rows merged by (security, date) into today's raw shape; `blp_client.historical_data` gains `on_response_error` (default `"ignore"`, byte-identical behaviour for every other caller; `"raise"` raises on a `responseError` message) and the puller passes `"raise"`. |
| `CRPS-f-3` | FWD-19 (the extraction half, `Z-S30`) | LOCAL | worker-light | `lib/research/corpus/extract.py`, `lib/research/corpus/typed.py`, `lib/research/corpus/tests/test_duplicate_content.py` (new) | ONE extract and ONE typed row per `report_id`: the canonical object is the lexicographically FIRST bronze key of that report_id; every other object under the same report_id is skipped in both stages with a printed `duplicate-content <report_id> <canonical> <skipped>` line; a read-only `--duplicates` flag on `extract` lists them. The body stays a function of its key. |

## 1a. Re-groundings performed at L5 (CLOUD HEAD at the cut)

- **f-1:** `crosswalk.py:833` sets `input_names = len(entries)` from the coverage document (`coverage_path()`, the 2026-09-10
  snapshot, 89 names); `:857-862` copies `coverage_vintage.denominator_folders` from the same file; `:869` pins
  `identity_universe` to the universe/v1 input. The served `crosswalk/v1/2026-09-25.json` carries 235 records over 94 distinct
  folders (this seat's census 01:5xZ; `1.0.0_SA_CTO~Z` and `3.0.0_SA_CVO~Z` independently). The live directory lists 94.
- **f-2:** `HIST_FIELDS` is 39 at HEAD and was 23 before `bb6b1f2f25`; `blp_client.historical_data`'s `handle()` returns early
  when a message lacks `securityData`, so a `responseError` is never read. Measured: 22 batches, every histdata `{}`, refdata and
  bestdata with content (`Z-S29`).
- **f-3:** across the corpus, 354 bronze research-report objects under 353 report_ids; exactly ONE report_id carries two files
  (`CPA_US_Equity/ff0e11955cb266f4`: `... Investor Day Presentation (1).pdf` and `... Presentation.pdf`). The stored extract was
  written from the sorted-first key, so the canonical rule re-runs clean against it. Readers of an extract's `bronze_key`:
  `typed.py:439`, `report_input.py:73` (compares it to the typed row's key), so the field STAYS and typed collapses the same way.

## 2. Rule 24 four-postulate record, for what this file ADDS

The only schema this file adds is f-1's three disclosure fields and f-3's `duplicate-content` line.
(i) MECE: `folders_in_records` and `research_folders_live` are two different populations (the object's rows; the live
directory) and each names its source; `snapshot_stale_against_live` is their comparison against the snapshot's 89, never a
third count. (ii) Same grain: folders, all three. (iii) One intent: disclosure. (iv) State coherence: no record, key, form or
resolution moves -- the remedy moves only what the object SAYS about itself.

## 3. Placement axis

f-1 on the identity builder (the surface `2.0.0_SA_COO~Z` has closed four limbs on this week -- that seat is told the cell
holds `crosswalk.py` and `add_security.py` until it drains). f-2 on the Bloomberg lane's two files, granted by `<paths>` for
this order only, as round 3's e-2 was. f-3 on this project's corpus package.

## 4. Dependency edges, keyed to OBSERVED completion

- f-1, f-2, f-3 are independent at build time (disjoint write sets, no read dependency).
- f-1 -> the drain's re-mint (a fresh never-widen pair; the put is the disclosure landing).
- f-2 -> the drain's pull + derive (change-management entry; derive under pair COO `2a3319e5ae` / CTO `35e4cb93ef`).
- f-3 -> the drain's production sequence; the dossier step runs AFTER the derive so the Model rows carry the figures.

## 5. The round -- one issuance, fan-out as data

- **ONE issuance covers all 3 cells.** Three worker slots: `~1` f-1, `~2` f-2, `~3` f-3 (worker-light).
  `fanout: 3 of 3 chains, cap 8, reason: three independent cells, no shared file.`
- **Drain duties owed by this seat, in order, each verify leg reading CONTENT (analysis s.6):**
  1. At every merge: the package suites, `py_compile`, ruff, beside `safe-merge.sh`'s row gate.
  2. f-2 VALID: READ_HERE s.2 + `bloomberg_health`; a change-management entry; ONE probe batch of 3 first, whose raw histdata is
     READ for rows (`rows > 0` per key, printed beside `objects present`) before the other 29 batches run; then the pull over the
     89 keys (Bloomberg identifiers, spaces), then `derive`; verify: per key FY rows > 0 and figures > 0 in the newest block,
     printed as `present / non-empty / empty` counts; the SA-fallback-fired count beside 89 (the CTO's owed figure).
  3. f-1 VALID: the re-mint pair (COO half + CTO half, before-state re-measured), ONE build + put of today's crosswalk key; verify:
     `folders_in_records` equals the distinct-folder count this seat computes from the records, and equals `research_folders_live`.
  4. f-3 VALID and item 2 done: `ingest --write`, then `production_sequence --run` with no 2 h ceiling; verify: extract prints the
     one `duplicate-content` line and no refusal; dossiers present for the 94 folders' resolved keys, each read for non-empty
     Model rows where a block has figures.
  5. The COO's one real run of each outcome at close, and the JUDGMENT evidence for f-2 AC4 laid out for the CVO.
- The surprise channel is `org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md` (seat rows to
  `Z-S31`; workers mint `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner 2.0.0_SA_COO~X`).

## 6. `<preflight>` -- what this decomposition actually ran

```
prd-signoff.py status AMGT_CORPUS        v0.6 @031c3a3a3e; ratified-text SIGNED current (3.0.0_SA_CVO~Z); brief SIGNED current (4.0.0_SA_CRO~Z); ADMITTED
sequence-check.py --project AMGT_CORPUS  FLAGS none (denominator 0 projects)
task-order status census (last <status>)  22 of 22 terminal on this project -> 0 open
comp-schedule --drift                    2 armed (G-3 CTO, G-7 POD4), 0 on these surfaces (C1=23 C2=5 C3=12 C4=21 C5=334)
comp-iam                                 NOT re-run this cut; the only S3 writes are the drain's, under their pairs
corpus duplicate census (boto3, read)    354 objects / 353 report_ids / 1 duplicate (CPA)
checks as files                          org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/*.sh, each run once at the base
```

## 7. comp-adversary declaration

This file specifies; it produces no artifact. The adversary lens applies at the drain to its three world-facing acts (the pull,
the derive, the re-mint), each under its own control in section 5.

## 8. Rulings this decomposition makes, and what it REFUSES to assume

- **f-1's reading of "re-pin identity_universe to the live research directory" is this seat's and the CTO may correct it:** the
  identity universe file stays the builder's IDENTITY INPUT (its 250 names feed resolution); the DENOMINATOR of record becomes the
  live directory, disclosed in `research_universe` and `denominators.research_folders_live`. A DATA change (rebuilding coverage
  records from the live listing) is not cut: the contents are already correct (analysis s.2, "a DISCLOSURE fix, not a data fix").
- f-2's split size of 25 is the INFERRED limit; the drain's probe batch is its measurement, and a probe that still returns `{}`
  stops the pull and becomes a row, never a guess at a smaller size.
- REFUSED to assume: that a raw object's presence is its content (Z-S26); that a dry run proves a vendor request is accepted
  (Z-S29); that a peer's uncommitted edit is the code under test (the pre-flight lesson).

## 9. Holds, and whose they are

| hold | on | owner | what lifts it |
|---|---|---|---|
| the FWD-12 pull + derive | this lane's drain | `2.0.0_SA_COO~X` | f-2 VALID; the entry; the probe batch reads rows > 0 |
| the re-mint | this lane's drain | `2.0.0_SA_COO~X`, under a fresh pair | f-1 VALID; before-state re-measured |
| the production sequence | this lane's drain | `2.0.0_SA_COO~X` | f-3 VALID and the derive done |

-- `2.0.0_SA_COO~X`
