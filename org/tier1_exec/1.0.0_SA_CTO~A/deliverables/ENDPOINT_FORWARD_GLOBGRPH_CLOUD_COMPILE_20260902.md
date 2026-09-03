# /endpoint --forward -- Cloud-Resident Graph Compilation + Gateway Traversal (step 2, PHASE 0)

**Seat:** `1.0.0_SA_CTO~A` -- **run:** 2026-09-02 ~17:2xZ, Andrew-direct at this terminal
(`/endpoint --forward globgraph-cloud-compile-and-gateway-traversal-20260901.md`; the file on disk is
spelled with the macro code, `globgrph-...`, and is the one and only match -- opened and confirmed to be
the CRO step-1 brief for this topic, not matched by name alone).

**Path taken:** GREENFIELD (F1-F5). Not a Step-F0 re-entry -- no remediation row, no existing PRD.

## F1 -- the brief

```
PATH       docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md
BYTES      27,974   LINES 403
GENERATED  no `generated` line. Header carries:
           "Step 1 of the canonical fabric loop . 4.0.0_SA_CRO . 2026-09-01 . mode NEW"
VINTAGE    @dfd24a010b  2026-09-01T19:49:44Z  (step-1 amend: CVO's F11 taken as a third argument)
           amended from @f6f2e41ce2  2026-09-01T19:45:01Z  (first landing)
PROJECT    NONE-YET (brief REFS block)        EXISTING PRD  NONE for this scope (brief REFS block)
```

## F2/F3 -- the ENDPOINT block, ready to paste

Paste the fenced block below VERBATIM into the step-4 PRD under the section titled exactly
`## ENDPOINT (step 2, /endpoint --forward)`, immediately after the PRD header and before `## 1. The arc`
(shape per `docs/architecture/_PRD_TEMPLATE.md` @b3584ea86a). `FWD-n` ids are PERMANENT and never reused.

```
## ENDPOINT (step 2, /endpoint --forward)

*Brief: docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md @dfd24a010b
(4.0.0_SA_CRO, 2026-09-01 19:49Z). Emitted by 1.0.0_SA_CTO~A 2026-09-02. FWD-n ids are
PERMANENT and never reused; a retired outcome leaves its number vacant.*

  FWD-1  Anyone can ask how the estate is wired and get an answer without ever
         building, refreshing or stitching the graph themselves
         DONE WHEN  EXERCISED -- someone who has never run a graph tool has asked
                    and been answered
         ACCEPT     a person who has never built the graph asks a question about
                    how things connect and gets the answer in the time an ordinary
                    lookup takes, with no step where they refresh or rebuild
                    anything first, and no wait they could blame on a build
         SOURCE     brief Part I O1; Part III bars 1 and 2

  FWD-2  The graph gets newer on the estate's own schedule -- nightly in full and
         within minutes of any cloud change -- never because someone asked
         DONE WHEN  EXERCISED -- the schedule has fired on its own at least once
                    and the next morning's answers carry that night's date
         ACCEPT     left completely alone overnight, the graph is newer in the
                    morning than it was the evening before; a change made in the
                    cloud during the day shows up without anyone asking for a
                    refresh; and no question anyone asks is ever the reason a
                    rebuild starts
         SOURCE     brief Part I O2; Part IV F1 (the nightly window already has
                    five members), F4 (nothing schedules the projection today), F10
         AMENDED    2026-09-02 in place, id unchanged (Andrew: "I agree with all
                    your recs", /open-calls CALL 1 rec (b)); the ratified 17:5xZ
                    text read "on the nightly clock"

  FWD-3  Anyone reading an answer can tell how old it is, from the answer itself,
         in plain words
         DONE WHEN  APPLIED -- the age is printed in plain language wherever an
                    answer is given
         ACCEPT     a reader who knows nothing about how the graph is built can
                    say from the answer alone "this is as of last night" (or
                    whenever it is), without looking up what any label means
         SOURCE     brief Part I O3; Part III bar 3

  FWD-4  There is a ceiling on how old any answer can be, and the ceiling belongs
         to the system, not to how carefully the reader checks
         DONE WHEN  EXERCISED -- a full cycle has passed with nobody enforcing the
                    ceiling by hand and no answer served older than it
         ACCEPT     nobody can be handed an answer older than the last scheduled
                    refresh, however careless they are about reading the fine
                    print; the oldest answer available is set by the schedule,
                    not by the reader's diligence
         SOURCE     brief Part I O3b; Part IV F11 (attributed to 3.0.0_SA_CVO,
                    msg 92472), F5 (answers served about a day and a half behind
                    on today's design)

  FWD-5  A new machine or a new person can ask graph questions on arrival,
         having never held or built the database
         DONE WHEN  EXERCISED -- a machine that has never held the graph has
                    asked and been answered
         ACCEPT     setting up a second computer adds a reader, not a build;
                    somebody on a fresh machine gets the same answer as everyone
                    else on their first try
         SOURCE     brief Part I O4; Part III bar 6; Part IV F9 (the P4
                    build-once-distribute ancestor)

  FWD-6  Nobody chooses a refresh mode
         DONE WHEN  APPLIED -- the full-versus-incremental choice no longer
                    appears anywhere an ordinary user works
         ACCEPT     there is no question a person can be asked, and no command
                    they can be told to type, about which kind of refresh to run;
                    someone who has never heard of the difference cannot make the
                    wrong choice, because there is no choice
         SOURCE     brief Part I O5; Part II (the ratified split becomes
                    invisible, not wrong)

  FWD-7  The estate keeps one graph story, and the per-machine copy is retired
         rather than kept alongside
         DONE WHEN  EXERCISED -- two people on different machines have asked the
                    same question at the same moment and received the same
                    answer, after the local copy was switched off
         ACCEPT     turning off every developer machine does not change what the
                    graph says; two people asking the same question at the same
                    moment get the same answer; and there is no second, older
                    copy anyone could still be reading from
         SOURCE     brief Part I O6; Part III bar 4; Part II boundary (a PORT
                    WITH A RETIREMENT, or a violation of the no-shadow-pipeline
                    rule); Part V item 3

  FWD-8  An operator can see that last night's refresh happened, and can see
         when it did not, without rerunning anything
         DONE WHEN  EXERCISED -- the answer has been read on a real morning, and
                    a night that did not run reads differently from one that did
         ACCEPT     an operator asking "did the graph refresh last night" gets a
                    plain yes or no with a time, and a missed night looks
                    different from a completed one; nobody has to run anything
                    to find out
         SOURCE     brief Part I O7; Part IV F6 (today's status surface points at
                    the wrong artifacts); Part VII item 3 (a rule being ENABLED
                    is not a run having happened)
         NOTE       brief Part V item 7: the MECHANISM behind this outcome sits
                    against the standing no-monitor moratorium (CLAUDE.md s.5).
                    The outcome is named here; the mechanism needs Andrew's
                    explicit word and must not be resolved by inference in a
                    decomp.

  NOT AN OUTCOME OF THIS PROJECT -- graph COVERAGE (whether every real thing in
  the estate is in the graph at all). Brief Part IV F12: a fresh graph that lacks
  a node is still silent about that node; coverage has a separate owner and a
  separate filed record (ADVI_PERFRP-S18 @3eb00f5905). A step-10 row citing
  coverage against any FWD above is misrouted, not a scope change.
```

**Outcome-to-brief map (every outcome traces to a brief line; nothing here was invented from the title):**

| id | brief outcome | bar | why that bar |
|---|---|---|---|
| FWD-1 | O1 | EXERCISED | real only when a never-compiled seat has actually been answered |
| FWD-2 | O2 | EXERCISED | a schedule that exists but has not fired is DESIRED wearing a rule |
| FWD-3 | O3 | APPLIED | legibility is real when built; nothing about it needs a run to be true |
| FWD-4 | O3b | EXERCISED | a bound is only shown to hold by a cycle passing without a hand on it |
| FWD-5 | O4 | EXERCISED | "graph-capable on arrival" is a claim about an arrival that happened |
| FWD-6 | O5 | APPLIED | the absence of a choice is a property of the surface as built |
| FWD-7 | O6 + Part V item 3 | EXERCISED | "one story" is testable only with two machines asking at once, after retirement |
| FWD-8 | O7 | EXERCISED | a run-confirmation surface nobody has read on a real morning proves nothing |

The retirement in FWD-7 is deliberate and stated in plain words (*"no second, older copy anyone could
still be reading from"*). Per the brief's Part II, a cloud graph that coexists indefinitely with the
local one IS the duplicate output path the NEVER rule forbids. If a later round finds that sentence
uncomfortable, the outcome is not obsolete -- the port is incomplete.

## F4 -- where it lands. NOT YET LANDED.

- **No PRD exists for this scope** (brief REFS: `EXISTING PRD NONE`). `docs/architecture/NFRA_GLOBGRPH_PRD.md`
  is the CLOSED-COMPLETE platform sibling (outline read; it carries no ENDPOINT section and is not this
  project's home -- the KUZUSPLIT O-3 precedent, Andrew-ratified 2026-07-17, is that a scoped follow-on gets a
  NEW project rather than reopening a closed platform record).
- **The project is not registered** (step 3). The block belongs at
  `docs/architecture/{PROJECT_CODE}_PRD.md` -> `## ENDPOINT (step 2, /endpoint --forward)`, first section
  after the header. Candidate code, a suggestion only: `NFRA_CLDGRPH`.
- **This file is the durable carrier until the PRD exists.** An endpoint that lives only in a terminal is the
  carrier problem the commissioning spec exists to close; committing this deliverable is the minimum act that
  makes it survive the session. It does not substitute for the PRD section.

## The brief's item (c), resolved on the record it named

**"Was NFRA_KUZUSPLIT O-4 ever ruled?" -- NOT SPECIFICALLY.**

```
RULING TEXT   2.0.0_SA_COO relay @c1eeaa102d, 2026-07-17 20:27Z (inbox 20260717T202755Z):
              "O-1 = YES ... O-2/O-3/O-4 proceed per PRD rec."
THE PRD REC   docs/architecture/NFRA_KUZUSPLIT_PRD.md @2ac7559bfd
                :104  O-3 carries "Rec: new project"
                :106  O-4 carries NO rec -- the bare fork "P4 build-once-distribute now, or defer"
                :86   P4 is labelled "(optional, two-machine payoff; ties to AGENTBUS)"
STATUS FIX    @2ac7559bfd (2026-07-17) marked O-3 RESOLVED and is SILENT on O-4.
```

So *"proceed per PRD rec"* landed on the one call that carried no rec. P4 was never built (brief F4: nothing
schedules or distributes the projection; that is a measured, carded fact). **O-4 is open in effect, and this
brief supersedes it with a wider ask** -- not "distribute the built file" but "take machines out of the
compile business". The step-4 PRD should record that supersession under Rulings-that-BIND rather than treat
P4 as a live sibling deliverable. Stated, not taken.

## Open for Andrew -- carried from the brief, not adjudicated here

| # | call | what this endpoint did about it |
|---|---|---|
| (a) | FWD-8's mechanism vs the no-monitor moratorium | outcome named; mechanism flagged in the block; needs the explicit word |
| (b) | does the query language survive the move (Cypher, or SQL over the engine already running) | FWD-1 written dialect-neutral on purpose so the endpoint does not pre-decide it; the fork is Part V item 1/2, for the PRD |
| (c) | was O-4 ruled | resolved above: not specifically; supersession is a step-3/4 ruling to record |

## F5 -- provenance

```
GROUNDED ON  the brief, read in full @dfd24a010b (27,974 B / 403 lines)
             docs/architecture/_PRD_TEMPLATE.md @b3584ea86a -- block shape + section title only
             docs/architecture/NFRA_KUZUSPLIT_PRD.md :84-90, :102-110 @2ac7559bfd via
               comp-read --enumerate 'O-4|P4\b' (4 hits / 113 lines / 32 sections) -- item (c) only
             comp-find 'KUZUSPLIT.{0,40}O-4|O-4.{0,40}KUZUSPLIT|build-once-distribute' --files --all
               20 hits / 144,899 files scanned (71,630 ephemeral-floor not searched) -- item (c) only
             inbox 20260717T202755Z (COO relay @c1eeaa102d) + 20260717T202040Z -- O-4 ruling text
             docs/architecture/NFRA_GLOBGRPH_PRD.md -- OUTLINE + header only, to confirm no ENDPOINT
               section and that it is the closed sibling
             docs/briefs/ANDREW_VOICE_MEMO_CANONICAL_FLOW_REMEDIATIONS_20260902.txt @3814be3317 --
               process-binding check only; it changes nothing at step 2
NOT READ     the TO register (to-check / query_project) -- refused per F1, even though sibling
               projects have TOs in flight
             any project JSON for this scope (none exists); org/projects/REGISTRY.md
             the NFRA_KUZUSPLIT task-order set; docs/architecture/NFRA_GLOBGRPH_ROADMAP.md
             the AWS plane, any timing, any artifact -- NOTHING was re-measured; every measured
               claim cited above is the brief's, at the brief's vintage (2026-09-01 19:15Z-19:45Z)
```

**NEXT (pipeline):** step 3 register (project code + JSON + REGISTRY row, CTO) -> step 4 PRD from
`_PRD_TEMPLATE.md` with this block pasted in -> COO decomp (step 5). Andrew reviews this output first
(voice memo 2026-09-02: *"I will review that output and we will kind of see where it needs to proceed from
there"*).

---

## ANDREW-DIRECT -- 2026-09-02 ~17:5xZ, at the `1.0.0_SA_CTO~A` terminal (recorded VERBATIM, same turn)

> "I agree with all of these only have one comment. First, I want to clarify that this is the kuzudb
> projection, and that every time you reference the "graph", that is what you are referring to. Secondly, I
> want to clarify the stitching/incremental refresh mechanism. For the Nessie/Iceberg graph, we have an SQS
> queue and associated lambda that manages the stitching, however, I want to understand how we manage this
> on the KuzuDB basis, if it can simply be downstream of this, which I think would be a simplified
> architecture. Let's discuss."

**Effect on the record (surfaced, not adjudicated wider or narrower):**

1. **FWD-1 .. FWD-8 RATIFIED AS WRITTEN** (*"I agree with all of these"*).
2. **SCOPE CLARIFICATION, binding on the step-4 PRD:** every occurrence of *"the graph"* in the ENDPOINT
   block means **the KuzuDB projection** -- the copy agents query (`infra/aws/globgrph/kuzu_nessie_db`, what
   `comp-kuzu` answers from) -- **not** the Nessie/Iceberg tables it is projected from, which stay where they
   are (brief Part II). When the block is pasted, add this gloss line to its preamble:
   *"'the graph' here means the KuzuDB projection -- the copy agents query -- not the Nessie/Iceberg tables it
   is projected from."* No outcome text changes; the referent is pinned.
3. **The refresh-mechanism question is OPEN for discussion.** Assessment below; the decision is Andrew's.

## ASSESSMENT -- can the KuzuDB projection simply sit downstream of the SQS/Lambda? (grounded 2026-09-02 17:3x-18:0xZ)

**Premise, corrected fairly.** The SQS queue + Lambda are the AWS-layer INCREMENTAL updater, not the stitch:
`opal-globgrph-incremental-events` (+ DLQ) -> `opal-globgrph-incremental-updater` (2-min debounce event-source
mapping, `infra/aws/terraform/globgrph/item2b.tf:175`; GLOBGRPH PRD s.2a Item-2b: CloudTrail -> bounded derive
-> Nessie commit). The STITCH is a different thing: `opal-stitch-produce` is a nightly CodeBuild (03:00Z) that
writes `stitch_graph.json` + its own artifact marker and **never touches Nessie** (`stitch-produce.tf:21,77`;
`derive_stitch.py:253` writes a file). Portal/pipeline-layer nodes reach the Nessie tables through the nightly
derive's producer fold (`derive_runner.py:2175` `ingest_graphuni_producers` -- "ONE derive -> ONE Nessie commit
+ ONE marker-advance", the NFRA_GRAPHUNI single-writer seam). So "downstream of the SQS/Lambda" would put the
projection downstream of ONE of at least five Nessie writers.

**The simplification is real, one level up.** Every writer to the Nessie graph -- nightly `derive_runner`,
the incremental Lambda, `cse_store`, `fedobs`, `resource_summaries` -- ends by stamping ONE object:
`s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json` (GLOBGRPH PRD s.2b F6 ruling; shared
`_provenance.stamp_marker` at `_provenance.py:194`; artifact-first-marker-last is the write-order contract).
Live marker at read time: `writer_id: incremental_updater`, `committed_at 2026-09-02T12:58:01Z`, per-table
`last_write_iso` populated for all four tables. **And the projection's own incremental engine ALREADY keys on
that marker**: `kuzu_incremental_refresh.py:64` reads the marker-pinned HEAD tables via pyiceberg from S3
(no Nessie REST, no Trino), diffs against the live DB, applies only the delta, count-guards, and falls back to
the full `kuzu_nessie_load` on a large delta (which is exactly what the nightly full derive produces).

**Recommended shape (CTO rec, not a ruling):**
```
  every Nessie writer ... -> PUT warehouse/_branch_head.main.json      (exists today; the commit point)
                              |  S3 event notification on that ONE key  (new; same pattern as item2b)
                              v
                      SQS opal-globgrph-projection-events (+DLQ)        (new)
                              |  event-source mapping, short batch window
                              v
                      projection worker = the existing kuzu_incremental_refresh logic
                        copy current -> apply delta -> count-guard -> (fallback: full load)
                        -> write Kuzu artifact + _build_manifest to S3 under a versioned key
                        -> advance ONE pointer object atomically (artifact first, pointer last)
                              |
                              v
                      serving plane (PRD fork, Part V item 1 -- NOT decided here):
                        a small always-on service on the existing opal-globgrph ECS cluster holding
                        the current artifact and swapping on pointer advance; the gateway (t4g.nano,
                        --workers 1, brief F7) is a THIN PROXY to it via the IntegrationSpec pattern,
                        never the host.
```
Why this and not the CloudTrail queue: one trigger covers every writer, present and future, with no
per-producer wiring; the projection can never run ahead of Nessie or from a half-committed state, because the
marker IS the commit point; and the engine that consumes it is already written and already certified
incremental-equals-full (`kuzu_incremental_refresh.reconcile`). The KUZUSPLIT `full`/`inc` split survives
intact but moves INSIDE the worker -- which is FWD-6 by construction.

**Measured, so the worker is sized against a number and not a feeling:** incremental updater over the last
24h (CloudWatch `/aws/lambda/opal-globgrph-incremental-updater`, filter `MARKER_STAMPED` / `REPORT`):
**45 marker stamps / 102 invocations**. Plus the nightly derive, cse, and the other producers: the worker
would fire on the order of 50 times a day, each an incremental apply the KUZUSPLIT PRD claims at seconds
(unverified here; P0-INSTRUMENT exists for it). Full-fallback duration is a DOCUMENT CLAIM (~6 min) and
decides Lambda-vs-ECS-task for the worker -- measure before choosing.

**One consequence for the ratified endpoint -- PROPOSED, not applied:** under this shape the projection
advances whenever Nessie advances (intraday as well as nightly), which satisfies FWD-2 and FWD-4 more
strongly than "nightly clock" states. Proposed in-place wording for FWD-2 (id unchanged): *"The graph gets
newer on the estate's own schedule -- nightly in full and within minutes of any cloud change -- never because
someone asked."* Andrew ratified the current text; changing it needs his word.

**What ports with the code:** the QUALIFIED verdict on `kuzu_nessie_load` (node/edge key asymmetry, brief F4)
-- fix at the port or carry it consciously. **What retires:** the local `kuzu_nessie_db` and the local
`comp-kuzu-full` / `comp-kuzu-inc` rebuild paths; `comp-kuzu` becomes a thin client (FWD-7's retirement).

**Prior art for FWD-8, found not chased:** NFRA_GLOBGRPH FRESHGUARD already designed the operator-facing
half. Leg 4 (writer wiring to the shared stamp) is an OPEN deploy-ledger entry HELD-SOVEREIGN-GATED since
2026-07-09 (`org/critical_paths/.open_deploys/freshguard-leg4-writer-wiring-finish.json`; L1-L3 closed, L4
verify open, "FAIL-BY-DESIGN standing state" declared 2026-08-20); leg 5 (per-producer freshness alarm) has
code at `infra/aws/globgrph/freshness_alarm/` but **no Lambda on the live plane** -- only two residual log
groups (`/aws/lambda/opal-globgrph-freshness-alarm`, `/aws/lambda/opal-globgrph-tool-activity-freshness`,
both LIVE-no-DECLARED). Andrew's word on FWD-8's mechanism is the same word FRESHGUARD is waiting on.

**Surprise channel (OBSERVATION class, INERT, to `3.0.0_SA_CVO`, not chased):**
- `warehouse/_branch_head.history/` is EMPTY (0 objects; positive control: the marker itself lists),
  although `_provenance._archive_superseded` (`:271`) says every overwrite archives the superseded marker
  first and REFUSES to overwrite without it. Either the CAS path that calls it is gated off, or the promise
  is not being kept; both mean the "what did the previous marker hold" question is currently un-evaluable.
- The FRESHGUARD leg-4 L4 criterion as ORIGINALLY written (per-table `last_write_iso` populated + writer_id)
  is observably TRUE on today's live marker; the entry's criterion was re-specced four times after, so this
  is an observation for the owner, not a closure.

---

## ANDREW-DIRECT #2 -- 2026-09-02 ~18:3xZ, same terminal, in reply to `/open-calls` (recorded VERBATIM, same turn)

> "I agree with all your recs. Just need to understnad the freshguard alarm and where it is interfacing as
> referenced in call 3."

**Rulings this lands (the three cards, recs as rendered at ~18:2xZ):**

| card | ruling | applied |
|---|---|---|
| CALL 1 | **FWD-2 = (b)**, widened in place, id unchanged | block above amended; `AMENDED` line carries the prior text |
| CALL 2 | **serving plane = (a)** a small ALWAYS-ON service on the existing `opal-globgrph` ECS cluster; the gateway is a thin proxy, never the host | PRD s.3 + s.6 (step 4) |
| CALL 3 | **FWD-8 mechanism = (a)** a PULL-style status surface only -- a read of the projection pointer's own manifest -- no alarm, SNS, checker or monitor; FRESHGUARD's alarm leg stays torn down on its own ruling | PRD s.6 (step 4) |

Decided in lane, stated to Andrew in the same output and not contested: the marker-downstream refresh shape
is the PRD's design; Cypher stays the query language; steps 3 and 4 proceed on this ratification.

**FRESHGUARD, answered on the record (what it is, where it interfaces, why it is not live):**
- **What it is:** NFRA_GLOBGRPH.FRESHGUARD, `0.7.0_AE_CloudOps` lanes, July 2026, five legs against one class of
  failure -- a graph surface that reads FRESH while its content is FROZEN (the `code_heat` nine-day
  stale-checkout incident; a `graph_edges` table 23h old under a minutes-old marker stamp).
- **Leg 4 -- per-table vintage IN THE MARKER (writer side, live).** Every Nessie writer stamps the one
  branch-head marker through the shared `_provenance.stamp_marker`, and the marker carries per-table
  `last_write_iso` so a stalled sole-writer shows as `graph_edges: STALE 23h` even under a fresh stamp.
  **This is the exact object the cloud projection consumes** (assessment above). Its deploy-ledger entry is
  HELD-SOVEREIGN-GATED only on its L4 verify criterion, re-specced four times; the field itself is populated
  on today's live marker for all four tables.
- **Leg 3 -- derive watchdog** (CloudWatch metric filter on `DERIVE_RUNNER_COMPLETE`, alarm on a 24h window,
  SNS) and **Leg 5 -- per-producer freshness alarm** (Lambda `opal-globgrph-freshness-alarm`: v1 served-object
  AGE per target; v2 PARITY-DRIFT, the served parquet's `repo_head_sha` vs live GitHub branch HEAD; metrics to
  `Opal/FreshnessAlarm`, one CloudWatch alarm per target, SNS) **were TORN DOWN 2026-07-17 @858554332d**
  (`freshness_alarm.tf` 404 lines, `freshguard_derive_watchdog.tf`, `tool_activity_freshness.tf`,
  `item2d_freeze_monitor.tf`; 44 destroys) **on Andrew's ruling (A) = remove ALL Class-A monitors** -- the
  kind that PAGES and does not REFUSE data -- relayed as CTO GO 235109Z: *"The correctness firebreaks we
  KEEP are the ones that REFUSE bad data ... a paging monitor is not one."* Re-arm = `git revert` of that
  commit. The two residual log groups on the live plane are what the census sees today.
- **Where it interfaces with THIS project:** (1) the marker leg is UPSTREAM of the projection worker and is
  the vintage the worker pins to; (2) the projection artifact + pointer on S3 would be a natural leg-5
  TARGET if that alarm class were ever re-armed -- **it is not, and CALL 3 (a) does not re-arm it**; (3)
  `comp-graph status` (brief F6, mis-pointed at legacy artifacts) is the operator-facing surface CALL 3 (a)
  repoints at the projection pointer's manifest -- a read, not a monitor.
- ⚠ CLAUDE.md s.5 cites `MDPF_DEBTCLEAN_PRD.md` s.11-12 for the moratorium; a word search of that file for
  "moratorium" returns 0 hits across 1,110 lines. The rule binds from CLAUDE.md regardless; the pointer is
  surfaced, not chased.

---

## ANDREW-DIRECT #3 -- 2026-09-02 ~19:3xZ, same terminal (recorded VERBATIM, same turn)

**The call put to him (one card):** *"Set `fabric` on org/projects/NFRA_CLDGRPH.json: (a) laptop, or (b) site-z?"*
-- rec (a). Context given: the step-6 gate's layer 3 refuses every TO against a project row with no `fabric`
key; `2.0.0_SA_COO` read his earlier 2026-09-02 word as "unfabricked projects are held deliberately" and did
not set it; this seat carried it rather than set it.

> "laptop"

**Effect on the record:** `org/projects/NFRA_CLDGRPH.json` gains `fabric: laptop` + `fabric_ruling` (verbatim +
this record's path); PRD v0.3 header gloss and s.7 note 3 updated; the `fabric` hold on step 6 is CLEARED. The
one remaining step-6 hold is `comp-adversary` admission RC5 PARTIAL (fabric-wide, `3.0.0_SA_CVO~A` @47f1045c7f),
not this project's. Broadcast to `0.0.0_AB_MSTR`, `2.0.0_SA_COO`, `1.0.0_SA_CTO` the same turn.

**Instruments this assessment used:** comp-read (`kuzu_incremental_refresh.py`, `kuzu_nessie_load.py`,
`_provenance.py`, `derive_runner.py`, `derive_stitch.py`, `item2b.tf`, `stitch-produce.tf`); comp-find
repo (`_branch_head` writers: 1,151 hits / 144,948 files) and `--corpus aws` (96 globgrph nodes / 2,100;
LAMBDA=1, SQS_QUEUE=2); live S3 read of the marker; CloudWatch `filter-log-events` 24h; deploy ledger read.
**NOT done:** no timing, no Lambda sizing, no network-reachability check, no serving-plane decision.
