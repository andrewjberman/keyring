# DSGN_AMGTV1 task order -- `AV-zd-1` -- THE LIVE SERVED ABSENT REASONS ARE CLASSED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~77</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from a fixture.
comp-adversary: RUN by the issuer at the cut on portal 7889655a -- liveclass.cjs 1 of 3 (FAIL as expected: the five live served reasons read `unmapped`; arm 3 PASS by design).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-zd-1` (round 26, decomposition v26; serves FWD-16)

DIRECT ACT. `portal/src/pages/SecurityAnalysis/reasonWords.ts` carries a table from each served Peers absent-column reason (exact text,
case and surrounding space ignored) to a class (`not-reported`, `ratio-only`, `one-year-estimates`, `leverage-undefined`,
`three-year-growth`), with `unmapped` for an unknown reason. The producer now serves FIVE of those reasons in new words (registry labels
in place of factor codes), so they read `unmapped` on the live page. Add these five served strings to the table, each at the SAME class
as the old string for the same column -- keep the old strings too:
- Cash -> `ratio-only`: `'Cash to Market Value' is a ratio; no absolute cash level`
- P/E 2027 -> `one-year-estimates`: `the value category carries trailing ('Earnings Yield') and NTM ('Earnings Yield NTM') only -- no second-forward-year estimate at any grain`
- Debt/Equity -> `leverage-undefined`: `the registry carries only 'Leverage' (category solvency) and states no numerator or denominator, so reading it AS debt/equity would be inferred, not measured; 'Debt to Assets' is debt to ASSETS`
- 5-yr growth EBIT -> `not-reported`: `no EBIT growth measure at any window ('EBIT to Enterprise Value' is a yield, 'EBIT Estimate Revisions (45D)' an estimate revision)`
- 5-yr growth FCF -> `not-reported`: `no FCF growth measure at any window ('Free Cash Flow Yield' and 'Free Cash Flow to Enterprise Value NTM' are yields)`
The table matches case-insensitively, so key them the way the existing entries are keyed. Nothing else changes; an unknown reason still
reads `unmapped`.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the file in `<paths>` changes (plus your deliverables and the channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/reasonWords.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~77/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round26/`,
`round24/`, `round23/`, `round22/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zd-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round26/checks/liveclass.cjs"; echo "exit=$?"</invocation><expect>THE LIVE SERVED ABSENT REASONS ARE CLASSED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zd-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/checks/reasonclass.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/peerwords.cjs" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>EACH ABSENT COLUMN STATES ITS REASON IN READER WORDS: 3 of 3 arms, then THE PEERS ABSENT-COLUMN REASONS ARE IN READER WORDS: 3 of 3 arms, then tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: arm 1 the five live strings are classed, 0 unmapped; arm 2 each keeps its predecessor's class; arm 3 an unknown reason still reads
unmapped. AC2 keeps rounds 23-25's Peers outcomes, the TYPECHECK and all 14 harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~77/DSGN_AMGTV1.TO-AV-zd-1.the-live-served-absent-reasons-are-classed.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W77-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). Issuer's round-25 close-walk finding. Chain ~77 alone. Base liveclass 1 of 3 on 7889655a.

<status>pending</status>
<round>26</round>
<slot>~77</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
