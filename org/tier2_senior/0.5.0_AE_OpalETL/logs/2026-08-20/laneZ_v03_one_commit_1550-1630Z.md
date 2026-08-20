# 0.5.0_AE_OpalETL~Z — W5-V03: the v0.3 ONE commit (1550–1630Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE (41-case battery + 9 probes + 4 mutants + LIVE validate), TRACE (Phase-1 census), COORDINATE

**Lane:** `~Z` (site Z). Logged in the BASE agent folder, lane-prefixed.

## What happened
- **Phase-1 census** (before writing): axis-token consumers = exercise(16)/gate(6)/battery(2)/emit(1) — all inside the TO's named set; `comp-blast gate` TIMED OUT at 60s (the named box hazard) → fallback import census: gate callers = `query_v0.py` + the exercise battery only; `--definitions` baseline 67 lines.
- **FINDING surfaced:** the emitter read the DELETED BG refs copy (`v01_path`) for its v0.1 routing fragments — a consumer my home-commit census missed (it grepped the BG tree; the consumer lived in `workflows/`). Loud-crash class, no silent output, no run in the window. Re-pointed to the one home's own content in the ONE commit, with an absent-home refusal.
- **THE ONE COMMIT @96dcb4a66a** (10 files): v0.3 catalog at the ONE home (`version: 0.3`, `supersedes: v0.2`) — `verdict_class`+`verdict_state` (held = deny+pending-andrew), firm tier-or-firm (per-scope 0, global 0; 4 families carry `firm_resolution: key-scope-segment`, firm OMITTED per the record's remedy — stated; mp.11 → opal-internal + `scope: all-firms-aggregate`), `family.axis` five values; gate rule 2 reason carries the state, rule 5 branches on `firm_resolution` (per-scope literal GONE incl. the reason-string rewording), `:70-71` unchanged; emitter single-output + value-set refusals + census prints; battery/validate/exercise re-pointed to the home; the v0.2 staged file DELETED; the V03 records addendum + DESIGN.md home rule in the same commit.
- **Exercised BEFORE the port (rcs unpiped):** emit rc=0 ×2 BYTE-IDENTICAL (29079a8fda329851…); emitter mutant rc=2 NOTHING WRITTEN + hash unchanged; battery 41/41 rc=0; P1–P8 + the NEW firm_resolution-removed mutant 9/9 rc=0 (scratch copies; real catalog hash-asserted untouched); exercise 16/16 rc=0 (rider v0.3 + mutants A/B); pytest 12/12; LIVE validate rc=0 (36 rows: 26 concrete OK, 10 families OK; report COMMITTED); commit-gate clean 5/5; tree clean.
- Proof instance V03-1..8 authored; checker run recorded there.

## Corrections (the honest column)
- The battery's first rc read came through a tail pipe and printed 0 while the battery was correctly FAILING on the not-yet-deleted staged file — every recorded rc re-captured unpiped.
- The P7 probe anchored on the token's first occurrence = the preamble COMMENT, not the row; its own assert caught it (re-anchored on the 8-space row form).
- One interim ruff F401 (SERVABLE_CLASSES import left behind by the rider rewrite) — fixed before commit.
- The patch script's first run failed its own anchor assert (a vf_missing line never read verbatim) — re-anchored on the unique return-2-then-write sequence; nothing was half-written (the failing rep preceded every file write).

## Blockers
None I hold. The PORT (V03-6) = laptop lane via MSTR~Z's ferry; CTO~Z's rows-4/7 delta + CVO~Z's second read land at their lanes (recorded, not gated).

## Compiler Tools
| Tool + command | Result | Note |
|---|---|---|
| `comp-find` axis tokens + import census | 3375/458 grouped; callers = query_v0 + exercise | comp-blast gate timeout (named) |
| `comp-estate --definitions` | 0 hits ×5 new tokens / 67 lines | scope collision carried (registry item) |
| emit / battery / probes / exercise / pytest / validate | 0 ×2 identical / 41/41 / 9/9 / 16/16 / 12/12 / rc=0 LIVE | all rcs unpiped |
| `.tools/commit-gate.sh` | clean 5/5 | |
| `.tools/safe-commit.sh` | @96dcb4a66a | tree clean after |
