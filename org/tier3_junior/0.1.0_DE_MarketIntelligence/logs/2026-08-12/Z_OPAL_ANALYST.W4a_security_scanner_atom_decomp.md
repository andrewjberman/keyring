# 0.1.0_DE_MarketIntelligence~Z — OPAL_ANALYST.W4a: atom_decomp `/security-scanner`

**archetype:** MIXED (EXPLORE → TRACE → VALIDATE)

**Date:** 2026-08-12 · **TO:** OPAL_ANALYST.W4a (1.0.0_SA_CTO~Z) · **Status at log time:** DRY, handed
to `3.0.0_SA_CVO~Z`, certification running
**Run:** `workflows/atom_decomposition/runs/portal-page-security-scanner/20260812T0158Z/`

**My first atom_decomp run.** The TO said so explicitly and did not pretend otherwise; I told CVO~Z
at handoff because the certifier calibrates to the author.

## Current State

DRY established and packet handed off. **Plane A 16/16 MEASURED; 24 cells UNMEASURED BY DESIGN**
(Planes B/C are CVO~Z's, verified untouched mechanically by constraint K4, not by my say-so).
Proof-of-spec **VALID rc=0**, 7 rows, C5/C6 honestly `UNCOMPUTABLE` pending certification rather
than inflated to PASS.

| step | commit |
|---|---|
| `DOMAIN_BAR.md` — **before enumeration** | `9238d01ce5` |
| Plane A (page-dir) | `d81a66c976` |
| Plane B (api-module · S3 · graph) | `e1e46fa72d` |
| Plane C (network-observed) + netlogs | `02c9c12850` |
| Reconciliation + axis + `c0` | `02c9c12850` |
| `c1` — Plane A measured | `07565f5d39` |
| `c2` · `dry` · `final` · seal · `run.json` | `b0417b7f92` |
| `ui-smoke.mjs --netlog` (portal DEV) | `99f3282d` |

## The method question this run actually answered

The TO required a **second, independent enumeration plane**. I argued the two it named — page-dir
and api-module/graph — are **both structural**, so they can share an obsolete frame exactly as two
page-rooted passes can, which is what binding V is about. Specimen from my own EXP1 work the night
before: `endpoints/market.ts` reaches `portal-proxy` directly, so a Plane-B enumeration of that page
would have missed its entire fallback leg. CTO~Z verified and found **two** such bypasses, not one.

**CTO~Z ratified a third, non-structural plane and restated the requirement as a PROPERTY rather
than a count** — complementary blind spots, at least one non-structural — bound as PRD **X**: *a
requirement stated as a count is satisfiable without the property the count was a proxy for, and the
count is the dangerous form because it is checkable.*

**Plane C then paid for itself twice, once against me:**
1. On page load only **1 of 3** accessors fires — the other two live in conditionally-rendered tab
   bodies. A single default capture would have reported a **1-entity page against Plane B's 13**, a
   catastrophic-looking plane disagreement that was entirely my own unexercised states.
2. **5 foreign `advisor-intelligence` endpoints** fire on this route, invisible to both structural
   planes. **A cross-route control on `/market` showed the identical set** → app-wide shell prefetch,
   excluded from the rectangle. Without that control I would have written five foreign entities in,
   each individually defensible.

## Findings

**F-ORPHAN-PRODUCER (headline).** S3 serves **9** universes; the `UniverseId` union admits **6**.
`msciusa`/`rmidcap`/`sp400` are **structurally unrequestable** — no call site can construct the
addressing parameter. **6 keys, 41.6 MiB**, frozen 2026-05-20 against every live key at 2026-08-07,
two clean write clusters. Cause in the module's own comment: the v0.2 migration was Andrew-reverted
2026-05-21 (SSCN_UNVREV) — **the code reverted and the data did not.** Four independent
corroborations, including the orphan payloads carrying `wt_csus`/`wt_ijh`, exactly the v0.2 columns.
Grounded at the consumed end 0/403 ×3 with a positive control (5/403) in a **separate** invocation.
**Rule 9: disposition row, no act.**

**F-SCHEDULE.** The producer fires on S3-ObjectCreated from a **manual monthly Excel upload** — no
EventBridge schedule, no event-source mapping. It freezes silently if the upload is missed. **No
monitor proposed** — the moratorium forbids exactly the deliverable this finding makes tempting.

**Explicit NON-FINDINGS, because a bar that only ever produces findings is not a bar:** the
2026-08-07 vintage is **healthy on a monthly cadence** (cadence resolved *before* any freshness
language — scoring it as "3 trading days behind" would have manufactured the estate's most-repeated
error class on a working producer); zero consumed universes missing from S3 (no F-ORPHAN-CONSUMER);
footer binds the artifact, not the manifest.

## Three self-caught defects, none buried

1. **My "careful" `useQuery(` count returned 0** — across all 17 files including the one holding all
   three calls, because every call is `useQuery<T>({`. Zero is exactly what "no accessors" looks
   like. The sloppy count (5) was too high and the careful one (0) catastrophically low — **opposite
   directions, neither fixed by care.** Only printing the matched lines beside the count
   discriminated. CTO~Z bound it as **Z**, then found their own published table was not reproducible
   by its own method.
2. **I committed `c0` without validating it.** The validator refused it three times on schema
   violations I would have seen instantly. Corrected in place and declared.
3. **My c2 sweep read `cell["basis"]` — a field merged cells do not carry**, producing a FALSE
   violation: true about an empty string, false about the rectangle. *The retrieval-returns-a-value
   class, inside the sweep whose job is catching it.*

Defect 3 surfaced a real method finding, **source-confirmed**: **`basis` is write-only.** The patch
schema accepts it; `apply_patch` never merges it (`:111-115`). It appears once in the whole
validator — a self-test fixture — and zero times in `apply_patch`; positive control, `evidence`
appears 4× and *is* merged. So author reasoning placed only there never reaches the consumable.
Second member of the K.3 write-only-contract class. Routed to CTO~Z.

## What I refused

The relayed K.1 intake spec named `rectangle.final.certified.json` as a **packet member**. That
artifact is derived *after* the verdict under binding K, so producing one at handoff would have put
the mutant on the path to the consumable — **the exact thing K exists to prevent.** I sent
`final.json`, said why, and flagged it to the routing seat rather than silently complying or
silently substituting. **CVO~Z confirmed the word was theirs, not a relay artifact**, and that
following it "would have INVERTED the control I built." They also escalated the deeper defect my run
made visible: **K.1 has never had a packaging mechanism** — it is a declaration over a shared
directory, and a withholding that depends on the verifier's own restraint is a courtesy, not a
control.

## The mutant, and the binding I applied to myself

Planted, sealed at plant time, committed **before** the handoff. **Binding W** — which came out of
my own re-derivation of CTO~Z's VOID — says the author must write down where they *expect* a
violation to live **before** choosing the plant site, then plant outside it, because a plant placed
where the author already suspects weakness tests *the certifier's agreement with the author*, not
the certifier. I recorded sscn.04 and `serving_state` as my expectations, then planted in a live
family's `consumer_set` — the cell I am most confident about.

**Verified not soft in both directions, run rather than assumed:** `ssot_validate` passes
`final.json` with 0 violations **and my own 8-check sweep also returns 0** on the mutated rectangle.

**And I handed over a weakened seal rather than a strong-looking one.** My incremental commit style
puts `c0`/`c1`/`c2` in git before the seal lands — COO~Z measured that 10 of 11 closed runs instead
publish in one act at closure. Since `dry` is **byte-identical** to an already-committed `c1`, K.1's
withholding of dry is **structurally void on this run** and a `git diff` names the plant outright. I
asked that the K.2 attestation record the route as **available-and-declined** rather than a bare
"no" — an attestation recording "no" where nothing was possible carries no information.

## Compiler Tools

| Tool | Result |
|---|---|
| `ssot_validate.py` | **Self-tested first** (rc=0, 5 checks incl. stale-patch and shape-invalid REFUSED). Live: refused my patches **three times** on real schema violations and wrote nothing on refusal. All final merges rc=0, all 5 rectangles 0 violations. The instrument discriminates and I have the refusals to prove it. |
| `comp-find` | ~15 invocations, each with its **denominator**, positive controls as **separate** invocations. Produced the 3-accessor correction, the 0/403 orphan verdict, the producer chain, the `screening_excel` binding. |
| `comp-estate` | Confirmed "no EventBridge schedule". Coverage measured at **1 of 13** consumed keys — a limit the tool declares itself, so a documented limit confirmed, not a defect found. |
| `ui-smoke.mjs --netlog` (added) | The non-structural plane. 5 captures incl. the `/market` cross-route control that adjudicated the foreign endpoints out. |
| `aws s3 ls/cp/get-object --range` | Listing **materialised and summed programmatically**; 19 keys, arithmetic closed. **Negative control** on a nonexistent key rc=254 — the instrument can fail, so the reads mean something. |
| `comp-to` | Race-free per-session TO_ID. |
| `proof-of-spec-check` | **VALID rc=0**, 7 rows. |

## Next Steps

- [3.0.0_SA_CVO~Z] Certification + semantics (Planes B/C) + K.2 attestation. Running now.
- [me] On the verdict: derive `rectangle.final.certified.json` from **dry** + semantics (binding K,
  never from `final.json`), flip C5/C6, re-validate, close.
- [1.0.0_SA_CTO~Z] Two PRD items routed: `basis` write-only; K.1 has no packaging mechanism
  (CVO~Z's escalation, my run as specimen). Plus two surprise-channel items —
  the app-wide advisor-intelligence 401s, and `generate-manifest` destroying `screening_excel`.
