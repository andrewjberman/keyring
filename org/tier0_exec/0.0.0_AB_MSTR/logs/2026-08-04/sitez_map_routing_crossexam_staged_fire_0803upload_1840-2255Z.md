# Site Z (~Z lane) — danger-map routing + incident record, cross-exam review, staged-fire /terminal-upload (first production run)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, COORDINATE, SCRIBE

**Agent:** `0.0.0_AB_MSTR~Z` · **Window:** 2026-08-03T18:40Z -> 2026-08-04T22:55Z
*(Delta log; prior: `sitez_st_rootfix_terminal_upload_skill_briefing_1610-1840Z.md`. /govern loop
stood down by Andrew 08-03 ~18:45Z ("for now"); zero crons since; event-driven throughout.)*

---

## Current State (zero-context handoff)

**Staged fire COMPLETE and accepted (08-04 22:50Z).** Andrew-direct via CTO ordered the first real
`/terminal-upload` run; result: served surface at `data_as_of 2026-08-03` (true T-1),
**the LTC/LTA -> LT/ULT rename LIVE on the portal** (codes [UST,ST,INT,LT,ULT]), all rows
content-sane, macro estate at the same frontier, single execution `20260804_v1-4047de02`
SUCCEEDED. Zero bad data sent. Two real faults found + handled inside the run:

1. **Model notebook pull-leg crash** — `TEMPLATES_DIR` hardcoded `C:\Users\YangLiu\...` (4th
   member of the literal-path device-portability class). Fallback per skill design: send-only on
   the morning-built artifacts. Routed to Yang via main fabric.
2. **Tripwire FAIL = true positive of the rename** — its constants (`REGRESSION_MODELS`,
   `MODEL_INDEX_NAMES`) predated v1.5.3; both 0803 pkls verified carrying the ratified new
   universe (matching Manav's 08-03 announcement + DS's 4/4 LT/ULT content-verify) -> constants
   updated in the LIVE OneDrive tripwire under the fire authorization (dated comment), re-run
   PASS. Repo twin (`org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables/opal_bbgtml/
   bbg_pkl_tripwire.py:47,:51`) routed to DT for mirror.
3. **MCP transport drop mid-upload** — response lost, operation NOT: live-verified (uploads
   landed 22:44:12Z, one execution, serve already advancing) before considering retry; none
   needed. A blind retry would have double-fired. Gateway `opal` MCP may need re-auth here.

**Danger-map arc (08-03 evening, closed):** Andrew ordered the site-Z map rebuild committed; I
measured the trade first (site-Z build = 927 edges/0 memory citations vs tracked 1,484/1,420 —
the builder's `_MEMORY_DIR` is laptop-hardcoded) and surfaced; Andrew re-routed ("route it") to a
laptop build. Base built 1,659 edges, CTO caught base's count-based verification hiding 197
gained/22 lost and ran a node-level diff before committing. **My own error corrected on the
record:** I had attributed the +2 node growth to today's docs — FALSE (a scope assumption stated
as fact; `docs/briefs/` and `deliverables/` are not corpus roots). Fix: condensed incident record
landed in the canonical corpus-root home `docs/references/INCIDENT_20260803_ST_MODEL_PORTFOLIO.md`
(@8a06f10cc, merged at 41a1cceaf0) — the map learns the incident by correct filing, and CTO's
map commit was re-sequenced to rebuild after pulling it.

**Cross-exam review (Andrew ask):** located CVO's `DENOMINATOR_CROSSEXAM_QUEUE_20260729.md`,
presented the materiality ranking + walk verdicts; live-corrected two of Andrew's recollections
(comp-surface-check is HALF-removed — de-cataloged but still advisory in safe-commit.sh:454;
comp-iam's real-state incorporation did NOT fully land — live/census tier exists as modules but
default output remains DESIRED-plane with the census stale). Clarified comp-system (the estate's
self-description compiler, `infra/system/06_current_state`) + briefed the 7 curiosity tools.
Open from that thread: comp-iam live-plane integration, comp-pipescript WS4, the 19-zero-use
/prune-quant census, and Andrew's word on stripping the surface-check advisory hook.

**comp-pulse timing (Andrew ask, measured):** fresh-map diff 0.58s; stale-triggered auto-refresh
1.42s total; standalone build 0.96s — trigger-on-stale-read (36h threshold) with ~100x timeout
headroom. The rebuild also demonstrated the corpus growing from the day's own records (925->927).

## Commits (mine, this window)

`8a06f10cc` incident record (pushed via merge `c1d53ae00`). Non-repo writes: live tripwire
constants (OneDrive, dated); no repo commit pending — `git status` carries only the pre-existing
other-lane set + the superseded site-Z map rebuild exhaust (awaiting CTO's laptop-built map to
land, then a `git checkout --` restores the tracked version here).

## MCP / bus traffic (significant)

Inbound: map-build verify + corpus-scope correction (392c2b9e), CTO node-diff heads-up (822b87dc),
staged fire order (ce2f618b), fire-closure ACK (c397c23c). Outbound: route-request w/ measured
trade (d194ed34), corpus-scope ACK + resequencing (bb72da0c), lost-edge hypothesis (b1060a50),
fire ACK (b55cb6ee), interim per-leg report (78de626c), fire-closed report (1180faae). All
inbound ACKed in-turn.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-pulse (timed x3) | PASS | 0.58s fresh / 1.42s w/ auto-refresh / 0.96s standalone build; AUTO-REFRESHED telemetry exercised |
| commit-gate + surface-check + risk-reflex (via safe-commit) | PASS | incident-record commit clean |
| nerves_lexical (read + timed) | — | source-read for the lineage answer; site-Z corpus blindness quantified (1,420 memory citations invisible) |

Operational aws (s3/stepfunctions) + BBG refdata probes off-rail per Rule 21; two rail-checked
greps (tool-caller census, constant-twin locate).

## Blockers

None mine. Open at others: **[DT]** tripwire repo-twin constants; **[Yang]** notebook
TEMPLATES_DIR literal + nid:52865; **[CTO base]** map commit post-rebuild (in flight);
**[NERVES owner]** `_MEMORY_DIR` portability; **[Andrew]** surface-check advisory strip?,
NFRA_VELOCITY re-open, /govern re-arm.

## Next Steps

- **[0.0.0_AB_MSTR~Z]** Event-driven standby; on CTO's map push: pull + checkout-restore the
  local map file; tomorrow's `/terminal-upload` is the second production run (pull leg still
  degraded on this box until Yang's path fix — send-only fallback stands).
