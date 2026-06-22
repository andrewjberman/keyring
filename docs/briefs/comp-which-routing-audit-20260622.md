# AUDIT — comp-which routing mechanics + comp-tool registry tagging

- **Audit ID:** comp-which-routing-audit-20260622
- **Date:** 2026-06-22
- **Author:** 0.0.0_AB_MSTR (Andrew-commissioned: "check the comp-which mechanics + make sure everything in the comp tool registry is appropriately/logically tagged so the tools are actually useful/accessible")
- **Owner of fix:** 1.0.0_SA_CTO (rail owner; `.tools/comp-which` = CTO/BASE_EXEC lane)
- **Priority:** HIGH — **prerequisite to the LD-0207 gate-hardening enforce-ramp** (see §5).
- **Grounding:** source-read (`comp-which`, `graph-call-manifest.yaml`) + 4 empirical comp-which runs (Rule 22 compliant — mechanism confirmed by running the tool, not inferred).

---

## 1. The headline

**The registry tagging is GOOD; the ROUTER is broken.** `graph-call-manifest.yaml` has rich,
keyword-dense `entries` + a `tools_index` covering ~all 36 comp-* tools. But `comp-which` — the
router agents are now *gated toward* (Rule 21) — can only reliably route the **~8 tools hardcoded in
its curated rules**. The other **~28 tools are effectively unreachable through comp-which**, because
the mechanism meant to cover them (the manifest-fuzzy backstop) is non-functional. Net: an agent
gated to comp-which for a question about comp-freshness / comp-validate / comp-pii / comp-types /
comp-trace / etc. gets a **raw grep dump or a misroute**, not the right tool.

## 2. How comp-which works (grounded against source)

Two layers + a never-dead-end:
1. **Curated RULES** (`comp-which:34-83`, ~11 rules): keyword→tool, phrase match +3 / token +2,
   STRONG = 4. Covers ~8 tools: comp-pipescript, pipescript, comp-transform, comp-routes, comp-iam,
   comp-aws, comp-blast, comp-cache.
2. **Manifest-fuzzy backstop** (`comp-which:131-148`, `_manifest_matches`): token-overlap over the
   manifest — *intended* to make all 36 tools queryable + "auto-include new tools as they're added"
   (per the tool's own docstring + manifest entry `meta.comp_which.router`).
3. **Never-dead-end:** no rich tool + a search term → RUN `comp-grep`/`comp-glob`.

## 3. The two compounding defects

### Defect A — backstop reads the WRONG KEY (one-line bug)
`_manifest_matches` iterates `data.get("use_cases", [])` (`comp-which:142`). The manifest has **no
top-level `use_cases:` key** — its entries live under **`entries:`** (`graph-call-manifest.yaml:39`).
So the backstop iterates an empty list and **matches nothing, always.** The "fuzzy backstop that
auto-includes every tool" has never fired. (Per-entry field names `use_case`/`id`/`tool` at
`comp-which:143-146` ARE correct — only the top-level collection key is wrong.)

### Defect B — decision flow runs the primitive BEFORE the backstop
Even with Defect A fixed, the backstop (`comp-which:290`) is only reached when there is **no
extractable term**. The branch at `comp-which:273` — `if (search_intent or best_score == 0) and
term:` — fires first: when no curated rule matches (`best_score == 0`) and any term is extractable,
comp-which **runs `comp-grep` on that term instead of consulting the manifest.** So a clean
comp-freshness/comp-validate question with no curated rule extracts a noise word and greps it.

### Consequence (empirically demonstrated 2026-06-22)
| Question | Should route | Actual |
|---|---|---|
| "what produces canonical_prices.parquet" | comp-pipescript io | **comp-pipescript io** ✓ (curated) |
| "is the upstream s3 data fresh enough to run the bd gold chain" | comp-freshness | raw `comp-grep "upstream"` (Defect B) |
| "does my gold artifact satisfy its invariants before upload" | comp-validate | raw `comp-grep "invariants"` (Defect B) |
| "does a component expose cleartext PII to external advisors" | comp-pii | **misrouted** to comp-transform/portal (Defect C) |

### Defect C (secondary) — curated rules narrow + one over-broad
~8 of 36 tools have a curated rule; the `portal/component` rule's keyword `component` is broad enough
to win (weak score) on a comp-pii question and mask the correct tool. A weak curated hit also
suppresses the backstop (which only fires on zero hits).

## 4. The fix (CTO scopes; direction)

1. **Defect A:** `comp-which:142` `get("use_cases", [])` → `get("entries", [])`. One line. Lights up
   the whole catalog through the backstop.
2. **Defect B:** reorder the decision flow — when `best_score < STRONG`, consult `_manifest_matches`
   **before** falling to run-the-primitive; only run `comp-grep`/`comp-glob` if the manifest backstop
   *also* misses. (Keep the never-dead-end; just make "consult the catalog" precede "grep a term.")
3. **Defect C:** add curated rules (or rely on the now-live backstop) for the high-value long-tail
   (comp-freshness, comp-validate, comp-pii, comp-types, comp-trace, comp-diff, comp-constants,
   comp-lambdamap, comp-graph, comp-registry, comp-coverage, …); tighten the `portal/component` rule
   so it doesn't mask comp-pii/comp-cache/comp-types.
4. **Regression guard:** a tiny test asserting comp-which routes a representative question for EACH
   tools_index tool to that tool (so a future tool added to the manifest is provably reachable). This
   is the standing "every tool is accessible" oracle Andrew is asking for.

## 5. Sequencing — this GATES the LD-0207 enforce-ramp

[[LD-0207]] hardens the rail to DENY raw grep + route agents to comp-which/comp-tools. That assumes
comp-which is a good router. It routes ~8/36 tools today. **Hardening the gate toward a router that
dead-ends ~28 tools would funnel agents into raw-grep dumps / misroutes at the exact moment raw grep
is denied** — friction + the rail failing its purpose. So: **fix comp-which routing BEFORE (or in the
same batch as) the Gate-1/Gate-2 enforce.** Recommend folding this into the NFRA_COMPRAIL hardening TO
as a prerequisite leg; TO-5 telemetry (`comp-which-rail.log` RUN-GREP vs ROUTE rate) is the
before/after measurement.

## 6. What's NOT broken (fair finding)
The manifest itself is well-tagged: rich `use_case` text + `tools_index` for ~all tools, sensible
ids/layers. The high-traffic curated path (the ~8 tools) routes correctly. The gap is the router not
USING the good tagging for the long tail — not the tags themselves. So the fix is ~entirely in
`comp-which` (the matcher), with only light curated-rule additions.
