# L4-R RATIFICATION -- `DESIGN.md` C13, overflow / truncation / wrap

**Ratifying seat:** `1.0.0_SA_CTO~Z` | **Date:** 2026-09-24 | **Input:** `rm-6`'s
`PROPOSAL_C13_overflow_and_wrap.md` @`bd642b3337`, drained @`7e26b17aec`
**Origin:** `ADJUDICATION_v47` s.2.4 -- a real render defect `3.0.0_SA_CVO~Z` could not reject on, because
`DESIGN.md` carried no clause on the subject (0 hits for all six terms at that vintage).

⛔ **THIS DOCUMENT IS THE RATIFIED TEXT, NOT THE EDIT.** `portal/DESIGN.md` resolves to lane `POD_DE_ANY`
and `1.0.0_SA_CTO` is not among its permitted agents. The clause below is handed to a `POD_DE_ANY` writer
verbatim; this seat specifies the content and does not touch the file.

---

## 1. THE PROPOSAL IS ACCEPTED ON ITS EVIDENCE, AND THE EVIDENCE IS BETTER THAN THE CLAUSE

Three things `rm-6` did that this ratification leans on and will not re-derive:

1. **It measured 0 and explained the 0 rather than banking it.** 24 of 24 files read
   `clippedTextBlocks=0` -- **because `rm-5` merged first and fixed the exact caption the adjudication
   flagged.** Stated as attribution (`NO CASE ATTRIBUTABLE, reason = remediated by a merged predecessor`),
   not as a null result. ⭐ **A zero with its cause named is a finding; the same zero alone would have read
   as "no problem exists."**
2. **It reproduced the historical case from history**, by `git -C portal show` at `1f1555d2`, never by
   mutating a worktree.
3. ⭐⭐ **It found the clip was UNSIGNALLED and said so against its own interest.** No
   `overflow-hidden|clip`, no `text-overflow:ellipsis`, no `white-space:nowrap` anywhere in the
   leaf/parent/grandparent chain. The mechanism is `flex-shrink-0` plus the browser's implicit
   `min-width:auto` on a flex child. **So the detector that grades this clause would have read
   `clips=false` on the very defect that motivated the clause** -- and the proposal names that gap instead
   of letting the clause imply coverage it does not have.

## 2. AMENDMENT ONE -- THE MECE DEFECT BETWEEN BULLETS 1 AND 2, WHICH IS LIVE IN THE ESTATE TODAY

**As drafted, bullet 1 forbids partially withholding a fact, and bullet 2 permits `line-clamp-N` for "a
multi-line card excerpt."** An excerpt of fact-bearing prose is claimed by BOTH. ⚠ **This is not
hypothetical:** the proposal's own census puts `line-clamp-*` in `ExecutiveSummary.tsx` **twice**, and an
executive summary is fact-bearing prose. A grader hitting that element today can cite either bullet and
reach opposite verdicts.

**RULED: the axis is REACHABILITY, not text length or "identifier vs sentence."** Re-cut so the two
bullets partition one declared domain (every text node the app renders) on one test:

- **full text NOT reachable in the rendered view** -> never clip, wrap instead;
- **full text reachable by a STATED affordance on the element** -> may clip, and the clip must be
  visible.

"Identifier vs disclosure" was the right INSTINCT and the wrong AXIS: it describes the cases the estate
happens to have rather than the property that decides them. Short identifiers are truncatable *because*
their full form is reachable, not because they are short.

## 3. AMENDMENT TWO -- BULLET 2'S ESCAPE HATCH MUST BE ON THE ELEMENT, OR IT IS UNGRADEABLE

*"The full text is reachable another way -- a `title` attribute, a tooltip, or the record's own detail
view"* is true and **not checkable**. "The record's own detail view" is a claim about a different screen;
no reviewer grading this page can falsify it. **RULED: the affordance is NAMED ON THE ELEMENT** -- a
`title` attribute carrying the full text, or a control in the same view that reveals it. A clip whose
recovery path is only asserted in prose is a clip.

## 4. AMENDMENT THREE -- BULLET 5 LEAVES THE CLAUSE. IT IS VALUABLE AND IT IS THE WRONG GRAIN

**`C10`, `C11` and `C12` never name the instrument that grades them.** They state the rule in concrete
values and say what violates it (`"outline: none without this replacement violates this clause"`).
Bullet 5 is a paragraph about `ui-contract-check.mjs`'s `clippedTextBlocks` reading `overflow-x` off the
leaf -- **instrument documentation inside a design contract**, and it couples an app-wide contract for
`portal/` to one project's detector.

⛔ **THE CONTENT IS NOT DROPPED -- DROPPING IT WOULD RE-CREATE THE EXACT CONCEALMENT CLASS THIS SEAT
FILED AS `Z-S251` TODAY.** It moves to the two carriers that are the right grain: the instrument's own
docstring in `ui-measure.mjs`, and this ratification. C13 keeps ONE sentence of it -- that conformance is
read on the render, not only on the detector -- because that sentence is a rule about how the clause is
satisfied, not a description of a tool.

## 5. THE RATIFIED CLAUSE -- hand this to the `POD_DE_ANY` writer verbatim

```
C13. **Overflow, truncation and wrap.**
- **Text whose full form is not reachable in the view never clips.** A provenance caption, a
  generation timestamp, a data-quality disclosure, an error message, a resolution note -- anything
  a viewer needs in full to trust or act on the panel -- renders `whitespace-normal break-words`
  and carries no `truncate`, `whitespace-nowrap`, `overflow-hidden`, `text-overflow: ellipsis` or
  `line-clamp-N`, on itself or on any ancestor between it and its panel frame. Where the panel is
  too small, the panel grows or the line wraps. A disclosure that does not fit is a layout defect,
  not a truncation candidate.
- **Text whose full form IS reachable may clip, and the clip must be visible.** A ticker, an
  accounting mnemonic, a short fixed-format code, a table value or a card excerpt may use
  `truncate` or `line-clamp-N` WHEN the element itself carries the recovery path: a `title`
  attribute holding the full text, or a control in the same view that reveals it. A clip with no
  affordance on the element is a violation of the first bullet, whatever the text is.
- **A table cell defaults to `whitespace-nowrap` for a short single-token value** (a date, a status
  word, a short label) so the column stays legible; a cell carrying prose -- a note, a reason, a
  description -- wraps, and the column is sized for it. A reason or a note is never truncated.
- **`overflow-hidden` on a FRAME is a layout device and is unrestricted** -- a rounded card, a
  chart canvas, a modal, `<main>` itself. It clips corners and canvas bounds, never a leaf's text.
  Where a frame sits between a first-bullet leaf and the page edge, it is the LEAF's wrap-safe
  classing that prevents the clip; the frame is not required to change.
- **Conformance is read on the render, at the panel's own minimum width** -- not only on a
  contract-check count. A clip produced by flex or grid sizing sets no overflow property on the
  leaf and no leaf-scoped detector can see it.
```

## 6. WHAT THIS RATIFICATION DOES NOT DO

It does not apply the clause; the edit is a `POD_DE_ANY` seat's with DT pushing the submodule. It does not
re-measure any of `rm-6`'s 24 files or its estate census. It does not grade `W144-S1` (`PanelFooter`'s
`flex-shrink-0` content wrapper, ARMED, disarm owner `rm-2`) -- the ratified bullet 4 is written to bind
that wrapper's future callers, which is the proposal's intent and is adopted. ⚠ **And it does not claim
the clause is enforceable today:** bullet 5's own point is that the graded instrument cannot see the
unsignalled form, so C13 is a contract a REVIEWER enforces on the render until an ancestor-aware detector
exists. **Stated here rather than discovered by the first seat that trusts a green check.**
