# DSGN_AMGTV1 task order -- `AV-ze-1` -- EVERY BAR AND BUBBLE CARRIES ITS SERVED IDENTITY ONE HOVER AWAY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-ze-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~78</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from captured fixtures.
comp-adversary: RUN by the issuer at the cut on portal fa529337 (PROD's tree; = DEV 415f50db for src/pages/SecurityAnalysis) -- identity.cjs 1 of 3 (FAIL as expected: no hover on any bar or bubble; arm 3 PASS by design).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-ze-1` (round 27, decomposition v27; serves FWD-2)

DIRECT ACT. The CTO's completion grades (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/COMPLETION_GRADES.round26.json` @0c4c6d6368) read FWD-2
NOT_REALIZED, a PAGE cell, on CVO~Z's `surprise-channel/adjudications/ADJUDICATION_v26.md` @07446385f1 (read both). FWD-2 (PRD v0.8, v0.6
restatement): "The same identity -- name, ticker, asset class, sub-asset class, sector, the period figure and places moved -- is read
on each FWD-21 bubble and each FWD-22 bar (its label, or one hover away). DONE WHEN: the walk reads every identity field on 3 bubbles
and 3 bars; no mark names a company by a code alone."

Today (`portal/src/pages/SecurityAnalysis/components/`):
- `PriceBars.tsx:116-160`: each bar is `<li data-price-bar=...>` with three spans (label, bar, value) and only an onClick. The served
  price row carries `name`, `ticker`, `classification {asset_class, sub_asset_class, sector}`, `return_30d_pct`, `places_moved` and
  `places_moved_reason` (see `RankingRowBase` in `../types.ts:139-170`), but none of it reaches the bar except name and value.
- `ChatterBubbles.tsx`: each bubble mark carries `data-bubble` and `data-chatter-bubble`; it shows only the name and the count. The
  served collected-chatter row (`CollectedChatterRow` in `../types.ts:207`) carries only `security_key`, `display_name`, `by_month`.

Build:
1. **Bars:** each `[data-price-bar]` element gets a native hover title (`title` attribute) that reads, in plain words: the name (or the
   ticker when no name is served), the ticker, the asset class, the sub-asset class, the sector (a null sector is said: "sector not
   served"), the period figure (the served `return_30d_pct`, one decimal with its sign, as the bar shows it), and places moved (the
   served `places_moved` in words: "up 2 places", "down 1 place", "no change"; when it is null, the served `places_moved_reason` in plain
   words through `guardedReason` from `../reasonWords`).
2. **Bubbles:** each `[data-bubble]` mark gets a hover title (an SVG `<title>` child of the mark's element, or a `title` attribute) that
   reads the served `display_name`, the month's collected count, and each identity field the chatter row SERVES. Add the optional fields
   to `CollectedChatterRow`: `ticker?`, `classification?` (same shape as the ranking row's), `places_moved?`, `places_moved_reason?`. A
   field the row does not serve is said in words ("classification not served", "places moved not served"). Never invent a value, and
   never join it from another payload: serving these fields on chatter rows is the producer's (routed to the CTO).
3. No hover text carries a code-shaped token (snake_case, `_Equity`, `.json`, UPPER_SNAKE). The served `display_name` prints as served.
Nothing else changes: the bars' order, colours, click and starred filter, and the bubbles' layout and month cursor all stay.
Presentation only. Do not edit `tabs/*`, `LeadPanel.tsx` or any harness.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served. C-FRIDAY -- a
served unit prints as served. **Design law (portal `DESIGN.md`):** a code may sit in a data attribute, never in visible or hover text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~78/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round27/`,
`round26/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-ze-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round27/checks/identity.cjs"; echo "exit=$?"</invocation><expect>EVERY BAR AND BUBBLE CARRIES ITS SERVED IDENTITY: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-ze-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round26/checks/battery.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY: ALL PASS -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 the three largest-move bars carry every served identity field one hover away; arm 2 the planted bubbles carry every served
field and a bare row says what is not served; arm 3 the comparator rejects a hover missing the ticker or carrying a code. AC2 is the
round 20-26 battery (12 checks, 14 page harnesses, the TYPECHECK).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~78/DSGN_AMGTV1.TO-AV-ze-1.every-bar-and-bubble-carries-its-served-identity.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W78-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO COMPLETION_GRADES.round26 FWD-2 NOT_REALIZED (page cell). Chain ~78 alone. Base identity 1 of 3.

<status>pending</status>
<round>27</round>
<slot>~78</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
