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
