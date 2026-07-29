# `comp-opalbizcluster` reroute — root cause, solution, and implementation recommendation

> **ANDREW-DIRECT RULING (2026-07-29 ~16:45Z, CVO terminal, VERBATIM — supersedes the name below
> and binds the build):** *"first of all, that tool should have a refresh function built in and a
> head with timestamp of its source very clearly depicted, it also should not be named pipescript
> it should be named comp-opalbizsem"*
> Three binding requirements onto the §6 plan: **(1) NAME = `comp-opalbizsem`** (updates this doc's
> `comp-opalbizcluster`; every reference below reads as opalbizsem). **(2) REFRESH FUNCTION BUILT
> IN** — the §5C reroute EXCEEDS this (the snapshot is eliminated; auto-refresh on HEAD-advance),
> but until steps 2-4 land, an interim `--refresh` that regenerates the resolver snapshot is the
> bridge; a frozen source with no refresh path is prohibited either way. **(3) SOURCE-TIMESTAMP
> HEAD, unmissable** — first line of every invocation's output states the source + its vintage
> (the current banner does this; the requirement makes it a CONTRACT, not a courtesy, and it
> survives the reroute as the kuzu provenance header). **Context that motivated the ruling: the
> 44-day frozen snapshot was serving the underscore TWIN as "primary served rollup LIVE fresh" —
> a stale estate map actively defends zombies. Renaming into the comp-* namespace also brings the
> tool inside the census glob + registration gate it structurally evaded (UNCLASSIFIED 4-of-89
> finding, 2026-07-29).**
>
> **SAME-DAY MEASURED CORROBORATION (COO 164052Z), attached by the recorder:** (a) the header
> already SAVED one answer today — COO hit the 44d snapshot on a routed question, and the vintage
> banner is the only reason it was re-verified instead of quoted: *"the failure mode the contract
> prevents is not a wrong answer — it is a CONFIDENT answer that nobody re-checks."* (b) The same
> contract already exists on the ARTIFACT plane (`_provenance.written_at/source_vintages`) and paid
> twice within one hour: it discriminated the publisher's 16:15Z run from a no-run when output
> bytes could not, and it exposed DT's whole-object-md5 acceptance oracle as spuriously breakable
> before it fired. CTO's generalization (163950Z: comp-tool-wide header contract) and COO's
> artifact-plane evidence converge on the general form: **anything that asserts freshness states
> its source and that source's vintage, unmissably.** (c) **CAVEAT, banked: read a self-stamp at
> ORIGIN, never through a CDN** — DT read the same field through CloudFront six minutes post-fire
> and got the PREVIOUS stamp: a false NO-FIRE on a leg that had fired. A self-stamp is only as good
> as the plane you read it from (Rule 22a on the layer axis); the same trap follows
> `comp-opalbizsem`'s header anywhere its output can be cached.

    author: 3.0.0_SA_CVO
    task:   Andrew-direct 2026-07-28 -- verify the kuzu blocker myself, then figure out a solution
            and recommend how to implement it. Not routed to CTO; he is on MDPF.
    all findings MEASURED against the live canonical graph (kuzu_nessie_db, 20,431 nodes /
    40,856 edges, built 2026-07-28T19:12Z, Nessie HEAD current) and the producer source.

---

## §1 CORRECTION FIRST — my own earlier finding was WRONG

I reported *"the graph models S3 at BUCKET granularity; there is no S3-key node type at all"* and
reframed the blocker as a **grain gap** requiring a new node type and ingest path.

**FALSE.** There are **232 `S3Key` nodes**. My predicate was
`node_type CONTAINS 'KEY'` — **case-sensitive**, against a type named **`S3Key`**. `'S3Key' CONTAINS
'KEY'` is false.

**Mechanism worth keeping:** my positive control passed (S3 buckets exist), my denominator was right
(58 distinct types), **and the FILTER was still wrong.** A control on the *retrieval* does not catch a
defect in the *predicate*. Had that reached CTO it would have mis-sized the work as far too expensive
to start. I caught it only because a traversal I ran for a different reason printed `S3Key` in edges I
had not asked about.

## §2 THE BLOCKER — TRUE, and narrower than the wrapper implies

    S3Key nodes total                                   232
    opal-data-inf                                        74
    opal-data-mdpf                                        4   <- incl. the OLD platinum key
    opal-data-portal-v2  (THE SERVING BUCKET)             0
    opal-data-assets     (THE MONOLITH)                   0

`pipescript`'s wrapper says the reroute is blocked because *"kuzu itself currently has no node for the
new key."* **Literally true.** But the shape is: **the key-level graph covers the OLD estate and not
the new one.** The two buckets that matter for MDPF today have **zero** key coverage.

## §3 ROOT CAUSE — the extractor's bucket vocabulary is a FIRM MAP

`infra/aws/globgrph/extract_gold_compute.py` produces `S3Key` nodes:

- **SOURCE:** the TraceGraph `.comp-graph/graph.json` — static analysis of **gold Python scripts**
- **BUCKET IS CONSTRUCTED, NOT OBSERVED:** node-id convention `"opal-data-<firm>/<key>"`, with
  `_FIRM = {black_diamond: bd, inf, mdpf, cot}` resolved from the script's repo path
  `data/<firm>/scripts` (`_firm_of_path`, `:36-38`)

> **`opal-data-assets` and `opal-data-portal-v2` can NEVER appear, because neither is a "firm."**
> The monolith consolidation changed the estate's bucket topology and the extractor still encodes the
> pre-consolidation one.

**This is the same root cause as everything else this session:** the estate migrated; the instrument
still models the pre-migration layout.

### And extending the firm map WOULD NOT FIX IT

**The new key's writer is the EC2 dispatch script — bash, S3-resident under
`s3://opal-data-mdpf/code/`, per Rule 12.** It is **not in the repo**, therefore not in the
TraceGraph, therefore invisible to a static gold-script extractor **no matter what bucket vocabulary
it is given.** This is the P2 runtime-provenance blind spot I documented this morning
(`@d4fee91bc`), now measurably biting the canonical graph — **the graph inherits `comp-clobber`'s
exact blindness because it uses the same primitive over the same source.**

## §4 THE JOIN THAT IS MISSING — the graph already has both halves

    SERVING SIDE  (current, correct)
      ServedURL  endpointurl:/api/general/mdpf/aggregate-aua-timeseries.json
        --SERVED_FROM--> S3_BUCKET_POLICY  opal-data-portal-v2      <- the RIGHT bucket
        --READS_URL-->   Endpoint          getMdpfAggregateAUATimeSeries
      ReactQueryKey rqk:mdpf-aggregate-timeseries
        --HAS_KEY-->     Hook  portal/src/pages/ModelPortfolios.tsx:378:useQuery

    PRODUCER SIDE (stale, pre-revamp)
      S3Key  opal-data-mdpf/platinum/mdpf/aggregate_aua_timeseries.json
        --WRITES_S3-->   PipelineScript  pipeline:mdpf:gold:build_aggregate_aua_timeseries

**NO EDGE JOINS THEM.** `SERVED_FROM` resolves to a **bucket policy** (bucket grain), never to a key.
A thread traversal therefore finds both halves and cannot connect them — and following the producer
side returns the stale platinum key. **That is exactly the failure that burned `pipescript` on
2026-07-23.**

## §5 SOLUTION — a LIVE-S3 producer for served keys, plus one edge

**Two changes. Neither is a schema redesign; the node type already exists.**

### (A) NEW PRODUCER — `extract_s3_served.py`, LIVE plane, bounded scope

Follows the **established producer-ingest pattern** (same shape as `extract_gold_compute.py`: emit a
producer-JSON delta, the single coordinated derive folds it in — **no parallel Nessie commit**).

    SOURCE      live S3 list_objects_v2 -- the plane itself, not a repo scan
    SCOPE       a DECLARED prefix registry, NOT all of S3 (that denominator is unbounded):
                  opal-data-portal-v2/json/**        (the serving surface)
                  opal-data-assets/platinum/**       (the monolith serve)
                  opal-data-assets/gold/**           (the monolith gold)
    NODE ID     `<bucket>/<key>` -- byte-converging with existing S3Key ids (the ~C convention
                already cited at extract_gold_compute.py:14, ruling 335edbd8f). NO new id scheme.
    OUTPUT      producers/graphuni/s3_served.json -> s3://...-globgrph/ -> derive folds

**Why LIVE and not an extended firm map:** the writer is outside the repo (§3). A live producer sees
the object regardless of who wrote it, in what language, from where. **It is immune to all three
blind spots at once** — the firm-map gap, the S3-resident-producer gap, and the
variable-interpolated-destination gap.

**In the classification schema landed today:** current ingest is `LIVE + derived`, denominator
`ENUMERATED` **from a hardcoded firm map**. The new producer is `LIVE + direct`, denominator
`ENUMERATED` **from S3 itself** — the denominator stops being an assumption.

### (B) ONE EDGE — `ServedURL --SERVED_FROM--> S3Key` at KEY grain

Today `SERVED_FROM` lands on `S3_BUCKET_POLICY`. Adding the key-grain target closes §4's gap and makes
the full chain traversable:

    Hook -> ReactQueryKey -> Endpoint -> ServedURL -> S3Key -> PipelineScript/producer -> S3_BUCKET

**That is the entire named-thread traversal `comp-opalbizcluster` exists to provide — live, from
canonical, with no frozen strings.**

### (C) Then the reroute is trivial

`comp-opalbizcluster` stops reading `estate-coverage-resolver.json` and issues the §5B traversal.
**The defect class disappears rather than being refreshed**: it no longer asserts key strings at all,
so it cannot assert a stale one. Its classification changes from
`PERSISTED + derived + MANUAL refresh + non-incremental` — **the worst profile in the taxonomy** — to
`PERSISTED + derived + auto-refresh-on-HEAD-advance`, inheriting the graph's provenance header.

## §6 IMPLEMENTATION ORDER — and what I can and cannot do

| # | step | owner | why |
|---|---|---|---|
| 1 | **Declare the served-prefix registry** | CVO (me) — it is a coverage denominator | this is the field I have spent the session establishing; it is a declaration, not code |
| 2 | `extract_s3_served.py` producer | **0.8.0_AE_CloudComp** or `0.7.0_AE_CloudOps` | `infra/aws/globgrph/**` is not my lane; I do not commit producers |
| 3 | `SERVED_FROM` key-grain edge in the derive | same | same lane |
| 4 | **VERIFY: the new key appears; the chain traverses end-to-end; the OLD key is still present and correctly labelled stale-or-superseded** | CVO (me) | I verify; I did not build it |
| 5 | rename + reroute `comp-opalbizcluster` | tool owner | gated on 1-4 |

**I am explicitly NOT doing steps 2-3.** Not because of scope-timidity — because a producer feeding
the canonical graph is exactly the artifact whose author must not also be its verifier, and I have
spent today proving why that separation pays. **Step 1 I can do now and it unblocks the rest.**

## §7 WHAT I WOULD VERIFY, stated in advance so it cannot be shaped to the result

1. **The new key appears as `S3Key` with the byte-converging id** — and the OLD key still appears
   (a producer that *replaces* rather than *adds* would silently delete history).
2. **The full chain traverses** Hook -> ... -> S3Key -> producer, live, for MDPF **and** for one
   non-MDPF thread (a single-thread pass would be a hand-chosen control).
3. **The denominator is declared and printed** — how many prefixes scanned, how many keys ingested.
   An unbounded S3 scan silently truncating is the failure mode this whole design guards against.
4. **A negative control:** a key that does NOT exist must NOT appear. A producer that ingests
   everything it globs is not discriminating.

## §8 LIMITS

- §3's root cause is **source-confirmed** (`extract_gold_compute.py:14-15, 36-38`). §4's missing edge
  is **measured** (the traversal returns both halves with no connecting edge). §5 is a **design
  proposal, not a measurement.**
- I did not measure how many OTHER served keys are missing beyond mdpf — `portal-v2` and
  `opal-data-assets` are at **zero**, so the answer is "all of them," but I have not enumerated the
  population that step 1's registry must cover. **That enumeration is step 1.**

— 3.0.0_SA_CVO
