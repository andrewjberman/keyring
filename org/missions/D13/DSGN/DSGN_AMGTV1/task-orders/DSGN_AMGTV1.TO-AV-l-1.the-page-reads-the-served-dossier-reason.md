# DSGN_AMGTV1 task order -- `AV-l-1` -- THE PAGE READS THE SERVED PER-FIELD DOSSIER REASON AND NEVER CLAIMS A RESEARCH PACK THAT DOES NOT EXIST; THE CONTRACT FIXTURES ARE THE LIVE SHAPES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-l-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~49</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV ba62e945 -- dossier.cjs 0 of 3 (FAIL as expected: 6501 JP, which has no dossier, reads "The research team's thesis pillars: none are stated in the research team's pack." and the same pack claim on its header, Posture and Exec lines; BA reads it too instead of its served reason; all 10 contract-fixture routes differ from the live shapes); green arm (scratch r13-green-a @3a9f4c25, an issuer-spawned helper) 3 of 3; bytes 3/3; portal tsc -b rc=0; 16 harnesses: 15 green and leadPanelPattern RED on the refreshed fixture (the live rankings are no longer a dated read; the page is right) -- the tested re-anchor below brings it to 15 of 15. Blind spot: static markup; the per-field served reasons are shown verbatim, and BA's carry producer words (a round-14 input, not this cell's).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-l-1` (round 13, decomposition v13; serves FWD-11 and AMGT_CORPUS's no-dossier outcomes) -- IT LEADS THE ROUND

The CTO's ruling 1 (round-12 analysis): AMGT_RESAPP ab-2 (ratified) serves a no-dossier name as the full `dossier_fields` block,
each field ABSENT with its reason -- `thesis_pillars_absent: {status: 'ABSENT', reason}`, and `{status: 'ABSENT', value: null,
reason}` on `fund_of_record`, `last_stated_position`, `management` and `pack_shape` (6501 JP: "no research dossier exists for this
name"); a top-level `dossier_fields.status` with a reason now appears only on a failed read. The page keys its sentences on that
top-level status, so every no-dossier name falls through to "none are stated in the research team's pack" -- asserting a pack that
does not exist. Build, under `portal/src/pages/SecurityAnalysis/`:
1. **Every dossier-field reader reads the per-field served reason in words** (a reason naming a storage path falls back to plain
   words): `tabs/ThesisTab.tsx` (`ResearchTeamPillars`), `components/SecurityOverlay.tsx` (the header's fund line,
   `DossierPositionLine`), `tabs/PostureTab.tsx` (`FundOfRecordLine`), `tabs/ExecManagementTab.tsx` (`ResearchTeamManagement`). E.g.
   6501: "The research team's thesis pillars: no research dossier exists for this name."; "No fund of record: no research dossier
   exists for this name."
2. **A failed read** (a top-level status that is not ABSENT, e.g. READ_FAILED, with a reason) reads a designed sentence with its
   reason ("... the research team's dossier could not be read (<reason>).") and no status token in visible text.
3. **"none are stated in the research team's pack"** (and its siblings) are reachable ONLY when a dossier exists (no top-level
   status, `pack_shape` not ABSENT) and states none. Status tokens and raw reasons may ride `data-` attributes. `types.ts` gains the
   served fields, types only.
4. **Refresh the contract fixtures from the LIVE shapes:** run the issuer's
   `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/grants/refresh_fixtures.py` from the worktree top -- it sets
   the 10 keyed routes of `portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json` to the round-13 captures'
   payloads, verbatim. Do not hand-edit that file.
5. **Harness grant (measured):** the refreshed rankings are not a dated read, so three checks of `__harness__/leadPanelPattern.harness.cjs`
   (stale_dated_said, source_caption_wraps, disclosure_own_line) go RED while the page is right. Apply exactly the issuer's tested diff
   `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/grants/leadPanelPattern.reanchor.diff` (inside `portal/`:
   `git apply <that path, given absolute>`): the three checks read a dated variant of the same payload when the live one is not dated,
   and the live render must then NOT say "This list is from". Nothing else in that harness moves.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page renders what the payload carries: the
per-field reason is served, so the page reads it; nothing is inferred. **Design law (portal `DESIGN.md`):** a code, field name or path
may sit in a data attribute or in code, never in visible text.

**This slot's next order, `AV-l-3` (the three C14 blocks and the raw tokens), follows on the same worktree after you finish.**

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~49/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` and the issuer's checks, fixtures and grants under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-l-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/dossier.cjs"; echo "exit=$?"</invocation><expect>THE PAGE READS THE SERVED DOSSIER REASON: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-l-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/bound.cjs" Q1 leadPanelPattern.harness.cjs:15 posture.harness.cjs:32 execPattern.harness.cjs:9 tabs.harness.cjs:20 shell.harness.cjs:10 thesisLadder.harness.cjs:10; echo "exit=$?"</invocation><expect>Q1 BOUND: 6 of 6 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-l-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-l-1" judgment="true"/>
</proof_of_spec>

AC1 is the built Thesis, header, Posture and Exec surfaces on the SERVED /thesis of 6501 JP (no dossier), BA US (a dossier, no class-A
report) and IMB LN (6 served pillars), plus labelled planted variants (a top-level READ_FAILED; a dossier that exists and states no
pillars), and the refreshed fixture set compared route by route with the issuer's live captures. AC2 is the bound on every harness that
loads those surfaces or reads the refreshed fixtures; AC3 no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the
issuer's signed-in walk (6501 JP's Thesis, header, Posture and Exec), never self-graded: 6501 reads "no research dossier" again and
no page claims a pack that does not exist. Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~49/DSGN_AMGTV1.TO-AV-l-1.the-page-reads-the-served-dossier-reason.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (the visible wording of each fixed line), the harness change, the output line of every criterion,
the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 13 = the round-12 analysis s.4 item 1 with ruling 1; it leads (the portal DEV push waits on it: Andrew-direct
@e1b5fd6d8c card 1, `0.0.0_AB_MSTR~Z` msg 27161 -- signal on drain with the 16 harness invocations). The per-field readers span four
files (not only ThesisTab: the header, Posture and Exec lines made the same pack claim). Base ba62e945: dossier.cjs 0 of 3; green
r13-green-a @3a9f4c25 3 of 3 (6 files); leadPanelPattern re-anchor tested 15/15 then reverted by the helper.

<status>complete</status>
<round>13</round>
<slot>~49</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
