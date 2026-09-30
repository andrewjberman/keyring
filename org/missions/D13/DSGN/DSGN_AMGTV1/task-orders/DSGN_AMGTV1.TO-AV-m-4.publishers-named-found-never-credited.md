# DSGN_AMGTV1 task order -- `AV-m-4` -- EVERY PUBLISHER IS NAMED, A FOUND-ONLY ARTICLE IS NEVER CREDITED TO A SEARCHED PUBLISHER, AND A NEVER-COLLECTED TIMELINE SAYS SO IN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-m-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~47</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 846ecc6c -- publishers.cjs 0 of 3 (FAIL as expected: ft, bbg and barrons read "a publisher this page has no name for yet"; 992 HK's served day reads "Searched: a publisher this page has no name for yet -- 2 found." -- crediting its one searched publisher with two found elsewhere; the day's rows and the news list print raw codes (wsj, sa); the never-collected timeline reads "No chatter_daily rows exist for this security_key yet"); green arm (scratch r12-green-c @1227560a, an issuer-spawned helper) 3 of 3, tsc rc=0, bytes 3/3. The green arm put the name map in TimelinePanel.tsx and turned shell.harness.cjs RED (its TimelinePanel stub lacks the new export); the same helper measured an import-free `components/publisherNames.ts` shared by both files: shell 10/10, posture unchanged, no harness edit -- that is the form granted below. Blind spots: static markup; the day tooltip is not rendered by the check (it uses the same sentence function).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-m-4` (round 12, decomposition v12; serves FWD-11 and AMGT_HARVST FWD-5 page half)

The CTO's ruling 1 (round-11 analysis), on AMGT_HARVST PRD v0.4 `C-HV-COVERED-VS-FOUND`: a day row keeps two publisher sets --
`publishers_covered_codes` (the publishers whose listing for the name ran that day: SEARCHED) and `publishers_found_codes` (the
publishers whose articles the day serves, by whatever path; HARVST round-27 q-5 serves it once a rebuild and a deploy carry it --
today no day carries it). "The page renders a publisher in the FOUND set but not the COVERED set as 'found, listing not run'.
Where the field is absent, the page says the day's search record does not say how the articles were found. It never credits a
covered publisher with them. The page's publisher-name map names every code the estate serves (bbg included)." The estate's codes
are the `publisher` enum of `lib/opal_data_harvest/article.schema.json`: sa, ft, wsj, bbg, barrons. Build, under
`portal/src/pages/SecurityAnalysis/`:
1. **Names:** a new import-free module `components/publisherNames.ts` holding the name map -- sa Seeking Alpha, wsj The Wall
   Street Journal, bbg Bloomberg, barrons Barron's, ft Financial Times -- and a `publisherName(code)` function (an unknown code
   reads the fixed phrase "a publisher this page has no name for yet", a missing one "unknown publisher"; never the raw code).
   `components/TimelinePanel.tsx` (its `PUBLISHER_NAMES` / `searchedLine`, the day's `ArticleRow`) and `components/HeaderBrief.tsx`
   (the news list's `FeedItemRow`, which prints `item.publisher` raw) read names through it.
2. **Found vs searched** (`TimelinePanel.tsx`): the "Searched:" line names only the covered publishers and never attaches the
   day's article count to them. A publisher in `publishers_found_codes` but not in the covered set reads "<name>: found, listing
   not run". Where `publishers_found_codes` is absent and the day serves articles, the day says its search record does not say how
   they were found (e.g. "2 articles are served for this day; the day's search record does not say how they were found."). The
   day tooltip reads the same. `publishers_found_codes` is added as an OPTIONAL field on the page's day types.
3. **The never-collected timeline** (the `NEVER_COLLECTED` PanelEmpty detail): in words, no field or table name -- e.g. "No
   articles have been collected for this company yet -- this is not the same as a quiet company with no articles."
4. **Nothing else moves:** round 11's DENIED wording ("Not searched for this company directly -- N articles found in other
   searches"), the served rows and their order, every `data-` attribute and the legend stay as they are.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: the sets and counts are
served; nothing is inferred about how an article was found. **Design law (portal `DESIGN.md`):** a code, field name or path may sit
in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. With the shared module above, the issuer's helper measured no
harness change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/publisherNames.ts
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~47/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/opal_data_harvest/article.schema.json`, `portal/DESIGN.md`, and the issuer's
checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-m-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/publishers.cjs"; echo "exit=$?"</invocation><expect>PUBLISHERS NAMED, FOUND NEVER CREDITED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-m-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bound.cjs" Q3 timelineFourStates.harness.cjs shell.harness.cjs:10 posture.harness.cjs:32 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>Q3 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-m-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-m-4" judgment="true"/>
</proof_of_spec>

AC1 is the built day dissection, panel and news list on the SERVED 992 HK /timeline/day/2026-08-13 (PARTIAL, covered [bbg], two
articles from wsj and sa, no found set), BA US /timeline/day/2026-09-08 (DENIED, five articles) and /overlay, and 6501 JP /timeline
(never collected), plus a labelled planted found set: every served code named; Bloomberg named as searched and never credited; the
absent found set said in words; the planted found-only publishers read "found, listing not run"; the never-collected state in
words; the DENIED wording unchanged. AC2 is the bound on every harness that loads the timeline, the header brief or the page around
them; AC3 no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (992 HK's and BA's
opened days, the news list, 6501's timeline), never self-graded: a PM reads which publishers were searched and never mistakes a
found article for a searched one (FWD-11, HARVST FWD-5). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit`
inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~47/DSGN_AMGTV1.TO-AV-m-4.publishers-named-found-never-credited.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 12 = the round-11 analysis s.4 item 4 with ruling 1, plus s.4 item 5's never-collected sentence (same file
as this cell: placed here so the chains' write sets stay disjoint). Base 846ecc6c: publishers.cjs 0 of 3; green r12-green-c
@1227560a 3 of 3 (shell RED in that form); the publisherNames.ts form measured by the helper with no harness change.

<status>pending</status>
<round>12</round>
<slot>~47</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
