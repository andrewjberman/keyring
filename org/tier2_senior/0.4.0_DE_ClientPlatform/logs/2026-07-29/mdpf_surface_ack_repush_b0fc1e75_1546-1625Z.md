# MDPF: 72f132c5 SURFACE_ACK re-push (b0fc1e75) + two-carrier root cause + cottonwood item-2 prior art — 1546–1625Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, TRACE

## What

Fresh session (spawned by MSTR 154626Z; predecessor died holding unread mail — 6th session-edge loss
today). Startup clean: registered PID 13452, watcher Monitor armed task `bgbbb911n` and confirmed
`running`, LD-0290 serial file written, A.3 PATH probe 93/93 resolve AND a forwarder actually RAN
(exercise half, not just `command -v`).

**Shipped: portal DEV `b0fc1e75`** (`72f132c5..b0fc1e75`, 1 file, +17, comment only). Closes the item
CTO and DT both had open: `72f132c5` was CI-RED as DEV head on a missing `^SURFACE_ACK:` line.

### The fix is NOT the obvious one, and the obvious one would have been wrong

`surface-check.yml:113` extracts the ack over `before..after` — so DT's "empty re-push with the ack
line" reading is right about the ack. But `:71-85` computes the CHANGED-FILE SET from the SAME range
and `:94-96` exits 0 on an empty set. **An empty commit carrying only the ack would have gone GREEN
WITHOUT THE CHECKER EVER EVALUATING THE SEV1 SURFACES** — a vacuous pass, and the exact green-theater
the workflow's own `:55-69` asserts exist to refuse. It would also have failed DT's stated condition
(a), a *genuine* pass.

So: landed the `1e4bdf14` shape — a real change to the file, carrying the anchored ack. Checked for
residue first and found NONE (`trendMetricType` fully gone; every candidate import still ≥2 uses;
tsc clean), so I did **not** manufacture a cosmetic diff. Landed instead the thing genuinely missing:
an in-code marker at the Trend Analysis panel header — where the toggle used to render, and where
that flex container is now visibly one-child — recording that the absence is DELIBERATE and carrying
Andrew's ~1425Z rationale verbatim. Zero behavioral change. Same remedy DT/CTO require on the
sleeve-level restore, applied to a deletion rather than an addition.

## ROOT CAUSE of all three ack misses today — TWO CARRIERS, not memory

The recurring miss is structural, and the agent who missed it HAD acked and HAD been told it worked:

```
carrier 1  pre-commit HOOK -> reads the SURFACE_ACK ENVIRONMENT VARIABLE
carrier 2  portal CI GATE  -> reads a ^SURFACE_ACK: LINE IN THE COMMIT MESSAGE
```

`72f132c5` satisfied carrier 1 ONLY. Artifact proof, `org/surface-check-ack-audit.log`:
`20260729T132308Z SURFACE_ACK surfaces=...headline reason='ANDREW-DIRECT ~0845Z via COO 124351Z...'`
The hook printed `SEV1 ACKNOWLEDGED ... Proceeding` and passed the commit, so nothing signalled a gap.
My own predecessor log (`..._1300-1325Z.md:35-36`) records "acked with audited SURFACE_ACK" — **and it
was telling the truth.**

**The discriminator is sitting in the same audit log.** Today's two CI-PASSING commits carry reasons
that literally say so — `051314Z` "ack carried in commit message", `052449Z` "ack in commit message" —
and `132308Z` does not.

**Gate proposed to CTO (one assertion, portal-side, small):** if the pre-commit hook fires an env
`SURFACE_ACK`, REQUIRE the message to also match `^SURFACE_ACK:`, else refuse. The failure is
structurally "carrier 1 without carrier 2" and never the reverse. A checklist cannot close it.

## Cottonwood item-2 prior art — READ-ONLY, changes the data-side ask

CTO's direction (via MSTR 161608Z) said cottonwood has no `non-model-assets.json` so "there may be a
data-side precondition." Found the prior art he asked for; it inverts that ask. @ `b0fc1e75`:

- `ModelPortfolios.tsx:550-552` — `non_model_assets.json` is **RETIRED estate-wide** (Andrew-direct
  ~0340Z; AE~A tore it down). No legacy fetch remains on the page.
- `ModelPortfolios.tsx:792-794` — per-firm Non-Model comes from the artifact's `non_model_aua`;
  `isPerFirm` guards against using global `nonModelData` for a per-firm view. **"zero pre-backfill =
  correct"** — which is cottonwood's exact current state.
- `ModelPortfolios.tsx:775-778` — Cohort-1c fold (Andrew-direct 2026-06-01): SMA sleeves fold into the
  combined Non-Model band (`non_model_aua + sma_aua`).
- Accessor: `pairedProvenanceRead.ts:319` / `:327`.

**Consequence:** asking DS~A to "produce cottonwood's non-model-assets.json" would rebuild an artifact
Andrew killed today, and the page still would not read it. The real precondition is the FIELD —
cottonwood's platinum per-firm `non_model_aua` must be populated (CTO's own byte-measure: `non_model
0/450`). On current evidence the render half is already CORRECT and item 2 is a DATA gap with no portal
work required. **Flagged to CTO as INFERRED, not verified** — I have not field-read the live platinum
cottonwood artifact; present-and-empty vs absent need different DS~A asks, and I said so rather than
letting an inference land as a ruling.

## Verify

- CI on `b0fc1e75`, measured via `gh` (not self-reported): `Surface-Check Gate` completed/**SUCCESS**;
  `CI - Build & Validate` completed/**SUCCESS**.
- **Genuine, non-vacuous pass proven from run 30469462795 stdout:** `changed portal file(s):
  src/pages/ModelPortfolios.tsx` → `Running comp-surface-check --mode blocking on 2 portal file(s)` →
  `CRITICAL: model_portfolios.benchmark (SEV1)` + `CRITICAL: model_portfolios.headline (SEV1)` →
  `SURFACE_ACK present ... audited to org/surface-check-ack-audit.log. Proceeding.`
- `tsc -b --noEmit` clean. eslint on the file: 0 errors / 4 warnings, all pre-existing
  (`react-hooks/preserve-manual-memoization` @ :967, unrelated to the edit).
- Pre-commit hook exercised the real path: raised both SEV1 CRITICALs, accepted the env ack, wrote
  `20260729T160921Z` to the audit log. Not a bypass.
- **Positive control earned its keep:** `gh run list --commit <sha>` returned `[]` while
  `--branch DEV` showed both runs — the `--commit` filter was a broken instrument, not evidence of
  missing runs. A zero from a filtered query got a control before it became a finding.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` (surface-check gate mechanism) | **NO CURATED RULE** | scored all 68 below the vetted band; correctly refused to fake a route. Answered by reading `surface-check.yml` directly. |
| `comp-which` (non-model display prior art) | **MIS-ROUTED** | returned `comp-surface-check` (a SEV1 guard) for a RENDER-path question. Wrong axis. |
| `comp-grep` `non_model\|nonModel\|readNonModelSeries` | **PASS** | the productive call — localized all three prior-art sites + the accessor in one pass with dependency context. |
| `comp-surface-check` (via portal pre-commit hook) | **rc=0, SEV1 ACKNOWLEDGED** | correct verdict on a deliberate MP-surface change; ack audited, not bypassed. |

**What worked:** `comp-grep` on the non-model question — exactly the Rule-21 case, one call surfaced
the retired-artifact comment, the per-firm guard and the Cohort-1c fold together, which a text-local
grep would have returned as three disconnected hits.
**What failed:** both `comp-which` calls. One honestly refused (good failure); one routed a render
question to a surface guard.
**Gap found:** `comp-which` has no coverage for CI/gate-mechanism questions ("which commit does the
gate read the ack from") and mis-routes render-path questions on SEV1 files toward the SEV1 guard
purely on filename overlap. Second consecutive session logging a `comp-which` gap on this page shape.

## Files Modified

| File | Change |
|---|---|
| `portal/src/pages/ModelPortfolios.tsx` | +17, comment only — deliberate-absence marker at the Trend Analysis panel header, Andrew ~1425Z rationale verbatim. See `b0fc1e75`. |

## MCP traffic

7 total. Significant: DT 141909Z/143343Z (NOT PROMOTABLE + ack text) — **RAVC closed** with green
evidence at 161838Z. DT 144943Z/155644Z (Andrew-authorized sleeve restore + blend-only revert build
request) — **ACK'd, HELD, not started.** MSTR 161608Z (CTO verbatim direction, cottonwood render half)
— **checked in with CTO 161925Z** as ordered; item-2 prior art 162159Z.

## Blockers

None assumption-based. Three external gates, all evidence-cited with named owners:
1. **[1.0.0_SA_CTO]** design gate on cottonwood items 1-4 — CTO stated "none of them to build before
   CTO gates the design." Not started.
2. **[1.0.0_SA_CTO]** the (A)-override word + topology word on the blend-only revert. DT explicitly
   said do not start on his message alone.
3. **[1.0.0_SA_CTO]** disposition on whether to build the two-carrier pre-push gate now or post-fires.

## Current State

- **portal DEV head = `b0fc1e75`** (was `72f132c5`). Both CI checks SUCCESS. `origin/DEV` == local.
- `72f132c5` (toggle removal) **stays on DEV UNPROMOTED** per Andrew ~1545Z. It is now merely
  *promotable*, not promoted. Nothing from me asks DT to promote it.
- Topology per DT (measured): `origin/PROD` 83afea3f already contains `70166741`; DEV = PROD + the
  toggle removal + this marker.
- **Blend-only revert NOT STARTED.** When CTO rules: branch off `origin/PROD` (NOT DEV), hand-apply
  the blend hunk ONLY (`totalHoldingsSleeveLevel` = `total.account_count` + blend-cohort counts, plus
  the `AccountDistributionMetrics` call site), leave `totalUnfundedCount` a field read (stays 49 — a
  wholesale `git revert 70166741` would drag the unfunded footnote back to the cross-artifact
  subtraction, 257, which nobody asked for), and land the Andrew-authorized-interim marker with
  verbatim + date + the `total.sleeve_level_count` successor named.
- Cottonwood global account-distribution aggregation (49f 7,053 + inf 544 = 7,597, cottonwood's 292
  absent) is **producer-side, DS~A/AE — explicitly NOT to be compensated client-side** (mixed-basis
  07-24 vs 07-28).
- Watcher Monitor `bgbbb911n` live; broker summary current.
- **Record drift noted, not acted on:** `prompt.md:90` says DE "Cannot `git push`" — stale against
  CLAUDE.md Agent Autonomy (explicitly pre-authorizes push to CLOUD/DEV) and against DT's direct
  instruction to re-push. DT gates the PROD promote, which I have not touched.

## Addendum — CTO reply 162343Z (arrived during log write)

**Item 2 ACCEPTED and RETRACTED UPSTREAM.** CTO told DS~A to drop the "produce cottonwood
non-model-assets.json" item entirely. Both lanes converged independently: my half (render field-reads
`non_model_aua`, zero-pre-backfill = correct) and DS~A's half (`non_model_aua` is a DERIVED BALANCE,
custody − model, undecidable on splice dates where custody is absent; a W-2b gate fails the build on a
fabricated one). **The empty Non-Model band is both sides behaving correctly.** Nothing to produce,
nothing to re-render.

**Item 1 sharpened and is now the live one.** DS~A found the real defect: `:587` copies the one-off's
provenance row verbatim, so 44 splice dates carry `interpolated_estimate` on cohorts whose VALUE IS
None — estimates asserted over nothing. My side renders `measured` / `interpolated_estimate` / `absent`
distinguishably, designed against the CORRECTED label semantics. Design only; build gated on DS~A's
design + CTO's gate.

**Item 3 NEW — answered read-only this window.** Confirm nothing reads global's 81,931 B
`non_model_assets.json`. **CONFIRMED: the read side is complete.** `comp-grep getNonModelAssets`
over `portal/src` = **2 matches / 2 files, scanned 404 of 404 in scope**: the definition itself
(`portal-proxy.ts:399`) and one COMMENT reference (`ModelPortfolios.tsx:802`). **ZERO call sites.**
The fetch function at `:406` is a live, exported, uncalled orphan. Caveat stated to CTO: the symbol is
exported, so a consumer outside `portal/src` or a dynamic reference would not appear in this scope —
within the stated denominator there are none. Routed as a zombie-artifact candidate for COO's teardown
list. **Reported, not deleted** (CTO: read-only).

**Item 4 in CTO's message is STALE — corrected back to him.** It says `72f132c5` is DEV head and CI-RED
on the missing ack. It was closed before his message: `b0fc1e75` pushed, both checks SUCCESS, and I had
already reported it at 161925Z. Likely crossed in flight.

**SURFACED, NOT ADJUDICATED:** CTO's item 4 frames DT as holding the promote on his two conditions
(and notes the publisher read has now FIRED at 16:15:32Z, satisfying the second). But Andrew-direct
~1545Z, relayed by DT, is LATER and says the toggle removal STAYS on DEV unpromoted. Latest +
most-restrictive is Andrew's. Flagged to CTO for his call; I have not acted on either reading.

**Also from CTO:** cottonwood platinum is NOT clobbered — 4 versions, 4 distinct etags, no interleaving,
all 37,518 B including today's 16:15:32Z publish. The publisher writes faithfully from a gold source
that lacks the interpolation. Nothing on the render side is being overwritten.

## Next Steps

1. **[1.0.0_SA_CTO]** design gate on cottonwood items 1-4; also (a) whether the marker-comment
   precedent satisfies the in-code interim requirement generally, (b) build the two-carrier gate now
   or post-fires.
2. **[1.0.0_SA_CTO]** (A)-override + topology word → releases the blend-only revert to me.
3. **[0.4.0_DE_ClientPlatform]** on CTO's word: field-read the live platinum cottonwood artifact to
   settle `non_model_aua` present-and-empty vs absent before that becomes a DS~A ask.
4. **[0.2.0_DT_PortfolioAnalytics]** nothing owed from me; `72f132c5` is green and promotable whenever
   Andrew wants it.
