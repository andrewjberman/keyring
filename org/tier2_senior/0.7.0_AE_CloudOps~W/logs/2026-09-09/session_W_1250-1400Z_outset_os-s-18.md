# Session log -- `0.7.0_AE_CloudOps~W`, 2026-09-09 12:50Z -> 14:00Z

**Scope:** `NFRA_OUTSET.TO-OS-s-18` (THE PUBLISH), resumed after the 2026-09-05 device crash.
`TO-OS-s-19` sequenced behind it and not started in this window.
**Branch:** `CLOUD`, main tree. **Respawned** by `2.0.0_SA_COO` at 12:50:19Z.

## What happened, in order

1. `/watcher` -- registration was absent after the crash. Re-registered; armed the persistent inbox
   Monitor (task `bz73i3lic`). No watcher process existed for this serial, so this was a genuine
   fresh arm and not a duplicate over a survivor.
2. Read the issuer's two messages (94459 the GO, 94465 the SPAWN-DIRECT resume) and both faces.
3. Committed the crash-orphaned `iam.tf` edit (`54ccbdb47d`), then `safe-apply` with the HALT gate
   acknowledged. Five pending messages surfaced at the gate, all 5-8 days old, all addressed to the
   BASE serial, none STOP-class, none naming this project's surfaces.
4. Published two seam artifacts, wrote and ran the `O18-AC1` battery, measured `O18-AC2` on three
   planes, and caught the runner box UP for its 09:00 run -- which made the EXERCISED reading
   possible at all.
5. Hit a lane refusal committing the battery. Censused the whole write surface, filed
   `NFRA_OUTSET-S18` (BLOCKING) plus `S16` and `S17`, and reported.
6. The issuer ruled remedy (c) at `cb43d05200` within ten minutes. Moved the battery, re-ran, filed
   the disarm ack `S19`, flipped the order.

## The three things worth carrying out of this window

**The publish, the grant and the read are three different claims and I measured them as three.**
DESIRED is the terraform source; APPLIED is the census; EXERCISED is the role itself making the
call. Only the third answers "can the runner read the seam", and it was available for eleven minutes
because the box self-stops. Had I run an hour later the honest answer would have been NOT-EVALUATED.

**A hardcoded root depth is the one line that cannot survive its own relocation.** The battery
resolved the workspace as `parents[2]`, correct where it was cut and wrong six levels down -- and it
would have failed as a WRONG ROOT with every derived path missing, not as an obvious move error.
Replaced with `git rev-parse --show-toplevel` plus a marker-walk fallback. The estate's own rule
already said this; I wrote the hardcode anyway because at the original path it was true.

**A `<paths>` block is a grant only for a worker serial.** `owned-paths-validate.py:123` matches
`^0\.9\.0_WK_<CODE>[~_]<n>$` and `:387` gates the whole additive clause on it. For a seat the block
can only narrow what the lane registry permits, never widen it. Round 1's batteries reached
`.tools/tests/` through workers, which is why the collision first appeared when round 2 seated the
same cells on a seat. Filed as `S18`; the issuer moved the invocation path rather than widening the
registry, because a lane member keyed to a serial goes stale when the serial is re-scoped.

## Rows filed

| Row | Class | Standing | Subject |
|---|---|---|---|
| `NFRA_OUTSET-S16` | OBSERVATION | ARMED | `ESTATE_OUTSET_SEAM_PREFIX` is set nowhere in terraform, so the consumer never looks at the seam. Setting it replaces the instance. |
| `NFRA_OUTSET-S17` | OBSERVATION | ARMED | The publish has no cadence; the artifact goes STALE at 26 h, so the seam's steady state as cut is FAILED. |
| `NFRA_OUTSET-S18` | BLOCKING | ARMED -> disarmed | Three granted paths unwritable by this seat; two are the `<invocation>` targets of `O18-AC1` and `O19-AC1`. |
| `NFRA_OUTSET-S19` | OBSERVATION | INERT | Disarm ack for `S18` on `cb43d05200`, verified at this seat on the face at HEAD. |

## Judgment calls, and what I declined

- **Declined `GIT_COMMIT_AUTHOR_OVERRIDE`** to force the battery into `TOOL_BATTERIES`. That lane is
  built so gate and author are different seats, with the CTO gating; an author overriding into it
  collapses exactly that separation.
- **Declined to set `ESTATE_OUTSET_SEAM_PREFIX`.** My `<paths>` reach the file, so this is not a cut
  defect and I did not claim one. `user_data_replace_on_change = true` makes it an instance
  replacement, which neither criterion asks for.
- **Declined to build a publish schedule.** Standing moratorium.
- **Declined to start the box** for a greener `A1` arm. Starting it fires a full report run with the
  old runner; a NOT-EVALUATED arm is cheaper and more honest than a manufactured one.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-iam` | `comp-iam refresh-census` | rc=0. `docs/briefs/cmpaws-iam-census-20260909.json`, generated 13:00:19Z, 224 roles / 1 group / 7 users, api `iam:GetAccountAuthorizationDetails`. Run BEFORE any applied-plane use per the 24 h TTL. Its own `managed_policies_resolved=false` is what forced the UNRESOLVED qualifier on the seventh statement. |
| `comp-read` | `comp-read estate_report_runner.py --enumerate 'ESTATE_OUTSET_SEAM_PREFIX\|_outset_read\|OUTSET_ANSWER_STATE_TO_STATUS'` | 12 hits across 2860 lines / 78 sections, 11 whole / 1 substring, bands DOCSTRING 1 COMMENT 1 DEF 1 CODE 9. Located the consumer half and the exact key composition at `:1844`. |
| `comp-read` | `comp-read instance.tf --enumerate 'user_data\|resource "aws_instance"'` | 11 hits / 277 lines. Found `user_data_replace_on_change = true` at `:83`, which is what turned `S16` from a one-line config note into an instance-replacement finding. |
| `comp-find` | `comp-find 'ESTATE_OUTSET_SEAM_PREFIX' infra/` | DENOMINATOR 5 hits across 11,398 files scanned, corpus=all. All five inside the runner; ZERO under `infra/aws/terraform/`. The denominator is the whole point of the `S16` claim. |
| `comp-find` | `comp-find --name 'TO-OS-s-1*' --limit 40` | MEASURED zero across 156,271 files, with 71,797 ephemeral-floor files disclosed as excluded. Correctly told me the orders are not named that way rather than that they were absent. |
| `owned-paths-validate.py` | `--check-agent 0.7.0_AE_CloudOps~W` over 13 paths | rc=1, 3 refused / 10 permitted. Negative control on `0.9.0_WK_NFRA_OUTSET~1` returned a different, larger set, which is what made the reading corroboration rather than a single-instrument claim. |

## State at close

`O18-AC1` PASS, `O18-AC2` recorded with no verdict for the CVO at L9, order flipped complete.
`TO-OS-s-19` next: the window is clear until 2026-09-10 13:00Z and the served runner baseline is
already measured at 125,857 B / 2026-08-25T05:36:35Z.
**Push state: LOCAL.** No push by this seat under either order's BOUNDS.
