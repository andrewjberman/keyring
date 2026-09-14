# MDPF_CANON v2.0 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~08:52Z · request: CTO message 96550.

**VERDICT: REFUSED, brief half.** The 30-entry denominator is correct. Three corrections are required in the consuming requirements: reconcile the firm-platinum address with the required builder, apply the builder prerequisite consistently to the bronze move, and specify how the existing portal callers reach the new scoped route. The other coverage dispositions and the explicitly open retirement-instrument decision are retained below.

## Exact review inputs

- PRD: `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md@3514843a123a72ddafa86e39f35dd179abd7dd6f`, v2.0, 400 lines.
- Brief: `docs/briefs/d8-mdpf-canon-migration-brief-20260913.md@fd579d3caf21b018bb06254c9ec63481a24f8299`, 337 lines.
- Reviewed brief-half SHA-256: `13cafd35564a53302b95db76c5d97ee809298b2f66508615f02e00799d88497e`.
- Ratified-text half, identified but not signed here: `aa9f141401d833e50c3a35f6934ded8266ebd0b6e4bc43e70dce7eef200e5f92`.
- Consumed contracts checked at the exact PRD pin: `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md` and `org/standards/NAMING_SCHEMA.json`.

Line numbers below refer to these pins unless explicitly labelled worktree. At review, HEAD and worktree PRD text both matched the offered PRD exactly. The canonical sign-off library calculated the two hashes above. The sequence check placed MDPF_CANON in stage 2, reported its LGIC_ENFORCE admission prerequisite MET and no project flags, with TRACK enforcement (`SEQUENCE.yaml@089ba2d431`). This is the assigned CRO review, not a migration act.

## R1 — The declared firm-platinum destination cannot be returned by the required builder contract

**Source obligation:** brief O2, O6 and IV.5 (lines 52–56, 75–79, 188–204) require a canonical firm-slice address and a scope-derived tenant boundary. IV.5 labels the layout a proposal to be ratified once. The PRD consumes the later ratified naming contract rather than defining an independent grammar.

**Conflict:** PRD CONTRACTS line 165 requires every string to come from `key()` / `address()`, and DEC-15, lines 278–281, rejects hand-spelled keys. Yet that same contract declares the concrete object address `s3://opal-data-{firm}/mdpf/{firm}/platinum/{leaf}.json`, repeated as the served-slice prefix in M9/M10, PATHS and the manifest (lines 317–318, 329, 391).

The consumed ENFORCE contract, lines 151–152, specifies `key(source, scope, tier, table, partition)` returning exactly **five segments**. `address(source, scope, tier, table, partition, object=None)` wraps that key with its registry-derived bucket and optional object. Its E3 acceptance at line 350 verifies the five-segment result. The naming schema, lines 23–36, gives the same grammar and keeps the object below the partition. MDPF's firm-platinum object has **four segments**: `mdpf / 49financial / platinum / aum-metrics.json`, for example. There is no documented builder argument vector that yields that result without dropping a required slot or changing the builder contract. This is a requirements incompatibility, not an implementation failure measured at runtime.

**Required correction:** decide a concrete, builder-compatible address mapping for the firm-platinum objects and carry it through CONTRACTS, M9/M10, route resolution, grants, PATHS and the manifest. Show at least one exact builder input/output vector for that family, preserving the served JSON shape and tenant boundary. If a different shape is required, resolve it at the owning schema/builder contract and consume that explicit contract; do not silently truncate the ruled key or add hand-spelled bypasses. Also bound the sentence “Every string comes from” to the applicable new addresses: the explicitly retained `platinum/mdpf/global/...` path is historical and differently ordered, and must not be silently moved to satisfy that sentence.

## R2 — M8 is exempted from the builder prerequisite despite writing a new canonical address

**Source obligation:** brief O7, lines 81–84, moves bronze into the canonical intake path; Part V, line 270, requires the shared path decision before emission. The PRD strengthens that obligation by consuming ENFORCE's builders for every new key.

**Conflict:** DEC-15 is titled “The key-bearing cells wait on LGIC_ENFORCE's builders,” but ends by exempting **M8** along with M1 and M7 (lines 278–281). The arc, line 294, likewise says the bronze move waits on nothing. M8, line 316, is an actual write/repoint/run into `s3://opal-data-assets/mdpf/{scope}/bronze/`; CONTRACTS line 165 says its string comes from the builders. M8 therefore cannot both proceed before E3 and satisfy the address contract. Independence from ADVI_FIRMBKTS's per-firm cutover does not remove this separate prerequisite.

**Required correction:** place M8's key-producing/repoint/run work behind E3, make `key()` / `address()` explicit consumed contracts in M8 and require its output address to be generated through them. Align DEC-15 and the arc. A read-only census or mapping phase may remain available earlier if it is separated from the dependent writes; the whole bronze move must not be labelled independent.

## R3 — The existing portal calls have no explicit transition to the new scoped route

**Source obligation:** brief IV.6, lines 206–214, names the portal consumers (`portal/src/api/endpoints/aum.ts`, `portal/src/api/portal-proxy.ts`, and the Model Portfolios page), their current `/api/general/mdpf/{firmId}/...` requests, and the required route-class change. O2 and the Part III bar require the legitimate advisor's page to work while another firm's session is refused. Part V, lines 276–277, requires the scoped route live before that firm's slice moves.

**Gap:** PRD DEC-5, lines 216–223, and M9, line 317, specify a scoped router, CloudFront behaviours and “the general route keeps only global.” PATHS lines 334 and the manifest at 392 allocate those infrastructure changes. They do not say what happens to the **existing firm-specific general-URL calls**: which callers change, or how those URLs are explicitly served with scoped authorization through a compatibility mapping. The portal is named as a consumer, but the transition for its known requests is not carried into M9's work or surfaces. A direct request to a newly added scoped URL could pass a negative test while the unchanged page continues asking the old general route for firm data.

**Required correction:** specify the chosen transition for existing caller URLs in M9. If the callers move to a scoped endpoint, declare the actual API-wrapper/source edits and their owner/deployment path. If their URLs are retained, specify the tenant-asserting compatibility mapping and its CloudFront/router ownership; retaining the old URL must not retain general authorization for firm data. Test the legitimate page's actual request path and the cross-firm attempt through that same transition, preserve general access to the composite, and state that this route/caller readiness precedes the slice switch. A frontend edit is not presumed necessary if an explicit secure compatibility route provides the transition.

**Evidence boundary:** the pinned brief supplies the caller finding. A supplemental local `comp-find 'api/general/mdpf' portal/src --all` found 16 hits across 792 files, including executable calls at `aum.ts:534,614` and `portal-proxy.ts:532`. Those files are present locally but absent from the offered CLOUD commit, so they are **worktree corroboration only**, not falsely attributed to that PRD pin or to deployed behaviour. Measured byte hashes: `aum.ts` = `f0c190d30334a30aa02cb66cfee196b9832806b483f623857f284e7f2ffb43cb`; `portal-proxy.ts` = `1f1f84b9f2dda4d147e6d8d8f492fbf82873f7f136136169cfa91970e5e60f65`. No live portal request was made for this review.

## Coverage audit — 30 entries

Measured from the pinned brief outside fenced code: **30 headings** = title plus Parts 0–VII (9), O1–O8 (8), IV.1–IV.12 (12), REFS (1). The PRD contains exactly coverage entries 1–30 at lines 352–381. Every entry is accounted for below; an entry's presence does not cure the conflicts in its consuming contract or cell.

| # | Brief entry | Content carriage and finding |
|---|---|---|
| 1 | Title / preamble | Midstream inheritance, D8 home, A-1/A-2/A-3, B1/B2, dedicated runner and never-widen boundary retained in preamble, CONTRACTS and DEC-1/14. |
| 2 | Part 0 | NOT CONSUMED as work, accepted as a method record. The old PRD's founding target and obligations are retained; DEC-12 expressly addresses MDPF_GLOBAL without relying on the accidentally seen TO state. |
| 3 | Part I heading | Structural; eight outcomes separately mapped. |
| 4 | O1 gold vintage and one home | Four snake_case artifact families, dated parquet, one addition per day, full available history, no history rewrite, no second write path; DEC-2 and M2/M3. |
| 5 | O2 own bucket and another firm refused | Own-bucket serving/grants, scoped authorization and positive/negative sessions are retained; R1 and R3 must make the storage and request contracts executable. |
| 6 | O3 composite stays with written reason | `global` remains in portal-v2; DEC-7/M7 require aggregation level, minimum firm count and no per-account/per-firm row, with X2 acknowledgement separately owed. |
| 7 | O4 one publisher and data unchanged | M5 reads only MDPF gold, switches last, reconciles the three populations and compares data-bearing leaves; CONTRACTS excludes the daily written-at timestamp. |
| 8 | O5 producers, raw inputs and code homes | M1/M4 census and repoints, all three deployed `/seams` axes, M6 packaging declarations and byte-identical frozen rollback; B1 through assets and B2 exception retained. |
| 9 | O6 dedicated runner and fence | One scope-named principal per firm, only its own platinum write grant, E5 prerequisite and byte-identical Deny before/after the deliberate run. R1 must resolve its destination/grant mapping. |
| 10 | O7 bronze in intake | Source prefix, new home and deliberate receiving-step proof retained; R2 corrects the contradictory builder prerequisite. |
| 11 | O8 retirement and hold | M11 consumes the 45-day standard, named observed-live instrument, reader repoints, prior-cleanup negative controls and confirmed removals; producer read/date-join evidence prevents clearing the hold merely on a 404. |
| 12 | Part II boundary | ADVI bucket/grant ownership and per-firm dependencies, additive host ownership, unchanged existing compute/platinum shape, B2 and demo boundary retained; MDPF_GLOBAL stays distinct. R3 adds the missing caller-transition allocation. |
| 13 | Part III bar | All endpoint outcome bars and deliberate positive/negative evidence remain represented. R1–R3 affect whether the related consuming cells can meet them coherently. |
| 14 | Part IV heading | Structural; twelve findings individually mapped. |
| 15 | IV.1 live trees | M1 remeasures; M2/M3 consume the empty intended home, two live JSON trees and dated backfill. Historical counts are fixtures, not current measurements asserted by this review. |
| 16 | IV.2 definitions/config census | M1 retains the 16 definitions and 50 config sites as a floor, prints its denominator and lists or explicitly excludes discovered readers/writers. A name census is not runtime absence proof. |
| 17 | IV.3 producers across three trees | M1/M4 and PATHS include MDPF producers, the assets Cottonwood scripts and SmartX's composite reader. Repoints preserve the composite's unchanged location. |
| 18 | IV.4 publisher and code artifacts | M5 handles the publisher port; M6 changes the bundle/zip packaging declarations and runtime pull locations, preserving frozen rollback bytes rather than copying objects by hand. |
| 19 | IV.5 path strings | Source-first ratification, snake_case parquet and kebab-case served leaves carried, but the firm-platinum instance conflicts with the consumed builder. R1 required. |
| 20 | IV.6 route-class change | Scoped router, tenant assertion, general-only composite and never-widen sign-off carried; the named existing portal call transition is not allocated. R3 required. |
| 21 | IV.7 X2 basis owed | DEC-7/M7 assign the written basis and ledger citation; Andrew's later acknowledgement remains distinct from writing the document. |
| 22 | IV.8 runner name correction | Scope-derived fence and canonical name replace the withdrawn outside-pattern approach; E5 is a prerequisite and no exemption is added for the run. |
| 23 | IV.9 hold / successor / date-join | DEC-9/M11 require producer evidence at the current read or date-join before repoint/supersession; no deletion of the hold merely because its old key is absent. |
| 24 | IV.10 trigger disagreement | DEC-13 explicitly cuts cells against the live plane and prohibits using the stale map for schedules. Existing conformant schedules remain outside the changes. |
| 25 | IV.11 compute and platinum shape | DEC-1(b)/14 distinguish the existing chain/JSON shape from changed firm-slice homes and the expressly requested additive runner. |
| 26 | IV.12 prior cleanups | M11 consumes their kill lists as negative controls; M2 replaces the producer output rather than treating a kill list as sufficient retirement. |
| 27 | Part V prerequisites | First-correct emitter/no dual write, census first, publisher last, per-firm serving gates, X2 basis, hold evidence, frozen rollback, stale-key disposition and B1/B2 retained. Corrected IV.8 supersedes the stale outside-pattern bullet. R1–R3 make address/route dependencies coherent. |
| 28 | Part VI status | NOT CONSUMED, accepted as historical status; M1 re-reads relevant figures instead of promoting the old clocks into current evidence. |
| 29 | Part VII limits | M1 names its instrument; M5 reconciles 522/492/13; M2 diffs twins; DEC-9/M11 read the date-join; M7 writes the basis; DEC-13 requires live schedules. R3 completes the scoped-route/caller read and transition. No runtime tracing or applied proof is claimed here. |
| 30 | REFS TO CARRY | NOT CONSUMED as work, accepted as a link list. Path ratification, home, runner and MDPF_GLOBAL have explicit dispositions; X2's basis is assigned to M7, not already written or acknowledged. |

## Retained open call and return

DEC-9 correctly retracts the endpoint's overbroad claim about logging coverage. The named trail's read selector does not cover the two assets-bucket trees; enabling the proposed billed read logging is explicitly Andrew's open call. The 45-day window cannot start before the required instrument is observed live and all readers are repointed. Any non-excluded event restarts the window. This review does not authorize logging, backdate evidence or permit retirement without the proof and required confirmation.

Return to CTO: resolve R1–R3 in the brief half and re-offer the exact resulting PRD pin/hash. The ratified-text half remains the CVO's review. No emitter, route, policy, principal, logging selector, object or deployment was changed or exercised here.

Content ACK was sent for 96550. The Codex branch of `org/XXX.md` B.0 has no `ack_messages`/`get_delivery_state` surface; exact-file handling is the equivalent act and no ledger ACK stamp is claimed. Archive follows the committed review, canonical refusal and completion receipt.

Push state: **LOCAL**. `git ls-remote origin refs/heads/CLOUD` measured `56608aadd493d738330e5b9324683019cf5417e3` during review. This seat performed no push.
