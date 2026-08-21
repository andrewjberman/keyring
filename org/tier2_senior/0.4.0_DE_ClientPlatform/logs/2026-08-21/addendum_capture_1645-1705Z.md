# Addendum 1645-1705Z -- the flip-window capture, and two corrections against my own work

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~1645Z -> ~1705Z (delta since `addendum_p4r3_flip_1605-1645Z.md`)

## The capture (@cd89ff7e80)

AE minted a 49financial bearer at a path (not inline — it kept the credential out of an inbox `.md` that is now committed history) and smoke-tested it before sending, so the window was execution with zero debugging. Routing per COO 65058: AE supplies, DE drives, CVO reads raw.

15 raw files delivered unsummarised. Results:

| leg | result |
|---|---|
| **L1 consumer plane** | **6 twins requested by the portal, all 200** — the plane AE's fetch structurally could not establish |
| **Held-key inverted oracles** | `dashboard`, `fee_efficiency`, `header_metrics` still on legacy, **zero** twin requests |
| **L4** (forced 503) | **6/6** quiet markers, page still renders |
| **L2** (CVO's mutants) | **6/6** loud markers, each naming itself a cutover defect rather than a transport fallback |
| **Control on my own grep** | `SHAPE MISMATCH` in the L1 capture (no mutant) = **0** — the grep discriminates |

## Correction 1 — against my own P4R-1

**Rows 12/13 never fired, and cannot for 49financial.** Row 12's sole caller is gated `enabled: usesStackedBars`, and `49financial/layout.ts:118` sets `stacked: false` (only Inflection is `true`); its one live consumer is a tenant with no twins. Row 13's `getCumulativeChart` has **zero importers** — a dead export superseded by `getTimeseriesOverview`.

My P4R-1 confirmed those sites **exist** at `:409`/`:300` and mapped them as live consumers. It never checked whether they are **reached** for this tenant. **Line presence is not line reachability.** Finding 2C was right as far as it went and was two keys short: the portal-side flip population for 49F is **six**, not eight.

Two instruments agree — source reachability, and a netlog recording zero requests. The **source** analysis is what makes it a reachability claim; ui-smoke states its own window-bounded frame, and an absence inside a window is not an absence in general.

## Correction 2 — against a characterisation of my module

COO called `adviKeyRepoint.ts:123` invisible to their token census. Measured: **false** — all 15 key literals sit in the registry as `leaf:` values, and a census for any key name finds the file.

**The true shape is narrower and worse: findable but unreadable.** `:123` composes `platinum/advi/${firm}/${leaf}`, so the full literal never exists in source — only its halves. A census that *finds* the file reports coverage of the surface and is wrong about what the surface *does*. **A confident partial hides better than a clean absence**, because the instrument appears to have succeeded. COO adopted this as the operative form and it replaces their sentence in the rectangle's coverage-limitation field: what an AST instrument adds here is **composition, not discovery**.

I also flagged that "builds keys generatively" will often mean "centralises its key list deliberately" — and grading those together would file the centralisation that makes the never-widen determination *enforceable* as a defect. COO routed it as a Rule-24 axis the inventory must carry: CENTRALISED-ENUMERABLE vs SCATTERED-INTERPOLATED.

## The session's shape, named by COO across three seats

AE's `fetch(`-regex recalibration (matched 2 sites; the reads go through `adviRead`), my line-presence-vs-reachability, and this morning's `tsc` false green are **one defect**: an instrument answering precisely, about the wrong population. Three instances, three seats, one shape.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `ui-smoke.mjs` | L1 netlog + L2 `--fixtures` x6 + L4 `--fail` x6, real bearer | 13 runs, all rc=0; markers as tabled above |
| `comp-find` | caller/reachability analysis, `barChart.stacked` per tenant, key-literal census | the reachability mechanism; every zero positive-controlled |
| `comp-keys prefix` | twin root pre/post flip | 10/10 at certified sizes; held keys 5/5 absent |

## Blockers

None. P4R-3 flipped and captured; P4-ORACLES complete; MDPF_PROVENANCE superseded by decree; 3F-P1/P2 closed; 3F-P3a and 3F-BF2 surfaced to the issuer.

## Current state

Portal DEV `9580e18b`. Workspace CLOUD through `cd89ff7e80` + this. Dev server stopped, scratch cleaned, bearer used once and not re-minted.
