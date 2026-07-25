# NFRA_TOOLUNIFY — CONSOLIDATED ESTATE MAP (audit complete, all 5 lanes CVO~Z-verified)

**author:** `1.0.0_SA_CTO~Z` · 2026-07-25 · **status:** AUDIT COMPLETE — decision input for "how we handle it"
**verification:** `3.0.0_SA_CVO~Z` re-derived every load-bearing claim at source; all 5 lanes PASS.
**lane deliverables (committed):** base @d4f80d742e · A @7df3559a26 · B @488d580 · C @163ec2ce5 · D @7490d459f7
**plan of record:** `docs/briefs/NFRA_TOOLUNIFY_ESTATE_CENSUS_PLAN_20260724.md` @6fd377d78

---

## 0 · The two findings that outrank the rest

**(1) THE STORE IS 93% OUTSIDE THE ONTOLOGY IT NOMINALLY HAS.** Of the federated cloud truth's 20,403
nodes, only **6.7% carry a type name matching its own governing vocabulary** (the GLOBGRPH PRD's 41 declared
classes). CVO~Z-verified decomposition:

| Bucket | Types | Nodes | Share | Remedy |
|---|---|---|---|---|
| Exact-name match to declared vocabulary | 14 | 1,372 | 6.7% | — |
| Declared concept, different name (vocab drift) | 13 | 1,384 | 6.8% | **alias table — hours** |
| Genuinely undeclared | 31 | 17,647 | 86.5% | **ontology must be authored** |

**It is a GRAIN gap, not neglect.** The PRD describes *resource-grain* topology (Lambda, S3 key, EventBridge).
The store has since grown a *symbol-grain* code-semantic plane it was never written for (`Field` 4969,
`JSXElement` 2205, `PipelineFunction` 1201, `TypeDecl` 807…) plus M365 (`MS_FILE` 4618, `MS_FOLDER` 1034).
Counter-control (CVO~Z, against its own framing): `LOG_GROUP` 233 is a plain *resource* type and is also
undeclared — so bucket C is not purely the semantic plane.

**(2) THE THROUGH-LINE — "a control that works and is inaudible reads exactly like health."** SIX instances of
ONE class, independent, in one night. The first five are controls that RAN and were inaudible:
- `stitch` CodeBuild: 20/20 nightly builds FAILED across its whole lifetime (07-07→07-24), heard by no one
- `opal-critical-surface-alerts`: 476 unconsumed messages, 0 consumers, email-to-Andrew subscription missing live
- `ms_heat`: real analytic, zero scheduled trigger, no consumer (its `comp-ms-find` route never shipped)
- `mdpf-daily`: event-only, no schedule (the pre-existing frozen-with-fresh-inputs class)
- two raw-cache readers (fixed @68bbf3dd2): no vintage guard at all

**The SIXTH (CVO~Z, from ~A's residual-24) is higher severity — a control you can READ in the tree that ISN'T
in the runtime at all.** NARROW, VERIFIED FACT: nine source directories — `bd-49f-freshness-probe`,
`bd-cot-freshness-probe`, `inf-gold-freshness-guard`, `mdpf-freshness-checker`, `bd-served-vintage-alarm`,
`opal-assets-absence-check`, `schwab-bronze-freshness`, `security-sweep-daily`, `market_query` — have **no
deployed Lambda counterpart under any name** (live substring search: zero live Lambdas contain "freshness"/
"vintage"/"absence"/"security-sweep"). **MANDATORY LIMIT — DO NOT DROP IT:** this is NOT "the estate has no
freshness guards" — that would be a false-outage claim of exactly the class CLAUDE.md's first NEVER-rule
forbids. The intended function may be served elsewhere (another Lambda, a Step Function, a CloudWatch alarm,
an EC2 job, or a local comp-tool — `comp-freshness` demonstrably exists). What is established is exact: THESE
SOURCE DIRS HAVE NO DEPLOYED LAMBDA UNDER ANY NAME. Whether served elsewhere is **UNVERIFIED**, and verifying
it is the necessary next investigation before any gap is asserted.

CVO~Z's assessment, which I share: the census was chartered to unify tools; what it produced is a six-instance
census of **controls that do not reach the runtime** — inaudible, unconsumed, unscheduled, or entirely
undeployed. That may be a more urgent program than tool consolidation, found BY it. Candidate REFRAME (§7).

---

## 1 · The complete real estate (verified, corrected from my first pass)

**THE FEDERATED CLOUD TRUTH = `NFRA_GLOBGRPH`** — a Nessie-git-branched Iceberg lakehouse, live, 46 refs.
- **10 TRUE Iceberg tables** (base correction — `metadata/` dir is the signature; Glue-registration ≠
  Iceberg): `graph_nodes`, `graph_edges`, `graph_contracts`, `resource_summaries`, `code_heat_snap`, `cse`,
  `cse_test`×2 (UUID anomaly), `fedobs_coevolution_snap`, `fedobs_coverage_snap`, `ms_heat_snap`. The other
  ~9 (`code_heat`, `tool_activity`, `fedobs_obs_findings`/`signals`, `axes_history`, `cse_ingest`,
  `snap_ingest`, `ms_heat`) are plain S3 parquet/JSON *beside* the core.
- **`kuzu` is a projection, not a second graph:** `kuzu_nessie_db` ← materialized from a Nessie snapshot.
  Deployed-plane counts verified exact: LAMBDA live=191=kuzu · EventBridge 141 (3-way base/~A/~C) · SF/SQS/
  S3/DynamoDB kuzu=live. Genuine kuzu staleness: IAM roles live=206 vs kuzu=193 (20.6h cohort).
- Maintained by `incremental_updater` Lambda (best-engineered piece found: DLQ + per-record isolation +
  retry/backoff + SNS-on-exhaustion — a positive pattern to propagate).

**THE LOCAL DEVICE END (the bridge's open span):**
- `.comp-graph/graph.json` = a **local working-tree scan** (source_sha = `sha256(bytes)[:12]`, NOT a git blob
  hash → no LOCAL↔COMMITTED drift capability today; self-heal guard covers 1,907 of 2,255 nodes). **It is a
  LIVE object during any census** — any tool reading it on SHA-drift triggers a full rebuild.
- Its LAMBDA=333 is the **outlier**, polluted (~A-corrected post-CVO~Z): `extract_s3.py`'s unbounded
  `rglob("*.py")` walks into pip-vendored dep trees (a vendored openai SDK under
  `portal_data_proxy/_build_tmp` — a **Rule-3 violation site**). Corrected breakdown: 208 matched (live/
  registry) + 82 phantom (73 vendor-confirmed + 9 org-dir-noise) + 19 alias-excess + **24 residual, now
  triaged: 11 deployed-under-a-different-name (benign), 9 = the §0.2 sixth-instance undeployed-guard dirs, 4
  ambiguous/test**. Crucially, graph.json's LAMBDA labels cover **191/191 live Lambdas exactly — zero
  missing**; the earlier "3-short residual" was itself a classifier false-positive that hid ~30 real deep-
  nested Lambdas (rebuilt on a live/registry cross-reference, not a path-shape guess). Full 333-node
  classification in `A_lambda_enumeration.json` for CVO~Z's random sample.
- **Git is partially surfaced — my "nowhere" was wrong:** core graph.json/kuzu carry zero git, but
  `nerves_traffic.py`/`nerves_accrete.py` walk `git log` and persist `CO_CHANGE` edges (nerves-edges.json,
  6688 commits/35d). Portal is a gitlink **5 commits behind its pinned pointer, no `.gitmodules`** — a live
  drift instance. Both repos' primary branches ≈ 21,992 commits; two-repo identity has no shared ID space.

**M365** is a **POPULATED PLANE** (5,669 `layer='ms'` nodes, growing) but **rides as a `layer` property on the
shared CloudNode label — it is NOT one of the declared 7 layers.** `ms_heat` analytic dormant, no consumer.

**THE TOOL SURFACE:** 92 rows (91 `comp-*` + pipescript; reconciles to 84/85). All 5 source classes live;
77/92 tools (84%) read 2+ surface types (genuinely multi-valued). `comp-residue` is unregistered (BLOCKED by
the registration invariant, live-confirmed). graph.json has a **dual vintage-discipline split** inside one
tool's closure (GUARDED-REBUILD primary vs SILENT via the `nerves_resolve.py:73` fallback).

---

## 2 · The bridge, as it actually stands

`LOCAL` (working-tree scan, polluted) —▷ `COMMITTED` (partial, via nerves CO_CHANGE only; no first-class
plane) —▷ `DEPLOYED` (the Nessie/Iceberg truth). The **cloud end is built and versioned**; the
**LOCAL↔COMMITTED span is the open work**, and the reconciliation the sovereign asked for is a bridge across
these with drift as a computed property.

---

## 3 · The central architecture question (mine to rule; Andrew's steer invited)

**Does one ontology span resource-grain AND symbol-grain, or are those two declared planes under a shared
identity?** My lean, consistent with the unity directive: **one ontology with grain as an explicit typed
dimension** — a Lambda-the-resource and a function-the-symbol coexist under one vocabulary and "which grain"
is a queryable property, not a separate store — plus (a) the cheap alias table for the 6.8% vocab drift and
(b) the real work: authoring vocabulary for the genuinely-undeclared 86.5%. Not yet ruled.

---

## 4 · Defect themes (FINDINGS — audit-first, not repaired)

1. **Inaudible-controls theme (§0.2)** — the through-line. `stitch` is **retired-by-design but never deleted,
   AND its replacement never actually worked.** The cloud CodeBuild failed 20/20 AND the local post-commit
   replacement has failed 83 straight since 07-08 (CVO~Z re-derived with `grep -a` — the log carries non-UTF8
   that silently truncates a plain grep). **There has been NO working producer for `stitch_graph.json` since
   the day it froze** — the replacement's only 17 "successes" were against a hand-regenerated TEST snapshot
   that never generalized to real input. So the remedy is NOT "finish the retirement" alone; a working
   producer must be established. Corrected, ordered remedy: (a) finish the 07-07-ordered cloud decommission
   (silently failing 18 nights past its retirement date); (b) **investigate `EXTERNAL_ENDPOINT=0` IN PARALLEL,
   not after** (path-independent — 0 in both cloud and local); (c) recalibrate `grain_baseline.json` against
   legitimate growth **only after (b)** — recalibrating while EXTERNAL_ENDPOINT is stuck at 0 would BAKE THE
   ZERO IN and blind the sentinel to the very thing it is currently, correctly, refusing to publish over.
   Alerts don't land (476 unconsumed, missing email sub).
2. **graph.json pollution** — 82 phantom Lambda nodes (73 vendored-dep Rule-3 site + 9 org-dir-noise) + 24
   unexplained inflate the LOCAL plane; the cloud truth (kuzu=191) is clean.
3. **Rule-4 drift** — 4 live Lambdas missing from the CI source-map, 5 registered-but-undeployed.
4. **Tool-map local-variable-binding miss class** (~D 6 misses, CVO~Z-found) — **RESOLVED**: an artifact bound
   to a local var and read through it lost its name (and could hand a call site a confidently WRONG binding —
   the `comp-types` cross-function collision). Fixed via function-scoped const + return-value resolution; the
   fix surfaced that **`comp-iam` writes its own DERIVED-CACHE** (a self-producer of what it later reads —
   notable). CVO~Z source-confirmed it (`extract_iam.py:116` returns the cache path, `:133` writes it) and
   recommends **`SELF-PRODUCER` as its own register role_flag**: production and consumption share ONE trust
   boundary — no external producer, no external watcher to catch a stale/bad write — on the tool Rule 22a
   already flags as failing GREEN (it cannot distinguish `(action)` from `(action,resource)` AND reads a
   vintage only it governs). The compound is worse than either half.
5. **Terraform/manifest gap** (Andrew-direct to base): plain object-store prefixes have zero Terraform
   declaring their purpose; `derive-build.tf` CodeBuild has no trigger config found.

## 5 · The acceptance properties CVO~Z earned (for the PRD) — two halves, both from findings against its OWN instrument
**(5a) Every instrument — INCLUDING the verifier's oracle — must state its own false-positive rate and be
validated against ground truth before its output is actioned.** CVO~Z's held-back control was itself 32%
false-positive (comments, docstrings, a `.endswith(".metadata.json")` suffix predicate matched as a filename);
it caught that only by validating its hits before reporting. An oracle inherits every disease of the thing it
measures.

**(5b) A fix must be verified by a before/after diff over the WHOLE output, not only against the known failures
it was meant to close.** Re-checking the known misses proves the fix works; only the full diff shows what else
MOVED — silent corrections of rows that were wrong all along, and regressions the fix itself introduced. Both
occurred in ~D's single rework: the diff surfaced a real wrong attribution in the *originally-delivered*
register (`comp-types` → `.fields.yaml` where source says `.blast.yaml`, confirmed at `types_cli.py:352/:355`)
that the held-back control was **structurally blind to** (an omission-detector cannot see a confidently-wrong
answer — the row exists and looks resolved), AND caught a regression the rework introduced before it shipped.

**Corollary for WS-2:** a register can score 100% on every control anyone thought to write and still contain
confidently-wrong rows. **The count of surfaced items is not a quality measure.**

**The honest symmetry (on the record, NOT a ranking):** CVO~Z's instrument found 6 omissions the lane missed;
the lane's instrument found a wrong attribution CVO~Z was structurally blind to; and CVO~Z's was separately 32%
false-positive. **Two instruments, two different blind spots — the argument for having both, not for either
outperforming the other.** ~D's classifier ships tracked + durable (`NFRA_TOOLUNIFY_CENSUS_TOOLS/` @2779752ac)
with its residual limitations documented inside its own module docstring — the packaging discipline the brief
argued for, shipped before the PRD exists.

## 6 · Open items
- **VERIFICATION COMPLETE.** CVO~Z checked ~A's 333-node classification exhaustively (106/106 non-live
  confirmed); 191/191 live coverage stands. All 5 lanes verified, zero open verification items.
- **NEXT INVESTIGATION — required before any gap is asserted (§0.2 sixth instance):** are the 9 GROUP-2
  source dirs (freshness/vintage/absence/security-sweep) served elsewhere — another Lambda, a Step Function,
  a CloudWatch alarm, an EC2 job, or a local comp-tool — or genuinely undeployed? Until answered, the finding
  is "no deployed Lambda counterpart under any name," NEVER "no guard exists" (NEVER#1 / false-outage).
  **→ RESOLVED 2026-07-25 (`~A`, REC1C_A.md §7, pending CVO~Z verification): 6 of the 9 were REAL, DEPLOYED,
  AND DELIBERATELY TORN DOWN by CTO-approved clean-house passes — each with a matching CTO-GO teardown
  commit citation, all six self-described git-recoverable. The remaining 3 were NEVER-DEPLOYED (one with an
  explicit author-stated "NOT deployed" commit message). So the sixth-instance reading softens materially:
  these are not silently-lost controls — the majority were consciously decommissioned, on the record. The
  full 24-residual closure (GROUP1 11 renamed-deployed via CVO~Z's earlier addendum + GROUP2 9 + GROUP3 4,
  incl. `data_refresh` → `opal-data-refresh-api` via live TF citation) leaves 0 unresolved.**
- ~D rework CLOSED: CVO~Z re-ran the SEALED held-back control (unchanged file) = **41/41** (up from 35/41,
  zero misses, both comp-iam caches in). The whole-output before/after diff also caught a real wrong-
  attribution in the ORIGINAL register (`comp-types`, §5b) and a rework-introduced regression, pre-ship.
- `cse_test` dual-UUID cause (needs Nessie REST, VPC-internal) — the one residual data-access limit.

**AUDIT STATUS: FULLY CLOSED.** All 5 lanes landed, CVO~Z-verified, and every rework/condition re-verified.
No open verification items. The estate is established; the decision space (§7) is Andrew's.

## 7 · The decision space for "how we handle it" (Andrew)
1. **Scope/reframe:** stay TOOLUNIFY (tool consolidation), or elevate the inaudible-controls through-line to
   the primary program and make consolidation a workstream under it? CVO~Z and I both think §0.2 may be the
   bigger object.
2. **The grain ruling (§3):** confirm one-ontology-with-grain-dimension, or split declared planes.
3. **Author the 86.5%:** commit to authoring symbol-grain vocabulary, or declare it out-of-ontology-by-design.
4. **PRD now?** WS-1's feasibility is *proven* (~D built a depth-4 sound instrument that beat the verifier's
   oracle) — the register seed exists. We can write the PRD against a verified estate whenever you say.

## 8 · Andrew's sequencing ruling (2026-07-25, session terminal, post power-crash restoration)

**VERBATIM:** *"Start with REC1, lets just get TOOLUNIFY sorted completely, then I think we can get into
COMPLEARNS from the perspective of putting the denominator expansion self-healing delta loop stuff into
play. There should be some /ontology docs on implementation describing these threads in greater detail"*

**Reading, surfaced not adjudicated beyond this:** REC-1 (exercise the register's `failure_mode` column,
seeded by the §0.2 six-instance through-line) is GO — dispatched to `0.8.0_AE_CloudComp~D` this turn,
`3.0.0_SA_CVO~Z` holding the positive-control+mutant bar. **§7.1 (REC-2, GRAPHLEARNS-as-WS-8) reads as
NOT ruled the way the fork's fork proposed** — Andrew sequenced COMPLEARNS as the NEXT program after
TOOLUNIFY closes, not folded in as a TOOLUNIFY workstream. The original separation ruling (*"This is a
separate project than GRAPHLEARNS and ARCHTOOL, we will return to those later. This will be TOOLUNIFY
under the NFRA macro"*) stands; this adds a sequencing slot, not a merge. Grounding docs for the
COMPLEARNS phase when it opens: `docs/architecture/NFRA_COMPLEARN_PRD.md` (the self-learning ratchet
loop — Behavior/Estate/Change federation, scheduled worklist), `docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md`
(the denominator doctrine), `docs/architecture/NFRA_TOOLARCH_PRD.md` (archetypes->patterns->tools,
sequenced behind this program's R-series), `docs/architecture/NFRA_ONTOLOGY2_PRD.md` (the D1/D2/D3 grain
rails).

**WS-4 (crosswalk build)** was also affirmed clean by the prior-session fork review (correct-but-hold,
now buildable) but was NOT explicitly named in this ruling — holding it pending an explicit go, since
Andrew named REC-1 specifically ("start with REC1").

## 9 · Fleet recovery + COO~Z stand-up (2026-07-25, same session, post power-crash)

MSTR restored live by Andrew. **VERBATIM (Andrew, same terminal):** *"I brought on MSTR, they can help,
ask them to bring on COO~Z as well to help you coordinate, just make sure that when they launch them
that we are all clear this is purely NFRA work; we're not getting into the MDPF stuff just yet"*

Routed to MSTR: (1) respawn `0.8.0_AE_CloudComp~D` + `3.0.0_SA_CVO~Z` (crashed with the rest of the
fleet; REC-1 dispatch already queued in their inboxes), (2) spawn `2.0.0_SA_COO~Z` fresh to help
coordinate the NFRA/~Z program, **STRICTLY NFRA-SCOPED — explicitly NOT MDPF**, per Andrew's own words.

**For the record, not adjudicated:** the `~Z` group was previously NO-COO by design (fabric-shape note:
*"~Z GROUP ... NO COO (COO~Z killed 07-20)"*). This is a deliberate, explicit reversal by Andrew, not an
inferred one — flagged to MSTR so the scope boundary (NFRA-only, no MDPF bleed) is stated at COO~Z's
launch, not assumed.

## 10 · Andrew's ruling on the advisory doc's two open items (2026-07-25, same session)

Reviewed `docs/briefs/NFRA_TOOLUNIFY_ADVISORY_NEXT_STEPS_20260725.md` (found uncommitted on disk, not
authored this session). Presented CTO~Z's recommendation on its two contested items; Andrew's reply,
verbatim: *"Agreed proceed it."*

**Q6 — RESOLVED, separate (not folded in).** GRAPHLEARNS/COMPLEARNS stays a **separate project, sequenced
after** TOOLUNIFY closes — NOT adopted as TOOLUNIFY's own WS-8/L3 phase. This confirms, does not reverse,
Andrew's original separation ruling and his §8 sequencing. The advisory doc's Q6 section is HELD, superseded
by this entry. **Exit-bar concept adopted from the advisory anyway** (it doesn't depend on the fold-in
question): TOOLUNIFY is "done enough" to open COMPLEARNS when (1) the crosswalk conformance suite (WS-4)
passes and (2) the register is enforced as a gate (WS-7), not maintained by care.

**Scope widening — GO on the cheap/bounded pieces, HOLD on the new-commitment pieces:**
- **GO now:** the hardcoded-path hook fix (un-blinds the census's own measurement instrument — CTO~Z
  fixing directly) + widened REC-1 (criticality-ranked: exercise `GATE-BLOCKING`/`PRODUCER`-flagged tools
  exhaustively, sample the rest — dispatched to `0.8.0_AE_CloudComp~D`, same acceptance discipline as v1).
- **GO, but as its own scoped TO, not bundled into REC-1's lane:** the missing SNS subscription fix
  (`opal-critical-surface-alerts`, 476 unconsumed messages) — real Terraform/deploy work, heavier discipline
  than census read-only reporting, needs its own acceptance criteria.
- **HELD, not started:** WS-4 crosswalk build, PRD-the-frame. REC-1's widened pass may surface more first;
  revisit after it lands.
