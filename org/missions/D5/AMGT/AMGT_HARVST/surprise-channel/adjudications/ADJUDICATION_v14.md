# AMGT_HARVST ROUND 6 -- L8 COMPILE + L9 ADJUDICATION (SCOPED)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-26 ~03:1xZ
**Requested by:** `1.0.0_SA_CTO~Z` msg 25967, which offered *"if any of the three is better served by a
partial or scoped slug, say so and I will take it as scoped."* **This one is, and here is why.**

⛔ **THERE IS NO DRAIN-END PACKET FOR ROUND 6.** Measured: `comp-find --name '*DRAIN_END*'` over the project
returns **0 hits across 112 files scanned**, and the project has **no `2.0.0_SA_COO*` deliverables
directory at all**. So this compile reads the CHANNEL and the ORDER -- which is what the spine's L8 input
names ("new investigation rows and no others") -- and **NOT** an issuer's account of the drain.
⚠ **THE COST, STATED: any act the issuer took that is recorded neither in the order nor in the channel is
invisible to this compile.** That is the whole of what "scoped" means here; everything below is measured.

---

## 1. L7 -- RE-MEASURED

**1 of 1 terminal.** `TO-HVST-s-1` reads `closed` on its LAST `<status>` tag -- **deliberately `closed` and
not `complete`**, and `project.json` says so in its own words: *"both terminal to
`surprise-row-gate.py:152` TERMINAL_TO_WORDS, but `complete` would assert an endpoint the cell did not
reach."* The issuer was careful, and this slug carries that care forward rather than flattening it.

### ⛔ THE FINDING: THE ROUND'S CENTRAL ACT NEVER HAPPENED

`TO-HVST-s-1` carries 8 criteria. Two are not live:

| criterion | status, from the order's own tag |
|---|---|
| `AC1` | `superseded_by="AC1a+AC1b"`, `status="SUPERSEDED -- DO NOT RUN"` |
| **`AC1a`** | **`status="NOT_EXERCISED -- UNEXERCISABLE BY ANY SEAT (see AMENDMENT 2, section 8)"`** |

**`AC1a` IS the round's reason for existing** -- the ONE bounded vendor invocation that would retry sa's
listing capture (the order's s.4 bounds: *"sa ONLY. ONE invocation of the CAPTURE (`run`, AC1a) and ONE of
the UPLOADER (`upload-harvest`, AC1b). No loop, no second attempt"*). It was never exercised, and
amendment 2 records it as unexercisable by ANY seat.

⭐ **SO "1 of 1 TERMINAL" IS TRUE AND WOULD MISLEAD ON ITS OWN. TERMINAL IS NOT THE SAME AS ENDPOINT
REACHED**, and a round-6 analysis cut from the terminal count alone would read a completed retry where
there was none.

## 2. L9 -- THERE IS NO JUDGMENT CRITERION, AND I AM NOT INVENTING ONE

**0 of 8 criteria carry `judgment="true"`.** ⚠ A zero from a detector is worth nothing without a control,
so the same detector was run against `AMGT_RESAPP.TO-AMGT-rr-2` in the same pass: **criteria=4,
judgment=1.** The detector fires. HARVST round 6 genuinely has none.

**L9 is therefore VACUOUS for this round, and is recorded as vacuous rather than as a pass.** Where no
real run exists, the answer is NOT GRADEABLE -- never a criterion conjured to fill the slot.

## 3. L8 -- THE CHANNEL COMPILE

Through `_latest_dispositions`: **52 items, 14 files read, `unknown: []`** -- 19 GRADUATED,
21 DISMISSED_WITH_REASON, **12 NON-TERMINAL.**

### GRADUATED -- 9

- **`Z-S19` ... `Z-S26` (8 rows, `2.0.0_SA_COO~Y`, 2026-09-24).** A COMPLETED SELF-CORRECTION, and the
  best instrument work in this channel. ⭐ **`Z-S23` caught the census CONTAMINATING ITS OWN INPUT:** the
  seat wrote its census result into the same append-only channel the census reads, and *"17 open before the
  census row existed, 0 after -- on nothing but a list being published."* **`Z-S26` then retracted the
  whole count:** *"MY 17 WAS NEVER A COUNT OF LIVE WORK ... my census generated the entire live backlog it
  was trying to measure."* The chain reaches its own conclusion and needs nothing from this seat but the
  disposition. (`Z-S20` and `Z-S21` are substantive besides: the Halliburton misspelling is a OneDrive
  folder name the pipeline faithfully carries with the correct name already in the same record as prose in
  `resolution_reason` for 13 of 250 entries; and R-75's "second identity path" is a NAME-ENRICHMENT arm that
  hangs off canonical identity and so can never create it -- 0 of 59 unresolved entries carry a `cik`.)
- **`Z-W19-S1`** -- **DESIRED became APPLIED, verified in the order's own tags.** The row found that AC1's
  literal invocation crashes before any vendor call (`--security-json` wraps a JSON ARRAY in ANOTHER list,
  so `worker.run()` indexes a list with a string key and raises `TypeError` -- sa was never contacted). The
  order now carries `AC1 status="SUPERSEDED -- DO NOT RUN"` and `AC1a+AC1b` in its place. Acted on.

### CARRIED -- 3, each unremedied, each with its reason

| row | standing | why it is not closed |
|---|---|---|
| `Z-S27` | ARMED | The CLI's own `--harvest-grammar` help says **"writes"** for a flag that writes NOTHING to S3, and *"reads as authoritative because it is the tool describing itself."* The correct docstring sits three files away. A one-line fix nobody has taken -- and it asserts the exact belief that made round 6's first cut unpassable |
| `Z-W20-S1` | BLOCKING, ARMED | **This is WHY `AC1a` is unexercisable.** The producer's runtime root (session vault + local outbox) is DEVICE-LOCAL to the main workspace tree, which the order forbids touching and does not grant; `worker.py:152` asks `SessionManager.get('sa')`, the vault miss falls through to `refresh()`, and the act cannot be performed from a worker worktree at all. Structural and unremedied |
| `Z-S28` | BLOCKING, ARMED | The silver `listing_hit` writer cannot write ANY publisher payload carrying an empty dict: sa's `themes` is `{}` on all 20 rows, arrow types it `struct<>`, and parquet refuses a struct with no child field -- **so sa's captured listing pages cannot reach silver at all.** ⭐ *"wsj's payload has no such column, which is the only reason this never surfaced"* |

⛔ **`Z-S28` WAS FILED AT 2026-09-26T02:37:37Z -- 57 MINUTES AFTER msg 25967's "all orders terminal since
~22:32Z".** A slug cut from that snapshot would not carry it. This is the whole reason L8 re-measures
rather than adopts.

### ⭐ THE SHAPE ACROSS THE THREE CARRIED ROWS

They are ONE class at three independent layers: **the cell's own instrument could not reach its target.**
The CLI's help misdescribes what the flag does (`Z-S27`); the runtime root is device-local so the vendor
call cannot happen from a worktree at all (`Z-W20-S1`); and the silver writer refuses the payload's SHAPE
even if it could (`Z-S28`). **Round 6 did not fail to run -- it discovered its path was blocked at three
separate points, and only the last was found by running.** That is a decomposition finding, not a cell
failure, and it belongs at the top of the round-6 analysis.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 1 of 1 (`closed`). **MET**, with the AC1a qualifier above.
2. **Every channel row dispositioned** -- 12 of 12: 9 graduated, 3 carried with named reasons. **MET**
3. **Every judgment criterion graded** -- 0 of 0. **MET VACUOUSLY**, stated as vacuous.

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S20",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-26T03:15:00Z",
    "one_line": "L8+L9 round 6, SCOPED because NO drain-end packet exists (0 hits over 112 files, no COO deliverables dir). THE FINDING: the order is TERMINAL but its central criterion AC1a is NOT_EXERCISED and UNEXERCISABLE BY ANY SEAT, so the round's one bounded vendor act never happened -- terminal is not the same as endpoint reached, and a count of terminal orders alone would read a completed retry where there was none. L9 is VACUOUS: 0 of 8 criteria carry judgment=true, confirmed against a positive control. 12 rows dispositioned, 9 graduated and 3 carried, and the three carried rows are ONE class at three layers: the cell's instrument could not reach its target.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCOPE DECLARED AND MEASURED: comp-find --name '*DRAIN_END*' over org/missions/D5/AMGT/AMGT_HARVST returns 0 hits across 112 files scanned, and the project has no 2.0.0_SA_COO* deliverables directory. So this compile reads the CHANNEL and the ORDER -- what the spine's L8 input actually names -- and not an issuer's account of the drain. THE COST: any act the issuer took recorded neither in the order nor the channel is invisible here. 1.0.0_SA_CTO~Z msg 25967 expressly offered to take a scoped slug.",
        "L7 RE-MEASURED: TO-HVST-s-1 reads 'closed' on its LAST <status> tag, deliberately closed and not complete. project.json states the reason in its own words: both are terminal to surprise-row-gate.py:152 TERMINAL_TO_WORDS, but 'complete' would assert an endpoint the cell did not reach.",
        "THE FINDING, FROM THE ORDER'S OWN TAGS: of 8 criteria, AC1 carries superseded_by=\"AC1a+AC1b\" status=\"SUPERSEDED -- DO NOT RUN\", and AC1a carries status=\"NOT_EXERCISED -- UNEXERCISABLE BY ANY SEAT (see AMENDMENT 2, section 8)\". AC1a IS the round's reason for existing -- the order's s.4 bounds it as 'sa ONLY. ONE invocation of the CAPTURE (run, AC1a) and ONE of the UPLOADER (upload-harvest, AC1b). No loop, no second attempt.' The round's central act never happened, so '1 of 1 terminal' is true and would mislead alone.",
        "L9 IS VACUOUS AND IS RECORDED AS VACUOUS: 0 of 8 criteria carry judgment=\"true\". A zero from a detector is worth nothing without a control, so the same detector was run in the same pass against AMGT_RESAPP.TO-AMGT-rr-2 and returned criteria=4 judgment=1. The detector fires; HARVST round 6 genuinely has no judgment criterion, and none was conjured to fill the slot.",
        "L8 THROUGH THE RESOLVER: _latest_dispositions reads 52 items over 14 files, unknown [], 19 GRADUATED, 21 DISMISSED_WITH_REASON, 12 NON-TERMINAL.",
        "GRADUATED, 8 ROWS, THE 2026-09-24 SELF-CORRECTION CHAIN OF 2.0.0_SA_COO~Y (Z-S19 through Z-S26). Z-S23 caught the census CONTAMINATING ITS OWN INPUT -- the seat wrote its census result into the same append-only channel the census reads, and measured 17 open before that row existed and 0 after, on nothing but a list being published. Z-S26 then retracted the count entirely: 'MY 17 WAS NEVER A COUNT OF LIVE WORK ... my census generated the entire live backlog it was trying to measure.' The chain reaches its own conclusion. Z-S20 and Z-S21 are substantive besides: the Halliburton misspelling is a OneDrive FOLDER NAME the pipeline faithfully carries, with the correct company name already in the same record as prose in resolution_reason for 13 of 250 entries; and R-75's second identity path is a NAME-ENRICHMENT arm hanging off canonical identity, so it can never create identity -- 0 of 59 unresolved entries carry a cik.",
        "GRADUATED, Z-W19-S1: DESIRED became APPLIED and it is verifiable in the order's own tags. The row found AC1's literal invocation crashes before any vendor call, because --security-json wraps a JSON ARRAY file in ANOTHER list so worker.run() indexes a list with a string key and raises TypeError -- sa was never contacted. The order now carries AC1 as SUPERSEDED -- DO NOT RUN with AC1a+AC1b in its place.",
        "CARRIED, 3 ROWS, EACH UNREMEDIED. Z-S27 (ARMED): the CLI's own --harvest-grammar help says 'writes' for a flag that writes nothing to S3 and reads as authoritative because it is the tool describing itself, while the correct docstring sits three files away -- a one-line fix nobody has taken, asserting the exact belief that made round 6's first cut unpassable. Z-W20-S1 (BLOCKING, ARMED): the producer's runtime root, session vault plus local outbox, is DEVICE-LOCAL to the main workspace tree which the order forbids touching and does not grant, worker.py:152 asks SessionManager.get('sa') and the vault miss falls through to refresh() -- this is WHY AC1a is unexercisable, and it is structural. Z-S28 (BLOCKING, ARMED): the silver listing_hit writer cannot write any publisher payload carrying an empty dict, because sa's 'themes' is {} on all 20 rows, arrow types it struct<> and parquet refuses a struct with no child field, so sa's captured listing pages cannot reach silver at all -- and wsj's payload has no such column, which is the only reason this never surfaced.",
        "Z-S28 WAS FILED AT 2026-09-26T02:37:37Z, 57 MINUTES AFTER msg 25967's 'all orders terminal since ~22:32Z'. A slug cut from that snapshot would not carry a BLOCKING row that did not yet exist when the ask was written. This is precisely why L8 re-measures rather than adopts.",
        "THE SHAPE ACROSS THE THREE CARRIED ROWS: they are ONE class at three independent layers -- the cell's own instrument could not reach its target. The CLI's help misdescribes the flag (Z-S27), the runtime root is device-local so the vendor call cannot happen from a worktree (Z-W20-S1), and the silver writer refuses the payload's SHAPE even if it could (Z-S28). Round 6 did not fail to run; it discovered its path was blocked at three separate points, and only the last was found by running. That is a decomposition finding, not a cell failure."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S19",
      "AMGT_HARVST-Z-S20",
      "AMGT_HARVST-Z-S21",
      "AMGT_HARVST-Z-S22",
      "AMGT_HARVST-Z-S23",
      "AMGT_HARVST-Z-S24",
      "AMGT_HARVST-Z-S25",
      "AMGT_HARVST-Z-S26",
      "AMGT_HARVST-Z-W19-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "1.0.0_SA_CTO~Z msg 25967 asserts that AMGT_HARVST round 6 has been fully terminal since ~22:32Z with s-1 closed on the HVST-s-1 ruling, that its newest adjudication is from 09-23, and that the round blocks a CTO analysis and nothing else.",
    "world_is": "All true, and three things it does not carry. The order is terminal but its CENTRAL criterion AC1a is NOT_EXERCISED and unexercisable by any seat, so the retry the round exists for never happened. The round has NO judgment criterion, so L9 is vacuous rather than passed. And a BLOCKING ARMED row, Z-S28, was filed at 02:37:37Z -- 57 minutes after that message -- naming a live defect that stops sa's listing pages reaching silver entirely.",
    "notes": "FOR THE ROUND-6 ANALYSIS, three items. (1) THE DECOMPOSITION FINDING LEADS: three independent layers each block the same act, and only one of the three was discoverable by running the cell. A fourth attempt cut against the same path will find the same wall, so the next cut should establish WHERE the vendor act can legally run before it establishes what it should do. (2) Z-W20-S1 is the load-bearing one: a bounded vendor act whose runtime root is device-local to the main tree cannot be issued to a worker at all under Rule 14b's worktree discipline, which is a standing conflict between two rules rather than a defect in either. Andrew's word or an explicit grant is the only resolution and neither has been asked for. (3) Z-S27 is the cheapest fix in this channel -- a help string that says 'writes' about a flag that writes nothing -- and it has now misled at least one cut. THREE ROWS STAY CARRIED AND NONE IS CLOSED: an exposure closed by building the guard, not by nothing having gone wrong yet."
  }
]
```
