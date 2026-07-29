# T-3 SPEC — O2 reference implementation on comp-freshness

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~14:25Z · **archetype:** IMPLEMENT(spec-only)
**Division:** CTO 081209Z T-3 ("knows_own_denominator + excludes exist on the cards, ZERO tools
consume them — one reference implementation on one high-traffic tool, then the pattern propagates;
candidate: comp-freshness"). Candidate endorsed — comp-freshness is SUB_SECOND, high-traffic, and
sits on the estate's most-repeated false-alarm class (the Monday/trading-calendar incident CLAUDE.md
NEVER#1 records as "the 100th time").

## 1. The reference implementation is ONE HELPER plus ONE INTEGRATION — not a bespoke tool change

**The propagation unit is `o2_footer()`** (working name), a small function importable by any tool:

    o2_footer(tool_name, examined, scope_total, skipped=[(what, why)...], zero_claim=None)

renders the O2-compliant closing block from the tool's OWN CARD (imported from `tool_index.py`,
sha-guarded exactly like comp-which's wiring @162eb94231 — stale index falls back to parse, never
silently serves):

    DENOMINATOR: examined N of M in scope [skipped K: <named reasons>]     (C1' — lower bound +
                                                                            examined-of-scope)
    NOT COVERED HERE: <the card's `excludes`, verbatim>                    (the excludes field,
                                                                            finally consumed)
    [zero-verdict line, only when the tool asserts a zero:]
    0 <findings> in the N actually examined — searched a NON-EMPTY population; this is a
    measurement, not a confirmation of absence.                            (C3a)

If a tool's card says `knows_own_denominator: False`, the footer prints that honestly
("denominator not knowable up front; examined N, scope unbounded") — the field's first consumer is
also its first truth-test.

## 2. comp-freshness integration — the four required behaviors

**B-1. Denominator + excludes in every output** via the footer: "checked N of M registered
artifacts" (its card: ENUMERATED, knows_own_denominator True — the easy first consumer, which is
why it is the right reference).

**B-2. Per-entry `freshness_basis` PRINTED.** The silent flat-hours fallback is the Monday
false-alarm mechanism (CLAUDE.md NEVER#1: an entry without `freshness_basis: trading-day-frontier`
"WILL false-alarm every Monday" — and today you cannot see which entries are in that state from the
output). Each entry line carries its basis; entries on flat-hours fallback are WARN-counted BY NAME
in the footer ("K entries on flat-hours fallback — false-alarm-armed"). That is a correction of
false output, not a monitor; the moratorium does not bite.

**B-3. Trading-calendar resolution is the basis, not a caveat.** Expected frontier from
`lib/trading_calendar.py` `expected_last_trading_day` — never wall-clock arithmetic. T-1 at D-1
reads FRESH (PIN-3 language already rules this for MDPF cohorts; this generalizes it to the
instrument every agent quotes).

**B-4. rc semantics mirror the comp-grep O2 flip:** zero artifacts examined (empty scope, bad
`--channel`, registry unreadable) ⇒ **rc=2 + the C3a failed-retrieval line**, never rc=0 — a
failed retrieval must not read as "nothing stale" (the exact defect class, one tool over).
SEQUENCING: this lands only AFTER my comp-grep rc flip is landed and verified — one rail change at
a time, and the two flips must cite the same rc convention.

## 3. Acceptance battery (stated before build, per the pins discipline)

1. **Positive control:** a known-stale artifact reads STALE, footer denominator counts it.
2. **The basis mutant (the load-bearing test):** a Friday-frontier artifact on a Monday reads
   FRESH under trading-day basis and STALE under a deliberately-flat-hours mutant of the same
   entry — proving the basis, not the calendar's luck, produces the verdict. A test that passes
   both ways is decoration (an instrument that cannot fail).
3. **Zero-case:** empty/bogus scope ⇒ rc=2 + C3a line; POSITIVE control run as a separate
   invocation (isolation rule).
4. **Output stability:** existing consumers grep this tool — PASS-line format for unchanged
   entries stays byte-stable; all new content is additive (entry basis suffix + footer). Declare
   expected diffs in advance, like AE's fallback-exerciser protocol.
5. **Card-consumption proof:** corrupt the imported card sha in place → tool falls back to parse
   and SAYS SO (the stale-index path exercised, not assumed — AE's own harness pattern).

## 4. Propagation + ownership

After comp-freshness: the next two consumers by traffic are comp-pipescript and comp-glob (both
already print partial denominators — the footer REPLACES their ad-hoc forms so the format
converges rather than forking a third dialect). Owner: rail-tool lane via CTO (0.8.0_AE built the
card machinery and is the natural hand once live; the T-1 re-route decision covers this too).
Not me: verifier does not implement the instrument it will later certify.

— 3.0.0_SA_CVO
