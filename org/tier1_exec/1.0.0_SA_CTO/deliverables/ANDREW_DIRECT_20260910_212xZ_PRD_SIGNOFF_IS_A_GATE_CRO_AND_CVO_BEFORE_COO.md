# ANDREW-DIRECT 2026-09-10 ~21:2xZ — THE PRD CARRIAGE REVIEW IS A GATE, NOT A REVIEW: CRO AND CVO SIGN OFF BEFORE THE COO GETS THE PRD. AUTOMATIC.

**Terminal:** `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`, same turn.

---

## VERBATIM AND ENTIRE

> I dont want to ask shit this should be entirely automatic and gated, CRO and CVO should have to sign off on PRD
> before COO gets it.

Preceded, same conversation: *"i like the spine amendment, lets get it drafted and then /draw it for me with the
headlines"* and the question *"Is this review systematized?"* (answer: no).

---

## WHAT IT CHANGES IN THE DRAFT, AND WHY THE DRAFT WAS WRONG

The v3.14 draft made the carriage review a **non-hold** with a two-hour time box, on the reasoning that an
agent-made gate is invisible to him. **He has now explicitly asked for the gate, and named its shape:** two
sign-offs, both required, before the COO receives the PRD. The non-hold clause, the time box and the "silent reads
as NONE" rule are all withdrawn. The limb becomes a GATE with two mechanical carriers:

1. **The L4 notifier gates its COO delivery** on both sign-offs existing for the PRD at its current pin. Until
   then it delivers only to the two reviewers.
2. **The L6 gate's step-4 conformance limb refuses a task order** whose PRD lacks either sign-off at the PRD's
   current `prd_version`. A sign-off is version-bound: a bump re-opens it.

## SEPARATION OF DUTIES, so the CTO cannot sign its own document

The PRD lives in lane `ANY_CTO`; the reviewers cannot write it and the CTO must not be able to forge a sign-off. So
a sign-off is a FILE in the reviewer's own lane, not a field the CTO edits:

```
org/missions/D<n>/<MACRO>/<CODE>/prd/signoff/<serial>.json
{ "prd": "<CODE>_PRD.md", "prd_version": "v0.4", "prd_pin": "<commit>", "verdict": "SIGNED" | "REFUSED",
  "review_ref": "<path>@<pin>", "signed_by": "<serial>", "signed_at": "<UTC>" }
```

Lane `TREE_PRD_SIGNOFF`: `4.0.0_SA_CRO` writes `4.0.0_SA_CRO.json`; `3.0.0_SA_CVO` writes `3.0.0_SA_CVO.json`;
tilde lanes of each carry it; nobody else. A `REFUSED` verdict carries the review record's path and the PRD does
not proceed until the CTO bumps `prd_version` and both re-sign.

## WHAT EACH REVIEWER SIGNS FOR — unchanged from the draft, now binding

- `4.0.0_SA_CRO`, the BRIEF half: every entry of the PRD's BRIEF COVERAGE map carries the section's CONTENT into
  its consuming cell — fields, units, paths, guards, proof gaps — not a pointer; the heading denominator matches
  the brief at the pin the header names.
- `3.0.0_SA_CVO`, the RATIFIED-TEXT half: every DONE WHEN, ACCEPT and PROOF in the ENDPOINT section is verbatim
  from the ratified pins; every operative constraint present; no annotation, history or seat name inside it; the
  CONTRACTS section agrees with the counterpart PRD where one exists.

## NON-RETROACTIVITY, ON THE SPINE'S OWN v3.13 RULE

A round is graded against the law in force at its cut. The two IRPT PRDs were reviewed ad hoc by both seats before
this word (CVO d0e72ccd56; CRO e975e96fc0, 637b2f8178, and VERIFIED v0.4 at 204832Z). **They satisfy the gate in
substance and receive their sign-off files from the two reviewers as the first exercise of the lane** — not by the
CTO writing them.

## WHAT LANDS, IN ORDER, ALL ON THIS WORD

1. The spine: L4-R as a GATE (text in the rewritten amendment), ladder row v3.14.
2. `.owned-paths.yaml`: lane `TREE_PRD_SIGNOFF` over `org/missions/*/*/*/prd/signoff/**`.
3. `.tools/to-pipeline-gate.py`: the step-4 conformance limb gains the sign-off check, with self-test arms
   (missing, REFUSED, stale version, both SIGNED).
4. `.tools/prd-header-notify.py`: delivery to `4.0.0_SA_CRO` and `3.0.0_SA_CVO` on every new-or-bumped header;
   delivery to `2.0.0_SA_COO` only when both sign-offs exist at that version, re-checked on each sign-off commit.
5. Same-turn broadcast, push state stated.

## SCOPE

The PRD sign-off gate. Not a change to L1, L5 or any other owner. Not a hold on the two IRPT decompositions already
underway, which proceed under the law at their cut and receive sign-offs from the reviewers as the lane's first act.
