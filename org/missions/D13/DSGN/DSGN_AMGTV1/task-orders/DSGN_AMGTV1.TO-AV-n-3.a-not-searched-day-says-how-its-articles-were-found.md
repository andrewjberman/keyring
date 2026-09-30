# DSGN_AMGTV1 task order -- `AV-n-3` -- A "NOT SEARCHED" DAY THAT CARRIES SERVED ARTICLES SAYS HOW THEY WERE FOUND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-n-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~42</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cuts (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 2bb60cc3 -- denied.cjs 1 of 3 (FAIL as expected: the DENIED day with 2 served articles reads "Not searched on this day"; its tooltip reads "not searched on this day -- 1 found anyway"; the control passes at base by design); green arm 3 of 3; ALL 16 of 16 harnesses and Q3 4 of 4 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0; 0 control bytes. Blind spot: static markup; the tooltip is rendered from its content element, the hover itself is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-n-3` (round 11, decomposition v11; serves AMGT_HARVST FWD-5, FWD-11)

The CTO's ruling (round-10 analysis, ruling 4): on 992 HK the day dissection read "NOT SEARCHED ON THIS DAY" above two served
articles. The data is honest -- no collection run searched 992 HK that day, and the articles surfaced from other names' searches --
but the page contradicts itself. A DENIED day that carries served articles reads "not searched for this company directly -- N
articles found in other searches". This is page wording from served fields only; the coverage state stays AMGT_HARVST's and nothing
is re-derived. Build, in `portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx` only:
1. The day dissection (`DayDissection`): a day whose `data_status` is DENIED and which carries N > 0 served articles reads, in its
   heading, "Not searched for this company directly -- N articles found in other searches" ("1 article" singular), above its rows.
2. The chart tooltip (`DayTooltip`): a DENIED day with `articles_total` N > 0 reads "<long date>: not searched for this company
   directly -- N articles found in other searches" ("1 article" singular) -- never "found anyway".
3. Nothing else moves: a DENIED day with 0 articles keeps "Not searched on this day" / "No articles this day"; PARTIAL and COMPLETE
   days are unchanged; the rows, their served order, every `data-` attribute (`data-dissection-status="DENIED"` included) and the
   legend ("not searched") stay as they are.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: the count is the served
articles' count, nothing is computed or re-derived. **Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data
attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the page
now states it, keep its claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness
needs a change, so none is granted.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~42/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/dateWords.ts`, `portal/DESIGN.md`, and the
issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-n-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/denied.cjs"; echo "exit=$?"</invocation><expect>A NOT-SEARCHED DAY SAYS HOW ITS ARTICLES WERE FOUND: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-n-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bound.cjs" Q3 timelineFourStates.harness.cjs errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>Q3 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-n-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-n-3" judgment="true"/>
</proof_of_spec>

AC1 is the built heading and tooltip on the SERVED 992 HK /timeline and its 2026-08-13 /timeline/day (DENIED, 2 articles) plus
labelled 1- and 0-article variants, with the rows, order, status and legend checked unchanged; AC2 the bound on every harness that
loads the timeline or the page around it; AC3 no control byte in the page's source. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9
on the issuer's signed-in walk (992 HK's opened days), never self-graded: the page no longer contradicts itself -- a PM reads how
articles on an unsearched day were found (HARVST FWD-5, FWD-11). Portal typecheck, if you run one: `node_modules/.bin/tsc -b
--noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~42/DSGN_AMGTV1.TO-AV-n-3.a-not-searched-day-says-how-its-articles-were-found.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11 = the round-10 analysis s.4 item 3 with ruling 4. Base 2bb60cc3: denied.cjs 1 of 3; green 3 of 3; ALL 16 of
16; tsc rc=0.

<status>complete</status>
<round>11</round>
<slot>~42</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
