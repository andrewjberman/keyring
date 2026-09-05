# comp-heat and the tooling at the outset of the Semantic Estate Pipeline -- L1 brief

**Author:** `4.0.0_SA_CRO` (L1, the only seat that briefs). **Date:** 2026-09-04, measured 12:55Z-13:50Z.
**Mode:** NEW (default). No project row exists for this work; `NFRA_COMPEFFICACY` is at ROUND_CLOSE and its
decomposition is spent (CTO 94163), so this is new work at L1 by Andrew's own route for new work.
**Commission, verbatim (Andrew, `/brief-create` at this terminal ~12:5xZ):** *"I would like you to make a brief
focused on the comp-heat tool and the trino analytics tooling, fedobs, all of that. the premise of this brief is that
we want to figure out how it works, why its not working currently, how to fix it, so that comp-heat can be a tool
agents use and that any comp-tooling at the start of the Semantic Estate Pipeline, of which there are several (and
convergence divergence aspects and combinations), all of which need to be analyzed, can be set in working order."*
**The earlier word this serves (Andrew at the CTO terminal ~09:5xZ, record @`26da5ec0fa`):** *"recs approved except
comp-heat, i want comp-heat to be figured out and developed properly"* -- and the standing condition on the pipeline
itself (LD-0522 Amendment 1, 2026-09-03 ~05:0xZ): the 26 PENDING estate-report days are deferred *"until we have the
comp-tool functions that feed that analysis 100% working and prioviding high signal data at the outset of the semantic
estate pipeline."* This brief is the carrier of that condition.

**HOW TO READ THIS.** Part I is the territory `/endpoint --forward` cuts outcomes from -- eight things a named person
can DO once this is done. Part II says what the work owns and what it only leans on. Part III is the bar, qualitative
and disputable. Part IV is what exists today, measured by this seat, with the one sentence per finding that changes
what the PRD has to buy. Part V names preconditions without ordering them. Part VI is a status snapshot with its
clock and is NOT outcome-bearing. Part VII is what this brief did not check.

---

## PART I -- THE OUTCOME TERRITORY

### O1. An agent answers a freshness question through the rail, bounded, at any grain
An agent at a terminal asks *"what is stale under this path"*, *"what have I written that is not committed"*, or
*"is this cold enough to archive"* by one `comp-heat` call -- and the answer states how much of the estate it looked
at, when the snapshot was taken, and stops inside a bound the caller gave it (Rule T), at the path grain the caller
named and not only the whole repo. Today the caller reaches for `git log` by hand, and the tool has no `--budget`.

### O2. An agent asks the LIVE estate a heat question in one call, without knowing Fargate exists
An agent asks *"which estate assets are hot in code and cold in the served graph"* (or the reverse) and gets a
joined answer from the Trino federation -- the iceberg graph catalogs x the git code-heat catalog -- carrying the
federation's vintage and the catalogs it joined, without hand-writing SQL and without knowing that a one-shot in-VPC
task ran to answer it. Today `comp-heat federated` does this and works (Part IV F2), but nobody has run it, nothing
documents that it exists (Part IV F3), and its answer carries no vintage.

### O3. A reader of the daily estate report traces every deterministic line to the tool that produced it
A reader of an estate report (Andrew at the sitting; the CVO adjudicating; any seat) can follow each deterministic
row -- a cold subtree, a co-moving pair, an undeployed change, a drifted resource -- to the comp-tool and vintage
that produced it, and re-run that tool to get the same row. Today the runner computes its own co-change, lifecycle
and census strata from a blobless clone and names the comp-tools only in a docstring (Part IV F7); nothing in the
report is re-runnable through the rail.

### O4. Andrew adjudicates a day whose proposals stand on high-signal tool evidence
At the sitting, each proposal cites the tool row it came from -- convergence or divergence between two resources,
co-evolution across producers, freshness, drift -- so a proposal is contested on its evidence rather than on whether
the pipeline saw the corpus. This is the outcome LD-0522 Amendment 1 waits on; when it holds, the deferral lifts on
evidence, not on assertion.

### O5. A seat reads the working order of every outset tool from one census, and a failed tool reads FAILED
Any seat can tell, for every comp-tool at the pipeline's outset (Part II names them), whether it is WORKING today --
rc, answer state, vintage, budget honoured -- from one census, and in the report a tool that could not answer says
so in its own voice with its denominator, never as an empty section that reads like a clean result.

### O6. A seat composes the outset tools without duplicating any of them
The LOCAL->GIT hop (`comp-heat drift`), the GIT->DEPLOY hop (`comp-pipescript deployed`, `comp-freshness`), the
co-evolution signal (fedobs), the pairwise CONVERGING / DIVERGING / PARALLEL read (`comp-heat compare`), and the
similarity and drift lenses (`comp-similar`, `comp-drift`/`comp-xray`) have ONE stated composition contract, and a
combination -- *"converging AND hot AND undeployed"* -- is expressible from it without a new tool and without a second
implementation of any leg.

### O7. comp-heat has a consumer that actually reaches it
A named consumer -- `comp-similar`'s heat weighting and the estate report's freshness stratum are the two that exist
in name today -- demonstrably reaches `comp-heat` and carries its output into the consumer's own artifact, shown by a
run, so the tool's "used by nothing" state ends with evidence rather than a wiring commit.

### O8. "What is safe to archive" is answerable through the rail, advisory-only, and never auto-acts
The heat engine's clustering, verify-before-recommend and hygiene-report legs (built 2026-06-25, unreachable from the
CLI today -- Part IV F5) are either reachable from `comp-heat` under the never-auto-delete doctrine, or explicitly
retired with the ruling cited -- so a seat gets a ranked, evidence-carrying archive-candidate list it can dispute,
and nothing is deleted by a tool.

---

## PART II -- WHERE THE BOUNDARY SITS

**This work OWNS:**
- `.tools/comp-heat` -- all five subcommands (`freshness`, `drift`, `score`, `compare`, `federated`), its budget,
  vintage and disclosure, its battery, and its reachability into the heat engine's O2-O4 legs (or their retirement).
- The caller contract of `.tools/_trino_fed.py` (the in-VPC run-task -> Trino REST -> CloudWatch transport) as
  comp-heat consumes it: what a caller must hold (IAM), what an answer must carry (vintage, catalogs, denominator).
- `comp-fedobs`'s consumer wiring -- the reader exists and is fresh; whether anything reads it is this work's.
- The COMPOSITION CONTRACT among the outset tools (O6) -- one document, one owner.
- The CONSUMPTION SEAM between the outset tools and the estate-report runner: that the runner consumes tool outputs
  (JSON with answer state, vintage, denominators) instead of re-deriving them (O3). The runner's own infrastructure
  is not owned here (below).
- The working-order CENSUS of the outset tools (O5), as an instrument that outlives this project.

**The outset tools this brief means -- the "several" in Andrew's sentence**, named from the FEDOBS PRD's five federated
observers plus the heat family and the reader over them: `comp-heat` (freshness / drift / compare; the git-history
heat engine), `comp-fedobs` (co-evolution, compiler-coverage, directive-effectiveness over the CSE log), `comp-drift`
(the local->git->cloud->nessie drift topology; kept-not-marquis), `comp-xray` (resource x-ray + temporal diff), `comp-similar`
(purpose-summary similarity; marquis), `comp-pipescript deployed` and `comp-freshness` (the GIT->DEPLOY hop),
`comp-blast` (propagation; marquis), and `comp-estate` (first contact for the Estate; marquis, usefulness gated on C(N)).
The "convergence / divergence aspects and combinations" are: `comp-heat compare`'s CONVERGING / DIVERGING / PARALLEL
verdict over two resources' per-window heat series; fedobs's co-evolution (co-sessions per subject pair); the runner's
own co-change stratum (GROUP B, a second implementation of the same idea -- F7); and any conjunction of these with
freshness and deploy state.

**This work RELIES ON, and does not build or move:**
- The Trino / Nessie / Iceberg serving plane on `opal-globgrph` -- `NFRA_CLDGRPH` (round 4 in flight under
  `2.0.0_SA_COO~A`) and `NFRA_GLOBGRPH` / `NFRA_GRAPHS`. Consumed as a query surface; never re-provisioned here.
- The fedobs PRODUCER (`fedobs_observe.py`, nightly 04:30Z, `NFRA_FEDOBS` complete) and the `code_heat` catalog's
  parquet (glue-bound; its refresh cadence is a Part V unknown).
- The estate-report RUNNER's infrastructure -- the EC2 box, the orchestrator, the manifest contract v2, the
  self-parking host, the `user_data` deploy trap (the ~B lane's, project W-15 / ESTATE_REPORT) -- and `/estate-pull`,
  which is the CVO's. This work changes what the runner CONSUMES, not how it boots or lands.
- The Kimi inferential stages (NARRATE / DETECT / AUTHOR) -- the AI half of the 2026-08-05 tool split. Out of scope
  entirely; the CTO's scope correction on the report's resource-vs-records axes (2026-08-06) binds the deterministic
  half and is inherited, not re-litigated.
- The engines behind `comp-drift`, `comp-xray`, `comp-similar`, `comp-blast`, `comp-pipescript` -- their own projects
  (`NFRA_COMPDRIFT`, `NFRA_COMPDIFF`, `NFRA_DEBTSCAN`, the graph projects). Consumed; not rebuilt.
- `NFRA_COMPEFFICACY`'s per-tool result schema (PRD s.4: identity, disclosure, answer state, bounds, battery) -- INHERITED
  as the bar every outset tool must meet; that project is not re-opened.
- The marquis list as ratified today (@`35c86c93e4`) -- comp-heat's place on it is downstream of it working and is not
  decided here.

**Siblings named:** `NFRA_COMPEFFICACY`, `NFRA_FEDOBS`, `NFRA_CLDGRPH`, `NFRA_GLOBGRPH`, `NFRA_COMPDRIFT`, `NFRA_COMPDIFF`,
`NFRA_DEBTSCAN`, `NFRA_EXPAND` Strand-C (`NFRA_HEATMAP_OBJECT`, no registry row), the ESTATE_REPORT pipeline (W-15),
`NFRA_MOTIF` and `NFRA_PROMOTE` (fedobs's downstream consumers, untouched).

---

## PART III -- THE QUALITATIVE BAR

No numbers are invented here. Each bar is disputable: who, what, and the alternative it displaces.

- **B1.** An agent answers a freshness or convergence question with a comp-heat call where today the same agent runs
  `git log` by hand -- observed in the rail log, not asserted.
- **B2.** A line in an estate report names the tool and vintage it came from, and a reader who doubts it re-runs that
  tool and gets the same row.
- **B3.** A tool that could not answer on a given day says so in the report in its own voice, and the day's manifest
  carries that failure -- never an empty section.
- **B4.** At the sitting, a proposal is contested on the evidence row it cites, not on whether the pipeline saw the
  corpus (the 2026-08-05 finding: the model had never seen the corpus).
- **B5.** No measurement exists twice: the runner does not carry a second implementation of what an outset tool
  computes, or where it must (the blobless host), the duplication is declared with the tool it stands in for.
- **B6.** A federated question is asked in the tool's vocabulary, not in SQL, and its answer says which catalogs it
  joined and when they were built.

---

## PART IV -- THE SUBSTRATE: what exists, measured

Each is a FINDING with its measurement. The one-line consequence for the PRD follows the dash.

### F1. comp-heat's local subcommands WORK today; "not working" is not a crash
`.tools/comp-heat` (415 lines, last @`a4b426e7ed` 2026-09-03, five subcommands). Run at this seat 13:0xZ:
`drift` rc 0 in 2 s (146 uncommitted writes, freshest first); `freshness .tools --json` rc 0 in 9 s (382 paths,
hot 99 / warm 36 / cold 247, the basis block and barriers in the output); `compare .tools/comp-heat .tools/comp-fedobs`
rc 0 in 2 s (VERDICT PARALLEL, six 14-day windows, denominators printed). Four answer states landed 2026-09-03
(T-20's result: identity, disclosure, `ANSWER-STATE:` token, `vintage.measured_at_utc` in JSON). -- The PRD buys no
engine; the local half is a wiring and bounding job.

### F2. `comp-heat federated` WORKS today, and the Trino plane is up
Run at this seat 13:2xZ: rc 0 in 86 s (the tool says "~3-4 min"); one in-VPC Fargate task; the answer is a heat-band
histogram joined across the iceberg graph catalog and the git code-heat catalog (cold 330 / warm 27 / hot 17 files,
avg scores). Live plane: ECS service `globgrph-trino` on cluster `opal-globgrph` ACTIVE, desired 1 / running 1,
task-def `globgrph-trino:6`; `trino.opal-globgrph.local:8080`; `glue_code_heat.tf` binds the code_heat catalog.
-- The federation is a working substrate, not a build; O2 is a consumer-and-disclosure job. The answer carries NO
vintage and NO catalog list today, and `--sql` runs an arbitrary federated query with no bound.

### F3. Nothing consumes comp-heat, and its federated plane was never enumerated
Usage: 0 CLI runs in 30 days (PRD v0.8 s.5a answer 7; not re-measured here). The only library consumer,
`comp-similar.load_heat_live`, returns `{}` before reaching it (S29, DISMISSED_WITH_REASON on the grading boundary,
not fixed). The estate-report runner names `comp-heat drift` in ONE docstring and ZERO code lines (comp-read
enumerate: 4 hits, 3 DOCSTRING / 1 COMMENT / 0 CODE over 2,333 lines). `NFRA_COMPEFFICACY` audited a tool it had not
fully enumerated: the round-6 answer named three subcommands; the file has five, and `federated` is in no cell.
`comp-which "what is comp-heat"` at this seat: NO CURATED RULE MATCHED (79 tools ranked, top score 0.36 =
comp-schedule) -- the router does not route heat questions, although the 2026-06-25 spec asked for the rows.
-- The PRD's first question is WHO READS IT; the wiring (O7), the router row (O1) and the enumeration (O2) are the work.

### F4. No budget anywhere; the one standing FAIL is at the source
T20-AC4 FAIL: `comp-heat freshness` with no path scores the whole repo and accepts no `--budget`; the CTO's read at
94163: 25 flag/def hits, zero budget, in 415 lines. The marquis ratification puts that FAIL "against comp-heat's own
development, not against the marquis clause." -- Rule T (`NFRA_COMPEFFICACY` PRD s.4.4) is inherited as a criterion, not
re-derived.

### F5. The heat FAMILY is five modules from 2026-06-25, and the CLI reaches two of them
`org/modules/heatmap/`: `heat_map.py` (S0 scoring), `object_freshness.py` (O1 engine; the one git pass -- DS),
`heatmap_object_emitter.py` (O1 producer on a cadence -- AE), `object_locality.py` (O2 subtree roll-up),
`object_recommend.py` (O3 verify-before-recommend, `git grep` inbound-reference check -> HOLD), `object_report.py`
(O4 hygiene report; AUDIT-TRAIL vs ORPHANED-ARCHIVE classes), `ms_heat_index.py` (S3, the MS write-heat index over
the MS graph slice, 2026-07-16). `comp-heat` exposes O1 (`freshness`, `drift`) and its own `score` / `compare` /
`federated`; O2-O4 and the emitter are reachable from nothing on the rail. -- O8 is a reachability decision (expose or
retire), not a build.

### F6. fedobs is LIVE, scheduled, and fresh -- and read by one reader that nothing reads
`comp-fedobs` at this seat 13:1xZ: SERVED vintage 2026-09-04T04:30:50Z, marker_head `8f28ad3a30`, source
`iceberg.globgrph.cse`; the co-evolution table lists portal subject pairs with co-session counts and the sessions
behind them (24, 13, 12, 11 ... co-sessions). The producer's rule `opal-globgrph-fedobs-producer-nightly` is ENABLED,
`cron(30 4 * * ? *)`. `NFRA_FEDOBS` reads `complete` in the registry; its PRD's P3 "reflective surface" is this
reader. Who consumes the signals: `NFRA_MOTIF` and `NFRA_PROMOTE` by the PRD's own "Feeds:" line -- neither wired to
the estate report. -- fedobs is an input that exists; the PRD decides where its co-evolution signal lands (O3, O6).

### F7. The estate-report runner RE-IMPLEMENTS the outset, from a blobless clone, and says so
`infra/aws/ec2/estate-report-runner/estate_report_runner.py` (2,333 lines): `capture_census` (deterministic, no AI),
`_stratum_cochange` (GROUP B: co-change at resource grain over 14 days "computed from git history METADATA"),
`_stratum_lifecycle` (GROUP C: cold subtrees "HONEST HALF-MEASURE, declared as one: the citation leg needs the estate
graph, which this host does not have"), `_stratum_propagation` (GROUP A: "DECLARED UNAVAILABLE ON THIS HOST ... the
ladder's instruments (comp-heat drift, comp-pipescript deployed, served-artifact md5, comp-freshness) require a
checked-out workspace with estate tooling; this runner works from a blobless no-checkout clone on a minimal box").
Sixteen `git` subprocess calls in CODE; zero comp-tool calls. -- The pipeline's outset is not the comp-tools today; it
is the runner's own census. O3 and O6 are one seam: either the tools' outputs reach the host as ARTIFACTS (the fedobs
pattern: a producer writes, the runner reads), or the runner is given a workspace it can run tools in. That choice is
the PRD's; this brief names both and picks neither.

### F8. The pipeline's frame, its condition, and its landing count
The Semantic Estate Pipeline is the daily ESTATE REPORT: 09:00 America/New_York window; orchestrator -> EC2 boot ->
run -> record -> self-park; deterministic census -> corpus -> Kimi NARRATE / DETECT / AUTHOR -> markdown -> manifest;
the CVO adjudicates with Andrew via `/estate-pull` (the AI proposes, Andrew ratifies, the CVO lands). Andrew's phrase
is his own (LD-0522 Amendment 1); the 2026-08-12 record renamed the Kimi Semantic Vertical Pipeline to the Kimi
Estate Pipeline. Landed adjudicated days at HEAD: 3 (`org/estate-reports/2026-08-09.md`, `-10`, `-20`); the CVO's
sitting packet (2026-09-04, in front of Andrew) carries 26 PENDING days -- the ones his word deferred. -- The
condition is measurable: the deferral lifts when O4 and O5 hold, and this brief's outcomes are what "100% working
and providing high signal data at the outset" means in gradable form.

### F9. Two structural findings on the pipeline's outset already on the record, inherited not re-derived
The 2026-08-05 tool split: tools versus the AI half (the finding of the day: the model had never seen the corpus --
computed, serialised, withheld by a truncation). The 2026-08-06 CTO scope correction: the report's single "resource"
axis served two intents (estate resources vs governance records) and failed Rule 24 on three of four postulates; the
correction puts records on their own axis. -- Both bind the deterministic half this brief owns.

### F10. The transport comp-heat federated uses is shared, and its caller needs IAM
`.tools/_trino_fed.py` (150 lines): `run_federated_query(sqls)` launches one in-VPC Fargate task that curls the Trino
REST API following `nextUri`, echoing pages to CloudWatch, polled 40 x 15 s; "Requires boto3 + AWS creds with
ecs:RunTask on the globgrph-trino task-def + logs:GetLogEvents". `trino_catalog_parity.py` (COMPDRIFT seam 6) reuses
it. -- Which seats hold that IAM (a worker subagent? the runner's role?) is a Part V precondition, not assumed.

### F11. What Andrew ratified this morning bounds the field
The marquis fourteen (@`35c86c93e4`): comp-find, comp-read, comp-which, comp-kuzu, comp-system, comp-pipescript,
comp-estate (gated on C(N)), comp-blast, comp-iam, comp-trigger, comp-adversary, comp-schedule, comp-similar, comp-pulse.
Kept, not marquis: comp-trace, comp-cache, comp-platinum, comp-dataflow, comp-drift, comp-denytest. comp-heat: "neither
retired nor kept-as-is -- to be figured out and developed properly, as new work." comp-xray and comp-fedobs appear on
neither list in that record. -- Their dispositions are the CVO draft v2's (@`c9785fb9e2`) and are not re-derived here
(Part VII).

### F12. The 2026-06-25 spec's intent, for the record the PRD will cite
comp-heat was specified as "the canonical surface over the NFRA_HEATMAP_OBJECT engine" answering the estate-cognition
questions ("what's stale / safe to archive?", "what have I written that isn't committed?", "is this code hot?") --
ADVISORY-ONLY, READ-ONLY, derived on demand from git (no persisted store), composing with `comp-pipescript deployed`
for the GIT->DEPLOY hop; with comp-which routing rows and a TOOLHUD nudge requested and, at this seat's read, never
landed (F3). -- The purpose was clear at birth; the consumer was never named. That is the question "figured out"
carries (CTO 94163 says the same).

---

## PART V -- WHAT MUST BE TRUE, without scoping it now

Named, not sequenced. Sequencing is L5.

- **P1.** The Trino service and the fedobs producer stay as they are (F2, F6); a change to either is a sibling's act.
- **P2.** A caller of the federated plane holds `ecs:RunTask` on the trino task-def and `logs:GetLogEvents` (F10) --
  which seats and roles do, and whether a v3 worker subagent or the estate-report host can, is unknown.
- **P3.** The `code_heat` parquet behind the federated join has a refresh cadence and an owner (unknown here); a
  federated answer's vintage must be that artifact's, not the query's clock.
- **P4.** Every outset tool meets `NFRA_COMPEFFICACY`'s result schema (identity, disclosure, four answer states, Rule T
  bound on any verdict-bearing rc, a battery with a RED mutant per arm) -- inherited as the bar.
- **P5.** The runner's consumption seam has one of two shapes (F7): tool outputs shipped as artifacts to the host, or a
  host that can run the tools. The choice constrains everything downstream and belongs to the PRD.
- **P6.** The Kimi half, the manifest contract v2, and `/estate-pull` are untouched; the CTO's two-axis correction (F9)
  is honoured by whatever the deterministic half emits.
- **P7.** The composition contract (O6) has a single carrier and an owner; `comp-heat`'s header already states one hop
  of it ("drift is LOCAL->GIT; the GIT->DEPLOY hop is comp-pipescript deployed + comp-freshness").
- **P8.** The never-auto-delete doctrine (NFRA_DEBTSCAN; comp-heat's own header) binds O8 absolutely.
- **P9.** A comp-which routing row exists for heat questions (F3), or agents will not find the tool however good it is.
- **P10.** The 26 PENDING days stay deferred until O4/O5 hold; nothing here adjudicates them.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured at this seat 2026-09-04 between 12:55Z and 13:50Z, at HEAD on CLOUD (LOCAL; origin/CLOUD @`351f309e0a` per
the CTO's ls-remote read at 12:40Z, not re-read here).

| what | state | clock |
|---|---|---|
| `.tools/comp-heat` | 415 lines @`a4b426e7ed`; five subcommands; `--help` rc 0 | 12:5xZ |
| `comp-heat drift` / `freshness --json` / `compare` | rc 0 / 0 / 0; 2 s / 9 s / 2 s; denominators present | 13:0xZ |
| `comp-heat federated` | rc 0 in 86 s; histogram over 374 files from Trino; no vintage line | 13:2xZ |
| ECS `globgrph-trino` | ACTIVE, desired 1 / running 1, task-def :6 | 13:2xZ |
| `comp-fedobs` | served vintage 2026-09-04T04:30:50Z; producer rule ENABLED cron(30 4 * * ? *) | 13:1xZ |
| comp-heat consumers | comp-similar returns `{}` before reaching it (S29); runner: 0 code refs; 0 CLI runs (PRD 5a) | record |
| comp-which routing for heat | NO CURATED RULE MATCHED | 12:5xZ |
| heat engine modules | 7 files under `org/modules/heatmap/`, last touched 2026-06-25 (S3 index 07-16) | HEAD |
| estate reports landed | 3 adjudicated days at HEAD; 26 PENDING in the CVO's sitting packet | HEAD / 05:4xZ |
| registry | `NFRA_FEDOBS` complete; `NFRA_COMPDRIFT`, `NFRA_COMPDIFF` complete; `NFRA_EXPAND` closed; no HEATMAP row | HEAD |
| `NFRA_COMPEFFICACY` | ROUND_CLOSE; 7 REALIZED / 3 NOT_EVALUATED; comp-heat's T20-AC4 FAIL stands against its own development | 13:3xZ |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It did not read the runner's 2,333 lines beyond their shape; the "re-implements the outset" finding (F7) rests on
  the strata's own docstrings and a subprocess census, which is strong but is not a line-by-line read.
- It did not measure the cost of one federated run (one Fargate task; dollars unknown) or the population behind the
  374-file histogram (which files the code_heat parquet covers, and when it was built -- P3).
- It did not verify which seats or roles hold the IAM the federated transport needs (P2).
- It did not re-measure comp-heat's usage; "0 CLI runs" is the PRD's number from the round.
- It did not re-derive comp-xray's or comp-fedobs's marquis disposition (F11); the draft v2 carries them.
- It did not open the Kimi half, the manifest contract, or `/estate-pull`'s adjudication loop beyond their stated
  contracts; nothing here changes them.
- It did not decide the consumption seam's shape (P5) or comp-heat's marquis standing; both are downstream.
- It did not run `comp-heat federated --sql` with an arbitrary query, `comp-drift`, `comp-xray` or `comp-similar` today;
  their working order is taken from `NFRA_COMPEFFICACY`'s round-6 results, not from this seat's runs.
- It deliberately did not fold in the two adjacent roll-up findings the CTO offered (comp-which F2: a non-existent
  gold id routed with confidence; comp-find F1: `--version` becomes a search pattern). Andrew said comp-heat and the
  outset tooling; those two belong to a tool-remediation pass and are named here so they are not lost.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/comp-heat-and-the-semantic-estate-pipeline-outset-tooling-brief-20260904.md
  PROJECT           NONE-YET
  EXISTING PRD      NONE (inherits the bar from org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md s.4;
                    the FEDOBS PRD docs/architecture/NFRA_FEDOBS_PRD.md is a sibling's, consumed)
  SIBLING PROJECTS  NFRA_COMPEFFICACY, NFRA_FEDOBS, NFRA_CLDGRPH, NFRA_GLOBGRPH, NFRA_COMPDRIFT, NFRA_COMPDIFF,
                    NFRA_DEBTSCAN, NFRA_EXPAND Strand-C (NFRA_HEATMAP_OBJECT, no row), ESTATE_REPORT (W-15),
                    NFRA_MOTIF, NFRA_PROMOTE
  PRIOR ART         .tools/comp-heat @a4b426e7ed; .tools/_trino_fed.py; .tools/comp-fedobs; org/modules/heatmap/* (S0, O1-O4,
                    S3); infra/aws/globgrph/fedobs/*; infra/aws/terraform/globgrph/{trino,fedobs_producer,glue_code_heat}.tf;
                    infra/aws/globgrph/trino_catalog_parity.py; infra/aws/ec2/estate-report-runner/estate_report_runner.py;
                    docs/briefs/comp-heat-tool-spec-for-cto-20260625.md; .claude/skills/estate-pull/SKILL.md
  RECORDS           Andrew-direct @26da5ec0fa (CTO) and @35c86c93e4 (CVO), 2026-09-04 ~09:5xZ; LD-0522 Amendment 1;
                    ANDREW_DIRECT_20260812_C4_DISSOLUTION_C3II_INFERENTIAL_KIMI_ESTATE_PIPELINE.md (CRO); the T-20 result
                    org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~I/comp-heat.result.md; rows S29, S31;
                    ESTATE_REPORT_SCOPE_CORRECTION_MEASURED_20260806.md (CTO); the 2026-08-05 tool-split log (CVO)
  MEASURED AT       2026-09-04 12:55Z-13:50Z (every Part VI row carries its own clock)
```
