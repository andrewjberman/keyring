# TO NFRA_CLDGRPH.TO-CG-F-7 -- CG-s-27 (ADDED at decomposition v0.6 on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S27): THE MANIFEST CONTRACT -- `_provenance.write_manifest` ACCEPTS AND STAMPS THE CLAIM for every producer that calls it (`edge_count_semantics` stored/attempted, `artifact_claim`, `content_sha256`, `bytes_written_at`, so bytes newer than a manifest are DETECTABLE); `format_provenance_header` prints the claim beside the counts, keeps the `!!` prefix for any `source_kind` beginning UNKNOWN or a claim ABSENT, and reads a store whose bytes are newer than its manifest as such. S53's CONSUMING half; W3-S7, W3-S8, W3-S11

<to_id>NFRA_CLDGRPH.TO-CG-F-7</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~3</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-09</issued_date>
<status>complete -- 2026-09-09 by `0.9.0_WK_NFRA_CLDGRPH~3` (spine v3 L7, slot ~3 on branch wk-cldgrph-6-3, worktree C:/tmp/wk-cldgrph-6-3, HEAD at hand-off c6b16d8f04). Acts commit 987e920554; instance + this flip in the commit that cites it. PUSH STATE: LOCAL -- never pushed, never merged, never rebased. F7-AC1 PASS (13 passed / 13 collected, the seven arms (a)-(g)); F7-AC2 PASS (PRODUCERS_STAMPING=3 of 3, LEGACY_HELPER_SITES=0, PRODUCER_PROBE_CONTROL=FIRED, kuzu_load.py EXCLUDED and reported PRESENT); F7-AC3 PASS (five arms on real renders of format_provenance_header, plus a clean-before-rewrite negative control on the BYTES NEWER arm); F7-AC4 PASS-BY-OUTPUT (10 passed / 10 collected -- and NFRA_CLDGRPH-W3-S16 records that this criterion's OWN named control is DEAD, measured, with the engine-free substitute f7_signature_bind.py delivered in-grant: SITES_BINDING=3 of 3, STRIPPED_CALLER_REFUSED=3 of 3, BIND_CONTROL=FIRED); F7-AC5 UNVERIFIABLE-BY-INSTRUMENT, the reading recorded and NO verdict written -- graded by `3.0.0_SA_CVO` at L9. proof-of-spec-check.py: VALID (rc=0), 5 acceptance rows, 3 surprises all resolving to channel rows. THREE ROWS FILED (channel 152 -> 155): W3-S14 (the claim has no served render to reach -- no projection file, CLI or module in infra/aws/globgrph calls format_provenance_header at all), W3-S15 (2 of 81 tests in the ordered tests home RED from an empty portal submodule), W3-S16 (F7-AC4's dead control; OBSERVATION/ARMED, disarm_owner 0.8.0_AE_CloudComp). PREVIOUS: pending -- GO = the spawn (spine v3 L7): slot ~3 on a fresh worktree from CLOUD at this issuance. ROUND 6 of NFRA_CLDGRPH (the recut as ONE issuance on the CTO's round-5 analysis @30027295be / msg 94610). Slot ~3's ONLY order (independent by the CTO's ordering; S26 in slot ~2 retires `kuzu_stitch_load.py` LATER and that is not your concern -- edit its call site at your HEAD as the contract requires). The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.6 @`30027295be` (s.7 row S27; the CTO's S53 rule: a value must carry its claim in a field a consumer can reject on) · **Decomp cell:** `CG-s-27` · **Lane:** `0.8.0_AE_CloudComp` · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~3`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~3; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~3 <0.9.0_WK_NFRA_CLDGRPH~3@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/`.** Every script and capture carries `f7_` in its name (W3-S13: a slot folder reused across orders collided on generic names). Scratch: `<your worktree>/.scratch/`.
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` inside the fenced json array per `org/surprise_channel/schemas/investigation_item.schema.json`; id `NFRA_CLDGRPH-W3-S<k>`, `<k>` the next unused within W3 (W3-S1..S13 exist at HEAD; start at S14); restate the header denominator by parsing every fenced block (152 rows at this cut); never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`.** Every `.py` edit passes `bash .tools/commit-gate.sh <file>`. Non-ASCII in code is refused. The comp-system two-phase gate may fire on `org/modules/graph/` edits -- this order edits NONE there (its files are under `infra/aws/globgrph/`); if it fires anyway, take the override as the gate directs citing W2-S36 and say so in the report (the discharge belongs to the drain).
- **NEVER:** run any loader against a real store (`kuzu_nessie_load.py`, `kuzu_stitch_load.py`, `kuzu_load.py` if present); open a store with an engine (`kuzu.Database` CREATES an absent store; the contract is exercised on TEMP paths with FAKE store bytes -- a manifest is a JSON file beside a path, and the path's bytes may be any file); touch the MAIN workspace's stores or their manifests (F-1 and F-6 own them); edit `derive_runner.py`, `projection_worker.py`, `kuzu_incremental_refresh.py`'s logic beyond the ONE manifest call (F-4 in slot ~2 edits those files' derive/pin logic -- your edit is the kwargs at the `write_manifest` call, nothing else, so the drain's merge is textual); `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused; a `cmd | grep` receiver is free.

## THE CELL (decomposition v0.6, this recut, s.1a; PRD v0.6 s.7 row S27 verbatim in its accept)

> **CG-s-27** | S27 THE MANIFEST CONTRACT: `_provenance.write_manifest` accepts and stamps the claim for all four producers (`edge_count_semantics` stored/attempted, `content_sha256`, `bytes_written_at`, so bytes newer than a manifest are detectable); `format_provenance_header` prints the claim beside the counts and keeps the `!!` prefix for any `source_kind` beginning UNKNOWN or `provenance_claim: absent` | -- (S53's consuming half; W3-S7, W3-S8, W3-S11) | claim: measured (the field landed on ONE of four producers through a local helper; the served header for `kuzu_db` still reads '1166 nodes / 2488 edges' with nothing beside it (C-S27); an honest claim card beside a manifest-less store SILENCES the `!! UNKNOWN VINTAGE` branch (W3-S8)) | status: OPEN -- ROUND 6 (recut) | lane `0.8.0_AE_CloudComp` | placement laptop | verb fix | depends_on: -- | **closes on (the PRD's accept, verbatim):** one manifest of each producer read with the field; the rendered header shows the claim beside the counts; a manifest-less store still prints `!! UNKNOWN VINTAGE` (the negative arm); a store whose bytes are newer than its manifest reads so

## MEASURED BY THE ISSUER AT THE CUT (2026-09-09 ~17:5xZ, HEAD f3aa619432)

- **The writer:** `infra/aws/globgrph/_provenance.py:49-73 def write_manifest(db_path, *, source_kind, source_vintage, node_count, edge_count, edges_skipped_missing_endpoint=None)` writes `schema_version 1`, `source_kind`, `source_vintage`, `built_at`, `node_count`, `edge_count` (+ `edges_skipped_missing_endpoint`), atomically (`.tmp` + `os.replace`). NO claim field. `MANIFEST_SUFFIX`, `manifest_path()` `:44`, `read_manifest()` (find it), `DEFAULT_AGE_WARN_HOURS = 26.0` `:41`.
- **The reader:** `_provenance.py:560 def format_provenance_header(db_path, *, age_warn_hours, check_nessie_distance)`: the `!! REFRESH FAILED` / `!! SERVED LABELED-STALE` branches `:570-586`; `m = read_manifest(db_path)`; **`m is None` -> `!! UNKNOWN VINTAGE -- no _build_manifest.json beside this DB.` `:591-595`** (the negative arm the PRD keeps); then `kind`, `vintage`, `built_at` `:597-599` and the counts line (find it: the `'1166 nodes / 2488 edges'` shape C-S27 quotes) -- **the claim must print BESIDE that line**, e.g. `  counts: 1166 nodes / 2488 edges (edge_count_semantics=attempted; artifact_claim=historical)`, and a manifest WITHOUT the claim prints `  !! provenance_claim: absent -- counts carry no semantics (S53)` with the `!!` prefix, as does any `source_kind` beginning `UNKNOWN` (case-insensitive).
- **The four producers by `comp-find 'write_manifest\('` (9 hits / 961 files; 4 SURFACED call sites):** `kuzu_nessie_load.py:252` (`edge_count=edges_stored` -- STORED, S8), `kuzu_incremental_refresh.py:254` (`edge_count=re_` -- STORED, the post-apply count), `kuzu_stitch_load.py:153` (`edge_count=written` -- merge ATTEMPTS, then E-3's `_stamp_claim(mpath, edge_count_claim="merge_attempts", artifact_claim="interim_local_projection")` `:165-169`), `kuzu_load.py:305` (merge ATTEMPTS, S53's origin; E-3's `_stamp_claim` helper lives here and in `kuzu_stitch_load.py`). **`kuzu_load.py` is being RETIRED by TO-CG-F-1 in slot ~1 in this same round: it is OUTSIDE your grant; do not edit it; if it is still present at your HEAD, leave it and say so (the census reads 3 of 3 remaining producers).** The `_stamp_claim` helpers become dead once the writer stamps the claim: remove the one in `kuzu_stitch_load.py` (inside your grant) and call `write_manifest` with the kwargs instead.
- **The E-3 field names already on disk** (`edge_count_claim`, `artifact_claim` on the two main-workspace claim cards) are the LEGACY spelling; the CTO's row names `edge_count_semantics`. **Ruling inside the grant:** the writer stamps `edge_count_semantics` (`"stored"` | `"attempted"`), `artifact_claim` (a short closed vocabulary: `"served_projection"` | `"interim_local_projection"` | `"historical"`), `content_sha256` (over the store's bytes: a file's bytes, or for a directory store the sha256 of the sorted `relpath:sha256` lines), `bytes_written_at` (the store's mtime at manifest write, ISO UTC); the reader ACCEPTS `edge_count_claim` as an alias of `edge_count_semantics` when the new key is absent (prints it with `(legacy key)`), so E-3's cards still read.
- **"Bytes newer than a manifest reads so" (W3-S11):** the reader compares the store's CURRENT mtime (and, when cheap, its sha256) against `bytes_written_at` / `content_sha256`; a store whose bytes are newer than the manifest prints `  !! BYTES NEWER THAN MANIFEST -- store mtime <t1> > bytes_written_at <t0>; the counts above describe an OLDER store (W3-S11)`. A store WITHOUT `bytes_written_at` (a legacy manifest) prints `  bytes-vs-manifest: UNKNOWN (no bytes_written_at)` -- never a silent pass.
- **The served header path:** `projection_client.py` / `projection_server.py` render the header for the SERVED graph (`format_provenance_header` is imported there or the served manifest is rendered by its own function -- find which by `comp-find 'format_provenance_header' infra/aws/globgrph .tools`; if the server renders its own, the claim line is added THERE too, inside your grant only if the file is in PATHS: `projection_server.py` IS; a site outside PATHS is a row).
- **Tests home:** `infra/aws/globgrph/tests/` (15 files at HEAD; `test_kuzu_incremental_refresh.py`, `test_projection_worker.py` exercise the callers' manifests -- keep them green). Add `test_provenance_claim.py` there.

## DELIVERABLE -- in this order

1. `_provenance.py`: the writer's four kwargs (keyword-only; `edge_count_semantics` REQUIRED -- a caller that omits it is a `TypeError`, so a silent absent claim is impossible from this writer; `artifact_claim` REQUIRED; the two hashes computed by the writer from `db_path`); `read_manifest` unchanged; the header's claim line, the `!!` arms, the bytes-vs-manifest arm. Commit-gate.
2. The three call sites (`kuzu_nessie_load.py:252` stored/served_projection, `kuzu_incremental_refresh.py:254` stored/served_projection, `kuzu_stitch_load.py:153` attempted/interim_local_projection with `_stamp_claim` removed). Commit-gate each. Run the existing tests that touch these files (`python -m pytest infra/aws/globgrph/tests/test_kuzu_incremental_refresh.py infra/aws/globgrph/tests/test_projection_worker.py -q` under `timeout 120`; a pytest that collects ZERO on an import-time SystemExit is a false green -- print the collected count).
3. `tests/test_provenance_claim.py`: on TEMP paths with fake bytes: (a) the writer stamps all four fields and `edge_count_semantics` is required; (b) the header prints the claim beside the counts; (c) no manifest -> `!! UNKNOWN VINTAGE`; (d) a manifest with `source_kind: UNKNOWN_tarball` -> `!!`; (e) a manifest without any claim key -> `!! provenance_claim: absent`; (f) bytes rewritten after the manifest -> `!! BYTES NEWER THAN MANIFEST`; (g) a legacy `edge_count_claim` manifest reads with `(legacy key)`.
4. `f7_producers_census.py`: an AST walk over `infra/aws/globgrph/` for every call of `_provenance.write_manifest` / `write_manifest` and whether it passes `edge_count_semantics` and `artifact_claim` -> `PRODUCERS_STAMPING=<n> of <n>` (every remaining call site) beside `LEGACY_HELPER_SITES=0` (`_stamp_claim` definitions outside `kuzu_load.py`).
5. The record `CG-s-27.manifest-contract-claim.result.md` (one fenced JSON block: the field spec, the call sites by line at your HEAD, the test denominators, a rendered header EXAMPLE for each arm) then prose; the instance; the flip.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="F7-AC1" cell_refs="CG-s-27"><invocation>timeout 120 python -m pytest infra/aws/globgrph/tests/test_provenance_claim.py -q -p no:cacheprovider</invocation><expect>([1-9][0-9]*) passed</expect></criterion>
`F7-AC1` -- THE CONTRACT, EXERCISED ON TEMP STORES: the seven arms (a)-(g) each a test, all passing, the collected count non-zero (a zero-collection is the false green named above).

<criterion id="F7-AC2" cell_refs="CG-s-27"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/f7_producers_census.py</invocation><expect>PRODUCERS_STAMPING=([0-9]+) of \1[\s\S]*LEGACY_HELPER_SITES=0[\s\S]*PRODUCER_PROBE_CONTROL=FIRED</expect></criterion>
`F7-AC2` -- EVERY REMAINING PRODUCER STAMPS THE CLAIM through the one writer (the denominator = every `write_manifest` call site under `infra/aws/globgrph/` at your HEAD, `kuzu_load.py` named as EXCLUDED-if-present); no `_stamp_claim` helper remains outside it; a planted call without the kwargs is caught.

<criterion id="F7-AC3" cell_refs="CG-s-27"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/f7_header_arms.sh</invocation><expect>ARM_CLAIM_BESIDE_COUNTS=true[\s\S]*ARM_NO_MANIFEST=!! UNKNOWN VINTAGE[\s\S]*ARM_UNKNOWN_KIND=!![\s\S]*ARM_CLAIM_ABSENT=!! provenance_claim: absent[\s\S]*ARM_BYTES_NEWER=!! BYTES NEWER THAN MANIFEST</expect></criterion>
`F7-AC3` -- THE RENDERED HEADER, FIVE ARMS ON REAL RENDERS (the function the estate calls, not an inner helper): the claim beside the counts; no manifest; UNKNOWN kind; claim absent; bytes newer -- each line printed as rendered.

<criterion id="F7-AC4" cell_refs="CG-s-27"><invocation>timeout 120 python -m pytest infra/aws/globgrph/tests/test_kuzu_incremental_refresh.py infra/aws/globgrph/tests/test_projection_worker.py -q -p no:cacheprovider</invocation><expect>([1-9][0-9]*) passed(?![\s\S]*failed)</expect></criterion>
`F7-AC4` -- THE CALLERS' EXISTING TESTS STAY GREEN with a non-zero collected count (the writer's new REQUIRED kwargs would break a caller that was not updated -- the control that can fail).

<criterion id="F7-AC5" cell_refs="CG-s-27" judgment="true"/> `F7-AC5` -- THE CONTRACT, READ: whether a consumer can now REJECT on the claim (which field, which value, at which read site), what the served header will show the morning after F-4's derive lands (a manifest written by the cloud worker through this writer), what the legacy alias costs (a second spelling alive for one round -- when it retires), and whether `!! BYTES NEWER THAN MANIFEST` could false-fire on a store the projection worker legitimately copies (mtime semantics on S3 -> local copy). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>F7-AC1, F7-AC2, F7-AC3, F7-AC4, F7-AC5</expected_criteria>

## SURFACES

`infra/aws/globgrph/_provenance.py` (the writer `:49`, the header `:560`) · `kuzu_nessie_load.py:252`, `kuzu_incremental_refresh.py:254`, `kuzu_stitch_load.py:153-169` (the call sites ONLY) · `projection_server.py` (the served render, only if it renders its own) · `infra/aws/globgrph/tests/` · `kuzu_load.py` (READ; EXCLUDED) · the E-3 record `deliverables/0.9.0_WK_NFRA_CLDGRPH~3/CG-s-19.residual-stores.result.md` + `_manifest_claims.py` (READ; your own slot's, round 5).

## BOUNDS

- **Edits are the writer, the reader, and the kwargs at three call sites.** No loader run; no real store opened; no main-workspace file touched.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
infra/aws/globgrph/_provenance.py
infra/aws/globgrph/kuzu_nessie_load.py
infra/aws/globgrph/kuzu_incremental_refresh.py
infra/aws/globgrph/kuzu_stitch_load.py
infra/aws/globgrph/projection_server.py
infra/aws/globgrph/tests/test_provenance_claim.py
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-F-7.manifest-contract-claim.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.6 (this recut), cell CG-s-27 (s.1a; ADDED on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S27, over W3-S7, W3-S8, W3-S11 and C-S27).
<owned_cells>CG-s-27</owned_cells>
Read-dependencies, NOT claimed: CG-s-19 (DONE; E-3's claim cards and vocabulary). Concurrent, NOT yours: CG-s-21 (slot ~1 retires `kuzu_load.py`), CG-s-24 (slot ~2 edits the derive/pin logic of two of your call-site files -- your edit is the kwargs only), CG-s-26 (slot ~2 retires `kuzu_stitch_load.py` last).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25 across 5 carriers); the C3 moratoria bind BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud act; a local code contract and its tests.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut -- `write_manifest\(` 9 hits / 961 files (1 DEF, 4 SURFACED call sites, 4 TEST in an unrelated adapter-audit module).
</preflight>

<proof_of_spec>
Criterion ids minted at the recut by the issuer: `F7-AC1`..`F7-AC5`. Instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-F-7.manifest-contract-claim.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> F7-AC1,F7-AC2,F7-AC3,F7-AC4,F7-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `F7-AC2` (the planted call) and `F7-AC4` (a caller left behind) are the controls that must be able to FAIL. `F7-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance pinning them).
</proof_of_spec>

<compiler_tools_mandate>
BEFORE ANY ACT: `python .tools/comp-read infra/aws/globgrph/_provenance.py --for "write_manifest's fields, read_manifest, and every branch of format_provenance_header including the counts line and the UNKNOWN VINTAGE arm"`; `python .tools/comp-find 'format_provenance_header|read_manifest\b' infra/aws/globgrph .tools org/modules/graph --limit 40` (every reader of the manifest is a consumer the new fields reach). Every `.py`: `bash .tools/commit-gate.sh <file>`.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the spawn.**
