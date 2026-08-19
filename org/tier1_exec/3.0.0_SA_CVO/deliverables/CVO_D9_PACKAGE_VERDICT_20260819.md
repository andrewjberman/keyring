# CVO VERDICT — D9 package (Tax SMA Ops: Close-Out, assess-first)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D9_TAX_SMA_OPS_PRD.md` @8d662d5f1f (163 lines, v0.1)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D9_ATOMDECOMP/run_20260819.md` @8d662d5f1f (71 lines)

**Verdict: ACCEPT — 0 P0, 2 P1.** The most epistemically self-aware package of the ten. It declares
itself a starter census and **justifies the deferral rather than apologising for it**:

- The run header states *why* completeness would be wrong here: *"pre-empting the assessment here would
  decide its conclusions before it runs."*
- §5.1-5.2 refuses to fake evidence: running the build-phase compiler set now *"would manufacture
  evidence for claims the assessment exists to test. **Stated per protocol rather than faked.**"*
- The boundaries apply Rule 22 verbatim: *"Project records are a MAP, not the territory: rows sourced
  from them are marked INFERRED-at-live and are the assessment's verification queue."*
- **F2 is left UNKNOWN and carries 17b's own caution** — *"a non-conforming tree is not a violation
  warrant"* — so the conformance read produces FINDINGS ONLY, no moves.
- Run D3 is **surfaced-not-chased** (adjacent-seat ETFS_SETUP.W2 stall), the surprise-channel discipline.
- §3's end-state specifies a **SCHEDULED** daily run citing the ad-hoc rule — the third package to apply
  it correctly (D4 did; D7 did not).

**Explicitly not a finding:** CTO banked this run's starter-census status at 185240Z; §4.3's candidate
sizing derives from INFERRED-at-live rows but the PRD states the set is *"sized from the records and
**re-scoped by (a)**"* — the provisionality is declared, so this is not the illegal-derivation class.
Checked specifically.

---

## P1-1 — For CTO. The DONE bar asserts the highest-stakes guardrail in the entire D-set is "verifiably intact" without naming a test that could fail.

The standing law, carried verbatim in both run A3 and the PRD header: *"the system GENERATES the trade
file, a HUMAN reviews and executes — **never auto-execute/auto-upload to Schwab, no Schwab/Factset
creds in code**."*

The DONE definition closes with: *"and the guardrail (human executes) **verifiably intact** end-to-end."*

**No test is named, and the claim is a negative — which is the hardest kind to verify and the easiest
to pass by assertion.** "Verifiably intact" can be satisfied by a reviewer reading the design and
concluding nothing auto-executes. That is care, not a control.

**This matters more here than anywhere else in the ten packages.** Every other DONE bar in the set
risks a wrong number, a stale view, or a missed ticket. **This one risks unauthorized trade execution
against client accounts at a custodian.** A close-out bar that can pass by assertion is not
proportionate to that.

**Recommend a test that fails if the claim is false** — Rule 22a's CODE layer, on deployed bytes, not
source:

1. **Credential absence:** scan the DEPLOYED artifacts (Lambda package bytes / on-instance read per the
   §6 fourth form you just ruled) for Schwab/Factset credential material and for any client
   construction against those endpoints — not a repo grep, which cannot see what actually shipped.
2. **No upload call path:** demonstrate the chain's terminal act is file generation — i.e. the deployed
   package contains no Schwab upload/execute call site reachable from the pipeline entry point.
3. **Exercised:** the assessment's workflow map (§4.1 item 2 already requires the guardrail be *marked*)
   states the last automated step and the first human step, with the handoff artifact named.

**Not dispatch-blocking** — TO-A is recon-only and starts now, and the build TOs cut after the meeting —
so P1, not P0. **But it must close before (c1) ships**, because (c1) is precisely the leg that makes the
chain run daily and unattended.

---

## P1-2 — For CTO + COO. D9 assigns half of a SOVEREIGN task order to D7. D7 does not know it has it.

Run D1 records **TO #42**: *"TAXSMA + Opal Ticket System scoping (verbatim record)"*, **Andrew-direct
2026-07-14**, PENDING at the dead seat `0.5.0_AE_OpalETL~A`. Confirmed independently this session via
`to-check.py`: issuer is **"Andrew (sovereign, direct terminal prompt)"**, status `pending`, **36 days
old.**

D9 §1 scopes out *"the ticketing half of stalled TO #42 **(owned by D7)**."*

**Measured this session:** `grep -in "taxsma|#42|tax sma"` over `D7_TICKETING_INTAKE_PRD.md` **and**
`D7_ATOMDECOMP/run_20260819.md` → **ZERO mentions in either artifact.** D7's scope is client DL mail →
tickets for three partner firms; it never references TAXSMA, TO #42, or a scoping obligation.

**So a sovereign instruction has been partitioned by one PRD, with one half assigned to a document that
carries no trace of it.** D9 is honest and explicit about the split — nothing is hidden — but **a
handoff declared in your own document does not create ownership in someone else's.** That is the
estate's own `in-body cc copies nobody` lesson at the PRD layer: the sender records a routing that the
recipient never receives.

**Why this is not P0:** D9 §7 Q3 does route the *seat* question (all three projects + both stalled TOs)
to the wave cut through COO, so the disposition has a channel. **Why it is still P1:** the seat question
and the content split are different questions. Re-seating D9's work does not place the ticketing half
anywhere — and that half has now sat unexecuted for five weeks on a sovereign order.

**Recommend:** either D7 explicitly accepts the ticketing half of TO #42 in its own §1 (making the
handoff real), or the split is put to Andrew as part of #42's disposition — **his instruction bundled
the two, and re-scoping a sovereign order is his call, not a PRD's.** Surfacing, not adjudicating: I am
not saying the split is wrong, only that it was made unilaterally and has not landed anywhere.

---

## Explicit deferrals

- **Starter-census status** — banked by CTO, justified in-artifact, and the deferral reasoning is
  correct. **Not a defect; the strongest §5 deferral in the set.**
- **INFERRED-at-live as a verdict variant** — seventh spelling across ten packages, but here it is
  *precisely defined* and consistently applied, and it names exactly the right epistemic state.
  Covered by @36a7fbd70e; **flagging that this particular coinage is worth keeping.**
- **F2 conformance UNKNOWN** — correctly owned by workstream (a), findings-only, migration
  ruling-gated. Rule 17b's caution carried. **No finding.**
- **Three ACTIVE projects at a dead seat** — surfaced (run A1/A2) and routed (§7 Q3). Records saying
  ACTIVE while no worker exists is real drift, but it is *named* and *channelled*, not hidden.
- **The `/tax-pt1`, `/tax-pt2`, `/tax-pt3`, `/tax-newacc`, `/taxsma-step1` skill family** (run C1) —
  enumerated with a denominator; no claim made about their currency. Appropriately scoped.

---

## What you should have asked but did not

**Every device-split table in the D-set is conditioned on a sitez capability nobody has measured — and
the split session is about to allocate against it.**

D9 proposes its assessment as *"one of the strongest whole-item sitez candidates in the D-set"*, gated
on *"IF sitez holds AWS read creds + m365 gateway reach (**MSTR capability-envelope confirm pending**)."*

That conditional is not local to D9. Across the ten:

| PRD | The condition |
|---|---|
| D9 | *"IF sitez holds AWS read creds + m365 gateway reach — MSTR capability-envelope confirm pending"* |
| D3 | *"revisit if sitez portal parity confirmed by MSTR envelope"* |
| D4 | *"EITHER if sitez portal dev proven"* |
| D2 | *"IF sitez holds read creds (MSTR envelope question)"* |
| D6 | run row 12 — the *"MECHANICAL-WORK ONLY"* vs *"get the labor out to the other fabric"* tension, **explicitly unreconciled** |

**Five packages defer to one envelope, and no PRD owns establishing it.** Each correctly declines to
adjudicate it — D6 routes it to the CTO+COO session by name — but the effect is that **the split
session will allocate legs to sitez on assumed capability rather than measured capability.**

**The failure direction is the expensive one.** If the envelope is narrower than assumed, the legs
allocated to sitez bounce back to the laptop *after* planning — and load-shedding is the split
session's entire purpose, so the plan fails precisely where it was supposed to help. It also lands on
the device the standing word already constrains, which is how an inferred scope becomes a stall.

**Recommend: the split session's FIRST act is to MEASURE the envelope, not allocate against it** — does
the sitez seat hold AWS read credentials, does it reach the m365 gateway, is portal dev parity real
there? Three probes, answerable in minutes, and every device-split table in the D-set resolves from
them. **Allocating first and measuring second inverts the dependency, and the D-set has already written
the dependency down five times without anyone owning it.**

*(Structurally the same shape as D4/D5's unowned CSV source, one layer up: a shared precondition that
every dependent names and no one owns.)*

— 3.0.0_SA_CVO
