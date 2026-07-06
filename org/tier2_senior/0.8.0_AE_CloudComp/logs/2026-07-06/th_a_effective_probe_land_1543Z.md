# TH-A EFFECTIVE-axis probe LANDED + a live COMPLEARN corpus-load regression fixed

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Summary
Monday return from the 07-03..07-06 Independence Day holiday dormancy (Andrew-confirmed; CVO startup
spot-check `bdfbe944d` already recorded it as holiday, not stall). Startup: `/watcher` (registered LIVE,
Monitor `bxk2cy050` armed) + `/cloud-ops` + XXX.md protocol. Picked up my one pending TO,
**NFRA_TOOLHEALTH.TH-A** (the EFFECTIVE-axis recurring probe), which was gate-cleared (COMPPROOF-B1 done)
and building in my ~D lane when dormancy hit -- found the build **stranded uncommitted**. Finished it,
demonstrated the load-bearing FIX-catch on LIVE, fixed a blocking regression found en route, committed +
pushed (`0191f9c9f`), TO=complete.

## What happened

### Ground-truth first (Rule 22, never trust the `<status>` claim)
`git log` since 07-02 20:00 + `get_agent_status ~D`: `tool_probe.py` (366 ln) + `tool_corpus.py` existed
on disk **untracked** (mtime 07-02 20:39), no ~D session live, TO `<issued_to>` = base serial = me. So I
am the correct owner to finish the stranded ~D build (MSTR REUSE-ruling; no new spawn).

### TH-A build finished + LIVE-demonstrated (ACs 1-3)
- `tool_probe.py` = per-tool/per-class blind-run probe: isolation gate (author!=solver!=judge; sealed
  answer PROVABLY stripped from the tool payload -- B1 diff-gate un-forked), REACH x USABILITY ->
  EFFECTIVE via `harness.score_run` un-forked, append-only emit (`effective_probe_log.jsonl` +
  `effective_feed.json`, the TH-B `--effective-feed` join input). `tool_corpus.py` = sealed 4-probe corpus.
- **LIVE run** (`python tool_probe.py --run`): comp-which/routing-01+02 -> EFFECTIVE=yes (reach usable
  3.5s/2.3s); comp-freshness/single-artifact -> yes (15.6s usable); comp-freshness/full-chain-under-load
  -> **no** (reach=no, too-slow, hit the 90s SLA cap). All 4 rows `isolation_ok=True` (AC-1).
- **The FIX-catch (AC-3, the whole point of the EFFECTIVE axis)**: fed the per-tool feed into TH-B.
  comp-freshness is USED(108 ev/6 roles)/value-healthy(0.981)/rail-chosen -> log-mining alone says KEEP.
  With the TH-A EFFECTIVE feed, `comp_tool_health --tool comp-freshness --effective-feed`: verdict flips
  **KEEP -> FIX** (effective=False). comp-which stays KEEP-eligible (effective=True). Only the blind-run
  axis surfaces that a used, value-healthy tool is functionally too-slow-under-load.
- COMPLEARN substrate UNFORKED (AC-2): `comp_learns_score.py` + owned tables untouched; TH-A adds an
  append-only NEW stream only.

### Blocking regression found + fixed en route (DIAGNOSE)
The TH-B join first CRASHED: `parse_rail` (tool_activity_emit.py:303) `open(encoding="utf-8")` with no
`errors=` hit a **non-UTF-8 byte** -- grounded to a truncated em-dash (bare `0xe2`, `comp-which-rail.log`
line 3445, some agent's mangled smart-punctuation in a rail marker). This crashed `load_corpus`, bricking
**COMPLEARN corpus load fabric-wide** for every consumer since ~07-02 (a regression against the 07-02
CVO~B TH-V validation). `parse_rolling_log` (236, reads the multi-writer `compiler-tools-log.md`) and
`parse_telemetry` (269, reads `agent_telemetry/*.jsonl`) had the identical latent bug. `comp_learns_score.py`
(all 3 opens) + tool_activity_emit open#390 were **already** `errors="replace"` -- the intent to harden
was established; 236/269/303 were simply missed. Hardened all three to the house pattern. Join then worked.

## Compiler Tools
Per the TO `<compiler_tools_mandate>` -- every `<run>` reproduced with observed result + pass/fail vs `<expect>`:

| Phase | Command | Result vs expect |
|---|---|---|
| P1 before-write | `git log`/`get_agent_status ~D` ground-truth; Read tool_probe.py+tool_corpus.py+harness.py; confirm append-only stream is ADD-not-mutate | PASS -- build stranded-uncommitted; COMPLEARN scorer untouched by design; one home compproof/ confirmed |
| P2 before-commit | `python tool_probe.py --self-test` (isolation + scorer) | PASS -- strip 4/4 clean; isolation VOIDs on author==solver + answer-leak; REACH x USABILITY->EFFECTIVE; FIX rollup (13 assert) |
| P2 before-commit | `python tool_probe.py --run` (LIVE, 4 probes) | PASS -- FIX-catch surfaced: comp-freshness EFFECTIVE=no on the full-chain probe (used-but-ineffective) |
| P2 before-commit | `.tools/ds-commit-gate.sh` x3 files | PASS (after fixing F401 unused-import + E702 semicolon in the ~D draft) |
| P3 after-commit | `comp_tool_health --tool comp-freshness --effective-feed` (no-feed vs +feed) | PASS -- KEEP->FIX flip demonstrated LIVE; comp-which KEEP-eligible |
| startup | `comp-iam`/`comp-*` not run this cycle | N/A -- no IAM/infra-policy change; the only infra edit was an I/O `errors=` robustness fix (no boto3/policy delta) |

**What worked:** the isolation self-test is a genuine structural guard (proves author==solver + answer-in-payload
both VOID); the `--effective-feed` seam TH-B pre-wired on 07-02 dropped in one-line and produced the flip.
**What failed:** the ~D draft carried 2 ruff violations (unused `corpus_loader` import -- docstring claimed a
reuse the code inlined; a semicolon 2-stmt line) -- gate caught both; fixed + corrected the docstring claim.
**Gap found (systemic):** three multi-writer-log parsers read strict-utf-8 without `errors=` -> one bad byte
bricks COMPLEARN corpus load fabric-wide. Fixed all three; recommend a lint/pattern check so new log readers
inherit `errors="replace"`.

## Blockers
None. TO complete on the build + live demonstration (AC1-3). One FOLLOW-ON surfaced (not a blocker):
the recurring **TRIGGER cadence/host** for the probe -- it is recurring-CAPABLE (append-only, idempotent
feed regen) but no auto-schedule is wired, because blind-runs are cost-heavy (a 90s-cap timeout per slow
probe) and auto-running them on every SessionEnd would be inappropriate. This is the same decision-class as
the emit-wiring cloud-vs-local pick CTO ruled -- RAVC'd to COO~B + CTO for a cadence/host call.

## Current State
- TH-A EFFECTIVE probe LANDED + pushed `0191f9c9f` (origin/CLOUD). Self-test PASS; LIVE FIX-catch proven.
- TH-B `--effective-feed` join works end-to-end (comp-freshness KEEP->FIX; comp-which KEEP).
- COMPLEARN corpus-load regression FIXED (3 log-parser opens hardened) -- was bricking load fabric-wide.
- Emit outputs (effective_probe_log.jsonl, effective_feed.json) left untracked (runtime, per the
  comp-which-rail.log gitignore pattern; regenerated each probe run).

## Next Steps
1. **[2.0.0_SA_COO~B / 1.0.0_SA_CTO]** rule the recurring-probe TRIGGER cadence + host (same class as the
   emit-wiring pick); I execute the wiring on the ruling.
2. **[3.0.0_SA_CVO~B]** TH-V honesty pass on the EFFECTIVE axis -- independently re-run `tool_probe.py --run`
   blind (the isolation gate is what makes her scoring meaningful) + confirm the KEEP->FIX flip.
3. **[me]** on the cadence ruling: wire the schedule + verify the served effective_feed advances on cadence.
