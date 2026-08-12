# FANOUT 07 — C2/C3.i naming + the C3.i↔C3.ii bridge (verbatim agent report, received 2026-08-12 ~21:15Z)

**Agent scope:** how C2 motifs and C3.i structures get their names; how the bridge (bound_pairs /
cross-partition matrix / dual key) actually works; what breaks under inferential C3.ii. **Evidence
class: agent-derived; the FIFTH-ACT claim was GROUND-CHECKED at the CRO seat same hour — the merge
record read at `C3II_COMPREHENSIVE_SEMANTIC_COVERAGE_SCAN_20260811.md:66-73` (a CRO~B deliverable,
"routed"), and the resolver re-measured NOW: 29 named_threads, BOTH mdpf and model-portfolios still
present. The drift is live.** The agent's report arrived as a consolidated addendum (its item 6, the
enforcement census) with prior-cited lines re-verified; two background sweeps (motif-catalog detail,
chain-census reconciliation) were still running at delivery and can only add detail per the agent.

---

## ADDENDUM — Item 6 completed: the invariant enforcement census

**Headline: the C3.ii invariant is CITED in prose at 8+ sites and ENFORCED by 0 executable gates.**
Phrase-sweep denominators (over `org/ docs/ infra/ .tools/ .claude/`, incl. gitignored): `DECLARED,
never discovered` **12 hits/9 files** — 12/12 prose; `DISCOVERED, never declared` **10/9** — 10/10
prose (one, `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/channel_sources.py:11`, is an
unrelated COT-depth invariant); `Emergence proposes` **7/5** + `legislation admits` **13/10** — 19 of
20 prose; `DECLARED-BUT-CHAINLESS` **5/5** — exactly 1 in code; `naming act` 343 (mostly inbox
traffic); `declared_but_chainless` (underscore) **0**.

**Every candidate gate, classified:**

| Site | Verdict |
|---|---|
| `opal_estate_infrastructure.py:634-641` DECLARED-BUT-CHAINLESS | `footer()` print, `return 0` — **not a gate**, and currently dead code (declared−used = ∅) |
| `estate_infrastructure_cli.py:429-451` `--validate` (`unbucketed` check, real `sys.exit(1)`) | **tautological** — the roster it checks against is built at `gen-estate-resolver.py:93` as `set(seen) \| set(resources_by_named_thread)`, i.e. the union of the values being checked; `unbucketed = []` by construction |
| `estate_infrastructure_cli.py:630-666` gate-b/gate-c (real `sys.exit(2)`) | **one-directional** — loop driven by `golden_fixtures.json`, so a resolver vertical absent from fixtures is never visited; a new undeclared vertical with new lambdas passes silently. Latent today (29==29) |
| `estate_infrastructure_cli.py:294-299` unknown-name rc=2 | read-side query rejection only — rejects a typed name, not a written membership |
| `comp_ontolint.py`, `manifest_check_cli.py` | **0 hits** for `named_thread`/`vertical` — no C3 checks at all |
| `c3ii_declared_plane_join.py:429-441` `RETIRED_BY_NAMING_ACT` | classifier label, falls back to `UNCLASSIFIED... not guessed` — nothing fails |

**The one real "emergence proposes; legislation admits" enforcement in the estate is in a DIFFERENT
system and does not touch the vertical roster:** `infra/aws/terraform/estate-report/iam.tf:3-8,120-142`
— an IAM **negative** grant (`Sid = "WriteOwnOutputPrefixesOnly"`; producers can write
`daily/*`+`manifest/*`, the reviewer surface is absent by design, *"because a producer that can write
the review surface can RATIFY ITS OWN PROPOSALS"*) — plus its software half
`estate_report_runner.py:179,186-189,2009-2015` (PROSE_FIELDS allowlist, drop-on-violation,
canon_set universe check). MEASURED: `named_thread` occurs **0 times** in that runner — it cannot
mint a vertical, and nothing in it defends the roster either.

**Naming acts on record: 4 of 29 (+2 assigns), all in one pass.** Durable records are two free-text
strings — `estate-coverage-manifest.yaml:26-31` (`adjudications_20260730`) and
`AUTHORITATIVE_lambda_taxonomy.json:196` (rows :185-191) — plus commit `97dc3e07b6`. The cited act
register, `NAMED_THREAD_CATALOG.md` (`RULE_BANK.yaml:685-687`), is a **2026-06-15 census seed** (167
lines, organized by chain, no date/authority/reason fields, **zero** occurrences of
etf-reports/ceo-digest/ticketing) — the other 25 verticals were read off the estate and then treated
as declared, **which is the invariant's own inversion.** The proposal-side record is
`ESTATE_WORLD_MODEL_PROCESS.md:97-108` (candidate clusters *"awaiting Andrew's naming word"* — a
human loop, no tool).

**A FIFTH act exists with NO durable record — live, gate-invisible drift:**
`C3II_COMPREHENSIVE_SEMANTIC_COVERAGE_SCAN_20260811.md:66-73` records mdpf+model-portfolios **MERGED
2026-08-07 (Andrew) → ratified roster = 28**, but resolver, fixtures, catalog, and `--matrix` all
still carry **29** (re-measured this session; CRO seat re-confirmed post-delivery: resolver = 29,
both names present). A ruled naming act that never reached the record, undetected by every instrument
above — the exact event class the invariant exists to prevent.

**"A matrix change is an adjudication event recorded with its reason" has no recording mechanism.**
4 prose citations (`C2C3_CANONICAL.yaml:205-207,24-30`; `RULE_BANK.yaml:709-710`; CVO handoff
`2026-07-30_1714Z.md:16`); **no** adjudication log/ledger file exists (`*adjudicat*` filename sweep:
15 files, none a C3 register; `*matrix*` under `org/modules/graph/`: 0); no LD-NNNN records the four
acts (`etf-reports|ceo-digest` in `org/tier0/ledger/`: 0 files). The matrix is view-compiled per
invocation and never persisted — git history on the two source files is the de-facto register,
unindexed and schema-less.

## Corrected/confirmed citations from the main report (all MEASURED directly)

- Exploration motif catalog: **21 families** counted from the tables (9 A + 4 B + 7 C + 1 D), doc
  self-describes "~20", `NFRA_ONTOLOGY_CANONICAL_MOTIF_CATALOG.md:16-53`, status line 4 still
  `DRAFT -- RAVC MSTR + CTO`; mined from 92 typed shapes of 197 distinct (:9-12).
- 13 A+B detectors: `NFRA_MOTIF_P1_canonical_ab_catalog.py:510-512` — `len(AB_CATALOG) == 13 and
  sum(... plane == "A") == 9`.
- "The exploration catalog PROPOSES, the ratified catalog ADMITS" — `RULE_BANK.yaml:345`
  (`motif_topology` under D2), confirmed verbatim.
- Motif-instance mint (hash, no name): `kimi_subdivision_harness/c2_individuate.py:429` —
  `mid = "motifi:%s:%s"`; materialized instances beside it in `c2_instances.json` (33,094 matching
  lines).
- Andrew's inferential ruling + 0.001%:
  `ANDREW_DIRECT_20260812_C4_DISSOLUTION_C3II_INFERENTIAL_KIMI_ESTATE_PIPELINE.md:40-46`, verbatim at
  :42; :46 restates *"emergence proposes nearly everything; legislation admits at ~0.001%"* — still
  no denominator attached anywhere in the file.
- **Potion axis dead as proposer at C3.ii grain:**
  `C3II_COMPREHENSIVE_SEMANTIC_COVERAGE_SCAN_20260811.md:139-150` — **zero admits on all 28 verticals
  at fw/p999/p99 with the positive control firing (self-cosine 1.0, 15 admits), so a TRUE negative**;
  per-vertical verdict rides BM25 null-gated. Corpus denominator :131 — **5,865 docs** (1,009 docs /
  307 projects / 4,549 logs).
- CRO discovery script disclaimer: `c3ii_prd_vertical_discovery.py:27` — *"IT NAMES NOTHING. Naming
  is sovereign; this surfaces candidates and their evidence."*

**Agent's closing note:** two background sweeps (motif-catalog detail, chain-census reconciliation)
still running at delivery; every claim above independently verified by direct measurement in-session,
so their completion can only add detail, not change any verdict stated.
