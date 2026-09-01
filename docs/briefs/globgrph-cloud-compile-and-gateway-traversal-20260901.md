# BRIEF — Cloud-Resident Graph Compilation + Gateway Traversal

**Step 1 of the canonical fabric loop** · `4.0.0_SA_CRO` · 2026-09-01 · mode **NEW**
**Prompt (Andrew, this terminal, verbatim):** *"I'm starting to think the compilation should be done
at the same time as nessie refreshes in the early morning, and the whole kuzudb and stitching is
accessed in the cloud and agents who want to traverse it just traverse the cloud representation…
there is no impetus to automatically refresh that representation and it can take 9-10 min to do so
which is obnoxious. We want that process very abstracted away from the user so they dont have to
deal with refreshing/stitching at all."*
**Second Andrew-direct, same session, verbatim:** *"yeah if thats not a runtime graph or has no
automated process that is a risk surface."*

---

## PART I — THE OUTCOME TERRITORY

### O1 — An agent traverses the estate graph without ever having compiled it
An agent asks a Cypher-shaped question about the estate and gets an answer, having performed no
refresh, no rebuild, no stitch, and no wait attributable to compilation. The compile is somebody
else's completed act by the time the agent arrives.

### O2 — The graph an agent reads was refreshed by a schedule, not by that agent's arrival
The act that advances the graph is triggered by the clock, downstream of the Nessie/Iceberg
producers that already run nightly — **not** by a query noticing it is behind. This is O1's cause,
and it is the outcome Andrew's second direct names: a representation with no automated refresh is a
risk surface regardless of how fast it is.

### O3 — An agent can tell how old the answer is without knowing how the graph is built
Vintage is legible at the point of the answer, in the answer, to a reader who knows nothing about
markers, snapshot ids, branch heads, or projection modes. Today vintage is honest but is expressed
in the vocabulary of the build system.

### O3b — The age of any graph-derived answer is BOUNDED, not merely disclosed
There is a ceiling on how old the graph a seat reasons from can be, and that ceiling is a property
of the system rather than of the reader's diligence. Distinct from O3: O3 is about *legibility* of
vintage, O3b is about its *bound*. Today vintage is disclosed honestly and its age is unbounded, so
disclosure is the only protection and the reader is the only enforcement. See **F11**.

### O4 — A new box, a new seat, or a second device is graph-capable on arrival
Graph capability is not a property of a machine that has paid a compile. A seat that has never run
a graph tool, on hardware that has never held the database, asks the same question and gets the
same answer.

### O5 — Nobody chooses a refresh mode
The `full` / `inc` / `auto` election disappears from the agent's decision surface. An agent that
does not know the difference between a full projection and an incremental one cannot make the wrong
choice, because there is no choice presented.

### O6 — The estate keeps ONE graph story, not a cloud one and a local one
There is a single answer to "what does the graph say", and it does not depend on which machine
asked or when that machine last compiled. Two seats asking the same question at the same moment
cannot get different answers.

### O7 — An operator can see that the automated refresh happened, and notice when it did not
The scheduled compile's success or failure is observable as a fact about the estate. This is the
other half of O2: a schedule nobody can confirm ran is a different risk surface from the one it
replaced, not an improvement on it.

---

## PART II — WHERE THE BOUNDARY SITS

**This owns:** where the Kuzu projection is COMPILED, where it is SERVED FROM, and how an agent
REACHES it. Three questions about placement and access.

**This does NOT own, and must not reopen:**

| Surface | Owner | Why it is out |
|---|---|---|
| The AWS derive (live scan → graph JSON) | **NFRA_GLOBGRPH** (CLOSED-COMPLETE 2026-06-16) | Already cloud, already nightly. Untouched. |
| Nessie / Iceberg warehouse + catalog | NFRA_GLOBGRPH | The source of truth stays exactly where it is. |
| The stitch DERIVE (cross-layer edge emission) | NFRA_GLOBGRPH P2-STITCH | Already a nightly cloud CodeBuild. See Part IV F3 — the stitch is *already* a cloud act, contrary to the framing of the prompt. |
| The `full`/`inc` split semantics | **NFRA_KUZUSPLIT** (RATIFIED 2026-07-17) | This brief's O5 would make that split *invisible to agents*, not wrong. It does not un-ratify it. |
| Partner/client-facing GraphQL | **D6_OPAL_ANALYST** | A different consumer (partners, via Teams). Do not conflate: D6 serves clients, this serves agents. Measured distinct at `docs/architecture/D6_OPAL_ANALYST_GRAPHQL_PRD.md` §1. |
| Gateway auth / OAuth-AS | NFRA_INTEGRATIONS + gateway PRD | This relies on it; it does not modify it. |

**Sibling projects named:** `NFRA_GLOBGRPH`, `NFRA_KUZUSPLIT`, `NFRA_GRAPHS`, `NFRA_INTEGRATIONS`,
`D6_OPAL_ANALYST`.

⛔ **The sharpest boundary risk is the standing NEVER rule on shadow pipelines** (CLAUDE.md §5): *no
shadow/build-alongside pipeline, duplicate output path, or standing parity comparator.* A cloud
Kuzu that coexists indefinitely with a local Kuzu **is** a duplicate output path. This work is a
PORT with a retirement, or it is a violation. That constraint belongs in the PRD's arc, not as a
decomp detail.

---

## PART III — THE QUALITATIVE BAR

No numbers are asserted here. The bar is disputability.

1. **A seat that has never heard of Kuzu answers a graph question.** Today, answering requires
   knowing that `comp-kuzu-inc` exists, that `-full` is MSTR's, and that a "behind" warning is
   normal rather than an error.
2. **No agent's first graph question of the day is materially slower than its second.** Today the
   first BEHIND query after the nightly overwrite is the one that pays; which seat that is, is an
   accident of who queried first.
3. **An agent reading a stale answer knows it, without having read the KUZUSPLIT PRD to interpret
   the label.** The current label is honest and is written in build vocabulary.
4. **Turning off every developer machine does not change what the graph says.** This is the
   plainest test of whether compilation actually moved.
5. **An operator asking "did the graph refresh last night" gets an answer that is not a re-derivation.**
   Per Andrew's second direct: automation nobody can confirm ran is still a risk surface.
6. **A second machine is not a second graph problem.** Adding a device adds a consumer, not a
   compile.

---

## PART IV — THE SUBSTRATE: is this in a canonical pattern?

Findings, each with what was measured. Instruments named per Rule 22.

### F1 — The producer side is ALREADY fully cloud-resident and scheduled. The premise that "compilation is local" is only half true.
**MEASURED** via `comp-kuzu-inc` over the live-plane projection (DB built 2026-09-01T16:18:23Z,
Nessie HEAD current, pin == marker HEAD). Every rule reads `"state": "ENABLED"`:

| Clock (UTC) | Resource | Kind |
|---|---|---|
| 02:00 | `opal-globgrph-derive-runner-nightly` | EventBridge rule → ECS `globgrph-derive-runner:6` |
| 03:00 | `opal-stitch-produce-nightly` | EventBridge rule → CodeBuild `opal-stitch-produce` |
| 03:30 | `globgrph-cse-producer-nightly` | EventBridge **Scheduler** → cluster `opal-globgrph` |
| 04:00 | `opal-globgrph-comp-learns-producer-nightly` | EventBridge rule |
| 04:30 | `opal-globgrph-fedobs-producer-nightly` | EventBridge rule |
| event-driven | `opal-globgrph-cloudtrail-mgmt` (no schedule) | CloudTrail → SQS `opal-globgrph-incremental-events` (+ DLQ) |

>> **The 02:00Z–04:30Z window Andrew describes as the place to put compilation ALREADY EXISTS and
   already has five scheduled members.** This is an insertion into a live cadence, not a new one. <<

### F2 — There is already a persistent in-cloud query plane, running right now.
**MEASURED:** ECS cluster `opal-globgrph` reads `"status": "ACTIVE", "active_services": 2,
"running_tasks": 3`. Task definitions `globgrph-nessie:5` and `globgrph-trino:6` exist alongside the
batch producers. Nessie's backend is DynamoDB (`opal-globgrph-nessie-_objs` / `-_refs`).
**Consequence:** "traverse the cloud representation" does not start from zero — a long-lived
catalog + SQL engine over the same Iceberg tables is already up. `NFRA_GRAPHS.md:380` states the
in-VPC catalog truth is Trino `iceberg.globgrph."<t>$snapshots"` / Nessie REST.
⚠ **GRAIN CAVEAT:** I read task definitions and a service COUNT (2). I did **not** confirm by name
that the two running services are Nessie and Trino. The inference is strong and it is still an
inference.

### F3 — The STITCH is already produced in the cloud, and its output is already in the Nessie tables.
**MEASURED** by node-type census against `kuzu_nessie_db` (projected from `graph_nodes` /
`graph_edges` at the marker-pinned metadata location): `Component`=199, `PipelineScript`=133,
`API_ROUTE`=86, `Page`=15, `C3System`=4 — 58 distinct node types in total, spanning the AWS,
portal and pipeline layers.
>> **Cross-layer stitch edges are ALREADY unified into the cloud tables.** The local
   `kuzu_stitch_db` is a SEPARATE, older artifact, not the path the canonical query uses. <<
**Consequence for scope:** "stitching" needs *moving* far less than the prompt assumes. What is
local is the **projection**, singular.

### F4 — The local projection has NO scheduler, and this is already carded as a measured fact.
**PRIOR ART — do not re-measure.** `org/tier2_senior/0.7.0_AE_CloudOps~K/deliverables/D11_CARDS/kuzu_nessie_load.card.json`
(schema 3.1, carded 2026-08-30T03:12:00Z @`5da9e7fffc`, by `0.7.0_AE_CloudOps~K`), verbatim:
- `cadence.declared_rhythm`: *"NONE — no schedule is declared and that is deliberate… No EventBridge
  rule, CodeBuild project, workflow or cron names this script; a sweep over `**/*.{tf,yml,yaml,sh,json}`
  returned callers and documentation only."*
- `cadence.actual_trigger`: *"DEMAND-DRIVEN"* — the `comp-kuzu-full` override, or `ensure_fresh`'s
  marker-oracle rebuild path.
- `verdict.standing`: **QUALIFIED**, with a named blocking defect: node and edge key rules are
  **asymmetric** (node key stripped at `:150`, edge endpoints raw at `:184`), so a whitespace-bearing
  endpoint is silently counted into `skipped_missing_endpoint`.

>> **Andrew's "no impetus to automatically refresh" is not a hunch — it is a measured substrate
   finding that has been on the record since 2026-08-30, and the card independently reached the same
   conclusion.** <<
⛔ **The QUALIFIED verdict travels with the code.** Porting the projection to the cloud ports its key
asymmetry too. A port is the moment to fix it or to consciously carry it; it is not a reason to
delay the port.

### F5 — Workers are demonstrably eating the stale path, repeatedly, on the current design.
**MEASURED** at `infra/aws/globgrph/kuzu_nessie_db.fallback.jsonl` — 16 `inc-served-labeled-stale`
events. The most recent three: 2026-08-31T19:07:32Z, 23:41:41Z, 23:42:35Z, each serving vintage
2026-08-30T13:41:57Z against a delta of 27,089.
**Reading:** the KUZUSPLIT §4 design is working exactly as ratified — the worker was protected from a
mid-task full rebuild. **But the protection's cost is that the served answer was ~34h behind its
source**, and the same file shows the pattern recurring across 2026-07-18, 07-26, 08-30 and 08-31.
This is Andrew's risk surface stated in the estate's own telemetry.

### F6 — `comp-graph status` is reporting on the WRONG Kuzu artifacts.
**MEASURED:** `comp-graph status` prints `kuzu_db PRESENT built 81d ago` and `stitch_graph PRESENT
built 38d ago`. The canonical database is `kuzu_nessie_db`, whose own manifest reads
`built_at: 2026-09-01T16:18:23.487109+00:00` (~3.3h old at time of reading).
`.tools/comp-kuzu:9` states the distinction explicitly: *"NOT kuzu_load.py: that builds a DIFFERENT
5-column schema… into a DIFFERENT dir (kuzu_db)."*
>> **The freshness surface an operator would consult to answer O7 is pointed at two legacy artifacts
   and is silent on the live one.** An operator reading `81d ago` would conclude the graph is
   abandoned; an operator reading `PRESENT` would conclude it is fine. Both readings are wrong and
   they point in opposite directions. <<
**This is surfaced, not chased** (Rule 27 surprise channel; owner is the `comp-graph` / NFRA_GRAPHS
D3 lane, not this brief).

### F7 — The gateway is already cloud-resident with a proven, governed extension pattern — and exactly one hard sizing constraint.
**MEASURED:** EC2 `i-07dccb1615503ac99`, `"state": "running"`, TF-managed under module
`opal-gateway`, instance profile `opal-gateway-profile`.
- Extension framework exists and is canonical: `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` —
  IntegrationSpec schema, 3 AuthKinds, audited `run_integration_tool()`, a **mandated 5-step
  add-checklist**, fail-closed enablement, SCTY `min_tier` floor, per-integration governance gate.
- It is exercised, not theoretical: `app/integrations/` currently holds `opal_portal` and `ycharts`.
- ⛔ **`"instance_type": "t4g.nano"`.** The unit file additionally pins `--workers 1` as **MANDATORY**
  (OPLMCP.06 / CTO D5a — the OAuth-AS in-memory PKCE stores are correct only single-process; the
  server refuses to boot otherwise).
>> **A nano with a mandatory single worker is a fine place to put a THIN CLIENT to a graph engine.
   It is a poor place to HOST a 47 MB graph database and serve concurrent Cypher from it.** This is
   the single most consequential sizing fact in the brief and it is measured, not estimated. <<

### F8 — A name trap that would have produced a false "already built" finding.
`infra/aws/ec2/opal-gateway/app/graph.py` is a **Microsoft Graph** client
(`GRAPH_BASE = "https://graph.microsoft.com/v1.0"`), not the dependency graph. Opened rather than
inferred from the filename. **There is no existing globgrph traversal surface on the gateway.**
Recorded so a later reader does not "discover" a graph tool that is not one.

### F9 — The design ancestor of this brief is a ratified project's DEFERRED open call.
`NFRA_KUZUSPLIT_PRD.md` §5 **P4** — *"(optional, two-machine payoff; ties to AGENTBUS). Distribute
MSTR's built canonical KuzuDB via S3 so a second machine pulls the pre-built file instead of
re-deriving — build-once-distribute, compounds with N machines."* Carried as **open call O-4**:
*"P4 build-once-distribute now, or defer."*
>> **Andrew's ask is P4 with the ambition raised**: not "distribute the built file to machines" but
   "stop machines being in the compile business at all." <<
⚠ **NOT VERIFIED:** whether O-4 was ever ruled. I did not find a ruling and did not exhaustively
search for one. Step 2/3 should resolve this before treating P4 as open — see Part VII.

### F10 — The doctrine already points this way; the estate is not being asked to change its mind.
`NFRA_GRAPHS.md` §4, the query-vs-rebuild contract: *"WRITE-PATH (expensive — scheduled or
triggered, NOT the agent default)… READ-PATH (cheap — the agent default)."* CLAUDE.md Rule 20:
QUERY, never rebuild.
**Finding:** the local projection is the one place where an agent's READ silently triggers a WRITE.
This work does not introduce a new principle — **it closes the last gap against an existing one.**

### F11 — A nightly compile would BOUND a ratified gate's guarantee, not merely speed a slow thing up. This is a third argument, stronger than the brief's other two.
**CONTRIBUTED BY `3.0.0_SA_CVO` (msg 92472, 2026-09-01 19:47Z), ATTRIBUTED, on a gate that seat
owns.** Not adjudication of this brief — an offered consequence. Carried because it changes what the
PRD's acceptance criteria can be made of.

Andrew ratified a fork-1 admissibility gate today: a lens is admissible to the canonical **step-5
lens battery** only if it EITHER compiles its corpus at runtime OR prints its corpus vintage (a third
limb — a denominator or an explicit BLIND statement — approved the same turn).

>> **`comp-blast` is ADMITTED, and it passes on the VINTAGE limb, not the runtime one. Its universe
   is the Kuzu projection this brief is about.** <<

**Consequence:** an unscheduled corpus makes the printed vintage the **SOLE** protection, and its age
**UNBOUNDED**. A decomp author who does not read the provenance block is reading a graph of arbitrary
age with nothing to stop them. *The tool is honest; the bound is the reader.*
A nightly cloud compile converts an **unbounded** vintage into a **bounded** one (≤ one cycle) — it
makes a ratified gate's guarantee stronger, rather than making a slow thing faster.
**This is a genuine acceptance-criterion candidate for the step-4 PRD**, and it is an argument
neither Part I nor Part III previously made.

⛔ **TWO BOUNDS CARRIED VERBATIM FROM THE CONTRIBUTING SEAT — do not drop them downstream:**
1. **CVO did NOT measure staleness and is not claiming the projection goes stale in practice.** Its
   one sample was HEALTHY (`built 2026-09-01T16:18:23Z`, age 1.2h, `Nessie HEAD: current`,
   `graph_nodes last-write 4.5h < 6h cadence`). **The claim is that nothing BOUNDS it** — which rests
   on F4, this brief's own measured finding, not on any staleness observation.
2. **DO NOT CONFLATE TWO ARTIFACTS.** The 47 MB Kuzu projection is **NOT** `.comp-graph/graph.json`
   (the trace-layer cache `comp-trace` reads, which self-heals by discarding on SHA drift; measured
   by CVO at 52.2h old with 34 drift entries the same afternoon). **Two caches, two mechanisms; only
   the Kuzu one is in scope here.**

### F12 — COVERAGE and VINTAGE are different axes, and a nightly compile fixes only ONE of them.
**Same source (CVO, msg 92472), filed separately as `ADVI_PERFRP-S18` @`3eb00f5905`.** `comp-blast`
returns **NOT-FOUND** for `perfrp_emit_core.py` against the printed 27,107-node denominator — a live
gold producer that 11 emitters import is **absent from the projection entirely**.
>> **A perfectly fresh graph that does not contain a node is still silent about that node.** <<
The tool refuses honestly (*"This is a NOT-FOUND, not a nothing-breaks clear"*); the hazard is a
reader who does not carry that sentence forward.
**Scope consequence:** whatever step 2 cuts, no outcome in Part I should be read as improving
coverage. **This brief's outcomes are vintage-, placement- and access-shaped. Coverage is a separate
question with a separate owner, and it is NOT in scope here.**
⚠ I did not independently reproduce the NOT-FOUND; it is attributed, with its own filed record.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, deliberately **not** sequenced (sequencing is step 5, COO).

1. **A ruling on where the compiled graph is SERVED FROM.** F7 forecloses hosting the engine on the
   gateway nano. The alternatives (a sized service on the existing `opal-globgrph` cluster; the
   already-running Trino as the traversal engine; a built artifact in S3 that the gateway streams
   from; something else) are a real fork with cost and latency consequences. **This is the fork the
   PRD exists to resolve — it is named here, not chosen here.**
2. **A decision on whether Cypher survives the move.** Agents write Cypher today against
   `CloudNode`/`CloudEdge`. Trino speaks SQL. Preserving the query dialect and moving the engine are
   two different projects with two different costs.
3. **The retirement condition for the local projection**, per the NEVER-shadow-pipeline rule. A port
   with no named retirement is a duplicate output path.
4. **The gateway's authorization model must cover agent-to-graph reads.** F7's framework is built and
   governed; whether an agent traversal fits its existing AuthKinds is unestablished here.
5. **Network reachability from the gateway EC2 to the graph plane** (VPC/subnet/SG). Not measured.
6. **The `kuzu_nessie_load` key asymmetry (F4) gets fixed or consciously carried.**
7. **An observability answer for O7** that does not violate the standing monitoring moratorium
   (CLAUDE.md §5: no alert/alarm/freshness-checker/monitor unless Andrew explicitly asks).
   ⚠ **O7 and that moratorium are in direct tension.** Andrew's *"no automated process is a risk
   surface"* reads as motion toward the thing the moratorium forbids building unasked. **This needs
   Andrew's explicit word; it must not be resolved by inference in a decomp.**
8. **The `comp-graph status` mis-pointing (F6) is owned somewhere**, since it is the natural home for
   O7's operator-facing half.

---

## PART VI — STATUS TODAY ⛔ NOT OUTCOME-BEARING

*Measured 2026-09-01, 19:15Z–19:45Z. Status ages; do not cut outcomes from this part.*

- Canonical local DB `infra/aws/globgrph/kuzu_nessie_db`: **27,107 nodes / 60,636 edges**, 46,997,504
  bytes on disk, `built_at 2026-09-01T16:18:23.487109+00:00`, `source_kind: nessie`,
  `schema_version: 1`.
- Pin state at read time: **`Nessie HEAD: current (pin == marker HEAD)`**.
- Per-table vintage reported by the tool itself: `graph_nodes` last-write 6.7h (flagged
  `STALE > 6h cadence`), `graph_edges` 17.4h, `cse` 16.1h, `graph_contracts` 1848.7h.
- Warehouse: `s3://opal-313476888478-globgrph`, HEAD oracle
  `warehouse/_branch_head.main.json`.
- Live-plane scan scope: 2,100 AWS nodes, 96 matching `globgrph`; drift `DECLARED=1511`,
  `LIVE-no-DECLARED=321` (both Nessie DynamoDB tables sit in the latter).
- All five nightly rules + the CloudTrail rule read `ENABLED`.
- `.mcp.json` in-repo registers `opal-agent-comms`, `deck-generation`, `playwright`. **opal-gateway
  is not registered there** — it is reached as a remote MCP over the EC2 service, which is consistent
  with F7 but was not traced to its client config.

⚠ **COST FIGURES ARE DOCUMENT CLAIMS, NOT MY MEASUREMENTS, AND THEY DISAGREE.**
`NFRA_KUZUSPLIT_PRD.md` §3 states derive **~10 min** / full projection **~6 min**.
`NFRA_GRAPHS.md` §3 states `comp-aws derive` **~8 min**.
KUZUSPLIT §2 states the incremental is **92× faster (3.9 s vs 356 s)**.
Andrew's stated experience is **9–10 min**.
>> **I did not time anything. Four figures from three sources for two different operations — I am
   deliberately not reconciling them, because picking one would manufacture a measurement.** The
   direction is not in doubt; the magnitude is unestablished and P0-INSTRUMENT in KUZUSPLIT §5 exists
   for exactly this. <<

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **I did not run or time `kuzu_nessie_load`, `comp-aws derive`, or a stitch.** Every duration in
   this brief is quoted and attributed. No timing here is mine.
2. **I did not confirm the two running ECS services by name** (F2). I read task definitions and a
   count. Nessie + Trino is an inference.
3. **I did not verify the nightly jobs SUCCEED** — only that their rules are `ENABLED`. `ENABLED` is
   a DESIRED-plane fact about a rule; it is not an EXERCISED-plane fact about a run. Given that O7 is
   precisely about confirming the automation ran, **this gap sits on the brief's own load-bearing
   claim** and I am naming it rather than softening it.
4. **I did not establish whether O-4 (F9) was ruled.** Absence of a found ruling is not a ruling.
5. **I did not measure how many agents pay the refresh cost per day, or how often.** The 16
   fallback rows (F5) count *labeled-stale serves*, which is a different quantity from *compiles
   paid*. Treating one as the other would be a denominator error.
6. **I did not check gateway network reachability to the graph plane**, nor whether a graph
   traversal fits an existing AuthKind.
7. **I did not evaluate whether Kuzu can run at all in the target cloud shape**, nor benchmark Trino
   as a substitute traversal engine. Part V item 2 is named, not analysed.
8. **I did not read the current NFRA_KUZUSPLIT task-order set** — this is mode NEW, and the P4/O-4
   reading is taken from the PRD, not from what is open.
9. **F6 is surfaced, not diagnosed.** I did not open `graph_status_cli.py` to determine why it points
   at legacy artifacts.
10. **The tension in Part V item 7 (O7 vs. the monitoring moratorium) is named, not resolved.** I
    have no authority to resolve it and did not attempt to.
11. **F11 and F12 are ATTRIBUTED to `3.0.0_SA_CVO`, not measured by me.** I did not re-run
    `comp-blast`, did not reproduce the `perfrp_emit_core.py` NOT-FOUND, and did not independently
    verify the step-5 admissibility gate's text. Per the relayer half of the Andrew-direct protocol,
    the grounding pointer travels with the claim: **msg 92472; `ADVI_PERFRP-S18` @`3eb00f5905`.**
    A second seat agreeing with F4 via F11 is **not corroboration of F4** — F11 *cites* F4 rather
    than re-measuring it, so the two are one instrument, not two.
12. **NOTHING here establishes that the projection actually goes stale in practice.** Both seats'
    only vintage samples were healthy. The measured claim is the absence of a bound (F4), not the
    presence of staleness. **Do not let F11's framing be read downstream as evidence of drift.**

---

## REFS TO CARRY

```
BRIEF PATH        docs/briefs/globgrph-cloud-compile-and-gateway-traversal-20260901.md
PROJECT           NONE-YET
EXISTING PRD      NONE for this scope.
                  Adjacent, do not reopen:
                    docs/architecture/NFRA_KUZUSPLIT_PRD.md      (RATIFIED 2026-07-17; P4/O-4 = ancestor)
                    docs/architecture/NFRA_GLOBGRPH_PRD.md       (CLOSED-COMPLETE 2026-06-16)
                    docs/architecture/NFRA_GRAPHS.md             (query-vs-rebuild contract, §3/§4)
                    docs/architecture/NFRA_INTEGRATIONS_STANDARD.md (gateway extension contract)
                    docs/architecture/D6_OPAL_ANALYST_GRAPHQL_PRD.md (DIFFERENT consumer)
SIBLING PROJECTS  NFRA_GLOBGRPH · NFRA_KUZUSPLIT · NFRA_GRAPHS · NFRA_INTEGRATIONS · D6_OPAL_ANALYST
CONTRIBUTED      F11 + F12 from 3.0.0_SA_CVO msg 92472 (2026-09-01 19:47Z), attributed in place.
                  F12's coverage finding filed separately as ADVI_PERFRP-S18 @3eb00f5905.
                  Not re-measured by CRO -- see Part VII items 11-12.
PRIOR ART         Substrate card (F4): org/tier2_senior/0.7.0_AE_CloudOps~K/deliverables/
                    D11_CARDS/kuzu_nessie_load.card.json @5da9e7fffc, carded 2026-08-30T03:12:00Z
                  Engine:   infra/aws/globgrph/kuzu_nessie_load.py · kuzu_cli.py ·
                            kuzu_incremental_refresh.py · derive_stitch.py · kuzu_stitch_load.py
                  Wrappers: .tools/comp-kuzu · comp-kuzu-full · comp-kuzu-inc · comp-aws · comp-graph
                  Gateway:  infra/aws/ec2/opal-gateway/app/integrations/{base,registry}.py
                  Telemetry: infra/aws/globgrph/kuzu_nessie_db.fallback.jsonl (F5)
MEASURED AT       2026-09-01 19:15Z-19:45Z, all Part VI + Part IV claims.
                  Instruments: comp-kuzu-inc (live-plane projection, DB built 16:18:23Z,
                  pin == marker HEAD) · comp-find --corpus aws · comp-read · comp-graph status ·
                  direct file reads of manifests and telemetry.
CONSTRAINTS       CLAUDE.md Rule 20 (query, never rebuild) · Rule 22 (evidence law) ·
                  Rule 27 (surprise channel -- F6 surfaced not chased) ·
                  NEVER: no shadow/build-alongside pipeline or duplicate output path ->
                    this is a PORT WITH A RETIREMENT (Part V item 3) ·
                  NEVER: no monitor/alerter unless Andrew explicitly asks -> Part V item 7 TENSION
OPEN FOR ANDREW   (a) O7 vs. the monitoring moratorium -- explicit word needed (Part V item 7)
                  (b) Does Cypher survive the move, or is SQL-over-Trino acceptable? (Part V item 2)
                  (c) Was NFRA_KUZUSPLIT O-4 ever ruled? (F9)
NEXT              step 2  1.0.0_SA_CTO  /endpoint --forward <this brief>
```
