# ANDREW-DIRECT: scope outcome arrays/predicates -- MECE + layer coverage, always (2026-08-20 ~145xZ, CRO terminal)

**Channel:** Andrew-direct at the 4.0.0_SA_CRO terminal, mid-turn during Response VII drafting (the
GPT causality exchange).
**VERBATIM:** "As you're getting these, I think it's important that we try to 'scope' them better
where possible, the most obvious case is the rule 24 framework, we need to always be testing these
outcome arrays/predicates/etc on whether they are at the very least MECE, need to make sure we are
robustly covering the layer a given schema is meant to cover"

**SCOPE (surfaced, not adjudicated):** a HOW-TO-RUN-THE-TEST directive on the widened Rule 24:
(1) outcome arrays / typed-result sets / predicates ARE schemas and get the test -- they escape the
gate precisely because they do not read as schemas; (2) the collective-exhaustion half of postulate
(i) is evaluated AGAINST THE DECLARED LAYER the schema covers (name the layer, then hunt the
uncovered member), never against internal consistency alone.

**Immediate application (same turn):** the three typed arrays adopted in Response VII round 7 were
run through the test BEFORE the response shipped. Findings: the advocacy-result array needs a
declared precedence rule AND is missing NOT_EXERCISABLE at its layer (an un-runnable control would
have read as a run one -- the unexercised-control class); the eligibility array needs the
one-evaluation-per-(assessment,scope) rule stated; the four failure surfaces cover mid-unit purpose
escalation ONLY IF the sterility cut is modeled as a leased closure member. One-sentence scoping
landed in CLAUDE.md Rule 24's widening clause (this commit). Standing consequence: every enum in the
consolidation PRD ships with its MECE-and-layer-coverage record attached.
