# ADVI_FIRMBKTS v1.0 — L4-R brief review

Author: `4.0.0_SA_CRO` · UTC: 2026-09-14 ~09:49Z · review request 96559 from `1.0.0_SA_CTO`.

**VERDICT: REFUSED, brief half.** The 30-entry denominator is correct, and all entries were reviewed for content. Three consuming requirements need correction: the serving grants omit the new keys' leading segments; the code destination conflicts with the blanket builder contract; and the claimed Inflection prerequisite is weaker in the operative cutover cell than in the brief. These are requirements defects, not claims about live failures.

## Exact inputs

- PRD: `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md@ecac007bf3fddcff1dfb57435ba8428e36485b85`, v1.0, 379 lines.
- Brief: `docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md@2b64208047720051371e2118a44f3c36dc6d3cc8`, 452 lines.
- Brief-half SHA-256: `61c59d8e870496b0718dae8ac7947deaed04b0760a3e84fd0524c7baeffa17cb`.
- Ratified-text half, identified but not reviewed or signed as that half here: `d4258a7d01a36218cbd0a93fbcfe8fb82529b0c6de36c328bc3a67b09a5ebfa9`.
- Supplemental contracts read at the PRD commit: `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md` lines 150–155; `org/standards/NAMING_SCHEMA.json`; `infra/logic/02_DOCTRINE.md` R1 and R16; and the carried endpoint, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D8_LEGACY_FIRM_BUCKETS_MIGRATION_20260913.md`, including its subsequent ruling stamps and proof-gap notes.

The entire pinned brief and PRD were read. At the content audit, HEAD and worktree PRD text both matched the offered pin. The canonical sign-off library calculated both hashes. Line references below are to these exact inputs, not a moving worktree.

## Required corrections

### R1 — Serving-grant paths do not contain the new served keys

**Brief obligation:** O4 (56–62), IV.5 (197–227), IV.9 (280–287), and Part V (347–358) jointly require source-first destinations, functioning serving grants before cutover, and tenant-grain protection. IV.9's older `platinum/**` shorthand must be reconciled with the ruled leading source and scope segments when the new grant is specified.

**Consuming defect:** CONTRACTS line 154 requires grants on `platinum/**`; F4 (295) and SURFACE MANIFEST (370) repeat that path. But line 151's exact served key is `advi/49financial/platinum/firm/header_metrics.json`, and DEC-6/F6 (203–205, 297) rewrite to `advi/{firm}/platinum/...`. A resource pattern rooted at `platinum/` does not include an object rooted at `advi/`. The same contract names MDPF and IRPT as consumers, whose source segments differ again. Completing F4 literally would not establish the serving access that F7–F9 depend on.

**Correction:** specify the full source-first resource prefixes for the mapped served families, with the bucket's own LONG firm fixed in the scope slot, and carry them through CONTRACTS, F4, paths and the manifest. Enumerate or derive the source families from the mapping/registry; do not repair this with an unrestricted bucket-wide grant. Require a positive read of representative mapped keys through the intended CloudFront access principal and the actual page route, plus foreign-firm refusal, before the router flip. Preserve the separate role-belt and never-widen requirements. If a legacy OAC gold path remains, name its retained or repointed disposition from IV.9 as well.

**Static check:** `platinum/*` fails to match the documented `advi/49financial/platinum/firm/header_metrics.json` and `mdpf/49financial/platinum/aum_metrics/aum-metrics.json` strings. This is a path-contract check, not an IAM simulation or live request.

### R2 — The code-home exception and the mandatory builder cannot both be followed

**Brief obligation:** IV.3's code class (177), IV.5's code example (217), and IV.6's code row (240) preserve a code home under `code/{source}/gold/`. The consumed doctrine expressly lists `code/` prefixes as a non-application of R1 at lines 103–105, and R16 at 275–283 distinguishes runner code homes from Lambda deployment artifacts.

**Consuming defect:** DEC-2 (177) retains `code/{source}/gold/`, but CONTRACTS (151) includes `code` among the tiers of its five-segment string and requires **every new address** to come from `key()`/`address()`. DEC-4 (189), DEC-16 (252) and PATHS (311) carry that blanket requirement into the moves. The consumed ENFORCE builder contract (152) returns exactly `{source}/{scope}/{tier}/{table}/{partition}` and derives the bucket; it cannot return the stated root-code destination with the same arguments. The PRD explicitly raises the entity-keyed family to LGIC_NAMING-S6, but gives no corresponding disposition for this code-family conflict.

**Correction:** explicitly reconcile the R16 code-home exception with the builder requirement, including a concrete source-to-destination vector and its authoritative construction contract. Carry the chosen treatment into F2, the affected move cells, PATHS and the coverage entries. If the schema/builder owner must settle it, name that dependency and hold code-family writes until it is resolved. Do not silently force code into a five-segment tier path contrary to the retained exception, or let a mover hand-spell a path contrary to the blanket contract. Preserve R16's non-application to Lambda artifacts.

### R3 — Inflection's precondition is claimed in coverage but not imposed on its cutover

**Brief obligation:** Part V line 362 says O7 and O8 each have a ruling **before `opal-data-inf` is touched**. O7/O8 and IV.10 identify the prohibited completion key and the standing B2 credential exception. They are decisions, not ordinary moves.

**Consuming defect:** coverage entry 27 (358) claims `O7 and O8 before opal-data-inf (DEC-13)`. DEC-13 (240–245) instead gates only retirement. F8 (299) allows the Inflection cutover with the two keys left in place until Andrew rules; DEC-16 (251–256) does not restore the broader prerequisite. Excluding those two objects from the move protects the objects, but does not consume the brief's stated prerequisite for touching the bucket. No cited supersession of that prerequisite appears in this PRD.

**Correction:** make both recorded dispositions a prerequisite of F8 and any Inflection-affecting repoints, or explicitly disposition the broader brief prerequisite with the authority for narrowing it. Align DEC-13, DEC-16, F8/F13 and coverage entry 27. Preserve the valid B2 outcome in which the bucket stays open for the credential, and the Door 6 outcome in which a successor or retirement is ruled. Neither decision is made by this review.

## Coverage audit — all 30 entries

The pinned brief has **30 headings outside fenced code**: title and Parts I–VII (8), O1–O8 (8), IV.1–IV.13 (13), and REFS (1). PRD lines 332–361 contain exactly entries 1–30 with no missing or duplicate identifier. The IV.3 heading says five classes, but its body includes the sixth, code; F1/F2 must count that body population. This heading-label issue is not a separate refusal.

| # | Brief entry | Content carriage and result |
|---|---|---|
| 1 | Title / preamble | D8 home, full swap, inherited rulings and L5–L7 never-widen boundary carried. Demo remains excluded. |
| 2 | Part I heading | Structural; eight outcomes separately reviewed. |
| 3 | O1 | Five-segment key vectors and independent reading exercise in DEC-1/F3; entity-keyed gap explicitly waits on S6. Code-family conflict is R2. |
| 4 | O2 | 228 attributed keys, one mapping, independent second placement and unplaceable-as-table-fault in DEC-2/F2. R2 prevents a coherent code row today. |
| 5 | O3 | Registry and generated views consumed from ENFORCE; DEF/config carriers repointed, history left intact; F5 requires one-row propagation. |
| 6 | O4 | Per-key never-widen sign-off, named rollback, data-bearing before/after comparison and untouched old copy in DEC-3/4 and F6–F9. Serving prerequisite needs R1. |
| 7 | O5 | Pattern versus scheduled triggers distinguished; live owner reads, Scheduler API and notification singleton hazard retained in DEC-7/11 and F10. |
| 8 | O6 | 45 consecutive days, named READ/WRITE instrument, observed-live floor, post-cutover start, probe exclusion, reset on other events and separate deletes retained. DEC-12 honestly exposes missing write coverage. |
| 9 | O7 | Prohibited key and watcher named; successor-or-retirement decision in DEC-13/F13. Its Inflection timing needs R3. |
| 10 | O8 | Exact B2 credential and standing exception retained; decision remains Andrew's. Its Inflection timing needs R3. |
| 11 | Part II boundary | D14 owns registry/builders/fence; D8 owns repoints and cutovers; IAMROLES owns belts; safe-apply, vendor per-use word and demo exclusions retained. |
| 12 | Part III qualitative bar | Endpoint carries all eight bars, including deliberate serving comparison and independent placement; R1–R3 affect the mechanisms supporting them. |
| 13 | Part IV heading | Structural; thirteen findings separately reviewed. |
| 14 | IV.1 repo census | F1 prints sets, denominators and instruments; F5 consumes the DEF/config bands; DEC-10 preserves the historical band. Counts are inputs to remeasurement. |
| 15 | IV.2 live census | F1 re-reads the live population and attributed keys; undeclared policies have their own disposition in DEC-8. |
| 16 | IV.3 key classes | Served, analytical, state, ingest, retire and code families carried through DEC-2/F1/F2. Code construction needs R2. |
| 17 | IV.4 competing grammars | DEC-1 records source-first supersession of the old tier-first template. The retained code exception needs R2. |
| 18 | IV.5 canonical strings | Exact gold and named-leaf platinum vectors; entity-keyed family explicitly held for S6; source-first grants and code treatment need R1/R2. |
| 19 | IV.6 mapping table | DEC-2 consumes the table as the rule; F2 produces its full data twin and independent placement; raw bronze and separate decision rows preserved. R2/R3 affect specific rows. |
| 20 | IV.7 portal pointers | Registry-derived router/guard/IRPT maps, independent guard derivation, bucket-plus-scope assertion and actual-page foreign-firm negative in F6. R1 remains a serving dependency. |
| 21 | IV.8 triggers | Completion sentinels follow assets, OTP follows state, schedules retain triggers while configuration repoints, singleton hazard preserved; held prices rule never re-enabled. Dark FIRMSEP expressly excluded as evidence; subsequent cot ruling carried. |
| 22 | IV.9 policies / grants | Legacy policy retirement, belt ownership and existing writer scope/exemption retained. Full destination serving prefixes need R1. |
| 23 | IV.10 embedded rulings / mockadv | Door 6, B2 and mockadv decision ownership retained; mockadv is an alias rather than a new scope. Inflection gate needs R3. |
| 24 | IV.11 fence / runner | E5 scope-derived fence is consumed rather than evaded by a name; existing writers must be scoped or exempt before landing. Sequence gate retained. |
| 25 | IV.12 records / holds | F1 enumerates; DEC-15/F12 require repoint or SUPERSEDED closure before decommission. Deploy ledgers remain history. |
| 26 | IV.13 identity spine | Superseded local-runtime ownership resolved to ENFORCE registry and generated views; this project repoints consumers. |
| 27 | Part V preconditions | Registry, builders, fence, independent guard, never-widen, raw re-land, instrument coverage, separate deletes and per-firm acts carried. New-bucket logging includes ordered selector/probe residuals. Grants/code/Inflection gate need R1/R2/R3. |
| 28 | Part VI status | NOT CONSUMED as work: historical clocks explicitly superseded; no live deployment assertion accepted from the brief's old snapshot. |
| 29 | Part VII proof gaps | Coverage expressly assigns producer tracing/counts/readers/lifecycles to F1, live schedules to DEC-11, live targets to F10, template read to F4, belts to DEC-8 and prior COO rejection read to F6. Missing write coverage remains explicit in DEC-12. No effort estimate invented. |
| 30 | REFS | NOT CONSUMED as work: link list; waiting items have named decisions/dependencies. R2/R3 prevent treating all relevant dependencies as fully reconciled. |

## Verification and boundaries

`sequence-check.py --project ADVI_FIRMBKTS` reported stage 2, `HELD,UNMEASURED`, TRACK, against `SEQUENCE.yaml@089ba2d431`. Its hold cap is DECOMP: PRD review and decomposition may proceed. LGIC_ENFORCE PRD admission is MET; applying its scope-derived fence on the firm-bucket template remains the manual gate. This review does not pass that execution gate.

The full pinned inputs, heading denominator, coverage identifiers and canonical half hashes were checked. Static prefix matching demonstrated R1's literal mismatch. R2 was checked against the consumed ENFORCE API and doctrine exception, and R3 against the exact brief prerequisite and operative PRD clauses. No builder implementation, live IAM policy, serving route, trigger, migration or retirement was exercised.

**Concurrent revision detected before commit (~09:51Z):** HEAD still held the offered v1.0 PRD, but the worktree had an uncommitted v1.1 revision to the tenant assertion, DEC-3 and F6. Its brief half measured `1a06a1664c502e611d291a2c320de0a3628d845d815f8facd83b9e06581ee670`. The equality guard stopped before mutation. This artifact remains the review of v1.0; the three cited requirements were unchanged in the observed draft. The findings and drift were sent to the CTO. A canonical refusal must use the offered v1.0 half hash and may not be forced onto the draft or a replacement pin; its actual result will be reported separately.

DEC-12's billed whole-bucket write logging remains an open call, and the 45-day proof cannot be claimed from a read-only instrument. LGIC_NAMING-S6, the fence application, mockadv and both Inflection dispositions retain their stated ownership. The review changes no application or infrastructure file and authorizes no deletion, vendor call or security change.

The exact request 96559 was read and content-ACKed. The Codex exception in `org/XXX.md` B.0 applies: no `ack_messages`/`get_delivery_state` surface exists and no ledger ACK stamp is claimed. Archive follows this committed review, the guarded canonical-refusal attempt and a completion receipt that identifies whether the stamp succeeded or was prevented by the revision.

Push state: **LOCAL**. `git ls-remote origin refs/heads/CLOUD` measured `56608aadd493d738330e5b9324683019cf5417e3` during review. This seat performed no push or cloud mutation.
