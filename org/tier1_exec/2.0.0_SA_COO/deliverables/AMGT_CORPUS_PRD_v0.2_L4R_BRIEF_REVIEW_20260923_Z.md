# AMGT_CORPUS PRD v0.2 -- L4-R BRIEF-HALF REVIEW -- **REFUSED**, one bounded ground

**Reviewer:** `2.0.0_SA_COO~Z`, in the CRO's stead per the spine's own provision (the brief half is
`4.0.0_SA_CRO~Z`'s *"or a live `2.0.0_SA_COO` not holding the round in its stead"*, PRD `:350`).
**Eligibility, stated:** this seat does **NOT** hold `AMGT_CORPUS` -- the project is UNSEATED (`:26-27`) -- so it
holds no round here and is unconflicted. It holds `AMGT_RESAPP`, the sibling that CONSUMES this project's
artifacts, which is disclosed below as the one place a reader should weigh this review carefully.

**Half reviewed:** everything except `ENDPOINT` (`:87-233`) and `CONTRACTS` (`:234-300`) -- i.e. `:1-86` and
`:301-358`. **Version:** v0.2 @`8a88326c3e`. **Brief:** `docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md`
@`6c52138c2f`, **pin verified rc=0 on this seat's own instrument**.

⚠ **ROUTING NOTE:** the L4 notifier has been advertising **v0.1**, most recently at 01:14Z. **This review is against
v0.2** on `1.0.0_SA_CTO~Z`'s instruction (msg 24491). The notifier's version is stale, not the PRD.

---

## VERDICT: **REFUSE**, on ONE ground. Two of the three candidates the CTO flagged are CLEARED.

⭐ **A refusal here disturbs nothing** -- there is no seat, no decomposition and no order behind this PRD
(`1.0.0_SA_CTO~Z`, msg 24491) -- and the ground is a two-line fix.

## CLEARED -- candidate 1: **O4 -> FWD-6 / FWD-7 is FAITHFUL, not a reading**

The CTO flagged that O4 became two outcomes. **The brief's own met-condition contains both halves, joined by
"and"** (brief `:79-83`):

> *"O4 is met when a bank's page carries NII and fee mix, NIM, cost/income, cost of risk, CET1 and RoTE beside the
> generic lines ... as an operating-KPI block the one-pager never had and the reports always did -- **and the Model
> tab keeps the generic typecast (F14) for everyone.**"*

**Two deliverables, both named in the outcome's own close: the sector-fit KPI block, AND the generic typecast
retained for everyone.** Splitting them into `FWD-6` and `FWD-7` makes each separately provable and drops neither;
under L10 both must grade REALIZED, so nothing can close on half of O4. **No defect.**

## CLEARED -- candidate 2: **O13 -> FWD-3 / FWD-4 is FAITHFUL**

Brief `:124-129`:

> *"O13 is met when each name folder of that library (93 at the scan, F13) **resolves to a security on the page** --
> **inducted into the harvest where it is not yet in the universe**, its prior reports ingested (O5), its report
> written (O1) -- and the page **can say which folders are not yet resolved and why.**"*

**Resolution, INDUCTION and printing-the-unresolved are all named in one sentence**, and the brief itself
cross-references O5 and O1 for the two parts that are not this project's. `FWD-3` (census + resolution + printed
unresolved) and `FWD-4` (induction) split exactly along the brief's own commas. **No defect.**

## ⛔ THE GROUND FOR REFUSAL -- candidate 3: **R12 CONTRADICTS THE PRD'S OWN RULE 24 RECORD**

**The manifest (`:319`, THIS half):**

> `| R12 | the lifted equity-research skill artifact, the message design and the cost card | repo documents under
> **this project's home** | (method; feeds the addendum) |`

**The Rule 24 record (`:210`, the ratified-text half, already SIGNED):**

> `| O1, O3, O6, O7, O10, O11, **O12** | **WHOLLY THE ADDENDUM'S** (each writes or serves the report) | **--** |`

**The brief (`:118-120`), which assigns the artifact to O12 by name:**

> *"**The method -- the lifted equity-research skill adapted**, the sector templates of O4, the continuation contract
> of O2 -- lives as a versioned prompt-and-schema artifact whose version is stamped into every report."*

⛔ **So the lifted equity-research skill artifact is O12's content by the brief's own sentence; the PRD's own record
says O12 is WHOLLY THE ADDENDUM'S with `--` landing here; and this half nonetheless builds it here as R12.** The
two halves of one PRD state the boundary two different ways.

⭐ **AND THIS IS THE FAILURE MODE THE PRD NAMES ABOUT ITSELF, ONE SECTION EARLIER** (`:226-228`), in its v0.1 O9
post-mortem:

> *"a reader of either carrier could conclude the OTHER owns O9's corpus-side half, and **no gate anywhere would
> fail -- an outcome falls between two projects precisely when each document believes the other has it.**"*

**R12 is that defect's MIRROR: not a gap but a DUPLICATION -- both carriers claim O12's artifact.** Same class, same
invisibility to every gate, and the PRD demonstrated one section earlier that it knows the shape.

**SECOND, INDEPENDENT SIGNAL, in this half and cheap to check: `R12` is the ONLY manifest row whose `serves`
column names no FWD.** R1-R11 each serve at least one; R12 serves `(method; feeds the addendum)`. The manifest's
own preamble (`:303`) says *"Each row is a surface a cell will build"* -- so R12 authorises a CELL WITH NO OUTCOME
BEHIND IT, against the canonical workflow's *"No cell is cut for coverage alone."* ⚠ **A row that serves nothing
is not merely untidy: it is work no endpoint outcome can grade, in a project whose L10 closes only when every FWD
grades REALIZED.**

### WHAT WOULD CLEAR IT -- either, and the choice is the CTO's

1. **MOVE R12 to the addendum** (the reading this seat finds better supported: O12 is the addendum's by `:210`, and
   the artifact's version is *"stamped into every report"*, which this project explicitly does not write, `:80-81`);
   **or**
2. **KEEP R12 here and MINT AN FWD for it**, amending `:210` so O12 is SPLIT rather than wholly the addendum's --
   which is the same remedy `:211-215` already applies to O2, O4, O5, O8 and O9, and would restate the close from
   `7 + 5 + 1 + 1 = 9`.

⛔ **What must NOT happen is the current state: the row stays, serves no FWD, and the record says the outcome is
somewhere else.**

---

## WHAT THIS HALF GETS RIGHT, recorded because a refusal is not a verdict on the whole

- **The brief is NOT copied into this tree** (`:33`) -- *"one brief, two consumers; a copy would age separately from
  its original."* ⭐ That is the citation-staleness discipline applied before it cost anything.
- **The v0.2 pin correction (`:43-52`) is better than the refusal that prompted it.** The CVO recommended the ADD
  commit; the CTO measured that the brief has TWO commits and that the +113 bytes are *"exactly the origin line that
  names Andrew's eighth message ... which is the authority FWD-3 and FWD-4 rest on"*, with a positive and a negative
  control. **Pinning to the recommended commit would have pinned this endpoint to a brief lacking the word two of its
  outcomes are built from.**
- **The Rule 28 cards (`:327-331`) ask the right questions**, K3 especially: 184 PDFs against 71 Word files, *"since
  the scan's term census read the Word files only"* -- a denominator caveat stated before any cell relies on it.
- **`OPEN CALLS` (`:337-342`) closes three calls with Andrew's own words and carries exactly one to L5**, to be
  decided by K2's measured number rather than by preference.

## DISCLOSURE

This seat drives `AMGT_RESAPP`, which **consumes** this project's artifacts and whose addendum is the other side of
the R12 boundary. ⚠ **A reader should note that the refusal's preferred remedy (1) moves work TOWARD the project
this seat drives.** That is why remedy (2) is stated as equally sufficient and the choice is left to
`1.0.0_SA_CTO~Z`: **the defect is the CONTRADICTION, not which side wins it.**

-- `2.0.0_SA_COO~Z`, 2026-09-23.
