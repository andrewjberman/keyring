# COMM_ASSIST through muse -- Andrew works his assistant from his tailnet VM, fed by a dell2 summary folder (L1 brief, MIDSTREAM)

**Author:** `4.0.0_SA_CRO` (laptop), 2026-10-13 ~14:4xZ. **Mode:** `--midstream COMM_ASSIST` (D9/COMM, placed on site Z).

**Commissioned by Andrew** (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`),
VERBATIM:

> *"we should ultimately aim to set up COMMS_ASSIST in a manner that I can handle most of it through "muse" on tailnet. Muse does
> not have AWS CLI, which means that information needs to be placed somewhere it can read, I think this can be hosted on DELL2 ...
> some kind of script that pulls open-calls and other summary info from AWS that muse would need on some local schedule to DELL2
> local for muse to access through SSH. ... Muse is a lot more user friendly/intelligence than Kimi, because the Quo-phone line
> approach is a little rigid and unintelligent compared to coming up with a muse-focused solution."*

**Consumer:** COMM_ASSIST's CTO on site Z (`1.0.0_SA_CTO~Z`) at L2 as a PRD addendum, through `0.0.0_AB_MSTR`. The laptop
`1.0.0_SA_CTO` rules the cross-box parts (a dell2 host for a site Z project; the SSH path owned by NFRA_CTLPLN FWD-27).

---

## PART 0 -- HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

- **Read:** COMM_ASSIST's `project.json` name and description; the PRD's four outcome headlines (FWD-1 to FWD-4); the served
  reality. The served reality covers:
  - the assistant's code event routes (`data/transcripts/scripts/teams_chat/tenant.py:929-934`);
  - its DynamoDB state row for today's End of Day post, read live today for an unrelated ask.
- **Not read:** COMM_ASSIST's task orders, decompositions, `phase` or `blocking`.
- **Where it bent:** this seat had already seen two of COMM_ASSIST's open acts on the cluster open-calls list today:
  - one channel @mention to exercise FWD-3;
  - one colleague mail to exercise FWD-4.

  They are status, not outcomes. They enter only Part VI.
- **Endpoint:** this brief does NOT re-open COMM_ASSIST's endpoint. It adds a way for Andrew to work the same assistant from a
  second place. The four existing outcomes stand unchanged.

## PART I -- THE OUTCOME TERRITORY

### O1 -- THE CANDIDATE THREAD: in muse, Andrew asks "what is waiting on me?" and gets the answer from a folder on dell2
- **What he sees:** the cluster's open calls and acts, the drafts waiting for his answer, and today's End of Day draft with its
  send time.
- **How it gets there:** muse reads them over tailnet SSH from a folder on dell2. A dell2 script refreshes that folder from AWS on
  a local schedule.
- **Grain:** one person (Andrew), one box (dell2), one question, read-only. This is FWD-1 of the addendum.

### O2 -- From muse, Andrew answers a waiting draft: send it, drop it, or redraft it with his notes
The answer has the same effect as his "1" / "0" / notes by text today: the assistant posts or drops the item as it does now.
Nothing goes out in his name without his answer, from either place.

### O3 -- From muse, Andrew settles the approvals that are his
- ad hoc work arriving over Teams/Outlook: who takes it, "at my discretion over that COMMS_ASSIST channel" (Andrew, ~14:0xZ);
- portal feature approvals (NFRA_DEVPLN decision c);
- a ruling on an open call.

Each reaches the box that asked, and the box's list closes on his answer.

### O4 -- Andrew can still be reached when he is away from muse, and no item is answered twice
The text path stays as the fallback. A draft answered in one place reads as answered in the other.

### O5 -- Everything muse shows says how old it is and what could not be read
A summary that could not refresh, or a source it could not reach, says so. It is never shown as "nothing waiting". Absent is not
empty.

### O6 -- muse holds no cloud credentials, and the dell2 folder is reachable only from inside the tailnet
muse never needs AWS access. The folder carries summaries and draft text Andrew is entitled to read, not keys or tokens. SSH to
dell2 answers tailnet devices only (Andrew, ~14:0xZ: "no external ssh available").

## PART II -- WHERE THE BOUNDARY SITS

- **COMM_ASSIST owns** this addendum: the assistant (LDO-001) stays the ONE assistant. The dell2 folder is a READER of it, and the
  muse answers are a second INPUT to it. It is not a second assistant. A parallel drafter or a second copy of state would be a
  shadow pipeline, which is a standing hard stop (CLAUDE.md section 5).
- **NFRA_CTLPLN (laptop) owns** SSH between tailnet devices (FWD-27, as re-scoped by Andrew ~14:0xZ to include muse). This addendum
  relies on it.
- **dell2** hosts the folder and the refresh script on Andrew's word. dell2's seats run it. COMM_ASSIST stays placed on site Z.
- **NFRA_DEVPLN (laptop)** supplies the portal approvals O3 carries. It does not own the channel.
- **The open-calls tools** (`.tools/open-calls.py`, the per-box lists and their S3 copies) are read, not changed.
- **Not in scope:** giving muse AWS access; replacing the drafting model; any alert or push notification. The CLAUDE.md
  moratorium on new notifications stands: the folder is pulled by muse, not pushed to Andrew.

## PART III -- THE QUALITATIVE BAR

- Andrew handles most of his day's assistant work in muse without opening a phone thread. The text path is what he uses when he
  is away, not the main channel.
- When muse says "nothing waiting", that is true at the time it states. When it cannot know, it says so.
- An answer given in muse lands exactly as the same answer by text would. Andrew never has to wonder which channel "counts".
- muse becomes more useful than the phone because it can explain and compare, not because it shows more items.

## PART IV -- THE SUBSTRATE (findings, measured 2026-10-13)

- **F1 -- The assistant's state is per-item rows in DynamoDB.**
  - Table `teams-global-chat-assist-table`, one row per chat and one per day's End of Day post (`pk` = object id, `sk` = `state`).
  - `pending` holds `draft`, `version`, `status`, `send_at`.
  - Read live today for `eod:2026-10-12`: version 3, status `approved`, posted at 21:08:05Z.
  - A summary script can read these rows; muse cannot (no AWS CLI, Andrew).
- **F2 -- Answers enter the assistant as events** (`tenant.py:929-934` ROUTES). `sms.reply` carries Andrew's text answers; the
  `job.open` / `job.bid` / `job.award` / ... routes already carry the ad hoc work bid Andrew described at ~14:0xZ. A muse answer is a
  new event source into the same routes, not new logic.
- **F3 -- Open calls already have a cloud copy per box.**
  - Path: `s3://opal-313476888478-globgrph/fabric/open-calls/v1/box=<box>/open_calls.json`.
  - Reader: `python .tools/open-calls.py list --all --cloud`, which read 4 boxes, 13 open, at 14:01Z today.
  - This is the first file the dell2 folder would carry.
- **F4 -- The day's sprint page and its End of Day draft are served objects.** `s3://opal-data-portal-v2/daily-reports/<day>/`
  holds the sprint page; the draft is in the F1 table.
- **F5 -- dell2 on the tailnet.**
  - dell2 is `100.104.84.87`, role "execution" (`org/devices/DEVICES.json`).
  - Key SSH from the laptop to dell2 works today, with password login still on (`3.0.0_SA_CVO~L` re-grade, FWD-27).
  - The rollout plan's ACL admits `muse` as a source to `dell2:22`
    (`org/tier1_exec/1.0.0_SA_CTO/deliverables/LD0644_ROLLOUT_PLAN_CLUSTER_REMOTE_ACCESS_TAILNET_20261011.md` line 83).
- **F6 -- muse.**
  - `muse` is Andrew's VM at `100.113.31.20` (same plan, line 16).
  - It authored the 2026-10-10 cluster remote-access document recorded as LD-0644, and it already reaches boxes over the tailnet
    (RDP via a Python TCP tunnel).
  - It has no AWS CLI (Andrew).
- **F7 -- dell2's AWS identity is narrower than the laptop's.** Today it is denied `kms:Decrypt` on the IRPT key (routed to the CTO
  today for a grant). Whether it can read the F1 table and the F3 bucket is NOT measured. The refresh script needs exactly those
  reads.
- **F8 -- The text path today:** Kimi drafts each item; the assistant texts it to Andrew's phone and accepts replies only from that
  number.

## PART V -- WHAT MUST BE TRUE (named, not sequenced)

- dell2's identity can read the F1 rows, the F3 lists and the F4 objects, scoped read-only. The grant is the laptop's to make
  (NFRA_CTLPLN C-ROLE-REQUEST).
- SSH from muse to dell2 works by key, tailnet-only, with password login off (NFRA_CTLPLN FWD-27).
- A folder on dell2, with a fixed layout muse is told once, and a refresh on a local schedule that stamps each file's read time.
- A way for a muse answer to reach the assistant's event routes (F2), carrying who answered and which draft version, so an answer
  to a stale version is refused as the text path refuses one.
- A rule for the two channels on one item: first answer wins, the other channel shows it answered (O4).
- What muse is told about its role: it may read and answer Andrew's own items and nothing else.

## PART VI -- STATUS (NOT OUTCOME-BEARING; measured 2026-10-13 ~14:0xZ-14:4xZ)

- COMM_ASSIST is active, placed on site Z, with 4 outcomes.
- Two of its open acts wait on Andrew: one channel @mention (17h) and one colleague mail (59h).
- The End of Day post of 2026-10-12 went out at 17:08 ET through the text path, version 2.
- Nothing exists on dell2 for muse today, and no folder is named.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- How muse itself is built, what model it runs, and what it can run on its own VM were not inspected. It is treated as a tailnet
  client that can SSH and read files.
- dell2's AWS read permissions for F1, F3 and F4 were not tested.
- The text path's sender check and its version rule were read only at the route level, not line by line.
- No refresh interval is proposed. Andrew said "some local schedule", and a number here would be invented.
- Whether Andrew wants muse to DRAFT (replacing Kimi) or only to read and answer is not settled; it is open decision 2.

## OPEN DECISIONS FOR ANDREW (each with the CRO's recommendation)

1. **muse beside the phone or instead of it.** (a) muse is primary and the text path stays as the away-from-desk fallback;
   (b) the text path is retired.
   **REC (a)**: your words were "most of it", and the fallback costs nothing once O4's first-answer rule exists.
2. **Who drafts.** (a) Kimi keeps drafting inside the assistant, and muse reads, explains and answers (notes trigger a redraft as
   today); (b) muse writes the drafts itself.
   **REC (a)** first: it changes one thing at a time and keeps one voice file. Move to (b) once muse answering is proven.
3. **How a muse answer gets back.** (a) muse writes an answer file into the dell2 folder over SSH, and a dell2 job forwards it to
   the assistant; (b) a small tailnet-only web endpoint on dell2.
   **REC (a)**: it opens no new listener and uses the same SSH path and folder.
4. **Host box.** (a) dell2 as you said; (b) the laptop.
   **REC (a)**: it keeps the laptop to planning, and dell2 already runs scheduled jobs. It needs F7's read grant.

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/comm-assist-through-muse-midstream-brief-20261013.md
  PROJECT           COMM_ASSIST (D9/COMM, placed sitez) -- PRD addendum, not a new project
  EXISTING PRD      org/missions/D9/COMM/COMM_ASSIST/prd/COMM_ASSIST_PRD.md
  SIBLING PROJECTS  NFRA_CTLPLN (FWD-27 SSH, C-ROLE-REQUEST grants), NFRA_DEVPLN (approvals carried)
  PRIOR ART         LDO-001 event routes incl. job.bid/award (F2); open-calls S3 copies + reader (F3); LD-0644 rollout
                    plan with muse in the ACL (F5, F6)
  MEASURED AT       2026-10-13 ~14:0xZ-14:4xZ UTC, laptop
```
