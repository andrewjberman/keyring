# SITE-Z DIRECTIVE ASSESSMENT + PROPOSED REGISTRATIONS (Rule 27 stages 1-2)

**Author:** 1.0.0_SA_CTO~Z, 2026-08-21 ~19:0xZ
**Commissioned:** Andrew-direct via `0.0.0_AB_MSTR~Z` relay -- *"1.) Assess what directives are on
their fabric, e.g. Tickets, etc., then 2.) Register projects based on the current needs as
associated with those directives. 3.) Run the [canonical process] as intended"* -- and, at my
terminal ~1755Z, *"get this shit driving, you should have everything you need now."*

---

## THE HEADLINE, AND IT IS A DEFECT NOT A STATUS

> **ALL THREE SITE-Z DIRECTIVES HAVE BROKEN OR ABSENT REGISTER MEMBERSHIP.** `/directives-check`
> reports **`TOs: 0 open`** for D6, D7 and D9 -- **a true zero over an empty or dangling member
> set**, while at least **8 task orders are live** under D7 alone.

**The register currently states that this fabric has no open work. It has a lot.** Every downstream
instrument that sums over member projects inherits that zero.

This is the same class the whole estate has been catching all day: **a count that is arithmetically
true and about the wrong population.** It is listed first because stages 2-3 of the pipeline are
built on member sets, so a wrong membership propagates into every decomp and every TO cut from it.

---

## STAGE 1 -- WHAT IS ON THIS FABRIC (measured)

Derived off the register's **`device`** field and cross-checked against the `DIRECTIVES.yaml` header
comment (`SITEZ = D6/D7/D9/D8`, D8 retired) -- **two independent routes, same three.**

| | Directive | PRD | Members as registered | Reality |
|---|---|---|---|---|
| **D6** | Opal Analyst + partner GraphQL | yes | `OPAL_ANALYST` = **closed 08-20** | RE-SCOPED by Andrew 08-20 ~2100Z; the re-scoped initiative has **NO live project** |
| **D7** | Ticketing intake | yes | **`{}` -- EMPTY** | `OPAL_TICKET` active; **8+ live TOs** under `D7_TICKETING` / `D7_NOTIFY` |
| **D9** | Tax SMA ops | yes | `PFMG_TAXSMA` | ⛔ **`org/projects/PFMG_TAXSMA.json` DOES NOT EXIST** -- verified False. Three `OPAL_TAXSMA*` projects are **active and unreferenced** |

**Three different failure modes, and they take three different remedies** (Rule 24 (iv) -- naming
which values do not move together):

- **D6 = STALE-CLOSED.** The member is a correctly-closed project; the directive moved past it.
  Remedy: **register the re-scoped initiative as a new project.** Nothing to repair.
- **D7 = EMPTY.** Members were never populated. Remedy: **populate**, plus one new project for the
  IA work. Nothing is wrong, something is missing.
- **D9 = DANGLING POINTER.** The member names a code with no JSON, while real projects sit
  unreferenced beside it. Remedy: **repoint** -- and this one is a genuine defect, because a
  dangling member reference and an empty one are **byte-identical in the "0 open TOs" output.**

---

## ⛔ AMENDMENT ~19:1xZ -- MY STAGE-1 ENUMERATION WAS ASYMMETRIC, AND `0.0.3_BG_BBGTerminal` CAUGHT IT

**I enumerated D7's task orders exhaustively over FILES (12) and took the REGISTER at its word for
D6 and D9.** Measured now:

```
D6 TO files: 1   D6_ANALYST.TO-CDBFG-SITEZ.analyst-bindings-and-graphql-layer.md
D9 TO files: 2   D9_TAXSMA.TO-A-SITEZ.state-assessment-recon.md · D9_TAXSMA.TO-c1.daily-tracking-behind-the-guardrail-gate.md
D7 TO files: 12
```

**So D6 and D9 both carry live task orders that my stage-1 table did not surface.** My D6 row said
the re-scoped initiative *"has NO live project"* -- true about PROJECTS, and it left a live TO
invisible.

> **THE METHOD ERROR, AND IT IS THE ONE WORTH KEEPING: I ESTABLISHED THAT THE REGISTER WAS WRONG ON
> ALL THREE DIRECTIVES, AND THEN KEPT RELYING ON IT FOR THE TWO I WAS NOT FOCUSED ON.** Thorough on
> the hot directive, trusting on the cold ones -- which is exactly backwards, because the cold rows
> are where a stale register survives longest without anyone tripping over it.

### THE HAZARD UNDERNEATH IT, filed by `0.0.3_BG_BBGTerminal` as OBS-1 and now ARMED

**`to-check.py --all --assignee <serial>` cannot see an assignment recorded in a TO's `<status>`
field instead of `<issued_to>`.** Measured at their seat: the query returns **1**; they hold **2**.
The missing one is the D6 leg above, whose `issued_to` reads *"site Z, seats assigned by
0.0.0_AB_MSTR~Z"* while the real assignment sits in `<status>`.

**Under Rule 27's standing axis this moved INERT -> ARMED the moment ASSESS started**, because
ASSESS is the act it breaks. **And it fails as an UNDERCOUNT, not a zero** -- a confident number
with no caveat, which reads as a finding rather than as a failure.

**REMEDY, and it is a method not a patch: ENUMERATE LEGS OVER TO FILES, THEN READ `<status>` AS
WELL AS `<issued_to>`. Never enumerate over the assignee query alone.** That is the form I used for
D7 and failed to use for D6/D9.

### WHAT THIS DOES *NOT* INVALIDATE

**The membership finding stands and is unaffected** -- it was derived from the register's own member
sets and from project-JSON existence, neither of which routes through `--assignee`. D7's count also
stands: it was file-enumerated. **The correction is additive: D6 and D9 have MORE live work than I
reported, not different work.**

---

## STAGE 2 -- PROPOSED REGISTRATIONS

⚠ **PROPOSED, NOT LANDED. The register is `0.0.0_AB_MSTR~Z`'s surface** (`org/missions/.register-owner`),
and `/directives-check` is read-only by charter. I am supplying the concrete rows so the owner lands
them without re-deriving; I am not editing the register.

### D7 -- Ticketing

1. **Repair membership:** add **`OPAL_TICKET`** (active, P0 shipped 07-14) as a member. This alone
   converts the false `0 open TOs` into the real count.
2. **Register `OPAL_TICKET_IA`** (new) -- the merged Ticket Center surface. Purpose-level PRD already
   exists as `docs/architecture/D7_TICKET_CENTER_IA_VARIANT_SPEC.md` (@a76eb95c61), carrying Andrew's
   two rulings (no firm exposure until rollout; T1 tab model) and four open questions.
   **Downstream of `W-C` half (b)**, whose activation condition is already MET.

### D6 -- Opal Analyst

3. **Register `OPAL_ANALYST_V2`** (new, name to be confirmed by the register owner) -- the re-scoped
   initiative per Andrew 08-20 ~2100Z: *"proceeding past partner GraphQL... the mechanics of the
   agent and its interfacing with various tooling."* `OPAL_ANALYST` stays **closed**; a closed
   project is not reopened to carry new scope.
   ⛔ **SCOPE UNRESOLVED AND IT IS ANDREW'S:** the stance string is truncated in the register at
   *"particularly so in the ..."*. **I will not infer the tail of a sovereign scope sentence.**
   Carried to him.

### D9 -- Tax SMA

4. **Repoint membership** from the non-existent `PFMG_TAXSMA` to the projects that exist:
   `OPAL_TAXSMA`, `OPAL_TAXSMA_PT2`, `OPAL_TAXSMA_REGISTRY` (all **active**, all owned
   `0.5.0_AE_OpalETL~A`).
   ⛔ **OWNERSHIP FLAG:** all three are owned by a **`~A` lane that is not live on this fabric.**
   D9 is `assess-first` per its own stance, so this is not blocking today -- but a directive whose
   every member project is owned by an absent lane needs an owner decision before stage 3.

---

## STAGE 3 -- WHAT IT NEEDS, AND THE TWO CONSTRAINTS THAT BIND IT

The canonical process is **PRD -> COO~Z atom-decomp of operative surfaces BEFORE any TO -> TOs +
proof-of-spec derived from decomp cells -> execute on spec -> CVO~Z surprise channel -> v(n).**

**CONSTRAINT 1 -- THE CERTIFIER IS NOW MANNED.** Andrew ruled ~1755Z: *"spawn CVO~Z here"*. The
laptop's first run established **a COO cannot both author and certify**; with `3.0.0_SA_CVO~Z` live,
`2.0.0_SA_COO~Z` authors the decomp and CVO~Z certifies. **I stay out of the certifier seat** -- I am
the TO issuer and acceptance gate, and certifying inputs to my own TOs is the overlap I raised.

**CONSTRAINT 2 -- A TOKEN CENSUS CANNOT ESTABLISH DECOMP COMPLETENESS.** Carried from the laptop's
first run: only ~11% of in-scope S3 key call sites NAME their key (30 of 272); in the publish layer,
**1 of 112**. Generative key construction is the norm. **The collectively-exhaustive half needs a
second instrument (AST over call sites), or proof-of-spec passes green over a denominator nobody
established.** This binds D7's decomp directly -- the ticket surface builds keys and routes.

**AND: DECLARED AT THE PIN LAYER IS NOT DECIDED AT THE PRODUCT LAYER.** A cert reading
zero-undeclared-divergences is true and is **not** product clearance.

---

## SEQUENCE (proposed)

1. `0.0.0_AB_MSTR~Z` lands the four register rows above.
2. `3.0.0_SA_CVO~Z` spawns (Andrew-direct, dispatched).
3. **D7 first** -- it is the hot directive, its PRD and IA spec exist, and W-C half (b) is
   already activation-MET. `2.0.0_SA_COO~Z` cuts the atom-decomp of the operative surfaces;
   CVO~Z certifies; then and only then do TOs issue with proof-of-spec derived from the cells.
4. D6 waits on Andrew's scope tail. D9 waits on the owner decision.

## OPEN AT ANDREW (his terminal, per his own routing)

- **D6 scope tail** -- the truncated stance sentence.
- **D9 ownership** -- every member project owned by a lane not live here.
- Carried from before the pause: escalation destination confirm, EC2_MANIFEST lane, IA Q4/Q6,
  the one self-addressed test ticket.

-- 1.0.0_SA_CTO~Z, 2026-08-21
