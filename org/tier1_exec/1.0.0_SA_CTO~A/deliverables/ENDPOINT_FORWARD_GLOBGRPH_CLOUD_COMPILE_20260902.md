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

  FWD-2  The graph gets newer on the nightly clock, never because someone asked
         DONE WHEN  EXERCISED -- the schedule has fired on its own at least once
                    and the next morning's answers carry that night's date
         ACCEPT     left completely alone overnight, the graph is newer in the
                    morning than it was the evening before; and no question
                    anyone asks is ever the reason a rebuild starts
         SOURCE     brief Part I O2; Part IV F1 (the nightly window already has
                    five members), F4 (nothing schedules the projection today), F10

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
