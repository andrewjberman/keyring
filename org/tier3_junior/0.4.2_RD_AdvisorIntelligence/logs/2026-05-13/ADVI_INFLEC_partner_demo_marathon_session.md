# Session Log — 0.4.2_RD_AdvisorIntelligence

**Date:** 2026-05-13
**Session:** ADVI_INFLEC partner-demo marathon — Andrew console-driven; 20+ ad-hoc fixes + INFTGT closure + 4 cross-firm investigations
**Mode:** /loop watchdog throughout; ad-hoc fixes interleaved with chain-coordination work

---

## Summary

Marathon partner-demo polish session driven inline by Andrew. INFTGT P1/P2 scope pass + correction (v1 → v2 after COO RAVC caught 4 false-negatives) → INFTGT 3-step atomic closure (COO `350c5e46d` + CTO `57e4f3cc1`). 12 portal CLOUD submodule bumps across the AdvisorIntelligence surface. 3 critical investigations routed to DS~C (CUSIP masking, NNA oscillation, BD cross-firm audit) all resolved within the session. 6 follow-on TOs documented for chain #26+ cycle.

Empirical evidence + verify-before-act discipline featured heavily — both for my own scope pass (corrected after COO RAVC) and DS~C's NNA-bug diagnosis (refuted my 3 hypotheses before locking the actual root cause).

---

## CLOUD Commits (parent repo, all pushed)

| Hash | Subject |
|------|---------|
| `27012c29f` | bump portal — Flat fee schedule tooltip wired (Brief B #4 IWM) |
| `98d4d8908` | bump portal — dim dormant client rows in IWM list |
| `7a7f3f73f` | bump portal — propagate fee_schedule_type endpoint fix |
| `64feb2b3f` | deliverable: INFTGT P1/P2 scope pass v1 (11 LANDED, 5+partial STILL-NEEDED) |
| `fafbe9718` | bump portal — TO-12 rank-delta column tenant-gated (Inflection hides) |
| `62fde4bdf` | deliverable: INFTGT scope pass v2 — 15 LANDED, 1 OBVIATED, 1 PARTIAL TO-11 (94% effective per COO correction) |
| `ab6483d9d` | bump portal — TO-11 quarter chip + $0 formatting |
| `d5e3bfc50` | bump portal — chip order Current LEFT canonical (revert) |
| `20a0f6407` | bump portal — ticker masking heuristic (CUSIPs render as security_name) |
| `ac7aa4fd2` | bump portal — strip-tracks-selection + Architect→Advisor Inflection lexicon |
| `a0a1806bb` | bump portal — drop GRO toggle on AdvisorAnalytics |
| `d28e01f8f` | bump portal — NNA empty-state prompt + final Architect→advLabel |

Plus session log + deliverable commits.

---

## Portal DEV Commits

| Hash | Subject |
|------|---------|
| `ca40f2e9` | feat(AdvisorPublicProfile): Tip "Flat fee schedule applies" tooltip when fee_schedule_type==='flat' |
| `15437aa4` | feat(ClientListPanel): dim dormant $0 client rows + tooltip |
| `97a88ab5` | fix(advisor-intelligence): propagate fee_schedule_type from summary.json#book through drilldown endpoint |
| `08844f09` | feat(AdvisorsTab): tenant-gate rank-delta column via showRankDelta layout flag (INFTGT TO-12) |
| `0913c616` | fix(TO-11): quarter chip chronological LTR order + $0 formatting (no "+" prefix on zero) |
| `7f4eb1a8` | fix(ConsolidatedOverviewPanel): revert chip order — Current LEFT canonical (anchor + walk-backward) |
| `6852817e` | feat(ticker-mask): substitute security_name when label is non-standard ticker (CUSIPs/CDs) |
| `a794e26b` | fix(DistributionTab): time-machine strip tracks selected segment + tenant-gate Architect→Advisor |
| `530bd53c` | fix(AdvisorAnalytics): drop GRO mode toggle (per-advisor growth_decomp not in pipeline) |
| `e3f34428` | fix(DistributionTab): NNA-mode empty-state prompt for right partition + last Architect string → advLabel |

---

## Major Threads

### 1. INFTGT Scope Pass + Correction + Closure

- **v1 deliverable** (`64feb2b3f`): 11 LANDED / 1 OBVIATED / 5+partial STILL-NEEDED (~71%)
- **COO RAVC caught 4 false-negatives** (TO-1b shipped 2026-05-11, TO-6 PartnerAnalytics already migrated, TO-8 cash_drag/activity_scan shipped, TO-14 funded-flag removed). My v1 relied on session-recall instead of empirical commit-log search.
- **v2 deliverable** (`62fde4bdf`): 15 LANDED / 1 OBVIATED / 1 PARTIAL TO-11 (~94%) after empirical re-verification.
- **3-step atomic closure**: COO `350c5e46d` (JSON + REGISTRY) + CTO `57e4f3cc1` (PRD Status line)
- 2 follow-up TOs deferred to chain #26 cycle (TO-11 #3 Fee Summary + #4 BPS columns — both DS-emit gaps in `INF_D_02.build_detail_json` per DS base empirical check)

### 2. TO-12 RANK Column Tenant-Gate

- Added `TenantLayoutConfig.panels.advisorList.showRankDelta?: boolean`
- Inflection layout sets `showRankDelta: false`
- Threaded through `LeaderboardRow` + `LeaderboardPinnedRow` + `LeaderboardCards` + 3 view wrappers (NNA/AUA/GRO)
- 49F continues to see rank-delta column (default true); Inflection hides entirely
- Commit `08844f09`

### 3. TO-11 Sub-Items Polish

- **Quarter chip ordering** — first shipped chronological (Current right-most); Andrew corrected to canonical "Current LEFT + walk-backward"; reverted in `7f4eb1a8`
- **$0 formatting** — changed `>= 0 ? '+' : ''` to `> 0 ? '+' : ''` at 4 sites in client-drilldown chain (`AdvisorBookAccountDetail`, `AdvisorBookAccountModal` ×3). Zero no longer rendered as `+$0`.
- **#5 Newest Relationship** — covered by DS~C `52478bb3a` orphan client[0] fix (v1.7.54 deploy pending)
- **#6 BOOK GROWTH (TTM)** — covered by DS~B `2e5539bac` upstream emit
- **#3 Fee Summary chart + #4 BPS columns** — DS base confirmed `fee_summary` absent in 3-client cross-advisor sample → new TO to author for INF_D_02 emit work

### 4. Brief B #4 + Lambda v1.7.53 Sparse-Field Wiring (IWM Avg Fee Rate)

- Lambda v1.7.53 (DS~C `9301dfe97`) emits `book.avg_fee_bps_earned` + `book.fee_schedule_type='flat'` when >1000 bps cap fires
- FE side: types extended (`PlatinumAdvisorSummary.book.fee_schedule_type?: 'flat' | 'bps'`), endpoint propagation in `getPlatinumAdvisorDrilldownSummary`, Tip rendering at `AdvisorPublicProfile.tsx:586`
- IWM (small balances, flat-fee minimum) renders `—` + tooltip "Flat fee schedule applies. Small-balance accounts billed at a flat-fee minimum produce an effective rate too high to express in basis points; not a meaningful bps comparison."

### 5. Ticker Masking — CUSIPs / CDs / Annuities

- Andrew flagged "03XXXXEY7" on IWM client 564 looking like an account number
- Empirical: it's a partially-masked CUSIP for *Ameris Bk Moultrie Ga Ctf Dep 3.75% 8/18/2026* (a Certificate of Deposit). Orion API masks 4 middle chars at source.
- **FE quick fix (b)** shipped `6852817e`: endpoint enriches `concentration.items[].display_label` from top_holdings.json `security_name` when label fails `/^[A-Z]{1,5}$/`
- **DS-side (a)** shipped by DS~C `d12598087` cross-firm: shared `lib/display_label.py` in INF + BD, `display_label` field on top_holdings emit. Phase 3 sentinel verified: 1 substitution per case (Ameris CD on INF; indexed_annuity on BD). Empirical prevalence: INF 0.58%, BD 24%.
- Both layers active as defense-in-depth.

### 6. Time-Machine Strip Tracks Selected Segment

- Andrew flagged: with Patrick Scanlan selected in Distribution > Segment Analytics > ADV donut, the strip below still showed firm-total AUA ($202M) instead of Patrick's ($20.9M)
- Root cause at `DistributionTab.tsx:3280` — `parentSegmentKey={parentSegment?.key || null}` only checked drill-state parent (which is null when selected but not drilled). When Patrick was top-level-selected, `parentSegmentKey === null` → fell through to firm-total path.
- Fix: `parentSegmentKey={isDrilledDown ? (parentSegment?.key ?? null) : (selectedSegment?.key ?? null)}`
- Strip now tracks the selected segment for each period via the per-period donut lookup

### 7. Architect → Advisor Tenant Lexicon

- Andrew: "Architect is 49F-specific term; Inflection uses Advisor"
- Added `TenantLayoutConfig.panels.advCohortLabel?: { singular: string; plural: string }` (defaults Architect/Architects)
- Inflection sets `{ singular: 'Advisor', plural: 'Advisors' }`
- 5+1 hardcoded sites in DistributionTab now use `advLabel` / `advLabelPlural`:
  - "AUA by Architect" / "NNA by Architect" panel headers
  - "Account Sizes by Architect"
  - "All Architects" breadcrumb
  - "Architects" drill-up button
  - "Search all architects..." placeholder
  - "Select a {state|advisor} to view ..." empty-state prompts (caught in DE polish followup)
- 49F continues to see "Architect" (default).

### 8. AdvisorAnalytics — GRO Toggle Dropped

- Andrew: per-advisor growth_decomp not in pipeline; GRO toggle's empty-state was UX noise
- `MODE_OPTIONS` reduced to `[aua, nna]`; helptext updated
- Commit `530bd53c`

### 9. NNA Oscillation Investigation (Critical Diagnostic Routed to DS~C)

- Andrew flagged Patrick Scanlan Lifetime Activity: AUA smooth ramp $0.5M→$20.9M Q2'20→Q2'26, but NNA showed near-perfect alternating ±$15M from Q3'24 onward
- **My 3 hypotheses** (all wrong): re-attribution artifact, double-counting by source_system, bronze-walk window drift
- **DS~C empirical refutation**: per-account decomposition Q4'24 showed clean values, biggest single-account inflow $640K, NO paired +/− entries
- **Actual root cause**: Lambda sparse-cumsum dict-lookup bug at `inf-portal-advisor-publisher/lambda_function.py:794-811`. `canonical_nna` is sparse (696 of 2170 dates have activity); `can_lookup.get(date_str, {})` returns `{}` on no-activity dates → falls back to 0.0. FE quarter-end deltas turn the flicker into ±$15M phantom flows.
- **Fix** (DS~C `14c54aec2`): `reindex(daily) + ffill` replaces dict-lookup. Verified across all 4 INF advisors — Q-deltas match canonical_nna raw sums exactly (all 25 quarters for Patrick).
- **Cross-firm BD audit** (DS~C `74593520a`): BD is CLEAN today because canonical_nna upstream is daily-DENSE (zero-padded), not sparse like INF. Defensive fix shipped anyway — `reindex+ffill` is no-op on dense data + removes latent vulnerability if BD ever switches to sparse storage.

### 10. ADHC_INFDIM_ORPHAN — DS~C Two-Bug Diagnostic

- 19 IWM accounts had null `household_id` upstream → orphan client[0] phantom row
- Bug A (INF_C_07 walk-back-to-healthy-partition, MEMORY pattern C.1) shipped `90306935b`+`f948658e6` — 17/19 reattributed (Peter Lee × 16, Patrick Scanlan × 1)
- Bug B (silver→gold accounts_dimension_latest freshness) deferred to AE-lane TO; needed for 2 brand-new accounts (4268, 4269)
- DS~C orphan client[0] Lambda fix `52478bb3a` queued for v1.7.54 bundle

### 11. Cross-Tenant Defensive Patterns Established

Over the day, two cross-firm parity ships made via the same audit pattern:
1. **display_label cross-firm** (INF + BD same code, both visible bugs, single commit `d12598087`)
2. **Sparse-cumsum cross-firm** (INF visible bug, BD latent vulnerability, separate commits but same defensive logic)

Memory entries saved:
- `feedback_alternating_pattern_fingerprint.md` (RD-angle): alternating ±X same-magnitude in delta-from-cumulative chart = sparse-cumsum bug fingerprint
- `feedback_cross_firm_publisher_audit_pattern.md` (DS-angle, by DS~C): when fixing publisher Lambda bug in one tenant, audit the analog tenant's publisher Lambda
- `feedback_prefetch_localhost_prod_stack_divergence.md` (yesterday's memory; referenced today for v2.1.83 deploy context)
- `feedback_verify_before_status_claims.md` (RD: scope passes need git-grep + code spot-check, not session-recall)

---

## Pending Items at Session End

| Item | Status | Owner |
|------|--------|-------|
| AE v1.7.54 Lambda bundle apply | Pending AE 0.7 source-map unblock | AE 0.6.1 |
| INF visible-bug closure post-bundle apply | Pending bundle | (5 fixes in bundle: orphan + display_label + mix_periods + avg_fee_bps + sparse-cumsum) |
| BD defensive sparse-cumsum fix materialization | Next BD nightly chain | (gold-d 04:00Z) |
| TO-11 #3 Fee Summary emit | New TO authoring | COO (DS-emit gap confirmed) |
| TO-11 #4 BPS columns emit | Same TO as #3 | COO |
| INF_C_07 Bug B silver→gold freshness | AE-lane TO | COO (post-v1.7.54) |
| ADHC_INFPUBHRD hardening proposal | Drafted `a449ad6e9` at `docs/briefs/proposal-inf-portal-advisor-publisher-hardening.md` | COO to route when bandwidth |

---

## RAVC Chain Summary

| Direction | Count |
|-----------|-------|
| Inbox messages processed | 30+ |
| Outbound messages | 25+ |
| RAVC ACKs sent | 12+ |
| Briefs drafted today | 4 (DS investigations: IWM book.json, fee data, ticker masking, NNA oscillation) |

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `bun run tsc --noEmit` | portal | 0 errors (12+ runs across iterative edits) |
| `git log --all --oneline --grep=...` | every TO claim in scope pass v2 | Empirical verify-before-act for all 17 TOs |
| `comp-transform schema-check` | InflectionInsightsPanel, AdvisorPublicProfile, DistributionTab | CLEAR (multiple runs) |
| `aws s3 cp ... composition.json` / `top_holdings.json` | client 564, peter_lee, IWM | Live data verification for ticker masking + NNA chart bug |
| Visual smoke (DEV server, mental) | Patrick selection, IWM advisor page, lifetime activity NNA | Each fix manually verified against the screenshot evidence |

---

## Lessons Captured (Memory)

1. **Alternating ±X same-magnitude pattern fingerprint** — not always data-quality artifact; can be publisher dict-lookup-on-sparse-source bug. Per-account decomp refutes data hypotheses cheaply.
2. **Verify-before-act on scope claims** — git-grep + code spot-check for EVERY status claim; session-recall produces false-negatives. My v1 had 4; COO caught all 4.
3. **Cross-firm publisher audit pattern** — when fixing publisher Lambda bug in one tenant, audit the analog. Two wins today (display_label visible, sparse-cumsum latent).
4. **Defense-in-depth FE backstop + DS contract** — multiple layers active. When DS emits the canonical field (display_label, fee_schedule_type), FE reads it directly; when DS doesn't, FE heuristic kicks in. Both stay active.
5. **Lambda overwrites narrower schema** — `inf-portal-advisor-publisher` Lambda overwrites INF_D_04's emit with its own (narrower) schema; any DS-side schema additions get silently dropped. 3 bugs of this shape found today; hardening pass proposed.

---

## Status

End of session. Bench-available pending AE v1.7.54 bundle apply.

INFTGT closed at 94% effective. v1.7.54 Lambda bundle (5 fixes from DS~C across 4 commits) ready to apply once AE 0.7 unblocks source-map. Post-apply: I run visual smoke on Patrick + Peter Lifetime Activity NNA mode; DS~C runs Q-delta validation against canonical_nna raw sums. Then RAVC2 to COO closing today's loop.
