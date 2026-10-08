# DSGN_AMGTV1 task order -- `AV-zzc-2` -- OFFICERS IN THE SERVED ORDER; TWO PACKS, TWO PHRASES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~114</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, rendered offline by the check.
comp-adversary: RUN by the issuer at the cut on portal DEV d1b21c97 -- r51b.cjs 1 of 3 (arm 1 FAIL: the chief executive is drawn first on three bundles whose served first row is another officer; arm 2 FAIL: "class A" reads "research pack"; PLANTED passes). 3 of 3 on a scratch reference edit of the three files. battery29.sh at the base: ALL PASS (0 skipped). The tree was restored after, 0 changes.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzc-2` (round 51, decomposition v51; two small page repairs)

All paths below are under `portal/src/pages/SecurityAnalysis/`.

### 1a. Officers are drawn in the served order (PRD row SAUX-38)

**Today** `tabs/ExecManagementTab.tsx` has a function `orderedOfficers` (about lines 143-153) that re-sorts the served list: the
chief executive first, then the chief financial officer, then the rest. The function that serves the list now ranks it itself, and
on one name (BP/ LN) the page's own sort put the chief financial officer above the chief executive the function had served first.

**Make it:** the page applies no sort of its own. The officer rows are drawn in the order of the served `management.officers`
list, name for name, with no officer dropped. Remove the re-sort (delete `orderedOfficers`, or reduce it to returning the served
list) and correct the comment above it. Nothing else on the tab changes.

### 1b. Two different packs get two different phrases (PRD row SAUX-40)

One screen today says "the research pack built for this name ... Worked" and, just below, "The research team's thesis pillars: no
research pack for this security." They are two different things under one phrase:
- **the pack this system builds for a name.** Its name is served ("the research pack built for this name"). The page does not
  change it. On the page, the bare phrase "research pack" now belongs to this one only.
- **the research team's own document.** The page words this one itself, and today it also calls it "research pack".

**Make it:**
1. `reasonWords.ts`, function `reasonInWords`: the two replacements that produce "research pack" produce "research-team report"
   instead. So "no class A report for this security" reads "no research-team report for this security", and the long form reads
   "because neither a research-team report nor an earnings update is on file for this name". "class B" still reads "earnings
   update". Correct the header comment's sentence "Class A is the research pack" to match.
2. `tabs/ThesisTab.tsx`, in `ResearchTeamPillars`: the sentence "none are stated in the research team's pack." becomes "none are
   stated in the research team's report."
3. Leave `postureCites.ts` alone: its "research pack" is the pack this system builds, which keeps the phrase.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no registry-reaching command, no push, no deploy. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep each file's line endings.
5. If a page harness in the battery asserts the chief-executive-first order on a list served in another order, or the words
   "research pack" for the research team's document, update ONLY that assertion, inside the harness file that asserts it, to the
   new behaviour, and name it in your report.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/reasonWords.ts
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~114/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round51/checks/r51b/r51b.cjs"; echo "exit=$?"</invocation><expect>OFFICERS IN THE SERVED ORDER AND TWO PHRASES FOR TWO PACKS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~114/DSGN_AMGTV1.TO-AV-zzc-2.officers-in-served-order-and-two-pack-phrases.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W114-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** PRD v0.18 @9a07662460 rows SAUX-38 and SAUX-40 (both FWD-27); CTO msg 31675; AMGT_RESAPP
  `ledger/ROUND_ANALYSIS.round78.md` @1a67e26433 R3; rows AMGT_RESAPP-Z-S372 (BP/ LN) and AMGT_RESAPP-Z-S373 (AMD).
- **L5 decision (SAUX-40):** the bare phrase "research pack" belongs to the pack the system builds, because that name is SERVED
  (`/overlay` and `/thesis` `input_provenance`, the `pack` row) and the page does not rewrite a served value. The research team's
  document takes the page's own new phrase, "research-team report" / "the research team's report".
- **Superseded:** `round29/checks/tabs/tabwords.cjs` arm 1 grades the page's own re-sort on a reversed list; SAUX-38 removes that
  sort ("this completes SAUX-32"). tabwords.cjs is not in battery29 and is not a criterion here.

<status>complete</status>
<round>51</round>
<slot>~114</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
