# IRPT_BCKEND -- L5 decomposition -- round 3 -- v0.3

**v0.2** (2026-09-11 ~11:5xZ, `2.0.0_SA_COO~B`, the ROUND-2 RECUT on the CTO's round-1 analysis `ledger/ROUND_ANALYSIS.round1.md` @`0d57ceb2f9` and the CVO's slug `surprise-channel/remediations/REMEDIATION_v1.md` @`27e67fa6a5`, against PRD v0.13 @`e6ba5d9878`, ADMITTED with both L4-R halves SIGNED). Round 1 (v0.1.1, 19 cells) closed at ROUND_CLOSE with 0 of 10 REALIZED; its cells are retained below by id (section 0) so every round-1 instance's `cell_refs` still resolves in this document's id space. Round 2 is twelve cells, `IB-rt-<n>` and the battery `IB-rtb-1`, cut to the CTO's eight rulings in his order: the seam and the guards first, the three declared producers next, then export, YCharts on the v0.9 mechanism, intake controls, records.

```json
{
  "project": "IRPT_BCKEND",
  "directive": "D9",
  "fabric": "laptop",
  "round": 18,
  "decomp_version": "0.22",
  "prd_ref": "org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md@4f942b7657",
  "prd_version": "v0.17",
  "round1_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round1.md@0d57ceb2f9",
  "round2_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND2_ANALYSIS.md@cfe3a33a9b",
  "round2_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v2.md@c1a8cd2543 (the L8/L9 commit; msg 97752)",
  "round1_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v1.md@27e67fa6a5",
  "brief_ref": "docs/briefs/investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd",
  "endpoint_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BCKEND_20260910.md",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11"
  ],
  "owns_grade": [
    "FWD-2",
    "FWD-7",
    "FWD-9",
    "FWD-10"
  ],
  "cells_round2": 12,
  "cells_round3": 5,
  "cell_id_shape": "IB-rtc-<n> (round 3, the recut on the round-2 analysis); IB-rt-<n>/IB-rtb-1 (round 2, retained by id)",
  "worker_serial": "0.9.0_WK_IRPT_BCKEND~<slot> (the round-1 subagents, continued) and 0.4.0_DS_ClientPlatform~X (one DS-lane cell, the rule-13 act)",
  "cut_head_round2": "67ef99e5c2",
  "cut_head": "cfe3a33a9b (the round-2 analysis commit; HEAD at the cut is stated in the issuance commit)",
  "counterpart_decomp": "org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md",
  "round3_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND3_ANALYSIS.md @5c59f68d70",
  "cells_round4": 8,
  "cell_id_shape_round4": "IB-rtd-<n>",
  "round4_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND4_ANALYSIS.md @561d6e1cc9",
  "cells_round5": 6,
  "cell_id_shape_round5": "IB-rte-<n>",
  "cells_round6": 14,
  "cell_id_shape_round6": "IB-rtf-<n>",
  "round5_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md@81472c3a47",
  "round6_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND6_ANALYSIS.md@fa2ff4f0dd",
  "cells_round7": 4,
  "cell_id_shape_round7": "IB-rtg-<n>",
  "round7_analysis_ref": "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND7_ANALYSIS.md @0d400d5c07",
  "round7_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v3.md @357565e863",
  "cells_round8": 6,
  "cell_id_shape_round8": "IB-rth-<n>",
  "round8_mid_round_addition_1": "IB-rth-5, ~14:5xZ 2026-09-21, on row W3-S52 and CTO ruling addendum 2 @afc015b4b2 (msg 99068)",
  "round8_mid_round_addition_2": "IB-rth-6, ~16:2xZ 2026-09-21, Andrew-direct @fb8c7a574c -- create opal-data-inflectionwealth + opal-data-cottonwoodcapital -- CLOSED SUPERSEDED ~17:5xZ on CRO msg 99124 @a0097b1ef4, the need was met another way",
  "round8_mid_round_addition_3": "IB-rth-7, ~18:0xZ 2026-09-21, on CRO msg 99124 + CTO msg 99128 -- reconcile Terraform state (ledger legs L1/L3/L4) against the manually-recovered bucket policy; carries row S116 (fence_patterns hyphen gap); found real drift, row W7-S2",
  "round8_mid_round_addition_4": "IB-rth-8, ~19:1xZ 2026-09-21, on row W7-S2 -- never-widen packet + sign-off + apply to clear 4 tainted lgic_firm resources found by IB-rth-7's plan",
  "round8_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_8_20260921.md @8e0f9a127e (msg 99299)",
  "round8_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v2.md @9d7a369b38",
  "cells_round9": 6,
  "cell_id_shape_round9": "IB-rti-<n>",
  "round9_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_9_20260922.md @9d4052728b (msg 99334; corrects the CTO's own rti-6 park ruling)",
  "round9_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v3.md @a62b69f6d3",
  "cells_round10": 4,
  "cell_id_shape_round10": "IB-rtj-<n>",
  "round10_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_10_20260922.md @703efac869",
  "round10_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v4.md @79d34e339c",
  "cells_round11": 1,
  "cell_id_shape_round11": "IB-rtk-<n>",
  "round11_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_11_20260922.md @23d5fe2e6b",
  "round11_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v5.md @d20200b92c",
  "cells_round12": 1,
  "cell_id_shape_round12": "IB-rtl-<n>",
  "round12_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_12_20260922.md @a8d306eb71",
  "round12_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v6.md @5a9a7eed81",
  "cells_round13": 1,
  "cell_id_shape_round13": "IB-rtm-<n>",
  "round13_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_13_20260922.md @e107b84d38",
  "round13_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v7.md @12738b5791",
  "cells_round14": 1,
  "cell_id_shape_round14": "IB-rtn-<n>",
  "round14_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_14_20260922.md @0782226170",
  "round14_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v7.md @5236fd2696 (round-14 addendum)",
  "cells_round15": 1,
  "cell_id_shape_round15": "IB-rto-<n>",
  "round15_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_15_20260922.md @81338c807a",
  "round15_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v7.md @4870207827 (round-15 addendum)",
  "cells_round16": 1,
  "cell_id_shape_round16": "IB-rtp-<n>",
  "round16_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_16_20260922.md @e6abd13f94",
  "round16_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v7.md @4e4808d815 (round-16 addendum)",
  "cells_round17": 3,
  "cell_id_shape_round17": "IB-rtq-<n>",
  "round17_authorization": "L4-R sign-off ADMITTED, PRD v0.17 @1450e05178 (commit 4f942b7657), both halves SIGNED (3.0.0_SA_CVO~B ratified-text, 4.0.0_SA_CRO brief) -- 1.0.0_SA_CTO msg 99478, 'round 17 is yours to decompose and cut. It rests on CONTRACTS THE RENDER IDENTITY, items 1-8.'",
  "round17_slug_ref": "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v8.md @7595037af9",
  "round17_analysis_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_17_20260922.md @9452002878",
  "cells_round18": 5,
  "cell_id_shape_round18": "IB-rtr-<letter>"
}
```

**One carrier, two sources.** Each round-2 face inlines VERBATIM the PRD v0.13 candidate row it serves and the CTO's ruling it executes; this document adds the ORDER, the ROOTS, the SEATING, the FENCE, the BATTERY and the round-2 findings. It restates no PRD row and re-cuts nothing round 1 delivered: the ten converged roots, the eleven live routes, the CloudFront path, the status envelope and recovery arms, the extraction and certification, and nineteen VALID instances stand and are BUILT ON (each face's "WHAT ROUND 1 DELIVERED" section names what).

---

## R18. ROUND 18 -- THE RENDER IDENTITY, BOUND TO THE REAL MODULES (CTO's round-17 analysis @9452002878; slug @7595037af9; v0.22, 2026-09-22, `2.0.0_SA_COO~B`)

Round 17 closed with a verdict, not a pass: **render contract NOT PROVEN.** The CVO's own cross-module probes (`IRPT_BCKEND_R17_PROBE.py`/`.mjs`, co-committed with `IRPT_BCKEND_R17_REVIEW_20260922.md`) ran the THREE MERGED modules together for the first time and found genuine integration defects no cell's own isolated-fixture test could see: V3's render branch omits `X-Origin-Verify`, so the real minter's token classifies UNKNOWN in the real resolver (`C-S200`); V2's `authorizeRenderToken` accepts all four forbidden claims (`role admin`/`firmRole admin`/`tier internal`/`userType Dev`) that V3 correctly refuses (`C-S201`); the enforcer's `RENDER_DELEGATE_OPERATIONS` allowlist (`performance`/`analysis_sections`/`narrative`) does not match the real served vocabulary (`performance_report`/`analysis_report`/`narrative_packet`, confirmed this tick from `docs/contracts/investor-reporting/v1/routes.json` + `_authz/served.py:key_operation`) -- as built, every real request is refused `OBJECT_NOT_COVERED` (`C-S203`); the delegator-identity adapter assumes subject==advisor-id and never checks the bundle id, so cache keys collide across distinct revisions (`W15-S5`); V3's asset allowlist assumes a `/investor-reporting/` prefix the real portal build does not use (`W16-S2`); and the cross-cell merge itself introduced a regression -- one previously-passing pre-existing `_scope` test now fails, and citations drifted again (`W15-S1/S2`). The CTO's round-17 analysis (four rulings: W16-S1/S3 resolved prospectively with a durable 19-test baseline plus an offline V1 harness; W16-S4 PARKED to its external owner `2.0.0_SA_COO~G`; W15-S6 is order-text debt folded into every round-18 grant; no key provisioning/deploy before R18-e's own L9 PASS) cuts round 18 as FIVE cells, four in parallel and the fifth gated on the first three landing. No PRD addendum -- v0.17 items 2, 4, 6 and 8 already require every one of these fixes; this round implements what was already ratified. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657`.

### R18.1 The rectangle (5 cells, id shape `IB-rtr-<letter>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtr-1` | **V3, THE ORIGIN MARKER + THE REAL ASSET ALLOWLIST (`C-S200`, the V3 part of `C-S203`, `W16-S2`).** `render_auth.mjs`'s `applyRenderHeaders` must ALSO inject `X-Origin-Verify: cloudfront` (mirroring the human path's own injection at `index.mjs:518`) -- without it, `classify_principal`'s branch 1 refuses UNKNOWN before the renderer branch is ever reached, exactly the defect the CVO's real-module probe found. Tests: a missing-marker control (asserting the CURRENT broken behavior fails, then passes after the fix) and a spoofed-marker control (a client-supplied `X-Origin-Verify` must still be OVERWRITTEN by the verified constant, never trusted from the request). GET-only admission, with an explicit POST control proving a POST to an otherwise-admissible render URI is refused (the CVO's review found the current handler forwards POST to an allowed API URI). The static-asset allowlist must be rebuilt from the PINNED portal build's real convention, never the untracked local `dist/` the CVO's review found as a counterexample (root `/assets/`, not `/investor-reporting/`-prefixed) -- read `portal/vite.config.ts`'s actual base/outDir/assetsDir configuration (checkout the submodule properly, do not guess from an unpinned build artifact) and derive the allowlist from that authoritative source; if no pinned manifest exists, file a row naming exactly what is missing and implement the narrowest defensible reading of the config itself, never a blanket extension-based guess. Unrelated-URI negatives required. | WK~17 (first invocation) | FWD-2, FWD-11 (contrib) | -- |
| `IB-rtr-2` | **BOTH VERIFIERS, THE FORBIDDEN CLAIMS + THE EXPIRY BOUND (`C-S201`, `C-S210`).** V2's `authorizeRenderToken` must reject all four forbidden claims (`role admin`, `firmRole admin`, `tier internal`, `userType Dev`) the SAME way V3 already does -- currently V2 has no such check at all. Both V2 and V3 must REQUIRE `exp`, bounded at 5 minutes or less from `iat`, with 60s or less clock skew leeway -- the CVO found V3 accepts a token 5s past `exp` (within its `clockTolerance`) but correctly refuses one 120s past, while V2's own boundary needs the same explicit bound stated and tested, never left to an implicit default. Controls required, each beside a valid positive: missing `exp`, an oversized `exp` (further than 5 minutes out), both skew edges (just inside/just outside 60s), and each of the four poisoned claims individually. Log `jti` and render id on BOTH accept and refusal paths at both verifiers (currently V2's accept log carries route/claimName only, no render identity) -- never log the token itself or any key material. The existing human `aud`/`iss` path is untouched by this cell (the CTO's own explicit carve-out -- that gap is its own separate change under its own halves). | WK~18 (first invocation) | FWD-2 (own) | -- |
| `IB-rtr-3` | **THE ENFORCER, REAL OPERATION NAMES + THE ITEM-8 IDENTITY ADAPTER (`W15-S5`, the served part of `C-S203`).** `enforce.py`'s `RENDER_DELEGATE_OPERATIONS` (currently `("performance", "analysis_sections", "narrative")`, line ~247) must become the REAL `key_operation`-transformed served vocabulary: `("performance_report", "analysis_report", "narrative_packet")` -- confirmed this tick against `docs/contracts/investor-reporting/v1/routes.json`'s three `operation` fields (`performance-report`/`analysis-report`/`narrative-packet`) run through `served.py:key_operation`'s hyphen-to-underscore transform. Prove it through the REAL route adapter/enforcer (not a renamed fixture), plus a fourth-operation denial. **The `_resolve_render_delegate` identity adapter** (`enforce.py:364-447`) needs three fixes, each independently tested: (1) the delegator's subject must resolve their CURRENT actual grant WITHOUT assuming subject equals advisor id -- the current code sets `delegator_headers["x-advisor-id"] = delegator` (the SAME value as `x-user-email`), which the CVO's probe showed fails EMPTY_GRANT for a real fixture human whose advisor id differs from their email subject; resolve the delegator's real identity properly (read `_scope.resolve`'s own identity resolution path for how a subject maps to its advisor id today, and use THAT, never a bare substitution) -- test with a subject whose advisor id is genuinely different from its email. (2) `load_render_bundle` is currently called with only `(tenant, revision)` -- the bundle id (`X-Render-Bundle`) is read into `trusted` but NEVER PASSED OR VERIFIED, so the CVO's probe found a DIFFERENT bundle name accepted against `bundle-1`'s own output; the loader call and its verification must also check the returned bundle's own identity matches the claimed `X-Render-Bundle` value, refusing on a mismatch. (3) the cache/idempotency fingerprint (`enforce.py:443`, `_scope.fingerprint(intersection, entitlement_revision, policy, self.binding.tenant)`) must also carry the RENDER_DELEGATE class and the bundle revision, so two distinct revisions never collide on the same key (the CVO's probe found exactly this collision). Controls: subject != advisor id, wrong bundle id, revoked delegator (already passing, do not regress), cache separation across two distinct revisions. | WK~19 (first invocation) | FWD-2 (own) | -- |
| `IB-rtr-4` | **RE-PIN CITATIONS TO ONE MERGED VINTAGE (`W15-S1`, `W15-S2`, `W16-S1`, `W16-S3`).** After round 17's three-way merge, `resolve.py`'s `TRUSTED_HEADERS`/`RENDER_TRUSTED_HEADERS` line-number citations drifted AGAIN (the CVO found `x-user-email`'s cited line 400 is now `console.warn`, not the injection site) and the real pre-existing `_scope` suite regressed by one test (28 of 29, not 29 of 29) -- re-pin every citation to the ACTUAL CURRENT merged-tree line numbers (confirm yourself, do not trust any prior round's citation, including this order's own). Run the unchanged scope suite AND the `IB-rtq-2` worker's own wrapper test AND (per the CTO's ruling-1 baseline) a NEW offline harness that invokes V1's actual `verifyAccessToken` with key retrieval faked -- the durable baseline is the 19 worker-authored tests from `IB-rtq-3`, pinned at their merged commit and UNEDITED; this cell adds the V1 harness alongside them, never replaces or retroactively relabels them. Report isolated-worker evidence and merged-tree evidence SEPARATELY, never conflated. | WK~20 (first invocation) | records integrity (no FWD directly) | -- |
| `IB-rtr-5` | **THE ONE OFFLINE ACTUAL-MODULE CHAIN -- THE ONLY PROOF OF THE RENDER CONTRACT.** Depends on `IB-rtr-1`, `IB-rtr-2`, `IB-rtr-3` landing (never `IB-rtr-4` -- that cell is citation/regression housekeeping, orthogonal to the chain). ONE offline test wiring the ACTUAL modules together, no claim-shaped stand-ins for any of them: the real minter (`_render_identity/mint.py`) mints a token -> the real V3 branch (`render_auth.mjs`/`index.mjs`) verifies and admits it, injecting real headers -> the real V2 branch (`portal-authorizer/index.mjs`) verifies and admits it -> the real resolver (`_scope/resolve.py`) classifies it -> the real enforcer (`_authz/enforce.py`) resolves its scope -> the real `served.py` operation-key boundary accepts it -- across THREE real bundle/account objects (not one, so a single-object coincidence cannot pass silently). Negatives, each run through the SAME real chain: a forbidden claim, an expired token, a swapped path id, a wrong bundle id, a fourth operation, a missing render marker. This is PRD item 7's full (a)-(k) table except (g) (the applied-IAM-policy read, which is a deploy-time-only check per the CTO's ruling 4) -- graded by the CVO at L9, never self-graded. | WK~21 (first invocation, spawned only after a/b/c drain) | FWD-2, FWD-3, FWD-4, FWD-8, FWD-11 (the round's own proof) | a, b, c |

### R18.2 Edges and fanout

Two waves. **Wave 1, parallel: A** `rtr-a`, **B** `rtr-b`, **C** `rtr-c`, **D** `rtr-d`. `rtr-c` (`_authz/enforce.py` only) and `rtr-d` (`_scope/resolve.py` citations + a new V1-harness test file) are fully disjoint from every other cell. **`rtr-a` and `rtr-b` share TWO FILES** (`render_auth.mjs`, `index.mjs` in `auth-validator-edge/`) **by the CTO's own ruling** -- `rtr-a` owns the origin-marker injection, the GET-only check and the asset allowlist; `rtr-b` owns V3's forbidden-claims/expiry-bound/logging additions on the SAME files, different functions. This is a git-mergeable overlap (disjoint functions, not disjoint files), flagged in both orders' own preflight so a genuine line-range collision at drain time is resolved by the issuer, never silently widened by either worker. **Wave 2: E** `rtr-e`, gated on A+B+C merging (never D). **fanout: 4 of 5 chains cut and spawned this tick, cap 8; the 5th (`rtr-e`) is cut in the SAME issuance but its worker is held and spawned only once `rtr-a`/`rtr-b`/`rtr-c` drain** -- a cross-slot wait the COO sequences at the drain, per the round-2 precedent (s.5 of this document) and the CTO's own explicit dependency statement.

### R18.3 Bounds carried (every order)

Still OFFLINE, still no deploy: no Secrets Manager entry, no SSM parameter, no AWS API call, no Lambda deploy, no Terraform/CloudFront change. Every fix proves against fixtures/synthetic requests, real code paths, real operation-name vocabulary -- never a renamed or claim-shaped stand-in for a module this round can build and run offline. No cell touches `.tools/naming-gate.py`/`lib/opal_naming.py` (`W16-S4` stays PARKED, owner `2.0.0_SA_COO~G`). No cell touches the existing human `aud`/`iss` gap (its own separate change). `IB-rtr-5` is the round's only judgment-graded criterion; `rtr-a`/`b`/`c`/`d` are mechanical (does the named test suite pass).

### R18.4 Not decided here

Whether/when `IB-rti-6` re-hands (external: BOTH `IRPT_FNTEND` FE-s-88 landing AND an `IB-rtr-5` PASS, per the CTO's own carry); the real key provisioning + deploy (a later round under NEVER-2, cut only once `IB-rtr-5` grades PASS at L9, per the CTO's ruling 4); `W16-S4`'s actual naming-gate repair (external owner); the human `aud`/`iss` standing gap (its own change).

### R18.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-17 analysis's five named cells (R18-a through R18-e) MINUS zero (every named cell is cut; none deferred, none invented by this seat) = 5 cells cut, matching exactly. SAME GRAIN: each cell is a code fix + test, proved by a local run, none a deploy. INTENT COHERENCE: one axis (bind the render contract to the real, merged modules and prove it); never widened to provisioning. STATE COHERENCE: FWD-2/3/4/8/11 stay NOT_REALIZED until `IB-rtr-5` itself grades PASS -- no cell in wave 1 moves an FWD clock by itself, since none alone proves the chain; write surfaces confirmed at the cut (see R18.2) -- `rtr-c`/`rtr-d` fully disjoint, `rtr-a`/`rtr-b` share two files by disjoint FUNCTION (flagged, not silent) -- so no cell's remedy can silently satisfy another's.

## R17. ROUND 17 -- THE RENDER IDENTITY (PRD v0.17 CONTRACTS items 1-8; L4-R ADMITTED @1450e05178; v0.21, 2026-09-22, `2.0.0_SA_COO~B`)

Round 16 closed with the capture-tool/metadata line fully closed (`C-S174`, `C-S195`) and the standing mechanism question opened for Andrew. Andrew-direct 2026-09-22 ~12:2xZ chose Option 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_122xZ_IRPT_RENDER_AUTH_OPTION2_SHORT_LIVED_RENDER_TOKEN.md @29d157110d`): a short-lived, narrowly-scoped RENDER TOKEN, never a human-captured session, because the portal's own refresh token lives only 7 days. `4.0.0_SA_CRO`'s research (`IRPT_RENDERER_AUTH_RESEARCH_20260922.md @55a47e2cfd`) censused 7 verifiers and recommended a separate signing key; the CTO's PRD v0.16 addendum turned that into a full contract; `3.0.0_SA_CVO~B`'s L4-R review found the v0.16 contract's FIRM_BINDING text FALSE for the principal-resolution path (an offline reproducer showed `classify_principal` returns UNKNOWN and `Enforcer.resolve_now` returns NO_PRINCIPAL for the renderer's own header set); the CTO's v0.17 correction added CONTRACTS item 8, the RENDER_DELEGATE principal. Both L4-R halves are now SIGNED against v0.17 @`1450e05178` (brief unchanged since v0.16, half_hash `9120aa6518e7...`; ratified-text re-signed, half_hash `4d95de5f4f98...`) -- ADMITTED. This round cuts the contract's THREE independent code surfaces, each restating the PRD verbatim. **No AWS write, no Secrets Manager entry, no Lambda deploy, no ledger entry this round** -- every cell builds and proves its component OFFLINE, against a worker-generated throwaway RSA keypair never written to any real secret store; the real key provisioning and every deploy are a SEPARATE later round under NEVER-2 ledger entries and their own never-widen halves (CONTRACTS item 7's own closing line), cut only once this round's code is CVO-adjudicated. PRD: `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657`.

### R17.1 The rectangle (3 cells, id shape `IB-rtq-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtq-1` | **B14 -- THE RENDER-KEY MINTER.** CONTRACTS items 1 (separate key, never `opal/auth/jwt-private-key`), 2 (exact claims: `iss opal-irpt-render`, `aud irpt-render`, `exp<=5min`, `nbf`/`iat` skew<=60s, `jti`=render id, `role renderer`, `tier render`, `firmId`=bundle tenant, `bundle`/`revision`/three path ids, `sub render:<render_id>`, `delegator`=the bundle-freeze subject per item 8), 3 (minted only from the frozen `ExportBundle` inside B14's export job, never from a request, logged with jti+render id), 6 (mint-side logging). Mirror the existing verifier pattern at `infra/aws/lambda/shared/opal_auth/__init__.py` (python-jose, RS256, boto3 `secretsmanager` client, container-cached key fetch) for the SIGNING side, as a NEW module under `infra/aws/lambda/investor-reporting/` (not a shared/opal_auth edit -- this minter is project-private); the private key is loaded by a `RENDER_JWT_PRIVATE_KEY` env var / injectable parameter for testability, never hardcoded, so a test can pass a throwaway keypair. The minter refuses to emit `role admin`, `firmRole admin`, `tier internal`, `userType Dev` (defensive: these must be structurally impossible to set, not merely unset by convention). | `0.9.0_WK_IRPT_BCKEND~14` (first invocation) | FWD-8, FWD-3, FWD-4 (contrib, B14 row) | -- |
| `IB-rtq-2` | **B3 -- THE RESOLVER, THE ENFORCER, AND V2.** CONTRACTS item 8's resolver/enforcer half + item 4's V2 half. In `infra/aws/lambda/investor-reporting/_scope/resolve.py`: add `render` and the three new trusted names (`x-render-delegator`, `x-render-bundle`, `x-render-revision`) to `TRUSTED_HEADERS` (`:88-98`) so `trusted_only` (`:140-150`) stops dropping them; add ONE new branch to `classify_principal` (`:154-196`), placed AFTER the existing origin/subject checks (`:176-180`, "branch 1") and BEFORE the OPAL_GLOBAL roster check (`:181-183`): `x-user-role == "renderer"` WITH the render marker present -> `RENDER_DELEGATE`; `renderer` WITHOUT the marker -> `UNKNOWN` (arm (j)). No existing branch's logic changes; `RENDER_DELEGATE` is added to `PRINCIPAL_CLASSES` (`:106`) and never falls through to `OPAL_GLOBAL`/`FIRM_OPERATIONS`/`FIRM_ADVISOR`/`CLIENT`. In `infra/aws/lambda/investor-reporting/_authz/enforce.py`'s `Enforcer.resolve_now` (`:256`): a `RENDER_DELEGATE` scope is the INTERSECTION of (a) the delegator's scope resolved NOW through the existing path (so revocation takes effect -- arm (i)) and (b) the bundle's pinned scope at `X-Render-Revision`; serves ONLY the three read operations for ONLY the bundle-pinned ids (arm (k) for everything else, refused with the existing refusal codes); an empty intersection refuses, never answers empty. In `infra/aws/users/lambda/portal-authorizer/index.mjs` (default-allow today): load the render public key; admit `aud irpt-render` ONLY when `routeKey` is one of the three named GETs AND each path id equals its claim; every other route/mismatch is an EXPLICIT deny (arm (b)); authorizer result TTL stays 0. | `0.9.0_WK_IRPT_BCKEND~15` (first invocation) | FWD-2 (own, B3 row) | -- |
| `IB-rtq-3` | **B15 -- V3, THE EDGE.** CONTRACTS item 4's V3 half + item 8's edge half. In `infra/aws/lambda-edge/auth-validator-edge/index.mjs`: a new render-key branch that runs BEFORE the admin-bypass evaluation (`:255-261`, the citation this contract refuses a render token to satisfy) and admits the render-key token ONLY for `/investor-reporting/print`, the SPA's static assets, and the same three API paths; on accept, it injects (mirroring the existing `X-Firm-Id` injection shape at `:404`) `X-User-Email render:<render_id>`, `X-User-Role renderer`, `X-Firm-Id` from the VERIFIED `firmId` claim, and the render marker (`X-Render-Delegator`, `X-Render-Bundle`, `X-Render-Revision`) -- overwriting any client-supplied header of those names exactly as the existing trusted set already does; it NEVER injects `X-Advisor-Id`, `X-Advisor-Role` or `X-User-Type`. Any other URI is refused. A render-key token carrying `tier internal` or `role admin` is refused HERE (arm (d)); a render token at V1 (`/auth/...`) is refused there unchanged (arm (e), no V1 edit); a human portal token's existing behavior on every route is unchanged (arm (f), the negative-widening control). | `0.9.0_WK_IRPT_BCKEND~16` (first invocation) | FWD-2 (own, B15 row), FWD-11 (contrib) | -- |

### R17.2 Edges and fanout

Three independent chains -- the contract (PRD v0.17 CONTRACTS "THE RENDER IDENTITY", items 1-8) is the ONLY shared dependency and it is already fully specified text, not another cell's output, so no cell waits on another's code landing. **A** `rtq-1`. **B** `rtq-2`. **C** `rtq-3`. **fanout: 3 of 3 chains, cap 8.**

### R17.3 Bounds carried (every order)

No AWS write of any kind (no Secrets Manager entry, no SSM parameter, no Lambda deploy, no CloudFront/API-Gateway change) -- every cell's proof runs against a worker-generated throwaway keypair and synthetic/fixture requests, offline. No never-widen packet this round (nothing served changes). The end-to-end acceptance arms 7(a)-(k) are NOT a mechanical criterion of any single cell -- each of B14/B3/B15 implements one component; the compound arms are graded by `3.0.0_SA_CVO` at L9 once all three land, reading across the three cells' proof instances together (a compound criterion spanning unlanded code is refused at the cut, per Rule 27's L7 discipline). `IB-rti-6`'s latency re-cut stays PARKED, sequenced behind `IRPT_FNTEND`'s own print-route render-claim branch (CONTRACTS item 5, PRD v0.17 `:224-227`) landing at FNTEND's own next L10 -- not this round, not this project.

### R17.4 Not decided here

The real Secrets Manager/SSM key provisioning and every deploy (a later round under NEVER-2 + never-widen, cut only after this round's CVO adjudication); `IB-rti-6`'s re-hand timing (external, gated on the FNTEND print-route branch); the V3 human `aud`/`iss` standing gap (PRD v0.17 `:263-265`, explicitly a separate change under its own never-widen halves, not this round's); the exact internal module name/path for the B14 minter beyond "a new module under `infra/aws/lambda/investor-reporting/`, never a `shared/opal_auth` edit" (the worker's own choice, following this estate's `_authz`/`_scope`/`_keys` underscore-module convention).

### R17.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = PRD v0.17 CONTRACTS "THE RENDER IDENTITY" items 1-8 (8 items) MINUS items already fully satisfied by construction with no code change (item 5's firm-binding half, satisfied as written by the existing `_authz/served.py`/`enforce.py` `FirmBinding` check; item 6's replay/audit bound, satisfied by the `exp`+scope shape itself with no server-side seen-set to build) MINUS items that are FUTURE/OTHER-PROJECT (item 5's frontend print-route half, `IRPT_FNTEND`'s own PRD; item 7's deploy/acceptance-grading process, not a code surface) = 3 code surfaces (mint / resolve+enforce+V2 / edge V3) = the 3 cells cut. SAME GRAIN: each cell is a set of code edits in named files proved by a local test run, none a live deploy. INTENT COHERENCE: one axis (implement the render-delegate contract), never widened to provisioning or deployment. STATE COHERENCE: no cell moves `FWD-2`/`FWD-11` to REALIZED by itself -- both stay NOT_REALIZED pending the CVO's cross-cell adjudication and the still-separate deploy round; no cell's remedy touches another cell's write surface (B14 mints, B3/V2 and B15/V3 verify -- disjoint files, confirmed against the codebase at cut: `_scope/resolve.py`+`_authz/enforce.py`+`portal-authorizer/index.mjs` for `rtq-2`, `auth-validator-edge/index.mjs` for `rtq-3`, a new module for `rtq-1`, zero overlap).

## R16. ROUND 16 -- THE RECUT ON THE ROUND-15 ANALYSIS (@81338c807a; slug @4870207827; v0.20, 2026-09-22, `2.0.0_SA_COO~B`)

Round 15 closed 0 of 99 open, 0 of 343 worker items undispositioned. `R115-AC1`/`R115-AC2` PASS -- the C-S174 hash repair is genuinely fixed, independently verified by `3.0.0_SA_CVO~B` on its own instruments (a byte reconstruction agreeing with the recomputation, plus a mutation-testing probe confirming the battery genuinely catches both a wrong-CRLF and a wrong-LF mutant). `C-S195` (`R114-AC3` PASS) is unchanged -- the capture tool itself is not in question. **`C-S174` stays OPEN/INERT for exactly one wording residual**, found by the CVO's own review: in the final `IB-rtk-1` proof (blob `f8253e60` @`6b8139682d`), line `:23` correctly records the later pass's PUBLISHED state, but lines `:269-270` still carry an unqualified exclusion ("any real host/SSM/S3 action... everything under stubs/static") that is TRUE of the historical diagnostic pass but FALSE of the publish pass, which DID act on real S3 bytes (with a verified readback). This is metadata only and holds nothing -- it does not reopen the hash work, does not imply a publish replay, and does not touch any code. FWD-2 stays NOT_REALIZED (the qualified human wait -- Andrew's capture is released, the host reads `stopped` on the CTO's own EC2 read); FWD-11 stays NOT_REALIZED. No PRD addendum. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R16.1 The rectangle (1 cell, id shape `IB-rtp-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtp-1` | C-S174 WORDING, SCOPED CORRECTLY (no publish replay, no code change, no behavior change, no hash recomputation -- the hashes are already correct as of `IB-rto-1`). The CTO's own design, restated verbatim as this cell's arms: **(a) SCOPE THE EXCLUSION TO WHAT IT IS ACTUALLY TRUE OF.** In the `IB-rtk-1` proof instance (blob `f8253e60` @`6b8139682d`, lines `:269-270`), the unqualified exclusion "any real host/SSM/S3 action... everything under stubs/static reads" is scoped correctly ONLY for the historical diagnostic pass and for whichever limbs remain genuinely never exercised (host start, SSM calls). It is WRONG for the S3 publish limb, which DID act on real S3 bytes with a verified readback (cited at line `:23` of the same proof). Rewrite the exclusion so it names each limb's TRUE state precisely: historical-diagnostic-pass-only for the parts that are true, and explicitly states the publish pass DID publish to S3 and DID read back, citing the readback evidence already present at line `:23` (or wherever the current text records it). **(b) DO NOT RECUT THE FIXED HASHES.** The CRLF and LF/git-object values are already correct as of `IB-rto-1`'s own fix -- do not touch them, do not re-derive them, do not second-guess them. This cell's ENTIRE scope is the exclusion sentence's wording. **(c) DO NOT REPLAY THE PUBLISH.** No S3 act, no ledger entry, no new packet, no sign-off. The published bytes and their readback already happened and are already correctly recorded; this cell only corrects how the EXCLUSION describes what was and wasn't exercised. **(d) DO NOT TOUCH ANY CODE.** `capture-session.cjs`, `capture-session.sh`, and `README.md` are NOT touched. If tempted, STOP and file a row instead. **(e) VERIFICATION.** Re-run `proof-of-spec-check.py` on the `IB-rtk-1` instance after the wording fix; VALID rc=0 required, no criterion verdict changed. Print the corrected exclusion text in full in the result.md so the CVO/CTO can verify the wording directly rather than trusting a paraphrase. | WK~13 (eleventh invocation, same serial -- continuity of the `deliverables/<SERIAL>/**` ownership) | records integrity (no FWD directly) | -- |

### R16.2 Edges and fanout

One chain: **A** `rtp-1`. **fanout: 1 of 1 chain, cap 8.**

### R16.3 Bounds carried (every order)

No hash recomputation (already correct); no code change; no publish replay; no S3 act; no sign-off. This cell's ENTIRE scope is one exclusion sentence's wording in the `IB-rtk-1` proof instance. `rti-6` stays PARKED at the cut, re-handed the moment `0.0.0_AB_MSTR` relays Andrew's successful capture -- if that relay lands before this round drains, the COO may re-hand `rti-6` INSIDE round 16 as the ruled un-park, not as a new cell.

### R16.4 Not decided here

Whether/when `rti-6` re-hands (external, gated on Andrew's own capture result); `W10-S2` (stays PARKED, unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 172 older stale rows (no bulk close).

### R16.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-15 analysis's round-16 section (2 items: the `C-S174` wording fix, and `rti-6`'s carried park/re-hand rule) MINUS `rti-6`'s carry rule (a rule for a future external event, not a cell issued now) = 1 cell, 0 uncovered, 0 invented by this seat. SAME GRAIN: one wording-scoping correction, sharing one write surface (the `IB-rtk-1` proof instance's own text). INTENT: `rtp-1` corrects wording; it does not repair, recompute, publish, or re-grade anything. STATE COHERENCE: `R114-AC3`'s PASS and `R115-AC1`/`R115-AC2`'s PASS are NOT reopened by this cell -- a residual imprecision in HOW one exclusion sentence described its own scope does not impeach any prior finding's substance, all of which stand independently verified on multiple instruments already.

## R15. ROUND 15 -- THE RECUT ON THE ROUND-14 ANALYSIS (@0782226170; slug @5236fd2696; v0.19, 2026-09-22, `2.0.0_SA_COO~B`)

Round 14 closed 0 of 98 open, 0 of 343 worker items undispositioned. **The capture-tool code line is DONE: `R114-AC3` PASSED** (`3.0.0_SA_CVO~B`'s L9, `ADJUDICATION_v11.md`, row `C-S195` @`d2e855e299`) -- `C-S179` closes on the source and the signed S3 delivery (not on the host, which has not been exercised); `W13-S6` closes via the prospective cut and the typed fixture; `C-S194` closes. The capture ask was released to Andrew at ~10:2xZ after `0.0.0_AB_MSTR` independently re-derived all three release conditions. **No capture-tool code defect remains.** This round is a pure metadata/record-integrity fix, not a behavior repair: `C-S196` (the CTO's own finding in `ADJUDICATION_v11`) shows the round-13/14 `C-S174` metadata correction ITSELF carries two further faults -- a TRANSPOSED CRLF hash value (`...03fbb20...` recorded where the true value, confirmed by both the stored diagnostic and an independent byte reconstruction, is `...03bfb20...`) and a MISATTRIBUTED LF hash (the proof text attributes `f03666ef...` to the worktree diagnostic, which is wrong -- that value is the git-object/LF hash, never what a worktree read produces on this CRLF-checkout box). FWD-2 stays NOT_REALIZED pending the human exercise (the essential, qualified wait -- no seat automates an internal-admin login or MFA); FWD-11 stays NOT_REALIZED and is not cut this round (it depends on the `rti-6` render chain). No PRD addendum. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R15.1 The rectangle (1 cell, id shape `IB-rto-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rto-1` | C-S174 METADATA, PROPERLY CORRECTED (no publish replay, no code change, no behavior change). The CTO's own design, restated verbatim as this cell's arms: **(a) RECOMPUTE, NEVER COPY.** Derive the CRLF value and the LF/git-object value FRESH, from the actual bytes, using the SAME instruments row `W13-S3` and this chain's own precedent established (a raw working-tree read on this box's CRLF checkout for the CRLF value; `git cat-file -p <blob> \| sha256sum` cross-checked with `git show <ref>:<path> \| sha256sum` for the git-object/LF value) -- do NOT copy either value from any prior commit, row, or this order's own citations below, even where they look correct; recompute both from scratch and let the recomputed value be the one you write. **(b) CORRECT THE TRANSPOSED CRLF VALUE.** Wherever `controls.mutant.observed` (or any other proof/metadata text this chain has written) currently reads the transposed `...03fbb20...` form, replace it with the freshly-recomputed correct form. Search every location this chain's own C-S174 fix touched (the `IB-rtm-1` proof instance, `battery_ib_rtm_1.py`, any result.md prose) -- a partial fix that corrects one location and misses a sibling copy is not acceptable. **(c) CORRECT THE MISATTRIBUTED LF HASH.** Wherever the proof or its prose attributes the LF/git-object hash value to "the worktree diagnostic" or similar language implying a raw/checkout-grain read produced it, correct the attribution: the LF/git-object value is what `git cat-file -p`/`git show` produce, NEVER a raw working-tree read on this box, which produces the CRLF value instead (row `W13-S3`'s own finding, restated correctly this time). **(d) ADD A RUN-TIME RECOMPUTATION CONTROL.** Extend `battery_ib_rtm_1.py`'s `--arm metadata` check (or add a new check in the same arm) that FAILS if either the stored CRLF value or the stored LF/git-object value differs from a FRESH recomputation performed at battery run time -- this makes a future silent copy-paste drift into this exact class of error a battery FAILURE, not a manual-review miss. **(e) VERIFICATION.** Run the widened `battery_ib_rtm_1.py --arm metadata` and confirm it PASSES with the corrected values AND that the new recomputation control itself is exercised (print evidence that the control actually ran a fresh computation and compared it, not merely that the stored values look right). Re-run `proof-of-spec-check.py` on every proof instance this cell touches; VALID rc=0 required. **(f) NO PUBLISH REPLAY, NO CODE CHANGE.** This cell touches ONLY metadata/documentation/proof text and the battery script's own check logic -- `capture-session.cjs`/`.sh` and the README are NOT touched, no new packet, no new never-widen sign-off, no S3 act. | WK~13 (tenth invocation, same serial -- continuity of the `deliverables/<SERIAL>/**` ownership) | records integrity (no FWD directly; a correctness precondition for any future citation of this evidence) | -- |

### R15.2 Edges and fanout

One chain: **A** `rto-1`. **fanout: 1 of 1 chain, cap 8.**

### R15.3 Bounds carried (every order)

R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped; no new publish, no new never-widen packet, no S3 act -- this cell is metadata-only; every hash cited must be FRESHLY RECOMPUTED, never copied, including from this very order's own citations; `rti-6` stays PARKED at this cut (Andrew's human exercise has not been relayed as complete as of the cut) and is re-handed the moment `0.0.0_AB_MSTR` relays success -- that re-hand is NOT this round's cell and is not cut here.

### R15.4 Not decided here

Whether/when `rti-6` re-hands (gated on `0.0.0_AB_MSTR`'s relay of Andrew's capture result, not on anything this round decides); `FWD-11` (explicitly not cut this round, depends on the `rti-6` render chain); `W10-S2` (stays PARKED, unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 172 older stale rows (no bulk close).

### R15.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-14 analysis's round-15 section (3 items: the `C-S174` metadata fix, `rti-6`'s re-hand-on-relay carry rule, and `FWD-11`'s explicit non-cut) MINUS `rti-6`'s re-hand (a CARRY RULE for a future tick, not a cell issued now -- it fires on an external relay, not on this cut) MINUS `FWD-11`'s non-cut (an explicit deferral, not a cell) = 1 cell, 0 uncovered, 0 invented by this seat. SAME GRAIN: one record-integrity correction sharing one write surface (the `IB-rtm-1` proof instance, `battery_ib_rtm_1.py`, and any result.md prose the original `C-S174` fix touched). INTENT: `rto-1` corrects metadata; it does not repair, publish, or re-grade anything behavioral. STATE COHERENCE: `R114-AC3`'s PASS grade is NOT reopened or re-graded by this cell -- a metadata citation error in HOW a prior finding was described does not by itself impeach the finding's own substance, which `C-S195` already established on independently re-run instruments; this cell's own postulate does not move that clock.

## R14. ROUND 14 -- THE RECUT ON THE ROUND-13 ANALYSIS (@e107b84d38; slug @12738b5791; v0.18, 2026-09-22, `2.0.0_SA_COO~B`)

Round 13 closed 0 of 97 open, 0 of 343 worker items undispositioned. `R113-AC3` FAIL (`3.0.0_SA_CVO~B`'s L9, `ADJUDICATION_v10.md`, rows C-S188-194): `C-S180` and `C-S187` are confirmed closed individually, and the original timeout-substring counterexample (`C-S179`'s first form) is genuinely fixed. **`1.0.0_SA_CTO`'s round-13 analysis REVERSES its own round-12 sign-off acceptance of row `W13-S6`** -- the "own deadline firing" fallback added in round 13 to avoid regressing the old R11/R12 test fixtures accepts EXACT message-text equality as proof of a timeout, which is STILL a message-text match, not a type-based classification, defeating invariant (iii) ("retry only the three TYPED causes") by construction. The CVO's own companion diagnostic proves it: a `TypeError` and a plain `Error` carrying the identical text `Timeout 60000ms exceeded` both wrongly retry and succeed; a single punctuation change flips the non-`TimeoutError` case to a correct refusal. **Capture stays HELD.** This is the SIXTH capture repair. The CTO's round-13 analysis states the design explicitly and prospectively: from this round on, a timeout is recognised ONLY by error TYPE or a deadline STATE the tool sets itself -- never by any comparison against message text, exact or otherwise -- and declares the old untyped-mock timeout cases HISTORICAL (expected to now report terminal, not a regression). No PRD addendum: every gap is a cell under an existing outcome. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R14.1 The rectangle (1 cell, id shape `IB-rtn-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtn-1` | CAPTURE HELPER SIXTH REPAIR (C-S179 remains the source clock; folds in metadata-only `C-S174`/`C-S194`). The CTO's own design, restated verbatim as this cell's arms: **(a) WHAT COUNTS AS A TIMEOUT.** Exactly one of: `error instanceof playwright.errors.TimeoutError` OR `error.name === 'TimeoutError'`; OR a deadline STATE the tool sets itself (its own `setTimeout`/`AbortController` fires and sets a flag BEFORE the navigation settles, and the catch block reads that flag). NO comparison against any message string, exact or otherwise -- this removes the exact-message fallback entirely. **(b) THE ACCEPTANCE FIXTURE.** A VERSIONED, typed-timeout fixture: throws a genuine `TimeoutError`-named error, with a real deadline behind it where the tool's own timer is involved; written in the cell's own granted test directory under a NEW name; never edits `3.0.0_SA_CVO~B`'s committed diagnostics. **(c) ACCEPTANCE.** The CVO's R13 typed-pair companion, run UNMODIFIED, must now SPLIT: `TimeoutError` recovers; `TypeError` and plain `Error` carrying identical text are terminal. R11/R10 diagnostics unmodified. R12 diagnostic unmodified WITH THE BLOB PASSED EXPLICITLY (its `argv[2]` default is an old blob). R9/R8 diagnostics unmodified. **(d) THE OLD UNTYPED-MOCK CASES ARE NOW HISTORICAL** (R11 "same-origin timeout then clean", R12 "actual timeout positive control" -- both throw an untyped `Error`): EXPECTED to be terminal now; each diff against the historical result is reported as INTENDED, never as a regression. No production code bends to keep them green -- this is the explicit, prospective contract change: from this round on, retry means typed-or-deadline-state only. **(e) PACKAGING.** A new never-widen packet and both halves; the README's expected-hash line is updated in the SAME act as the publish. No host start, no MFA automation. **(f) GRADING.** The bar is unchanged: the four finite invariants from round 12. The JUDGMENT grade (the `R113` successor) is `3.0.0_SA_CVO~B`'s, never the issuer's. Also folds in metadata-only fixes, no publish replay: `C-S174` (attribute the diagnostic hash correctly and print its FULL value -- the battery's check currently compares `[:12]` only, make it compare the full hash); `C-S194` (finalize the result BEFORE pinning the proof; re-pin the R113 proof to the final result blob `af259448...` @`9423390c47`, not the STOPPED `586021b5`). | WK~13 (eighth invocation, same serial -- continuity of the `deliverables/<SERIAL>/**` ownership) | FWD-2 (serving; the `rti-6`/`rth-2` chain's remaining blocker) | -- |

### R14.2 Edges and fanout

One chain: **A** `rtn-1`. **fanout: 1 of 1 chain, cap 8.**

### R14.3 Bounds carried (every order)

The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped; a served-property change (a new publish) is packet + both never-widen halves BEFORE the act; never weaken an existing check to make a new case pass; the retry taxonomy is CLOSED at type-or-deadline-state ONLY, NEVER message text under any framing, exact or substring; `rti-6` stays PARKED; its un-park condition (1) is this round's `rtn-1`. **A sign-off half does not relax a bar** -- the explicit lesson from the CTO's own round-13 self-correction: a half either refuses a reading that conflicts with the issued BOUNDS, or routes the conflict to the bar's owner as a prospective change; it never accepts it inline.

### R14.4 Not decided here

Whether `rtn-1`'s repair is sufficient to re-open the ask to Andrew (`3.0.0_SA_CVO~B`'s successor grade, on the measured battery result, never assumed by the cut); `W10-S2` (stays PARKED, unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 171 older stale rows (no bulk close).

### R14.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-13 analysis's round-14 section (3 items: the sixth capture repair covering the type-or-deadline-state-only redesign, and two metadata-only fixes C-S174/C-S194) MINUS both metadata fixes (folded into `rtn-1`'s own arm, not separate cells -- same write surface, same worker's own deliverables folder, the identical pattern the CTO's own design used for round 13's C-S174/C-S187 and round 11's C-S160) = 1 cell, 0 uncovered, 0 invented by this seat. SAME GRAIN: one classification-redesign defect sharing one write surface (`capture-session.cjs`, the README, the new packet, a new versioned test fixture). INTENT: `rtn-1` repairs. STATE COHERENCE: `C-S153`, `C-S127`, `C-S125`/`C-S126` stay ARMED/host-byte-limited until `rtn-1`'s own judgment grade lands; the CTO's four-invariant bar is unchanged and inherited verbatim a second time, but its invariant (iii) reading is now sharpened (type-or-deadline-state, never message text under any framing) -- this cell does not re-litigate that reading, it implements it.

## R13. ROUND 13 -- THE RECUT ON THE ROUND-12 ANALYSIS (@a8d306eb71; slug @5a9a7eed81; v0.17, 2026-09-22, `2.0.0_SA_COO~B`)

Round 12 closed 0 of 96 open, 0 of 342 worker items undispositioned. `R112-AC3` FAIL (`3.0.0_SA_CVO~B`'s L9, `ADJUDICATION_v9.md`, rows C-S178-187): `C-S170` and `C-S171` are confirmed genuinely fixed on the published bytes (the CTO independently re-read them from S3 himself). The new decisive counterexample is `C-S179` (ARMED): `capture-session.cjs:404` classifies a retryable timeout by matching `/timeout/i` against the error MESSAGE TEXT, so a non-timeout error (e.g. a certificate failure) becomes wrongly retryable whenever the word "timeout" appears anywhere in its message -- one example being a same-origin URL containing `timeout=1`. This violates round 11's own retry-taxonomy bound (arm c: retry only the three TYPED causes). `C-S180` (INERT, not independently decisive): when the post-rename latch recheck fires and `unlink` itself fails (EPERM), the file stays on disk while the tool's own message claims it was deleted -- untruthful reporting, not reachable in normal operation. **Capture stays HELD.** This is the FIFTH capture repair; the CTO's round-12 analysis states the bar as FOUR finite invariants (prospectively, his own criterion prerogative) rather than re-deriving arm-by-arm: (1) no bytes on disk unless the latch is clear after the in-memory capture; (2) only main-frame navigation to a foreign origin latches; (3) retry only the three TYPED causes; (4) every failure is truthfully reported. No PRD addendum: every gap is a cell under an existing outcome. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R13.1 The rectangle (1 cell, id shape `IB-rtm-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtm-1` | CAPTURE HELPER FIFTH REPAIR (C-S179, C-S180; `C-S153`/`C-S127` stay ARMED until this passes). The CTO's own design, restated verbatim as this cell's arms: **(a) CLASSIFY ERRORS BY TYPE, NEVER BY MESSAGE TEXT.** A timeout is recognised ONLY as `error.name === 'TimeoutError'` (Playwright's `errors.TimeoutError`) or the tool's own deadline firing -- never a regex over free text. A 5xx is the response status. A missing marker is the tool's own readiness result. Everything else is terminal, including any `net::ERR_*` navigation error, and prints its cause -- closes `C-S179`. **(b) REPORT CLEANUP FAILURE TRUTHFULLY.** If the post-rename latch fires and deleting the file fails: print `ERROR: session file could NOT be removed: <path> (<errno>) -- delete it manually before any use`, exit with a DISTINCT non-zero code, and the README names that code and the manual step. The contract is a truthful report plus a bounded residual state, never a claim of infallible I/O -- closes `C-S180`. **(c) ACCEPTANCE.** `3.0.0_SA_CVO~B`'s R12, R11, R10, R9 and R8 diagnostics, run UNMODIFIED, must all hold: R12's `ERR_CERT_AUTHORITY_INVALID`-with-`timeout=1`-in-the-message case must now be TERMINAL; R12's actual-timeout positive must still recover; its HTTP 404 control must stay terminal. A single-difference pair for EACH of (a) and (b), each with its own positive control. **(d) DELIVERY.** A new never-widen packet and both halves; the README's expected-hash line is updated in the SAME act as the publish. No host start, no MFA automation. **(e) THE BAR IS THE FOUR FINITE INVARIANTS** (stated by the CTO, prospectively): (1) no bytes on disk unless the latch is clear after the in-memory capture; (2) only main-frame navigation to a foreign origin latches; (3) retry only the three TYPED causes; (4) every failure is truthfully reported. A future counterexample FAILs the grade only if it defeats one of these four; one that defeats none opens a row and does not by itself hold the capture. **(f) THE JUDGMENT GRADE (successor to `R112-AC3`) is `3.0.0_SA_CVO~B`'s, never the issuer's.** Also folds in metadata-only fixes carried from round 12's slug, no publish replay: `C-S174` (correct `controls.mutant.observed`'s text so it accurately describes `fffef738` as the worker's original CRLF/checkout-grain value and `f03666ef` as the git-object sha256, never calling either a "packet-only typo"); `C-S187` (re-pin the result to the post-publish HEAD, scope the "no real S3" exclusion to the pass it actually applies to). | WK~13 (sixth invocation, same serial -- continuity of the `deliverables/<SERIAL>/**` ownership) | FWD-2 (serving; the `rti-6`/`rth-2` chain's remaining blocker) | -- |

### R13.2 Edges and fanout

One chain: **A** `rtm-1`. **fanout: 1 of 1 chain, cap 8.**

### R13.3 Bounds carried (every order)

The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped; a served-property change (a new publish) is packet + both never-widen halves BEFORE the act; never weaken an existing check to make a new case pass; the retry taxonomy is CLOSED (exactly three TYPED causes, classified by type never by message text) and NEVER widened past it; `rti-6` stays PARKED; its un-park condition (1) is this round's `rtm-1`. **Worker-worktree hygiene, per the CTO's ruling on `S117`:** before ANY worktree is removed, the worker's final report is required, termination is confirmed, and dirty work is reconciled -- a commit landing is not end-of-turn. The issuer (`2.0.0_SA_COO~B`) owns this for every drain this round.

### R13.4 Not decided here

Whether `rtm-1`'s repair is sufficient to re-open the ask to Andrew (`3.0.0_SA_CVO~B`'s successor grade, on the measured battery result, never assumed by the cut); `W10-S2` (stays PARKED, unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 168 older stale rows (no bulk close).

### R13.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-12 analysis's round-13 section (3 items: the fifth capture repair covering C-S179/C-S180, and two metadata-only fixes C-S174/C-S187) MINUS both metadata fixes (folded into `rtm-1`'s own arm, not separate cells -- same write surface, same worker's own deliverables folder, same pattern the CTO's own design used for round 11's C-S160) = 1 cell, 0 uncovered, 0 invented by this seat. SAME GRAIN: one repairable classification-and-reporting defect pair sharing one write surface (`capture-session.cjs`, the README, the new packet). INTENT: `rtm-1` repairs. STATE COHERENCE: `C-S153`, `C-S127`, `C-S125`/`C-S126` stay ARMED/host-byte-limited until `rtm-1`'s own judgment grade lands -- this cell does not move those clocks by proxy, and the CTO's four-invariant bar (R13's own text) is inherited verbatim rather than re-derived, so a future counterexample is graded against a FIXED bar this round did not invent.

## R12. ROUND 12 -- THE RECUT ON THE ROUND-11 ANALYSIS (@23d5fe2e6b; slug @d20200b92c; v0.16, 2026-09-22, `2.0.0_SA_COO~B`)

Round 11 closed 0 of 95 open, 0 of 338 worker items undispositioned. `R107-AC3` FAIL (`3.0.0_SA_CVO~B`'s L9, `ADJUDICATION_v8.md`, rows C-S169-177): the round-11 repair genuinely closes both R10 residuals, but TWO further defects surfaced from its OWN new diagnostic -- `C-S170` (ARMED, pre-existing, not introduced this round): the final `refuseIfLatched()` runs BEFORE `await context.storageState()`, so a foreign navigation during that await still latches yet the write proceeds; `C-S171` (ARMED, a NEW regression this round): the response listener carries no navigation filter, so an ordinary same-origin PAGE's foreign-origin SUBRESOURCE (an image, a font, an analytics call) wrongly latches a terminal refusal even though the page itself never left the portal. **Capture stays HELD.** This is the FOURTH capture repair; the CTO's round-11 analysis names the recurring cause explicitly -- each prior repair guarded a POINT in the lifecycle (a specific navigation, a specific retry) rather than the INVARIANT (no bytes reach disk unless the origin was never violated), and states round 12's design to guard the invariant at the one place the file is written, restated verbatim below as the cell's arms, not re-derived. No PRD addendum: every gap is a cell under an existing outcome. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R12.1 The rectangle (1 cell, id shape `IB-rtl-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtl-1` | CAPTURE HELPER FOURTH REPAIR (C-S170, C-S171; `C-S153`/`C-S127` stay ARMED until this passes). The CTO's own design, restated verbatim as this cell's arms: **(a) THE INVARIANT -- no bytes reach disk unless the latch is clear AFTER the state was captured.** Capture `storageState()` to MEMORY, no `path` argument. Then check the latch. Only then write the file, atomically (write to a temp file, then rename). Check the latch AGAIN immediately after the rename; if it has set, delete the file and exit non-zero. This makes the TIMING of any navigation irrelevant, because the check follows the last await that could admit one -- closes `C-S170`. **(b) THE OBSERVER'S SCOPE IS MAIN-FRAME NAVIGATIONS ONLY.** `request.isNavigationRequest()` AND `frame === page.mainFrame()`, on BOTH the request and the response paths (the request path already has this; the response path does not, which is exactly `C-S171`'s regression). Foreign subresources never latch -- the property being guarded is WHERE THE PAGE IS, not what it loads. **(c) RETRY TAXONOMY -- behavior and documentation must agree, literally.** The code retries EXACTLY the set the README lists: a timeout, a 5xx response, a marker-absent-after-load. Any other outcome is a terminal refusal with its cause printed. A foreign origin is never retryable, under any framing (folds in `W13-S1`'s carried finding: a `404` or a generic non-timeout navigation error must NOT silently retry alongside the three named causes). **(d) ACCEPTANCE.** `3.0.0_SA_CVO~B`'s R11, R10, R9 and R8 diagnostics, run UNMODIFIED, must all hold: R11 must now refuse the final-await case AND must succeed on BOTH same-origin twins (the navigation twin and the resource twin). A single-difference pair for EACH of (a) and (b), each with its own positive control. **(e) PUBLICATION.** A new never-widen packet and both halves; the README's expected-hash line is updated in the SAME act as the publish, exactly as `IB-rtk-1`'s own fourth pass did it. No host start, no MFA automation. **(f) THE JUDGMENT GRADE (successor to `R107-AC3`) is `3.0.0_SA_CVO~B`'s, never the issuer's.** | WK~13 (fifth invocation, same serial -- continuity of the `deliverables/<SERIAL>/**` ownership) | FWD-2 (serving; the `rti-6`/`rth-2` chain's remaining blocker) | -- |

### R12.2 Edges and fanout

One chain: **A** `rtl-1`. **fanout: 1 of 1 chain, cap 8.**

### R12.3 Bounds carried (every order)

The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped; a served-property change (a new publish) is packet + both never-widen halves BEFORE the act; never weaken an existing check to make a new case pass; the retry taxonomy is CLOSED (exactly three named causes) and NEVER widened past it; `rti-6` stays PARKED; its un-park condition (1) is this round's `rtl-1`.

### R12.4 Not decided here

Whether `rtl-1`'s repair is sufficient to re-open the ask to Andrew (`3.0.0_SA_CVO~B`'s successor grade, on the measured battery result, never assumed by the cut); `W10-S2` (stays PARKED, unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 166 older stale rows (no bulk close).

### R12.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-11 analysis's round-12 section (2 items: the fourth capture repair covering C-S170/C-S171/W13-S1's retry taxonomy, and C-S174's metadata reconciliation) MINUS C-S174 (already satisfied -- the recovery drain @`495359ce62`, independently re-verified by the issuer this tick: `DEPLOYED-VERIFIED` state, correct hash, corrected packet row, both `W13-S1`/`W13-S2` present in `surprises`, historical framing preserved; no further commit needed) = 1 cell, 0 uncovered, 0 invented by this seat. SAME GRAIN: one repairable defect pair sharing one write surface (`capture-session.cjs`, the README, the new packet). INTENT: `rtl-1` repairs. STATE COHERENCE: the invariant-based design is chosen specifically because the prior three repairs each fixed a POINT and left the INVARIANT unguarded -- this round's four-postulate record inherits that lesson rather than repeating the same class of gap a fifth time.

## R11. ROUND 11 -- THE RECUT ON THE ROUND-10 ANALYSIS (@703efac869; slug @79d34e339c; v0.15, 2026-09-22, `2.0.0_SA_COO~B`)

Round 10 closed 0 of 94 open, `R102-AC1` PASS (independently corroborated by the CTO), **`R101-AC3` FAIL** (`3.0.0_SA_CVO~B`'s own lifecycle diagnostic, `IRPT_BCKEND_R10_CAPTURE_LIFECYCLE_DIAGNOSTIC.cjs`: the round-10 repair genuinely closes the C-S153 counterexample but two DIFFERENT, pre-existing residuals survive -- `C-S158`, no navigation observer during the human-interaction wait, so a foreign hop that occurs and returns during that wait is invisible and capture still succeeds; `C-S159`, a detected foreign hop on the verification navigation is treated as retryable rather than terminal, so the violation is forgotten on a clean retry). **Capture stays HELD.** `R102-AC2` came back `NOT_EVALUATED` for a defect in the ORDER, not the work: `IB-rtj-2`'s face listed it in `<expected_criteria>` but never defined a substantive bar (`C-S162`) -- the CTO ruled it RETIRED, prospectively, never re-issued with an invented retrospective bar; `R102-AC1`'s PASS is not overturned or asked to cover for it. No PRD addendum: every gap is a cell under an existing outcome. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R11.1 The rectangle (1 cell, id shape `IB-rtk-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtk-1` | CAPTURE HELPER THIRD REPAIR (C-S158, C-S159; folds in C-S160's metadata fix as its own first arm since it's the same worker's own deliverables folder). Design direction is the CTO's own, restated verbatim as the cell's arms, not re-derived: (a) fix `IB-rtj-1`'s stale second-pass proof-instance pin first (C-S160), metadata only, no publish replay; (b) install ONE session-lifetime navigation observer on the page BEFORE the first `goto` (`framenavigated` filtered to the main frame, plus response/request listeners), live through the whole interactive interval and every verification navigation; (c) refusal is TERMINAL and STICKY -- the first foreign origin the observer sees at any point latches a refusal, writes nothing, prints no success, exits non-zero, and no later clean navigation clears the latch (closes C-S159); (d) the retry path survives ONLY for same-origin transient failures (a timeout, a 5xx, a missing marker) -- a foreign hop is never retryable; (e) acceptance: CVO~B's unmodified R10 lifecycle diagnostic refuses both residuals, the R9 and R8 diagnostics still pass, a single-difference interval pair (same-origin vs. middle-hop-foreign) with a positive control, a single-difference retry pair (foreign-then-clean vs. transient-then-clean, the transient case still succeeds); (f) a NEW never-widen packet and both halves, runbook hashes updated in the same cell, no host start, no MFA automation. **The judgment grade (successor to `R101-AC3`) is `3.0.0_SA_CVO~B`'s, never the issuer's.** | WK~13 (third pass, same serial -- avoids the `deliverables/<SERIAL>/**` ownership issue `IB-rti-1`'s C-S154 fix hit) | FWD-2 (serving; the `rti-6`/`rth-2` chain's remaining blocker) | -- |

### R11.2 Edges and fanout

One chain: **A** `rtk-1`. **fanout: 1 of 1 chain, cap 8.** `C-S162` (retire `R102-AC2`) is ISSUER-DISCHARGED at the cut, a face correction on `IB-rtj-2`, not a chain.

### R11.3 Bounds carried (every order)

The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped; a served-property change (a new publish) is packet + both never-widen halves BEFORE the act; never weaken an existing check to make a new case pass; the retry path narrows, it never widens (same-origin-transient only, per the CTO's arm (d)). `rti-6` stays PARKED; its un-park condition (1) is this round's `rtk-1`, corrected onto its face @`460df053b5`.

### R11.4 Not decided here

Whether `rtk-1`'s repair is sufficient to re-open the ask to Andrew (`3.0.0_SA_CVO~B`'s successor grade, on the measured battery result, never assumed by the cut); `W10-S2` (stays PARKED, unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 164 older stale rows (no bulk close).

### R11.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-10 analysis's round-11 section (2 items: the third repair covering C-S158/C-S159 with C-S160 folded in as its own arm, and C-S162's retirement) MINUS the ONE merge already built into the CTO's own design (C-S160 as `rtk-1`'s arm (a), not a separate cell) MINUS C-S162 (issuer-discharged, a face edit, not a worker chain) = 1 cell, 0 uncovered, 0 invented by this seat. SAME GRAIN: one repairable defect pair sharing one write surface (`capture-session.cjs`, the README, the new packet). INTENT: `rtk-1` repairs. STATE COHERENCE: `C-S153`, `C-S127`, `C-S125`/`C-S126` stay ARMED/host-byte-limited until `rtk-1`'s own judgment grade lands -- no cell here moves their clocks by proxy.

## R10. ROUND 10 -- THE RECUT ON THE ROUND-9 ANALYSIS (@9d4052728b, msg 99334; slug @a62b69f6d3; v0.14, 2026-09-22, `2.0.0_SA_COO~B`)

Round 9 closed 0 of 91 open, R92-AC3 PASS, R93-AC3 NOT_EVALUATED, **R91-AC7 FAIL** (`3.0.0_SA_CVO~B`'s round-9 L9, row `IRPT_BCKEND-C-S153`: the capture helper's first `page.goto` discards its response, so a portal -> foreign-origin -> portal redirect hop followed by valid authentication still writes a session and reports success). A second finding, `C-S156`, showed the human runbook starts the host and runs the wrapper without first delivering or hash-verifying the fixed bytes, so a human following it today would run the OLD tool. **The CTO's own round-8 rti-6 park ruling that called the capture tool "fixed" and the ask to Andrew "unblocked" was WRONG on both counts and is corrected in the round-9 analysis; the ask was RE-HELD.** No PRD addendum: every gap is a cell under an existing outcome, and the capture defect is a tooling defect, not an endpoint mis-statement. FWD-2 stays SPLIT/NOT_REALIZED; FWD-11 backend ADVANCED/overall NOT_REALIZED; nothing claims REALIZED. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R10.1 The rectangle (4 cells, id shape `IB-rtj-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rtj-1` | CAPTURE HELPER SECOND REPAIR + HOST-DELIVERY RUNBOOK (C-S153/C-S127 merged with C-S156, one cell on the CTO's invitation to merge on write-path overlap -- both live under `infra/aws/ec2/investor-reporting-export/`, both gate the same un-park condition, and a worker repairing the code is the natural author of the runbook step that delivers it). Guard the COMPLETE navigation lifecycle (the initial response, every hop, the interactive interval), not just the final URL. Acceptance: `3.0.0_SA_CVO~B`'s redirect diagnostic (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R9_CAPTURE_REDIRECT_DIAGNOSTIC.cjs`) unmodified refuses every counterexample arm; the round-8 diagnostic still passes; a single-difference initial-foreign-return regression plus an authenticated-positive control; the README's runbook DELIVERS the fixed bytes to the host and VERIFIES both hashes BEFORE any capture or credential entry, as an explicit printed step. No allowlist widening, no MFA automation; fold in W9-S1 (derive the allowlist from `IRPT_PORTAL_ORIGIN`, `ssm.tf:84`, or fail on drift, never a typed/widened value). A new publish needs its own packet + both never-widen halves at HEAD. | WK~13 | FWD-2 (serving; the rti-6/rth-2 chain's remaining blocker) | -- |
| `IB-rtj-2` | L4 BOUNDED TEST PRINCIPAL (W11-S1; CTO ruling msg 99312 CALL 1): one NON-EXEMPT role, created through Terraform (`safe-apply`), matching neither `*-inf-*` nor `*-cot-*` (name printed beside both `ArnNotLike` lists). Its ONLY grant: `s3:ListBucket` on `opal-data-inflection` + `opal-data-cottonwood` plus one unfenced control bucket. Positive arm on the control; negative arm on each fenced bucket, the deny attributed to the resource policy's explicit deny (CloudTrail or S3 error context), never the bare code. The role is DESTROYED in the same session; deletion verified by `get-role` -> `NoSuchEntity`. Change-management ledger entry opened at start, closed at completion. **SIGN-OFF: two halves, CTO + CRO** (the CloudOps~V precedent), before the Terraform apply -- this supersedes the CTO's 99299 "no grant is widened" line for this ONE bounded, self-deleting role only. Addressed as a task order to the LIVE Tier-2 seat, never a new v3 worktree (LD-0529; no new lane seated -- `0.7.0_AE_CloudOps~V` is already live). | `0.7.0_AE_CloudOps~V` | FWD-11 | -- |
| `IB-rtj-3` | METADATA REPAIR (C-S154): the rti-1 proof instance named two FIRST-PASS blobs (battery, publish-output) after a second pass replaced both; `declared_exclusions` and `compiler_tools` still said arm (f) never ran. **ISSUER-DISCHARGED AT THE CUT, already complete -- no worker order:** a pure record-accuracy fix using facts the CVO already established, same pattern as `rti-4`/`rti-5`. Re-verified both blobs against `git rev-parse HEAD:<path>` before editing; no criterion verdict changed; `proof-of-spec-check` re-run clean (rc 0, 7 rows, 0 violations); an issuer addendum appended to the worker's result.md (prior text retained) rather than a rewrite. Committed @`809b35f48d` under the audited singular `GIT_COMMIT_AUTHOR_OVERRIDE` (the owning worker `0.9.0_WK_IRPT_BCKEND~9` is disbanded; `deliverables/<SERIAL>/**` is owned by the serial in the path, never the issuer, per `owned-paths-validate.py` clause 4 -- discovered this round, first use of the override in this project). | issuer (complete) | records integrity | -- |
| `IB-rtj-4` | SOURCE-MAP NOTE CORRECTION (W10-S3): `lambda-source-map.json`'s `_staged_from_note` on the `irpt-ycharts-generate` entry still says no source exists for the two members, beside the two `staged_from` pins (rti-2) that now resolve them. Correct the note only -- no widened deployment scope, no copy of served files. Grant: exactly this one file, `<paths>`-scoped, matching the `rti-2`/`W10-S2` precedent (a v3 worker's write surface is its order's `<paths>`, not `.owned-paths.yaml`'s `YANG_PIPELINE_DEPLOY` lane, which does not enumerate a worker). | WK~14 | records integrity | -- |

### R10.2 Edges and fanout

Chains (an edge chain is a chain; an issuer-discharged cell is not): **A** `rtj-1`; **B** `rtj-2`; **C** `rtj-4`. `rtj-3` is discharged at the cut (already complete, above) and carries no chain. **fanout: 3 of 3 chains, cap 8.** Disjoint write surfaces (capture-tooling directory + README; a new IAM role + two bucket policies, read/destroy only; one JSON note) -- A, B, C run in parallel. B is issued to an existing live Tier-2 seat, not a new worktree.

### R10.3 Bounds carried (every order)

The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped by any cell (rtj-1 included -- the runbook is written and battery-tested under stubs, never exercised against the real host by the worker); a served-property change (a new publish, a Terraform apply) is packet + both never-widen halves BEFORE the act; **rtj-2's role is the ONE exception to "no grant widened" this round, self-deleting, CTO+CRO halves, never a precedent for any other principal.** rti-6 stays PARKED; its amended un-park condition (1) is this round's `rtj-1`, written onto its face @[this round's issuance commit].

### R10.4 Not decided here

Whether `rtj-1`'s repair is sufficient to re-open the ask to Andrew (the CTO's call, on the measured battery result, never assumed by the cut); the ycharts redeploy (`W10-S2`, stays PARKED, its own un-park condition unchanged); `S116`/`W1-S47` (CTO's own lane); break-glass role deletion (CRO/Andrew); the 159 older stale rows (no bulk close); a `listAnalysisRequests` route (only if an FWD needs it, none does today).

### R10.5 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-9 analysis's round-10 wave-1 list (5 items: capture repair, host-delivery runbook, L4 bounded principal, metadata repair, source-map note) MINUS the ONE merge the CTO invited and this seat took (capture repair + host-delivery runbook -> one cell, `rtj-1`, on write-path overlap) = 4 cells, 0 uncovered, 0 invented by this seat. SAME GRAIN: each cell is one repairable defect or one bounded measurement act. INTENT: `rtj-1` repairs, `rtj-2` measures-then-destroys (a bounded, self-deleting test), `rtj-4` corrects a record. STATE COHERENCE: `rtj-3`'s fix moves no criterion verdict (Rule 22's STATE axis: DESIRED ≠ APPLIED ≠ EXERCISED -- the artifact citations were wrong, the underlying PASS/FAIL facts were not); `rtj-2`'s role, once destroyed and verified `NoSuchEntity`, leaves no standing grant.

## R9. ROUND 9 -- THE RECUT ON THE ROUND-8 ANALYSIS (@8e0f9a127e, msg 99299; slug @9d7a369b38; v0.13, 2026-09-21, `2.0.0_SA_COO~B`)

Round 8 closed with NO PRD addendum and no outcome REALIZED (FWD-2 SPLIT and NOT_REALIZED; FWD-11's backend half
ADVANCED, NOT_REALIZED). Round 9 is the CTO's wave-1/wave-2 carry, cut in ONE issuance. Prd: `../prd/IRPT_BCKEND_PRD.md` v0.15.

### R9.1 The rectangle (6 cells, id shape `IB-rti-<n>`)

| cell | what | executor | outcome | edges |
|---|---|---|---|---|
| `IB-rti-1` | CAPTURE-TOOL REPAIR (C-S125/126/127; R80-AC2 FAIL): the emitted port-forward command executable verbatim and the README matching it; a POSITIVE authenticated-readiness signal that refuses error, redirect and 5xx pages; the portal origin ENFORCED. Acceptance includes CVO~B's own VM diagnostic (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R8_CAPTURE_DIAGNOSTIC.cjs` @06fe4f1848): its HTTP500 and arbitrary-origin counterexamples must REFUSE, its password-present control must still pass. No host start, credential or live login. Two-pass: source + packet, STOP for both never-widen halves, then S3 publish. | WK~9 | FWD-2 (serving; unblocks the rth-2 chain) | -- |
| `IB-rti-2` | S102, THE YCHARTS MISSING-SOURCE BUILD DEFECT: `irpt-ycharts-generate` cannot be rebuilt from HEAD (its `files[]` declares `firm_registry.json` and `settings.json`, neither with a tracked source). CVO confirmed NOT fixed (S111 amended the DENOMINATOR only). INVESTIGATE FIRST, read-only; a member is declared from a TRUE source or the cell STOPS -- never a hand copy of served bytes (S96). Rebuild-and-compare only; NO apply. | WK~10 | FWD-2 / FWD-4 (the export chain) | -- |
| `IB-rti-3` | L4 NEGATIVE CONTROL, INSTRUMENT REVISED BY THE CTO'S RULING: for each of 2 buckets, an EXISTING non-exempt principal whose IAM already allows the exact action, a POSITIVE arm outside the fence, a NEGATIVE arm attributable to the bucket policy (never the bare error code). If none exists the honest result is "cannot discriminate without a new grant" -- a finding routed to the CTO, not a PASS. No grant widened, no host started. | WK~11 | FWD-11 | -- |
| `IB-rti-4` | C-S144: THE R77 SUCCESSOR BAR. **ISSUER-DISCHARGED AT THE CUT -- no worker order:** a judgment bar is the issuer's to write. It is issued as `R96-AC3` on `IB-rti-6`'s face (R9.4 below); `R77-AC2` stays NOT_EVALUATED, no retroactive PASS. | issuer | FWD-2 | -- |
| `IB-rti-5` | PREMISE CORRECTIONS (W3-S51 / C-S134, W1-S46 / C-S135). **ISSUER-DISCHARGED AT THE CUT -- no worker order:** errata on the faces and R8.10 above, commit `ca91fbc11b` (originals retained under R-43; nothing flipped to `complete`). | issuer | records integrity | -- |
| `IB-rti-6` | WAVE 2 -- THE RTH-2 RE-CUT: rth-2's ORIGINAL bounded latency measurement re-run unchanged, under a session the FIXED tool verified authorized (ruling @438312b085 + addendum @e73c8e2f71). Rows W2-S62, W3-S52, W1-S43 ride with it. **Authentication and render latency stay SEPARATE questions.** The sync-vs-async contract is the CTO's, decided on the measured number, not before; NO wiring is built here. **STAGED**: becomes pending only when `IB-rti-1` is complete and deployed AND a human has started the host and captured a session. | WK~12 (staged) | FWD-2 | `IB-rti-1`, a human session |

### R9.2 Edges and fanout

Chains (an edge chain is a chain; an issuer-discharged cell is not): **A** `rti-1`; **B** `rti-2`; **C** `rti-3`;
**D** `rti-6 <- rti-1 (+ a human session)`. `rti-4` and `rti-5` are discharged at the cut and carry no worker.
**fanout: 3 of 4 chains at the hand-off, cap 8, reason: chain D is gated on chain A and on Andrew's session;
`rti-4`/`rti-5` are issuer acts.** A, B, C are independent (disjoint write surfaces: the capture tooling directory;
the ycharts source dir + source map; read-only IAM census) and run in parallel -- the parallelism the CTO named.

⚠ **ROUND-OPEN IMPLICATION, stated so it is not discovered later:** `rti-6` is a STAGED order; the refuser counts it
open, so round 9 cannot close until it drains or is disposed. If waves 1's cells are terminal and the human session
has not landed, the round would be held by a human calendar exactly as round 8 was. The remedy is the same one that
worked: ask the CTO to PARK `rti-6` for the round-9 close with owner and un-park condition on the order. Raised with
the CTO in the issuance message; NOT assumed.

### R9.3 Bounds carried (every order)

The forward-looking-criterion bar; R-40 (content hash per run/artifact READ AT the event); S56 vintage pins
`path:line @ <commit-ish>`; NO LIVE VENDOR CALL; no host is started or stopped by any cell; no grant widened; a
served-property change is packet + both never-widen halves BEFORE the act; a lane refusal on a granted path is a
BLOCKING row, never an override (row W1-S48's lesson: the source map is lane-gated).

### R9.4 The R77 successor bar (C-S144) -- issued as `R96-AC3`

PASS iff ALL of: (i) AUTHENTICATION IS SEPARATE AND PROVEN -- the session the measurement used is one the FIXED
capture tool verified against its POSITIVE readiness signal (the instance cites that tool run's own output and the
deployed blob hash, never a hand-made file), and the renderer's run shows authenticated print-route access rather than
SESSION_ABSENT; (ii) THE NUMBER ANSWERS THE QUESTION -- N renders as the original bounded measurement specified, each
identified by its SSM command id, with min/median/max and denominators, none from the excluded invalid-origin run, each
PDF a nonzero byte length; the sync-vs-async question stated against the 29,000 ms gateway ceiling, never against the
900 s script budget; (iii) NO CLAIM BEYOND THE MEASUREMENT -- no contract decision (the CTO's), no wiring built, and any
"a receipt is produced" backed by a receipt read from the real path or absent. FAIL if any of the three rests on the
absence of a negative. NOT_EVALUATED only if the session or the measurement did not occur.

### R9.5 Not decided here, and named so it is not silently adopted

The sync-vs-async contract (CTO). `S116` and `W1-S47` (`lib/opal_naming.py`, the CTO's own lane, LGIC_ENFORCE). Deleting
the two break-glass roles (CRO / Andrew). The 150 older rows rth-4 carried stay open -- no bulk close. FWD-5's
realization exercise (no claim this round). NOT re-dispatched, REMEDIATED in-round: W1-S48, S111, S112, S113, W7-S2, W8-S2.

### R9.6 Four-postulate record (Rule 24, by SUBTRACTION from the printed denominator)

Denominator = the CTO's round-8 analysis, wave 1 (5 items) + wave 2 (1 item) = 6. MINUS the REMEDIATED-in-round set
(6 rows, excluded by the CTO's own ruling) MINUS the external set (S116, W1-S47, role deletion, the 150 rows) = 6 cells,
0 uncovered, 0 invented by this seat. SAME GRAIN: each cell is one repairable defect or one measurement. INTENT: `rti-1`
repairs, `rti-2` investigates-then-builds, `rti-3` measures, `rti-6` measures. STATE COHERENCE: a cell that finds it cannot
proceed (no eligible principal; a member with no true source; no session) records that as its result and does NOT
manufacture a pass -- the one remedy each names.

## R8. ROUND 8 -- THE RECUT ON THE ROUND-7 ANALYSIS (@0d400d5c07, msg 98978; v0.8, 2026-09-21, `2.0.0_SA_COO~B`)

**Input:** round 7 CLOSED at L10 (0 open of 79 proof-based; 4/4 AC2 PASS, none self-graded; CVO slug @`357565e863` -- 12 rows, 9 GRADUATED / 3 DISMISSED). The CTO's analysis @`0d400d5c07` affirms the CVO's grades: **FWD-5 ADVANCED-NOT-REALIZED** (the refusal affirmed over the completion report's headline -- ⭐ *"removing a blocker is not realizing an outcome"*; the S100 fix is real work graded at R75-AC2 PASS, but FWD-5's own DONE WHEN names a three-firm replay with reconcile-before-and-after and denominators that nobody has run); **FWD-2 SPLIT** (containment REALIZED round 6, serving ADVANCED-NOT-REALIZED on W3-S50 + W1-S43). No PRD addendum. Round 8 closes the two disclosed serving-half gaps and the records-hygiene the round-7 close surfaced.

### R8.1 The rectangle (4 cells, id shape `IB-rth-<n>`)

| cell | owes | assignee | serves | supersedes |
|---|---|---|---|---|
| IB-rth-1 | INFLECTION serving route (W3-S50): the live 2-of-3 shortfall is an S3 404 in `_authz/served.py::enforcer_for`'s eager ownership-map load for inflection, UPSTREAM of `route_for`. INVESTIGATE FIRST (read-only): whether inflection's ownership-map object can be produced/read on the EXISTING `opal-data-inflection` bucket without the console -- a discriminating s3 call, the wire result verbatim. ⚠ BOUNDED BY ANDREW-DIRECT 98869 answer 2, HIS TERMS NOT WIDENED: rectify the EXISTING bucket FIRST; a minted principal ONLY if rectification cannot be done; new buckets the LAST resort and he said he would prefer not; **the root console is NOT an option**. If the fix needs the mint-principal or new-bucket branch, STOP and carry to the CTO/Andrew with the discriminating evidence -- never taken ad hoc. Any served/bucket change is packet + halves BEFORE the act. Acceptance: inflection's live performance request resolves a TenantRoute end-to-end (no S3 404, no UNEXPECTED), 3-of-3 firms live. | WK | FWD-2 (serving) | -- |
| IB-rth-2 | EXPORT SUBMIT-WIRING (W1-S43): the deployed `submit_export` raises NOT_READY -- the receipt CONTRACT is proven (round-7 rtg-1 R72 PASS) but the submit controller that produces a receipt in production is not wired. Wire it; packet + halves BEFORE the deploy (the rtg-1 shape); acceptance: an exercised submit-export -> receipt round trip on the REAL path produces + serves the receipt (no NOT_READY), the S105/S106 taxonomy unchanged. | WK | FWD-2 (serving) | IB-rtg-1 (the submit half rtg-1 disclosed) |
| IB-rth-3 | STATUS-WORD HYGIENE: the 7 orders terminal-by-proof at HEAD whose `<status>` word is not terminal (`IB-rt-6`, `rtf-3`, `rtf-4`, `rtf-7`, `rtf-10`, `rtf-12`, `rtf-14`) -- flip each face's `<status>` to a terminal word citing its VALID proof instance, changing NOTHING else. ⚠ BOOKKEEPING, NOT RE-WORK: the proofs are VALID at HEAD and terminality already reads from them; this only stops a status-word census returning a wrong number (the §4 class three projects over). Acceptance: the status-word count and the gate's proof-based resolver AGREE for IRPT_BCKEND. | WK | records integrity | -- |
| IB-rth-4 | THE 110 STALE OWNED REMEDIATION ROWS (2+ rounds unmoved; the gate's 9x non-refusal disclosure) -- a DISPOSITION-PER-ROW cell, owned by `2.0.0_SA_COO~B` as issuer. ⛔ NOT a bulk close; ⛔ NO row closed by AGE (staleness is a PROCESS signal, never HAZARD evidence -- the label-vs-evidence inversion); each row on its OWN evidence, a still-live row STAYS live and says so; the cell PRINTS its denominator + per-disposition counts so the next round can tell a real fall from a narrowed census. | WK | channel hygiene | -- |

**Not cells of this project:** FWD-5's REALIZATION exercise -- its OWNER line names `IRPT_FNTEND` for the three-firm replay; this project holds join correctness, the reconcile control, the denominators and the revision-bound `HoldingsSnapshot`, which round 8 MAY build as this project's SHARE but which CANNOT realize FWD-5 alone (a round-8 report claiming FWD-5 REALIZED is refused on the round-7 grounds). The broader FWD-11 bucket program beyond inflection's serving path (Andrew). The `opal-data-inflection` ownership-map PRODUCER re-key, if the map is missing at source (DS `d08`).

### R8.2 Edges and fanout
Four INDEPENDENT chains (disjoint write surfaces -- inflection authz/bucket; export submit; order faces; the surprise channel): A `rth-1`; B `rth-2`; C `rth-3`; D `rth-4`. **fanout: 4 of 4 chains, cap 8.** No cross-cell dependency. ⚠ **EXECUTION PACED ONE WORKER AT A TIME** under Andrew's ~02:4xZ stay-light hold (98915/98916): the issuance cuts all four; the COO spawns them SERIALLY, reusing one worktree per slot, the two records-hygiene cells (rth-3, rth-4 -- no served change) ahead of the two served-change cells (rth-1, rth-2).

### R8.3 Bounds carried
NEVER-1 (packet + CTO+COO halves at HEAD BEFORE any served/bucket change -- rth-1's rectification if it writes, rth-2's deploy); the arm-(d) SUBTRACTION gate; the LEDGER OPENED BEFORE the act; R-40 (content hash per run/artifact); S56 vintage pins; the forward-looking-criterion bar; the identity bar (arm-(e) live proof under the DEPLOYED role + bytes); **Andrew-direct 98869 answer 2's inflection ladder** (rectify existing FIRST / mint only if not / new buckets LAST / NEVER the root console -- rth-1); the **110-row disposition bounds** (per-row on its own evidence, NO age-close, print denominator + per-disposition counts -- rth-4); ⭐ **"REMOVING A BLOCKER IS NOT REALIZING AN OUTCOME"** -- no round-8 report claims FWD-5 REALIZED, and the CTO's standing read applies (*"has this EVER been graded" vs "does THIS round contain it"*).

### R8.4 Not decided here
Whether the inflection bucket CAN be rectified without the console (rth-1's read-only investigation determines it; the mint-principal and new-bucket branches are Andrew's/the CTO's, carried with evidence, never cut ad hoc); the submit controller's production shape (rth-2's judgment, Rule 24 record); which of the 110 rows dispose vs stay live (rth-4's per-row evidence).

### R8.5 Four-postulate record (Rule 24 over the round-8 cell set)
(i) MECE over the DECLARED domain = the round-7 carries {W3-S50 inflection, W1-S43 submit-wiring, status-word hygiene, the 110 stale rows} MINUS {FWD-5 realization (IRPT_FNTEND), the broader FWD-11 (Andrew), the DS producer re-key} -> the four cells remain, none uncovered. (ii) SAME GRAIN: each is one bounded remediation -- two served-path fixes, two records-hygiene sweeps. (iii) INTENT COHERENCE: one axis -- close what round 7 left open and make the records read true. (iv) STATE COHERENCE: a cell disposing rows or flipping status words does NOT move any FWD; rth-1/rth-2 ADVANCE FWD-2's serving half but do NOT alone realize it (containment already REALIZED round 6; FWD-5 untouched, its exercise is IRPT_FNTEND's).

### R8.6 MID-ROUND ADDITION (~14:5xZ 2026-09-21) -- on row W3-S52 (the render-host SESSION_ABSENT finding) and the CTO's ruling addendum 2 (@afc015b4b2, msg 99068)

`IB-rth-5` (WK~5): rth-2's build STOPPED honestly on a THIRD structural blocker beyond the two the CTO's original ruling (CTO_RULING_IRPT_BCKEND_W2-S62...) named -- the render host has no authenticated portal session, and `render_export.cjs` deliberately implements no login capability at all ("NO OTP BRANCH, NO SIGN-IN LOOP... never a credential prompt and never a retry"). The COO's own follow-on investigation (msg 99064) found: (1) the script launches a fresh, non-persistent browser context every run -- no session-reuse mechanism exists to exploit, not merely an unused one; (2) the portal's own auth is first-party with MFA, ruling out a trivial scripted login; (3) zero hits estate-wide for a reusable service-credential/session-minting pattern (the closest precedent, `IB-rte-2`'s bounded test principal, is API-level and does not transfer to a browser-session mechanism). CTO ruling addendum 2 (99068): CUT this as the successor cell, bounded to (a) persistent-context support in `render_export.cjs` (`launchPersistentContext`/`storageState`) and (b) SSM port-forward/session-capture tooling supporting a ONE-TIME operator-completed MFA login, refreshed on whatever cadence the session needs. **NOT authorized: a non-MFA service-account path** -- a standing portal security-posture decision, Andrew's to make on its own merits if ever pursued, never bundled into this cell. The actual MFA completion is a human act neither this cell nor its worker performs; the deliverable ends at tooling-ready + naming who must complete it (Andrew or a delegated operator holding valid portal creds), never at forcing a session through. Once a session exists (by the human step, outside this cell), rth-2's original bounded measurement re-runs unchanged and the sync-vs-async decision tree resolves on the real number -- this cell does not touch that tree. Chain E (independent of A-D, and of rth-1/rth-2 which continue on their own tracks): `rth-5` alone, no dependency. fanout 5 of 5 chains this round (A `rth-1`, B `rth-2`, C `rth-3` CLOSED, D `rth-4` CLOSED, E `rth-5`), cap 8. Grant: `infra/aws/ec2/investor-reporting-export/`, the SSM document/runbook home, this project's own deliverables/investigation faces -- no portal auth-system source (`portal/src/contexts/AuthContext*`, `portal/src/App.tsx` login route) is in grant; a change there is a STOP and a carry, not this cell's to make.

### R8.7 MID-ROUND ADDITION (~16:2xZ 2026-09-21) -- Andrew-direct @fb8c7a574c: create opal-data-inflectionwealth + opal-data-cottonwoodcapital

`IB-rth-6` (WK~6): Andrew-direct, VERBATIM: *"We need to keep moving so if there is no mechanism for us to
access these buckets, and our work is dependent on these buckets existing, then we need to create
opal-data-inflectionwealth and opal-data-cottonwoodcapital and take care to not create them with
restrictive bucket policies that land us in this situation."* Root cause, CTO-researched and COO-verified
this tick against the live registry: `infra/logic/registry/exemptions.json`'s `opal-data-inflection`/
`opal-data-cottonwood` rows already carry the fix that should have shipped originally -- three operator
identities (`Andrew_Berman`, `Andrew_Berman_Console`, `Opal_Terminal`, confirmed 3 of 3 each) exempt from
the per-firm Deny fence -- but `IB-rte-3`'s original apply shipped with an EMPTY exemption list, so the
fence denied every identity the estate holds, including the one that would need to sign and re-apply the
fix; the deploy ledger sentinel (`org/critical_paths/.open_deploys/irpt-bckend-ib-rte-3-lgic-firm-buckets.json`,
confirmed still present/open this tick) has sat RED since 2026-09-18 for exactly this reason. **The new
buckets exist to route around a lockout, not to repeat it: the exemption rows go in at the FIRST apply,
never as a later patch.**

**R8.7 CLOSED SUPERSEDED (~17:5xZ 2026-09-21, `2.0.0_SA_COO~B`, on `4.0.0_SA_CRO` msg 99124 @`a0097b1ef4`).**
`IB-rth-6`'s own conditional premise -- new buckets "if there is no mechanism for us to access these
buckets" -- was never met: Andrew personally recovered `opal-data-inflection`/`opal-data-cottonwood` at
the console (break-glass IAM roles `firmsep-inf-bucket-recovery-role`/`firmsep-cot-bucket-recovery-role`
matching the fence's own `role/*-inf-*`/`role/*-cot-*` admit-pattern; PUT the same TF-rendered policy this
cell's arm (d) would have produced, with the same 3-identity exemption; AFTER-read clean as
`user/Andrew_Berman` with no role, 2 of 2 buckets). `IB-rth-6` never reached arm (c); the worker's honest
STOP on the registry naming-law wall (row `IRPT_BCKEND-W6-S1`) is disarmed by citation, not overwritten
(row `IRPT_BCKEND-S115`). No new buckets, no naming exception, no registry edit. The cell text below is
kept verbatim as the historical record of what was staged; none of it executed. Remaining bucket-program
work -- deploy ledger legs L1/L3/L4 (a Terraform plan should now read 0 change on `aws_s3_bucket_policy.
lgic_firm`; the negative control), and the CRO's disclosed-but-unmeasured `fence_patterns()` hyphen gap
(row `IRPT_BCKEND-S116`) -- is picked up fresh, not as this cell's continuation: see R8.8, `IB-rth-7`.

Cell, exactly as Andrew's ruled fix specifies (his four points, restated as the cell's own arms) --
**STAGED ONLY, SUPERSEDED BEFORE EXECUTION, kept for record:**
(a) registry-addressed via `lib/opal_naming.py address()`, NEVER hand-typed (Rule 30) -- update the
`bucket` field on the `inflection`/`cottonwood` entries in `infra/logic/registry/scopes.json` to the new
long-form names (verified live this tick: `bucket_provisioned: true`, `bucket_managed_by:
s3-lgic-firm-buckets.tf` on both, matching the 49financial pattern `bucket = opal-data-<long>` in shape
though the new names are NOT `opal-data-<long>` -- they are Andrew's own two names, verified against
whatever the naming tool actually derives; a mismatch is a STOP, not a silent override), set
`bucket_provisioned: false` until built; do NOT rename the firms' `key`/`short`/`aliases` (referenced
estate-wide; Andrew asked for new buckets, not a firm rename). (b) copy the SAME three-identity exemption
rows from `exemptions.json`'s `opal-data-inflection`/`opal-data-cottonwood` entries into new
`opal-data-inflectionwealth`/`opal-data-cottonwoodcapital` rows -- load-bearing that these ship in the
FIRST apply. (c) mark the old buckets abandoned in `scopes.json` (NO delete -- confirmation-gated,
nothing asks for it), correct the stale "opal-data-inflection does not exist yet" alias note while in that
file. (d) standard mechanism: ledger entry opened before apply with its OPEN sentinel committed
immediately, `safe-apply.sh` only, both never-widen halves before the apply.

Chain F (independent of A/B/C/D/E -- different write surface, `infra/logic/registry/` + a new Terraform
apply on `s3-lgic-firm-buckets.tf`, no dependency on rth-1/rth-2's still-open work). fanout 6 of 6 chains
this round (A `rth-1` near-terminal, B `rth-2` parked on the human MFA step, C `rth-3` CLOSED, D `rth-4`
CLOSED, E `rth-5` CLOSED, F `rth-6`), cap 8. Andrew's own sequencing rec: ahead of anything else
non-blocking, since `IB-rtf-5`/`rtf-7` (and whatever else needs these buckets) are stalled on exactly
this. Grant: `infra/logic/registry/`, `infra/aws/terraform/**/s3-lgic-firm-buckets.tf` (or wherever that
root actually lives -- confirm, do not assume), `org/critical_paths/change_management/`,
`org/critical_paths/.open_deploys/`, this project's own task-order/investigation faces.

### R8.8 MID-ROUND ADDITION (~18:0xZ 2026-09-21) -- on `4.0.0_SA_CRO` msg 99124 (@a0097b1ef4) and `1.0.0_SA_CTO` msg 99128, superseding `IB-rth-6` (R8.7)

`IB-rth-7` (WK): the bucket LOCKOUT itself is now recovered (R8.7's closure note above) -- what remains is
RECONCILIATION, not creation. Three arms, all VERIFY-CLASS, no apply unless a plan shows drift: (a) a fresh
Terraform plan on the `shared-infra` root (the `s3-lgic-firm-buckets.tf` module) reads `0 to add / 0 to
change / 0 to destroy` on `aws_s3_bucket_policy.lgic_firm` for both `opal-data-inflection` and
`opal-data-cottonwood` -- the manually-applied policy (CRO's PUT) must match byte-for-byte what the
generator renders, since Terraform's own state never saw the apply; a NON-ZERO plan is a STOP (report the
diff, do not `apply` to force convergence without a fresh packet) -- this closes deploy ledger leg L3
(`org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md`).
(b) the negative control (leg L4): from host `i-02448edb624a7a7cf` if RUNNING, the host role's write to
`opal-data-inflection` and the 49f principal's read of `opal-data-cottonwood` both DENIED, 2 of 2 -- same
UNEXERCISED-not-FAIL vocabulary as `IB-rtf-5`'s `R62-AC3` if the host is STOPPED (this order does not start
it). (c) leg L1 (the original 10-resource activation) is a JUDGMENT call for the CVO, not self-graded by
the worker: does a clean L3 plan (0 change) mean L1 is satisfied BY CONVERGENCE even though no
`safe-apply.sh` ever ran against this state, or does L1 require an actual Terraform apply to bring the
state file itself current (`terraform import` / a no-op apply that only updates state) before it can close
-- state the tradeoff, do not rule it unilaterally. (d) IF (a) finds drift: STOP, file a row, do not
apply without a fresh never-widen packet -- the CRO's manual PUT was itself a never-widen act authorized
directly by Andrew ("go ahead you have egress as needed"), and a worker-initiated apply on TOP of it is a
NEW act needing its own halves. (e) SEPARATELY, carry row `IRPT_BCKEND-S116` (the `fence_patterns()`
hyphen-gap: `role/*-inf-*`/`role/*-cot-*` does not match this firm's own `inf-*`/`cot-*` pipeline role
names) -- MEASURE whether it is real (does any of this project's own served Lambda roles or a Terraform
`aws_iam_role` in this estate actually need to write to these two buckets, and does its role name in fact
fail the pattern -- printed, not assumed) and report to the COO; fixing `fence_patterns()` itself is
OUTSIDE this project's lane (a shared-infra module owned elsewhere) and is a carry, never a fix landed
here. Chain G (independent of A-F). fanout 1 of 1 this addition (rth-6 CLOSED SUPERSEDED, not counted).
Grant: `infra/aws/terraform/shared-infra/` (plan only; no apply unless (d) authorizes one under a fresh
packet), `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`, this project's own
task-order/investigation faces. NOT authorized: any change to `fence_patterns()` or any other firm's
bucket policy; starting the host; any IAM role/user creation (Andrew's own break-glass roles stay as they
are, deletable later once L3 reads clean, not this cell's to touch).

### R8.9 MID-ROUND ADDITION (~19:1xZ 2026-09-21) -- on row `IRPT_BCKEND-W7-S2` (`IB-rth-7`'s honest STOP: arm (a)'s fresh plan is NOT 0/0/0)

`IB-rth-8` (WK): `IB-rth-7`'s own worker measured real drift, exactly the contingency its order anticipated
in advance -- a fresh Terraform plan on the `shared-infra` root shows FOUR `lgic_firm` resources TAINTED
(`aws_s3_bucket_policy.lgic_firm["inflection"/"cottonwood"]`, `aws_s3_bucket_versioning.lgic_firm[same]`),
leftover from the original 2026-09-18 half-landed apply (row W3-S45), each forcing a REPLACE
(destroy-then-create). The live bucket policy is already correct (CRO's console PUT, msg 99124) and both
buckets remain empty (0 keys, re-confirmed multiple times) -- so a replace cycle carries no DATA exposure
risk, but a policy-resource destroy-then-create still opens a real WINDOW with no explicit Deny on the
bucket, and this project's own doctrine (`IB-rtf-5`'s own task order text) names exactly this ordering
hazard: *"a root delete-bucket-policy run AFTER the apply strips the new fence and no arm can prevent
it."* This is a never-widen act (CLAUDE.md NEVER-1) -- CTO+COO halves signed BEFORE any apply, same
discipline as `IB-rtf-5`. Three arms: (a) MEASURE the actual provider-level semantics of the replace for
BOTH resource types before writing the packet -- does `aws_s3_bucket_policy`'s destroy actually call
`DeleteBucketPolicy` (removing the fence) before the create's `PutBucketPolicy` restores it, and does
`aws_s3_bucket_versioning`'s destroy call anything at all against a live bucket (AWS has no "delete
versioning" API -- versioning is only Enabled/Suspended, so the provider's destroy behavior needs reading,
not assuming) -- `terraform plan -json` inspected for the exact per-resource action sequence, printed; (b)
THE PACKET naming the measured window precisely (both halves sign at HEAD against this packet's blob, per
NEVER-1's writer-census discipline), rollback (buckets are empty -- if anything looks wrong post-replace,
re-apply the fence policy immediately, no data can have been lost); this cell STOPS here if both halves
are not obtained same-pass -- commit the packet, leave the order open, report what's owed, exactly as
`IB-rtf-5`'s own precedent; (c) ONLY once both halves are signed at HEAD: `.tools/safe-apply.sh` on
EXACTLY the four tainted resources (a plan naming any other resource, or `demo`/`49financial`, is a STOP),
immediate post-apply verification (get-bucket-policy both buckets, matching the CRO's already-live policy,
0 keys re-confirmed, re-plan `0/0/0`), close ledger legs L1 and L3 with the apply output + resource list +
plan output as proof, disarm row `IRPT_BCKEND-W7-S2` by citation. Leg L4 (the negative control) stays
whatever `IB-rth-7` left it -- UNEXERCISED, host stopped, not this cell's to force. Chain H (independent,
following `IB-rth-7`'s drain). fanout 1 of 1 this addition. Grant: `infra/aws/terraform/shared-infra/`,
`org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`, this project's own
task-order/investigation/deliverables faces. NOT authorized: touching any resource outside the four named;
starting the host; any change to `fence_patterns()`, exemptions.json, or scopes.json.

### R8.10 ERRATA (round 9, issuer `2.0.0_SA_COO~B`, on CVO~B's L9 and the CTO's round-8 analysis) -- the rows above are RETAINED under R-43, not rewritten

- **`IB-rth-1`'s row (R8.1) and its face name `opal-data-inflection` as the bucket the serving route was blocked
  on (C-S135 / W1-S46).** That conflated two buckets. `data/firm_registry.json` firms[inflection].bucket =
  `opal-data-inf` (the LEGACY bucket -- re-read by the issuer 2026-09-21; cottonwood = `opal-data-cot`,
  49financial = `opal-data-bd`). `opal-data-inflection` is the LGIC full-name bucket, FWD-11's SEPARATE program.
  The serving fix (`_authz/loaders.py`: S3 AccessDenied treated as absent) reached inflection HTTP 200 at
  15:43:53Z, before that bucket was recovered (17:35:59Z, CRO msg 99124), so it does not depend on it.
- **`IB-rth-3`'s row (R8.1) and its face say `superseded` is "true for some of the seven, false for others"
  (C-S134 / W3-S51).** It is false for all seven: no later cell names any of them in a `supersedes` column
  (rounds 6-8 read). The seven stay terminal-by-proof with honestly non-terminal words.
- **`IB-rth-2`'s judgment `R77-AC2` was issued with an id and the word "judgment" but no bar (C-S144)** -- ungradeable
  by construction. It stays NOT_EVALUATED; no retroactive PASS. The successor bar is issued in round 9 (R9.4).

## R7. ROUND 7 -- THE RECUT ON THE ROUND-6 ANALYSIS (@fa2ff4f0dd, msg 98554; v0.7, 2026-09-20, `2.0.0_SA_COO~B`)

**Input:** round 6 CLOSED at L10 (0 open of 75; 47/47 AC2 PASS; 52 rows disposed, 40 graduated incl. S110). This recut's whole subject is the round's headline: THE SCOPE PLANE AND THE DATA PLANE HAVE DIVERGED -- the advisor is identified, firm-bound, scope-resolved and told exactly how much of the book is withheld (the refusal vocabulary WORKS), then served NO DATA on any tab (the data paths do NOT). No PRD addendum -- round 7 re-attempts FWD-2 (the serving/data half) and FWD-5, both existing. Scope determined by investigation a7edd66ed0: FOUR of the five residual data-plane defects are IRPT_BCKEND BACKEND handler cells; the fifth (the ownership-map count) is DS. The four carries stand (S110's vacuous negative control taints the REFUSAL side of rtf-10/rtf-12 arm-(f), served-path grants unaffected; the grant moved to 44/19; the ledger-retroactive EXPOSURE; the headline).

### R7.1 The rectangle (4 cells, id shape `IB-rtg-<n>`)

| cell | owes | assignee | serves | supersedes |
|---|---|---|---|---|
| IB-rtg-1 | EXPORT S105+S106 (ONE cell, CTO ruling @0110b9de01): align `export/entry.py:63-64,100` `RECEIPT_KEY_TEMPLATE` to the writer's `firms/{firm}/generations/.../exports/{rev}/` family AND write the receipt beside the bundle in `export/handler.py:126-130`, AND rewrite `export/entry.py:104-105`'s `except` to decide refusal off `exc.response['Error']['Code']` + HTTP status not the class name. S106 FIRST-OR-WITH S105, never after; `IRPT_EXPORT_RECEIPT_KEY` Terraform override REFUSED. Packet + halves BEFORE the deploy; acceptance on a REAL wire error (403/AccessDenied -> policy code; 404/NoSuchKey -> NOT_FOUND), never a constructed stub | WK | FWD-2 | -- |
| IB-rtg-2 | STATUS: write the real `status_loader` in `ops/` (reads TenantLease/checkpoint + `ops/manifests.py` against the backend's OWN `irpt-jobs` store) and wire it into `ops/entry.py` in place of `ops/status.py:338`'s always-raising `_default_status_loader`. Packet + halves; acceptance: an exercised status-summary for a real job returns a validated StatusEnvelope, not UNSUPPORTED_OPERATION | WK | FWD-2 | -- |
| IB-rtg-3 | PERFORMANCE (W2-S27): reconcile `performance/tenants.py:81-101` `route_for` to the id space the boundary binds on via the ESTATE'S EXISTING `_ids` normalizer -- NEVER a fourth firm-token mapping. BOUND: if the fix cannot be done without minting a new lookup, it is FirmBinding's axis (W2-S9) and is ROUTED to the CTO, not cut ad hoc. Packet + halves; acceptance: an authorized, scope-resolved performance request for each of the 3 registry firms resolves a TenantRoute, 0 fourth-id-space literals | WK | FWD-2 | -- |
| IB-rtg-4 | HOLDINGS S100 (this seat's own row): make `holdings/entry.py:88` `_load_directory` FOLLOW the `latest.json` pointer the way `_authz/loaders.py:71-78` does (holdings reads the pointer doc as the artifact). Packet + halves; acceptance: an exercised holdings request for an account the principal's own resolve granted reads a scope-resolved answer, never FIRM_BINDING with firm_id absent | WK | FWD-5 | -- |

**Not cells of this project:** the OWNERSHIP-MAP COUNT (44/19 live vs 33/18) -- DS gold, `data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py`; backend only READS it (object-scoped GetObject) and round 7's cells RE-DERIVE the count at build/measure time, NEVER inherit 33/18. FWD-11 / rtf-5 -- PARKED on Andrew's security re-scope (un-park condition + owner on the order @919a261242, not re-opened here). The S100/S110 control-repair EVIDENCE (not a cell) un-taints when IB-rtg-4 moves S100.

### R7.2 Edges and fanout
Four INDEPENDENT chains (four different handlers, disjoint write surfaces): A `rtg-1`; B `rtg-2`; C `rtg-3`; D `rtg-4`. **fanout: 4 of 4 chains, cap 8.** No cross-cell dependency (the S106-first-or-with-S105 ordering is INTERNAL to rtg-1). Each is a served-path handler deploy and STOPs at its never-widen halves on the first pass (the rtf-13 shape).

### R7.3 Bounds carried
NEVER-1 (packet + CTO+COO halves at HEAD BEFORE every deploy -- all four change served behaviour); the arm-(d) SUBTRACTION gate (the W1-S37 lesson: compare `resource_changes` per root minus a CLOSED PRINTED volatile set, never a whole-planfile digest); THE 44/19 RE-DERIVE CONSTRAINT (read the ownership map live and print the count, never inherit 33/18); R-40 (content hash per run/artifact); S56 vintage pins; the forward-looking-criterion bar; the reader-census bar; the LEDGER OPENED BEFORE the act (the W1-S41 / rtf-3 exposure -- no principal/apply cycle without a pre-opened change-management ledger); no served bytes committed as source; the identity bar (arm (e) runs the DEPLOYED role + bytes).

### R7.4 Not decided here
Whether IB-rtg-3's reconciliation needs a new firm-token mapping (if so -> the CTO, W2-S9 axis, not cut here); the status_loader's manifest shape (rtg-2's judgment, Rule 24 record); the ownership-map producer's re-key (DS, d08's owner); anything about FWD-11 (Andrew).

### R7.5 Four-postulate record (Rule 24 over the round-7 cell set)
(i) MECE over the DECLARED domain = round-6 residue section 5 MINUS {parked, DS, evidence-not-cells}: the owed set is {export S105/S106, status, performance, holdings S100, ownership-map count}; SUBTRACT the ownership-map count (DS) and FWD-11 (Andrew, parked) and the S110 evidence (un-taints via holdings) -> the four backend cells remain, none uncovered. (ii) SAME GRAIN: each cell is one handler's served-behaviour fix. (iii) INTENT COHERENCE: one axis -- make the DATA paths serve. (iv) STATE COHERENCE: a cell realizing its serving does NOT move FWD-11 (parked) or the DS count (re-derived, not fixed here).

## R6. ROUND 6 -- THE RECUT ON THE ROUND-5 ANALYSIS (@81472c3a47, msg 98115; v0.6, 2026-09-19 ~03:4xZ, `2.0.0_SA_COO~B`)

**Input:** six judgment PASS, 17 rows disposed (16 graduated with carriers, 3 dismissed), NO PRD addendum -- round 6 is a recut. Four round-5 orders closed on truthful FAILs and each FAIL is a cell here; S77 (the CVO) is the finding of the round: the cross-firm fence is stale while its stated cause is false, because the generator was never re-run after the flip -- the reader-census bar (the mirror of the writer census) is adopted on every face. The L4 rulings carried: @457cf494c6 (no-source members: measure, then branch), @61627f39f9 (partial projection: admit and disclose, three conditions). Corrections adopted: registry rows are the CRO's lane (`PLATFORM_LOGIC_DOCS`), landed @845343f925; a blob pin is written `blob <hash>`; no `memory/` path is cited on a face (S78).

### R6.1 The rectangle (5 cells, id shape `IB-rtf-<n>`)

| cell | owes | assignee | serves | supersedes |
|---|---|---|---|---|
| IB-rtf-1 | round-5 analysis s.5 item 1: the no-source members MEASURED then BRANCHED (W4-S34/S35 + W1-S26's six members + the 3 UNRESOLVED); DELTA=0 declares, DELTA!=0 packets and stops | WK~4 | provenance of every served function | IB-rte-4 |
| IB-rtf-2 | s.5 item 2 / W1-S27: the ordering inversion in `enforce.py` with the disclosure field NON-OPTIONAL, the IRPT_FNTEND consumer-obligation row, the empty branch refusing; packet + halves BEFORE the deploy (a STOP at (d) is the expected first pass) | WK~1 | FWD-1, 2, 5 | IB-rte-6 |
| IB-rtf-3 | IB-rte-2's re-cut: the principal created, the four outcomes exercised on the DISCLOSED-PARTIAL path, deleted | AE `~N` (staged, behind rtf-2) | FWD-1, 2, 5, 11 | IB-rte-2 |
| IB-rtf-4 | s.5 item 3 / S77: every generated block re-derived from the registry at HEAD, the fence proven both signs, the flag's readers censused | WK~3 | FWD-1, 7, 10 | -- |
| IB-rtf-5 | s.5 items 4-5: IB-rte-3's re-hand -- the re-apply after Andrew's step 4 under both halves naming the 4 tainted resources + the last 2 of 10 + the regenerated fence; the host control EXERCISED or UNEXERCISED, never simulated | WK~3 (staged, behind step 4 + rtf-4 + halves) | FWD-1, 7, 10 | IB-rte-3, IB-rte-7 |

**Not cells of this project:** (b) of the partial-projection ruling (the ownership-map producer re-keyed to the Schwab spine) -- DS-owned, carried to `d08_firm_ownership_map.py`'s owner; the IRPT_FNTEND rendering obligation -- the CTO's L4 carrier in FNTEND's PRD (rtf-2 files the row); FWD-11's SSM roster parameter -- a separate act with its own sign-off; IB-rtd-7's port -- still superseded behind rtf-5, both halves and the FNTEND reader cell; starting host `i-02448edb624a7a7cf` -- operational, outside every cell (a REC to the CTO: it is the only closer of W3-S44).

### R6.2 Edges and fanout

Chains: A `rtf-1`; B `rtf-2 -> rtf-3`; C `rtf-4 -> rtf-5` (rtf-5 also behind Andrew's step 4 and both halves). **fanout: 3 of 3 chains, cap 8.** Handed now: rtf-1, rtf-2, rtf-4. rtf-3 on rtf-2's drain with arm (e) passing; rtf-5 on step 4 (the issuer measures `get-bucket-policy` at the hand-off), rtf-4's drain, and both halves. The DS lane holds no round-6 order.

### R6.3 Bounds carried

R-40, R-42, R-44, R-45; the forward-looking-criterion bar; S56's vintage pins; Rule 30; NEVER-1 on every served-behaviour change (rtf-2's deploy, rtf-5's apply: both halves at HEAD BEFORE the act); the reader-census bar; `blob <hash>` notation; no `memory/` citation on a face; no served bytes committed as source on any branch (rtf-1); the empty-set branch refuses on every path (rtf-2); nothing written to either bucket (rtf-5); no host start by any cell.

### R6.5 MID-ROUND ADDITIONS (~06:4xZ 2026-09-19) -- on rows W4-S41 / W1-S29 and the Andrew-direct ~06:3xZ

`IB-rtf-6` (WK~4, `wk-irpt-6-4b`): the manifest re-pinned after the shared-surface drains. rtf-1 pinned the shared `_authz/` files to `c28c728a30`'s blobs; rtf-2 changed `enforce.py`/`served.py` and deployed through `rte6_package_deploy.py`, which bypasses the pins -- the declared source and the served bytes disagree, and a `build-and-upload.sh` from HEAD would stage the PRE-inversion bytes (a regression of @61627f39f9 by build). Re-pin to the served-matching HEAD blobs, prove the regression on the mutant, deploy nothing; the diverged `holdings/enforce.py` (W1-S29) is rowed, never pinned. Grant: `infra/aws/lambda/ci/` + the channel. The two-packager class is R63-AC2's for L4.
`IB-rtf-7` (AE `~V`, first on that seat): Andrew-direct ~06:3xZ (record `ANDREW_DIRECT_20260919_063xZ_STEP4_BUCKET_POLICY_AE_ATTEMPT_THEN_PROCEED.md`, verbatim *"have an AE deal with it. if they cant for whateve rreason, proceed and note it for later"*): step 4 -- the bucket ACCESS POLICY removed, never the bucket -- attempted with every identity the seat holds, each response verbatim under a ledger entry; success unblocks rtf-5 that tick; AccessDenied everywhere is the truthful result (only root escapes a `Principal: *` Deny), the round proceeds, and "step 4 -- Andrew at the console when next present" is carried on the drain-end packet and the slug as a PARKED item with owner and un-park condition.
`IB-rtf-3` RE-ADDRESSED `~N` -> `~V`: the /mstr-spawn 1d census found `~N` encumbered by `ETFS_POSITIONING.TO-14-AE` (site Z, 2026-08-29, ACTIVE) -- the Tier-2 one-project rule; `~V` reads 0 orders / 0 processes / 0 markers / 0 armed disarm rows / no inbox. Chains now: A `rtf-1 -> rtf-6`; B `rtf-2 -> rtf-7 -> rtf-3` (one AE seat, rtf-7 first); C `rtf-4 -> rtf-5` (rtf-5 behind step 4, whichever hand performs it). fanout 3 of 3 chains, cap 8.

### R6.6 MID-ROUND ADDITION (~08:1xZ 2026-09-19) -- on the CTO's ruling S82 (@b37fdfd5cd, msg 98178)

`IB-rtf-8` (WK~1, `wk-irpt-6-1c`): holdings' forked enforcer folded onto the shared module. The per-route census (7 `entry.py`, `os.walk`) found EXACTLY ONE local `enforce.py` -- `holdings/` -- bound by `holdings/snapshot.py:44` (`blob 8f849457be`, 635 lines, the pre-ruling refusal order, `unprojected_grant` never populated) while the shared `served.py` supplies the field present at zero: on that route a real gap renders as NO gap and no absence guard can see it -- Rule 22's shared-dependency blindness INVERTED (seven routes share `served.py`; one does not share `enforce.py`). The CTO's ruling: FOLD, never patch the fork; the fold also closes W1-S27's residual on the same route (S81: disarmed on the shared path, live on holdings). Shape: diff the fork before deleting it (a load-bearing fork-only behaviour is a STOP, never a silent drop), re-bind, re-declare the manifest member, the census as the acceptance instrument, packet + halves BEFORE the deploy (the rtf-2 shape), then the live holdings request reading `count > 0` where the fork read zero. Chains: B `rtf-2 -> rtf-8` beside `rtf-7 -> rtf-3`; fanout 3 of 3 chains, cap 8. The Surprises clause on this face names the channel's PREVAILING EOL (CRLF, measured at HEAD every line; W4-S44) rather than round 1's "LF".

### R6.7 MID-ROUND ADDITION (~08:5xZ 2026-09-19) -- on row S86 (IB-rtf-3's STOP @f60b3f0942)

`IB-rtf-9` (AE `~V`, declare-only): the two-key test-principal packet on the REAL mint path. IB-rtf-3 stopped before any write: the deployed auth-handler mints the token's advisor claim ONLY from `opal-partner-<firm>` keyed by e-mail; the first packet's K1 field (`advisorKey` on the user row) is never read, so K1 + K2 would mint a 49financial session with NO advisor claim -- UNKNOWN on the scoped routes. The CTO half's own rule (s.1 @482b2c627e): a discovered key is a STOP and a NEW packet. rtf-9 re-declares three keys (K1 the user item as the reader reads it, K1b the partner-table binding with its OWN writer/reader census and `DeleteItem` rollback, K2 the ephemeral session), both branches per key, the exercise plan restated on the two keys, `0` writes measured; both halves re-sign against its blob; IB-rtf-3 is then re-handed against that packet. Andrew's 17:3xZ approval covers the bounded principal under both halves; the partner binding is the part the first packet mis-located, not a new act. The exposure rtf-3 named (a firm login with no book admitted by firmId on the older portal routes) is the CTO's. Chain B: `rtf-2 -> rtf-7 -> rtf-9 -> rtf-3`. fanout 3 of 3 chains, cap 8.

### R6.8 MID-ROUND ADDITION (~11:2xZ 2026-09-19) -- on rows S90 (BLOCKING) and S92 (IB-rtf-3's re-hand @dddf5ef318)

The first authenticated requests ever sent through the REAL path (the bounded principal minted by the real login, rtf-3 re-hand) were refused UNEXPECTED before the scope resolved, 12 of 12 -- an OUTAGE, not a policy refusal. Two causes: the directory role bans `platinum/` by design (IB-s-1) while the `_authz` loader reads the ownership map from there; `irpt-status`/`irpt-holdings` carry no `IRPT_DIRECTORY_BUCKET_MAP`. Every earlier "SERVED" proof ran in-process under operator credentials (rtf-2 (e), rtf-8 (e) `declared_exclusions`) -- the deployed roles were never exercised. Two cells, NOT paired (infra vs code; they share nothing but the route): `IB-rtf-10` (AE `~V`): the census of the 7 serving functions' grants/environments, the PACKET (object-scoped GetObject on each client firm's `ownership_map.json`, derived from the registry; the bucket map on every serving function), plan with `0 to destroy`, STOP at the halves on the first pass, then apply under ledger and PROVE the path under the deployed roles with the bounded principal (rtf-9 blob, new epoch). The design question (the deliberate `platinum/` ban vs the map's home) is pitched to the CTO with the issuer's recommendation; the CTO half on the packet is the ruling. `IB-rtf-11` (WK~1): `directory/entry.py` reads `q`/`limit`/`selection` from the payload-2.0 shape the integration sends, proven on a real fixture with the pre-fix entry as the mutant; no deploy (rides rtf-10's second pass). Chain D: `rtf-3 (FAIL S90) -> rtf-11 -> rtf-10 -> rtf-3 (third hand, same packet, new epoch)`. fanout 4 of 4 chains, cap 8. S91 (the None error sink) is the CTO's. Also carried, not cut: `holdings/entry.py`'s `_no_grant` wiring (IB-rt-7's decision) means the deployed holdings route serves nothing even after S90 -- rtf-8's live proof was in-process for that reason (declared exclusion); the CTO's round-6 analysis reads rt-7.

### R6.9 MID-ROUND ADDITION (~15:1xZ 2026-09-19) -- on row S98 (IB-rtf-10's fourth pass @4ce6319d03)

rtf-10's grants APPLIED exactly as signed (7 of 7 roots, 0-diff after; map allowed 18 of 21, directory 21 of 21, bucket map 7 of 7, negatives denied 27 of 27, `CodeSha256` 7 of 7) and the live proof under the deployed roles STILL read UNEXPECTED 9 of 10: S90's THIRD cause -- `_ids/ids.py` opens `raw_keys.json` beside itself at runtime and that file is in 0 of 7 deployed zips and 0 of 7 manifest entries (every zip flattens `ids.py` without it; every in-process proof passed because the repo has the file beside the module). `IB-rtf-12` (AE `~V`, the S96 shape): the premise re-measured incl. a census of every `__file__`-relative open under `_ids/`; the file DESCRIBED for the halves (shape, firm-attributability, credential NONE, writers); ONE sibling-identical `staged_from` object per function (7); the seven rebuilt under a build ledger with the per-function served delta verified as EXACTLY the added member; a NEW never-widen packet (K-CODE x 7, rollback = the prior live `CodeSha256` per function); STOP at the halves; on the re-hand apply + rtf-10's arm (f) unchanged. rtf-10's apply stands. Chain D becomes `rtf-3 -> rtf-11 -> rtf-10 -> rtf-12 -> rtf-3 (third hand)`. fanout 4 of 4 chains, cap 8. Carried for the analysis: a build-time check that a `__file__`-relative open is a staging member by construction (the binding-check class @3580608505, a third population row); the identity bar's "deployed BYTES" clause.

### R6.10 MID-ROUND ADDITION (~18:1xZ 2026-09-19) -- on rows S103/S104 (IB-rtf-12's third pass @7db8f2c67b)

rtf-12 applied the six as signed and the scope now RESOLVES on 8 of 8 counted requests (S90's three causes closed on the deployed path); two defects that lived in the prior live bytes became reachable: S103 -- directory search reads `DirectoryEntry.schema.json` from the checkout path or `IRPT_CONTRACTS_DIR`, and `irpt-directory-search` has neither (the S98/S96 class a third time, outside rtf-12's `_ids/` census); S104 -- the export receipt route's evidence-bucket read fails under `irpt-export-render-role` only (an IAM/key-prefix question; under operator credentials the read is NOT_FOUND). The rollback on rtf-12 was ruled NOT executed: the apply did what the halves signed and rolling back regresses resolve; a defect made reachable is an exposure the act uncovered. Two cells, disjoint surfaces, in parallel: `IB-rtf-13` (WK~1, the manifest + the directory root): a census of EVERY runtime file open across the seven functions against their staged members (the class-ending arm), the contract staged as a member with `IRPT_CONTRACTS_DIR` set the way holdings does, ONE rebuild under a packet (K-CODE + K-ENV), STOP at the halves, apply + prove search/resolve under the deployed role and bytes. `IB-rtf-14` (AE `~V`, the export root): the cause MEASURED (the concrete receipt key vs the policy's ARNs; the swallowed denial printed as the role; the receipt's existence), the narrowest grant as a packet (or the no-grant case rowed for the CTO), STOP at the halves, apply + prove the receipt route as the role. Chain D: `... -> rtf-12 -> rtf-13 -> rtf-3 (third hand)`; chain E: `rtf-12 -> rtf-14`. fanout 5 of 5 chains, cap 8.

### R6.4 Not decided here

Whether `firm_registry.json` becomes a builder output (rtf-1's judgment); the disclosure field's `kinds` taxonomy (rtf-2's judgment, Rule 24 record); whether `bucket_managed_by` becomes a closed enum and whether generators re-run at commit time (rtf-4's judgment -- proposals for the CTO, never gates built here); what rtd-7's port lacks after rtf-5 (rtf-5's judgment).

## R5. ROUND 5 -- THE RECUT ON THE ROUND-4 ANALYSIS (@561d6e1cc9, msg 98036) AND ANDREW'S 17:3xZ APPROVAL (@af794c77e3)

**Input:** seven judgment PASS, zero of ten FWDs REALIZED (all ten advisor-facing; the structural blocker is that no principal has ever existed to exercise them), S56 and S68 CLOSED, no PRD amendment; s.8 names six owed items; Andrew's verbatim *"Approved"* adopts the two `/open-calls` RECs (the two LGIC firm buckets NOW, creation only; a bounded test principal under both halves). The CTO's correction on W1-S20/W2-S59 changes the remedy: declare the true source in `files[]` / stage from a pinned blob, never a third copy.

### R5.1 The rectangle (5 cells, id shape `IB-rte-<n>`)

| cell | owes | assignee | serves |
|---|---|---|---|
| IB-rte-1 | s.8 item 1 / Andrew call 2: the bounded test principal DECLARED -- identity plane measured, keys, exercise plan, never-widen packet; creates nothing | WK~1 | FWD-1, 2, 5, 11 |
| IB-rte-2 | the principal CREATED under both halves, the four outcomes EXERCISED at a live session by artifact hash, DELETED as the cell's last arm | WK~1 (after rte-1 + halves) | FWD-1, 2, 5, 11 |
| IB-rte-3 | s.8 item 2 / Andrew call 1: `opal-data-inflection` + `opal-data-cottonwood` CREATED EMPTY via `name()`, in the 49 Financial bucket's shape, gate enumerations regenerated, fence proven; no objects, no cut-over | WK~3 | FWD-1, 7, 10 |
| IB-rte-4 | s.8 item 4 / W1-S20, W2-S59: the served members declared from their TRUE sources (no third copy), served zips verified member-for-member, clean-checkout builds with 0 manual steps | WK~4 | provenance of every served function |
| IB-rte-5 | s.8 item 6 / W2-S57 residual: the manifest-history census (rtd-2's Q2), FWD-7's FIVE arms on the controlled clock against the deployed code, the fresh-dispatch case named or driven | WK~2 | FWD-7 |

**Not cells of this project:** s.8 item 3 (S68's cause, the `.gitattributes eol=lf` act) is MDPF's owner's -- the CTO's own, by its word. s.8 item 5 (IRPT_FNTEND's per-firm as-of consequence) is a CARRY: sent to `2.0.0_SA_COO~F` 11:55Z (QUEUED, no live session) and now escalated to `1.0.0_SA_CTO` to land in FNTEND's PRD at L4, which is the only carrier that does not decay. IB-rtd-7 (the port) stays SUPERSEDED until rte-3's buckets, both halves and the FNTEND reader cell exist -- re-cut then, not now.

### R5.2 Edges and fanout

Chains: A `rte-1 -> rte-2`; B `rte-3`; C `rte-4`; D `rte-5`. **fanout: 4 of 4 chains, cap 8.** Handed now: rte-1, rte-3, rte-4, rte-5. rte-2 on rte-1's merge + both halves at HEAD (the COO half is this seat's on the packet; the CTO half is asked the same tick the packet drains). The DS lane holds no round-5 order (nothing Rule-13-shaped is cut); it stays seated for the port's bundle work.

### R5.3 Bounds carried

R-40, R-42, R-44, R-45; the forward-looking-criterion bar and S56's vintage pins on every face; Rule 30 on every name (builder output or a drafted registry row); NEVER-1 on the principal (both halves before creation; deletion inside the same order); creation-only on the buckets (no object, no cut-over, no legacy retirement -- Andrew's prior word stands); no third copy of a served member; read-only on every served bucket in rte-5 (a reconciliation is declared, never performed).

### R5.5 MID-ROUND ADDITION on row W1-S22 (IB-rte-1 @01ba67fe65) -- the issuer's ruling, ~22:0xZ

`IB-rte-6` -- the served path admits a projected advisor grant. Today EVERY live FIRM_ADVISOR request is refused `UNPROJECTED_GRANT`: 0 of 13 entry points pass `id_projection`, and 0 of 22,646 ownership grants join the directory even with the projection applied (custodian keys vs the crosswalk id the directory mints from). RULED: the wiring half ADJUDICABLE (L5/L6) and cut; the id-space half PITCHED to `1.0.0_SA_CTO` with REC (a) -- resolve custodian keys through `dim_identity_crosswalk` (already readable under K2) -- carried on the face as arm (b), a MEASUREMENT the ruling confirms or re-cuts. Seat WK~1 (`wk-irpt-5-1b`). Edge: `rte-6 -> rte-2` (the exercise cannot pass on a path that refuses every advisor). fanout stays 4 of 4 chains, cap 8 (rte-6 is chain A's new middle). Carried INERT: W1-S21 (advisor ids are raw ownership-map keys, never opaque-minted -- my face assumed otherwise), W1-S24 (cottonwood's termination field unpopulated). The live incident on IB-rte-3 (W3-S42/S43/S44: the new buckets' Deny fence locked out the applying identity; ledger OPEN RED) is ESCALATED `[STUCK]` to the CTO + MSTR (98062/98063) -- root `delete-bucket-policy` + two registry edits outside any worker's grant; rte-3 stays open and is re-handed after.

### R5.6 MID-ROUND ADDITION on the CTO's registry-deadlock record (@9eeb9a70a8, msg 98087) -- the issuer's ruling, ~00:1xZ 2026-09-19

`IB-rte-7` -- the LGIC firm buckets survive the registry flip. The CTO answered the rte-3 incident's registry half by RUNNING the gate: the two registry edits are mutually blocking -- `s3-lgic-firm-buckets.tf:70-73` selects on `bucket_provisioned == false` (flipping it stages a DESTROY of the 8 landed resources), and the naming gate refuses an exemption row for a bucket whose flag is false. Its remedy is five steps and step 1 is a Terraform change: a cell, RULED adjudicable at L5/L6 and cut. The issuer's measurement that re-shapes step 1: `scopes.json` @ea5edd1fe4 carries FOUR FIRM rows and two of them (`49financial`, `demo`) are `bucket_provisioned: true` with their buckets declared elsewhere IN THE SAME ROOT (`s3-49financial.tf`, `s3.tf`), so the CTO's "block keyed on PROVISIONED FIRM rows, with `moved` blocks" would plan `2 to add` -- the membership is re-keyed on a DRAFTED registry field (read with `lookup`, absent-safe) OR the unflipped flag, instance keys unchanged, no `moved` block, no state verb; proven by three plans (HEAD-identical; the flip applied locally reading `0 add / 0 destroy / <=2 policy changes`; the mutant on HEAD's Terraform reading the destroy) and never applied. Seat WK~3 (`wk-irpt-5-3b`, cold start). Grant: the one Terraform file + the channel; the registry is deliberately NOT granted (Rule 30, the CTO's, and its stated intent at 98087 -- it lands steps 2-3 on rte-7's drafted delta). Chain B becomes `rte-7 -> [CTO registry] -> [Andrew step 4, delete-bucket-policy] -> rte-3 re-hand (step 5)`; fanout stays 4 of 4 chains, cap 8. rte-3 stays open by its own FAIL; its ledger entry and sentinel stay OPEN RED. Carried to the CTO the same tick: the `demo`/`49financial` measurement, so its step-1 shape is re-cut on the fact and not on the record.

### R5.4 Not decided here

Whether one bounded identity serves FWD-11 or a second is needed (rte-1's judgment); whether `_authz/` becomes a shared package (rte-4's judgment, L4's); whether the D14 register already names the two buckets (rte-3's judgment); the fresh-dispatch design (rte-5's judgment).

## R4. ROUND 4 -- THE RECUT ON THE ROUND-3 ANALYSIS (@5c59f68d70, msg 97944)

**Input:** the CTO's round-3 analysis: nine judgment PASS, zero of ten FWDs REALIZED, no PRD amendment, round 4 unblocked; s.9 names six owed items and s.4 ADOPTS the forward-looking-criterion bar. The issuer adds ONE carried row (W1-S16, the first round-4 cut per S57) and excludes S73 (an estate-instrument defect, routed elsewhere by the CTO).

### R4.1 The rectangle (8 cells, id shape `IB-rtd-<n>`)

| cell | owes | assignee | serves |
|---|---|---|---|
| IB-rtd-1 | s.9 item 1: the 13:00Z organic fire graded on what it ACTUALLY loaded (bundle VersionId + CodeSha256 at invocation; artifacts by hash; the scheduler as invoker) | WK~2 | FWD-7 organic arm |
| IB-rtd-2 | s.9 item 4 / W2-S57: `last_manifest()` finds the COMPLETED manifest at the runner's date; the no-op branch fires on its positive case; deployed; driven after the organic fire | WK~2 (after rtd-1) | FWD-7 |
| IB-rtd-3 | s.7 / s.9 item 5 (S71): the holdings contract aboard the bundle; the two-schema diff recorded; the re-arm trigger guarded by a test | DS~X | FWD-5, FWD-7 |
| IB-rtd-4 | s.6 / s.9 item 5 (S68): the route-bindings drift measured by content, consumers + writers censused, the never-widen packet written -- declares only | WK~3 | deploy discipline |
| IB-rtd-5 | S68 resolved under both halves (CTO = MDPF's owner + COO), root converged | WK~3 (after rtd-4 + halves) | deploy discipline |
| IB-rtd-6 | s.9 item 2: the LGIC address built (`address()`, refusals -> drafted registry rows), readers/writers censused across both projects, the port planned, the write-grant packet written -- declares only | WK~4 | FWD-1, FWD-7, FWD-10 |
| IB-rtd-7 | the port under both halves + the CTO's registry rows + FNTEND's reader cell, one window, legacy retired | WK~4 (after rtd-6 + 3 gates) | FWD-1, FWD-7, FWD-10 |
| IB-rtd-8 | W1-S16: `Enforcer.covers()` firm check restored on BOTH enforcer copies (`_authz/enforce.py:351`, `holdings/enforce.py:319` @5c59f68d70), six-swap tests, deployed, proven on live routes | WK~1 | FWD-2, FWD-11 |

**Not a cell:** s.9 item 3 (the per-firm as-of consequence for IRPT_FNTEND) is a COO carrier -- a message to `2.0.0_SA_COO~F` with the fact and its consequence for the API/as-of display, sent with this issuance. S56's vintage pins and the forward-looking bar are BOUNDS on every face, graded at the drain (bare `:NNN` citations `0 of N`).

### R4.2 Edges and fanout

Chains: A `rtd-1 -> rtd-2`; B `rtd-3`; C `rtd-4 -> rtd-5`; D `rtd-6 -> rtd-7`; E `rtd-8`. **fanout: 5 of 5 chains, cap 8.** Handed now: rtd-3, rtd-4, rtd-6, rtd-8. rtd-1 is handed ~12:5xZ so the worker reads the 13:00Z fire rather than predicts it (the hand-off timing is the issuer's; the cell has no calendar wait beyond the event it grades -- the CTO ruled the organic arm correctly shaped, s.4). rtd-2 after rtd-1 merges (a deploy must not change what the organic fire loads). rtd-5 after rtd-4 + both halves (or SUPERSEDED if the packet recommends no apply). rtd-7 after rtd-6 + the CTO's registry rows + both halves + FNTEND's reader cell.

### R4.3 Bounds carried

R-40, R-42, R-44, R-45 on every face; the forward-looking-criterion bar (s.4); S56's vintage-pin bar on every judgment record; S73 excluded by name; Rule 30 on every address (builder output or a drafted registry row, never a typed path); NEVER-1 sign-off on every widening (rtd-5, rtd-7 gated on both halves); no shadow/dual-write on the port. Worker rows mint `IRPT_BCKEND-W<slot>-S<k>`; the DS mints `IRPT_BCKEND-D-S<k>`.

### R4.4 Not decided here

Which HoldingsSnapshot schema is the contract (L4's); whether the port is this project's conformance or a D14 rider (rtd-6's judgment record puts the evidence in front of the CTO); the enforcer consolidation (rtd-8's judgment record); the `eol=lf` attribute (a row).

## R3. ROUND 3 -- THE RECUT ON THE ROUND-2 ANALYSIS (v0.3, 2026-09-18 ~01:5xZ, `2.0.0_SA_COO~B`)

**Input:** the CTO's round-2 analysis @cfe3a33a9b (on the CVO's L8/L9 @c1a8cd2543, msg 97752): 11 PASS / 1 FAIL across
twelve judgment criteria, ZERO outcomes REALIZED because no round-2 cell was cut to exercise one; five items the round
carries (RT5-AC2's one-paragraph repair; W4-S25/W4-S28 re-owned under R-42 with W4-S28's disarm act as a BYTES
comparison; the ACROSS-INPUTS renderer control before FWD-3/4/8 are narrowed again; W4-S23's re-cut bar and S32's
stale batteries retired; the 53 graduated ARMED rows' intake against LIVE owners). Plus this seat's own carries from the
drain (S53/S54/S55): the wall behind IB-rt-6 is narrower than round 2 recorded, and FWD-1/FWD-7 cannot wait on
ADVI_FIRMBKTS. **The choice: RE-ISSUE against the frozen v0.2 rectangle, not a re-decomposition** -- every round-3 cell
is a repair, an exercise or a control on a round-2 surface; no PRD row is newly served and no surface is added.

### R3.1 THE RECTANGLE -- five round-3 cells

| cell | executes | serves | write surface | verb | deploys | live arm |
|---|---|---|---|---|---|---|
| `IB-rtc-1` | RT5-AC2's repair (analysis s."THE ONE FAIL") | FWD-1, FWD-5, FWD-7 | IB-rt-5's proof instance (the RT5-AC2 row gains the sibling's host reading, cited and hashed) | record | no | no |
| `IB-rtc-2` | row W2-S51 (the bundle's closure), the Rule 13 DS act | FWD-1, FWD-7, FWD-5 | `.tools/safe_deploy_core.py` CODE_TREES; the re-mint through `--mint-bundle`; on-host import proof | deploy (DS lane) | S3 mint | no |
| `IB-rtc-3` | FWD-7's exercise on the deployed dispatch for inf and cot; the 49f arm measured BLOCKED on the control | FWD-7 own, FWD-1 | none (the runner and the dispatch as deployed; artifacts land in the firm buckets) | exercise | no | no |
| `IB-rtc-4` | W4-S28 (bytes), S32 (retire), W4-S23 (vendor bar), W1-S17 (layer fetch) | FWD-4, FWD-3, FWD-8, FWD-2 | rt2_verify_deployed.py; two result headers; RT8's census bar | repair | no | no |
| `IB-rtc-5` | W4-S19's across-inputs renderer control; the real-path arm HUMAN-GATED | FWD-8, FWD-3, FWD-4 | none (the renderer as built; fixtures under the worker's home) | verify | no | no |

**Outcome coverage, run not asserted:** FWD-1 (rtc-1, rtc-2, rtc-3), FWD-2 (rtc-4), FWD-3 (rtc-4, rtc-5), FWD-4 (rtc-4, rtc-5),
FWD-5 (rtc-1, rtc-2), FWD-7 (rtc-1, rtc-2, rtc-3), FWD-8 (rtc-4, rtc-5): **7 of 10 outcomes have a round-3 cell.** FWD-9 and
FWD-10 read ADVANCED cleanly and carry nothing this round. **FWD-11 and the EXERCISED bars of FWD-1/2/5 are NOT cut**,
deliberately: each bars at a live session (a granted advisor; a restricted advisor; an Opal user across firms), which is
the test principal RT2 recorded HUMAN-GATED -- the reserved card at Andrew (restated to `0.0.0_AB_MSTR` at this
issuance). A cell that "exercises" them without the principal would be the self-wrapping harness bound 12 forbids.

**HELD, named:** the 49 Financial directory build (FWD-1/FWD-7's third firm). Its source read is behind
`DenyForeignFirmPrincipals` on `opal-data-49financial`, a CONTROL not a gap; the remedy is a DESIGN decision (run that
firm's build under a 49 Financial principal, or another shape) pitched to `1.0.0_SA_CTO` with this seat's rec at this
issuance. `IB-rtc-3` measures the refusal on this vintage and does not work around it.

### R3.2 THE EDGES AND THE FENCE

```
  edges (1):  IB-rtc-2 -> IB-rtc-3      (the closure must be aboard the bundle before any build)
  heads at spawn = 4 : IB-rtc-1 IB-rtc-2 IB-rtc-4 IB-rtc-5      leaves = 4 : IB-rtc-1 IB-rtc-3 IB-rtc-4 IB-rtc-5
  M, maximal paths = 4          components = 4          depth = 2 (IB-rtc-2 -> IB-rtc-3)         acyclic: trivially
```

| wave | cells | reason |
|---|---|---|
| 1 | `IB-rtc-1` `IB-rtc-2` `IB-rtc-4` `IB-rtc-5` | four heads, four seats, from the first hand-off |
| 2 | `IB-rtc-3` | after the DS lane's mint merges |

### R3.3 SEATING AND THE FAN-OUT

```
fanout: 4 of 4 chains, cap 8, reason: four independent heads and one dependent exercise; four worker
        subagents cold-started (the round-2 subagents died with their sessions -- slot 1: IB-rtc-1;
        slot 2: IB-rtc-3 after IB-rtc-2 merges; slot 3: IB-rtc-4; slot 4: IB-rtc-5) and the DS lane
        0.4.0_DS_ClientPlatform~X re-seated by the issuer under /mstr-spawn for the one act no worker
        may take (IB-rtc-2, Rule 13); the single cross-slot wait is IB-rtc-3 on IB-rtc-2.
```

Each hand-off is a fresh worktree from `HEAD` at hand-off time (`git worktree add -b wk-irpt_bckend-3-<n> /c/tmp/wk-irpt-3-<n> HEAD`;
the DS lane `/c/tmp/wk-irpt-3-ds`), `.tools/terraform.exe` provisioned by the issuer where a root is read.

### R3.4 BOUNDS CARRIED, AND ONE ADDED

Items 1-13 of s.8 stand verbatim on every face. Added on every round-3 face: **R-40** (`1.0.0_SA_CTO` @233f5fd5e4) --
a criterion whose subject is a run or a produced artifact records that artifact's CONTENT HASH beside its run id and is
graded against the hash; and **R-42** -- a `disarm_owner` is a SEAT SERIAL, never a cell, an order or a condition.

### R3.5 WHAT THIS RECUT DOES NOT DECIDE

- The 49 Financial build's principal (a design fork, the CTO's); the test principal (Andrew's card); the scheduled fire
  that is FWD-7's acceptance (the schedule is ENABLED and untouched; the cell's manual invoke is QA).
- The 53 graduated ARMED rows' intake: an OWNER'S word, not a cell's. The 36 owned by `2.0.0_SA_COO~B` are given in
  this seat's own rows during the round; the CTO's 7 and the CVO's 2 are theirs; the 5 owned by terminated worker slots
  carry their carve-outs and are re-placed on `2.0.0_SA_COO~B` under R-42 when this seat gives its word on each.

### R3.6 AMENDMENT 1 (2026-09-18 ~03:1xZ) -- on R-44 and R-45 @57bc083d45, the two calls this round pitched

**Why an amendment and not a round:** both rulings answer calls this seat pitched mid-round on measurements the
round's own cells produced (rows S57->S62, S58, S59 from IB-rtc-2's first pass; S53 from the drain). The rectangle's
cells are the same repairs, exercises and controls; two are RE-CUT to carry the ruled shape, and two are ADDED for the
principal R-44 rules, split at the signature so no cell waits for a seat.

| cell | change | serves | slot |
|---|---|---|---|
| `IB-rtc-2` | RE-CUT: the guard's member-level DISTRIBUTION flag, the 8-file closure with S58's two members ADMITTED, R-45's two-leg consistency control with a one-leg mutant, the re-mint, the on-host repo-shaped import proof | FWD-1, FWD-7, FWD-5 | DS `~X`, re-handed |
| `IB-rtc-3` | RE-CUT: gains the repo-shaped unpack in `refresh.py` and the directory root's apply under ledger before the inf/cot exercise | FWD-7 own, FWD-1 | `~2`, after rtc-2 |
| `IB-rtc-6` | NEW: the 49 Financial principal DECLARED (builder-named role, trust from the host role, five dimension reads and nothing else), the runner's 49F source set through the assumed role, the writer census, plans with 0 destroys, the never-widen sign-off PACKET; NO apply | FWD-1, FWD-7 | DS `~X`, after rtc-2 |
| `IB-rtc-7` | NEW: both halves at HEAD, the two applies under ledger, the NEGATIVE CONTROL (another firm's prefix DENIED, the destination write DENIED, the name off the denied prefixes), then the 49f build through the dispatch -> 3 of 3 directories | FWD-1, FWD-7 | `~1`, after rtc-3, rtc-6 and both halves |

```
  edges (amended): IB-rtc-2 -> IB-rtc-3   IB-rtc-2 -> IB-rtc-6   IB-rtc-3 -> IB-rtc-7   IB-rtc-6 -> IB-rtc-7   (+ the two sign-off halves -> IB-rtc-7)
  heads at this hand-off = 1 : IB-rtc-2      leaves = 1 : IB-rtc-7      depth = 3
  fanout (amended): 1 of 3 chains at the hand-off, cap 8, reason: the DS lane holds rtc-2 then rtc-6 in sequence (Rule 13 on both),
                    slot ~2 takes rtc-3 on rtc-2's merge, slot ~1 takes rtc-7 last; the sign-off halves are the seats' acts, not a cell's
```

**The sign-off split, stated once:** a never-widen act needs CTO+COO halves naming blast radius and rollback per key
(CLAUDE.md NEVER-1). A cell cannot wait for a signature, so `IB-rtc-6` writes the PACKET and stops, the two seats sign,
and `IB-rtc-7` applies. The COO half is `2.0.0_SA_COO~B`'s and is written from the packet, never before it.

**ADDED ~06:4xZ on the packet (IB-rtc-6's NEVER_WIDEN_SIGNOFF_PACKET, step 5) and rows S65/S68:** `IB-rtc-8` -- the `investor_reporting` bundle re-minted through the guard after IB-rtc-6's runner edit merged, so the host runs the K5 runner (a Rule 13 DS act; verified on the served object and on the host, no apply). Edge: `IB-rtc-8 -> IB-rtc-7`. `IB-rtc-7` is amended to re-read the packet's blob hash against the COO half, to apply the mdpf-pipeline root TARGETED to K3 (the one departure from s.6's `-target` never, signed in the COO half because that root also plans an unrelated `mdpf_route_bindings` change, row S68), and to wait on `IB-rtc-8`. `IB-rtc-3` was amended a second time (AMENDMENT 2, @af7d39d96f) on row W2-S55: the dispatch passes no explicit `--as-of`; upheld by `1.0.0_SA_CTO` at 97857 on the PRD's own REUSE row for `lib/trading_calendar.py`.

**ADDED ~07:5xZ on row W2-S56 (IB-rtc-3 AMENDMENT 2's real fires, drained @a4db909717 as FAIL-measured):** `IB-rtc-9` -- both gold runners call jsonschema 4.x-only API (`Draft202012Validator`, `ValidationError.json_path`) on a host running 3.2.0, so every firm's build dies at validation the moment it passes the date check; the two call sites are made version-tolerant in the DS lane (never by mutating the shared MDPF host), pinned by a test with a mutant-environment control, the bundle re-minted, the fix exercised ON THE HOST with the pre-cell tarball as the positive control of the defect. Issuer's ruling: ADJUDICABLE (L5/L6), a code defect in a DS file. Edges: `IB-rtc-9 -> IB-rtc-7`; `IB-rtc-9 -> IB-rtc-3 (AMENDMENT 3: the battery re-run only, no code)`. The eleven contracts use no 2019/2020-only keyword (0 of 11 at HEAD), so draft-7 grading on 3.2.0 is the same grading. IB-rtc-3's instance @a4db909717 is INVALID at HEAD on a CCX pin (an artifact pinned PENDING-THIS-COMMIT that an earlier commit carried); it is replaced by AMENDMENT 3's run.

**Bounds carried:** R-40 and R-42 on every face; R-45's added control (two legs, one mutant) on `IB-rtc-2`; R-44's three
conditions split across `IB-rtc-6` (1, the packet of 2) and `IB-rtc-7` (the apply of 2, and 3).

---

## 0. ROUND 1, CLOSED -- the nineteen cells retained by id

| cell | PRD | round-1 status | what round 2 does with it |
|---|---|---|---|
| `IB-s-18` | B18 | DONE | the eleven schemas move under one versioned artifact (`IB-rt-1`); `AnalysisReport` gains an optional `date_claim` (`IB-rt-10`) |
| `IB-s-17` | B17 | DONE | key constructors typed (`IB-rt-4`) |
| `IB-s-5` | B5 | DONE | the execution-role trust is CloudOps' (carried, s.9) |
| `IB-s-1` | B1 | DONE | ids through one normalizer (`IB-rt-3`); the runner minted (`IB-rt-5`) and built on the schedule (`IB-rt-6`) |
| `IB-s-2` | B2 | DONE | the grain agreed and the projection on the served path (`IB-rt-3`, `IB-rt-2`) |
| `IB-s-3` | B3 (library) | DONE | the wrapper on the six dispatched handlers (`IB-rt-2`) |
| `IB-s-4` | B4 | DONE | a real `build_fn` (`IB-rt-6`) |
| `IB-s-12` | B12 | DONE | the handler and the holdouts (`IB-rt-7`); the prefix removed (`IB-rt-3`) |
| `IB-s-8` | B8 | DONE (wrong mechanism at v0.9) | RECUT to the fixed cloud chain (`IB-rt-9`) |
| `IB-s-6` | B6 | DONE | intake controls (`IB-rt-11`); the poller stays DISABLED (bound 1) |
| `IB-s-7` | B7 | DONE | currency/unit controls (`IB-rt-11`) |
| `IB-s-9` | B9 | DONE | a real request handler on the analysis route (`IB-rt-2`); eviction/self-healing on the broker (`IB-rt-9`) |
| `IB-s-10` | B10 | DONE | glyphs and dates (`IB-rt-10`) |
| `IB-s-11` | B11 | DONE | guarded (`IB-rt-2`); ids normalized (`IB-rt-3`) |
| `IB-s-13` | B13 | DONE | guarded (`IB-rt-2`); the layer rebuilt to five contracts (`IB-rt-8`) |
| `IB-s-14` | B14 | DONE (renderer absent) | the worker renders (`IB-rt-8`) |
| `IB-s-16` | B16 | DONE | unchanged; its stand-in export arm re-measured at `IB-rtb-1` |
| `IB-s-15` | B15 | DONE (after the ruling on W2-S12) | the contract published (`IB-rt-1`); S15-AC3 reissued (`IB-rt-1`) |
| `IB-sb-3` | B3 (battery) | DONE | re-run authenticated on the real path (`IB-rtb-1`) |

---

## 1. THE RECTANGLE -- twelve round-2 cells

| cell | PRD | ruling | slug rows closed | serves | write surface | verb | tf root(s) | deploys | live arm |
|---|---|---|---|---|---|---|---|---|---|
| `IB-rt-1` | B15/B18 | 1, 8 | C-S72, C-S77 | FWD-2 own, FWD-3, FWD-11 | `docs/contracts/investor-reporting/v1/` (routes.json + 11 schemas + CONTRACT.md); the api root reading it; the paired producer-to-consumer tests; the S15-AC3 reissue | build | api (plan clean) | no | no |
| `IB-rt-2` | B3 | 2 | W1-S10, W2-S7 (served half), W2-S9 (handler half) | FWD-2 own, FWD-11 | `guard()` + `FirmBinding` on the six dispatched handlers; a real request handler on `POST /analysis`; a real export-status operation; the unguarded census with its control; the test principal from the existing authorizer's path or a HUMAN-GATED record | build+deploy | directory, performance, ycharts, narrative, export | yes | no |
| `IB-rt-3` | B2/B17 | 4 (ids, grain) | W1-S7, W1-S9, W2-S11, W2-S2 | FWD-1, FWD-2, FWD-5 | `_ids/` (one normalizer, declared raw keys per firm); the runners, handlers and the projection on it; the grain fixtures; the layer carrying `_ids` | build+deploy | performance, narrative (layer) | yes | no |
| `IB-rt-4` | B17 | 4 (keys, exceptions) | W3-S12, W2-S10 | FWD-10 own, FWD-2 | `_keys` typed at every constructor; the one error envelope on every handler error path; injected negatives | build+deploy | directory, intake, ycharts, export, ops | yes | no |
| `IB-rt-5` | B1/B12 | 3(c) | W1-S8, W2-S5 | FWD-1, FWD-5, FWD-7 (dependency) | `.tools/safe_deploy_core.py` CODE_TREES bundle `investor_reporting`; the mint through `--mint-bundle`; artifact verification | deploy (DS lane) | none | S3 mint | no |
| `IB-rt-6` | B4/B1 | 3(a) | C-S73 (refresh) | FWD-7 own, FWD-1 | a real `build_fn` (SSM dispatch of the minted runner on the mdpf daily-runner host, the accrual-trigger pattern); three production builds; four arms on the real path | build+deploy | directory | yes | no |
| `IB-rt-7` | B12 | 3(b), 7 | C-S73 (holdings), C-S75, W2-S11 (holdings) | FWD-5, FWD-2 | `holdings/` handler + root; the api integration; attribution holdouts, distinct clocks, the redistribution difference control | build+deploy | holdings (new), api | yes | no |
| `IB-rt-8` | B14/B13 | 5 | W4-S9, W4-S10, W4-S12, W4-S13, C-S76 | FWD-8, FWD-3, FWD-4 | the render controller + host dispatch on the estate's browser-host pattern; the layer at 5 of 5 contracts; stable export identity; the synthetic PDFs inventoried and reader-excluded | build+deploy | export, ycharts (host), performance, narrative (layer) | yes | no |
| `IB-rt-9` | B8 | 6 | W3-S1, W3-S2 | FWD-4 | the session broker on the packets (cutover, fencing, rotation, eviction on fixtures); the research root absorbed; the host STOPPED | build+deploy | ycharts (+ research root retired) | yes | **qualified** (arm 5 is L10's) |
| `IB-rt-10` | B10 | 6 | W3-S10, W3-S11 | FWD-4, FWD-3 | per-document font mapping; `date_claim` provenance (optional contract property) | build | none | no | no |
| `IB-rt-11` | B7 | 7 | C-S74 | FWD-9 own, FWD-4 | currency/unit validation; quarantine over relabeling; correction provenance | build | none | no | no |
| `IB-rtb-1` | B3 (battery) | 2 (proof) | W1-S10 (measurement) | FWD-2 own, FWD-11, FWD-1, FWD-5, FWD-8 | the authenticated replay across every v1 route on the real path (or HUMAN-GATED beside the post-authorizer plane) | verify | none | no | no |

**Outcome coverage, run not asserted: 10 of 10 `FWD-n` in the PRD header have >= 1 round-2 cell** (FWD-1: rt-3 rt-5 rt-6 rtb-1; FWD-2: rt-1 rt-2 rt-3 rt-4 rt-7 rtb-1; FWD-3: rt-1 rt-8 rt-10; FWD-4: rt-8 rt-9 rt-10 rt-11; FWD-5: rt-3 rt-5 rt-7 rtb-1; FWD-7: rt-5 rt-6; FWD-8: rt-8 rtb-1; FWD-9: rt-11; FWD-10: rt-4; FWD-11: rt-1 rt-2 rtb-1). **Slug coverage: 25 of 25 OPEN remediation rows are closed by a cell or carried by name in section 9** (W1-S4, W3-S3 carried to CloudOps with the CTO as gate; every other row in the table above).

**Placement axis:** `laptop`, every cell.

**Cell vocabulary (Rule 24):** as v0.1.1 -- `status` = DONE / IN-FLIGHT / OPEN / HELD / NOT-EVALUATED. Every round-2 cell reads OPEN at v0.2.

---

## 2. WHAT L5 ADDS PER CELL

Inlined on each face under "What L5 adds (decomposition v0.2 s.2, s.6, s.9)"; the faces are the carrier. Two additions bind every cell and are s.8 bounds 12 and 13: **no self-wrapping harness as evidence** (an arm's subject is the real route file, the real dispatcher, the deployed function, the served object) and **typed, issued identifiers at every boundary** (a display name, an e-mail, a raw upstream key or a request-controlled firm token is refused and never echoed).

---

## 3. THE CHAIN READ -- computed from the edge set, not chosen

```
  edges (9, keyed to OBSERVED completion of the source cell):
    IB-rt-3 -> IB-rt-6    IB-rt-3 -> IB-rt-7    IB-rt-5 -> IB-rt-6
    IB-rt-1 -> IB-rtb-1   IB-rt-2 -> IB-rtb-1   IB-rt-4 -> IB-rtb-1
    IB-rt-6 -> IB-rtb-1   IB-rt-7 -> IB-rtb-1   IB-rt-8 -> IB-rtb-1

  heads releasable at spawn (no incoming edge) = 9 :  IB-rt-1 IB-rt-2 IB-rt-3 IB-rt-4 IB-rt-5 IB-rt-8 IB-rt-9 IB-rt-10 IB-rt-11
  leaves (no outgoing edge)                     = 4 :  IB-rt-9 IB-rt-10 IB-rt-11 IB-rtb-1
  M, maximal paths through the edges            = 10
  edge-connected components                     = 4 (the battery pole; rt-9; rt-10; rt-11)
  longest dependency depth (cells)              = 3 :  IB-rt-3 -> IB-rt-6 -> IB-rtb-1  (also IB-rt-5 -> IB-rt-6 -> IB-rtb-1)
  acyclic: checked (the chain script refuses a cycle)
```

**THE BINDING FACTS.** (a) Round 2 is WIDE and SHALLOW where round 1 was narrow and deep: nine heads, depth three. The useful width is therefore the slot count, not the pole count: five seats work from the first hand-off. (b) The one shared dependency is `IB-rt-3` (the normalizer): `IB-rt-6` and `IB-rt-7` consume it and it is finished BEFORE either is handed. (c) `IB-rt-5` is a DS-lane act on a shared tool; the refresh build waits on it by an edge, so no worker is asked to do a DS act.

---

## 4. THE ROUND FENCE -- the dependency waves inside ONE issuance

| wave | cells | the fence's reason |
|---|---|---|
| 1 | `IB-rt-1` `IB-rt-3` `IB-rt-4` `IB-rt-5` `IB-rt-8` | the seam, the ids, the keys, the mint, the renderer: five heads, five seats, the CTO's "seam first" |
| 2 | `IB-rt-2` `IB-rt-7` `IB-rt-9` | the guards (after the seam's v1 file), the holdings handler (after the normalizer), the broker (after the keys) |
| 3 | `IB-rt-6` `IB-rt-10` | the refresh build (after the mint and the normalizer), glyphs and dates |
| 4 | `IB-rt-11` | intake controls |
| 5 | `IB-rtb-1` | the authenticated replay across everything |

The fence is a plan, not a commitment; a wave is the dependency order inside a queue and the order in which the COO hands cells across queues at the drain.

---

## 5. SEATING AND THE FAN-OUT L6 WILL CARRY

**Eleven cells are worker cells** (`0.9.0_WK_IRPT_BCKEND~n`, the four round-1 subagents CONTINUED with their context intact -- the spine's "no respawn, no cold start"; Opus at high effort, the model passed explicitly at every resume until the definition's own value is trusted again), **and one cell is a DS-lane cell** (`0.4.0_DS_ClientPlatform~X`, seated by the issuer with `/mstr-spawn` for this order alone; the rule-13 act the CTO's ruling 3(c) opened). Under RULING 1 a seat's write surface is exactly the `<paths>` its order names.

```
fanout: 5 of 10 chains, cap 8, reason: the round is nine heads wide and three deep, so every seat
        works from the first hand-off; four are the round-1 worker subagents resumed on the surfaces
        they already own (slot 1 ids-holdings-replay: IB-rt-3, IB-rt-7, IB-rtb-1; slot 2 seam-guards-
        refresh: IB-rt-1, IB-rt-2, IB-rt-6; slot 3 keys-broker-extract-intake: IB-rt-4, IB-rt-9,
        IB-rt-10, IB-rt-11; slot 4 export: IB-rt-8) and the fifth is the DS lane for the one act no
        worker may take (IB-rt-5); the cross-slot waits are IB-rt-6 on IB-rt-3 and IB-rt-5, IB-rt-7 on
        IB-rt-3, and IB-rtb-1 on rt-1, rt-2, rt-4, rt-6, rt-7, rt-8 -- hand-offs the COO sequences at
        the drain.
```

| seat | queue (dependency order) | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` | `IB-rt-3` -> `IB-rt-7` -> `IB-rtb-1` | `IB-rtb-1` after `IB-rt-1`, `IB-rt-2`, `IB-rt-4`, `IB-rt-6`, `IB-rt-8` merge |
| `~2` | `IB-rt-1` -> `IB-rt-2` -> `IB-rt-6` | `IB-rt-6` after `IB-rt-3` and `IB-rt-5` merge |
| `~3` | `IB-rt-4` -> `IB-rt-9` -> `IB-rt-10` -> `IB-rt-11` | none |
| `~4` | `IB-rt-8` | none |
| DS `~X` | `IB-rt-5` | none; its merge releases `IB-rt-6` |

Each hand-off is a fresh worktree from `HEAD` at hand-off time (`git worktree add -b wk-irpt_bckend-2-<n> /c/tmp/wk-irpt-2-<n> HEAD`; the DS lane `/c/tmp/wk-irpt-2-ds`), `.tools/terraform.exe` provisioned by the issuer, the halt-gate serial file written by the worker before any apply, the OPEN sentinel committed before any act (round-1 rule W3-S4).

---

## 6. TERRAFORM ROOTS, STATE AND THE DEPLOY DISCIPLINE

The ten round-1 roots stand (s.6 of v0.1.1; state keys unchanged; every provider cache was purged estate-wide on 2026-09-11 so every plan begins with `init` on the vendored binary). Round 2 adds ONE root and retires one:

| root | state key | cells | change |
|---|---|---|---|
| `holdings/` (new) | `investor-reporting/holdings/tfstate` | `IB-rt-7` | the holdings handler Lambda + role |
| `ycharts-research-20260911/` (retired) | its own | `IB-rt-9` | absorbed into `ycharts/` by `state mv` under the ledger, then removed from the tree |
| `api/` | unchanged | `IB-rt-1`, `IB-rt-7` | reads the v1 contract path; gains the holdings integration |
| `directory/`, `performance/`, `narrative/`, `export/`, `intake/`, `ops/`, `ycharts/` | unchanged | as the rectangle says | code/hash changes and the layer version only; plans show nothing else |
| `portal-auth/` | not this project's | none | the WAF read artefact is CloudOps' (CTO item 4); no cell touches it |

Every apply is `.tools/safe-apply.sh` under a change-management entry whose OPEN sentinel is committed BEFORE the act and whose close is committed BEFORE the grading reads; served bytes verified as `CodeSha256`; `-target` never; two worktrees never apply one state (the seating above keeps each root in one slot; `api` is shared by `IB-rt-1` and `IB-rt-7` in dependency order across slots, handed only after the earlier merges).

---

## 7. THE BATTERY -- run at L5, with each instrument's blindness stated

| instrument | disposition | result | what it does NOT cover |
|---|---|---|---|
| the chain read | RUN | 9 edges, 9 heads, 4 leaves, M=10, 4 components, depth 3, acyclic (section 3) | trusts this document's edges; a missing edge shows as false width |
| outcome + slug coverage | RUN | 10 of 10 `FWD-n` served; 25 of 25 OPEN slug rows closed by a cell or carried by name (section 1, section 9) | a served outcome is not a REALIZED one; two rows are carried to another lane, not closed |
| ruling coverage | RUN | 8 of 8 rulings map to >= 1 cell (1: rt-1; 2: rt-2, rtb-1; 3: rt-5, rt-6, rt-7; 4: rt-3, rt-4; 5: rt-8; 6: rt-9, rt-10; 7: rt-7, rt-11; 8: rt-1 + section 9) | the mapping is this document's reading of the rulings; the CTO's L10 read is the check |
| surface re-pin | RUN at `67ef99e5c2` | every round-1 surface the faces build on PRESENT (the ten roots, `_authz`, `_scope`, `_keys`, the runners, the packets, the layer); the new homes ABSENT as they must be (`_ids/`, `holdings/`, `docs/contracts/investor-reporting/`) | existence, not content |
| the gold-execution pattern | RUN (comp-find) | `infra/aws/lambda/mdpf-pipeline/mdpf-accrual-trigger/lambda_function.py` runs a minted bundle on the mdpf daily-runner host by SSM (`tar -xzf` into `/opt/mdpf/scripts/gold/`, `python3 ...`) -- the pattern `IB-rt-6` reuses | whether that host carries the runner's dependencies is measured by `IB-rt-6` arm (d), not here |
| the browser-host pattern | RUN (read at the round-1 drains) | the BD auto-login host and the YCharts host carry a browser runtime; the export renderer reuses that STYLE (`IB-rt-8`) with zero egress | whether either host's runtime renders the counterpart's package is `IB-rt-8` arm (a); a HUMAN-GATED reading is admitted |
| `comp-schedule`, `comp-iam` | INHERITED from the round-1 cut; re-run per cell where a schedule target or a role changes (rt-6, rt-2, rt-3, rt-4, rt-7, rt-8, rt-9) and recorded in each instance | a ledger of gates; DESIRED plane only |
| lane read | RUN | the worker serials hold no open order on any other pipeline project (round 1 is 19 of 19 complete); the DS lane `~X` is fresh; the round-1 model flip is repaired at HEAD (`worker.md` `model: opus`, 0d57ceb2f9) and the model is still passed explicitly at every resume | the seating lint at commit is the enforcement |

---

## 8. BOUNDS THAT BIND EVERY ORDER, inlined at L6

Items 1-11 of v0.1.1 s.8 stand verbatim on every face (no live vendor call, the mailbox read and a YCharts login or capture included; no monitor; cross-firm both shapes; deploys under ledger with the OPEN sentinel committed before the act; Andrew's fixed constraints plus the v0.9 fixed YCharts mechanism; no credential; no served output touched; the spec frozen with the row as the only off-spec act; every invocation terminates; the commit gate; scratch). Two are added:

12. **NO SELF-WRAPPING HARNESS AS EVIDENCE** (rows W1-S10, S24): an arm's subject is the real route file, the real dispatcher, the deployed function, the served object; a census prints its denominator and a `0 of 0` reads VACUOUS; every manifest of hashes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY** (rows W2-S9/S11, W1-S7, W3-S12): a display name, an e-mail, a raw upstream key or a request-controlled firm token is refused at every function boundary and never echoed.

And the round-1 qualification stands: a live arm is an express qualification on the face, read by the CTO at L10 on Andrew's per-use word, never a mechanical criterion (v0.1.1 s.8 item 1). One cell carries one: `IB-rt-9` (arm 5 of v0.9, Comparison and Multi-Comparison live).

---

## 9. ROUND-2 FINDINGS AND CARRIES, for the CTO's L10 read

1. **Two OPEN slug rows are not this project's to close and are carried by name with the CTO as gate:** `W1-S4` (the IRPT roots' provider-lock policy -- `0.7.0_AE_CloudOps`; the lock files are tracked at HEAD and every root plans clean on 5.100.0, so the row is a policy question, not a drift) and `W3-S3` (the per-firm execution roles' trust -- `0.7.0_AE_CloudOps`; `IB-rt-2`'s guards do not depend on assuming them).
2. **The rule-13 act is seated, not absorbed:** `IB-rt-5` is issued to `0.4.0_DS_ClientPlatform~X`, a DS lane this issuer spawns for that order under `/mstr-spawn` (COO function, Andrew-direct 2026-08-28); the face is under this project's `task-orders/` with a pointer in the lane's own `task_orders/` home so the receiver rule (`AGENTS.md`) is met.
3. **Deletion of the four synthetic PDFs is Andrew's word** and stays carried (`IB-rt-8` proves reader exclusion and inventories; it moves nothing).
4. **The optional `date_claim` property on `AnalysisReport`** is the one contract edit of the round (`IB-rt-10`), additive under `additionalProperties:false`; it is the L5 proposal the slug asked for and the CTO reads it at L10.
5. **The unguarded three were protected by accident** (a consent gate, an identity-less request shape, an absent operation); `IB-rt-2` replaces accident with the wrapper and the judgment names which accidental protection changed.
6. **The counterpart's round-2 seam cell regenerates against `IB-rt-1`'s artifact**; the two lanes share FILES (`docs/contracts/investor-reporting/v1/`), never messages; a consumer fixture that disagrees with II.3 fails the paired test on this side and is a row, never a schema change.

---

## 10. CROSS-PROJECT SEAMS (no cell is jointly owned)

| seam | this project | the counterpart | graded inside |
|---|---|---|---|
| the contract artifact `docs/contracts/investor-reporting/v1/` | `IB-rt-1` publishes; the paired producer-to-consumer tests | its round-2 seam cell regenerates the typed client against it | FWD-1, 2, 3, 5, 11 |
| `RenderPackage` (versioned, `runtime: 'browser'`) | `IB-rt-8` executes the counterpart's real package | its F9 produces it (the FNTEND slug's W2-S4) | FWD-8, FWD-3, FWD-4 |
| the browser request half of `AnalysisRequest` (v0.10) | `IB-rt-2`'s analysis request handler consumes it and builds the `resolved` half server-side | its F5 sends it | FWD-4 |
| `date_claim` on `AnalysisReport` | `IB-rt-10` adds the optional property | its consumer reads it | FWD-4, FWD-3 |
| `StatusEnvelope` reason codes (closed enum) | `IB-rt-4`'s error envelope | its status panel | FWD-6 (its), FWD-10 |

---

## 11. WHAT THIS DECOMPOSITION DOES NOT DECIDE

- **The `<paths>` block of any order** -- L6's, per order; under RULING 1 it IS the grant.
- **Which existing host renders** (`IB-rt-8`) and **which host runs the minted runner** (`IB-rt-6`): the cells read the estate's patterns and choose inside the bounds; a host that needs egress is a HUMAN-GATED arm.
- **Whether a test principal exists** (`IB-rt-2`): the first read is the measurement; HUMAN-GATED is an admitted reading.
- **The live YCharts arms** (arm 5 of v0.9): the CTO's qualified read on Andrew's per-use word.
- **The DS lane's own tooling choices inside the guard** (`IB-rt-5`): the guard's shape is copied, its tests are the control.

---

## 12. ADDENDUM, ROUND 19 (2026-09-27, 2.0.0_SA_COO~P, on 1.0.0_SA_CTO 101946/101977) -- cell IB-sr-1, the COT BD session auto-login

One cell, cut from surprise row `IRPT_BCKEND-S158` (ARMED). It is not part of any round's rectangle: it is the issuer's remediation
cell for a row whose disarm owner the CTO named.

| cell | outcome served | owner | risk | depends on |
|---|---|---|---|---|
| `IB-sr-1` | FWD-1's COT Performance hop (a live `blackdiamond/cot/session`), goal criteria 1 and 3 at COT | `0.6.2_AE_PartnerETL~S` (MSTR seats it on the order's commit, 101975) | SERVED | none |

**What is measured (CTO 101946):** scheduler `cot-bd-session-daily-et` ENABLED (cron 07:30 America/New_York); SSM document
`opal-cot-bd-session-fetch` last Success 2026-09-16, Failed 09-24..09-27 (latest 60650bfe, rc 1, output empty -- `set -e` aborts
before the S3 log upload at `infra/aws/terraform/cot-pipeline/ssm.tf:63-69`); `blackdiamond/cot/session` last changed 09-16.

**The cell:** name the failure cause from the box's own log, make the document upload its log on failure, and reach ONE Success
that moves `blackdiamond/cot/session` AWSCURRENT. Vendor sign-in only through the document (its scheduler or its existing
trigger), never by hand.

## 13. ROUND 19, WORKSTREAM ~P (2026-09-28, 2.0.0_SA_COO~P, on PRD ADDENDUM v0.18 @33ae74760b, CTO 102396)

Cut from `STATUS~P.md` @025cef10fd's next-list in its priority order. Base: CLOUD HEAD (MSTR's act-4 drain landed
@c161a2faca; B3 proof row IRPT_BCKEND-S178). Checks: `deliverables/2.0.0_SA_COO~P/checks/r19/`, each dry-run at the
base before this cut (build arms FAIL, control arms PASS).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-191` | FWD-3 (Performance backend half), goal criterion 1 at 49F; NEW-01 (rows S176/S177) | WORLD (path floor; the cell builds and tests only, the served move is the COO's act under both halves) | none | A |
| `IB-pr-192` | FWD-3; UIC-06 backend half and UIC-07 (Since inception from the account's first data point) | WORLD (as above) | `IB-pr-191` (same files: f49_engine.py, entry.py) | A |
| `IB-pr-193` | FWD-9 (Export) hygiene: a refused async replay logs REFUSED, not FAILED | WORLD (path floor; code and test only) | none | B |

**IB-pr-191 -- the 49F engine never serves an impossible return.** `f49_engine.calculate` refuses by a named class
`EngineReturnImplausible(EnginePerformanceRefused)` when any linked row in the window carries `r_net <= -1.0` (the
measured NEW-01 shape: OK, bmv 13,360.59, emv 0.0, cf_net 0.0 on 2026-04-16; 28 such OK account-days YTD across 24
accounts). The boundary (`performance/entry.py` `build_entry` reasons) names it `DEPENDENCY_UNAVAILABLE`. The
arithmetic (`parity_period_returns`) and the producer (`c02_twr_engine.py`) are NOT touched: the producer rule is a
design fork routed to 1.0.0_SA_CTO.

**IB-pr-192 -- Since inception answers from the account's first data point.** A request whose start is the portal's
Since-inception sentinel `1970-01-01` (UIC-07, measured) is read as the engine lane's ruled period `SI`, anchored at
the account's first OK `business_date` in `twr_daily`; the report's `dates.actual_start` is that day and
`returns.period_returns` names `SI`. Every other unruled window (3Y) still refuses as `WindowNotRuled`. The anchor is
read, never typed; the IB-pr-191 guard applies to SI as to every window.

**IB-pr-193 -- the async export log says what happened.** `export/entry.py` `run_async_submit` logs stage `REFUSED`
(and re-raises) when `submit_async.run` raises `AsyncSubmitRefused` before the pointer moves; every other exception
still logs `FAILED`.

**Not cut this round, with the reason:** the live Comparison + export window (K4/K5/K8/K10) is the COO's own act at
this round's close, under its own packet and both halves (TO-IV-e-78 is complete); the per-headline causal filter has
no cell text yet (CTO tick 65 names it only as enrichment); the ~P hygiene items that are not code (proof_of_spec
template path S167, directory Terraform root, cherry-pick review) are record acts, not cells.

fanout: 2 of 2 chains, cap 8.


### 13.1 ADDENDUM 1 (2026-09-28 ~22:3xZ, 2.0.0_SA_COO~P, on 4.0.0_SA_CRO D1 RESULT @5f82151a2e and 1.0.0_SA_CTO 102447)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-194` | FWD-3; NEW-01 on the served surface (ledger irpt-adapter-implausible-guard-20260928 D1) | WORLD (path floor; code and tests only, the served move is the COO's act under both halves) | `IB-pr-191` (on CLOUD) | A (carried by the REOPENED order TO-IB-pr-191, slot ~63) |

**IB-pr-194 -- reopen refuses a pre-guard impossible report.** The served page reopens RETAINED reports
(`retained.py` `_compute` -> `reopen`) and never re-runs `f49_engine.calculate`, so IB-pr-191's guard did not reach the
two NEW-01 reports retained before 22:02Z. `retained.implausible_engine_series(report)` (any
`daily_cumulative_series` value <= -1.0) gates `reopen` for the engine firm, raising `EngineReturnImplausible`. Nothing
in the store is deleted, rewritten or re-derived. Live census at the cut: 23 retained 49F reports, exactly 2 flagged
(790fe675, 74fb35a4). This packet's blast radius counts BOTH readers of the served figure (compute and reopen) -- the
miss the adapter packet made.

fanout: 1 of 1 chains, cap 8.


### 13.2 WORKSTREAM ~E, ROUND 19 (2026-09-28 ~22:5xZ, issuer 2.0.0_SA_COO~P, on Andrew-direct calls 2-3 and 1.0.0_SA_CTO 102456/102461)

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-er-191` | FWD-3 (49F Performance): the engine's daily return is holdings-based, no flow logic; closes rows S181 and W61-S2 | WORLD (rewrites the served twr_daily history; QA prefix first, then both never-widen halves) | none | E |

**IB-er-191 -- the 49F engine's daily return is holdings-based.** Andrew's call 3 fixes the method: the day-t account
return is the weight-pro-rated day-t price return of the securities held at the end of t-1 (weights over the account's
t-1 fair value; cash earns zero; no inflow/outflow term). This replaces the flow-based `c02_twr_engine.py:264`, whose
full-value exits and scaled flows produce 26 OK rows at r_net <= -1 year to date. The rebuild also restores the value
columns of the two partitions of row W61-S2. One order, to the DS seat 0.4.0_DS_ClientPlatform~E (seated by MSTR
102458). A disjoint scope (a producer outside every IRPT write surface), hence its own workstream.

fanout: 1 of 1 chains, cap 8.

**13.2 CANCELLED (2026-09-28 ~23:0xZ):** Andrew-direct ~22:4xZ (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`)
moves every firm channel to the holdings basis in ONE consolidated gold shape. `IB-er-191` is cancelled with that
pointer; its 49F work is re-cut as a slice of the consolidated gold after the CRO brief (L1) and the CTO L4 addendum.
The deployed NEW-01 page guard (adapter hcZpXDDo) and its reopen remedy (`IB-pr-194`) stay.


## 14. WORKSTREAM ~E, ROUND 1 (2026-09-28 ~23:5xZ, issuer 2.0.0_SA_COO~P, on PRD ADDENDUM v0.19 @65f3dde719 rulings 10-11)

The holdings-basis gold thread (spine v3.16: round 1 builds the thread). One cell, one order, to the DS seat
0.4.0_DS_ClientPlatform~E. Its downstream hops (the adapter reading the gold, the page, the PDF) are ~P's own later
cells, cut once this gold exists.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-er-201` | FWD-3 thread, hop 1: one invested 49F account (0010498003), YTD, silver -> holdings-basis gold | WORLD (new gold prefixes; no reader switched, nothing served moves) | none | E1 |

**IB-er-201.** The source declaration as data (ruling 1), the gold script writing `holdings_performance_daily` and
its manifest at the builder addresses (ruling 9), the method of call 3 (rulings 2-5), and an ad-hoc QA run for the
thread account over the YTD trading days. The schedule, the other two firms and the adapter switch are later rounds.

fanout: 1 of 1 chains, cap 8.


## 15. ROUND 20, WORKSTREAM ~P (2026-09-29 ~01:2xZ, issuer 2.0.0_SA_COO~P, on PRD v0.19 rulings 10-12 and 1.0.0_SA_CTO 102519)

The FWD-3 thread's next hop on ~P: the adapter reads the holdings gold (~E round 1 built hop 1 for account
0010498003). One chain, one worker; the page and PDF hops follow the served move.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-201` | FWD-3 thread hop 2: `holdings_gold` reader with f49_engine's contract (YTD/QTD/1Y/SI) | WORLD (path floor; code and tests) | ~E r1 gold | A |
| `IB-pr-202` | FWD-3: `retained.py` switches 49F to the gold (ruling 12, no fallback) and never reopens an engine-era report | WORLD (path floor; code and tests) | `IB-pr-201` | A |

**Served-move precondition (the NEW-01 lesson, both readers):** the switch serves only once the gold covers EVERY 49F
account (today: the thread account only). Otherwise every other 49F account would refuse. The widening is ~E's; it is
asked of 1.0.0_SA_CTO to place.

fanout: 1 of 1 chains, cap 8.


## 16. WORKSTREAM ~E, ROUND 2 (2026-09-29 ~01:4xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ruling 102520 and PRD v0.19 rulings 4, 6, 9, 12)

The 49F gold goes from the thread account to every account, over the full history, and gets its production trigger.
~P's adapter switch (round 20) serves only after this round's manifest reads complete.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-er-202` | FWD-3 (49F): gold for every account 2024-07-09..2026-09-25, manifest complete | WORLD (new gold objects; nothing served moves) | ~E r1 | E2a |
| `IB-er-203` | FWD-3: the daily schedule irpt-holdings-performance-daily + runner Lambda, own ledger | WORLD (new infra) | none | E2b |

IB-er-203 goes to a ~P worker slot because the schedule and Lambda are Terraform (rule 13 keeps the DS seat on
gold scripts); the path grant is the order's `<paths>`, and the producer stays the DS seat's code.

fanout: 2 of 2 chains, cap 8.

## 17. WORKSTREAM ~E, ROUND 3 (2026-09-29 ~05:0xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND-19 ANALYSIS section 6 items 1 and 4, PRD v0.19 rulings 1-9, 11)

Inflection joins the holdings gold (ruling 11's order: 49F, then Inflection, then Cottonwood), and 49F gets its FWD-13
comparison points from the Black Diamond files already landed. The daily runner stays scoped to 49F this round: its
role is firm-scoped (row W65-S1), and widening it to INF is a later cell once IB-er-301's declaration lands.
Cottonwood follows Inflection, and its comparison needs one Black Diamond pull per point (Andrew-direct 2026-09-29, card 3).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-er-301` | FWD-3 (INF): gold for every INF account 2020-04-27..2026-09-25, manifest complete | WORLD (new gold objects; nothing served moves) | ~E r2 | E3a |
| `IB-er-302` | FWD-13 (49F): one comparison row per landed Black Diamond file, both bases stated | WORLD (new gold objects; nothing served moves) | ~E r2 | E3b |

Both cells go to 0.4.0_DS_ClientPlatform~E (rule 13: gold scripts are the DS seat's). The two chains share no output
prefix; they share the producer's home, so the seat works them as one queue.

fanout: 2 of 2 chains, cap 8.

## 18. ROUND 21, WORKSTREAM ~P (2026-09-29 ~06:0xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND-19 ANALYSIS sections 3 and 6, PRD v0.20 rulings 13-17, window 21's K8, 2.0.0_SA_COO~M 102599)

The adapter switch to the holdings gold (round 20, drained @a595a14264) was refused at its CRO half on the gold
(S195). Its re-cut is ~E's producer fix (TO-IB-er-301 amendment 1) plus the adapter guard of ruling 16 below. The
re-cut packet then carries IB-pr-211 and IB-pr-214 in the same artifact.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-211` | FWD-9: the release re-check passes the request, so a render names its grant (W21 K8, entry.py:61) | WORLD (Lambda source) | none | P21a |
| `IB-pr-212` | FWD-5: HoldingsSnapshot contract CATEGORY revision a69fe8e33e staged in irpt-holdings + irpt-ycharts-generate + the lambda-tree copy (~M's step 1) | WORLD (served validator pin) | none | P21b |
| `IB-pr-213` | PRD item 1: the edge role reads only the two public keys (S132), plan only | WORLD (IAM, shared auth) | none | P21c |
| `IB-pr-214` | FWD-3: the fresh path refuses any series point <= -1 (ruling 16), matching the reopen path | WORLD (Lambda source) | none | P21d |

Every served move stays the issuer's, under its own ledger and both halves. The workers build, prove and plan only.
Slots: `1 + max(n)` over the WK~n author lines at HEAD is 67 (row S187's rule), so the round uses 67, 68, 69 and 70.
IB-pr-211 and IB-pr-214 edit different files in one package; they drain separately and meet in the one rebuild.

fanout: 4 of 4 chains, cap 8.

## 19. ROUND 22 (workstream ~P) and ROUND 4 (workstream ~E) (2026-09-29 ~08:4xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND-19 ANALYSIS section 6 item 1, PRD v0.19 rulings 10-12 and ruling 11's order, v0.20 rulings 13-17)

Inflection's gold is complete (~E round 3), so its adapter switch is the next thread hop. Cottonwood, the third firm,
gets its gold. INF's FWD-13 comparison points (weekly Orion household factors) and the daily runner's widening to INF
and COT are the following cells: they are named here, and are cut once their shapes are read.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-221` | FWD-3 (INF): holdings_gold per firm + holdings_sources in retained + installed composes INF; the Orion read retires for INF (both readers in the criteria) | WORLD (Lambda source) | ~E r3 (INF gold, complete) | P22a |
| `IB-er-401` | FWD-3 (COT): gold for every COT account 2026-06-10..2026-09-25, manifest complete, under v0.20 | WORLD (new gold objects; nothing served moves) | ~E r3 (the producer on v0.20) | E4a |

IB-pr-221 goes to worker slot 74 (S197: 1 + max(author lines 72, issued_to 72, branches 61) was 73 at the cut, but ~Y's TO-IB-yr-221 took 73 in the same window @52e63f09ee; amendment 1 re-slots to 74 before any spawn). IB-er-401 goes to
0.4.0_DS_ClientPlatform~E (rule 13).

fanout: 2 of 2 chains, cap 8.

## 20. ROUND 23, WORKSTREAM ~P (2026-09-29 ~12:5xZ, issuer 2.0.0_SA_COO~P, on 2.0.0_SA_COO~M 102754/102775 and 1.0.0_SA_CTO SWEEP-2 ANALYSIS section 3)

~M's round 22 (TO-IB-m22-221, AD-10) adds an optional `account_masks` to the Directory entry. Its docs copy is
committed @4ecbaca410 (blob 27d9a8f7). The lambda-tree contract copy is ~P's shared packaging, and the directory
runner's pre-flight validation stays red until that copy carries the property (row W75-S1). ~M drains IB-mr-221 once
this cell's drain hash lands. The sweep-2 ~P enrichment (the 49F re-switch, then INF) is served acts of the issuer,
with no build cell.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-231` | FWD-5: `_contracts/DirectoryEntry.schema.json` byte-equal to the docs blob 27d9a8f7 (additive `account_masks`) | WORLD (the L6 floor for an infra path; no served Lambda stages this copy) | none | P23a |

One cell, one file; not a direct act, since an infra path's floor is WORLD. Slot 79 (S197: 1 + max(author lines 78, issued_to 78, branches 78)).

fanout: 1 of 1 chains, cap 8.

## 21. ROUND 5, WORKSTREAM ~E (2026-09-29 ~14:3xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO 102832 and row S205)

Row S205 showed that the scheduled producer is the gold's real author. A local re-emit is not. 1.0.0_SA_CTO 102832
carries this to the INF switch (pr-221): its packet must name the SCHEDULED Inflection producer and a fire of it. Today
the one schedule is 49F's (source schwab_08335338). Cottonwood follows as its own cell once INF's shape is read.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-er-501` | FWD-3 (INF): the holdings-performance root schedules `orion` under its own function, role and schedule (firm isolation), grants derived from the registry; plan only | WORLD (schedule + IAM + Lambda, plan only) | none | E5a |

Slot 80 (S197: 1 + max(author lines 79, issued_to 79, branches 79)).

fanout: 1 of 1 chains, cap 8.

## 22. ROUND 24, WORKSTREAM ~P (2026-09-29 ~18:3xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO 102951/102969 and row S216)

Inflection's RAW Orion files stopped after 2026-09-27. Only the parquet copy of positions lands, and it comes from
inf-api-positions, so the ingest mirror refuses it (Ruling 16). The INF holdings producer and the INF adapter switch are
blocked. The CTO ruled the July hold lifted and asked for a diagnosis before any restart. This round names the writer;
the restart is the next cell, under both halves.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-241` | FWD-3 (INF): the raw writer and its stop cause named from logs (read-only); the ingest mirror's stale DOOR 5 comment corrected | WORLD (infra path; no deploy, no AWS write) | none | P24a |

Slot 81 (S197: 1 + max(author lines 80, issued_to 80, branches 80)).

fanout: 1 of 1 chains, cap 8.

## 23. ROUND 25, WORKSTREAM ~P (2026-09-29 ~20:4xZ, issuer 2.0.0_SA_COO~P, on TO-IB-pr-241's diagnosis @0b5cdb06f9)

pr-241 named the raw writer: EC2 inf-bronze-runner i-083ad9ae297f88e9f, started by inf-bronze-trigger. Two independent
fixes follow. The restart and the 09-28/09-29 raw backfill are the issuer's served act under both halves, once both
land.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-242` | FWD-3 (INF): inf-ec2-launch-monitor never suppresses an EMPTY StateTransitionReason (drop '' from NORMAL_PATTERNS) + a unit test | WORLD (Lambda source; no deploy) | none | P24b |
| `IB-pr-243` | FWD-3 (INF): why the recovered runner wrote no raw on 09-28 -- deployed-vs-repo shas + the code path, or the named journal read | WORLD (read-only diagnosis) | none | P24c |

Slots 85 and 86 (S197: 1 + max(author lines 83, issued_to 84, branches 84)).

fanout: 2 of 2 chains, cap 8.

## 24. ROUND 26, WORKSTREAM ~P (2026-09-30 ~14:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND-25 ~P ANALYSIS @dd4c69b696 section 4)

The round-25 analysis found the cause behind S216 to be one file: `lib/silver_ids.py` was never shipped to the INF code prefix after
the 09-28 refactor, so the gold chain that writes Inflection's raw files dies at its third step every day. Round 26 ships it, moves the
already-drained launch-monitor fix to its served function, and answers S219's reader question.

**The reader census the analysis asked for (S219), measured at the cut:** `comp-find 'twr_daily' data infra portal lib` reads 69 hits
across 16,252 first-party files scanned (34,063 ephemeral-floor and 2,820 binary files excluded): DEF 2 (`runners_49f/c02_twr_engine.py`,
the writer; `performance/f49_engine.py`, the adapter's engine reader), SURFACED 19 (the DEF pair plus `holdings_performance.py`,
`runners_49f/{c04_validation_battery,chain_49f_entrypoint,parity_period_returns,perfrp_contract,perfrp_emit_core,perfrp_rollup}.py`,
`runners_cot/c02_twr_engine.py`, `runners_inf/{c02_twr_engine,c04_validation_battery}.py`, `performance/{holdings_gold,retained}.py`,
`performance/retained.tf`, `shared-infra/s3-49financial.tf`, `portal/scripts/perfrp-contract-exercise.mjs`,
`portal/src/pages/AdvisorIntelligence/_shared/perfrp/{cards,contract}.ts`), CONFIG 3, TEST 3. Readers are one or more, so the four
columns are filled by the DS lane (the analysis's second branch); S219 does not close with the retirement.

**The issuer's reading behind IB-pr-261 (recorded so the CTO reads it at the round-26 analysis):** the gold runner syncs every `code/`
prefix FLAT by basename into `/tmp/orion_gold_scripts` (`orion-gold-dispatch.sh:65`, `sync_scripts()` ~:545-620), every INF gold script
imports its helpers flat (`from dtype_coerce import ...`, six scripts), and `_orion_api_silver_lib.py` is the only file under
`data/inf/scripts` importing `from lib.` (1 hit across 174 files). So "ship to the INF code prefix" lands `silver_ids.py` flat beside its
importer under `code/silver/`, and the importer keeps `from lib.silver_ids` first with a flat fallback second -- the accommodation every
other INF script already carries, not the revert ruling 103057 refused. The worker prints both readings before the copy, per the ruling.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-261` | FWD-3 (INF): `lib/silver_ids.py` shipped to where the runner resolves it, after the two readings; ONE real full chain run reaches `INF_API_PULL_POSITIONS_DAILY`; ledger `inf-silver-ids-ship-20260930`; S216 disarms on the issuer's `fact_positions` frontier read at the drain, not on the copy's rc | WORLD (S3 code deploy + one production chain run) | none | P26a |
| `IB-pr-262` | FWD-3 (INF): the pr-242 launch-monitor fix (drained @1431d66d9b, live CodeSha256 `RdBNvM6I...` of 2026-09-21 still carries `''` in NORMAL_PATTERNS) SERVED -- the issuer's own act: build-and-upload, a never-widen packet naming every function that pulls the artifact key `inf-pipeline/inf-ec2-launch-monitor.zip`, both halves at HEAD, safe-apply under a ledger. No worker face: a worker cannot sign or apply | WORLD (served Lambda move) | none | P26b (issuer) |
| `IB-pr-263` | FWD-3 (49F): the two `twr_daily` partitions missing bmv/emv/cf_net/cf_gross filled by the producer's own path (DS lane, rule 13); neighbours byte-identical; ledger `twr-daily-two-partition-column-fill-20260930` | WORLD (two gold objects) | none | P26c |

Carried, not cut: S132 (edge-role least privilege, round-19 analysis) and the INF adapter switch under the sweep-2 every-period rule,
which cannot run until IB-pr-261 lands and the INF holdings producer fires on its schedule.

IB-pr-261 goes to worker slot 97 (S197: 1 + max(author lines 92, issued_to 96, branches 93) = 97). IB-pr-263 goes to
`0.4.0_DS_ClientPlatform~S` (rule 13; no other project on that instance), spawned by the issuer in the issuance turn. IB-pr-262 is the
issuer's.

fanout: 2 of 3 chains, cap 8 (the third chain is the issuer's own served move).

## 25. ROUND 27, WORKSTREAM ~P (2026-09-30 ~19:3xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND-26 ~P ANALYSIS @7c9ed807bb section 4)

Round 26 repaired the INF chain's first break; the analysis rules the next four acts. The top cell is the API enforcement the CTO
made a precondition for window 27 (S238). Three read-only answers decide what round 28 repairs, and one order goes to the Schwab
ingest lane, parked while that lane is dark.

**The reading behind IB-pr-271 (measured at the cut, recorded for the CTO's round-27 analysis):** seven Lambda bundles ship
`_authz/served.py` (`lambda-source-map.json` `files`): irpt-performance-adapter, irpt-directory-search, irpt-narrative,
irpt-ycharts-generate, irpt-export-render, irpt-holdings, irpt-status. Only irpt-performance-adapter and irpt-ycharts-generate ship
`canonical_profile_reads.py`. The proposed patch (~Y @4a3cabe67d) imports it lazily inside the method with a catch-all that fails
closed; `import-closure-check.py` exempts lazy imports by design. On a scratch copy the patch alone fails the deployed-layout check on
exactly five bundles, and would have refused every service principal on every firm in directory-search (the S238 route) with no gate
saying so. So the cell carries the module and its top-level closure (`maintained_sources.py`, `ids.py`) into every bundle that ships
`served.py`, and the deployed-layout criterion (CTO 103370) proves the import in each bundle's own layout.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-271` | FWD-3 CONSTRAINT: `_authz/served.py` refuses a SERVICE principal's selected firm outside its `allowedFirmIds` (FIRM_BINDING), with the profile read injectable and the reader's closure in all 7 bundles; no build or apply in the cell | WORLD (source of 7 served functions; no deploy) | none | P27a |
| `IB-pr-272` | FWD-3 (INF): three read-only answers -- the 09-24 NNA rows (ruling 1: branch A packet or branch B repair), why the mirror and silver-orion did not move `fact_positions` on today's raw (ruling 2), whether Orion positions accept an as-of date from documentation only (ruling 3) | WORLD (read-only; no write, no call) | none | P27b |
| `IB-pr-273` | FWD-3 (49F): the S237/S239 blast-radius read -- the deployed adapter's SI and 3Y for 0093614544 and two others, its reader shape, and every served reader of `twr_daily` with a propagates flag (ruling 4) | WORLD (read-only on deployed bytes) | none | P27c |
| `IB-pr-274` | FWD-3 (49F): the Schwab silver for 2026-09-29 lands via `/49-schwab-conv` and the cause of the missed hour is recorded (ruling 5, row S235); PARKED on `0.6.2_AE_PartnerETL~C` until that seat is LIVE | WORLD (silver data, AE lane) | none | P27d (parked) |
| `IB-pr-275` | FWD-3 CONSTRAINT: the served move of IB-pr-271 -- build, a never-widen packet naming the 7 functions and each one's profile-table grant, both halves, targeted applies under a ledger, then ~Y's live negative control under svc-irpt-analysis (CTO 103318 item 2) | WORLD (served; the issuer's act, no worker face) | IB-pr-271 | P27a |

Conditional, not cut (ruling 4): the 49F holdings-basis re-switch joins round 27 as the issuer's cell only if IB-pr-273 reads
PROPAGATES. Conditional, not cut (ruling 1): the NNA excusal packet (branch A) or the upstream repair (branch B) follows IB-pr-272.
Carried: S132 least privilege on the edge role; the INF adapter switch after S216 disarms and the INF producer fires on schedule.

Slots 98, 99, 100 (S197: 1 + max(author lines 97, issued_to 97, branches 84) = 98). IB-pr-274 goes to the AE lane (parked); IB-pr-275
is the issuer's.

fanout: 3 of 4 chains, cap 8 (chain P27d is parked on a dark AE seat; IB-pr-275 rides chain P27a as the issuer's act).

## 26. ROUND 28, WORKSTREAM ~P (2026-10-02 ~08:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 126 item 1, msg 104117)

Hop 12 of the Analysis trace (`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md` section 12): an
Analysis report exports as an Opal-branded PDF. Batch 126 rules it this workstream's (it owns `export/**`, lane IRPT_COMPLETION_P,
and the export render host). Round 27 stays open on its parked AE order (IB-pr-274); this round is independent of it.

**The reading at the cut:** the gap is in the export Lambda's own resolver -- `export/retained_export.py:71-72` refuses anything but
`report_kind == "PERFORMANCE"` with a server-issued `account_set_id`; `render_grant()` pins `accountSetId`; `print_query()` hard-codes
`kind: "performance"` and the requested window. The rest already speaks Analysis: `export/handler.py:257` chooses
`analysis-portrait-letter` for `report_kind != "performance"` and `:315` forbids "Narrative" text in an analysis PDF; the portal print
page reads `?kind=performance|analysis` and renders `AnalysisDocument` (`portal/src/pages/InvestorReporting/render/PrintEntry.tsx:17-36,
:99-100`). `ops/owned_report.py:90` already builds an ANALYSIS authorization row.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-281` | FWD-9 enrichment (batch 126): `resolve()` admits a retained ANALYSIS report under the current principal with its own identity (no account set), `render_grant()` pins the analysis ids, `print_query()` emits `kind: analysis` with the report's own ids; tests for both kinds; one REAL retained READY Analysis report built locally into a contract-valid bundle and print query (reads only; nothing submitted, rendered or written) | WORLD (source of a served function; no deploy) | none | P28a |
| `IB-pr-282` | the served move of IB-pr-281: build, a never-widen packet with both halves, the targeted apply under a ledger, then ONE Analysis export downloaded for a READY request (batch 126's proof) | WORLD (served; the issuer's act, no worker face) | IB-pr-281 | P28a |

Slot 101 (S197: 1 + max over issued_to, authors and branches = 1 + 100). The worker shares the one worktree DIR
`C:\Users\AndrewBerman\Desktop\wk-irpt-dashbd-1` on its own branch `wk-IRPT_BCKEND-101`, after that DIR's current IRPT_DASHBD order
drains: the laptop disk reads under 10 GB free and a second worktree costs about 3.6 GB.

fanout: 1 of 1 chains, cap 8 (IB-pr-282 rides chain P28a as the issuer's act).

## 27. ROUND 29, WORKSTREAM ~P (2026-10-02 ~10:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND-28 ~P ANALYSIS @ CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_28_P_20261002.md, msg 104156)

Round 28 made `resolve()` admit ANALYSIS (merge @9079753aa7); nothing is exportable until rows W101-S1, S2, S3 close. The analysis's
enrichment list section 2 is this round's rectangle. E3 (the print page's request id) is cut to `2.0.0_SA_COO~D` by the analysis, not
here; the backend's print query already carries `bundle` and `request` (`retained_export.print_query`, @9079753aa7).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-291` | E1 (W101-S1): a PROSPECT-SCOPE render grant in the shared `_render_identity/grant.py` -- for a report with no accounts the grant names exactly the report's own retained artifacts (the report, its sections, its composition, its retained vendor PDF, its `prospect_input_id`) under the exact-owner rule, NOTHING account-scoped and nothing firm-wide; a prospect grant that could read one account or another owner's artifact is refused at build; `retained_export.render_grant()` builds it for a prospect-owned ANALYSIS; the account branch unchanged, every caller named | WORLD (source of a shared served module; no deploy) | none | P29a |
| `IB-pr-292` | E2 (W101-S2): the submit path's Analysis branch in `export/**` -- no narrative step, template `analysis-portrait-letter`, the cutoff is the report's own as-of (the latest section `as_of_date` read from the retained report, never `dates.actual_end`); `submit_installed._validate` admits ANALYSIS with that cutoff | WORLD (source of a served function; no deploy) | none | P29b |
| `IB-pr-282` | E4: the served move as written in section 26, after E1-E3 | WORLD (the issuer's act) | IB-pr-291, IB-pr-292, E3 | P29a |

Write sets are disjoint: IB-pr-291 writes `_render_identity/grant.py`, its new test and `export/retained_export.py` (the grant call);
IB-pr-292 writes `export/submit_installed.py`, `export/narrative_submit.py` and its new test. ONE worker slot (101) takes both in
order: the disk admits one worktree.

fanout: 1 of 2 chains, cap 8, reason: one worktree (disk under 10 GB free); chain P29b queues behind P29a on slot 101.

**Section 27 addendum (2026-10-02 ~10:5xZ, issuer 2.0.0_SA_COO~P, on CTO ADDENDUM 1, cell E5, batch 143 @11340658da, msg 104177).**
IB-pr-291 stored the prospect grant, but the Enforcer refuses `EMPTY_GRANT` on its empty account list (row W101-S4). The addendum
places one cell in round 29, not a recut. GATE (x) of `.tools/to-pipeline-gate.py` admits no new order file into a round that already
has orders at HEAD (and reads no override), so the issuer labels the order ROUND 30, a one-cell round for this addendum cell (row
IRPT_BCKEND-S267). Round 29 (IB-pr-291, IB-pr-292) is terminal; its L10 slug waits on IB-pr-293 so that it carries E5's result.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-293` | E5 (W101-S4): the Enforcer's prospect branch in `_authz/enforce.py` -- typed on the stored prospect scope (passed through `grant.render_ports`), the exact owner re-resolved at read time, `permitted_account_set` empty, `covers` admitting exactly the four pinned artifact keys, its own PROSPECT fingerprint; `_scope/resolve.py` untouched | WORLD (source of the shared served Enforcer; no deploy) | IB-pr-291 (merged @dff84e882f) | P29a |
| `IB-pr-282` | E4, now also after E5 and rows W101-S5/S6 (asked of the CTO, msg 20261002T105037Z) | WORLD | IB-pr-291, IB-pr-292, IB-pr-293, E3 | P29a |

Write set: `_authz/enforce.py`, `_render_identity/grant.py` (`render_ports` only), `_authz/served.py` (port wiring only) and two new
`_authz/tests` files; disjoint from IB-pr-292's (merged @4f3f36d16c). Slot 101 takes it.

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk under 10 GB free); one cell.

**Section 27 addendum, second cell (2026-10-02 ~11:2xZ, issuer 2.0.0_SA_COO~P, on CTO ADDENDUM 2, cell E6, and PRD ADDENDUM v0.24,
batch 149 @11e1413e28; ratified-text half re-signed @e978d1f839, msg 104196).** Rows W101-S5 (serve_submit not routed; ExportBundle
required `narrative_packet_ref`) and W101-S6 (the packaged AnalysisReport contract stale). GATE (x) admits no second new file into
round 30 either, so this cell is ROUND 31 (row IRPT_BCKEND-S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-294` | E6 (W101-S5, S6): `serve_submit` through the Analysis branch (no narrative, the report's own as-of); the ExportBundle takes exactly one of `narrative_packet_ref` or `analysis_report_ref`, docs copy and CONTRACT.md `:330` first, packaged copy byte-equal; the packaged AnalysisReport byte-equal to its docs copy; every reader of `narrative_packet_ref` named | WORLD (the published v1 contract and a served function's source; no deploy) | IB-pr-292 (merged @4f3f36d16c) | P29b |
| `IB-pr-282` | E4, after E5 (IB-pr-293) and E6 (IB-pr-294) | WORLD | IB-pr-291, IB-pr-292, IB-pr-293, IB-pr-294, E3 | P29a |

Write set: `export/{submit_service,narrative_submit,handler,bundle}.py`, the two packaged schemas, the docs ExportBundle schema and
CONTRACT.md, three new `export/tests` files; disjoint from IB-pr-293's (`_authz/`, `_render_identity/grant.py`). It queues on slot
101 behind IB-pr-293: the disk (9.1 GB free) admits one worktree.

fanout: 1 of 2 chains, cap 8, reason: one worktree (disk under 10 GB free); chain P29b queues behind IB-pr-293 on slot 101.

**Section 27 addendum, third cell (2026-10-02 ~11:3xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 154 @4b3e51674c, msg 104203: the
guard's owner amends it).** Item 22 (the request history filtered by client) is refused by `_authz/served.py`'s owner-read guard,
which ~P holds. One cell, ROUND 32 (GATE (x), row IRPT_BCKEND-S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-295` | batch 154: `client_id` admitted on `analysis-request-history` only, by an allowlist keyed by operation in `served.py`; proven through `served.Entry` (history(client) a subset of history(), an unknown client `items: []`, one refusal arm per other owner read) | WORLD (the shared served layer's source; the served move is irpt-status's next packet, 2.0.0_SA_COO~Y) | IB-pr-293 (merged @88480ab9d8) | P32 |

Write set: `_authz/served.py` and two new `_authz/tests` files; disjoint from IB-pr-294's. It queues on slot 101 behind IB-pr-294.

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk under 10 GB free); one cell, queued behind IB-pr-294 on slot 101.

**Section 27 addendum, fourth cell (2026-10-02 ~12:3xZ, issuer 2.0.0_SA_COO~P, inside its own decomposition).** Rows W101-S7 (no
production reader feeds the Enforcer's owner port, so every served prospect render refuses) and W101-S9 (print_query decides Analysis
by shape, not kind); remedy owner ~P; batched into ONE cell. Row W101-S8 (portal adapt.ts) needs no cell: 2.0.0_SA_COO~D msg 104228
showed no portal path reads a server-frozen ExportBundle (previewExportBundle rejects NoDeclaredRoute; the portal composes its own).
ROUND 33 (GATE (x), row IRPT_BCKEND-S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-296` | W101-S7 + S9: `render_ports_from_env` passes a read-only retained-owner reader (the report index the function already reads, the writer's key); `print_query` takes the resolved kind | WORLD (the shared served layer's source; the served move is E4) | IB-pr-293, IB-pr-294 (merged) | P29a |
| `IB-pr-282` | E4, after IB-pr-296 | WORLD | IB-pr-291..296, E3 | P29a |

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk under 10 GB free); one cell.

**Section 27 addendum, fifth cell (2026-10-02 ~15:0xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 175 @6621e009c6, msg 104290).**
E4's readiness record (`deliverables/2.0.0_SA_COO~P/E4_ANALYSIS_EXPORT_READINESS_20261002.md`, @1772640238) found four gaps. G1
(export packaging) and G2 (every grant-staging function packages the owner reader; row S271 ARMED) are this seat's, as is G4 (the
receipt's route; row S272): one repair cell, ROUND 34 (GATE (x), row S267). G3 (irpt-status render ports) is 2.0.0_SA_COO~Y's after
M2 and hop 11 (requirements sent 14:41Z).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-297` | G1 + G2 + G4: the export stages AnalysisReport and ExportBundle at HEAD; every function staging grant.py stages report_owner.py and reports/repository.py, with a packaging test; the receipt names the live download route, and the live entry answers a SigV4 signed GET in hop 11's shape | WORLD (build map + a served function's source; no deploy) | IB-pr-296 (merged) | P29a |
| `IB-pr-282` | E4, after IB-pr-297 and ~Y's G3 | WORLD | IB-pr-291..297, E3, G3 | P29a |

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk 7.3 GB free); one cell.

**Section 27 addendum, sixth cell (2026-10-02 ~17:4xZ, issuer 2.0.0_SA_COO~P, on CTO RULINGS batch 178 @2a537cbad4, msg 104324 --
Andrew's IR fold-in, Performance P-1..P-7 to this workstream).** P-4 first: the served holdings-gold path labels a gross figure NET
(row S275). Batched with row S276 (ARMED): build-and-upload.sh deleted 19 tracked performance/ files during this seat's adapter build
(restored from HEAD). ROUND 35 (GATE (x), row S267). P-2, P-3 and P-6 are IRPT_DASHBD cells (its decomposition); P-5 waits on
Andrew's population vendor word; P-1 is the acceptance.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-298` | P-4 (holdings_gold.py fee_basis GROSS) + S276 (cleanup_staged restores tracked paths; staging refuses a dirty tracked destination) | WORLD (a served function's source and the shared build tool; no deploy) | none | P35 |

fanout: 1 of 1 chains, cap 8, reason: one worktree (disk 7.0 GB free); queued behind IRPT_DASHBD DB-b-10 on the shared DIR.


## 28. ROUND 36, WORKSTREAM ~P (2026-10-03 ~03:4xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 202 @8da55ee13b, msg 104524)

Row S292 (ARMED, relayed from 3.0.0_SA_CVO): Inflection's gold missed 2026-10-01 because each scheduled fire computes exactly one
day, and the adapter links over a missing day silently. The disarm is done: 10-01 was landed as one new key (row S294, @6e22aca10b),
and the ledger's A1 is amended. Batch 202 places the CLASS here as two cells, both firms: the consuming half first, then producer
catch-up. GATE (x) puts them in ROUND 36 (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-299` | the adapter names a trading day with no partition on the value and drops its `measured` claim; never refuses, never links silently (nothing served) | WORLD (the served adapter's source) | none | P36a |
| `IB-pr-300` | the holdings producer's scheduled fire computes every missed trading day through T-1, at most 5 per fire, stopping at a day without silver; an explicit `date` unchanged (nothing served) | WORLD (the handler of both firms' producers) | none | P36b |
| `IB-pr-301` | P-6's server half (CTO batches 201 and 203): submit-export accepts a PATH B (PLATINUM) Performance export under the reporting route's coverage; the bundle pins the series revision (VersionId, sha256, as_of) inside `authorized_report_revisions`; the render reads that exact version; the receipt names the frozen as_of; PATH A exports unchanged (nothing served) | WORLD (the export submit, render and ExportBundle contract; batch 203 named SERVED, the gate's floor for infrastructure paths is WORLD) | none | P36c |

P-2's window (IRPT_DASHBD section 11, E1) waits on IB-pr-301 and on 2.0.0_SA_COO~D's print and export page half (batch 201); one rollback reverts both.

fanout: 3 of 3 chains, cap 8, reason: disjoint write surfaces (the adapter, the producer's handler, the export); workers 0.9.0_WK_IRPT_BCKEND~102, ~103 and ~104 in their own worktrees.


## 29. ROUND 37, WORKSTREAM ~P (2026-10-03 ~05:0xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 205 @a6f6e7165e, msg 104544)

IB-pr-301 (merged @26240fa401) left four rows that block the PATH B export end to end:
- W104-S1: the Enforcer does not admit the reporting route for a render delegate.
- W104-S2: the read role cannot read by VersionId.
- W104-S3: MEASURED; the 49F bucket's DenyForeignFirmPrincipals denies the multi-firm irpt-export-render-role.
- W104-S4: no receipt slot for the frozen as_of.
Batch 205 ruled option (c): read through the 49F reporting route, leave the fence untouched, drop the export role's platinum policy.
GATE (x) puts this in ROUND 37 (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-302` | P-6 export end to end: submit pins (X-Opal-Version-Id, sha256, as_of) through the reporting route; render reads that version and refuses on a sha mismatch; the Enforcer admits reporting-read for a render delegate; reporting-read gains GetObjectVersion on the platinum prefix; the export role's platinum policy dropped; ExportReceipt carries the frozen as_of (nothing served) | WORLD | IB-pr-301 (merged) | P37 |

The census suite (`_authz/tests/test_unguarded_census.py`) fails 6 tests at the base, before DB-b-16 included (measured at
f26fa5fb4d and 00145f3a27). That is row S15, placed by the CTO's rounds 2-9 analysis at the P-2 drain, so this cell grades
"no new failure", not "all pass".

P-2's window (IRPT_DASHBD section 11, E1) waits on IB-pr-302 and on 2.0.0_SA_COO~D's held branch (@c16a31e9, P-3 + P-6 print and
export halves; only the receipt's frozen as_of waits on this cell).

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~105 in its own worktree.


## 30. ROUND 38, WORKSTREAM ~P (2026-10-03 ~05:3xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 207, CTO half @d9f15bc006, msg 104550)

Batch 207 signed the round-36 packet's D2, which is served (@7924f2237a). D1 is re-cut: IB-pr-299's claim `"partial"` grows the
measured/inferred/held/absent vocabulary, so it becomes `"inferred"`, keeping the PARTIAL absence that names the days. Batch 207
also says YES to landing Inflection's three historic gaps (2026-05-11, 06-30, 08-10) as their own packet, after Monday's A1.
GATE (x) puts this in ROUND 38 (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-303` | the adapter's gap claim reads "inferred" (constant, value_facts and result; three test assertions) -- nothing else moves (nothing served) | WORLD | IB-pr-299 (merged) | P38 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~106 in its own worktree.


## 31. ROUND 39, WORKSTREAM ~P (2026-10-03 ~06:1xZ, issuer 2.0.0_SA_COO~P, inside its decomposition)

IB-pr-302 (merged @7d02c6fe8b) landed the Enforcer half of batch 205's route-based export, and filed two rows naming this seat:
- W105-S1: the edge's render branch admits no reporting path.
- W105-S2: the reporting-read function has no render-grant wiring.
Both fail closed. One cell closes both. GATE (x) puts it in ROUND 39 (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-304` | P-6 export end to end: the edge admits the reporting SERIES path for a render token (manifest and summary not); reporting-read gets IRPT_EVIDENCE_BUCKET, a GetObject on the render-grant objects only, and `_render_identity/grant.py` + `report_owner.py` in its package (nothing served) | WORLD | IB-pr-302 (merged) | P39 |

After this cell, P-2's window carries:
- the gold, publish and read deploys;
- the edge publish;
- the export deploy;
- ~D's held branch;
- P-6's retirement of PATH A for 49 Financial.
All are under one never-widen packet with one rollback. IB-pr-302's other notes ride the window as its legs: the export needs the
portal origin reachable and `IRPT_EXPORT_RENDER=on` for the submit's mint.

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~107 in its own worktree.


## 32. ROUND 40, WORKSTREAM ~P (2026-10-03 ~06:3xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 211 @827e6c8bed, msg 104557)

Row W101-S13: the served export download answers `download_route` with `url` and `expires_at`, plus `sha256` and `byte_length`, but
the published response contract forbids them. Batch 211 rules that the contract follows the server, the signed link lives only in
the response, and ExportReceipt is unchanged. It is hygiene, never held for a round. GATE (x) puts this in ROUND 40 (row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-305` | E4: the export-download response contract declares a response-only `download_route` (url https and required, expires_at a date-time and required) and the integrity facts, with a test validating the handler's answer; ExportReceipt byte-unchanged (nothing served) | WORLD (a published contract) | none | P40 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~108 in its own worktree.


## 33. ROUND 41, WORKSTREAM ~P (2026-10-03 ~07:1xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 201 (P-6 option a) and batch 203 (the census accepted))

P-6's backend half had no cell. PATH A (`performance/retained.py`) still composes 49 Financial, and batch 201 retires it WHOLE, in
the same window that PATH B covers every 49F account. The retirement reuses the existing `ProviderPathNotComposed` /
`UNSUPPORTED_OPERATION` refusal through a named subclass: no new reason code, no contract change. GATE (x) puts this in ROUND 41
(row S267).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-306` | P-6: 49F out of COMPOSED_FIRMS; a named `*Retired*` subclass of ProviderPathNotComposed for a fresh request and a retained reopen; Inflection and Cottonwood unchanged; PATH A 49F tests converted (nothing served) | WORLD | none (served only in P-2's window) | P41 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~109 in its own worktree.


## 34. ROUND 42, WORKSTREAM ~P (2026-10-03 ~19:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 226 (S307: fix forward, no window rollback))

The P-2 window's leg V walk (2.0.0_SA_COO~D, msg 104700) found a 49F PATH B export on PROD code refusing DEPENDENCY_UNAVAILABLE.
The edge (V3, :22) admits the render-delegate token on the reporting SERIES route; the API Gateway authorizer (V2) does not --
its RENDER_ROUTE_CLAIMS holds three routes (row S307). Batch 226 rules fix forward: one authorizer cell, served under its own
never-widen half the CTO signs on receipt; leg V closes on the walk after that deploy.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-307` | P-6 (the export): V2 admits a render token on `GET .../reporting/{account_id}/{which}` for which = series only, account_id matched to the token's accountSetId; manifest, summary, a foreign account and forbidden claims refused; the human path byte-unchanged | WORLD | none | P42 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~110 in its own worktree.


## 35. ROUND 43, WORKSTREAM ~P (2026-10-03 ~20:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 229 (S308 re-pointed to ~P))

With S307 fixed, the 49F PATH B export is accepted and frozen, but the render host's `render_export.cjs` allow-list
(`PRINT_QUERY_KEYS`) drops `account` and `version` from the print URL, so the served print page refuses the bundle (row S308;
root cause found by 2.0.0_SA_COO~D, msg 104732). Batch 229: add account, version and request, with a test, under its own half.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-308` | P-6 (the export): the render host forwards the PATH B print query (account, version) and an Analysis print's request; unlisted keys still dropped; the render flow unchanged | WORLD | none | P43 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~111 in its own worktree.

## 36. PRD v0.25 ADDENDUM 25, STEP 5 (2026-10-03 ~21:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO msg 104767 @702845982e) -- NO CELL

Addendum 25 names IRPT_YCDGEN as a consumer of B8's session broker and B16's provider-account operation lease (same lease key,
store and pace). It changes no CONTRACTS row and no ENDPOINT, and nothing served moves, so there is nothing to build: no cell is
cut and no round opens. It binds as a BOUND on every later cell of this project that touches the broker, the lease key or the
pacing: such an order names IRPT_YCDGEN among the readers it must keep working, and its criteria include one that IRPT_YCDGEN's
research run still takes the lease. The issuer inlines that bound at the cut.

## 37. ROUND 44, WORKSTREAM ~P (2026-10-03 ~22:5xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 234 items 1-2, msg 104804)

Batch 234 carries two rows from L10 sweep 7 as ~P cells at this issuance. S264: the source map still records the 09-24 deploys
of three investor-reporting functions; the recorder's `--function` mode has existed since 14346d1f09, so the remedy is one run
per function. S299: three AE roles grant `astn/kimi/api-key-*`; each narrows to `-??????`, then one targeted safe-apply per root
(the issuer's), closing on get-role-policy. No served output moves, so no never-widen half is owed (batch 234).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-309` | S299: the Kimi key ARN narrowed in estate-report, cot-pipeline and bd-49f-auto-login iam.tf; the issuer applies each root | WORLD | none | P44a |
| `IB-pr-310` | S264: the source map records the live CodeSha256 of irpt-ycharts-generate (after irpt-y5v D1, closed 22:12Z), irpt-holdings and irpt-status | WORLD (the gate floor for an infrastructure path; a record only, no served bytes move) | none | P44b |

fanout: 2 of 2 chains, cap 8, reason: two independent cells; workers 0.9.0_WK_IRPT_BCKEND~112 and ~113, each in its own worktree.

## 38. ROUND 45, WORKSTREAM ~P (2026-10-04 ~01:2xZ, issuer 2.0.0_SA_COO~P, on row S293 (owner ~P), CTO batch 234 item 1 and the CVO grade @e73818b94f)

Row S293 is the S264 class on ~P's own functions (CTO batch 234). The source map holds the adapter's 09-24 deploy record and no
deploy record for the 49F holdings-performance producer. It has no row at all for the Inflection producer, which shares that
artifact by design, and it names the 49F role wrongly. The CVO's rounds 42-44 grade re-reads it as open. The remedy is the
row's own: one recorder run per function, the Inflection entry added, the role corrected.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-311` | S293: the source map records what runs for irpt-performance-adapter, irpt-holdings-performance-lambda and irpt-inf-holdings-performance-lambda (new row; the 49F iam_role corrected) | WORLD (the gate floor for the source map; a record only) | none | P45 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~114 in its own worktree.

## 39. ROUND 46, WORKSTREAM ~P (2026-10-04 ~02:2xZ, issuer 2.0.0_SA_COO~P, on row W114-S1 and 1.0.0_SA_CTO msg 104879)

IB-pr-311's amendment 1 carried two steps on row W114-S1, the 49F `iam_role` correction and the Inflection producer's row,
because the naming limb refused them. The CVO's rulings (@7b38f056ca, msg 104877), implemented in the gate @1c3fc41a4d and
@7de9db9085, admit both: a source-map row may cite a builder-minted name, and a `tf_resource` that its `tf_file` declares. The
cell lands the carried steps and records the Inflection function.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-312` | S293 / W114-S1: the 49F producer row names its live role; the irpt-inf-holdings-performance-lambda row is added and recorded at live | WORLD (the gate floor for the source map; a record only) | none | P46 |

fanout: 1 of 1 chains, cap 8, reason: one open cell; worker 0.9.0_WK_IRPT_BCKEND~115 in its own worktree.

## 40. ROUND 47, WORKSTREAM ~P (2026-10-04 ~21:3xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO ROUND ANALYSIS rounds 42-46, msg 104972)

The analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_42_46_P_20261004.md` section 3) makes
this a reconciliation round: E1 reconcile, E2 remedies for what E1 finds live, E3 the recorder for S178's class. The issuer's
census reads 42 ~P remediation rows not closed, by each row's latest copy across REMEDIATION_v1..v19 (388 rows parsed). That
matches the CTO's 42.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-313` | E1: each of the 42 rows' close condition read against live; a closing row for each that holds; the still-live list handed back | LOCAL (read-only) | none | P47a |
| `IB-pr-314` | E3 / S178: the recorder --function for the six lagging investor-reporting functions (irpt-ycharts-generate is ~Y's S320) | WORLD (the gate floor for the source map; a record only) | none | P47b |
| E2 | the live BLOCKING rows IB-pr-313 returns, one remedy cell each (at most three criteria, a never-widen half where served) | by row | IB-pr-313 | cut on E1's return |

fanout: 2 of 2 chains, cap 8, reason: E1 and E3 are independent; E2 depends on E1's output and is cut when it returns. Workers
0.9.0_WK_IRPT_BCKEND~116 (E1) and ~117 (E3), each in its own worktree.

## 41. PRD v0.26 STEP 5 (2026-10-04 ~23:2xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO msg 105024 @c74c8439b3 and the adjudication @a2ed4e681a) -- NO NEW CELL

v0.26 amends FWD-3 in place. It now covers the firms whose page serves the holdings basis: Inflection and Cottonwood. 49F's served
figure is IRPT_DASHBD's flow-adjusted return. IRPT_BCKEND still produces 49F's holdings-basis gold every trading day (FWD-12) as
IRPT_DASHBD's guard rail. No cell is cut, and no open ~P cell served 49F's FWD-3. Two keys bind every order from round 47's E2
on (the adjudication, call 2):
- outcome_ref cites the ratified FWD: export of a branded report FWD-8; a second firm from the global view FWD-11; the Analysis
  export FWD-4; email intake FWD-9.
- A 49F holdings-basis figure on a rendered view or PDF is no longer an outcome; a cell that would add one is refused at the cut.

## 42. ROUND 48, WORKSTREAM ~P (2026-10-04 ~23:5xZ, issuer 2.0.0_SA_COO~P, E2 on E1's LIVE list @db0adf0053 and the CTO adjudication 105022)

E1 (IB-pr-313) returned 17 HOLDS (closed) and 25 LIVE. E2 takes the live BLOCKING rows in E1's order, plus S322 and S324 (CTO).

| cell / act | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-315` | S278: build-and-upload.sh hands the sha by file and asserts the written value | WORLD (infra floor; nothing deployed) | none | P48a |
| `IB-pr-316` | S322 + S178's remainder: the three stale reporting rows re-keyed to the live irpt-49f-* names and recorded | WORLD (source-map floor; a record) | none | P48b |
| S272 (issuer act) | one signed-in download of EXP-e29b5415.. through its receipt link, the PDF sha read against the receipt | SERVED read | the UI-walker account (ARM via 0.0.0_AB_MSTR) | issuer |
| W101-S1/S2/S4/S5, W101-S11 | E4 (IB-pr-282): one served Analysis export of a prospect-owned report | WORLD | IB-pr-282's state, read next tick | issuer |
| W100-S2 | the 49F perfrp leaf: re-emit without 2025-01-10, or withdraw under a never-widen half (an S3 delete is Andrew's word) | SERVED | 1.0.0_SA_CTO's choice | asked |
| S324 | the PATH B export's narrative ref, or the v0.24 contract amended by name | SERVED | 1.0.0_SA_CTO's choice (irpt-narrative idle since 09-20) | asked |

The rest of E1's LIVE list is not BLOCKING, and it is batched as ONE repair cell at the next issuance, per the spine's "repairs
batched into ONE cell": S220, S204, S218, W80-S1, S260, S241, S282, S297, S298, W101-S14, W101-S16, W62-S1, S175, S180, S252 and W69-S1.

fanout: 2 of 2 chains, cap 8, reason: two independent build cells now; S272 and E4 are the issuer's acts; W100-S2 and S324 are
asked. Workers 0.9.0_WK_IRPT_BCKEND~118 and ~119, each in its own worktree.

## 43. ROUND 49, WORKSTREAM ~P (2026-10-05 ~00:5xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 247 and PRD v0.27 @06ad58d478)

Batch 247 answers E2's two forks.
- S324 is accepted, narrowed: v0.27 ruling 28 gives a PATH B performance export `narrative_state: NOT_ATTACHED` with its reason.
- W100-S2 is not withdrawn under IRPT_BCKEND. One readers census is owed first: no reader re-points the row to ADVI_PERFRP inert;
  a live reader brings a never-widen packet back to the CTO.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-317` | S324: PATH B bundles carry narrative_state NOT_ATTACHED + reason; the ExportBundle schema requires it on the PLATINUM branch | WORLD (served Lambda code; the deploy is the issuer's, under a never-widen half) | none | P49a |
| `IB-pr-318` | W100-S2: one read-only readers census of the 49F perfrp leaf (CloudFront, routes, portal PROD) | LOCAL (read-only) | none | P49b |

fanout: 2 of 2 chains, cap 8, reason: two independent cells. Workers 0.9.0_WK_IRPT_BCKEND~120 and ~121, each in its own worktree.

## 44. ROUND 50, WORKSTREAM ~P (2026-10-05 ~01:5xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 251 @8ea5889048, msg 105089)

The W100-S2 census (IB-pr-318, drained @0f69381e7c) read LIVE_READER: the PROD portal's AdvisorBookView still loads the 49F perfrp
leaf through shared-advisor-router. Row W121-S1 is BLOCKING / ARMED. Batch 251 rules: withdraw the leaf and keep the portal's call,
since its 404 is the designed shell state. The never-widen packet goes to the CTO, and the S3 delete is Andrew's.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-319` | W121-S1: the withdrawal packet (versioning, every perfrp key under platinum/advi/*/ with its writer and its 2025-01-10 measurement, the withdrawal set, rollback per key, ETag stop, PROD after-read) | LOCAL (reads only) | IB-pr-318 (merged) | P50 |
| (the act) | the withdrawal under the CTO half and Andrew's word, then the after-read; W121-S1 disarms on the after-read | SERVED | IB-pr-319 | the issuer's act |

fanout: 1 of 1 chains, cap 8, reason: one read-only cell; the delete is a signed act. Worker 0.9.0_WK_IRPT_BCKEND~122 in its own worktree.

## 45. ROUND 51, WORKSTREAM ~P (2026-10-05 ~03:1xZ, issuer 2.0.0_SA_COO~P, the batched remainder of section 42)

A read-only sweep of E1's 16 non-BLOCKING remainder rows found all 16 still open. They sort into three groups:
- **Eight are LOCAL code or test repairs:** S220, S282, W62-S1, S241, S297, S298, W101-S14, W101-S16. Per the spine, they are ONE repair cell.
- **Five wait on a ruling or a read:**
  - W80-S1 is a CTO ruling, asked 03:01Z and due before the INF fire at 14:00Z.
  - S260 and S175 need a CTO reason-code vocabulary, then a served release.
  - S218 needs an SSM journal read, then a CTO allowance ruling.
  - S252 needs an S3 read.
- **Three are records:** S204 is the issuer's ledger record; S180 is disposed with S260; W69-S1 is 0.0.0_AB_MSTR's worktree provisioning.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-320` | the eight LOCAL remainder rows, each fixed with a test naming it | WORLD (code under infra/; deploys are the issuer's) | none | P51 |
| (the issuer) | the served releases of S241, S297, S298 and W101-S14 under never-widen halves; the S218 and S252 reads; the S204, S180 and W69-S1 records | SERVED | IB-pr-320 (for releases) | the issuer's acts |

fanout: 1 of 1 chains, cap 8, reason: one repair cell; the rulings and reads are the issuer's. Worker 0.9.0_WK_IRPT_BCKEND~123 in its own worktree.

## 46. ROUND 52, WORKSTREAM ~P (2026-10-05 ~05:0xZ, issuer 2.0.0_SA_COO~P, on 1.0.0_SA_CTO RULINGS batch 253 @35e313ec06)

IB-pr-320 merged @f9e1c4ab96. The S260 and S175 reason codes now go to the same `_authz` surface:
- BucketUnmapped -> FIRM_BINDING;
- MaintainedSourceRefused is split by class (NOT_AUTHORIZED, NOT_READY, INVALID_INPUT) into subclasses that declare their code,
  with no message branching.

Batch 253 numbered ten raise sites, but the file holds about 50, so the cell classifies every site by the ruled classes and rows
any site that fits none. W100-S2 closed this round: CTO batch 256, ledger closed @752ffa138a, W121-S1 disarmed by S331.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-321` | S260, S175 (and the S180 read): declared reason codes, the raise-site census, tests | WORLD (code under infra/; deploys are the issuer's) | IB-pr-320 (merged) | P52 |
| (the issuer) | ONE release round for IB-pr-320 + IB-pr-321 code under never-widen halves: authz consumers, holdings-performance x2, performance, export, irpt-ycharts-generate | SERVED | IB-pr-321 | the issuer's acts |

fanout: 1 of 1 chains, cap 8, reason: one code cell on a single write surface. Worker 0.9.0_WK_IRPT_BCKEND~124 in its own worktree.

## 47. ROUND 53, WORKSTREAM ~P (2026-10-05 ~06:0xZ, issuer 2.0.0_SA_COO~P, on rows W124-S1 and W124-S2 under CTO batch 253's class rule)

IB-pr-321 merged @0fff3d8363: 46 sites were classified and UNEXPECTED went from 46 to 0 in maintained_sources.py. Its worker
found two remainders, ruled here by the issuer under batch 253's class rule (no new code and no vocabulary change):
- W124-S1: 25 bare raises in canonical_profile_reads.py and retained_input_authorizer.py;
- W124-S2: opaque_firm_for answers FIRM_BINDING for a malformed server artifact, which is NOT_READY by the class rule.

S218 was disarmed by S333 (3 of 3 live-build READY jobs spent no session_refresh). S204 was disarmed by S332 (ledger 49f-r3
closed SUPERSEDED).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-322` | W124-S1, W124-S2: the remaining refusal codes, a census, tests | WORLD (code under infra/; deploys are the issuer's) | IB-pr-321 (merged) | P53 |

fanout: 1 of 1 chains, cap 8, reason: one code cell on the same write surface. Worker 0.9.0_WK_IRPT_BCKEND~125 in its own worktree.

## 48. ROUND 54, WORKSTREAM ~P (2026-10-05 ~06:4xZ, issuer 2.0.0_SA_COO~P, on the CTO half for release r54 @f342ba6664)

IB-pr-322 is merged @23f867773a. The r54 release plan (@07d113a19c) covers 10 functions. The CTO half is signed with four
conditions; condition 2 is a per-function census of the built zip against the live bundle, with every change attributed or the
function dropped as a rider. 2.0.0_SA_COO~Y answered that HEAD is shippable for irpt-status and irpt-ycharts-generate (msg 105192).
build-and-upload.sh has no build-only mode, so the census cannot run before an upload. One tooling cell first.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-323` | CTO condition 2: BUILD_ONLY in build-and-upload.sh + release_census.py (built vs live, attributed or RIDER) | WORLD (script under infra/; no upload) | none | P54 |
| (the release) | 10 functions under both halves: before-read stop, census, build+upload, targeted safe-apply, record, change invoke + happy-path invoke, per-function legs | SERVED | IB-pr-323 | the issuer's acts |

fanout: 1 of 1 chains, cap 8, reason: one tooling cell; the release is the issuer's. Worker 0.9.0_WK_IRPT_BCKEND~126 in its own worktree.

## 49. ROUND 56, WORKSTREAM ~P (2026-10-05 ~12:1xZ, issuer 2.0.0_SA_COO~P, on CTO batch 260 @7bd2946ccd)

Release r54 shipped irpt-holdings-performance-lambda (handler.py, IB-pr-320). V2 proved TARGET_ALREADY_LANDED live after the 11:30Z
landing; A2 (INF) follows the 14:00Z fire. The rest of rounds 49-53's code reaches no served function through the staged_from pins.
The r55 re-pin plan (REPIN_PLAN_R55.json @db3b9632d3; CTO count 26 CLEAN / 10 RIDER of 36) is approved as proposed, with three
conditions: an import smoke per function, the census attribution rule, and irpt-status stays in ~Y's lane. The issuer computed the
plan itself: on disk 3.4 GB, no worktree fit.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-324` | the approved re-pin set in the source map + BUILD_ONLY census + import smoke per function | WORLD (carrier edit under infra/; no upload) | IB-pr-323 (merged) | P56 |
| (the release) | a never-widen plan for halves on the census-clean functions | SERVED | IB-pr-324 | the issuer's act |

fanout: 1 of 1 chains, cap 8, reason: one carrier edit. Worker 0.9.0_WK_IRPT_BCKEND~127 in its own worktree.

## 50. ROUND 57, WORKSTREAM ~P (2026-10-05 ~15:1xZ, issuer 2.0.0_SA_COO~P, on CTO batch 264 @f49b5958b0, row S335)

The 13:30Z directory refresh failed at all three firms again after the runner restart (S335): it starts the host and ends, and the next
fire is a day later. Batch 264 rules a second schedule 10 minutes later, plus a never-widen packet for the first successful fire, which
replaces three latest.json keys frozen at 09-25. Round 56 (IB-pr-324) drained @f36a8cdefd. Release r57's halves are signed (CTO
@3d6e1ed58c, COO @e860151215), and its deploys follow the invoke-payload prep.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-325` | S335: the 09:40 ET retry schedule + the latest.json never-widen packet | WORLD (Terraform under infra/; the apply is the issuer's after both halves) | none | P57 |

fanout: 1 of 1 chains, cap 8, reason: one schedule edit + packet. Worker 0.9.0_WK_IRPT_BCKEND~128 in its own worktree.

## 51. ROUND 58, WORKSTREAM ~P (2026-10-06T00:19Z, issuer 2.0.0_SA_COO~P, on CTO batch 265 @aee5b1d269 item 2, release r57 served)

Release r57 is served on four functions (ledger closed @7091e7b1d9). Its first finding: the guarded path's enforcer_for call site
(`_authz/served.py:1050-1054`) hard-codes the public code, so the classes IB-pr-321/322 declared (BucketUnmapped FIRM_BINDING,
FirmArtifactIncomplete NOT_READY) reach only the log record's classifier_code, never the wire. Batch 265 item 2 names the wire fix as this
seat's cell; its release changes a served public_reason_code and takes its own never-widen half (batch 253 stays the target).

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-326` | the refusal classes at the enforcer_for call site reach the wire (S260/W124-S2 class rule, batch 253) | WORLD (code under infra/aws/lambda; the order applies nothing, the build and apply are the issuer's after both halves) | none | P58 |

fanout: 1 of 1 chains, cap 8, reason: one call-site edit plus its tests. Worker 0.9.0_WK_IRPT_BCKEND~129 in its own worktree.

## 52. ROUND 59, WORKSTREAM ~P (2026-10-06T00:55Z, issuer 2.0.0_SA_COO~P, on CTO batch 271 and the r58 CTO half @38fbca18a2 condition 1)

IB-pr-326 drained @abf14e56ba. The r58 packet @c847d5fceb found that `_authz/loaders.py:204` (`pointer["key"]`) is a KeyError that
`errors.reason_for` maps to NOT_FOUND once the call site classifies, so a broken server-side pointer would read as a client fault. Batch 271
item 2: a server fault gets a declared class in the same release. The CTO half is signed on the packet, 327 before 328.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-327` | a latest.json pointer that is not a dict or has no non-empty `key` raises FirmArtifactIncomplete (NOT_READY) | WORLD (code under infra/aws/lambda; applies nothing, the re-pin cell IB-pr-328 and the release follow) | none | P59 |

fanout: 1 of 1 chains, cap 8, reason: one guard plus its tests. Worker 0.9.0_WK_IRPT_BCKEND~130 in its own worktree.

## 53. ROUND 60, WORKSTREAM ~P (2026-10-06T01:10Z, issuer 2.0.0_SA_COO~P, on the r58 CTO half @38fbca18a2 condition 1)

IB-pr-327 drained @d8d8e7d868. Every function stages `_authz/served.py` and `_authz/loaders.py` from a per-member pin in
`infra/aws/lambda/ci/lambda-source-map.json` (`staged_from[].pin` + `sha256`), so IB-pr-326 and IB-pr-327 ship only when those pins move
(the IB-pr-324 pattern). This cell moves them, for the four functions this seat releases, to the merged blobs. The changed-member census, the
builds and the applies follow under the CTO half; for `irpt-directory-search` and `irpt-holdings` the census diff goes to the CTO first.

| cell | serves | risk | depends on | chain |
|---|---|---|---|---|
| `IB-pr-328` | the served.py and loaders.py staged_from pins of reporting-read, export-render, directory-search, holdings -> d8d8e7d868 | WORLD (the source map is the build input of four served functions; the order applies nothing) | IB-pr-327 (drained) | P60 |

fanout: 1 of 1 chains, cap 8, reason: one source-map edit, eight members. Worker 0.9.0_WK_IRPT_BCKEND~131 in its own worktree.

## 54. ROUND 61, WORKSTREAM ~P (2026-10-07 ~09:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO round analysis @e363a194ed section 5)

The rectangle is the analysis's ENRICHMENT LIST for ~P, E-P1..E-P7, one cell per item. Rounds 47-60 were repair and release rounds and
moved no outcome; these cells aim at FWD-2, FWD-3 (INF export, via the adapter build) and FWD-7, plus the four record/tooling rows.
Write sets are disjoint per cell: only IB-pr-334 edits `lambda-source-map.json` (the irpt-directory-search row); IB-pr-329 changes the
builder only; IB-pr-332 moves the adapter's three build-only modules out of the scanned top level and does not touch the map.
Checks: `deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py`, every one dry-run at base 6e462d3499.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-329` | E-P1 one S3 key per function (S343) | the builder uploads to the map's artifact_s3_key | WORLD (floor: infra/ path; analysis class LOCAL) | none | P61-a |
| `IB-pr-330` | E-P2 the deploy recorder stages only its own paths (S344) | release records | WORLD (floor: infra/ path; analysis class LOCAL) | none | P61-b |
| `IB-pr-331` | E-P3 the release census is the issuer's own build against live (S337 census half) | release tooling | WORLD (floor: infra/ path; analysis class LOCAL) | none | P61-c |
| `IB-pr-332` | E-P4 the adapter builds (W127-S1) | FWD-3 (INF export needs an adapter build) | WORLD (floor: infra/ path; analysis class LOCAL) | none | P61-d |
| `IB-pr-333` | E-P5 the refresh manifest records the fire that ran (S348) | FWD-7 | WORLD (floor: infra/ path; analysis class SERVED; the release and the driven fire are the issuer's under its half) | none | P61-e |
| `IB-pr-334` | E-P6 FWD-7 on current bytes: the search serves the over-age branch | FWD-7 | WORLD (code + the map row; release, the five-arm live drive and both halves are the issuer's) | IB-pr-333 (one release packet) | P61-e |
| `IB-pr-335` | E-P7 FWD-2 replay on current bytes | FWD-2 | SERVED (read-only replay against the live API) | none | P61-f |

fanout: 6 of 6 chains, cap 8, reason: five independent cells plus the E-P5 -> E-P6 queue that ships as one directory release packet. Slots 0.9.0_WK_IRPT_BCKEND~132..137, one worktree each; ~136 holds IB-pr-333 then IB-pr-334.

## 55. ROUND 62, WORKSTREAM ~P (2026-10-07 ~10:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO round-61 analysis @aae1ed7781 section 3 and the r61 directory release CTO half @74e91285b4)

The rectangle is the analysis's ENRICHMENT LIST for ~P (E-P8, E-P9, E-P10; E-P11 is the issuer's own disarm row, filed in this
issuance, not a cell) plus the two preconditions the r61 directory release's CTO half sets (the handler.py pin; the two-instrument consumer
census). Write sets are disjoint: only IB-pr-337 edits lambda-source-map.json; IB-pr-336 owns export/ and the render host; IB-pr-338 adds
tests only; IB-pr-339 owns _ids/. Checks: `deliverables/2.0.0_SA_COO~P2/checks/r62/p62_cells.py`, every one dry-run at base bc794d2770.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-336` | E-P9 the export takes a client report (a1 submit, a3 render host + unknown-template refusal, a4 print package) | IRPT_CUSTDY hop 5; export integrity | WORLD (floor: infra/; analysis class LOCAL) | none | P62-a |
| `IB-pr-337` | r61 release precondition: refresh stages handler.py from the running blob (S357) | FWD-7 (the directory release) | WORLD (floor: infra/) | none | P62-b |
| `IB-pr-338` | r61 release precondition P1: every reader of the search response passes on plain and over-age (W136-S1) | FWD-7 (the directory release) | WORLD (floor: an infra/ test path) | none | P62-c |
| `IB-pr-339` | E-P8 the seam holds no 'None'; ids.py treats 'None'/'nan' as unmapped; the writer named (IRPT_CUSTDY W5-S1) | FWD-1/FWD-2 coverage; IRPT_CUSTDY E1 gate | WORLD (floor: infra/; analysis class LOCAL) | none | P62-d |
| `IB-pr-340` | E-P10 one fixture per gated route (W137-S1) | FWD-2 | SERVED | none | P62-e |

fanout: 5 of 5 chains, cap 8, reason: five independent cells; the analysis's "fan-out 3" counts E-P8..E-P10, and the two release preconditions are this issuer's addition under the CTO half. Slots 0.9.0_WK_IRPT_BCKEND~138..142; portal_ref: 8ddfe409 (portal DEV at the cut) for ~138 and ~140.

## 56. ROUND 63, WORKSTREAM ~P (2026-10-07 ~10:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on 1.0.0_SA_CTO~DELL2 ruling msg 337)

IB-pr-338 (round 62) found 5 of 7 readers of the search response failing on the over-age envelope, so the r61 directory release HOLDS on
its CTO half's P1. Ruling msg 337: the 4 portal failures are the server's defect (a server-only `internal_correlation_id` in the over-age
`_status`); the IRPT_CUSTDY reader reads directory.json and is outside the census's population (W140-S2). One cell; round 62 already has
orders at HEAD, so it is round 63. Check: `deliverables/2.0.0_SA_COO~P2/checks/r63/p63_cells.py`, dry-run at base 1758606f46.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-341` | the over-age status carries only public members; the 4 portal reader tests pass (W140-S1) | FWD-7 (the r61 directory release, P1) | WORLD (floor: infra/) | IB-pr-334, IB-pr-338 (drained) | P63-a |

fanout: 1 of 1 chains, cap 8, reason: one ruled cell. Slot 0.9.0_WK_IRPT_BCKEND~143; portal_ref: d53a7a0f (portal branch wk-IRPT_BCKEND-140-portal, IB-pr-338's reader tests).

## 57. ROUND 64, WORKSTREAM ~P (2026-10-07 ~10:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the IRPT_CUSTDY round-3 analysis @ec25e39844 S8(b), msg 383)

One measurement cell routed to this workstream: which of the 7,022 granted accounts are NOT_IN_DIRECTORY (1,961 per IRPT_CUSTDY's run) and
why each is absent. Read-only; the firm-bucket fence now admits dell2 on 49financial and inflection (cottonwood still denied). Check:
`deliverables/2.0.0_SA_COO~P2/checks/r64/p64_cells.py`, dry-run at base 33949e002d.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-342` | directory-coverage census of the NOT_IN_DIRECTORY granted accounts, reason per account | FWD-1/FWD-7 directory coverage; IRPT_CUSTDY S8(b) | SERVED (read-only against served data) | none | P64-a |

fanout: 1 of 1 chains, cap 8, reason: one measurement cell. Slot 0.9.0_WK_IRPT_BCKEND~144.

## 58. ROUND 65, WORKSTREAM ~P (2026-10-07 ~11:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on 1.0.0_SA_CTO~DELL2 PRIORITY msg 439, PRD v0.30 @f20371eb03 items 33-36)

Row W142-S4 is ARMED: export reads FAIL OPEN (`export/entry.py` `_covered` admits any holder of an export id when the receipt names no
account). The CTO orders three items ahead of every other round-65 cell. Checks: `deliverables/2.0.0_SA_COO~P2/checks/r65/p65_cells.py`,
dry-run at base 31b26bff2d.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-343` | (1) receipt names covered_account_ids at freeze; `_covered` REFUSES an empty list; both schema copies require it | FWD-2 | WORLD (floor: infra/) | none | P65-a |
| `IB-pr-344` | (2) back-fill tool + DRY-RUN census (read / filled / unfillable); the apply is the issuer's under a never-widen pair | FWD-2 | WORLD (floor: infra/) | IB-pr-343 | P65-a |
| `IB-pr-345` | (3) exposure: read-log census of cross-scope export reads while the branch was served | FWD-2 | SERVED (read-only) | none | P65-b |

fanout: 2 of 2 chains, cap 8, reason: (1) then (2) share the field and its derivation (one worker's queue); (3) is independent. Slots 0.9.0_WK_IRPT_BCKEND~145 (343 then 344) and ~146.

## 59. ROUND 66, WORKSTREAM ~P (2026-10-07 ~12:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO review msg 403 and the dell2 portal toolchain going live, msg 472)

The PrintEntry custody-report candidate (@cdda4378, IB-pr-336's portal half) was reviewed LAND-WITH-NOTE: typecheck + eslint + one 0-request
refusal test before DEV, and readReportKind must refuse an unknown kind. Both are one file on the page, so one cell. Row S365 disarms when
it lands. Check: `deliverables/2.0.0_SA_COO~P2/checks/r66/p66_cells.py`, dry-run at base fd0c709235 (AC1 FAIL; AC2 is a control, PASS).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-346` | print page refuses an unknown kind; the custody-report candidate's typecheck, eslint, refusal test | FWD-8/FWD-4; IRPT_CUSTDY hop 5 | WORLD (a portal product file) | IB-pr-336 (drained) | P66-a |

fanout: 1 of 1 chains, cap 8, reason: one page file. Slot 0.9.0_WK_IRPT_BCKEND~147; portal_ref: cdda4378 (branch wk-IRPT_BCKEND-138-portal).

## 60. ROUND 67, WORKSTREAM ~P (2026-10-07 ~12:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 525 and the IRPT_CUSTDY round-4 analysis @16d9b128c0, msg 512)

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-347` | who can reach the fail-open export read NOW (non-Opal principals with a firm grant on the export routes); decides kit-wait vs an emergency apply | FWD-2 (W142-S4 / W146-S1) | SERVED (read-only) | none | P67-a |
| `IB-pr-348` | E-P8 criterion 4: the seam guard treats every spelling of none/nan/null as unmapped | FWD-1/FWD-2 coverage | WORLD (floor: infra/) | IB-pr-339 (drained) | P67-b |

fanout: 2 of 2 chains, cap 8, reason: two independent cells. Slots 0.9.0_WK_IRPT_BCKEND~148, ~149. Check: `deliverables/2.0.0_SA_COO~P2/checks/r67/p67_cells.py`, dry-run at base 8d7577866e.

## 61. ROUND 68, WORKSTREAM ~P (2026-10-07 ~13:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 590 / half amendment 1 @4493cf1800 and MSTR ruling 106243, msg 589)

IB-pr-347 measured non_opal_reach = 7, so under the CTO's msg 525 this is a security exception: a laptop applier releases IB-pr-343 BY HASH.
The source map staged export/entry.py at 0642c9d004, so a build at 34f71024a1 omitted the fix (COO half refused @477f0faa28). The re-pin
is @b921635dad, whose census is exactly nine members; both halves are signed against it. Check: `deliverables/2.0.0_SA_COO~P2/checks/r68/p68_cells.py`.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-349` | EMERGENCY release of irpt-export-render at pin b921635dad (fail-closed export read + admitted-read log), laptop applier, with after-reads | FWD-2 (W142-S4 / W146-S1 / W148-S1) | WORLD (a deploy) | IB-pr-343 (drained), IB-pr-347 (drained) | P68-a |

fanout: 1 of 1 chains, cap 8, reason: one function, one release. Applier 0.7.0_AE_CloudOps~I (laptop seat, MSTR ruling 106243), not a worker slot.

## 62. ROUND 69, WORKSTREAM ~P (2026-10-07 ~13:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO half of IB-pr-343's emergency release, msg 576)

IB-pr-349 makes every receipt that names no account unreadable. The back-fill (PRD v0.30 item 35) fills the receipts written before
IB-pr-343. IB-pr-344's dry run listed 1 receipt, which dell2 could not decrypt (W145-S5), so the census and the apply run on the laptop
applier under their own pair. Check: `deliverables/2.0.0_SA_COO~P2/checks/r69/p69_cells.py`.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-350` | back-fill covered_account_ids into pre-343 receipts: pass 1 census + packet (stop at halves), pass 2 apply + after-reads | FWD-2 | WORLD (an S3 write) | IB-pr-349, IB-pr-344 (drained) | P68-a (queued after IB-pr-349) |

fanout: 1 of 1 chains, cap 8, reason: one write set, queued behind IB-pr-349 on the same applier.

## 63. ROUND 70, WORKSTREAM ~P (2026-10-07 ~17:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's IRPT_CUSTDY round-6 ADDENDUM 1 @c3addc6f25 ruling item 2, cut now on msg 917)

Hop 5 of IRPT_CUSTDY (the custody report export) breaks at five points (IRPT_CUSTDY-S14). Breaks 1, 2 and 4 are this workstream's.
Round 70 runs concurrently with round 69 (IB-pr-350) under the one issuer. The write sets are disjoint: IB-pr-350 rewrites S3 receipts
with a tool and changes no code. Check: `deliverables/2.0.0_SA_COO~P2/checks/r70/p70_cells.py`, dry-run at base c09237491c.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-351` | P-c1: custody write path (`reports/custody_write.py`) over `ReportRepository.persist`, round-tripped through `retained_export.resolve` | FWD-8 / CUSTDY hop 5 | WORLD (floor: infra/; no deploy until its release pair) | none | P70-a |
| `IB-pr-352` | P-c2: `submit_async.accept` reads the business date by kind | FWD-8 / CUSTDY hop 5 | WORLD (floor: infra/; no deploy until its release pair) | none | P70-b |
| `IB-pr-353` | P-c3: `PrintEntry` admits custody-report and mounts `ClientReportDocument` | FWD-8 / CUSTDY hop 5 | LOCAL (portal DEV; PROD is Andrew's word, break 5) | none | P70-c |

fanout: 3 of 3 chains, cap 8, reason: three disjoint write sets. Slots 0.9.0_WK_IRPT_BCKEND~160, ~161, ~162 (AMENDMENT 1: re-slotted from ~150/~151/~152, which ~Y and ~M orders already hold); portal_ref: 339851c7 (portal origin DEV).

## 64. ROUND 71, WORKSTREAM ~P (2026-10-07 ~18:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 945 on 2.0.0_SA_COO~Y2 msg 942, row W152-S1)

IB-yr-631 (~Y) made uploads.py admit an internal filer on behalf of a firm its allowedFirmIds names. But InteractiveAccess.current()
carries no allowedFirmIds, and authorize_current requires principal == current(), so the admit is unreachable in production. ALL never
admits (ruling (2)). Y's X-1 release waits on this cell; both ship under one pair. Check: `deliverables/2.0.0_SA_COO~P2/checks/r71/p71_cells.py`,
dry-run at base 6115baf2e7.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-354` | current() carries allowedFirmIds for an OPAL_GLOBAL subject; on-behalf admitted only on an explicit firm; ALL, an unlisted firm, a non-internal principal and a missing value refused | TCKT_VNEXT FWD-1 via intake | WORLD (floor: infra/; no deploy until the shared pair) | IB-yr-631 (drained) | P71-a |

fanout: 1 of 1 chains, cap 8, reason: one file. Slot 0.9.0_WK_IRPT_BCKEND~163 (census: max used 162).

## 65. ROUND 72, WORKSTREAM ~P (2026-10-07 ~19:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO rulings msg 973 (row W162-S1, option (a)) and msg 998 (row IRPT_YCDGEN-S16), and the issuer's ruling on row W163-S1)

IB-pr-353 stopped: the bundle carries only custody_report_ref and no route reads a retained CUSTODY_REPORT. The CTO ruled a scoped GET
reusing retained_export.resolve. IB-pr-355 serves it and IB-pr-356 consumes it, both built to one contract stated in their faces.
IB-pr-356 supersedes IB-pr-353.

IB-pr-357 is the F1 stop: response_envelope leaks internal_correlation_id. IB-pr-358 wires IB-pr-354's profile reader into the
analysis-input-upload constructor (row W163-S1). Both may write _authz/served.py, so they are one chain on one slot.

Check: `deliverables/2.0.0_SA_COO~P2/checks/r72/p72_cells.py`, dry-run at base 0d2aff87b3.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-355` | GET custody-report/{reportId} (custody-report-read, irpt-export-render), authorized by retained_export.resolve; routes.json row | FWD-8 / CUSTDY hop 5 | WORLD (a route; release under a pair naming the route and every principal class) | IB-pr-351 (drained) | P72-a |
| `IB-pr-356` | client op + manifest + resolveBundle + PrintEntry mount ClientReportDocument; supersedes IB-pr-353 | FWD-8 / CUSTDY hop 5 | LOCAL (portal DEV; PROD is Andrew's word) | the contract (none at build) | P72-b |
| `IB-pr-357` | response_envelope drops internal_correlation_id from every status | IRPT_YCDGEN F1 | WORLD (every success route using response_envelope) | none | P72-c |
| `IB-pr-358` | the analysis-input-upload constructor passes the existing profile reader | TCKT_VNEXT X-1 | WORLD (floor: infra/; ships with Y's X-1 pair) | IB-pr-354 (drained), IB-pr-357 (same file) | P72-c |

fanout: 3 of 3 chains, cap 8, reason: 355 and 356 are joined only by the stated contract, so they build in parallel; 357 then 358 share _authz/served.py on one queue. Slots ~164, ~165, ~166 (P block 160-199); portal_ref: portal origin DEV at the cut.

## 66. ROUND 73, WORKSTREAM ~P (2026-10-07 ~22:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO review msg 1113 of IB-pr-356 portal b3fedfea)

The CTO passed IB-pr-356 for DEV on two conditions. W165-S2 (ARMED: the wire-generator tests rewrite 25 tracked contracts/wire files)
must be disarmed before the DEV push. W165-S1 (the custody read sits outside parseIrEnvelope) must close before PROD. Both are portal
test or validation edits on one branch stacked on b3fedfea, so they are one cell. Check: `deliverables/2.0.0_SA_COO~P2/checks/r73/p73_cells.py`,
dry-run in worktree ~167 at portal b3fedfea.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-359` | generator tests write to temp, never tracked contracts/wire; the custody read passes a named envelope validation | FWD-8 / CUSTDY hop 5 | LOCAL (portal) | IB-pr-356 (portal b3fedfea) | P73-a |

fanout: 1 of 1 chains, cap 8, reason: one portal branch. Slot ~167; portal_ref: b3fedfea (IB-pr-356's commit).

## 67. ROUND 74, WORKSTREAM ~P (2026-10-08 ~01:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on row S381)

The export build's ADHC_DRIFTD.002 parity limb flags IB-pr-344's operator tool, which sits in the export source dir unregistered, so
every irpt-export-render build since needs BAU_PARITY_SKIP=1. The tool moves to export/tools/, outside the limb's top-level scope; no
packaged member and no build script changes. Check: `deliverables/2.0.0_SA_COO~P2/checks/r74/p74_cells.py`.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-360` | the back-fill tool moves to export/tools/; the parity rule finds 0 extras; its tests pass | FWD-2 / FWD-8 releases | WORLD (floor: infra/; the deployed zip is unchanged) | none | P74-a |

fanout: 1 of 1 chains, cap 8, reason: one file move. Slot ~168.

## 68. ROUND 75, WORKSTREAM ~P (2026-10-08 ~03:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on row S388 after the owner split)

One regeneration of the portal wire types on DEV d1b21c97 changes 6 files. Four are ~P's: ExportBundle (IB-pr-336), ExportReceipt
(IB-pr-343), and responses/index (the route table, IB-pr-355). AnalysisReport is IRPT_YCDGEN's (~G2 owns it, msg 1188) and
HoldingsSnapshot is MDPF_SECCLASS's (relayed to dell1 via ~M2). This cell regenerates ~P's four from their contracts and restores
the rest. Check: `deliverables/2.0.0_SA_COO~P2/checks/r75/p75_cells.py`, dry-run in worktree ~169 at portal DEV d1b21c97.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-361` | regenerate ExportBundle, ExportReceipt, responses, index from their contracts; nothing else | FWD-2 / FWD-8 | LOCAL (portal) | none | P75-a |

fanout: 1 of 1 chains, cap 8, reason: one regeneration. Slot ~169; portal_ref: d1b21c97 (portal origin DEV).

## 69. ROUND 76, WORKSTREAM ~P (2026-10-08 ~05:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's rounds 69-74 analysis @b35c7d8c73, msg 1214)

The CTO's enrichment list names two items, which the CTO numbers "round 75". Round 75 already holds IB-pr-361, so they are cut here
as round 76, ONE issuance. E1: the four ARMED rows disarmed or re-justified. E2: the custody release packet, as one release pair; the
packet only, nothing applied. The PROD print promote follows E2 on Andrew's word. Check: `deliverables/2.0.0_SA_COO~P2/checks/r76/p76_cells.py`.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-362` | E1: S334, W140-S1, W145-S2, W165-S2 disarmed with evidence, or ARMED with the one disarm act and its owner | round-close hygiene | LOCAL | none | P76-a |
| `IB-pr-363` | E2: the custody release packet (census at one pin, every member owned, both branches, rollback per function, after-reads) | FWD-8 / CUSTDY hop 5 | WORLD (floor: infra/; the packet only, nothing applied) | IB-pr-351/352/355/356/359 (drained) | P76-b |

fanout: 2 of 2 chains, cap 8, reason: disjoint write sets (E1: rows + its deliverable; E2: a possible source-map re-pin + its deliverables). Slots ~170, ~171.

## 70. ROUND 77, WORKSTREAM ~P (2026-10-08 ~17:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on both never-widen halves of IB-pr-363: COO half @7a5f0d2fb7, CTO half @652141d7cc, msg 1314 "the release order is yours to cut")

The custody release pair at pin 1e0cdaf90c, applied from dell2 (step C applied 12:39:33Z, msgs 1288/1297; irpt-export-render is not one
of the ten protected functions in `infra/aws/terraform/nfra-ctlpln-identity/protected_functions.json`; no firm bucket, state-bucket
config, shared key or assets bucket is changed, so the before-rule does not bind and the act is reported after). Function first,
then the one route. Check: `deliverables/2.0.0_SA_COO~P2/checks/r77/p77_cells.py`, dry-run at base 0c9d22dbd1 (both FAIL, no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-364` | release irpt-export-render at 1e0cdaf90c (3 members), then apply the custody-report-read route; after-reads per both halves | FWD-8 / CUSTDY hop 5 | WORLD | IB-pr-363 (drained @7a5f0d2fb7) | P77-a |

fanout: 1 of 1 chains, cap 8, reason: one release pair, ordered acts. Slot ~172.

## 71. ROUND 78, WORKSTREAM ~P (2026-10-08 ~17:5xZ, issuer 2.0.0_SA_COO~P2, on the CTO analysis ADDENDUM 1 @e4ad79e976, msg 1344: E4)

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-365` | E4: bound comp-tagauthz's IAM read (timeout failing CLOSED with a named reason, or a narrower read); disarm S334. Commit lane `GIT_COMMIT_AUTHOR_OVERRIDE=0.5.0_AE_OpalETL` naming msg 1342 | release hygiene (S334) | LOCAL | none | P78-a |

fanout: 1 of 1 chains, cap 8, reason: one tool file + one row (round 77 holds the release; ONE ISSUANCE PER ROUND, so E4 is cut as
round 78, which the analysis permits). Slot ~173. Check `deliverables/2.0.0_SA_COO~P2/checks/r78/p78_cells.py`, dry-run at base 212717f781 on dell2: AC1 PASS (61.4 s,
the read returns here), AC2 FAIL (rc 0, no bound), AC3 FAIL (no row).

## 73. ROUND 80, WORKSTREAM ~P (2026-10-08 ~18:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO analysis ADDENDUM 4 @eba8fde8bb: E7)

The custody route is live but irpt-export-render packages reports/repository.py at 83e8b9577a, whose KINDS lacks CUSTODY_REPORT
(row D2-W172-S3, ruled ~P's by ADDENDUM 4). This round repins and writes the packet; the release follows under a new pair (round 81),
built from a clean worktree (row D2-S3). Section 72 (round 79, IB-pr-366) is on branch wk-IRPT_BCKEND-174; the drain unions both.
Check: `deliverables/2.0.0_SA_COO~P2/checks/r80/p80_cells.py`, dry-run at base 2c287dec89: AC1, AC2, AC3 FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-367` | E7 part 1: repin repository.py (+ any read-path policy row) past b13bab7495; clean-tree BUILD_ONLY; never-widen packet | FWD-8 / CUSTDY hop 5 | WORLD (floor: infra/; nothing uploaded or applied) | IB-pr-364 (drained) | P80-a |

fanout: 1 of 1 chains, cap 8, reason: one repin and its packet. Slot ~175.

## 74. ROUND 81, WORKSTREAM ~P (2026-10-08 ~19:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 5 msg 1408: E7 releases first)

Both halves of IB-pr-367 are at HEAD (COO @764a0abf3c, CTO @275e506034). The custody after-reads move to the order after E8 (~M2) and
IRPT_CUSTDY E2 (~K2); this order adds the CTO half's retained-read regression (one existing ANALYSIS/PERFORMANCE report read back by
reference before and after; any change is Branch B). Check: `deliverables/2.0.0_SA_COO~P2/checks/r81/p81_cells.py`, dry-run at base
ea6b96a66a: AC1 FAIL, AC2 FAIL (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-368` | release irpt-export-render at a0d8d4943f (repository.py + retention.py) from a clean worktree; pre/post retained read-back | FWD-8 / CUSTDY hop 5 | WORLD | IB-pr-367 (drained @9a594e96a8) | P81-a |

fanout: 1 of 1 chains, cap 8, reason: one release with ordered acts. Slot ~176.
## 72. ROUND 79, WORKSTREAM ~P (2026-10-08 ~18:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO analysis ADDENDUM 2 @b227133904, msg 1362: E5)

Release 2 (irpt-ycharts-generate, X-1) rolled back at 17:44:54Z: on the served path the guard builds InteractiveAccess with no profile
reader and resolves the create owner as the actor itself, so uploads.py's on-behalf branch is unreachable. This cell fixes the served
guard (~P's lane); uploads.py (~Y2) is the target rule, not edited. After it drains, ~Y2 re-pins and a new release-2 pair is signed.
Check: `deliverables/2.0.0_SA_COO~P2/checks/r79/p79_cells.py`, dry-run at base 5ff7717f66: AC1 FAIL, AC2 FAIL (no test file), AC3 PASS.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-366` | E5: the live guard resolves the on-behalf owner for an OPAL_GLOBAL filer whose allowedFirmIds lists the firm; real served-path test, four negative arms; existing suites green | X-1 / TCKT_VNEXT TV-r-1 | WORLD (floor: infra/; nothing built or applied) | none | P79-a |

fanout: 1 of 1 chains, cap 8, reason: one guard change and its test. Slot ~174.

## 75. ROUND 82, WORKSTREAM ~P (2026-10-08 ~19:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 6 msg 1415: E9)

ReportRepository reserves every family under one default revision; a CUSTODY_REPORT must live under its own policy row
(irpt-custody-x10-v1, E8, ~M2) so irpt-x10-v1 stays byte-unchanged. This cell is the code; its release is a later pair after IB-pr-368
is live. Order (ADDENDUM 6): IB-pr-368 release -> E8 PENDING -> E9 + its pair -> E8 ACTIVE -> IRPT_CUSTDY E2 real report -> after-reads.
Section 74 (round 81, IB-pr-368) is on branch wk-IRPT_BCKEND-176; the drain unions both. Check:
`deliverables/2.0.0_SA_COO~P2/checks/r82/p82_cells.py`, dry-run at base 038b35d676: AC1, AC2, AC3 FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-369` | E9: ReportRepository retains each family under its own policy revision; custody callers pass the custody revision; regression arm | FWD-8 / CUSTDY hop 5 | WORLD (floor: infra/; nothing built or applied) | none (code) | P82-a |

fanout: 1 of 1 chains, cap 8, reason: one repository change and its tests. Slot ~177.

## 76. ROUND 83, WORKSTREAM ~P (2026-10-08 ~19:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 6/9 msg 1474: E9 under its own pair)

IB-pr-369 (per-family revisions) drained @0c2bdf7634; E8's PENDING row at HEAD (fdc0a92a21); IB-pr-368 live (idanP8nX). This round
writes E9's release packet: repin repository.py, composition.py (row D2-S6) and the registry row, clean-tree BUILD_ONLY, packet with
the PENDING -> ACTIVE answer and a replay regression arm for the release order. Check `deliverables/2.0.0_SA_COO~P2/checks/r83/p83_cells.py`,
dry-run at base 25076d5af5: AC1, AC2, AC3 FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-370` | E9 release packet: repin set, census, clean-tree BUILD_ONLY, never-widen packet | FWD-8 / CUSTDY hop 5 | WORLD (floor: infra/; nothing uploaded or applied) | IB-pr-369 (drained) | P83-a |

fanout: 1 of 1 chains, cap 8, reason: one repin and its packet. Slot ~178.

## 77. ROUND 84, WORKSTREAM ~P (2026-10-08 ~20:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on both halves of IB-pr-370 and CTO msg 1536: release E9 now)

E9 releases at pin 0a57f3c0e9 (five members); custody stays refused under the PENDING row; the ACTIVE row rides E10's pair (CTO adopted
the REC, msg 1536). The offline differential replay (IB-pr-368's AMENDMENT 1 shape) runs before the apply. Worktree cut from box/dell2.
Check `deliverables/2.0.0_SA_COO~P2/checks/r84/p84_cells.py`, dry-run at base c086ec4c2b: AC1 FAIL, AC2 FAIL (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-371` | release irpt-export-render at 0a57f3c0e9 (E9, five members) from a clean worktree; replay before apply | FWD-8 / CUSTDY hop 5 | WORLD | IB-pr-370 (drained) | P84-a |

fanout: 1 of 1 chains, cap 8, reason: one release with ordered acts. Slot ~179.

## 79. ROUND 86, WORKSTREAM ~P (2026-10-08 ~21:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 1651: RECUT E10)

IB-pr-372 (round 85, branch wk-IRPT_BCKEND-180 @3528d24f92) reached the custody writer through a caller-asserted direct-invoke event
(row D2-W180-S2, ARMED). The CTO ruled: do NOT drain it (draining would put the write path in HEAD for any later release), and recut so
the persist takes no principal from its caller. That branch is never drained; its section 78 and order never reach HEAD; this round
replaces it. Check `deliverables/2.0.0_SA_COO~P2/checks/r86/p86_cells.py`, dry-run at base b012511132: AC1, AC2, AC3 FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-373` | E10 recut: server-derived owner + accounts; trigger via the guarded Entry or in-function schedule; no direct-invoke path; packaging + ACTIVE row + census + BUILD_ONLY + packet | FWD-8 / CUSTDY S07 | WORLD (floor: infra/; nothing uploaded or applied) | IB-pr-371 (live) | P86-a |

fanout: 1 of 1 chains, cap 8, reason: one writer entry and its packet. Slot ~181.

## 80. ROUND 87, WORKSTREAM ~P (2026-10-08 ~22:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on both halves of IB-pr-373 and CTO msg 1719)

The CTO gave its half of IB-pr-373 (release as is) with conditions: the replay at release; re-read live PbyqmHBQ; the IAM leg (row
D2-W181-S1) is its own laptop sign-off owed BEFORE the route; and before any firm reads a Performance client statement, a cell adds
persisted_by and binds the content to the retained composition hash (row D2-W181-S2). This round: the function-only release, and that
cell, in disjoint write sets. The route is a later order after the IAM leg. Check `deliverables/2.0.0_SA_COO~P2/checks/r87/p87_cells.py`,
dry-run at base ece42ad420: all four criteria FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-374` | release irpt-export-render at 9238309eca (function only, no route); replay before apply | FWD-8 / CUSTDY S07 | WORLD | IB-pr-373 (drained) | P87-a |
| `IB-pr-375` | persisted_by + content bound to the retained composition hash; tests | FWD-8 / CUSTDY S08 | WORLD (floor: infra/; code only) | IB-pr-373 (drained) | P87-b |

fanout: 2 of 2 chains, cap 8, reason: disjoint write sets (P87-a: export tf, source map, ledger, deliverables ~182; P87-b: two source
files + tests + deliverables ~183). Slots ~182, ~183.

## 81. ROUND 88, WORKSTREAM ~P (2026-10-08 ~22:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO half of IB-pr-373 condition 1)

IB-pr-375 (persisted_by + the composition-hash binding) is drained; the CTO requires it live before any firm reads a Performance client
statement. custody_persist.py ships from the source dir; custody_write.py is a staged row pinned at d34a46f37d, so the release repins it.
This round writes the packet; the release goes to 0.7.0_AE_CloudOps~DELL2 (Andrew-direct msg 1756), function only (the route waits for
the IAM leg pair @77440a907b). Check `deliverables/2.0.0_SA_COO~P2/checks/r88/p88_cells.py`, dry-run at base 7c08fe294e: AC1, AC2 FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-376` | IB-pr-375 release packet: custody_write.py repin, census, clean BUILD_ONLY, never-widen packet | FWD-8 / CUSTDY S08 | WORLD (floor: infra/; nothing uploaded or applied) | IB-pr-375 (drained) | P88-a |

fanout: 1 of 1 chains, cap 8, reason: one repin and its packet. Slot ~184.
## 82. ROUND 89, WORKSTREAM ~P (2026-10-08 ~22:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the r61 directory release halves and msg 1832)

The r61 directory release (signed 2026-10-07, both gates met per row S364) never applied: dell2 had no terraform (S364). Row D2-S11
(0.7.0_AE_CloudOps~DELL2) verifies terraform on dell2. Live CodeSha256 of both directory functions still equals the packet's "live", and
the census at 4710b8007b equals the signed member lists; entry.py differs from the packet pin only by IB-pr-341's P1 fix (4850c85632).
The directory root's "NOT INITIALISED" header is stale (state object 195,705 bytes, 2026-10-06). The apply goes to the dell2 applier.
Check `deliverables/2.0.0_SA_COO~P2/checks/r89/p89_cells.py`, dry-run at base 4710b8007b: AC1, AC2 FAIL.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-377` | apply the r61 directory release (refresh then search), at 4710b8007b, by 0.7.0_AE_CloudOps~DELL2 | FWD-7 | WORLD | D2-S11 | P89-a |

fanout: 1 of 1 chains, cap 8, reason: one release with ordered acts. Assignee: 0.7.0_AE_CloudOps~DELL2 (a seat, not a worker slot).

## 83. ROUND 90, WORKSTREAM ~P (2026-10-08 ~23:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the IB-pr-376 halves + CTO sequencing ruling)

The IAM leg for the Performance client statement writer applied at 22:47:14Z (laptop). The CTO half of IB-pr-376 (@b97fa248b2) ruled the
order: the function with persisted_by and the binding (pin 49bc13131d, built 7T29wPhz) first, then the custody-report-persist route only
after a live read shows that sha, so no persist is served without them. One apply order to 0.7.0_AE_CloudOps~DELL2. The real persist
and the owner/other-firm reads follow IRPT_CUSTDY E2a. Check `deliverables/2.0.0_SA_COO~P2/checks/r90/p90_cells.py`: AC1, AC2 FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-378` | release irpt-export-render at 49bc13131d (replay first), then apply the custody-report-persist route | FWD-8 / CUSTDY S07-S08 | WORLD | IB-pr-376 (drained), IAM leg (applied) | P90-a |

fanout: 1 of 1 chains, cap 8, reason: one release then one route, ordered. Assignee: 0.7.0_AE_CloudOps~DELL2.

## 84. ROUND 91, WORKSTREAM ~P (2026-10-08 ~23:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 1949)

IB-pr-377 (round 89) graded PASS at dc3ff4c2c9: the r61 directory release is live (refresh RbpsijC2, search IV7P2AL4). Its driven refresh
was READY at 49financial and REFRESH_FAILED+SAFE at inflection and cottonwood, because clients the previous build carried are absent (row
D2-S13). The CTO ordered this cell FIRST in the round, landed before those served directories go OVER_AGE (expiry.py: over 2 trading days).
The cell measures the cause per firm (BUILD_BUG, KEY_CHANGE or SOURCE_REMOVAL), fixes a build or key fault at its root without weakening the
disappearance rule, and packages the release for the applier. SOURCE_REMOVAL stops at the diagnosis with a row to the CTO. Check
`deliverables/2.0.0_SA_COO~P2/checks/r91/p91_cells.py`: AC1, AC2, AC3 FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-379` | diagnose and fix the dropped entries in the inflection and cottonwood builds; package the refresh release | FWD-7 | WORLD | IB-pr-377 (PASS) | P91-a |

fanout: 1 of 1 chains, cap 8, reason: one fault, one cell; the release order follows its packet. Assignee: 0.9.0_WK_IRPT_BCKEND~187.

## 85. ROUND 92, WORKSTREAM ~P (2026-10-09 ~00:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 1959)

IB-pr-379 (round 91) stopped at its diagnosis, as its SOURCE_REMOVAL clause requires. Both dropped entries are source removals, one each:
an inflection household the vendor merged away, and a cottonwood zero-value account no longer emitted. The build is right, and the
disappearance rule fails them indefinitely (row D2-W187-S1, BLOCKING, ARMED). The CTO ruled the rule:
- an entry absent from both the build and the source is carried forward as TERMINATED + source_removed_on, and the build goes READY;
- an entry in the source but missing from the build stays REFRESH_FAILED, and that is the negative arm, run on both firms' real cases;
- each refresh prints its TERMINATED count.

The release goes under its own pair and must be live before cottonwood's OVER_AGE on 2026-10-12, so by Friday 10-09's close. Check
`deliverables/2.0.0_SA_COO~P2/checks/r92/p92_cells.py`: AC1, AC2, AC3 FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-380` | carry source-removed entries forward as TERMINATED; real-case replay with the negative arm; package the refresh release | FWD-7 | WORLD | IB-pr-379 (diagnosis drained) | P92-a |

fanout: 1 of 1 chains, cap 8, reason: one rule, one cell; the release order follows its pair. Assignee: 0.9.0_WK_IRPT_BCKEND~188.

## 86. ROUND 93, WORKSTREAM ~P (2026-10-09 ~00:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling msg 1988)

IB-pr-380 (round 92) is graded 3/3 PASS (P 8953eccfca, built xGc9a2m7; the replay is READY with terminated 1 at both firms, and the live
and negative arms are REFRESH_FAILED). Its rows show the release alone is fail-closed with no gain:
- D2-W188-S1: the runner writes the served directory and emits no source_client_ids;
- D2-W188-S2: inflection's previous READY manifest is outside the 10-trading-day window, so a 10-09 fire reads false additions.

The CTO ruled: (a) count every writer of latest.json and directory.json FIRST, because a served as_of of 10-08 after a failed refresh
means a second writer until proven otherwise, and the pair names every writer; then (b) the runner carries; (c) the previous state is
the served directory; (d) no contract change (S3). 380 and 381 ship as ONE release under one pair, live before cottonwood's 10-12
OVER_AGE. Check `deliverables/2.0.0_SA_COO~P2/checks/r93/p93_cells.py`: AC1, AC2, AC3 FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-381` | writer census; runner carry + source_client_ids; previous state = served directory; one release packet for 380 + 381 | FWD-7 | WORLD | IB-pr-380 (PASS, drained) | P93-a |

fanout: 1 of 1 chains, cap 8, reason: (a) gates (b)-(c), and one release covers both. Assignee: 0.9.0_WK_IRPT_BCKEND~189.

## 87. ROUND 94, WORKSTREAM ~P (2026-10-09 ~02:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 2151 and 2128)

IB-pr-381 (round 93) is graded 3/3 PASS under AMENDMENT 1 and drained @93e31749b4. Its findings:
- the served directory has 1 writer, the runner;
- the served directories already lost the entry, so a per-firm seeding run is needed (row S1).

Both halves of the ONE release are GIVEN: COO @8323d3fb19 and CTO @f0a2f049f7, with conditions:
- no seeding concurrent with a scheduled fire;
- the replay re-run on the real artifacts;
- S71 shown red at base;
- 49financial's first landing read.

S4 (the runner should refuse to land a build that drops an entry still in the source) is ruled yes, as a cell AFTER this release. CTO
msg 2128 separately gives ~P the three production custody ports for release 6 (contract @859ae01405); ~M2 builds port 2 and ~Y2
wires release 6. The directory release stays first in ~P's order.

Checks: `deliverables/2.0.0_SA_COO~P2/checks/r94/p94_cells.py` (IB94-1, AC1-AC3 FAIL at base) and `.../r94/p94_release_cells.py` (IB94-2,
AC1-AC2 FAIL at base).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-383` | apply the ONE directory release (refresh 6eOFTopG + runner bundle 2e3e6648), seed inflection and cottonwood, after-read READY 3/3 | FWD-7 | WORLD | IB-pr-380, IB-pr-381 (drained); both halves | P94-a |
| `IB-pr-382` | production custody ports current_selection, interpret_source, validate_evidence + read set for release 6 | FWD-8 / CUSTDY E2a | WORLD | none (port 2 ~M2, installer ~Y2 in parallel) | P94-b |

fanout: 2 of 2 chains, cap 8, reason: independent chains (directory release; custody ports). Assignees: 0.7.0_AE_CloudOps~DELL2 (383),
0.9.0_WK_IRPT_BCKEND~190 (382). The S4 refuse-drop cell is cut after 383 lands.

## 88. ROUND 95, WORKSTREAM ~P (2026-10-09 ~03:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 2351)

IB-pr-383 (round 94) is live through leg A1: irpt-directory-refresh reads 6eOFTopG (03:40:03Z). The bundle, the seeding and the
after-read follow. IB-pr-382 (the custody ports) is complete and drained @3998906069, and handed to ~Y2 for release 6.

The CTO ruled (msg 2351) that the three code-only cells start now and that their releases follow 383's after-read under their own pairs.
H1 (Terraform for the applier) waits as ruled (msg 2192).

Checks: `deliverables/2.0.0_SA_COO~P2/checks/r95/p95_s4.py`, `p95_svc.py` and `p95_svccom.py`. The new-test and surface criteria FAIL at
base; the suite criteria PASS as controls.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-384` | runner refuses a build that drops a source entry; stale directory root header removed (D2-S23) | FWD-7 | WORLD | none (release after 383) | P95-a |
| `IB-pr-385` | verified_internal_subject admits ONE firm-bound svc-custody-statement | FWD-8 / CUSTDY E2a | WORLD | none | P95-b |
| `IB-pr-386` | svc-commentary read-only REQUEST_COMPOSITION via get(), tenant-bound, one callable surface | NFRA_TRNSPT FWD-10 H2 | WORLD | none | P95-c |

fanout: 3 of 3 chains, cap 8, reason: three independent code-only cells. Assignees: 0.9.0_WK_IRPT_BCKEND~195, ~196, ~197. H1 is cut after
IB-pr-383 closes.

## 89. ROUND 96, WORKSTREAM ~P (2026-10-09 ~04:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 2363 and 2368)

IB-pr-384 (refuse-drop) and IB-pr-385 (svc-custody-statement) are graded PASS and drained (@1895f16a0b, @dd02e66933). IB-pr-386
(svc-commentary surface) is graded 3/3. The CTO added one code-only cell on `_authz/served.py`, which is the same file as IB-pr-385, so it
is cut only now that 385 is drained (one writer per file). Corrected by msg 2368: the narrowing keys to the PROFILE row, found by the
verified identity, because the token carries no allowedFirmIds claim. A non-list value is refused. Check
`deliverables/2.0.0_SA_COO~P2/checks/r96/p96_cells.py`: AC1 FAILs at base and AC2 PASSes (the control).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-387` | profile-row allowedFirmIds narrowing extends to internal callers; non-list refused; ALL never admits | FWD-8 | WORLD | IB-pr-385 (drained, same file) | P96-a |

fanout: 1 of 1 chains, cap 8, reason: one file, one writer. Assignee: 0.9.0_WK_IRPT_BCKEND~198. Release after 383, under its own pair.
