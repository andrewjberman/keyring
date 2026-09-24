---
name: closer-drive
description: The FAST tick body -- the project's seat builds the next item itself while Andrew is present under a live FAST lease (/drive-mode). No subagents, no task orders; per item its own test, typecheck/lint and ONE real run looked at; lands on portal DEV itself; STATUS.md overwritten in place; the CVO grades after the fact. Reached from /canonical-drive when the lease reads FAST. The project's COO lane only.
---

# /closer-drive -- build it yourself while Andrew is here

Authority: report 2 (RCN-0017) C2, section 6, with calls 2, 3, 5 and 6, approved by Andrew 2026-09-24. The joint
model with report 3 is in section 12. Spine: the Closer subsection, FAST mode. This is the FAST body of the
project's ONE loop. `/canonical-drive` is the FULL body, and the lease picks between them each tick.

## Each tick

0. **Read the lease:** `python .tools/drive-mode.py read <CODE>`. It prints the mode, and for this seat it stands
   the search rail down for the lease's life.
   - FULL -> run the FAST -> FULL boundary below, then the `/canonical-drive` body.
   - HOLD -> do nothing on this project this tick.
   - FAST, and this tick is the first -> run the FULL -> FAST boundary first.
1. **Read STATUS.md** (`<project home>/STATUS.md`, shape: `/closer`'s `templates/STATUS.md`) and run
   `python .tools/drive-mode.py status` for overlapping claims. A project with several FAST seats keys one lease per
   seat, `<CODE>~<lane>`, on disjoint surfaces: each seat reads its own key and writes `<project home>/STATUS~<lane>.md`.
2. **Pick ONE item.** A defect that breaks the live thread comes first; otherwise take the top of the next-list,
   which is the enrichment backlog in order. Claim it in STATUS.md's Write claims before building.
3. **Build it** in the seat's own worktree, across frontend and backend as the item needs. Do not spawn a subagent.
4. **Check it.** That is the whole bar:
   - the item's own test (write one if cheap);
   - typecheck and lint on the touched package;
   - **ONE real run, looked at:** the page served with real or served data (`/frontend-dev`, and read the
     screenshot), or the real entry point for a backend item.
5. **Land it.**
   - Commit through `safe-commit.sh`.
   - Portal: pull-merge DEV, then push DEV yourself, with CI (VALGATE) running (call 2). DEV only; PROD stays gated.
     Before the push, `git -C portal log --format='%h %an' origin/DEV..HEAD` must list only your own commits and
     their merges. A push publishes whatever is local, so another seat's commit in that list stops the push.
     `.tools/hooks/never-rules-gate.sh` admits a DEV push only from a live FAST lease's seat. When two seats land in
     one window, the second merges forward, never by force.
   - A deploy goes to QA/DEV under the normal rules: a ledger entry and `safe-apply`.
6. **Overwrite STATUS.md** with pins, claims, next and limits. A finding off the item is ONE parked line with its
   owner and the condition that un-parks it. It is not a row and not a message.
7. **Messages:** only an interface published, a blocker, or a review handoff to the CVO naming the pin. No
   acknowledgements and no status messages.
8. `heartbeat`, then the next item. While working, keep going; the loop wakes an idle seat every 10 minutes.

## Review

- **You are Andrew's live reviewer on the screen.**
- **The CVO grades each landed pin after the fact (call 3).** A FAIL becomes the next item. Nothing waits on the
  grade, and the CVO grades on the real run's artifact, never on static markup.

## Boundaries (spine, FAST mode)

- **FULL -> FAST:**
  - Cut nothing new.
  - Let each running worker finish the order in hand, and merge it; or merge what is terminal and flip the rest
    `superseded`, with the pointer "superseded by FAST lease, drive-mode.log line N".
  - Write STATUS.md from the round's open cells plus the enrichment backlog.
  - Send the CVO one line: "FAST from <time>; pins graded after the fact".
- **FAST -> FULL** (the lease lapses, or `full`):
  - Commit what builds. Commit an unfinished edit on your branch as a work-in-progress pin; never leave it
    uncommitted in the shared tree.
  - Overwrite STATUS.md.
  - Run `bash .tools/freeform.sh off "$CLAUDE_CODE_SESSION_ID"`.
  - At the next tick, cut round N+1 straight from STATUS.md's next-list under the verification diet, with no CTO
    round-N analysis for that one cut (call 5). The CTO's analysis resumes at that round's L10.
  - The CVO's next slug carries one section on the FAST interval.

## What FAST never relaxes

`safe-commit.sh`; your own worktree; no rebase on a shared branch; the never-widen sign-off on served output; the
deploy ledger (NEVER-2); `safe-apply` and Terraform only; vendor egress on Andrew's per-use word; PROD promotion;
destructive-act confirmation; the cross-firm guard; LGIC builder output for any new address or name (or park the
item); secrets. **A FAST lease never lowers a `<risk>` class:** a deploy inside FAST is still `WORLD`.
