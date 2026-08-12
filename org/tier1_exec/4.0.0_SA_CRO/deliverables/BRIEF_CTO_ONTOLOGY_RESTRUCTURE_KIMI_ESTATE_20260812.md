# BRIEF TO CTO — the ontology restructure: C4 dissolution, inferential C3.ii, and the Kimi Estate Pipeline

**Author:** `4.0.0_SA_CRO` · 2026-08-12 · **Commission:** Andrew-direct R5 (@8447ad7293, verbatims there)
**Evidence base:** `deliverables/KIMI_ESTATE_FANOUT_20260812/` — 7 verbatim agent reports + index,
all committed. **This brief is a MAP over those files, not a replacement** (Andrew-direct persistence
instruction, mid-fanout). Citations `[F01]`..`[F07]` point at them; every figure re-derivable there.
**Routing:** CTO arch-gate. Research proposes; CTO gates; COO decomposes; nothing here dispatches.

---

## 0. WHY ONE COHERENT RE-DERIVATION, NOT POINT EDITS — the measured argument

The last ratified-line inversion landed as point edits (the 07-20 `layer`->`estate` migration,
against a spec that said "do not half-land"). **Measured residue 23 days later, live in production:
1,337 nodes on `pipeline` (retired at v1.9) + 23 on `semctl` (dropped 07-20) = 1,360 nodes carrying
values the law had already retired, and the ratified value `codebase` at ZERO nodes.** Nobody noticed
for three weeks. R1/R2 invert ratified lines exactly as 07-20 did; this brief therefore lands as ONE
gated program with the rename first, or the same residue class compounds — two migrations' residues
in one column, mutually unattributable.

**Sequencing spine (your arch-call 184153Z, adopted, extended):**
```
S0  layer->substrate column rename            (discharges 07-20; AE lane, your gate, CVO verify)
S1  Subject seed map + propagation             (needs S0's clean column)
S2  grid-membership computation + annotation carrier   (the two builds C4 deletion depends on)
S3  C4 rung dissolution                        (cheap once S2 exists -- one code read)
S4  C3.ii inferential loop via Kimi Estate Pipeline    (wiring, mostly -- see section 5)
S5  registry v3.0 + Layer mint                 (Layer stays staged until S0, per the v2.1 changelog)
```

## 1. C4 COMPRESSION/DELETION — cheap, with two prerequisites that do not exist yet [F04, F03]

**The whole code surface is ONE line** — `opal_estate_infrastructure.py:660` is the only code read of
`c4_segments` in 26,104 files. C4 is not in the graph (0 rows), has no snapshot (positively
controlled), no gate/hook/CI dependency. Deletion cost: `cmd_segments()` + one argparse flag + the
`tool_index.py` routing rows + prose in 4 ontology docs.

**But R1's "membership computes from the grid" assumes a computation that DOES NOT EXIST** — the 38
slots are hand-assigned; zero code reads `c4_subject_function_grid`. And the annotation layer that
absorbs `high_signal` + `flags` does not exist either — seven annotation-like stores measured, none
keyed on world-model entities [F03 §7]. **Prerequisite builds:**
- **B1 grid-membership resolver:** segment = a named query (`subject:client` etc.) evaluated over
  Subject/Function values. ~Small; lands with S1.
- **B2 annotation carrier:** extend the `keep-dormant.yaml` schema pattern (the richest existing:
  8 required fields, >=40-char reason, file:line cite, `revalidate_by` TTL whose expiry renders
  STALE and never auto-promotes) re-keyed to world-model entities (vertical/structure/thread ids).
  TTL is non-negotiable — a stale annotation is worse than none, and the 90-day dormancy default is
  the natural clock. The live `sys-causality-engine RETIREMENT-PENDING` flag is migration case #1.

**Also owed in the same act:** the `andrew-infrastructure` rename landed in prose but NOT in the
`c4_segments` data key — the tool serves the retired name today [F04 §3]. And the RULE_BANK carries a
duplicate `c4_verticals` block still reading RATIFIED + "DECLARED, never discovered" — it contradicts
R2 and must be struck with this program, not before [F04 §6].

## 2. WHAT "INFERENTIAL" MEANS OPERATIONALLY [F06, F01]

**Named honestly: the exercised inferential instrument is BM25, null-gated, ablated — with the
semantic axis retired at gate severity.** The C3.ii scan already ran (5,865 docs x 28 verticals x 25
decoys, on the laptop): **Potion admitted ZERO at every threshold with a firing positive control;
BM25 carried 1,824 admits.** Three agreeing derivations. The design's own recovery bar stands: a
semantic axis re-enters only by recovering what BM25 structurally misses, measured on the bm25-ABSENT
set. So R2's "potion/nlp etc analysis layer" = **BM25-led, null-gated, ablate-don't-fuse, decoy-null
thresholds — Potion on probation against the recovery bar** (candidate fixes: bigger model (8M),
doc-shaped queries, different pooling — all testable against the existing artifact).

**Run shape: scan-and-persist on schedule, never standing index infrastructure.** The estate tore
down its only vector DB in 2025-12 as unused cost; there is no vector store, no packaging path for
Potion to AWS, and the full ML stack lives on this laptop only [F06]. The deployed compute substrate
is sufficient: ECS `opal-globgrph` (7 task families, nightly producer pattern) for batch scans; the
transient self-stopping EC2 runner for LLM calls. The scan output persists like `c2_instances.json`
does today — an artifact, adjudicated, then landed.

**MS is a special case with a hard gap [F01]: 47.2% of documents (PDF/docx/pptx) have NO
text-retrieval mechanism in the estate** — the gateway ships zero extraction libraries ("Full
document text-extract is an honest follow-on", its own docstring). The producer is metadata-only,
triple-enforced. **So R3 (MS inferential off Potion NLP) requires a text-extraction leg first**, or
phase-1 MS classification runs on metadata only (name/path/owner — weak but honest). Also owed before
any bulk MS scan: Graph 429 handling (none exists anywhere), the `_TOP=200` pagination truncation,
and the 12.1% denominator contamination (.git internals crawled as documents). Recommend: MS subject
classification is **phase 2**, after the AWS/portal-plane loop is proven.

## 3. WHAT THIS MEANS FOR C3.ii [F07]

**R2 is legitimized by the record, not just ruled:** the "DECLARED, never discovered" invariant is
prose-only — cited 8+ sites, enforced by ZERO executable gates (every candidate classified: one dead
print, one tautological check, one fixture-driven one-directional gate, one read-side rejection).
Only 4 of 29 verticals have naming acts on record; the other 25 were read off the estate and treated
as declared — the invariant's own inversion. **And the fifth act proves silent drift:** Andrew's
08-07 mdpf+model-portfolios merge (ratified roster = 28) never reached resolver/fixtures/catalog/
matrix — all still carry 29, re-verified live at this seat. A declared layer with no enforcement
drifts exactly like an undeclared one, minus the honesty.

**C3.ii becomes:** a naming layer over BM25-proposed candidates. The loop: scheduled scan proposes
(candidate clusters + evidence) -> Andrew admits at ~0.001% (the thin margin, via the Kimi user-input
channel) -> the act lands in a DURABLE REGISTER that does not exist today and must (the matrix
"adjudication event recorded with its reason" has NO recording mechanism — git history on two source
files is the de-facto register). **B3: the naming-act register** — append-only JSONL (act, authority,
date, reason, roster-after), and the resolver/fixtures/catalog regenerate FROM it. That single build
closes the fifth-act class permanently. First entry: the 08-07 merge, backfilled with its authority.

**Immediate hygiene riding S4:** propagate roster 28; retire the `CATALOG_ORDER` hand-list (carries
retired `attribution`, missing the three 07-30 admits) [F03 §5d].

## 4. SEMANTIC-LAYER NAMING FOR C2 AND C3.i [F02, F07]

**The real problem is not naming convention — it is THREE disjoint populations sharing ZERO
vocabulary** (verified with positive controls): the canonical 12 prose families ("publish-serve") vs
the 19+4 live semctl detector nodes ("a-serve", "b-dataflow") vs the harness 6,138 instances / 1,255
structures (never landed). Every quoted coverage % measures the second; everyone reads the first.
**Unification IS the naming act:** ratify ONE family vocabulary, map detectors to it (the exploration
catalog's own law already says it: "the exploration catalog PROPOSES, the ratified catalog ADMITS"),
and land the harness populations into the graph under it. C3.i names stay naming-only (borrowing
C3.ii business names per the existing naming ladder); motif instances stay hash-minted (they are
not named things). Annotation (B2) carries everything else said ABOUT them.

## 5. THE C3.i<->C3.ii BRIDGE UNDER THE KIMI ESTATE PIPELINE [F05, F07]

**Ground truth: the pipeline is deployed, fired today, verified at three layers — and it is the
estate report; they are one system.** It proposes prose-field edits on 4 allowlisted fields against a
386-entity canon set; it CANNOT mint verticals (verified: `named_thread` 0 occurrences in the
runner); its IAM already enforces the one real emergence/legislation separation in the estate (the
producer cannot write the review surface — "a producer that can write the review surface can RATIFY
ITS OWN PROPOSALS").

**The rename to Kimi Estate Pipeline is mostly wiring, in order of leverage:**
- **W1 — close the user-input loop:** the text-input uploader is LIVE (6 days of captures in
  `text-input/`) and the runner reads ZERO of it — corpus frozen at 2026-07-30, its own stale
  docstring says why. This is the ~0.001% channel and the F3 operator-signal axis, already built on
  the upload side. One consumer change.
- **W2 — fold in the friction/state call kinds** (built, hand-fired, standing egress ruled 08-12;
  NOT in the deployed runner — 0 occurrences, ETag-verified). Adds the lifecycle/trajectory proposal
  stream that resolves `Lifecycle_Value` as an ANNOTATION on a vertical (the 12-day contest closes).
- **W3 — the bridge itself:** the dual key (family -> C3.i, named_thread -> C3.ii) already stamps
  chains; the matrix is the standing instrument. What changes: matrix deltas write to the B3 register
  as adjudication events, and Kimi proposals arrive AGAINST register state, never against the frozen
  census mirror.
- **Registry acts owed:** OPAL_KIMIPIPELINE project rename; its PRD is stale on both the instance-id
  (nonexistent) and the removed monolithic design; EC2_MANIFEST.json stale on two fields (Rule 8
  source of truth); the estate-capture-writer IAM path matches zero live objects (works only via
  ambient admin creds) — an AE fix, one line [F05 §10].

## 6. 100% COVERAGE AT DETERMINISTIC/INFERENTIAL — the honest arithmetic [F02]

**The ratified >=90% deterministic budget is arithmetically impossible at node grain with today's
detectors: the ceiling is 39.7% estate-wide** (in-detector-scope 8,179 / 20,616). Per substrate:
pipeline 100% ceiling (96.6% now — done), aws 77.7%, portal 46.3%, ms 0.0%. At instance grain the
same estate reads 82% — **the budget never says which grain binds, and the two answers straddle it.**

**Ruling needed (Andrew, via you): the Cascade budget's binding grain.** Recommendation: bind at
C0-node grain (the denominator independent of the instrument), re-derive the budget per-substrate,
and treat 90/9/1 as the TARGET SHAPE at maturity, not a day-one gate — the entry's own
"floors-of-honesty" clause already forbids force-fitting.

**The path to real coverage is catalog extension, not detector tuning — 10,375 nodes no detector
references:** portal 5,286 role-mapped-but-undetected nodes (the ratified RENDERS/PROP_PASSES
relations have NO consuming motif — build the frontend motif family: render-tree, data-fetch,
prop-flow); ms 5,886 (needs the MS anchor + extractor, phase 2 per §2); aws 458 out-of-scope types
(census then extend). TypeDecl 807 stays declared-out (correct). The inferential layer then covers
the residue the extended catalog still cannot reach — that is what <=9% is FOR.

## 7. SYSTEM_DEFINITIONS UPDATES (v3.0, one naming act, AFTER your gate)

Prepared, not landed: **C4** -> routing-index-over-grid, rung status removed; **World_Model** spine
re-derived (C3-headed traversal; grid + segments as entry views); **C3.ii** invariant rewritten
(BM25-proposed, register-admitted, ~0.001% human margin); **Cascade** re-derived per §6 ruling;
**+Annotation** (the B2 carrier, bounded by the already-ratified Observation_Not_Assertion);
**Lifecycle_Value** contest RESOLVED (an annotation on a vertical, not an attribute — its
"NOT YET ESTABLISHED as same object as lifecycle_class" closes: different layers); **Layer** minted
only after S0 (already staged in the v2.1 changelog); **Subject/Function** entries updated from
declared to derived-with-seed-map. Also: `estate` now carries three senses (Estate-totality,
subject:estate, scope-enum estate) — one token, three axes; a terminology_law note is owed.
⚠ Registry text stays ASCII — the U+26D4 crash class is fixed and must not return; the cmd_definitions
guard at `opal_estate_infrastructure.py:573` is still owed code-side (tool lane).

## 8. COMP-TOOLS UPDATES — particularly comp-estate [F03]

**Breaks (1 tool):** comp-estate `--segments/--matrix/--structure/--list/<vertical>` re-point from
`c4_segments` + resolver to grid + register; `--layers` doc rewrite (it serves falsified canon
verbatim, no drift check); the silent-degrade printer and the forbidden `denominator: 5 segments`
footer go. **Unaffected:** comp-kuzu, comp-which routing, the HUD, 64/76 routable tools.
**Live defects to fold in (found by the fanout, independent of the restructure):** `--refresh`
regresses `last_review` to a hardcoded 2026-06-15 (the staleness remedy makes it staler — and the
14d fuse trips 2026-08-14, the standing memory trigger); `c3-walk-agenda.py` resolves the lifecycle
enum by FIRST-MATCH regex (a Subject enum inserted above line 401 silently redefines it — fix before
S1 lands any new enum in the rule bank); `check_system_definitions.py` validates authority pointers
for presence only; three Potion supply chains consolidate to the vendored hash-pinned one-home.
**New capability:** the grid resolver (B1) and register (B3) become what comp-estate serves.

## 9. GROUND-CHECK ACCOUNTING (per the pre-registered table, committed before results)

**14 load-bearing agent-derived claims; 8 ground-checked at this seat; 3 cross-corroborated by two
independent agents; 3 UNCHECKED and flagged.** Checked: MS content cert + no-extraction-lib (L2, read
at source); zero-vocabulary overlap + ceiling arithmetic (L3, positive controls); the fifth act /
roster drift (L4, resolver re-measured live); the --definitions crash (L1, reproduced + fixed); the
Potion retirement (first-party artifact + two agent derivations); the layer census (first-party).
Cross-corroborated: C4 single-code-reader (F03+F04 independently); C4-not-in-graph (doc + file-scan,
different derivations); Kimi=estate-report identity (F05 internally at 3 layers). **UNCHECKED,
flagged, harmless-if-wrong-before-build:** the estate-capture IAM path mismatch, the EC2_MANIFEST
staleness, the MS _TOP=200 truncation specifics — all verify trivially at their build steps and none
gates a decision in this brief.

## 10. OPEN AT ANDREW (through you, or direct)

1. **Cascade binding grain** (§6) — the one ruling everything downstream sizes against.
2. **`build` as a fifth Function value** — settled empirically by the 29-vertical placement pass.
3. **`Deploy_State` axis key** — values ratified verbatim; the key is CRO-proposed, one word.
4. **TIER0_EXEC** — held by MSTR (their own agent home; interested party), still at Andrew.
