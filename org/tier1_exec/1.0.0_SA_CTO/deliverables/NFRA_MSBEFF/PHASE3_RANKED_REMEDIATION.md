# NFRA_MSBEFF Phase 3 — the framework's weakest cells, ranked, with owners + acceptance tests

**Charter tie-back (Andrew, §0):** *"I should be able to query an agent very lightly with all the
preexisting opal context and have what I want be immediately obvious, and the context to complete
that request be immediately obvious... the missing layer is truly understanding state and
dependencies, which the tools should solve for."* Phase 3 converts the audit into a ranked build
list against exactly that bar.

**Evidence base (all committed, all grounded):** Phase-0/1 telemetry (21,775 log rows + 6,954 jsonl
runs), the M2→M3 correction (true mech failure ~0.87%), Case Study 1 (per-RF grid + CS1-1..4), and
718 verified NL findings (0 fabricated quotes). Governance: comp-tool **standard** changes route to
main CTO before landing; ~Z owns measurement/remediation/doctrine; 0.8.0 builds; CVO~Z verifies once
for the PSTMRT family.

## The one-paragraph conclusion

**The framework is CORRECT and BROAD but BLIND AT ITS EDGES and UNTRIGGERED.** Tools rarely crash
(0.87% true). They fail by (1) answering confidently about a **smaller world than the query assumed**
— coverage invisible at query time (FAILED_COVERAGE 253/718 = 35%, top class; comp-pipescript alone
95); (2) answering from the **wrong vintage without saying so** (47 findings); (3) **not firing at
the moment work happens** (comp-state 0 runs during a live drift). The three efficiency layers map
cleanly: MECHANICAL = coverage + vintage; SEMANTIC = discovery + coverage-visibility; BEHAVIORAL =
triggers. **Andrew's "state and dependencies" gap is named verbatim by an agent:** *"comp-* cannot
answer a DATA-FLOW question ('does this assign a value that did not come from the canonical
source?')"* — the single highest-value missing capability, and it is a SEMANTIC/MECHANICAL gap, not
a behavioral one.

## Ranked remediation cells (impact x frequency x leverage; each with owner + acceptance)

### R1 — COVERAGE-VISIBLE-AT-QUERY-TIME (SEMANTIC standard; the highest-leverage single change)
**The defect:** a tool answers about what it models and is silent about what it does not — so a
covered-sounding question returns a confident answer about a smaller world (comp-pipescript blind to
dynamic-keyed I/O; comp-blast "indexes only 23 COMPONENT nodes"; comp-iam "DESIRED only"). 46+
findings; the root of the 35% coverage class.
**Remedy:** every comp-tool answer carries a **coverage statement** — its denominator and what it
structurally cannot see — as a standard output contract (generalize the mdpf-preflip-check /
item-7 denominator-printing convention). This is exactly PSTMRT's "print the denominator of every
scan" doctrine, applied to the tool *surface* instead of one gate.
**Owner:** main CTO gate (STANDARD change) → 0.8.0 builds the shared output helper → CVO~Z verifies.
**Acceptance:** a sampled set of tools, run against a target they partially cover, emit a coverage
line an agent can read; a mutant (a tool that covers 0% of the target) says so LOUD, never returns a
clean empty.

### R2 — THE DATA-FLOW / CANONICAL-SOURCE QUERY (the charter's named gap; new capability)
**The defect (agent-verbatim, signal 3):** *"comp-* cannot answer a DATA-FLOW question ('does this
assign a value that did not come from the canonical source?')"* + *"the compiler-graph doesn't model
field-threading at the typed-shape boundary"* + *"the converse (endpoint reads X; new feature data
lives in Y) is not checked."* This IS "truly understanding state and dependencies."
**Remedy:** a `comp-dataflow` capability — trace a served/consumed value back to its producing
assignment and flag when it does NOT originate from the declared canonical source. Overlaps the
PSTMRT layer-grammar gate (item 9: no producer reads a served artifact) — build them as one family.
**Owner:** ~Z designs (charter fit) → 0.8.0 builds → CVO~Z verifies. **NOT a standard change**
(new tool). **Acceptance:** exercised on RF-7 (49F counts imported from a legacy served artifact) —
the tool must flag it; negative control on a clean canonical read must pass.

### R3 — VINTAGE-HONEST OUTPUT (MECHANICAL standard; 47 findings + this week's 3 live catches)
**The defect:** tools answer from a stale plane and do not say so — comp-iam DESIRED-vs-APPLIED, the
doc-of-record staleness family, the M2 wrong-artifact read, the appender frozen verdict set. 47
findings. comp-kuzu's provenance header is the estate's own proven good pattern (praised in-corpus).
**Remedy:** a **provenance/vintage header as a standard output contract** — every tool states the
plane it read (DESIRED vs APPLIED, graph vintage, source-vs-projection) so "which vintage?" is
answered before it is asked. Composes with R1 (coverage + vintage = the full "what am I looking at").
**Owner:** main CTO gate (STANDARD) → 0.8.0 → CVO~Z. **Acceptance:** a tool reading a stale plane
emits the vintage; a mutant staleness is discriminable from a fresh read in the output text.

### R4 — CLOSEOUT/DEPLOY TRIGGERS FOR THE UNRUN TOOLS (BEHAVIORAL; the widest gap by stakes)
**The defect:** capability present, nothing fires it — comp-state 0 runs while RF-15 registry drift
sat; dump_enriched_templates never run in 4 months (RF-14); *"No tool detected the deploy gap
automatically pre-run. Today's PROD bd-gold-trigger fired against 4 stale S3 scripts."*
**Remedy:** bind the record/deploy tools to the moments their answer matters — comp-state on a
**project closeout/supersession** trigger (auto drift sweep), comp-pipescript-deployed on a
**deploy-completion** trigger. This is TRIGGER_LAYER doctrine applied to tools, not findings: move
them from *available* to *fires at a moment of work*.
**Owner:** ~Z doctrine + the trigger design → 0.8.0/hook lane builds → CVO~Z. **Acceptance:** a
staged project-close with an injected registry drift auto-fires comp-state and surfaces it; a deploy
with a stale script auto-fires the deployed-check.

### R5 — THE KEY/PARTITION ENUMERATION PRIMITIVE (MECHANICAL; measured rail demand)
**The defect:** 178 aws_freshness rail-overrides are mostly NOT freshness questions — they are
"which keys/partitions exist" (CS1-4). Agent-verbatim: *"no comp-tool enumerates per-table partition
dates"* · *"comp-freshness lacks an arbitrary/raw-prefix mode."* Highest measured override demand.
**Owner:** ~Z specs → 0.8.0 builds (`comp-freshness --raw-prefix` mode or a `comp-keys` primitive) →
CVO~Z. **Acceptance:** the two repeat override-intents (earliest-partition discovery, per-firm served
key existence) run through the tool with no rail override; rail-override rate for aws_freshness drops.

### R6 — PHANTOM-NAME + RETIRED-TOOL RECONCILIATION (SEMANTIC hygiene; cheap)
**The defect:** the log referenced 129 tool names vs 83 registered — ~46 phantoms, incl. retired
tools still cited/invoked (coverage-map 39x, tool-hud 18x, learns-backlog 22x). Record-vs-reality
drift inside the instrument layer — the same class the whole family exists to close, at the
telemetry layer.
**Owner:** ~Z (measurement leg) → sweep the docs/HUD/prompts for retired names; where a name still
routes, fix the pointer. **Acceptance:** a phantom-name scan over docs+HUD returns 0 retired-but-
cited names; comp-manifest-check gains a retired-alias check (ties to R-registration).

### R7 — comp-which DISCOVERY REDESIGN (SEMANTIC; already ~Z-owned, confirm scope)
**The defect:** comp-which is 1.3% of chosen flow and its misroutes are coverage-in-disguise + the
argmax-as-confidence defect (observed live, corpus-confirmed). It fails safe (routes to grep) but the
signal is noise.
**Owner:** ~Z (already redesigning per the corpus quote). **Acceptance:** near-tie/low-confidence
queries render as "no confident route + here is the fallback" rather than a spurious argmax; a query
no tool covers routes to comp-grep with that stated, not a false match.

## The interim already in flight (not new — tracking)
The M3 appender fix (VERDICT_EXIT_TOOLS derived from comp-tools.yaml contracts) is gate-approved and
building at 0.8.0 — it is R3's first concrete instance (a tool no longer miscounting its own verdict
plane) plus a registration-invariant precedent R1/R6 reuse.

## Sequencing recommendation (to main CTO via MSTR for the standard-gated items)
1. **R1 + R3 together** (one shared output-contract change: coverage line + vintage header) — the
   highest leverage, one standard-change proposal, one build. 2. **R4 triggers** (~Z doctrine, no
   standard change, high behavioral payoff). 3. **R5 + R2** (new capabilities, measured demand). 4.
   **R6 + R7** (hygiene + the redesign already underway). Phases 4+ (the remaining 4 NL chunks) only
   refine frequencies — they do not change this ranking.
