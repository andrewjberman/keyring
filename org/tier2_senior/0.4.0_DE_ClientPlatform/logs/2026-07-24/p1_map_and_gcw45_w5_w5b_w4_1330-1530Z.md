# P1 consumption map delivered + GC-W45 W-5/W-5b landed, W-4 built and held (1330-1530Z)

**archetype:** MIXED
**secondary_archetypes:** TRACE, IMPLEMENT, VALIDATE

- **Agent:** 0.4.0_DE_ClientPlatform
- **Window:** 2026-07-24 ~13:30Z -> ~15:30Z (session start -> now)
- **Workspace commits:** `b656257697` (P1 consumption map)
- **Portal commits (DEV):** `02fb2956` (W-5), `96e8c67d` (W-5b) -- both pushed
- **Held uncommitted:** W-4 render (blocking precondition, see Blockers)

## What was done

### 1. P1 CONSUMPTION MAP -- delivered, CTO-ACCEPTED
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/MDPF_P1_CONSUMPTION_MAP_20260724.md`
@`b656257697`, pushed `962ded51a`. CTO ACCEPTED 135700Z; COO relayed. Closes CTO DISPATCH
161738Z (parked post-serve 165038Z).

- Denominator: **10/10 useQuery hooks; 17 distinct served keys; 13 in MDPF generator scope;
  12/12 existing in-scope keys downloaded and field-checked live.** Subtree components fetch
  NOTHING -- verified, not assumed.
- **Superseded the 07-22 audit AS A KEY LIST**: +597 lines, a 332-line read module, a 10th hook
  and a new key family (`json/mdpf/{firm}/aum-metrics.json`) since `08c6d8b2`. Re-walking found
  it; re-reading would not have.
- APPLIED grounding (Rule 22a): live `get-distribution-config EVTSA9VEHNZVH` -> 24 behaviors,
  **NO `/api/general/mdpf/*` behavior exists**; everything falls to `/api/general/*` ->
  `opal-data-portal-v2`. Live `get-function-configuration` -> publisher `ASSETS_BUCKET =
  opal-data-assets`, so its 11-key map is read by nothing. Corroborates 0.7.0's Lambda-layer
  refutation at the CloudFront layer.
- 8 findings. F-1 (Global/per-firm name their total differently -> the 147 tooltip defect) RULED
  by CTO as one access path + a required `basis` sibling. F-3 (49F/INF pre-contract
  cohort_provenance) folded into W-4. Write-attribution UNDETERMINED -> now a HARD gating
  precondition on the P1 build.

### 2. GC-W45 W-5 -- nullable count contract, BOTH layers (`02fb2956`)
`account_count: number` was a lie: **40 nulls of 447** in `aggregate[]` and in each of the 5
`by_model` series. Fixed `portal-proxy.ts:213-214` (SOURCE) + `aum.ts:404-405`
(re-declaration) -- the brief's S4.4 named only the latter. Plus `aum.ts:63 PeriodData`,
compiler-forced (tsc TS2322 proved the null flows from the same artifact); COO APPROVED it
as "the scope being discovered correctly", not scope creep.
**Fixed 3 of 10 declarations; the other 7 NAMED as UNCOVERED** (unverified, not innocent --
their artifacts measured 0 nulls today).

### 3. GC-W45 W-5b -- the `aum` sibling lie (`96e8c67d`)
Same lines, same artifact: **24 nulls of 447**. COO-approved as its own commit. The honest-null
propagation **REMOVED five pre-existing zero-assertions** (`totalGrowth: 0`, `totalGrowthPct: 0`,
`avgMonthlyChange: 0`, `peakAUM: 0`, `peakPeriod: ''`) and ADDED zero coercions. Deltas across an
unknown endpoint stay null; unknown points are EXCLUDED as peak candidates rather than coerced
(a 0 would compete in the comparison and could win an all-null series).

### 4. GC-W45 W-4 -- provenance visible at render (BUILT, HELD)
Measured the real vocabulary first: **six classes, not two**, splitting on VALUE-BEARING
(`band_2firm` 24, `frontier_stamp` 1) vs VALUE-NULL with three distinct MEANINGS
(`exempt_absorbed`, `lag_window`, `source_absent`). The old reader collapsed five into one
`interpolated_estimate` -- worse than ignoring the field, because the collapse is invisible.
Reader now carries the producer's raw class; band derives ONLY from the class; tooltip names it.

**AC-5 mutant PASSES** with controls:
| Render | REFAREAS | Meaning |
|---|---|---|
| CONTROL (real bytes) | 5 | baseline |
| MUTANT (ONE element flipped) | **6** | the flip moves the render |
| CONTROL re-run | 5 | determinism -- not run-to-run variance |
| VALUE mode, control bytes | 0 | Andrew's 07-23 Global materiality ruling INTACT |

Denominator trap (COO): all 24 `band_2firm` dates measured inside [2026-05-28..2026-07-17],
zero before `cottonwood_covered_first` -- the class-driven design inherits the boundary for free.
Four reframes in ~90 min changed the VOCABULARY only (no hardcoded N / firm / date ever entered
the path); "Partial basis (2 of 3 firms)" -> "Declared count basis (partner subset)".

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-cache collisions` | P1 audit | PASS | 105/105 useQuery sites, 0 unparseable, 0 type mismatches |
| `comp-routes behaviors` / `trace` x5 | P1 audit | PASS | uniform `/api/general/*` -> portal-v2; DESIRED plane, APPLIED confirmed separately |
| `comp-transform schema-check` x6 | P1 + W-5 | PARTIAL | resolved 2 of 6 components; **no pass claimed on the 4 it could not resolve** |
| `comp-transform fields ModelPortfolios` | P1 audit | FAIL (tool gap) | 7 paths vs >=45 enumerated; unchanged from 07-22, persists across two audits |
| `comp-platinum page ModelPortfolios` | P1 audit | **FAIL (tool defect)** | composes bucket `S3-opal-data-bd` for a behavior the live distribution binds to `opal-data-portal-v2`; 2 of 10 fetches traced |
| `comp-grep` | producer sweep | PASS | fed the UNDETERMINED write-attribution verdict |
| `comp-surface-check check` + `selfcheck` | W-5, W-5b | **BLOCKED rc=2, ACKed** | SEV1 `model_portfolios.headline`; selfcheck ALL PASS -- **it SEES portal and DOES block** |
| live `cloudfront get-distribution-config` | P1 APPLIED limb | PASS | 24 behaviors, no mdpf behavior |
| live `lambda get-function-configuration` | P1 APPLIED limb | PASS | `ASSETS_BUCKET=opal-data-assets` |
| live `s3api get-object` x12 / `head-object` x4 | P1 + W-4 | PASS | field-presence + null measurement |
| `bun run typecheck` (tsc -b) | W-5, W-5b, W-4 | PASS | five-state error-then-clean sequence = the positive control |
| `ui-smoke.mjs` x7 | W-4 AC-4/AC-5 | PASS | control/mutant/re-run/value-mode + 1 INVALID PROD baseline (retained on the record) |

**What worked:** grounding APPLIED on live primitives caught what DESIRED-plane tools got wrong;
measuring each artifact for nulls is what separated a real type lie from a correct declaration.
**What failed:** `comp-platinum`'s `--firm` default composes another firm's bucket for a
non-firm-routed behavior; `comp-transform fields` coverage unchanged across two audits.
**Gap found:** **CLAUDE.md Rule 20 was STALE** -- it described `comp-surface-check` as advisory,
portal-blind and unable to block. All three clauses exercised FALSE (selfcheck folds the portal
change, rc=2 BLOCKED, the portal pre-commit hook REFUSED the commit until an audited
`SURFACE_ACK`). Routed to CTO, who amended the rule the same hour.

## Instrument self-corrections (kept, because a silent re-run looks identical)

1. First AC-3 coercion scan **FIRED on `?? 0` inside the warning COMMENTS I had just written** --
   a text-match on a mechanism. Re-run over non-comment lines only.
2. First bucket check used `--query KeyCount` and returned `None` for BOTH target and control --
   the positive control failed, so the instrument was rebuilt on `Contents[]` before any verdict.
   A bare `None` on the target would have read as proof of absence.
3. Reported "205 account_count OCCURRENCES"; 205 was `grep -c`, which counts **LINES**. Python
   re-derivation: **245 occurrences / 205 lines / 20 files**. Mechanism proven (`aum.ts:344`
   carries two on one line). Corrected in the W-5b commit message; no fix decision affected.
4. `git log --since "12:00"` **silently excluded my own P1 commit** -- the host is UTC-4 and
   `--since` reads LOCAL. Re-derived with explicit `Z`. This is VERIFICATION LAW (11), hit again.
5. A live-PROD baseline render came back with Total AUA $0 / no charts (auth stub does not reach
   PROD data endpoints) -- declared INVALID and NOT cited. Attribution resolved instead by
   non-mutating `git show HEAD:`.

## Blockers

- **W-4 render: HELD, evidence-cited.** COO 145950Z made the class-set convergence with
  `0.4.0_DS_ClientPlatform~A` a **BLOCKING precondition** before the render lands. My half sent
  150215Z; their confirmation not yet received. Not assumption-blocked -- the gate is explicit
  and the counterparty is named.
- `git stash` for a render baseline was **correctly BLOCKED** by the shared-worktree gate. Worked
  around non-mutatingly (`git show HEAD:`), not overridden.

## Current State

- P1 map committed `b656257697`, pushed `962ded51a`, CTO-accepted. It is the write denominator
  for CTO's P2/P4 one-process-writes-both Lambda.
- Portal DEV at `96e8c67d` (pushed). W-5 + W-5b landed; typecheck clean; no render path touched
  by either.
- W-4 changes live UNCOMMITTED in the portal working tree: `src/lib/pairedProvenanceRead.ts`
  (six-class carry-through, `sourceClass` on the point, `VALUE_BEARING_NON_MEASURED`,
  `COUNT_CLASS_LABEL`) and `src/pages/ModelPortfolios.tsx` (`count_class` threaded on both firm
  branches, `trendCountBasisDates` + `trendCountClassByPeriod` memos, count-mode ReferenceArea
  band, `interp_total` traced from the PRODUCER total in count mode, tooltip basis note,
  `interpolatedRunsOverRows` parameterised with a default preserving prior behavior).
- Evidence PNGs staged at `%TEMP%/claude/w4shots/` -- they commit WITH the render.
- Joint finding pending with DS~A: `exempt_absorbed` is 20 ENUMERATED + 18 FALLBACK under one
  label, **and two independent searches found NO read-time discriminator** (theirs at the
  producer, mine across all six series + all 17 meta keys + a refuted trading-day hypothesis).

## Next Steps

1. **[0.4.0_DS_ClientPlatform~A]** confirm the class-set convergence -> unblocks the W-4 commit.
2. **[2.0.0_SA_COO]** one design call: the count band reuses the VALUE band's alarm-yellow idiom.
   Under Andrew's "declared contract, not a warning" reframe that reads wrong. Neutral or
   leave-as-is -- two-line change either way. Not mine to decide on a SEV1 surface.
3. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** route the **PRE-EXISTING null->0 coercion** on the count bar
   path (`ModelPortfolios.tsx` HEAD `:2084` and `:2303`) -- a missing per-model row renders as a
   real ZERO ACCOUNTS bar. Visible as zero-spikes in the daily count chart. Not mine, not in
   W-4's scope, real.
4. **[1.0.0_SA_CTO]** P2/P4 standing by; write-attribution must be RESOLVED (CloudTrail / runner
   logs) before any generator takes those keys.
