# AMGT_RESAPP task order -- `AMGT-ro-3` -- THE THESIS SECTION CARRIES THE HEADER'S VERDICT: a section headed 'Company description' only when its sentences describe the business

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~154</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-39 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-ro-3` (round 40, decomposition s.48)

The identity header says *"Description: ABSENT -- ... no served D-1 company_description sentence passing the
describes-the-business test"*, computed server-side for `/overlay` in `lib/research/api/scoped_amgt.py`
(`read_security_overlay` -> `description`; tests in `lib/research/api/tests/test_description_line.py`). The Thesis tab renders
the drafter's `company_description` section as its own block under the heading "Company description"
(`portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:272-274` and its render) even when none of its sentences passes that
test -- for BA the block holds backlog figures. **The header is CORRECT; the section is the defect** (round-39 analysis s.5):
do not touch the header. **Build:** (1) the thesis route's payload carries, on the company-description section, the SAME
verdict the overlay computes -- one function, called by both routes, never a second implementation -- as additive fields
(state and reason); a test module `lib/research/api/tests/test_thesis_description_verdict.py` proves both routes agree on a
passing and a failing fixture; (2) `ThesisTab.tsx` renders the "Company description" heading over the section only when the
verdict passes; when it fails, the block renders the SAME ABSENT sentence the header shows, and the drafted sentences stay
reachable under a heading that says what they are (your wording, one line, no claim they describe the business).

## 2. BOUNDS

1. **No server.** You start no vite, dev build or listener (Andrew-direct: portal dev builds use port 5174 only, and that
   run is the issuer's). Your criteria are the files named below, run from the worktree root exactly as written.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-154-portal` at DEV `46c0ae11`. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.
3. Standing: no install, no push, no promote, no S3 write, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_thesis_description_verdict.py
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~154/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-3.AC1.sh; echo "exit=$?"</invocation><expect>the cell's test module exists and passes (N passed, 0 failed) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ro-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-3.AC2.sh; echo "exit=$?"</invocation><expect>drafting exit=0, tabs exit=0, tsc exit=0 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ro-3" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git diff --stat $(git merge-base HEAD CLOUD) -- lib/research/api/scoped_amgt.py portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx; echo "exit=$?"</invocation><expect>the change set a person reads to judge whether the Thesis section now says only what its sentences are; RECORDED, no verdict (the round-39 ruling: a cell that changes what a served section claims carries a judgment criterion)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~154/AMGT_RESAPP.TO-AMGT-ro-3.the-thesis-section-carries-the-verdict.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 item 3. `scoped_amgt.py`'s thesis route only; the print route is ro-1's library, not this file's section. Served only through ro-7's deploy.

<status>pending</status>
<round>40</round>
<slot>~154</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
