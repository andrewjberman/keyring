# P5 DEBT-IDENTIFICATION METHODOLOGY SPEC — high-fidelity liveness classification for the cleanup stage

**Author:** `4.0.0_SA_CRO~A` · 2026-08-11 ~18:10Z · **archetype:** RESEARCH+DESIGN (no act)
**Commission:** Andrew-direct ~1750Z (*"research on how we can identify debt most effectively with
highest fidelity for the cleanup stage, should cover all resources as well as artifacts"*),
retargeted *"Do it for CRO~A"*; brief @11908b1835
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/BRIEF_CRO_DEBT_IDENTIFICATION_RESEARCH_20260811.md`).
**Route:** CVO (instrument review) -> CTO (ratify) -> Andrew.
**Boundaries honored:** research + spec ONLY. Nothing here deletes, moves, reclassifies, enables
logging, or builds a detector/monitor/notifier (moratorium). Every enablement below is a PROPOSAL
ruled at review; every gap-closure is a gate/tool CANDIDATE routed, not built.
**Inherited law (cited, not re-derived):** Rule 25 (90d dormancy + two-kind exceptions +
successor-check) · Rule 24 (four postulates at authoring) · Rule 22a (comp-iam floor-not-ceiling;
never a deletion warrant) · NEVER#3 (served moves = never-widen) · NEVER#1 (trading-day frontier)
· retrieval controls (denominators; materialised lists; positive controls on ABSENT) · the
phase framework (P5 gated on portal-verified; migrate-before-kill).

---

## 0. THE ONE-PARAGRAPH METHOD

**Evidence of LIVE is cheap and definitive; evidence of DEAD is expensive and never definitive —
so the methodology spends bottom-up.** Most candidates classify LIVE or DECLARED-EXCEPT off one or
two cheap instrument reads and leave the pipeline immediately. The expensive machinery — the
closed-world consumer enumeration, the observation window, the deny-probe — is reserved for the
small residue heading toward KILL, because **evidence requirements scale with the IRREVERSIBILITY
of the disposition, never with the size of the artifact.** A keep-decision may rest on one tier-0
read. A kill-decision rests on the full chain of §4, and nothing else authorizes `rm`.

## 1. RQ1 — THE EVIDENCE LADDER (fidelity-ranked; each rung: proves / cannot prove / blind spot)

| Tier | Instrument class | PROVES | STRUCTURALLY CANNOT PROVE | Blind spot (the §2-brief FP class it feeds if trusted alone) | Cost |
|---|---|---|---|---|---|
| **0** | **Live-wire positive read**: deployed-FE read census (D_00 — what the deployed frontend ACTUALLY requests, line-cited); deployed router/Lambda CONFIG read (key-mappings, env vars, resolved at the deployed version); an observed invocation with the caller identified | LIVE — a named consumer exists and its edge is real | DEAD — absence of THIS evidence is absence of one consumer class, not of consumers | FE census sees only FE demand: agents, crons, sibling Lambdas, external partners are invisible. Router config proves a MAPPING, not traffic | cheap (censuses exist: D_00 x3 firms; ~B's router adjudication is the type specimen) |
| **1** | **Runtime observation over a window**: CloudWatch Lambda `Invocations`/`Errors` (already collected, free); DDB `ConsumedRead/WriteCapacityUnits` (free); EventBridge `TriggeredRules`/`InvocationsSentToDlq`; CloudTrail MANAGEMENT events (already on, 90d — incl. `AssumeRole` per IAM role, `GetFunction`, console reads); S3 server-access logs / CloudTrail DATA events (NOT enabled today — enablement is a §6 proposal) | READS/FIRES HAPPENED — the strongest practical "something touches this" | dead. Absence over window W bounds consumer cadence > W; it never reaches zero (annual, incident-only, on-demand consumers) | Invocation is not outcome (Rule 12): an invoked-and-erroring function reads LIVE here while serving nothing. Metrics are per-FUNCTION, never per code path. **A window's silence is evidence ONLY if the instrument is proven emitting: every window carries a POSITIVE CONTROL (a known-live key of the same class must appear in the same window) — an enabled-but-misconfigured log yields clean silence, the anti-correlated instrument class (22b)** | free where metrics exist; S3 read-evidence needs enablement |
| **2** | **Deployed-plane structural enumeration**: who COULD read it — EventBridge rules in **BOTH namespaces** (`events list-rules` AND `scheduler list-schedules` — single-namespace absence is a false deletion warrant, SSOT-matrix banked); S3 event notifications + EventBridge S3 rules; **Lambda async destinations (live on the CALLER — search FOR the name, the 08-10 lesson)**; SSM documents; CF behaviors + DEPLOYED edge-router version (comp-routes is DESIRED-plane; ground security-relevant branches on the deployed artifact per 22a); IAM policies naming the ARN; EC2_MANIFEST + on-host cron/services; bucket policies/replication | A CONSUMER EDGE EXISTS (potentially-live) | that the edge ever fires | Computed keys: a consumer that composes the key at runtime is invisible to every static read (the brief's FP-1 — 5 of 21 cot "orphans" were router-mapped). Enumeration is closed-world ONLY if the namespace list is itself complete — §3's namespace roster is normative | cheap-moderate (aws reads; the sweep is enumerable) |
| **3** | **Repo/source reference census**: `comp-find` FOR the name (bands separate a source edge from a doc mention; denominator printed; UNREADABLE files named) | something NAMES it | liveness in either direction: deployed-vs-repo drift means a repo-silent artifact can have deployed consumers, and a repo-named artifact can be long-retired ("a REFERENCE is not a FAILURE") | DOC-band hits are records, not edges. Deployed bytes with no repo home (the pull_inflection class, pre-baseline) escape entirely — pair with tier-2 | cheap |
| **4** | **Producer freshness**: age vs Rule 25 (90d), trading-day frontier, declared TTL | the WRITER stopped (producer-side dormancy) | anything about READERS. And dormant is not a deletion warrant (Rule 25 verbatim) | Age cannot distinguish ABANDONED from KEY-MIGRATED (FP-2, opposite dispositions) nor from CLOSED-PERIOD-IMMUTABLE (FP-3, where refresh would be the defect) | free (comp-freshness + listings) |
| **5** | **Records/believed state**: ledgers, TOs, catalogs, docs, comp-estate snapshot names, sentinels | a CLAIM was made | anything — 6 of 10 records FALSE on the last measured run (SSOT matrix); the wo4c sentinel sat 14d "held" past completion (FP-5) | Records enter the methodology as HYPOTHESES to verify on the live plane, never as evidence rows | free, and worth exactly that |

**Ladder law:** a LIVE verdict may rest on any single tier-0/1 positive. A DEAD verdict may rest
on NO single rung — it is a conjunction (§4), because each rung's negative is only "this consumer
class is absent."

**Per-resource-class "nothing reads this" instrument (the key design question), best-available →
gap:**

| Resource class | Best available today | Designed blind spot | Gap (→ §6) |
|---|---|---|---|
| Lambda | CW `Invocations` window + tier-2 trigger census both namespaces + async-destination search-FOR | invoked≠served; per-path blindness | none blocking |
| EventBridge rule/schedule | `TriggeredRules` + target existence | disabled-but-referenced states | none blocking |
| DynamoDB table | consumed-capacity metrics (free, on) | per-key blindness (table-grain) | acceptable at P5 grain |
| IAM role | CloudTrail `AssumeRole` lookup (90d, free, already on) | role-used ≠ every-grant-used (22a: grants are a FLOOR — never least-privilege-prune from absence) | none for role-grain; grant-grain OUT OF SCOPE for P5 deletion |
| S3 prefix/object | **NO read-evidence instrument exists** — composite proxy: D_00 census + deployed-config reads + repo sweep | the entire non-enumerated consumer space | **GAP-1, the estate's largest.** Proposal §6: bounded-window server-access logging on KILL-CANDIDATE prefixes only |
| CF/API-GW route | comp-routes (DESIRED) + deployed edge version | behavior-grain traffic needs logs (not enabled) | GAP-2 (accept: route retirement rides its S3 origin's evidence) |
| EC2 service | EC2_MANIFEST + SSM run history + process liveness | manifest is a record (tier 5) — verify live | none blocking |
| Repo script | safe-deploy map membership + deployed-copy existence (comp-pipescript deployed) + runner telemetry | the second-distribution-target class (today's calendar file: `lib/` outside mapped homes) — deployed-copy census must sweep ALL code stores, not the map's homes | GAP-3: code-store roster (see §6) |
| comp-tool | registration gate + rail/usage logs (real telemetry exists) | consumers via `command -v` fail SILENT when a binary vanishes — the FP-7 ordering law exists because of this | none — ordering rule covers |
| Freshness/registry entries | key-existence check per entry | an entry pointing at an archived key false-alarms forever (measured TODAY: the flat platinum mdpf key archived 08-06, its cadence entry live) | GAP-4: registry-key existence lint |

## 2. RQ2 — THE NEGATIVE-EVIDENCE PROBLEM (windows per cadence class; what observation can never prove)

**Window rule: W >= 2x the candidate's declared consumption cadence, spanning at least one
month-end AND one quarter-end where any reporting consumer is plausible.** Where cadence is
UNKNOWN, observation cannot conclude — the candidate routes to consumer-side enumeration (§3),
not to a longer wait.

| Cadence class | Window sufficient for DORMANT-grade evidence | Note |
|---|---|---|
| daily/weekly | 15 trading days | clears NEVER#1 by construction |
| monthly | 2 calendar months + one month-end | |
| quarterly | 2 quarters | the ONE class near Rule 25's bar — must carry its declared exception before, not after |
| annual (`cma` class) | **observation cannot conclude inside program time** — consumer enumeration ONLY | Andrew's named example |
| incident-only (DR/rollback), on-demand (compliance/audit), human-browsed, external-partner-read | **NEVER provable dead by observation** — these four classes are enumeration-only, and external-partner reads are invisible without S3 access logs even then | the honest list the brief asked for |

**The window clock starts when the instrument is positive-controlled, not when it is enabled.**

**The terminal control for a kill candidate — the DENY-PROBE (proposal, ruled-per-class):**
after the §4 chain reaches believed-dead, a **bucket-policy/explicit deny on the candidate for a
probation window** converts an IRREVERSIBLE delete into a REVERSIBLE refusal: any surviving
consumer surfaces as a LOUD AccessDenied instead of a silent post-mortem. The estate has already
exercised this exact shape (the bronze `.parquet` bucket-policy deny, live + behavior-exercised).
It is a bounded P5-execution act with same-window rollback, not a standing monitor. **It
deliberately breaks a live consumer if the evidence chain was wrong — so it is legal ONLY as the
LAST link after the full §4 chain, is ruled per class (internal/code-store classes freely; any
serving-adjacent class = CTO+COO, Andrew where served), and its probation window follows the
cadence table above.**

## 3. RQ3 — THE CLASSIFICATION SCHEMA (Rule-24-conformant; state-coherence test run in-line)

**Census unit (postulate ii):** LEAF-GRAIN ONLY, adopting the SSOT matrix's ruled form — every
census declares its leaf; parents carry derived summaries, never a state of their own.
**Family resolution BEFORE classification (defeats FP-4):** a candidate is resolved to its FULL
FAMILY — both spellings (`_`/`-`), every nesting level, every layer-twin — via the family map
(§6 GAP-5), before any member takes a state. A leaf name is a label, not an identity.

**AXIS 1 — LIVENESS STATE** (one intent: state of use; MECE at leaf grain):

| State | Entry evidence (minimum) |
|---|---|
| `LIVE` | any tier-0/1 positive inside the cadence window |
| `DORMANT-EXCEPTED(kind=long-ttl-live)` | Rule 25 declared exception; age measured against the DECLARED TTL |
| `DORMANT-EXCEPTED(kind=closed-period-immutable)` | declared; a refresh would be the defect (23 measured instances day one) |
| `SUPERSEDED(drained \| still-read)` | named successor + migration record VERIFIED live-plane (successor fresh, shape-compatible); sub-state from tier-1 on the OLD key |
| `SOVEREIGN-RETIRED-STILL-SERVING` | a ruling says dead + tier-0/1 says live (FP-6, certified-AUA class). Debt by ruling, live by wire |
| `DORMANT-UNEXCEPTED` | >=90d, no declared exception, **successor-check RUN and negative** (Rule 25's mandatory link), consumer evidence absent at tiers 0-2 |
| `DEAD-EVIDENCED` | the full §4 kill chain — never fewer links |

**Postulate (iv) state-coherence, run:** the axis FAILS single-remedy — deliberately — and names
which values move under which remedy: {LIVE, DORMANT-EXCEPTED} → keep-class; {SUPERSEDED,
SOVEREIGN-RETIRED-STILL-SERVING} → migrate-class (**the remedy is a migration act, never a
delete, and never "un-rule"**); {DORMANT-UNEXCEPTED} → hold-for-evidence (it is not a deletion
warrant); {DEAD-EVIDENCED} → teardown-class. No value is moved by another value's remedy; the
brief's "LIVE/DORMANT/DEAD x remedy" axis is exactly this map.

**AXIS 2 — DISPOSITION** (one intent: what P5 does; assigned per leaf, reachable only from the
states listed): `keep` (LIVE) · `keep-declared-exempt` (DORMANT-EXCEPTED; registry entry) ·
`migrate-then-kill` (SUPERSEDED-still-read, SOVEREIGN-RETIRED-STILL-SERVING) · `drain-then-kill`
(SUPERSEDED-drained) · `kill` (DEAD-EVIDENCED only) · `permanent-exempt`
(closed-period-immutable). **No disposition is reachable from DORMANT-UNEXCEPTED** — that state's
only successor is more evidence (window/enumeration) or an exception declaration.

**THE CLOSED-WORLD NAMESPACE ROSTER (normative — an enumeration is closed only over this list,
and amending this list is a spec-amendment event):** repo (comp-find, all bands) · deployed
Lambda code+env (all functions, materialised) · EventBridge BOTH namespaces · S3 event
notifications + EventBridge S3 rules · Lambda async destinations (caller-side sweep) · SSM
documents · CF behaviors + deployed edge routers · API-GW routes · IAM policies naming the ARN ·
EC2_MANIFEST + on-host cron · safe-deploy maps + ALL code stores (GAP-3 roster) · comp-tool
registries + freshness/cadence configs · the served-JSON estate (D_00 censuses) · portal FE
source · external-partner contracts (enumerated from the vendor registry — the one class with no
technical sweep).

## 4. RQ4 — EVIDENCE CHAIN PER DISPOSITION (minimum set; attestor; instance form)

| Disposition | Minimum evidence chain | Attestation |
|---|---|---|
| `keep` | one tier-0/1 positive, cited | lane |
| `keep-declared-exempt` / `permanent-exempt` | exception KIND + rationale + registry row | lane declares; CTO ratifies the registry |
| `drain-then-kill` | successor live-plane verified + old-key tier-1 zero over its cadence window + repoint census (every §3-roster edge moved; search-FOR clean WITH denominator) | lane + CVO cert |
| `migrate-then-kill` | all of drain-then-kill PLUS same-state equivalence evidence (paired pulls in one window or ex-ante tolerance frame — a diff indistinguishable from a trading day of drift proves nothing; CVO A2, adopted) + never-widen co-sign where any served key moves | CVO cert; CTO+COO co-sign; **Andrew where served keys move** |
| `kill` | (1) closed-world enumeration over the FULL §3 roster, each namespace with its denominator and its instrument's positive control; (2) observation window per §2 with in-window positive control; (3) successor-check run (negative); (4) family resolution complete (no live twin); (5) reversibility mechanism named (versioned bucket / archive-copy / tombstone) and, where ruled, (6) the deny-probe survived its probation window | CVO cert; teardown TO carries a PROOF_OF_SPEC instance, phase=P5-DECOMMISSION |

**The PROOF_OF_SPEC instance for a P5 teardown TO carries:** candidate id + family map · census
commit + vintage · state + disposition · one row PER evidence link (instrument, exact invocation,
denominator, result, vintage, positive control) · successor row · ordering row (§5 in-edge count
= 0, sweep cited) · reversibility row · attestor chain. **A missing link is a missing link — the
TO is DECLARED-GATED, never rounded up.**

## 5. RQ5 — THE ORDERING RULE (consumers-first-binary-last, generalized)

Build the **NAMES-EDGE graph** over the census: X→Y iff X names/reads/schedules/maps Y (edges
from the §3 roster sweeps). **A node is deletable only when its live in-edges are zero, verified
by search-FOR-the-name AT TEARDOWN TIME** (a census-time zero is stale by teardown time — the
sweep re-runs inside the teardown TO). Teardown order per family:

1. **Consumers/edges first** — repoint or retire every reader, then re-sweep.
2. **Instrument/registry entries second** — freshness rows, comp-tool registrations, HUD/route
   entries pointing at the candidate retire BEFORE the artifact, so no instrument is left doing a
   `command -v`-class silent skip (FP-7's mechanism: **a gate whose binary vanishes does not fail
   — it stops being run**).
3. **The artifact last** (with its reversibility mechanism armed).
4. **Tombstone the record** — the ledger entry that says what was removed, when, on which chain,
   pointing at the archive. Records are claims, so the tombstone also states the verifying sweep.

Two special rules: **guarded sets tear down as ONE family or not at all** (a half-deleted
spelling pair recreates the FP-4 hazard at teardown); **regenerated artifacts** (a gold twin a
run re-mints) are not deletable by object-delete at all — the PRODUCER retires first or the
delete is a no-op that reads as done (the measured account-distribution class: same filename
family, opposite consequence per layer).

## 6. RQ6 — INSTRUMENT FIT + GAPS (gaps are DEFECTS; closures are candidates ROUTED, not built)

**Fit today:** comp-estate (thread/ownership; snapshot-vintage declared, C0 roster non-denominator
by its own label) · comp-kuzu/comp-blast (modeled edges; vintage-bound, computed-key-blind) ·
comp-find (the search-FOR instrument: bands + denominators + UNREADABLE named) · comp-freshness
(producer-side only) · comp-iam (floor, never warrant) · comp-routes (DESIRED; deployed edge =
22a read) · comp-pipescript deployed (repo-vs-deployed per mapped home) · deploy ledger (claims).

**Gaps, named as defects (the comp-tooling is foundational, not additive):**
- **GAP-1 (largest): no S3 read-evidence instrument.** Proposal: enable server-access logging (or
  CloudTrail data events, priced at review) on KILL-CANDIDATE prefixes ONLY, for the §2 window,
  disabled at window close — observation, not alerting; enablement ruled at CVO/CTO review, per
  the brief's own carve-out. Candidate tool: `comp-readers <prefix> --window` (reads the logs,
  prints per-key reader census + denominator). ROUTED, not built.
- **GAP-2: CF behavior-grain traffic** — accepted residual; route retirement rides its origin's
  evidence.
- **GAP-3: no code-store roster.** Today's calendar incident is the class: `lib/` sits outside
  every safe-deploy home, so deployed-copy censuses sweep the MAP's stores and miss real ones.
  Candidate: a declared roster of ALL code stores (the CPR-5/second-target act already in flight
  covers the known two; the roster generalizes it), consumed by comp-pipescript.
- **GAP-4: registry-key existence lint** — a comp-freshness/comp-estate entry whose key 404s is
  instrument debt that false-alarms or false-passes forever. Candidate: a config-sweep lint
  (commit-time), gate candidate to CTO.
- **GAP-5: no family-map instrument.** The `_`/`-` spelling law, nesting twins, and layer twins
  live in single-homed knowledge (publisher `_KEY_RE`, MEMORY guards). Candidate: `comp-family
  <leaf>` — resolves a leaf to its full family across layers/spellings before any census verdict;
  P5's census REQUIRES family resolution (§3), so this gap is on P5's critical path and is the
  first tool worth building when Andrew opens that door.

## 7. THE ADVERSARIAL TEST — the methodology vs the seven measured FP classes + COO's four live calls

| FP class (brief §2) | Where the methodology defeats it |
|---|---|
| 1 router-mapped orphans | tier-2 deployed-router read is a REQUIRED rung; router maps are on the §3 roster — an S3-side-only census cannot reach a verdict |
| 2 key-migration-as-abandonment | successor-check is a mandatory chain link (Rule 25); SUPERSEDED is a first-class state with its own (opposite) remedy |
| 3 closed-period immutables | exception KIND in the schema; permanent-exempt disposition; a TTL implementation cannot mis-handle what is not a TTL |
| 4 same-leaf twins / guarded sets | family resolution BEFORE classification; families tear down whole; GAP-5 named |
| 5 sentinel-never-learned | tier-5 records are hypotheses, never evidence rows; every record-claim verifies live-plane |
| 6 deprecated-but-serving | SOVEREIGN-RETIRED-STILL-SERVING state; only remedy = migration act; wire beats ruling for sequencing, ruling beats wire for end-state |
| 7 consumers-first-binary-last | §5 generalizes it, adds instrument-entries-second + regenerated-artifact + guarded-set rules |

**COO's four flagged-not-concluded calls, worked as examples (classification only — no act):**
`partner_analytics/header_metrics.json` → family-resolve against the live `_annual/_monthly/
_quarterly` grain-refinement siblings → SUPERSEDED pending one equivalence read; `partner_
analytics/timeseries_chart.json` → nesting twin of a live leaf → family-resolve, likely
SUPERSEDED; `firm_composition.json` → no live sibling → DORMANT-UNEXCEPTED → hold: enumeration +
window, no disposition; `account_quality_tiers_2026-04-02.json` → date-stamped key → candidate
DORMANT-EXCEPTED(closed-period-immutable) pending declaration.

## 8. WHAT THIS SPEC DOES NOT DO

No census executed, no state assigned outside §7's worked examples, no logging enabled, no tool
built, no deletion ordered, no park touched. P5 executes behind its sovereign gate
(portal-verified event); this methodology is the instrument P5 picks up when that gate opens.

-- 4.0.0_SA_CRO~A
