# SPINE AMENDMENT v3.14 — THE PRD SIGN-OFF GATE BETWEEN L4 AND L5

**Status:** RATIFIED ON ANDREW'S WORD, 2026-09-10 ~21:2xZ: *"I dont want to ask shit this should be entirely
automatic and gated, CRO and CVO should have to sign off on PRD before COO gets it."* Record:
`ANDREW_DIRECT_20260910_212xZ_PRD_SIGNOFF_IS_A_GATE_CRO_AND_CVO_BEFORE_COO.md`. **The earlier draft of this
document made the review a non-hold with a time box; that draft is SUPERSEDED by his word and this text replaces it.**
Drafted by `1.0.0_SA_CTO`; lands in the spine, the lane file, the L6 gate and the L4 notifier in that order.

---

## THE HEADLINE

**A PRD reaches the COO only after the brief's author and the verifier have each signed it at its current
version. The L4 notifier withholds the COO delivery until both sign-offs exist, and the L6 gate refuses any task
order cut from an unsigned PRD. The CTO cannot sign its own document.**

## WHY, MEASURED

The two Investor Reporting PRDs landed at 20:21Z as decomposable. Between 20:31Z and 20:48Z, three unrequested
review passes found thirteen defects — a reuse path that was the wrong file, an export with no render owner, three
cells carrying their brief sections by pointer and not by content, contract rows that disagreed across the two
documents, a coverage column that did not exist. Every one would have gone into cells. The flow's gates check three
structural things on a PRD and nothing about whether it carried its brief. The seats that can see that loss are the
brief's author and the holder of the ratified text, and the spine engaged neither before L5.

## THE LIMB

```
### L4-R — The PRD sign-off gate

- Owner: 4.0.0_SA_CRO signs the BRIEF half; 3.0.0_SA_CVO signs the RATIFIED-TEXT half. Not engaged:
  1.0.0_SA_CTO (the author under review; it cannot sign), 2.0.0_SA_COO (it does not receive the PRD until both
  signatures exist), every worker.
- Trigger: the L4 notifier. On every new or bumped PRD header, .tools/prd-header-notify.py delivers the header,
  version and pin to 4.0.0_SA_CRO and 3.0.0_SA_CVO. It delivers to 2.0.0_SA_COO ONLY when both sign-off files
  exist for that prd_version, and re-checks on every commit that touches prd/signoff/.
- Input: the PRD at its committed pin; the brief at the pin brief_ref names; the endpoint at the pins the ENDPOINT
  section cites; the counterpart PRD where the project has one.
- The BRIEF half (4.0.0_SA_CRO): every entry of the BRIEF COVERAGE map carries its section's CONTENT into the
  consuming cell -- fields, units, paths, guards, proof gaps -- not a pointer; the heading denominator matches the
  brief at the named pin. Corrections are returned BY PINNED LINE; a REFUSED verdict carries the review record.
- The RATIFIED-TEXT half (3.0.0_SA_CVO): every DONE WHEN, ACCEPT and PROOF in the ENDPOINT section is verbatim
  from the ratified pins; every operative constraint is present; no annotation, history or seat name is inside it;
  the CONTRACTS section agrees with the counterpart PRD.
- Output, the sign-off: org/missions/D<n>/<MACRO>/<CODE>/prd/signoff/<serial>.json, written by the reviewer in
  lane TREE_PRD_SIGNOFF (4.0.0_SA_CRO and 3.0.0_SA_CVO and their tilde lanes; nobody else):
    { "prd": "<CODE>_PRD.md", "prd_version": "vX.Y", "prd_pin": "<commit>", "verdict": "SIGNED" | "REFUSED",
      "review_ref": "<path>@<pin>", "signed_by": "<serial>", "signed_at": "<UTC>" }
  A sign-off is VERSION-BOUND: a prd_version bump re-opens both; the notifier re-fires to the reviewers on the
  delta and withholds the COO again until both re-sign.
- Gate, two carriers, both mechanical:
    (1) the notifier withholds the COO delivery without both SIGNED files at the current version;
    (2) .tools/to-pipeline-gate.py's step-4 conformance limb REFUSES a task order whose PRD lacks a SIGNED file
        from each reviewer at the PRD's current prd_version, or carries a REFUSED one. Self-test arms: missing,
        REFUSED, stale version, both SIGNED.
- Separation of duties: the PRD is lane ANY_CTO and the sign-off files are lane TREE_PRD_SIGNOFF; the CTO cannot
  write a sign-off and the reviewers cannot write the PRD. A sign-off names the pin it reviewed, so a later
  edit to the PRD without a bump is visible as a pin mismatch and is refused by (2).
- Non-retroactivity (v3.13): a round is graded against the law at its cut. A PRD already decomposed before this
  limb landed is not re-cut; its reviewers sign it as the lane's first act if the ad hoc review already happened,
  and the gate binds from the next prd_version.
- Cost: two reads per PRD version, on the critical path by design. Measured 2026-09-10: thirteen corrections in
  three passes on two PRDs the flow had already declared decomposable.
- Non-application: a prd_version bump that touches only the header is signed on the header alone; an L10 addendum
  that changes no cell row is signed on the ENDPOINT delta alone.
```

## THE LADDER ROW

```
| 3.14 | 2026-09-10 | Andrew-direct ~21:2xZ at the 1.0.0_SA_CTO terminal, "I dont want to ask shit this should be
entirely automatic and gated, CRO and CVO should have to sign off on PRD before COO gets it"; measured cause:
3.0.0_SA_CVO d0e72ccd56 and 4.0.0_SA_CRO e975e96fc0 / 637b2f8178 on the two IRPT PRDs, thirteen corrections in three
unrequested passes | L4 gains **THE PRD SIGN-OFF GATE** (L4-R): the brief's author signs the coverage map for
CONTENT carriage, the verifier signs the ENDPOINT section against the ratified pins and the CONTRACTS section against
the counterpart; both sign-offs are files in the reviewers' own lane, version-bound to the PRD; the L4 notifier
withholds the COO delivery until both exist and the L6 gate refuses a task order from an unsigned PRD. The CTO cannot
sign its own document. Two mechanical carriers, one new lane, no new owner. |
```

## WHAT THIS DOES NOT CHANGE

L4 stays the CTO's alone; the reviewers sign or refuse, they do not author. L5 stays the COO's and begins when the
notifier delivers, which is now after both signatures. L8, L9 and the L9 coverage-limb grade are unchanged; this
limb is earlier, and the L9 grade remains the backstop. L1 ownership is unchanged.

## LANDING ORDER

1. Spine: this block after L4; the ladder row; the version line.
2. `.owned-paths.yaml`: lane `TREE_PRD_SIGNOFF` over `org/missions/*/*/*/prd/signoff/**`.
3. `.tools/to-pipeline-gate.py`: the sign-off check in the step-4 conformance limb, with four self-test arms.
4. `.tools/prd-header-notify.py`: reviewer delivery on every bump; COO delivery gated on both sign-offs.
5. Same-turn broadcast with push state.
