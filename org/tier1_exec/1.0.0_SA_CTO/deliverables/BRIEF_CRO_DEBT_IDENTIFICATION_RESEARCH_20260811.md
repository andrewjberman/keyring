# RESEARCH BRIEF -- HIGH-FIDELITY DEBT IDENTIFICATION FOR THE CLEANUP STAGE (P5)

**Commissioned by:** Andrew (2026-08-11 ~1750Z, CTO terminal: *"a brief... to do some research on
how we can identify debt most effectively with highest fidelity for the cleanup stage, should
cover all resources as well as artifacts"*).
**Authored:** 1.0.0_SA_CTO. **Addressee:** 4.0.0_SA_CRO~A (Andrew-direct retarget ~1757Z: "Do it
for CRO~A" -- dispatched by CTO on his word; the brief text below retains "CRO" generically).
**Deliverable wanted back:** a DEBT-IDENTIFICATION METHODOLOGY SPEC -- how P5 will census, grade,
and evidence estate debt -- routed CVO (instrument review) -> CTO (ratify) -> Andrew. Research
and design only: **no detectors, monitors, or notification machinery** (the standing moratorium),
and **nothing in this research deletes, moves, or reclassifies anything** -- P5 executes later,
gated on the portal-verified event per the phase framework
(`docs/architecture/GOLD_MIGRATION_PHASE_FRAMEWORK.md`).

## 1. THE PROBLEM

At P5 the program decommissions every legacy path the migration obsoletes. The estate's failure
mode is NOT missing debt -- it is MISCLASSIFYING live things as debt (and deleting them) or
ratifying debt as live (and keeping it forever). The research question is therefore a FIDELITY
question: **for each candidate, what evidence establishes LIVE vs DORMANT vs DEAD with the
smallest false-positive rate, and what is the cheapest sufficient evidence chain per class?**

Scope = ALL resource classes and ALL artifact classes: Lambda functions + layers, EventBridge
rules (BOTH namespaces -- default and SCHEDULER), S3 prefixes/objects (bronze/silver/gold/
platinum + code stores), DynamoDB tables, IAM roles/policies, CloudFront/API-Gateway routes,
EC2 services (EC2_MANIFEST.json), SSM documents, repo scripts/configs, comp-tool registrations,
freshness entries, deploy-ledger sentinels, and the serving JSON estate.

## 2. WHAT TODAY ALREADY PROVED, ONE DAY'S SPECIMENS (each is a false-positive CLASS your
methodology must defeat -- all measured 2026-08-11)

1. **Router-mapped "orphans":** 5 of 21 cot orphan-candidates were CLAIMED by the scoped router's
   key-mapping (`artifacts/x` -> `gold/artifacts/x`), invisible to any S3-side census. Only the
   router's deployed config (read live) adjudicated them. *A key nothing names directly can be a
   key everything reads.*
2. **Key-migration wearing abandonment's clothes:** `gold/clients/` -- 2,949 objects, 126.5d
   stale, reads "abandoned"; the live successor (`gold/entities/clients/`, 17,318 objects, 0.5d)
   sat one prefix over, migration documented at `gold-artifact-mapping.md:174`. Age alone cannot
   distinguish these, and the two dispositions are OPPOSITE.
3. **Closed-period immutables:** 23 quarterly snapshots (2020Q3..2025Q4), dormant forever and
   CORRECTLY -- a refresh would be the defect. Not a TTL; a permanent exemption KIND (Rule 25's
   two-kind exception split, CLAUDE.md).
4. **Guarded sets / same-leaf twins:** `header_metrics.json` live at one nesting level, dormant
   at another; the `account_units`/`account-units` spelling pair where gold spells `_` and served
   spells `-` BY CONSTRUCTION -- a census keyed on leaf name reads the other half as orphaned,
   and BOTH directions fail toward deleting the live one.
5. **A sentinel that never learned:** the wo4c deploy-ledger sentinel sat 14 days "held" while its
   work order had COMPLETED under a successor entry -- record-vs-record drift, third instance that
   day. Ledger state is a CLAIM, not evidence.
6. **Deprecated-but-serving:** certified-AUA -- ruled dead by Andrew 07-24 -- is the LIVE serving
   basis at bd (DEGENERATE_CERT_MODE hold) and a serving override at cot. Debt by RULING, live by
   wire: your taxonomy needs a value for "sovereign-retired concept still carrying production
   traffic," and its remedy is a migration act, never a delete.
7. **Retirement done right (the estate's own precedent):** comp-surface-check -- consumers
   retired FIRST, binary LAST, because a gate whose binary disappears fails SILENT (`command -v`
   skip). Any teardown ordering your methodology proposes inherits this law.

## 3. THE STANDING LAW YOUR METHODOLOGY INHERITS (do not re-derive; cite)

- **Rule 25 (CLAUDE.md, landed today):** stale >= 90d = DORMANT unless DECLARED exception; an
  exception declares its KIND (long-TTL-live vs closed-period-immutable); DORMANT IS NOT A
  DELETION WARRANT; successor-check before concluding.
- **NEVER#3:** moving served output = never-widen sign-off. **Migrate-before-kill**, always.
- **T-1/trading-calendar (NEVER#1):** no staleness reasoning on wall-clock.
- **Rule 24 taxonomy law:** your debt classification schema passes all four postulates AT
  AUTHORING TIME -- in particular (iv): if one remedy does not move every value on an axis, name
  which values do not move (the LIVE/DORMANT/DEAD x remedy map is exactly such an axis).
- **comp-iam under-reporting (Rule 22a):** an IAM grant absent from a trace is NOT unused --
  four measured blind axes; never mint deletion warrants from comp-iam output.
- **Retrieval controls:** every census prints its denominator; paginated `list-*` materialised,
  never `--query length()` per page; an ABSENT verdict carries a positive control.

## 4. RESEARCH QUESTIONS (the deliverable answers these)

1. **EVIDENCE LADDER:** Rank the available liveness-evidence classes by fidelity and cost, e.g.:
   deployed-FE read census (the D_00 method -- what the frontend ACTUALLY requests, line-cited) >
   router/Lambda deployed-config reads > CloudTrail data events / S3 server-access logs / Lambda
   invocation + CloudWatch metrics over a WINDOW > producer freshness > repo references >
   believed-state docs. For each: what it CAN prove, what it structurally CANNOT (its designed
   blind spot, per the instrument-domain doctrine), and its false-positive class from §2.
   **Key design question: what is the estate's best available "nothing reads this" instrument per
   resource class, and where none exists, what is the cheapest sufficient one to ENABLE
   temporarily during P5 (e.g. S3 server access logging on candidate prefixes for a bounded
   observation window) -- observation, not alerting.**
2. **THE NEGATIVE-EVIDENCE PROBLEM:** absence of observed reads over a window is the strongest
   practical evidence and still not proof (annual/quarterly consumers; the cma 1yr class). How
   long must the observation window be per cadence class, and which candidates can NEVER be
   proven dead by observation alone (requiring consumer-side enumeration instead)?
3. **CLASSIFICATION SCHEMA (Rule-24-conformant):** propose the debt taxonomy -- suggested axes:
   liveness state (LIVE / DORMANT-declared-exception / DORMANT-unexcepted / SUPERSEDED-by-named-
   successor / SOVEREIGN-RETIRED-still-serving / DEAD-no-consumer) x disposition (keep / migrate-
   then-kill / kill / permanent-exempt) -- with the state-coherence test run on it and every
   value's evidence requirement named.
4. **EVIDENCE CHAIN PER DISPOSITION:** what minimum evidence set authorizes each disposition,
   who attests it (lane / CVO cert / CTO / Andrew where served keys move), and what the
   PROOF_OF_SPEC instance for a P5 teardown TO looks like (the phase enum already carries
   P5-DECOMMISSION).
5. **THE ORDERING PROBLEM:** consumers-first-binary-last generalized -- propose the teardown
   dependency ordering rule (a thing is deletable only after everything that names it is gone or
   repointed, verified by search-FOR-the-name, not search-from-the-mechanism).
6. **INSTRUMENT FIT:** which existing comp-tools (comp-estate, comp-kuzu, comp-blast, comp-find,
   comp-freshness, the deploy ledger, the graph) cover which evidence classes TODAY; name the
   coverage gaps as DEFECTS (the tooling is foundational, not additive) -- but propose gap
   closures as gate candidates for routing, do not build.

## 5. INPUTS IN HAND (start here, cite rather than re-derive)

- The D_00 census artifacts (all three firms; ~B's cot census @17c8faa9f5 + router adjudication
  is the type specimen of the method at its best).
- The 19-channel disposition map (CRO decom spec); the SSOT recon matrix
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SSOT_RECON_MATRIX_20260811.md`).
- COO's 2026-08-11 dormancy census (denominators printed; the 4 flagged-not-concluded per-artifact
  calls are live test cases for your methodology).
- `memory/feedback_90_day_dormancy_default_with_declared_exceptions.md`; Rule 25; the phase
  framework doc.
- The estate-wide cert-basis inventory (bd hold path + cot override -- specimen of §2.6).

## 6. BOUNDARIES

Research + methodology spec ONLY. No deletions, no moves, no reclassification acts, no standing
detectors/monitors/alerts, no new S3 logging enabled yet (enabling is a P5-execution proposal
inside the spec, ruled at review). Egress: none needed; everything is estate-internal. Timeline:
P5 is the LAST phase -- this research runs parallel to P1-close/P2 and is not on their critical
path; quality beats speed.
