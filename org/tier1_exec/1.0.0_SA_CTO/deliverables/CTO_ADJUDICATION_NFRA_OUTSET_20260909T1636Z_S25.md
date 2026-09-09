# CTO ADJUDICATION -- NFRA_OUTSET round 3, S25: the identity the device-side drift timer publishes under

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-09 ~16:3xZ · **On:** `2.0.0_SA_COO` 94569 (drive tick 13), row `NFRA_OUTSET-S25`
@`12fd0c7a72` (`0.7.0_AE_CloudOps~W`, BLOCKING/ARMED under TO-OS-s-21) · **Prior:** @`98722f9355` (S23: drift is a device property,
published on the device's own timer under a named identity with its Put reach read on the APPLIED plane), PRD v0.6 @`be662c311f`,
the identity census under OS-s-6 (the laptop holds one principal, `user/Andrew_Berman`, AdministratorAccess via its group) and
under OS-s-21 (0 of 224 roles reach `outset/*` for Put; the freshness publisher got an exact-key role).
**Standing word that bounds it:** Andrew's 2026-09-05 "recs approved" CALL 2 @`8e89f1127f` -- ambient box credentials accepted *"as (a)
for now, a STANDING ITEM to be named in the next PRD"*; his ~12:5xZ word today (OUTSET adjudications move; no new work before the transcript).

---

```
+-- CALL 1 of 1 -- S25 --------------------------------------------------+
  **Under which NAMED identity does the laptop's drift timer publish
  outset/laptop/comp_heat_drift.json? The laptop holds one principal, the
  admin user; the face disqualifies ambient admin reach; no timer exists,
  and the hand artifact turns SILENT ~2026-09-10T17:55Z.**
  (a) a new IAM user with long-lived keys; (b) publish via git and a cloud
  role; (c) a hand publish as this round's cadence; (d) a scoped role
  assumed from the principal the device already holds.
  --------------------------------------------------------------------
  **REC -- (d).** One role in estate-report/iam.tf under safe-apply: trust
  = user/Andrew_Berman as sole assumer; permissions = s3:PutObject on the
  one key. The scheduled task assumes it and Puts under the role session.
  A named publisher, the CloudTrail actor a role session, no new long-lived
  credential on the laptop. Fallback: (c) for round 3 with a PRD line
  naming the manual cadence, the identity a round-4 cell.
  --------------------------------------------------------------------
  **RULING -- (d) ADOPTED, with five sharpenings; (a) and (b) refused;
  (c) stays the honest QA interim until the timer's first fire, never the
  cadence and never the exercise.**
+---------------------------------------------------------------------+
```

## WHY (d), and what it does and does not change about the device's posture

The question S23 asked was *which identity PUBLISHES*, so that the artifact's writer is a named principal whose reach is read on
the applied plane and whose CloudTrail actor is not an admin user. (d) answers exactly that: the publish is performed by a role
session whose only permission is one Put on one key, assumable by one principal. **It does not change the ROOT of trust** -- the
admin user's long-lived keys are already on this laptop and stay there -- and the ruling says so plainly rather than letting a
scoped role read as a hardening it is not. That root is the laptop instance of the STANDING ITEM Andrew accepted on 09-05 (ambient
credentials, *"as (a) for now"*), and it is carried under that item, not solved here. (d) narrows what publishes without widening
what is stored; that is the whole of its merit and it is enough for the face's clause as written.

(a) adds a second standing credential beside the admin one for no gain in naming -- refused. (b) makes the drift vintage the
commit's and puts a push on every daily publish -- refused; a device's dirty tree is precisely what is not in git. (c) is honest and
fails the spec's own *"on that device's OWN timer"*; it stays the QA interim until the timer's first fire, and is never the cadence
and never the exercise (a hand publish is QA -- the S23 ruling, unchanged).

## THE FIVE SHARPENINGS

1. **ONE ROLE PER DEVICE, keyed to its own device segment.** The role is `outset-drift-publisher-laptop` (site Z gets its own when the
   roadmap allocates it), and its single statement is `s3:PutObject` on `outset/laptop/comp_heat_drift.json` -- no List, no Get, no
   other key -- so a device cannot write another device's row. The trust policy names the assuming principal by ARN and nothing
   wider; session duration the minimum the SDK allows; **a FIXED role session name** (`outset-drift-laptop`) so CloudTrail reads the
   device from the actor without parsing.
2. **THE ARTIFACT CARRIES ITS PUBLISHER.** Beside `device`, `tree_root`, `git_head` and the denominators (S23), the artifact carries
   `publisher_arn` = the assumed-role session ARN, so the consumer and the grader can match the artifact to CloudTrail's PutObject
   by the same actor at the same second. The accept's applied-plane evidence is then three reads on three planes: `iam:GetRolePolicy`
   on the role (DESIRED == APPLIED, the one key), CloudTrail's PutObject by the role session on that key at the fire (EXERCISED), and
   the served group A naming `laptop` with an n equal to the device's own porcelain count at `git_head` (S23's control).
3. **THE TIMER FIRES BEFORE THE 13:00Z RUN, EVERY DAY, AND ITS FAILURE READS FAILED.** A Windows scheduled task under the user's own
   scheduler, firing daily at a fixed hour ahead of 13:00Z; it runs `comp-heat drift --json` on the workspace tree resolved by
   `git rev-parse --show-toplevel` (never a hardcoded path -- LD-0405; the device-ness lives in the fabric key, not in a path), then
   the seam publish under the assumed role. A failed assume or Put prints FAILED and exits non-zero, and the task's last-run result
   is the local control; the consumer's 26 h ceiling is the served control (SILENT, never FRESH, when a fire is missed).
4. **NOTHING NEW IS STORED ON THE LAPTOP.** No access key is minted, written or cached by this row; the task uses the credential
   source the device already uses for every AWS act. If the device's credential source is ever moved to short-lived (SSO) credentials,
   the role's trust policy is the one line that follows it; the task does not change.
5. **THE DEVICE TOUCH IS INFORMATION TO ANDREW, NOT A GATE** -- as the COO proposed: one line at the COO terminal before the task is
   installed, with the exact command line and the one-line removal recorded in the deliverable (a scheduled task is recoverable; the
   Agent Autonomy clause reserves confirmation for the unrecoverable). The face's BOUNDS carry it.

## WHERE IT LANDS

- **Now, the COO's:** the amendment to TO-OS-s-21's face carrying this ruling (the role's name and single statement, the fixed
  session name, `publisher_arn` on the artifact, the fixed hour, the failure reading, the removal line), S25 dispositioned and
  disarmed, the GO to `0.7.0_AE_CloudOps~W` citing the order. The role lands in `estate-report/iam.tf` under `safe-apply` with a
  NEVER-2 entry, the same shape as the freshness publisher's exact-key grant.
- **At round 3's L10 (this seat's):** OS-s-21's PRD row gains `publisher_arn` and the per-device role in its accept; no PRD bump now
  (the identity is a clause inside the row the face already carries, and a version per call is the wrong cadence).
- **Timing, stated so it is not discovered:** the hand artifact (published 15:55Z 09-09) reads FRESH at tomorrow's 13:00Z run and
  turns SILENT ~17:55Z; the first EXERCISED drift read is the first 13:00Z run preceded by a timer fire, 2026-09-11 at the earliest.
  Tomorrow's served day still grades OS-s-20 (group A on) and the freshness half of OS-s-21 if the publisher fires at 12:30Z.

## WHAT THIS RULING DOES NOT DO

Harden the laptop's root of trust (the standing item, carried) · mint any credential · touch the freshness publisher's role or key ·
change O21-AC2 · install anything (the loop cuts it; Andrew's "no new work" stands -- this is an adjudication on a placed row) ·
move the push (Andrew's 16:2xZ word is with MSTR).

## Push state
LOCAL on commit; origin/CLOUD @`58adeff90c` by the COO's ls-remote at 16:32Z, re-read at this seat's next act; LD-0522's window is
MSTR's on Andrew's 16:2xZ word.
