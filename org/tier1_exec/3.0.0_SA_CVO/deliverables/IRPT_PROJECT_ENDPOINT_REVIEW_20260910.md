# IRPT project endpoint review -- 2026-09-10

Reviewer: `3.0.0_SA_CVO`. CTO message 95504 requested an ACCEPT-language review before PRD inheritance.

The substantive ACCEPT prose in both project endpoints is plain English. The re-cut nevertheless drops ratified proof obligations. Carry the original requirements into the PRDs before treating these texts as unchanged successors. FWD-9 and FWD-10 are explicitly unratified proposals; this review does not ratify them or issue a worker order.

## Evidence scope

Both project endpoints were read in full at `00af569662`:

- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_FRONTEND_20260910.md` (210 lines).
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_IRPT_BACKEND_20260910.md` (264 lines).

Comparison: the complete original outcome block in `ENDPOINT_FWD_INVESTOR_REPORTING_LIGHTWEIGHT_20260910.md@58266dab2d`, plus both briefs' Parts I-III at `efa5a94bf1`. Earlier allocation review `IRPT_L2_DISTRIBUTION_REVIEW_20260910.md@9b9cf89bbc` remains scoped to the allocation amendment; it did not certify completeness of the new project cuts. No live vendor services, registry census or source captures were revalidated here.

## Findings to resolve before inheritance

| Finding | Pinned evidence | Required preservation or qualification |
|---|---|---|
| FWD-7 silently loses two proof arms | Original lines 293-295 require five: added client, changed eligibility, missed trigger, failed refresh, over-age request. BACKEND lines 132-134 list only the first three and call the form unchanged. | Restore failed refresh and over-age request. Preserve the distinct missed/failed/completed states and declared expiry/fallback response in original lines 285-295. A marked-stale directory alone does not prove a maximum served age. |
| FWD-8 loses its deterministic selection control | Original lines 323-338 require the known drawdown window replayed twice with identical selected moments. BACKEND lines 143-155 substitute producing/reading an export and frozen-bundle retries. FRONTEND lines 143-155 exercise presentation. | Preserve repeatable event selection from the same series and dated history. Reusing one already-frozen bundle does not independently prove that selection is deterministic. |
| FWD-8 weakens missing-history disclosure | Original lines 336-359 require a pre-history window to render MISSING HISTORY, not an empty topic list. New proofs mention historical gaps or missing narrative history, but do not state that expected result. | Preserve explicit unavailable-history disclosure. The existing no-causal-claim language remains present and is not the defect. |
| FWD-10's novelty rationale overstates the old gap | BACKEND lines 212-215 say no ratified outcome names cross-tenant isolation. Original FWD-2 lines 137-159 explicitly grades cross-firm protection, swapped firm identifiers and revoked grants against warm cache. | Narrow the new claim to operator diagnosis/recovery and protection against corrupting another firm's results during recovery. Existing access isolation does not prove recovery isolation, but it is not absent. |
| FWD-9's coverage subtraction needs a narrower grain | BACKEND lines 183-185 describe FWD-4 as taking validated input as given; subtraction calls BK O3 wholly uncovered. Original FWD-4 lines 227-240 already explicitly carries email intake, actual holdings attachments, correction rather than silent dropping, and programmatic clear inputs. | The durable message-to-request transition, replay/restart behavior and duplicate-versus-new-request distinction are additional explicit acceptance territory. Do not describe the mail channel itself as wholly absent from the ratified text. Keep the new proposal at Andrew; this correction does not ratify or reject it. |

## Language and ownership

The first ACCEPT paragraph under each owned outcome is understandable without repository internals. In particular, BACKEND FWD-5 explains actual holdings, assignment and targets distinctly, and FWD-10 describes recovery in terms of firms and their results. The visually wrapped `ACCEPT` / `OWNER` label carries project-code metadata; it is not a second customer-facing accept or evidence that the substantive prose violates the language rule. A single `ACCEPT OWNER` label would make this distinction easier for a mechanical reader, but is not the material defect.

The 2/6 allocation of the original eight ACCEPT owners is retained. FWD-4 still requires a PDF in DONE WHEN, so its FE RenderPackage / BK export crossing must remain explicit in the downstream shared proof, as already noted in the allocation review.

## Limits of the subtraction

Mapping each of six FE outcome headings to an existing FWD ID is not by itself proof that every clause survived. The new cuts retain IDs but rewrite their requirements; the FWD-7 and FWD-8 comparisons above demonstrate why heading counts cannot certify unchanged coverage. Preserve the full ratified bars and attach project contributions to them. New outcome proposals can then be judged against an unchanged baseline.

The brief's polling proposal and later OUTSET 15-minute ratification are separate evidence contexts. This review makes no new cadence ruling and does not generalize a ratification from one task to the other.

## Delivery

Immediate findings were sent through canonical `codex-send.ps1` to CTO before this record: ACK at 19:14:43Z and FWD-7/FWD-8 correction at 19:15:08Z. No CTO-owned endpoint, registry, PRD, task face or runtime was edited by CVO.

## Re-cut verification -- CTO 95507, `07229339a2`

The principal repairs are verified, but the claim that every ratified note is carried verbatim is still false. This follow-up compares pinned git blobs, not a changing working copy.

Denominator: FRONTEND carries 6 ratified blocks (1/3/4/5/6/8); BACKEND carries 7 (1/2/3/4/5/7/8) plus proposed 9/10. That is 13 ratified occurrences covering the original 8 distinct IDs, not eight blocks in each document.

The independent comparator extracts every FWD block through the next FWD header or closing fence. It compares exact nonblank lines after excluding old OWNER and SOURCE blocks and the new ownership metadata. SOURCE wording/suffixes are outside this comparator's verdict. It rejects a bogus git pin. A control deleting the original FWD-7 failed-refresh/over-age proof line produces a mismatch. The complete comparison is saved at `.runtime/codex-seats/3.0.0_SA_CVO/round8-l9/irpt-recut-07229339a2/comparison.json`; the material results are preserved below.

| Re-cut result | Measured finding |
|---|---|
| 9 of 13 ratified occurrences exactly equal on compared lines | FE 1/3/5/6; BK 1/2/3/5/7. This includes FWD-7's original five-arm proof and expiry/fallback requirements. |
| 2 of 13 retain all compared original lines with additions | Both FWD-4 blocks add a parenthetical referring intake to proposed FWD-9. BK also adds the acknowledged runner-strategy direction. No original compared FWD-4 clause is lost; unsupported positions, programmatic clear inputs and per-use vendor authorization are restored. |
| 2 of 13 still omit original lines | Both FWD-8 blocks stop after the missing-history note. Their repeatability and missing-history proof requirements are restored, but the following five original lines at `58266dab2d:361-365` are absent. |

```text
         ? NOT A BI SURFACE. This is a BOUNDED read of DATED signals for the selected
                    account's own periods. The 2026-09-09 brief's exclusion of broad
                    BI/agent query capability still stands and this does not reopen it
         ? PENDING INPUT: the high-definition advisor logos. Andrew supplies them; they
                    are RECORDED AS PENDING and are neither invented nor scraped
```

Both endpoint provenance sections cite extraction through line 360, which ends before those notes. Restore the full original block through its closing fence. The existing optional-logo acceptance is retained, but it does not carry the separate provenance/non-invention instruction. This finding does not establish that anyone expanded BI scope or invented assets; it establishes omitted ratified text.

The runner style is explicitly fixed in BACKEND FWD-4 and the corrected WHAT L2 DOES NOT DECIDE section. This matches the already-read BK brief's same-runner/no-OTP direction; the additional CRO relay is attributed rather than independently fetched here. The parenthetical about FWD-9 and runner note should be identified as additions; they are not ownership/source metadata.

The earlier novelty qualifications remain unresolved in this pin: BACKEND lines 353-356 still deny any ratified cross-tenant isolation, despite FWD-2; lines 366-368 still call BK O3 wholly uncovered, despite the original FWD-4 mail/correction clauses now carried immediately above. Correcting the quoted DONE WHEN in FWD-9 does not resolve those broader claims. Both proposals remain explicitly unratified; no new verdict on them is made here.

CTO received the remaining five-line omission at 19:22:51Z, before this record was committed. Verification is confined to the endpoint repairs; it is not PRD approval, implementation acceptance or a project-wide completion grade.

## Follow-up: renamed endpoints at 2dcd88091f (message 95516)

CVO read the entire five-message Andrew-direct record at this pin. The codes are
now `IRPT_FNTEND` and `IRPT_BCKEND`; FWD-9 is ratified, FWD-10 carries the ingestion
construction ruling, and FWD-11 carries the new Global view with the named Model
Portfolios frontend pattern and scoped backend layout. This read confirms the
record and endpoint text, not the registry rows or the unread implementation.

The exact five-line FWD-8 tail at original `58266dab2d:361-365` occurs contiguously
in BOTH renamed endpoint blobs. The prior NOT A BI SURFACE / PENDING INPUT omission
is closed. FWD-9 now acknowledges the original email/correction coverage and
locates its additional bar in durability; FWD-10 distinguishes access from storage
isolation. Those prior novelty overclaims are narrowed in the new blocks.

Three residuals need correction before PRD inheritance:

- FNTEND lines 279-284 correctly count seven carried outcomes and five backend-owned
  contributions, then say closure requires the **four** crossing contributions.
  FWD-11 made that five. The closure sentence must explicitly include the Global-view
  contribution; adding it to the display block alone leaves the closure bar stale.
- BCKEND lines 449-452 claim eleven outcomes and ten backend acceptance owners.
  The actual block headers are FWD-1,2,3,4,5,7,8,9,10,11: **ten** outcomes, **nine**
  backend acceptance owners and one frontend owner. A second stale count line at
  452 still calls FWD-9/10 NEW and gives the old eight-plus-one total. Remove that
  contradictory leftover and recompute from the actual IDs.
- BCKEND FWD-9 lines 351-355 bind the quoted phrase "attributed to the right advisor
  and client" by the sender's domain. Andrew's recorded sentence fixes **firm**
  assignment from email; it does not establish that a domain identifies an advisor
  or client. Bind the firm at ingestion while retaining independent advisor/client
  resolution and the already-required unresolved-owner proof. The record's
  domain-to-firm generalization is an interpretation of his email example, not an
  additional verbatim instruction. Do not silently propagate that ambiguity into
  the shared contract.

The counted populations above come from pinned block-header enumeration, not the
summary totals. CVO did not rerun all original-block comparisons at this new pin;
the closure claim here is confined to the exact restored tail and the new blocks
read. Two projects and one acceptance owner per outcome remain the governing cut.

## Follow-up: ownership ruling and coverage obligation at 68d8b16a91 (95520)

CVO read the exact notice and the full three-file diff from `2dcd88091f` to
`68d8b16a91`, including the two added Andrew-direct messages. The prior allocation
is superseded: advisor-facing FWD-1/3/4/5/6/8/11 belong to IRPT_FNTEND; machinery
FWD-2/7/9/10 belong to IRPT_BCKEND. FWD-12 is a frontend proposal at Andrew, not
another ratified outcome. Its component and design requirement has not been
implementation-verified by this review.

Pinned block enumeration finds eight frontend blocks (seven ratified plus proposed
FWD-12) and ten backend blocks. Each block carries exactly one acceptance owner;
all six shared IDs, FWD-1/3/4/5/8/11, agree on the frontend owner in both copies.
This verifies ownership consistency in the blocks, not in every summary paragraph.

The old frontend closure residual is now a **superseded ownership rule**, not merely
a four-versus-five typo. FNTEND lines 345-347 still require two frontend-owned
outcomes plus four contributions graded by backend. Replace that paragraph with
the new owned-outcome closure rule, retaining both projects' evidence for the
crossing outcomes and keeping proposed FWD-12 separate pending Andrew's decision.

BCKEND lines 465-469 still say eleven carried outcomes and list seven frontend
contributions, including FWD-6, which has no block in this endpoint. The measured
local population is ten: four backend-owned blocks plus six frontend-owned blocks.
Line 469 retains the obsolete eight-plus-one allocation; the landing instruction
at 508-509 also says the header may list eleven. Those summaries must use their
declared population consistently. A project-wide list of eleven ratified IDs is
different from the ten blocks this endpoint actually carries.

The FWD-9 sender-domain attribution ambiguity from the preceding review is
unchanged by this diff and remains open. Firm assignment must not be confused
with independent advisor/client resolution.

Both endpoints now carry the brief-coverage obligation. For future L9, an FNTEND
grade on FWD-3/4/5/8/11 must read the backend data, parity, entitlement or execution
proof as well as the frontend proof. One project's mock cannot certify the other
half. The coverage limb must enumerate each project's brief sections and mapped
source documents, with consumers or explicit non-consumption reasons. Recording
that obligation does not establish that a not-yet-reviewed PRD is lossless: the
actual map and the content carried into cells must be read. An explanation for
omission is reviewable evidence, not automatic permission to omit a binding
requirement. No PRD, coverage-map or implementation acceptance is issued here.

## Follow-up: residual repair at 450763f963 (95523)

CVO read the complete two-endpoint diff from `68d8b16a91` and re-enumerated the
pinned block headers. BCKEND still carries exactly ten blocks; its count now
agrees: four backend owners and six frontend contributions. The stray old
eight-plus-one allocation is removed, FWD-6 is excluded from the local block
count, and the landing sentence now says ten. Those residuals are closed.

FNTEND replaces the superseded two-plus-four ownership rule and explicitly
requires both proof halves for FWD-3/4/5/8/11. That repair is confirmed. Two
contradictions remain at this pin, so the notice's blanket closure claim is not
accepted:

- FNTEND line 346 requires all EIGHT owned outcomes to grade REALIZED, while
  lines 306-307 and 341 still mark FWD-12 as a proposal awaiting Andrew. Closure
  must apply to the seven ratified owned outcomes, adding FWD-12 if ratified;
  alternatively cite a later ratification and update its status. This review
  supplies no such ratification. Ownership of a proposal is not its acceptance.
- BCKEND lines 365-369 still say the quoted advisor/client attribution is bound
  by sender domain and cannot change. The added note at 370-375 correctly says
  domain fixes the firm, not advisor/client, but leaves both statements operative.
  Replace the earlier sentence's subject with the request's FIRM assignment and
  retain the explicit L4 advisor/client resolution note. That makes the correction
  unambiguous without changing the ratified ACCEPT or asking for another ruling.

The coverage-map obligation remains a future evidence requirement. This bounded
prose review does not certify a PRD, an implementation, or project completion.
