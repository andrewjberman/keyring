# MACRO ENUM for D7 -- the Rule 24 four-postulate record + word-boundary token census

**archetype:** SCRIBE (record)
**Author:** `2.0.0_SA_COO~V2` (dell2), 2026-10-07 ~16:3xZ. Seated by `0.0.0_AB_MSTR~DELL2` (msg 858) on
`1.0.0_SA_CTO~DELL2` msg 856. **Carrier (DATA):** `org/missions/MACROS.yaml` `directives.D7`, read by
`.tools/missions-tree-index.py` refusal R2. **Form follows** the D12 and D9 records so they compare.
**Status:** PROPOSED. The ratification belongs to Andrew alone. This record flips nothing and edits no carrier.
At L3, `1.0.0_SA_CTO` writes the MACROS.yaml line (rule 27).
**Authority for the card:** Andrew-direct 2026-09-03 ~08:4xZ, "Recs approved", answering "Name D7's macro ... or
leave both to CTO~Z to propose" -> **CTO PROPOSES; one card with both names; ratification is his word on that card**
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260903_084xZ_mstrZ_RECS_APPROVED_STRIKE_COO_ROW_0828_CLAUSE_D7_NAMES_CTO_PROPOSES.md`).

---

## 1. The proposal -- ONE card, two names, and the alternative he must see

| | macro (D7 enum) | project code (renames `OPAL_TICKET_VNEXT`) | grammar (contract `levels[1..2]` at HEAD) |
|---|---|---|---|
| **REC (CTO msg 856, this seat concurs)** | `TCKT` | `TCKT_VNEXT` | `^[A-Z]{4}$` yes; tail `VNEXT` 5 chars, `^[A-Z]{4}_[A-Z0-9]{3,18}$` yes |
| **ALTERNATIVE (honours his 07-14 name)** | `OPAL` | `OPAL_TICKETVNEXT` | yes; tail `TICKETVNEXT` 11 chars, yes |

**THE FACT THE CARD MUST CARRY.** `TCKT` is not new. On 2026-07-14 ~21:0xZ Andrew said, verbatim: *"let's make sure
ticket project is registered as OPAL_TICKET in the registry."* `0.5.0_AE_OpalETL~A` carried that out as
`TCKT_CENTER -> OPAL_TICKET`, `macro TCKT -> OPAL`, and retired the one-day `TCKT` macro row the same day
(`org/projects/OPAL_TICKET.json` history; `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/ANDREW_DIRECT_20260714_taxsma_ticket_system_scoping.md`
ADDENDUM 4). His words name the PROJECT CODE. The macro swap was the seat's consequence and he never ruled on it.
Even so, the REC brings back a token that left the register on his word. He sees that on the card, and nobody
infers his view for him.

---

## 2. The declared domain

**Domain:** the macro under which a NEW project may enter the TREE for D7. Prospective only (spec s.8). The 392
flat rows stay out of scope.

**Members today:** `DIRECTIVES.yaml` D7 `members.projects` = `[OPAL_TICKET_VNEXT]`, and that is the entrant. No other
row carries `directive: D7` (1 of 392 parsed, 0 parse errors). Its row carries `macro_code: OPAL_TICKET`. That value
has 11 characters, so it is not a macro at all.

**Two bars, independent (the D9 shape):** (a) D7 has no MACROS.yaml entry, so R2 refuses any D7 registration.
(b) `OPAL_TICKET_VNEXT` has a second underscore, so R1 refuses it under ANY macro. Clearing (a) leaves (b) in place.
**Both options above rename the code.** No option enters the tree under the current name.

---

## 3. The four postulates

**(i) MECE over the declared domain.** Found by subtraction from 1 entrant: either option covers 1 of 1.
**Uncovered-member hunt:** the brief and PRD name WS-3..WS-6 of `docs/architecture/D7_TICKET_VNEXT_PRD.md` as out
of this project (endpoint "What L4 must settle"). FWD-7's second request type is still a ticket type. All the named
D7 scope is Ticket Center. **No uncovered member is in the domain today.** If a D7 project that is not the
Ticket Center wants a tree home, it brings its own record and Andrew's word.

**(ii) Same grain.** `TCKT` names one product line. It matches `ETFS`/`MDPF`/`IRPT`/`DSGN`. `OPAL` is the firm
name. In the flat register, 29 rows carry it across D2/D6/D9/none (taxonomy, runners, tax SMA, alerts, analyst,
tickets). **`OPAL` is a namespace for "Opal's platform", a coarser grain than every ratified macro.** This is
the main reason for the REC.

**(iii) Intent coherence.** The axis is which product or system line the project belongs to. `TCKT` answers that
axis. `OPAL` answers "whose" (always Opal), so it carries no information on this axis.

**(iv) State coherence -- the values this flip does NOT move.** Ratifying D7 changes D7 ONLY. It does not touch
`OPAL` in any other directive (OPAL is in none; D9 refused `[IRPT, OPAL]`). It does not rename the 2 closed rows
`OPAL_TICKET` and `OPAL_TICKET_IA`. It does not rename any infrastructure (`ticket-center` TF module/tag,
`opal-ticket-api`, `opal-tickets`). That matches the 07-14 rename, which changed the project code only. It writes
no register row, mints no folder and grants no seat. Those are L3 (`1.0.0_SA_CTO`).

---

## 4. Word-boundary token census (my reads, 2026-10-07 ~16:3xZ, dell2 @bd545eb4bf + working tree)

| pattern | instrument | result | referent |
|---|---|---|---|
| `\bTCKT\b` | `comp-find --all` [corpus=all] | **28 hits / 61,720 files**; SURFACED 1, CONFIG 2, DOC 25 | All 28 refer to the Ticket Center: the 07-14 registration and rename, the 07-14/15 P0 logs, today's 856/858 traffic, and 1 HUD line from this session. **Zero hits for another referent, so no collision.** |
| `\bOPAL_TICKETVNEXT\b\|\bTCKT_VNEXT\b\|\bTICKETVNEXT\b` | same | **5 hits / 61,722 files**, DOC 5 | All 5 are this decision's traffic (856, 858, the 09-03 record, `PRD_DRAFT_TCKT_VNEXT_20261007.md`). Neither code is taken. |
| flat rows `macro_code == OPAL` | python over `org/projects/*.json` | **29 of 392** (D9 4, D2 1, D6 1, none 23) | firm-platform namespace (s.3 ii) |

**NOT COVERED by those zeros:** 524 ephemeral-floor files, 3,683 binary files and 1 unreadable file
(comp-find's own disclosure). **CTO's "60 hits"** (msg 856) is a different vintage or scope. I did not re-derive it,
and this record carries only my own measurement.

---

## 5. What makes it bind

R2 in `.tools/missions-tree-index.py`. Until `directives.D7` exists with a RATIFIED line, the tree accepts nothing
under D7. R1 also refuses `OPAL_TICKET_VNEXT` under any macro, so the rename travels with the ratification. The
PRD draft already uses `TCKT_VNEXT` as `proposed_code`.

## 6. Alternatives named and rejected

- **`OPAL` / `OPAL_TICKETVNEXT`.** Not rejected. It is on the card (s.1) because it keeps his 07-14 name almost
  letter for letter. REC against it on grain (s.3 ii-iii): it makes the firm name a product-line macro, the shape
  D9 already refused.
- **`[TCKT, OPAL]`.** REJECTED: one entrant. A second macro with no member is the wish-list shape that D8, D9 and
  D13 all refused.
- **Keep `OPAL_TICKET_VNEXT` and widen the grammar.** REJECTED: it is not a D7 decision. The contract grammar is
  estate-wide, and changing it needs its own word.

## 7. The card (for `0.0.0_AB_MSTR~DELL2`, per msg 858)

> **D7 (Ticket Center): ratify macro `TCKT` and rename the project `OPAL_TICKET_VNEXT -> TCKT_VNEXT`?**
> REC yes. TCKT names the product line. You retired TCKT on 07-14 when you asked for "OPAL_TICKET". If you
> want to keep that name, the legal form is macro `OPAL`, code `OPAL_TICKETVNEXT`. Answers: `yes` / `OPAL` / other.

Ratification mechanics: on his word, `1.0.0_SA_CTO` writes `directives.D7` with `macros: [<his choice>]` and a
`RATIFIED <this record> <date>` line that quotes him verbatim. Any wider list needs a new record and a new word.

`2.0.0_SA_COO~V2`
