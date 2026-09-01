# CVO 2026-09-01 ~18:12Z -- I ran the admissibility gate I had written, and two claims in my own Andrew-agreed adjudication turned out to be false

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, SCRIBE

Delta since `session_close_1730-1900Z_...` @`6f9bf277f1`. Three commits, one law edit, one
broadcast to 9 seats.

⚠ **A DEFECT IN THAT PRIOR LOG'S OWN FILENAME, found by anchoring this one.** It is named
`session_close_1730-1900Z` and the measured time now is **2026-09-01T18:11:57Z** -- so it claimed a
window ending an hour in the FUTURE. **I typed the close time instead of deriving it.** Same class
as the banked "sprint display dates are DERIVED, never typed". No downstream consequence found
(nothing keys on that filename), but it is a false timestamp on the record and it is mine.

---

## 1. WHAT THE WINDOW WAS FOR

The AT-SELF gate carried in the handoff: *"per-tool compilation measurement for fork 1's
admissibility gate -- MUST PRECEDE admission."* The battery in the Andrew-agreed fork adjudication
was **proposed on two measured tools and six assumed ones.** Andrew then approved all nine
`/open-calls` recs and said *"get it done and spec whatever needs to be spec'd so CTO and COO can
get it incorporated."*

## 2. THE MEASUREMENT: 7 ADMITTED, 1 REFUSED

Two instruments, deliberately: SOURCE read of each resolved implementation file, plus LIVE
EXERCISE. **The exercise plane is the authority** -- the gate's predicate is about PRINTED OUTPUT,
and a docstring is the artifact describing itself. Every tool resolved by reading its SHIM, because
the previous attempt at this measurement mis-resolved `comp-similar` and its numbers were discarded.

```
  ADMIT   comp-blast      kuzu 27,107 nodes + worktree overlay; prints built: + age + BOTH Nessie
                          snapshot ids + per-table cadence
  ADMIT   comp-dataflow   parsed .py at working-tree HEAD; explicit VINTAGE: + COVERAGE + BLIND
  ADMIT   comp-schedule   "VIEW-TIME COMPILED; no artifact, nothing to go stale"
  ADMIT   comp-iam        395 .tf / 3 trees; declares plane + denominator + its own holes
  ADMIT   comp-trigger    live EventBridge/Scheduler; denominator + region
  ADMIT   comp-pipescript ast.parse x4 + glob/os.walk x10; REFUSES without --pipeline
  ADMIT   comp-denytest   live simulate; holds no corpus
  REFUSE  comp-similar    NO vintage, NO denominator, on EITHER carrier
```
`comp-similar --json` top-level keys are **exactly `['arn','neighbors']`** -- 40 neighbours out of an
unstated corpus, while reading the SAME kuzu corpus `comp-blast` prints a full provenance header
over. **Its self-test is 7/7 with genuinely discriminating controls. The tool is not weak, it is
UNDISCLOSED** -- and under a gate about disclosure that is the whole question. Routed to
`0.8.0_AE_CloudComp`; the remedy is emitting the header its sibling already emits.

## 3. TWO CLAIMS IN MY OWN ANDREW-AGREED DOC WERE FALSE

**Both inherited from prose and re-emitted as measured.** I wrote the battery table from tool
DESCRIPTIONS during the 106-tool scan and carried it into an adjudication Andrew agreed to without
opening two of the eight.

- **"the dependency graph EXPLICITLY CACHED ... any lens reading it must print the provenance
  vintage."** `comp-blast` **does not read that graph at all** (`cli.py:812`: *"the main path's
  universe is kuzu"*; its own banner: *"The old private trace universe (2,255 nodes) is retired"*),
  and it **already prints a richer vintage than my gate demanded.**
- **"`comp-iam` population is LAMBDA ENTRY POINTS ONLY."** Measured `Lambda 166 / EC2 21`. The real
  declared holes are **24 policy blocks NEVER SEEN** and **2 unparsed deny statements**, with the
  tool's own banner stating it **CANNOT answer "is this denied?"** -- covering NEVER#1's cross-firm
  Deny belts. **That is the bound a decomp must carry, and it is not the one I wrote down.**

⭐ **A near-miss worth recording.** I had a filed finding drafted -- *"`_emit_trace_provenance`
claims 'printed on EVERY walk' but has one caller, so comp-blast prints no vintage"* -- built
entirely from the source read. The exercise refuted it: comp-blast's vintage comes from a different
subsystem entirely. **A source read finds A reason; the run finds THE reason.**

## 4. BUILT ON THE APPROVALS

| commit | what |
|---|---|
| `5992cb125f` | the measurement record + the AS-BUILT steps 1-10 drawing + corrections in place at the head of the adjudication doc |
| `40bf270dec` | **cards 3 + 4**: the third admissibility limb and the step-3 fabric fork, both folded into the SAME choke point |
| `83a4561e53` | **card 5** the step-8 notifier, the CTO/COO incorporation spec, **card 9** the CLAUDE.md law edit, and the verbatim Andrew-direct record |

**Card 3** -- a preflight `RUN` now owes a denominator or an explicit blindness word on its own line.
**Card 4** -- `fabric: laptop|site-z` required on the project JSON; measured **0 of 349** carried any
fabric key before this. Both prospective only.

**Card 9 (LAW EDIT)** -- Rule 21 limb (i) DISCHARGED. Verified `--enumerate` by EXERCISE before
editing: it prints its denominator, bands hits, separates whole-value from substring, and WARNs when
every hit is a fragment -- **the false zero a bare `grep -c` hands you silently.** The expiry clause
fired exactly as it was written to.

## 5. THREE THINGS ANDREW NAMED THAT MY ADJUDICATION HAD MISSED

Found by re-reading the transcript in full rather than from my summary of it:
- **the step-3 fabric fork** -- I had marked step 3 "exists" and moved on. 0 of 349 carriers.
- **`/endpoint`** -- the skill EXISTS (instance TEN of "the estate already had it") but its phase 1
  reads TOs IN FLIGHT, so it cannot serve a pre-PRD ask. Andrew anticipated this: *"or a derivation
  of this skill."* **This is the keystone**: step 10's SCOPE-CHANGE limb is decided by "does the PRD
  name this OUTCOME?", and with no named endpoint that limb collapses into the spec-error limb.
- **`comp-adversary` spawns NO subagent and makes NO model call** -- `anthropic` 0, `Agent(` 0,
  `subagent` 0, `api_key` 0, `requests.post` 0. Andrew had weighed it as *"too operationally heavy"*
  on the belief it ran a parallel subagent. **The objection does not survive the measurement.**

## 6. Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-blast` | 4 | PASS | 3 refusal paths + 1 answer path; the answer path is what carried the provenance block |
| `comp-dataflow` | 1 | PASS | its BLIND/DENOMINATOR line is the specimen that justified the third limb |
| `comp-schedule` | 1 | PASS | self-declares VIEW-TIME COMPILED; found a DRIFT CANDIDATE it correctly refuses to close |
| `comp-iam` | 2 | PASS | the banner is the best-disclosed in the battery; refuted my own doc |
| `comp-trigger` | 1 | PASS | 140 rules + 18 schedules with region stated |
| `comp-similar` | 3 | **REFUSED** | 7/7 self-test, but no vintage/denominator on text OR json |
| `comp-pipescript` | 2 | PARTIAL | refused correctly without `--pipeline`; my `-p` guess was wrong |
| `comp-read --enumerate` | 1 | PASS | exercised as the precondition for the law edit, not after it |
| gate control harness | 12 | PASS | 6 preflight + 6 fabric, incl. the line-bleed control |
| watcher control harness | 13 | PASS | **caught 2 real bugs** |
| `bash -n` / `ast.parse` | 4 | PASS | every edit |

**What worked:** running the exercise plane *before* filing. It killed one finding of mine that was
fully drafted off a correct source read.
**What failed, and it was mine:** **`grep -c` PRINTS "0" AND RETURNS rc=1 on zero matches**, so
`grep -c ... || echo 0` emits BOTH and the count becomes `"0\n0"`. Every downstream `$(( ))` threw
and the zero-row case was broken. Caught by the shrink control, not by reading.
**Gap found:** `comp-similar` has no provenance header while its sibling over the same corpus does.

## 7. Blockers

**No CVO-owned blocker.** All three commits are LOCAL; push is integrator-only (LD-0367).
- `comp-similar` header -> `0.8.0_AE_CloudComp`. Blocks its admission only.
- `/endpoint --forward` -> `1.0.0_SA_CTO`. Specced, not built.
- **AT ANDREW, and it is the one to read:** **card 8 (D3-vs-D8) is NOT settled.** Its rec was the
  explicit non-recommendation *"no recommendation with confidence."* **Approving a
  non-recommendation authorizes nothing.** Card 6 likewise: the POSTURE is approved (nobody acts
  first), the underlying question is unruled.

## 8. Current State -- for a reader with ZERO context

- **PUSH STATE, MEASURED** (`ls-remote`, negative control `83a4561eZZ` refused correctly):
  `origin/CLOUD = 6f9bf277f1`; `5992cb125f`, `40bf270dec`, `83a4561e53` **ALL LOCAL**; 17 ahead.
- **THE GATE NOW REFUSES FOUR THINGS** on a newly-added `org/**/task_orders/*.md`: a registered
  project JSON, a `dep_stage` in the ratified enum, a `fabric` in `laptop|site-z`, and a
  `<preflight>` whose every `RUN` carries a denominator or blindness word on its own line. Override
  `# pipeline-override: <reason>`, audited. `--sweep` reports both axes: dep_stage **316/349
  ABSENT** (`BRIEF` x2 still off-enum, unowned), fabric **349/349 ABSENT**.
- **THE NOTIFIER IS LIVE-CAPABLE, NOT ARMED.** `org/surprise_channel/surprise-watch.sh <serial>
  {stream|once|status|reset}`. Baseline seeded: **18 files, 190 rows, 17 projects**. It is READ-ONLY
  on what it watches -- unlike `inbox-watch.sh`, whose mv-before-echo is what makes its orphan a
  thief. **An orphan of this one cannot steal.** Its state file is NOT an oracle for "CVO read it".
- **BROADCAST SENT**: msg 92413-92421, **9 DELIVERED / 0 QUEUED / 0 REFUSED**, carrying the law
  edit, the two new refusals, the battery result, both premise corrections, and the card-8 warning.
- **~12 inbound messages went UNPROCESSED this window by standing rule** (fabric work is default-off
  absent `/govern`). A CTO/COO exchange over the D2 stop-condition settled between them -- COO's own
  words: *"this needs no adjudication tonight."*

## 9. Next Steps

1. **[1.0.0_SA_CTO]** Build `/endpoint --forward` as a MODE on the existing skill. Set `fabric` on
   every newly registered project -- enforcing now.
2. **[2.0.0_SA_COO]** Adopt the preflight evidence form; place the verbatim step-7 trigger in every
   TO; give the flow-ingestion defect its OWN carrier, not D2.
3. **[3.0.0_SA_CVO]** Card 2's next build: mandate `spec_asserts`/`world_is` (step 7) and
   `route`/`loop_target` (step 10) on the row validators. **Census the readers of the 17 existing
   INVESTIGATION docs BEFORE the markdown-to-JSON container swap** -- the rows are already JSON;
   only the container is not, and I will not break 17 live documents to win a format argument.
4. **[3.0.0_SA_CVO]** Backfill today's findings into `ADVI_PERFRP/INVESTIGATION_v1.md` as S18+.
   Still owed from the previous window.
5. **[Andrew]** Card 8 (D3 vs D8) and card 6 (the 91668 ruling) remain open.
