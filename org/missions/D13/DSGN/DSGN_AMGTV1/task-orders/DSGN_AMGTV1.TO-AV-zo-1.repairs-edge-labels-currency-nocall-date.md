# DSGN_AMGTV1 task order -- `AV-zo-1` -- REPAIRS: NO LABEL ACROSS A BUBBLE; NO CROSS-CURRENCY AVERAGE; THE NO-CALL STATE IS DATED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zo-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~99</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures captured read-only on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal DEV 56b71adb -- repairs37.cjs 2 of 5 (arm 1 FAIL: 90D "IDEXX Laboratories Inc", 365D "Synopsys Inc" and "Kim..." straddle a bubble outline; arm 2 FAIL: 18 faults incl. MSFT Peers "Average 158,633 (n=12)" over mixed prices; arm 3 FAIL: 9 no-call renders print no date; KEEP 8/8 and PLANTED pass). It reads 5 of 5 with a scratch reference fix loaded through CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zo-1` (round 37, decomposition v37; a batched repair cell; serves FWD-21, FWD-8 and FWD-10)

Three faults in `portal/src/pages/SecurityAnalysis/`, each seen on the served DEV build. The check names every offender at base.

1. **A collage label straddles a bubble's outline (FWD-21: "no label clips or overlaps").** In `components/ChatterBubbles.tsx`
   (window mode), the live 365D collage draws "Kim..." (Kimberly-Clark) across the edge of its own bubble, and "Synopsys Inc" across
   its own bubble's edge. At 90D "IDEXX Laboratories Inc" does the same.
   - The fault: the last-resort placement (`:468-474`) accepts a slot that "only this label's own bubble touches". A label half
     inside and half outside its own bubble crosses the outline.
   - Requirements:
     - A label sits wholly inside its own bubble or wholly outside every bubble, its own included.
     - It meets no other label and no other bubble.
     - No leader line crosses a label other than its own.
     - Every label box stays inside the viewBox.
   - Keep round 34-36's rules: labels at 11px or larger, deterministic layout (no clock, no random), a shortened label's `<g>`
     carries a `<title>` with the full served name, every bubble keeps its hover, and a label with no clean slot may drop.
   - **Measured at the cut:** a strict rule alone leaves 3 names unlabelled on round 29's synthetic 95-name month, which breaks
     `round29 collage.cjs` (run by the KEEP arm). The scratch reference fix falls back to the old placement only when a label has no
     clean slot anywhere. On the served 30/90/365 windows every label is then clean. You may use that or a better rule.
2. **The peer table averages prices in different currencies (FWD-8; the CTO's rule: "no cross-currency average ever; a mixed group
   says it is mixed and prints no average").** On MSFT US Peers the "Price (last)" column holds local prices (2,365; 230,500 ...)
   with no currency, and the page-computed summary rows average them with USD prices ("Average 158,633 (n=12)").
   - What the payload serves, measured: `members[].cap_currency` (USD on 12 of 12, Mkt Cap only) and `subject.currency`. **No
     member carries a price currency.** A member's `country` is never a currency.
   - Requirements (`cscTable.ts` `:178` builds the summaries; `tabs/PeersTab.tsx` `:231-235` prints them):
     - A money column whose members are not all one SERVED currency prints no Average/Median/Min/Max. Instead it says, in words,
       that the values are in different or unstated currencies.
     - A column that is one served currency (Mkt Cap in USD) keeps its summaries.
     - A price whose currency is not served is never labelled with a guessed one.
   - Until the producer serves a member price currency, the Price column prints no summary on any name.
3. **The "no call" state has no date (FWD-10: "no call reads as a designed empty state with its date").** AMD and MSFT read "No call
   on this name yet / no posture has been drafted for this name yet; the research team adds one", with no date anywhere.
   - What the payload serves, measured: the posture block is `status ABSENT`, `as_of` absent, `posture_read.as_of null`. The
     thesis read carries `generated_at`.
   - Requirements, in `components/LeadPanel.tsx` (`:321`), `components/SecurityOverlay.tsx` (`:212`) and `tabs/PostureTab.tsx`
     (`:540`):
     - Every no-call render prints a served date in words: the posture's own date first, then its read's date, then the thesis
       read's `generated_at`. Print it through `dateWords.ts` (`longDate` or `longStamp`), for example "as of October 5th, 2026".
     - With no served date, print no date. Never invent one.
   - **Interface the check pins:** LeadPanel's `PostureHeaderLine` takes a `readAt` prop carrying that served date.

**Contracts:**
- C-PRESENTATION-ONLY: served values are formatted, never changed. A date or a currency is printed only when served.
- No hard-coded colour outside `lib/chartColors.ts` tokens and the panel ink tokens the files already use.
- Do NOT touch `tabs/ModelTab.tsx` or `modelSheet.ts`: another project (AMGT_CORPUS) owns them this week.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~99/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zo-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round37/checks/repairs/repairs37.cjs"; echo "exit=$?"</invocation><expect>NO LABEL ACROSS A BUBBLE, NO CROSS-CURRENCY AVERAGE, THE NO-CALL STATE IS DATED: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zo-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

The KEEP arm inside repairs37.cjs runs rounds 29, 34, 35 and 36's checks (eight of them), and each must exit 0. battery29 includes the
CI's ESLint step.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~99/DSGN_AMGTV1.TO-AV-zo-1.repairs-edge-labels-currency-nocall-date.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W99-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Sources:** CTO enrichment list @9b2ed08fe2 items 1-3; COMPLETION_GRADES.round36.json rows FWD-21, FWD-8, FWD-10 (@c706123ec2).
- **Producer gap, not this cell:** no peer member carries a price currency (`members[]` has `cap_currency` only). Until RESAPP serves
  one, the Price column carries no summary on any name, the conservative reading of "never". Routed to the CTO at the close for
  RESAPP.
- **Item 4 of the list** (reads of FWD-5/11/19) is the issuer's real run at the close: `round37/walk/reads37.mjs`.
- **Not graded here** (the issuer's close walk): the collage at 365D in a browser; the Peers face on MSFT; the dated no-call on AMD.

<status>complete</status>
<round>37</round>
<slot>~99</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
