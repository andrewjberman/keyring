# DSGN_AMGTV1 task order -- `AV-w-4` -- EXEC MANAGEMENT: THE LAST DARK BAND AND ITS RAW "READ DETAIL"

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-w-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~16</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV a93071b8 -- exec.cjs 0 of 3 (FAIL as expected); bound 4 of 4 (PASS; execText and execFallback print CHECKS 5/5). Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-w-4` (round 4, decomposition v4; serves FWD-7, FWD-11)

Round 3 put Exec Management's absence into words on the face. Two things remain on `tabs/ExecManagementTab.tsx`:
1. Its panel header is still the estate `PanelHeader`, which resolves to the dark band -- the page's last second band
   (DESIGN.md C3: one band per page). The Thesis, Posture and Model tabs already carry their own white header (a plain
   header element on the white panel with navy ink, marked `data-thesis-panel-header` / `data-posture-panel-header` /
   `data-model-panel-header`); give Exec Management the same, marked `data-exec-panel-header`, and no estate `PanelHeader`.
2. The "Read detail" drawer (a `<details>`) prints field names and codes: on INTU "roster_status UNRESOLVED-SOURCE;
   roster_reason no declared shape read this section ...; source_item Item 10. Directors, Executive Officers and Corporate
   Governance; source_accession 000089687826000037". The Bloomberg-fallback line prints "roster_status ...; roster_reason
   ...". The officer table on Valero prints upper-case "ABSENT" in cells. Each becomes words: e.g. "Where we looked: the
   company's 10-K, section 'Item 10. Directors, Executive Officers and Corporate Governance' (filing 0000896878-26-000037).
   The section did not list officers in a form this page can read." A missing cell reads as words ("not stated"). No field
   name (roster_status, roster_reason, source_item, source_accession), no status code (UNRESOLVED-SOURCE, ZERO_OFFICERS), no
   upper-case ABSENT/RESOLVED label on the face or in the drawer. The served values stay on data attributes
   (`data-exec-status`, `data-exec-absent-because`, and add `data-exec-roster-status` / `data-exec-source-accession` if a
   harness needs them).

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

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~16/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-w-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/exec.cjs"; echo "exit=$?"</invocation><expect>EXEC BAND AND DETAIL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-w-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/bound.cjs" W4 execPattern.harness.cjs:9 execText.harness.cjs execFallback.harness.cjs tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>W4 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-w-4" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on two served payloads (INTU absent, Valero resolved) and the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: Exec Management adds no second band, and its detail says where the officer list was looked for in words (FWD-7, FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~16/DSGN_AMGTV1.TO-AV-w-4.exec-management-band-and-detail.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = the round-3 analysis's enrichment list @46d28c6c4c section 4 (CTO msg 26587). Decomposition v4.
Base a93071b8: exec.cjs 0 of 3 (FAIL as expected); bound 4 of 4 (PASS; execText and execFallback print CHECKS 5/5).

<status>complete</status>
<round>4</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
