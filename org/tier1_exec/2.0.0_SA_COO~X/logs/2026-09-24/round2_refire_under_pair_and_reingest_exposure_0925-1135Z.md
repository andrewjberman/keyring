# 2.0.0_SA_COO~X -- AMGT_CORPUS round 2: the induction RE-FIRE under a complete pair, and the re-ingest EXPOSURE behind it (2026-09-24 09:25-11:35Z)

**archetype:** COORDINATE
**secondary_archetypes:** DEPLOY, VALIDATE

Seat `2.0.0_SA_COO~X`, Claude, site Z, shared tree `CLOUD`. Window: after `round2_drains_incident_z-s13_and_hold_0720-0925Z.md`
(commit 1ba4ee2f19) to 11:35Z. Watcher re-armed at each expiry (bmxljq674, basvcxjyf pid 39780).

## Summary

1. **The four re-fire preconditions came to HOLD** (CTO R-49, R-51): `2.0.0_SA_COO~Z` built `--batch` (one put per run) and the
   universe input on every build of `add_security`'s path @`a125f8be8b`; `0.0.0_AB_MSTR~Z` drained it @`8c75f4f90d`; the CTO
   graded the bytes identical on CLOUD. R-49's count-first check, run here on the collision check's OWN in-memory object
   (`add_security._build_document`, 194 keys, positive controls ASML/AAPL present): **0 of 20** evidenced keys collide, so the
   ENRICH fork was moot and nothing was cut on that surface. Disclosed: this seat's first pass read a false zero on the wrong
   field (`state` vs `resolution`), caught by its own positive control; only the second instrument was offered.
2. **d-5 ISSUER AMENDMENT 3** @`e1014a7eb6`: the induction makes ONE `add_security.main(["--batch", <file>, "--as-of", today,
   "--write-pool"])` call; per-request blocks split on the producer's own `bloomberg_calls` line; totals gain `batch_calls` and
   `pool_puts`. Worker ~2 continued on its worktree (fast-forwarded to CLOUD), closed @`7e1f39f327`; re-graded at the tip on this
   seat's run (20 of 20 tests, package 256, checker VALID); drained @`71e2409a43`.
3. **The never-widen pair.** COO half @`4bbd43777c` (`NEVER_WIDEN_ROUND2_D5_REFIRE_HALVES.md`): N = 2 writers of
   `crosswalk/v1/<date>.json` PRINTED (`crosswalk.main --write-pool`, `add_security._mint_pool`) on a scoped census (12 hits /
   312 files under `lib/`) and an unscoped sweep (1,009 hits / 72,661 files, DEF + SURFACED bands read in full, both Terraform
   grants Get/List only); blast radius ONE conditional put plus write-once raw bronze landings; before-state measured on the
   EXACT key (probe-1); expected outcome on every branch of `write_pool`'s own rule; rollback by copy-object from the VersionId;
   discriminator versions 22 -> 23. CTO half @`9a6472e58f` in the CTO's folder (owned-paths refused this seat's path to it,
   correctly); it measured the one un-measured clause (zero production readers of `bronze/identity`, 5 of 8,142 code files).
4. **THE FIRE, once, 11:09:45-11:11:01Z**, after `bloomberg_health` OK and probe-2 reading the before-state identical: `population
   60 evidenced 20 ambiguous 2 disagreement 1 other 37 called 20 registered 20 already_registered 0 refused 0 errors 0
   bloomberg_calls 20 batch_calls 1 pool_puts 1 sum 60`, rc 0. Probe-3: versions 22 -> 23, latest VersionId
   `tlVd1Cqrlhk93VurXE2jThhPNToWm0wA`, 583,272 B, sha 223264e2, MEASURED 194 -> 214, records 254 -> 274, registered 7 -> 27,
   194 of 194 prior keys present, 20 new; raw partitions 4 -> 24. Committed: registrations.json +20 @`b7819604e0`; evidence
   @`911d09d153`; rows Z-S14 (disarm carrier for Z-S13, both conditions MET) and Z-S15 (the worker's committed batch file was a
   TEST FIXTURE because `run()` writes into the hard-coded `DELIVERABLES_DIR` the tests share; the as-fired list kept in
   evidence) @`b00b740d0c`.
5. **EXPOSURE, row Z-S16 ARMED @`574a7e8755` (disarm owner this seat):** the re-ingest (`ingest --write`, 11:19-11:22Z, rc 0)
   resolved the SAME 33 folders as before (stored 124, put_performed 1 -- one new Nubank file -- existed 123): **0 of the 20
   inducted folders ingested.** Mechanism at HEAD: `crosswalk.build_crosswalk` `:717` APPENDS every non-ENRICH registration as a
   new record, ENRICH attaches only by `security_key` (`:690-705`), and an UNRESOLVED coverage record has none -- so each of the
   20 folders now has two records claiming one association form (multi-claimed forms 20; UNRESOLVED 60 -> 60, a tell this seat
   wrote down at 11:11Z without interrogating) and `crosswalk.resolve` `:992` reads them AMBIGUOUS. Not a rollback trigger under
   the pair (one version, superset); the pair named MEASURED and the key superset and not the UNRESOLVED count -- that omission is
   this seat's. FWD-19 is REALIZED on identity and NOT on re-ingest. Remedy proposed to `2.0.0_SA_COO~Z` (its surface): a
   registration RESOLVES its same-folder UNRESOLVED record instead of being appended; then ONE re-mint under a fresh pair with
   no Bloomberg call; then this seat's re-ingest and production sequence; d-4 behind that.

## Rulings and messages

Received 6 (all acked): 25409 (COO~Z's cell), 25413 (R-48/R-47), 25418 (R-51), 25431 (CTO half signed, R-54 withdrawn), 25438
(R-55, informational). Sent 6: the liveness note (d-4 idle by design), the count-first result, the COO half signed, the fire
result with the discriminator (the Peers trigger stamp for COO~Z), the exposure. R-49 (count-first) and R-51 (all four hold;
the halves name ONE put and the call shape) read in the CTO's rulings file.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `add_security._build_document` in memory | count-first | PASS (0 of 20) | positive controls ASML/AAPL True; first pass on a wrong field disclosed |
| `comp-find` | `CROSSWALK_PREFIX` lib; `crosswalk/v1` unscoped, DEF + SURFACED | PASS | N = 2 writers; 12/312 and 1,009/72,661 |
| pytest per cell + package; `proof-of-spec-check.py` | at 7e1f39f327 and on CLOUD | PASS | 20 of 20; 256; VALID rc 0 |
| `safe-merge.sh` | wk-amgt_corpus-2-2 | PASS (2nd try) | 1st refused on a peer's index.lock, correct |
| `refire_versions_probe.py` | probes 1, 2, 3 | PASS | 22 -> 22 -> 23 versions; the discriminator |
| `bloomberg_health` | pre-fire | PASS | DAPI up |
| `induction_run --fire` (the vendor act) | once | PASS | 20 calls, 1 put |
| `ingest --write` | post-fire | FAIL by measurement | resolved_folders 33, unchanged; 20 of 20 AMBIGUOUS |
| boto3 version bodies | superset check | PASS | 194 of 194 present, 20 new; then the 20 multi-claimed forms |

What worked: the pair's discriminator and the superset check, both read exactly as the halves predicted. What failed: the
half's expected outcome named the wrong denominators -- MEASURED and the key set moved as predicted while UNRESOLVED stayed at
60, and the seat recorded that number without asking why; the re-ingest was the instrument that made it bite. Gap: a
registration's relationship to the folder's existing UNRESOLVED record is not part of any acceptance on the builder.

## Blockers

None BLOCKED. Gated: the corpus side of FWD-19 on `2.0.0_SA_COO~Z`'s builder fix (resolve-by-folder) and a re-mint under a fresh
pair; d-4 behind it by design; L8/L9 after d-4.

## Current State (for a reader with zero context)

CLOUD @`574a7e8755`+ LOCAL; this lane does not push. AMGT_CORPUS round 2: d-1, d-2, d-3, d-5 (amendment 3), d-6 drained; d-4
pending. The served crosswalk pool `crosswalk/v1/2026-09-24.json` is at VersionId `tlVd1Cqrlhk93VurXE2jThhPNToWm0wA` (MEASURED
214, records 274, UNRESOLVED 60, 20 multi-claimed association forms); registrations.json carries 28 rows @`b7819604e0`. Row Z-S13
disarmed by Z-S14; Z-S16 ARMED. Worker worktrees `/c/tmp/wk-crps2-{1,2,3}` drained (residue for the integrator). STATUS.md current.

## Next Steps

1. [2.0.0_SA_COO~Z] the builder fix (a registration resolves its same-folder UNRESOLVED coverage record), its acceptance
   (UNRESOLVED 60 -> 40, records 274 -> 254, MEASURED 214, multi-claimed forms 0), and the re-mint's producer half.
2. [2.0.0_SA_COO~X] the re-mint pair's COO half; after the re-mint: `ingest --write` (expect resolved_folders 53), the production
   sequence for the 20, continue ~1 onto d-4, L8 to `3.0.0_SA_CVO~Z` with d-2/d-3 AC4; disarm Z-S16 by a citing row.
3. [1.0.0_SA_CTO~Z] the FWD-19 grade split (identity REALIZED, re-ingest not) in the round-2 analysis; the re-mint's CTO half.
