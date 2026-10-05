# AMGT_CORPUS task order -- `CRPS-an-4` -- ROUND 38: the /ui-walk walker closes the timeline day it opened

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-an-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check is static. Do NOT arm the walker or run a walk: the shared walker account needs a slot from 0.0.0_AB_MSTR~Z; the real walk is the issuer's CRPS-an-6.
comp-adversary: RUN by the issuer at the cut -- an4_check.cjs build 0/1 control 1/1.
EGRESS CLASS, declared: NONE.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 38.

## 1. THE CELL -- `CRPS-an-4`

`.claude/skills/ui-walk/walk.mjs` walks a portal page as a signed-in user. Its `async function walkTimeline(page, sec)` (about line
443) presses the newest timeline day bar (`[data-day-bar]`), waits for the day's state (`waitForDayState`), takes its checks, then
does the same for the first `[data-timeline-event]`. It never closes the day dialog it opened.

The redesigned page shows the day as a dialog ("OPAL CAPITAL -- NEWS TIMELINE", a date, "The day's articles about this company,
strongest first"). So every later step's screenshot is taken under the open dialog. The 2026-10-05 TSM walk
(`tmp/ui-walk/20261005T135401Z`, shots 012 and 013 of the Model tab) shows only the dialog.

The walk already closes what it opens elsewhere: the card step presses Escape after a card's dialog (about lines 616-617, "a card's
'View breakdown' dialog blocked the next tab click on 2026-09-27").

**Build, in `walk.mjs` only, in `walkTimeline` only:**
1. After the day bar's state wait AND after the event's state wait, close the opened dialog before the next press and before the
   function returns. Press Escape, as the card step does. If the dialog is still visible after Escape, click its close control.
2. Record nothing new and change no other step. The timeline-day rows the walk keeps (`timelineDays`) and its checks stay as they
   are.

## 2. BOUNDS

1. Do NOT arm the walker, run `walk.mjs`, or start a dev server. The account is shared across devices; its slot is the issuer's.
2. Only the files in `<paths>` change. Write with the Edit/Write tools. ASCII only.
3. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-an-4.walker-closes-the-timeline-day.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-an-4.walker-closes-the-timeline-day.md
</paths>

Read-only: the whole repository, in particular `.claude/skills/ui-walk/SKILL.md` and the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round38/an4_check.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-an-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round38/an4_check.cjs"</invocation><expect>(?m)^an4 build 1/1 control 1/1$</expect></criterion>
</proof_of_spec>

- AC1: build -- `walkTimeline` closes the dialog after its last day-state wait; control -- `node --check walk.mjs` parses.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1 --governing-order <this order>` AFTER your final commit. It must return rc 0.
2. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
3. Report ONCE: the diff summary, AC1's output line, your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the instrument repair that round-37 analysis ruling 2's page read needs (the walk evidence of 10-05). Base:
an4_check build 0/1 control 1/1. walk.mjs is maintained by 2.0.0_SA_COO~D (DSGN); DSGN's open round-38 cells write other files.
<risk>LOCAL</risk>
<status>pending</status>
<round>38</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
