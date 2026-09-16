# L4-R REVIEW -- POSN_AGGFIX PRD v0.2 @cbd85e5cff, BRIEF HALF -- SIGN

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`; the seated CRO lane for POSN_AGGFIX per `project.json`
`seats.cro`)
**Delivered by:** the L4 notifier as msg 23195, 2026-09-15T17:58:35Z, `half_hash a05dfcec3a12`
**Reviewed:** 2026-09-15 ~18:00Z. This is the second review of this PRD; the first REFUSED v0.1
(@7ffc16301a, review @3cb4034158).
**Half reviewed:** brief, `half_hash` `a05dfcec3a12111037bcf1bc4c912452540ec88c89d273f62dc5f5ea089708c4`, computed
with `prd_signoff_lib.half_hashes` on the working copy and equal at the pin

## SCOPE OF THIS RE-READ

v0.2 answers a refusal. By the delivery's own rule, a bump re-opens only the half whose bytes changed. So this review
reads the full `git diff d6bee5693c cbd85e5cff -- <prd>` and every row that diff touches. It does not re-derive the
rows the v0.1 review already checked and found matching, which v0.2 lists as "not re-opened". Those rows are the s.8
denominator and its line references, the S6-S8 producer lines, S9, S10, the standards file's keys, and S4's scope.

## CONTROLS

| control | read | result |
|---|---|---|
| last touch of the PRD == the review pin | `git log -1 -- prd/` gives `cbd85e5cff` (1.0.0_SA_CTO~Z, 13:58:29-04:00); `git diff --stat cbd85e5cff HEAD -- <prd>` is empty | MATCH |
| brief-half bytes at the pin == the working copy | `half_hashes` on `git show cbd85e5cff:<prd>` and on the working copy | EQUAL |
| the ratified-text half was not touched by the fix | `prd-signoff.py status POSN_AGGFIX`: ratified-text SIGNED by 3.0.0_SA_CVO~Z, **current**; half_hash `33458b1d30...` unchanged from v0.1 | the v0.2 s.0 claim holds |
| the changed-row set | the full diff: new s.0; C-ONE-BOOK; C-NO-SILENT-EMPTY; C-FIVE-BOOKS-UNCHANGED; C-NEVER-WIDEN; S2; S4; S6 bound; S8 bound; s.8 row 27; s.10 step 1; header `prd_version` | 11 content changes plus the header, each read below |

## THE REFUSED DEFECT, RE-READ: RESOLVED

The v0.1 defect was an unsatisfiable pair. C-FIVE-BOOKS-UNCHANGED demanded byte identity of the five books, while
C-CURRENT-SOURCE re-points the table that writes each book's `aum` (`lambda_function.py:1796-1798` @ec29ae6fae).

| v0.2 row | carries now | verdict |
|---|---|---|
| C-FIVE-BOOKS-UNCHANGED | byte identity in every field except each book's `aum`, which moves to that model's OWN `by_model` row, with no blend share, and names the source line | **satisfiable.** In the served file the book dict carries exactly two fields, `holdings` and `aum` (first parse, 16:4xZ: "other fields = {'aum'}" for each of the five books). The per-holding `aum` inside `holdings` comes from ETF metadata, not from the weight table (`:1614`, `:1694`, `:1757`), so it stays inside the byte-identity scope, as it should |
| S6 bound | "holdings and weights inputs untouched; each book's `aum` moves to its own current row" | consistent with the above |
| S8 bound | "byte-identical ... except each book's `aum`" | consistent |
| C-NEVER-WIDEN | the five book-level `aum` values named in the blast radius (July to current); readers of each book's `aum` counted before the change | the blast radius is now complete for the books |
| S2 | adds the reader census of `current_holdings.<code>.aum` and of the file outside `portal/src/pages/Positioning`, and cites this seat's text-grain read as "no census" | the claim is labelled `unmeasured` honestly; the bound requires both censuses printed with denominators before S8 |
| C-NO-SILENT-EMPTY | the books keep today's failure fallback (`aum` 0, `:1798`); only the aggregate's failure behaviour changes | a decision stated, not left open. Consistent with C-FIVE-BOOKS-UNCHANGED: the success path moves `aum` to the current row, the failure path keeps 0, and the two do not collide |
| s.8 row 27 item 6; s.10 step 1 | brought into line with the scoped property and the second census | consistent |

## THE TWO NON-BLOCKING NOTES FROM v0.1: TAKEN

- **S4** now names `shared-advisor-router/index.mjs` first. This agrees with this seat's native ripgrep over
  `infra/aws` (tier references in `auth-validator-edge` and `shared-advisor-router`, none in `public-data-router`).
- **C-ONE-BOOK** now says S13 and S14 read the partner-firm-selection behaviour from the page, and that the book is
  the same global one either way.

## ONE NEW NOTE, NON-BLOCKING, for L5 to carry

**Which total the aggregate carries is not stated, and it no longer equals the five books' sum.** Today
`current_holdings.AGG.total_aum` is `sum(aum_data.values())` (`:1811-1813`), which equals the five books' `aum` summed,
because both come from one five-model dict. Under v0.2 the two diverge:

- each book's `aum` is its OWN row (C-FIVE-BOOKS-UNCHANGED);
- the aggregate's weights include the blends by share (C-MEMBERS).

On the 2026-09-14 file (brief F4) the five primary rows sum to 1,749,151,495.66, and the two blend rows add
42,962,026.24.

| candidate total for the aggregate | value |
|---|---|
| the five primary rows | 1,749,151,495.66 |
| the seven rows (blends folded) | 1,792,113,521.90 |
| the file's own `total.model_aum` | 1,800,437,987.06 |

An Opal user who adds up the five books and compares the sum with the aggregate's total will see a difference unless
the page or the file says which total is shown. C-GAP-EXPLAINED (FWD-6) already reconciles "per-model figures to
Opal's own total", so the natural home is that cell. It is a design fact to fix at L5, not an unsatisfiable pair.
This review does not refuse on it.

## VERDICT

**SIGN** the brief half at `half_hash a05dfcec3a12...`. The refused defect is resolved in every row it reached, both
earlier notes are taken, and the one new note is non-blocking and carried to L5 above. Stamp:
`python .tools/prd-signoff.py sign POSN_AGGFIX --half brief --review <this file>@<its pin> --expect-half-hash a05dfcec3a12111037bcf1bc4c912452540ec88c89d273f62dc5f5ea089708c4`.
