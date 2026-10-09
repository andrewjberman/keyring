# Process report -- GitOps and the driving skills, 2026-10-09

**For:** Andrew. **By:** 1.0.0_SA_CTO (laptop), ~15:25Z.

**Window:** mainly 09:00Z-15:20Z, with the whole day from 00:00Z used where it shows a trend. Every number names its source.

**Words used:**
- **Box:** one of the four machines: the laptop, site Z, dell1 and dell2.
- **COO / CTO / CVO / CRO:** the seats that run work, rule calls, verify, and research.

---

## 1. Verdict

**Git moves a very large volume, and about one sync in four held today.**
- 3,706 commits (not counting merges) reached the shared branch `CLOUD` today.
- Of 400 sync runs, 264 finished cleanly and 95 held on a conflict or an uncommitted-file overlap.
- Every hold was cleared, most within one to two hours.

**The worst Git stretch was 12:20Z-14:20Z, and part of it was my fault.**
- A schema edit I made at 13:00Z broke every proof check on every box.
- Three boxes then repaired it independently, and their three repairs collided.
- Separately, two merges into `CLOUD` took 10 and 14 minutes, against a normal 15-60 seconds.

**The driving skills are each working, with clear weak spots:**
- **/keep-driving** is on for every box.
- **The 10-minute open-calls scan** runs on all four boxes. It missed some passes, with gaps of up to 50 minutes.
- **/canonical-drive** and **/self-drive** ran all day and produced most of the output.
- **/unblock** closed 28 of 29 files the same day. About a third were live waits rather than real blocks, and each still cost a research, ruling and review pass.

**Top fixes (section 6):**
1. Merge append-only logs by keeping both sides, on every box.
2. One owner repairs a fleet-wide defect; other boxes report it and wait.
3. Time each phase of a sync.
4. Treat a dated wait as waiting, not as a block.
5. Close the open-deploy backlog.
6. Fix the register's box fields.

---

## 2. Git operations

### 2.1 How the per-box branches work

**Each box commits to its own branch,** `box/<box>`, which only that box's manager pushes.
- **Box pass:** takes the latest `CLOUD` into the box's branch and pushes it.
- **Integrate pass:** run by the laptop manager (`0.0.0_AB_MSTR`). It merges each box's branch into `CLOUD`.

**A pass holds instead of merging in two cases:**
- **conflict:** the same lines were changed on two sides;
- **dirty-overlap:** a file it must touch has unsaved edits in the working folder.

**Pushes:** this morning's push law (`CLAUDE.md`, d92d08c448) lets agents push without your word. The one exception is a portal production push that changes a client-facing page. The push gate still decides who may push which branch; it refused my own direct push of `box/laptop` at ~13:25Z, correctly.

### 2.2 Sync runs today

Source: `org/git-author-override-audit.log`, 3,957 rows dated 2026-10-09.

| Kind of run | Clean | Failed | Skipped (another pass running) | Held | Total |
|---|---|---|---|---|---|
| Integrate into `CLOUD` | 101 | 2 | 16 | 21 | 140 |
| Box pass, laptop | 101 | 7 | 5 | 27 | 140 |
| Box pass, dell1 | 21 | 0 | 3 | 13 | 37 |
| Box pass, dell2 | 24 | 0 | 3 | 16 | 43 |
| Box pass, site Z | 16 | 0 | 5 | 18 | 39 |
| Box pass by the CRO | 1 | 0 | 0 | 0 | 1 |
| **All** | **264** | **9** | **32** | **95** | **400** |

**Why passes held** (per box; one integrate can hold several boxes):

| Cause | Count |
|---|---|
| conflict | 63 |
| dirty-overlap | 35 |
| skipped, another pass held the lock | 27 |

**The 9 failures:**
- 4 failed fetches: 01:00Z, 02:34Z, 10:12Z, 12:30Z.
- 5 laptop passes refused by a gate between 04:30Z and 04:51Z.

### 2.3 How long a sync takes

Seconds, clean and held runs:

| Hour (UTC) | Box pass: median / longest | Integrate: median / longest |
|---|---|---|
| 05 | 12 / 15 | 20 / 25 |
| 07 | 15 / 25 | 15 / 58 |
| 09 | 28 / 81 | 34 / 80 |
| 10 | 20 / 89 | 34 / 124 |
| 11 | 26 / 92 | 36 / 77 |
| 12 | 20 / **414** | 59 / **370** |
| 13 | 23 / **311** | **181 / 853** |
| 14 | 41 / **701** | 62 / 236 |

**The slowest runs:**
- integrate 13:34:21Z, 853 s, clean;
- dell1 box pass 14:05:44Z, 701 s, held;
- integrate 13:10:14Z, 607 s, clean;
- laptop box pass 12:10:50Z, 414 s;
- integrate 12:46:18Z, 371 s.

**What the slow runs cost:**
- While one integrate held the lock, four later ones were skipped (13:03Z-13:25Z), so fixes waited longer to reach `CLOUD`.
- Of the 607 s run, only about 150 s is explained (four merge checks of 21-60 s each). The rest is not measured.
- Filed as issue row **NFRA_CTLPLN-S9107** (9dda913a5b).
- By 14:22Z integrates were back to 47-57 s.

### 2.4 Commits and gates

**Commit gate: 1,528 PASS, 31 BLOCK.** Every block was a seat writing outside its lane, and the gate was right each time. The lanes refused:

| Lane | Blocks |
|---|---|
| deliverables of another project | 10 |
| test battery | 4 |
| cloud operations | 4 |
| loop mechanism | 2 |
| cross-box records | 2 |
| IRPT completion registry | 2 |
| test-file refusals | 2 |
| executive base | 1 |

**Commit timing, 1,067 two-phase commits:**

| Step | Median | 90th percentile | Longest |
|---|---|---|---|
| Gates (validation) | 13.5 s | 43.5 s | 478 s |
| After-commit hooks | 3.9 s | | |
| Hold on the shared index | 1.5 s | | |

The gates are where commit time goes.

**Overrides:**
- 19 audited author overrides.
- 19 issue-row overrides, of which 10 were honoured.
- 3 overrides of the stale-system check.

**Volume, 09:00Z-15:00Z:** 1,573 commits. The busiest authors:

| Author | Commits |
|---|---|
| dell2's CTO | 97 |
| dell1's CTO | 80 |
| the CVO | 68 |
| dell1's manager | 55 |
| COO `~R1` | 55 |
| COO `~C2` | 48 |
| COO `~D1` | 42 |
| COO `~P2` | 39 |

Most COO work now runs on the Dells.

### 2.5 Every hold today and how it was cleared

| # | When (UTC) | Box | Cause | Cleared by |
|---|---|---|---|---|
| 1 | early morning | laptop | dirty-overlap on the shared audit logs | logs committed; record allowlist widened (23ad9da6f3) |
| 2 | ~07:50Z | laptop | dell1's CTO and I both wrote LGIC_BLANKFIX's round-9 analysis | I moved mine out (a0d1d52b5b). A project placed on a box has its analysis written by that box's CTO |
| 3 | ~09:00Z | laptop, 320 behind | the laptop CVO graded dell1's round 9 and wrote a second v8 grade file | CVO moved its copies (8897a19ad4). Same lesson: grading belongs to the box running the project |
| 4 | 09:01Z | dell2 | conflict on one global "last deploy recorded" key that every deploy rewrites | dell1 fix D1-S7: the recorder stops writing that key |
| 5 | 11:30Z-12:03Z | site Z (6 integrates) | conflict on a cross-box record and on NFRA_GATSCP's issue log | ruled: take `CLOUD`'s record, keep both issue rows; site Z's manager resolved |
| 6 | 12:19Z-12:44Z | laptop (6 passes) | the append-only override audit log had no "keep both sides" merge rule | set `merge=union` in the laptop's local Git settings; clean at 12:58Z |
| 7 | 13:00Z-14:20Z | all four | my schema break, then three independent repairs that collided | ruled `CLOUD`'s copy canonical; the laptop took it (2009fc1439) and dell2 was told to; a separate dell1 deploy-map conflict was ruled "keep both entries" |
| 8 | 15:04Z, 15:18Z | laptop | a dirty file, then a cross-box record closed from both sides | laptop copy set to equal `CLOUD`'s (3cb55f8042); merge clean |

**Box lag:**
- All four boxes read 0 commits behind `CLOUD` at 10:20Z and again after 14:20Z. Between those times each box catches up at its own next pass.
- Site Z fell furthest behind (up to 276) during its 11:30Z hold.

---

## 3. The driving skills

### 3.1 /keep-driving -- your on/off switch

**What it does:** one cloud file turns two behaviours on or off for every box:
- the 10-minute open-calls scan;
- an empty COO tick running `/next-calls --drive`.

**State:** **both on for all four boxes, no per-box override** (`open-calls.py mode get`, read 15:1xZ). It was set at 01:53:41Z on your word ("send out the message of /keep-driving ON for all boxes, all COOs") and has not changed since.

**Verdict:** working as designed.

### 3.2 The 10-minute open-calls scan (the automatic tick that wakes the CTO)

**What it does:** a scheduled task on each box reads that box's open calls, nudges its CTO when one is due, and carries the unblock steps.

**Laptop evidence:**
- **78 passes** from 00:36Z to 15:11Z, against about 88 due, so about 10 were missed.
- Gaps: 01:11Z (30 min), 08:01Z (45), 09:31Z (20), 12:01Z (20), **12:31Z (50)** and 13:41Z (20).
- 72 passes found nothing due. **6 sent a nudge, and each was ruled the same tick.**

**Every box's heartbeat** (cloud copy, 15:14Z): all four scanned within 8 minutes, with the switch on and every CTO live.

| Box | Last scan | Calls due | Nudge sent | Open deploy ledgers |
|---|---|---|---|---|
| laptop | 15:11Z | 0 | no | 18 |
| site Z | 15:14Z | 1 | yes | 120 |
| dell1 | 15:07Z | 0 | no | 95 |
| dell2 | 15:09Z | 0 | no | 105 |

**Verdict:** works, and every nudge led to a ruling. Two weaknesses:
- missed passes (up to 50 minutes);
- large counts of open deploy ledgers (issue 5).

### 3.3 /next-calls -- open calls and next steps in one pass

**What it does:** with `--drive`, a COO runs it on an empty tick to find work before declaring a block.

**Evidence:**
- 34 commit messages today name it, for example COO `~C2`: "empty-tick /next-calls --drive output -- the split repair needs no new source".
- There were 205 COO drive-log commits today.

**Verdict:** used, and it finds work where it runs. Git cannot show how many empty ticks skipped it, because a drive log that does not name it looks the same either way.

### 3.4 /canonical-drive -- each COO's loop through the ten workflow steps

**Evidence:**
- 89 commit messages name it today, for example "/canonical-drive IRPT_DASHBD 13Z -- round 44 issued and drained 3/3" and "/canonical-drive MDPF_STRATID hour 13Z -- FWD-1 read (PASS)".
- About 15 COO lanes committed in the window.

| COO lane | Commits |
|---|---|
| `~R1` | 55 |
| `~C2` | 48 |
| `~D1` | 42 |
| `~P2` | 39 |
| `~T2` | 36 |
| `~V1` | 34 |

**Verdict:** this is the engine of the day's output, and it ran steadily on dell1, dell2 and site Z.

**Weak spot:** some projects cycle without a new outcome. DSGN_AMGTV1 hit a third empty tick at 09:10Z and again at 13:28Z, waiting on your own walk of the page. That wait was then ruled seat-provable through /unblock.

### 3.5 /unblock -- the third empty tick goes to research, then a ruling, then review

**What it does:** after two empty ticks, the COO writes its position to the CRO. The CRO proposes a new approach, the box CTO folds it in, and the CVO signs. Since ~06:3xZ the COO first chases any seat that owes it an act.

**Today:** **29 unblock files, 28 closed, 1 open** (NFRA_OPALAI, 14:46Z).

| Box | Files |
|---|---|
| dell1 | 14 |
| dell2 | 8 |
| site Z | 7 |
| laptop | 0 |

Repeats: AMGT_CORPUS 5, NFRA_OPALAI 5, TCKT_VNEXT 3, DSGN_AMGTV1 3, and six projects with 2 each.

**Went well:**
- Same-day closure with a ruling file.
- Several real changes of approach:
  - DSGN_AMGTV1's main outcome was made provable by a signed-in seat instead of waiting on you, and it graded MET;
  - COMM_ASSIST's dependency on the transcripts encryption key was removed;
  - NFRA_OPALAI's live-traffic tests were re-planned.

**Went badly:** several files were live waits, not blocks.
- NFRA_TRNSPT's UB-413a says "Every open act sits with a live owner on a stated clock".
- The CRO answered "no new approach", and the CVO signed "live wait, no reroute".
- Each such file still cost a CRO pass, a CTO ruling and a CVO signature.
- The CRO's earlier fix (d2012292b9) covers repeat files about the same wait, but not a first file that is a wait from the start.

### 3.6 /self-drive -- the CTO loops on each box

**This seat:**
- Ticks 37-60 today, at a 60-minute cadence until ~06:0xZ and 30 minutes after, on your word.
- 18 committed logs; quiet ticks write only to a runtime file.
- Since 10:00Z:
  - ruled 7 cross-box calls;
  - cleared or ruled 5 sync holds;
  - moved LGIC_ENFORCE to dell1;
  - fixed 3 shared tools: the proof-schema kind (then repaired), the deploy-check hook (d29f2f61de) and the safe-deploy summary (dd78f5dd5e).

**Other boxes' CTOs** (commit subjects naming a self-drive tick):

| CTO | Ticks named |
|---|---|
| dell2 | 28 (its tick 21: "11 calls ruled since tick 20") |
| dell1 | 15 |
| site Z | 10 |

**Verdict:** nothing waits on you except acts only you can do (13, each cited).

**The cost is volume:** dell1's CTO made 179 commits today and dell2's made 199.

---

## 4. Errors today

| # | When (UTC) | What | Impact | Fix |
|---|---|---|---|---|
| 1 | 13:00Z | **My proof-schema edit wrote text into a field's type** (e7c10e5b4b). My script placed the text by position, not by parsing the file | every proof check on every box failed, so no order could be marked complete for ~25-80 minutes per box; reported by COO `~C` at 13:19Z | 59a9442734 at 13:25Z (schema meta-check OK, a real proof check VALID). Lesson: I checked the file parsed, not that each field kept its type |
| 2 | 13:43Z-14:20Z | **Three boxes each repaired error 1** | the merge into `CLOUD` held up to three boxes for ~35 min | `CLOUD`'s copy ruled canonical (2009fc1439) |
| 3 | 13:10Z, 13:34Z | **Merges into `CLOUD` took 607 s and 853 s** | 4 later merges skipped; the repair waited | issue row S9107; cause not yet measured |
| 4 | 12:19Z-12:44Z | **Laptop passes held 6 times on the audit log** | laptop up to 108 behind | local union-merge rule; clean 12:58Z |
| 5 | 4 times | **Fetch failed** | one pass lost each time | the next pass worked |
| 6 | 04:30Z-04:51Z | **5 laptop passes refused by a gate** | ~20 minutes | cleared by the next pass |
| 7 | 09:29Z on | **The base laptop CloudOps seat went deaf** (desktop locked) | a dell2 password window closed 44 minutes after its trigger, still inside its 4-hour limit | COO `~C` seated two new lanes |
| 8 | 11:01Z | **dell1 listed three deletes twice on your act list** | your list read 15 instead of 13 | ruled closed |
| 9 | 13:4xZ | **My issue row was refused** (wrong id coordinate, time format) | ~5 minutes | fixed as S9107 |
| 10 | 13:2xZ | **Wrong message id in a signed addendum** | record accuracy | b2faa349c4 |
| 11 | 14:5xZ, 15:18Z | **I closed a cross-box record from the laptop while dell2 closed it from its side**, and the two edits conflicted | one laptop hold | copy set to equal `CLOUD`'s (3cb55f8042) |

**Earlier slips, all caught in the same session:**
- a shell quoting slip ran text as a command (nothing changed);
- a status-reader fix first reopened 17 task orders (ea8d5ba5cd);
- a secrets-tool change first broke 6 readers (9e4730450c).

---

## 5. Success stories

1. **Zero lag three times.** All four boxes read 0 behind `CLOUD` at about 10:20Z, 10:50Z and after 14:20Z, while 3,706 commits landed across four machines.
2. **The Dells deploy on their own, with the laptop told before and after.**
   - At 14:25Z dell1's deploy seat sent a before-the-act notice for two read grants, and I approved it within minutes (a1127785b0).
   - At 14:45Z it reported the result: applied through Terraform, read back live with the allowed file allowed and a neighbouring file still denied, ledger closed.
   - No laptop hands were needed.
3. **A fleet-wide break was caught and fixed fast.** It was reported 19 minutes after my commit, and the repair landed 6 minutes after the report.
4. **/unblock turned three stuck waits into progress**, including DSGN_AMGTV1's main journey graded MET without needing your walk.
5. **The scan woke the CTO 6 times, and each wake ended in a ruling.** Your list holds only acts only you can do, each with its citation.
6. **The audit-log fix worked at once.** After six held passes, the 12:58Z laptop pass was clean.
7. **Your market-update answer reached dell2 in minutes** as an exact site, folder and file id (e422fa5dc5).
8. **The gates held.**
   - 31 lane refusals.
   - The push gate refused my own push.
   - No rebase of a shared branch.
   - Every change to served data carried its signed halves.
9. **Two projects closed rounds with every outcome met** (LGIC_BLANKFIX 9 of 9, NFRA_GATSCP round 3). Several major releases went live: gateway r29, IRPT gold R44, the transcripts reader role, the trade Lambdas, and Security Analysis rounds 58-65 on portal PROD.

---

## 6. Issues and ideas for improvement (ranked)

None of these adds an approval gate or a monitor. Each changes an existing mechanism or setting.

1. **Merge every append-only log by keeping both sides, on every box.**
   - **Issue:** dirty-overlap (35) and log conflicts were the most common hold. The laptop's fix lives only in its local, untracked settings.
   - **Change:** list the append-only logs as `merge=union` in the tracked `.gitattributes`. Keeping both sides preserves the shared start of the file, so the audit archive's check still holds.
   - **Owner:** `0.0.0_AB_MSTR`.
2. **One owner repairs a fleet-wide defect; other boxes report it and wait.**
   - **Issue:** three correct repairs of one break blocked `CLOUD` for 35 minutes.
   - **Change:** one line in `/integrate` and `/self-drive`: a defect in a shared file is repaired on its owner's box, and a box that already repaired it takes `CLOUD`'s copy at its next pass.
   - **Owner:** 1.0.0_SA_CTO.
3. **Time each phase of a sync.**
   - **Issue:** the 607 s and 853 s merges cannot be explained from a row that prints only a total.
   - **Change:** `box-sync.sh` prints fetch, merge, grade and push seconds in the row it already writes.
   - **Owner:** NFRA_CTLPLN (row S9107).
4. **A dated wait is not a block.**
   - **Issue:** about a third of today's unblock files were live waits.
   - **Change:** in `unblock.py`, an empty tick whose every blocker names a live owner and a time reads WAITING on its first occurrence, extending d2012292b9.
   - **Owner:** CRO `~B`.
5. **Close the open-deploy backlog.**
   - **Issue:** the scans report open deploy ledgers of 18 (laptop), 95 (dell1), 105 (dell2) and 120 (site Z), some dated 2026-10-07. Each is either a truly half-finished deploy or a stale entry.
   - **Change:** each box's deploy seat checks each artifact and closes the finished ones as superseded, under the existing rule.
   - **Owner:** each box's CloudOps lane.
6. **Fix the register's box fields.**
   - **Issue:** six dell2 projects read `laptop`, five dell1 projects read `site-z`, and 20 of 59 "active" projects have no box at all. Call ownership and the scope check read this field.
   - **Change:** each box CTO sets the field for the projects it runs; the idle rows are placed or closed.
   - **Owner:** the four box CTOs, starting with the laptop (I own the register).
7. **Do not miss scan passes.**
   - **Issue:** the laptop scan missed about 10 of ~88 passes.
   - **Change:** set "run as soon as possible after a missed start" on the existing scheduled task on each box. A setting, not a new task.
   - **Owner:** each box manager.
8. **Edit structured files by parsing them, never by text position.**
   - **Issue:** error 1.
   - **Change:** load the JSON or YAML, change the object, write it back, and meta-validate a schema before committing.
   - **Owner:** 1.0.0_SA_CTO, as a recorded trap.
9. **Refuse a duplicate open-call row.**
   - **Issue:** dell1's duplicate deletes.
   - **Change:** `open-calls.py add` refuses an open row whose subject and source match an existing open row on the same box, and names the existing id.
   - **Owner:** the CRO.
10. **A cross-box record is closed by one side's file at a time.**
    - **Issue:** errors 11 and 5 in section 2.5; most rulings sent box to box read "not delivered until acknowledged", so I could not see whether they were read.
    - **Change:** each side records only its own half of the record, after taking the other side's latest copy. Rulings that must stick travel as cross-box records, whose acknowledged and closed states are files.
    - **Owner:** each box CTO.

---

**Sources:**
- `org/git-author-override-audit.log`
- `git log origin/CLOUD` for 2026-10-09
- `open-calls.py mode get` and `list --all --cloud`
- each box's scan heartbeat in the cloud, and the laptop scan task log
- `unblock.py list`
- the four skill files
- this session's record

**Not read:** what each merge-attempt exit code means; the other boxes' local scan logs; the Dells' COO tick files.
