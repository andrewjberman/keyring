# AMGT_RESAPP task order -- `AMGT-vv-3` -- THE FOUR PAGE HARNESSES RUN AGAIN, NONE BLINDED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-vv-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~169</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the harnesses render committed fixtures in node; nothing reaches AWS.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a harness made to pass by making it blind: the bound forbids deleting or weakening a check, and a check that reads a REAL page defect is REFUSED with a row, never edited to agree with the page.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-vv-3` (round 47, decomposition s.55)

The page harnesses under `portal/src/pages/SecurityAnalysis/__harness__/` render the Security Analysis page in node (each
transpiles page sources itself) and check what it shows. Four no longer run clean at portal DEV (measured at the cut):

1. `shell.harness.cjs` and `posture.harness.cjs`: `Error: Cannot find module '@/api/api-client'` -- `HeaderBrief.tsx` now mounts
   `TimelinePanel.tsx` (AMGT_HARVST `92a25762`), whose `@/` imports these loaders cannot resolve (row `Z-W167-S1`; `shell` also has
   a second, older break behind it). Round 46 fixed the SAME class in `exportCompare.harness.cjs` with one `SOURCE_STUBS` entry that
   renders `TimelinePanel` as nothing (the timeline is not what these harnesses check) -- read it as the precedent.
2. `tabs.harness.cjs`: `Error: Cannot find module '@/ui/components/graphic/HeroGraphic'` -- another `@/` import its loader cannot
   resolve.
3. `leadPanelPattern.harness.cjs`: loads, prints 15 `CHECK` lines, and reads 4 the wrong way --
   `rows_rendered`, `source_caption_wraps`, `disclosure_own_line`, `caption_facts_unchanged` (row `Z-W167-S2`: it predates round 38's
   rm-5 change to the lead panel's Source caption).

**Build:** make each harness load the page as it is and report truthfully. For a loader gap, stub or resolve the import, stating in
a one-line comment which and why. For each wrong-way check, READ the page source it checks and decide: (a) the check encodes an
OLD page contract that a later ratified cell changed (name the cell or commit) -> bring the check to the current contract; or (b)
the page is actually wrong -> REFUSE AC2 with a row naming the check, the page line, and what it shows. Never delete a check, never
make one vacuous, never edit a page file.

## 2. BOUNDS

1. **Harness files only** (the four named). No page file, no Python, no fixture edit.
2. **No server; no vite; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~169/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, including every page source the harnesses load.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-vv-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-3.AC1.sh; echo "exit=$?"</invocation><expect>HARNESSES LOAD AND PASS: 3 of 3 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-vv-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-3.AC2.sh; echo "exit=$?"</invocation><expect>leadPanelPattern: rc=0; checks printed 15 (or more); CHECKS-WRONG-WAY none -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~169/AMGT_RESAPP.TO-AMGT-vv-3.the-four-page-harnesses-run-again.proof_of_spec.json`. Report once: per harness what you changed and why (for each of the four wrong-way checks, (a) with the cell/commit that changed the contract, or (b) with the row), the verdict counts, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-46 analysis s.4 item 3 (rows Z-W167-S1, -S2), widened at the cut to the fourth harness (`tabs`, HeroGraphic)
measured the same way. Base at portal DEV 5fac7a37 (measured on the shared tree after DSGN_AMGTV1's merges): AC1 FAIL (0 of 3 load), AC2 FAIL (4 wrong-way). LOCAL: the instruments only.

<status>complete</status>
<round>47</round>
<slot>~169</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
