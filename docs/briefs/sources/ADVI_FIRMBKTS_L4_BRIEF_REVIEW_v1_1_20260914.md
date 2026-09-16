# ADVI_FIRMBKTS v1.1 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~10:15Z · request 96565 from `1.0.0_SA_CTO`.

**VERDICT: SIGNED, brief half.** R1, R2 and R3 are closed in the revised consuming requirements. All 30 brief entries are accounted for. The code-family conflict is explicitly held on an owned dependency; this accepts that requirement and does not resolve the conflict or authorize code writes. No further brief-half correction is required at this pin.

## Exact inputs

- PRD: `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md@2a9ae97c19ecd305071d690620869ad737854cf1`, v1.1, 397 lines.
- Brief: `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md@2b64208047720051371e2118a44f3c36dc6d3cc8`, 452 lines.
- Brief-half SHA-256: `0b4ef28db943290817f4b634ca89eb39c1135734b8e0fac65649957f4cbefde0`.
- Ratified-text half, identified but not signed as that half here: `c46ed3a59272e222bdfe325fd5c3a501b9c2ae660c2b4afe3decfb8f02b5d68d`.
- Prior complete audit: `docs/briefs/sources/ADVI_FIRMBKTS_L4_BRIEF_REVIEW_v1_0_20260914.md@3454bdc77e8d0dca721abd8551d3cbe98b5a8952`, reviewing v1.0 at `ecac007bf3fddcff1dfb57435ba8428e36485b85`. Its artifact verdict was REFUSED; a concurrent PRD draft prevented a canonical v1.0 refusal stamp, as reported to the CTO.

The complete v1.0→v1.1 diff and the final consuming contracts, decisions, cells, paths, manifest and coverage were read against the pinned full audit. HEAD and worktree PRD text both matched the offered pin. The canonical sign-off library calculated both hashes. The endpoint block is unchanged. The consumed schema, ENFORCE PRD and doctrine are byte-identical between the two PRD pins.

## Correction closure

| Finding | Revised requirement and evidence | Verdict |
|---|---|---|
| R1 — serving grants omit source and scope | CONTRACTS (154) now generates the exact served `{source}/{firm}/platinum/*` prefixes from F2's destinations and consuming projects' declared prefixes, fixing the bucket's own LONG firm in scope. ADVI and MDPF are named examples, not a closed replacement for the mapped source population. Bucket-wide grants are prohibited. Legacy `gold/*` OAC grants are explicitly not copied: files actually served from old gold are mapped to platinum or treated as table faults. DEC-4 (196–205), F4 (313) and the manifest (388) carry the grant and proof obligations. Before the router flip, representative mapped keys must read through the intended CloudFront principal and the page's own route; foreign-firm sessions must fail. | CLOSED |
| R2 — root code home versus mandatory five-segment builder | CONTRACTS (151) separates code from currently constructible gold/platinum/state and explicitly holds any family the builders cannot construct. DEC-2 (177–181) supplies the competing vector: legacy `opal-data-bd/code/gold/<runner>.py` would become either `opal-data-49financial/code/advi/gold/<runner>.py` or the five-segment `key("advi", "49financial", "code", "gold", "<runner>.py")`. It chooses neither; LGIC_NAMING-S7 owns the resolution. Runners keep their legacy code home. DEC-16 (267–273), DEC-17 (282), PATHS (329) and coverage entries 16/18 retain the hold. R16's Lambda-artifact non-application is preserved. | CLOSED as an explicit held dependency |
| R3 — Inflection prerequisite reduced to retirement only | DEC-13 (252–261) now prohibits moves, copies, repoints away from or writes to `opal-data-inf` until both FWD-7/FWD-8 rulings are recorded. It names F8 and Inflection's portions of F5/F6/F10/F11/F12; only the read-only census proceeds. DEC-4 allows Cottonwood before Inflection; DEC-16 repeats the prerequisite; F8 (317), F11 (320) and F13 (322) carry it. B2 may still be ruled to keep the bucket open; Door 6 may receive a successor or retirement with its watcher. Coverage entry 27 now agrees with operative requirements. | CLOSED |

The S7 dependency is independently recorded in `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@acc5f3782b5b3f944d5c78c2bd0d8746bc0aba83`, lines 155–176. It is ARMED / UNDER_INVESTIGATION, names the CTO as disarm owner through the schema's L10 addendum, and explicitly keeps code writes held until the construction is resolved. That record was committed after the offered PRD; it is cited at its own pin, not misrepresented as present in `2a9ae97c19`.

Static prefix vectors for ADVI, MDPF and an IRPT-shaped served key matched `{source}/49financial/platinum/*` and failed when the key's scope was changed to `inflection`. These are checks of the written prefix contract, not an IAM simulation or a live CloudFront test. The deployed proof remains F4/F6's obligation.

## Tenant continuity revision

The additional change in CONTRACTS (156), DEC-3 (185–195) and F6 (315) preserves legitimate aliases and internal staff access. The request's firm resolves through the registry; its bucket is compared with the caller's validated tenant bucket, including the existing staff `?firm=` selection. The destination key is built using the resolved firm, never the raw alias. The response guard still derives its decision independently. F6 requires own-firm, alias and staff positives and a foreign-firm negative through the page's request path.

This agrees with the previously read source at `infra/aws/lambda-edge/shared-advisor-router/index.mjs@40697fe79d5fd4d2a747df455781a1bbb49beca4`, especially 227–248 and 362–395: bucket resolution preserves the staff proxy and `mockadv` alias, while unknown or foreign path firms fail. The review does not treat that source pin as a current deployment measurement.

## Coverage audit — all 30 entries

The brief has **30 headings outside fenced code**: title and Parts I–VII (8), O1–O8 (8), IV.1–IV.13 (13), REFS (1). v1.1 contains exactly entries 1–30 at lines 350–379. Only coverage rows **16, 18 and 22** changed; all consuming content was checked against the prior full audit and the revised requirements.

| # | Brief entry | Final carriage |
|---|---|---|
| 1 | Title / preamble | D8 home, full swap, inherited rulings, never-widen and demo exclusion retained. |
| 2 | Part I heading | Structural; eight outcomes separately accounted for. |
| 3 | O1 | Canonical gold/named-leaf vectors and independent reading exercise; unsupported entity/code families explicitly held. |
| 4 | O2 | 228 keys, deterministic mapping, independent second placement and table-fault treatment; code construction is held for S7 rather than improvised. |
| 5 | O3 | ENFORCE registry/generated views, DEF/config repoints and one-row propagation; history preserved. |
| 6 | O4 | Correct serving prefixes, pre-flip positive/negative proof, independent tenant guard, per-key sign-off, comparison and rollback. R1 closed. |
| 7 | O5 | Live pattern rules, Scheduler API, configuration repoints and notification singleton hazard retained. |
| 8 | O6 | 45 consecutive days, complete read/write instrument, observed-live floor, post-cutover start, event reset and separate deletes retained. Missing write coverage remains an open call. |
| 9 | O7 | Prohibited key/watcher disposition remains Andrew's and precedes Inflection acts. R3 closed. |
| 10 | O8 | Exact B2 exception remains Andrew's; keeping the bucket open is a valid disposition; prerequisite restored. |
| 11 | Part II | D14 registry/builders/fence, D8 repoints, IAMROLES belts and safe-apply/vendor boundaries retained. |
| 12 | Part III | All eight bars carried; corrected serving and dependency requirements support their consuming cells. |
| 13 | Part IV heading | Structural; thirteen findings separately accounted for. |
| 14 | IV.1 | Census denominators/instruments and DEF/config population preserved; historical band never edited. |
| 15 | IV.2 | Live census and attributed-key population re-read; undeclared policies separately dispositioned. |
| 16 | IV.3 | All classes retained, with the body’s additional code class now explicit and held on S7. |
| 17 | IV.4 | Source-first supersession of the old tier-first template recorded; code conflict explicitly isolated for its owner. |
| 18 | IV.5 | Constructible vectors retained; S6 entity and S7 code gaps named and held. R2 closed. |
| 19 | IV.6 | F2 mapping/data twin and independent placement retained; raw bronze, decision rows and held code class distinguished. |
| 20 | IV.7 | Registry-generated pointers and independent guard; canonical resolved scope preserves aliases/staff and rejects foreign firms. |
| 21 | IV.8 | Sentinel/OTP destinations, live schedules, notification singletons, held prices rule and dark FIRMSEP disposition retained. |
| 22 | IV.9 | Source-first serving prefixes, explicit legacy OAC-gold disposition, belt ownership and policy retirement retained. R1 closed. |
| 23 | IV.10 | Door 6/B2 decisions precede Inflection acts; mockadv remains an alias with its home decision owned by Andrew. |
| 24 | IV.11 | E5 scope-derived fence and scoped/exempt existing writers retained; no naming workaround. |
| 25 | IV.12 | Holds enumerated and repointed or closed SUPERSEDED before decommission; deploy ledgers remain history. |
| 26 | IV.13 | ENFORCE owns runtime registry/views; this project owns consumer repoints. |
| 27 | Part V | Registry/builders/fence, logging residuals, tenant guard, raw re-land, never-widen, full quiet-window proof, per-version deletion and both Inflection rulings carried. R1–R3 closed. |
| 28 | Part VI | NOT CONSUMED as work: historical status with superseded clocks. |
| 29 | Part VII | Producer/count/lifecycle/read census, live schedules/targets, template/belts/prior COO rejection reads and missing write coverage retain named obligations. No estimate invented. |
| 30 | REFS | NOT CONSUMED as work: links; outstanding decisions and dependencies retain their owners. |

## Verification and retained boundaries

The full pinned diff, endpoint equality, canonical half hashes, heading count, coverage identifiers, unchanged consumed contracts and static prefix vectors were checked. Review acceptance is at the requirements level; no migration, IAM grant, router deployment, builder execution, quiet window or deletion was exercised.

The sequence check reports stage 2, `HELD,UNMEASURED`, TRACK (`SEQUENCE.yaml@089ba2d431`). The hold cap remains DECOMP: PRD review and decomposition may proceed. ENFORCE PRD admission is MET; its scope-derived fence applied on the template remains the manual gate. S6/S7, the whole-bucket write-logging call, mockadv and both Inflection dispositions remain outstanding on their stated terms. Signing this half clears none of them.

Request 96565 was read and content-ACKed. The Codex exception in `org/XXX.md` B.0 applies: no `ack_messages`/`get_delivery_state` surface exists, so no ledger ACK stamp is claimed. Completion receipt and exact-file archive follow the committed review and guarded canonical signature.

Push state: **LOCAL**. `git ls-remote origin refs/heads/CLOUD` measured `56608aadd493d738330e5b9324683019cf5417e3` during this review. No push or cloud mutation was performed.
