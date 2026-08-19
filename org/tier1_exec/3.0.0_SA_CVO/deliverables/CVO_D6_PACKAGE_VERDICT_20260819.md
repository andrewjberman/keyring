# CVO VERDICT — D6 package (Opal Analyst v0 + Partner GraphQL Access Layer)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned — AMENDED VINTAGE per CTO 190441Z:**
- `docs/architecture/D6_OPAL_ANALYST_GRAPHQL_PRD.md` **@a02f9ff5a4** (143 lines + ADDENDUM ~18:57Z)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D6_ATOMDECOMP/run_20260819.md` @375c874a9e (55 lines)

**Verdict: ACCEPT WITH 1 P0 + 1 P1.** Strong run — row 7 carries its own vintage caveat *and* a named
remedy (U2: *"first act of any dispatch touching the program: re-read the JSON + certification
artifacts"*), row 9's greenfield claim is properly grounded with denominators and band disambiguation
(99/26,823, HEAD=9 all vendored lexer), and row 12 flags the live device-scope tension between *"site Z
is MECHANICAL-WORK ONLY"* and today's *"get the labor out to the other fabric"* while **explicitly
routing reconciliation to the CTO+COO session rather than adjudicating it.** The addendum carries
Andrew's phasing qualification verbatim and applies the INTERNAL-FIRST law correctly.

**The P0 is a consequence of the addendum being good** — it landed real new ground truth, and the run
did not move with it.

---

## P0-1 — For CTO. The addendum discharged U1 at the PRD layer, so the RUN now contains a false statement — and an entire new workstream traces to no run row.

**The two halves of the package now disagree.**

| Artifact | What it says about Andrew's spec file |
|---|---|
| Run row 10 | *"Andrew holds a spec file; **NOT yet delivered** (slot open)"* — verdict `MEASURED-RECORD (the pend is the fact)` |
| Run U1 | *"GraphQL schema surface — **BLOCKED-INPUT** on Andrew's spec file"* |
| PRD addendum | *"**U1 DISCHARGED: the spec file LANDED**"* — stored, extracted, bound |

Row 10 was true when written and is **false now.** A reader of the run alone concludes the schema half
is blocked; a reader of the PRD concludes it is unblocked with a new workstream attached. **You defined
the review unit as PRD + run; the unit is now self-contradictory.**

**The substantive half is what makes this P0, not the bookkeeping.** The addendum introduces material
that the ground-truth chain requires to trace to a run row, and none of it does:

- a **schema surface** (Account / Advisor / Strategy / Custodian / FeeSplit / Performance / Benchmark /
  DataIssue, + Household);
- **an entirely new workstream — TO-G, the entity-resolution service** — *"the brief mandates it as a
  SEPARATE capability **sequenced BEFORE GraphQL execution**"*, which is a dependency reorder, not an
  addition;
- an **agent-surface reshape** (five business tools compiling to GraphQL internally);
- **guardrails binding as spec** rather than advice.

These are honestly cited to the ingest note by section (`§10`, `§0` verbatim), so this is **not** the
unmarked-untraced class — the evidence exists and is committed. The defect is that **the chain
specifies run rows as the grounding layer, and an addendum routed around it.** Per your own rule, TO-G
cannot carry a TO expected-value off a surface claim with no row.

**Recommend (CTO), cheap:** amend the run with a row (R14) pinning the delivered brief + ingest note,
re-verdict row 10, and mark U1 **DISCHARGED** with its pointer. Then the addendum's claims trace
normally and TO-G is dispatchable.

**The generalizable half, worth a family ruling — this is the third run/PRD desync tonight but the
first of its KIND.** D1 (`R1-R14` vs R1–R17) and D3 (`#1-#11` vs #1–#13) were pointer
under-declarations: the run was right, the pointer was stale. **Here the run itself has gone false.**
A run is a point-in-time artifact and a PRD can outrun it within hours. **Recommend: when a PRD is
amended with new ground truth, the run gains a row in the same commit** — otherwise the "trace to a run
row" gate silently stops applying to exactly the newest and least-reviewed material.

---

## P1-1 — For CTO. TO-G's entity resolution inherits an unclassified residual that D3 exists to close, and no cross-PRD gate says so.

The addendum specifies TO-G as *"fuzzy name -> canonical ID, confidence, disambiguation-on-ambiguity"*,
consuming *"the measured identity plane (a06 crosswalk, dim_portfolio_group/bridge when landed,
household nesting)."* Naming those inputs is right. **What is missing is that two of them are not
settled, and one is D3's entire precondition workstream.**

- D3 §4.1 measures the a06 crosswalk at **99.65% end-to-end**, and TO-D3.1's whole purpose is to drive
  it *"to 100%-CLASSIFIED: every account either joins or carries an explained residual class"*, with a
  residual enum (`NO_SMARTX_ALLOCATION | NOT_IN_ACCOUNT_UNIVERSE | NON_8DIGIT_KEY | OTHER_CUSTODIAN |
  CLOSED | UNRESOLVED`) **not yet finalized.**
- `dim_portfolio_group`/`bridge_group_account` are threaded into **D2's** decomposition (CRO~A T2) and
  do not exist yet — the addendum's own *"when landed"* concedes this.

**So an entity resolver built before TO-D3.1 lands would assign confidence over a universe whose
~0.35% residual is unclassified — and "unresolvable" and "resolvable but in the residual" would be
indistinguishable in its output.** That is a confidence score that cannot mean what it says. §6 carries
no gate expressing this; TO-E gates on TO-B, and TO-G has no gate row at all.

**Recommend:** give TO-G an explicit gate on TO-D3.1's residual enum (not on all of D3), and state that
its disambiguation classes must be drawn from that enum rather than minted separately — otherwise we
get two residual vocabularies for one identity plane, which is the Rule-24 duplicate one layer up.

---

## Explicit deferrals

- **U2 certification-count drift** — row 7's count is JSON-vintage and **says so**, with the re-read
  named as the first act of any dispatch. **Exemplary handling of a record-sourced count; the pattern
  D0's TO-5 should have followed.**
- **Row 12 device-scope tension** — correctly surfaced and explicitly NOT adjudicated (*"reconciliation
  belongs to the CTO+COO split session, NOT this run"*). Right call; scope adjudication is not the
  run's to make.
- **Row 9 greenfield claim** — 99 hits / 26,823 files with all 9 HEAD hits identified as a vendored
  pygments lexer, plus a name-glob cross-check. **Absence claim done properly.**
- **The `*autologin*` disambiguation** (3 hits, all bd-vendor auth, distinct system) — a name collision
  caught and resolved inside the run. No finding.
- **Parquet-plane phasing** — Andrew's INTERNAL-FIRST qualification carried verbatim and applied (v0
  binds operational surfaces only). Conforming; not mine to adjudicate.

---

## What you should have asked but did not

**D7 deferred a live authorization finding on the premise that the Analyst stays internal-only. D6
makes the Analyst partner-facing. Does that premise survive?**

D7 §7 Q3 defers the ticket-API authorization finding (R6 — *"opal-ticket-api STAMPS caller identity,
never CHECKS it: no per-caller/per-firm authorization on six /api/scoped/ routes; any authenticated
portal user can list/claim/complete any firm's tickets"*, standing at Andrew since 08-12) with this
reasoning: *"v1 stays internal-only, **so intake does not widen the exposure class**."*

**D6 §1 then makes the same Analyst the termination point of a partner-facing query layer** — *"partner
(Teams) → GraphQL query layer"*, resolvers bound to the W5 index, which is by its own definition the
one catalog of *"where to find various info for easy access via aws reads."* And the addendum's
guardrail item 4 mandates *"server-side tenant authz on EVERY resolver — never rely on the model to
scope access correctly."*

**That guardrail is exactly right, and it is being applied FORWARD to the new layer while the adjacent
existing surface in the same product family has none.** The two PRDs were authored in one pass by one
seat, and the deferral premise in D7 is conditioned on a scope that D6 changes.

**I am not asserting exposure — I do not know whether the W5 index catalogs the ticket surface, and
that is precisely the question.** Three things to settle before TO-E, none expensive:

1. Does the W5 request index include the ticket/DDB surface? If yes, D7's *"internal-only"* premise is
   no longer sufficient on its own to defer R6.
2. Does the GraphQL layer's server-side tenant authz sit **above** an underlying API that performs no
   tenant check — and if so, is the authz then the *only* thing standing between a partner and another
   firm's rows? A correct check above an unchecked surface is a single point of failure, not
   defence in depth.
3. If the answer to (1) is no, **say so in D6 §4.5's resolver floor** — an explicit exclusion is worth
   one line and makes D7's deferral premise durable instead of incidental.

**Why neither PRD could catch this:** each is internally consistent. The premise of D7's deferral lives
in D7; the scope change that pressures it lives in D6. Only a reader holding both sees it — which is
the whole reason the ten went to one reviewer.

— 3.0.0_SA_CVO
