# NFRA_CTLPLN PRD v0.1 -- ratified-text half review (3.0.0_SA_CVO, 2026-10-06 13:36Z by `date -u`)

Delivered by `1.0.0_SA_CTO` msgs 105566 and 105567. PRD `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md`
@2283d5afd7 (v0.1), half hash 0f3586621975. Read whole. The brief half is admitted (the CRO wrote the brief).

**Verdict: SIGN.**

| check | this seat's read | result |
|---|---|---|
| ENDPOINT against the pin | the twelve blocks against `ENDPOINT_FORWARD_FOUR_DEVICE_CONTROL_PLANE_20261006.md` @1641471f2c, whitespace normalized: 11 of 12 identical; FWD-4 differs only in its SOURCE line, which adds "Andrew's confirmation (headline wording)" | PASS |
| the pin is ratified | Andrew at the CRO terminal, VERBATIM "im good with all of this", the record listing what was before him: FWD-1 to FWD-11 as proposed, FWD-4's headline "per lane", FWD-12 added, register under D0 and start FWD-5 first. FWD-4's headline reads "no lane falls more than one round behind"; FWD-12 is present | PASS |
| no annotation, history or seat name inside the section | 0 seat serials, 0 history words in the block | PASS |
| measured claims re-read here | `.tools/git-hooks/pre-push-safe-deploy.sh:41-70` runs `safe-deploy.sh --commit-range` for every pushed ref that is not a delete or a tag, as stated. `.tools/agentbus-sqs.sh:84-86` hardcodes `laptop` and `sitez` and `:157-158` infer the device from the profile path, as stated | PASS |
| builder output | `name()` re-run here: `agentbus-global-dell1-queue`, `cloudops-global-dell1-agent-role` reproduce; the `.fifo` suffix is left to a registry change, as C-BUS says | PASS |
| every operative constraint present | a publish never deploys (C-TRUNK-DEPLOY, FWD-5 first); one trunk writer and the push rule changed only by Andrew's exact text (C-PUSH-RULE); identity set at bring-up, never from a path (C-REGISTRY, LD-0405); the Dells refused by policy (C-IDENTITY); builder names (C-NAMES); no alerts (C-MORATORIUM); no parallel bus (C-NO-SHADOW) | PASS |
| cited files | the brief, the proposal and the per-box file precedent `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` exist | PASS |

**Notes (not conditions).**
1. Andrew's question in the same record -- how work is spread as projects come online, and how a heavy mid-stream project
   moves when one box can no longer hold it -- is answered by the CRO as a recommendation. The PRD carries it only as
   C-PLACEMENT's "each move is his when it happens". A rule for moving a project in flight is not stated.
2. C-TRUNK-DEPLOY deploys on site Z's push of the trunk, and FWD-6 makes that push wait for Andrew when the round carries
   a pipeline script. Until the law text lands, the current rule stands (C-PUSH-RULE); the two agree.
3. Round 1 is exercised on two boxes; FWD-1, the thread, waits for dell1, as Andrew ordered.

-- 3.0.0_SA_CVO

## Addendum 14:21Z -- v0.2 @d2231e70d8 (msgs 105587, 105588, half hash 26177213656d): SIGN

The diff against v0.1 @2283d5afd7, read whole: FWD-3 and FWD-7 amended in place, FWD-13 added; contracts C-SERIALS and
C-BID; manifest S13. The other ten outcomes are byte-equal.

| check | read | result |
|---|---|---|
| FWD-3 within his word | "only the MSTR agents are the ones that communicate between boxes"; the outcome routes every cross-box message seat to own-box fabric manager to other-box fabric manager to seat, and keeps the read proof | PASS |
| FWD-7 within his word | "Yes CTO moves a project or workstream"; the placed unit becomes "project or workstream". The SOURCE says this is the CRO's stated reading, not corrected by him | PASS (note 4) |
| FWD-13 within his word | the CTO elects, the box's fabric manager runs the bid, "agreed on all points go ahead"; between rounds only, nothing lost, the box with the most room by measured load | PASS (note 4) |
| C-SERIALS, C-BID against the second record | one CTO on the laptop; `~DELL1`, `~DELL2`, `~SITEZ` with `~Z` kept as an alias; the laptop's fabric manager awards a move, LDO-001 keeps Teams remote jobs | PASS |
| cited code | `.tools/remote-job.py:38` `DEVICES = ("laptop", "sitez")`; `:80-81` CPU and memory through `psutil`; no disk or storage read, as stated | PASS |
| form | no seat serial and no history clause in the block ("can no longer hold its work" is the outcome's plain wording) | PASS |

**Note 4.** FWD-7's workstream unit and FWD-13 rest on the CRO reading his "Yes" as covering both, written in the record
and "not corrected by him", followed by his "agreed on all points go ahead". This seat reads that as his word. A one-line
read-back would make it explicit.

-- 3.0.0_SA_CVO
