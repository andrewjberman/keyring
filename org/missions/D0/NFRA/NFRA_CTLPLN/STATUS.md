# NFRA_CTLPLN -- status

Seat `2.0.0_SA_COO~C` (CLAUDE). Contract: the PRD `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` v0.3 (v0.2 ADMITTED
both halves; v0.3 adds C-PUSH-RULE timing only). Reviewer `3.0.0_SA_CVO`. Overwritten by the seat at 16:3xZ 2026-10-06.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `coo-c-ctlpln-r1`, DIR `C:\Users\AndrewBerman\Desktop\coo-c-ctlpln` |
| Workspace candidate pins | FWD-5 `891d03c8f3` -> CLOUD `cd69719aef`. FWD-2 `39ed9e4d83` + `f4e0945d97` -> CLOUD `0bf062e971`; fallback drop `71b27096f4` -> CLOUD `9365944cf5`. FWD-8 `96d8fc907e` + FWD-7 `ed7e23c2a2` -> CLOUD `55e20b6e03` |
| Portal candidate pin | n/a (round 1 touches no portal file) |
| Deployed artifact pin | NOT DEPLOYED (round 1 deploys nothing). Live on this box: the pre-push hook (FWD-5), the readers (FWD-2) and pre-commit stage 12 (FWD-8, installed 16:3xZ) |
| Push state | origin/CLOUD `66b1b42a71` (ls-remote read 16:3xZ) carries FWD-5 and FWD-2 through `9365944cf5`; `55e20b6e03` (FWD-8, FWD-7) is LOCAL. The seat never pushes `CLOUD` |

## Mode

FAST lease, armed by `1.0.0_SA_CTO` on Andrew's word ("Let's bring on COO~C to take it on, /closer-drive instruction"), seat
`2.0.0_SA_COO~C`, until 18:43Z. Surface: `.tools/git-hooks`, `org/missions/D0/NFRA/NFRA_CTLPLN`, `org/devices`, plus exact files by
ruling 105617. FULL -> FAST boundary run 15:05Z: no task order open, nothing cut; CVO told 15:08Z.

## Live thread

State: NOT LIVE. FWD-1 (one real round laptop -> dell1 -> site Z -> laptop) needs dell1, which is not delivered.
Round 1 is the PRD's section 2 list, exercised on the two boxes that exist.

## Acceptance IDs (round 1)

| ID | State | Evidence |
|---|---|---|
| FWD-5 the push gate deploys only on `refs/heads/CLOUD` | PASS (`3.0.0_SA_CVO`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_CTLPLN_PINS_GRADE_20261006.md`) | `cd69719aef`; `bash .tools/git-hooks/test-pre-push-safe-deploy.sh` 14/14 incl. 2 REAL pushes to a local bare remote and a pre-FWD-5 control. Live on site Z only after it pulls |
| FWD-2 one device register; scripts read it | PASS at round-1 reach (CVO, same file, graded at `0bf062e971`); fallback drop `9365944cf5` landed after the grade, ungraded. EXERCISED bar (a new box, a seat started on it) is round 2 | `org/devices/DEVICES.json`; `python org/devices/test_readers.py` 15/15 (fixture box added once and read by `agentbus-sqs.sh devices`/`device`, `remote-job.py`, `sequence-check.py`; real-register control; fresh-process cases: unset refuses with no path derivation, persisted user setting read by a shell older than the setting, pre-drop control derives from the path). `AGENTBUS_DEVICE` read back: laptop `laptop` (HKCU, 15:4xZ), site Z `sitez` (relayed 105620) |
| FWD-8 per-box append files; readers union them | LANDED `55e20b6e03`, ungraded; stage 12 INSTALLED. EXERCISED bar (two boxes, one full round each, no conflict) is round 2 | read half: `python org/devices/test_fwd8_channel_union.py` 4/4, no reader edited. Write half: `.tools/git-hooks/one-writer-check.py --self-test` 14/14; real paths graded (ETFS_INGEST `v1.Z.md` BLOCKED on laptop, OK as sitez). Census: 1,458 append-only files, 66 suffixed, all `.Z` site Z. LIVE HOOK: a safe-commit of a one-byte edit to `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` on the laptop was REFUSED by stage 12 (HEAD unchanged, edit reverted) |
| FWD-7 a box field on every project or workstream; placement check | LANDED `55e20b6e03`, ungraded | the field exists on 37 of 37 `project.json`; `python .tools/placement-check.py --self-test` 7/7; real run: 29 live projects, laptop 15, sitez 14, 0 unplaced, 23 cross-box write overlaps (parked below) |

## Write claims

None open. Round-1 files released at `55e20b6e03`.

## Next proof

Round 1 is built. The CVO's grade of `9365944cf5` (FWD-2 fallback drop) and `55e20b6e03` (FWD-8, FWD-7) is the next read. Round 2
(FWD-1 thread with FWD-3, FWD-10) needs dell1 standing; nothing after round 1 is cut ahead of it.

## Lane-letter rules to align with the device-name suffix (ruling 105634; the CTO lands any that are its own)

| Where | What it says today | Owner |
|---|---|---|
| `org/ref/SURPRISE_CHANNEL_PROTOCOL.md:114` | site Z's per-fabric file is `INVESTIGATION_v<N>.Z.md` beside the laptop file | `3.0.0_SA_CVO` (last author @a83dca303f; `org/ref/**` lane ANY_EXEC) |
| `org/ref/SURPRISE_CHANNEL_PROTOCOL.md:140`, `:181` | adjudication / remediation files: `.Z.md` on site Z | same |
| `org/ref/SURPRISE_CHANNEL_PROTOCOL.md:309` | "site Z writes `INVESTIGATION_v<N>.Z.md`; the same for adjudication and remediation files" | same |
| `org/ref/SURPRISE_CHANNEL_PROTOCOL.md:125` | row ids carry the fabric coordinate `<CODE>-Z-S<n>` on site Z (lane-letter grain; a dell has no coordinate yet) | same; the gate half is `.tools/surprise-row-gate.py` (`_row_is_other_fabric`) |
| `.owned-paths.yaml:1869` (note) | names `INVESTIGATION_v{N}.Z.md` as the site Z file | `2.0.0_SA_COO` as registry grantor; `1.0.0_SA_CTO` |

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| laptop merge window CLOSE | `0.0.0_AB_MSTR` | msg 105643: CLOSED, origin `66b1b42a71` | DONE |
| the push-rule law text (FWD-6, not round 1) | Andrew | APPROVED, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_150xZ_PUSH_RULE_LAW_TEXT_APPROVED.md` @7b5782d0c6; lands WITH C-QUEUE and C-TRUNK-DEPLOY, never before (CTO msg 105615) | HELD to C-QUEUE |
| dell1 standing (round 2) | Andrew | hardware | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| A second device list: `org/audit/archive/DEVICES.txt` (GOVERNANCE_AUDIT admission authority for `.tools/audit-archive-invoker.py`) still names `laptop`/`sitez` by hand; FWD-2's "named once" needs it derived from, or checked against, the register | `1.0.0_SA_CTO` | a third box is registered (round 2), or the CTO rules sooner |
| `.tools/direct-act-order.py:316` picks the channel file to append by `INVESTIGATION_v(\d+)\.md$`, so off the laptop it appends to the laptop's file (the FWD-8 stage WARNs, does not block) | `1.0.0_SA_CTO` (owner of the tool's lane to name) | C-QUEUE, when the unsuffixed WARN becomes a BLOCK |
| 23 cross-box write overlaps from `.tools/placement-check.py` (mostly `org/critical_paths/.open_deploys` and `change_management`; also `infra/logic/registry` LGIC_ENFORCE/AMGT_RESAPP, `infra/aws/ec2/EC2_MANIFEST.json`, broad `portal` and `.tools/tests` paths) | `1.0.0_SA_CTO` | the CTO places or splits them, or rules the deploy-ledger directories a shared register |

## Limits

Nothing deploys in round 1. No outcome is PASS until `3.0.0_SA_CVO` grades it on a pinned candidate.
