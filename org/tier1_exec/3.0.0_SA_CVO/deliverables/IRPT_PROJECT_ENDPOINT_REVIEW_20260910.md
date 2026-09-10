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
