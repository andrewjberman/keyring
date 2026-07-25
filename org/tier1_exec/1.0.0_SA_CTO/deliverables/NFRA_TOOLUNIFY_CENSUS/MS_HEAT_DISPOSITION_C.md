# ms_heat Disposition Recommendation — leave-dormant-with-declared-status

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **RECOMMENDATION ONLY** — no schedule created, no
resource touched, per the dispatch's explicit constraint (standing no-new-alerts / no-proliferation
discipline). Decision + routing are CTO~Z's.
**grounding:** own census `C.md` §2 (source-read producer, live-measured S3 vintages, trigger sweep) —
facts re-cited below, not re-derived; nothing about the artifact changed between the census (07-24) and
this memo except one more day of dormancy.

---

## The facts that decide it (from C.md §2, all grounded there)

1. **What it is:** a write-recency heat index over MS_FILE/MS_FOLDER nodes of the ONE ingested SharePoint
   library — plain S3 JSON (`warehouse/ms_heat/ms_heat_index.json`) + an Iceberg sibling
   (`ms_heat_snap`). S2 metadata only; content/comms never read.
2. **Producer:** `org/modules/heatmap/ms_heat_index.py` — a bare, manually-invoked CLI. **Zero triggers
   anywhere** (derive_runner grep zero; no EventBridge/Lambda/ECS schedule; the 07-16 "born healthy"
   CloudWatch alarm no longer exists in live AWS). Its own docstring left cadence as an unresolved
   "sizing RAVC to COO/CTO" — the RAVC was never resolved.
3. **History:** exactly 3 runs, 2026-07-15/16/17 — the NFRA_MSGRAPH.S3 build-and-prove TO window — then
   nothing. Not "computing but failing to land" (pending-ingest dir checked empty); simply not run.
4. **Consumers: none.** The artifact's entire designed consumer — S4 `comp-ms-find`, the comp-which MS
   route that would ANSWER questions from this data — **was never built**. `comp-which` has zero curated
   MS route (live-checked in the census; incidentally re-confirmed by this batch's comp-which exercise).
   No tool, Lambda, portal surface, or report reads `ms_heat_index.json` or `ms_heat_snap` today.

## The three options, priced

- **RETIRE** (delete artifacts + script): wrong. The producer is proven-working, the build-and-prove
  investment is real, storage cost is a few MB of S3 JSON + an idle Iceberg table, and S4/S5 remain the
  declared (merely unbuilt) roadmap that would consume exactly this. Retiring buys ~nothing and re-costs
  the whole prove-out if S4 ever lands.
- **SCHEDULE**: wrong, and specifically the wrong lesson to apply. The "A PRODUCTION PIPELINE MUST HAVE A
  SCHEDULE" rule (CLAUDE.md) governs *production* pipelines — things whose output something consumes.
  ms_heat is not production; it has zero consumers. Scheduling a producer nobody reads would (a) create a
  new recurring compute + a new silent-failure surface the fabric must then watch, (b) violate the
  standing no-new-alerts/no-proliferation discipline, and (c) manufacture exactly the artifact class the
  estate keeps re-learning about: a thing that runs, lands, goes stale or breaks, and pages someone — for
  data nothing would miss. A schedule is justified by a consumer, never by the existence of a producer.
- **LEAVE-DORMANT-WITH-DECLARED-STATUS**: right. Keep the artifacts and script exactly as they are, and
  make the dormancy a *declared, findable fact* instead of an ambient stale timestamp.

## Recommendation

**Leave dormant, declare the status, bind revival to a consumer.** Concretely (all CTO~Z-routable, none
actioned by this lane):

1. **Declare DORMANT where a reader will look:** a status line in `org/projects/NFRA_MSGRAPH.json`
   (S3 shipped + proven; producer dormant by disposition, not by defect) and a one-line DORMANT-BY-DECISION
   note in `ms_heat_index.py`'s docstring replacing the unresolved cadence-RAVC language. The point is to
   pre-empt the false-outage class: a future census/monitor reading a months-old `LastModified` must find
   "dormant by decision <date, this memo>" — not conclude "broken pipeline," and not spend another lane's
   session re-deriving what C.md §2 already established.
2. **Revival condition, stated now:** the day S4 (`comp-ms-find`) or any other real consumer lands,
   ms_heat becomes a production input — and at THAT moment the schedule rule applies in full force (a
   consumer-bearing pipeline with no schedule is a defect). Scheduling is then mandatory, sized by the
   deferred cadence RAVC. Until then there is nothing to be stale *of*.
3. **Do not silently fold this into the alarm estate:** the vanished 07-16 CloudWatch alarm should not be
   recreated for a dormant artifact (no-new-alerts); its disappearance is already recorded in C.md.

One asymmetry worth naming: dormant-undeclared and dormant-declared cost the same to keep — the entire
difference is whether the next reader burns a session on it. That is why the recommendation is the third
option and not the cheaper-looking "do nothing": *nothing* is what the artifact is already doing; the
deliverable here is the declaration.
