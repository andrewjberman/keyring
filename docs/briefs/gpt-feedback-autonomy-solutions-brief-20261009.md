# BRIEF -- the external (GPT) feedback and the no-cross-box-dependency rule, as solutions against the estate as it is

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-10-09 ~19:3xZ (UTC) | **For:** `1.0.0_SA_CTO`, who rules each item and routes any build
through the canonical workflow, or through the owner's lane for a tool fix.
**Asked by:** Andrew, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_190xZ_GPT_FEEDBACK_TO_CRO_FOR_SOLUTION_ANALYSIS.md`
(@ed55306998, CTO msg 108093) and `ANDREW_DIRECT_20261009_191xZ_NO_CROSS_BOX_DEPENDENCIES_AFTER_MIGRATION_AND_DELL_PACKAGES.md`
(@d5494eee0e, CTO msg 108095), same folder.
**Constraints honoured:** no new approval gate, no new monitor or alert, no shadow pipeline; the four boxes stay autonomous. Every fix below
is an existing mechanism, a setting, or a small change to a tool that already runs.
**Vintage:** laptop, 2026-10-09 ~19:0xZ-19:3xZ. Reads: the laptop tree, `origin/*` branches (fetched), the S3 fabric records each box
publishes, `org/git-author-override-audit.log`, the unblock store. No Dell or site Z tree was read directly; where a number comes from a
box's own published record, that is said.

---

## Summary

| # | Item | Size today (measured) | Smallest fix | Rung | Owner |
|---|---|---|---|---|---|
| 1 | Shared log conflicts | 2 of 4 append-only audit logs have `merge=union`, on the **laptop only** (untracked `.git/info/attributes`); 2 have it nowhere. Holds today: 35 dirty-overlap + the 12:19Z-12:44Z run (6 passes) | Move the union rule into tracked `.gitattributes` for all four logs | setting | `0.0.0_AB_MSTR` (integrator) |
| 2 | One owner for fleet-wide repairs | 1 collision today (3 boxes repaired `PROOF_OF_SPEC.schema.json`, 13:00Z-14:20Z) | One rule in `/integrate`: a break of a trunk-shared file is repaired only by the seat that owns the file's lane, on its own box; other boxes take `CLOUD` | existing mechanism (owned-paths lanes) | `0.0.0_AB_MSTR` (skill text) |
| 3 | The moving origin | 199 integrates today: 25 skipped (lock held), 21 held, 2 push refused. Rows carry only total seconds; ~450 s of the 607 s run is unexplained | Already serialized and fetch-first; add per-phase seconds to the row; retry a refused push inside the pass, as `box` mode already does | minimum code | `4.0.0_SA_CRO~A` (box-sync owner) |
| 4 | Waiting vs blocked | 37 unblock cases, all CLOSED; 36 name a dated or scheduled wait in `## Blocked`; 5 answered "no new approach" | Let `unblock.py tick` take `--wait-until` **before** a case (today only after a fold, @d2012292b9) | minimum code | `4.0.0_SA_CRO` |
| 5 | Deploy backlog vs live state | **24** tracked open entries, the same on every branch; 11 of the laptop's 23 are past their window. The 95-131 per Dell/site Z are untracked files on disk and stale worker worktrees, counted by my own scan | Fix the scan to read each worktree's `HEAD` (the rule in CLAUDE.md section 5); reconcile the 24 with `deploy_ledger.py check` and the existing SUPERSEDED close | existing mechanism + a fix to my tool | `4.0.0_SA_CRO` (scan); each entry's author (closes) |
| 6 | Project ownership in the register | Mission tree: 32 live, all carry both fields, **16 disagree**. Flat `org/projects/`: 71 live, 33 carry neither, 38 `fabric` only, 0 `placement` | `placement` in the mission `project.json` is the one field; readers already prefer it (@4934c4b98b); a transfer edits that one field; the flat row stops carrying `fabric` | existing mechanism | `1.0.0_SA_CTO` (register writer) |
| 7 | Autonomy, no shared writable state | Items 1-6 together, plus the 7 dependency rows below | Remove each shared writable file or cross-box need at its source; add nothing that watches | -- | per row |
| D | No cross-box dependency after a migration | 7 rows (CTO record section 2) | Per row below: rights on the owning box, a box-local lane, or a served interface | mixed | per row |

**The finding that matters most:** the deploy "backlog" in the CTO's report (dell1 95, dell2 105, site Z 120) is mostly not a backlog.
Every branch tracks the same 24 open entries. The rest are untracked files on each box's disk and entries left in stale worker worktrees,
which my `open_deploys.json` counts because it reads disk, not `HEAD`. That is my defect, and it inflated the number the CTO reported.

---

## 1. Shared log conflicts -- per-box append-only logs with deterministic consolidation

**What exists:**
- `.git/info/attributes` on the laptop only (untracked, so no other box has it):
  `org/mcp/agent-spawn-audit.log merge=union`, `org/mcp/drive-mode.log merge=union`, `org/git-author-override-audit.log merge=union`.
- Tracked `.gitattributes:61` gives `merge=union` to `org/compiler-tools-log.md` only.
- `git check-attr merge` on the laptop: `org/law-edit-audit.log` and `org/safe-deploy-bypass-audit.log` are **unspecified**.
- `.tools/merge-resolve-known.py` (`union_append`, `union_channel`, `union_rows`) resolves the two known classes when box-sync meets a
  conflict. @514c71db66 resolves `agent-spawn-audit.log` and `law-edit-audit.log` as base + CLOUD tail + box tail, and commits a seat's
  uncommitted appends before the land.

**Size:** holds today, from the report's section 2.5: dirty-overlap 35 (some on these logs); hold #1 (shared audit logs, early morning);
hold #6 (12:19Z-12:44Z, 6 laptop passes, the override audit log had no union rule). The afternoon (15:20Z-18:51Z) had 3 dirty-overlap holds
in 134 runs.

**Smallest fix (a setting):** add to tracked `.gitattributes`:
```
org/git-author-override-audit.log merge=union
org/mcp/agent-spawn-audit.log merge=union
org/mcp/drive-mode.log merge=union
org/law-edit-audit.log merge=union
org/safe-deploy-bypass-audit.log merge=union
```
`git merge-tree --write-tree` (what box-sync uses) honours the built-in union driver, so every box and the integrator merge these logs with
no conflict. Then remove the laptop-only lines from `.git/info/attributes`, so one tracked file is the truth.

**Per-box logs (GPT's literal proposal):** not recommended now. Splitting each log into `<log>.<box>` removes the conflict entirely, but every
reader of the single file (the audit-archive invoker's append-only walk, `/mstr-review`, the commit-time readers) would have to union N files.
Union merge gives the same result for an append-only file at the cost of one setting. Revisit only if a union merge ever reorders lines in a
way a reader depends on.

**What it will NOT fix:** a dirty-overlap hold caused by a seat's **uncommitted** appends on a path the trunk changed. That is a working-tree
problem, not a merge problem. @514c71db66 already commits the appends for two logs before the land; the same step should cover all five.
**Owner:** `0.0.0_AB_MSTR` (integrator; `.gitattributes` is a trunk file). The box-sync step: `4.0.0_SA_CRO~A`.

## 2. A single owner for fleet-wide repairs

**What exists:** owned-paths lanes (`.tools/owned-paths-validate.py`, the commit gate) already name one owning lane per path. Today's gate
refused 31 out-of-lane writes and was right each time (report section 2.4). Cross-box records (`org/devices/crossbox/`) carry calls between
boxes. The trunk has one writer (`0.0.0_AB_MSTR`, `box-sync.sh integrate`).

**Size:** 1 collision today. Hold #7, 13:00Z-14:20Z, all four boxes: one schema break on `PROOF_OF_SPEC.schema.json`, then three independent
repairs on three boxes that conflicted with each other. Cleared by ruling `CLOUD`'s copy canonical.

**Smallest fix (existing mechanism, one rule in the skill text):** in `/integrate` and in the box-sync HELD message: *"When a trunk-shared
file breaks, the seat that owns the file's lane repairs it, on its own box, and every other box takes `CLOUD` at its next pass. A box that is
not the owner does not repair it locally."* The lane owner is read from the owned-paths registry; no new list is needed.

**What it will NOT fix:** a break in a file whose lane is ANY or unclaimed (the commit gate cannot name an owner). For those, the integrator's
box repairs. It also does not prevent the first break; the import-closure reads before deploys (CTO record section 3) cover that.
**Owner:** `0.0.0_AB_MSTR` (the `/integrate` skill and the box-sync message).

## 3. The moving origin -- serialize integration, fetch first, retry, and time the phases

**What exists (`.tools/box-sync.sh`):**
- Serialization: one writer of `CLOUD` (an MSTR serial only, `:70-74`) and a per-mode pass lock (`:78-86`). A second pass is **skipped**,
  never overlapped (rc 3).
- Fetch first: `git fetch -q origin` before any merge (`:92`).
- Retry: `box` mode rebuilds on a moved tip up to 3 times (`:201-237`). `integrate` mode does not: a refused push exits rc 3 and waits for
  the next 10-minute slot (`:182-185`).
- Timing: one `secs=` total per row (`:63`). No phase is timed.

**Size (`org/git-author-override-audit.log`, 2026-10-09 to 19:01Z):** 199 integrate rows: rc 0 149, rc 1 2, rc 3 27 (25 `skipped=overlap`,
2 `push=refused`), rc 4 21. The slowest: 853 s and 607 s (row NFRA_CTLPLN-S9107); of the 607 s, about 150 s is explained (four merge checks).

**Smallest fix (minimum code, in the tool that already runs):**
1. **Time the phases.** Add `t_fetch`, `t_merge_<box>` (merge-tree + grade, per box) and `t_push` to the row note. About 8 lines. This is
   what "confirm the win" needs: the slow 450 s cannot be fixed until it is measured.
2. **Retry a refused push inside the pass,** as `box` mode does: re-fetch, rebuild on the new `origin/CLOUD`, push again, at most twice.
   About 10 lines.

**What it will NOT fix:** the 25 skips are a slow pass holding the lock, not an origin race. They fall only when the slow phase (found by
step 1) is fixed. Retry does not help a HELD conflict (rc 4); that is items 1 and 2.
**Owner:** `4.0.0_SA_CRO~A` (box-sync's owner; this seat if `~A` is not live).

## 4. Distinguish waiting from blocked

**What exists:** `.tools/unblock.py` and `/unblock`. Since today:
- @d2012292b9: a dated wait recorded on a fold or resume (`--wait-until`) reads WAITING and holds the count at 0.
- @5ed9bf8cf7: the chase comes first; an owed act is chased until an ack, and a chase act counts as tick work.

**Size (the unblock store, read 19:2xZ):** 37 files, all CLOSED. 36 name a dated or scheduled wait in their `## Blocked` section. 5 were
answered "no new approach" by a CRO. So the cases were almost all live waits with an owner and a clock, which is what GPT names.

**Smallest fix (minimum code):** `unblock.py tick --result nothing --wait-until <UTC ISO> --owner <serial>`, taken **before** any case is
opened. It records the wait in the tick counter (local, per box) and reads `WAITING UNTIL <time>` with the count held at 0, exactly as a
resumed case does now. It reuses `parse_wait` (at most 7 days ahead). About 15 lines, and one line in `/unblock` and `/next-calls --drive`:
"a dependency with a live owner and a time is a wait: record it, do not count it".

**What it will NOT fix:** a wait with no time (an owner who never answers). That stays the chase: nudge until an ack, then a workaround
(Andrew-direct ~06:3xZ). It also does not decide whether the owner is live; the chase's peek does.
**Owner:** `4.0.0_SA_CRO` (built `/unblock` today).

## 5. Reconcile the deploy backlog against live state, close with evidence

**What exists:**
- `.tools/deploy_ledger.py check` / `list`: every OPEN and HELD ledger with age, window, the legs still unproven ("stranded"), and a
  FOREIGN-VIEW mark for another box's entry. Exit 1 if any are open. Laptop read 19:1xZ: 23 entries scanned, 23 of 23.
- CLAUDE.md section 5 (NEVER-2): before acting on an open entry, measure the artifact; world-done -> close SUPERSEDED, never re-execute.
- `close-leg` and `close` refuse a leg without proof.

**Size (measured):**
- Tracked: **24** sentinels on `origin/CLOUD`, and 24 on each of `box/laptop`, `box/dell1`, `box/dell2`, `box/sitez`.
- Laptop, from the ledger: 23 entries, 11 past their own window, 1 with no window, 3 older than 48 h. One is HELD-STALE 37 days
  (`d12-sms-origination-identity-activation`, gated on carrier verification).
- Each box's `open_deploys.json` (my scan, read 19:0xZ): laptop 23 (1 worktree); dell1 106 (85 in the main tree, 21 only in worker
  worktrees, 56 of 63 worktrees read); dell2 119 (88 / 31, 69 worktrees); site Z 131 (101 / 30, 54 of 59). With 24 tracked, about 60-80 per
  box are untracked files on disk or entries on worker branches never merged.

**Smallest fix:**
1. **Fix my scan (this seat, now):** `open_deploys_doc` reads each worktree's `HEAD` (`git ls-tree` + `git show`), as CLAUDE.md section 5
   says, and counts untracked sentinel files apart (named, not counted as open). The per-box numbers then mean what the CTO read them as.
2. **Reconcile the 24 with the existing mechanism:** each entry's author runs `deploy_ledger.py check`, measures each past-window entry's
   artifact, and closes it with proof or SUPERSEDED. No new tool.
3. **Stale worker worktrees:** Andrew's standing word (memory, 2026-10-08 ~23:0xZ) is "Force-removing merged worktrees is mandatory" at each
   drain. 54-69 worktrees per Dell/site Z says drains are not removing them. That is each box's COO drain step and `/cleanup`, not a new
   mechanism.

**What it will NOT fix:** an entry that is genuinely open and waiting on an external gate (the 37-day SMS entry). That stays HELD, correctly.
The untracked files on each box's disk are a recursive cleanup, which waits on Andrew's word (it is the same class as the retired-root
leftovers this seat asked about today).
**Owner:** `4.0.0_SA_CRO` (the scan), each entry's author (closes), each box's COO and MSTR (worktree removal).

## 6. Correct project ownership in the register, and update it on every transfer

**What exists:**
- Two carriers per project: the mission `project.json` (`fabric`, `placement`) and the flat `org/projects/<CODE>.json`.
- A transfer edits both by hand (example: ca565d1871, LGIC_BLANKFIX LAPTOP -> DELL1, 2 files).
- `.tools/placement-check.py` now reads `placement` before `fabric` (@4934c4b98b, `2.0.0_SA_COO~C`). It moved dell2 from 2 to 10 projects
  and cut overlaps from 64 to 48.

**Size:** mission tree: 50 `project.json`, 32 live; all 32 carry both fields; **16 disagree** (`fabric` names the old box). Flat registry:
398 rows, 71 live; **33 carry neither field, 38 carry `fabric` only, 0 carry `placement`**. LGIC_BLANKFIX, moved this morning: mission
`placement` DELL1, flat `placement` absent.

**Smallest fix (existing mechanism):** one field is the truth: `placement` in the mission `project.json`. Readers already prefer it. A
transfer is one edit of that field (and the move's commit names the record). The flat row and `fabric` stop being read for placement;
`fabric` keeps its other meaning (the box the project was born on) or is dropped by the register writer. No gate: `placement-check.py`
already prints the disagreement as a finding when asked.

**What it will NOT fix:** the 33 live flat rows with no box at all are legacy flat projects with no mission tree. Whether they are live is
the spring-clean question (Andrew, 2026-08-25: a project not on the directives register is closed), not a placement one.
**Owner:** `1.0.0_SA_CTO` (the register writer; it made today's moves).

## 7. Keep the four boxes autonomous; remove shared writable state and unnecessary escalations

This is the sum of 1-6 and the dependency rows below. Shared writable state today, by measurement: the five append-only logs (item 1), the
trunk-shared files a repair touches (item 2), the cross-box records (`org/devices/crossbox/`; the 15:18Z conflict, cleared by "each side
records its half on top of the other's latest copy"), the two placement carriers (item 6), and sentinels on disk (item 5). Each fix above
removes one at its source. Nothing in this brief adds a watcher, a gate or a second pipeline.

---

## D. No cross-box dependency after a migration (Andrew ~19:1xZ)

Rows from the CTO record's section 2. "Inferred" there stays inferred here unless measured.

| Project (box) | Depends on | Smallest removal | Kind |
|---|---|---|---|
| MDPF_DEMQUE, MDPF_SECHIST, ETFS_RIVALS, AMGT_HARVST, AMGT_CORPUS (dell1) | site Z deploy lanes and manager windows: the Bloomberg Terminal and the harvest runners are on site Z | **Bloomberg: a served interface, kept.** The Terminal is one physical machine; the DEMQUE request queue (`MDPF_DEMQUE`; owners ruled @8a625fa88a: DEMQUE owns request, pacing, ticker map; SECHIST owns the stored series) is that interface, and Bloomberg pulls go only through it (CLAUDE.md). The dell1 projects file requests and read the stored series; they never need a site Z lane. **Harvest runners:** move the runner host or give dell1 a box-local deploy lane to it (the Dell group already SENDs command documents to 6 route hosts, NFRA_CTLPLN amendment 19); measure which runners are site-Z-only first | served interface (Bloomberg); rights on the owning box (runners) |
| NFRA_TRNSPT FWD-6, ADVI_BILLING (dell2) | site Z's gateway release queue (NFRA_OPLGTW) | The Opal Gateway is one served host. A release is a deploy to it; give dell2 a box-local release lane to the gateway host (the same SSM route grant), with the gateway's own release gate unchanged. Until then it is a served interface: dell2 files a release request, it does not wait on a site Z seat | rights on the owning box |
| IRPT_ANLREQ, IRPT_YCDGEN, TCKT_VNEXT (dell2) | laptop `0.7.0_AE_CloudOps~CTL` opening `svc-irpt` password windows (5 today) | Move the secret's resource-policy window into dell2's own rights: an NFRA_CTLPLN grant (the same shape as today's amendments 20-24) lets the Dell group open and close that one window on that one ARN. The window stays audited; only the box that opens it changes | rights on the owning box |
| AMGT_RESAPP kk-1 (dell1) | a laptop deploy seat (the name-list republish needed laptop rights) | The same: one scoped grant to the Dell group for that republish target | rights on the owning box |
| MDPF_STRATID (dell1) | the laptop CTO's never-widen half (MDPF_GLOBAL is owned by the laptop CTO) | No new right: the never-widen sign-off is "CTO+COO" (CLAUDE.md section 5), not "the laptop CTO". When MDPF_GLOBAL's served output is moved by a dell1 project, dell1's CTO signs the CTO half. One ruling by `1.0.0_SA_CTO` on whose CTO signs for a placed project | box-local lane (a ruling) |
| dell1/dell2 IAM changes | laptop TO-APPLY-29 | **Stays, by design.** A box cannot grant itself permissions; the control plane that grants the Dells their rights is the one legitimate standing dependency, and it is the mechanism that removes the rows above. Batch the Dells' grant needs into one amendment per round, so it is rare, not removed | control plane (kept) |
| NFRA_CTLPLN (laptop) | dell1 exercises CT-x-1/CT-x-2 | **Stays, by design:** it tests the Dells, so it is migration-class work and ends with the project | migration (kept) |

**What this will NOT fix:** a dependency created by a new project placed without its rights. The fix is at placement time: the move's
checklist names the rights and lanes the project needs on the new box, and the move is not done until they are there. That is a line in the
CTO's transfer act (item 6), not a gate.

---

## What this seat does next, without waiting

- Item 5 step 1: fix `open_deploys_doc` to read each worktree's `HEAD` and name untracked files apart. My tool, my defect.
- Item 4: the pre-case `--wait-until` on `unblock.py tick`, if the CTO rules it.
- Item 3: the phase timing and the in-pass retry in `box-sync.sh`, if the CTO rules it and `4.0.0_SA_CRO~A` is not live.

## Not read

- The Dell and site Z trees directly: their numbers come from the records each box publishes to S3 (`open_deploys.json`) and from `origin/*`.
- Which harvest runners are site-Z-only, and whether the Dell group's SSM route grant covers the gateway host. Both are named as the first
  measurement in their rows.
- The CTO record's section 3 (Dell packages) is routed to the Dell managers by the CTO; it is not analysed here.
