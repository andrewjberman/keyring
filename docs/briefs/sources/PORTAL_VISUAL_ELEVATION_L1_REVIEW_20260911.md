# Portal Visual Elevation: CRO L1 adoption review

Reviewed by `4.0.0_SA_CRO` at 2026-09-11T07:43:41Z in response to inbox message 95900.

## 1. Disposition

**Treat the submitted brief as L1 input; do not adopt its current wording unchanged.** Andrew's
recorded product direction is accepted. The corrections below concern unsupported conclusions
and implementation choices presented as required outcomes. They do not reopen his rulings or
require him to repeat them. This is a brief review, not a PRD refusal or a new pipeline gate.

Andrew explicitly directed the originating author to write this brief. That instruction is
sufficient authority for the authorship; the author's tier is not a reason to discard or
duplicate the work. Preserve the original attribution when incorporating these corrections.

Accepted direction: new portal visual-elevation work under D13 Design on LAPTOP; light canvas
`#F4F6FA`, deliberate inverted bands using `#0A1733`, mature presentation that preserves useful
chart color, and pinned provenance for external skills. The original record distinguishes
Andrew's instruction about unlicensed sources from the author's subsequent choice to use the
manifest mechanism for all seven repositories. Keep that distinction.

## 2. Reviewed sources and limits

- Brief: `docs/briefs/portal-visual-elevation-brief-20260911.md` at
  `d4b20a28ba67ed96e5ce74327273c54a3df33dbe`.
- Andrew-direct record:
  `org/tier3_junior/0.1.1_RD_MarketPerformance/deliverables/ANDREW_DIRECT_20260911_PORTAL_VISUAL_ELEVATION_FIVE_RULINGS.md`
  at `e46f5061c917d54e75659b16d1c468e326239820`.
- Review requirements: `.claude/skills/brief-create/SKILL.md` and the canonical workflow's L1/L2
  descriptions. Outcomes must be citable capabilities; findings must distinguish measurement
  from inference; L1 does not decompose the work.
- A concurrent, uncommitted amendment was observed in the brief, Git blob
  `2849dc79d57cdad6659874d73426846908dbd3eb`: it adds density and empty-state outcomes, expanding
  nine outcomes to eleven. It is not treated as a committed handoff vintage. This review does
  not edit or commit that author's working copy.

This is a source and outcome review. CRO did not repeat the browser captures, inspect the
installed third-party trees, verify licenses, or run the vendoring gate. The brief's reported
measurements retain their original provenance. ADHC_DESIGN and the workspace design-system
tree are not chased here, consistent with Andrew's recorded direction; the disclosed prior-art
gap remains open.

## 3. Corrections for the next brief vintage

### R1. Make color outcomes describe comprehension and hierarchy

O3 and Part III.4 require one hue for every ordered quantity. That would also prescribe one hue
for over/under-weight or positive/negative scales with a meaningful midpoint. The blanket rule
does not follow from the reported duration-ladder observation.

Suggested O3: **An advisor can distinguish order, direction around a meaningful reference, and
separate categories consistently across charts.** Select the scale according to the quantity;
retain labels or equivalent cues so interpretation does not depend on hue alone. The existing
duration ladder is a concrete candidate for a sequential treatment, not proof of a universal rule.

O4 and Part III.3 literally reserve the accent for one occurrence, while O5 calls for the
website's purple focus ring. Replace the color-count rule with a discernible primary action and
consistent selected, focused, and disabled states. Accent restraint is a design proposal;
keyboard focus must remain visible even when the primary action uses that accent.

For O7, preserve separate semantic tokens for status and data. Do not turn this into a ban on a
data color that intentionally communicates a loss or negative movement. Distinguishable meaning
is the outcome; different token names alone do not prove it.

### R2. Keep renderer consolidation as a candidate implementation

O8 and Part IV.6 equate consistent charts with one rendering library. An import census proves
multiple libraries are present; it does not prove they cannot share a presentation contract.

Suggested O8: **An advisor reads axes, ticks, legends, tooltips, and interaction states
consistently across charts.** Shared tokens, adapters, and eventual consolidation are candidate
mechanisms. Let the implementation assessment establish which migration is necessary. The
same distinction applies to icon and animation dependencies.

### R3. Narrow the substrate claims to the evidence

Part IV.4 establishes that a token file is wired into the application; it does not establish
that the architecture needs only value changes. Keep the wiring finding and describe the
value-swap approach as a hypothesis to validate against the competing declarations.

Part IV.7 locates prior-art paths but concludes that their uninspected contents already provide
the required contract and gate. Keep those paths and the disclosed gap. State compatibility
with the desired contract as unverified. Brand continuity with a marketing site also does not
by itself require copying its exact grid, every radius, or every interaction into an application.

### R4. Separate scan results from licensing and gate conclusions

The absence of a repository-level SPDX result or license file in a reported scan does not
establish the terms of every installed skill. Record the checked path and revision and mark
unverified terms as unknown. Likewise, observing a font served on a website does not verify
the portal's right to redistribute those font files. Retain the existing verification gap.

Part V.6 reports that the selected upstream Python failed the universal lint gate. That
supports a failure for those files under that gate configuration, not the claim that all
third-party Python is impossible to vendor. Preserve the actual failure and the manifest
workaround without asserting a universal prohibition. CRO does not adjudicate the estate's
vendoring policy or bypass its gate.

### R5. Refresh the handoff snapshot without promoting it into an outcome

Part VI still says six repositories and uncommitted artifacts, while the broadcast reports
seven repositories and committed captures/contract. Restate status at a measured UTC time
with repository and commit for each artifact. Commit the intended source vintage before L2
uses it as a pinned reference.

In the observed eleven-outcome amendment, O10's completion sentence incorrectly says O11.
Correct that reference if the amendment is retained. Preserve the distinction between the
observed empty-state rendering and unmeasured density with populated data; do not require
content to fill an otherwise intentionally short page.

## 4. Boundaries carried forward

`portal/DESIGN.md` is a candidate contract, not ratified authority for IRPT_FNTEND's existing
conformity work. Any later shared-token adoption must identify its approved contract and
consumer scope. D13 registration and the placement-field edit remain with their canonical
owners. This review neither changes portal code nor registers or decomposes the project.

The submitted seven-part structure, explicit product boundary, named consumers, and disclosed
measurement gaps are useful and should be retained. Incorporate R1-R5 in a new brief vintage;
the CTO can then cut L2 outcomes from the corrected capabilities without inheriting these
unsupported implementation constraints.

## 5. Push state at review

LOCAL review. Measured `origin/CLOUD` at this read:
`46f7e03df8e7101bc2e463b9f2cbd1a66f54407f`. This is perishable evidence, not a claim that the
review or every source artifact is published. No push is performed by this review.
