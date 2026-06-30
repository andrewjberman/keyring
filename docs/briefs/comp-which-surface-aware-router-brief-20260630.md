# comp-which Surface-Aware Posterior Router — Brief (COMPLEARN delta)

**Author:** 0.0.0_AB_MSTR (Tier-0, MSTR)
**Date:** 2026-06-30
**Authority:** Andrew-direct (MSTR session 2026-06-30, live design — observed 0.4.0_DE routing comp-cluster off comp-which and hitting a fuzzy-match miss; then steered the DE to brief MSTR so this approach folds in the reusable P2-3 work). Commission ledgered LD-0231.
**Incorporates:** 0.4.0_DE's P2-3 brief (`docs/briefs/comp-cluster-graph-manifest-approach-brief-20260630.md`) + the live NFRA_COMPLEARN P0 status (COO~B ferry, LD-0116: tool_activity catalog LIVE).
**Issued to:** 1.0.0_SA_CTO — fold into the NFRA_COMPLEARN PRD (Section 5a deepening) + arch-gate. COO~B coordinates (already on COMPLEARN + the DE).
**Status:** Commissioned as a DELTA to NFRA_COMPLEARN (LD-0225) — not a new macro-project. comp-which becomes the loop's first live CONSUMER.

> One-line: upgrade comp-which from a **pure text classifier with no prior + silent argmax** to a
> **light surface-aware posterior** — `prior (surface/role from comp-coverage-map) x likelihood
> (query match) x learned affinity (tool_activity) -> posterior`, with a **margin-disambiguation gate**
> that surfaces a near-tie instead of guessing. The Behavior plane that feeds the affinity term is
> ALREADY LIVE (COMPLEARN P0). The curated RULES become the cold-start prior; hand-adding a rule per
> miss stops being the mechanism.

---

## 1. The trigger — two live mis-routes, two distinct failure modes

**Exhibit A — within-margin, cross-tool (the cluster miss).** Watching 0.4.0_DE route comp-cluster
questions through comp-which: "panel to drilldown tree" routed to **comp-transform**, not
**comp-cluster**. Both tools legitimately home on the **portal/component grain**
(`tool_grain_calibration`: comp-transform `[component, field]`, comp-cluster `[cluster, component]`),
the query straddled them, the fuzzy scores were within noise, and the router **committed to the wrong
one silently**.

**Exhibit B — same-surface, pure-likelihood (the comp-drift miss, DE-confirmed).** comp-drift's own
self-query routes to **comp-aws**, not comp-drift (DE verified via stash-revert: pre-existing, not
caused by the cluster change — `.tools/comp-which` routing test, the lone standing FAIL at 34/35).
Both tools are **AWS-CLOUD surface**, so a surface prior alone would NOT separate them — this is a
**likelihood** failure (comp-drift's name/intent vocabulary isn't reaching its own tool). It proves the
prior is necessary but not sufficient: same-surface collisions need the likelihood + learned-affinity
terms too.

The DE's reflex on A — add a curated cluster rule (done: took the regression test 33/35 -> 34/35) —
patches *that phrasing*. The next ambiguous phrasing misses the same way. That is **linear
rule-accretion**: the friction the COMPLEARN brief (Section 5a) already names as the routing-rule
mutation space's reason to exist. The class is: **comp-which has no PRIOR and never expresses
UNCERTAINTY.**

## 2. What comp-which is today, precisely

`score(tool) = fuzzy_overlap(query_tokens, tool_keywords)`; curated `RULES` as hard overrides on top;
then **silent argmax**. Two structural gaps, one per exhibit:

- **No prior (Exhibit A).** The query alone is underdetermined. "panel to drilldown tree" is ambiguous
  in isolation but near-certain once you know *the asker is a DE editing portal cluster components*.
  comp-which ignores **where the agent is operating**.
- **No margin + thin likelihood (Exhibit B).** A 0.51-vs-0.49 split and a 0.95-vs-0.05 split both
  resolve to a silent pick; and a tool whose own intent-vocab is under-represented (comp-drift) never
  surfaces. The near-tie and the under-matched tool are exactly where the system should express doubt,
  and today both are invisible.

## 3. The thesis — a light posterior with a margin gate

Upgrade the scorer to a weighted posterior over the ~44-tool inventory (microseconds; no runtime
model or embedding):

```
score(tool) = w_q * query_match(tool, query)            # LIKELIHOOD (existing fuzzy, enriched)
            + w_s * surface_prior(tool, agent_context)   # PRIOR  (NEW -- from comp-coverage-map)
            + w_h * history_affinity(tool, query)        # LEARNED (NEW -- from tool_activity, LIVE)
```

Then **argmax with a margin gate**: if `score(top1) - score(top2) < epsilon`, **do not silently
pick** — surface both candidates with their `concern` strings from the coverage-map:

```
ambiguous: did you mean
  comp-cluster   -- page-rooted cohort/drilldown cluster + panel grain
  comp-transform -- portal component schema/props (field-level)
```

Curated `RULES` stay — as the **cold-start prior** (and hard overrides for the truly unambiguous
intents). They stop being the place we react to every miss.

## 4. The three signals — all cheap, all already on disk

**(1) Surface-of-operations = the PRIOR. The table already exists in comp-coverage-map.yaml — and it's
CI-guarded.** We do NOT build a new structure — the COMPUNIFY map already declares every tool's home,
and `comp_coverage_view.py --verify` already keeps the manifest/tools_index a drift-free projection of
it (DE-confirmed 35/35). The prior table:
- `surfaces[].high_level_tool` + `tools[].surface` + `tool_grain_calibration.tool_grain_map` =
  the **surface/grain -> tool** table. That IS the prior.

Detected at invocation, all a few ms in the bash shim:
- **Agent role** (`$OPAL_AGENT_SERIAL` / `.comp-graph/.agent_context`): DE -> portal surface,
  DS -> pipeline/gold, DT/AE -> infra/iam. Strong, free, structurally stable. (Needs one small
  addition to the map — see Section 5.)
- **Working-set** (`git diff --name-only`, recent mtimes): editing `portal/.../cluster/*` vs
  `data/*/scripts/gold/*.py` vs `infra/*.tf` is a decisive surface signal.
- **Session trajectory**: the tail of this agent's own recent calls in `org/mcp/comp-which-rail.log`
  / comp_log. Three prior comp-cluster calls means the next ambiguous one almost certainly is too.

**(2) Query tokens = the LIKELIHOOD.** Keep the fuzzy overlap; enrich the match target with each
tool's `concern` + `distinct_from` text from the map (not just bare keywords). This is also the
Exhibit-B fix: comp-drift's `concern` text reaches its own tool.

**(3) History affinity = the LEARNED term — and its substrate is ALREADY LIVE.** COMPLEARN P0 landed
(COO~B/LD-0116): `tool_activity` is the **3rd Trino catalog** (125,162 rows incl 259 gap-found
annotations; federation proven via a live `tool_activity x code_heat` 5,502-row join). So
`history_affinity` is not a future dependency — it's a **query against a live catalog**: which
`(query, surface) -> tool` mappings actually **paid off** (a route NOT followed by a rail-escape /
immediate re-run = a good route). Precomputed offline by the COMPLEARN tick (~E is already on P1:
federated views + the comp-learns-status dashboard) into a small affinity table the shim reads — no
per-call training.

## 5. Why this is COMPLEARN, not a new project (the deepening)

The COMPLEARN brief Section 5a already establishes:
- the comp-which RULES are a **first-class champion-config surface** the loop proposes mutations to;
- LD-0226 is the **worked routing-rule iteration** (MSTR hand-wired a comp-xray rule to kill a
  served-content rail-escape);
- the `comp-which-rail.log` action mix (ROUTE / RUN-GREP / RUN-GLOB / DENY / rail-checked) is the
  **primary routing-quality signal** the scorer already reads.

This brief **deepens the mutation space** from "propose a curated RULE" to "tune a posterior":
the loop now also proposes/learns (a) the **surface-prior weights** `w_s` per role/surface, (b) the
**margin threshold** `epsilon`, and (c) the **per-(query, surface) affinity table** `w_h` — all scored
on the **same** rail-escape-reduction signal already in the scorer. No new scorer, no new substrate —
the Behavior plane is live; this is the same loop pointed at a richer champion.

**One small COMPUNIFY hook:** add a **role -> surface affinity** to comp-coverage-map.yaml (DE->portal,
DS->pipeline/gold, DT/AE->infra/iam, CVO->cross). Small, declarative, COMPUNIFY-owned (coordinate ~C).
It is the only net-new data structure; everything else is read from the live map + rail log + the
live tool_activity catalog.

**The payoff framing:** comp-which becomes the **first live CONSUMER of the COMPLEARN loop** — and
because P0 is already done, that payoff is **near-term**, not a long warm-up: the affinity table is a
P1 query away.

## 6. Verification — the regression test IS the gate, and it unifies with the loop (DE pattern, lifted)

The DE established the **routing regression test as the acceptance gate** (`.tools/comp-which` routing
test; their curated rule moved it 33/35 -> 34/35; the lone FAIL is Exhibit B, comp-drift). Carry this
in as the posterior's contract:
1. **The posterior + margin gate must keep the regression test green** — every existing route a test
   case; no regression on a change (the DE's gate, generalized to the scored router).
2. **The test set GROWS with each margin-gate disambiguation.** A human-confirmed `query -> tool` pick
   at a near-tie becomes BOTH a new regression test case AND a `tool_activity` training row. The UX
   fix and the learning loop are the **same event** — the gate feeds the champion.
3. **comp-drift (Exhibit B) is the first new green:** a curated comp-drift rule + the enriched
   likelihood takes the test to 35/35 now (immediate, like the cluster rule); the posterior then keeps
   it green structurally.

## 7. Design discipline (carry into the PRD)

1. **Surface is a PRIOR (additive bias), never a FILTER.** The agent in portal-land usually means the
   portal tool but MUST still be able to reach comp-iam. A hard surface filter would break the
   legitimate cross-surface query — the bias only breaks near-ties, never excludes a tool. (Exhibit B
   underlines this: same-surface tools can't be separated by the prior at all — the bias must never
   become exclusion.)
2. **The margin gate disambiguates, never silently picks** — and **every disambiguation is a labeled
   training example** (Section 6.2). The gate is both the UX fix AND the loop's best data source.
3. **Weights are LEARNED, not hand-tuned** — and scored on VALUE not usage (the COMPLEARN Goodhart-
   honesty gate, reused verbatim): rail-escapes prevented / correct-route rate, never invocation count.
4. **Stays a light CLI.** Dict lookups (surface prior) + a precomputed affinity read + a weighted sum
   over ~44 tools. No runtime model, no per-call embedding. The shim remains instant.
5. **Cold-start safe.** With an empty affinity table (`w_h` contributes 0), the router degrades to
   today's behavior PLUS the surface prior PLUS the margin gate — already strictly better than silent
   argmax, before the loop has learned anything.

## 8. Immediate vs principled — the split + recommendation

- **Now (DE, cheap, unblocks today):** the DE's curated cluster rule + a curated comp-drift rule land
  (-> 35/35 regression). They are the correct cold-start priors; no reason to hold them on this brief.
  (Landing is gated on the authoring-vs-landing question — Section 9.)
- **Principled (the real answer):** the surface-aware posterior + margin gate as an **early COMPLEARN
  milestone** — the surface-prior read + margin gate need only the coverage-map + the rail log (both
  live) = a small near-term add; the learned weights/affinity ride the **live tool_activity catalog**
  (~E's P1 federated views) rather than waiting on new substrate. Most value lands early; learning
  refines it.

## 9. The authoring-vs-landing governance fork (DE-surfaced — needs a CTO/COO~B ruling)

The DE hit a real seam landing comp-cluster: the owned-paths gate blocks a DE from landing
`infra/aws/globgrph/comp_cluster_cli.py` (lane CLOUD_OPS_OR_ETL, AE-only) and from registering in
`graph-call-manifest.yaml` (lane ANY_EXEC, exec-only). So **a DE can AUTHOR a comp-tool's logic +
wrapper but not LAND the infra engine or the exec-owned manifest entry.** This generalizes — it will
recur for every non-AE/non-exec comp-tool author.

**MSTR recommendation (for CTO/COO~B to ratify):** split the lifecycle deliberately, don't grant a
blanket lane —
- **AUTHORING (logic + wrapper + the curated rule)** = the builder's lane. To unblock the infra-import
  wall, **relocate read-side comp-tool engines to a lane-portable home** (`org/modules/graph/`, where
  the other comp-engines live) and **shell to `comp-kuzu --json`** instead of importing
  `infra/aws/globgrph/_canonical` directly (the DE's option (a)). A read-side query tool should not
  have to live in the AE infra-deploy lane; this makes authoring lane == landing lane for the engine.
- **LEDGER REGISTRATION** stays the **governor's** act (COMPUNIFY ~C owns comp-coverage-map; the
  manifest is its projection). This is **correct separation, not friction**: the coverage-map is the
  one-home source of truth and its non-redundancy gate is exactly what must stay governor-owned. So the
  flow is: builder authors + briefs the governor -> governor registers the home in the ledger -> the
  manifest projection regenerates (`comp_coverage_view.py`). The builder lands their own engine; only
  the *home registration* crosses to the governor, which is where it belongs.

This keeps comp-tools lane-portable to build, while the one-home discipline (the thing the whole
program protects) stays with the governor. CTO/COO~B settle the final shape; ~C is the registration
owner.

## 10. Lane / governance

- **MSTR** (this brief + LD-0231) scopes the delta; does not author the PRD.
- **CTO** (`1.0.0_SA_CTO`) folds it into the COMPLEARN PRD + arch-gate; owns the posterior/scorer design
  + the Section-9 authoring-vs-landing ruling.
- **COO~B** (`2.1.0_SA_COO`) coordinates — already on COMPLEARN + the DE; threads the curated-rules-now
  vs posterior-later split + the Section-9 landing path so the DE isn't blocked.
- **CVO** (`3.0.0_SA_CVO`) verifies the no-Goodhart honesty (score on value) + that a flagged mis-route
  reproduces as a real near-tie / under-match on the rail log (the routing-quality ground-truth).
- **~E** (`0.8.0_AE_CloudComp~E`, COMPLEARN lane) — the affinity table is a P1 federated-view/dashboard
  deliverable off the live tool_activity catalog it just stood up.
- **~C** (`0.8.0_AE_CloudComp~C`, COMPUNIFY governor) — the role->surface affinity add + the comp-tool
  home/ledger registration (Section 9).
- **DE** (`0.4.0_DE`) lands the curated cluster + comp-drift rules now; reshapes comp-cluster to the
  Section-9 engine-home standard; consumes the posterior router when it ships.
