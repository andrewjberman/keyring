# ANDREW-DIRECT RULING -- managed semantics: the daily semantic-evolution pipeline
**Channel:** 3.0.0_SA_CVO terminal, 2026-07-30 ~21:35Z. **Recorded verbatim per org/XXX.md
(the phrasing IS the ruling); broadcast same turn to MSTR + CTO + COO.**

## VERBATIM

> THe issue CTO is bringing up, which we're specing a fix for via RESOLVER_DEFROST_DESIGN.md
> (ee35d1c) is that we can never ever have dependencies on frozen maps. it is a cardinal rule not
> to do this. What is more nuanced that CTO is picking up on is the "Route B" (Ontology) error
> whereby the semantics are changing despite no change to the surface itself. There needs to be a
> way to manage semantics. What I think it should be, is that there is a daily scan based on
> activity in the Estate, what is changing, what commits are happening, that is analyzed/summarized
> by AI (i'd recommend using the Kimi API and K3). It's basically like an Exec Summary of goings on
> and in the process there is some prompt that effectively suggests potential semantic prose
> evolution for resources where things are shifting around. This is an automated process, likely a
> lambda with the kimi api structure on it (very similar to our BD API setup, really the exact same
> just differnet prompt attached instead of screenshots for captchas/otp) and that report is
> surfaced to a queue that is updated every day at 9a Eastern (9a regardless of daylight savings
> time). MSTR (base, no tilde) must have one of its rules be to surface that report and ask me for
> any changes ideas etc. and then MSTR adjusts the relevant items accordingly.

## PARSED DESIGN (CVO reading; the verbatim above wins on any divergence)

1. **CARDINAL RULE (doctrine-grade): never ever have dependencies on frozen maps.** Companion to
   the CTO fix being spec'd in RESOLVER_DEFROST_DESIGN.md @ee35d1c (commit cited by Andrew; not
   yet visible on this clone at record time -- verify at landing). Law-surface routing is CTO's.
2. **The Route B (Ontology) error, named:** semantics drift WITH NO CHANGE to the surface itself.
   View/runtime compilation (the serving law) cannot fix this layer -- semantic PROSE is
   hand-legislated by construction. What cannot be view-compiled must be ACTIVITY-REVIEWED:
   that is the design's core move.
3. **Mechanism:** daily Estate-activity scan (what is changing, what commits are happening) ->
   AI analysis/summary (Kimi API, K3 model) -> an Exec Summary of goings-on PLUS prompted
   suggestions of semantic-prose evolution for resources where things are shifting -> report
   surfaced to a queue, updated daily at 9a Eastern.
4. **Infrastructure shape:** a Lambda carrying the Kimi API structure -- clone of the existing
   BD API setup ("really the exact same, just different prompt instead of captcha/OTP
   screenshots"). Existing pattern homes: infra/aws/terraform/bd-49f-auto-login/ (the Kimi
   harness) + astn-pipeline (second live Kimi integration). Terraform-only deploy (Rule 1),
   scheduled (the ad-hoc/production rule: A PRODUCTION PIPELINE MUST HAVE A SCHEDULE).
5. **Schedule semantics -- INTERPRETATION FLAGGED:** "9a Eastern (9a regardless of daylight
   savings time)" read as WALL-CLOCK 09:00 America/New_York year-round (EventBridge Scheduler
   with a timezone-aware schedule, which handles DST natively -- NOT a fixed-UTC classic cron,
   which would drift an hour twice a year). If Andrew meant a fixed UTC offset instead, this one
   line is the correction point.
6. **MSTR standing rule (BASE serial, explicitly NO tilde):** surface the daily report to Andrew,
   solicit changes/ideas, then MSTR adjusts the relevant items accordingly. Human-in-the-loop is
   LOAD-BEARING: the pipeline SUGGESTS prose evolution; Andrew ratifies; MSTR lands. Semantic
   changes remain naming acts -- the AI proposes, legislation admits (the same emergence-vs-
   legislation posture as C3.ii).

## AUTHORIZATION NOTES (recorded so no future agent re-litigates)

- **Moratorium:** this daily scan/report/queue is Andrew-asked BY NAME (verbatim above) -- the
  2026-07-28 moratorium does not bite; the build carries the `# andrew-asked:` marker citing this
  record.
- **Vendor egress:** Kimi API/K3 for THIS pipeline is an Andrew-direct per-use designation
  (cloud-Lambda-scoped, the arxiv-precedent shape). Not a blanket Kimi lift.
- **Lanes:** CTO = spec (companion to RESOLVER_DEFROST_DESIGN.md); AE/CloudOps = Lambda +
  scheduler + queue build via Terraform; MSTR-base = its own standing-rule amendment; CVO =
  this record + verification at delivery.

## CONNECTION TO TODAY'S WORK (context for the spec author)

The Route B error is exactly what today's tactical patches touched: the census-vintage prose
defuse ("SNAPSHOT-CLAIMED fresh"), the frozen-digit purges, and the C3.ii fold were all
render-time or hand-pass corrections of semantic drift. This pipeline is the SYSTEMIC layer:
frozen STRUCTURE dependencies die via the defrost design; frozen SEMANTICS get a daily
activity-driven review loop with sovereign ratification.

-- 3.0.0_SA_CVO
