# Addendum 1605-1645Z -- the sovereign decree, and the P4R-3 flip

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~1605Z -> ~1645Z (delta since `addendum_tac_oracles_1545-1605Z.md`)

## 1. Sovereign decree -- MDPF_PROVENANCE T-A + T-C (@3f821bd4dc)

Andrew-direct at the DS terminal, relayed by `0.4.0_DS_ClientPlatform` (64982). VERBATIM: *"no, none of this work matters"* / *"mark any of these associated TOs superseded by sovereign decree"* / *"i do not want this thrash and irrelevant effort"*.

Recorded + broadcast **same turn**, per the law. DS marked T-B; T-A and T-C were mine. Two boundaries stated as FACTS rather than as readings of his intent:

- **The mark is a DISPOSITION, not a revert instruction.** T-A is live in PROD (`edcc503e`, v2.1.163). Marking a TO superseded does not unland working code, and a seat reading it as "revert PROD" would manufacture exactly the thrash he is stopping.
- **The tolerance STAYS**, and is now doubly held: superseded, and independently measured this morning as the only thing making the Global provenance read resolve. **Verified intact at source AFTER the marks** (`pairedProvenanceRead.ts:312/:719`) — because "I only edited status fields" is a claim about my own actions, and what has to survive is the tolerance.

Scope boundary stated so nobody widens it silently: the decree is the MDPF_PROVENANCE chain, **not** OPAL_ADVIPOINTERS.

## 2. P4R-3 FLIPPED (@9580e18b) -- the leg blocked all session

AE landed remedy (A). I held to my own bar and **confirmed the URL contract against the LANDED ROUTER SOURCE before flipping**, not against the report:

- `PLATINUM_ADVI_PREFIX = "platinum/advi/"` — trailing slash load-bearing (without it `platinum/advisors/` falls into the class and drags the PII-blocked `summary.json` with it).
- Traced the tenant assertion for **both** identities my module presents: a real 49F caller (bucket `opal-data-bd`; path segment `49financial` → same) and an `opal-capital` staff caller whose `?firm=bd` resolves the same bucket. Both match; cross-firm refuses. **`adviTwinUrl` needed no change.**

### Answering COO's control question from source

COO asked the sharpest question of the thread: did the cross-firm control refuse with `scope_denied`, or 404 because no other firm directory exists? **It refused, provably, without re-running it:** `"Firm scope mismatch"` occurs **exactly once** (`:333`), and that return precedes `bucket = CANONICAL_PLATINUM_BUCKET` (`:337`), `const domainName` (`:344`) and the origin mutation (`:346`). **The assertion fires before origin selection**, so a tripped request never reaches S3 and a 404 on that path is structurally impossible. CTO: *"DE's source read settles the control question for good."*

### Verified at this seat

| leg | result |
|---|---|
| S3 | **10/10** certified twins at their certified byte sizes vs manifest anchors |
| NEVER-WIDEN control | **5/5** held/structural keys ABSENT from the twin root — the control that tests COO's determination, not the flip |
| typecheck | `tsc -b` rc=0 unpiped, 0 lines, **mutant control run FIRST and firing** (rc=2, naming my file) |
| build | rc=0, 10.16s |

Scope bounded **structurally**: the per-key `state` field means flipping the constant cannot widen the determination. Revert = one flag, same window.

## 3. What I refused to produce, and why

CVO needs a netlog capture, mandatory L1 on rows 12/13, and console markers. All three need a real bearer through the auth path. **This seat does not hold one** — checked rather than assumed: the D8 tokens were minted by AE and my `--token` flag merely consumed one.

A tokenless run would 401, the module would record `fallback-transport`, the page would serve legacy — **demonstrating the tolerant read works and demonstrating nothing about the flip.** A capture that looks like evidence and answers a different question is worse than no capture, because the next reader cannot tell which one they hold. COO ruled the routing: AE supplies, DE drives, CVO reads raw.

Runbook written ahead of the token so the window is mechanical (`P4R3_FLIP_WINDOW_CAPTURE_RUNBOOK.md`), with four things pre-verified — including that **CVO's fixtures cannot leak onto the legacy read** (the fixture key is a substring of the twin URL and not of the legacy one, so the LOUD fallback lands on the real legacy artifact rather than on another fixture; that is what makes the L2 exercise non-circular).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-keys prefix` | twin root, pre- and post-flip | 10/10 at certified sizes; held-key control 5/5 absent |
| `comp-find` | router source, `App.tsx`, ui-smoke flags, fixture format | route confirmed `App.tsx:438`; `"Firm scope mismatch"` count **1** — the decisive uniqueness measurement |
| `git show origin/CLOUD:` | landed router source | path class + assertion ordering read at the deployed vintage, not the report |

## Blockers

**ONE, named, with an owner:** the authenticated capture, waiting on AE's bearer. Everything else on this lane is closed, superseded, or surfaced.

## Current state

Portal DEV `9580e18b` (flip). Workspace CLOUD through `3f821bd4dc` + this. LD-0441's DT trigger now has one named dependency instead of an unreachable precondition.
