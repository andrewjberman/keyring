# 2.0.0_SA_COO~B -- session log, 2026-09-10 21:30Z to 2026-09-11 03:25Z -- IRPT_BCKEND round 1, L7 drain (part 1)

Continues `logs/2026-09-10/session_cooB_1950-2130Z_irpt_bckend_seated_L5_L6_spawn.md` (7c7913a43f). Spine v3 L7: worker subagents `0.9.0_WK_IRPT_BCKEND~1..4`, one worktree each under `/c/tmp/wk-irpt-1-<n>`, drained through `.tools/safe-merge.sh` (every drain conflicted on the append-only channel and the shared manifests; resolved as strict unions, `--continue` inside the guards). Push state of every commit below: LOCAL (this seat never pushes; LD-0522).

## Drained (11 of 19 cells), in order

| cell | slot | merge | instance | rows carried |
|---|---|---|---|---|
| IB-s-18 | ~1 | 410f28f7db | VALID | W1-S1..S2 |
| IB-s-17 | ~1 | 6800337403 | VALID | W1-S3..S4 |
| IB-s-11 | ~4 | adaed9762d | VALID | W4-S1..S3 |
| IB-s-1 | ~2 | f1aac99b66 | VALID | W2-S1..S5 |
| IB-s-5 | ~1 | 79eb9dcc3a | VALID | W1-S5..S6 |
| IB-s-8 | ~3 | 95a34541f8 | VALID | W3-S1..S2 |
| IB-s-2 | ~2 | 22a125e098 | VALID | W2-S7 (ARMED), W2-S8 |
| IB-s-3 | ~2 | 3cca035c66 | VALID | W2-S9, W2-S10 (both ARMED) |
| IB-s-13 | ~4 | e31ad6b8a1 | VALID (3 mech + 1 judgment) | W4-S5..S8 (INERT) |
| IB-s-6 | ~3 | 5236a7603d | VALID (arm g sub-clause declared unmet) | W3-S3 (ARMED, worker-disarmed), W3-S4 |
| IB-s-12 | ~1 | 3bed36da5b | VALID | W1-S7 (ARMED), W1-S8 (BLOCKING) |

In flight at close: ~2 on IB-s-4 (handed at 975941ee61), ~3 on IB-s-7 (handed at 5236a7603d). Idle by dependency: ~1 (IB-s-16 waits on 9 and 14), ~4 (IB-s-14 waits on 10). Remaining un-handed: 9, 10, 14, 15, 16, sb-3.

## Issuer amendments (FE-s-2 / FE-s-5 shape: un-handed faces only, recorded on the channel)

- a2e5071940 -- IB-s-2 (nullable `relationship_id`), IB-s-4 / IB-s-12 (explicit first-mint; artifact not exit code), IB-s-13 (shared layer `irpt-common`). 6b493ae940 -- IB-s-12 re-seated ~2 -> ~1.
- 72582e34ee -- IB-s-15: disarm of W2-S7 (ownership-map `id_projection` seam fails silent-safe; wired projection, absence is a refusal, one opaque-id definition, arm (g)); row S8.
- 812bbec0e9 -- eight un-handed faces (4, 7, 9, 10, 14, 15, 16, sb-3): disarm of W2-S9 (firm id has two spellings; `FirmBinding`) and W2-S10 (`_keys` refusal text discloses the refused value); arm "(amend)"; row S9.
- 975941ee61 -- IB-s-4: disarm of W1-S8 (no declared bundle for the rule-13 first-mint; reads BLOCKED-BY-W1-S8 once, carried to L10 for the DS lane) and W1-S7 (directory id space resolves for 49F only; Phase-1 trace + arm (i)); row S10.
- 65467248f3, 57341cebaf -- IB-s-9: PRD v0.8 B9 measured contracts and the v0.5 REST decision table as the replay's shapes; PRD v0.9 fixed mechanism (Lambda replay of a fenced session; the transport is the packet's `cloud_transport.py`); live arm stays the L10 qualified read; rows S11, S12.

## Decisions recorded on the channel (seat rows S6..S12)

- S7: `worker.md` `model:` flipped to `sonnet` at the SITEZ merge; ~2/~4 stopped and respawned with the model explicit; every spawn passes it.
- S11/S12: PRD moved v0.4 -> v0.9 mid-round; round 1 stays frozen on v0.4 for every rectangle; only IB-s-9 amended (measured shapes, fixed mechanism). IB-s-8 (complete on v0.4, stopped-host runner) is the wrong mechanism by Andrew's word -> round-2 recut. B16/B17 deltas -> round 2.

## Carried to the drain-end slug (L10)

1. Decomposition sequencing defect (mine): IB-s-1 and IB-s-11 handlers merged before the `_authz` wrapper (s.1 said the library lands first; s.5's chains did not enforce it). Measured at IB-sb-3's replay.
2. W1-S8 / W2-S5: the rule-13 first-mint has no declared bundle in `.tools/safe_deploy_core.py CODE_TREES`; both gold scripts read 404 on the served code prefix. DS-lane / tooling owner.
3. W3-S3: per-firm `execution_role`s trust only `lambda.amazonaws.com`; no running function can assume them (IB-s-5's surface, CVO L9).
4. W3-S4: the one-turn deploy sentinel ordering; cheap rule = commit the OPEN sentinel immediately after `deploy_ledger.py open`.
5. W1-S7: directory vs holdings id space coincides for one firm of three (INF, COT raw-key selection); IB-s-4 traces it.
6. W2-S10 estate-wide: `_keys.KeyComponentRefused` names the refused value (IB-s-17's surface, round 2).
7. IB-s-13 S13-AC3: no historical Topic Cloud exists in the estate (722 keys, 2 top-level files, one overwritten in place).
8. Export prefix with no generation attempt (S17-AC3); real YCharts specimens; every live arm; PRD v0.5..v0.9 deltas on B8/B9/B16/B17.

## Instruments and traps met this stretch

- `safe-merge.sh` refused twice on foreign staged paths (NFRA_CLDGRPH channel, IRPT_FNTEND channel) -- correct refusals; waited for the index to clear.
- A CRO commit landed on CLOUD during a 580 s index wait; the merge then started at that HEAD (parents verified: 34e16f4ce6 + 1555b17893).
- One drain loop lacked the source-map resolver and exited 9 with the merge OPEN; resolved by hand in the same guards and continued.
- CTO messages 95732 (gate change), 95751 (v0.8), 95756 (v0.9) read and acked.
