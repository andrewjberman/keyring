# DSGN_AMGTV1 task order -- `AV-zp-1` -- EVERY CARD ENDS IN THE SHARED FOOTER; THE PAGE ENDS WITH THE END LINE; WHAT CHANGED USES THE DESIGNED STATES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~100</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures captured read-only on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal 85e24287 -- repairs38.cjs 2 of 5 (arm 1 FAIL: What changed has no PanelLoading/PanelError and shows a skeleton on a 500, incl. the remount path; arm 2 FAIL: 14 cards with no footer plus the Lead Panel's hand-rolled "date | Source" line; arm 3 FAIL: PageEnd renders 0 times in 17 of 17 renders; KEEP 9/9 and PLANTED 17/17 pass). It reads 5 of 5 with a scratch reference fix loaded through CHECK_SRC_OVERRIDE (type-checked under tsconfig.app.json, 0 errors).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zp-1` (round 38, decomposition v38; a batched cell; serves FWD-11 and FWD-19)

The CTO's round-38 list (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/CTO_LIST_ROUND38.md`) asks for three things on the Security
Analysis page, `portal/src/pages/SecurityAnalysis/`. The check names every offender at base.

1. **What changed uses the designed states (FWD-19).** `components/model/WhatChangedPanel.tsx` hand-rolls its loading state (a
   skeleton) and has no error state. On a failed compare read (a 500) the live page shows skeleton bars, never an error.
   - Requirements:
     - Loading renders the shared `PanelLoading` and an error renders the shared `PanelError`, both from `src/ui/components/states`.
     - An error never shows a skeleton, including on the remount path. A failed probe mounts a second view on the same pair, which
       re-fetches; that path must also settle on `PanelError`.
     - A served compare still draws its table.
2. **Every card ends in the shared footer (FWD-11).** The reference pages (/market, /philosophy) end each card in the shared
   `PanelFooter` (`src/ui/components/panels/PanelFooter.tsx`), which reads as a time and a source: "<date in words> | Source:
   <source>". The Security Analysis cards have none.
   - Requirements:
     - Every card whose payload SERVES a time and a source ends in exactly one shared footer.
     - The time is one of that card's served values, printed in words through `dateWords.ts`.
     - The source names every served source in words, never a raw code.
     - Nothing visible follows the footer inside the card.
     - A card that serves no time or no source prints no footer line at all, never a placeholder (FWD-27).
     - The Lead Panel's hand-rolled "date | Source" line becomes the shared footer.
   - Which served fields each card carries was measured at the cut; the check holds the table. For example:
     - key figures: `header_figures[].vintage` + `header_figures[].source`;
     - recent news: `feed.items[].published_at` + `.publisher`;
     - the timeline: no source is served, so it gets no footer;
     - the Model tab: `model.generated_at` + figure `source`.
     Machine provenance (an s3 path, "pool", `feed.source`, `identity.crosswalk_source`) is never a source.
   - **PanelFooter paints a dark band**, which the light-card checks reject. Add ONE optional prop to `PanelFooter.tsx`, for
     example `ground="light"`. The default must stay the band, so every other page is unchanged; this page passes the light ground.
     A page-owned wrapper, `components/CardFooter.tsx` (new), may hold the time/source formatting.
3. **The page ends with the end line (FWD-11).** /market and /philosophy end with the shared `PageEnd`
   (`src/ui/components/PageEnd.tsx`): "End of <page>. Data as of <date>."
   - Requirements:
     - `SecurityAnalysis.tsx` renders exactly one `PageEnd`, last on the page: "End of Security Analysis. Data as of <served date>."
     - In Security mode the date is the overlay's `price.as_of_date`, else an `axis_reads[].as_of_date`.
     - In Universe mode there is no served page read, so the line carries no date; any date printed must be served.

**Contracts:**
- C-PRESENTATION-ONLY: served values are formatted, never changed. A time or a source is printed only when served.
- `tabs/ModelTab.tsx` belongs to another project this week. Your change there is limited to the footer: one import and one footer
  line inside ModelTab's own Panel. Do NOT touch `modelSheet.ts`.
- `src/ui/components/panels/PanelFooter.tsx` is shared by the whole portal: one optional prop, default unchanged, nothing else.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/components/CardFooter.tsx
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/ui/components/panels/PanelFooter.tsx
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~100/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round38/checks/repairs/repairs38.cjs"; echo "exit=$?"</invocation><expect>WHAT CHANGED USES THE SHARED STATES, EVERY CARD ENDS IN THE SHARED FOOTER, THE PAGE ENDS ON THE SHARED END LINE: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

The KEEP arm inside repairs38.cjs runs nine earlier checks, and each must exit 0. battery29 includes the CI's ESLint step. AC1 takes
several minutes.

## 4a. AMENDMENT 1 (issuer, 2026-10-05 ~08:2xZ, on row DSGN_AMGTV1-Z-W100-S1 and S2)

1. **The page's own harnesses are granted.** battery29 reads 3 of 14 harnesses green because the harness loaders under
   `portal/src/pages/SecurityAnalysis/__harness__/` carry fixed import lists. They lack `CardFooter`, `@/ui/components/PageEnd`,
   `@/ui/components/panels` and `@/ui/components/states`, and the Panel stub lacks PanelFooter. Also, `leadPanelPattern.harness.cjs`
   asserts the retired hand-rolled "date | Source" caption (`source_footer`, `caption_facts_unchanged`).
   - Update the 11 harnesses listed below so they load the new imports (a stub, as each loader already does for shared chrome).
   - Re-point the Lead Panel's caption assertions to the shared footer: its served time and served source, in words.
   - Weaken no other assertion. A harness that asserted something still true keeps asserting it.
2. **No invented clock (row S2).** A card whose served time is a bare day (e.g. `2026-09-15`) must not print a time of day.
   - Format the time in `CardFooter.tsx` from what is served: a day prints as a day, a stamp prints with its time.
   - If PanelFooter only accepts a raw timestamp, it may take ONE more optional prop for a pre-formatted time string, default unchanged.
3. AC2 stays as written: battery29 ALL PASS (0 skipped).

Added to `<paths>` by this amendment:
- `portal/src/pages/SecurityAnalysis/__harness__/{errorEmpty,drafting,execFallback,execText,tabs,shell,execPattern,modelPattern,posturePattern,thesisLadder,leadPanelPattern}.harness.cjs`

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~100/DSGN_AMGTV1.TO-AV-zp-1.footers-end-line-whatchanged-states.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W100-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Sources:** CTO list @0a865d7e8f items 1-2; ROUND37_CLOSE.md section 3 (fwd19 What changed FAIL; the FWD-11 captures).
- **Issuer rulings:**
  - **ModelTab.tsx:** a one-line footer only. AMGT_CORPUS's candidate 75efe9d6 has landed on DEV; COO~X was told before the cut.
  - **PanelFooter.tsx:** a shared estate file, one optional prop with the default unchanged. Flagged to the CTO at the cut; the CTO
    reviews the product-file candidate.
- **Producer gap:** the timeline serves no source, so it gets no footer. Route to RESAPP with the close.
- **Item 3 of the list** (the FWD-11 re-read) is the issuer's real run at the close.

<status>complete</status>
<round>38</round>
<slot>~100</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
