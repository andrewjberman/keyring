# NFRA_CTLPLN -- status

Seat `2.0.0_SA_COO~C` (CLAUDE). Contract: the PRD `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` v0.3 (v0.2 ADMITTED
both halves; v0.3 adds C-PUSH-RULE timing only). Reviewer `3.0.0_SA_CVO`. Overwritten by the seat at 15:2xZ 2026-10-06.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `coo-c-ctlpln-r1`, DIR `C:\Users\AndrewBerman\Desktop\coo-c-ctlpln` |
| Workspace candidate pin | FWD-5: `891d03c8f3` (branch), merged on CLOUD as `cd69719aef` |
| Portal candidate pin | n/a (round 1 touches no portal file) |
| Deployed artifact pin | NOT DEPLOYED (round 1 deploys nothing; the hook is live in every worktree at CLOUD HEAD) |
| Push state | CLOUD LOCAL @cd69719aef; origin/CLOUD e82f508eef (ls-remote read 15:1xZ). The seat never pushes `CLOUD` |

## Mode

FAST lease, armed by `1.0.0_SA_CTO` on Andrew's word ("Let's bring on COO~C to take it on, /closer-drive instruction"), seat
`2.0.0_SA_COO~C`, until 18:43Z. Surface: `.tools/git-hooks`, `org/missions/D0/NFRA/NFRA_CTLPLN`, `org/devices`. FULL -> FAST
boundary run 15:05Z: no task order was open, nothing cut; CVO told (msg to `3.0.0_SA_CVO`, 15:08Z).

## Live thread

State: NOT LIVE. FWD-1 (one real round laptop -> dell1 -> site Z -> laptop) needs dell1, which is not delivered.
Round 1 is the PRD's section 2 list, exercised on the two boxes that exist.

## Acceptance IDs (round 1)

| ID | State | Evidence |
|---|---|---|
| FWD-5 the push gate deploys only on `refs/heads/CLOUD` | LANDED, ungraded | `cd69719aef`; `bash .tools/git-hooks/test-pre-push-safe-deploy.sh` 14 of 14 PASS on the shared tree: 11 fed-stdin cases, 2 REAL `git push` runs to a local bare remote (work branch: 0 deploy calls; CLOUD: 1), and a negative control (the origin/CLOUD pre-FWD-5 hook deploys on the work-branch push). HALTGT block unchanged. No push to origin made |
| FWD-2 one device register; scripts read it | BUILDING | -- |
| FWD-8 per-box append files; readers union them | NOT STARTED | -- |
| FWD-7 a box field on every project or workstream; placement check | NOT STARTED | -- |

## Write claims

- `2.0.0_SA_COO~C`: FWD-2 -- `org/devices/DEVICES.json` and its test (in lease). The readers outside the lease (below) wait on the
  `1.0.0_SA_CTO` answer to the write-set ask (15:20Z).

## Next proof

FWD-2 (round-1 reach: the two existing boxes; the EXERCISED bar needs a new box, so it closes in round 2): one register file holds
each box's name, role, inbound queue, seat limit and lane letters; the measured device-naming scripts read it
(`comp-find '\bsitez\b'`, 52 hits / 1,246 files: `.tools/agentbus-sqs.sh`, `.tools/remote-job.py`, `.tools/sequence-check.py`,
`.tools/audit-archive-invoker.py`, `.tools/hooks/presence-stamp.sh`, `.tools/tests/test_remote_job.py`). Proof: add a fixture box to
a copy of the register and show every reader lists it with no script edit. Identity comes from the user env `AGENTBUS_DEVICE`, which
is UNSET on the laptop today (read 15:2xZ): it is set on each box before any reader drops the path fallback.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| FWD-2 write set: register home + lease widened to the readers | `1.0.0_SA_CTO` | msg 15:20Z | ASKED |
| the push-rule law text (FWD-6, not round 1) | Andrew | APPROVED, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_150xZ_PUSH_RULE_LAW_TEXT_APPROVED.md` @7b5782d0c6; lands WITH C-QUEUE and C-TRUNK-DEPLOY, never before (CTO msg 105615) | HELD to C-QUEUE |
| dell1 standing (round 2) | Andrew | hardware | AWAITED |
| `AGENTBUS_DEVICE` set on site Z | `0.0.0_AB_MSTR~Z` | user env | NOT ASKED (after the write set) |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| The box key spelling: scripts and the bus say `sitez`, C-PLACEMENT's `fabric` enum says `site-z` | `1.0.0_SA_CTO` | the FWD-7 item starts (the register carries `sitez` with alias `site-z` until then) |
| Laptop seat limit: C-ROLES says at most one execution lane; Andrew's standing word is at most three COO sessions (four for IRPT) | `1.0.0_SA_CTO` | the register's `seat_limit` field is read by a gate |

## Limits

Nothing deploys in round 1. No outcome is PASS until `3.0.0_SA_CVO` grades it on a pinned candidate.
