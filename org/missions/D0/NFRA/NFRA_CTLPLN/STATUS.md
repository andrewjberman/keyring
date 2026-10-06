# NFRA_CTLPLN -- status

Seat `2.0.0_SA_COO~C` (CLAUDE). Contract: the PRD `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` v0.3 (v0.2 ADMITTED
both halves; v0.3 adds C-PUSH-RULE timing only). Reviewer `3.0.0_SA_CVO`. Overwritten by the seat at 15:4xZ 2026-10-06.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `coo-c-ctlpln-r1`, DIR `C:\Users\AndrewBerman\Desktop\coo-c-ctlpln` |
| Workspace candidate pin | FWD-5: `891d03c8f3`, merged as `cd69719aef`. FWD-2: `39ed9e4d83` + `f4e0945d97`, merged as `0bf062e971` |
| Portal candidate pin | n/a (round 1 touches no portal file) |
| Deployed artifact pin | NOT DEPLOYED (round 1 deploys nothing; the hook is live in every worktree at CLOUD HEAD) |
| Push state | CLOUD LOCAL @0bf062e971; origin/CLOUD e82f508eef (ls-remote read 15:1xZ). The seat never pushes `CLOUD` |

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
| FWD-2 one device register; scripts read it | LANDED (round-1 reach), ungraded; EXERCISED bar needs a new box (round 2) | `0bf062e971`. `python org/devices/test_readers.py` 8 of 8: box `dell9` added ONCE to a fixture register is listed/resolved/admitted by `agentbus-sqs.sh devices` + `device`, `remote-job.py parse_device`, `sequence-check.py box_fabric`, no script edit; NEGATIVE CONTROL the real register refuses it in all four. `test_devices.py` 0 failures, 5 of 5 mutants. Unchanged suites: `test_remote_job.py` 10 passed, `sequence-check --self-test` 32/32. Real run: queue URLs byte-identical to before; both queues exist live. Laptop `AGENTBUS_DEVICE=laptop` set + read back (HKCU) 15:4xZ; site Z asked via `0.0.0_AB_MSTR` 15:42Z. Path fallback KEPT (ruling 105617 item 3) |
| FWD-8 per-box append files; readers union them | NOT STARTED | -- |
| FWD-7 a box field on every project or workstream; placement check | NOT STARTED | -- |

## Write claims

- `2.0.0_SA_COO~C`, FWD-2 (released at `0bf062e971` except the fallback removal): `org/devices/**`, `lib/devices.py`,
  `.tools/agentbus-sqs.sh`, `.tools/remote-job.py`, `.tools/sequence-check.py`, `.tools/hooks/presence-stamp.sh` (exact files,
  ruling 105617). The fallback removal re-claims `.tools/agentbus-sqs.sh` and `.tools/sequence-check.py` when both boxes read back.
- `2.0.0_SA_COO~C`, FWD-8: scoping (no file claimed yet).

## Next proof

FWD-8: append-only files are one file per box (`<name>.<device>.md`) and the surprise-row gate and the channel compilers read
every per-box file of a channel. Proof: two per-box files of one fixture channel; the gate and each compiler see the union, and a
row id minted in both is caught. Then FWD-2's fallback removal once site Z reads back.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| FWD-2 write set | `1.0.0_SA_CTO` | ruling 105617 (batch 284): exact files, lane `NFRA_CTLPLN_FAST_C` @41d921ee40 | ANSWERED |
| the push-rule law text (FWD-6, not round 1) | Andrew | APPROVED, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_150xZ_PUSH_RULE_LAW_TEXT_APPROVED.md` @7b5782d0c6; lands WITH C-QUEUE and C-TRUNK-DEPLOY, never before (CTO msg 105615) | HELD to C-QUEUE |
| dell1 standing (round 2) | Andrew | hardware | AWAITED |
| `AGENTBUS_DEVICE=sitez` set + read back on site Z | `0.0.0_AB_MSTR~Z` via `0.0.0_AB_MSTR` | user env, HKCU read-back | ASKED 15:42Z |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| A second device list: `org/audit/archive/DEVICES.txt` (GOVERNANCE_AUDIT admission authority for `.tools/audit-archive-invoker.py`) still names `laptop`/`sitez` by hand; FWD-2's "named once" needs it derived from, or checked against, the register | `1.0.0_SA_CTO` | a third box is registered (round 2), or the CTO rules sooner |

## Limits

Nothing deploys in round 1. No outcome is PASS until `3.0.0_SA_CVO` grades it on a pinned candidate.
