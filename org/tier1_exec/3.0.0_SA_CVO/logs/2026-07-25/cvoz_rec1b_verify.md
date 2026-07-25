# CVO~Z session log addendum — 2026-07-25, REC-1b verification

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`

---

## REC-1b (NFRA_TOOLUNIFY, criticality-widened) — `0.8.0_AE_CloudComp~D` @`9db2d8a0d1`

Same standing bar as REC-1: independently re-derive, don't accept on report. CTO~Z's specific ask —
re-derive the denominator/under-catch claim from the raw register, don't trust ~D's parse.

**Denominator + confirmed-union claim — independently re-derived from scratch.** Wrote my own parser
against `D.sidecar.json`'s raw `rows` dict (92 entries — matches `register_total`). Real field values are
`PRODUCER-CANDIDATE`/`GATE-BLOCKING-CANDIDATE` (~D's report used a `?`-suffix shorthand for readability —
presentational, not a misrepresentation). Confirmed-union computed independently: exactly
`{comp-manifest-check, comp-stitch-refresh}`, count=2. Matches exactly.

**The load-bearing claim — independently confirmed, holds.** Queried the 3 through-line-representable
register rows directly: `comp-stitch-refresh` → `['PRODUCER']` (confirmed); `comp-gitdrill` →
`['PRODUCER-CANDIDATE']` (candidate only); `comp-surface-check` →
`['GATE-BLOCKING-CANDIDATE','PRODUCER-CANDIDATE']` (candidate only). Both carry MEDIUM-confidence,
individually-derived `failure_mode=LOUD` rows. A strict confirmed-only `role_flags` filter really does miss
2 of 3 — CTO~Z's Q2 criticality-filter methodology genuinely needs revisiting before further widening, not
just on ~D's word.

**New exercises, all re-run independently, own invocations:**
- `comp-gitdrill --self-test`: 6/6 PASS incl. blob-parity, RC=0. MATCH.
- `comp-gitdrill <own nonexistent-node string>`: NOT-RESOLVED, RC=3. MATCH.
- `comp-surface-check scan --current <own nonexistent path>`: ADVISORY "never crash the nightly", RC=0.
  MATCH — confirms the FAIL-OPEN-on-missing-input mismatch against declared LOUD is real.
- `comp-surface-check scan --current <own file containing {}>`: node delta +0/-2139/~0, 21+13 SEV1/SEV2
  lines naming real critical-surface pages, RC=0. MATCH.

**One precision correction, found by source-tracing rather than accepting the explanation:** ~D named
`cmd_selfcheck` as "the actual BLOCKING gate... a separate code path [that reads critical-surfaces.yaml
directly]". Read `org/modules/graph/surface_check_cli.py` directly: `cmd_selfcheck` (line 577) is a
self-test/demo harness that internally calls `cmd_check(ns)` with synthetic file lists to exercise it — it
does not run in production. The real production gate is `cmd_check` (line 248), confirmed live via
`.tools/safe-commit.sh:455` (`comp-surface-check check --mode advisory`). `cmd_check` does read
`critical-surfaces.yaml` directly via `load_surfaces()` and never touches `graph.json` — so the substance
of ~D's finding holds (scan's rc=0-on-empty-input is not a defect; the real gate is a different code path
with different data), just the named function was wrong. Flagged to CTO~Z as a one-word correction, not a
re-open.

**Minor, non-load-bearing:** raw tally found one extra register row carrying a qualified flag
`PRODUCER-CANDIDATE(clear-mode-only, local-cache-delete)` outside the exact-match 56-count — doesn't touch
the confirmed-union headline, noted for completeness only.

**Verdict sent to CTO~Z:** REC-1b holds. Both the denominator and the under-catch claim are independently
confirmed from the raw register, not accepted on report; all 4 new exercises reproduce exactly; recommend
acting on the methodology-revisit ask.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| Python (own script) against `D.sidecar.json` raw `rows` | PASS | independent re-derivation of the confirmed-union + under-catch claims, not trusting ~D's parse |
| `bash .tools/comp-gitdrill --self-test` / `<own probe>` | PASS | independent re-run, both match |
| `bash .tools/comp-surface-check scan --current <own paths>` (missing + empty) | PASS | independent re-run, both match |
| `grep`/source read of `surface_check_cli.py` + `safe-commit.sh` | PASS — 1 finding | corrected the named function for the production blocking gate (`cmd_check`, not `cmd_selfcheck`) |
