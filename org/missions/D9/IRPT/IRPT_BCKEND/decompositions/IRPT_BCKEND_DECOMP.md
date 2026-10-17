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
| `IB-er-201` | FWD-3 thread, hop 1: one invested 49F account (acct#24ccad9d), YTD, silver -> holdings-basis gold | WORLD (new gold prefixes; no reader switched, nothing served moves) | none | E1 |

**IB-er-201.** The source declaration as data (ruling 1), the gold script writing `holdings_performance_daily` and
its manifest at the builder addresses (ruling 9), the method of call 3 (rulings 2-5), and an ad-hoc QA run for the
thread account over the YTD trading days. The schedule, the other two firms and the adapter switch are later rounds.

fanout: 1 of 1 chains, cap 8.


## 15. ROUND 20, WORKSTREAM ~P (2026-09-29 ~01:2xZ, issuer 2.0.0_SA_COO~P, on PRD v0.19 rulings 10-12 and 1.0.0_SA_CTO 102519)

The FWD-3 thread's next hop on ~P: the adapter reads the holdings gold (~E round 1 built hop 1 for account
acct#24ccad9d). One chain, one worker; the page and PDF hops follow the served move.

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
| `IB-pr-273` | FWD-3 (49F): the S237/S239 blast-radius read -- the deployed adapter's SI and 3Y for acct#c8072993 and two others, its reader shape, and every served reader of `twr_daily` with a propagates flag (ruling 4) | WORLD (read-only on deployed bytes) | none | P27c |
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

## 90. ROUND 97, WORKSTREAM ~P (2026-10-09 ~05:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 2507)

Rounds 95 and 96 are complete: IB-pr-384, 385, 386 and 387 are graded PASS and drained. IB-pr-383's S1/S2/V1 wait only on laptop
AMENDMENT 27, the runner-host grant (rows D2-S25 and D2-S27). The CTO ruled (msg 2507) that the idle lane builds two things now, with
nothing applied:
- (a) H1 as DESIRED Terraform. It belongs to IRPT_ANLREQ, and its apply pair and after-reads go to ~T2 with ~Y2 driving.
- (b) The release packets for 384, 385+387 and 386. Those pairs are signed after 383 closes.

Checks:
- `deliverables/2.0.0_SA_COO~P2/checks/r97/p97_h1.py` (IB97-1): AC1 and AC2 FAIL at base. AC3 is terraform fmt on the touched files only
  and PASSes at base. dell2's provider mirror lacks hashicorp/local, so there is no offline validate.
- `.../r97/p97_release.py` (IB97-2..4): every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-388` | H1 READY-event trigger as DESIRED Terraform (stream, filtered mapping, exact grant) | NFRA_TRNSPT FWD-10 | WORLD | none | P97-a |
| `IB-pr-389` | release packet: runner bundle (IB-pr-384) | FWD-7 | WORLD | IB-pr-384 drained | P97-b |
| `IB-pr-390` | release packet: _authz served.py hosts (IB-pr-385 + 387) | FWD-2 / FWD-8 | WORLD | IB-pr-385, 387 drained | P97-c |
| `IB-pr-391` | release packet: svc-commentary composition-read Lambda (IB-pr-386) | NFRA_TRNSPT FWD-10 H2 | WORLD | IB-pr-386 drained | P97-d |

fanout: 4 of 4 chains, cap 8, reason: independent artifacts. Assignees: 0.9.0_WK_IRPT_BCKEND~199, ~200, ~201, ~202.

## 91. ROUND 98, WORKSTREAM ~P (2026-10-09 ~06:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 2621 and 2655)

Two cells:
- **H1 is WITHDRAWN** (CTO msg 2621, rescinding msg 2507 (a), on ~Y2 msg 2610). IRPT_ANLREQ's I3 queue is the one trigger, so IB-pr-388's
  mapping and grant are removed before any apply. Nothing was ever planned or applied.
- **FWD-14, the holdings publish gate**, is admitted at v0.32 with both halves signed (CTO msg 2655; Andrew-direct @f8e7d992dd). It is
  folded into ~P after the ~M Holdings workstream closed. S392 retires once FWD-14 is deployed and its first scheduled fire is read; until
  then today's manual read stands (armed, 14:47Z).

Workers come from ~P's agreed block ~260..~299 (~M2 msg 2557, ~Y2 msg 2560). Checks: `deliverables/2.0.0_SA_COO~P2/checks/r98/p98_h1_withdraw.py`
(AC1 FAILs at base, AC2 PASSes) and `.../r98/p98_fwd14.py` (AC1 and AC2 FAIL at base).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-392` | H1 withdrawn: delete ready_trigger.tf (mapping + kms grant) | NFRA_TRNSPT FWD-10 | WORLD | IB-pr-388 drained | P98-a |
| `IB-pr-393` | FWD-14 holdings publish gate: WORSE does not re-point; refusal record at address(); closed account listed | FWD-14 | WORLD | none | P98-b |

fanout: 2 of 2 chains, cap 8, reason: independent cells. Assignees: 0.9.0_WK_IRPT_BCKEND~260 and ~261. The FWD-14 deploy is a never-widen
pair after the cell.

## 93. ROUND 100, WORKSTREAM ~P (2026-10-09 ~06:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 2726 and Andrew's release-now)

IB-pr-390's pair is complete: COO half @567612e686, CTO half @b97ebb6b98 (msg 2726), with conditions:
- the replay is re-run before the ledger;
- the ledger states the pin and the six sha256;
- after-read 2 is satisfied by the replay, with no profile edit;
- the two held hosts stay held.

Andrew's word (via ~V2 msg 2536) releases it now and standalone. MSTR seated `0.7.0_AE_CloudOps~IB2` for it (msg 2725). Round 98's IB-pr-393
(FWD-14) is complete and drained @42793c81fc; its row W261-S2 (cottonwood closed-account marking) is asked of the CTO before its pair.
Check `deliverables/2.0.0_SA_COO~P2/checks/r100/p100_apply_390.py`: AC1 and AC2 FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-395` | apply IB-pr-390 on 6 hosts (replay before ledger; held hosts untouched) | FWD-2 / IRPT_ANLREQ FWD-1 | WORLD | IB-pr-390 pair GIVEN | P100-a |

fanout: 1 of 1 chains, cap 8, reason: one release. Assignee: 0.7.0_AE_CloudOps~IB2.

## 94. ROUND 101, WORKSTREAM ~P (2026-10-09 ~07:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 2738)

IB-pr-393 (FWD-14 gate) is graded 2/2 PASS and drained @42793c81fc. Its row W261-S2 found that the v0.32 closed-account exemption cannot fire
for a firm whose directory marks no closures: cottonwood is all UNKNOWN. The CTO ruled PRD v0.33 (@13ee60595d), and the CVO admitted it
(msg 2744): for such a firm, account_lost is LISTED and never refuses alone. One follow-up cell builds it; the FWD-14 release pair follows.
IB-pr-395 (the 390 release on 6 hosts) is out to 0.7.0_AE_CloudOps~IB2. Check `deliverables/2.0.0_SA_COO~P2/checks/r101/p101_v033.py`:
AC1 PASSes at base as a regression guard (the 15 existing gate tests plus the suite); AC2 FAILs.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-396` | FWD-14 v0.33: all-UNKNOWN firm's account_lost listed, not refusing | FWD-14 | WORLD | IB-pr-393 drained | P101-a |

fanout: 1 of 1 chains, cap 8, reason: one change. Assignee: 0.9.0_WK_IRPT_BCKEND~263.

## 92. ROUND 99, WORKSTREAM ~P (2026-10-09 ~06:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 2690 via ~V2 msg 2691)

IB-pr-390 (385+387 release packet, under AMENDMENT 1) holds two of the eight served.py hosts out:
- irpt-holdings: parity gate, row W201-S5;
- irpt-narrative: TypeError on the new served.py, row W201-S6.

The CTO orders their fix and release as the next cell, because IRPT_ANLREQ FWD-1's seat run starts only when every route reads ONE. The
cell branches from IB-pr-390's code pin (@74a62fb46c), so it builds on the new served.py. Round 98 is drained (@1aad66a284); IB-pr-392 (H1
withdrawn) is complete @f8b570d0f4. Check `deliverables/2.0.0_SA_COO~P2/checks/r99/p99_held_hosts.py`: AC1 and AC2 FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-394` | irpt-narrative TypeError + irpt-holdings parity gate fixed, restaged, release packet | FWD-2 | WORLD | IB-pr-390 code pin @74a62fb46c | P99-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, two hosts on the same served.py. Assignee: 0.9.0_WK_IRPT_BCKEND~262.

## 95. ROUND 102, WORKSTREAM ~P (2026-10-09 ~07:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 2748 and 2765)

The CTO's halves are given for IB-pr-391 (the composition reader, standalone after 395, @a946f8b829) and for IB-pr-394's irpt-holdings
(@7f294053f0). irpt-narrative is HELD: its rebuild widens a no-row internal caller (row W262-S1). ~V2 has amended svc-commentary's pair,
which meets 391's precondition. IB-pr-396 (FWD-14 v0.33) is graded 2/2 PASS and drained @5eeef73870. FWD-14's release packet is now
cuttable (msg 2748). IB-pr-395 (the 390 release) is applying on ~IB2.

Check `deliverables/2.0.0_SA_COO~P2/checks/r102/p102_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-397` | apply the composition reader (391) on ~IB2 | NFRA_TRNSPT FWD-10 H2 | WORLD | IB-pr-395 closed | P102-a |
| `IB-pr-398` | apply irpt-holdings only (394) on ~IB2; narrative untouched | FWD-2 | WORLD | IB-pr-395 closed | P102-a |
| `IB-pr-399` | narrative TypeError fix keeping the opal-capital binding (no widening) + release packet | FWD-2 | WORLD | IB-pr-394 drained | P102-b |
| `IB-pr-400` | FWD-14 release packet (runner bundle carrying the publish gate) | FWD-14 | WORLD | IB-pr-393, IB-pr-396 drained | P102-c |

fanout: 3 of 3 chains, cap 8, reason: lane ~IB2 runs 397 then 398 in order; two independent worker cells. Assignees:
0.7.0_AE_CloudOps~IB2 (397, 398), 0.9.0_WK_IRPT_BCKEND~264 (399), ~265 (400).

## 96. ROUND 103, WORKSTREAM ~P (2026-10-09 ~08:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO half @1428af7198 and row D2-W265-S1)

The CTO's half on IB-pr-399 (irpt-narrative) is GIVEN under conditions 1-4 (@1428af7198); the COO half is @08070100ee. IB-pr-395 is
COMPLETE (~IB2, drained @770f25558f; issuer re-grade 2/2 PASS on live). IB-pr-400 is graded PASS and drained @dda85dc8f4. Its row
W265-S1 shows the ordered runner key is not what the scheduled holdings fire runs: three per-firm bundles are. A fresh build of them
moves 17 non-FWD-14 members. Ruling (row D2-S37): the FWD-14 release is the three per-firm keys, NARROW (live bytes plus the FWD-14
commits on holdings_snapshot.py only); the ordered key is out of the release.

Check `deliverables/2.0.0_SA_COO~P2/checks/r103/p103_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-401` | apply irpt-narrative (399) on ~IB2 under CTO conditions 1-4 | FWD-2 | WORLD | IB-pr-397, IB-pr-398 closed | P103-a |
| `IB-pr-402` | FWD-14 narrow per-firm holdings bundles + release packet | FWD-14 | WORLD | IB-pr-400 drained | P103-b |

fanout: 2 of 2 chains, cap 8, reason: ~IB2 takes 401 after its queue; one independent worker cell. Assignees:
0.7.0_AE_CloudOps~IB2 (401), 0.9.0_WK_IRPT_BCKEND~266 (402).

## 97. ROUND 104, WORKSTREAM ~P (2026-10-09 ~09:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling @03521b4de0)

The CTO placed dell1's row MDPF_SECCLASS-D1-S8 with ~P (msg 2962). SC-e-56's CUSIP fallback in holdings_snapshot.py (dell1's) can fire
only on a node that carries a CUSIP security_id, and 49F's SmartX-path SECURITY nodes carry TICKER or VENDOR only. One cell: they carry
the source's CUSIP where it holds one and are listed where it holds none. Its release rides IRPT_BCKEND's pair AFTER dell1's SC-e-56 is
live.

Check `deliverables/2.0.0_SA_COO~P2/checks/r104/p104_cells.py`: AC1 and AC3 FAIL at base; AC2 is the suite control (PASS).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-403` | 49F SmartX-path nodes carry CUSIP security_id; none -> listed, never invented | FWD-2 (SECCLASS e56 acceptance 1) | SERVED | none (release after SC-e-56 live) | P104-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~267.

## 98. ROUND 105, WORKSTREAM ~P (2026-10-09 ~09:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO half @c4df78131d)

IB-pr-402 is graded 3/3 PASS and drained. Its pair is GIVEN: COO @a9d5043ef9 and CTO @c4df78131d (msg 3017), which requires all three keys
to land before the 14:15Z fire or roll back, and the ledger committed per leg. IB-pr-398 is COMPLETE (~IB2 @236d19e1ae). One apply cell,
sequenced on ~IB2 after 397 and before 401.

Check `deliverables/2.0.0_SA_COO~P2/checks/r105/p105_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-404` | land IB-pr-402's three narrow per-firm holdings bundles on ~IB2; replay on uploaded bytes; first-fire read | FWD-14 | WORLD | IB-pr-402 drained; pair GIVEN | P105-a |

fanout: 1 of 1 chains, cap 8, reason: one apply cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 99. ROUND 106, WORKSTREAM ~P (2026-10-09 ~10:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 3088 / IRPT_DASHBD ADDENDUM 9.2 (2))

IRPT_DASHBD's custody-statement runner must stop reading irpt-requests directly. The CTO refused a table grant. IRPT's owned read returns
the persist inputs, re-authorized per request, and svc-custody-statement reads them for cottonwood only. Released later under ~P's pair.

Check `deliverables/2.0.0_SA_COO~P2/checks/r106/p106_cells.py`: AC1 and AC3 FAIL at base; AC2 is the suite control (PASS, one
pre-existing failure excused by name, row IRPT_BCKEND-D2-S43).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-405` | owned read returns persist_inputs; svc-custody-statement cottonwood-only; release packet | FWD-2 (IRPT_DASHBD DB-b-85) | WORLD | none | P106-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~268.

## 100. ROUND 107, WORKSTREAM ~P (2026-10-09 ~10:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ruling D1-S8 AMENDMENT 2 @b58f09e1b8)

dell1's SC-e-56 CUSIP fallback (01e843ce2e) is live only in the ordered key, which no scheduled fire runs. The 49F fire runs the per-firm
bundle, which IB-pr-404 lands narrow and without e56. The CTO approved ONE 49F-only narrow release on the post-404 bytes. It carries the e56
member delta plus IB-pr-403's holdings_49f.py, digest-gated. The pair is ~P2's COO half, dell1 ~M1's COO half for the e56 member, and the
CTO half. The other firms are untouched.

Check `deliverables/2.0.0_SA_COO~P2/checks/r107/p107_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-406` | 49F narrow bundle: e56 member + IB-pr-403 member on IB-pr-402's built bytes; packet + replay | FWD-2 (SECCLASS e56 acceptance 1) | WORLD | IB-pr-402, IB-pr-403 drained (base = 402's built bytes; apply after 404) | P107-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~269.

## 101. ROUND 108, WORKSTREAM ~P (2026-10-09 ~11:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 17 (msg 3220))

IB-pr-405 is graded 3/3 and drained @6f51e09a79. ADDENDUM 17 ruled (a), sequenced: IB-pr-405's irpt-status release is built narrow on
IRPT_ANLREQ release 1's live bytes, AFTER release 1 lands (~Y2), so it is event-gated and not cut here. The routes/schema publication
cell can be cut now; it must pass the unguarded census.

Check `deliverables/2.0.0_SA_COO~P2/checks/r108/p108_cells.py`: AC1 and AC3 FAIL at base; AC2 is the control (PASS).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-407` | publish include=persist_inputs in routes.json + the read's response schema + contract tests | FWD-2 (IRPT_DASHBD DB-b-85) | WORLD | IB-pr-405 drained | P108-a |
| (event-gated) | IB-pr-405 narrow irpt-status release + pair | FWD-2 | WORLD | IRPT_ANLREQ release 1 LIVE | -- |

fanout: 1 of 1 chains, cap 8, reason: one cuttable cell. Assignee: 0.9.0_WK_IRPT_BCKEND~270.

## 102. ROUND 109, WORKSTREAM ~P (2026-10-09 ~12:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 18 (msg 3272))

The CVO adjudicated rounds 106 and 108 (ADJUDICATION_v49 @f99141d333). ADDENDUM 18 gives row D2-S46 ONE owner, ~P2: 9 investor-reporting
`_contracts` tests are red at HEAD. Until each is fixed or named with its owner and expected green commit, every investor-reporting
release packet prints the red list and STOPs if its members touch a red target. One cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r109/p109_cells.py`: both criteria FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-408` | bisect each red _contracts test to its breaking cell; FIX (tests/fixtures/declarations only) or NAME with owner + expected green | FWD-2 (suite integrity for every IRPT release) | WORLD | none | P109-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~271.

## 103. ROUND 110, WORKSTREAM ~P (2026-10-09 ~12:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 18.1 (msg 3284))

IB-pr-401 STOPPED before upload (row D2-S48). The W264-S1 enforcer-scope arm reads UNKNOWN on live and OPAL_GLOBAL on built for a no-row
Opal caller. The CTO ruled FIX: no widening, no client-data enumeration. Re-packet with a new hash and a 14-arm replay in which the
enforcer-scope arm reads IDENTICAL; the CTO re-signs then. IB-pr-401 stays held, and TCKT_VNEXT's seat run reads 26/27.

Check `deliverables/2.0.0_SA_COO~P2/checks/r110/p110_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-409` | narrative: no-row Opal caller stays UNKNOWN as live; TypeError fix kept; new packet | FWD-2 (and TCKT_VNEXT FWD-1's 27th route) | WORLD | none | P110-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~272.

## 104. ROUND 111, WORKSTREAM ~P (2026-10-09 ~13:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on row D2-W269-S1)

IB-pr-406 (worker ~269) built the 49F bundle (e56 + IB-pr-403) and replayed it on real inputs. The FWD-14 gate REFUSES: IB-pr-403's CUSIP
security_id hides the ticker from fill_display, and 13,892 SmartX nodes lose their class. dell1's e56 itself is sound (0 custody nodes
lost). One cell fixes IB-pr-403 inside ~P's decomposition (a ticker= fact, as custody rows already carry) and rebuilds and replays the
bundle. It supersedes IB-pr-406's artifact; IB-pr-406 closes on it.

Check `deliverables/2.0.0_SA_COO~P2/checks/r111/p111_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-410` | 403 ticker fix + 49F narrow bundle (e56 + fixed 49f) + replay with class parity + packet | FWD-2 (SECCLASS e56 acceptance 1) | WORLD | IB-pr-404 landed | P111-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~273.

## 105. ROUND 112, WORKSTREAM ~P (2026-10-09 ~13:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on IRPT_DASHBD ADDENDUM 12 item 3 / CTO msg 3370)

IRPT_DASHBD's runner keeps its verify-persisted-sha256 limb dormant until IRPT serves `report_index.sha256` (W64-S1). The persist response
already returns it; the owned read does not. One cell adds it, with the contract. It rides IB-pr-405's narrow irpt-status release, after
IRPT_ANLREQ release 1.

Check `deliverables/2.0.0_SA_COO~P2/checks/r112/p112_cells.py`: AC1 and AC3 FAIL at base; AC2 is the control (PASS).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-411` | persist_inputs.report_index carries the stored object's sha256; contract + tests | FWD-2 (IRPT_DASHBD W64-S1) | WORLD | IB-pr-405, IB-pr-407 drained | P112-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~274.

## 106. ROUND 113, WORKSTREAM ~P (2026-10-09 ~14:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 18/19)

The red `_contracts` list (IB-pr-408) leaves 4 NAMED entries. Two are ~P2's: the custody-report-read (IB-pr-355) and custody-report-persist
(IB-pr-373) controls, red because their response-contract files do not exist. One cell publishes both contracts from the shipped handlers;
routes.json keeps response_schema null (row W167-S1). The route-census test and the analysis-request-original control stay red, owned by
IRPT_ANLREQ (AR-y-22).

Check `deliverables/2.0.0_SA_COO~P2/checks/r113/p113_cells.py`: AC1 and AC2 FAIL at base; AC3 is the control (PASS).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-412` | publish responses/custody-report-read + custody-report-persist contracts + fixtures | FWD-2 (suite integrity, ADDENDUM 18) | WORLD | IB-pr-408 drained | P113-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~275.

## 107. ROUND 114, WORKSTREAM ~P (2026-10-09 ~14:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the IB-pr-410 pair)

IB-pr-410 is graded 3/3 and drained. Its COO half (@ec2d6b6f68) and CTO half (@56bc28957c) are GIVEN; dell1 ~M1's half on the e56
member is asked via MSTR~DELL2. One apply cell is cut now so ~IB2 can start the moment both gates read met: ~M1's half filed, and
IB-pr-404's ledger CLOSED after its L6 fire read.

Check `deliverables/2.0.0_SA_COO~P2/checks/r114/p114_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-413` | land IB-pr-410's 49F bundle on ~IB2; replay on uploaded bytes; first-fire read with wall time | FWD-2 (SECCLASS e56 acceptance 1) | WORLD | ~M1 half filed; IB-pr-404 ledger CLOSED | P114-a |

fanout: 1 of 1 chains, cap 8, reason: one gated apply cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 108. ROUND 115, WORKSTREAM ~P (2026-10-09 ~14:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 19.1 (msg 3478))

IB-pr-404's first fire published inflection and cottonwood, but the 49financial producer was SIGKILLed on the 4 GiB runner box (row D2-S56).
49F still serves its prior publication. The CTO ruled: no rollback now; IB-pr-410/413 HELD; one cell measures the 49F producer's peak RSS
(pre-404 / 404 / 410) against an 85%-of-4-GiB line and fixes the gate's memory under it (a bigger box is not the fix). If no fix is signed by
Monday 13:00Z, 404's Branch B runs on the 49F key only.

Check `deliverables/2.0.0_SA_COO~P2/checks/r115/p115_cells.py`: AC1 and AC3 FAIL at base; AC2 is the control (PASS).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-414` | 49F producer peak RSS on 4 trees + FWD-14 gate memory fix + gate-decision replay at 3 firms | FWD-14 | WORLD | none | P115-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~276.

## 109. ROUND 116, WORKSTREAM ~P (2026-10-09 ~15:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO ADDENDUM 20 (@c3fd5df57a))

ADDENDUM 20 places three open rows. (1) The 9x e56 cost joins IB-pr-414's harness: TO-IB-pr-414 AMENDMENT 1 adds wall time and table
lookups on all four trees. (2) The safe-deploy summary goes to the laptop tooling owner via MSTR (not this seat). (3) The wrong-parent
negative control is one LOCAL fix cell here: IB-pr-399's replay driver derives its control from pin^, which at a later pin is the bound
entry itself.

Check `deliverables/2.0.0_SA_COO~P2/checks/r116/p116_cells.py`: both criteria FAIL at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-415` | ~264's replay driver: control re-pointed to cabad9008c^ and shown to fail on its defect | FWD-2 (replay integrity) | LOCAL | none | P116-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~277.

## 110. ROUND 117, WORKSTREAM ~P (2026-10-09 ~16:5xZ, issuer 2.0.0_SA_COO~P2 on dell2)

IB-pr-414 graded complete: all three criteria PASS and the proof is VALID. The fix's 49F peak is 3,139,624,960 B, under the 3,650,722,201 B
line; wall time is 417.2 s against 760.4 s; gate decisions are identical at 3 firms. That meets CTO ADDENDUM 20's release line, so the
49F bundle is rebuilt for IB-pr-413.

Three other items enter:
- Row D2-S60 (2.0.0_SA_COO~Y2): three live functions ship call-signature splits. CTO msg 3732 asks for a live-call read within the
  hour, then a rollback or fix pair for a failing route, or a cell for a latent one.
- The containment ruling's code cell (item 3).

Check `deliverables/2.0.0_SA_COO~P2/checks/r117/p117_cells.py`: every criterion FAILS at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-417` | 49F narrow bundle = IB-pr-410's members + IB-pr-414's gate memory fix; memory, replay, packet (re-points IB-pr-413) | FWD-14 | WORLD | none | P117-a |
| `IB-pr-419` | D2-S60 live-call read: one real GET per split route + 24h CloudWatch counts; FAILING or LATENT | FWD-2 | WORLD | none | P117-b |
| `IB-pr-416` | D2-S60 repair: irpt-narrative, irpt-performance-adapter, irpt-status rebuilt from one tree; attribute-call limb; packet | FWD-2 | WORLD | none | P117-c |
| `IB-pr-418` | containment item 3: 12 code files + TO-IB-er-201 free of account ids; er-201 proof back, redacted and VALID | FWD-3 | LOCAL | none | P117-d |

fanout: 4 of 4 chains, cap 8, reason: four independent cells. Assignees: 0.9.0_WK_IRPT_BCKEND~279 (417), ~281 (419), ~278 (416),
~280 (418).

## 111. ROUND 118, WORKSTREAM ~P (2026-10-11 ~03:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the IB-pr-416 pair; CTO msgs 3959, 3961, 3980)

Round 117 is terminal 4 of 4. IB-pr-416 built irpt-performance-adapter, irpt-narrative and irpt-status from one commit (361c44fa9d); the
pair is signed (COO @c362f7e0fb; CTO @d29ccddb17, conditions 1-9). One cell applies the adapter (failing closed on performance-report
since 2026-10-09T15:41Z) and then the narrative, with the three candidate source-map entries landed first (row D2-W278-S2). irpt-status's
apply is 2.0.0_SA_COO~Y2's (IRPT_ANLREQ TO-APPLY-Y1 AMENDMENT 8, CTO msg 3928) and is not a cell here.

Check `deliverables/2.0.0_SA_COO~P2/checks/r118/p118_cells.py`: every criterion FAILs at base. Condition 8's reach read:
`checks/r118/REACH_READ_IB416_BUILT_ZIPS_20261011.txt` (adapter count 0 under CTO half A4).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-420` | source-map entries landed; adapter then narrative applied under the pair; live-call arm each; ledger | FWD-2 | WORLD | IB-pr-416 complete, pair signed | P118-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 112. ROUND 119, WORKSTREAM ~P (2026-10-11 ~07:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4416)

Round 118 is terminal 1 of 1. The DSGN_IRPTV1 FWD-1 walk of 2026-10-11 07:30Z breaks at Performance: the applied adapter admits the
request and refuses it at `performance/authorization.py:90`, the one-use vendor plan gate (4 of 4 requests, `VendorEgressRefused`,
public code OBJECT_NOT_COVERED). The CTO ruled the gate retired by Andrew-direct 2026-10-09 (egress open except Bloomberg; its two
vendors are Black Diamond and Orion). One cell removes the plan requirement, keeps and tests the packaged-path, own-mapping,
caller's-firm-and-accounts and use-record-as-a-log behaviours, rebuilds the adapter from one commit and writes the never-widen packet.
The change WIDENS served output, so the apply comes by a later order under a pair.

Check `deliverables/2.0.0_SA_COO~P2/checks/r119/p119_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-421` | vendor performance path without the one-use plan; kept behaviours tested; adapter rebuilt; packet | FWD-2 (DSGN_IRPTV1 FWD-1's Performance hop) | WORLD | IB-pr-420 applied | P119-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~282.

## 113. ROUND 120, WORKSTREAM ~P (2026-10-11 ~08:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4488)

Round 119's one order (IB-pr-421) is complete and built, not applied. Row D2-W282-S1: the adapter role holds no secretsmanager
GetSecretValue, because `retained.tf` count-gates both vendor session-read policies on the retired plan variable. The CTO ruled ONE
release: IB-pr-421's zip plus the two policies, under one pair. One cell ungates the two policies and produces the Terraform plan and
its packet; nothing is applied in it.

Check `deliverables/2.0.0_SA_COO~P2/checks/r120/p120_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-422` | two session-read policies ungated from the plan variable; plan adds exactly those two; naming limb; packet | FWD-2 (DSGN_IRPTV1 FWD-1's Performance hop) | WORLD | IB-pr-421 complete | P120-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~283.

## 114. ROUND 121, WORKSTREAM ~P (2026-10-11 ~09:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the IB-pr-421 + IB-pr-422 pair; CTO msg 4524)

Rounds 119 and 120 are terminal (IB-pr-421 built OF+8j4uc; IB-pr-422 planned 2 add, 0 change, 0 destroy, targeted). The pair is signed
(COO @468df7baa4; CTO @7a01aa805a, conditions 1-5). One cell applies the release in one sitting under one ledger entry: the adapter's
source-map entry, the two single-secret session-read policies by a targeted apply, then the zip on the full root, then the live-call
arm. No vendor call is made by the apply; the close reads APPLIED, UNEXERCISED and the laptop's re-walk grades DSGN_IRPTV1 FWD-1.

Check `deliverables/2.0.0_SA_COO~P2/checks/r121/p121_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-423` | source-map entry; two session-read policies (targeted); adapter zip; live-call arm; ledger | FWD-2 (DSGN_IRPTV1 FWD-1's Performance hop) | WORLD | IB-pr-421, IB-pr-422 complete; pair signed | P121-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 115. ROUND 122, WORKSTREAM ~P (2026-10-11 ~10:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4624) -- ROLLBACK

Rounds 119-121 released the vendor performance path (IB-pr-421, 422, 423). That release serves Cottonwood a Black Diamond-calculated
return, against the ratified ENDPOINT: FWD-3 serves a figure computed by Opal from holdings, and ADDENDUM v0.19 makes a vendor figure a
comparison point only (FWD-13). The refusal the release removed was that design (retained.py:53-62; batch 66 item 2, row S247). The
issuer recommended and signed the release without reading the ENDPOINT; escalation record @a5f045cabf. The CTO ruled the rollback and
withdrew msgs 4416 and 4616. One cell takes the pair's signed Branch B and puts the tree back so no later build re-ships it.

Check `deliverables/2.0.0_SA_COO~P2/checks/r122/p122_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-424` | adapter zip back to 9kYLdR64; source-map entry back; performance/ and retained.tf back to fb3bae3b99; two session policies removed (targeted); ledger | FWD-3 (the ENDPOINT's state restored) | WORLD | none | P122-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 116. ROUND 123, WORKSTREAM ~P (2026-10-11 ~10:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4729)

Round 122 rolled the vendor release back. The Performance hop for Cottonwood is FWD-3's own outcome: a figure computed by Opal from
holdings. The CTO ruled the source stays the declared silver fact_holdings (read current by the issuer: 91 partitions, 2026-06-09 to
2026-10-09, 86 of 86 trading days) and that the thread is row S252: a minority of securities carry the prior day's close, measured so
far on 10 of 81 partitions. One read-only cell measures it on every trading-day partition and names the securities. The basis
declaration that follows is the CTO's ruling on that read, and is not this cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r123/p123_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-425` | S252 on every trading-day partition: per-day counts, the lagged securities and their classes, a planted control | FWD-3 (Cottonwood) | LOCAL | none | P123-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~284. DIRECT-ACT (one cell, read only, LOCAL).

Parked for the next issuance, each ruled and unblocked: the one-tree re-pin of irpt-ycharts-generate (CTO msg 4657; owner this seat);
the `_contracts` smoke-map pin with the two custody-route fixtures (2.0.0_SA_COO~D2 msg 4714; owner this seat).

## 117. ROUND 124, WORKSTREAM ~P (2026-10-11 ~10:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 4621 and 4657)

Row IRPT_ANLREQ-D2-S39 read irpt-ycharts-generate's digests as disagreeing. The issuer's read (@2cef0485fd): the live package tdpterTM is
release 6b, 104 of 104 members match a commit, and the source map's record is one release behind. The CTO ruled one re-pin of the whole
entry to one merged commit taken after the performance/ restoration, a fresh build, and a census of every member that moves against
live. One build-only cell does that. The issuer then reads the ENDPOINT against every served change before any half is written; the
apply comes by a later order under a pair.

Check `deliverables/2.0.0_SA_COO~P2/checks/r124/p124_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-426` | irpt-ycharts-generate from one commit: candidate map, moved-member census (served or inert), replay, packet | FWD-4 | WORLD | IB-pr-424 closed (the restoration is in the tree) | P124-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~285.

Still parked, owner this seat: the `_contracts` smoke-map pin with the two custody-route fixtures (2.0.0_SA_COO~D2 msg 4714). Un-parks
when the workspace's portal pin carries the 22-entry smoke map; before that the test would fail against the 12-entry map it reads.

## 118. ROUND 125, WORKSTREAM ~P (2026-10-11 ~11:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4786)

Round 123's read (IB-pr-425, drained @7aa373487b) measured row S252 on 85 of 85 gradeable trading-day partitions: 2,514 of 37,806
moved security-days at the prior close, per day 0.0 to 59.0 percent with a median of 5.9, and one CUSIP's rows disagreeing with each
other on 50 of 85 days. The CTO ruled that no basis is declared on that read and ordered one more: by account, and by custodian or
source field. One read-only cell, counts only, no account id in any output.

Check `deliverables/2.0.0_SA_COO~P2/checks/r125/p125_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-427` | lagged closes by account class and by custodian or source field; the neither rows; accounts behind per day; planted control | FWD-3 (Cottonwood) | LOCAL | IB-pr-425 drained | P125-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~286. DIRECT-ACT (one cell, read only, LOCAL).

## 119. ROUND 126, WORKSTREAM ~P (2026-10-11 ~11:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4801)

The portal's readers refuse the producer fixtures of five routes; 2.0.0_SA_COO~D2 read all five fixtures valid against the v1
contract (@da62c58fa1). The CTO asked this seat, as the producer, whether each HANDLER's own answer has its fixture's shape, from the
handlers' code and their own tests, with no live call. One read-only cell. It fixes nothing and does not rule which side moves.

Check `deliverables/2.0.0_SA_COO~P2/checks/r126/p126_cells.py`: every criterion FAILs at base. The control route
(comparison-catalogue) is expected SAME_AS_FIXTURE and was not measured by the issuer; a different reading stops the cell.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-428` | five routes: where the answer is built, a run, the schema result, shape against the fixture; a control route | FWD-2 (DSGN_IRPTV1's readers) | LOCAL | none | P126-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~287. DIRECT-ACT (one cell, read only, LOCAL).

## 120. ROUND 127, WORKSTREAM ~P (2026-10-11 ~11:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4825)

Round 125's read (IB-pr-427, drained @ea10544bdf): of 614 accounts with moved rows, 553 are always on their own date, 0 always behind,
61 mixed by day; 386 of 1,000 accounts have no moved row on any day. The CTO ruled the basis per ACCOUNT-DAY as a measured claim
(OWN_DATE, PRIOR_CLOSE, NOT_GRADED), a return served only when an account-day and its prior trading day both read OWN_DATE, the rest
blank with the reason, nothing shifted. Before the PRD addendum the CTO asks what the instrument needs daily and the share of
account-days the rule blanks. One read-only cell counts both.

Check `deliverables/2.0.0_SA_COO~P2/checks/r127/p127_cells.py`: every criterion FAILs at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-429` | one claim per account-day; NOT_GRADED by reason and what those accounts hold; served and blank under the rule; the instrument's daily needs; a constructed control | FWD-3 (Cottonwood) | LOCAL | IB-pr-427 drained | P127-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~288. DIRECT-ACT (one cell, read only, LOCAL).

## 121. ROUND 128, WORKSTREAM ~P (2026-10-11 ~12:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 4858 and 4865)

Round 126's read (IB-pr-428, drained @7b8605503e): the handlers' data member has its fixture's shape on 5 of 5 routes, and four closed
v1 response schemas omit the envelope member `unprojected_grant` that `response_envelope` always adds. The CTO ruled the four schemas
gain the member (the portal's envelope parser already requires it). The CTO also ruled, on 2.0.0_SA_COO~D2's read, that two producer
fixtures are thin and are re-made by their handlers: DirectoryPage (an entry's revision must be the page's) and AnalysisUploadResult
(the portfolio's source must name its upload). One cell does both. It changes no handler and no deployed byte.

Check `deliverables/2.0.0_SA_COO~P2/checks/r128/p128_cells.py`: AC1, AC3 and AC4 FAIL at base; AC2 is a bound and PASSes at base
(2 failed, 203 passed, both failures analysis-request-original). A fourth criterion is stated with its reason on the face.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-430` | four response schemas declare unprojected_grant; their valid fixtures follow; two producer fixtures re-made by the handlers' own code path | FWD-2 (the v1 contract agrees with what the handlers send) | WORLD | IB-pr-428 drained | P128-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~289. Class WORLD by the L6 floor (its paths name infra/); not a direct act. It deploys nothing. The ratified-text
signer 3.0.0_SA_CVO is told at issuance: the four files are contract files.

## 122. ROUND 129, WORKSTREAM ~P (2026-10-11 ~12:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4916, URGENT)

The resident on the YCharts host refused a request on 2026-10-11 with CAPTURE_FAILED:AUTH_FAILED:NO_AUTHENTICATED_PROBE, then
SIGNED_OUT, then SESSION_REFRESH_ALREADY_USED (host journal read by 0.7.0_AE_CloudOps~YC2). The CTO ruled the session runner
IRPT_BCKEND's and stopped every seat from sending another request down the YCharts path until the failure is read: every
submission makes the host try to sign in, and repeated failed sign-ins can lock the one vendor account. One READ-ONLY cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r129/p129_cells.py`: AC1-AC3 FAIL at base (no record). The checks grade shape and
bounds; the host's state is unmeasured by the issuer.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-431` | why the host's session capture failed to sign in, from the host's lines and the runner's stored state; when a YCharts-path job last reached READY there; no sign-in attempted | FWD-4 (a session is usable only when verified; never an endless login contest) | WORLD | none | P129-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: the applier seat 0.7.0_AE_CloudOps~IB2 (the read is by SSM on the host).

## 123. ROUND 130, WORKSTREAM ~P (2026-10-11 ~13:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 4923)

IRPT_YCDGEN's journey read (hop 11; rows IRPT_YCDGEN-W2-S13 and IRPT_YCDGEN-W6-S4): the sections answer for an Opal-made
report carries provider, computation_validation and retained_ref, while the published response schema requires
extraction_validation and closes data. PRD ADDENDUM v0.28 item 29 already ratifies the Opal form. The CTO sent the contract
rows to this workstream and ruled that no reader goes first (the portal's sections reader already reads the Opal member).
One cell: the response schema's data member admits exactly the two closed forms. No handler and no deployed byte changes.

Check `deliverables/2.0.0_SA_COO~P2/checks/r130/p130_cells.py`: AC1 FAIL at base on arm (a) with arms (b), (c), (d) holding;
AC2 a bound, PASS at base; AC3 FAIL at base (no record).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-432` | the sections response schema admits the Opal-made report form beside the vendor form, each closed; producer fixtures of both forms made by the handler | FWD-4 / PRD ADDENDUM v0.28 item 29 (the v1 contract agrees with what the handler answers) | WORLD | none (write set disjoint from IB-pr-430's) | P130-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~290. Class WORLD by the L6 floor (paths name
infra/); it deploys nothing. The ratified-text signer 3.0.0_SA_CVO is told at issuance.

## 124. ROUND 132, WORKSTREAM ~P (2026-10-11 ~13:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5025)

IB-pr-431's read (0.7.0_AE_CloudOps~IB2, @6a254507a6): the host's sign-in was not rejected; the form was submitted and the probe
never passed; the read cannot say whether the vendor accepted the credentials, because login_submission and probe_pair are
persisted nowhere and the signed-out-app-chrome diagnosis is gated on no submission. No session bundle has been written since
2026-10-05T10:04Z. The CTO ruled one BUILD-ONLY cell; the vendor path stays stopped, and the change reaches the host only in a
resident release under its own pair (st32, IRPT_YCDGEN's issuer). The first sign-in after it is ONE request on the CTO's word.

(Round 131's number is not used: the v0.35 re-count runs as IB-pr-429 AMENDMENT 2 after the L6 gate refused a new order.)

Check `deliverables/2.0.0_SA_COO~P2/checks/r132/p132_cells.py`: AC1-AC3 FAIL at base. Measured at base: the existing offline
suite exits 0 under the netguard preload; the session tests read 118 passed, 1 skipped.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-434` | the capture persists login_submission and probe_pair as closed secret-free members; the signed-out-app-chrome diagnosis fires after a submission under its own code; stderr kept per run | FWD-4 (a session is usable only when verified from the transport; never an endless login contest) | WORLD | IB-pr-431 read | P132-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~292. Class WORLD by the L6 floor; build only,
no request sent, nothing deployed.

## 125. ROUND 133, WORKSTREAM ~P (2026-10-11 ~14:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5082)

The re-count under PRD ADDENDUM v0.35/v0.36 (IB-pr-429 AMENDMENT 2, branch wk-IRPT_BCKEND-288b @4f263f004c): UNGRADEABLE 42,967,
ACCT_OWN_DATE 20,138, NOTHING_TO_GRADE 13,636, ACCT_PRIOR_DATE 55; 57.3 percent of 75,796 eligible account-days blank; 382 of 999
accounts never served; OUTSIDE_ANCHOR on 34,437 account-days. The CTO ruled: the serving rule stands; a cash-flagged priced row
outside the anchor is cash only where the source's own price is equal on the day and the prior trading day; the sixth reason is
a refusal of the stamp; the next cell reads the anchor's coverage from what the estate already holds. No gold producer before it.

Check `deliverables/2.0.0_SA_COO~P2/checks/r133/p133_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-435` | the securities behind OUTSIDE_ANCHOR ranked by account-days with the half and ninety-percent counts; the cash rule counted; whether a held price store carries each security's close | FWD-3 (Cottonwood's figure on a basis somebody measured) | LOCAL | IB-pr-429 AMENDMENT 2 (its instrument, read from its branch) | P133-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~293. DIRECT-ACT (one read-only cell, LOCAL).

## 126. ROUND 134, WORKSTREAM ~P (2026-10-11 ~14:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5157)

IB-pr-435's read (branch wk-IRPT_BCKEND-293 @497c7628fd): 734 securities behind OUTSIDE_ANCHOR, 9 mutual funds cover half; the
four market-close stores find 144 of 45,216 needed security-days; only the custodian's own mark covers them. The CTO ruled the
custodian's mark is not the anchor, and the next cell reads an independent daily NAV for the nine funds from a source the estate
already runs: the gateway's YCharts series tools first (403 on the issuer's two calls, not retried), then the Yahoo reader
ADVI_COTBKF runs (named by 2.0.0_SA_COO~C2, msg 5159). No Bloomberg. Nothing is re-graded.

Check `deliverables/2.0.0_SA_COO~P2/checks/r134/p134_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-436` | nine funds by 85 days: per fund, the days the custodian's mark equals the NAV of the day, of the prior day, of both, of neither; a control on a security the anchor carries; the account-day effect as an upper bound | FWD-3 (Cottonwood's figure on a basis somebody measured) | LOCAL | IB-pr-435 (its ranking and instrument, read from its branch) | P134-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~294. DIRECT-ACT (one read-only cell, LOCAL).

## 127. ROUND 135, WORKSTREAM ~P (2026-10-11 ~15:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on 2.0.0_SA_COO~D2 msg 5188)

A defect of this workstream's own IB-pr-432 (drained @8aa28be2a8): the sections response schema lists its members under
data.properties as description-only schemas, and the portal's wire generator refuses an untyped member on purpose; three portal
tests are red at portal DEV b92696c1 (2.0.0_SA_COO~D2's measure). Nothing served is affected. One repair cell, its seam probe
run against the real neighbour: the portal's own generator in a provisioned portal worktree.

Check `deliverables/2.0.0_SA_COO~P2/checks/r135/p135_cells.py`: AC1 FAIL at base, AC2 FAIL at base, AC3 a bound, PASS at base.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-437` | every member of the sections response schema is typed so the portal's generator renders it; the two closed forms keep their meaning; the generator's rewritten wire files listed for the portal's lane, not committed | FWD-4 / PRD ADDENDUM v0.28 item 29 (a contract its consumer can read) | WORLD | IB-pr-432 drained | P135-a |

fanout: 1 of 1 chains, cap 8, reason: one cell; portal_ref: b92696c1ed61. Assignee: 0.9.0_WK_IRPT_BCKEND~295.

## 128. ROUND 136, WORKSTREAM ~P (2026-10-11 ~15:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5211)

IB-pr-436's read (branch wk-IRPT_BCKEND-294 @d1adf5102e): on eight of nine funds the custodian's mark equals the day's NAV on
every fund-day measured and the prior day's on none; FPNIX returned no data; 497 of 124,645 rows sit at the prior day's NAV.
Nine funds free only 563 account-days, because an account-day is freed only when every security it holds is graded. The CTO
ruled the unit is the account-day and the next cell sizes it over all 734 securities, one pass, read only. Whether an unofficial
reader may be a production anchor is a PRD question ruled on that table.

Check `deliverables/2.0.0_SA_COO~P2/checks/r136/p136_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-438` | the same reader over all the outside-anchor securities, one pass; the account-days freed when every security a day holds is graded; the sizing under v0.36; the account-days the prior-day rows blank | FWD-3 (Cottonwood's figure on a basis somebody measured) | LOCAL | IB-pr-436 (its measure, read from its branch) | P136-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~296. DIRECT-ACT (one read-only cell, LOCAL).

## 129. ROUND 137, WORKSTREAM ~P (2026-10-11 ~16:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5298)

PRD ADDENDUM v0.38 @83f1d66bd8 (ratified-text half signed @8ae7b1a563) repairs v0.37: a witness's DATE LABEL is measured before it
grades; YAHOO_CLOSE grades only an admitted class, today EXCHANGE_TRADED, on thin evidence; mutual funds are NOT admitted; the
37.0 percent sizing of round 136 is WITHDRAWN. The first cell under it is read only: state the source's instrument-type field,
widen the evidence to every security both witnesses carry, re-size with funds outside, and count priced fund transactions.

Check `deliverables/2.0.0_SA_COO~P2/checks/r137/p137_cells.py`: AC1-AC3 FAIL at base (no file); both branches of the
type-field question are graded.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-439` | the instrument-type field; both witnesses per type (equal, one day off, neither); the sizing under v0.38; a count of fund-dates with a priced custodian purchase or redemption | FWD-3 (Cottonwood's figure on a basis somebody measured) | LOCAL | IB-pr-438 drained | P137-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~297. DIRECT-ACT (one read-only cell, LOCAL).

## 130. ROUND 138, WORKSTREAM ~P (2026-10-11 ~16:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 5373 and 5376)

Two read-only cells with disjoint write sets and no edge between them.
(a) 2.0.0_SA_COO~D2's row DSGN_IRPTV1-D2-S18: in a portal fixture the Holdings card reads a total the table under-lists, because two
SMA sleeve nodes have no security node beneath them. The CTO asks whether a SERVED holdings answer can carry such a leaf.
(b) IB-pr-439's read (branch wk-IRPT_BCKEND-297 @e6462bdd4a): the holdings source states no instrument type, so no class is admitted
to the second witness and 58.2 percent stands; the transactions table beside it carries SEC Asset Type and Share Class Type by CUSIP
and dated trade prices. The CTO ruled one cell produces the two tables an addendum would rest on; the field classes nothing yet.

Check `deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py`: six criteria, all FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-440` | the holdings producer's rule on a sleeve leaf with no security node, read in code; such leaves counted in one firm's served answer for one day | FWD-5 (missing attribution stays visible) | LOCAL | none | P138-a |
| `IB-pr-441` | both witnesses per instrument type, the type joined by CUSIP from the transactions table; each priced fund trade beside the reader's bar for its date and the days either side | FWD-3 (a basis somebody measured) | LOCAL | IB-pr-439 (its instrument, read from its branch if not merged) | P138-b |

fanout: 2 of 2 chains, cap 8, reason: two independent read-only cells. Assignees: 0.9.0_WK_IRPT_BCKEND~298, ~299. DIRECT-ACT each.

## 131. ROUND 139, WORKSTREAM ~P (2026-10-11 ~17:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 5453 and 5460)

IB-pr-441 MERGED @0be2f61548 and read on the trunk unchanged by the issuer: 894 securities, 12 types, 5 one-day-off security-days of
64,536; 6,149 priced fund trades: same day only 4,490, prior day only 28, next day only 0. PRD ADDENDUM v0.39 @90bfa5fc4f, its
ratified-text half signed @5d8db9acaf, admits seven source-stated pairs to the second witness and leaves out RIC/BDC Inst, RIC/BDC
Not Available, the untyped and the mixed. Its cost is not known. One read-only cell sizes it; no producer is cut on the sizing.

Check `deliverables/2.0.0_SA_COO~P2/checks/r139/p139_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-442` | the account-days freed when only securities of the seven admitted types are graded by the second witness; the blank share and never-served accounts; what the rest waits on, counted both ways; the reviewer's two points (the to-the-cent next-day trades named; the fund trades split by pair) | FWD-3 (Cottonwood's figure on a basis somebody measured) | LOCAL | IB-pr-441 drained and read on the trunk | P139-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~300. DIRECT-ACT (one read-only cell, LOCAL).

## 132. ROUND 140, WORKSTREAM ~P (2026-10-11 ~18:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5501)

IB-pr-442's sizing (branch wk-IRPT_BCKEND-300 @721d34910e, drain in progress at this cut): admitting PRD v0.39's seven pairs sizes
the blank share at 50.3 percent (58.2 in force) and never-served accounts at 357 (382); the institutional fund share class, left
out on two one-day-off security-days of 1,474, is what most of the rest waits on (6,960 account-days by it alone, an upper bound).
The CTO does not admit it on smallness and orders one read: a third dated value beside both witnesses on the five one-day-off
security-days, and whether the first witness's partition for the window's last day is the prior day's.

Check `deliverables/2.0.0_SA_COO~P2/checks/r140/p140_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-443` | the five one-day-off security-days of IB-pr-441, each with both witnesses over three days and a third dated value; one verdict each (which witness is off, or cannot be told); the last-day question | FWD-3 (a basis somebody measured) | LOCAL | IB-pr-441 drained | P140-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~301. DIRECT-ACT (one read-only cell, LOCAL).

## 133. ROUND 141, WORKSTREAM ~P (2026-10-11 ~18:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5524)

The fifth run was made on the CTO's word with IB-pr-434's build on the host (release st32). 2.0.0_SA_COO~G2's host-side read
@77f135f74f: one submission; the posted credentials match the secret; the vendor answered the post 302; then seven steps and both
arms of the closing probe read 202 and NOT_LIVE; the reason is the old NO_AUTHENTICATED_PROBE and the new after-submit reason did
not fire. The CTO's inference: accepted, then a web firewall's challenge. One read-only diagnosis cell: which receipt leaves
confirm or kill that, and why the new reason did not fire. No request and no sign-in; the vendor path stays stopped.

Check `deliverables/2.0.0_SA_COO~P2/checks/r141/p141_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-444` | the deciding leaves of the capture receipt with their confirming and killing values; why the after-submit reason did not fire, by line; the verdict from what is already read; the reads to ask of the host reader | FWD-4 (a session is usable only when verified; never an endless login contest) | LOCAL | IB-pr-434 drained | P141-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~302. DIRECT-ACT (one read-only cell, LOCAL).

## 134. ROUND 142, WORKSTREAM ~P (2026-10-11 ~18:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5549)

IB-pr-443's read (merged; 3 of 3 PASS on the issuer run): on both institutional-class one-day-off days the READER repeats the
prior day's bar while the first witness moves (verdicts inferred from the series; no priced trade within three trading days); the
three exchange-traded days are half-cent rounding. The CTO ruled the institutional class stays out on that finding, since a
repeated bar is the dangerous direction, and named a guard that would close it for every class: the second witness does not
grade a security-day on which its own bar equals its bar for the prior trading day. One read-only cell measures the guard.

Check `deliverables/2.0.0_SA_COO~P2/checks/r142/p142_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-445` | the overlap table again under the unmoved-bar guard, per type; three sizings (seven types with no guard, under the guard, and with the institutional class under the guard); what the guard un-grades in the seven admitted types | FWD-3 (a basis somebody measured) | LOCAL | IB-pr-441, IB-pr-442, IB-pr-443 drained | P142-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~303. DIRECT-ACT (one read-only cell, LOCAL).

## 135. ROUND 143, WORKSTREAM ~P (2026-10-11 ~18:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5579)

2.0.0_SA_COO~G2's read-out of the eight leaves IB-pr-444 named (@07f11659ea): the firewall action class is `challenge` on both
probe arms while the page reads CH-AUTHENTICATED on seven steps and the session cookie's name is present; every probe went via
node-port. The CTO ruled the challenge CONFIRMED on the probe: the credentials are right, the browser is signed in, the account is
not locked. No cell that changes HOW the vendor is reached is cut; that question is put to Andrew. One read-only, code-only cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r143/p143_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-446` | what node-port is and why the probe uses it and not the page; whether the vendor calls a job makes after a capture go the same way; what changed on our side since the bundle of 2026-10-05, or that nothing did | FWD-4 (a session is usable only when verified from the transport that will use it) | LOCAL | IB-pr-444 drained | P143-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~304. DIRECT-ACT (one read-only cell, LOCAL).

## 136. ROUND 144, WORKSTREAM ~P (2026-10-11 ~19:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5611)

Row IRPT_ANLREQ-D2-W53-S3 ruled a RESULT: 21 of 28 live members of irpt-intake-poller have no blob in git, so the function serves
from bytes the tree cannot reproduce; its rollback target is the live package itself. The remedy is a release of the poller by
IRPT_BCKEND (cell IB-s-6), after one read; until then the live package is held once as the rollback artifact. Two cells, disjoint
write sets, no edge between them. The release itself is NOT cut here.

Check `deliverables/2.0.0_SA_COO~P2/checks/r144/p144_cells.py`: all six criteria FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-447` | does the running poller read firm_registry.json (read from the live package's bytes), which fields, and where each would come from under the naming canon's registry; what a release that drops the file would do | FWD-9 (intake) | LOCAL | none | P144-a |
| `IB-pr-448` | the live package held as the rollback artifact: its version id found among the artifact key's versions by content, or the order stops; nothing is written | FWD-9 (intake) | WORLD (declared; reads only, by an applier) | none | P144-b |

fanout: 2 of 2 chains, cap 8, reason: two independent cells. Assignees: 0.9.0_WK_IRPT_BCKEND~305 (IB-pr-447, DIRECT-ACT) and
0.7.0_AE_CloudOps~IB2 (IB-pr-448).

## 137. ROUND 145, WORKSTREAM ~P (2026-10-11 ~19:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5624 and PRD v0.40 @6d12b3dd65)

IB-pr-445 drained @7d31765674. The CTO adopted the unmoved-bar guard (PRD v0.40) and did not admit the institutional class: six of
its 71 outside securities repeat their bar on more than half their days, and nothing measured says what the bar is when it moves.
One read-only cell, counts only.

Check `deliverables/2.0.0_SA_COO~P2/checks/r145/p145_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-449` | for the overlap securities of the Inst and RIC/BDC Not Available pairs, the first moved bar after each repeated run, beside the anchor (five outcomes, no remainder); and the six institutional securities' moved days with their held rows against the bar | FWD-13 (a date label is measured, never assumed) | LOCAL | IB-pr-445 drained | P145-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~306. DIRECT-ACT (one read-only cell, LOCAL).

## 138. ROUND 146, WORKSTREAM ~P (2026-10-11 ~19:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5650)

PRD v0.40 and v0.41 both SIGNED: the guard is contract and may be built, nothing served. The read v0.40 names is IB-pr-449 (round
145, issued @b3500144f4 before msg 5650 arrived, amended @1286cbf961 with v0.41's count); it is not re-issued. The grading
instrument is not product code today (it is the measurement scripts in worker folders), so the guard lands as one pure function in
IRPT's gold folder with its tests; nothing imports it. A served change comes later under its own pair.

Check `deliverables/2.0.0_SA_COO~P2/checks/r146/p146_cells.py`: AC1-AC3 FAIL at base (no module).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-450` | `second_witness_grades(bars, t)`: true only with a bar on t, a bar on the calendar's prior trading day, and the two differing by more than relative 1e-4; with its tests | FWD-13 (a date label is measured, never assumed) | LOCAL | none | P146-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~307 (worker-light). DIRECT-ACT.

## 139. ROUND 147, WORKSTREAM ~P (2026-10-11 ~19:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5665)

Row DSGN_IRPTV1-D2-S21 ruled: the page carries the title for the 33 codes and maps the 12 unit tokens; no schema change now.
The producer's side owes one owner read confirming both on a SERVED vendor answer, key names only. One read-only cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r147/p147_cells.py`: AC1-AC3 FAIL at base (no record).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-451` | one owner read of a served vendor report's sections through the service principal: is there a title or label member, the section_type and units tokens with counts; key names only, GET only | FWD-5 (what a reader of a finished report is served) | WORLD (declared; reads only, by an applier) | none | P147-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 140. ROUND 148, WORKSTREAM ~P (2026-10-11 ~20:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5724 and PRD v0.42 @73d4348a31, signed @b05e8baee2)

IB-pr-449 drained @eb0c2d4890: 416 of 416 comparable first moved bars equal the anchor that day. v0.42 admits nine pairs under the
guard. The reviewer's note: five institutional securities have no anchor, so nothing shows their moved days are dated right. The
CTO rules a per-security exclusion on three numbers. One read-only cell, counts only.

Check `deliverables/2.0.0_SA_COO~P2/checks/r148/p148_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-452` | nine pairs sized under both guard sentences (blank share, never served, freed); the same with ADLYX, BISOX, EIBLX, GPPIX, OLCYX not graded by the second witness; how many securities of the nine pairs outside the first witness repeat on more than half their days | FWD-13 (a date label is measured, never assumed) | LOCAL | IB-pr-449, IB-pr-450 drained | P148-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~308. DIRECT-ACT (one read-only cell, LOCAL).

## 141. ROUND 149, WORKSTREAM ~P (2026-10-11 ~20:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5748)

Ruled on 2.0.0_SA_COO~G2's question: whether commentary was asked for is decided once, at acceptance, and carried on the accepted
record; the worker sends analysis_ready only with a ticket id AND that member true. The accepted record's contract changes, so the
CTO writes an addendum first, from one code-only read. Nothing is bound before that half lands. One read-only cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r149/p149_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-453` | which member of a submission, or of its ticket, says commentary is asked for today; where acceptance could read it; every reader of the accepted record and what each does with an absent or unknown member | FWD-4 (the vendor-path job and what it signals) | LOCAL | none | P149-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~309. DIRECT-ACT (one read-only cell, LOCAL).

## 142. ROUND 150, WORKSTREAM ~P (2026-10-11 ~20:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 5788 and 5800; PRD v0.43 @44828c43b8, signed @4c07d90a47)

IB-pr-452 drained @6a7b589f9e (nine pairs blank 43.9218 percent; the five cost 10 account-days; seven securities mostly repeat).
v0.43 adopts the repeated-share rule; the reviewer's note is that a rule over 'the grading run' is not reproducible. One build
cell: the instrument's product form with a FIXED trailing window, built and tested, nothing served, returning the window proposal,
the distribution in tenths and the rule's cost. The served change is a later pair.

Check `deliverables/2.0.0_SA_COO~P2/checks/r150/p150_cells.py`: AC1-AC3 FAIL at base (no module).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-454` | `date_basis_grading.py`: the ordered claim rule, the two witnesses, the nine pairs, the guard (imported) and the repeated-share rule over a fixed trailing window, as pure functions with tests; one read-only run returning the proposed window, the securities by share of repeated days in tenths, and the cost of the securities the rule takes | FWD-13 (a date label is measured, never assumed) | LOCAL | IB-pr-450, IB-pr-452 drained | P150-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~310. Not direct-act (above the size floor).

## 143. ROUND 151, WORKSTREAM ~P (2026-10-11 ~21:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5863; IRPT_YCDGEN PRD v0.13 @39c807e066, signed @6f8aeb03b7)

SERVICE FIRST: the worker's half is merged and dormant (@dddafd6832); the submission and acceptance half is IRPT_BCKEND's; the
form's half follows only after this half's release is live and read. One build cell here; its release pair is a later act and
names every reader of the accepted record with one read through each. Disjoint write set from IB-pr-454 (round 150, running).

Check `deliverables/2.0.0_SA_COO~P2/checks/r151/p151_cells.py`: AC1 FAIL, AC2 FAIL, AC3 PASS at base (AC3 is the control).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-455` | the submission's closed set admits the optional boolean `commentary_requested` and refuses any other type; acceptance copies it into the accepted record only when sent; the public contract declares it; a submission without it is accepted exactly as today | FWD-4 (the vendor-path job and what it signals) | WORLD (L6 floor: paths under infra/; nothing released) | the worker half merged @dddafd6832 | P151-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~311.

## 144. ROUND 152, WORKSTREAM ~P (2026-10-11 ~21:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5863)

IB-pr-455 drained @0322231fc8: the submission admits commentary_requested and acceptance carries it; nothing released. Its release
pair names every function, every moved member and every reader. One build-only cell with AWS reads is that read; no apply order
is cut here and none follows without a signed pair. Known entanglement: irpt-ycharts-generate's one-tree rebuild (IB-pr-426) is
merged and held on the CTO's word.

Check `deliverables/2.0.0_SA_COO~P2/checks/r152/p152_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-456` | every source-map entry packaging one of the three changed members (by subtraction), each built from a minimal candidate map and set beside live: moved members, riders, the minimal-release word; the entanglements; every reader of the accepted record re-counted at base with the pair's read through each; replay arms; the packet | FWD-4 (the vendor-path job and what it signals) | WORLD (live reads and builds; nothing uploaded) | IB-pr-455 drained | P152-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~312.

## 145. ROUND 153, WORKSTREAM ~P (2026-10-11 ~22:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 5896 and 5933; PRD v0.44 @84fec7b9b4, signed @7b75b691c1)

IB-pr-454 drained @ddf890e1f6: the grading module exists with no importer. v0.44 fixes the window at 40 trading days, floor 20.
The next cell is the producer's design as a READ, not a build: where the module would be called, what it would serve, every
consumer of the date-basis member; with one count the CTO asked for. Runs beside IB-pr-456 (round 152), disjoint write sets.

Check `deliverables/2.0.0_SA_COO~P2/checks/r153/p153_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-457` | the candidate call sites with their schedules and what each lacks; where each module input lives (a landed source of the second witness's bars, or none); every consumer of the date-basis member and of the gold it rides on, by subtraction, with the read a release makes through each; the security-days the short-history floor leaves ungraded split from the repeat rule's | FWD-3 (a return on that account's own end-of-day holdings) and FWD-13 | LOCAL | IB-pr-454 drained | P153-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~313. DIRECT-ACT (one read-only cell, LOCAL).

## 146. ROUND 154, WORKSTREAM ~P (2026-10-11 ~22:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 5993)

Ruled on 2.0.0_SA_COO~T2's question: the drafter learns the ticket id from the draft store's persist answer. That answer is a
contract, so the CTO writes an addendum first, from one code-only read. Runs beside rounds 152 and 153, disjoint write sets.

Check `deliverables/2.0.0_SA_COO~P2/checks/r154/p154_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-458` | the persist answer's members today per outcome and where its shape is declared; who invokes persist; every consumer of the answer by subtraction; whether the store reads the accepted record at persist; what the answer carries with and without a ticket id | FWD-4 (the vendor-path job and what it signals) | LOCAL | none | P154-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~314. DIRECT-ACT (one read-only cell, LOCAL).

## 147. ROUND 155, WORKSTREAM ~P (2026-10-11 ~23:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6004)

IB-pr-457 drained @01502183ee with ten open design questions. The CTO owes the producer's addendum and does not write it before
two facts. One read-only cell measures both. Runs beside rounds 152 and 154, disjoint write sets.

Check `deliverables/2.0.0_SA_COO~P2/checks/r155/p155_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-459` | (1) the landed prices store's yahoo-labelled points against the unadjusted Close for the 878 tickers, each ticker placed, with the store's writer, schedule and cadence; (2) the performance route reader's answer (days_excluded, claim, absences) for a window holding a non-OK day, by the reader's own code over the served gold, with a control | FWD-3 (a return on that account's own end-of-day holdings) | LOCAL | IB-pr-457 drained | P155-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~315. DIRECT-ACT (one read-only cell, LOCAL).

## 148. ROUND 156, WORKSTREAM ~P (2026-10-11 ~23:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 6024 and 6033; PRD v0.45 @9de9ab8cf2, signed @83e8664d75)

IB-pr-458 drained @ee2d9af09b: the draft store holds the ticket id at persist and returns only tenant and owner. v0.45: the first
OK persist answer carries ticket_id when the record has one, absent otherwise. The store first, the drafter second
(2.0.0_SA_COO~T2). One cell here: the build and the release read for the one function; its pair follows from the read. No apply
order is cut. Runs beside round 155, disjoint write sets.

Check `deliverables/2.0.0_SA_COO~P2/checks/r156/p156_cells.py`: AC1 FAIL, AC2 FAIL, AC3 PASS at base (AC3 is the control).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-460` | `commentary_draft_store.py`: the first-persist OK answer carries the record's ticket_id from the read it already makes, absent when the record has none; new tests, the existing test file untouched; then irpt-commentary-draft-store-lambda built from a minimal candidate beside live: moved members, riders, replay, the one consumer, the packet | FWD-4 (the vendor-path job and what it signals) | WORLD (L6 floor: paths under infra/; nothing released) | IB-pr-458 drained | P156-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~316.

## 149. ROUND 157, WORKSTREAM ~P (2026-10-11 ~23:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the signed pair of IB-pr-460 and CTO msg 6150)

IB-pr-460 drained @294566c734. COO half @39597f02ec; CTO half @7a2a9182a2, bound to the COO half's sha256, the crash-recovery
reading confirmed, its riders note withdrawn. One apply cell: one function, one member, no riders. The store first; the drafter's
switch is 2.0.0_SA_COO~T2's later pair.

Check `deliverables/2.0.0_SA_COO~P2/checks/r157/p157_cells.py`: AC1-AC3 FAIL at base (no record).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-461` | irpt-commentary-draft-store-lambda applied through safe-apply: who may invoke read first, precheck, a refused-shape before-read, the BUILD_ONLY digest equal to the signed one from a pin at or after the reader's revert, the plan for the one function, after-reads persisting nothing, the member on a real persist recorded UNEXERCISED LIVE; Branch B the recorded S3 version | FWD-4 (the vendor-path job and what it signals) | WORLD | IB-pr-460 drained; both halves signed | P157-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.7.0_AE_CloudOps~IB2.

## 150. ROUND 158, WORKSTREAM ~P (2026-10-12 ~00:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6192)

Site Z tracked four IRPT deploy ledger sentinels left OPEN 16 to 18 days ago (three by 2.0.0_SA_COO~P, one by 2.0.0_SA_COO~M),
relayed by 0.0.0_AB_MSTR~DELL2 msg 6190. The CTO ruled this lane inherits all four, to MEASURE and close, never to re-execute.
Each has exactly one open leg, a verify leg (read by the issuer @d68d9a5eda). One read-only cell.

Check `deliverables/2.0.0_SA_COO~P2/checks/r158/p158_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-462` | the four entries read from origin/box/sitez; each open leg's artifact measured now against what the leg was to produce, with a positive control; verdict SUPERSEDED (world-done, or overtaken and said so) or NOT_DONE with what is half-landed and since when; how and where a close is written; nothing re-executed | FWD-1 (the journey's releases are on record as landed or not) | LOCAL | none | P158-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~317. DIRECT-ACT (one read-only cell, LOCAL).

## 151. ROUND 159, WORKSTREAM ~P (2026-10-12 ~01:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6237)

Row TCKT_VNEXT-D2-S52 (2.0.0_SA_COO~V2): the portal authorizer's source in the tree is 188 lines ahead of the build input the
source map records as deployed; the added code is a render-token path this project's orders built (IB-rtq-2, IB-rtr-2, export
section A, IB-pr-307). The CTO reads the row as this lane's. One read-only cell; nothing is invoked, built or released.

Check `deliverables/2.0.0_SA_COO~P2/checks/r159/p159_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-463` | the live authorizer read by its bytes and matched by content to a commit's blob; the commits after it; how the function is packaged and whether the map's recorder sees it; every render-token sender and route with what it gets from the live authorizer today; the orders behind the unreleased commits; one verdict of four | FWD-7 (the export of what the advisor sees) | LOCAL | none | P159-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~318. DIRECT-ACT (one read-only cell, LOCAL).

## 152. ROUND 160, WORKSTREAM ~P (2026-10-12 ~01:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6245; PRD v0.46 @3f577ef37f, ratified-text half asked)

IB-pr-459 drained @9e2f9ef21e. PRD v0.46 is the date-basis producer's contract (ten design answers); nothing is served by it and
NO build cell is cut before three reads. Three read-only cells, disjoint write sets, no edge between them; (b) goes to the CTO
first. Reads need no signature; a build cell waits for the ratified-text half.

Check `deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py`: every criterion FAILs at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-464` | (b) the performance route's reader, per composed firm and per window: accounts with an excluded day, each placed first-day-only, interior-only, both, or last-day; the claim the reader gives them; what a non-OK row means | FWD-3 | LOCAL | none | P160-a |
| `IB-pr-465` | (a) whether the holdings-performance producer function's network reaches the vendor, from configuration; what a fetch would use; whether the package carries it | FWD-13 | LOCAL | none | P160-b |
| `IB-pr-466` | (c) the pages that render the route's returns, by subtraction over the portal checkout; what each shows of the claim, the absences and the excluded days; what the adapter drops | FWD-3 | LOCAL | none | P160-c |

fanout: 3 of 3 chains, cap 8, reason: three independent reads. Assignees: 0.9.0_WK_IRPT_BCKEND~319, ~320, ~321. DIRECT-ACT each.

## 153. ROUND 161, WORKSTREAM ~P (2026-10-12 ~02:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6315)

IB-pr-464 drained @03e9d0d4c2. The CTO ruled the first-day exclusions right and does not rule the interior and last-row ones
blind: a zero base (an empty account re-funded) and a negative or flagged-positive base need opposite rulings. One read-only
cell, the same code over the same gold, counts only. No build first.

Check `deliverables/2.0.0_SA_COO~P2/checks/r161/p161_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-467` | per firm entry and window, every interior and last-row excluded day by status token and by the prior day's ending value (zero, negative, positive, no prior row); the zero-run lengths; accounts all-zero-base against those with a negative or a flagged-positive base | FWD-3 (a return on that account's own end-of-day holdings) | LOCAL | IB-pr-464 drained | P161-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~322. DIRECT-ACT (one read-only cell, LOCAL).

## 154. ROUND 162, WORKSTREAM ~P (2026-10-12 ~02:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6362)

The other fabric's CTO ruled (@479d6deba0 on origin/box/dell1) that its demand queue lands the as-traded closes; this fabric
builds no lander and fetches no price. One read-only cell rebuilds the 878-ticker list (only its count was committed) and
writes the request file in the queue's format. The manager carries it; the quote goes to the CTO.

Check `deliverables/2.0.0_SA_COO~P2/checks/r162/p162_cells.py`: AC1-AC2 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-468` | the request file for the demand queue: 878 securities (symbol and cusip), tier 2, close, 125 trading days to 2026-10-09 by the trading calendar, plus enrolment in the standing daily extension; no price fetched | FWD-3 (a return on that account's own end-of-day holdings) | LOCAL | none | P162-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~323. DIRECT-ACT (one read-only cell, LOCAL).

## 155. ROUND 163, WORKSTREAM ~P (2026-10-12 ~03:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6379)

Rounds 161 and 162 drained (@49f2812ac8, @fd273706f4). The CTO ruled that what a vendor section's column IS becomes a wire
member of this project's contract, after one read. One read-only cell; no build before the member is signed.

Check `deliverables/2.0.0_SA_COO~P2/checks/r163/p163_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-469` | per section code (S01, S03, S18, S14, S15, S16) where the column's label is in the source and whether it is dropped or never read; one stored report's section ids counted by code, slug and column against the 36 the rule predicts for S18; every consumer of the section id's shape | FWD-5 (a finished report read by what each value is) | LOCAL | none | P163-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~324. DIRECT-ACT (one read-only cell, LOCAL).

## 156. ROUND 164, WORKSTREAM ~P (2026-10-12 ~03:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msgs 6414 and 6420)

PRD v0.48 (contract C-CHAINCLAIM) is signed. One read before its cell: the closed status set with counts, and whether a
NON-POSITIVE-BASE day belongs to an account that held positions the day before. No cell before the table reaches the CTO.

Check `deliverables/2.0.0_SA_COO~P2/checks/r164/p164_cells.py`: AC1-AC3 FAIL at base (no file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-470` | the status tokens the gold's producer can write, with each count over the served gold; per firm entry and window the NON-POSITIVE-BASE days by what the account held the prior day; the order of assignment against ALL-HOLDINGS-EXCLUDED; the accounts whose claim moves under the contract as written and under the other reading | FWD-3 (a return on that account's own end-of-day holdings) | LOCAL | IB-pr-467 drained | P164-a |

fanout: 1 of 1 chains, cap 8, reason: one cell. Assignee: 0.9.0_WK_IRPT_BCKEND~325. DIRECT-ACT (one read-only cell, LOCAL).

## 157. ROUND 165, WORKSTREAM ~P (2026-10-12 ~18:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6476 = PRD ADDENDUM v0.49 @6bed773b76 section 3)

The CTO's list has seven items. Items 3 to 7 are cut now (independent of the reader). Items 1 and 2 (C-CHAINCLAIM in the reader;
PARTIAL only when an absence holds) wait on the CVO's re-sign of the ratified-text half, by the CTO's word, and are cut in a
later issuance of this workstream as round 166 (one release under one never-widen pair). Item 3 and items 1-2 share
`performance/holdings_gold.py`; the later cut reads the merged file, so no two orders write it at once.

Check `deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py`: AC1-AC3 FAIL at base for IB165-1, -2, -3, -5 and for IB165-4 AC1 and AC3
(no file). IB165-4-AC2 PASSes at base BY DESIGN: it is the regression guard (the existing staging test, 5 passed, and test_build_only.sh, rc 0).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-471` | the opening/closing value members' names: every emitter and the wire contract, then a one-side producer rename only if the contract names them (PRD item 3, row W321-S1) | FWD-3 | WORLD (floor: infra path; nothing deployed) | none | P165-a |
| `IB-pr-472` | the extractor locates a label inside its own section's bounds, proven offline on a page that carries both labels (item 4, row W324-S2) | FWD-4 | WORLD (floor) | none | P165-b |
| `IB-pr-473` | the capture probe classifies a challenge as the READ path does; the probe pair runs only when the jar holds a token; the receipt keeps the probe's leaves per step (item 5, rows W302-S1/S2/S3, S85) | FWD-4 | WORLD (floor) | none | P165-c |
| `IB-pr-474` | `build-and-upload.sh` exits non-zero when a restore from HEAD fails and names the files left (item 6, row S72) | FWD-14 | WORLD (floor) | none | P165-d |
| `IB-pr-475` | two reads: `commentary_ref` at HEAD (row W309-S2); the prices store's writer and its schedule (row W315-S3) (item 7) | FWD-8, FWD-13 | LOCAL | none | P165-e |

fanout: 5 of 5 chains, cap 8, reason: five cells with disjoint write sets and no edge. Assignees: 0.9.0_WK_IRPT_BCKEND~326 to ~330 (one each).

## 158. ROUND 166, WORKSTREAM ~P (2026-10-12 ~19:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6503 = CTO ROUND-166 ANALYSIS section 3)

The CTO's list has six items; the ratified-text half is SIGNED current at v0.50 (prd-signoff read, status ADMITTED). Items 1 and 2 are ONE cell (one release under one never-widen pair, the same reader surface). Item 5 is cut as its first
step only: the CTO's own words are "bd_adapter's rename cut on that read", so this round reads every reader of `value_facts` (the portal included) and declares the contract's two members in both schema copies; the portal adapter's move and
the `bd_adapter` rename are cut in a later round on that read, ordered as one pair per the analysis section 2 (portal reads the contract members with a market-value fallback; `bd_adapter` renames; the fallback is removed).
`IB-pr-476` and `IB-pr-479` touch different objects of `PerformanceReport.schema.json` only if `IB-pr-476` needs a schema edit; it is not granted one (the two new integers ride in the open `value_facts` object).

Check `deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py`: AC1-AC3 FAIL at base for IB166-1, -3, -5 and IB166-2 AC1/AC3, IB166-4 AC1/AC2; IB166-2-AC2 and IB166-4-AC3 PASS at base BY DESIGN (regression guards).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-476` | the reader's claim by the excluded day's status (C-CHAINCLAIM, v0.48 as amended by v0.49 s1) with the two counts beside `days_linked`; PARTIAL only when an absence holds (row W321-S2); the claim-move counts reproduce the CTO's | FWD-3 | WORLD (floor: infra path; nothing deployed) | none | P166-a |
| `IB-pr-477` | a challenged stored-bundle probe ends the capture without a fresh sign-in (rows W328-S1, S109); the pair gate `discriminating !== true` (W328-S2) | FWD-4 | WORLD (floor) | none | P166-b |
| `IB-pr-478` | the packager reads `commentary_ref` from the item's sibling attribute, the record untouched; a round-trip test from the writer to the packager (row W309-S2) | FWD-8 | WORLD (floor) | none | P166-c |
| `IB-pr-479` | C-VALUEFACTS step 1: every reader of `value_facts` (backend and portal, read-only) and the two members declared in both schema copies (row W321-S1) | FWD-3 | WORLD (floor) | none | P166-d |
| `IB-pr-480` | every reader of the landed prices store under `investor-reporting/` and whether a served figure depends on it (row W315-S3) | FWD-13 | LOCAL | none | P166-e |

fanout: 5 of 5 chains, cap 8, reason: five cells with disjoint write sets and no edge. Assignees: 0.9.0_WK_IRPT_BCKEND~331 to ~335 (one each).

## 159. ROUND 167, WORKSTREAM ~P (2026-10-12 ~20:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6517 = PRD ADDENDUM v0.51 section 2 and ROUND-166 ANALYSIS section 3a)

PRD v0.51 withdrew v0.50's schema order (the frozen v1 contract does not move) and gave four items; the ratified-text half reads SIGNED current at v0.51 (prd-signoff, ADMITTED). Item 2 is the release of round 166's reader change, cut here as its build and never-widen PACKET only: the apply is a later order to `0.7.0_AE_CloudOps~IB2` once the pair is signed.
Item 3 is the C-VALUEFACTS pair in the CTO's order, reader first: the portal adapter candidate (step 1, `IB-pr-483`) and the `bd_adapter` rename (step 2, `IB-pr-484`); step 3 (the fallback removed at the pair's close) and the pair's packet are cut after both merge. Item 4 is two cells: the resident package change (`IB-pr-485`, a worker) and the CTO's "read first" of the live host's bindings (`IB-pr-486`, an order to the cloud-ops seat).

Check `deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py`: 14 of 18 criteria FAIL at base; IB167-1-AC2, IB167-3-AC2, IB167-4-AC2 and IB167-5-AC2 PASS at base BY DESIGN (regression guards).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-481` | both `PerformanceReport.schema.json` copies restored to their bytes at c16bf9d7bb^ (the frozen v1 contract; v0.50's schema bullet withdrawn) (row W334-S2) | FWD-3 | WORLD (floor: infra path; nothing deployed) | none | P167-a |
| `IB-pr-482` | `irpt-performance-adapter` rebuilt from one pin carrying the reader's claim change, and the never-widen packet printing the MOVES (49F 23/19/2/20; orion 750/76/7/106) with the REACH beside them (rows W331-S2) | FWD-3 | WORLD (declared; the later apply's reach) | none | P167-b |
| `IB-pr-483` | C-VALUEFACTS step 1, a PORTAL candidate: the adapter reads `start_value`/`end_value`, the market-value names kept for the Black Diamond path only | FWD-3 | LOCAL | none | P167-c |
| `IB-pr-484` | C-VALUEFACTS step 2: `bd_adapter.py` writes `start_value`/`end_value` | FWD-3 | WORLD (floor) | none (its apply waits on 483's landing) | P167-d |
| `IB-pr-485` | `ycharts/research` in the resident package's DIRS; a test resolves every import on both binding branches (row W333-S1) | FWD-8 | WORLD (floor) | none | P167-e |
| `IB-pr-486` | READ ONLY on the live host: whether the installed `resident_bindings.json` carries `commentary_ready_queue_url` (the CTO's read first) | FWD-8 | WORLD (a host read) | none | P167-f |

fanout: 6 of 6 chains, cap 8, reason: six cells with disjoint write sets and no edge. Assignees: 0.9.0_WK_IRPT_BCKEND~336 to ~340 (workers; ~338 is a portal cell) and 0.7.0_AE_CloudOps~IB2 (IB-pr-486).

## 160. ROUND 168, WORKSTREAM ~P (2026-10-12 ~21:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6559 = ROUND-168 ANALYSIS section 3)

The CTO's list has three items. Item 1 is the apply of round 167's IB-pr-482 release under the signed pair (COO half 21:03:15Z; CTO half msg 6557, Branch A): cut here as ONE order to `0.7.0_AE_CloudOps~IB2`, carrying the COO half's seven limbs and Branch B's rollback version named BEFORE the upload. Item 2 is the C-VALUEFACTS sequence, whose
every step starts only after the one before is read live: (a) the portal candidate `wk-IRPT_BCKEND-338-portal` @183860ba lands on DEV (the box manager's act, approved by the CTO), (b) a render of the Reporting tab on DEV against a holdings answer, (c) on Andrew's word, PROD, (d) the `bd_adapter.py` rename's own pair and apply, (e) the fallback's removal. Nothing in item 2 is cut now: (a) is the box manager's, (b) waits on (a), (c) is Andrew's.
Item 3 (W333-S1) is nothing to cut: the staging fix rides the next resident release.

Check `deliverables/2.0.0_SA_COO~P2/checks/r168/p168_cells.py`: AC1-AC3 FAIL at base (the re-pin has not landed; live is `kMB8xCI93/...`; no after-reads file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-487` | the apply of `irpt-performance-adapter` (built `abep4h7R...`, live `kMB8xCI93/...`) under the signed pair: ledger first, the one source-map re-pin, the rollback version named before the upload, the digest control, Terraform `safe-apply` on a 1-change planfile, the after-reads and the four direct-invoke arms (which persist named retained revisions) | FWD-3 | WORLD (a deploy) | IB-pr-482 merged and both halves signed | P168-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, an apply to a live seat. Assignee: 0.7.0_AE_CloudOps~IB2. Not a worker spawn.

## 161. ROUND 169, WORKSTREAM ~P (2026-10-12 ~23:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6660 = ROUND-169 ANALYSIS section 3)

The CTO's list has three items. Item 1 is the walker's `--firm` flag (the `/ui-walk` engine, `.claude/skills/ui-walk/walk.mjs`; no other live order names it: `comp-find` over the task orders reads 0 hits across 29,390 files). Item 2 is the live read that closes row D2-S114: one Inflection walk keeps its selection reference, and the deployed function is invoked once with it, the claim and the two counts compared with the reader's offline prediction. Item 3 is carried: the `bd_adapter.py` rename's APPLY waits until the portal reader is on PROD (Andrew's held promote `dell1-e7f2`), so nothing is cut for it; the DSGN_IRPTV1 fixture cell (row D2-W63-S1, routed by the CTO msg 6626) is cut as a fourth cell.

Items 1 and 2 are one chain: the walk (cell 2) needs the flag (cell 1); the live invoke (cell 3) needs the reference the walk keeps. The CTO's item 2 is cut as two cells because the executors differ (a worker walks; a CloudOps seat invokes a live function and persists up to two retained revisions).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py`, dry-run at the base: IB169-1 AC1 PASS (a bound), AC2 FAIL, AC3 FAIL; IB169-2 AC1 FAIL, AC2 PASS (a bound), AC3 FAIL; IB169-3 AC1-AC3 FAIL; IB169-4 AC1 FAIL, AC2 PASS (a bound), AC3 PASS in a clean worktree. IB169-1-AC2 was also run on a patched copy (PASS) and a patched copy that accepts `--firm` with no label (FAIL).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-488` | the walker gains `--firm "<label>"` (select the header Firm option by its visible label; `FIRM_OPTION_ABSENT` if absent) and `--first-client` (pick the first search result under that firm) | FWD-3 | LOCAL | none | P169-a |
| `IB-pr-489` | one walk `--firm Inflection --first-client --performance-state` keeps ONE `sel_` reference outside any git tree and leaves the walker disarmed | FWD-3 | SERVED (arms a dormant service account in `opal-users-v2`, reads live data through the local build) | IB-pr-488 | P169-a |
| `IB-pr-490` | one direct invoke (at most two windows, at most two retained revisions) of the deployed `irpt-performance-adapter` with that reference; claim equals the offline prediction, both counts present; closes D2-S114 | FWD-3 | SERVED (a live function read that persists named retained revisions) | IB-pr-489 | P169-a |
| `IB-pr-491` | the producer's two `AnalysisReport` contract fixtures send a section the extractor can send (row D2-W63-S1) | FWD-3 | WORLD (the gate floor for an `infra/` path) | none | P169-b |

fanout: 2 of 2 chains, cap 8, reason: chain P169-a is a queue (cells 1 and 2 to worker slot ~341, cell 3 to `0.7.0_AE_CloudOps~IB2` after the walk is drained); chain P169-b is one fixture cell (worker slot ~342).

## 162. ROUND 170, WORKSTREAM ~P (2026-10-13 ~02:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6739 = ROUND-170 ANALYSIS section 4, and the CTO's DSGN_IRPTV1 round 32 and 33 analyses section 2a and 1)

The CTO's list is carried, nothing new: (1) the PRODUCER pair for DSGN_IRPTV1 rows D2-S28, D2-W69-S1 and D2-W72-S2: a last-four search returns the ACCOUNT entry, each 49 Financial ACCOUNT node carries an `account_id` member (the directory's id, additive), and the pair's packet carries a read-only COUNT of 49F accounts whose node id differs from the directory's account id, per state (served / refused / withheld), denominator printed, no id in any file; (2) the fixture follow-up of row D2-W63-S1: the portal's wire copy and generated fixtures; (3) C-VALUEFACTS's rename APPLY, which waits for the portal reader on PROD (`e7f2`, Andrew's held promote), so nothing is cut for it. D2-S121 (the left-out branch, offline-proven only) is non-blocking and cuts no cell: this seat reads the first organic Inflection answer with `days_with_return_left_out` above 0 at its next tick that sees one.

The producer item is cut as THREE build cells, not one: the search producer (`irpt-directory-search`, a Lambda), the node member (the gold-runner builder plus the HoldingsSnapshot contract and its fixture, whose staged copies two Lambdas pin), and the read-only count. Their APPLIES and the never-widen pair are NOT cut now: a served member added to a contract needs its own pair (COO half and CTO half), and the staged schema copies make the source-map pins of `irpt-holdings` and `irpt-ycharts-generate` stale the moment the docs copy changes (the apply order re-pins them first, as IB-pr-487 did).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py`, dry-run at the base: IB170-1 AC1 FAIL, AC2 FAIL, AC3 PASS (a bound: the existing directory suite reads 173 passed, 10 failed, 28 errors at base); IB170-2 AC1 FAIL, AC2 FAIL, AC3 PASS (a bound: 22 builder tests and 24 contract tests pass); IB170-3 AC1-AC3 FAIL; IB170-4 AC1 FAIL (29 files carry the old tokens), AC2 PASS (a bound: 21 portal tests pass), AC3 FAIL. IB170-1-AC2 was also run against a throwaway reference implementation of the behaviour: PASS.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-492` | the directory search producer returns an ACCOUNT entry when the query matches an account's tail (and resolve accepts that entry) | FWD-3 | WORLD (the gate floor for an `infra/` path; build only, no deploy) | none | P170-a |
| `IB-pr-493` | an additive `account_id` member on each 49F ACCOUNT node: the builder, `HoldingsSnapshot` schema (three copies), fixture, `raw_keys.json` | FWD-3 | WORLD (floor; build only) | none | P170-b |
| `IB-pr-494` | the read-only COUNT of 49F accounts whose node id differs from the directory's, per state | FWD-3 | SERVED (a read of served custody and directory data; counts only) | none | P170-c |
| `IB-pr-495` | the portal's AnalysisReport wire copy and generated fixtures carry the extractor's section form (a portal candidate for DEV; its PROD rides `e7f2`) | FWD-3 | LOCAL | none (the producer fixtures are merged: IB-pr-491) | P170-d |

fanout: 4 of 4 chains, cap 8, reason: four disjoint write sets (the directory Lambda folder; the gold-runner builder and contract files; a records-only count; the portal fixtures folder), no edge between them.

## 163. ROUND 171, WORKSTREAM ~P (2026-10-13 ~04:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6764 = ROUND-171 ANALYSIS section 2, and the CVO's v0.52 ratified-text review @cab1de19b0)

The CTO's list has three items. Item 1, FIRST: the 49F temp-file cell (row D2-W345-S3: the live builder copies the Tax membership snapshot, which carries client account numbers, to a system temp file and never removes it) with the one read of the host's temp space (counts only, a person deletes what is found), and the declared-key correction of D2-W344-S2 in the same builder cell. Item 2: the producer pair in the CVO's ORDER: both packaged `HoldingsSnapshot` copies re-pinned and deployed BEFORE the builder first writes `account_id`, then the builder's `account_id` (merged in round 170, IB-pr-493), the last-four ACCOUNT entry (merged, IB-pr-492) and the 49F node/account mismatch count (measured, IB-pr-494). This round BUILDS and PACKETS the two functions whose artifacts change: `irpt-holdings` (the staged schema copy) and `irpt-directory-search` (`handler.py`); their APPLIES are the next round's orders under the signed pair. NOT cut now: `irpt-ycharts-generate`'s re-pin of the same schema (the CTO ruled: IRPT_ANLREQ's reader release goes FIRST on that function and this re-pin follows it, or rides it if that pair names it: its baseline is moving; owner me, condition: that release landed); the host-bundle deploy of the builder's `account_id` (the gold-runner bundle's own pair: after the two Lambdas). Item 3: the portal generator repair (D2-W346-S2, S3) and the `selected_sections` alignment (D2-W346-S4).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py`, dry-run at the base: all twelve build criteria FAIL as expected (IB171-1 AC1 no test file, AC2 the leak reproduced offline with a stub S3, AC3 holdings_source names the smartx map; IB171-2, -3 and -4 no records; IB171-5 AC2 `S-ALLOC-2` unresolved, AC3 15 fixtures carry the old section in the main portal checkout); IB171-5-AC1 (it runs the generators) is dry-run in a throwaway portal worktree, not the shared checkout.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-496` | the builder reads or removes the Tax snapshot (no temp file left on return or raise; an operator-owned env-var file kept); `raw_keys.json` cites the live mint | FWD-3 | WORLD (the `infra/` floor; build only) | none | P171-a |
| `IB-pr-497` | ONE read-only count (and ages) of leftover snapshot temp files on the runner host(s), by SSM, no names, no contents, no delete | FWD-3 | SERVED (a read on a host holding client-bearing files) | none (the file-name suffix is known from the code) | P171-b |
| `IB-pr-498` | `irpt-holdings` rebuilt with the schema copy that admits `account_id`, and its never-widen packet | FWD-3 | WORLD (floor; build only) | none (IB-pr-493 merged) | P171-c |
| `IB-pr-499` | `irpt-directory-search` rebuilt with the tail-to-ACCOUNT handler, its reach per firm and its never-widen packet | FWD-3 | SERVED (reads the landed directory counts) | none (IB-pr-492 merged) | P171-d |
| `IB-pr-500` | the portal's `fe-s-15` and `fe-s-18` generators reproduce their committed bytes; `selected_sections` resolves | FWD-3 | LOCAL | none | P171-e |

fanout: 5 of 5 chains, cap 8, reason: five disjoint write sets (the gold-runner builder and `raw_keys.json`; a records-only host read; one Lambda's candidate build; another Lambda's candidate build; the portal fixtures and generators), no edge between them. Four worker spawns (slots ~347 to ~350) and one order to `0.7.0_AE_CloudOps~IB2`.

## 164. ROUND 172, WORKSTREAM ~P (2026-10-13 ~04:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6783 = ROUND-172 ANALYSIS section 4)

The CTO's list has three items. Item 1: read which packaged `HoldingsSnapshot` copies are validated at serve, then their minimal re-pin, then the builder's `account_id` (the CTO ruled `irpt-holdings` NOT re-pinned: it does not validate at serve; TARGET serving and the `multi_asset` enum change are their own pairs, and the frozen-v1 enum finding is routed to dell1's MDPF_SECCLASS owner). Item 2: the fe-s-18 truth decision (the committed bytes the portal's tests consume) and the generator repair (rows W350-S1, W346-S3). Item 3: the host bundle carrying the temp-file fix, when the host is next Online.

CUT now: the READ of item 1 (`IB-pr-501`) and item 2 (`IB-pr-502`). NOT cut now, with the reason and the condition: the minimal re-pin and the builder's `account_id` apply (they depend on the verdict of `IB-pr-501`, an unmet dependency inside the round; the next round cuts them from the record, owner me); the `irpt-ycharts-generate` leg also waits on IRPT_ANLREQ's reader release; `irpt-directory-search` apply (the signed pair, after the CVO's re-sign); item 3, the host bundle (rides the next host bundle; the host is stopped and a start for a read alone is not cut; condition: the host Online).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py`, dry-run at the base: IB172-1 AC1, AC2, AC3 FAIL (no record; a synthetic record passes all three and a contradicting `validated_at_serve` fails AC3); IB172-2 AC3 FAIL (no record), AC2 PASS at base (28 pass, 8 skip, 0 fail: a regression guard), AC1 (runs the generator) fails at base by round 171's trial and is dry-run in a throwaway portal worktree, not the shared checkout.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-501` | a READ of which functions package the `HoldingsSnapshot` schema copy and which validate against it at serve, with the minimal re-pin members | FWD-3 | LOCAL | none | P172-a |
| `IB-pr-502` | the portal's `fe-s-18` generator reproduces the committed bytes the portal's tests consume, with the decision record | FWD-3 | LOCAL | none | P172-b |

fanout: 2 of 2 chains, cap 8, reason: two disjoint write sets (a records-only read; one portal test-folder generator), no edge between them. Two worker spawns (slots ~352 and ~353).

## 165. ROUND 173, WORKSTREAM ~P (2026-10-13 ~05:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6798 = ROUND-173 ANALYSIS section 2)

The CTO's list has three items. Item 1: the export envelope fixture correction (row D2-W353-S5: the FIXTURE moves; the frozen envelope gains `facts.covered_account_ids`, synthetic ids, validated against the v1 schema, the generator reproducing it). Item 2: the `irpt-holdings` pass-through replay, then which packaged copies validate at serve (DONE in round 172: neither does), then the builder's `account_id` with its host bundle (which also carries the 49F temp-file fix, when the host is next Online). Item 3: the fe-s-18 truth decision and generator repair, carried (the repair is built and merged on the workspace side in round 172; the portal candidate awaits the DEV review lane).

CUT now: the pass-through replay (`IB-pr-503`) and the fixture correction (`IB-pr-504`). NOT cut now, with the reason and the condition: the builder's `account_id` host-bundle deploy (it depends on the verdict of `IB-pr-503`, an unmet dependency inside the round, and on the host being Online for the bundle that also carries the temp-file fix; the next round cuts it as a never-widen pair, owner me); the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign); the repair of the no-op report validator in the ycharts generate composition (row W352-S1; the CTO: before any path calls it, none does yet).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r173/p173_cells.py`, dry-run at the base: IB173-1 AC1, AC2, AC3 FAIL (no record, no script); IB173-2 AC3 FAIL ("covered_account_ids is a required property"; a temporary edit adding the member passes it, restored), AC2 PASS at base (28 pass, 8 skip, 0 fail: a regression guard), AC1 (runs the generator) fails at the portal DEV base by round 171's trial and is dry-run in a throwaway worktree.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-503` | an OFFLINE replay of the packaged `irpt-holdings` serve path on a synthetic snapshot whose ACCOUNT node carries `account_id`, a node without it and a node with an unknown member | FWD-3 | LOCAL | none | P173-a |
| `IB-pr-504` | the frozen export envelope carries `facts.covered_account_ids` (synthetic ids), validated against the v1 `ExportReceipt` schema, and the generator reproduces it | FWD-3 | LOCAL | round 172's generator repair (merged; the portal branch `wk-IRPT_BCKEND-353-portal` @e1cd356e2f is fast-forwarded into the worker's portal worktree) | P173-b |

fanout: 2 of 2 chains, cap 8, reason: two disjoint write sets (a records-only replay; one portal generator and one fixture), no edge between them. Two worker spawns (slots ~354 and ~355).

## 166. ROUND 174, WORKSTREAM ~P (2026-10-13 ~05:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6812 = ROUND-174 ANALYSIS section 2)

The CTO's list has three items. Item 1: the builder validates its own output against the repository's v1 schema before it writes, with a planted-member test (row D2-W354-S2), and the contract line "enforced at build; not at serve". Item 2: the portal wire union and type to the contract's enum, `multi_asset` included (row D2-S127), a portal candidate through the CTO's review lane, DEV only. Item 3, carried: the fe-s-18 generator repair (built and merged on the workspace side in rounds 172 and 173; the portal candidates await the DEV review lane) and the builder's `account_id` with its host bundle (which also carries the 49F temp-file fix), when the host is next Online.

The issuer's read before cutting: the builder ALREADY validates (`validate_snapshot` in `holdings_snapshot.py`, called in the build path before the refusal logic and as the `validate=` hook of `land`) and refuses a planted ACCOUNT-node member (probed offline on the contract's valid fixture). So item 1 is a READ plus the missing PROOF (a test), with no product-code edit unless the read finds an unvalidated write path (then a row). The contract line is the PRD's (the schema is generated from the PRD CONTRACTS table): sent to the CTO, not cut.

CUT now: `IB-pr-505` (the read and the planted-member test) and `IB-pr-506` (the portal wire union and type). NOT cut now, with the reason and the condition: the builder's `account_id` host-bundle deploy (a never-widen pair; the host is stopped and the bundle also carries the temp-file fix: condition, the host Online; owner me); the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign); the repair of the no-op report validator in the ycharts generate composition (row W352-S1; before any path calls it, none does yet).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r174/p174_cells.py`, dry-run at the base: IB174-1 AC1 and AC3 FAIL (no test file, no record), AC2 PASS at base (a regression guard on the validator); IB174-2 AC1 FAIL (IVE48-AC1 fails), AC2 FAIL (1212 pass, 5 fail in the shared portal checkout), AC3 FAIL (no test file).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-505` | READ of the build path's validation before any write, and the planted-member test (a stray member refuses the build, zero puts) | FWD-3 | LOCAL | none | P174-a |
| `IB-pr-506` | the portal wire union and type follow the contract's enum, `multi_asset` with a plain fallback label; `IVE48-AC1` passes | FWD-3 | LOCAL | none | P174-b |

fanout: 2 of 2 chains, cap 8, reason: two disjoint write sets (a gold-runner test and a records read; the portal wire type and holdings tab), no edge between them. Two worker spawns (slots ~356 and ~357).

## 167. ROUND 175, WORKSTREAM ~P (2026-10-13 ~07:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6829 = ROUND-175 ANALYSIS section 3)

The CTO's list has three items. Item 1: the builder host bundle's never-widen pair (the 49F temp-file fix plus the builder's `account_id`), applied at the runner host's next SCHEDULED Online (no seat starts the host for it). Item 2: the import-order repair of the tolerance test (row D2-W356-S3). Item 3: the combined portal candidate to the CTO's review lane (DONE this round before the cut: approved RE 6832, landed on portal DEV as e50a1379 by the box manager, receipt msg 6834, CI success), with the fe-s-18 truth carried.

CUT now: `IB-pr-507` (a READ-ONLY census of the host bundle) and `IB-pr-508` (the import-order repair). NOT cut now, with the reason and the condition: the pair itself (the sign-off packet and the apply order) depends on the census: the guard declares twelve bundle members and `holdings_49f.py` and `holdings_inf.py` are not among them, so how the builder files reach the host, and which members the live object holds against HEAD, is unknown until `IB-pr-507` is read (an unmet dependency inside the round); the next round cuts the packet from the record, owner me; its APPLY is gated by the host's next scheduled Online (CTO RE: no start for it), and its first read is the leftover temp-file count (counts only). Also not cut: the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign) and the repair of the no-op report validator in the ycharts generate composition (row W352-S1; none calls it yet).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r175/p175_cells.py`, dry-run at the base: IB175-1 AC1, AC2, AC3 FAIL (no record; a synthetic record naming the twelve guard members passes AC1 and AC2); IB175-2 AC1 FAIL (0 passed, 1 collection error), AC2 FAIL (rc 2), AC3 FAIL (no record).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-507` | a READ-ONLY census of the investor-reporting host bundle (the live S3 object against HEAD, member by member, and how the host reads it) | FWD-3 | SERVED (a read of the object that decides what the host runs) | none | P175-a |
| `IB-pr-508` | the tolerance test's import order repaired so the three builder suites run together | FWD-3 | LOCAL | none | P175-b |

fanout: 2 of 2 chains, cap 8, reason: two disjoint write sets (a records-only AWS read; one gold-runner test file), no edge between them. Two worker spawns (slots ~359 and ~360).

## 168. ROUND 176, WORKSTREAM ~P (2026-10-13 ~07:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6844 = ROUND-176 ANALYSIS section 2)

The CTO's list has three items. Item 1: the per-firm holdings package census (read-only): which firms, the S3 keys `IRPT_HOLDINGS_BUNDLE_MAP` names (`refresh_dispatch.py:65`), each package's members against HEAD, the commits since each object was written, denominators printed (row D2-W359-S1; the CTO said yes in RE 6838). Item 2: the host-bundle pair on that census, naming exactly the packages and members the release needs (the 49F temp-file fix and the `account_id` builder), every other member at today's bytes, applied at the runner host's next scheduled Online (no start for it). Item 3, carried: the import-order repair (W356-S3), DRAINED in round 175 (`89af2d14e4`).

CUT now: `IB-pr-509` (the census). NOT cut now, with the reason and the condition: the pair (item 2) depends on the census record (which packages exist, which members differ and which commits explain them: an unmet dependency inside the round); the next round cuts it from the record, owner me; its apply is gated by the host's next scheduled Online and its first read is the leftover temp-file count (counts only). Also not cut: the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign) and the repair of the no-op report validator in the ycharts generate composition (row W352-S1; none calls it yet).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r176/p176_cells.py`, dry-run at the base: IB176-1 AC1, AC2, AC3 FAIL (no record); a synthetic record naming the three BUILDERS firms with the guard's 45 closure members at HEAD hashes passes all three (removed).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-509` | a READ-ONLY census of the per-firm `investor-reporting-holdings.tar.gz` packages (the bundle map against the guard, each package's members against HEAD, where the two merged changes land) | FWD-3 | SERVED (a read of the packages that decide what the host runs) | none | P176-a |

fanout: 1 of 1 chains, cap 8, reason: a single records-only AWS read with no sibling cell. One worker spawn (slot ~361).

## 169. ROUND 177, WORKSTREAM ~P (2026-10-13 ~08:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on CTO msg 6863 = ROUND-177 ANALYSIS section 2)

The CTO's list has two items. Item 1: the host-bundle pair: ONE minimal package per firm (the live package's members by hash plus only the temp-file fix and the `account_id` builder member(s); the four unattributed live members carried unchanged and named by path and sha256), applied at the runner host's next scheduled Online (no start for it); the pair prints each package's member diff against live and a scratch-install read; rollback per firm is the live object version (CTO RE 6859). Item 2: the provenance read (S3 metadata and the CloudTrail `PutObject` event per package object; a line diff of the four members against their nearest historical blob) and the evidence archive of the four members (row D2-W361-S3 (b), (c)), not blocking the pair.

CUT now: `IB-pr-510` (the three minimal candidate packages BUILT, censused, scratch-installed, with the never-widen packet and the COO half) and `IB-pr-511` (the provenance read and the evidence archive). NOT cut now, with the reason and the condition: the APPLY (an order to `0.7.0_AE_CloudOps~IB2` under the signed pair, at the host's next SCHEDULED Online; the pair needs the CVO/CTO halves signed first, an unmet dependency inside the round; owner me; condition: pair signed and the host's scheduled start) and its first read, the leftover temp-file count (counts only; a person deletes any found, row D2-W345-S3); also not cut: the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign) and the repair of the no-op report validator in the ycharts generate composition (row W352-S1).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r177/p177_cells.py`, dry-run at the base: IB177-1 and IB177-2 AC1, AC2, AC3 FAIL (no record). Positive control for IB177-1-AC2: a synthetic replaced member (holdings_49f.py at 135fc3509e against its parent) passes the hunk-subset test with the commit declared.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-510` | three minimal per-firm holdings packages built from the live objects plus only the allowed commits' hunks (BUILD ONLY), their member diff against live, a scratch install, and the never-widen packet | FWD-3 | WORLD (host code that writes served data; build only) | none (the census record IB176-1 is merged) | P177-a |
| `IB-pr-511` | READ-ONLY provenance of the three package objects (S3 metadata, CloudTrail PutObject) and the evidence archive of the four unattributed live members | FWD-3 | SERVED (a read of the objects that decide what the host runs) | none | P177-b |

fanout: 2 of 2 chains, cap 8, reason: two disjoint write sets (the candidate packages and packet; the provenance record and the archive), both reading the same three live objects and writing none. Two worker spawns (slots ~362 and ~363).

## 170. ROUND 178, WORKSTREAM ~P (2026-10-13 ~08:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's RE 6867 = "cut the apply order with that step", the round-177 analysis (msg 6863) and the signed pair IB-pr-510)

The pair IB-pr-510 is signed by both halves at the packet sha256 `c2b7275939d0` (COO half @aa1ffa367e, CTO half @eec092e994). The CTO asked for the apply order with one added step: the applier confirms, BEFORE any write, that the runner role is admitted by the bucket policies of `opal-data-49financial` (which carries two PutBucketPolicy writes by another fabric's agent user, 2026-10-11) and `opal-data-inflection`; not admitted = STOP, and the policy goes to ADVI_FIRMBKTS through `0.0.0_AB_MSTR`. The apply is gated by the host's next SCHEDULED Online; no seat starts the host for it (CTO round-176 and round-177 rulings); its first read is the leftover temp-file COUNT.

CUT now: `IB-pr-512` (the apply, to `0.7.0_AE_CloudOps~IB2`, which is live and idle). The CTO's formal round-178 analysis has not arrived at this writing; this cell is cut on the CTO's explicit RE 6867 and is the only act the signed pair leaves open. NOT cut: the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign), the repair of the no-op report validator in the ycharts generate composition (row W352-S1), and any cell that depends on the apply's first read (the leftover-file count may produce a human act, a delete of client-bearing temp files, raised then).

Check `deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py`, dry-run at the base: IB178-1 AC1, AC2, AC3 FAIL (no record); a synthetic apply record built from the IB-pr-510 record's live and candidate values and the packet's stamp passes all three (removed).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-512` | the APPLY of the signed pair: two per-firm holdings packages put at the host's next scheduled Online, digest-gated, step 0 on the bucket policies first, then the first read | FWD-3 | WORLD (writes two S3 objects the host runs; rollback per key) | the signed pair (done); the host's scheduled Online (a clock the order waits on without starting it) | P178-a |

fanout: 1 of 1 chains, cap 8, reason: one applier, one act. Not a spawn: the order is addressed to a live seat.

## 171. ROUND 179, WORKSTREAM ~P (2026-10-13 ~14:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's RE 6992 = "round 179 = IB-pr-513, one read-only count after a build")

The round-178 apply (IB-pr-512) put the two minimal holdings packages; IB2's first leftover-file count (0 and 0, ~13:37Z) preceded any build on them, so row D2-W345-S3 (the 49F builder leaves a client-bearing temp file) stays ARMED. The CTO ruled (RE 6992): ONE read-only count after a real build that ran on the new packages, today if the host is Online, else at its next scheduled Online; the wait is qualified because a driven build would write served output outside its schedule. PASS: 0 leftover Tax snapshot temp files after a build that ran on the new packages; the build is named (start time and the package digest it ran); positive control: the build's own log line showing it took the snapshot path; W345-S3 disarms on PASS. The formal round-179 analysis follows the CVO's compile of round 178.

CUT now: `IB-pr-513` (to `0.7.0_AE_CloudOps~IB2`). NOT cut: the `irpt-directory-search` apply (the signed pair, after the CVO's re-sign); the repair of the no-op report validator in the ycharts generate composition (row W352-S1); the provenance of the three package objects beyond CloudTrail's management events (not established: not worth a cell now).

Check `deliverables/2.0.0_SA_COO~P2/checks/r178/p178_cells.py` cell IB178-2, dry-run at the base: AC1, AC2, AC3 FAIL (no record).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-513` | ONE read-only count of leftover snapshot temp files on the runner host after a real build that ran on the new packages, the build named | FWD-3 | SERVED (a read on a host that may hold client-bearing files) | IB-pr-512 (done); a real scheduled build on the new package; the host Online | P179-a |

fanout: 1 of 1 chains, cap 8, reason: one applier, one read. Not a spawn: the order is addressed to a live seat.

## 172. ROUND 180, WORKSTREAM ~P (2026-10-13 ~15:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's RE 7016 = round 180: item 1 the served 49F account_id read, then item 2 the directory-search apply)

The `account_id` line: the builder's host packages are live (round 178) and the temp-file fix is shown clean (round 179, row S136). The CTO ordered (RE 7016): item 1, read-only and counts only, the latest served 49F HoldingsSnapshot built on `UHOCIkWj` (ACCOUNT nodes total; those with `account_id`; those whose `account_id` is in the landed directory population; those without, by reason; the negative arm is the pre-release snapshot reading 0 with `account_id`); item 2, the `irpt-directory-search` apply under its signed pair, AFTER item 1 passes. The formal analysis follows the CVO's compile.

CUT now: `IB-pr-514` (item 1). NOT cut now, with the reason and the condition: item 2, the directory-search apply (it is ordered after item 1 passes: an unmet dependency inside the round; it also needs the CVO's re-sign of PRD v0.53's ratified-text half for the signed pair to stand at the current bytes; owner me; condition: IB-pr-514 passes and the pair re-reads as signed); the repair of the no-op report validator in the ycharts generate composition (row W352-S1).

Check `deliverables/2.0.0_SA_COO~P2/checks/r180/p180_cells.py`, dry-run at the base: IB180-1 AC1, AC2, AC3 FAIL (no record); a synthetic record in a path the run created itself passes all three (path removed).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-514` | READ-ONLY, counts only: the latest served 49F snapshot built on the new package: ACCOUNT nodes total, with `account_id`, in the directory population, without by reason; the pre-release snapshot as the negative arm | FWD-3 | SERVED (a read of a client-bearing served snapshot, counts only) | none (IB-pr-512 done) | P180-a |

fanout: 1 of 1 chains, cap 8, reason: one read with no sibling cell. One worker spawn (slot ~364).

## 173. ROUND 181, WORKSTREAM ~P (2026-10-13 ~16:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's RE 7037 = "round 181 = the directory-search apply, step 0 reads which home it reads; no home moves")

Round 180 item 1 passed (7639 of 7640 49F ACCOUNT nodes carry `account_id`, all in the landed directory; row S137). Item 2 is the `irpt-directory-search` apply under its signed pair. **The pair is not signed and its digest is stale:** the packet `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-499.md` (both halves UNSIGNED) names the live zip at CodeSha256 `TefVhmG...` (2026-10-12T14:06Z), but IRPT_ANLREQ's status-rule release (ledger `irpt-status-rule-all-eight-20261013`, `last_deployed_commit` `1b88b22dea`) redeployed `irpt-directory-search` at 2026-10-13T12:34:28Z; the live CodeSha256 is now `tvrsQ+w820jp...` (the source map row records it); a second deploy ledger, `irpt-status-rule-exercise-20261013` (0.7.0_AE_CloudOps~AQ2, 6 legs), names the function too. An apply by the old packet's digest gate would STOP, and the sequencing law (an act naming a function another OPEN ledger names waits for it to read CLOSED) holds it behind AQ2.

CUT now: `IB-pr-515` (a BUILD-ONLY re-census of the candidate against the CURRENT live, step 0 per the CTO's RE 7037 on the directory home, the open ledgers, the replay and reach, and a refreshed packet). NOT cut now, with the reason and the condition: the APPLY itself (both halves of the refreshed pair signed at the packet's bytes, the open ledger(s) CLOSED and step 0 matching: an unmet dependency inside the round; owner me); the repair of the no-op report validator in the ycharts generate composition (row W352-S1).

Check `deliverables/2.0.0_SA_COO~P2/checks/r181/p181_cells.py`, dry-run at the base: IB181-1 AC1, AC2, AC3 FAIL (no record); synthetic records in a path the run created itself (live sha256 taken from the source map) pass all three; path removed.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-515` | `irpt-directory-search` candidate rebuilt and censused against its CURRENT live, step 0 (which directory home the function reads, against the builder's), the open deploy ledgers naming it, the replay and reach, and the refreshed never-widen packet | FWD-3 | SERVED (reads the live function and the landed directories; builds only) | none (round 171's candidate and arms are the prior art) | P181-a |

fanout: 1 of 1 chains, cap 8, reason: one rebuild with no sibling cell. One worker spawn (slot ~365).


## 174. ROUND 182, WORKSTREAM ~P (2026-10-13 ~17:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the signed pair IB-pr-515 (COO half; CTO half @01d0a01db9, msg 7098) and Andrew's word at this seat, row D2-S140: "Your CTO on this box can handle Call 1")

Round 181 built and censused the refreshed candidate (order 515 @23fb169341) and left the apply behind three gates. All three read met at the artifact (row D2-S141): both halves signed at packet sha256 `3c369b9086b3...`; the CTO's condition 3(a) (the built `handler.py` over every landed directory: 7,694 + 884 + 863 = 9,441 ACCOUNT entries, 0 with a null, empty or absent account id; positive control reads 1); no open deploy marker names the function (0 of 271 files on 15 readable worktrees); the live CodeSha256 is unchanged (`tvrsQ+w82...`).

CUT now: `IB-pr-516`, the APPLY to `0.7.0_AE_CloudOps~IB2` by the Terraform path, digest-gated, with Branch B named before the first upload and one synthetic tail search through the deployed function. NOT cut now: the repair of the no-op report validator in the ycharts generate composition (row W352-S1), the latent `served`/`enforce` attribute mismatch (W349-S1, identical on live and built), and any IB-pr-456 step (waits on Andrew's execution ID).

Check `deliverables/2.0.0_SA_COO~P2/checks/r182/p182_cells.py`, dry-run at the base: IB182-1 AC1, AC2, AC3 FAIL (no record); a synthetic record in a temp root the run created itself passes all three, one defect per arm fails that arm, and the root is removed.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-516` | `irpt-directory-search` moved to the signed built digest (`handler.py` only) by the module's Terraform path and `safe-apply`, then one synthetic-directory tail search and its resolve through the deployed function | FWD-3 | WORLD (moves a client-facing search) | none (the pair and the three gates above) | P182-a |

fanout: 1 of 1 chains, cap 8, reason: one apply with no sibling cell; the seat is the live `0.7.0_AE_CloudOps~IB2` (no worker spawn).


## 175. ROUND 183, WORKSTREAM ~P (2026-10-13 ~19:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-183 analysis (msg 7149) and its addition (msgs 7178 and 7189: "key the catalogue entries by Opal model identity; the YCharts id is an optional vendor mapping"))

Round 182 closed (the directory-search apply landed; ledger closed; CVO compile v83). Round 183 carries two threads. (1) IB-pr-456's after-read and apply, **NOT cut now: an unmet dependency (Andrew's PROD execution ID is the BEFORE record; no placeholder is admissible); it is cut in the round after the ID arrives; owner me.** (2) The O1 hop the CTO added: the comparison catalogue lacks the Opal Ultra Short-Term model (Y2's read `0.9.0_WK_IRPT_ANLREQ~86/r22/ULTRA_SHORT_TERM_READ.json`: `templates.json` `comparison_catalog.entries` holds 4 of the 5 models the Model Portfolios page lists).

Measured before the cut (rows D2-S148 and D2-S149): no seat can read a YCharts model identity (the gateway search returns nothing even for Opal Short-Term, the positive control), so the cell does not use one; the composition requires a `vendor_id` FIELD and a code-pinned per-key policy digest, not a YCharts id, so an entry in namespace OPAL carrying Opal's own model code (`UST`) passes it; the YCharts path reads `catalog[k]["security_id"]` (`recipe.py` in `validate_envelope`), so it needs a stated refusal for an unmapped entry. Scope: the five models the Model Portfolios page lists (UST, ST, INT, LT, ULT); Fixed Income and the two 50/50 blends are declared in the portal's colour map and are NOT in that served list, so they are recorded, not added.

CUT now: `IB-pr-517` (BUILD only, in a worktree): the new entry, the canonical order, the pin, the YCharts-path refusal and the tests. NOT cut now, with the condition: the census and never-widen packet for the function(s) that package `templates.json`, `maintained_sources.py` and `recipe.py` (round 184, after this builds; a build order carries at most three criteria and the packet is its own cell), and the apply.

Check `deliverables/2.0.0_SA_COO~P2/checks/r183/p183_cells.py`, dry-run at the base: IB183-1 AC1, AC2, AC3 FAIL; a positive control in a temp tree the run created itself (the change applied by hand) passes AC1 and AC2 and the refusal arm of AC3; the temp tree removed.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-517` | Opal Ultra Short-Term added to the comparison catalogue keyed by Opal's own model identity (namespace OPAL, code UST, no YCharts id), the five models in canonical order, its policy pin, the YCharts path's stated refusal of an unmapped entry, and the tests | FWD-1 (O1 hop) | WORLD (the gate infers the floor from the infrastructure path templates.json; this order is BUILD ONLY and applies nothing) | none | P183-a |

fanout: 1 of 1 chains, cap 8, reason: one build with no sibling cell. One worker spawn (slot ~366).


## 176. ROUND 184, WORKSTREAM ~P (2026-10-13 ~21:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-184 analysis (msg 7233: "the census and never-widen packet for the function that packages the catalogue, then the pair, then the apply; IB-pr-456 on Andrew's execution ID"))

Round 183 built the catalogue release (IB-pr-517 @0d0e9e1229). Round 184's list has two items. (1) The census and never-widen packet for the function that packages it: **CUT now** as `IB-pr-518`. The issuer measured the package first (row D2-S151): the function is `irpt-ycharts-generate`; the release moves `templates.json` (native) and `maintained_sources.py` (staged at a pin: one source-map row) and must not move `recipe.py` (its live bytes are not the repo's current blob); the CTO's text named only `templates.json`, and the packet names the real set. (2) IB-pr-456's after-read and apply: **NOT cut now: an unmet dependency (Andrew's PROD execution ID is its BEFORE record and has not arrived); cut in the round after it arrives; owner me.** NOT cut and not owed here: the pair's two halves and the apply (they follow the packet, in later rounds, one order per round); the four custody tests that fail at base (queued behind O1/O2 by the CTO, named in each pair).

Check `deliverables/2.0.0_SA_COO~P2/checks/r184/p184_cells.py`, dry-run at the base: IB184-1 AC1, AC2, AC3 FAIL (no records); positive control in a temp root the run created itself (a copy of the real source map, synthetic records) passes all three, each negative (a third changed member, a stale live digest, a packet without the recipe.py statement or the current live digest, an altered copy admitted) fails its own arm; root removed.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-518` | `irpt-ycharts-generate` censused and rebuilt against its CURRENT live with the catalogue release (two members, one source-map row in scratch), the four arms, the open ledgers, and the never-widen packet | FWD-1 (O1 hop) | SERVED (reads the live function and the source map; builds only) | IB-pr-517 (merged) | P184-a |

fanout: 1 of 1 chains, cap 8, reason: one census with no sibling cell. One worker spawn (slot ~367).


## 177. ROUND 185, WORKSTREAM ~P (2026-10-13 ~23:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-185 analysis (msg 7305) and the signed pair IB-pr-518 (COO half @d06ee1f0fc, CTO half @f7bd0b5b7e, msg 7310 "cut the apply"))

Round 184 closed (IB-pr-518 @414adbfdc0). The CTO's round-185 list has three items. (1) The catalogue apply on the signed pair: **CUT now** as `IB-pr-520`, to `0.7.0_AE_CloudOps~IB2`. (2) The export re-pin (row D2-S152): **CUT now** as `IB-pr-519`, a BUILD-ONLY census and packet for `irpt-export-render` with the stored-receipt count and the branch rule of RE 7262; the root cause was found read-only before the cut (the live function writes `facts.covered_account_ids` but packages a stale `ExportReceipt.schema.json`). (3) IB-pr-456's after-read and apply: **NOT cut now: an unmet dependency (Andrew's PROD execution ID is its BEFORE record; open call `f61b`); cut in the round after it arrives; owner me.** NOT cut and not owed here: the pair for the export re-pin (a later round, after its packet), and the `account_activity_daily` backfill (the CTO queued it behind these).

Two cuts, independent chains: the apply moves `irpt-ycharts-generate` and the export census reads `irpt-export-render`; they share no file and no function. Both orders carry one WORLD or SERVED class decided by the gate's floors (the apply: WORLD; the census: SERVED, paths under org/ only).

Check `deliverables/2.0.0_SA_COO~P2/checks/r185/p185_cells.py`, dry-run at the base: IB185-1 and IB185-2 AC1, AC2, AC3 all FAIL (no records); positive controls in temp roots the runs created themselves pass all three of each cell, and fourteen negatives each fail their own arm; roots removed.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-520` | `irpt-ycharts-generate` moved to the signed built digest (`templates.json` and `maintained_sources.py`; the form's model order changes) by its Terraform path, digest-gated, then a health proof with no invoke | FWD-1 (O1 hop) | WORLD (moves a client-facing catalogue) | the signed pair IB-pr-518 (both halves) | P185-a |
| `IB-pr-519` | `irpt-export-render` censused and rebuilt against its CURRENT live with ONE staged contract re-pinned, the stored-receipt count (dry run), the four arms, the open ledgers, and the never-widen packet | FWD-1 (O1 hop) | SERVED (reads the live function, the source map and the receipt store; builds only) | none | P185-b |

fanout: 2 of 2 chains, cap 8, reason: two independent chains. One worker spawn (slot ~368) and one live seat (`0.7.0_AE_CloudOps~IB2`).


## 178. ROUND 186, WORKSTREAM ~P (2026-10-13 ~23:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-186 analysis (msg 7355) and the signed pair IB-pr-519 (COO half @b667f38d96, CTO half @a047ade972))

Round 185 closed (IB-pr-520 applied; IB-pr-519 census and packet @295d98d389; packet @a47c87446b to the CVO). The CTO's round-186 list has three items. (1) The IB-pr-519 apply on its signed pair: **CUT now** as `IB-pr-521`, to `0.7.0_AE_CloudOps~IB2` (the receipt store is re-read at its start; a receipt lacking the field is a STOP). (2) IB-pr-456 on Andrew's execution ID: **NOT cut now: an unmet dependency (the ID is its BEFORE record; open call `f61b`); it re-censuses against the new live bytes `xP47NQDn` when it is cut; owner me.** (3) The `account_activity_daily` backfill, "census and pair first, under the 2012 floor": **CUT now as the census** `IB-pr-522` (read-only; the issuer read the writer first: the Lambda `irpt-reporting-gold` has an explicit backfill event bounded per invocation, `handler.py` lines 20-40, 118-119, 519-600); NOT cut and not owed here: the backfill's pair and its runs (later rounds, after the census packet).

Two cuts, independent chains: the apply moves `irpt-export-render`; the census reads the gold tables and the repository and writes nothing.

Check `deliverables/2.0.0_SA_COO~P2/checks/r186/p186_cells.py`, dry-run at the base: IB186-1 and IB186-2 AC1, AC2, AC3 all FAIL (no records); positive controls in temp roots the runs created themselves pass all three of each cell, and fourteen negatives each fail their own arm; roots removed. The first control run of IB186-2 found my own rename slip (a sed that rewrote the word tempfile in the control script); repaired before the cut.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-521` | `irpt-export-render` moved to the signed built digest (one schema member) by its Terraform path, digest-gated, the one stored receipt validated offline against the DEPLOYED schema, a health proof with no invoke | FWD-1 (O1 hop) | WORLD (moves a client-facing receipt read) | the signed pair IB-pr-519 (both halves) | P186-a |
| `IB-pr-522` | the `account_activity_daily` backfill censused: writers counted, tables per firm, demand under the 2012 floor, the observed rate, the plan and its packet; reads only | FWD-3 | SERVED (reads listings, logs and the repository; writes only the worker's records) | none | P186-b |

fanout: 2 of 2 chains, cap 8, reason: two independent chains. One worker spawn (slot ~369) and one live seat (`0.7.0_AE_CloudOps~IB2`).


## 179. ROUND 187, WORKSTREAM ~P (2026-10-14 ~01:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-187 analysis (@718356ee39, msg 7389): ruling 1 Design (B) for the 49F activity backfill; ruling 2 Cottonwood and Inflection activity per the Opal Shape)

Round 186 closed (IB-pr-521 applied; IB-pr-522 census @a377bb4d49; packet @4556bc40d4). The CTO's round-187 list has three items. (1) The 49F activity backfill, Design (B), "the code change and its never-widen pair": **CUT now the CODE CHANGE** as `IB-pr-523` (a BUILD-only order: the backfill event gains a `stages` key; an activity-and-lots-only run never writes returns or class); the pair (census, packet, signed halves) and the apply and the chunked runs are later cells (one order per round per cell; the pair needs the built candidate first). (2) IB-pr-456 on Andrew's execution ID: **NOT cut now: an unmet dependency (open call `f61b`); it re-censuses against the then-live `irpt-ycharts-generate`; owner me.** (3) The one read cell for Cottonwood and Inflection: **CUT now** as `IB-pr-524` (read only: the landed transaction source of each firm and its mapping to the `account_activity_daily` shape; no new vendor pull). NOT cut and not owed here: the producer build for the two firms (after the mapping is read), the two per-firm censuses and pairs.

Two cuts, independent chains: the build changes `reporting-gold/handler.py` and one new test file offline; the read lists prefixes and reads code.

Check `deliverables/2.0.0_SA_COO~P2/checks/r187/p187_cells.py`, dry-run at the base: IB187-1 and IB187-2 AC1, AC2, AC3 all FAIL (no new tests and the default event runs the returns under a lots-only request; no record); positive controls pass all three of each cell (IB187-1 in a throwaway git worktree at HEAD with my own hand implementation: 95 tests; IB187-2 in a temp root); eleven negatives each fail their own arm; control roots removed. The first control attempt in a partial copy of the tree failed 34 tests for want of the repository's other modules: the control moved to a real worktree.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-523` | the reporting-gold backfill event gains a `stages` key: absent runs all stages as today, exactly ["lots"] runs the activity and lots stages only (no compute, no returns emit, no class emit), anything else is refused by name; tests; offline build only | FWD-3 | WORLD (the gate infers the floor from the infrastructure path; the order is BUILD ONLY and applies nothing) | the census IB-pr-522 (merged) | P187-a |
| `IB-pr-524` | the landed transaction sources of Cottonwood and Inflection read, each shape column mapped, derived or marked absent, per firm; reads only | FWD-3 | SERVED (reads listings and the repository; writes only the worker's records) | none | P187-b |

fanout: 2 of 2 chains, cap 8, reason: two independent chains. Two worker spawns (slots ~370 and ~371).


## 180. ROUND 188, WORKSTREAM ~P (2026-10-14 ~02:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-188 analysis (@f82cf22b5c, msg 7418): Inflection serves with the two gain columns ABSENT; "your list accepted, in order")

Round 187 closed (IB-pr-523 the Design-B code change @0009c27ae2; IB-pr-524 the COT/INF read @8dfd755758; packet @754b9f4570). The CTO's round-188 list has three items. (1) The Design-B census and packet for the 49F function, "the pair proves 0 returns partitions changed": **CUT now** as `IB-pr-525` (a BUILD-only census of `irpt-49f-reporting-gold-lambda` with a returns baseline, the four offline arms on the BUILT zip's bytes, and ONE packet for the two acts the pair signs: the code release and the chunked runs). (2) The IR holdings class rule (row D2-S156): the CTO's order is "the count of holdings that move per firm, then the build from ONE shared definition, then its pair": **CUT now the COUNT** as `IB-pr-526` (read only, per firm, from each firm's served snapshot); the BUILD depends on the count (its premise: what moves and where the shared definition must reach), so it is **NOT cut now: an unmet dependency inside the round; owner me; cut next round.** (3) IB-pr-456 on Andrew's execution ID: **NOT cut now: an unmet dependency (open call `f61b`); it re-censuses against the then-live `irpt-ycharts-generate`; owner me.** NOT cut and not owed here: the Cottonwood and Inflection activity producers (the CTO queued them next).

Two cuts, independent chains: the census reads the live function and S3 listings of one firm; the count reads three firms' served snapshots and code. Neither writes or invokes anything.

Check `deliverables/2.0.0_SA_COO~P2/checks/r188/p188_cells.py`, dry-run at the base: IB188-1 and IB188-2 AC1, AC2, AC3 all FAIL (no records); positive controls in temp roots the runs created themselves pass all three of each cell, and seventeen negatives each fail their own arm; roots removed. The control's first packet was too short for the check's 4,000-character floor (a control slip, repaired).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-525` | `irpt-49f-reporting-gold-lambda` censused and rebuilt against its CURRENT live with the stage-selection change (one changed member), the four arms on the built bytes, the returns baseline (a digest over the returns prefix's keys and ETags), and the never-widen packet for the release and the chunked runs; builds only | FWD-3 | SERVED (reads the live function and S3 listings; builds only; org/ paths) | IB-pr-523 (merged) | P188-a |
| `IB-pr-526` | the IR holdings class rule's count: per firm, the served holdings that carry a cash-type sub_asset_class but a class other than cash (the ones the shared rule would move), with their public tickers; reads only | FWD-3 | SERVED (reads served snapshots into memory, counts only out) | none | P188-b |

fanout: 2 of 2 chains, cap 8, reason: two independent chains. Two worker spawns (slots ~372 and ~373).


## 181. ROUND 189, WORKSTREAM ~P (2026-10-14 ~03:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-189 analysis (@318056547a, msg 7467): Cottonwood's lost account read; the IR holdings class rule built and packaged)

Round 188 closed (IB-pr-525 @368dd470e4, IB-pr-526 @05d5a8d786; packet @0c5677447a; the CVO's adjudication v89 dismissed 10 rows, nothing applied). The CTO's round-189 list has two items and three carried. (1) The read of Cottonwood's one lost account (ruling call 3, step 1): **DONE by the issuer THIS tick as a DIRECT-ACT** (LOCAL, under the size floor; reads of the refusal record, three landed directories and six silver tables in memory, counts and a hash prefix out): `deliverables/2.0.0_SA_COO~P2/COTTONWOOD_LOST_ACCOUNT_READ_20261014.md`, row D2-S160. Its finding is branch 3 as the CTO ruled (not closed, not re-keyed, missing from the allocations feed since 2026-10-09), plus two questions only the CTO can rule; **no dependent cell is cut** (a branch-2 pair needs the CTO's word that a zero-value account dropped from the feed counts as left). (2) The IR holdings class rule, built and packaged, no apply: **CUT now as two cells**: `IB-pr-527` the BUILD (one shared rule at the canonical-row return of `classify_security`, canonical-only because FDRXX resolves on the canonical branch: row D2-S161, a scan of the canonical table) and `IB-pr-528` the COUNT BY LAYER, the FDRXX-on-Inflection node check and the never-widen packet. Carried and **NOT cut, each with its owner and condition**: IB-pr-456 (waits on Andrew's execution ID, open act `f61b`; owner me); the Design-B CTO half and its runs (the CTO's call 1: the backfill waits for FWD-21's builder to read `account_activity_daily`; also behind D2's held thresholds-swap ledger, read at 11:41Z); the Cottonwood and Inflection activity producers (under IRPT_DASHBD round 101's read cell).

Two cuts, independent chains: the build is offline code and tests; the count reads served snapshots, the canonical table and S3 listings. Neither writes or invokes anything.

Check `deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py`, dry-run at the base: IB189-1 AC1, AC2, AC3 and IB189-2 AC1, AC2, AC3 all FAIL (no rule, no test file, no record); positive controls (a throwaway `git worktree add --detach` and a temp root, both created and removed by the run) pass all three of each cell, and negatives each fail their own arm (eight for the build, twelve for the count). One control slip: the first synthetic packet was below the check's 3,000-character floor (repaired in the control).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-527` | the shared cash rule built: `apply_cash_rule` called once at the canonical-row return of `classify_security`; a Cash sub serves the cash class on the canonical branch only; tests; builds only | FWD-3 | LOCAL (offline code and tests; no served byte; not an infrastructure path) | IB-pr-526 (merged) | P189-a |
| `IB-pr-528` | the movers split by layer (canonical branch / fallback branch) per firm against IB-pr-526's upper bounds; the FDRXX-on-Inflection node check; the never-widen packet for the rule's later release; reads only | FWD-3 | SERVED (reads served snapshots, the canonical table and S3 listings; writes only the worker's records) | IB-pr-526 (merged) | P189-b |

fanout: 2 of 2 chains, cap 8, reason: two independent chains. Two worker spawns (slots ~374 and ~375).


## 182. ROUND 190, WORKSTREAM ~P (2026-10-14 ~04:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-190 analysis (@6e527b13c6, msg 7498): one cash rule on both layers; the directory exemption repair; the producer census)

Round 189 closed (IB-pr-527 @dff35d95da, IB-pr-528 @e09575dde1; packet @4b1f71d676; the CVO's adjudication v90 dismissed 7 rows and put the cross-page question, which the CTO ruled). The CTO's round-190 list has four items. (1) The cash rule on the fallback layer: **CUT now** as `IB-pr-529` (the same `apply_cash_rule` at the fallback return of `classify_security`, with tests). (2) The exemption repair: **CUT now** as `IB-pr-530` (the all-UNKNOWN test reads source-marked statuses only; a replay through the real gate). (3) The producer census: **CUT now** as `IB-pr-531` (read only: schedule, bundles, code hashes, release path, rollback by manifest version, and the S71 reconciliation). (4) One packet for one release of the producer carrying both changes, counted per change per firm from the producer's own rules on the newest candidate: **NOT cut now: an unmet dependency inside the round** (it counts the movers of the fallback rule and the candidates the repaired exemption would publish, which need the two builds merged, and its Branch A needs the census); **owner me; cut next round (191).** Carried and NOT cut, each with its owner and condition: IB-pr-456 (waits on Andrew's execution ID, open act `f61b`; owner me), and the Design-B CTO half (the CTO's round-188 call 1; owner the CTO).

Three cuts, independent chains: two offline builds on `holdings_snapshot.py` in different functions (`classify_security`, `directory_marks_no_closures`) with disjoint test files except that IB-pr-529 rewrites one test in the existing `test_holdings_cash_rule.py`; and a read-only census. Neither build writes or invokes anything; the census reads.

Check `deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py`, dry-run at the base: IB190-1, IB190-2 and IB190-3 AC1, AC2, AC3 all FAIL; positive controls (a throwaway `git worktree add --detach` for the two builds and a temp root for the census, created and removed by the run) pass all three of each cell, and negatives each fail their own arm (eleven for IB190-1 and IB190-2 together fail on the arm they test, eleven for the census). Two control slips caught and repaired in the control, not the check: the test-count floor of the fallback build (the rewritten test counts once: 109, not 110) and the control's first run of the rewritten test.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-529` | `apply_cash_rule` also at the fallback return of `classify_security` (one definition, two call sites), its old "fallback unchanged" test rewritten and three added; builds only | FWD-3 | LOCAL (offline code and tests; no served byte; a data/assets path) | IB-pr-527 (merged) | P190-a |
| `IB-pr-530` | `directory_marks_no_closures` ignores the entries the directory builder carries forward and reads source-marked statuses only, with a replay through the real gate; builds only | FWD-3 | LOCAL (offline code and tests; no served byte) | none | P190-b |
| `IB-pr-531` | the holdings producer's deployment censused: runner, dispatch, schedule, the three served standalone bundles (version, sha256, whether they carry the rule), release path and ledger rule, rollback by manifest version per firm, the S71 reconciliation; reads only | FWD-3 | SERVED (reads the live schedule, served bundles and manifest versions; writes only the worker's records) | none | P190-c |

fanout: 3 of 3 chains, cap 8, reason: three independent chains. Three worker spawns (slots ~376, ~377 and ~378).


## 183. ROUND 191, WORKSTREAM ~P (2026-10-14 ~05:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-191 analysis (@10401d0134, msg 7531): the packet and the pair for one holdings-producer release)

Round 190 closed (IB-pr-529 @1464de48be, IB-pr-530 @4db49e0a27, IB-pr-531 @ace53f9692; packet @07aa5b57d2; the CVO's adjudication v91 dismissed 9 rows). The CTO's round-191 list has two items. (1) Read 49financial's failed 2026-10-09 fire before any blast radius is signed: **DONE by the issuer as a DIRECT-ACT this round** (LOCAL reads of SSM command history and one index, counts and dates out): rows D2-S164 (the command TIMED OUT and its process was killed, exit 137) and D2-S165 (the next fire did not recover it: 49financial's served series has NO 2026-10-08 row; the dates present each carry a manifest pointer with a hash); the gap is inlined into the next cell as a key the release must not widen or hide. (2) The never-widen packet and the COO half for ONE release carrying both changes, counted per firm and per change by running the producer's own rules on each firm's newest candidate: **CUT now** as `IB-pr-532` (the census's `--mint-bundle` release, the NEVER-2 ledger the releasing seat opens, the stop rule on both branches). **My COO half is not a cell: I write and sign it at the packet's sha256 after the cell merges.** The CTO signs on receipt; the apply is round 192. Carried and NOT cut, each with its owner and condition: IB-pr-456 (Andrew's execution ID, open act `f61b`; owner me) and the Design-B CTO half (the CTO's round-188 call 1).

One cut, one chain: the cell depends on the merged builds (IB-pr-527, -529, -530) and the merged census (IB-pr-531), all in the tree; the 49financial gap it needs is already measured.

Check `deliverables/2.0.0_SA_COO~P2/checks/r191/p191_cells.py`, dry-run at the base: IB191-1 AC1, AC2, AC3 FAIL (no record, no packet); the positive control (a temp root the run created and removed) passes all three and the negatives each fail their own arm (fifteen). Two control slips caught and repaired in the control, not the check: the synthetic packet was below the check's 4,000-character floor twice.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-532` | the release's movers counted per firm and per change by running the producer's own rules over each firm's newest candidate (the cash rule built twice over the same inputs, the gate evaluated before and after the exemption repair), and the never-widen packet for ONE `--mint-bundle` release with Branch A, Branch B, the 49financial 2026-10-08 gap, the releasing seat's NEVER-2 ledger and the stop rule; reads only | FWD-3 | SERVED (builds candidates from served sources, reads served publications and directories; writes only the worker's records) | IB-pr-527, IB-pr-529, IB-pr-530, IB-pr-531 (all merged) | P191-a |

fanout: 1 of 1 chains, cap 8, reason: one cell; the two items of the CTO's list are one direct read (done) and one order. One worker spawn (slot ~379).


## 184. ROUND 192, WORKSTREAM ~P (2026-10-14 ~06:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-192 analysis (@296869062d, msg 7551): the release and its business-date condition; why select_business_date answers the current day; 49financial's missing day)

Round 191 closed (IB-pr-532 @a33cb9b030; packet @26d98874cb; the CVO's adjudication v92 put the business-date question; the CTO signed his half at the packet's sha256 `4129abf31f3d` and added condition 8). The CTO's round-192 list has three items. (2) Why `select_business_date()` answers the current day before the session: **DONE by the issuer as a DIRECT-ACT** (LOCAL, code reads and a calendar positive control): row D2-S167 (the function returns the CUTOFF, today when a trading day; the published date is the newest source partition at or before the cutoff, T-1 only because partitions land after the close; nothing refuses a source partition dated today). (1) The release (apply) under the signed pair with condition 8: **NOT cut now: an unmet dependency inside the round.** Its stop rule compares the release's re-measured movers with the packet, and the scratch harness that measured them is deleted and its inputs were not pinned, so a re-measure on a later candidate (the 2026-10-13 sources land overnight) would differ for reasons that are not the code; the release's comparison needs a committed, replayable harness (cell `IB-pr-533`). The apply order (a CloudOps seat, WORLD) is cut the round after `IB-pr-533` merges; **owner me**. The release window is open until the 14:15Z scheduled fire, then the next trading day; I tell the CTO this reading of condition 4 (a replay on pinned inputs is the comparison; the date condition is checked separately on the then-newest candidates) in the same tick. (3) 49financial's missing 2026-10-08: **CUT now** as `IB-pr-534` (the timeout numbers and the one-date replay packet; the replay itself runs after the release's after-read under its own pair). Carried and NOT cut: IB-pr-456 (Andrew's execution ID, open act `f61b`; owner me) and the Design-B CTO half (the CTO's round-188 call 1).

Two cuts, independent chains: a read-only harness and its pinned replay; a read-only SSM and code read with a packet. Neither writes or invokes anything.

Check `deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py`, dry-run at the base: IB192-1 and IB192-2 AC1, AC2, AC3 all FAIL (no harness, no record, no packet); positive controls (a temp root with a copy of the trading calendar, created and removed by the run) pass all three of each cell, a record naming a real deviation from the packet also passes, and the negatives each fail their own arm (twenty-seven). No control slip this round.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-533` | the release re-measure harness committed and replayed twice per firm on a pinned source date (movers by layer, the gate before and after the exemption repair, lost accounts listed, a digest of the pinned source receipts), compared with the signed packet with its deviations named, and the first-fire business-date check recorded against the trading calendar; reads only | FWD-3 | SERVED (builds candidates from served sources and reads served publications; writes only the worker's records) | IB-pr-532 (merged) | P192-a |
| `IB-pr-534` | 49financial's SSM execution timeout and the durations of its latest ten or more fires, whether the 2026-10-08 sources exist, and the one-date replay packet (what it writes, that every other date is untouched, the gate's answer to an older date and the route that needs, rollback); reads only | FWD-3 | SERVED (reads SSM history, the dispatcher's configuration and served listings; writes only the worker's records) | IB-pr-531, IB-pr-532 (merged) | P192-b |

fanout: 2 of 2 chains, cap 8, reason: two independent chains. Two worker spawns (slots ~380 and ~381).

## 185. ROUND 193, WORKSTREAM ~P (2026-10-14 ~13:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-193 analysis (@e9dabffe7b, msg 7614) and the signed pair IB-pr-532 (both halves at sha256 4129abf31f3d))

Round 192 closed (IB-pr-533 @866f3e94d6, IB-pr-534 @40201b2539; packet @a93d73e6e8; CVO adjudication v93 6 of 6 PASS). The CTO's round-193 list has three items, all CUT now. (1) The release apply under the signed pair with the per-firm rules (Step 0 pins each firm to its packet's custody partition, Inflection on 2026-10-13; the business date graded PER FIRM at the fire; a wrong stamp is a STOP and a late firm never rolls the others back): `IB-pr-535`, to `0.7.0_AE_CloudOps~IB2`, minted from a detached worktree at the release pin 49467335d2 so no cell of this round can ride into the bundles. The issuer re-measured Inflection at the 2026-10-13 pin before the cut (774 canonical + 67 fallback, PUBLISHED before and after, 0 listed: equal to the packet). (2) The `as_of` assertion on the bypass path: `IB-pr-536`, an offline build (a flag no scheduled fire passes, the assertion block, the one-firm one-date waiver of `source_frontier_older` only, a mutant that fails). (3) The cause of the 2026-10-09 kill: `IB-pr-537`, read, to the same seat (it needs a read-only host command; the verdict decides one step of the apply). The round-191 erratum the CTO asked for rides the round-193 drain-end packet.

Not cut and why: the 2026-10-08 replay itself (it follows `IB-pr-536`, the release's after-read and its own signed pair; the packet is re-written on the bypass path in a later round); IB-pr-456 (Andrew's execution ID, open act f61b, still unmet).

Check `deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py`, dry-run at the base: IB193-1, IB193-2 and IB193-3 AC1, AC2, AC3 all FAIL (no records, no new test, no marker block); positive controls in temp roots the runs created themselves (a stub producer in a throwaway git repo, synthetic records, a copy of the trading calendar; control script `control193.py`) pass all nine, and twenty-three negatives each fail their own arm. The first control pass found two slips of mine, both in the control and the check, not the cells: a changed-paths comparison that counted the worker's own record, and a mutant test that failed for the wrong reason; both repaired before the cut.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-535` | the three standalone holdings bundles minted from the release pin under the signed pair: gates, the re-measure on per-firm pins, Branch B re-read, the digest gate, the seat's ledger, the three mints, the business date stated per firm, the first fire read per firm (T-1 stamp or a named hold), the Cash rows and the 2026-10-08 gap | FWD-3 | WORLD (moves the code of the scheduled holdings fires for three firms) | the signed pair IB-pr-532 (both halves); IB-pr-537 (its verdict decides the memory-read step) | P193-a |
| `IB-pr-537` | the cause of the 2026-10-09 kill read from the host's own record: OOM, not OOM, or unreadable (at most two read-only host commands) | FWD-3 | SERVED (reads SSM history and one runner host) | none | P193-a |
| `IB-pr-536` | the one-firm, one-date operator bypass of `source_frontier_older` with the landed-date-equals-as_of assertion and its mutant; offline build only | FWD-3 | LOCAL (offline code and tests; no served byte) | none | P193-b |

fanout: 2 of 2 chains, cap 8, reason: the apply and the kill-cause read are one chain (one seat, the read first; the apply reads its verdict), the bypass build is independent. One live seat (`0.7.0_AE_CloudOps~IB2`) and one worker spawn (slot ~382).

## 186. ROUND 194, WORKSTREAM ~P (2026-10-14 ~14:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-194 analysis (@c601d6a13a, msg 7667) and the CVO slug for round 193 (adjudication v94))

Round 193 closed (IB-pr-537 @a792d9c31e, IB-pr-536 @b80e382520; IB-pr-535 STOPPED at its digest gate, cancelled; packet @b18f769b46). The CTO's round-194 list has three items. (1) Packet v2, the FULL pin mint characterized (route (a), ruled): **CUT now** as `IB-pr-538`, a READ-ONLY worker cell: each firm's moved-member table (one class per member, recomputed from git by the check), the trading-calendar delta and the T-1 old against new for the next three fires, the write addresses old against new (a change is a STOP), the added matcher's importer, and the harness re-measure at the pin. (2) The apply under packet v2: **NOT cut now: an unmet dependency (both halves must sign v2 first, and the apply order is cut from v2's table); owner me; cut in the round after both halves sign.** (3) The `as_of` assertion cell: **landed in round 193** (`IB-pr-536`, merge b80e382520); nothing to cut. Issuer repairs the CTO asked for, done in the same tick and not cells: D2-S172 (the AC3 check now diffs the worker's own commits, @9f2ecfc3e7) and the withdrawn exclusion restored with its amendment line in the 536 instance (@8d4eb3ab2b).

Check `deliverables/2.0.0_SA_COO~P2/checks/r194/p194_cells.py`, dry-run at the base: IB194-1 AC1, AC2, AC3 all FAIL (no record, no packet); the positive control (a throwaway git repo with a live and a pin commit holding a docs-only change, a behaviour change, a line-endings-only change, a data change, an added member, an importer, and the REAL old and new trading calendars; `control194.py`) passes all three, and nineteen negatives each fail their own arm. The control found no slip of mine this round.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-538` | packet v2 of the holdings-producer release as the FULL pin mint: the moved-member tables per firm (live commit, pin commit, class, effect), the calendar and write-address and matcher reads, the re-measure at the pin on per-firm custody pins, the digest gate rewritten over the table; both halves UNSIGNED; reads only | FWD-3 | SERVED (downloads the live bundles by version id, builds candidates from served sources; writes only the worker's records) | the stop evidence of IB-pr-535 (committed) | P194-a |

fanout: 1 of 1 chains, cap 8, reason: one characterization with no sibling cell. One worker spawn (slot ~383).

## 187. ROUND 195, WORKSTREAM ~P (2026-10-14 ~15:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-195 analysis (@9a5f871655, msg 7686) and the CVO slug for round 194 (adjudication v95))

Round 194 closed (IB-pr-538 @55d4929a90; packet @98209c1a0c). The CTO's round-195 list is one READ cell and then packet v3 (v2 plus the differential as the signed scope): **CUT now** as `IB-pr-539`. Per firm, run the LIVE bundle's bytes as downloaded and the PIN on the same custody pin and the same source receipts; compare the rows, the account set, the changed values (with a stated tolerance and the largest delta) and the gate; attribute every difference to the two signed changes, to a commit W383-S2 names (account_id, the keyed gate, the CUSIP fallback, multi_asset), or UNATTRIBUTED, which is a STOP; run it twice for one digest with a planted mutant; write packet v3. The apply follows only after both halves sign v3 (**NOT cut now: an unmet dependency; owner me**).

The issuer took a direct read of the same builds before the cut (scratch outside the repository, one pass each, receipts seeded from the pin build): 49financial 32 changed SECURITY nodes (asset_class only, to cash), Inflection 841 (asset_class only, to cash), Cottonwood 485 (asset_class 253, asset_class_basis 236, sub_asset_class 51; the signed cash rule is 249 of the 253), no node added or removed, `clocks` differing only by its wall-clock timestamp. The order carries those figures as a cross-check, not an input. The cut is therefore not blind: Cottonwood has a measured scope beyond the signed rule, and the attribution to named commits is what decides whether it is a W383-S2 scope or a STOP.

Check `deliverables/2.0.0_SA_COO~P2/checks/r195/p195_cells.py`, dry-run at the base: IB195-1 AC1, AC2, AC3 all FAIL (no record, no packet v3); the positive control (a throwaway git repo with three commits and synthetic records in the flat shapes of the real artifacts; `control195.py`) passes all three, and twenty negatives each fail their own arm. This control was written from the real records' shapes after round 194's slip.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-539` | the live-against-pin differential per firm on the same custody pin and receipts (rows, account set, changed values and the largest delta, the gate), every difference attributed to a signed change or a W383-S2 commit (UNATTRIBUTED is a STOP), two runs one digest, a planted mutant, and packet v3 = v2 plus the differential as the signed scope; reads only | FWD-3 | SERVED (downloads the live bundles by version id, builds candidates from served sources; writes only the worker's records) | IB-pr-538 (merged) | P195-a |

fanout: 1 of 1 chains, cap 8, reason: one differential with no sibling cell (the per-member hybrid builds run inside it). One worker spawn (slot ~384).

## 188. ROUND 196, WORKSTREAM ~P (2026-10-14 ~18:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-196 analysis (@51675bfa49, msg 7765) and the CVO slug for round 195 (adjudication v96))

Round 195 closed (IB-pr-539 @0bf58c4ab0; packet @e1ae9ca335). The CTO's round-196 list is three cells and then packet v3: (1) the bundle closure fixed into a NEW pin, proven by `python -I` imports of every closure member from each firm's BUILT bundle and by closure == traced import set both ways: **CUT now** as `IB-pr-540`; (2) the differential re-run on the BUILT bundles (live bundle bytes against the new pin's bundle bytes), same custody pin, one served state for the gate, 32 and 841 reproducing exactly: `IB-pr-541`; (3) Cottonwood's 236 beyond-rule changes attributed by TOGGLING the four named commits one at a time on the new pin's built bundle (a change no single revert removes is UNATTRIBUTED, a STOP; member-level attribution is not enough): `IB-pr-542`; then packet v3 = the new pin, the built-bundle differential and the attribution: `IB-pr-543`. All four orders are committed in this ONE issuance; the apply is NOT cut (both halves must sign v3 first; owner me).

The chain is `IB-pr-540` -> `IB-pr-541` -> `IB-pr-542` -> `IB-pr-543`: 541 builds from 540's new pin, 542 needs 541's beyond-rule count and 540's pin, 543 reads all three records. So only `IB-pr-540` is spawned now; each later order is spawned (a fresh slot with its own worktree cut after its predecessor merges) when the drain lands its predecessor. The new pin is a side branch (`pin-ib-pr-540`) from the OLD pin (the old pin plus the one closure line), merged to trunk at the drain so the hash stays addressable; the signed producer bytes (`holdings_snapshot.py` at the old pin) do not move, and the round-193 `as_of` bypass build on trunk does not ride into the bundles.

Check `deliverables/2.0.0_SA_COO~P2/checks/r196/p196_cells.py`, dry-run at the base: IB196-1 to IB196-4, AC1 to AC3, all twelve FAIL (no record, no packet v3); the positive control (a throwaway git repo with an old pin, a new pin adding one closure member, four named commits and an unrelated one; synthetic records in the shapes the orders ask for; `control196.py`) passes all twelve, and thirty-one negatives each fail their own arm. The control and the commit-id rule were written from the real artifacts' shapes: a packet that must name commit ids is exempted from the long-digit rule for exactly those ids.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-540` | the bundle closure gains `silver/opal_unidentified.py` on a new pin (old pin + one line); every `.py` closure member imported under `python -I` from each firm's built bundle; closure == traced files both ways; bundle delta exactly +1 member | FWD-3 | LOCAL (a declaration in `.tools/`; no served byte) | none | P196-a |
| `IB-pr-541` | the live-against-pin differential on the BUILT bundles, one served state for the gate, 32 and 841 exact, Cottonwood's groups named for 542; reads only | FWD-3 | SERVED (downloads the live bundles, builds candidates from served sources) | IB-pr-540 | P196-a |
| `IB-pr-542` | Cottonwood's beyond-rule nodes attributed to the four named commits by single reverts on the built bundle; unattributed 0; reads only | FWD-3 | SERVED (same) | IB-pr-540, IB-pr-541 | P196-a |
| `IB-pr-543` | packet v3 = the new pin, the built-bundle differential and the attribution; both halves UNSIGNED | FWD-3 | LOCAL (a document from committed records) | IB-pr-540, IB-pr-541, IB-pr-542 | P196-a |

fanout: 1 of 1 chains, cap 8, reason: a four-cell chain with real data dependencies (each reads its predecessor's record or pin), so one worker is spawned now (slot ~385) and each next slot (~386, ~387, ~388) when its predecessor merges.

## 189. ROUND 197, WORKSTREAM ~P (2026-10-14 ~22:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-197 analysis (msg 7864, CTO_ROUND_ANALYSIS_IRPT_BCKEND_P_ROUND_197_20261014.md) and the CVO slug for round 196 (adjudication v97))

Round 196 closed (IB-pr-540 @cbc7701656 pin b1d354cfc9; 541 and 540 complete, 542 and 543 cancelled). The CTO's round-197 rulings: the release ships the cash rule WITHOUT the CUSIP port 01e843ce2e (the closure fix stays); the port becomes its own release after a READ of why 45 Cottonwood sub-class values become absent; the built-bundle differential is re-run at the new pin; packet v3 is written on it. Pin 2 = 5fad7eaaa8fb4c512190fa406b78c683c4b6ad1f (one commit on b1d354cfc9, the reverse of the port in holdings_snapshot.py, merged to trunk at de08782c38) was committed by the issuer on the CTO's ruling because a worker cannot commit on a tree that lacks its order.

Check `deliverables/2.0.0_SA_COO~P2/checks/r197/p197_cells.py`, dry-run at the base: IB197-1 to IB197-4, AC1 to AC3, all twelve FAIL (no record, no packet v3); the positive control (`control197.py`, a throwaway git repo with an old pin and a pin 2 whose diff is the saved toggle diff; synthetic records) passes all twelve and twenty-seven negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-544` | pin 2 verified: bundle delta exactly holdings_snapshot.py, `python -I` import of every closure member per firm, closure == traced set both ways | FWD-3 | LOCAL | none (pin 2 committed) | P197-a |
| `IB-pr-545` | built-bundle differential at pin 2: 32 and 841 exact, Cottonwood only the signed cash rule (about 253), same-state gate, two digests, mutant | FWD-3 | SERVED | IB-pr-544 | P197-a |
| `IB-pr-546` | packet v3 on pin 2: signed scope, Branch A/B, both halves UNSIGNED | FWD-3 | LOCAL | IB-pr-544, IB-pr-545 | P197-a |
| `IB-pr-547` | READ why the port blanks 45 Cottonwood sub-class values: causes with rule sites at the pin, prior path, options and a recommendation; releases nothing | FWD-3 | SERVED | none | P197-b |

fanout: 2 of 2 chains, cap 8, reason: chain P197-a (544 -> 545 -> 546) has real data dependencies, so slot ~389 is spawned now and ~390 and ~391 when their predecessors merge; chain P197-b (547) is independent and takes slot ~392 now. The apply is NOT cut (both halves must sign v3 first; owner me).

## 190. ROUND 198, WORKSTREAM ~P (2026-10-15 ~02:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-198 analysis (@daa0cbc57d, msg 7910): per-firm pins; each firm moves by the signed cash rule alone)

Round 197 closed MAY-CLOSE (packet @1eb73ef0a4). The CTO ruled: 49financial ships on the closure-fix pin b1d354cfc9 (the CUSIP port is already live there; 32 changed nodes), Cottonwood and Inflection on pin 2 5fad7eaaa8 (255 and 841); the divergence is a named, temporary fork closed by the CUSIP port's own release; packet v3 carries the per-firm pin table and the three differentials; both halves sign, then the apply runs per firm. Every measurement the table needs is already committed: 49financial 32 at the closure-fix pin (IB196-2, ~386), Cottonwood 255 and Inflection 841 at pin 2 (IB197-2, ~390), the closure proof at the closure-fix pin (~385) and the pin 2 verification (~389); the served states of IB196-2 and IB197-2 are identical per firm (same manifest versions and latest dates). So the round is ONE cell, the packet.

Check `deliverables/2.0.0_SA_COO~P2/checks/r198/p198_cells.py`, dry-run at the base: IB198-1 AC1 to AC3 all FAIL (no packet v3); the positive control (`control198.py`, synthetic records and packets in a temporary root) passes all three and fourteen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-548` | packet v3 on per-firm pins: the table, the two pins, why 49financial is not on pin 2 (119), the temporary fork, the signed scope, Branch A per firm, Branch B; both halves UNSIGNED | FWD-3 | LOCAL (a document from committed records) | none | P198-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one document; every record it reads is committed, so one worker (slot ~393) starts now.

## 191. ROUND 199, WORKSTREAM ~P (2026-10-15 ~02:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's packet-v3 half (msg 7943, "cut the per-firm apply") and ruling msg 7914 (the Orion re-pull is IRPT_BCKEND's))

Round 198 closed MAY-CLOSE (close commit 9bf42e367d). Both halves of packet v3 are signed at sha256 94eca88e9071 (COO half @9bf42e367d, CTO half @513fad5add). Two chains, disjoint write surfaces: (A) the per-firm apply of the holdings-producer release (WORLD, to the CloudOps seat 0.7.0_AE_CloudOps~IB2: three mints, each from its firm's pin, between fires, then the first fire's after-read); (B) the READ the Orion Inflection re-pull needs (SERVED, a worker): the two absent days 2026-07-01 and 2026-09-28, the pull path, why the scheduled pull skipped them, and the re-pull method that writes only those days' keys. The re-pull itself and its never-widen pair are NOT cut: they follow the READ.

Checks `deliverables/2.0.0_SA_COO~P2/checks/r199/p199_cells.py` (with p199_apply.py), dry-run at the base: IB199-1 and IB199-2, AC1 to AC3, all six FAIL (no records); the positive control (`control199.py`, synthetic records, a synthetic packet v3 with section 2 tables, a ledger file and the trading calendar in a temp git root) passes all six and thirty-nine negatives (thirteen on IB199-1, twenty-six on IB199-2) each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-549` | apply packet v3: re-hash, both halves, per-firm pins and blobs, Branch B and the manifest anchor rule, the per-firm re-measure (32, 255, 841), the digest gate against the packet's moved members, the five-leg NEVER-2 ledger, three mints each from its pin between fires, the business date stated, the first fire's after-read per firm | FWD-3 | WORLD | none (both halves signed) | P199-a |
| `IB-pr-550` | READ the Orion Inflection gap: target partitions empty, the pull path stage by stage, the skip cause with its claim, the re-pull method (proposed, not executed) | FWD-3 | SERVED | none | P199-b |

fanout: 2 of 2 chains, cap 8, reason: chain P199-a is an order to the CloudOps seat 0.7.0_AE_CloudOps~IB2 (a seat, not a worker subagent; it waits on the mint window after today's 14:15Z fires and on the next fire), chain P199-b takes one worker now (slot ~394); one worker is spawned.

## 192. ROUND 1, WORKSTREAM ~PS (the filled-report serve path; 2026-10-15 ~03:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ruling 076d @fd4c44fb48 and msg 7974: XA-20261015T024033Z-ef7f ruled "one scope, one issuer")

A SECOND WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179; the gate keys one issuance to the round and a second workstream issues its own round): the filled-report serve path, hops 2-4 (the platinum publisher, the /report route, the export source kind) as ONE never-widen pair, on the document shape hop 1's owner fixed (contract 0.5.1, msg 7970). Disjoint from workstream ~P (the holdings release and the Orion gap): its write surface is the worker's records only, and the files the pair will later change (reporting-publish, reporting-read, export) are not touched by any ~P cell. The workstream is a SCOPE; the issuer is the same seat. Hop 5 (the render host) is 0.7.0_AE_CloudOps~IB2's under the same pair's window; hop 6 is 2.0.0_SA_COO~F2's.

Check IB199-3 (`deliverables/2.0.0_SA_COO~P2/checks/r199/p199_serve.py`), dry-run at the base: AC1 to AC3 all FAIL (no record, no packet); the control passes nine positives and fifty-three negatives (fourteen on IB199-3), each negative failing its own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-551` | hops 2-4 as ONE never-widen pair: the design record (files to change read at HEAD, the input contract 0.5.1, the scope rule, the blast radius, the rollback per key, 49 Financial first, the LOCAL build slices) and the packet, both halves UNSIGNED; READ ONLY | FWD-3 | SERVED (a design for a new served route and publication; the order writes only the worker's records) | none | PS1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one document; every file it reads is committed; one worker (slot ~395) starts now.

## 193. ROUND 1, WORKSTREAM ~PO (the Orion Inflection raw feed and its 6 AM ET fold; 2026-10-15 ~04:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msgs 7914 and 7980 (row D2-S180))

A THIRD WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a second workstream issues its own round): the Orion Inflection raw producer, the days the mirror silently dropped, the re-pull's cost per feed and the producer's place in the 6 AM ET fold. Disjoint from ~P (the holdings release) and ~PS (the filled-report serve path): its write surface is the worker's records only. The re-pull pair is NOT cut; it follows this READ (CTO: "locate the raw producer, then cost the re-pull per feed, then the pair"). One cell, five questions: the raw producer located; every other dropped parquet-only day (a format the mirror ignores is a defect to fix at the mirror, not per day); the re-pull cost per feed (requests, pacing, time); the fold design (one schedule, builder names from opal_naming, trading-day frontier); the account-performance feed that 2.0.0_SA_COO~I2's round 116 may add.

Check IB199-4 (`deliverables/2.0.0_SA_COO~P2/checks/r199/p199_orion2.py`), dry-run at the base: AC1 to AC3 all FAIL (no record); the control passes twelve positives and sixty-six negatives (thirteen on IB199-4), each negative failing its own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-552` | READ the Orion raw producer, the dropped-day census per feed, the re-pull cost per feed and the 6 AM ET fold design; READ ONLY | FWD-3 | SERVED (reads served prefixes and live schedule objects; writes only the worker's records) | none | PO1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one document; one worker (slot ~396) starts now.

## 194. ROUND 2, WORKSTREAM ~PS (the filled-report serve path, the three build slices; 2026-10-15 ~05:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 7995: CTO half of the pair signed @82183fcfaf, the document's source ruled "gold parquet by ~D2, JSON by the publisher", "build slices may start now")

Round 1 of ~PS closed MAY-CLOSE (close commit 4d5dea9d59; the pair is signed at packet sha256 7daa29f0fe10). The ruling: gold is parquet and platinum is the only JSON producer; 2.0.0_SA_COO~D2 builds the gold table `filled_report_values` (hop 1); this seat's publisher reads that gold and composes the platinum JSON (hop 2); the new named-account reader with negative tests is in the pair (hop 3). The deploy legs and the first exercise wait on 49F gold for one date. The three LOCAL build slices of the packet's section 7 are cut now. They are three independent chains by WRITE SET (publisher + registry; entry.py + Terraform; export), each against the packet's fixed contract (object name `filled_report.json`, the builder's address, the contract-0.5.1 document), and no cell consumes another's output: the packet's order a to b to c named a reading order, not a data dependency. Slice a ships the publisher's PLUMBING only (the composer from gold waits for the gold table; the scheduled pass ships OFF).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r200/p200_cells.py`, dry-run at the base: IB200-1 to IB200-3, AC1 to AC3, all nine FAIL (no work, no record); the positive control (`control200.py`: stub packages at the real relative paths in temporary git roots with a worker commit, marker blocks, new tests and records) passes all nine and forty-one negatives (with the Orion cell's) each fail their own arm. The difference control removes the cell's BEGIN/END block(s) in memory and requires failed assertions, not import errors.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-553` | hop 2 publisher plumbing: `FILLED_REPORT_OBJECT`, `report_address()` from the builder, the registry family row, a validating put, a default-OFF pass with a not-yet-available gold reader; tests | FWD-3 | WORLD (the path floor of an infrastructure path; the work edits repository files only, nothing is deployed) | none | PS2-a |
| `IB-pr-554` | hop 3: the /report route, a new named-account reader, the all-accounts scope refusal (negative tests by name), the route declaration (one new route resource) | FWD-3 | WORLD (the path floor of an infrastructure path; the work edits repository files only, nothing is deployed) | none | PS2-b |
| `IB-pr-555` | hop 4: the `filled_report` export source kind, additive only (at most six removed lines), pinned by VersionId and sha256 | FWD-3 | WORLD (the path floor of an infrastructure path; the work edits repository files only, nothing is deployed) | none | PS2-c |

fanout: 3 of 3 chains, cap 8, reason: three disjoint write sets with no data dependency between them; three workers (slots ~397, ~398, ~399) start now.

## 195. ROUND 2, WORKSTREAM ~PO (the Orion pairs; 2026-10-15 ~05:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8014: cut both pairs as packets, three conditions)

Round 1 of ~PO closed MAY-CLOSE (close commit 136f730225). The CTO ruled: (b) the scheduled producer in the 6 AM New York fold PORTS the manual positions CLI into the scheduled function with no second producer beside it and the CLI retired or repointed in the same pair; (a) the seven-day positions re-pull writes THROUGH (b)'s code path to the flat key the mirror reads, reading the seven keys ABSENT first and pacing the 2,240 requests; names and addresses from the builders, the trading-day frontier; the account feed of B-IN round 117 joins (b) by addendum. One packet covers both pairs, in the order b then a.

Check IB200-4 (`p200_orion.py`, dry-run at the base: AC1 to AC3 all FAIL; thirteen negatives in `control200.py`).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-556` | the design record and the never-widen packet for the Orion pairs (b) and (a); both halves UNSIGNED; READ ONLY | FWD-3 | SERVED | none | PO2-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one document; one worker (slot ~400) starts now.

## 196. ROUND 3, WORKSTREAM ~PS (the filled-report serve path, the export contract and the export scope rule; 2026-10-15 ~06:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-3 analysis (@a4718eab10, msg 8058) and the CVO's L10 slug for round 2 (ADJUDICATION_v102 @6a4b9d068b))

Round 2 of ~PS closed MAY-CLOSE (packet @aefc53ef3a; override 409a7f7ef2 accepted by the CTO). The CTO's two rulings: (1) the packaged ExportBundle contract gains `filled_report` as an allowed source kind for NEW bundles (a MINOR revision step; both arms tested: a new bundle validates and an existing bundle validates unchanged); (2) the export freeze uses the route's ONE named-account reader (`household.accounts` plus the account-keyed `by_row` keys), written once, with its own negative test (a freeze that scopes narrower than the route is a widening). The deploy legs and the first exercise still wait on 49 Financial gold for one date (condition 3 of the CTO half). Two cells, two independent chains by write set (two JSON schema copies and a test; a shared module, entry.py, the export freeze and tests).

Checks `deliverables/2.0.0_SA_COO~P2/checks/r201/p201_cells.py`, dry-run at the base: IB201-1 and IB201-2, AC1 to AC3, all six FAIL; the positive control (`control201.py`, stub files at the real relative paths in temporary git roots with a worker commit) passes all six and fifteen negatives each fail their own arm. The contract cell's difference control serves the BASE schema bytes in memory (JSON is data, not a marker block); the freeze cell's removes the FILLED-REPORT-D blocks.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-557` | the packaged and docs ExportBundle schemas gain `filled_report_source` (byte-equal copies, one minor revision step), tests for both arms | FWD-3 | WORLD (the path floor of an infrastructure path; the work edits repository files only, nothing is deployed) | none | PS3-a |
| `IB-pr-558` | the export freeze on the shared named-account reader (one module, defined once, imported by the route and the freeze), with its negative test | FWD-3 | WORLD (same) | none | PS3-b |

fanout: 2 of 2 chains, cap 8, reason: two disjoint write sets with no data dependency (the schema copies and their test; the shared module, entry.py, the freeze and their tests); two workers (slots ~401, ~402) start now.

## 197. ROUND 3, WORKSTREAM ~PO (the Orion Inflection raw feed, the unlocated flat-key writer; 2026-10-15 ~05:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO half of the Orion pairs packet (@acaae0ff99, condition 1) and the four managers' answers (msgs 8063, 8070, 8073))

Round 2 of ~PO closed MAY-CLOSE (close commit 17172025c0); both halves of the Orion pairs packet are signed at sha256 c3dcc22f02e8. The CTO's condition 1: the writer of the daily flat keys (11:39-11:56Z) is located before the scheduled handler deploys, or the handler does not deploy. The four boxes' scheduled tasks and processes were read and none runs it (dell2 195, dell1 196, laptop 211, site Z 214): the writer is in AWS or a seat's session cron. This round is ONE READ cell over AWS (object metadata, CloudTrail data events, S3 access logs, Lambda, EventBridge and Scheduler, ECS, Glue, EC2 and SSM, CodeBuild, Step Functions). The three LOCAL build slices of the packet (the port, the schedule declaration, the Scope account addendum) are NOT cut this round: the port and schedule slices wait on what the READ finds (the hand-over shape), and the Scope addendum waits on B-IN round 120's second-household probe (CTO msg 8082: the feed's reason rows take NO_START_DATE_AT_SOURCE and NO_MODEL_AT_SOURCE from accounts_v2 with claim inferred; page words neutral until measured).

Check `deliverables/2.0.0_SA_COO~P2/checks/r202/p202_cells.py`, dry-run at the base: IB202-1 AC1 to AC3 all FAIL (no record); the control (`control202.py`, a synthetic record in a temporary root) passes all three and eleven negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-559` | READ AWS for the writer of the daily Orion flat keys: object metadata, CloudTrail, S3 access logs, the compute inventory; its kind, name, claim, evidence and the hand-over path; READ ONLY | FWD-3 | SERVED | none | PO3-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one document; one worker (slot ~403) starts now.

## 198. ROUND 4, WORKSTREAM ~PO (the Orion pairs RE-CUT on the located writer; 2026-10-15 ~07:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8127 (YES, re-cut (b) as a re-timing of the existing chain; (a) through the chain steps) and the located writer (IB-pr-559, row D2-S186))

Round 3 of ~PO closed MAY-CLOSE (close commit e9fec793a0). The writer of the daily flat keys is the Orion pull steps of the gold chain on `inf-gold-layer-runner`, started by `inf-gold-trigger` (fired by `inf-silver-aggregator`) at about 11:32Z, and the same pulls feed the silver steps. The CTO voided the IB-pr-556 packet's design of pair (b): consolidate, never build alongside. (b) = MOVE the existing trigger chain into the 06:00 America/New_York fold (no new function, no port, silver steps chained), after a read of whether Orion's T-1 is complete by 06:00 NY (else the earliest measured-complete time); (a) = re-run the 36 absent trading days through the chain's own pull steps, each key read ABSENT first, ABSENT-AT-SOURCE recorded, never an empty key; the manual CLIs retired with a message naming the chain. One cell: the design record and the packet v2 (which supersedes v1), both halves UNSIGNED.

Check IB203-1 (`deliverables/2.0.0_SA_COO~P2/checks/r203/p203_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control203.py`) passes all and seventeen negatives on IB203-1 each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-560` | the re-cut design and packet v2: (b) the re-timing of the existing chain into the 06:00 fold with the T-1 completeness read, the CLIs retired; (a) the 36-day re-run through the chain's own steps; READ ONLY | FWD-3 | SERVED | none | PO4-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one document; one worker (slot ~404) starts now.

## 199. ROUND 1, WORKSTREAM ~PY (the IB-pr-456 rebuild on the live R29c bytes; 2026-10-15 ~07:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8116 (row D2-S185: the live irpt-ycharts-generate bytes are IRPT_ANLREQ release 29 leg L3) and the Y2 correction (msg 8130))

A FOURTH WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round): the commentary_requested release (IB-pr-455/456) whose candidate package `AHxuDf7h...` was built before R29c landed. Applied as it is, it would silently revert release 29's L3 code. The CTO ruled: rebuild from current trunk source, restate the pre-apply digest as `5TRFZf6G...`, re-sign the pair only if ENDPOINT bytes move. Disjoint from ~P, ~PS and ~PO: its write surface is the worker's records only and the apply remains Andrew's execution ID (call f61b). One cell, READ ONLY on AWS, local build.

Check IB203-2 (same file), dry-run at the base: AC1 to AC3 all FAIL; the control passes all and eight negatives on IB203-2 each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-561` | REBUILD the irpt-ycharts-generate candidate from current trunk; the live digest and moved members with their denominator; release 29's four members not moved; the three ENDPOINT members compared by hash; the pre-apply digest restated | FWD-3 | SERVED | none | PY1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~405) starts now.


## 200. ROUND 4, WORKSTREAM ~PS (the serve path: the source map stages the shared reader, and the server pins the filled report at submit; 2026-10-15 ~07:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-4 analysis @ac865e2d91 (msg 8138) and his ruling on call f50a (msg 8104))

Round 3 of ~PS closed MAY-CLOSE. The CTO's round-4 analysis names two cells, one issuance. (1) Row D2-W402-S3: `infra/aws/lambda/ci/lambda-source-map.json` is explicit per file and lists no entry for the shared named-account reader `_scope/filled_named_accounts.py`, which the filled-report route and the export freeze import by name; add a `staged_from` entry in EVERY function that packages an importing module, plus a build-only import test per function. (2) Call f50a: the SERVER pins the filled report at submit (freeze_filled_report reads the current object's VersionId, sha256 and size; the page sends the client id only; a forged client pin is ignored). Deploy legs still wait on 49 Financial gold for one date. Disjoint write sets: the map and one CI test; the export package.

Checks (`deliverables/2.0.0_SA_COO~P2/checks/r204/p204_cells.py`, `control204.py`), dry-run at the base: all six FAIL; the control passes 6 positives and 16 negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-562` | the source-map `staged_from` entry for the shared reader in every importing function, a BUILD_ONLY import test per function | FWD-2 | WORLD (path floor) | none | PS4-a |
| `IB-pr-563` | the server-side pin at submit: freeze_filled_report reads the current object, the submit handler calls it, a forged client pin is ignored | FWD-2 | WORLD (path floor) | none | PS4-b |

fanout: 2 of 2 chains, cap 8, reason: two cells with disjoint write sets; workers (slots ~406, ~407) start now.

## 201. ROUND 2, WORKSTREAM ~PY (the IB-pr-456 candidate rebuilt WITH THE CANDIDATE MAP; 2026-10-15 ~07:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on ~Y2's live count (msg 8161) and CTO row D2-S187)

Round 1 of ~PY closed MAY-CLOSE on a candidate (`MfxpvRhV`, IB-pr-561) that is WRONG: the issuer's cell said "rebuild from current trunk", but the trunk source map pins the three ENDPOINT members of irpt-ycharts-generate at commits that predate commentary_requested, so the build dropped the feature and equals the live zip except for composition_admission.py. ~Y2 counted the live zip (commentary_requested 0 times in the three members); the issuer confirmed the pins (0 at the pins, 3/3/1 at HEAD). The IB-pr-456 method re-pins exactly those three members with make_candidate_map.py at the signed commit e7bb7e923a and builds with BAU_SOURCE_MAP_OVERRIDE; release 29's pins (uploads.py, interactive_access.py) stay. One cell: the rebuild and its record; read-only, nothing uploaded. The pair's re-sign question waits on this record.

Check IB205-1 (`deliverables/2.0.0_SA_COO~P2/checks/r205/p205_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control205.py`) passes all three and fifteen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-564` | REBUILD the irpt-ycharts-generate candidate with the candidate map: the ENDPOINT members at the signed pin carry commentary_requested, release 29's members stay at the live bytes, composition_admission.py recorded, the pre-apply digest restated | FWD-3 | SERVED | none | PY2-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~408) starts now.

## 202. ROUND 5, WORKSTREAM ~PO (the Orion chain read for the backfill and the fold; 2026-10-15 ~07:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ruling @1dca8c9e4d (msgs 8169, 8170) on the V2 read)

Round 4 of ~PO closed MAY-CLOSE with the design and packet V2 (IB-pr-560) and ten rows. The CTO ruled: no date token is added to the scheduled chain; the absent trading days are backfilled ONCE with the same pull code plus a date (if the dispatch script invokes the manual_api scripts they are the production code and are not retired; if not, a present day's key shape and bytes are compared first); the denominator is recomputed per feed span against lib/trading_calendar.py; the 06:00 New York fold does not move until Orion's T-1 completeness is read from the last 20 trading days' pulls; the silver aggregator's missing source (W404-S5) is a source-map and registry gap owned by the issuer. One READ cell: the chain read, the spans, the completeness read and the silver aggregator's source status. Packet V3 (supersedes V2) is the next cell, cut on this record.

Check IB206-1 (`deliverables/2.0.0_SA_COO~P2/checks/r206/p206_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control206.py`) passes all three and twenty-three negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-565` | READ the chain's pull steps against the manual_api scripts, the per-feed span denominators, the T-1 completeness over 20 trading days, the silver aggregator's source status | FWD-3 | SERVED | none | PO5-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~409) starts now.

## 203. ROUND 5, WORKSTREAM ~PS (the filled-report serve path: the submit caller and the installed reader; 2026-10-15 ~08:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round-5 analysis @25f361860e (msg 8183))

Round 4 of ~PS closed MAY-CLOSE (source-map staging, the server-side pin). The CTO's round-5 analysis names two cells, ONE issuance: (1) W407-S1: `freeze_filled_report` has no production caller; the export submit handler calls it (ruling f50a, the server pins) and a test drives the real handler; (2) W407-S2: `irpt-export-render` installs the filled reader and its filled-source branch reads the pinned object through the shared named-account reader, with one pinned filled report rendered from a fixture. Deploy legs still wait on hop 1's first cloud write (B-49F round-120 analysis @5e358b0a8f). Disjoint write sets: cell 1 owns submit_async.py, submit_service.py and retained_export.py; cell 2 owns entry.py, a new filled_reader_installed.py and the render files.

Checks (`deliverables/2.0.0_SA_COO~P2/checks/r207/p207_cells.py`, `control207.py`), dry-run at the base: all six FAIL; the control passes 6 positives and 16 negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-566` | the PATH C caller: the submit path freezes the server-pinned filled report through ports["filled_reader"] and serves it from the frozen row; tested through the real handler | FWD-2 | WORLD (path floor) | none | PS5-a |
| `IB-pr-567` | the installed filled reader (new module, installed in entry.py) and the render-side read of the pinned object through the shared reader; one pinned filled report rendered from a fixture | FWD-2 | WORLD (path floor) | none | PS5-b |

fanout: 2 of 2 chains, cap 8, reason: two cells with disjoint write sets (the three submit-path files; entry.py, a new module and the render files); workers (slots ~410, ~411) start now. The two meet at the port name ports["filled_reader"] and its signature, fixed in both faces.

## 204. ROUND 1, WORKSTREAM ~PB (the Orion pair (a) act: the one-time 33-day dated backfill; 2026-10-15 ~09:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the signed Orion pairs V3 (COO half @dd855fdea5, CTO half @b5b6db462a) and the CTO's "cut the order", msg 8195)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round): the ACT of the Orion pair (a) signed at packet V3 (sha256 03a77b33174c). The ~PO workstream's round 5 already holds its issuance (IB-pr-565, the READ), so the act issues as ~PB round 1. Disjoint from ~P, ~PS, ~PO and ~PY: its write surface is at most 33 flat bronze keys in opal-data-inf, a ledger entry and its records; the executing seat is CloudOps `0.7.0_AE_CloudOps~IB2`, whose holdings mint (IB-pr-549, 14:30Z window) takes precedence if the two meet. One cell: the dated backfill of positions 4, transactions 7, performance 22, with the performance positive control committed before any performance day.

Check IB208-1 (`deliverables/2.0.0_SA_COO~P2/checks/r208/p208_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control208.py`) passes all three and twenty-three negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-568` | APPLY pair (a) of the signed Orion packet V3: the one-time dated backfill of the 33 absent flat bronze keys by the same pull code; the performance control first; read-back per key | FWD-3 | WORLD | the signed pair (done) | PB1-a |

fanout: 1 of 1 chains, cap 8, reason: one act, one executing seat (CloudOps IB2); no worker subagent: the act is the seat's.

## 205. ROUND 1, WORKSTREAM ~PC (the S158 READ: why Cottonwood's account is absent from the holdings candidate; 2026-10-15 ~10:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8020 and row D2-S158)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round): the READ the CTO asked for in msg 8020 ("the S158 READ in a later ~P round"). The ~P workstream's round 199 still holds IB-pr-549 pending at CloudOps IB2 (the 14:30Z holdings mint), so the READ issues as ~PC round 1 rather than waiting for ~P's close; its write surface is the worker's records only and it touches no file or object of ~P. Cottonwood's served holdings are four trading days behind (2026-10-08 served; later candidates refused by the publish guard on `account_lost` count 1). One cell: the refusals, where the account is lost against the source, the cause, whether it clears, the acceptance path as the publisher's code has it (guard, closed-account exclusion, the one-date bypass, any directory exemption) and the other firms' state. Nothing is published or bypassed.

Check IB209-1 (`deliverables/2.0.0_SA_COO~P2/checks/r209/p209_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control209.py`) passes all three and nineteen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-569` | READ why Cottonwood's account is absent from the holdings candidate; the acceptance path in the code; the other firms' refusal state | FWD-21 | SERVED | none | PC1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~412) starts now.

## 206. ROUND 2, WORKSTREAM ~PC (49 Financial's refusal and the Cottonwood validator, both READ; 2026-10-15 ~11:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8248: "cut both READs now, 49 Financial's refusal FIRST")

Round 1 of ~PC closed MAY-CLOSE (IB-pr-569, the S158 READ). Its finding: Cottonwood's residual lost account is listed in the source and dropped by the COT account screen (cause inferred), the first refusal named 9 lost accounts (8 closed), and 49 Financial, the P1 firm, ALSO has a refusal record (served 2026-10-12, two trading days behind T-1 at 2026-10-14). The CTO ordered two reads, 49 Financial FIRST: (1) which condition refused 49 Financial, how many accounts, which class of account or field (ids private); (2) the Cottonwood validator run OFFLINE on the dropped account's source rows to name the failing condition in `cot_screen_accounts`. The guard stays and no bypass is widened; the CTO rules the fix (a screen correction, or a custodian TERMINATED mark) on the reads. Two cells, disjoint write sets (each writes only its own record folder and the shared append-only channel), no edge between them (the order of the reads is the CTO's priority, not a data dependency).

Checks (`deliverables/2.0.0_SA_COO~P2/checks/r210/p210_cells.py`, `control210.py`), dry-run at the base: all six FAIL; the control passes 6 positives and 25 negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-570` | READ 49 Financial's refusal: the condition, the count, the class of account or field, the days behind (recomputed), the acceptance path in the code | FWD-21 | SERVED | none | PC2-a |
| `IB-pr-571` | READ the Cottonwood validator offline on the dropped account's source rows: the failing condition, the fix options in the code | FWD-21 | SERVED | none | PC2-b |

fanout: 2 of 2 chains, cap 8, reason: two READ cells with disjoint write sets; workers (slots ~413, ~414) start now (413 first by the CTO's priority).

## 207. ROUND 1, WORKSTREAM ~PD (the split-adjusted holdings price return: the READ; 2026-10-15 ~12:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ruling @9913bf3ed4 (msg 8251) and the CRO's research @fe343dbc14)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round). The CTO ruled that the 2026-04-21 VUG IC|RO rows are a 6-for-1 STOCK SPLIT (non-flow, partition INTERNAL), that the defect is `holdings_performance_daily`'s price-only return (not split-adjusted), and that IRPT_BCKEND owns the fix: the custodian's own same-day STK "STOCK SPLIT" ratio (quantity after over quantity before for an account with no same-day trade), confirmed against the close-price ratio, with `SPLIT_RATIO_ABSENT` where it cannot be measured; the three other CUSIPs split that day are inside the fix; the other two firms are read for split days; the change moves served numbers, so it lands under a never-widen pair counting the DELTA per account-day. The build cannot be cut blind: the pure core has no split input and the custodian split rows are read from a different source. One READ cell first (this round): the producer's price contribution in the code, the custodian split rows per firm (columns, rows, split days, measurable or absent ratios, agreement with the close-price ratio), and the served DELTA projection. The build cell and the pair follow on its record.

Check IB211-1 (`deliverables/2.0.0_SA_COO~P2/checks/r211/p211_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control211.py`) passes all three and eighteen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-572` | READ the split-adjusted return's inputs: the producer sites, the custodian split rows and ratios per firm, the served DELTA projection | FWD-21 | SERVED | none | PD1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~415) starts now.

## 208. ROUND 1, WORKSTREAM ~PE (49 Financial's candidate screen run offline; 2026-10-15 ~11:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8256)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round); ~PC round 2 holds its issuance (IB-pr-570 and IB-pr-571), so the third read issues as ~PE round 1. The 49 Financial refusal READ (IB-pr-570, merged @a9eb88ed54) found the P1 firm served at 2026-10-12 (two trading days behind T-1), the 2026-10-13 candidate refused on `account_lost` count 1, the lost account marked ACTIVE in the directory (so the closed-account exemption cannot clear it), and the candidate builder's filter that omits it unread. The CTO ordered it measured, beside Cottonwood's validator read: run 49 Financial's candidate screen OFFLINE on the account's source rows, name the exact failing condition, and say whether it is the condition Cottonwood's IB-pr-571 finds; if both firms share it, one screen fix under one never-widen pair covers both, and the pair states the served DELTA (one account each back in the snapshot) and the dates owed per firm. The guard is untouched. One cell, READ ONLY.

Check IB212-1 (`deliverables/2.0.0_SA_COO~P2/checks/r212/p212_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control212.py`) passes all three and fifteen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-573` | RUN 49 Financial's candidate screen offline on the lost ACTIVE account's rows; the failing condition; the comparison with Cottonwood's; the fix options in the code | FWD-21 | SERVED | none (the Cottonwood comparison reads IB-pr-571 if landed) | PE1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~416) starts now.

## 209. ROUND 1, WORKSTREAM ~PF (how Cottonwood's EMPTY-at-the-source account is accepted as closed; 2026-10-15 ~12:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8263)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round). The Cottonwood validator READ (IB-pr-571) measured the failing condition: the account has only no-position rows in the custodian source, so the validator refuses an empty custody frame. The CTO ruled (msg 8263) that the source itself reports zero positions on three trading dates, so the account is EMPTY at the source, not silently lost: the "closed at the source" branch of his S158 ruling. The acceptance is a never-widen pair bound to the one account and the first date it is accepted from (evidence: the source rows' dates and zero position counts; blast radius one account leaving the served snapshot; rollback the prior publication; guard unchanged, no general override, no custodian contact), and the directory's missing TERMINATED mark is filed as a row for the directory's owner. The pair needs the MECHANISM: the guard exempts an account only through the directory's TERMINATED mark (`closed_account_ids`). One READ cell: who writes the mark, its shape, the precedent (2 TERMINATED entries in 271), the evidence dates, and an OFFLINE gate run with a stub closed-account provider proving the account lists as closed and not refused and no other node moves. Nothing is written. The pair packet follows on its record.

Check IB213-1 (`deliverables/2.0.0_SA_COO~P2/checks/r213/p213_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control213.py`) passes all three and eighteen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-574` | READ the TERMINATED mark's writer, shape and precedent, the zero-position evidence dates for the one account, and an offline gate run with the mark stubbed | FWD-21 | SERVED | none | PF1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~417) starts now.

## 210. ROUND 2, WORKSTREAM ~PE (49 Financial's lost ACTIVE account across the dim_balance partitions; 2026-10-15 ~13:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8274)

Round 1 of ~PE closed MAY-CLOSE (IB-pr-573): 49 Financial (the P1 firm, served 2026-10-12, two trading days behind T-1) has a lost ACTIVE account with ONE row in the 2026-10-12 dim_balance partition and NONE in 2026-10-13, so no screen drops it: a source gap on the candidate date. The CTO ordered (msg 8274) the account's presence read across dim_balance 2026-10-08 to 2026-10-14 and the upstream writer's run for 2026-10-13 (row counts by partition; did it fail or truncate), and ruled: an account ABSENT from the source is not the zero-position case, the guard keeps refusing; if 2026-10-14 carries it again the 2026-10-14 candidate publishes cleanly and 2026-10-13 stays an unpublished day stated in words; if it is gone for good the remedy is a custodian-confirmed TERMINATED mark, a partner-firm contact the issuer drafts for Andrew. One READ cell.

Check IB214-1 (`deliverables/2.0.0_SA_COO~P2/checks/r214/p214_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control214.py`) passes all three and seventeen negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-575` | READ the lost account's presence across dim_balance 2026-10-08 to 2026-10-14, the upstream writer in the code and its 2026-10-13 run, whether the refusal clears | FWD-21 | SERVED | none | PE2-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one record; one worker (slot ~418) starts now.

## 211. ROUND 1, WORKSTREAM ~PG (the closed_at_source exemption of account_lost in the holdings publish gate: the BUILD; 2026-10-15 ~13:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msgs 8268 and 8284)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179: a workstream issues its own round). The reads (IB-pr-569 to 575) found 49 Financial (the P1 firm, served 2026-10-12) and Cottonwood (served 2026-10-08) refused on a lost account the SOURCE shows with no positions, and the directory's TERMINATED mark cannot be written for an account absent from its source. The CTO ruled (msg 8284) one never-widen pair covering both firms for a guard exemption with a completeness condition: exempt an `account_lost` only when the source shows the account with no positions (absent or zero) in BOTH the positions and balance tables on the candidate date AND the prior trading day, each of those partitions complete (account count at least 95 percent of the prior day's), and each exempted account recorded in the publication manifest as `closed_at_source` with its dates; a reappearing account is re-included by the daily rebuild; the served DELTA is measured per firm by a producer dry run, before and after, and the pins and both branches go in the packet. This cell BUILDS the pure exemption, the gate's integration through one optional provider (default None, nothing else changes) and the manifest record, LOCAL, with the seven named tests and a difference control. The evidence loaders per firm, the dry-run DELTA and the pair packet are the next cells. Class LOCAL: the path is a data-pipeline script, not infrastructure.

Check IB215-1 (`deliverables/2.0.0_SA_COO~P2/checks/r215/p215_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control215.py`) passes all three and seven negatives each fail their own arm.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-576` | BUILD closed_at_source_exempt, the gate's provider argument and the manifest record, with tests and a difference control | FWD-21 | LOCAL | none | PG1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one product file; one worker (slot ~419) starts now.

## 212. ROUND 1, WORKSTREAM ~PH (the absent_at_source exemption goes live with its visible listing; the split-adjusted holdings price return for 49 Financial; 2026-10-15 ~14:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msgs 8284, 8290, 8302, 8311 and the ruling @9913bf3ed4)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). Two cells with disjoint write surfaces. IB-pr-576 built the exemption inert; worker 419's rows W419-S1 and S2 (disposition row D2-S201) named what was left. The CTO ruled (msg 8311, CVO v119) that the exemption is wired into `run_firm` ONLY together with the visible listing of the account (kept in the served snapshot, "Not reported by the custodian since <date>", no stale value as current) in ONE change, and that every remaining "closed" name becomes `absent_at_source`. The agent read of the code found that the snapshot has no household node (a household is a directory entry), so the listing is a fresh zero-value ACCOUNT node appended after the gate with the snapshot's scope and count bookkeeping brought in line; the published manifest is written by `publication.py` (a path under infra/, so the cell's class is WORLD although nothing is deployed). The second cell builds the split adjustment of the holdings price return for the 49 Financial channel from the READ IB-pr-572 (ratio = the median over accounts without other activity, clean to 0.5 percent, else SPLIT_RATIO_ABSENT and not graded). Served DELTA and the never-widen pairs are later acts from producer dry runs, not these cells.

Checks IB216-1 and IB216-2 (`deliverables/2.0.0_SA_COO~P2/checks/r216/p216_cells.py`), dry-run at the base: AC1 to AC3 of both cells all FAIL; the control (`control216.py`) passes all six positives and fourteen negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-577` | WIRE the evidence loaders and the listing with the exemption, the published manifest fact, the rename of the closed names | FWD-21 | WORLD | none | PH1-a |
| `IB-pr-578` | BUILD the split-adjusted holdings price return for 49 Financial (declared split source, median ratio, SPLIT_RATIO_ABSENT, manifest codes) | FWD-21 | LOCAL | none | PH2-a |

fanout: 2 of 2 chains, cap 8, reason: two cells on disjoint files (holdings_snapshot.py and publication.py; holdings_performance.py and sources.json); workers slots ~420 and ~421 start now.

## 213. ROUND 1, WORKSTREAM ~PI (the APPLY of the signed pair IB-pr-456 with its ADDENDUM 1, the `commentary_requested` release of irpt-ycharts-generate; 2026-10-15 ~14:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ruling @7f7acb0e42 and msg 8316)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). The pair IB-pr-456 is signed by both halves (the candidate `3+fMEJhQ8...` replaces `AHxuDf7h...`; pre-apply `5TRFZf6G...`, read live at ~14:2xZ). The apply waited on call f61b, Andrew's own PROD submission; Andrew tried the PROD Ticket Center on 2026-10-15 and the form cannot be submitted there (the model, ticker and firm lists do not load), so the CTO WITHDREW f61b (@7f7acb0e42, msg 8316): the BEFORE record is the applier's wrong-typed body refused as an unknown member on the live function, and one already-accepted request read by get-item before and after. Nothing waits on Andrew. Four COO seats (`~G2`, `~Y2`, `~T2` and this one) wait on the release. One cell, class WORLD, to the CloudOps seat `0.7.0_AE_CloudOps~IB2`, which holds the project's applies.

Check IB217-1 (`deliverables/2.0.0_SA_COO~P2/checks/r217/p217_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control217.py`) passes all three and fourteen negatives plus the no-record case each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-579` | APPLY the signed pair IB-pr-456 and ADDENDUM 1: the four members to `irpt-ycharts-generate` by its Terraform path, the reworded BEFORE record, the after-read, the health proof | FWD-4 | WORLD | none | PI1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one function; the seat is a CloudOps seat, not a worker subagent.

## 214. ROUND 1, WORKSTREAM ~PJ (the served DELTA of the two ~PH builds, measured by READ-ONLY dry runs; 2026-10-15 ~14:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8302 and the ruling @9913bf3ed4)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). ~PH r1 built, at HEAD only, the `absent_at_source` exemption wired live with its listing (IB-pr-577) and the 49 Financial split adjustment (IB-pr-578). Each reaches the firms only by an apply under a never-widen pair whose blast radius is a measured served DELTA. The CTO ruled (msg 8302, CVO v118) that the exemption's DELTA is measured ALONE: the same candidate with and without it, per firm. Two READ cells with disjoint outputs: IB-pr-580 builds each firm's candidate once from the live pinned inputs, gates it without and with the evidence provider on a deep copy, and compares node by node, then simulates the second fire; IB-pr-581 runs the producer's return over the 47 split days of the READ IB-pr-572 before and after the adjustment and counts the account-days moved. Both are read-only, counts only, SERVED. The never-widen pairs, the release pins and the applies are later acts.

Checks IB218-1 and IB218-2 (`deliverables/2.0.0_SA_COO~P2/checks/r218/p218_cells.py`), dry-run at the base: AC1 to AC3 of both cells all FAIL; the control (`control218.py`) passes all six positives and fourteen negatives plus the no-record cases each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-580` | READ the exemption ALONE per firm: counts with and without, nodes added, no other node changed, the second fire | FWD-21 | SERVED | none | PJ1-a |
| `IB-pr-581` | READ the split adjustment before and after over the 47 split days of 49 Financial | FWD-21 | SERVED | none | PJ2-a |

fanout: 2 of 2 chains, cap 8, reason: two read-only cells with disjoint outputs; workers slots ~422 and ~423 start now.

## 215. ROUND 1, WORKSTREAM ~PK (two small repairs the CTO named after ~PH r1: the receipts record the exemption's evidence reads; a split row with no key is counted, never skipped; 2026-10-15 ~15:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8359)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). The CTO's msg 8359 (CVO v120) says the two ~PH builds are correct and names the next round: the two dry-run DELTAs (already cut as ~PJ), two never-widen pairs (the exemption for both firms; the 49 Financial split), and two repairs, which are these cells. IB-pr-582 (W420-S1): `run_firm` freezes the source receipts before the gate, so the prior-day partitions the exemption's evidence readers read are not in `_source_objects` nor in the revision digest; the receipts are re-taken after the gate when the provider read anything. IB-pr-583 (W421-S2): a split row whose key chain (cusip, then ticker) is empty is dropped today; it is now counted (`unkeyed_split_rows`, `days_ratio_absent`) and the day says `SPLIT_RATIO_ABSENT` in its attrs and the manifest. Two LOCAL cells on disjoint files (holdings_snapshot.py; holdings_performance.py). The DELTA reads of ~PJ measure the HEAD before these repairs; the harness is committed and is re-run on the repaired HEAD before the pairs.

Checks IB219-1 and IB219-2 (`deliverables/2.0.0_SA_COO~P2/checks/r219/p219_cells.py`), dry-run at the base: AC1 to AC3 of both cells all FAIL; the control (`control219.py`) passes all six positives and fourteen negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-582` | the source receipts record the absent_at_source evidence reads (re-taken after the gate when the provider read anything) | FWD-21 | LOCAL | none | PK1-a |
| `IB-pr-583` | a split row with no key marks the day SPLIT_RATIO_ABSENT and is counted in the attrs and the manifest | FWD-21 | LOCAL | none | PK2-a |

fanout: 2 of 2 chains, cap 8, reason: two cells on disjoint files; workers slots ~424 and ~425 start now.

## 216. ROUND 1, WORKSTREAM ~PL (why 49 Financial still refuses after the exemption: a READ; 2026-10-15 ~15:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the READ IB-pr-580 and the CTO's msg 8359)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). The served-DELTA read of the exemption alone (IB-pr-580, row S203) found that the exemption exempts ONE lost account of 49 Financial and the gate still refuses on `account_lost` (other lost accounts) and on `classified_security_lost`; the exemption therefore does not unblock the firm, while Cottonwood already publishes at HEAD. Before the never-widen pair for the exemption is written, the CTO and the CVO need what else holds 49 Financial back. One READ cell, counts only: the lost accounts classified by evidence (exempted; closed by the directory; still reported by the source with positions, so dropped by the build; evidence incomplete; other), and what `classified_security_lost` counts.

Check IB220-1 (`deliverables/2.0.0_SA_COO~P2/checks/r220/p220_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control220.py`) passes the three positives and nine negatives plus the no-record case each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-584` | READ the anatomy of 49 Financial's remaining refusal: lost accounts by class, classified_security_lost, the conditions that remain | FWD-21 | SERVED | none | PL1-a |

fanout: 1 of 1 chains, cap 8, reason: one read-only cell; one worker (slot ~426) starts now.

## 217. ROUND 2, WORKSTREAM ~PJ (the release candidates the two never-widen deploy pairs need; 2026-10-15 ~16:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO round analysis @57266eeb77, msg 8435)

The CTO's round analysis of ~PJ and ~PK round 1 (both MAY-CLOSE) recuts in ONE issuance: (1) the anatomy READ of 49 Financial's remaining refusal becomes an order (IB-pr-584, issued in workstream ~PL a few minutes earlier and amended @d911b8752f with the per-condition threshold, value and source-or-join cause the CTO named; it is the cell that serves item 1 and stays in ~PL); (2) the never-widen deploy pair for IB-pr-580, 582 and 583 is cut now, in parallel. The pair's COO half names the blast radius per firm and per key and the rollback per key, so it needs, per release, a CANDIDATE: the package built from a pin and compared with the live one. Two READ cells, BUILD ONLY, disjoint outputs: IB-pr-585 builds the candidate of the 49 Financial performance function that carries the split adjustment (IB-pr-578 and 583) and compares it with the live package; IB-pr-589 builds the three per-firm holdings bundles from a pin that carries the exemption, its listing and the receipts (IB-pr-576, 577, 582) and compares them with the live bundles IB-pr-549 minted. Neither uploads, mints or invokes anything. The pair packet is written when they land.

Checks IB221-1 (`checks/r221/p221_cells.py`) and IB222-1 (`checks/r222/p222_cells.py`), dry-run at the base: AC1 to AC3 of both all FAIL; the controls (`control221.py`, `control222.py`) pass their positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-585` | READ the 49 Financial performance function's release candidate (the split adjustment), BUILD ONLY, against the live package | FWD-21 | SERVED | none | PJ3-a |
| `IB-pr-589` | READ the three per-firm holdings bundles' release candidates (the exemption, its listing, the receipts), BUILD ONLY, against the live bundles | FWD-21 | SERVED | none | PJ4-a |

fanout: 2 of 2 chains, cap 8, reason: two read-only build cells with disjoint outputs; workers slots ~427 and ~428 start now.

## 218. ROUND 1, WORKSTREAM ~PN (the Orion Scope account feed: the BUILD; 2026-10-15 ~16:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8411 and the signed pair (b) addendum 1)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). The CTO round-118 analysis ADDENDUM 1 (msg 8411) moved the feed from "after IB-pr-568" to "now": the feed is an addendum to pair (b), writes only its own prefixes (disjoint from pair (a)), and only its APPLY waits for the executor. The addendum (`deliverables/2.0.0_SA_COO~P2/ORION_PAIR_B_ADDENDUM_1_SCOPE_ACCOUNT_FEED.md`, blob 1e138cbeea) carries the rules of rounds 118 to 121: one Scope call per household with the Account grouping, `calcGrossOfFees` false on every request, `fee_basis` NET with its note (round 119), the coverage rule with `ABSENT` and the reason classes `NO_GROUP`, `GROUP_NO_SERIES` and `NO_START_DATE_AT_SOURCE` with the claim per account (rounds 120 and 121), never a zero and never an Opal fill, writes to the feed's own bronze and silver prefixes built by `address()`. The COO half is signed (`NEVER_WIDEN_ORION_PAIR_B_ADDENDUM_1_SCOPE_FEED_COO_HALF.md`) and the CTO half is signed @9de748bb47 (msg 8448). Two LOCAL/WORLD-by-path cells on disjoint files: IB-pr-586 builds the pull step, its tests and its one catalog row in the dispatch script (repository copy); IB-pr-587 lifts the one-account limit of `orion_account_mapping.py` in the same release and adds a household-members helper. The apply (script upload, the dispatch object edit, the first-run read) is a CloudOps order cut after these merge, queued directly after IB-pr-568.

Check IB223 (`deliverables/2.0.0_SA_COO~P2/checks/r223/p223_cells.py`), dry-run at the base: AC1 to AC3 of both cells all FAIL; the control (`control223.py`) passes the six positives and fourteen negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-586` | BUILD the Scope account feed pull step (coverage rule, fee_basis NET, own prefixes) and its catalog row | FWD-3 | LOCAL | none | PN1-a |
| `IB-pr-587` | LIFT the one-account limit of orion_account_mapping.py, add the household-members helper | FWD-3 | WORLD | none | PN2-a |

fanout: 2 of 2 chains, cap 8, reason: two cells on disjoint files (a new pull script with the dispatch script; the Lambda mapping module); workers slots ~429 and ~430 start now.

## 219. ROUND 3, WORKSTREAM ~PJ (the minimal overlay candidate of the three holdings bundles; 2026-10-15 ~16:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the finding of IB-pr-589)

IB-pr-589 (record `IB222-1_holdings_bundles_candidate.json`) built each firm's bundle from the current HEAD and found that besides `holdings_snapshot.py` and `publication.py` (the two files the exemption, its listing and the receipts changed) SIX unrelated closure members differ from the live bundles, because other projects' commits landed since the minting pins: `dim_mdpf_aggregate_aua_timeseries.py`, `dim_mdpf_aum_metrics.py`, `mdpf_category_registry.py` (MDPF_CANON), `exemptions.json` and `opal_naming.py` (the registry owner) and `reporting_policies.json` (IB-pr-553). Shipping them under the exemption pair would widen its blast radius to changes it does not own. The cell builds the MINIMAL candidate: each firm's bundle from its MINTING pin with only the two files overlaid from HEAD, BUILD ONLY, and runs the exemption tests on that overlay tree to prove the two files need nothing the drifted members carry. If the tests fail the finding is which drifted member the new code needs, and the pair then names it.

Check IB224-1 (`deliverables/2.0.0_SA_COO~P2/checks/r224/p224_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control224.py`) passes the three positives and ten negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-590` | READ the overlay release candidates of the three holdings bundles (minting pin + the two files), BUILD ONLY, tested offline, against the live bundles | FWD-21 | SERVED | none | PJ5-a |

fanout: 1 of 1 chains, cap 8, reason: one read-only build cell; one worker (slot ~431) starts now.

## 220. ROUND 1, WORKSTREAM ~PM (the served manifest names the ratio-absent split securities; 2026-10-15 ~17:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO half of the 49 Financial split pair @ab04a4b5a2, condition 3)

A NEW WORKSTREAM of IRPT_BCKEND (row IRPT_BCKEND-S179). The CTO signed the split pair (msg 8466) on the condition that the 13 ratio-absent security-days stay ungraded AND "the served manifest names them by security and day. They are never silent." The build (IB-pr-578 and 583) records only counts in the run manifest's `split_adjust` block. This cell adds the names (`ratio_absent`: day, security, accounts used; the unkeyed rows by day), LOCAL, grading unchanged. The release candidate of IB-pr-585 is then REBUILT (its digest changes) and the pair's COO half re-issued on the new digest for the CTO to re-bind; the apply order waits for that.

Check IB225-1 (`deliverables/2.0.0_SA_COO~P2/checks/r225/p225_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control225.py`) passes the three positives and seven negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-592` | BUILD the named ratio_absent list in the frame attrs and the run manifest (day, security, accounts used; unkeyed rows by day), grading unchanged | FWD-21 | LOCAL | none | PM1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one product file; one worker (slot ~432) starts now.

## 221. ROUND 2, WORKSTREAM ~PN (the Scope account feed stores the daily factor, admits SERIES_ENDED_AT_SOURCE and walks calendar days; 2026-10-15 ~17:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's msg 8484 and B-IN's round-122 probe)

IB-pr-586 (merged @7b150e672a) built the feed with `return_value = performance / 100` per series point. B-IN's history probe (294 households, series calendar-day and contiguous from each account's start; chained factors equal Orion's period return up to a year; Orion annualizes its summary over a year; two series end 95 and 120 days early) and the CTO's ruling (round-118 ADDENDUM 3, msg 8484) fix four things: store the daily FACTOR only (never a summary), admit the reason class `SERIES_ENDED_AT_SOURCE` for the scheduled feed too, chain CALENDAR days weekends included, and give the scheduled run a window from the day after the newest landed partition. One LOCAL cell on the one script. The feed's apply order waits for it.

Check IB227-1 (`deliverables/2.0.0_SA_COO~P2/checks/r227/p227_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control227.py`) passes the three positives and seven negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-594` | the feed stores the daily factor only, SERIES_ENDED_AT_SOURCE, calendar-day rows, the scheduled window from the newest landed day | FWD-3 | LOCAL | none | PN3-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one script; one worker (slot ~433) starts now.

## 222. ROUND 4, WORKSTREAM ~PJ (the TRANSPLANT candidates of the three holdings bundles: the exemption alone; 2026-10-15 ~18:0xZ, issuer 2.0.0_SA_COO~P2 on dell2)

IB-pr-590's overlay candidate (merged @53d1153a4b) overlaid HEAD's whole `holdings_snapshot.py` on each firm's minting pin. Reading the file against each pin with the exemption blocks removed showed that HEAD's file is NOT the pin plus the exemption: it also carries (a) the unreleased one-date bypass of IB-pr-536 (`allow_older_date`, the `ONE-DATE-ASSERT` block, a manual-path flag whose sign-off is not part of the exemption pair) for all three firms, and (b) for 49 Financial the REVERSAL of the CUSIP port (pin 1 keeps it live on purpose; pin 2 reversed it for Cottonwood and Inflection) and a `multi_asset` list change. The never-widen pair must move the exemption ALONE. This cell builds the TRANSPLANT candidate: each firm's minting-pin file with ONLY the exemption commits (IB-pr-576, 577, 582) applied, verified by stripping the exemption blocks and diffing against the pin, with the two transplanted files committed per firm so the check recomputes their hashes, BUILD ONLY, the offline tests on each transplant tree, and the live comparison. The exemption pair's COO half waits on it.

Check IB228-1 (`deliverables/2.0.0_SA_COO~P2/checks/r228/p228_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control228.py`) passes all and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-595` | READ the transplant release candidates (exemption alone) of the three holdings bundles, BUILD ONLY, tested, against the live bundles | FWD-21 | SERVED | none | PJ6-a |

fanout: 1 of 1 chains, cap 8, reason: one read-only build cell; one worker (slot ~434) starts now.

## 224. ROUND 5, WORKSTREAM ~PJ (the REBUILT release candidate of the 49 Financial performance function; 2026-10-15 ~18:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO half of the split pair, condition 3)

IB-pr-585 built the candidate (`fvmE5j1h...`) before IB-pr-592 added the named `ratio_absent` list to the run manifest, which the CTO's signed half requires. The candidate is rebuilt at the current HEAD, BUILD ONLY, against the live package and the first candidate; the split pair's COO half is then re-issued on the new digest for the CTO to re-bind. One read-only cell; its harness is IB-pr-585's.

Check IB230-1 (`deliverables/2.0.0_SA_COO~P2/checks/r230/p230_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control230.py`) passes the positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-597` | READ the REBUILT performance function candidate (with the named ratio-absent list), BUILD ONLY, against the live package | FWD-21 | SERVED | none | PJ7-a |

fanout: 1 of 1 chains, cap 8, reason: one read-only build cell; one worker (slot ~435) starts now.

## 223. ROUND 6, WORKSTREAM ~PO (the APPLY of the Orion pair (b) ADDENDUM 1, the Scope account feed; 2026-10-15 ~18:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the signed halves and the CTO's msgs 8499 and 8496)

Pair (b) ADDENDUM 1 is signed by both halves (blob 1e138cbeea; CTO half @74aa15de73). The builds are merged: IB-pr-586 (the pull step and its catalog row), IB-pr-587 (the one-account limit lifted) and IB-pr-594 (the daily factor, `SERIES_ENDED_AT_SOURCE`, calendar days, the scheduled window; the CTO's ADDENDUM-2 condition 1 gates BOTH applies on it). IB-pr-568 closed on the same executor, so the feed's apply takes IB2's next slot (the CTO's round analysis msg 8499). One WORLD order to `0.7.0_AE_CloudOps~IB2`: the gates (halves signed, builds complete, the live dispatch object equal to the repository copy, the roster column, the runner role's grants incl. the cross-bucket write, the LIVE notification filter, the bound equal to the household count read at the apply, the Inflection-only write set), the writes (script and trading calendar beside it, the address sidecar generated from `address()`, the dispatch object edited by the one row and its chain entries, the saved copy named first), and the FIRST SCHEDULED RUN read (coverage equals the denominator, no zero, the daily factor stored, within the bound). The account mapping's release (IB-pr-587) and the history backfill (ADDENDUM 2) are separate acts.

Check IB229-1 (`deliverables/2.0.0_SA_COO~P2/checks/r229/p229_cells.py`, committed @f9d2f4541b), dry-run at the base: AC1 to AC3 all FAIL; the control (`control229.py`) passes the three positives and seventeen negatives plus the no-record cases each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-596` | APPLY the Scope account feed: the gates, the script and its beside-files, the sidecar, the dispatch row and entries, the first scheduled run | FWD-3 | WORLD | none | PO6-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2).

## 225. ROUND 3, WORKSTREAM ~PN (the Scope account feed writes a day's keys only when the day is complete; 2026-10-15 ~18:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's round analysis msg 8536, item 4)

The feed (IB-pr-586, amended by IB-pr-594) calls Orion once per household and today writes every day's bronze and silver keys from the households that answered, even when some household failed. A partial day reads as a complete one: its missing accounts look like accounts with no return. The CTO's analysis orders the rule, with a test: a day's key pair is written ONLY when every household in that day's universe answered OK; the skipped days and the households that blocked them are named in the output, and the exit is non-zero. One LOCAL cell on the one script; the feed's apply (IB-pr-596) waits for it.

Check IB231-1 (`deliverables/2.0.0_SA_COO~P2/checks/r231/p231_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control231.py`) passes the positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-599` | the feed writes a day's key pair only when the day is complete, names skipped days, exits non-zero | FWD-3 | LOCAL | none | PN4-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one script; one worker (slot ~436) starts now.

## 226. ROUND 7, WORKSTREAM ~PO (the APPLY of the Scope account feed's IAM pair; 2026-10-15 ~19:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ruling msg 8553 after IB2's STOP at gate (f) of IB-pr-596, msg 8548)

`address()` puts the feed in `opal-data-assets/orion/inflection/` (doctrine R4, the CTO ruled it right); the inf gold runner role reaches `opal-data-inf` only, so the feed's write simulates implicitDeny. The IAM pair (packet blob cea5395ee7; COO half @afc428c27c; CTO half @d0bf7c5ea7) grants ONE new inline policy: Put/Get on the two `scope_account_returns` prefixes, ListBucket under an `s3:prefix` condition, no Delete, no KMS. One WORLD order to `0.7.0_AE_CloudOps~IB2` applies it through `safe-apply` under its own ledger and proves it both ways (four allowed and four denied simulation arms) plus the CTO half's condition 3: the feed's own `exists()` run on the runner against a known-absent key must read ABSENT. IB-pr-596 resumes after it, amended.

Check IB232-1 (`deliverables/2.0.0_SA_COO~P2/checks/r232/p232_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control232.py`) passes the three positives and fifteen negatives plus the no-record cases each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-600` | APPLY the one IAM resource for the feed's keys; the simulation arms; the exists() read on the runner | FWD-3 | WORLD | none | PO7-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2).

## 227. ROUND 2, WORKSTREAM ~PL (49 Financial's refusal anatomy and the exemption-alone DELTA, re-measured on the TRANSPLANT tree; 2026-10-15 ~19:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ruling ADDENDUM 1 @334382c7f4, msg 8538)

IB-pr-584 (anatomy) and IB-pr-580 (DELTA) were measured on HEAD's `holdings_snapshot.py`, which reverses the CUSIP port that 49 Financial's live bundle keeps (pin 1). IB-pr-595 (merged @5bf120faa2) built the 49 Financial transplant tree: pin 1 plus the exemption alone. The CTO orders both measurements repeated on that tree before the join, classification and dry-run cells (msg 8527 items 1 to 3) are cut, each only for what still trips against the new denominator. One READ cell, counts only; the harnesses are IB-pr-580's and IB-pr-584's, run with the two transplant files in place of the repository's.

Check IB233-1 (`deliverables/2.0.0_SA_COO~P2/checks/r233/p233_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control233.py`) passes the three positives and fifteen negatives plus the no-record case each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-602` | READ the anatomy and the exemption-alone DELTA of 49 Financial on IB-pr-595's transplant tree | FWD-21 | SERVED | IB-pr-595 (drained) | PL2-a |

fanout: 1 of 1 chains, cap 8, reason: one read-only cell; one worker (slot ~437) starts now.

## 228. ROUND 8, WORKSTREAM ~PO (the Scope feed's IAM resource rebuilt to pass the commit-time naming gate; 2026-10-15 ~19:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on IB2's STOP on IB-pr-600, msg 8563)

IB-pr-600 stopped before any apply: the commit of the signed packet's HCL is refused by the commit-time naming gate (LGIC_ENFORCE, rule 30). The policy name carries a token in no vocabulary, and the scope, bucket and prefix strings were typed by hand where the gate permits only the `opal_name` module and `lookup()` over a registry-fed local. The defect is the packet's (mine): rule 30 asks the L4 text to cite builder output. One WORLD-by-path BUILD cell, repository only: the same resource, the same two statements, the same actions and conditions, spelled through the module and the registry, committed through the gate, its evaluated prefixes equal to `address()` output. No plan, no apply, no registry edit. The packet is then re-issued at the committed text for the CTO to re-bind, and IB-pr-600 applies from HEAD without editing the file.

Check IB234-1 (`deliverables/2.0.0_SA_COO~P2/checks/r234/p234_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control234.py`) passes the three positives; seven HCL negatives, five record negatives, two counter/notes negatives and the no-input cases each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-603` | the IAM resource spelled through opal_name and the registry; the gate accepts the commit | FWD-3 | WORLD (path floor) | none | PO8-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one Terraform file; one worker (slot ~438) starts now.

## 229. ROUND 3, WORKSTREAM ~PL (the 49 Financial account join fixed, the guard unchanged; 2026-10-15 ~20:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on IB-pr-602's finding and the CTO's ruling @334382c7f4 item 1)

IB-pr-602 (merged @98bfeea0f2, the 49 Financial anatomy and the exemption-alone DELTA on IB-pr-595's transplant tree) found: `classified_security_lost` no longer trips (4 to 0 of 1,839; so the registry classification cell of the CTO's msg 8527 item 2 is not cut), `account_lost` still trips on ONE of 7,640 served accounts, cause `join` (the source reports it with positions, the candidate drops it), and the exemption alone moves no node because that account keeps the gate refusing. The CTO's item 1: fix the join, not the guard; a synthetic test with that account's shape; the held rows W426-S2 (a negative test) and W426-S3 (counts only on the console) ride in the same cell. One LOCAL build cell on `holdings_snapshot.py`. The exemption pair's transplant candidate is then rebuilt with this commit added (a later read cell); the dry run at HEAD with 0 lost follows it.

Check IB235-1 (`deliverables/2.0.0_SA_COO~P2/checks/r235/p235_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control235.py`) passes the positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-604` | the account join fix (key found in process), W426-S2 negative test, console counts only | FWD-21 | LOCAL | IB-pr-602 (drained) | PL3-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one module; one worker (slot ~440) starts now.

## 230. ROUND 1, WORKSTREAM ~PQ (the APPLY of the holdings EXEMPTION pair; 2026-10-15 ~21:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on both halves signed: packet blob b4ad2d79c9, COO half @faa1fc5dc9, CTO half @a937b9931c, msg 8632)

The exemption pair is signed, bound to IB-pr-595's transplant digests `d2eaf305` (49financial) and `bc2e8f54` (Cottonwood and Inflection). One WORLD order to `0.7.0_AE_CloudOps~IB2`: the gates, the digest gate per firm (the two members plus SHA256SUMS, `allow_older_date` 0, 49financial's CUSIP lines 12 against 12, the six drifted members equal live), the re-measure at the release (49financial refusing or publishing one listed account; Cottonwood four listed accounts; Inflection measured, any other verdict a STOP for Inflection only), the ledger, the three mints between fires, the business date stated before the fire, the first fire per firm and the exemption's after-read. It starts only after IB-pr-549's ledger is CLOSED (its after-read is the 2026-10-16 14:15Z fire). The join fix (IB-pr-604) and a candidate rebuilt with it are a separate addendum.

Check IB236-1 (`deliverables/2.0.0_SA_COO~P2/checks/r236/p236_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control236.py`) passes the three positives and twenty-one negatives plus the no-record cases each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-605` | APPLY the exemption pair: gates, digest gate, re-measure, three mints, first fire per firm | FWD-21 | WORLD | IB-pr-549 ledger closed | PQ1-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2).

## 231. ROUND 3, WORKSTREAM ~PL, AMENDMENT 1 (cell `IB-pr-604` re-cut as the ADDENDUM 1 build; 2026-10-15 ~21:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO's ADDENDUM 1 @9fef489152, msg 8644)

The cell of section 229 stopped: worker `~440` measured that no join key is wrong for 49 Financial's one remaining lost account (candidate-day custody 0 balance and 0 position rows under every key form; prior day 1 and 13; candidate-day SmartX map 1 row; rows W440-S1 to S3, drained @6c58d386ab). The CTO ruled (msg 8644): the SmartX row is evidence the account exists, so it is exempt-eligible; the exemption pair's ADDENDUM 1 writes that as a rule change with its own pair and names `smartx_map_present` as the manifest evidence; the two-consecutive-day threshold and the 95 percent floor are unchanged (one absent day is not eligible; the next business day decides); (c) is refused; the signed exemption pair ships first and Cottonwood does not wait; 49 Financial stays served at 2026-10-12 until the amended rule clears it on real data. `IB-pr-604` is re-cut as the code build of that addendum: the SmartX evidence read for 49 Financial's reader and the `evidence` key in the manifest entry, inside `ABSENT-AT-SOURCE-D` spans, with the exemption's decision, floor and threshold untouched. The criterion ids, the cell id and the check file stay; the worker slot is `~441`, the test file, the marker and the named tests change (check amended, control re-run: 3 positives pass, 7 negatives each fail their own arm, 0 unexpected; base dry-run AC1 to AC3 FAIL).

Reading recorded for the CTO (not a ruling asked): `absent_at_source_exempt` does not consult SmartX at all; it already exempts any lost account absent from both custody tables on two consecutive days. So this build changes no gate decision, only adds the evidence key to the entry. The same rule, applied by the signed pair alone, exempts the account on the first business day after the apply on which custody still lacks it.

Next cells, not yet cut (each needs the previous commit): the 49 Financial addendum candidate (the D spans applied onto the transplanted file of IB-pr-595, a new digest, the changed members still exactly the two files), then the addendum pair packet (COO half, the CTO half).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-604` | ADDENDUM 1 code build: SmartX evidence read and the `smartx_map_present` key (re-cut) | FWD-21 | LOCAL | IB-pr-602 (drained) | PL3-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one module; one worker (slot ~441) starts now.

## 232. ROUND 4, WORKSTREAM ~PL (the 49 Financial ADDENDUM 1 release candidate; 2026-10-15 ~22:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on IB-pr-604 drained and the CTO's ADDENDUM 2 @594e598878, msg 8664)

IB-pr-604 is drained @f888350689 (IB235-1 AC1 to AC3 re-run PASS on the landed tree, instance VALID, 77 tests pass, three `ABSENT-AT-SOURCE-D` spans in `holdings_snapshot.py`; the exemption's decision, floor and threshold untouched). The CTO ruled 49 Financial's publishing does not wait on the evidence key (msg 8664): the signed exemption pair covers its branch (ii), and the evidence-key addendum ships after under its own candidate digest and pair, its Branch A reading the node set unchanged. This round cuts the READ cell that builds that candidate: IB-pr-595's signed transplant files for 49financial plus ONLY the D spans, BUILD ONLY, compared with the live bundle, a NEW digest; the addendum pair packet (COO half) follows it, then the CTO half and a later apply cell.

Check IB237-1 (`deliverables/2.0.0_SA_COO~P2/checks/r237/p237_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control237.py`) passes the three positives and sixteen negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-606` | READ the 49financial addendum candidate: signed transplant plus the D spans, build only, tests, compare with live | FWD-21 | SERVED | IB-pr-604 (drained) | PL4-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one bundle build; one worker (slot ~442) starts now.

## 233. ROUND 5, WORKSTREAM ~PL (the SmartX evidence is never omitted silently; 2026-10-15 ~22:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO half of the exemption ADDENDUM 1, msg 8719 condition 2)

The CTO signed the addendum's CTO half (blob `835fd2886e`, candidate `32d6dfcb`) with a condition the built candidate does not meet: the SmartX read is evidence and never a gate, and a read that fails or is refused at run time must give the account's `evidence` key the value `unread` with the reason, never omitted silently; Branch A reads `smartx_map_present` or `unread`; no IAM change rides. IB-pr-604's spans omit the key on a failed read, so candidate `32d6dfcb` is void for the apply and the addendum's COO half is re-stated on a rebuilt candidate. One LOCAL build cell changes the D spans (a reason CATEGORY set, no identifier, no message) and the tests; the candidate is then rebuilt (a later read cell) and the COO half re-stated.

Check IB238-1 (`deliverables/2.0.0_SA_COO~P2/checks/r238/p238_cells.py`), dry-run at the base: AC1 to AC3 all FAIL (AC2 refuses to grade until the three `unread` tests exist); the control (`control238.py`) passes the three positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-607` | the SmartX evidence `unread` with a reason category on a failed or refused read; decision unchanged | FWD-21 | LOCAL | IB-pr-604 (drained) | PL5-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one module; one worker (slot ~443) starts now.

## 234. ROUND 6, WORKSTREAM ~PL (the 49 Financial ADDENDUM 1 candidate rebuilt on the CTO's `unread` condition; 2026-10-15 ~23:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on IB-pr-607 drained and the CTO half, msg 8719)

IB-pr-607 is drained @53c238604b (IB238-1 AC1 to AC3 re-run PASS in the worker tree, instance VALID, 79 tests pass over the six files, three `ABSENT-AT-SOURCE-D` spans; a failed or refused SmartX read now gives `evidence` `unread` with a reason category; the one wiring-test dict edited by AMENDMENT 1; row W443-S2: `partition_missing_or_empty` also covers a partition with rows and no usable account number). Candidate `32d6dfcb` (IB-pr-606) predates it and does not meet condition 2 of the CTO half: it is VOID for any apply. This round cuts the READ cell that rebuilds the 49financial candidate from IB-pr-595's signed transplant files plus the CURRENT D spans, BUILD ONLY, a NEW digest; the addendum pair's COO half is then re-stated on it and the CTO half re-signed at the new bytes.

Check IB239-1 (`deliverables/2.0.0_SA_COO~P2/checks/r239/p239_cells.py`, the r237 check with the slot, ids and paths moved to this order), dry-run at the base: AC1 to AC3 all FAIL; the control (`control239.py`) passes the three positives and sixteen negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-608` | READ the 49financial addendum candidate v2: signed transplant plus the current D spans, build only, tests, compare with live | FWD-21 | SERVED | IB-pr-607 (drained) | PL6-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one bundle build; one worker (slot ~444) starts now.

## 235. ROUND 7, WORKSTREAM ~PL (every exempted account carries exactly one of three SmartX evidence values; 2026-10-16 ~00:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO half's revision note, msg 8774)

The CTO answered the open question on revision 2 of the addendum's COO half: "a missing key reads the same as 'not checked'", so a read that SUCCEEDS and does not show the account must write `"evidence": "smartx_map_absent"` instead of no key; every exempted account of the 49 Financial reader carries exactly one of `smartx_map_present`, `smartx_map_absent`, `unread` (with a reason category), and Branch A reads exactly one value per account. Candidate `75c6902d` (IB-pr-608) writes no key in that third case and is VOID for the apply. One LOCAL build cell changes the listing hook's D span and the tests; the candidate is then rebuilt (a later read cell) and the COO half re-stated again; the CTO signs the new blob the turn it arrives.

Check IB240-1 (`deliverables/2.0.0_SA_COO~P2/checks/r240/p240_cells.py`), dry-run at the base: AC1 to AC3 all FAIL (AC2 refuses to grade until the two new tests exist); the control (`control240.py`) passes the three positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-609` | the listing hook writes `smartx_map_absent` when the obtained map does not show the account; tests | FWD-21 | LOCAL | IB-pr-607 (drained) | PL7-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one module; one worker (slot ~445) starts now.

## 236. ROUND 8, WORKSTREAM ~PL (the 49 Financial ADDENDUM 1 candidate rebuilt on the three-value evidence; 2026-10-16 ~00:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on IB-pr-609 drained and the CTO half's revision note, msg 8774)

IB-pr-609 is drained @1ff5e87e40 (IB240-1 AC1 to AC3 re-run PASS in the worker tree, instance VALID, 80 tests pass over the six files, three `ABSENT-AT-SOURCE-D` spans; every exempted account of the 49 Financial reader now carries exactly one of `smartx_map_present`, `smartx_map_absent`, `unread` with a reason; HEAD's file with the spans stripped equals the file at `e2700915d2`). The candidates built before it (IB-pr-606, `32d6dfcb`; IB-pr-608, `75c6902d`) are VOID for any apply. This round cuts the READ cell that rebuilds the 49financial candidate from IB-pr-595's signed transplant files plus the CURRENT D spans, BUILD ONLY, a NEW digest; the addendum pair's COO half is then re-stated on it (revision 3) and the CTO signs the new blob the turn it arrives.

Check IB241-1 (`deliverables/2.0.0_SA_COO~P2/checks/r241/p241_cells.py`, the r239 check with the slot, ids and paths moved to this order), dry-run at the base: AC1 to AC3 all FAIL; the control (`control241.py`) passes the three positives and sixteen negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-610` | READ the 49financial addendum candidate v3: signed transplant plus the current D spans, build only, tests, compare with live | FWD-21 | SERVED | IB-pr-609 (drained) | PL8-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one bundle build; one worker (slot ~446) starts now.

## 237. ROUND 2, WORKSTREAM ~PQ (the APPLY of the holdings EXEMPTION ADDENDUM 1; 2026-10-16 ~01:5xZ, issuer 2.0.0_SA_COO~P2 on dell2, on both halves signed: COO half revision 3 blob `5d162efd37`, CTO half `..._ADDENDUM_1_R3_CTO_HALF.md`, msg 8830)

The addendum pair is signed on candidate `61537d6d` (IB-pr-610, merged @65650cbbbd; every exempted account carries exactly one of `smartx_map_present`, `smartx_map_absent`, `unread`). One WORLD order to `0.7.0_AE_CloudOps~IB2`: the gates, the digest gate against the exemption pair's bundle `d2eaf305` (exactly `holdings_snapshot.py` and `SHA256SUMS` change), the re-measure with the SAME node set in two arms, the ledger, the mint between fires, the business date stated before the fire, the first fire's after-read with one evidence value per account. It starts only after IB-pr-605 is done (its ledger CLOSED and its first-fire after-read written), because the live bundle must read `d2eaf305` and the CVO's per-artifact rule (msg 8750) puts both applies on one bundle in sequence; IB-pr-605 waits in turn on IB-pr-549's ledger (its after-read is the 2026-10-16 14:15Z fire).

Check IB242-1 (`deliverables/2.0.0_SA_COO~P2/checks/r242/p242_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control242.py`) passes the three positives and twenty-four negatives each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-611` | APPLY the addendum: gates, digest gate, re-measure, one mint, first fire, evidence after-read | FWD-21 | WORLD | IB-pr-605 done | PQ2-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2).

## 238. ROUND 2, WORKSTREAM ~PM (the APPLY of the 49 Financial split-adjusted price-return pair, ACT 1; 2026-10-16 ~04:1xZ, issuer 2.0.0_SA_COO~P2 on dell2, on both halves signed: pair sha256 `8f645588ab`, ADDENDUM 1 blob `f0cec424f4`, the CTO halves @ab04a4b5a2 and msg 8632)

The split pair has been fully signed since ~20:2xZ (candidate `LiDXhN74`, IB-pr-597, against live `o9UugRAV`) and had no apply order: found on the empty tick of the 30m drive (the exemption addendum apply IB-pr-611 and IB-pr-605 wait on IB-pr-549's 14:15Z fire, IB-pr-596 on the 11:32Z chain run; this cell waits on neither: a different artifact). One WORLD order to `0.7.0_AE_CloudOps~IB2`, ACT 1 only: the gates (one change on the function AND its Terraform root, which the Cottonwood holdings-performance function shares), Branch B named before the upload, the siblings' CodeSha256 read before and after (the CTO addendum's added condition), the source-map rows landed, the build from the REAL map printing `LiDXhN74`, one saved plan 0/1/0 by `safe-apply`, the deployed handler's date line (Act 2 needs it), the health proof, and the first scheduled run's manifest. ACT 2 (the restatement of the 47 split days; 1,291 of 266,455 account-days change, served history) is NOT cut: it is a separate order after the first scheduled run is read (CTO half condition 5), and it needs its own window (at least 30 minutes either side of the scheduled fire).

Check IB243-1 (`deliverables/2.0.0_SA_COO~P2/checks/r243/p243_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control243.py`) passes the three positives and twenty-five negatives plus a changed pair and an unsigned CTO half each fail their own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-612` | APPLY Act 1: the source-map rows, the real-map build, one safe-apply, siblings unmoved, the health proof, the first scheduled run | FWD-21 | WORLD | none (both halves signed) | PM2-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2).

### 238 AMENDMENT 1 (2026-10-16 ~05:0xZ, issuer 2.0.0_SA_COO~P2, after IB2's STOP of `IB-pr-612` at step 1 (row D2-S214) and the CTO's ruling (b), msg 9037, ADDENDUM 2 signed both halves at blob `47e819dd93`, CTO half @97d1198270)

The cell's premise was wrong: the 49F, Inflection and Cottonwood performance functions read ONE S3 artifact key (`lambda.tf` lines 23, 71, 117), so the one release moves all three and the root plan reads exactly 3 changes, not 1. The cell is unchanged in id, risk and chain; its content is amended: the three functions move together under one saved plan; the sibling manifest readers are counted first (`deliverables/2.0.0_SA_COO~P2/IB-pr-612_SIBLING_MANIFEST_READER_CENSUS_20261016.md`: no first-party serving reader that parses or refuses is found; limits stated); each sibling's first scheduled run is replayed with the pre-change code and must match row for row (DELTA = 0) with the manifest differing only by the added `split_adjust` block; Branch B returns all three by the prior VersionId; no other apply runs on the root while the ledger is open. Check IB243-1 amended and its control re-run (0 unexpected); base dry-run AC1 to AC3 FAIL. Act 2 stays out of this cell.

## 239. ROUND 3, WORKSTREAM ~PM (the APPLY of the 49 Financial split pair, ACT 2, STAGED; 2026-10-16 ~05:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, prepared on the empty tick of the 30m drive while every live order waits on an event)

Act 2 restates the 47 split days (2024-07-09 to 2026-09-03): the function is invoked with `{"date": "<D>"}` once per day, in ascending order, outside the scheduled fire window, and each new key is compared with its prior version row by row (1,291 of 266,455 account-days change, 985 on 2026-04-21). It is the part of the signed pair that changes served history. It is cut now as a `staged` order so no tick is lost after IB-pr-612's first scheduled run is read: it does NOT start on reading; the issuer flips it to `pending` and sends a GO citing it when IB-pr-612 is `complete`, its first scheduled run is read (declared, run ok, each sibling's DELTA = 0), its ledger is CLOSED and the 49 Financial function reads `LiDXhN74`. The day list and the per-day counts are read from the signed delta record, never typed. One thing is unmeasured: the delta record was measured by a harness (a BEFORE arm with the declaration removed in memory, an AFTER arm with it), not on the stored keys; if a stored key differs from the harness's BEFORE arm for any reason, the first such day stops the run, by design (CTO half: the first disagreement stops).

Check IB244-1 (`deliverables/2.0.0_SA_COO~P2/checks/r244/p244_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control244.py`) passes the three positives and each negative fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-613` | APPLY Act 2: 47 dated invokes of the 49F function, per-day prior version and row comparison, first disagreement stops | FWD-21 | WORLD | IB-pr-612 (complete, first run read, ledger closed) | PM3-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2); staged until the GO.

## 240. ROUND 4, WORKSTREAM ~PM (the forward fix of ACT 1: the 49 Financial role's transactions-read grant, then ONE recovery invoke; 2026-10-16 ~12:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO ruling msg 9318 and both halves signed: packet blob `03cd6e9d46`, CTO half @334655f31b)

IB-pr-612 Act 1 left the 49F function failing (row `IRPT_BCKEND-D2-S217`, ARMED, mine): its role has no grant for the split-adjust transactions prefix, which the signed pair did not carry. NEVER-2 forbids leaving the deploy half-landed, so the CTO ruled a forward IAM pair now, with Branch B of Act 1 at 13:00Z. One WORLD order to `0.7.0_AE_CloudOps~IB2`: the 14-arm simulate battery before and after, the one `locals.tf` edit, one saved plan of 1 change by `safe-apply`, then one recovery invoke with the schedule's own input. IB-pr-612's ledger stays open until this is read; IB-pr-613 (Act 2) stays staged. It takes round 4 of ~PM because rounds 2 and 3 of ~PM already carry an issuance (IB-pr-612, IB-pr-613) and the gate keys ONE ISSUER PER ROUND to the round; it is the completion of the round-2 change, not a new design round.

Check IB245-1 (`deliverables/2.0.0_SA_COO~P2/checks/r245/p245_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control245.py`) passes the three positives and each of 29 negatives fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-614` | APPLY the role grant (plan 1/0/0), battery before and after, one recovery invoke | FWD-21 | WORLD | none (both halves signed) | PM2-b |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2); this is the completion of the open IB-pr-612 change.

## 241. ROUND 5, WORKSTREAM ~PM (the on-demand read that closes L6 of the IB-pr-521 ledger; 2026-10-16 ~17:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO ruling (A), msg 9653)

Ledger `irpt-export-receipt-repin-20261013` (IB-pr-521, the export receipt re-pin) was OPEN 64 hours past its 6-hour window with L6 waiting on "a person's after-read": one NEW export readable on DEV and the pre-existing receipt still reading. The export function had 0 invocations since the apply (my CloudWatch read), so no person was going to supply it soon. The CTO ruled that the read, not the reader, was what he named, and that a seat drives it now (no FWD is a wait). One SERVED order to `0.7.0_AE_CloudOps~IB2` (rule 34): mint ONE transient staff-only user by the signed helper (the XA-20261016T160537Z-f98b shape: staff role only, no firm entitlement row, role set printed, removal read back ABSENT), read one pre-existing receipt, request ONE new DEV export through the portal route as the page calls it, no client emailed, read its status, remove the user. I close L6 and the ledger on the record.

Check IB246-1 (`deliverables/2.0.0_SA_COO~P2/checks/r246/p246_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control246.py`) passes the three positives and each of 19 negatives fails its own arm (0 unexpected). Rounds 2 to 4 of ~PM already carry an issuance (IB-pr-612, IB-pr-613, IB-pr-614), so this takes round 5.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-615` | DRIVE one DEV export under a transient staff user, read the new status and the old receipt, remove the user | FWD-21 | SERVED | none (ruling msg 9653) | PM5-a |

fanout: 1 of 1 chains, cap 8, reason: one cell, one CloudOps seat (IB2).

## 242. ROUND 7, WORKSTREAM ~PS (the APPLY of hops 3 and 4 of the signed pair IB-pr-551 with its ADDENDUM 1 and 2, STAGED; 2026-10-16 ~21:5xZ, issuer 2.0.0_SA_COO~S2 on dell2, on the CTO's msgs 9528, 9546, 9576 and 9614)

The pair IB-pr-551 (hops 2 to 4 of the filled-report serve path) is signed by both halves, with ADDENDUM 1 (the export role's read of the platinum filled object, blob `9462b5ad35af`) and ADDENDUM 2 (the fence row of that role, blob `b5c303ea69ff`), both halves SIGNED. The CTO split the release (msg 9614): `~D2`'s publish pair carries hop 2 (the reader, switch OFF; TO-DB-b-312, ledger `irpt-dashbd-49f-publish-hop2-reader-readgrant-20261016`, open at this writing) and this cell carries hops 3 and 4, both to `0.7.0_AE_CloudOps~IB2` (rule 34), hop 2 first, one apply at a time. The filled-report switch-on pair is separate and is cut only when hops 2, 3 and 4 are all live. This cell is cut now as a `staged` order so no tick is lost once hop 2 lands: it does NOT start on reading; the issuer flips it to `pending` and sends a GO citing it when hop 2's ledger is CLOSED and `~D2`'s TO-DB-b-312 is `complete`, and, for the IAM leg only, when the second fence row for `irpt-export-render-role` is at HEAD of `infra/logic/registry/exemptions.json` and the laptop's regeneration is read back (the IAM leg waits; the code legs do not). The legs are the packet's legs 2 and 3 (the report route on `irpt-49f-reporting-read-lambda`; the export bundle with `server_pinned_body`), then the one IAM statement of ADDENDUM 1. The BEFORE state, the STEP 0 and the rollbacks are in `deliverables/2.0.0_SA_COO~S2/IB_pr_551_HOPS_3_4_RELEASE_PLAN_BEFORE_STATE_20261016.md` @0d9a58d59e, re-read at the GO.

Check IB247-1 (`deliverables/2.0.0_SA_COO~S2/checks/r247/p247_cells.py`), dry-run at the base: AC1 to AC3 all FAIL (no record); the control (`control247.py`) passes the three positives and each of 13 negatives (including the no-record case) fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-616` | APPLY hops 3 and 4: the report route and the read function bundle, the export bundle, then the one IAM statement on `irpt-export-render-role` (after the fence row is read back) | FWD-21 | WORLD | `~D2` TO-DB-b-312 complete and hop 2 ledger closed; the IAM leg also the second fence row regenerated | PS7-a |

fanout: 1 of 1 chains, cap 4 (CTO msg 8765), reason: one cell, one CloudOps seat (IB2); staged until the GO.

## 243. ROUND 8, WORKSTREAM ~PS (the export reads the CURRENT filled-report object and refuses on a sha256 or size mismatch: the BUILD behind IB-pr-551 ADDENDUM 3; 2026-10-17 ~01:5xZ, issuer 2.0.0_SA_COO~S2 on dell2, on XA-20261017T010553Z-d493 RULED (B), CTO msg 10126 and the CTO half of ADDENDUM 3 @94032d0bb7)

The fence validator closes the scoped read set at GetObject (no GetObjectVersion, one row per bucket), so the export role cannot read a pinned VersionId. The ruling keeps the validator and changes the export: it reads the current object and refuses unless the bytes' sha256 and size equal what the export server recorded at submit. ADDENDUM 3 (COO half blob `87a46d9cf370c293dae46a413cba213db721b5ef`, CTO half signed) fixes the grant to GetObject only and names the behaviour change: an overwritten report is REFUSED with a worded state, not exported as the pinned bytes. This cell is that code change and its tests, a repo-only build (declared WORLD because the L6 gate floors every `infra/` path at WORLD), in this seat's own surface (`export/retained_export.py` and the three filled-report test files). The new export bundle (an IB2 apply, TO-IB-pr-618) and the IAM statement (TO-IB-pr-616 Step 6) follow it, in the CTO's order: the bundle live and read back BEFORE the statement is applied. It is a small cell (about 20 lines of code plus the tests that move with it), cut as ONE order on the full limbs, since a WORLD class excludes the direct-act path.

Check IB248-1 (`deliverables/2.0.0_SA_COO~S2/checks/r248/p248_cells.py`), dry-run at the base `bba05481507a` on dell2: AC1 (the three test files pass and the two new tests exist and pass), AC2 (the seam: no version_id passed to the reader, the sha256 and size refusal kept and worded, `filled_reader_installed.py` byte-equal to the base) and AC3 (the difference control: the new tests FAIL against the base `retained_export.py`) all FAIL at the base. AC2 was also run against a reference copy of the change and PASSES.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-617` | BUILD: read_pinned_filled reads the current object and refuses on a changed object with a worded state; the tests move with it; a planted-changed-object test | FWD-21 | WORLD (path floor) | none | PS8-a |

fanout: 1 of 1 chains, cap 4 (CTO msg 8765), reason: one cell, one worker (slot ~481); disjoint write surface (retained_export.py and three test files).

## 244. ROUND 9, WORKSTREAM ~PS (a remediation of IB-pr-617: four stale comments and one docstring in retained_export.py made true; 2026-10-17 ~02:2xZ, issuer 2.0.0_SA_COO~S2 on dell2, on worker 481's row IRPT_BCKEND-D2-W481-S1)

IB-pr-617 changed `read_pinned_filled` to read the CURRENT object and refuse on a sha256 or size mismatch (`302d7fc367`). Worker 481 correctly left four statements outside the two named functions unedited under its change-nothing-else bound, and filed row W481-S1: the PATH C banner (the freeze "reads that VersionId"), the IB-pr-563 block ("reads back exactly that VersionId"), the FILLED-REPORT-F banner ("never the current object") and the `filled_leg_read` docstring ("The current object is never consulted") now state the opposite of what the code does. They sit in a security-relevant pinning path, and the export bundle (TO-IB-pr-618) is built from this file, so they are corrected BEFORE the bundle: comments and one docstring only, no code token. The module's own head (PATH B, the platinum series read through the route) stays true and is not touched. Cut as one small order for the same worker slot (the next order is handed to the SAME subagent), merged with IB-pr-617 at the chain end.

Check IB249-1 (`deliverables/2.0.0_SA_COO~S2/checks/r249/p249_cells.py`), dry-run at the worker's state `dae909c87f` on dell2: AC1 (the bound, 31 tests pass) PASS and AC2 (the bound, no code token differs from the build commit) PASS as bound checks should at the base; AC3 (the build: the four stale statements gone and the sites say the current object is re-read) FAILS. AC3 also run against a scratch copy with the four planned replacements applied and PASSES.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-619` | REPAIR: four stale comments and one docstring in retained_export.py describe the old pinned-VersionId read; make them true, comments and docstring only | FWD-21 | WORLD (path floor) | IB-pr-617 (built) | PS8-a |

fanout: 1 of 1 chains, cap 4 (CTO msg 8765), reason: one cell on the same chain as IB-pr-617, so the same worker continues; one write surface (retained_export.py).

## 245. ROUND 10, WORKSTREAM ~PS (the APPLY of the new export bundle that reads the CURRENT filled-report object and refuses on a sha256 or size mismatch: the first of the three things IB-pr-616 Step 6 waits on; 2026-10-17 ~03:xxZ, issuer 2.0.0_SA_COO~S2 on dell2, after the drain 1dab1295ef of IB-pr-617 and IB-pr-619)

IB-pr-616 Step 5 left `irpt-export-render` on the bundle whose `read_pinned_filled` reads the pinned VersionId (live CodeSha256 `5bIgn/MLNgtN...`, read by the issuer 2026-10-17). IB-pr-551 ADDENDUM 3 grants `s3:GetObject` ONLY, so that code would be refused by the role once the statement lands. The merged code (`1dab1295ef`) reads the current object and refuses on a sha256 or size mismatch. This cell applies that bundle through `0.7.0_AE_CloudOps~IB2` (code attributes of the one function; the filled-report switch is not touched; no IAM change), before the fence row regeneration and the Step 6 statement. Order of the three, per the CTO: bundle, then the fence row and regeneration, then the statement.

Check IB250-1 (`deliverables/2.0.0_SA_COO~S2/checks/r250/p250_cells.py`) reads the record IB2 writes; dry-run at the base on dell2: AC1, AC2 and AC3 each FAIL (no record), as a build check should.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-pr-618` | APPLY: the export bundle with the current-object read and sha256 refusal, code attributes only | FWD-21 | WORLD | IB-pr-617 and IB-pr-619 (merged), IB-pr-616 Steps 1 to 5 (applied) | PS8-b |

fanout: 1 of 1 chains, cap 4 (CTO msg 8765), reason: one APPLY cell on the CloudOps lane IB2, the single seat for this macro on dell2 (rule 34); it follows the build chain PS8-a.

## 242. ROUND 6, WORKSTREAM ~PM (the served account-id HMAC list producer, cell 1: the READ; 2026-10-17 ~03:0xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO msg 10155 and ruling B, msg 10161; plan blob `f1f250ab37`)

The laptop CTO ruled (@3ffa142af0) that `client-data-check.py` reads a keyed list, `HMAC-SHA256(key, UPPER(id))`, produced by a scheduled served-layer job; the dell2 CTO ruled B: the step goes in `irpt-directory-refresh`, the existing all-firm reader, as its LAST stage after the directory write commits (its failure never alters or rolls back the directory output, proved by a planted-failure test), the object holds only sorted HMACs (no firm, count by firm or id), the role gains `GetSecretValue` on one ARN and `PutObject` on one key, and a never-widen pair; the hook flip to refuse-on-absent is the laptop CTO's after the first list lands. Six cells (IB-hm-1 to IB-hm-6, plan section 3). This section cuts the first: a READ-ONLY repository measurement by a worker, so that the producer code (IB-hm-2), the Terraform (IB-hm-3) and the pair (IB-hm-4) are built on cited facts, not on my reading of two files. IB-hm-2 to IB-hm-6 are cut when this one is graded.

Check IBHM1 (`deliverables/2.0.0_SA_COO~P2/checks/r247/p247_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control247.py`) passes the three positives and each of 18 negatives fails its own arm (0 unexpected). Rounds 2 to 5 of ~PM already carry an issuance, so this takes round 6.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-1` | READ the seven facts (last stage, where the ids live, spelling, names, IAM and env, the gate, the tests) with evidence that resolves | FWD-21 | LOCAL | none (ruling B) | PM6-a |

fanout: 1 of 6 chains cut, cap 8, reason: IB-hm-2 and IB-hm-3 depend on this read's facts; IB-hm-4 on 3; IB-hm-5 and 6 on 4 and the IB2 lane.

## 243. ROUND 7, WORKSTREAM ~PM (the served account-id HMAC list producer, cell 2: the BUILD; 2026-10-17 ~03:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO rulings msg 10161 and msg 10203)

IB-hm-1 (the READ, graded: criteria PASS, the key claim re-read by me in `directory_runner.py` and `_ids/ids.py`) found that the directory's account ids are opaque minted ids (`acc_` plus 24 hex), so a list over them alone would miss the raw custodian numbers the hook exists to catch. The laptop-side containment target is the RAW numbers; the dell2 CTO ruled (msg 10198, then 10203): the raw keys are already in process in the runner at the mint, under the runner's own profile, so no new reader; the step goes in `directory_runner.py` per firm in `run_firm`, HMAC(key, UPPER(raw)) plus the minted hex, ONE key per firm in the globgrph folder (`address()` output), the box pull tool reads all of them and the hook reads their union; the combined key and its hand-off are dropped (so the READ cell IB-hm-1b I had drafted was not cut). The plan's cell list changes accordingly:

| cell | item | risk | depends on |
|---|---|---|---|
| `IB-hm-2` | BUILD the stage in the runner (this section): `emit_hmac_list`, the two arguments, ten tests | LOCAL | IB-hm-1 |
| `IB-hm-3` | REGISTRY + TERRAFORM + DISPATCH: registry rows for the secret and the globgrph product folder (bucket `opal-313476888478-globgrph`, declared in the globgrph module), the secret, the runner profile's two grants (one `GetSecretValue` ARN, one `PutObject` key per firm), `refresh.py` `runner_script` passing the two arguments | LOCAL (plan) | IB-hm-2, and the runner profile's TF home (measured in the cell) |
| `IB-hm-4` | PAIR: packet, COO half, CTO half | SERVED | IB-hm-3 |
| `IB-hm-5` | APPLY by `0.7.0_AE_CloudOps~IB2`: the bundle mint, the plan, the secret, one QA run, the first scheduled fire | WORLD | IB-hm-4 signed, the IB2 lane |
| `IB-hm-6` | READERS: the grant for each box identity to read the three firm keys and the secret; the pull tool and the hook edit are the laptop CTO's | WORLD | IB-hm-5 |

It takes round 7 of ~PM because round 6 already carries IB-hm-1's issuance (the gate keys one issuance to the round); it depends on IB-hm-1's graded facts, so it could not have been cut in the same issuance.

Check IBHM2 (`deliverables/2.0.0_SA_COO~P2/checks/r248/p248_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control248.py`, synthetic git repos) passes the three positives and each of 10 negatives fails its own arm (0 unexpected; it caught a parsing defect in my own check on the first run).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-2` | BUILD `emit_hmac_list` as the LAST stage of `run_firm`, isolated, with ten named tests | FWD-21 | LOCAL | IB-hm-1 | PM6-b |

fanout: 2 of 6 chains cut (IB-hm-1 graded, IB-hm-2 now), cap 8, reason: IB-hm-3 waits on the runner profile fact and on IB-hm-2's argument names; IB-hm-4 on 3; IB-hm-5 and 6 on 4 and the IB2 lane.

## 244. ROUND 8, WORKSTREAM ~PM (the served account-id HMAC list producer, cell 3: REGISTRY and BUILDER outputs; 2026-10-17 ~04:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO ruling B, msg 10234, and rule 30)

The dell2 CTO ruled (msg 10234) that the secret read and the three puts live on a NARROW role the stage assumes (`secretsmanager:GetSecretValue` on the one secret, `s3:PutObject` on the three firm keys; the host profile gains only `sts:AssumeRole` on that one role; the trust policy names the host's role only; the pair says plainly that B buys attribution (CloudTrail AssumeRole, fixed session name `hmac-list-stage`) and one place to revoke, not isolation). Rule 30 makes every name and address builder output. The READ cell found the registry has no globgrph product row, no irpt SECRET row and no HMAC-list home, so this cell adds the minimum rows and records the builder calls whose results the Terraform and dispatch cells will carry. The remaining chain, revised: `IB-hm-7` (the stage assumes the role: an argument `--hmac-role-arn` and the fixed session name, after IB-hm-2 lands), then `IB-hm-8` (Terraform: the secret container, the narrow role, the host-profile `AssumeRole`, tests by static markers) and `IB-hm-9` (`refresh.py` `runner_script` passing the arguments from the Lambda environment) in one later round, then the pair (IB-hm-4), the apply by IB2 (IB-hm-5) and the readers (IB-hm-6). It takes round 8 of ~PM because round 7 carries IB-hm-2's issuance.

Check IBHM3A (`deliverables/2.0.0_SA_COO~P2/checks/r249/p249_cells.py`), dry-run at the base: AC1 to AC3 all FAIL; the control (`control249.py`, synthetic git repos with a stub naming module) passes the three positives and each of 14 negatives fails its own arm (0 unexpected).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-3` | REGISTRY rows and recorded builder calls: three firm key addresses (globgrph bucket), the stage role and policy names, the irpt SECRET row | FWD-21 | WORLD (gate floor: an infra/ path) | IB-hm-1, CTO msg 10234 | PM8-a |

fanout: 3 of 9 chains cut (IB-hm-1 graded, IB-hm-2 running, IB-hm-3 now), cap 8, reason: IB-hm-7 waits on IB-hm-2's landed stage (same file); IB-hm-8 and IB-hm-9 wait on IB-hm-3's recorded names. A cell id takes no letter suffix by the decomposition grammar (the gate refused `IB-hm-3a`), hence the numbers.

## 245. ROUND 9, WORKSTREAM ~PM (the served account-id HMAC list producer, cell 7: the stage ASSUMES the narrow role and accepts the list bucket; 2026-10-17 ~04:3xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO rulings msg 10203 and 10234)

IB-hm-2 (BUILD, graded: IBHM2 AC1 to AC3 re-run PASS in the worker's worktree by me, the proof VALID; the worker's runner diff read whole) landed the stage `emit_hmac_list`. Two points of its diff do not match the later rulings, and both are mine to correct because my order left them open: (1) it REFUSES a destination whose bucket is not the firm's own bucket (`_parse_hmac_uri`), a constraint the worker added to keep the stage from overwriting a directory object; the CTO ruled (msg 10203) that the list goes to the globgrph folder, so the bucket is the one the URI names and the refusal narrows to a key inside a directory prefix of the firm's own bucket; (2) it reads the secret and puts the object under the ambient (host) session, but the CTO ruled B (msg 10234): a narrow role assumed with the fixed session name `hmac-list-stage`. This cell makes both changes in the one file with six new named tests. The check IBHM7 (`deliverables/2.0.0_SA_COO~P2/checks/r250/p250_cells.py`) dry-run at the base: AC1 to AC3 all FAIL; the control (`control250.py`) passes the three positives and each of 10 negatives fails its own arm (0 unexpected).

Side notes from the worker's rows (all OBSERVATION, INERT): `W449-S1` the status when upload is off is a distinct value (`skipped_no_upload`); `W449-S2` one `--hmac-list-uri` names one object, so `main` refuses it for more than one firm (the dispatch is per firm); `W449-S3` the runner test folder is red at base (136 failed, 20 errors, identical after), which is not ours. One edge to carry into the pair: a client carried forward from the previous directory (terminated) contributes its minted hex but not a raw key (the raw keys exist only for entries built in this run).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-7` | BUILD: `--hmac-role-arn`, `assume_role` with the fixed session name for the secret read and the put; the destination bucket rule; six tests | FWD-21 | LOCAL | IB-hm-2 (merged), CTO msgs 10203 and 10234 | PM9-a |

fanout: 4 of 9 chains cut (IB-hm-1 graded, IB-hm-2 graded, IB-hm-3 running, IB-hm-7 now), cap 8, reason: IB-hm-8 (Terraform) and IB-hm-9 (dispatch arguments) wait on IB-hm-3's recorded names; IB-hm-4 on 7, 8 and 9.

## 246. ROUND 10, WORKSTREAM ~PM (the served account-id HMAC list producer, cells 8 and 9: the Terraform DECLARATION and the DISPATCH; 2026-10-17 ~05:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO rulings msgs 10203, 10234 and 10259)

The registry cell turned out to need no row (builder outputs recorded in `deliverables/2.0.0_SA_COO~P2/IB-hm-3_BUILDER_OUTPUTS_FOR_THE_HMAC_LIST_20261017.md`: the three per-firm list keys `s3://opal-data-assets/globgrph/<firm>/silver/account_id_list/hmac`, the role and policy names, the secret `irpt/hmac-list/key`), and the stage in the runner now assumes the narrow role (IB-hm-7, merged). The remaining build work is two independent cells cut in ONE issuance: `IB-hm-8` declares in Terraform, mirroring `principal_49f.tf` (the 49F source principal is exactly this shape: a narrow role the shared host assumes, names from the `opal_name` module, trust the host role ARN only, a header that says the apply is a separate signed order): the role and its two-statement policy (`GetSecretValue` on the one secret, `PutObject` on the three keys), the secret CONTAINER (no version, no value) and three additive environment keys on the directory refresh Lambda; it applies nothing and writes nothing outside the root, and reports whether the host role's identity policy needs an `sts:AssumeRole` statement in another root (a separate cell if so). `IB-hm-9` makes `refresh.py` hand the three arguments to each firm's build from those environment variables, validated like the source-role map (a value that is not safe is dropped), only when all three are configured, the script byte-identical otherwise.

Checks: IBHM8 (`r251`, static markers plus the builder re-run for the three URIs; control passes the three positives and each of 16 negatives fails its own arm, 0 unexpected) and IBHM9 (`r252`, pytest plus AST; control 12 negatives, 0 unexpected); both dry-run at the base: AC1 to AC3 all FAIL. IB-hm-8 is declared WORLD because the gate's floor for an `infra/` path is WORLD; it applies nothing. After both are graded: the never-widen pair (IB-hm-4), the apply by IB2 (IB-hm-5: the bundle mint, the plan, the secret value put once and never printed, one QA run, the first scheduled fire), the readers (IB-hm-6).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-8` | DECLARE the narrow role, policy, secret container and three Lambda environment keys (no apply) | FWD-21 | WORLD | IB-hm-3 (superseded: outputs recorded), IB-hm-7 | PM10-a |
| `IB-hm-9` | BUILD the dispatch half in `refresh.py` (validated arguments, byte-identical when absent) and six tests | FWD-21 | WORLD (gate floor: an infra/aws/lambda path) | IB-hm-7 | PM10-b |

fanout: 2 of 2 chains cut this round, cap 8, reason: the two cells touch disjoint write surfaces (one Terraform file and `schedule.tf`; `refresh.py` and its tests), so they run in parallel; IB-hm-4 waits on both.

## 247. ROUND 11, WORKSTREAM ~PM (the served account-id HMAC list producer, cell 10: the HOST ROLE may assume the stage role; 2026-10-17 ~05:4xZ, issuer 2.0.0_SA_COO~P2 on dell2, on the CTO ruling msg 10234 and the finding of worker ~454)

IB-hm-8 (graded and merged) declares the stage role in the `directory` root with a trust that names the shared daily-runner host role only. Worker ~454's step 6 read the host role's identity policy (`infra/aws/terraform/mdpf-pipeline/iam.tf`, the `mdpf_runner` inline policy) and found it holds an `sts:AssumeRole` statement for the 49 Financial source principal (Sid `IrptDirectory49fAssumeSourcePrincipal`, lines about 659 to 664, Resource built from the builder name `module.irpt_49f_directory_read_role_name.name`) and none for the stage role. The CTO's ruling (msg 10234) says "the host profile gains only `sts:AssumeRole` on that one role". Whether the statement is strictly needed in one account (a trust policy that names the role ARN suffices unless a permission boundary or an SCP intervenes) is NOT measured; the statement follows the precedent in the same policy and the ruling, and the apply's step 5 reads the assume as the host would make it. This cell adds, in the OTHER root, one name module (`irpt_hmac_list_stage_role_name`, builder inputs system irpt, function hmac-list-stage, kind role, no scope) and one statement (Sid `IrptHmacListStageAssumeRole`), additions only, nothing applied.

Check: IBHM10 (`r253`, diff-based: additions only, one module, one statement, no wildcard, no Principal; the builder re-run; the one-commit surface; control passes the three positives and each of 12 negatives fails its own arm, 0 unexpected); dry-run at the base: AC1 to AC3 FAIL. WORLD because the gate's floor for an `infra/` path is WORLD; it applies nothing. The apply is a second leg of the HMAC list apply (a change of 1 resource in the `mdpf-pipeline` root, a root other projects also apply: the pair counts its writers).

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-10` | DECLARE the host role's `sts:AssumeRole` statement for the stage role and its builder name module (no apply) | FWD-21 | WORLD | IB-hm-8 | PM11-a |

fanout: 1 of 1 chains cut this round, cap 8, reason: one cell, one file in the second root; IB-hm-4 (the pair) now waits on IB-hm-10 too.

## 248. ROUND 12, WORKSTREAM ~PM (the served account-id HMAC list producer, cell 5: the APPLY in the `directory` root; 2026-10-17 ~07:2xZ, issuer 2.0.0_SA_COO~P2 on dell2, under the signed pair: packet blob e6d82eb31f with the CTO half @f52943766f, msg 10336, and ADDENDUM 1 blob cbcf940fbc with the CTO half @f953fdedd3, msg 10358)

All build cells are graded and merged (IB-hm-2, 7, 8, 9, 10; IB-hm-3 superseded). The pair is signed. This cell hands the apply to `0.7.0_AE_CloudOps~IB2` in the order the ADDENDUM corrected: the runner bundle first (the live runner uses strict `parse_args` and would refuse the three arguments the Lambda hands every build once its environment keys exist; the new runner with the arguments absent behaves as before), the refresh Lambda zip at the pinned digest `I7T8wRYmv11nytYpD7i+4XCwwvy6JUaB3fdsgtHyXmA=` (built twice by me at HEAD `94831b912e`; live against built, only `refresh.py` differs, touched only by IB-hm-9), the `directory` root through `safe-apply` (3 to add, 1 to change, 0 to destroy), the simulation battery, the secret value put once and never printed, and ONE QA run read as PASS or FAIL per check. The CTO added a condition: `lib/tests/test_trading_calendar.py` is run and printed before the mint. The `mdpf-pipeline` leg (the host role's statement, IB-hm-10) is NOT in this order: that root has a second writer whose ledger read OPEN at the CTO's reading (MDPF_CANON FWD-10, c5dd8b293a); it is a later order cut when that ledger closes, followed by the one more QA run the addendum allows. The first scheduled fire's read (Monday 2026-10-19 13:30Z) and the readers' grant (IB-hm-6, with the laptop CTO's pull tool and hook edit) follow.

Check: IBHM5 (`r254`, a record-based apply check: gates, legs, after-reads; control passes the three positives and the assume-fact-true variant and each of 32 negatives fails its own arm, 0 unexpected); dry-run at the base: AC1 to AC3 FAIL (no record). WORLD.

| cell | item | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `IB-hm-5` | APPLY by IB2: bundle, zip, `directory` root, simulation, the one secret put, one QA run | FWD-21 | WORLD | IB-hm-8, IB-hm-9, IB-hm-2, IB-hm-7 (all complete), the signed pair | PM12-a |

fanout: 1 of 2 chains cut this round, cap 8, reason: the second chain (IB-hm-11, the `mdpf-pipeline` leg) waits on the other writer's open ledger on that root and is cut when it closes; IB-hm-6 (readers) waits on this apply.
