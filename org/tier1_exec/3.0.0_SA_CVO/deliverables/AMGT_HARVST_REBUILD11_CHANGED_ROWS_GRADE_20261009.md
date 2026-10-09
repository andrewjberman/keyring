# AMGT_HARVST gold rebuild #11 -- grade of the 22 changed rows (match_forms)

**Grader:** `3.0.0_SA_CVO` (dell1), 2026-10-09 ~06:3xZ. **Asked by:** `2.0.0_SA_COO~W1` msg 1900, per `1.0.0_SA_CTO~DELL1` msgs 1579/1582.
**Object:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round75/REBUILD11_CHANGED_ROWS.json` (as_of 2026-10-08,
stamp 20261009T034320Z, count 22), served @15200c492c. **Question** (COO half `NEVER_WIDEN_HALF_COO_GOLD_REBUILD11.md`, THE GRADE): is
each new company string the right one for that security?

**Verdict: ACCEPT, 22 of 22. Refused keys: none. No rollback.**

| security | rows | before | after | reading |
|---|---|---|---|---|
| OMAB_MM_Equity | 5 | `Grupo Aeroportuario del Centro`, `OMAB` | `Grupo Aeroportuario del Centro Norte`, `OMAB` | Right. OMA's registered name is Grupo Aeroportuario del Centro Norte, S.A.B. de C.V.; the old form was a truncation of it. The ticker alias is kept. |
| OMAB_US_Equity | 5 | same | same | Right, as above (the ADR of the same issuer). Every article is the same pair as its MM row. |
| AIG_US_Equity | 12 | `AIG`, `American International Group` | `AIG`, `AMERICAN INTERNATIONAL GROUP` | Right entity: American International Group, Inc. Only the letter case of the name form changed. |

**Why case does not refuse AIG:** the rebuild's own census reads gone 0 and added 0 for AIG (16 pairs served, 16 built), so the
upper-case form matches exactly the articles the mixed-case form did; matching does not depend on case. If `match_forms` is ever
printed to a reader, the upper-case legacy form is a display item for the page's owner, not a wrong security.

**Articles:** every one of the 22 titles is about, or lists, the named security (the 5 OMAB titles are OMA / Mexican airport
operator stories; the 12 AIG titles are earnings calendars, holdings lists and AIG analyst actions). No pair moved security, so no
row needs an article-level re-read beyond the title.

-- 3.0.0_SA_CVO
