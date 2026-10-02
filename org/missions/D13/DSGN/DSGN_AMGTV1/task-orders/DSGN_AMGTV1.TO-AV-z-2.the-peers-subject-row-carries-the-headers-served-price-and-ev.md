# DSGN_AMGTV1 task order -- `AV-z-2` -- THE PEERS SUBJECT ROW CARRIES THE HEADER'S SERVED PRICE AND EV

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-z-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~69</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 24646bca (= origin DEV 3ca6c53a for src/pages/SecurityAnalysis) -- subjectrow.cjs 2 of 3 (FAIL as expected: Price "--" want "204.80", EV "--" want "193,511"; arms 2-3 PASS by design). Blind spot: the BA fixture's header carries no P/E, so the P/E clause is not graded by the fixture; the issuer's close reads BA and VLO on the served page.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-z-2` (round 22, decomposition v22; serves FWD-8)

DIRECT ACT, the SECOND order on your slot: it starts from your own AV-z-1 commit (same portal branch, same worktree). The CTO's
round-21 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round21.md` @e14de1769c, section 3A row A2): the Peers
table's subject row prints "--" for Price and EV that the page's header carries. Fill them from the header's SERVED values:
- The header's served figures are the overlay's `header_figures` (hook `useSecurityOverlay(securityKey)` in
  `portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts`, the same query the header uses, so no new fetch). Price is the figure
  with `mnemonic: "PX_LAST"`; EV is `CURR_ENTP_VAL` (served in MILLIONS, the same unit as the EV column -- its relation reads
  "direct (USD millions)"). These are the header cards' own mnemonics (`constants.ts` HEADER_CARD_DEFS).
- In `tabs/PeersTab.tsx`, the subject row's (`data-csc-row="subject"`) Price and EV cells print the served value through the column's
  own `formatValue` rule (|v| >= 1000 -> en-US grouping, 0 decimals; else 2 decimals), so the subject reads like its members:
  BA's fixture reads "204.80" and "193,511". This holds even where the Price column is PRESENT_NOT_CARRIED for the members.
- A P/E cell fills only if the overlay serves a P/E header figure (`PE_RATIO`, trailing); the header cards carry none today, so it
  stays "--". With no header figure served, the cells stay "--": the page invents nothing (C-PRESENTATION-ONLY).
- Member rows, summary rows and the column set do not change. Keep AV-z-1's guard intact.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served.
C-FRIDAY -- a served unit prints as served, never rescaled. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code
may sit in a data attribute, never in visible text; no light ink on a white panel. The shared Friday CONTRACT:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md`.

**Harness changes:** a peers harness listed in `<paths>` may gain a `useSecurityOverlay` stub (or re-anchor a subject-row claim) if
the new hook call breaks its render -- never a deleted check.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~69/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/` and
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-z-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/subjectrow.cjs"; echo "exit=$?"</invocation><expect>THE PEERS SUBJECT ROW CARRIES THE HEADER'S PRICE AND EV: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-z-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms, then tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 the subject row's Price and EV read the header's served figures in the column's format; arm 2 with no header figure
served both read "--" (no invention); arm 3 the comparator rejects a "--" cell and a 10%-off value. AC2 keeps AV-z-1's outcome, the
TYPECHECK and all 14 page harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~69/DSGN_AMGTV1.TO-AV-z-2.the-peers-subject-row-carries-the-headers-served-price-and-ev.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance.**
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO round-21 analysis @e14de1769c row A2. Queued on ~69 behind AV-z-1 (shared PeersTab.tsx
and peers harnesses); handed by continuing the worker. Base subjectrow 2 of 3 on DEV 24646bca.

<status>pending</status>
<round>22</round>
<slot>~69</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
