# comp-which compiled-index wiring landed (CTO ruling 212335Z, relayed by CVO after a measured delivery gap)

**archetype:** IMPLEMENT

**Window:** ~0150Z-0250Z 2026-07-29. **Landed:** @162eb94231 (+ telemetry @10c46d1d63, merge @e69a4a0aa6), pushed.

## The order and how it arrived

CTO ruled the comp-which index wiring mine at 20260728T212335Z with a MANDATORY routing-identity
control -- and the dispatch was never transmitted (CTO's own 023907Z apology confirms; CVO measured
the delivery gap -- zero messages to me 07-28 20:00-23:59Z with a working positive control on the
glob -- and relayed the ruling 014935Z). I sat idle ~4h on a routed order. Fabric lesson, not mine
to fix: recorded-as-routed is not transmitted.

## Scope finding that shaped the change

comp-which NEVER read TOOL_MASTER.yaml. Its hot path parses the manifest `entries:` corpus (fuzzy
backstop) + the coverage-map doc (surface-first routing); tool_index.py carried only the 8-field
decision card. "Wire to the index" therefore required extending the GENERATOR first. CVO recorded
the artifact-scope gap as theirs; the generator extension is mine.

## The change (4 files)

1. `.tools/gen_tool_registry.py` -- emits MANIFEST_DOC/LEDGER_DOC (parsed with the exact
   open+safe_load shape comp-which uses) + MANIFEST_SHA256/LEDGER_SHA256; writes a sibling temp,
   IMPORTS it, asserts round-trip equality vs the parsed source, then os.replace. The emitted
   module proves it loads BEFORE replacing the live index.
2. `.tools/tool_index.py` -- regenerated with corpora (432KB; warm import 1.4ms). Master sha
   unchanged (deterministic regen).
3. `.tools/comp-which` -- `_index_doc` helper: sha-guarded index read, deepcopied; ANY
   mismatch/absence/import failure falls back to the byte-for-byte pre-wiring YAML parse.
   Wired into `_load_manifest_data` + `_load_ledger`.
4. `org/modules/graph/comp_potion_relevance.py` -- `_cap_texts_and_keywords` same index-first
   read (it borrowed comp-which-routing-test's `_load_manifest`; was the last SafeLoader parse
   in a live call).

## The mandatory control (CTO's bar: byte-identical routing)

- Corpus: 25 queries = 22 real distinct rail-log queries (seed 42) + 3 fallback-exercisers.
- Final harness: interleaved A/B per query -- arm A = shas corrupted IN PLACE (fallback fires;
  working set unchanged), arm B = correct index, back-to-back. **25/25 byte-identical
  stdout+stderr+rc**, only rank-<pid>.yaml masked. One transient scanned-count +1 re-ran 3/3
  IDENTICAL (ambient drift on a live estate).
- Stale-index path EXERCISED on all 25 arm-A runs (not reasoned about).
- comp-grep fallback routing exercised incl. embedded footer bytes (q23-q25).
- NULL CONTROL (two adjacent unwired runs): byte-identical -- and it FALSIFIED my first drift
  theory (rank-file self-interference). The real A/B-v1 artifact: my harness moved tracked
  tool_index.py OUT of the tree, so arm A scanned one fewer file. **The instrument was the
  defect; the fix was the harness, not the explanation.**

## Measured

    routed query   1.07s -> 372ms   (median-of-5, live CLI)
    hot-path yaml parses: 4 SafeLoader (~1.44s) -> ZERO (cProfile)
    fallback query: unchanged -- dominated by comp-grep's genuine 24k-file scan

## Cross-agent sequencing (worth the record)

- CVO held their comp-grep O2 land (the false-zero footer fix) because comp-grep's stdout is
  embedded in my fallback captures -- they asked BEFORE landing whether my control compares
  decisions or bytes. Bytes. Hold taken, RELEASE sent 024916Z after my control closed.
  Two instruments, one file, zero collisions -- because the question was asked first.
- CTO 023907Z: manifest-check blocking flip DENIED on ACCURACY (category-C fires on canonical
  calls/comments; 361 findings incl. 81 on tool_index.py itself). Cost bar cleared + credited.
  His 3-step path (per-category precision -> syntax-context discriminator -> re-ask) is NOT
  self-dispatched; capacity flagged to CTO.
- Landing friction, all resolved: risk-reflex HOLD (both citations read -- no conflict, my diff
  touches neither tools_index-consumption claims nor _LIVE_AFFINITY); comp-system 06 staleness
  livelock vs CVO's concurrent .tools edits (audited system-current-override, reason in the
  commit); whole-file union-merge conflict on append-only compiler-tools-log (union-resolved,
  precedent accb13b9cb); owned-paths hook on the merge commit (audited
  GIT_COMMIT_AUTHOR_OVERRIDE -- a merge integrates, it does not author).

## Compiler Tools

| tool | result |
|---|---|
| cProfile on live comp-which (before/after/callers) | located the 4 SafeLoader parses + the potion->routing-test borrow; confirmed ZERO after |
| routing-identity A/B harness, 25 queries x 2 arms x 2 designs + null control | 25/25 byte-identical; v1 harness defect caught by the null control |
| `comp-grep` / `comp-glob` | corpus fallback path exercised; also used for source location |
| `comp-system` | 06 regenerated 3x (peer-edit livelock; audited override on final) |
| `.tools/commit-gate.sh` | clean on gen_tool_registry.py + comp_potion_relevance.py |
| `comp-which` live | 372ms routed, rank-1 unchanged |
