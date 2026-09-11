# DSGN_REBRND v0.2: CVO L4-R correction review

Reviewer: `3.0.0_SA_CVO`. Cut: 2026-09-11 08:43Z. Decision: **SIGN the ratified-text half**. C1-C6 and N1 from the initial adversarial review are closed at the pin below. Both halves were read for the requested adversarial critique; the brief-half stamp belongs to the designated `2.0.0_SA_COO~D`.

This is the review record the canonical stamp will reference. It does not itself claim a committed stamp or gate admission. Those are measured by `python .tools/prd-signoff.py sign DSGN_REBRND --half ratified-text --review <this-path>@<this-commit>` and `python .tools/prd-signoff.py status DSGN_REBRND` after this record is committed.

## Reviewed cut and authority

- PRD: `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@8ad762f7bfb1a0609d2f133934104af726dafdff`, v0.2, all 248 lines. Line references below are to this pin.
- Endpoint: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D13_PORTAL_VISUAL_ELEVATION_20260911.md@8ad762f7bfb1a0609d2f133934104af726dafdff`. The complete v0.1 source was read in the initial review; every intervening source change was read here and all carried fields compared.
- Initial review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_L4R_ADVERSARIAL_REVIEW_20260911.md@638c8085b65474cabecfb469d0722f87c35e64f3`. Its REFUSED decision remains the historical verdict on v0.1.
- Brief: `docs/briefs/portal-visual-elevation-brief-20260911.md@bed01b226a15d80d05269b84dae94f18a1fecfc1`, read in full for the initial review and unchanged as the PRD's pinned input. Its measured limitations and Appendix A table remain part of this review.
- Review assignment: CTO messages 95913 and 95918, on the pinned Andrew instruction `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_080xZ_DSGN_REBRND_COO_D_SIGNS_CVO_ADVERSARIAL_SELF_DRIVE_WIDENED.md@2daf4d8b85d146784ab262f29d67effb222f6990`.
- Governing check: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md@e7e552f7c4752c4e78d196684ca8b76f3bb3d754`, L4-R. ENDPOINT plus CONTRACTS is the CVO half; all other sections form the brief half. A section-byte change requires a current half stamp.

## Corrections checked against the counterexamples

| Finding | Current lines | Result and reason |
|---|---|---|
| C1: history inside ENDPOINT | 20-98; 217-227 | CLOSED. The complete ENDPOINT section, heading through the next heading, contains the outcome block and operative constraints. Dates, superseded archetype history, attribution annotations and renumbering history moved to the separate PROVENANCE AND AMENDMENT HISTORY section. The light canvas, in-place rewrite, chart colour, permanent FWD-9 identity and Andrew-only comparison remain operative. SOURCE citations remain traceable. |
| C2: accent budget conflicts with focus and selection | 44-54; 109-110; 126 | CLOSED. The budget counts one persistent primary-action emphasis. Transient focus and text selection share the accent while data colour has its own budget. FWD-4's three fields were restated in the endpoint source and copied exactly. The original counterexample is now an explicit proof: primary visible, secondary focused, text selected; persistent count remains one. R5, R6 and DesignContract agree. |
| C3: every route forced to reach the fold | 84-89; 114 | CLOSED. Representative routes use named populated fixtures. A valid short populated page is graded on contract spacing and an explicit designed end state. The one-row control is present and cannot fail merely because it ends above the fold; filler, stretched rows and added panels cannot manufacture a pass. The viewport share remains an observation, with no invented occupancy quota. FWD-10's three fields and R10 agree. |
| C4: unsupported token provenance and a self-chosen contrast minimum | 107; 111-112; 122-129 | CLOSED. Every contract value is labelled fixed brand, measured website, preserved data or derived. The source explicitly supplies no status/data/dark-mode/contrast authority. Derived choices carry their rule beside the value; status/ramp/dark-mode rules are stated, and the existing model colours are preserved. The numeric acceptance floor is set in this PRD independently of the later DesignContract: normal text 4.5:1, large text 3:1, and UI boundaries/focus 3:1, identified here as WCAG 2.1 SC 1.4.3/1.4.11. R3 must use that floor or a stricter one across canvas, inverted bands and selected dark mode, printing its text-class/background denominator. Choosing 1:1 in R7 cannot pass. This review accepts the PRD's explicit bar; it does not certify rendered accessibility conformity. |
| C5: unconditional light canvas contradicts retained dark toggle | 28; 105; 107; 126 | CLOSED. Light is the default mode; deliberate dark selection has its own values in the same JSON and matching native `color-scheme`. R3 requires light -> dark -> light with no residual dark declaration, while retaining the default light and inverted-band rules. |
| C6: product claims supported by only three sample routes | 101; 107; 110; 117; 148; 157-160; 200; 244 | CLOSED. R14 produces an affected-surface inventory with the portal route count and every touched state, fixture source, read-render record and interactive keyboard obligation. Every touched layout must be rendered; component reuse cannot substitute. R3 and R6 explicitly consume the expanded coverage and the evidence table binds every-route/every-element claims to it. The original three routes remain the fixed comparison set. The existing verification loop supplies the method. |
| N1: Appendix A counts and invented A21 cleanup portion | 167; 204 | CLOSED. The PRD now records 21 outcome-bearing rows and two cleanup-only rows, A15 and A22, exposing the source prose/table disagreement. A21 remains O11/FWD-9 through R5. There is no invented cosmetic half of A21. |

## Whole-PRD agreement and boundaries

The additional brief-half correction is present at lines 18, 223 and 231: implementation cells write only to `feature/d13-visual-elevation` in both repositories, with worker worktrees drained onto that feature branch. No cell writes DEV or CLOUD. Promotion is a separate act on Andrew's word. The manifest enumerates the R1-R14 implementation surfaces governed by that constraint. This L4-R review and its canonical governance stamp do not execute those cells.

R7's draft source is located on the feature branch at portal `10236236` (lines 111 and 215); it remains input to the ratified contract. The correction does not elevate a draft to authority. The coverage map still accounts for all 32 brief sections and all 23 defect rows. R14 adds the evidence needed for existing claims; it does not add a new product outcome.

The remaining contracts agree at this cut: one brand JSON writer and generated theme CSS, retained dark-mode roles, disjoint status/data families, one chart/icon/animation system, in-place archetype and colour-law rewrite, and the existing render/review loop. IRPT_FNTEND remains a consumer with its v0.6 round-1 basis preserved (line 126). FWD-9 still requires Andrew's recorded word after the comparison he chooses; this stamp does not grade that outcome. No competitor capture, data-plane repair, information-architecture change or wider responsive commission was added.

No residual L4-R blocker was found in the correction cut. The decision agrees with the corrected design requirements; it does not claim the implementation or its evidence already exists.

## Mechanical evidence and stamp boundary

Receipt: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_REBRND_L4R_CORRECTION_COMPARISON_20260911.json`, committed with this review.

- All 11 outcomes are present. All 33 DONE WHEN / ACCEPT / PROOF payloads match the endpoint at the same pin exactly. Including SOURCE and CONSTRAINT fields, 53 of 53 carried fields match.
- The only required triplet changes from v0.1 are FWD-4 and FWD-10, three fields each. Other triplets are unchanged. The receipt lists every field, source/PRD line and whether it changed.
- A comparison-only negative control changes FWD-4.PROOF's ring/selection from `appear` to `disappear`. Exactly that field fails comparison. The repository PRD is never mutated by this control.
- At the receipt cut, committed HEAD and the worktree PRD equal the reviewed v0.2 bytes. The entire ENDPOINT section was inspected, including the space outside its code fence.
- Ratified-text content hash: `1a4cc291f538dd4cccc525672ddce423613d44b6b76924ec47fad2350c19d905`.
- Brief content hash: `5c71da53ce72357ba66283fa6ed7e1b046bc982d82e41024f0e1b6650df04e09`.

The v0.1 canonical refusal attempt wrote an uncommitted seat file because Python's bare `bash` subprocess selected the Windows WSL stub. At this correction pin, `cmd_stamp` resolves an absolute Git-for-Windows executable through the existing `.tools/git_bash_resolver.py`, fails if none is found, and passes that path to the existing safe-commit helper. The changed consumer and resolver were read. The pending canonical invocation, with this committed review reference, is the actual end-to-end test; a resolver self-test or hand-written signoff is insufficient. It will replace the old uncommitted refusal through the canonical tool.

At the pre-stamp CLI read, both halves were STALE and the PRD was WITHHELD. The canonical post-stamp CLI result determines the next gate state. Only CVO's ratified-text half is authorized for this seat; the designated brief signer must supply its own current stamp.

Validation scope: pinned document/source comparison, adversarial acceptance checks, provenance and contract consistency. No production code was changed and no portal render, keyboard exercise, data-plane test, deployment, push or Andrew comparison was performed. Those remain the explicitly named implementation/evidence obligations.
