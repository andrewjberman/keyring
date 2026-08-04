# TO Vocabulary Census — the wild set, enumerated

**archetype:** DIAGNOSE
**Author:** 1.0.0_SA_CTO · 2026-08-04 ~0150Z
**Method authority:** COO binding instruction (010502Z, 2026-08-04): *enumerate from the WILD SET, not the states we remember*; read status + assignee + body prose, never status alone.
**Feeds:** COO's pointer-convention disposition + the CTO-held vocabulary-split call (deliberate calm-board item). This census is INPUT to both; it enacts neither.
**Engines:** 4 scratchpad passes (`to_vocab_census.py`, `to_vocab_crosstab.py`, `to_vocab_normalize.py`, `to_vocab_tolevel.py`); detail JSONs preserved in session scratchpad.

---

## 0. Population — a predicate, not a roster

**PREDICATE: every `*.md` under any literal `task_orders/` directory component beneath `org/`, minus filenames matching `README|TEMPLATE|_INDEX` (3 files). N = 1,854.**

Reconciles with the carried 1,856 (~B's exposure census, Δ2 explainable by exclusion-rule
and same-night file churn). **Denominator lesson, banked in-line:** a first-cut
`find -path '*task_orders*'` (substring match) returned **1,998** — 144 phantom members from
paths merely *containing* the string. The census population must be a path-component
predicate; a substring roster silently inflates every percentage below by ~7%.

## 1. Axis 1 — the `status` field

### 1a. TO-level grain (first status-shaped field per file)

| measure | value |
|---|---|
| files with a TO-level status | 1,837 of 1,854 |
| files with **no status field at all** | **17** |
| distinct TO-level heads in the wild | **52** (documented vocabulary: 3) |
| documented trio (`staged/pending/complete`) coverage | 1,588 / 1,837 = **86.4%** |
| TO-level values carrying **prose past the token** | **289 (15.7%)** |
| files carrying **conflicting status heads** (2+ fields, different values) | **86 (4.6%)** |

### 1b. The undocumented tail is STRUCTURED, not noise

The 49 undocumented heads cluster into exactly the semantic families the 3-word vocabulary
cannot express — each cluster is a question authors needed to answer and had no field for:

| family | heads (count) | the unexpressible question |
|---|---|---|
| **closure MODE** (~120 values) | closed 85, done 12, complete-superseded 8, archived 4, closed-superseded 3, complete-as-superseded 2, delivered, executed, complete-verified, closed-verified, complete-partial, closed-scope-revised, complete-resolved-by-cascade, complete-empirically-fee-independent | *HOW did it close — verified? superseded? partial? by cascade?* |
| **liveness DEGREE** (~55) | active 37, ready 9, dispatched 8, queued 5, issued 2, in-progress, in_progress, executing, active-queued | *How live — assigned? GO'd? actually being worked this minute?* |
| **HOLD reason** (~10) | gated 3, held 2, on-hold, deferred, pending-ruling, blocked-on-base-0 | *Waiting on WHAT — a dependency? a ruling? Andrew?* |
| **terminal NON-success** (~35) | superseded 17, cancelled 14, cancelled-suspended 2, withdrawn-wrong-premise, dropped | *Ended without shipping — why?* |
| **one-off states** (~10) | cto-half, verified-live, built, scope-corrected, proposed, proposed-not-built, spec, accepted, leg-a-complete, graph-native, load-layer | partial-completion and artifact-stage states minted ad hoc |

**`pending` at TO level is only 74 files** — the 59-row exposure cut plus recently-flipped
items; consistent with the /to-check triage numbers.

### 1c. Syntactic fragmentation (all grains)

2,537 status-shaped values across THREE syntactic families: **XML tag 1,810 · XML/attr
`status="x"` 584 · markdown `Status:` line 143** — plus quoting variants (`"pending"`,
`"pending"/>`), markdown-bold prefixes (`** COMPLETE`), and a mojibake em-dash. Raw-text
equality over any two records is impossible today; any future lint normalizes first.

### 1d. Multi-grain collision

The SAME field name `status` carries TO-grain state AND nested-element state
(acceptance-criteria/check/dependency items: `met`, `functional`, `clear`, `required`,
`pass`, `fail`, `ok`, `will_engage`...) in the same files — 88 distinct heads at all-grains
vs 52 at TO grain. A parser that does not disambiguate grain reads a check result as a TO
state. (This census's own first pass did exactly that; pass 4 corrected it.)

## 2. Axis 2 — the assignee field

The ~B pair-diff finding (no shared field to drift against) is **the estate-wide
condition**, not a 7-pair quirk:

| field shape | files |
|---|---|
| `issued_to` only | **1,481** |
| `assigned_to` only | **248** |
| markdown `To:`/`Assignee:` only | 54 |
| none found | 65 |
| `issued_to` + md `To:` | 6 |

Two disjoint field-name populations (1,481 vs 248) that **no diff, lint, or equality check
can ever compare** — structurally unobservable disagreement by construction, estate-wide.
**134 assignee values carry prose past the serials** (dispatch-holds, role notes, gate
text living inside the addressing field).

## 3. Axis 3 — body free-text state signals

| signal | files |
|---|---|
| STAGED marker | 364 |
| gate language (GATED-ON / GO after / awaiting GO) | 322 |
| BLOCKED | 235 |
| SUPERSEDED | 222 |
| HELD / ON-HOLD | 205 |
| PARKED | 47 |
| **DO-NOT-DISPATCH** | **46** |
| **ANDREW-GATED / ANDREW-RESERVED** | **15** |
| **DO-NOT-ISSUE** | **7** |

## 4. THE HAZARD CLASS — looks-dispatchable-but-held: **31 files**

Status head reads live (`pending/staged/ready/active/queued/issued/open/dispatched`) while
the body carries **DO-NOT-ISSUE / DO-NOT-DISPATCH / ANDREW-GATED**. **AMD-P3a is member 1
of 31, not an outlier.** 13 sit in COO's own `task_orders/` folder; 9 carry the
Andrew-authority marker specifically.

⚠ **These are RECALL candidates, not confirmed findings** — the marker regex cannot
distinguish "this TO is held" from a body *discussing* holds. The precision layer is a
record-read, which is exactly COO's carried AUG-4 triage method (read each RECORD, never
filter status). Full list with per-file signals: `held_but_live.json` in the census
scratchpad; the 31 paths are reproduced in Appendix A.

## 5. Where did the state go, and why did it leave

1. **State left `status` because the vocabulary could not express what authors needed**:
   closure mode, liveness degree, hold reason, and the difference between *waiting for GO*
   and *never GO without Andrew*. Every cluster in §1b is one of those unexpressible
   questions answered in the only field that never rejects a value — prose.
2. **The dangerous migration is authority state**: 46 DO-NOT-DISPATCH + 15 ANDREW-GATED +
   7 DO-NOT-ISSUE live ONLY in prose, while the parseable field says `pending`/`ready` —
   producing the 31-member hazard class. CI-R7R8 (invisible P0) and AMD-P3a
   (Andrew-reserved item reads dispatchable) are the two failure directions of the same
   defect, and §4 shows the second direction has 30 more standing instances.
3. **The field split (issued_to vs assigned_to) removed the possibility of detection**:
   with no shared field, drift between spec copy and lane copy is unobservable by any
   mechanical check. Detection cannot be retrofitted; the field must unify or the
   duplicate must die (path-only pointers).
4. **A field whose value never varies conveys zero bits** (the 14-pair-file observation
   generalizes): at TO level, `complete`+`closed`+`done` variants are 1,530+ of 1,837 —
   the status field is overwhelmingly a tombstone marker, and the live-state minority is
   exactly where the vocabulary breaks down.

## 6. What this recommends (proposals — enacted by their owners, not by this census)

- **[COO — convention disposition]** The census independently strengthens **path-only
  pointers**: the field-name split is estate-wide (§2), so parity-check options are dead
  on arrival everywhere, not just in the 7 pairs.
- **[COO — AUG-4 triage]** Appendix A is a ready worklist: 31 record-reads, ranked with
  Andrew-authority markers first (9 files).
- **[CTO — the vocabulary split, when ruled]** The wild set says the minimal sufficient
  split is **5 exclusive states** (LIVE · STAGED-AWAITING-GO · HELD(reason=dependency|
  ruling|ANDREW) · CLOSED-SUCCESS · CLOSED-NON-SUCCESS(mode)) **+ 2 orthogonal
  annotations** (closure-mode, liveness-degree) as separate fields — every compound token
  in §1b decomposes into state+annotation with zero loss. **HELD(ANDREW) must be a
  first-class parseable value**: it is the one state whose prose-only existence spends
  sovereign authority when missed (§4). Ruling deferred to the calm-board window per the
  standing CTO hold; this section is the evidence base, not the ruling.
- **[any future lint]** Normalize the three syntactic families before comparing; resolve
  grain by position (TO-level = first status field); never read nested-element status as
  TO state.

## Appendix A — the 31 looks-dispatchable-but-held files

Andrew-authority marker (andrew_gated and/or do_not_issue) — 9 files:
1. `org/projects/NFRA_COMPLEARN/task_orders/NFRA_COMPLEARN.AMD-P3a.leg3-producer-robustness.md` (pending; do_not_issue + do_not_dispatch + andrew_gated) — the known member; DO-NOT-ISSUE ruled binding across copies 08-04
2. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_AGENTBUS.AB-ACTIVATE.wire-real-fleets-live.md` (staged; do_not_dispatch + andrew_gated)
3. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_COMPTEAM.B2-ACTIVATE.provision-real-teammate.md` (staged; do_not_dispatch + andrew_gated)
4. `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADHC_GLDINC.P1.ae-load-flows-watermark-plumbing-proof.md` (active; andrew_gated)
5. `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/DATA_SSOTMG.CUTOVER-1.ae-ec2-unattended-canonical-chain.md` (staged; andrew_gated)
6. `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_VELOCITY_ESTATE.WS-E5.estate-sensors-recall-denominators.md` (pending; andrew_gated)
7. `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_VELOCITY_ESTATE.WS-E8.c3-state-labeling-series.md` (pending; andrew_gated)
8. `org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_COMPSIMILAR.PH1.corpus-resource-summaries-table.md` (pending; andrew_gated)
9. `org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_KUZUSPLIT.P0-P1.instrument-and-split-commands.md` (pending; andrew_gated)

DO-NOT-DISPATCH only — 22 files:
10. `org/projects/NFRA_COMPLEARN/task_orders/NFRA_COMPLEARN.AMD-P3b.leg4-activation-goodhart.md` (pending)
11. `org/projects/NFRA_COMPLEARN/task_orders/NFRA_COMPLEARN.AMD-P3c.ingestion-honesty-disclosure.md` (pending)
12. `org/projects/NFRA_GRAPHDEPTH/task_orders/NFRA_GRAPHDEPTH.P3.depth-scoped-tooling.md` (staged)
13. `org/projects/NFRA_PASSCRAFT/task_orders/NFRA_PASSCRAFT.TO-1.recon-scaffolding-sdk.md` (pending)
14. `org/projects/NFRA_PASSCRAFT/task_orders/NFRA_PASSCRAFT.TO-2.toolaudit-cse-schema-emitter.md` (pending)
15. `org/projects/NFRA_PASSCRAFT/task_orders/NFRA_PASSCRAFT.TO-3.backfill-3-toolpasses.md` (staged)
16. `org/projects/NFRA_TOOLGRAPH/task_orders/NFRA_TOOLGRAPH.TO-1.tool-graph-nodes-edges-coupling-diff.md` (pending)
17. `org/projects/NFRA_TOOLGRAPH/task_orders/NFRA_TOOLGRAPH.TO-2.assurance-plane-trino.md` (staged)
18. `org/projects/NFRA_TOOLGRAPH/task_orders/NFRA_TOOLGRAPH.TO-3.effective-wire-promote-gate-join.md` (staged)
19. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_CMTQUE.TO-6R.loadtest-run-phased-cutover.md` (pending+staged conflict)
20. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_COMPILERKIT.P2.config-compiler.md` (ready)
21. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_COMPILERKIT.P3.ticket-compiler-cross-plane.md` (ready)
22. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_COMPTEAM.A1.agent-kit-refresh-striplist-gate.md` (ready)
23. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_COMPTEAM.B2-DESIGN.scoped-read-partition-design.md` (ready)
24. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_INFRPT.P3.contract-integrity.md` (ready)
25. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_SCTY.W1W2.w1-w2-closeout.md` (ready)
26. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_SCTY.WS2.vendor-partner-diligence.md` (ready)
27. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_SCTY.WS4.ai-agent-fabric-hardening.md` (ready)
28. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_SCTY_PREMCP.P2.network-isolation-broker-review.md` (pending)
29. `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_SEMCTL.GOV-B.hot-registration-seam.md` (ready)
30. `org/tier2_senior/0.8.0_AE_CloudComp/task_orders/ADHOC.comp-tool-universe-audit.md` (staged)
31. `org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_GRAPHUNI.SFNBRIDGE.trace-graph-sfn-invoke-edges.md` (pending+staged conflict)

## Compiler Tools

| tool / probe | result | note |
|---|---|---|
| custom census passes (4 scripts, scratchpad) | PASS | No comp-tool models TO-record field vocabulary (comp-state is BM25 drift over commits — a different question); `comp-which` routes estate/code questions, not org-record grammar. Population predicate printed every pass. |
| denominator control | **CAUGHT** | substring `find` overcounted 1,998 vs predicate 1,854 — the census's own first number was wrong by 144 files; §0 records the mechanism |
| grain control | **CAUGHT** | pass-3 read nested-element statuses as TO states (88 heads vs true 52); pass-4 corrected by position rule; §1d records it |
