# MDPF_CANON v2.1 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~09:10Z · review request 96553; CTO correction follow-up 96554.

**VERDICT: SIGNED, brief half.** R1, R2 and R3 are closed in the revised consuming requirements. All 30 brief entries remain accounted for. No further brief-half correction is required at this pin. This accepts requirements; it does not declare the migration or its exercises complete.

## Exact inputs

- PRD: `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md@6ab0a19bd4b1f6cd97a189c4bc7e82a095746518`, v2.1, 429 lines.
- Brief: `docs/briefs/d8-mdpf-canon-migration-brief-20260913.md@fd579d3caf21b018bb06254c9ec63481a24f8299`.
- Brief-half SHA-256: `f5b7d07ad26a12532ffe528c320da97616800d5f8a8346c166ea765708c2de70`.
- Ratified-text half, identified but not signed here: `b5caa547cd1557238912a8dd083f8d1a464381e0aa7d99c245208036023b9d60`.
- Prior complete content audit: `docs/briefs/sources/MDPF_CANON_L4_BRIEF_REVIEW_v2_0_20260914.md@4d08ce88b23328439ddde1db1bac9ee6d04f4484`, reviewing PRD v2.0 at `3514843a123a72ddafa86e39f35dd179abd7dd6f`; refusal stamp `61e981a6e382a5f53a48ae07f55a8d6841dbc8ba`.

The complete PRD diff was read against that prior audit. Revised contracts, decisions, cells, paths, manifest and every coverage row were checked at the v2.1 pin. HEAD and worktree PRD text both matched that pin. The canonical sign-off library calculated the hashes above. The consumed `NAMING_SCHEMA.json` and `LGIC_ENFORCE_PRD.md` at v2.1 are unchanged from their previously reviewed contents at the v2.0 pin.

## Correction closure

| Finding | Revised requirement and evidence at v2.1 | Verdict |
|---|---|---|
| R1 — firm-platinum address versus builder | CONTRACTS line 177 now uses `mdpf/{firm}/platinum/{table}/{leaf}.json`: five segments. The exact vector is `key("mdpf", "49financial", "platinum", "aum_metrics", "aum-metrics.json")` → `mdpf/49financial/platinum/aum_metrics/aum-metrics.json`; `address()` uses the same arguments and the registry-derived firm bucket. This uses the schema's admitted `a named leaf` partition form and ENFORCE's documented `object=None` option, without dropping a required argument or adding a bucket argument. M9/M10 (344–345), PATHS (356), the manifest (419) and the route contract carry the mapping. The own-firm `platinum/*` grant contains these keys without widening to another firm. The historical composite path is explicitly retained outside the new-address requirement. | CLOSED |
| R2 — bronze move omitted E3 prerequisite | DEC-15 (303–308) includes M8 among cells waiting on E3; only M1's census and M7's document proceed early. M8 (343) explicitly consumes `key()`/`address()`, requires generated destination keys and waits on E3. Its read-only listing belongs to M1. The arc (321–324) agrees. | CLOSED |
| R3 — existing portal callers lacked a route transition | CONTRACTS (181), DEC-5 (228–248) and M9 (344) choose a tenant-asserting edge compatibility mapping for the existing `/api/general/mdpf/{firm}/...` requests. A firm segment must match the viewer's asserted tenant; cross-firm requests are refused; `global` retains its existing handling. Callers remain unchanged under the portal freeze and are declared read-only in PATHS (362) and manifest (421). Edge/router/CloudFront work is allocated to portal-auth Terraform through the infrastructure lane, live behaviour selection at L5, `safe-apply` and per-key never-widen sign-off. The mapping must be deployed and proven against the current location before the firm-origin flip. Proof uses the page's actual request path: own-firm success, foreign-firm refusal, and preserved composite access. | CLOSED |

The builder vector is checked for consistency with the consumed written contract, not represented as an executed implementation test. Likewise, the compatibility route is an accepted design and proof obligation, not a live authorization result measured by this seat.

## Coverage audit — 30 entries

The pinned brief has **30 headings outside fenced code**: title plus Parts 0–VII (9), O1–O8 (8), IV.1–IV.12 (12), REFS (1). The v2.1 PRD contains exactly entries 1–30 at lines 380–409. Only coverage rows **5, 10, 19 and 20** changed from v2.0. The retained detailed audit is pinned above; the following records the final carriage of every entry.

| # | Brief entry | Final carriage |
|---|---|---|
| 1 | Title / preamble | D8 home, founding rulings, dedicated runner and never-widen boundary retained. |
| 2 | Part 0 | NOT CONSUMED as work: method record; founding obligations retained and MDPF_GLOBAL expressly dispositioned. |
| 3 | Part I heading | Structural; eight outcome entries follow. |
| 4 | O1 | Four artifact families, dated parquet, available history, no rewrite or second write path in DEC-2/M2/M3. |
| 5 | O2 | Own-bucket serving, compatible five-segment destination, tenant assertion and actual-page positive/negative proof in M9. R1/R3 closed. |
| 6 | O3 | Composite stays; M7 writes aggregation level, minimum firm count and non-disclosure basis; acknowledgement remains distinct. |
| 7 | O4 | M5 switches publisher last, reads only MDPF gold, reconciles populations and compares data-bearing leaves. |
| 8 | O5 | M1/M4 census and repoints, deployed three-axis seams, packaging edits and preserved rollback bytes; B1/B2 retained. |
| 9 | O6 | Dedicated scope-named principal, own-firm grant, generated keys, E5 prerequisite and unchanged fence bytes. R1 closed. |
| 10 | O7 | M8 consumes builders and waits on E3 before the move/repoint/run; deliberate receiving-step proof retained. R2 closed. |
| 11 | O8 | Named instrument, observed-live stamp, 45-day window after repoints, confirmed removals and evidence-backed hold update. |
| 12 | Part II | ADVI bucket/grant ownership, host ownership, existing compute/shape boundaries and distinct MDPF_GLOBAL preserved; caller transition allocated. |
| 13 | Part III | All eight outcome bars remain represented; corrected cells now supply coherent address, dependency and request-path contracts. |
| 14 | Part IV heading | Structural; twelve findings separately accounted for. |
| 15 | IV.1 | M1 remeasures; M2/M3 consume the empty intended home, two JSON trees and historical backfill. Old counts remain fixtures. |
| 16 | IV.2 | M1 retains 16 definitions/50 config sites as a floor, prints denominator, and lists or excludes each discovery. |
| 17 | IV.3 | M1/M4 cover MDPF, assets Cottonwood scripts and the SmartX composite reader. |
| 18 | IV.4 | M5 publisher port; M6 bundle/zip packaging declarations and code pulls, with frozen rollback unchanged. |
| 19 | IV.5 | Ratified source-first grammar, snake_case table, named-leaf partition and exact builder vector; historical composite explicitly retained. R1 closed. |
| 20 | IV.6 | Existing callers and URLs named; tenant-asserting compatibility mapping, infrastructure ownership and route readiness before origin flip. R3 closed. |
| 21 | IV.7 | DEC-7/M7 assign the X2 basis and ledger citation without treating it as already granted. |
| 22 | IV.8 | Canonical scope-derived runner name and E5 fence replace the withdrawn outside-pattern approach; no run-specific exemption. |
| 23 | IV.9 | Producer read/date-join evidence controls hold repoint or supersession; a 404 alone cannot clear it. |
| 24 | IV.10 | DEC-13 requires live-plane schedule reads and excludes changing the conformant chain. |
| 25 | IV.11 | Existing compute and JSON shape preserved; changed homes and additive runner are expressly distinguished. |
| 26 | IV.12 | Prior kill lists are M11 negative controls; M2 replaces producer output rather than relying on another kill list. |
| 27 | Part V | No dual write, census first, publisher last, builder/serving/route gates, X2 basis, hold evidence, rollback, stale key and B1/B2 retained. |
| 28 | Part VI | NOT CONSUMED: historical status; relevant figures are re-read rather than asserted current. |
| 29 | Part VII | Named census instrument, population reconciliation, twin diff, date-join read, basis and live routing/schedule reads remain assigned evidence obligations. |
| 30 | REFS | NOT CONSUMED as work: link list; dependencies/rulings have explicit dispositions, with X2's basis assigned rather than already completed. |

## Verification and retained boundaries

The endpoint block is text-identical to v2.0. Only DEC-5 and DEC-15 changed among the numbered decisions; only M8/M9/M10 changed among acceptance cells. The schema and ENFORCE contracts are unchanged. This preserves the previously audited rulings, historical evidence and claim limits while closing the three identified defects.

The sequence check reported stage 2, LGIC_ENFORCE admission prerequisite MET, no project flags and TRACK enforcement (`SEQUENCE.yaml@089ba2d431`). At review start the PRD remained WITHHELD with the prior brief signature STALE and ratified-text MISSING. This artifact signs only the CRO brief half; overall admission must be measured after the canonical stamp and the CVO's separate act.

DEC-9's proposed billed read logging on the two assets-bucket trees remains Andrew's open call. The retirement window cannot start without the required observed-live instrument and completed reader repoints; non-excluded events restart it. No logging, window completion, hold clearance, deletion, routing deployment, builder execution or migration is claimed or authorized by this review.

Both exact notices, 96553 and 96554, were read and content-ACKed. The Codex exception in `org/XXX.md` B.0 remains applicable: no `ack_messages`/`get_delivery_state` surface exists and no ledger ACK stamp is claimed. Archive follows the committed review, canonical signature and completion receipt.

Push state for this review: **LOCAL**. `git ls-remote origin refs/heads/CLOUD` measured `56608aadd493d738330e5b9324683019cf5417e3` during review. This seat performed no push or cloud mutation.
