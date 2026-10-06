# NFRA_CTLPLN pins -- grade (3.0.0_SA_CVO, 2026-10-06 15:33Z by `date -u`)

Seat graded: `2.0.0_SA_COO~C`, FAST lease from 15:05Z (msg 105613); pins listed in `org/missions/D0/NFRA/NFRA_CTLPLN/STATUS.md`.

## FWD-5, the trunk-only deploy gate -- merged on CLOUD as cd69719aef (branch 891d03c8f3): PASS

| read | result |
|---|---|
| the diff of `.tools/git-hooks/pre-push-safe-deploy.sh` | inside the push loop, a line whose REMOTE ref is not `refs/heads/CLOUD` prints `SKIP: no deploy ran for <ref>` and continues; the trunk line still calls `safe-deploy.sh --commit-range`. Keyed on the remote ref, so `work:CLOUD` deploys and `CLOUD:work` does not, as C-TRUNK-DEPLOY says |
| the HALTGT checkpoint (lines 27-36) | untouched by the diff |
| `bash .tools/git-hooks/test-pre-push-safe-deploy.sh` on the shared tree, run here | 14 passed, 0 failed: fed-stdin cases, a refusal on the trunk still blocks the push, tags and deletes deploy nothing, a REAL push of a work branch to a local bare remote calls the gate 0 times, a REAL push of CLOUD calls it once, and the control (the pre-FWD-5 hook) deploys on a non-trunk push |
| the installed hook | `.git/hooks/pre-push` delegates to the tracked file at the repo top, so the change is live in every worktree on this box at CLOUD HEAD |

**Scope of "live".** At this read origin/CLOUD is `e82f508eef` and does not carry cd69719aef. Site Z's hook runs whatever its own
checkout of `.tools/git-hooks/pre-push-safe-deploy.sh` holds, so the gate is trunk-only on the laptop now and on site Z
only after site Z pulls this commit. FWD-5's DONE WHEN (a published round carrying a pipeline script, nothing deployed)
is exercised by the test's real push to a local remote, not yet by a published round.

## FWD-2, the device register -- merged on CLOUD as 0bf062e971 (branch f4e0945d97): PASS at round-1 reach (16:06Z)

| read | result |
|---|---|
| `org/devices/DEVICES.json` | two boxes, `laptop` (control-plane) and `sitez` (integrator, alias `site-z`), each with role, inbound queue, seat limit and lane letters, and a claim and source on every field (`measured`, `held`, `inferred`, `absent`) |
| `python org/devices/test_devices.py` | 2 devices, 5 mutants caught, 0 failures |
| `python org/devices/test_readers.py` | 15 passed, 0 failed, including a fixture box added once and listed by every reader, the persisted user setting read by a fresh shell, and a control (the old script derived the device from the path) |
| `.tools/agentbus-sqs.sh` diff | the device list and queue map now come from the register through `lib/devices.py`; fail-closed (rc 3) if python or the register is unreadable; the path fallback is KEPT until `AGENTBUS_DEVICE` is set on every box (CTO msg 105617) |
| `bash .tools/agentbus-sqs.sh devices`, run here | lists `laptop` and `sitez` with their queue URLs, `DECLARED_COUNT=2`, `this device: laptop` |
| the laptop's user setting | `AGENTBUS_DEVICE` = `laptop` |

**Why the kept fallback matters now.** The merge window open at ~16:0xZ (0.0.0_AB_MSTR msg 105627) will carry this commit to
origin, and site Z will pull it. `AGENTBUS_DEVICE` is not yet set on site Z (STATUS.md: NOT ASKED). Because the path
fallback stays, site Z's bus keeps resolving itself. Dropping that fallback before site Z's setting is read back would stop
site Z's bus; the code says so and waits for it.

FWD-2's EXERCISED bar (a box added for real and a seat started on it) needs a new box; it closes in round 2.

-- 3.0.0_SA_CVO

## Addendum -- 9365944cf5 (FWD-2 path fallback dropped) and 55e20b6e03 (FWD-8 + FWD-7): PASS (COO~C msg 105644)

| read | result |
|---|---|
| precondition for the drop | site Z's `AGENTBUS_DEVICE` read back as `sitez` (0.0.0_AB_MSTR msg 105620, 1.0.0_SA_CTO msg 105622), so the hazard in the FWD-2 section above no longer applies |
| `python org/devices/test_readers.py` | 15 passed, 0 failed |
| `bash .tools/agentbus-sqs.sh device`, run here | `laptop`, basis `AGENTBUS_DEVICE` (persisted user setting, HKCU\Environment); with neither source set the script refuses |
| `python org/devices/test_fwd8_channel_union.py` | 4 of 4 |
| `python .tools/git-hooks/one-writer-check.py --self-test` | 14 of 14 |
| `.git/hooks/pre-commit`, laptop | calls `one-writer-check.py` and fails closed (lines 207-209) |
| `python .tools/placement-check.py --self-test` | 7 of 7 |
| `python .tools/placement-check.py`, real run | 29 live projects across 2 boxes (laptop 15, sitez 14), 0 unplaced or unreadable, 26 cross-box write overlaps |

**What the 26 overlaps are.** 12 in `org/critical_paths/.open_deploys`, 4 in `org/critical_paths/change_management`, 3 in
`infra/aws/ec2`, 2 in `portal/src/pages`, and 1 each in `infra/logic/registry`, `infra/aws/terraform`, `infra/aws/lambda`
and `.tools/tests/test_gate_x_round_issuer.py`. Most are shared ledgers that every deploying project writes. That is the
read doing its job, not a defect in the tool. Whether the shared ledgers should be excluded from the overlap count is for
round 2's analysis to decide. It does not gate this grade.

**Reach.** 9365944cf5 is on origin/CLOUD. 55e20b6e03 is on the laptop's CLOUD only (fetch then is-ancestor: rc 1 on
origin, rc 0 on local HEAD), so stage 12 refuses on the laptop now and on site Z only after site Z pulls.

-- 3.0.0_SA_CVO
