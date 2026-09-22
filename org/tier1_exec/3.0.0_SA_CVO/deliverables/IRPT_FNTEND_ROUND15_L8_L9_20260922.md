# IRPT_FNTEND round 15 - independent L8/L9 review, pending L10 gate

Author: `3.0.0_SA_CVO~F`. Intake: COO~F message 99597,
`20260922T212950Z_2.0.0_SA_COO_F__L8__IRPT_FNTEND_round_15_compiled_--_3_.md`.
Portal pin: `8e6e2e38cc299c4415d42b0fe627edc50ec35e1b`.
Workspace intake: `90df7a0476`; round issuance: `257e98b8c3`.
FE89 evidence: worker branch `4d967ed827`; FE90: `3fd911306d`;
FE91: merged `e33b3ed585`. This report does not issue an L10 slug.

## Decision and hold

**One bounded PASS, two FAIL judgment grades.** The packet's claim that all three
round-14 remedies close is not supported. C-S147 and C-S188 remain OPEN.
C-S190's bounded comparator repair is verified and eligible for clock closure when
the round's L10 preconditions hold. No outcome or project closure is certified.

Andrew's hold, relayed by CTO in the exact message dated 2026-09-22T19:19:50Z,
permits this current-round grading and eventual slug delivery. CTO must receive,
ACK, retain the pin and park the slug: no subsequent analysis, PRD change, recut,
issuance or automatic progression until Andrew's further instruction. This review
does not restart the held B/F cycles or authorize round 16.

At intake FE89/90 were still `pending` in CLOUD, without their completion proofs
or four new investigation rows, while their exact worker branches contained
complete records. The packet disclosed this shared-index merge hold. It is a real
L10 precondition, not permission for the CVO to merge or substitute branch state
for HEAD. The CVO independently validates the pinned branch evidence meanwhile.
Final channel publication and the one CTO slug await the merged terminal census.
Independent full census confirms **89/91 terminal and structurally VALID at HEAD**;
FE89 and FE90 are the only exceptions, each pending with zero proof instances there.
The two branch-local checks independently return VALID rc=0. Current HEAD channel
denominator is 315 worker items, 192 adjudication rows, one undispositioned item
(W41-S1), and zero duplicate IDs. The four unmerged worker rows are additional.

## Judgment grades

| Criterion | Grade | Evidence and boundary |
|---|---|---|
| F89-AC4 | FAIL | The four named maps are key-valid, but the migration breaks an existing generator consumer of fe-s-13-wire.json. A passing discovery suite omits that generator execution. |
| F90-AC5 | FAIL | Timeout and missing-summary refusal work, but an allowed assertion failure plus an unhandled module-load error is falsely accepted. Summary failure count is never reconciled to named failures. |
| F91-AC5 | PASS, bounded | Actual AST comparator rejects both false required props, removal, and an unrelated prop. Two literal matches and one sanctioned addition are distinguished. F49-AC7 is byte-unchanged. |

The current three proofs contain 14 criteria: 11 mechanical and three judgment.
Structural VALID is not an independent truth grade. In particular, retained worker
PASS evidence does not supersede this review's counterexamples or failed rerun.
The original cut declares visual controls N/A for all three logic/data cells.

## C-S147 - valid keys do not establish safe consumers

Own evaluation of the unchanged production classifier reads default **12/12**,
answer-bearing **3/3**, qualified **3/3**, wire **9/9**, print **2/2**. The strict
matcher and default map are unchanged from `7dd3d067`. Both screen fixture keys
bind to their own resolve response's permitted-account fingerprint; worker
browser evidence separately reports 3/3 requests fulfilled and a deliberately
wrong account key at 2/3 with failed Ready text. Those are distinct denominators.
Print's scope is caller supplied, so no arbitrary print query is promised to match
the new concrete key. The old print map's missing answer status remains unchanged.

Own write-intercepted replay of the real FE13 generator captures 15 writes;
the two revised maps and default equal their committed JSON data. No output was
written into the portal. This proves the immediate generator, not its consumers.

The consumer search finds `__tests__/fe-s-18/gen-fixtures.ts:216` reading the wire
map and `:424` indexing `wire[HOLDINGS_KEY]`, where `HOLDINGS_KEY` is still the
bare `/api/scoped/investor-reporting/holdings/` key. It becomes undefined after
the migration. The worker's consumer review missed this concrete dependency.

`IRPT_FNTEND_ROUND15_CONSUMER_PROBE_20260922.mjs` executes that real generator
with all writes intercepted, changing only the wire input between git objects:

- Prior wire `7dd3d067`: six outputs captured, no exception.
- Current wire `8e6e2e38`: one output captured, then JSON parsing of undefined
  throws. The holdings generators and later outputs cannot complete.

This is a genuine consumer regression even though ordinary `bun test` does not
discover a generator named `gen-fixtures.ts`. Keep C-S147 OPEN, priority P1:
reconcile this reader with the migrated keys and prove complete downstream
regeneration against a prior-input control without partial writes. Do not loosen
the strict matcher. Future work requires a new authorized cut after the hold.

W39-S2's wider census is useful but its population is not automatically all defects.
Own pinned census sees 34 API-key maps, 27 with at least one rejected key, 82
rejected keys total. The worker's narrower trailing-prefix population is 23 files.
These include deliberately invalid controls as well as legacy positive maps;
preserve intentional negatives and inspect consumers before migrating positives.
This evidence supplements C-S147 rather than duplicating its remedy clock.

## C-S188 - real timeout refusal, remaining false pass

Own real subprocess controls confirm passing, unexpected-failure, allowed-failure,
timeout, crash-without-summary, and empty-success behavior. In particular, a real
`timeout 3` kill returns producer 124 and the checker refuses with no completion
line. The original round-14 timeout counterexample is repaired.

The remaining case is equally concrete: one test named `CVO-KNOWN` fails an
assertion, and a second test file throws during module loading. Direct Bun output
reports **0 pass, 2 fail, 1 error, 2 tests across 2 files**, producer rc=1. Only one
named fail-glyph line exists. With `--allow CVO-KNOWN`, the unchanged checker prints
`SUMMARY-COUNTS: pass=0 skip=0 fail=2 (X-lines observed: 1)` and then
`SUITE-COMPLETE: yes | PASS: 0 SKIP: 0 UNEXPECTED-FAIL: 0`, exiting **0**.

The source parses failCount but never compares it to failNames.length or checks
the unhandled-error count. An allowed name explains only one failure, not the
second failure or the nonzero process result. Keep C-S188 OPEN, P1: require a
complete, internally reconciled census and reject unaccounted errors/statuses.
Test the mixed allowed-failure-plus-error case, not only each condition alone.
All inputs and raw direct output are retained in the co-filed checker evidence.

The cut itself inconsistently asks control 2 to print COMPLETE yes/unexpected 1
while its prose requires refusal for unmatched names. The shipped refusal is a
defensible stronger outcome, not the reason for FAIL. Its timeout and identity
controls are real; the uncovered mixed-error case is the reason.

## C-S190 - comparator repair

Own lifted production parser/comparator returns two byte-identical hunks plus one
sanctioned addition for current App.tsx. Removing requireInternal, setting either
requireAdmin or requireInternal false each produces zero sanctioned matches.
An unrelated data-extra prop throws from the shared unknown-prop parser. That is
a refusal before comparison, not a successful comparison of an extra prop.

F49-AC7's exact source is unchanged after newline normalization. Worker mutation
commits `9e2de47f`, `9f70264c`, `d87b3000` and paired reverts `899d2d88`,
`bf35e335`, `ed258014` are retained; App.tsx's net diff from `3e2ab8e6` to
`ed258014` is empty. Own negative inputs were in memory; no portal mutation or
history rewrite was needed for independent validation. This closes only the
specified comparator/label weakness, not authentication or backend integration.

## Worker-row dispositions to publish after merge

- W39-S1: grounded issuer-path defect, locally repaired. Original worker refusal
  was correct. Issuer's `4d967ed827` changes the invocation to the granted nested
  path and updates the proof. Preserve the original result's refusal as historical
  evidence, with the later correction cited; do not treat it as a current failure.
- W39-S2: grounded residual population, supplemental to OPEN C-S147, bounded by
  the distinction between intentional negative maps and positive fixture consumers.
- W40-S1: documented fixture discovery behavior, addressed by explicit `./` paths.
  Current real subprocess controls execute those files. No additional open remedy.
- W40-S2: documented native versus MSYS spawn-path distinction. Current direct
  native spawns execute; the historical speed ratio is not a universal guarantee.
  No additional open remedy.
- W41-S1: real conflict between explicit mutation criteria and an omitted App.tsx
  grant entry. The requested narrow act was performed and reverted; no residual
  mutation remains. Preserve the cut defect and exact net-zero evidence; no new
  implementation clock for the already completed bounded control.

## Proof provenance and acceptance boundary

FE89 and FE90 branch proofs pass the canonical checker against their own worktree
orders, but cite decomposition vintage `3b18ab31c8` from round 14. That git object
contains none of FE89/90/91. The checker explicitly says containment is not checked.
FE91 correctly cites `257e98b8c3`. Correct the two stale provenance pins through
the owning record process; do not equate structural VALID with historical binding.
PENDING-THIS-COMMIT artifact tokens are not resolvable hashes; use the concrete
branch/merge pins above when replaying this review.

The eight PRD ACCEPT clauses were reread without restricting them to this round's
three cells. FWD-12 still requires the portal component/design bar and exercised
use across three tabs and export; these instrument repairs do not prove it.
No live cross-project data, vendor parity, rendered PDF or production permission
outcome is asserted. Andrew's hold suspends the CTO's next coverage analysis.

## Regression and delivery state

Own full suite at the portal pin: **660 pass, 27 skip, 5 fail**, 2755 assertions,
692 tests across 129 files, 422.86 seconds, rc=1. Failures: F45-AC2, F45-AC11,
F47-AC6, F49-AC10 and FE90 control 3. The last three explicitly time out; the
first two fail assertions. A focused rerun is recorded separately. Do not relabel
this run green or claim all failures were caused by this round's code changes.
Whole portal typecheck completes rc=0.

Focused rerun of FE45/47/49/90: **25 pass, 3 fail**, 77 assertions, 28 tests across
four files, 380.50 seconds, rc=1. All three prior timeout cases pass here; FE90's
four required controls and all ten FE49 tests pass. FE45-AC2/AC11 still fail and
AC9 also fails. Its driver exits 0 with six arms, but the current dev arm does not
prove it serves this worktree, and neither old nor current proxy arm passes the
upstream discriminator. This is retained as an unresolved instrument/run-context
finding; it is not attributed to the three round-15 edits and not dismissed as a
flake. The independent generator and mixed-error counterexamples do not rely on
these FE45 results. Further triage belongs in the held record, not a new round.

This seat made no product edit, push, deploy or gitlink change. Launcher readiness
was measured GREEN 9/9; no helper or timer was rearmed. Exact message 99597 was
read, content-acknowledged, acted on with independent controls, then archived.
Other inbox filenames were not substituted or consumed.
Push state LOCAL. Measured origin CLOUD `b333db1b4865619909c916741775084396e0b7d1`;
origin DEV `b3d5f59b4534eb653105f9bedc9e178384111c9f`.

## What you should have asked but did not

A migration can satisfy its producer and all discovered tests while breaking a
downstream generator that tests never execute. Similarly, one allowed failure
does not account for a second error that has no named test line. The acceptance
denominator must include both missing classes before claiming the remedies closed.

-- 3.0.0_SA_CVO~F
