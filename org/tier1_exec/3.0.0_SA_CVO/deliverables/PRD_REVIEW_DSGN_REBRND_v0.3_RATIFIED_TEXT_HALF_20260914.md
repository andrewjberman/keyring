# PRD REVIEW -- DSGN_REBRND v0.3 @179884e46b -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96630 (16:48:44Z), and `1.0.0_SA_CTO` msg 96632.

**Prior:** v0.2 SIGNED @8ad762f7bf (review `DSGN_REBRND_L4R_CORRECTION_REVIEW_20260911.md@b96f670a76`).

**Read, UTC 2026-09-14, after 16:48Z:**
- The PRD @`179884e46b`. HEAD and the working copy are byte-identical to the pin (0 diff lines each; the positive
  control, v0.2 against HEAD, reads 52).
- The full diff v0.2 -> v0.3 (the one commit on the path since v0.2).
- A census of every accent / persistent / chip / second-action carrier in the v0.3 file, mapped to its section.
- Andrew's record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_150xZ_DSGN_REBRND_RESTORE_SELECTIVE_INDIGO_ACCENTS_AND_AN_INDIGO_FAVICON.md` @`d54876b585`.
- The brief's O4 @`bed01b226a` (`docs/briefs/portal-visual-elevation-brief-20260911.md:60-64`).
- The measured website file `design/brand/opalinvest.com.json` (`:14`, `:79-83`), the source the CONTRACTS preamble
  cites for every MEASURED value.
- The counterpart PRD `org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md` (211 lines).

**Half hash:** the notifier's `8cd0066e445e`. Not recomputed by this seat; the stamp binds the current bytes.

## VERDICT: REFUSE on R1 -- one carrier in this half still classes the accent by its pre-v0.3 roles

## THE DIFF OF THIS HALF, v0.2 -> v0.3

- **ENDPOINT:** FWD-4's DONE WHEN, ACCEPT and PROOF rewritten. FWD-4's SOURCE and every other outcome
  (FWD-1..3, FWD-5..11) are byte-unchanged.
- **CONTRACTS:** the `DesignContract` row's accent clause gains the identity set. Nothing else moved.

## WHAT IS RIGHT -- the amendment is verbatim to his selections

| Andrew's selection (record, "option selections") | v0.3 DONE WHEN / ACCEPT | CONTRACTS row |
|---|---|---|
| RESTORE the page-title vertical bar | "the page-title vertical bar" | yes |
| RESTORE the header subtext | "the header subtext" | yes |
| RESTORE the ACTIVE TAB indicator (label and underline) | "the active tab's label and underline"; ACCEPT: "a tab marks its active state by the accent on its label and underline, never by a filled chip" | yes |
| RESTORE the SIDEBAR ACTIVE ITEM and the user AVATAR | "the sidebar's active item, and the user avatar" | yes |
| DO NOT RESTORE the toggle/segmented-control active fill | ACCEPT: "segmented controls and toggles mark their active state by weight and rule, never by a filled accent chip per option" | (not named; consistent) |

- Five of five RESTORE members present in both carriers; the one DO-NOT-RESTORE held.
- The PROOF discriminates: it enumerates every PERSISTENT carrier and names each as the one action or a member of the
  set, so a sixth persistent carrier FAILS it.
- No history, annotation or seat name entered ENDPOINT; the provenance sits in PROVENANCE v0.3, outside the half.
- **Counterpart agreement:** `IRPT_FNTEND`'s PRD carries no accent, `DesignContract` or `#5F3BE3` clause (0 hits;
  control: 14 hits for its own code in the same file). Its one design tie (`:79`, "built from the portal's own
  header, tabs ...") consumes whatever this contract defines and does not contradict the widening.

## R1 -- the CONTRACTS preamble classes the accent by TWO roles; v0.3 adds a THIRD with no class

**The carrier.** CONTRACTS, the preamble (`:122` @179884e46b): *"Every value the contract names belongs to exactly
ONE of four classes, and the contract labels each: ... **MEASURED website values** (canvas `#F4F6FA`, **the accent's
two roles**, ... -- from `design/brand/opalinvest.com.json`, [3/3] rows only)"*. It closes: *"it is ratified by the
L4-R stamps on this section."*

**What the cited source measures.** `design/brand/opalinvest.com.json:14`: `"accent": { ... "role": "single action
accent + focus ring" }`, surface share 1.0 / 0.7 / 0.9 %. And `:81`, its recorded decision: *"spend #5F3BE3 there
and nowhere else"*. The two roles the preamble classes as MEASURED are exactly those two, and the website measures
no third.

**What v0.3 added.** A third persistent role, the closed IDENTITY set. By Andrew's own record, this is a departure from
the one-accent rule, ruled by him; it was not measured from the website.

**The defect.** The section asserts that every value has exactly one class and that its stamps ratify that labelling.
After v0.3:
- the identity role belongs to none of the four classes as written;
- a builder following `:122` labels all accent roles MEASURED, which cites a source whose own decision reads "nowhere
  else".

The `DesignContract` row requires *"YAML front matter naming every token value WITH ITS CLASS"*, so the label flows
into `portal/DESIGN.md`. That is a value carrying the wrong claim, in the one section a stamp ratifies.

**How it happened.** The amendment moved FWD-4 and the `DesignContract` accent clause, and left the one carrier in the
same half that classes those values. The CTO's note (96632: "nothing else in either section moved") is accurate, and
that is exactly the defect.

**The fix, which is the CTO's to choose.** One phrase at `:122`:
- keep "the accent's primary-action and transient roles" under MEASURED; and
- class the identity set explicitly. The recommended home is **DERIVED** ("design choices the website does not
  supply"), with its rule written beside it: *the closed list Andrew selected 2026-09-14 (PROVENANCE v0.3)*. That
  keeps the four-class schema intact.

A fifth class is also legal, but it changes the schema; the four-class record would then need its own
MECE statement.

**Sign condition:** `:122` no longer classes as MEASURED any accent role beyond the two the website measures, and the
identity role carries exactly one class with its rule beside it. Nothing else in this half needs to move for SIGN.

## NOTES (non-blocking)

- **N1 -- FWD-4's SOURCE now cites only a text the outcome departs from.** SOURCE reads *"brief O4; III.3; IV.2
  (accent never above 1.0 % on the website)"*. O4 (`brief:62-64`) says the accent goes on *"the one primary action
  and nothing else"*, with tabs marked *"by weight and rule"*. The DONE WHEN, ACCEPT and PROOF are explicit and are
  what L9 grades, so this does not block. A grader who follows SOURCE, however, finds the opposite of the identity set
  and of the tab rule. If convenient, in the same edit, add a seat-free source token, e.g. *"Andrew-direct 2026-09-14
  ~15:0xZ (the identity set; PROVENANCE v0.3)"*. That is a source, not history, and it names no seat.
- **N2 -- CLOSED is read from the selections, and that reading is correct; the one open edge is stated.** His Ask 1
  sentence also says *"There are other locations as well where this is valuable."* The follow-up question's
  selections answer it, and the selection is the ruling, so the set is closed at five. The record lists the
  selections but not the full option list, so whether he was offered other locations is not on record. A sixth
  location therefore needs his next word, not an inference. It would be an addendum that re-opens this half only.
- **N3 -- carried from v0.2, stakes raised.** Two gaps remain unbounded:
  - The FORM of each identity member (a fill, a rule, or text colour). His words do not specify it, and adding a bound
    would be narrower than his word.
  - FWD-4 prints the accent share per route and sets no bar. The 1.0 % in SOURCE describes the website, not a
    portal target.

  Five more persistent carriers make both gaps more consequential. The PROOF names every carrier and prints the share,
  so L9 will see both.

## NOT CLAIMED

- **The brief half.** It is `2.0.0_SA_COO~D`'s, by Andrew's word on the project row, and is also STALE at v0.3.
- **That `portal/DESIGN.md` carries the mislabel today.** It lives on `feature/d13-visual-elevation`, and I did not
  read it. R1 is a defect of the ratified text, which the built contract is required to follow.
- **The favicon (Ask 2).** It changes no outcome's text, and I agree it needs no amendment here.
- **Anything about the RB-s-5 reopen.** It is a modification, `.tools/to-pipeline-gate.py` LIMB 6 does not fire on
  it, and this refusal does not stop it.
