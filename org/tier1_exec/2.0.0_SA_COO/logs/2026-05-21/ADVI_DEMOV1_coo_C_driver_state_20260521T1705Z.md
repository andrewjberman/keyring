# COO~C Session Log — ADVI_DEMOV1 Administration — State Snapshot
- **Agent:** 2.0.0_SA_COO~C
- **UTC:** 2026-05-21T17:05Z
- **Supersedes:** the 16:20Z snapshot.
- **Scope lock:** ADVI_DEMOV1 only.

## Crash recovery this turn
Session crashed mid-`opal-agent-comms` call, just after closing TO-0 and
GO'ing TO-2. On restart, verified actual state rather than assuming:
- Post-phase-0 commit `90a7b45a4` (close TO-0 + amend TO-2/TO-3) was committed.
- CTO had since committed PRD **v0.1.3** (`c01273c5c`, 16:42Z) — the ruling that
  resolves the gold/ scope open-item I had flagged in TO-2.
- TO-2 GO **landed** — `ADVI_DEMOV1.002` shows as a pending TO on DS~C.
- 4 commits were unpushed; origin/CLOUD was stale at `098f102bb`.

## Reconciliation done
- TO-2 amended to fold PRD v0.1.3: transform scope = **platinum/** only**;
  gold/ prefix dropped (getClientDetail route orphaned — zero portal call
  sites, superseded by getPlatinumClientSummary). Open-item language removed
  from delta bullet 4 + AC 3c; engine stays prefix-agnostic by design.
- Committed `8b1ad7b5d` (base COO serial — `POD4_OR_EXEC` owned-paths permits
  `2.0.0_SA_COO`, not the `~C` variant; tilde-lane authoring gap, noted below).
- Pushed `098f102bb..8b1ad7b5d` — origin/CLOUD now current (carries PRD v0.1.2,
  post-phase-0, CTO v0.1.3, TO-2 reconciliation).
- Scope-finalization relayed to DS~C; v0.1.3-folded confirmation sent to CTO.

## ADVI_DEMOV1 standing
| TO | Phase | Owner | State |
|----|-------|-------|-------|
| TO-0 | probe | DS~C | COMPLETE — RAVC2-accepted |
| TO-1 | infra | AE~C | approved; gated solely on the 0.7.0_AE_CloudOps~C lane (Andrew decision) |
| TO-2 | transform engine | DS~C | GO; scope FINAL (platinum/** only); DS~C runs on rotation off YALP_MDSRC.B1 |
| TO-3 | firm + user registration | DS~C | staged; v0.1.3 to be folded at GO time |
| TO-4 | run + PII-leak scan | DS~C | staged |

## Open notes
- `POD4_OR_EXEC` in `.owned-paths.yaml` lists DS `~A..~D` variants but no
  COO/CTO tilde variants — COO~C must author TOs under the base `2.0.0_SA_COO`
  serial. Not blocking; flag only if a tilde-author commit is ever required.
- TO-3 "both serving paths" = dynamic + static platinum — unaffected by the
  gold/ drop; no edit needed until GO.

## Next events (tracking mode)
1. DS~C TO-2 RAVC2 (reviewed engine + --dry-run) -> validate, close, RAVC2 to CTO.
2. Andrew stands up 0.7.0_AE_CloudOps~C -> GO TO-1 (runs parallel to TO-2).
