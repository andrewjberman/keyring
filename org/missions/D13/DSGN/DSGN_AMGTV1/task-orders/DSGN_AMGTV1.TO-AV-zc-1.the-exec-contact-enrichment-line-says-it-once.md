# DSGN_AMGTV1 task order -- `AV-zc-1` -- THE EXEC CONTACT-ENRICHMENT LINE SAYS IT ONCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~74</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from a fixture.
comp-adversary: RUN by the issuer at the cut on portal 41eeda55 -- lushaline.cjs 2 of 3 (FAIL as expected: the line repeats "Contact enrichment was skipped"; arms 2-3 PASS by design).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-zc-1` (round 24, decomposition v24; serves FWD-11)

DIRECT ACT. The CTO's ruling (msg 28350, on row DSGN_AMGTV1-Z-S14): "when the served Lusha reason is code-free, print it alone, as one
sentence." In `portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`, the SKIPPED line (`<p data-lusha-enrichment="SKIPPED"
data-lusha-reason=...>`, ~line 315-325) prints "Contact enrichment was skipped for this company" and then " -- <served reason>" when the
reason has no code-shaped token (`hasCodeShapedToken` from `../reasonWords`). The served reason now reads "Contact enrichment was
skipped: no company web domain is on record for this name, and a guessed domain would enrich the wrong company", so the phrase repeats.
Change the line so that:
- a CODE-FREE served reason prints ALONE (its text, trimmed; a period added only if it has none);
- a reason that HAS a code-shaped token, or no reason at all, keeps the page's plain sentence "Contact enrichment was skipped for this
  company.";
- `data-lusha-reason` keeps carrying the served reason in both cases.
Nothing else on the page changes. Presentation only.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY. **Design law (portal `DESIGN.md`):** a code may sit in a
data attribute, never in visible text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the file in `<paths>` changes (plus your deliverables and the channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites the file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~74/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/`,
`round23/`, `round22/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/checks/lushaline.cjs"; echo "exit=$?"</invocation><expect>THE CONTACT-ENRICHMENT LINE SAYS IT ONCE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zc-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/accession.cjs" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms, then THE EXEC FACE NAMES THE FILING, NOT ITS ACCESSION: 3 of 3 arms, then tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 a code-free served reason prints alone with the phrase once; arm 2 a coded reason keeps the plain sentence and the attribute;
arm 3 the comparator rejects a repeat. AC2 keeps rounds 22-23's Exec outcomes (codeface arm 3 needs a plain Lusha reason printed
verbatim, which this change keeps), the TYPECHECK and all 14 harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~74/DSGN_AMGTV1.TO-AV-zc-1.the-exec-contact-enrichment-line-says-it-once.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W74-S<k>`.
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO ruling 28350 on Z-S14; fold in only if re-merged and walked by 11:30Z. Chain ~74 alone.

<status>complete</status>
<round>24</round>
<slot>~74</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
