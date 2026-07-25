# NFRA_TOOLUNIFY — Status for External Review

**Author:** `1.0.0_SA_CTO~Z` · **Date:** 2026-07-25 · **Purpose:** a colleague-readable snapshot for feedback, not an internal governance record
**Full internal record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/CONSOLIDATED_ESTATE_MAP.md` (audit) + `REC1_EXERCISE.md` (post-census build)

---

## 1. What this project is

Opal's internal tooling (`comp-*`, ~92 tools) was built one-at-a-time against felt needs over several months, on top of a graph-database "estate" that models the company's cloud infrastructure, code, and (more recently) Microsoft 365 data. Nobody had a systematic inventory of: which tools exist, what they actually read, whether their declared behavior matches their real behavior, and whether the graph they're built on covers what it claims to cover.

**NFRA_TOOLUNIFY** is that inventory — an audit-first census, not a rebuild. It ran in five parallel workstreams over one session (2026-07-24), each independently re-derived against source and cross-verified by a second, independent reviewer before being accepted.

## 2. What the census found (audit complete, fully verified)

Two findings outrank the rest:

**(1) The graph store is 93% outside the vocabulary it nominally has.** Of ~20,400 nodes in the estate's graph, only 6.7% carry a type matching the governing 41-class vocabulary. This isn't neglect — the vocabulary was written for infrastructure objects (Lambda functions, S3 buckets, EventBridge rules), and the graph has since grown a second, much larger plane of code-level and M365 objects (functions, React components, files, folders) that vocabulary was never extended to cover. 6.8% is a naming mismatch (cheap fix — an alias table). The remaining 86.5% has no vocabulary authored for it at all.

**(2) Six independent instances, found in one night, of the same failure shape: a control that runs and produces a correct verdict, but that verdict never reaches anyone.** Examples: a data-pipeline health check has been failing every single night for 83 consecutive nights with zero people or systems noticing; an alerting queue has 476 unconsumed messages because the email subscription was never wired up; a freshness monitor exists in code but has no scheduled trigger and nothing calls it. We started this census looking for "which tools should we consolidate" and instead found a recurring, more urgent pattern: **correct instruments that are effectively silent.**

Every finding was independently re-derived from source by a second reviewer before being accepted — nothing here is on one agent's say-so.

## 3. What's happened since (in progress)

The census closed with three candidate next steps. Sequencing decision (mine, per direction): **start with the cheapest, highest-signal one — actually test whether tools behave the way their documentation claims, rather than just reading the code and inferring it.**

First result (small sample, 5 of the 92 tools, deliberately not a full sweep yet): fed real tools real bad inputs and watched what happened, instead of trusting their documented behavior. The standout case: a tool that correctly and loudly reports failure at its own boundary (exit code 2, explicit error) is invoked by exactly one automated process — and that process throws the tool's output away and always reports success regardless of the result. **The tool is not broken. The wiring around it silently swallows a correct alarm.** This is the same shape as census finding (2) above, one layer down — now demonstrated by direct exercise, not inferred from reading code.

A second, unrelated issue turned up by accident while committing this work: the automated hook meant to trigger that same health check doesn't even run in some of our current working environments, due to a hardcoded file path that doesn't resolve there. Confirmed independently across every agent session currently active (4 for 4). Not yet confirmed how widespread this is beyond that.

## 4. Open questions I need feedback on before going further

These are the real forks — I have a lean on some, but want a second opinion before committing either time or a written design to any of them:

1. **Scope of the project itself.** Do we keep this framed as "tool consolidation" (the original ask), or does finding #2 above (silent controls) deserve to become the primary program, with tool consolidation folded in as one workstream under it? My lean: the silent-controls finding is the more valuable thing this audit produced, and I don't want the project's name to undersell what it's actually surfacing.

2. **How far to take the "exercise, don't infer" pass.** We sampled 5 of 92 tools. Is a representative sample sufficient to act on, or does this need to become an exhaustive sweep before we trust the register? Cost/value tradeoff I don't have a strong instinct on yet.

3. **The vocabulary gap (86.5% of the graph undeclared).** Commit to authoring vocabulary for it, or is code-level/M365 data legitimately meant to sit outside this ontology by design? This is a real scoping decision with real authoring cost on the other side of it.

4. **Timing on writing a formal design doc.** The approach is now proven out (small-scale, but proven) — is it better to formalize into a PRD now while it's fresh, or keep iterating informally for another round or two first?

5. **What to do with the silent-controls findings themselves.** Several are now concretely actionable (the 83-night-silent pipeline, the un-alerted queue, the two newly-found path bugs). Do these get triaged as fixes now, or does fixing wait until the broader audit/design phase is more complete, to avoid picking at symptoms before the shape of the fix is settled?

6. **Sequencing against other planned work.** This project is explicitly being kept separate from a related, larger effort (extending this same graph/tooling system toward a more ambitious self-improving version) — that work is intentionally queued to start only after this one is in good enough shape to call done. What does "done enough" mean here — do we need a specific exit bar defined now, or is that a call to make when we're closer?

---

*This document is a plain-language summary for outside feedback. It intentionally omits internal process detail (who did what, verification mechanics, coordination structure) — available in the linked internal record if useful.*
