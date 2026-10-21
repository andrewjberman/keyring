# NFRA_MCPINDEX -- decomposition addendum, ROUND 28, workstream GATEWAY (2.0.0_SA_COO~MI)

**archetype:** COORDINATE

Companion to `NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md`. One issuer, one round, ONE issuance (workstream GATEWAY, round 28). Spec-frozen once issued.

Source: PRD v0.20 FWD-26 (SIGNED and ADMITTED by `3.0.0_SA_CVO~Z`, review @a81f56eb3e; CTO relay msg 36309), the CTO's round-27 analysis `ledger/ROUND_ANALYSIS.round27.md` @f5f824c16e (msg 36317) and the ruling on the size thresholds (msg 36313, @03aed790203). FWD-26: for a plain-words question about Schwab, Orion or Cottonwood Black Diamond, Claude picks the right folder and table from the index without listing the bucket first; every indexed table carries its folder, its plain-words meaning and a size class (small / large / very large, from measured rows and bytes per partition); no per-dataset typed tools are built. FWD-26 grades the folder and table picks, not tools, so it does not wait on NFRA_OPLGTW FWD-23's tool names.

Rulings in force: the size class thresholds are small = under 8 MiB and under 1,000,000 rows (uncompressed total of the newest partition; listed bytes for json and other formats), large = 8 MiB up to 24 MiB, very large = 24 MiB or more, or 1,000,000 rows or more (234 / 15 / 32 on the census of 2026-10-21); the 24 MiB line rests on one observation (a factor of 2.63) and moves if NFRA_OPLGTW FWD-23 proof (e) shows a different factor; the index states the class and refuses nothing (the engine's ceilings refuse); the question set is accepted with O3 passing only once candidate e is served. Nothing reaches the trunk catalog before the ledger of NFRA_OPLGTW release batch17 reads CLOSED (the release's check requires the tracked catalog to equal md5 03d2dbbae1f07b8d4fa5f0eaa73355d6).

Nothing in this round touches the gateway, a grant, the trunk catalog, `members.yaml`, or sends anything. Every worker cell edits one script and its tests; the real emit, the placement and the grading run are the issuer's drain acts after batch17 (R28.4).

## R28.1 INPUTS (read-only to workers)

- `deliverables/2.0.0_SA_COO~MI/round28/evidence/SIZE_CENSUS_20261021.json` (`size_census/1`: `entries[]` with `entity`, `section`, `bucket`, `prefix`, `retired`, `newest_partition`, `partitions`, `objects_in_newest`, `bytes_newest`, `bytes_largest_object`, `rows_newest`, `bytes_uncompressed_newest`, `rows_note`, `format`, `error`; `skipped[]`; `read_at`; `catalog_md5`), `SIZE_CLASS_PROPOSAL_20261021.md`, `FWD26_QUESTION_SET.json` (`fwd26_questions/1`).
- `workflows/atom_decomposition/emit_catalog_v02.py` and its tests, `workflows/gateway_battery/size_census.py`, `tool_battery.py` and their tests; the tracked catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (read-only; the emitter is NOT run into it by a worker).

## R28.2 THE CELLS (two independent chains)

| cell | analysis item | class | deliverable | slot |
|---|---|---|---|---|
| `MX-l-1` | 1 the size-class emitter with a measured claim | code | edit `workflows/atom_decomposition/emit_catalog_v02.py` + `tests/test_size_class.py` | ~97 |
| `MX-l-2` | 2 the question-set grader | code | NEW `workflows/gateway_battery/fwd26_grade.py` + `tests/test_fwd26_grade.py` | ~98 |

The three event-gated items (routing and battery on candidate e after batch17; the per-vendor re-run after OPLGTW's next round; the 24 MiB line re-measure on FWD-23 proof (e)) are carried as drain acts. Write sets are disjoint.

## R28.3 FROZEN CONTRACTS

**L1 SIZE-CLASS EMITTER.** `emit_catalog_v02.py` gains `--size-census FILE` (optional; absent = the existing output byte for byte). The file is a `size_census/1` document (shape in R28.1); a named file that does not exist, is not JSON, or has another schema exits 2 before anything is read or written. For every row of `silver_datasets`, `portal_datasets` and `harvest_datasets` the emitted row gains a `size:` mapping, placed after the row's existing fields:
- when the census has an entry for the row's (bucket, prefix) with no `error`: `size: {class: small|large|very large, claim: measured, measured_at: <the census read_at as YYYY-MM-DD>, newest_partition: <date>, rows: <rows_newest or null>, bytes: <bytes_uncompressed_newest when present, else bytes_newest>, basis: uncompressed|listed}`; the class is computed in the emitter by the ruled thresholds (constants in the emitter: 8 MiB = 8388608, 24 MiB = 25165824, 1000000 rows): `very large` when bytes >= 25165824 or rows >= 1000000, else `large` when bytes >= 8388608, else `small`; `basis` is `uncompressed` when `bytes_uncompressed_newest` is present, else `listed`;
- when the census has no usable entry (a census `skipped` item, an entry with `error`, or no entry): `size: {class: unmeasured, claim: absent, reason: <the census skipped reason, the error code, or "not in the census">}`.
Every other emitted field of every row, and the whole tool_index, is unchanged. The census `catalog_md5` is recorded once in the catalog header comment as `# size census: <read_at> over catalog <catalog_md5> (thresholds 8 MiB, 24 MiB, 1000000 rows)`. A row whose census entry names a prefix twice is an emit error (exit 2). `validate_claim` accepts the `claim: measured` form (a measured claim carries `measured_at`) and refuses `class` values outside the four. Two emits with the same inputs give the same bytes. The existing naming gate must pass on the new fields (they hold no firm token).

**L2 QUESTION-SET GRADER.** `python workflows/gateway_battery/fwd26_grade.py grade --questions FILE --picks FILE --out FILE [--served-md5 MD5]`. `--questions` is the `fwd26_questions/1` file (R28.1); `--picks` is `fwd26_picks/1`: `{"schema","run":{"principal":str,"read_at":str},"picks":[{"id","bucket","prefix","table","listed_bucket_first":bool}]}` (one pick per question id; the run records for each question the FIRST folder and table named from the index). Verdicts per question, in this precedence: `missing_pick` (no pick for the id) FAIL; `listed_first` (listed_bucket_first true) FAIL even when the folder is right; `s2_folder` (the prefix's last segment ends `_s2`) FAIL unless the question's expected location itself ends `_s2`; `wrong_folder` (the (bucket, prefix) is in neither `expected_locations` nor `accept_also`) FAIL; `wrong_table` (the pick's table differs from the table of the matched location, taken from the location's last prefix segment) FAIL; else PASS. When `--served-md5` is given and does not equal the questions file's `catalog_md5_read`, a question listed in `needs_candidate_e_served` that FAILs `wrong_folder` or `missing_pick` is graded `not_served` (a FAIL that names the cause) instead. The output `fwd26_grade/1` holds per-question `{id, verdict, class, matched}`, `counts` (`questions`, `pass`, `fail`, `not_served`, per class) and the questions' `size_classes_proposed` carried through. Stdout `FWD26 questions=Q pass=P fail=F not_served=N`; exit 0 iff `fail` and `not_served` are 0, 1 otherwise, 2 on an unreadable or malformed input (a pick for an unknown id, a duplicate id, a non-bool `listed_bucket_first`). A second subcommand `ideal --questions FILE --out FILE [--mutate none|listed|s2|wrong-folder|wrong-table|missing]` writes a picks file in which every pick equals the first expected location (the control); each `--mutate` mode then applies exactly one defect to exactly the first question so the grader's refusals can be planted. Same input, same bytes.

## R28.3a AMENDMENTS AT THE CUT (fork findings on the real emitter and census; each order's section 1 is the exact specification and wins where it differs)

- **L1:** a census entry is matched to a catalog row by ENTITY (the census holds two entities on one location, so (bucket, prefix) is not unique); the "names a prefix twice" emit error becomes "names an entity twice". The `size:` mapping is validated by a separate `validate_size` (a date-only `measured_at` is not the full UTC stamp `validate_claim` demands); `validate_claim` itself is unchanged.

## R28.4 THE ISSUER'S REAL RUN (not worker cells)

1. After the ledger of NFRA_OPLGTW batch17 reads CLOSED: re-run `size_census.py` live against the then-tracked catalog, `emit_catalog_v02.py --size-census` with the same maps and serves-map as candidate e, diff the new candidate against the placed catalog (expected diff: the `size:` mappings, the header line and the build head only), place it (audited lane override, as in rounds 24 to 26), and ask `2.0.0_SA_COO~O` to serve it in its next batched release. Whether `opal_discover` / `gateway_query_catalog` return the `size` field is app code and an ask to COO~O.
2. Grade the question set against the index (a run of Claude picking from the served index, no bucket listing) with `fwd26_grade.py`; record the verdicts.
3. Carried: routing and battery on candidate e once served; the per-vendor re-run after OPLGTW's next round; the 24 MiB line re-measure on FWD-23 proof (e).
4. `round-close-check --round 28`, then the L10 slug to `1.0.0_SA_CTO~Z`.

## R28.5 WHAT THIS CUT DOES NOT CLAIM

It does not change a grant or a tool, edit the trunk catalog, serve the catalog, or realize FWD-26 by itself. The FWD-26 grade needs the size field served and a graded run of the question set.
