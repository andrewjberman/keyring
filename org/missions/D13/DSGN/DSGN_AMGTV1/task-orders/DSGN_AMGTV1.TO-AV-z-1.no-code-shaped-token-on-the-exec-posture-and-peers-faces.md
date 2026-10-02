# DSGN_AMGTV1 task order -- `AV-z-1` -- NO CODE-SHAPED TOKEN ON THE EXEC, POSTURE AND PEERS FACES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-z-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~69</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 24646bca (= origin DEV 3ca6c53a for src/pages/SecurityAnalysis) -- codeface.cjs 2 of 3 (FAIL as expected: exec 2 tokens, posture 1, peers 20; arms 2-3 PASS by design); bound ALL 14 of 14 and tsc rc 0 (controls PASS). Blind spot: a fixture render sees BA only; the issuer's close reads BA, VLO and AMD on the served page.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-z-1` (round 22, decomposition v22; serves FWD-11)

DIRECT ACT. The CTO's round-21 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round21.md` @e14de1769c, section 3A row A1;
read it): Exec, Posture and Peers render a plain reason whenever the string they would print carries a code-shaped token. The
CTO's rule (section 1): a served string is fixed at its producer, not rewritten on the page; **the page keeps ONE guard -- it never
prints a code-shaped token, and it falls back to a plain generic reason**. The served string may ride a `data-` attribute.

A code-shaped token, in VISIBLE text (attributes are not text), is any of: `[a-z]+_[a-z0-9_]+` (a field code: `ey_ntm`, `cash_mv`);
`_Equity` (a security key such as `VLO_US_Equity`); `\.json` (a file name such as `domains.json`); the state words `ABSENT` and
`UNMAPPED`; `[A-Z][A-Z0-9]*_[A-Z0-9_]+` (a vendor mnemonic or a state code such as `PRESENT_NOT_CARRIED`).

The sites, measured at the cut (all under `portal/src/pages/SecurityAnalysis/`):
1. `tabs/ExecManagementTab.tsx:315-318` prints `Lusha enrichment: SKIPPED -- {lusha.reason}` verbatim. The live VLO reason is
   "no declared domain for VLO_US_Equity in domains.json". The line must read as plain words (for example "Contact enrichment was
   skipped for this company."), with the served reason kept only in a `data-` attribute whenever it carries a token; a reason with
   no token prints as served.
2. `tabs/PostureTab.tsx` prints each served `posture.basis[].claim` verbatim. The fixture's claim 2 reads "Both names' fit scores are
   ABSENT rather than low ...". Under the guard a claim with a token prints a plain generic reason; the served claim rides a
   `data-` attribute. (Its producer fix is routed to the CTO; do not reword served prose on the page.)
3. `tabs/PeersTab.tsx:186-196`, the "Absent columns" disclosure, prints `{column.column}: {column.state} -- {column.reason}`. The state
   word (`ABSENT` / `UNMAPPED`) is never printed (say it in words, e.g. "not in the comparison map"), and a reason with a token falls
   back to a plain generic reason. The column-head tips (`HelperTip content={column.reason}`) follow the same guard.
4. `cscTable.ts:131` writes its own reason `in the factor registry (${present.code}); R-1 carries no per-member value for it` -- a page-
   written code. Word it without the code (the code may ride the column's data, never its text).
Put the token test in ONE function (a small module such as `reasonWords.ts`, or restated per file if a page harness cannot resolve
a new import), so every site applies the same rule. Presentation only: no fetch change, no served value moves. Do not edit
`tabs/ModelTab.tsx` (AMGT_CORPUS's) or `__harness__/errorEmpty.harness.cjs` (another order's).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served.
C-FRIDAY -- a served unit prints as served; the page never constructs a date. **Design law (portal `DESIGN.md`, portal `CLAUDE.md`
colour law):** a code, field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white
panel. The shared Friday CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** a page harness listed in `<paths>` may be RE-ANCHORED where it asserts the old visible words (for example a
claim that reads "ABSENT --" or "Lusha enrichment: SKIPPED") -- never a deleted check, never a weakened expectation.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/reasonWords.ts
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~69/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/` and
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-z-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs"; echo "exit=$?"</invocation><expect>NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-z-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders ExecManagementTab, PostureTab and PeersTab over the BA fixture with the served strings the analysis names planted (the
VLO Lusha reason, an absent-column reason naming `ey_ntm` and `factor_metadata_registry.json`, the fixture's own "ABSENT" claim):
arm 1 reads 0 tokens over the three faces; arm 2 proves the census catches each class; arm 3 proves plain served words still print
verbatim (the guard must not blank a reason that carries no token). AC2 the TYPECHECK and all 14 page harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~69/DSGN_AMGTV1.TO-AV-z-1.no-code-shaped-token-on-the-exec-posture-and-peers-faces.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO round-21 analysis @e14de1769c row A1 (msg 28252). Chain ~69: AV-z-1 then AV-z-2 (same
worker, continued). Drain by 11:30Z or drop. Base codeface 2 of 3 on DEV 24646bca.

<status>pending</status>
<round>22</round>
<slot>~69</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
