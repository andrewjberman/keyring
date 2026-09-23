# IRPT_FNTEND round 10: independent L8/L9 read

Seat: `3.0.0_SA_CVO~F`. Recorded 2026-09-21, 23:14 UTC (approximately).
Input: COO~F message 99314, exact unread carrier
`20260921T230324Z_2.0.0_SA_COO_F__DRIVE_IRPT_FNTEND_round_10__L8_packet__.md`.
Authority: Andrew's Track-B assignment @4368801e4b; the spine assigns L8/L9/L10
to this seat. The message is acknowledged by this act, not a mid-round peer send.

## Locate and measured pickup

- Home `org/missions/D9/IRPT/IRPT_FNTEND`, D9/laptop, active, claimed EXECUTING.
  Brief and endpoint pointers remain those in project.json. PRD v0.9 @5fd2dc9ab5
  is ADMITTED with both current signatures. FWD-12 is this round's only outcome.
- Decomposition v0.10; issuance `fcf38f866b` covers FE-s-61..64:
  fanout 4 of 4 independent chains, cap 8. Decomposition diff since that cut is empty.
  FE-s-63 was explicitly amended at `84077faa2d`; the original refusal is retained.
- Workspace intake HEAD `0a28a5d1b4`; portal DEV `243089eb8f49514e99c97360259ce70c0772c859`.
  Four round orders complete. `to-check --all --project IRPT_FNTEND`: zero active;
  the row gate's own `_open_tos_for_project`: `([], 64, '')`.
- Four bound receiving checks ACCEPT. Repeated proof-of-spec-check with the
  EXACT criterion-id list extracted from each governing order: VALID, rc=0,
  5/9/8/6 acceptance rows, 28 total. Coverage is not inferred from the wrapper's
  initial coverage-unchecked run. This is form/record validation, not truth.
- No uncommitted project-tree or portal InvestorReporting changes at intake.
  No unmerged branch matching this project's name; no round-10 worker worktree
  remains in the worktree list. The workspace has 22 unrelated/older stashes;
  none restored, popped or deleted. No assertion about their contents.
- comp-surprise intake: 276 worker/seat investigation items, 13 unresolved,
  115 CVO carrier rows. All thirteen packet ids agree with the rollup.
  Prior round-9 slug is REMEDIATION_v6; this round has no slug at intake.
- Class OPEN-ROUND; next act L8/L9 is MINE. Production is this report and the
  accompanying read-only probe, not a judgment that any peer is stalled.
  Event-driven inbox intake worked. No new surprise watcher or runtime helper
  was launched; no independent surprise-stream watermark readiness claimed.

## Independent exercise

At portal `243089eb`, this seat ran `bun run typecheck` (rc=0) and
`bun test src/pages/InvestorReporting` (rc=0): **612 pass, 22 skip, 0 fail,
634 tests across 114 files, 2579 expect calls, 76.16 seconds**. Browser-gated
skips remain skips; the test suite's own temporary servers are not a live
backend or an advisor acceptance session.

Read DESIGN.md in full. Read all four governing orders, worker result records,
the thirteen row bodies, proof evidence, relevant source and the PNGs directly.
Visual evidence used: ~11's BEFORE/AFTER supplementary pair at both widths;
~12's supplementary Holdings pair and Analysis BEFORE/AFTER pair at both widths;
~13's export and print pairs, print-ground BEFORE/AFTER and period-note crop.
These are worker-produced, fixture-fed captures independently READ by this seat,
not browser captures produced anew by this seat. Sources were read at portal HEAD.

`IRPT_FNTEND_ROUND10_CHECKS_20260921.ts` (beside this report), run from the
workspace root, rc=0, reads without writing or calling a backend:

1. Original `fe-s-16-print-narrative.json` performance envelope is REFUSED by
   parseIrEnvelope on **unprojected_grant**, code ENVELOPE_UNPROJECTED_GRANT.
   New print-ready envelope is accepted READY. Add ONLY unprojected_grant to the
   original: accepted UNCERTAIN (still no stated status). Remove ONLY that field
   from the new envelope: refused on that field. Both maps ALREADY have the same
   performance/ and narrative/ route keys. Thus the replacement worker's
   route-key explanation does NOT explain the separately reported diagnostic
   fixture's failure. The parser seam is proved; the complete old browser path
   was not rerun. No implication that adding one field alone makes a READY print.
2. Census names independently compared against `9e0370009f`: 65 -> 73, added
   AnswerStatus, AppliedBranding, ExportModalPanel, GenerateComposer, PanelEmpty,
   ReceiptPanel, RevisionIdentity, UnnamedReasonCodeFlag; removed zero.
   Against the committed 70: added AnswerStatus, PanelEmpty, UnnamedReasonCodeFlag;
   removed zero. Current split 28 REUSED / 45 NEW.
3. UnnamedReasonCodeFlag and PageSheet really carry identical reason strings,
   despite different functions.
4. Source-colour contrast #595959 on #FFFFFF is 7.0047:1 using relative luminance.
   Not a screenshot-pixel or physical-print measurement.

## Judgment grades: the issued bar, not an outcome grade

| Criterion | Verdict | Scope and limit |
|---|---|---|
| F61-AC5 | NOT_EVALUATED | Header and period-control changes are readable, with both-width BEFORE/AFTER evidence. PageSurfaceControl is imported by both FirmDropdown and ModelPortfolios (source, not appearance). But the required summary cards, chart, period results and ScopeSummary partial-disclosure fact do not occur in the supplied captures. A style judgment over those absent renderings is unavailable. No fabricated pass or failure of the unseen product. |
| F62-AC9 | NOT_EVALUATED | Source confirms CategoryViewTree/model-colour reuse and SliceTable's real table. The visible Analysis typography fix is supported at both widths. But Analysis says requests unavailable (no-declared-route); input review and stage display are absent, and Holdings shows an authoritative ADVISORY token, not the required withheld state. A whole-criterion grade cannot be inferred from a subset of its named surfaces. |
| F63-AC8 | PASS | The criterion asks for a RECORD of the export/print read and the period-note question, not a declaration that the product conforms. Both-width export/print captures and the crop support that record. The note is rendered as '1 of 5 events not yet reflected in this narrative.' The export's visible contract violations remain findings, not a passing brand review. No clause explicitly names a print-sheet role, but C1's 'anywhere', C9's actual-backdrop contrast and C11's product-wide language are not annulled by that omission. The note's source colour clears C9's normal-text threshold on white; a full print-brand verdict is not claimed. |
| F64-AC6 | PASS | Record-grade: all 45 NEW names are listed with domain needs/dispute points, both historical baselines and additions/removals are correct, and the pinned census test is run and disclosed. The criterion does not order implementation. The actual PRD constraint that existing components cannot meet each NEW need remains unsupported by those role labels; W14-S2 graduates. This is not approval of 45 new components or of FWD-12 realization. |

Machine-readable grades are appended to ADJUDICATION_v3, bound to each instance
at `0a28a5d1b4`. No existing worker verdict, task-order status or prior grade edited.

## Dispositions and scoped corrections

| Item(s) | Disposition | Grounded finding / limit |
|---|---|---|
| W11-S1, W12-S1 | GRADUATED | Named fixture operation keys do not match consumed wire routes; canvas/click lines cannot certify READY content. Supplementary evidence does not repair the ordered test. |
| W11-S2 | GRADUATED | Required Reporting content is not captured. Include the uncaptured ScopeSummary partial fact in the evidence gap. Do not substitute a print page for the on-screen Reporting tab. |
| W11-S3 | GRADUATED | index.tsx red-only error and shared StatusPanel's filled Retry/Reload alongside Export contradict C12/C8; directly visible and source-confirmed. |
| W11-S4 | GRADUATED | Reusing PageSurfaceControl is real; copying ModelPortfolios' old class string does not supersede C1/C11. Cohort/slate findings are source-level, not a cohort screenshot claim. Cross-file tests and shared-pattern constraints need a coherent grant. |
| W12-S2 | GRADUATED | CategoryViewTree is a dark container inside a white panel: C3. Correction: purple CHART SERIES/legend is not inherently an unauthorized C8 action accent; data use is explicitly excepted. The A-0001 breadcrumb is styled in DrillTree, not CategoryViewTree. Do not route every subclaim to one shared file. |
| W12-S3 | GRADUATED | Red-only errors are C12 findings. Narrow table content is outside the initial viewport, but SliceTable has overflow-x-auto and min-w-[640px]; a still PNG does NOT prove inaccessible or irrecoverably clipped content. Test reachability before asserting a layout defect. C10 does not literally contain the filer's 'no clipped content' quotation. |
| W13-S1 | GRADUATED; REMEDIATED/DISARMED | Issuer amendment and wire-valid replacement fixtures yield actual documents; both current proof invocations and PNGs corroborate the local disarm. The older diagnostic's cause is corrected above. Original stale shared fixtures were not repaired by authoring replacement fixtures. |
| W13-S2 | GRADUATED; OPEN/ARMED | The screen print-ground fix is real (BEFORE/AFTER and print.css). The row ALSO concerns ui-smoke measuring a different ground; that future false-positive mechanism remains. Accept only the localized disarm, not a whole-row disarm. No edit to hazard-at-birth. |
| W13-S3 | GRADUATED; REMEDIATED/DISARMED | Its blocking condition was no rendered note. The current print/crop resolves that condition. No invented print-specific palette rule; generic clauses and source-colour contrast remain assessable. |
| W14-S1 | DISMISSED_WITH_REASON | census.test.ts explicitly documents reading written historical JSON and tells callers to regenerate separately. The conditional 'if it fails' in HOW 4 is not a promise that the test detects live drift. 70 vs 73 is a disclosed vintage difference, not a defect in that test's actual contract. Never cite its pass as live freshness. |
| W14-S2 | GRADUATED | The copied reason is demonstrably wrong; broader NEW-vs-existing needs are unproved. Counting wrappers NEW is not inherently wrong, and self-use inclusion is an inventory-definition question, not proof components are absent. |
| S69 | GRADUATED | ReceiptPanel fabricates LOADING whenever receipt is null, including before submission. NOT proved: post-click nontermination. NOT accepted: the claim that only a new shared enum can fix it; an idle presentation might be local. |
| CVO supplemental finding: Analysis/Holdings evidence coverage | GRADUATED | The supplementary images still omit named F62-AC9 surfaces. Existing listAnalysisRequests explicitly refuses no-declared-route; do not invent a backend operation to make a screenshot pass. |
| CVO supplemental finding: export visual contract | GRADUATED | ExportModalPanel uses a dark chart Panel and filled-purple selected branding chips; source and both captures show C3/C8 conflicts. Historical colour-law tests allow any Panel anchor and do not grade these current clauses. Preview overflow is deliberate horizontal scrolling in source: no unsupported clipping verdict. |

Of the thirteen incoming rows, twelve graduate and one is dismissed. Two of the
twelve are already remedied/disarmed. Two additional CVO findings are remediation
inputs. All sixteen new CVO carriers (grades, dispositions, supplemental findings
and a correction record) are append-only. One remediation document, v7, carries
fourteen rows; it is not fourteen messages.

## Handoff and boundaries

L10 precondition is checked again at commit by the canonical row gate. The one
slug goes to CTO only after that gate admits it. No mid-round peer ACK, no
COO/worker instruction, no portal edit, no push, no deployment and no gitlink bump.
FWD-1/3/4/5/6/8/11 retain the packet's backend boundary. No realization grade on
any outcome is issued by this record: that act belongs to CTO.

Push state LOCAL. Remote CLOUD was not changed by this seat; final ls-remote
measurement is reported with the send/turn completion rather than inferred from
a tracking branch.

