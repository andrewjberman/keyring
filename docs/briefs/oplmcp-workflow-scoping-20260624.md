# Workflow-Scoping over OPLMCP Traffic — scoping riff

**Andrew sovereign · MSTR-scoped · design-riff 2026-06-24.** A scoping concept, NOT a
build commitment or a committed project — the array of *what the capability is* and
*how its layers tie* so it can be sequenced against OPLMCP .05 (R8 audit-lake) as that
lands. Owner: 0.0.0_AB_MSTR. Sovereign: Andrew.

## Premise (why meter, don't ask)

The OPLMCP M365 gateway will carry heavy traffic from Opal employees (email / calendar /
Outlook / Graph / OneDrive operations brokered through one server). We want our
colleagues to have estate-specific *workflows* (multi-step procedures they invoke to get
a job done) — but **the procedural-authoring gap is real**: it is too hard for a user to
sit down and conceive/specify the workflows they'd want. It is far easier to **meter the
patterns they already perform** and render those into candidate workflows.

The hard part — and why this is several layers, not "watch traffic → here's the
workflow": a raw traffic pattern is a *shape without a why*. **Nuance and scoping matter**
(intent, decision-points, exceptions, when-it-applies-vs-not). So the job is to
**classify + rank workflow CANDIDATES**, then run a **human interview/scoping** step
with the people who actually do the pattern to turn a statistical candidate into a real,
scoped, verified workflow. **The system proposes; humans dispose.**

## The pipeline

### L0 — Capture + distill (the meter is a privacy filter, not just a tap)
Tap the gateway request stream. Per MCP call, run **sharp, granular token-level analysis
IN-FLIGHT** — the actual query semantics / param values / intent / entity-*types*, NOT a
coarse tool-name shape (tool-shape-only is garbage-in: it cannot tell billing-triage from
chatter). This sharp analysis is **ephemeral** — it runs in a recent-session **hot zone**,
then distills each event to a **de-identified semantic signature**, which is what persists
to the **R8 audit-lake** (OPLMCP .05: gateway `_emit` -> S3/Firehose -> Athena; already in
flight — the durable substrate). **Raw tokens + identity are dropped at the distillation
boundary.**
- **Privacy = de-identify, NOT coarsen** (Andrew ruling 2026-06-24). Keep the analysis
  sharp; remove identity instead of blurring signal. A workflow is **identity-INVARIANT**
  (same procedure for any client/person), so typing entities (`Acme` -> `<vendor>`) +
  stripping the person costs ~zero workflow signal. **No identity information is persisted.**
- **Ephemeral identity-linkage IS permitted in the hot zone** (Andrew ruling): retroactively
  **stitch connected sessionIDs** — correlate sessions belonging to the same actor or the
  same cross-session task — to get coherent threads for analysis + distinct-actor counting
  + interview-targeting. The stitch lives only in the hot zone (short TTL) and is **dropped
  before persistence**. Durable store = zero identity, zero re-identifiable session-linkage.
  Keep this token-level analysis **deterministic/cheap** (tokenize + type + signature), not
  an LLM-per-call, or the economics break.

### L1 — Sessionize (units-of-work) — granular, cross-session-stitched
Raw events -> coherent **units-of-work** (UoW). A workflow is not one call; it is a
recurring *sequence* that accomplishes a goal — and it may **span session boundaries**
(paused/resumed). Segment + **stitch**: combine trace-id / time-gap / agent-turn /
goal-completion signals WITH the hot-zone **sessionID-stitch** (auth/token continuity +
shared entity-handles + temporal adjacency) so a cross-session workflow is reconstructed
WHOLE, not fragmented into half-patterns. Granularity is **token-level** (what the
operation really did), validated against L4 feedback (does our UoW match what a person
calls one task?). The interleaved-multi-actor boundary problem is the hard piece; bad
segmentation poisons everything downstream. heat_map's "cluster units-of-work" maps here.

### L2 — Mine candidates (semantic + chronological)
The step representation is a **semantic signature**, not a tool-name: built via NLP /
tokenization-abstraction over the de-identified query AND result content ->
`step(intent, entity-types, filters, result-shape)`. Mining then clusters by
**intent-similarity** -- same goal via different tools clusters together; same tool for
different goals does NOT (the fix for garbage-in at the mining layer).
**Chronology is mandatory** (Andrew 2026-06-24): full sequence + timestamps are always
preserved -- without sequencing you cannot establish consistent patterns. Mine frequent
**chronological** patterns (PrefixSpan/SPADE-class) + template-induction (collapse
entity-binding variants -> one parameterized template). **Partial-order is a learned
generalization built ON the chronology, never a replacement:** across instances you observe
two steps sometimes A->B, sometimes B->A with the same outcome -> infer interchangeable
(prevents over-fragmentation) -- derivable only because the chronology was kept.
**Order-free / set representation is OFF the table.**
Also: detect frequent **sub-patterns** as candidates in their own right (composable
skill-primitives, not just monolithic workflows). Count support in **distinct ephemeral
actors** (k-anonymity-aligned), not raw instances. Candidate dossier = distinct-actor
support, dept spread, variance, surfaces, example abstracted traces.

**The semantic signature is a first-class REUSABLE substrate** (Andrew 2026-06-24), not a
mining-internal intermediate: a de-identified typed semantic feature per event + per UoW
(result-derived signal is distilled in the hot zone -- raw result tokens never persist).
Workflow mining is ONE consumer. Peer consumers: **use-case archetyping** (a bottom-up
taxonomy of what people actually do -- onboarding / billing-triage / compliance-review /
meeting-prep -- from usage, not the org chart) + **downstream analyses** (demand/coverage
gaps, department-activity profiling, usage trend/drift, load concentration, anomaly
detection). One substrate, many consumers. Archetypes feed BACK into L3 (a UoW's archetype
sharpens its classification + the strategic-priority overlay).

### L3 — Classify + Rank (the nuance layer)
- **Classify** by intent/type; by **mutation-class as a hard GATE** (read-only ops flow
  normally; mutating ops -- send/create/delete -- route to a stricter track: higher bar
  to surface + mandatory L4 authorization + L5 shadow-mode); by department; by coverage.
- **Rank as a human-attention-budget TRIAGE policy** (the L4 interview budget is the
  scarcest resource), on two orthogonal axes: *confidence it's a real procedure* (>=K
  distinct actors, low-variance, entity-coherence, intent-consistency, not-an-artifact) x
  *value if real* (hours-saved/week from measured manual-time x frequency x population;
  friction; strategic overlay). Policy: high-confidence x high-value -> surface now;
  high-value x low-confidence -> gather more evidence first (don't spend an interview on a
  shaky candidate); low-value -> log, never surface.
- **Artifact-rejection is a TRAINED classifier**, not a fixed rule-list: heuristic priors
  (polling / retry-storms / single-user / coincidental co-occurrence / seasonal bursts) at
  cold-start, then trained on L4 accept/reject + L5 adoption -> fits the org's real
  work-manifold.
- **Cross-department patterns get special treatment** (Andrew-liked): a pattern spanning
  multiple depts is high-leverage (standardize org-wide) AND needs careful scoping (per-dept
  variant-variance is meaningful, not noise) -> a multi-dept L4 interview -> common core +
  dept-specific variants -> one configurable workflow.
- **Fork coverage -> adoption-gap stream:** a high-support pattern an existing skill already
  covers = the rail isn't routing to it -> routing-layer remediation, NOT a new-workflow
  interview.
- **Dedup into candidate-families** before surfacing (L2 emits overlapping variants); pick
  the representative + its composable sub-parts. Output: **CANDIDATE-LIST-ONLY**.

### L4 — Interview + Scope (the key move: react, don't author)
A ranked candidate is a **hypothesis** ("we think your team repeatedly does X"). The trace
shows the *shape* but not the *why/when*. L4 turns the statistical candidate into a scoped
spec by extracting exactly what the trace cannot show.
- **React, don't author -- with a graceful fallback ladder** (strawman quality is the
  make-or-break; if the draft is bad, "correct it" silently becomes "rewrite it"):
  1. *best:* a runnable draft workflow the person tries + tweaks;
  2. *fallback (low synthesis-confidence):* the observed pattern as a narrative + example
     ("you do A->B->C ~N x/week; one-click it?") -- confirming a pattern is a lower bar
     than confirming a generated procedure;
  3. *floor:* a yes/no/annotate -- even a thumbs-down is a valuable label.
  Degrade by confidence so a weak draft never forces authoring-from-scratch.
- **Scaffolded extraction -- five fixed slots** the strawman pre-fills + the human confirms:
  intent/goal · decision-points (the trace's variance -> "when X vs Y?") · exceptions/scope
  ("when does this NOT apply?") · start-state + done-state · success criteria. Bounded
  interaction, not an open conversation (open = the burden we're avoiding).
- **Two review roles:** *originators* (whose hot-zone threads produced it -- targeted via the
  ephemeral link) validate the SHAPE + nuance; a *department lead / process-owner* blesses the
  SCOPE + standard + policy. Cross-dept candidates -> a multi-party reconcile (common core +
  dept-variants -> one configurable workflow).
- **Engagement is load-bearing, not polish:** near-zero-effort (react + ladder) + immediate
  visible value (the L3 hours-saved/week as the carrot) + surface in-context (in the tool
  they're already in, not a separate portal) + visibly close the loop when their workflow
  ships. If the human layer starves, the whole pipeline stalls.
- **Every interaction is a structured label** (accept / reject / "split this" / "missed a
  step" / "seasonal-only") -> flows back to L3 artifact-rejection + L1/L2 tuning. L4 is the
  pipeline's labeling engine.
- **Timing coupling (privacy):** targeting an originator needs the hot-zone link -> a candidate
  must reach L4 before its TTL drops the link, else fall back to cohort/self-claim ("anyone in
  billing recognize this?").
- Output: an **enriched, scoped workflow spec** (statistical candidate + human nuance + scope).

### L5 — Synthesize + Verify + Adopt
- **Synthesize from the spec as a COMPILER INPUT, not a prompt:** the L4 spec (intent + steps
  + confirmed branches + scope-guards + success-check) deterministically compiles to a skill
  scaffold; generation fills only the gaps (cheap + reproducible + verifiable -- the
  determinism discipline). The L4 strawman is the seed; L5 hardens it (bind params, insert the
  confirmed branch logic, add scope-guards + success-check).
- **Verify tiered by mutation-class** (grounding discipline; never deploy on self-report):
  - *Read-only:* dry-run on de-identified inputs + output-sanity + a human spot-check.
  - *Mutating:* mandatory **shadow-mode** (actions intercepted + shown as "would send
    X to Y," never executed) until a human certifies a batch -> then a **staged rollout**
    (originator first, monitored) + a kill-switch + a per-mutation audit trail.
  - The **verification oracle** (hard, open): replay against historical de-identified traces
    (reproduces observed-correct outcomes?) + originator shadow-run acceptance + property-checks
    (stays in scope? touches only declared entity-types?). Layer all three.
- **Deploy via the rail -- inheriting the unsolved routing problem** (the in-house
  tool-routing problem): the strongest mitigation is **route at moment-of-need** -- the SAME
  recognition engine that mines candidates offline also detects a LIVE instance of a known
  workflow and offers it ("looks like you're doing X -- run the workflow?"). Mining (offline) +
  routing (live) are one recognition engine pointed at two time-horizons.
- **Adoption signals (the feedback backbone), each routing to a remedy:** invocation rate ·
  success rate · edit-on-use (spec slightly wrong -> back to L4) · abandonment (friction) ·
  still-manual rate (routing gap OR wrong scope). Captured structurally (per-session-source
  discipline).
- **Lifecycle -- version, drift, retire:** workflows are versioned; the same drift/freshness
  sensing that finds candidates flags a deployed workflow going STALE (usage drifts from spec
  / invocations start failing) -> re-enrich or retire; an unused workflow is retired (don't
  accumulate dead skills -- that's the slop the rail must wade through). Born from a pattern,
  retired when the pattern dies.
- **Govern mutating workflows like deploys, not read-tools:** staged rollout + kill-switch + audit
  ledger + human-authorization gate (the never-half-land discipline applies to a workflow that
  sends/creates on employees' behalf).

## The scoping loop (how it tightens with use)
`capture -> sessionize -> mine -> classify/rank -> interview/scope -> synthesize/verify ->
deploy -> measure.` Each cycle's adoption + still-manual signals refine the next round's
ranking + mining; unaddressed manual work (employees still hopping by hand, uncovered by any
workflow) is the signal for the next candidate. The loop also closes the LIVE side: the same
recognition that mines candidates offline offers known workflows at moment-of-need.

## Cross-cutting concerns (the parts that aren't simple)
1. **Privacy — the two-zone model** (Andrew ruling 2026-06-24): an **ephemeral hot zone**
   (recent sessions, short TTL, access-controlled, never logged/backed-up, ideally
   client-perimeter) where sharp token analysis + **sessionID-stitch** + distinct-actor
   counting + interview-targeting run WITH ephemeral identity; a **durable cold zone**
   holding only de-identified, k-anonymized pattern signatures. Identity + raw
   session-linkage are dropped at the distillation boundary. **No identity persisted;
   ephemeral session-stitch OK.** The trio (ephemeral stitch + identity-invariant workflow
   + k-anonymity) wants the same thing, so privacy and signal-quality stop fighting.
   Residual risk: the hot zone transiently holds identity-linkable data -> bound the TTL
   tightly + enforce a k-anonymity floor + small-cohort (<=2-person dept) suppression at
   distillation. Open knobs: hot-zone TTL (~rolling day, tunable); the "connected" signal
   for the stitch (auth/token continuity + shared-entity + temporal adjacency, weighted).
2. **Unit-of-work segmentation** (L1) — the hard boundary-detection problem.
3. **Candidate-vs-artifact discrimination** (L3) — real procedure vs statistical noise.
4. **The mutation bar** — read-only ops auto-surface as candidates; mutating ops surface but never
   synthesize without explicit human authorization + verification.
5. **Attribution under shared/proxied sessions** — correctly tying traffic to the right
   employee/department through one gateway. Same class as the comp-log TO_ID race; apply
   the per-session-source discipline (LD-0205), not a shared last-writer-wins context.
6. **Cold-start** — little early traffic => low candidate quality; need a minimum-evidence
   threshold + a ramp before surfacing.
7. **Slow feedback clock** — adoption signal accrues over time; don't over-fit to early
   noise.
8. **Human-layer engagement** (L4) — if employees don't engage, the pipeline starves;
   near-zero-effort + visible value + in-context surfacing are load-bearing, not polish.
9. **Workflow lifecycle** (L5) — version / drift-detect / retire; don't accumulate dead skills.

## Ties to existing internal assets
- **R8 audit-lake (OPLMCP .05, in flight)** — the L0 capture substrate. The single most
  important tie: the data foundation is already being built.
- **heat_map** — freshness/activity sensing; write/read axes + decay + "cluster
  units-of-work" feed L1-L3 (which patterns are alive/hot vs dead) + L5 drift-detection.
- **the rail (routing layer)** — L5 deploy + the "make-it-get-used" half (route-at-moment-of-
  need); also the agents-still-grep-when-better-exists problem, addressed in-house first.
- **comp-graph / OPLMCP graph-onboarding (.07, closed)** — the gateway architecture is
  graph-native, so the scoping layer can reason about the gateway's surfaces/operations
  via the graph.
- **per-session-source discipline (LD-0205)** — the attribution mechanism for who-did-what.

## Technical implementation — grounded on the OPLMCP graph (`m365-mcp` thread, 2026-06-24)
Examined via comp-which -> pipescript `m365-mcp` + comp-kuzu (graph CURRENT, HEAD-pinned,
built <1h; OPLMCP is graph-native since .07). **The scoping layer is largely an EXTENSION
of resources that already exist — not greenfield.**

**The gateway as it runs today (graph edge-confirmed):**
- **EC2 gateway** `m365-mcp-gateway` (instance `i-07dccb1615503ac99`; `app/server.py`
  uvicorn `0.0.0.0:8080`; `infra/aws/ec2/m365-mcp-gateway`) — the single server ALL employee
  M365 traffic flows through. SSM-managed; instance-profile `m365-mcp-gateway-profile` ->
  role `m365-mcp-gateway-role`.
- **ALB** `m365-mcp-gateway` + HTTPS listener doing **authenticate-oidc (Entra App-1) ->
  forward** -> target group; SGs `m365-mcp-gateway-alb-sg` / `-sg`;
  `infra/aws/terraform/m365-mcp-gateway`.
- **Served:** `https://mcp.opalinvest.dev/mcp` (MCP Streamable-HTTP; Route53 ALIAS -> ALB;
  OIDC-gated). Clients = Claude Code/Desktop remote MCP.
- **Secrets (Secrets Manager):** `opal/mcp/m365-login` (OIDC app), `m365-graph` (Graph creds),
  `m365-fernet` (token encryption), `m365-gateway-jwt` (the .06 embedded OAuth-AS RS256 key).
- **Already built into the gateway** (per the graph node's `what`): per-user **delegated
  Graph token brokered on-box**, a central **kill-switch** + **per-user blocklist**, and —
  decisively for L0 — **tool-level audit**.

**The .05 / R8 audit-lake — now SOURCE-CONFIRMED** (graph nodes `opal-mcp-audit` +
`opal-mcp-athena-results` present + CVO AC#3 verify-on-served PASS, Athena-queryable; the
IAM-grant edges the graph hadn't re-derived yet are confirmed by comp-iam + source):
- `comp-iam service m365-mcp-gateway` -> the role's only grant is **`s3:PutObject [GRANTED]`
  via `_s3_client.put_object` at `app/audit.py:48`** — the gateway is **write-only** to the
  lake (so the scoping/analysis layer is a *separate* consumer needing its own least-privilege
  **read** role = Athena + `s3:GetObject` on `opal-mcp-audit`, NOT the gateway's write-role).
- **Capture chokepoint = 100% coverage:** every MCP tool call flows through ONE dispatch in
  `app/tools.py` -> `audit.log_call(email, tool, args, outcome)`. `_emit` writes a local JSONL
  **floor** + best-effort ships the SAME record to S3 (`audit/dt={day}/{ts}-{uuid}.jsonl`,
  Athena-queryable; lake-write failure never breaks a call). The L0 emit-hook already exists
  and covers every tool call.
- **What the existing record holds:** `{ts, user:email, tool, redacted-args, outcome, detail}`.
  `_redact` is **coarse truncation only** (body/content -> `<N chars>`, >200-char strings
  clipped) — NOT semantic; and **results are not captured** (args + outcome only).

**So L0 is precisely: a richer distill on an existing 100%-coverage hook.** Net-new on top of
`log_call`/`_emit`: (a) the **token-level semantic signature** (intent / entity-types /
result-shape via NLP) — today's `_redact` is truncation, not semantics; (b) **result-shape
capture** — the record omits results; (c) **sessionID-stitch / unit-of-work threading** —
`app/context.py` is only a per-request email contextvar; there is NO session/thread concept today.

**Privacy reconciliation — a real gap to close (source-found):** the current audit **persists
`user:email`** to both the JSONL floor AND the S3 lake — which **contradicts the no-identity-
persisted ruling.** Under the two-zone model this reconciles cleanly: the gateway's per-request
identity is already **verified in-process** (`app/identity.py`: ALB authenticate-oidc ->
`x-amzn-oidc-data` -> ES256-verified vs the regional ELB key -> email claim) — that IS the
ephemeral hot-zone identity. The scoping L0 distill must **de-identify at the distillation
boundary** (email -> ephemeral cohort-pseudonym, used in-hot-zone for stitch + k-anon, then
dropped) so the **scoping lake holds zero identity.** The existing identity-bearing floor can
remain for security/compliance under tighter access; the workflow-scoping lake reads only the
de-identified signature stream. (The gateway already HAS the identity it must-drop; the .05
lake just doesn't drop it yet.)

**How the layers map onto real resources (the payoff — it's mostly extension):**
- **L0 capture** = the richer distill on the existing 100%-coverage hook (detailed above):
  hooks the `app/tools.py` dispatch where `log_call` already fires; de-identifies in the hot
  zone; the de-identified signature lands in `opal-mcp-audit`, read via Athena
  (`opal-mcp-athena-results`).
- **Ephemeral identity (the hot-zone) is ALREADY present:** the ALB authenticate-oidc + the
  per-user delegated-token brokering means the gateway holds per-user identity in-process —
  exactly the ephemeral identity the hot-zone uses for session-stitch + k-anon distinct-actor
  counting, then **drops at `_emit`/distillation**. The privacy model rides the identity the
  gateway already has-and-discards.
- **L2/L3 + archetyping/analyses** = Athena queries over `opal-mcp-audit` (the de-identified
  signature lake). One R8 substrate, many consumers.
- **L5 routing** rides the same `server.py` request path — the live "route-at-moment-of-need"
  recognizer sits where the offline miner's capture sits: one engine, two time-horizons, one
  process.
- **Governance** inherits OPLMCP's discipline: EC2 via safe-ec2-deploy + S3-artifact-store,
  Terraform-managed infra, Secrets-Manager secrets, and the **kill-switch + per-user blocklist
  already exist** (the mutating-workflow safety controls are partly built).

**Net:** the principal net-new build is the token-level semantic-signature distill (L0), the
mining/ranking (L2/L3), the interview/scope UX (L4), and synth/verify (L5) — bolted onto an
OPLMCP gateway that already gives us the traffic chokepoint, the per-user identity, the
tool-level audit, the R8 lake, and the kill-switch.

## Open questions
1. Segmentation algorithm for units-of-work in an interleaved MCP stream (L1).
2. Semantic-signature granularity (tool+intent vs +entity-type-roles vs full embedding) (L2).
3. Archetyping method: unsupervised clustering vs seeded taxonomy; where labels come from (L2).
4. The confidence-vs-value ranking policy + the trained artifact-rejection classifier; its
   cold-start before L4/L5 labels exist (L3).
5. Strawman-synthesis quality + the fallback-ladder threshold that picks the rung (L4).
6. The exact privacy abstraction: minimal shape captured such that mining works but no
   content/PII is ever stored (L0); hot-zone TTL vs interview-targeting coupling (L0/L4).
7. Verification oracle for generated workflows, esp. mutating ones (L5).
8. Route-at-moment-of-need: the offline mining engine doubling as the live router (L5/rail).
9. Workflow lifecycle: drift-detection + retirement criteria for deployed workflows (L5).

---
*Scoping riff, not a build order. Sequence against OPLMCP .05 (R8 lake) landing. Owner:
0.0.0_AB_MSTR. Sovereign: Andrew.*
