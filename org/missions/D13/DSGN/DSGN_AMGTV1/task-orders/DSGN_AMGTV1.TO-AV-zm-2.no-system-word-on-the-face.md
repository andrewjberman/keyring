# DSGN_AMGTV1 task order -- `AV-zm-2` -- NO SYSTEM WORD ON THE FACE: EVERY "NOT CARRIED ON THIS PAYLOAD" SAYS WHAT IS MISSING IN PLAIN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~95</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically.
comp-adversary: RUN by the issuer at the cut on portal 055ba370 -- payload35.cjs 2 of 4 (RENDERED FAIL: 0 of 18 surfaces clean; CENSUS FAIL: 14 graded literals across 40 files; KEEP and PLANTED pass). It reads 4 of 4 with a scratch reference fix of 9 files loaded through CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zm-2` (round 35, decomposition v35; serves FWD-27 "no system wording on the face")

The Security Analysis page's designed empty states print the system word "payload". A PM does not know what a payload is. The
sentences, in `portal/src/pages/SecurityAnalysis/`:

- `components/GenerationCaption.tsx:35` -- "generation: not carried on this payload";
- `components/LeadPanel.tsx:302` and `components/SecurityOverlay.tsx:193` -- "Posture: not carried on this payload.";
- `components/SecurityOverlay.tsx:427` -- "sector/country not carried on this payload";
- `components/StatTile.tsx:172` -- "not carried on this payload";
- `tabs/ExecManagementTab.tsx:376`, `:455` -- "<heading>: not carried on this payload."; `:410` -- "Source: the report is not named
  on this payload";
- `tabs/PostureTab.tsx:513`, `:564` -- "Posture: ..." and "Fund of record and last stated position: not carried on this payload.";
- `tabs/ThesisTab.tsx:113` -- "<pillars heading>: not carried on this payload."; `:163` -- "Source: the report is not named on this
  payload";
- `components/ThesisCards.tsx:234` -- "A passage from a filing this payload does not name";
- `readCompleteness.ts:88` -- "this payload carries no read_completeness field..." (a reason a person reads).

Rewrite each one in plain words that name the missing thing, in the form "<the missing thing> is not in this security's data" (for
example "Sector and country are not in this security's data", "Source: the report is not named in this security's data"). The exact
words are yours, under three rules:
- no visible text on the page says "payload";
- each sentence still names what is missing;
- each stays a designed empty state, with the same component, data attributes and conditions as now. Only the words change.

Comments, identifiers and machine `data-*` values (for example `data-completeness-state="NO_PAYLOAD"` in `RankedChart.tsx`) that
say "payload" may stay; the rule is about text a person sees. Note `GenerationCaption`'s sentence reaches the page only through the
`data-generation-detail` attribute; it is graded there, so reword it too. A field name in a sentence (`read_completeness`) is
system wording as well: say what is missing in words.

**Contracts:**
- C-PRESENTATION-ONLY: no served value changes; only the page's own sentences change.
- The data attributes the existing checks read (`data-header-posture`, `data-generation-caption` and the rest) stay as they are.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/readCompleteness.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~95/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zm-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round35/checks/words/payload35.cjs"; echo "exit=$?"</invocation><expect>NO SYSTEM WORD ON THE FACE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zm-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

The KEEP arms inside payload35.cjs run the round-29 header, round-32 wording and round-34 repair checks over the same files, and
each must exit 0. battery29 includes the CI's ESLint step.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~95/DSGN_AMGTV1.TO-AV-zm-2.no-system-word-on-the-face.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W95-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** ROUND34_CLOSE.md section 4 item 3 (@a408efb24a): FWD-24's designed empty state read "sector/country not carried on
  this payload" on the close walk of 055ba370.
- **Issuer instrument to amend at the close walk:** `round34/walk/gapread.mjs:518-520` expects the old sentence for the FWD-24
  control; it is the issuer's, not this cell's.
- **Not graded here** (the issuer's close walk): how the sentences read in place.

<status>complete</status>
<round>35</round>
<slot>~95</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker-light</worker_class>
