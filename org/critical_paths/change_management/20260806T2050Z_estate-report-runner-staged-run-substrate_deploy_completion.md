# Deploy-completion ledger: estate-report-runner STAGED-RUN SUBSTRATE (7782bc7b0)

**Opened:** 2026-08-06T20:50Z, AT DEPLOY START (not retroactive)
**Status: CLOSED 2026-08-06T20:59:15Z — LANDED AND VERIFIED. L1-L6 DONE; L7 open by design.**
**Authority:** **ANDREW-DIRECT, sovereign, 2026-08-06 at the CTO~B terminal. VERBATIM: *"Go, get it
up"*** — on an explicit statement that this does NOT fix KIMI_TIMEOUT and that I had deployed
something eight minutes before its veto earlier the same day.
**DEP5** of this key. Siblings: `…1456Z corpus-vintage` (DEP1) · `…1645Z corpus-delivery` (DEP2) ·
`…2312Z budget-inversion` (DEP3) · `…1412Z kimi-timeout-pair-fix` (**DEP4 — deployed then ROLLED
BACK on veto; nothing from it is live**).

## The act

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`. Transient box,
systemd oneshot pulls on boot -> re-uploading IS the deploy (`EC2_MANIFEST` `_deploy_note`, Rule 12).

| | value |
|---|---|
| deployed vintage | `7782bc7b0` (CTO~B, 2026-08-06) |
| tree-vs-vintage | `git diff 7782bc7b0` on the file = 0 bytes; pin re-derived at deploy time |
| Phase-2 local md5 | `60dcac6d1127fbcdb7f8d3a154bbd0c3` |
| local bytes | 97,535 (was 75,026 — +22,509) |
| PRE | ETag `"13b790058b8ed3ce4360dda654ee99df"` / 75,026 B / 2026-08-06T14:22:18Z / VersionId `zwAf4aAXNXV7uS9Nsp4mpBga5EtUYS.I` (**= DEP3, restored by DEP4's rollback — unchanged since**) |
| Phase-3 head-object ETag | `"60dcac6d1127fbcdb7f8d3a154bbd0c3"` — EQUAL to Phase-2 md5, no `-N`, plain md5, valid |
| POST | 97,535 B / 2026-08-06T20:59:15Z / VersionId `P2pCy4vT97yaaJV6GOeImI.Rsif2OaYZ` |
| read-back | served md5 identical, 97,535 B, `py_compile` PASS **on the served bytes**, non-ASCII **0** |
| rollback | PRE VersionId `zwAf4aAXNXV7uS9Nsp4mpBga5EtUYS.I`; the DEP4 rollback exercised this exact path today, so it is a PROVEN path and not a planned one |

## What it changes

The **staged-run substrate**, wired under the existing monolith. Design:
`STAGED_RUN_SUBSTRATE_CONSOLIDATION_20260806.md`, CVO-validated (one merge broke and was fixed).

- **`should_run()` returns a REASON, never a bool** — a cache hit and a blocked stage are opposite
  outcomes and a boolean returns `False` for both, which is `failure != zero` rebuilt inside the
  merge that fixes it.
- **Status is the only outcome channel** — the deck's `{ok,error,started}` EXTENDED with
  `{skipped_deps_unmet,not_run}`.
- **One output-contract hook** — drops counted and reasoned, never silent.
- **THE PIN** — from the cloned tree's real HEAD; `complete()` requires the recorded pin to equal the
  run pin, making a stale cache entry unrepresentable. Exists because of a MEASUREMENT (CVO: three
  runs, three HEADs, one empty canon universe).
- **Two health signals now reach the record**: `degraded_sources` sets `load_corpus` to `error`;
  **`maps["_degraded"]` is surfaced at last** — it was already computed and never emitted, so a
  resolver-load failure has been reading as *"the resolver is bad"* rather than *"the resolver did
  not load."*
- `run_bundle` lands in the report JSON **and the manifest** (the manifest is what an adjudicator
  reads first).

Vocabulary and artifact name taken VERBATIM from `deck_generation/engine/orchestrator.py` —
the estate already had three names for this artifact and two vocabularies for the split.

## Exercise (pre-deploy)

`py_compile` PASS · `ruff` PASS (py39) · non-ASCII **0** · AST parse OK.
Local battery **28/28**, no AWS and no vendor egress, with **TWO MUTANT CONTROLS reproducing the
exact defects CVO's validation found**: restore the boolean predicate and the two did-not-run cases
collapse to `False == False`; drop the pin comparison and a superseded stage reads COMPLETE.

## Scope honesty — stated before the act, not after

**THIS DOES NOT FIX `KIMI_TIMEOUT`.** The 2026-08-07 13:00Z fire will still fail on the AI half.
**What changes is that it will SAY SO** — with a pin, per-stage statuses, drop counts and attribution
health — instead of being reconstructed by hand from EC2 logs, which is what two seats spent the
morning of 08-06 doing.
**The risk this carries is to the DETERMINISTIC half, which currently works.** That is the honest
exposure: new code in a healthy path, to improve the record of a path that is already failing.
Mitigation is the battery above plus a rollback proven twice today.
**Deployed != exercised.** First execution is the 2026-08-07 13:00Z boot.
No alert/alarm/SNS/SES/checker/monitor built.

## Legs

| # | leg | evidence | status |
|---|---|---|---|
| L1 | authority | Andrew-direct *"Go, get it up"*, on a stated no-fix-to-timeout scope | DONE |
| L2 | pre-state | head-object = DEP3 artifact restored by DEP4 rollback, unchanged | DONE |
| L3 | PutObject | one call, no `--quiet`; VersionId `P2pCy4vT97yaaJV6GOeImI.Rsif2OaYZ` | DONE |
| L4 | ETag verify | ETag `60dcac6d…` == Phase-2 md5; 75,026 -> 97,535 B; LastModified 20:59:15Z | DONE |
| L5 | read-back | served md5 identical; `py_compile` PASS on SERVED bytes; non-ASCII 0; markers on served bytes: `class StagedRun` 1 · `def should_run` 1 · `skipped_deps_unmet` 4 · `def validate_output` 1 · `run_bundle` 3 · `STAGE_KINDS` 3 | DONE |
| L6 | negative control | superseded DEP3 md5 `13b790058b…` is NOT current (`60dcac6d…`) — **DIFFERS**, so the L4/L5 match is meaningful rather than vacuous | DONE |
| L7 | emitted-artifact verify | **OPEN BY DESIGN** — 2026-08-07 13:00Z boot. The discriminating read is whether `run_bundle` appears in the manifest with a real pin and per-stage statuses | OPEN by design |
