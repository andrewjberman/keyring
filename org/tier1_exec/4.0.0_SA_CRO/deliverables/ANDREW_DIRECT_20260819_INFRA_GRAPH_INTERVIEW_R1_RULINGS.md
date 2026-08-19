# ANDREW-DIRECT 2026-08-19 (CRO terminal) — infra-graph planning interview, ROUND 1 RULINGS (Q1–Q5)

**Recorded by:** 4.0.0_SA_CRO · **Channel:** CRO terminal, written answers to the five round-1 interview questions on the voice memo (`ANDREW_DIRECT_20260819_INFRA_GRAPH_VOICE_MEMO_VERBATIM.md` @3033712139) · **Time:** 2026-08-19 ~15:4xZ
**Status:** RECORDED + BROADCAST same turn. The Cascade refinement (Q2) is EXECUTED in the same commit (SYSTEM_DEFINITIONS v3.2).

## Q1 — the endpoint benchmark. VERBATIM:

> "Yes this is the ultimate benchmark, we don't have a test case yet but we will very soon with new
> partner onboarding which is why we need to be prepared. Other than that context, yes we are aligned
> with your rec; I would just specify that there are a lot of smaller tests and work building up to
> this point, which is the true crown jewel performance benchmark."

**Binding content:** zero-shot partner instantiation = the CROWN JEWEL performance benchmark. A real
test case arrives SOON via new partner onboarding — readiness is the point. The program carries a
LADDER of smaller tests building up to it.

## Q2 — the hierarchy IS the Cascade, refined. VERBATIM:

> "This is just a refinement of cascade where NLP is being explicitly threaded in. The 'Cascade' is
> essentially a high level guideline for how to think about the process of transcribing large
> amounts of information into rapidly-accessible high signal derived insight fast. A refinement i
> might add on this subject is that bm25/corp-localize work should really be covering 90-95%, then
> nlp should be 5-8% (nlp used properly is a lot cheaper than AI inference), AI use is maybe a
> couple percent effectively the balance, and user input is more like 0.1% or less in terms of
> volume of information, but it is the highest signal in a proper system. This is really to
> establish a framework understanding of how processes are to be created, we want to really do
> everything deterministically/lexically, if it must be elevated, then we elevate to NLP, if that
> must be elevated its elevated to AI inference, if that must be elevated only then does it go to
> the user. Does that make sense? It's really a philosophy above all."

**Binding content:** my round-1 rec (sibling term) is OVERRULED — this is a CASCADE REFINEMENT, not
a new axis. Four stages: deterministic/lexical 90–95 → NLP 5–8 → AI inference (targeted, effectively
the balance, ~a couple percent) → user input (≤0.1% of volume, highest signal). Escalation law:
everything at the lowest rung that can carry it, elevated only when it must be. A philosophy above
all — the framework for how ALL processes are created.
**CRO formalization, flagged for one-word correction if wrong:** the former INFERENTIAL band (≤9)
SPLITS into NLP (5–8) + AI inference (~balance); the former USER_DESCRIBED (≤1) tightens to ≤0.1
volume. Node-grain binding, per-substrate re-derivation, floors-of-honesty, and the W-01 framing
rider are UNTOUCHED by the refinement.

## Q3 — "resolves" = COMPILABLE coverage universes. VERBATIM:

> "What derive means is that if we tie something to 'substrate' as a coverage universe, and
> substrate is defined as 'AWS' 'MS' 'ajb_workspace' 'portal', then those substrate C0-C3 elements
> and associated D1-D3 should all be cogently mapped within that substrate parameter, so a comp-tool
> with coverage defined as 'substrate: AWS' has full coverage of those defined elements and there is
> no ambiguity whatsoever on that. This is the general idea, that when we use terms, which become
> our coverage universe, either a substrate, a C(N) layer, etc. that all of these concepts resolve
> in a machine-readable/deterministic manner; they should be compilable not just conceptual or
> hand-drawn. Your rec is aligned with this I'm just hammering it in more forcefully and
> specifically. We need to know every square inch of our estate at every layer of granularity C(N)
> and D(N), and that means making sure our ontology and definitions allow for that kind of
> resolution."

**Binding content:** the audit predicate (derivable-by-tool + declared-count parity + drift gate)
is CONFIRMED, strengthened: every registry term that functions as a coverage universe must
**COMPILE** — resolve machine-readably to its member set at every C(N)/D(N) grain, zero ambiguity.

## Q4 — substrate order. VERBATIM: "Rec approved."
codebase substrate first (instantiation derives from code + Terraform patterns; rides S0), MS /
document space second; aws/portal already strong.

## Q5 — program form + lead. VERBATIM: "Rec approved, you lead it."
Macro program, own PRD + atom_decomp ground-truth run at issuance, **CRO leads end-to-end**,
absorbing the 08-12 S0-S5/B1-B3 spine (CTO asked to discharge or fold the W-06 arch-gate).

## Execution in this commit
- Cascade entry refined + registry v3.1 → v3.2 (checker + comp-estate exercise post-edit).
- Program PRD + registration follow the interview's close (round 2 pins the plan skeleton).
