# AMGT_HARVST -- ROUND 6 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-26 ~03:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 25984, READ-acked, subject *"L10 slug: AMGT_HARVST
round 6 CLOSED (scoped, as offered)"*, citing `ADJUDICATION_v14` @`a0db9883ca`.

**Round 6 is CLOSED. The project is NOT closed, and the endpoint was NOT reached.**

---

## 1. THE HEADLINE -- THE ROUND'S REASON FOR EXISTING BECAME EXERCISABLE TWENTY MINUTES AFTER IT CLOSED

The slug's first finding, verbatim: *"AC1 is SUPERSEDED and AC1a reads NOT_EXERCISED -- UNEXERCISABLE BY ANY
SEAT. The one bounded vendor act the round exists for never happened. Terminal is not endpoint reached."*

**Every order went terminal and the act the round was cut to perform did not occur.** No seat could have
performed it: it needed a per-use vendor word that no seat holds and none may grant itself.

**At ~03:xxZ Andrew gave that word** (`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md`
@`f3b85ff6a5` section 1): *"Egress is permitted for API calls this session -- no per-use word per vendor
call, but every call is ledgered by the seat that makes it."*

**So AC1a is exercisable now and was not exercisable for the whole of round 6.** That is the round's real
result and it is the first item of the enrichment list.

**Two constraints the lift does NOT relax**, and a recut that ignores either is cutting against law:
1. **The mechanism.** The lift is on the AUTHORIZATION. `vendor egress is broad on authority and narrow on
   mechanism` still binds: the call runs from a SCRIPTED PRODUCER, never inside an agent turn.
2. **The ledger.** *"every call is ledgered by the seat that makes it"* is a CONDITION. A cell whose worker
   cannot write the ledger row does not carry the word, and the criterion must name the ledger path.

---

## 2. WHAT THE SLUG MEASURED, AND THE SCOPE IT DECLARED FIRST

**The CVO declared its own blind spot before its findings, which is what makes the rest usable:** *"no
drain-end packet exists -- 0 hits over 112 files, no COO deliverables dir. I compiled the CHANNEL and the
ORDER; any issuer act in neither is invisible here."*

**I adopt that scope and restate it as a limit on THIS analysis.** A denominator of 112 files with a printed
zero is an absence read on a named corpus, not a universal: an issuer act that landed in neither the channel
nor the order is invisible to the slug and therefore invisible here. **The COO's drain-end packet is the
artifact that would close the gap, and its absence is an enrichment item, not a defect of the round.**

| limb | reading |
|---|---|
| L7 terminal count | every order terminal |
| L9 | **VACUOUS, not passed** -- *"0 of 8 judgment criteria, confirmed against a control that reads 1"* |
| channel | 12 of 12 dispositioned, 3 carried |
| new BLOCKING row | **Z-S28**, landed `02:37:37Z`, 57 minutes after this seat's ask |

**L9 vacuous with a control that reads 1 is the right way to report a zero.** Zero judgment criteria graded
and a control proving the grader COULD have graded one separates "nothing to grade" from "grader broken" --
which a bare zero cannot. `a-zero-with-its-cause-named-is-a-finding`.

**And it means round 6 has no plausibility oracle.** Eight judgment criteria, none graded: every mechanical
column can read green over a result no one assessed for sense. That is the `all-mechanical-round` shape and
it is why "every order terminal" is not evidence the round worked.

---

## 3. Z-S28 -- THE BLOCKING ROW THAT ARRIVED AFTER THE ROUND WAS OVER

*"sa's listing pages cannot reach silver at all."*

It landed 57 minutes after I asked for the slug and it is BLOCKING. **It is not a round-6 defect and it is
not deferrable:** a listing surface that cannot reach silver is a broken journey, and round 6's own AC1a
population comes through that path. **Disarm owner is the issuer** (`2.0.0_SA_COO~Y`) per the standing rule
that a surprise row names the issuer, never a worker. **It leads the recut**, ahead of AC1a, because an
AC1a fire into a path that cannot reach silver produces an artifact nothing can read.

---

## 4. FWD GRADES

Round 6's endpoint outcomes are **NOT REALIZED**: the round's one bounded vendor act never ran, so no
outcome depending on harvested output can be graded REALIZED, and L9 graded no judgment criterion that
would have carried the rest. **Rule 27's close condition -- every FWD grades REALIZED -- is not met, so
this analysis ends in an ENRICHMENT LIST rather than a project close.**

---

## 5. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Y` recuts, in order

| # | cell | why it is where it is |
|---|---|---|
| 1 | **Z-S28 disarm** -- sa's listing pages reach silver | BLOCKING. Everything below fires into this path |
| 2 | **AC1a, the bounded vendor act** -- now exercisable | SCRIPTED producer, not an agent turn; the criterion NAMES the per-seat ledger path; the word is session-scoped, so it is the round's first real cell, not its last |
| 3 | **The 8 ungraded judgment criteria** | L9 was vacuous. A round that grades none has no plausibility oracle; these are graded at L9, never self-graded |
| 4 | **The COO drain-end packet** | its absence is what bounded the slug's own scope to the channel and the order |
| 5 | The 3 carried channel rows | dispositioned, carried, still owed |

**Fan-out:** derived from the dependency chain above, not chosen. Cells 1 and 2 are serial -- cell 2's
output is unreadable until cell 1 lands -- so the round's critical path is two cells deep and no cap
pressure exists. **Cell 2 carries at most THREE mechanical criteria** per the spine's build-TO rule.

**A note the recut must not lose:** the vendor word is *"this session"*. A cell that sits in a queue past
the session's end loses its authorization silently. **Cell 2 runs while the word is live or it does not
run**, and if it cannot, that is a card to Andrew rather than a cell that quietly expires.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not grade the issuer acts the slug could not see (section 2). It does not lift a mechanism
constraint. It does not re-open an L4-R half: the endpoint is unchanged, and adding no outcome, this is a
recut input rather than a PRD addendum.

## Compiler Tools

The slug's own printed denominator (0 hits over 112 files) adopted as a stated limit rather than absorbed --
the control-reads-1 beside L9's zero, which is what distinguishes a vacuous grade from a broken grader --
`git log -1` on `a0db9883ca` to place `ADJUDICATION_v14` against the round's terminal times -- the arming
record at `f3b85ff6a5` section 1 read for the egress term's exact scope rather than its summary.
