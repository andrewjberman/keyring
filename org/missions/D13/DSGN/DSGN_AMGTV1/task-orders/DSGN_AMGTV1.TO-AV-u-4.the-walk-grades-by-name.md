# DSGN_AMGTV1 task order -- `AV-u-4` -- THE WALK GRADES FWD-1, FWD-2, FWD-11 AND THE TIMELINE (DSGN FWD-5, HARVST FWD-5 / FWD-6) BY NAME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-u-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~25</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 4f927ad0 -- walkthread.cjs 0 of 3 (FAIL as expected: no --thread, no lead-lists.json, no timeline step); green arm 3 of 3; walkvoid.sh YES (PASS; 5174 serving). Blind spot: walk.mjs is read statically -- the issuer's signed-in round-6 walk is its live run.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-u-4` (round 6, decomposition v6; serves FWD-1, FWD-2, FWD-11, and AMGT_HARVST's FWD-5 / FWD-6)

The round's walk must grade these outcomes BY NAME, so the walker (`.claude/skills/ui-walk/walk.mjs`) must reach every state
their clauses name. The outcomes, verbatim:

- **DSGN FWD-1** ACCEPT: "The PM picks Valero out of the list by its company name, reads its header as four cards and opens the
  Financials one, opens the Thesis and reads it as three cards under the main chart, then opens the Recommendation and can say
  whose view it is and which document each citation comes from."
- **DSGN FWD-2** ACCEPT: "In all four lists every row shows the company's name, its ticker, Opal's own asset class, sub-asset
  class and sector, the period figure and how many places it moved since the last run -- laid out like the Positioning page's
  holdings breakdown. No row names a company by a code the PM would have to look up."
- **DSGN FWD-11** ACCEPT: "Put beside the Market, Positioning and Philosophy pages, the cards, windows, charts, empty states and
  footers are the same pieces; every footer reads as a time and a source; and no raw code, id or storage path shows anywhere on
  the page." (The walker already walks any `--route`, e.g. `/market`, `/positioning`, `/philosophy`; no build is needed for them.)
- **AMGT_HARVST FWD-5** DONE WHEN: "an analyst has opened a company's timeline, picked a day, and read the articles behind it listed
  strongest first"; ACCEPT: "On a company's page there is a day-by-day line of how much it was written about; clicking any day shows
  the articles behind that day, strongest first."
- **AMGT_HARVST FWD-6** DONE WHEN: "the timeline for the validation security shows at least the event runs the stored articles
  support, each with its lead headline, and opening one lists its articles"; ACCEPT: "Bursts of real coverage about the company
  appear as marked events with a headline, not just as spikes in a count."

Build, in `walk.mjs` (read-only by construction: no new write request, no new admitted route):
1. **FWD-1's thread, by name.** A `--thread "<company name>"` option (into `opt.thread`). When given, after the Security Analysis
   lead-panel walk, ONE function walks the thread: open the route, set Trending x Price List view, find the lead-list row
   (`li[data-row-name-state]`) whose `[data-row-lead]` text contains the company name -- NEVER through "Search any ticker" and never
   by ticker; if no row reads the name, record a measured finding `thread:name-not-found` and stop the thread. Then five steps,
   each through `checks(page, label)`: `thread-1-list` (the list with the row found), `thread-2-header-cards` (the name opened),
   `thread-3-financials-window` (the Financials header card's window open), `thread-4-thesis-cards` (the Thesis tab),
   `thread-5-recommendation-window` (the Recommendation card's window open). Press Escape after each window.
2. **FWD-2's four lists, read.** On each lead-panel List view the walk reads every row: `data-row-lead`, `data-row-ticker`,
   `data-row-name-state` and the row's visible text, and writes all four lists to `lead-lists.json` in the walk's output folder
   (beside findings.json), so the CVO reads which columns each row shows.
3. **The timeline's states.** For every opened `--security`, after its overlay step: press one day bar (`[data-day-bar]`, the
   newest), run a checks step labelled `<sec>-timeline-day` (the day's articles, strongest first, or the day's words); then look
   for an event span (`[data-timeline-event]`): open the first and run `<sec>-timeline-event`, else record a measured finding with
   check `timeline:no-event-element` (the panel builds no event layer today -- the walk must say so, never pass silently).
4. One line in `.claude/skills/ui-walk/SKILL.md` documenting `--thread` and `lead-lists.json`.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network beyond the walker's own localhost run, no install, no push, no deploy. REFUSE, do not rescue.
   Never run the walker signed in; never arm, disarm or read the secret of the walker account (`ui_walker_account.py`); the
   walker change is proven statically and by the issuer's walk. `--no-login` runs (the AC2 control) are allowed.
2. Only the files in `<paths>` change. The network guard, DO_NOT_CLICK list, account handling and outputs are unchanged apart
   from the above.
3. Commit with safe-commit on your branch.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~25/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `.claude/skills/ui-walk/signin_detect.mjs`, `.claude/skills/ui-walk/ui_walker_account.py`
(never run it), `portal/src/pages/SecurityAnalysis/components/RankedList.tsx` (the row attributes), `components/TimelinePanel.tsx`
(`data-day-bar`), and the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-u-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/walkthread.cjs"; echo "exit=$?"</invocation><expect>WALK GRADES BY NAME: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-u-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/walkvoid.sh"; echo "exit=$?"</invocation><expect>SIGNED-OUT CONTROL: the walk FAILS on the sign-in page: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-u-4" judgment="true"/>
  <criterion id="AC4" cell_refs="AV-u-4" judgment="true"/>
  <criterion id="AC5" cell_refs="AV-u-4" judgment="true"/>
  <criterion id="AC6" cell_refs="AV-u-4" judgment="true"/>
  <criterion id="AC7" cell_refs="AV-u-4" judgment="true"/>
</proof_of_spec>

AC1 is the built walker, read statically; AC2 the bound (the round-4 sign-in guard still fails a signed-out walk; it needs the 5174 build serving -- if it does not answer 200, AC2 prints "not runnable": file a BLOCKING row and report). The FIVE JUDGMENT criteria are graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in round-6 walk (thread Valero; names VLO US, INTU US, SAP GY, 992 HK; routes /security-analysis, /market, /positioning, /philosophy), never self-graded: AC3 DSGN FWD-1 (the thread, hop by hop); AC4 DSGN FWD-2 (the four lists, from lead-lists.json and the list shots); AC5 DSGN FWD-11 (the side-by-side read); AC6 AMGT_HARVST FWD-5 (a day opened, its articles strongest first); AC7 AMGT_HARVST FWD-6 (event spans with a headline, or the walk's `timeline:no-event-element` finding). One walk grades both projects' clauses; nothing is walked twice.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~25/DSGN_AMGTV1.TO-AV-u-4.the-walk-grades-by-name.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 6 = round-5 analysis s.4 item 4 + CTO~Z msg 26751 (AMGT_HARVST ROUND_ANALYSIS.round19.md ruling 5 @a251f02116: HARVST FWD-5 / FWD-6 graded on this walk). Base walk.mjs @CLOUD: walkthread 0 of 3; green (scratch walkThread + readLeadList + walkTimeline) 3 of 3; walkvoid YES.

<status>pending</status>
<round>6</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
