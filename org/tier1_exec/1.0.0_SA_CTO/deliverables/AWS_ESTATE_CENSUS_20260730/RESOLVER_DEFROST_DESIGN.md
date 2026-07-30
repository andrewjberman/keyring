# DEFROSTING THE THREAD MODEL — field-level split of the frozen census

**Andrew-direct 2026-07-30 ~21:3xZ, VERBATIM:** *"the simple solution is that graph B half that is
frozen, simply cannot be frozen. We need to identify what information that is providing and figure
out how to make it view-time/run-time compiled for that which can be assembled deterministically,
and then the prose aspects need to be assessed for stability and depending on that, we either have
some kind of recurring job for an agent and/or just stamp a date on that segment of the file
specifically, maybe its a .yaml with that in mind or something."*

**Canon backing:** this is not a new principle, it is the estate's OWN serving law being applied to
an artifact that escaped it — *"anything C3-or-below is NEVER served from a hand-written document —
a document about the computed layers is a map that will drift"*
(`C0_C1_C2_C3_C4_SYSTEM_LAYERS.md`). `estate-coverage-resolver.json` serves C3/C2/C1 content out of
a frozen file. The defrost brings it back under the law it already lives under.

## 1. What the frozen half actually provides — all 9 fields, classified

Source: `logs/2026-06-15/estate_census/pass1_inventory.json`, **113 threads**, joined per-thread by
`gen-estate-resolver.py`. Every field, and which side of the split it belongs on:

| # | Field | Kind | Verdict |
|---|---|---|---|
| 1 | `thread_id` | key | **KEY** — stays; it is the join column |
| 2 | `producers` | list of "name (type, trigger cron/event, role)" | **DETERMINISTIC** — this IS the trigger graph + lambda/EC2 census. Fully derivable from the fact graph + live AWS. It is also the field most likely to be WRONG when frozen, because triggers change |
| 3 | `served_artifacts` | list of `s3://...` keys (+ freshness adjectives) | **DETERMINISTIC (keys) + DERIVED-LIVE (freshness)** — keys from producer source/AST; freshness NEVER stored, always `comp-freshness` at call time. This is defect D1's home |
| 4 | `family` | thread -> C3.i grouping | **DETERMINISTIC** — union-find over shared constituents; the canon already says C2/C3 are DISCOVERED, never declared |
| 5 | `current_coverage` | which tool covers it | **DETERMINISTIC** — derivable from tool registration + coverage map; today it duplicates the manifest's `owning_tool` |
| 6 | `classification` (IN_SCOPE / …) | adjudication | **PROSE-STABLE** — a judgment, rarely changes; already duplicated as manifest `status` |
| 7 | `classification_reason` | one-line justification | **PROSE-STABLE** |
| 8 | `enrichment` | what the pipeline does to the data | **PROSE-STABLE** — semantic, slow-changing |
| 9 | `description` | the human "what this thread IS" | **PROSE-SEMI-STABLE** — the highest-value field in the whole artifact and the one Andrew's census is now producing better versions of |
| 10 | `frontend_resolution` | where it surfaces in the portal | **DETERMINISTIC-ISH** — derivable via comp-transform/comp-routes; CVO already ground-truths it separately as `reachability_status` |

**Headline: 5 of 10 are deterministically derivable TODAY from instruments that already exist**
(fact graph, comp-freshness, comp-routes, comp-transform, the trigger census). **4 are prose.**
**1 is a key.**

## 2. The split, and where each piece lives

```
                    RUN-TIME COMPILED (never stored)          STORED + DATED (prose)
                    -------------------------------          ----------------------
  producers      -> fact graph (CloudNode/CloudEdge)
  served keys    -> producer source (AST) + graph
  freshness      -> comp-freshness at call time                  description
  family/C3.i    -> union-find (canon: DISCOVERED)                enrichment
  coverage/tool  -> tool registration + coverage map              classification(+reason)
  frontend       -> comp-routes / comp-transform                  [each with its own
                                                                   last_reviewed + reviewer]
```

**Consequence:** the resolver stops being a JOIN OF TWO FILES and becomes **a prose layer + a
compile step**. There is then no frozen half to go stale, because the stale-able half no longer
exists as a file.

## 3. Per-field dating — Andrew's "stamp a date on that segment specifically"

The prose half becomes YAML **built for staleness visibility**, per thread:

```yaml
threads:
  bd-bronze-transactions:
    description:
      text: "Daily BD transaction download to bronze + silver parquet ..."
      last_reviewed: 2026-06-15
      reviewer: 3.0.0_SA_CVO
      stability: SEMI-STABLE        # STABLE | SEMI-STABLE | VOLATILE
    enrichment:
      text: "parquet conversion, CUSIP/ticker normalization"
      last_reviewed: 2026-06-15
      reviewer: 3.0.0_SA_CVO
      stability: STABLE
    classification:
      value: IN_SCOPE
      reason: "cloud-deploy AND pipeline consumer"
      last_reviewed: 2026-07-30
      reviewer: 3.0.0_SA_CVO
      stability: STABLE
```

**The rendering rule (this is what makes dating worth doing):** comp-estate prints a prose field
with its age, and **a field past its stability window renders with an explicit staleness marker** —
never silently. Same discipline CVO just applied to freshness adjectives: a claim carries its own
vintage, and over-warning is the safe direction.

**Stability windows (proposed, Andrew to set):** STABLE 180d · SEMI-STABLE 90d · VOLATILE 30d.

## 4. The recurring review job — scope it to what actually rotted

A blanket "re-review 113 threads" job dies of its own size. Scope it by SIGNAL:

**A thread's prose is queued for re-review when its COMPILED half changed** — new/removed producer,
changed trigger cadence, served key added or dropped, family membership moved, frontend
reachability flipped. That is computable, because the compiled half is now computed. A thread whose
facts did not move does not need its prose re-read.

Plus the flat expiry from §3 as a floor, so nothing rots silently even if its facts never move.

**Owner:** a scoped agent pass (CVO or a lane) over the QUEUE, not the corpus.

## 5. Migration order (safe, and honours the FREEZE)

The 07-24 record says **FREEZE, do not "fix" by regenerating** — because regenerating stamps fresh
mtimes over a frozen census and destroys `last_review`. This design does not violate that; it
retires the need for it:

1. **Extract prose to the dated YAML with `last_reviewed: 2026-06-15` and the ORIGINAL reviewer
   preserved.** No mtime lies: the date recorded is the date the content was actually reviewed.
   *(This is the step the freeze exists to protect, and it is satisfied by carrying the date across
   rather than restamping it.)*
2. **Build the compile step** for the 5 deterministic fields; run it BESIDE the frozen resolver and
   DIFF. The diff is a finding-rich artifact in its own right — every disagreement is 45 days of
   drift made visible, thread by thread.
3. **Cut over** once the diff is understood, not once it is empty (an empty diff would be
   suspicious).
4. **Retire** `estate-coverage-resolver.json` and the date-pinned census path from the generator.

**Andrew's decisions:** stability windows · whether `description` for a thread now carrying a
sovereign semantic note (72 storage resources + counting) should be SOURCED from this program's
notes rather than re-authored · who owns the review queue.
