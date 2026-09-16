# MDPF_CANON v2.2 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~09:58Z · request 96562 from `1.0.0_SA_CTO`.

**VERDICT: REFUSED, brief half, for R4 below.** The v2.2 route correction is accepted: it preserves registry aliases and internal staff selection while refusing another firm's session. The complete coverage recheck exposed a retained code-packaging versus builder contradiction that I missed when signing v2.1. It is not a regression introduced by this route revision. Prior findings R1–R3 remain closed.

## Exact inputs

- PRD: `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md@ef21e346608974de3611bd69ee36a1a110a6b355`, v2.2, 435 lines.
- Brief: `docs/briefs/d8-mdpf-canon-migration-brief-20260913.md@fd579d3caf21b018bb06254c9ec63481a24f8299`, 337 lines.
- Brief-half SHA-256: `8a3ec329c64f91791cac44a01904966a3e53ee651d894e462165e93b671a6ade`.
- Ratified-text half, identified but not signed as that half here: `d5177552975dceaaca733a6e8d5a790765891b9fcf7b6ef5e77ccece7b5e1fac`.
- Prior audit: `docs/briefs/sources/MDPF_CANON_L4_BRIEF_REVIEW_v2_1_20260914.md@f44f70c06949da7cc37b27a68756d528143ed40c`, reviewing PRD `6ab0a19bd4b1f6cd97a189c4bc7e82a095746518`. Its historical brief SIGNED stamp is `6f600be875c70a1b2ebc6cd9bf173f73c42c997a`.
- The full v2.0 content audit remains `docs/briefs/sources/MDPF_CANON_L4_BRIEF_REVIEW_v2_0_20260914.md@4d08ce88b23328439ddde1db1bac9ee6d04f4484`.

The full v2.1→v2.2 PRD diff, all current contracts, decisions, cells, paths, manifest and all 30 coverage entries were read against those prior audits. Relevant brief content was re-read at its exact pin. The endpoint and the entire coverage/manifest tail are text-identical to v2.1. At review, HEAD and worktree both matched the offered pin. The canonical library calculated both half hashes above.

## Accepted route revision

CONTRACTS line 181 and DEC-5 (228–254) now resolve the requested firm and the authenticated tenant through the registry, including aliases. They retain two allowed session classes: the same resolved firm, and validated internal Opal staff (`opal-capital`). For staff on the frozen MDPF caller, the path's firm is the selection; another firm's session remains refused. `global` retains its existing handling, and the old general URL does not retain general authorization for firm data.

M9 (350) adds an actual-page staff-selection positive alongside the existing own-firm positive, foreign-firm negative and global-continuity proof. The mapping must still be deployed and proven against the existing location before the origin flips, under the infrastructure lane's `safe-apply` and per-key never-widen sign-off. No portal source edit is added.

Supporting reads:

- `infra/aws/lambda-edge/shared-advisor-router/index.mjs@40697fe79d5fd4d2a747df455781a1bbb49beca4`, lines 227–248 and 362–395: existing staff selection is separate from partner resolution; the tenant check compares resolved buckets and rejects unknown path firms. The comments expressly preserve the `mockadv` alias and staff proxy. This proves the cited source mechanism, not current deployment parity.
- `portal/src/pages/ModelPortfolios.tsx`, local snapshot SHA-256 `a63983a7e458ee8b30fe981ecec57611be67edf8c385757a07a1650361368657`, lines 351–360: the S5 record preserves the internal selector/global default while external users resolve their own firm. This is a local supporting snapshot, not represented as a file pinned in the root CLOUD commit.
- `org/projects/MDPF_SCOPED.json@88a659f8c8ca12aa1cf82fab440eff463b364c46` records the S5 external-firm scoping and Andrew's completed production visual check. The previously audited `aum.ts` / `portal-proxy.ts` callers use the firm in the path; v2.2 declares the staff compatibility handling rather than requiring a new query parameter from frozen callers.

These changes preserve the substance of brief O2 and IV.6. They correct the bare segment-equality requirement in v2.1. This review accepts the requirements; it does not claim a live authorization exercise.

## R4 — Code packaging has no construction contract consistent with its required destination

**Brief content:** O5 (68–73) puts the accrual bridge's bundle in `opal-data-mdpf/code/` and moves the gold Lambda artifact out of the retiring tree while preserving frozen rollback objects. IV.4 (177–186) identifies the two deployment artifacts and requires packaging-declaration edits, not object copies. IV.5 line 192 gives the code example `opal-data-mdpf/code/mdpf/gold/...`.

**Consuming contradiction:** CONTRACTS line 177 requires **every NEW address** to come from `LGIC_ENFORCE`'s `key()` and `address()`, with only the unmoved historical global slice excepted. DEC-15 (309–314) expressly includes M6 among cells taking new addresses from those builders. But M6 (347) and PATHS (360) specify new packaging under `s3://opal-data-mdpf/code/` for the accrual bundle and gold Lambda zip. The manifest (423) also carries code objects. The consumed builder returns exactly `{source}/{scope}/{tier}/{table}/{partition}` with source `mdpf` for these instances; it cannot return the required root-code prefix under that contract.

**Authority check:** at the v2.2 PRD commit, the consumed `LGIC_ENFORCE_PRD.md` contract at lines 151–152 defines the five-argument key and registry-derived address, with no alternate code constructor. `infra/logic/02_DOCTRINE.md` R1 (103–105) excepts `code/` roots; R16 (275–283) distinguishes runner code from Lambda deployment artifacts, whose key grammar is still graded. `org/standards/NAMING_SCHEMA.json` supplies the five-segment grammar. These distinctions need an explicit per-artifact disposition; neither a universal root-code exception nor a universal new tier path may be silently invented by the mover.

**Required correction:** reconcile CONTRACTS, DEC-15, M6, PATHS and the manifest for the accrual bundle and Lambda zip separately. Supply concrete destination/construction vectors and their authority, preserving packaging-declaration ownership and frozen rollback bytes. If the schema/builder owner must resolve a gap, name that dependency and hold the affected code writes until the construction contract exists. Do not let packaging bypass the mandatory builder implicitly, and do not erase the retained R16 code-root exception by forcing every artifact into a new tier path.

This is a requirements conflict already present at v2.1. My earlier review accepted the code-home carriage without checking it against the universal new-address clause and M6's builder dependency. That conclusion is corrected here. The approved platinum vector, M8 builder prerequisite and caller transition from prior R1–R3 are unaffected.

## Coverage audit — all 30 entries

The pinned brief has **30 headings outside fenced code**: title and Parts 0–VII (9), O1–O8 (8), IV.1–IV.12 (12), REFS (1). v2.2 contains exactly entries 1–30 at lines 386–415. Their text is unchanged from v2.1; their consuming requirements were rechecked, including changed DEC-5/M9 and the newly identified M6 conflict.

| # | Brief entry | Final carriage at this pin |
|---|---|---|
| 1 | Title / preamble | D8, inherited rulings, dedicated runner and never-widen boundary retained. |
| 2 | Part 0 | NOT CONSUMED as work: method record; MDPF_GLOBAL explicitly dispositioned separately. |
| 3 | Part I heading | Structural; eight outcomes separately accounted for. |
| 4 | O1 | Four dated parquet artifact families, full available history and no rewrite/second write path in DEC-2/M2/M3. |
| 5 | O2 | Compatible five-segment firm-platinum vector; revised resolved-tenant/alias/staff handling and actual-page proof in DEC-5/M9. Route revision accepted. |
| 6 | O3 | Composite retained; M7 writes aggregation level, minimum firm count and non-disclosure basis; acknowledgement remains distinct. |
| 7 | O4 | M5 is publisher last, MDPF-only reads, population reconciliation and data-bearing comparison. |
| 8 | O5 | M1/M4 census, deployed three-axis seams and B1/B2 retained. M6 code-home construction needs R4. |
| 9 | O6 | Scope-named dedicated principal, full own-firm `mdpf/{firm}/platinum/*` write prefix and unchanged E5 fence bytes. |
| 10 | O7 | M8 consumes and waits on builders; deliberate receiving-step proof; prior R2 remains closed. |
| 11 | O8 | Named instrument, observed-live floor, 45 days after reader repoints, hold evidence and separate confirmed removals retained. |
| 12 | Part II | ADVI bucket/grant ownership, new host ownership, frozen callers and existing compute/shape boundaries preserved. R4 affects packaging implementation. |
| 13 | Part III | Eight qualitative bars carried; route revision preserves legitimate users and denies foreign firms. R4 prevents full code-home consistency. |
| 14 | Part IV heading | Structural; twelve findings separately accounted for. |
| 15 | IV.1 | M1 remeasures; M2/M3 use empty intended home, two JSON trees and available history as fixtures. |
| 16 | IV.2 | 16 definitions/50 configuration sites are the floor; every discovery listed or excluded with denominator and instrument. |
| 17 | IV.3 | M1/M4 cover MDPF, assets Cottonwood scripts and SmartX composite reader across pipeline trees. |
| 18 | IV.4 | M5 publisher port retained; M6 declares both packaging edits and rollback preservation but requires R4. |
| 19 | IV.5 | Gold/bronze/platinum strings and historical global exception retained; code-family construction needs R4. |
| 20 | IV.6 | Existing callers/URLs retained; tenant-asserting edge mapping now includes resolved aliases and staff selection, with route readiness before flip. |
| 21 | IV.7 | DEC-7/M7 assign X2 basis and ledger citation without claiming acknowledgement granted. |
| 22 | IV.8 | Canonical scope-derived role and E5 fence retained; no run-specific exemption. |
| 23 | IV.9 | Producer read/date-join evidence controls hold disposition; 404 alone never clears it. |
| 24 | IV.10 | Live schedules required; conformant schedule chain unchanged. |
| 25 | IV.11 | Existing compute and JSON shape retained; added runner and moved firm homes explicitly distinguished. |
| 26 | IV.12 | Prior kill lists are negative controls; producer output must change rather than repeat a cleanup-only act. |
| 27 | Part V | No dual write, census first, publisher last, route/serving/fence gates, basis, hold evidence, rollback and stale key retained. R4 reconciles the code-family builder obligation. |
| 28 | Part VI | NOT CONSUMED: historical status; figures are re-read. |
| 29 | Part VII | Census instrument, populations, twin diff, date-join evidence, basis, live route and schedules remain assigned obligations. |
| 30 | REFS | NOT CONSUMED as work: links; dependencies/rulings dispositioned, with the newly exposed code construction gap now R4. |

## Verification and boundaries

The complete diff changes only the version, scoped-route contract, DEC-5 and M9. The endpoint, coverage and manifest tail are unchanged. Canonical hashes, exact pin equality, the 30-heading denominator and entries 1–30 were checked. This is document and source-contract validation, not a live route test or executed builder test.

`sequence-check.py --project MDPF_CANON` reported stage 2, no project flags, LGIC_ENFORCE admission prerequisite MET and TRACK (`SEQUENCE.yaml@089ba2d431`). At review start v2.2 was WITHHELD with both prior signatures STALE. A new canonical verdict must bind the exact offered half; a concurrent revision must not inherit this review automatically.

ADVI's per-firm serving readiness and the E5 fence remain dependencies, not facts supplied by this review. DEC-9's scoped logging call remains open; no quiet window, hold clearance, removal, deployment or security change is claimed. The 45-day proof still requires the complete reader/writer claim in M11, and cannot be inferred from mere instrument presence.

Request 96562 was read and content-ACKed. The Codex exception in `org/XXX.md` B.0 applies: no `ack_messages`/`get_delivery_state` surface exists, so no ledger ACK stamp is claimed. Completion receipt and archive follow the committed review and guarded canonical-refusal result.

Push state: **LOCAL**. The latest origin/CLOUD measurement in this active turn was `56608aadd493d738330e5b9324683019cf5417e3`. No push or cloud mutation was performed.
