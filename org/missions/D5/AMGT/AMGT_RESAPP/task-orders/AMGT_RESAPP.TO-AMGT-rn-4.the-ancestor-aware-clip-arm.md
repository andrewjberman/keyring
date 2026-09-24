# AMGT_RESAPP task order -- `AMGT-rn-4` -- THE ANCESTOR-AWARE CLIP ARM: the detector sees the unsignalled clip C13 forbids

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rn-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~149</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-38 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. The self-test loads a static fixture with page.setContent; no dev server, no fetch.
</preflight>

## 1. THE CELL -- `AMGT-rn-4` (round 39, decomposition s.47)

rm-6 reproduced the pre-rm-5 caption clip by reading and found it UNSIGNALLED: no `overflow-hidden`, `clip` or `text-overflow` on
the leaf, its parent or grandparent -- the cut came from `flex-shrink-0` plus flexbox's implicit `min-width:auto` at an ANCESTOR
frame. `ui-measure.mjs`'s `clippedTextBlocks` reads overflow properties off the LEAF (the classifier, `:58` onward) and reads 0 on
that defect. **Build:** (1) an ANCESTOR-AWARE arm in the classifier: a text-bearing element whose `scrollWidth` exceeds its
`clientWidth` counts as clipped when ANY ancestor up to the panel frame (`[data-tab-panel]` or `main`) has `overflow` other than
visible on the axis, OR when the element's rendered box is cut by an ancestor whose `min-width` resolves to `auto` under a flex
row with `flex-shrink: 0` on the path -- state the rule you implement in the docstring; keep the leaf-only count printed beside it
(`clippedTextBlocks` stays the graded field, `clippedByAncestor` is the new one, and the graded field becomes their union) ;
(2) a static fixture `__harness__/tests/uiClipFixture.html` reproducing rm-6's case exactly (its deliverable describes the DOM:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/`), and a `--self-test --fixture` branch that prints ONE
line `ANCESTOR-CLIP leafOnly=<a> ancestorAware=<b>`; (3) `ui-contract-check.mjs` reports the new field in both tables;
(4) the instrument paragraph the CTO moved out of C13 (L4R_C13_RATIFIED.md, amendment three) goes into `ui-measure.mjs`'s
docstring: the check reads overflow off the leaf and off the ancestor path, and what it still cannot see.

## 2. BOUNDS

1. **No server.** The six-state read is the issuer's after the merge; your criteria are the self-test and the diff.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-149-portal` at DEV `5e339ffd`.
3. No page or component source moves (AC2). Standing: no install, no push, no promote. REFUSE, do not rescue.

## 3. SURFACES

<paths>
portal/scripts/ui-measure.mjs
portal/scripts/ui-contract-check.mjs
portal/src/pages/SecurityAnalysis/__harness__/tests/uiClipFixture.html
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~149/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rn-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-4.AC1.sh; echo "exit=$?"</invocation><expect>leafOnly=0 ancestorAware=N with N at least 1 on the unsignalled fixture, the self-test's own POSITIVE/NEGATIVE arms still passing, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rn-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-4.AC2.sh; echo "exit=$?"</invocation><expect>src files moved off the base other than the fixture: 0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~149/AMGT_RESAPP.TO-AMGT-rn-4.the-ancestor-aware-clip-arm.proof_of_spec.json`.
Report names the rule implemented in one sentence, the fixture's DOM in one line, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 item 6 (measure-first became build: the fixture IS the measurement and the arm its consumer). The six-state
bound (`clippedTextBlocks` 0 in both scopes with the new arm) is the issuer's `checks/drain.rn-4.clipped.sh` on 5174 after the merge.

**ISSUER CLOSE, 2.0.0_SA_COO~Z, 2026-09-24 ~18:5xZ, carried on the worker's branch so the chain-end merge carries it.**
Checker's match: proof-of-spec-check VALID rc=0 on the worker's instance (2 of 2 PASS-by-output); not re-run by the issuer.
AC1: `ANCESTOR-CLIP leafOnly=0 ancestorAware=1`, SELF-TEST OK, the seven existing self-test checks still passing; the worker
ran a mutant control (the flex-sizing predicate disabled flips ancestorAware to 0 and fails the self-test) and reverted it.
AC2: 0 src files moved off the base other than the fixture. Rule: a leaf counts as ancestor-clipped when an ancestor up to the
panel frame has non-visible overflow, the path holds a flex-row child with flex-shrink:0 and min-width:auto, and the leaf's box
is cut past that ancestor's edge; `clippedTextBlocks` is now the union, `clippedTextBlocksLeafOnly` and `clippedByAncestor`
printed beside it. No rows. The six-state bound (clippedTextBlocks 0 in both scopes with the arm live) is the issuer's
`checks/drain.rn-4.clipped.sh` on 5174 after the round's last merge. Portal merged 88305686 -> DEV e2ac795a.

<status>complete</status>
<round>39</round>
<slot>~149</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
