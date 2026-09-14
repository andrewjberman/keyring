# PRD REVIEW -- DSGN_REBRND v0.5 @01378b0a5b -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96653 (17:34:36Z), and `1.0.0_SA_CTO` msg 96655.

**Prior:**
- v0.3 was REFUSED on R1: review @d779f0b32f, stamp @a878d78f90.
- v0.4 was REFUSED on R2: review @2f6af3147b, stamp @856bc58831.

**Read, UTC 2026-09-14, after 17:34Z:**
- The PRD at HEAD, where the last commit on the path is `01378b0a5b`. The working copy is identical to HEAD.
- The two commits since v0.4:
  - `40d6e992c9` changes CONTRACTS `:122`, PROVENANCE and the header.
  - `01378b0a5b` changes PROVENANCE only, one line, so it is in the brief half.
- `design/brand/opalinvest.com.json`: last changed @d4b20a28ba (2026-09-11) and clean in the working copy, so the
  whole-file read behind the v0.4 review (111 lines) is still the current file.

**Half hash:** the notifier's `deb2e35abfc5`. `01378b0a5b` does not touch this half. The stamp is bound with
`--expect-half-hash`.

## VERDICT: SIGN -- R2 closed; every MEASURED member has a line in the file it cites

## THE DIFF OF THIS HALF, v0.4 -> v0.5

- **ENDPOINT:** byte-unchanged. FWD-4 keeps v0.4's SOURCE, which cites his word.
- **CONTRACTS `:122`:**
  - MEASURED: *"the accent's primary-action and transient roles"* becomes *"the accent's primary-action role and the
    focus ring"*.
  - DERIVED gains *"the text-selection highlight on the accent"*.
  - The rule list gains *"the text-selection highlight takes the accent so that transient feedback shares one colour,
    FWD-4 and brief A23"*.
  - Nothing else moved.

## R2 -- CLOSED: the MEASURED class, re-counted against the file

| MEASURED member at `:122` (v0.5) | `opalinvest.com.json` |
|---|---|
| canvas `#F4F6FA` | `:12` |
| the accent's primary-action role | `:14` "single action accent", `:79-81` |
| the focus ring | `:14` "+ focus ring", `:56-57` |
| radii 2/3/4px | `:50` |
| no drop shadow | `:54-55` |
| the 2px focus ring | `:56` |
| weights 400/700 | `:31` |
| `letter-spacing: normal` | `:33` |
| the 40/60 split | `:63` |

**9 of 9.** These are the v0.4 census's ten rows less the selection highlight, which is now DERIVED. The CTO's
"9 of 9" (96655; PROVENANCE after `01378b0a5b`) matches this count.

- **The selection highlight** carries exactly one class, DERIVED, and its rule is beside it.
- **The identity role** is unchanged from v0.4: DERIVED, with the closed-list rule.
- **The sign condition from the v0.4 review is met on both clauses.**
- **Corroboration by a different instrument:** the CTO searched for "selection" over
  `design/brand/opalinvest.com.{json,md}` and got 0 lines, with a control of 10 for "focus". My method was a
  whole-file read. The two methods differ and agree, so this is corroboration, not a repeat.

## CARRIED, AND UNCHANGED BY THIS VERSION

The amendment is verbatim to his selections: 5 of 5 RESTORE members and the toggle fill held out. The PROOF
discriminates, since a sixth persistent carrier fails it. `IRPT_FNTEND`'s PRD carries no conflicting clause. All three
stand as read in the v0.3 review, and v0.4 and v0.5 did not touch FWD-4's DONE WHEN, ACCEPT or PROOF.

## NOTES (non-blocking)

- **N3 carries.** The identity members' FORM and an accent-share bar remain unbounded. The PROOF names every carrier and
  prints the share per route, so L9 sees both.

## NOT CLAIMED

- **The brief half.** It is `2.0.0_SA_COO~D`'s and reads STALE at v0.5. `01378b0a5b` is in that half.
- **That `portal/DESIGN.md` carries these class labels.** It is on `feature/d13-visual-elevation`, and I have not read
  it. This stamp ratifies the text that the contract is required to follow.
