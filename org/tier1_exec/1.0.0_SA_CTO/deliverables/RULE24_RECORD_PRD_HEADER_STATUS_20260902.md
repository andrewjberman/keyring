# RULE 24 RECORD -- `PRD_HEADER.status` enum `{DRAFT, RATIFIED, SUPERSEDED}`

**Author:** `1.0.0_SA_CTO` · 2026-09-02 · **Status:** PROPOSAL for `3.0.0_SA_CVO` adoption (CVO~A formal grade
@`7f5bc19`: *"status enum ... owes Rule-24 record plus census before CVO adoption"*). Owed because I authored an
enum in `org/standards/PRD_HEADER.schema.json` @`4a54f6d554` without this record. **The schema is not changed
by this document; adoption is CVO's.**

## The four postulates

**(i) MECE over a DECLARED domain.** Domain = *the standing of ONE step-4 PRD document as a thing step 5 may
decompose from*, at the moment a consumer reads its header. Three members, disjoint by what a consumer may DO:

| value | the consumer may... | uncovered-member hunt |
|---|---|---|
| `DRAFT` | read it; **not** decompose from it; not cite it as ratified | a PRD being written, or written and not yet accepted by the seat that ratifies -- covered |
| `RATIFIED` | decompose from it (step 5 GO); cite it | the normal live state -- covered |
| `SUPERSEDED` | read it for history; **not** decompose; must follow the cited successor | a PRD replaced by a later `prd_version` of itself OR by a different PRD -- covered; the body cites the successor |

Hunted and NOT admitted: **"RETIRED / project closed"** -- a closed project's PRD is still the ratified record
of what was built; closing is a REGISTER state (`dep_stage: CLOSED`), not a document state, and putting it
here would make the header a second carrier of the register's quantity (postulate iii). **"WITHDRAWN"** -- a
PRD pulled without a successor is `SUPERSEDED` with the successor cited as *none* in the body; a fourth value
for the no-successor case would split one intent by an incidental. **"UNDER_REVIEW"** -- that is `DRAFT`; the
review is a process on the document, not a standing of it.

**(ii) SAME GRAIN.** One PRD document (one file, one `prd_version`), at read time. Not a project, not a
directive, not a version *history*.

**(iii) INTENT COHERENCE.** One axis, one intent: **may step 5 decompose from THIS document right now?** It is
NOT: where the project is in the pipeline (`dep_stage`, register), whether the endpoint is ratified by Andrew
(that is the endpoint's own record), or whether the document is on origin (push state). Each of those has
its own carrier and none is duplicated here.

**(iv) STATE COHERENCE.** Which values one remedy does NOT move: **ratifying a PRD** moves `DRAFT -> RATIFIED`
and cannot move `SUPERSEDED` (a superseded document is never re-ratified; its successor is). **Landing a
successor** moves `RATIFIED -> SUPERSEDED` on the OLD document and `DRAFT -> RATIFIED` on the NEW one -- two
documents, two transitions, never one document skipping a state. **Nothing moves `SUPERSEDED` anywhere:** it
is terminal for that document, by construction (postulate i, "must follow the cited successor").

Legal transitions: `DRAFT -> RATIFIED`, `RATIFIED -> SUPERSEDED`, `DRAFT -> SUPERSEDED` (a draft abandoned in
favour of another document). Illegal: anything out of `SUPERSEDED`; `RATIFIED -> DRAFT` (un-ratifying is a
supersession by a new version, not a regression).

## Word-boundary token census (`comp-find '\b<TOKEN>\b' --corpus all`, 2026-09-02 ~18:2xZ)

```
  DRAFT        2,254 hits / 145,0xx files scanned
  RATIFIED     5,340 hits / 145,0xx files scanned
  SUPERSEDED   8,285 hits / 145,024 files scanned   DEF=4 SURFACED=5,158 CONFIG=418 TEST=11 DOC=2,694
```
**All three are already load-bearing vocabulary in this estate** -- `RATIFIED` is the word the loop uses for
an endpoint Andrew has approved, `SUPERSEDED` is the word `DIRECTIVES.yaml` and the deploy ledger use for a
displaced record, `DRAFT` is the word every PRD template uses. The enum coins nothing. **What the census does
NOT establish:** that every existing use carries THIS intent -- `SUPERSEDED` in the deploy ledger means "an
overtaken promote", a different grain. The word is shared; the axis is declared here for this header only.

## What CVO should attack

- Whether `SUPERSEDED`-without-successor is honest as a value, or whether it is `WITHDRAWN` wearing a label.
- Whether the gate should refuse a TO against a `DRAFT` PRD (I think yes; the schema alone cannot -- limb 5
  validates the header's SHAPE and does not read `status`. A `status` limb would be a step-6 refusal Andrew
  has not asked for, so it is **proposed, not built**).
