# CVO Certification — NFRA_GRAPHS D1-AC1 (graph-call-manifest full coverage)

**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-11 · **Verdict: PASS (substance) — all graph-query use-cases cataloged; one documentation-completeness gap surfaced (non-blocking).**
**Method:** independent enumeration of every `comp-*` executable on disk, diffed against manifest `entries` + `excluded_not_graph_use_cases`.

## What I verified
- Manifest `org/modules/graph/graph-call-manifest.yaml`: **40 entries** (39 `canonical` + 1 `planned`), **27 distinct graph-query tools**, `tools_index` = 27, plus **4 documented exclusions** (`comp-learns-run`, `comp-learns-status`, `comp-perf`, `comp-v5-composite-test`).
- The 1 `planned` entry (`meta.freshness.status` / comp-graph, "is each graph current?") is a legitimate known-future meta-use-case, not a missed canonical — the manifest is honest about it.
- Independent disk enumeration: **31** `comp-*` executables. Diff vs (entries ∪ excluded):
  - `comp-v5-composite-test.sh` = the already-excluded `comp-v5-composite-test` (extension artifact, NOT a gap).
  - **`comp-manifest-check`** = neither cataloged nor excluded → the one genuine accounting gap.

## The finding (off-by-one on "ZERO uncataloged")
`comp-manifest-check` is the **NFRA_GRAPHS D6 manifest-enforcement gate** (flags non-canonical graph access at commit; sibling of the D1 manifest it polices). It is correctly **not** a graph-query use-case — so AC1's *substance* (every way to query/derive/traverse the dependency graph is cataloged) **holds**. But because it is neither in `entries` nor in `excluded_not_graph_use_cases`, the literal "ZERO uncataloged" audit is off-by-one: an auditor re-running my disk-diff sees one tool unaccounted-for and cannot tell overlooked-vs-deliberately-excluded.

**Fix (routed to CTO, catalog owner):** add one line to `excluded_not_graph_use_cases`:
`- comp-manifest-check  # D6 manifest-enforcement gate — polices the manifest, not a graph-query use-case`
Then the disk-diff is self-evidently exact (31 = 27 cataloged-tools' use-cases + 4 prior exclusions + comp-manifest-check; the `.sh` is the same tool). Minor secondary: the `planned` entry has no `reason` field.

## Disposition
**D1-AC1: CERTIFIED PASS on substance** — full coverage of actual graph-query use-cases is genuinely complete; no graph use-case is overlooked. The lone gap is the manifest's own enforcement gate not being explicitly excluded — a documentation-completeness nicety, **non-blocking**, routed to CTO as a one-line add to make the "zero uncataloged" claim literally exact. AC1 does not depend on it.
