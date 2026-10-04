# DSGN_AMGTV1 task order -- `AV-zi-2` -- ONE NEWS ITEM AT REST, THE REST ONE PRESS AWAY: THE TABS START INSIDE THE FIRST VIEWPORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zi-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~89</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders HeaderBrief statically from captured and planted fixtures.
comp-adversary: RUN by the issuer at the cut on portal 2defab11 -- feedrest.cjs 3 of 4 (arm 1 FAILS as expected: 2 open, "67 more"); with FEED_OPEN_AT_REST = 1 planted through CHECK_SRC_OVERRIDE it reads 4 of 4.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zi-2` (round 31, decomposition v31; serves SAUX-15 and FWD-12 / FWD-27's first viewport)

At 1440x900 on BA, the first tab panel must start above y=900.
- The round-30 close walk measured the active tab's underline at y=917, so the first panel started at about y=943.
- The served BA feed grew from 1 item to 69, so the news card now draws 2 open items plus "Expand (67 more)".
- One open item at rest recovers about 49 px.

Build, in `portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx` only:
1. **One news item open at rest.**
   - Exactly ONE `[data-feed-item]` sits outside the closed Expand `<details data-feed-expand>`. Every other item sits inside that
     one closed details.
   - Its summary names the remaining count in words: "Expand (68 more)" for 69 items, "Expand (4 more)" for 5.
   - With 1 served item, that item is open and no Expand is drawn.
   - Today this is `const FEED_OPEN_AT_REST = 2` (line 87). Update its comment to say one item.
2. **Keep everything the existing checks read:**
   - one `[data-header-feed]`;
   - every item still in the markup with its `data-feed-item` and title, and a link only where a url is served;
   - the description in a closed `<details>` with a words summary;
   - no timeline of its own; `postureLine` ignored.
   - `HEADER_FEED_VISIBLE_COUNT` in `constants.ts` is not yours. Leave it.
3. **Optional, inside this file only:** trim the news card's own vertical padding or line gaps by a few pixels if it reads cleanly.
   Remove no text.

The tab-bar position is graded at the issuer's close walk, not by a check here.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. The base worktree's
   files may be CRLF; keep each file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~89/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository. In particular, the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round31/`, `round30/` and `round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round31/checks/viewport/feedrest.cjs"; echo "exit=$?"</invocation><expect>ONE NEWS ITEM AT REST, THE REST ONE PRESS AWAY: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zi-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1's KEEP arm also runs, and needs both of these to exit 0: the round-29 `timeline/dayopen.cjs` and the round-30
`repairs/served.cjs`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~89/DSGN_AMGTV1.TO-AV-zi-2.one-news-item-at-rest.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W89-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, the pixels you removed
(if any beyond the one item), and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded here:** the tab-bar y (measured at the close walk, target: first panel above 900); how one item plus Expand reads.
- **Model:** worker-light on the Sonnet override. The account hit its weekly model limit (resets 17:00Z) and the session was idle
  ~01:57Z to ~16:2xZ; the order was issued at 16:39Z.

<status>complete</status>
<round>31</round>
<slot>~89</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker-light</worker_class>
