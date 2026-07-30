# TRIGGER ASSESSMENT PROTOCOL (TAP) — the parallelizable trigger→writer→destination audit

**Commissioned:** Andrew-direct 2026-07-30, to systematize the trigger walk and hand it down to
`0.7.0_AE_CloudOps~*` lanes in disjoint chunks.
**Purpose, in his words:** use the triggers to *track the writers* and see where the compute is
going, cross-referenced against the semantic rulings we already hold on the write targets — in
service of **centralized PARTNER DATA consolidation (C4)** and **a canonical singular pipeline per
function** (no duplicate buckets, no ambiguous ETF-ownership tables, no `opal-data-mdpf` shapes).

**Why triggers first, not lambdas:** a lambda inventory is an alphabetical list of capability. A
trigger inventory is the estate's *causal graph with a clock attached* — it tells you what actually
runs, in what order, writing where. The lambdas fall out of it.

---

## 0. The unit of work: one TRIGGER-EDGE

`(trigger) -> (target) -> (write destination)`. 154 triggers expand to 163 configured target edges
(~A's census, `docs/briefs/TRIGGER_GRAPH_AND_RUNTIME_MAP.md`, zero drift as of 2026-07-30 20:1xZ).
Each edge gets ONE record. Records are JSONL so N lanes merge without collision.

## 1. The seven-check battery (T1–T7)

Checks are ordered so a failure short-circuits meaningfully. **T1–T5 are mechanical and scriptable;
T6 is a JOIN against rulings we already hold; T7 is judgment.**

| # | Check | Question | Method | Fail means |
|---|---|---|---|---|
| **T1** | FIRES | Did the trigger fire in the last 7d? | `AWS/Events Invocations` (or Scheduler group attempts, N/O per-schedule) | dead trigger, or disabled debt |
| **T2** | DELIVERS | Did dispatch succeed? | `FailedInvocations == 0` | broken delivery leg (FIRMSEP class) |
| **T3** | EXECUTES | Did the TARGET actually run? | target's own metric (Lambda `Invocations`, CodeBuild `Builds`, SSM cmd status) | trigger fires into nothing |
| **T4** | WRITES | Did a write land, after the last fire? | destination newest-object/row mtime vs last-fire time | executes but produces nothing |
| **T5** | WRITES **DATA** | Is the newest artifact DATA or a RECEIPT? | **one GetObject / one row read — C-14, non-negotiable** | receipt-not-data (the 107-day class) |
| **T6** | WRITES **WHERE IT SHOULD** | Is the destination canonical, or a deprecated twin / condemned location? | JOIN destination against `20_rulings/SEMANTIC_NOTES/*` + ledger | write-to-deprecated-twin, split-write |
| **T7** | ORDERED CORRECTLY | Does it depend on an upstream, and is that dependency an EVENT or a HOPE? | read the schedule ladder + event patterns of siblings | wall-clock-ladder and friends |

**Evidence bar (inherited, non-negotiable):** behavior claims need exercise/metric evidence, never
config reads (C-11). Every absence claim carries a positive control run **separately** (C-10 lineage).
State the denominator of every scan. Match FULL bucket+key, never a basename (C-15).

## 2. The PATHOLOGY CHECKLIST — measured, not invented, and OPEN

Every entry below was found in the estate on 2026-07-30. Lanes tag each edge with zero or more.
**P-codes are append-only: a lane that finds a new shape ADDS one** (Andrew: *"or potentially some
other fuckery we haven't discovered yet"* — the list is designed to grow, and a new P-code is a
first-class deliverable, not a footnote).

| P | Pathology | Type specimen |
|---|---|---|
| **P1** | **wall-clock-ladder** — sequential steps ordered by cron offsets with no completion check | inf 09:17→09:47; bd 17:38→18:30 |
| **P2** | **no-schedule-only-event** — a production pipeline whose ONLY trigger is another pipeline's success (CLAUDE.md NEVER-rule) | `mdpf-daily-refresh-trigger` |
| **P3** | **cron-at-mismatched-capacity** — schedule fires at an executor whose lifecycle is event-driven/stopped | canonical-schwab pair (my own false read; class is real) |
| **P4** | **applied-despite-hold** — rule applied over a written HOLD, waiting on an event nobody emits | `canonical-schwab-xref-success` (0 fires/30d) |
| **P5** | **duplicate-target-edge** — one rule invokes the same target twice per match | 8 rules incl. all `news-api-*` |
| **P6** | **receipt-not-data** — writes land on schedule carrying nothing | seeking-alpha, 107 days |
| **P7** | **pin-to-last-partition** — consumer reads `newest<=date`, source frozen, no error ever | `wsd-49f-partner-held-etf-daily` |
| **P8** | **estimate-shadowing-exact** — a derived estimate where an exact source exists upstream | mdpf ETF decomposition |
| **P9** | **write-to-deprecated-twin** — writes into a location already ruled deprecated | smartx-v2 compat write |
| **P10** | **split-write** — writes canonical AND legacy simultaneously | assets/schwab + opal-data-schwab escape hatch |
| **P11** | **failed-delivery-100pct** — control that has never once delivered | `FIRMSEP-s3-direct-access-bypass` |
| **P12** | **overmatched-pattern** — event pattern matches normal traffic at volume; repairing delivery would create a storm | FIRMSEP (~250K/day legit matches) |
| **P13** | **disabled-but-declared** — rule disabled while its resources stay live/declared | 18 rules + 1 schedule estate-wide |
| **P14** | **orphan-driver** — target runs daily with NO rule targeting it (chain-invoked; a config read calls it unwired) | seeking-alpha-news-dedup; wsd-49f |
| **P15** | **asymmetric-control** — a control exists for firm A and B but not C | 49F has no hourly value-parity; inf+cot do |
| **P16** | **source-map-missing** — deployed target absent from `lambda-source-map.json` | 4 named by ~A + inf-silver-chain + news trio |
| **P17** | **reattempt-pair** — a second schedule compensating for an unreliable primary rather than fixing it | `opal-assets-bd49f-daily-pull` 22:30 + 00:30 |

## 3. The record schema (one JSONL line per trigger-edge)

```json
{"edge_id":"<rule>::<target_id>","trigger":"","trigger_type":"Rule|Schedule","state":"ENABLED|DISABLED",
 "schedule_or_pattern":"","target":"","target_type":"lambda|ecs|ssm|sns|sqs|logs|codebuild",
 "estate":"Inflection|49 Financial|Cottonwood|Global|Internal","product":"","vertical_candidate":"",
 "T1_fires":{"v":"PASS|FAIL|N/O","evidence":""},"T2_delivers":{"v":"","evidence":""},
 "T3_executes":{"v":"","evidence":""},"T4_writes":{"v":"","destination":"","evidence":""},
 "T5_writes_data":{"v":"PASS|RECEIPT|N/A","evidence":""},
 "T6_destination_ruling":{"v":"CANONICAL|DEPRECATED-TWIN|CONDEMNED|UNRULED|SPLIT","basis":""},
 "T7_ordering":{"v":"EVENT|SCHEDULED-OK|WALL-CLOCK-LADDER|UNKNOWN","evidence":""},
 "pathologies":["P1"],"consolidation_note":"","verdict":"HEALTHY|DEFECTIVE|DEAD|MIGRATION-BLOCKER",
 "confidence":"MEASURED|INFERRED","not_assessed_reason":null}
```

**`vertical_candidate` is the ontology payload** — the C3/semantic-vertical this edge belongs to,
in business language. It is the field the whole exercise exists to populate.

## 4. Chunking for parallel lanes — BY FIRM-ESTATE

Recommended cut for the Advisor-Intelligence/Data-Platform group (55 edges), because it is disjoint,
**respects firm separation (NEVER#2) by construction**, and each chunk yields one firm's complete
canonical-pipeline picture — which is exactly what the PARTNER DATA consolidation needs:

| Lane | Chunk | Edges | Yields |
|---|---|---|---|
| `~A` | **Inflection** | 23 | the inf daily ladder + event spine + parity controls |
| `~B` | **49 Financial** | 23 | the bd evening ladder + the assets-side migration pulls running alongside it |
| `~C` | **Cottonwood + Global** | 9 | the reference implementation (cot is event-driven and correct) |

Later groups (News/Market Intelligence 33, Model Portfolios 15, Graph Infra 6, Ops 4, …) chunk the
same way. **Rule: one lane never crosses a firm boundary within a chunk.**

## 5. What each lane returns

1. `TAP_<chunk>_<date>.jsonl` — one record per edge, schema above.
2. A short narrative: the chain as it actually runs, the pathologies found, and **the consolidation
   verdict** — for each edge, does it survive the move to `opal-data-assets` as-is, need
   re-pointing, or die?
3. **Any NEW P-code**, with its type specimen.
4. Contradictions against existing semantic notes, surfaced loudly (same rule as the enrichment pass).

## 6. Tooling

`comp-estate` is FIRST CONTACT for Estate-Infrastructure questions (CVO's consolidation landed
2026-07-30; surfaced via the comp HUD). `comp-kuzu` for edges, `comp-dataflow origin` for
value-origin on a producer, live AWS primitives for applied truth. ~A's
`TRIGGER_GRAPH_AND_RUNTIME_MAP.md` is the starting denominator — verified zero-drift, so lanes do
not re-derive the inventory; they assess it.
