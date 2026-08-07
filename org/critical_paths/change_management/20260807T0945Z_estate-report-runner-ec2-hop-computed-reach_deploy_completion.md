# Deploy-completion ledger: estate-report-runner EC2-HOP COMPUTED REACH (57d183ab98)

**Opened:** 2026-08-07T09:45Z, AT DEPLOY START (not retroactive)
**Status: CLOSED 2026-08-07T09:45:47Z — LANDED AND VERIFIED. L1–L6 DONE; L7 open by design.**

**DEP6** of `s3://opal-estate-report/code/estate_report_runner.py`. Siblings: `…1456Z corpus-vintage`
(DEP1) · `…1645Z corpus-delivery` (DEP2) · `…2312Z budget-inversion` (DEP3) · `…1412Z
kimi-timeout-pair-fix` (**DEP4 — deployed then ROLLED BACK on an Andrew veto; nothing from it is
live**) · `…2050Z staged-run-substrate` (DEP5, landed 20:59:15Z).

**Authority:** standing lane pre-authorization (CLAUDE.md Agent Autonomy — Opal-owned infra, own
lane). **NOT an Andrew-directed deploy**; DEP5 carried his verbatim *"Go, get it up"* and this one
does not. Surfaced to him in-session rather than gated on him, per the no-manufactured-gates rule.
Commit landed under the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` (owned-paths: this
file is the AE lane; one lane, one file).

## Why this is being deployed and not deferred like the globgrph derive tonight

**The two are opposite on the exact axis AE and I used to defer that one — blast radius and the
length of the verification tail.**

| | globgrph derive (DEFERRED) | this (PROCEEDING) |
|---|---|---|
| consumers | **5 task-defs** floating on a shared `:latest` the build cannot avoid moving | **1** transient box, one key |
| pickup | UNATTENDED, 5 fires in a 2.5h window ~17h out | ~3h out, **attended**, I verify before it |
| tail | build -> ECR -> ECS -> instances -> item 7 | L1–L6 now, L7 at the 13:00Z boot |
| rollback | image retag across 5 | same-key put, **rollback path exercised by DEP4** |

Recording the comparison because a reader seeing "deferred a deploy at 09:30Z, fired one at 09:45Z"
should be able to see the distinction was principled rather than convenient.

## The act

ONE `s3api put-object` to `s3://opal-estate-report/code/estate_report_runner.py`.

## What changed

`coverage.ec2_hop_note` — a hardcoded string asserting `"EC2 hop has ZERO measured reach (0 of 28
service names match a resolver producer name)"` — replaced by `coverage.ec2_hop_reach`, computed
each run. Wrong three ways: **denominator drifted** (27 services, not 28); **"zero reach" conflated
reach with the name join** (the hop's `ec2-unthreaded:` exit resolves to `producer:<name>`, kind
`chain`, with no join at all — so the note read as a *deletion warrant for live code*); and it would
have **printed beside a contradicting `by_hop` entry in today's own report**, because this file lives
under `estate-report-runner`'s own `source_path`.

Controls, run against the real `EC2_MANIFEST.json`: POSITIVE (reach 2 of 3, docs path correctly
misses) · NEGATIVE (reach 0, join still prints its denominator) · THREADED (to_thread 1, unthreaded
1). **The old note would have printed "ZERO measured reach (0 of 28)" on all three.**

## Ledger

| Leg | What | Evidence | State |
|---|---|---|---|
| L1 | pre-state | ETag `60dcac6d…`, 97,535 B, 20:59:15Z, VersionId `P2pCy4vT…` — **identical to DEP5's landed values, no drift** | DONE |
| L2 | intended bytes | md5 `d292af7eb17250c50eb0382cef5372db`, 99,270 B, non-ASCII 0 | DONE |
| L3 | PutObject | one call, no `--quiet`; VersionId `trHl889cvDlpSnmCAmeaJWBiYDQp16vo`; SSE AES256 | DONE |
| L4 | ETag verify | ETag `d292af7eb17250c50eb0382cef5372db` == L2 md5; 97,535 -> 99,270 B; LastModified 2026-08-07T09:45:47Z | DONE |
| L5 | read-back | served md5 `d292af7e…` identical to intended; **`py_compile` PASS on the SERVED bytes** (not the local file); non-ASCII 0; markers on served bytes: `ec2_hop_reach` 1 · `ec2_hop_note` **0 (removed)** | DONE |
| L6 | negative control | superseded DEP5 md5 `60dcac6d…` is NOT the current served md5 — **DIFFERS**, so the L4/L5 match is meaningful rather than vacuous | DONE |
| L7 | emitted-artifact verify | **OPEN BY DESIGN** — 2026-08-07 13:00Z boot. Discriminating read: `coverage.ec2_hop_reach` present with a live denominator, and if any changed path sits under a registered service, `by_hop` carries an `ec2-*` entry consistent with it | OPEN by design |
