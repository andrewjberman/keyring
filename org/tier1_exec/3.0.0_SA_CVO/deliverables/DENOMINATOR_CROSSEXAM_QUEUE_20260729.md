# DENOMINATOR CROSS-EXAMINATION QUEUE — questionable tools ranked by measured usage

**Author:** 3.0.0_SA_CVO · 2026-07-29 ~17:25Z · **archetype:** VALIDATE
**Andrew-direct:** *"anything without an explicit denominator that fits into this category, do a
cross-examination based on tool-call counts from the mcp comp-tool jsonl and the session logs and
see what is called the most, rank the questionable tools by frequency of use and lets go down the
line from there analyzing and refining as needed."*

**Method:** questionable = UNCLASSIFIED ∪ `declares_denominator_in_output:False` ∪
`knows_own_denominator:False` ∪ (PERSISTED + non-kuzu universe). Usage cross-examined from BOTH
sources: `org/mcp/comp-tool-runs.jsonl` (9,758 rows, 07-14→now, real clock) and
`org/compiler-tools-log.md` per-run rows (27k, longer history). 7d column = current relevance.

**Headline: 82 of 89 tools flag** — the class is systemic, not a few offenders. 63 have measured
usage; **19 flagged tools have ZERO measured usage ever** (a /prune-quant retirement census in
waiting, incl. comp-whoread — a SIMULATE-class tool nobody has invoked).

## The queue (top 20 by combined use; walk order = 7d-weighted)

| # | tool | combined | jsonl | 7d | md-log | flags |
|---|------|----------|-------|----|--------|-------|
| 1 | comp-surface-check | 13,849 | 3,671 | 1,217 | 10,178 | no-denom-in-output, denom-unknowable |
| 2 | comp-pulse | 6,642 | 3,307 | 1,132 | 3,335 | denom-unknowable |
| 3 | comp-kuzu | 3,515 | 924 | 313 | 2,591 | no-denom-in-output, denom-unknowable |
| 4 | comp-pipescript | 2,937 | 145 | 95 | 2,792 | no-denom-in-output, denom-unknowable |
| 5 | comp-system | 1,212 | 592 | 480 | 620 | denom-unknowable |
| 6 | comp-iam | 958 | 217 | 185 | 741 | denom-unknowable |
| 7 | comp-blast | 777 | 97 | 52 | 680 | persisted-non-kuzu-surface |
| 8 | pipescript | 644 | 66 | 41 | 578 | UNCLASSIFIED (→ comp-opalbizsem, ~C WS1) |
| 9 | comp-routes | 527 | 116 | 95 | 411 | persisted-non-kuzu-surface |
| 10 | comp-manifest-check | 521 | 192 | 121 | 329 | denom-unknowable |
| 11 | comp-transform | 419 | 25 | 19 | 394 | no-denom-in-output, persisted-non-kuzu |
| 12 | comp-platinum | 377 | 28 | 10 | 349 | no-denom-in-output, persisted-non-kuzu |
| 13 | comp-validate | 278 | 24 | 22 | 254 | no-denom-in-output, persisted-non-kuzu |
| 14 | comp-aws | 261 | 20 | 13 | 241 | denom-unknowable |
| 15 | comp-trace | 254 | 2 | 2 | 252 | persisted-non-kuzu (historical; near-dead now) |
| 16 | comp-lambdamap | 177 | 32 | 9 | 145 | no-denom-in-output, persisted-non-kuzu |
| 17 | comp-build | 162 | 4 | 4 | 158 | persisted-non-kuzu-surface |
| 18 | comp-cache | 159 | 34 | 23 | 125 | denom-unknowable |
| 19 | comp-types | 140 | 28 | 24 | 112 | persisted-non-kuzu-surface |
| 20 | comp-drift | 121 | 10 | 3 | 111 | denom-unknowable |

## FIRST-PASS FINDING (before any per-tool walk): THE CARDS DRIFT IN BOTH DIRECTIONS

The refresh_mechanism field over-credits (stamps "gate-enforced at registration" on tools whose
DATA is snapshot-frozen — pipescript's 44d resolver PASSES a staleness query; registration-fresh ≠
data-fresh — the field-semantics split is ~C's WS3). And the top of this table shows the INVERSE:
**#1 and #2's cards under-credit their own behavior** — comp-pulse PRINTS a full denominator every
run ("N file(s) checked against 1484 danger node(s) — a MEASURED result, not a default") and
comp-surface-check prints its examined count, yet their cards flag them. Observed dozens of times
this session at commit time. **So the walk is not only "fix tools" — it is "reconcile card vs
BEHAVIOR per tool," in whichever direction the drift runs.** A card that under-credits teaches
agents to distrust a sound instrument; one that over-credits teaches them to trust a hollow one.

## Walk order (7d-weighted, skipping what is already in flight)

1. comp-surface-check + comp-pulse (2,349/7d combined — hook-embedded, so every commit inherits
   their card truth; likely card-fix not tool-fix)
2. comp-system (480/7d — the ~Z parity instrument; card claims vs its --check output)
3. comp-kuzu (313/7d — the canonical substrate itself; provenance header vs card)
4. comp-iam (185/7d — already has the deepest known-insufficiency record; card should carry it)
5. comp-manifest-check (121/7d) · comp-routes (95/7d) · comp-blast (52/7d — persisted surface,
   what snapshot does it read?)
SKIP as in-flight: comp-pipescript (WS4), pipescript (WS1/opalbizsem). PARK: the 19 zero-use
flagged tools → /prune-quant census after the walk.

---

## WALK ITEM 1 — comp-surface-check + comp-pulse (~17:40Z, both exercised live, isolated runs)

**comp-pulse: MODEL CITIZEN — CLEARED, and it corrects the QUEUE, not the tool.** Observed output
carries the full contract already: invocation echo, **source vintage** ("danger map: 14.1h old" —
it implements the header contract today), a TWO-SIDED denominator ("N file(s) checked against
1,484 danger node(s)"), and measured-vs-default discrimination. Its card's
`declares_denominator_in_output: True` is accurate; its only flag was my filter counting
`knows_own_denominator: False` as questionable — **which is the HONEST value for a TRAVERSED
tool** (denominator built at run time). Self-correction recorded: the v1 predicate over-flagged.

**comp-surface-check: HALF-DECLARED — one-line output fix, routed to ~C.** Observed: "OK: 1
changed file(s) touch no critical surface." — declares the EXAMINED count but NOT the screening
population (against how many critical-surface rules?). The estate's single most-invoked instrument
(13.8k combined) states half its denominator; its portal-side twin BLOCKS commits at SEV1 moments,
where the population matters most. Fix: adopt pulse's two-sided form — "OK: N changed file(s)
touch no critical surface (screened against M critical-surface rules)". Card is accurate as-is
(`declares: False` — correct today, flips True with the fix). `refresh_mechanism` over-credit
(registration-fresh ≠ data-fresh) applies to both tools' cards — already in ~C WS3.

## QUEUE v2 (refined predicate: UNCLASSIFIED ∪ no-denom-in-output ∪ persisted-non-kuzu;
pure knows_own=False dropped as honest-TRAVERSED): **60 of 89 flagged.** Walk order by 7d use:
surface-check(1227) → **kuzu(313)** → [comp-pipescript 95 = WS4 in-flight, skip] → routes(95) →
blast(52) → [pipescript 41 = WS1, skip] → trigger(25) → types(24) → validate(22) → transform(19)
→ residue(13) → platinum(10) → lambdamap(9) → constants(9). **NEXT: comp-kuzu.**

## WALK ITEM 2 — comp-kuzu (~18:05Z, exercised live; the exercise TRIGGERED the auto-refresh)

**Verdict: HEADER-CONTRACT EXEMPLAR; TWO CARD CORRECTIONS; behavior CLEARED.** The live run
demonstrated the whole freshness machinery under observation: BEHIND-HEAD detected (pin ≠ Nessie
HEAD from today's 15:04Z chain write) → designed daily ground-truth FULL rebuild (CTO condition 2,
self-labeled NOT-a-defect) → dead rebuild lock correctly stolen (heartbeat stale 1,465s — the
discriminator working) → provenance block: **20,447 nodes / 40,912 edges (a printed denominator),
snapshot IDs both tables, built-at WITH AGE, "Nessie HEAD: current."** This tool is where the
header pattern comes from, and it is honest under load.
- **Card fix 1:** `declares_denominator_in_output: False` is WRONG — the provenance header IS the
  population+vintage declaration (per-query result shapes are user-defined; the tool-level
  denominator is the graph, and it is declared). → True.
- **Card fix 2:** `cost_band: SECONDS` is wrong at the tail and it BITES (my own probe hit the
  120s harness timeout and got backgrounded): the refresh-triggering path is MINUTES by design.
  Card needs the bimodal declaration (SECONDS typical / MINUTES on HEAD-advance or daily reset) —
  an undeclared cost tail trains agents to kill a healthy rebuild mid-flight, which is plausibly
  exactly where the stale lock I stole came from.

## WALK ITEM 3 — comp-routes (~18:10Z, exercised live)

**Verdict: CLEARED — post-reform exemplar; the flag was a CARD ARTIFACT.** The header is the
estate's most thorough (COVERAGE/BLIND/PLANE/VINTAGE with DESIRED-plane-only declared, the
catch-all-/*-is-a-DEFAULT disclosure, firm-parametric bucket REFUSAL, the fail-loud rewrite parser
that replaced the drifted transcription, and named residuals carrying their own honest-fix notes).
Output opens with a counted denominator ("CLOUDFRONT BEHAVIORS (25)"). **Card fix:** `state:
PERSISTED / universe: "authored ledger"` is wrong — the tool parses cloudfront TF + Lambda@Edge
routers + api-gateway TF + portal/src AT WORKING-TREE HEAD per invocation. It reads no snapshot;
its vintage line says so itself. → state: derived-at-invocation (SOURCE), universe: the parsed
source set.

## META-PATTERN AFTER 3 ITEMS (load-bearing for the rest of the walk)

**The reformed tools are exemplary; the CARDS lag the reforms.** comp-pulse, comp-kuzu,
comp-routes, comp-dataflow all carry post-O2/MACHINEFLAG-era headers with denominators, vintages,
and named blindness — and all were flagged by REGISTRY fields classified before or during the
reform wave. Three of three walk items so far produced CARD corrections, zero tool defects (the
tool defects live where already known: surface-check's half-line, comp-pipescript's WS4 set, the
pipescript reroute). **The queue is mostly a card-refresh queue.** Implication for ~C WS3: after
the field-semantics split, a RE-CLASSIFICATION pass over the reformed tools is the bulk fix —
per-tool walk continues to catch the exceptions.

## WALK ITEM 4 — comp-blast (~18:45Z, exercised live on dim_mdpf_aggregate_aua_timeseries)

**Verdict: HONEST-BUT-ANSWERS-ANYWAY — one behavior refinement, two card fixes.** The tool opened
with the best staleness declaration of the walk: `STALE_NODE_WARN: 35 node(s) have source-file SHA
drift since last comp-build`, per-node indexed→current SHAs, and the remediation named
(`rerun comp-build`). Then it **built the trace graph and answered over the drifted index anyway**
(2,252 nodes / 2,944 edges in 104.4s). The warn is excellent; the proceed is the gap: a blast
radius involving any of the 35 drifted nodes (which tonight included `endpoint:getMdpfAggregate-
AUATimeSeriesByFirm` — MDPF-central) is UNVERIFIED-AT-CURRENT-SHA and nothing in the answer says
which parts. **Refinement (→ ~C queue, small): tag result rows that traverse drifted nodes, or
offer `--fresh` to auto-comp-build first.** Card fixes: `cost_band: SECONDS` → bimodal (104s
build-on-invoke tail — same class as kuzu's); `universe: authored ledger` → hybrid (persisted
index + graph built at invocation from git+registry). The drift-declares-but-proceeds pattern is
WEAKER than kuzu's auto-refresh and STRONGER than silence — worth naming as the middle tier of
the freshness ladder: auto-refresh > declare-and-proceed > silent-stale.

## WALK ITEMS 5-6 — comp-trigger + comp-types (~18:50Z, exercised live)

**comp-trigger: CLEARED — the two-system reform is its opening line** ("census — 143 events-rules
+ 11 schedules, region us-east-1"), per-row trigger-system labeled, ENABLED/DISABLED state shown.
Card fix: `state: PERSISTED / universe: authored ledger` wrong — it reads LIVE EventBridge +
Scheduler at invocation (the very tool that closed today's list-rules blindness cannot be
classified as a snapshot reader).
**comp-types: CLEARED** — "Validated against 752 known portal declarations" + counted consumer
sites (10) + timing. Card: declares=True correct; universe should name the portal source set.

## WALK PHASE-1 SUMMARY (top of queue done: 6 walked + 2 in-flight skips)

Six of six walked tools are BEHAVIORALLY SOUND; every finding was card-side except two small
output refinements (surface-check's half-denominator line; blast's drift-traversal tagging). The
deliverable of this walk is therefore: **(a) the card-correction list for ~C's WS3
re-classification pass** — pulse, kuzu(×2), routes, blast(×2), trigger, types — **(b) the two
output refinements, (c) the freshness ladder** (auto-refresh > declare-and-proceed >
silent-stale) as the classification vocabulary for the new data_refresh field. Remaining tail
(validate 22/7d, transform 19, residue 13, platinum 10, lambdamap 9, constants 9) queues for a
batch pass with the same expectation; the 19 zero-use flagged tools remain the /prune-quant
census candidate.

## RETRACTION (~18:40Z, ~C's WS3 census + my own re-verification): THE "PHANTOM ROW" WAS MY FALSE FINDING

**`comp-v5-composite-test` IS NOT A PHANTOM — `.tools/comp-v5-composite-test.sh` exists (4,894 B,
May 26; `ls`-verified by me after ~C's catch).** My probe checked the bare stem; the file carries
`.sh`; I read a suffix-blind predicate's miss as "NO FILE ON DISK" and filed it as "the sharper
finding" — **the unprinted-predicate class, committed by the prosecutor mid-prosecution.** ~C's
inversion warning stands verbatim: the delete-the-row remedy I implied would have DE-REGISTERED a
real tool, and the later re-flag would never have been connected to the deletion. Same suffix
class: `comp-which-routing-test.py`. Same predicate-blindness inverted: ~C's own comp-* glob
missed bare-named `pipescript` and they caught themselves before filing it. **The 93-vs-89
"discrepancy" also dissolves: 94 FILES vs 90 LOGICAL TOOLS vs 89 master rows — five dual-file
tools double-counted, two suffixed-only tools missed; two honest instruments, two predicates,
reconciling by COUNT would have manufactured a defect.** Propagated-to and now corrected-at: CTO
(163837Z/171426Z threads), MSTR (custody note), ~C dispatch. The UNCLASSIFIED-4 finding itself
STANDS (classification empty for all four) — only the phantom characterization retracts.

— 3.0.0_SA_CVO
