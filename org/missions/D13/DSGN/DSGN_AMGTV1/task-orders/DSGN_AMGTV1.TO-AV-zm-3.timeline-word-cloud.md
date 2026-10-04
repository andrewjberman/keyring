# DSGN_AMGTV1 task order -- `AV-zm-3` -- THE TIMELINE'S WORD CLOUD: THE SERVED TERMS, SIZED BY THE SERVED COUNT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zm-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~96</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures captured on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal 055ba370 -- cloud35.cjs 2 of 5 (arms 1-3 FAIL: 0 [data-word-cloud] containers on BA, VLO and AMD; KEEP and PLANTED pass). It reads 5 of 5 with a scratch reference fix loaded through CHECK_SRC_OVERRIDE, and 1 of 5 when only TimelinePanel.tsx is overridden (negative control).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zm-3` (round 35, decomposition v35; serves FWD-5)

PRD FWD-5 (v0.14): "The word cloud renders the terms AMGT_RESAPP FWD-39 serves (`word_cloud` on the timeline payload), sized by the
served count; an empty served list renders its served reason. The page counts nothing."

The timeline range route (`/api/scoped/amgt/security/<key>/timeline`, already read by
`portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx`) now serves one more key:

```
word_cloud: {
  terms: [{ term: string, count: number }],   // count = headlines carrying the term; ordered count desc, then term asc; at most 40
  window: { from: 'YYYY-MM-DD', to: 'YYYY-MM-DD' } | null,
  reason: string | null                         // null only when terms is non-empty
}
```

Served captures: `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round35/fixtures/timeline.<key>.json` (BA, VLO,
AMD, MSFT, ASML NA, ROG SW; each serves 40 terms over 2026-01-01..2026-10-03). The producer's empty reasons include "no coverage
headlines in this window".

Build the word cloud into the timeline card:
1. Add `word_cloud` to the range response type in `TimelinePanel.tsx`, as an optional key because an older payload has none.
2. Render a word cloud from the served terms in a new component, `components/TimelineWordCloud.tsx`. TimelinePanel renders it when
   the range read resolves, inside the timeline card, near the chart.
3. The DOM contract the check grades:
   - One container carrying `data-word-cloud`, with value `terms` (non-empty served list), `empty` (served list empty: print the
     served `reason` verbatim inside it) or `absent` (no `word_cloud` key: print a short designed sentence, and do not crash).
   - Each served term is ONE element carrying `data-term="<served term>"` and `data-count="<served count>"`, in served order. It
     has a hover name (a `title`) that holds the term and its count, for example "refinery -- in 10 headlines", and an inline
     `font-size` in px.
   - When `window` is not null, the container prints the served window in words through `dateWords.ts`'s `longDate`, in every
     state (an empty list with a window prints it too). When `window` is null, no "undefined", "null", "NaN" or "Invalid Date"
     prints.
   - The hover name is a `title` ATTRIBUTE on the term element (not a `<title>` child: the static renderer hoists one outside an
     `<svg>`). No `[data-term]` element renders outside the container.
   - The new component lives under `src/pages/SecurityAnalysis/` (shared chrome under `src/components/**` and `src/ui/**` renders as
     a stub in the checks).
4. Size each term by its served count. A larger count is never smaller, no term is below 11px, and the largest is visibly larger
   than the smallest when the counts differ.
   - Use ONE data-family hue from `lib/chartColors.ts` for every term. The served terms carry no sentiment, so do not use the
     market page's sentiment colours or any status colour.
   - Keep the layout deterministic (a flowed, wrapped cloud: no random placement, no clock). It must render in a static render.
   - Weights stay within 400/700 and the font stays Lato.
5. The page counts nothing: every count printed or used is the served one.

**Contracts:**
- C-PRESENTATION-ONLY: served terms and counts are printed as served.
- One purple action per view; no hard-coded colour outside `lib/chartColors.ts` tokens and the panel ink tokens the file already uses.
- Keep the round-29 timeline checks and the round-34 navy axis ink passing.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/TimelineWordCloud.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~96/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round35/checks/cloud/cloud35.cjs"; echo "exit=$?"</invocation><expect>THE WORD CLOUD RENDERS THE SERVED TERMS SIZED BY THE SERVED COUNT: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zm-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

The KEEP arms inside cloud35.cjs run the round-29 timeline check and the round-34 repair check, and each must exit 0. battery29
includes the CI's ESLint step.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~96/DSGN_AMGTV1.TO-AV-zm-3.timeline-word-cloud.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W96-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** decomposition v32-B (the cell is cut against the served shape when a route serves the field). RESAPP AMGT-ap-4
  closed 2026-10-04 ~00:5xZ on FcVBPafw; the issuer's capture at the cut (`round35/fixtures/capture_timeline.py`) reads 40 terms
  on 6 of 6 names.
- **Upstream, not this cell:** RESAPP aq-1 (FWD-39 list repair: a company's own words, e.g. "amd" on AMD) is in RESAPP round 67,
  not yet deployed. The page prints what is served.
- **Not graded here** (the issuer's close walk): how the cloud reads in place, and the hover in a browser.

<status>complete</status>
<round>35</round>
<slot>~96</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
