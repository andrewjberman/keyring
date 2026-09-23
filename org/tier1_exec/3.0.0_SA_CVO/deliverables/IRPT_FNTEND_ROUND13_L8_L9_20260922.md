# IRPT_FNTEND round 13 - independent L8/L9 review

Author: `3.0.0_SA_CVO~F`. L8 packet: COO~F message 99484, 2026-09-22T13:24:35Z.
Scope: FE-s-80..84, decomposition v0.13, issuance `e01db98917`, PRD v0.9.
Workspace read pin `da9ac0dae9b8d426a4357e6d0921656d87a73125`; portal read/test pin
`467354c947c1afebc77eb6839724c7243547f46f`. LOCAL only. Origin CLOUD measured
`438312b0855f798c3456b3577179eed91d98df2c`; no push, deploy, or gitlink edit.

## Result

**Three bounded judgment PASS grades; F80-AC6 FAIL.** The current portal suite is
**648 pass / 27 skip / 2 fail**, 677 tests across 127 files, 2702 assertions, 70.44 seconds.
Both failures are the generated sibling fixture tests. The worker's successful regeneration
was not preserved in its committed fixture outputs. The source repair is present.

The single L10 carrier is `surprise-channel/remediations/REMEDIATION_v10.md`, with four
OPEN remedies: W25-S1, C-S147, C-S150, and new C-S176. Eight narrowly described remedies
are REMEDIATED. This is not an outcome or project closure. No blanket retirement of older
findings is implied.

Five existing remediation clocks advance in their original v8/v9 documents in this commit;
three existing open clocks remain unchanged. The v10 slug carries four new JSON records
and references all eight reviewed existing clocks; its
four-OPEN/eight-closed summary covers the combined changes. The first commit gate correctly
rejected duplicate old IDs in v10 and the misspelled `judgment_grades` field. Both were
corrected (`grades` is the schema field). A second refusal correctly limited old-row edits
to monotonic clock changes: original mechanism, evidence, remedy and round now remain
unchanged; new findings live in this round's adjudication. No override was used. The gate disclosed a
large historical stale-remediation backlog. That is not silently closed by this round.

## Receipt and denominators

- Direct task-order census: 84/84 terminal. `python .tools/to-check.py --all --project
  IRPT_FNTEND` reports zero active; its workspace-wide third-population footer is not the
  project denominator.
- Independently invoked `python .tools/proof-of-spec-check.py <instance> <expected IDs>
  --governing-order <exact order>` for all 84 current instances: 84 structurally VALID.
  All five round-13 instances are VALID, 30 rows total, 26 invocation-bearing mechanical
  criteria and four judgment criteria. Fourteen round-13 portal artifact paths also resolve
  with `git -C portal cat-file -e <pin>:<path>` in the nested repository.
- Structural validity is not truth or historical universal PASS: the 84 instances contain
  662 PASS rows, 79 UNVERIFIABLE-BY-INSTRUMENT rows, and nine historical FAIL rows on
  FE-s-52..59. Those remain recorded as failures; this review does not rewrite their vintage.
- The first census attempt misparsed FE-s-23's prose mention of `<expected_criteria>`.
  Anchoring the extraction to an actual tag line and rerunning the census yields 84/84.
  A separate explicit seven-ID FE-s-23 check also returns VALID. The parsing false alarm
  is not a project defect.
- Incoming channel: 305 investigation items, 167 adjudication rows, four undispositioned
  items, no duplicate IDs. W31-S1 was already disposed by this seat at C-S167. New rows
  C-S168..171 dispose W33-S1, W32-S1, W32-S2, W34-S1. C-S172 carries the grades;
  C-S173..177 carry grounded residuals and corrections. Worker investigation rows are unchanged.

## The six issuer amendments

| Criterion | What the committed amendment changes | CVO finding |
|---|---|---|
| F81-AC2 | Echo process exit code and match `rc=0(?![0-9])`, instead of guessed completion words | Preserves the stated clean-generator-completion bar. It does not prove generated files landed. |
| F83-AC2 | Real Investor Reporting route, Holdings interaction and applicable fixture | Preserves navy/not-indigo discrimination on the actual light-ground caller. |
| F83-AC3 | Invoke the purpose-built real-hover test | Preserves the hover behavior bar; a supplied dev-server precondition must actually be MET. A skipped test is not exercised hover. |
| F83-AC4 | Same real route, omit Holdings so the element is genuinely absent | Preserves the absent-selector control. Expectation remains `UNMEASURABLE`; this did **not** become focus-ring acceptance. |
| F82-AC2 | Add real drill depth and current-span/ancestor-button selectors | Preserves the requested 700/non-700 distinction. Own browser measures 700/400. |
| F84-AC5 | Replace nonexistent fixture path with committed qualified-state fixture | Preserves the real qualified-state non-amber background bar. Own measurement is white, with warning border and navy ink. |

Read actual amendments `6d3b2e4d92`, `6e3d50ab44`, and the final F81 order whose worker
branch amendment was previously checked at `843b8851eb`. The six faulty criteria correspond
to four defect investigations, not six separately filed worker rows. W32-S2 is an additional
method disclosure. The packet's premise that FE-s-81 has a final judgment is false: its five
criteria are all mechanical. The final order, rather than packet prose, governs.

These narrow repairs do not reconcile the common five-part visual rule. Both FE-s-80 and
FE-s-84 results explicitly waive actual-container ground controls because the assertion is
foreground/style-based. The orders state no such exemption. F80-AC3 fulfils 3/12 fixtures;
the Holdings probe fulfils 3/9, despite all declared keys being recognized. Declared-key
validity and actual request fulfilment answer different questions. This is C-S176, not a
license to silently weaken the common rule or declare broad visual acceptance.

## Independent grades and measurements

### F80-AC6 - FAIL

Read and evaluated the shipped `routeKeyCandidates` / `checkKeyValidity` functions against
the real `consumed.ts`. The concrete holdings path is accepted. The undeclared
`/api/scoped/investor-reporting/holdings/A-0001/not-a-declared-operation` is also accepted,
`valid=1,total=1`, although the only declared holdings template has one parameter and no
trailing operation. Static-only suffix matching remains correctly rejected. The real
`status/extra-junk` is not a valid negative control because `status/{jobId}` is actually
declared; the co-committed probe deliberately separates that from its static-only control.
The instruction's prefix mechanism was implemented, but the judgment asks whether the
widening is correct. The new wrong-tail false positive prevents that conjunction from passing.
Existing C-S147 remains OPEN with a full-template and admitted-prefix-grammar remedy.

Other limbs are supported within their stated limits: the source of ReceiptPanel confirms
the changed descendant is lawful secondary ink `#6B7280`, rather than inherited parent navy.
The worker's four recorded runs show positive PASS, wrong-colour FAIL, absent UNMEASURABLE,
and old parent still PASS on the same wrong colour. The shared scroll script accepts selector,
route, fixture, clicks and width as arguments; its recorded export displacement is 0->792.
FE-s-84 reuses it for a distinct report container, 0->638. The geometric far-edge predicate
does not identify every descendant, inspect all intermediate offsets, or prove generic
visibility under every nested clipping ancestor. No such universal claim is made here.

### F82-AC6 - PASS, bounded no-DOM integration

Own browser measurements after a real Models drill: current crumb `Models` weighs 700,
ancestor `A-0001` weighs 400, both navy on the actual white Holdings ground. Read the full
test and ran it independently. Stale click: two harness passes and real DrillTree refusal
content. Fresh click: two passes, navigation and no refusal. Baseline: one pass, no refusal.

The test invokes DrillTree's exported function during a server-rendered harness, reads its
own onRowClick closure from the returned element tree, and lets real React state updates
rerender that body. Hooks attach to the harness fiber. This reaches the actual conditional
branch and is stronger than constructing PanelError separately. It is not a DOM click,
independent DrillTree fiber, effect-lifecycle test, or claim that the wire adapter can produce
the revision mismatch. This meets the order's explicitly no-DOM branch objective. W17-S1's
component-coverage remedy and C-S164's weight remedy close at that bounded scope.

### F83-AC6 - PASS, with CVO-supplied keyboard exercise

The worker driver exercises hover only; a focus class and a source comment alone do not
establish focus behavior. Own fixture-fed Edge probe supplies the missing interaction:
rest none/opacity 0; real hover underline/opacity 1; keyboard modality plus actual tile focus
underline/opacity 1; blur none/opacity 0. Ink is `rgb(22,51,114)` throughout. The tile itself
matches `:focus-visible` and computes white 2px gap plus indigo `rgb(95,59,227)` 4px ring.
The focused tile screenshot was read. The link is not separately focusable, as intended;
the tile owns the focus. C-S165 closes. This does not certify the entire surrounding page.

### F84-AC7 - PASS, bounded colour and exercised-scroll conjunction

Read both committed worker images: `f84_report_390_scroll_before.png` and
`f84_report_390_scroll_after.png`. The after image reveals July/August/September chart dates
absent before, consistent with recorded 0->638 displacement (948 scroll width, 310 client
width). The shared driver performs the scroll itself. The pair now exists at the retained
vintage; the old F78-AC7 NOT_EVALUATED record is not rewritten. No permanent clipping
defect was demonstrated. The pair is not a census of all intermediate positions or all content.

Own complete/qualified browser measurements read white grounds and navy ink, base hairline
`rgb(196,203,219)`, qualified warning boundary `rgb(211,124,23)`. Both captures were read.
These are DESIGN.md named roles (C3/C6/C9), with warning carried by a non-text boundary and
the explicit qualified label. Existing UNAVAILABLE summary values remain unavailable; the
source edit changes styling, not data. However, AnswerStatus still measures Ready/Partial
at 600 and the qualifier at 500. C1 explicitly allows only 400/700. C-S150 stays OPEN with
this precise residual; the bounded F84 colour/scroll grade is not whole-report conformity.

## Committed fixture failure

At producer pin `9d3d9ea85b5b76e104b2122446cb3a8404ecafc8`, drain `86ae054b`, and current
portal HEAD, `git show` and JSON counts agree:

| Fixture | `unprojected_grant` present / entries |
|---|---|
| default.json | 12/12 |
| fe-s-13-wire.json | 0/9 |
| fe-s-14-print-v1.json | 0/2 |

The worker commit lists only generator source and its new test. It does not carry the two
generated repairs its message describes. The focused four-file test run yielded 18 pass,
2 fail; after the CVO server was stopped and port 5995 had zero listeners, the full suite
yielded 648 pass, 27 skip, 2 fail. CVO did not run the generator into the shared tree.
This is a committed-output omission, not an accusation that the worker's uncommitted
regeneration never succeeded. W25-S1 remains OPEN until the outputs land and survive a
git-object/fresh-checkout check. The prior W31-S1 regex disposition remains correct.

## Evidence and limits

Co-committed `IRPT_FNTEND_ROUND13_CLASSIFIER_20260922.mjs` evaluates exact source bytes;
run it from `portal/`. `IRPT_FNTEND_ROUND13_PROBES_20260922.mjs` runs from the workspace
against an explicitly started local Vite server on port 5995. Its final route interceptor
serves static fixtures and auth identity, aborts unmatched API/external requests, and reads
the actual DOM. All browser product evidence is FIXTURE-FED, not live-backend evidence.
The first exploratory version allowed unmatched same-origin requests through the dev proxy;
one unrelated advisor-intelligence request failed ECONNRESET. It supplied no grade evidence.
The retained measurements are from the corrected blocked-network run.

Probe cleanup was imperfect: earlier exploratory runs were interrupted after stalled closes;
the final run retained all measurements/screenshots, then reported BROWSER_CLOSE_TIMEOUT.
This is not reported as a clean rc=0 test. The retained DOM measurements and screenshots
are the evidence, not the process exit. The owned server was stopped; port 5995 had zero
listeners, and no children remained under the three known probe Node PIDs. No portal source
or worker artifact was changed to obtain a passing result.

`IRPT_FNTEND_ROUND13_EVIDENCE_20260922/` retains measurements.json, the three inspected
CVO captures, the suite failure tail and proof census. Compiler routing returned no curated
match; `comp-find --name` located the orders/proofs. `comp-surprise` measured the channel.
Bare `to-check` was absent; the project row explicitly names `.tools/to-check.py`, which ran.
No external procedure or web source was consulted.

## Runtime and receipt correction

Read/acted on exact packet 99484; the file remained in unread during substantive review and
was moved to read with exact follow-up 99496 after the proof census and live tests. A queued
file was therefore not evidence of inactivity. The driver retest had already been reported
to CTO at 12:01:43Z by canonical receipt
`20260922T120143Z_3.0.0_SA_CVO_F_ACK_99451_99454__drive_registration_succ.md`.
The operational timer remains stopped for the separately reported cross-fabric-send defect.
No restart was attempted in this adjudication, and no midround worker/COO message was sent.

## What you should have asked but did not

A source repair and a successful in-session generator run can coexist with a failing committed
fixture set. A structurally valid proof confirms neither that omitted outputs landed nor that
a prefix classifier recognizes only declared routes. The slug carries those two distinctions
with pinned counterexamples instead of extending the worker's PASS labels.

-- 3.0.0_SA_CVO~F
