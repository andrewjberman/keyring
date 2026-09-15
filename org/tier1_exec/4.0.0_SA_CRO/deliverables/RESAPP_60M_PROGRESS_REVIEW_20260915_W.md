# RESAPP: 60-minute progress and connection review

Seat: `4.0.0_SA_CRO~W`  
Authorized window: **2026-09-15 06:13:02Z–07:13:02Z**  
Status: **COMPLETE — closing snapshot 2026-09-15 07:13:38Z**  
Authority: Andrew's verbatim instruction in `ANDREW_DIRECT_20260915_RESAPP_60M_PROGRESS_LOOP_W.md@76ab87a06e`.

## Changes observed

The watch began after the v0.6 brief-half review. Both v0.6 review halves were refused; round 10 was at ROUND_CLOSE. The review identified five concrete producer/consumer defects, sent their connection briefs to CTO, and followed those requirements into PRD v0.7. A sixth brief covers the provisional COO round-11 cut; a seventh records residual connections after its amendment.

PRD **v0.8 @1170b4da69d1f37471baff2b2d4d042712e41264** is now **ADMITTED**. This seat signed the brief half at `e1d8b2d643`, review `AMGT_RESAPP_v07_BRIEF_REVIEW_20260915_W.md@4786fedcc3`; its bytes are unchanged in v0.8. CVO signed the ratified-text half at `0e6592e88c`, review `AMGT_RESAPP_V08_RATIFIED_TEXT_REVIEW_20260915_W.md@3d451234b7`. The final relocation moved review provenance out of ENDPOINT without changing an outcome or contract.

The local-operation instruction initially remained missing from the revision. Its exact source was located at `ANDREW_DIRECT_20260914_DOWJONES_HARVEST_W.md@187f003998`, line 21, and sent to CTO. The committed PRD now expressly puts both session acquisition and API pulls on this box. It treats the earlier EC2 estate as history/available infrastructure and preserves Andrew's later reservation of recurring activation and cadence.

## Briefs sent to CTO

All files below are in `org/tier1_exec/4.0.0_SA_CRO/deliverables/`. Each was pathspec-committed and delivered through `org/mcp/codex-send.ps1`.

| Brief | Commit | Concrete finding | Follow-through observed |
|---|---|---|---|
| `RESAPP_CONNECTION_BRIEF_POOL_READERS_20260915_W.md` | `0e7de170e3` | Producer field `published` versus consumer `published_at`; exact body/link join; deduplication, partial reads and packaged schemas/dependencies | Carried in signed C-ONE-STORE and section 9 |
| `RESAPP_CONNECTION_BRIEF_IDENTITY_20260915_W.md` | `b90bfdd20d` | Model/Bloomberg keys versus plain-ticker and folder-hash publication associations | Carried in signed C-ONE-IDENTITY and section 9 |
| `RESAPP_CONNECTION_BRIEF_SOCIAL_SERP_20260915_W.md` | `36a08d3d1a` | Documented X profile discovery is not broad cashtag search; Reddit keyword route; async job persistence; typed social items and admission | Carried in section 9's bounded S13 measurement and content map |
| `RESAPP_CONNECTION_BRIEF_FILING_EVIDENCE_20260915_W.md` | `a65fe406c2` | Inline tags have no saved passage map; existing gate passes an unknown ID without a quotation and checks titles rather than body passages | Carried in signed C-FILINGS-ANALYZER and section 9 |
| `RESAPP_CONNECTION_BRIEF_RANKING_RETRIES_20260915_W.md` | `5ae6dd04b5` | Same-date writer retains former winners and fails to clear an empty result | Carried in signed C-RANKING-GENERATION and section 9 |
| `RESAPP_CONNECTION_BRIEF_ROUND11_CUT_20260915_W.md` | `0f9a04e81e` | Provisional-cut ownership conflicts, missing CIK input, evidence strings versus IDs, crosswalk/generation amendments, two-sided QA dependencies, S13 disposition and inconsistent subtraction | COO v1.3 `73938cdae4` carries substantial amendments; residuals in the next brief |
| `RESAPP_CONNECTION_BRIEF_ROUND11_FOLLOWUP_20260915_W.md` | `865e4fc113` | Actual social call type; list/point/history generation migration; index-read completeness; remaining file/dependency edges; correct same-day/empty controls; comparison-pair timing; expanded row IDs | Delivered to CTO and COO at 07:02Z; final checkpoint below |

COO's provisional v1.2 `a0f08622ae` defined 12 cells against v0.6 while preserving the issuance hold. Its v1.3 amendment `73938cdae4` defines 13 cells: the crosswalk/CIK comes first, the filing batch is local, evidence IDs resolve to passages, the pool reader and complete-generation writer are explicit, and S13 has a bounded measurement cell. The 07:04:46Z checkpoint found zero round-11 task-order files and no uncommitted decomposition change. That is progress in the plan, not a claim that the cells have run.

## Evidence and limits

- The filing-gate and ranking-writer probes ran locally against the actual functions with synthetic inputs; the ranking writer's AWS resource was replaced by an in-memory table. They did not alter a live table or make a model/publisher call.
- Official Bright Data documentation established the documented discovery call shapes; no dataset job was submitted. Account capability and an end-to-end social collector remain unproven by that documentation review.
- The source-map check resolved all 24 explicit adjacent path/pin references. The original pinned brief has 21 Markdown headings; the supplement has 22 provenance rows, 10 content-map rows and nine measurement-limit rows.
- Source design, signed specification, provisional decomposition, issued work and validated feature behavior are separate states. Incorporation into a signed PRD does not mean the defects have been implemented away.
- Compiler risk reflex remained PARTIAL_OR_BLIND due its stale danger map; Markdown commit gates inspected no implementation files. Those outputs are not used as validation of the findings.
- At 07:09:17Z the Windows task `Opal Data Harvest - Local Publications` was Disabled, its trigger property was null (zero actual triggers), and its next run was null. The repository config still had `recurring_schedule_enabled=false` and `automatic_uploads_enabled=false`. No task was started or changed by the review.

## Final checkpoint

The watch closed at **07:13:38Z**, after the authorized 06:13:02Z–07:13:02Z window. PRD v0.8 remained ADMITTED with both halves SIGNED/current. The decomposition remained at ROUND_CLOSE, with **zero round-11 task orders issued**. The exact-seat root inbox was empty. The in-session checkpoint log is `.runtime/opal-data-harvest/resapp-progress-checks.jsonl`; `.runtime/opal-data-harvest/resapp-progress-loop.json` records the completed watch and seven delivered connection briefs. No recurring watcher or additional inbox helper was installed.

COO committed a second amendment at **07:12:43Z**, `41fe04767a5ed6909e8c053e697a03f20c0197bb`, with no uncommitted decomposition change at closing. The 13-cell plan now pins admitted v0.8, counts the 20 source requirements correctly, gives the ranking row-shape edit one owner, checks generation row counts against eventual index reads, preserves all-zero Trending ties versus empty Breakout, selects the documented Reddit keyword method, and explicitly puts rj-8 after rj-6 in its cell and handover prose. These are meaningful plan corrections; implementation and live acceptance remain ahead.

Two substantive handoff issues from the seventh brief remain in that closing revision:

1. **Preserve PRICE and historical reads during generation migration.** The amendment requires every ranking reader to follow a generation pointer and never read a bare date partition. The unchanged PRICE producer still writes the existing date-partition keys without such a pointer. The shared reader must explicitly support unmigrated PRICE/history, or the producer and historical data must be migrated as a tested dependency. A blanket pointer requirement can otherwise hide existing results. This is the compatibility requirement already stated in brief `865e4fc113`.
2. **Choose the QA pair before its producers finish.** The amendment chooses the pair at rj-7's drain while also requiring that pair in the original spawn prompts of rj-6/rj-7/rj-8. rj-6 and rj-7 can run concurrently, so that ordering does not ensure both securities receive the necessary artifacts. Choose the pair before those cells start, or define a concrete follow-up/re-entry step to produce missing artifacts before paired QA. In addition, align section 19e's dependency edges and the older five-way fan-out wording with the new rj-8-after-rj-6 requirement.

These are decomposition and implementation acceptance issues, not a request to reopen the signed PRD. This closing report carries them to CTO and COO; the 60-minute watch is finished.

Publisher collection remains disabled pending Andrew's decision. This progress review does not clear the independent Barron's verification limitation, activate a daily harvest, or authorize a broad backfill.
