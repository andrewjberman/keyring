# L4-R BRIEF-HALF RE-REVIEW -- DSGN_REBRND PRD v0.3 @179884e46b (half hash 364fa381f608)

**Reviewer:** `2.0.0_SA_COO~D`, the designated brief-half signer. The designation is on the project row, by Andrew's word
@`2daf4d8b85`.
**Supersedes:** `laneD_L4R_BRIEF_HALF_REVIEW_DSGN_REBRND_v0.2.md`@`7533130e28` (SIGNED against half hash
`5c71da53ce72`).
**Delivered by:** `1.0.0_SA_CTO`, msgs 96631 and 96633.
**Scope:** the brief half's delta only. It moved in exactly two places:
- R5's acceptance clause;
- the v0.3 provenance entry.

The instrument is `git show 179884e46b`: 7 insertions and 6 deletions in one file. The rest of the half is
byte-identical to the v0.2 bytes signed @`7533130e28`. The diff shows no other brief-half hunk, so those verifications
carry forward and are not re-run.

## VERDICT: SIGN

## 1 -- R5's acceptance clause names exactly Andrew's set, no more and no less

The v0.3 R5 row (`DSGN_REBRND_PRD.md:109` @179884e46b) adds: *"and otherwise only on FWD-4's closed identity set
(page-title vertical bar, header subtext, active-tab label and underline, sidebar active item, user avatar), each
enumerated by name"*.

That set was checked against Andrew's option selections in the record
`ANDREW_DIRECT_20260914_150xZ_DSGN_REBRND_RESTORE_SELECTIVE_INDIGO_ACCENTS_AND_AN_INDIGO_FAVICON.md`@`d54876b585`,
member by member, 5 of 5:

| record (RESTORE) | R5 v0.3 |
|---|---|
| the page-title vertical bar | page-title vertical bar |
| the header subtext | header subtext |
| the ACTIVE TAB indicator (label and underline) | active-tab label and underline |
| the SIDEBAR ACTIVE ITEM | sidebar active item |
| the user AVATAR | user avatar |

- **The NOT-restored member is also held.** R5 still reads *"no filled accent chip per option in any tab, toggle or
  segmented control"*. That matches his "do not restore the toggle/segmented-control active fill". A tab now carries
  the accent on its label and underline, not on a chip, so the two clauses do not collide.
- **The set is CLOSED.** "otherwise only on" is an exclusive phrasing, so an accent on any sixth persistent element
  fails R5 as written. That is the grain L9 needs.
- **The consuming cell carries the content.** The reopened `DSGN_REBRND.TO-RB-s-5` (feature branch @3b45dfb5e3) names
  the same five sites with file, line and before/after classes, and grades them mechanically with
  `rb5-accent-check.py`. That checker was exercised on four trees: 0/7 today, 4/7 pre-rebrand, 7/7 on a positive
  control, and 0/7 NOT-FOUND on an empty tree.

## 2 -- The provenance entry quotes him verbatim and attributes the channel

The v0.3 entry quotes *"I'd like to make a concerted effort to keep selective indigo accents, like in the page title
vertical bar and maybe the subtext"*. It is byte-equal to the record's Ask 1, and it is marked "verbatim in part", which
is true. It separates his option selections from his words and cites the record by pin and the relay by msg id. It
states why the spec moved mid-round: his timing ("NOW, THIS ROUND") and the L9 grain. It also says the favicon changes
no outcome's text, which is correct: no FWD names an icon.

## 3 -- The heading denominator is unchanged

`brief_ref` is still `docs/briefs/portal-visual-elevation-brief-20260911.md@bed01b226a`, and the BRIEF COVERAGE table
moved in place: one row edited, none added, none removed. So the heading denominator matched at v0.2 still matches.

## 4 -- One correction, by pinned line, NON-BLOCKING, for the next bump

`DSGN_REBRND_PRD.md:109` @179884e46b, R5's final clause:
- **Reads:** *"...is walked on each of the three routes and the persistent count stays one"*.
- **Should read:** *"...and the persistent ACTION count stays one"*.

This matches FWD-4's v0.3 PROOF, which already says ACTION count.

**Why not a refusal:**
- In its own sentence, "the persistent count" reads back to "exactly ONE PERSISTENT primary action", so in context it
  is not a second rule.
- FWD-4, the governing ratified text, is exact.
- The reopened order's `RB5-AC6` already grades "the persistent ACTION count is still one" and lists the identity sites
  separately. No worker reads the loose form.

A refusal would cost a full re-sign round trip on one word, against a round Andrew timed as NOW. The word goes to
`1.0.0_SA_CTO` with this stamp.

## Instruments

| instrument | read | result |
|---|---|---|
| `git show 179884e46b` | the whole diff | 1 file, +7/-6; brief-half hunks = R5 row + v0.3 provenance entry |
| `prd-signoff.py status DSGN_REBRND` | before the stamp | WITHHELD; brief STALE (5c71da53ce72 -> 364fa381f608), owed by `2.0.0_SA_COO~D` |
| Read | the Andrew-direct record @d54876b585 | the 5-member RESTORE set and 1 NOT-restore member, compared member by member |
| `rb5-accent-check.py` (issuer) | 4 trees | 0/7, 4/7, 7/7, 0/7 NOT-FOUND; the consuming cell grades the same set |
