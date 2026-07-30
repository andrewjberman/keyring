# The Opal World Model — how business functions are defined, at what granularity, and how the map evolves

**Commissioned:** Andrew-direct 2026-07-30 (tool-walk #1 deep pass): *"this seems like the Opal World
Model tool… the number 1 tool agents use for coherence, therefore this is critical to get perfect on
every detail."* **Tool:** `comp-semantic-estates`. **Author:** `3.0.0_SA_CVO`. **This document is the
process of record for the world model's definition, granularity, refresh, and evolution.** The
tool's registry entry (`comp-tools.yaml`) and the resolver's `generated_from` point here.

---

## 1. The four-layer granularity ladder (what exists, who says so, how it refreshes)

| L | Unit | Count @07-30 | What it IS | Defined by | Derivation mode | Refresh |
|---|---|---|---|---|---|---|
| **L1** | `named_thread` — **a BUSINESS FUNCTION** (news, mdpf, advi-bd, smartx…) | 27 | a semantic commitment: "this cluster of machinery serves one business purpose." Ontology: C3-system-grade; a **Route-C naming act** — legislated, not discovered | **Andrew/CVO legislate the name**; catalog: `NAMED_THREAD_CATALOG.md` (d33fe4aab) | **HAND — necessarily.** There is no fact of the matter until named (ROUTE_LOGIC §8: C closes by deciding) | Only by explicit naming act. The loop SURFACES candidates (see §4); it never auto-names |
| **L2** | `family` / sub-thread — **a CHAIN** (bd-allocations, inf-portal-publisher…) | 134 | one coherent producer → served artifact → frontend consumer path with a reachability verdict. Ontology: a D2 path instance | census pass + COO population, **CVO verifies each determination** (status / owning_tool / reachability are adjudications, not observations) | **HAND-ADJUDICATED over DERIVED raw material** (triggers, env, code) | On L3 delta touching the chain; `last_reviewed` per row is the honesty stamp |
| **L3** | resource — lambda / EC2 / StepFn | census 169 (live: 192) | a C0 node | `AUTHORITATIVE_lambda_taxonomy.json` (26b32687a): hand-adjudicated `lambda → named_thread` | **DERIVABLE** (TF + AWS enumerate it; only the *assignment* to L1 is judgment) | **`--census-drift`** (mechanized 2026-07-30): set-diff census vs TF (DESIRED) and vs AWS (APPLIED). **Set, never count** — see §3 |
| **L4** | served key — S3-key-shaped write | 603 | a C0 at artifact grain | nobody — derived | **LIVE-DERIVED at call time** from producer source (the successor engine's plane) | every invocation (`--keys`/`--drift`); the one layer that cannot go stale |

**Cross-cutting determinations** (all L2-grade adjudications, all CVO-verified): `status`
(in-scope / explicit-out-with-reason / unreviewed-LOUD), `owning_tool` (routing to the specialist
sub-resolver — deliberately NOT heuristic: a heuristic once over-assigned comp-pipescript 79 vs the
correct 13, caught by CVO, seed-of-record 61e91d334), `reachability_status` (CVO ground-truth, not a
live grep — a grep is scaffolding-fooled), `debtscan_flags`.

## 2. The definition pipeline (how the map is BUILT, artifact by artifact)

```
  DEFINITION / BUILD PLANE                              QUERY PLANE
  ────────────────────────                              ───────────
  ESTATE (AWS + TF + repo + portal)                     agent: comp-semantic-estates <name>
     │  census passes (pass1_inventory,                        │
     │  pass2_gapfamilies) — enumeration                       ▼
     ▼                                                  resolver JSON (the one read-source)
  AUTHORITATIVE_lambda_taxonomy.json   ← L3 assignment         ▲
     │                                    (hand-adjudicated)   │
  NAMED_THREAD_CATALOG.md              ← L1 naming acts        │
     │                                    (legislated)         │
     ▼                                                         │
  estate-coverage-manifest.yaml        ← L2 rows: CTO schema · │
     │    COO populates · CVO verifies determinations          │
     ▼                                                         │
  gen-estate-resolver.py  ── JOIN (manifest=routing authority  │
     │                        + census detail + taxonomy) ─────┘
     ▼
  golden_fixtures.json  ← gate-b/gate-c oracle pins (re-baselined
                          DELIBERATELY, with provenance, on every
                          reviewed change — never silently)
```

**Authority split, stated once:** *naming* is sovereign/CVO (L1) · *adjudication* is CVO-verified
(L2, assignments) · *enumeration* is derived (L3/L4) · *the join* is mechanical
(gen-estate-resolver). A change at any layer that skips its authority is drift, not evolution.

## 3. Refresh mechanics — what goes stale, what cannot, and the instruments

- **L4 cannot go stale** (derived at call). Its honesty line: "a statement about the scanned
  roots, not about the estate" (repo working tree = DESIRED plane; deployed divergence is
  comp-kuzu's job).
- **L3 rots silently and CANCELS ON COUNT.** Measured 2026-07-30, the founding specimen: census 169
  vs TF 169 — **count-parity concealing 66 membership changes** (33 new, 33 gone). Applied-plane
  discrimination: **19 truly dead** (the entire causality family, bd-portal-publisher,
  bd-time-machine, mdpf-freshness-checker, 3 test stubs) · **14 alive-but-unmanaged** (console-only,
  invisible to TF — their own debt class) · **42 live functions not in the census at all** (incl.
  whole new business functions: the ETFS reports family, find-insure-serving-*, opal-ticket-api,
  the value-parity QA family, astn-wsjft). ~⅓ of the live estate unmodeled or misrepresented after
  45 days. **Therefore: `comp-semantic-estates --census-drift` is the standing instrument** — a
  SET diff (never a count) against TF (default, DESIRED) and `--census-drift --plane aws`
  (APPLIED). Run it at review time and after any infra wave; a nonzero residue is a worklist, not
  an error.
- **L2/L1 refresh is a REVIEW, not a derivation** — which is why `--refresh` deliberately cannot
  advance `last_review`: the stamp asserts a human adjudication happened. (Learned 2026-07-30: the
  refresh path structurally cannot discharge its own staleness banner; that is correct behavior,
  now documented instead of surprising.)
- **Every reviewed change re-runs `--gate-b` and re-baselines fixtures WITH provenance.** The
  07-29/30 incident is the reason stated plainly: the rename regression dropped `--gate-b` from the
  CLI, so the 07-30 map review *could not* run the oracle that its own docstring demands — a broken
  tool hiding the check that would have exposed what broke. The oracle is only an oracle while it
  is invocable; its invocability is part of every review's checklist.

## 4. Evolution — how the map grows new business functions (the loop, applied to the world model)

The archetypal learning loop (`infra/system/ontology/ARCHETYPAL_LEARNING_LOOP.md`), instantiated:

1. **PIN:** the world model's denominators are pinned — taxonomy @26b32687a, catalog @d33fe4aab,
   manifest `last_full_review`, fixtures. A pin that moves is the trigger.
2. **HEAD-ADVANCE:** estate change (TF apply, new lambda, new portal endpoint) advances the live
   head. `--census-drift` computes the delta as a SET.
3. **ROUTE the delta:**
   - **A (autonomous):** a new resource that belongs to an existing thread (e.g.
     `mdpf-accrual-trigger` → mdpf) — assignment within a known L1; CVO adjudicates the row,
     fixtures re-baseline, done.
   - **B (instrument):** a resource no predicate reacts to (alive-but-unmanaged console lambdas are
     exactly this — TF-blind, so the TF-plane diff can never see them; the AWS-plane diff is the
     added predicate).
   - **C (model):** a CLUSTER of unassigned resources with no existing thread to join —
     `find-insure-serving-*` today — is a **candidate new business function. The loop surfaces it;
     ONLY a naming act admits it** (Andrew/CVO), because an L1 name is a semantic commitment the
     estate then organizes around. Auto-naming here would be the confident-wrong-answer class.
4. **CODIFY:** name → catalog entry → manifest rows (COO populates, CVO verifies) → regenerate
   resolver → re-baseline fixtures → gate-b green → the new function is ordinary queryable surface.

**The standing worklist from today's founding measurement:** 42 unassigned live resources (Route
A/C triage owed), 19 dead census threads (retirement adjudication — feeds WS-E3, and note the
resolver DEFENDS these as live until the census regenerates), 14 unmanaged-console lambdas (Route B
+ an infra-governance question), and the L1 candidate clusters awaiting Andrew's naming word:
**etfs-reports · find-insure · ticket · value-parity(→ ops-internal?) · astn-wsjft**.

## 5. Perfection bar (what "get it perfect" means, checkably)

1. `--census-drift` residue = 0 on both planes, or every residual row carries an owner + route.
2. `--gate-b` green at all times; every fixture change carries provenance.
3. Every L2 row's `last_reviewed` ≤ the last infra wave touching its chain.
4. No thread served as live whose producers are dead (the zombie-defense line exists to be read,
   not to absolve).
5. The count digits in registry prose (25/134/169) are DERIVED-at-read or absent — a frozen digit
   in prose is the class this document exists to kill.
