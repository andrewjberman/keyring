# Security data and filings: current path and completion brief

**Proposed closer S.** Own identity, numeric inputs, filings, derived security facts and successful on-demand collection through the shared API integration. Primary authority: `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` v0.24, FWD-1..20. This brief does not replace those outcomes.

## End-to-end assessment

| Connector | Evidence now | Required completion |
|---|---|---|
| Covered/library/held name -> canonical identity | Latest crosswalk: 96 records, 36 MEASURED / 60 UNRESOLVED. Latest universe: 250 names, 191 MEASURED / 59 UNRESOLVED, dated September 16. CORPUS backlog: 93 folders, 33 resolved. These are different denominators. | One dated reconciliation of each population; executable induction requests consumed by the identity owner; explicit ambiguous, ADR/local-listing and slash-bearing-name controls. Do not replace any denominator with another. |
| Explicit request -> queue -> terminal consumer -> durable state | `opal-research-pull-enqueue` deployed; `pull_consumer.py` provides a bounded box-side Bloomberg pull/derive consumer. `/api/scoped/amgt/refresh` merely declares its carrier and enqueues nothing. Frontend `requestRefresh` types the result as `{queued: boolean}`. | Prove the real click/request reaches the declared enqueue route and consumer, shows FETCHING then LANDED/FAILED, and surfaces terminal unavailable distinctly. Do not count HTTP 200 as queued. Expand orchestration only to the contracted channels; no invented daemon. |
| Bloomberg -> bronze -> typed numeric/derived model | Current bucket contains 49 refdata, 49 histdata and seven bestdata bronze objects, plus 123 physical objects under `derived/model_block`. | Per-security/mnemonic/period/basis coverage matrix, replay from retained inputs, dedupe, bounded recovery and explicit absent reasons. Counts do not establish populated fields or freshness. |
| Identity -> annual filing -> accepted document | Ordered battery exists: ticker EDGAR, Bloomberg CIK, LEI ESEF, bounded company site, national regulator. HKEX is the only implemented national-regulator adapter in inspected source. | First **accepted annual** report wins under right-entity/current/family checks; retain exact source and passage lineage for every successful rung. Quarterly forms needed by the new report must be added explicitly. |
| Accepted filing -> source persistence -> analysis -> Thesis | Round 36 packet records HKEX stock-ID fix and fixture win propagation (111 tests). It does not establish a live Lenovo annual-report-to-Thesis result. Latest bucket has 180 filing-attempt state objects, 12 drafting objects; annual analysis and unresolved markers coexist. | One controlled live validation chain through the real writer, gate, served object, browser and source click. Repair source persistence for successful battery rungs and registry/IAM support together. Preserve held/newer versus served state. |
| Numeric facts -> management, peers, Posture, scores | 18 management, 797 peers, 33 Posture and 66 scores physical objects in legacy roots. Five-tab source UI exists. | Distinct latest-security coverage and freshness, valid comparable universe, officer/tenure lineage, explicit missing checks, numeric house-case forecast and independent FCF/divergence control. No count-based PASS. |
| API -> page -> checks | 16 AMGT API routes have deployed CUSTOM authorizers. Actual API ZIP has four differing members out of 48 inspected; local header check-face and changed-held marker additions are not in deployed `scoped_amgt.py`. | R integrates S's fixes and verifies actual deployed bytes/IAM and authenticated responses. Each displayed figure must carry its applicable checks, basis and as-of. |
| Page -> saved versions / print | Versions enumerate model-block stamps. Print consumes the block selected by the API and verifies identity; that is valuable existing work. | Preserve those controls; R adds immutable full-report revisions and frozen export without confusing numeric versions with report history. |

## What to retain and what remains open

Retain the identity resolver and builders, generated harvest prefixes, filing family/acceptance logic, typed numeric readers, check-face and existing print renderer. Do not replace them with a parallel research stack. The September 23 round-36 packet at `ledger/ROUND36_L8_PACKET_20260923.md` and `ROUND_ANALYSIS.round35.md` distinguish a fixed discovery mechanism from a proven final report. The packet also identifies reproduction scratch outside the committed tree; accepted closure must retain reproducible evidence durably.

Current `project.json` phase wording lags the available round-36 packet. This package uses exact orders and artifacts, not the phase sentence, for present state. The pending Lusha order rk-49 names its own website/key constraints; it is not justification to block unrelated reporting work. Prior records of shared-surface grant conflicts must be rechecked against current ownership before implementation, not inherited as facts about today's locks.

## Acceptance and scope retention

| RESAPP outcome | Gap register / acceptance home |
|---|---|
| FWD-1 covered pack; FWD-2 uncovered/on-demand | S02, R02, R03; actual request -> complete or explicitly partial pack |
| FWD-3 defensible numbers; FWD-10 visible checks | S05, S06; displayed figure -> retained source, basis, period and check result |
| FWD-4 recent commentary | H01, H03, H04; real article link from the security page |
| FWD-5 Adam's forwarded pack | R03, R04; retain actual operator acceptance, never manufacture forwarding |
| FWD-6 two saved versions | R03; selected immutable report versions, with numeric lineage |
| FWD-7 whole-population freshness | S01, S06, R02; denominator and per-channel state, not newest-object timestamp |
| FWD-8 peers; FWD-17 executives; FWD-19 Posture; FWD-20 house forecast | S05, R01, R02; sources and declared missing states plus positive controls |
| FWD-9 generated prose | R01, R02; machine marker and evidence gate on every served sentence |
| FWD-11 admitted social; FWD-14 lists/decay | S06; explicit source policy and owner, with any notifier conflict decided explicitly |
| FWD-12 per-input ledger/rerun; FWD-13 identity | S01, S02, S03; no duplicate pull or guessed security |
| FWD-15 four Lead Panel axes | H03, S06; Trending/Breakout crossed with Chatter/Price, correct server-ranked generations |
| FWD-16 description/feed/posture header; FWD-18 sourced Thesis/driver chart | S03, S05, R02; correct joined payload and visible accepted source |

Validation cohorts must retain the existing CAT, CSL, Keyence and Lenovo cases, plus a slash-bearing key (BP/ or NG/), an ambiguous identity, an uncovered name and absent-input controls. A representative proof is the release's first gate, not authorization to drop the remaining contracted population. Bloomberg or filing calls remain bounded by their actual granted run scope; no fleet rerun is inferred from this research request.

**Principal sources:** PRD v0.24; round-35 analysis and round-36 packet; `lib/research/{identity/crosswalk.py,filings/battery.py,api/scoped_amgt.py}`; `integrations/bloomberg/research/pull_consumer.py`; `portal/src/api/endpoints/amgt-lead-panel.ts`; `portal/src/pages/SecurityAnalysis/`; fresh evidence JSON.
