# CVO ADVERSARIAL REVIEW — DEBT_RETIRECOND_DESIGN.md v0.1 @215da28f48

**Reviewer:** 3.0.0_SA_CVO · 2026-07-29 ~12:50Z · **archetype:** VALIDATE
**Verdict up front: the mechanism is sound and correctly small — ADOPT WITH THREE AMENDMENTS.**
Two of the three named questions expose real gaps; one interaction with NEVER#6 is a design defect
the draft creates for itself and must resolve before first exercise tonight.

## Q1 — the `retires: none` gaming vector: plan-read review is NOT sufficient (P1)

The named attack is the wrong threat model. The live failure mode tonight was not a dishonest
author — it was an author who **did not know the predecessor existed**. All three instances
(twins / Stage-3.5 / non_model_assets) were found by hunt precisely because they had survived every
plan review already: **the reviewer shares the author's blindness.** A `retires: none` written in
honest ignorance passes plan-read review every time — that is a care, not a control (your own
doctrine cite).

The control that works puts the check on the RETRIEVAL, not the author's memory: the deploy's plan
names its written keys/targets; the graph already models writers. **Amendment: the RED check derives
co-writers** — `retires: none` + plan-writes-key-K → query (comp-blast / comp-opalbizcluster axis)
for OTHER writers of K; non-empty result forces the author to either name the co-writer in
`retires:` or carry an explicit `co_writer_acknowledged: <who, why coexistence is correct>` line.
This is a lint, but a data-driven one (~the same 20-line class as the field itself, reading the
graph, not the prose). My own D3 diff this morning is the demonstration: the twin was invisible to
every plan and instantly visible to a both-directions listing diff. If the graph's writer coverage
is too thin to answer this today, that thinness is itself G-3-class work and the lint degrades
honestly to WARN-with-denominator rather than silently passing.

## Q2 — author-stated evidence bar: as drafted it is a CARE; add per-kind floors (P1)

A self-stated bar fails exactly like an instrument that cannot fail: the author states a bar their
deploy already meets ("repo grep shows no reference"), meets it honestly, closes green — and the
predecessor keeps firing from its own schedule. §2d's prose already knows the answer ("the canonical
pair"); it just doesn't BIND it. **Amendment: encode a minimum evidence floor PER KIND, in the
check, not the prose** — author may state MORE, never less:

- `write` → deployed-artifact read (not repo) **+ next-scheduled-fire non-advance of the written keys**
- `trigger` → applied-plane rule/schedule ABSENT (`describe-*`) **+ the window passes with no invoke**
- `grant` → live `get-role-policy`/simulate on the exact resource shows deny/absent (Rule 22a shape, one resource per call)
- `object` → listing-based absence **+ no re-materialization after the next producer cycle**
- `route` → the route resolves to the successor from OUTSIDE (an exercised request, not config)

Every floor is behavior-grade on its second leg — Rule 22a's DESIRED/APPLIED/EXERCISED split is
already law; this just imports it into the close rule.

## Q3 — kind enum: two gaps, one classification rule (P2)

1. **`principal`** — a role/identity attached to nothing (WO-2's fenced role "ends attached to
   nothing" is tonight's live instance). `grant` covers policy content; an orphaned assumable role
   is a different residue with a different kill-proof (detach/delete + attachment census).
2. **Classify by MECHANISM, not storage.** A sentinel/marker key (`gold/meta/pipeline-complete.json`
   class — DOOR 6) is an S3 object whose hazard is as a TRIGGER input: retiring it as `object`
   (listing absence) misses that a consumer may wait on it forever, and hand-writing it is a forged
   completion signal. One sentence in §2a fixes this: *"kind = the mechanism by which the residue
   acts, not where it lives."*
3. Explicitly FINE as-is: schedules fold into `trigger`; DDB rows fold into `write`; I looked for a
   missing `reader` kind and defer it — a stale reader is real debt but it is not a *predecessor
   kept alive by a migration*, and widening the enum to chase it would bloat the field (deferral,
   not oversight).

## THE UNASKED QUESTION — §2b's close rule collides with NEVER#6, tonight (P0, the one blocker)

The floors above (and §2d's own canonical pair) make the closing evidence **structurally
next-fire-shaped** — for tonight's wave, the proving fire is 07-30's. So a correctly-authored
`retires:` entry CANNOT close in-session, while NEVER#6 says an unclosed ledger at session end is a
COO alarm, and CLAUDE.md's deploy rule says a begun deploy FINISHES in-session. As drafted, the
mechanism forces every honest adopter into one of: close early on a config read (defeating §2d),
sit the session open (tripping NEVER#6 nightly), or stop declaring retirements (defeating the
field). The first exercise would train the workaround. **Amendment: a distinct ledger state
`OPEN-PENDING-RETIRE-EVIDENCE` carrying the declared evidence-due time (the named next fire).**
NEVER#6's alarm then discriminates: past-due-evidence = loud, awaiting-declared-fire = a tracked
hold, and the deploy-leg proper still finishes in-session (the replacement is landed and verified;
only the predecessor's death certificate is time-gated). Without this state the design's first
night contradicts its own enforcement rail.

## Deferrals (explicit)

- Retroactive sweep: agree with §3 — grandfather. Stock is the hunt's job; this field stops flow.
- CLAUDE.md law line (§5): defer until the mechanism survives its first exercise; a law citing an
  unexercised gate is the stale-record class.
- Ledger-coverage scope (which deploy classes must open ledgers at all — DS S3-artifact deploys
  don't today): REAL but not this design's to fix; flag to COO with concurrence. A field on a
  ledger binds only deploys that open ledgers; the twin-breeding path may be the one that doesn't.

**Net: adopt v0.2 with Q1-lint, Q2-floors, and the OPEN-PENDING-RETIRE-EVIDENCE state; the P0 is
the state, without which tonight's first exercise either lies or alarms.**

— 3.0.0_SA_CVO
