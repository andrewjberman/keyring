# Model Overlay independent acceptance matrix

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO~M`. Prepared September 22, 2026, approximately 4:50 PM Eastern.
Scope: Andrew's direct P/M/Y completion assignment; paired implementer `2.0.0_SA_COO~M`.
This records baseline findings, R1-R3 closure at `eeffdc9a5b`, and bounded holdings selection/release acceptance at `aefcfb6541` below. It is not a completed-product or deployed E2E verdict.

## Authority and baseline

Authority: CTO `IRPT_MVP_COMPLETION_20260922/{AUTHORITY,CONTRACT,CVO_M,COO_M}.md` at `9b99dc12cd8d842e2d92e332ed1b07f36fd1b062`; CONTRACT v1.1. Read all six desktop product briefs; folder 06 equals the repository SmartX brief, SHA256 `31299F948C87A51A59F7147DBD962706773C005D1FF206A0DF6278F34462C112`.

Current coordination authority, read September 22 at approximately 5:01 PM Eastern: CONTRACT v1.2 and OVERSIGHT.md at `4688c59ef2`. This update preserves the baseline observations and every candidate NOT_EVALUATED grade below.

Measured baseline:

| Surface | Observation |
|---|---|
| Workspace | CLOUD, HEAD `9b99dc12cd8d842e2d92e332ed1b07f36fd1b062`; shared tree contains other seats' changes and staged backend L8 evidence |
| Portal | DEV, HEAD `7dd3d067a17ee00b878ecfceff23c557649a2331`; tracked-status output empty at observation |
| Origin CLOUD | `b2b2f0f4c1b6863f04f4715378fd03a23faa0d7c`, measured with `git ls-remote` |
| Origin portal DEV | `b3d5f59b4534eb653105f9bedc9e178384111c9f`, measured with `git -C portal ls-remote` |
| Builder bytes tested | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, SHA256 `CE063C4188C52D1A1ED28D9BE607AE548E5DE0BA99E6D21B9DD57953480E9B29` |
| Runtime | Canonical status oracle exit 0, all nine checks GREEN; heartbeat 35016, bridge 35176, detector 28664; thread `01a0cadc-1d11-7272-93f0-d69fabaace02` |
| Sequence | IRPT_BCKEND PLACED stage 0, no project flags; this assignment preserves the separate B/F progression hold |
| Push state | LOCAL. This seat has not pushed. |

At baseline, no completed candidate, deployed candidate pin, fresh account/position census, or live browser trace had been delivered. The later bounded source candidate is reviewed below; deployed pins, full census and browser evidence remain outstanding. Historical cloud measurements in the briefs remain historical evidence.

## Reproduced baseline failures

Command: `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/baseline_math_probe.py`.
Output: adjacent `baseline_math_probe.json`. Probe copied from CRO's cited runtime evidence, formatted to pass the repository's Python gate, and independently rerun against the measured builder bytes with identical observations. It AST-extracts actual builder functions and substitutes synthetic readers/identity helpers. Zero network calls; exit 0 means probe execution succeeded, not product acceptance.

| Case | Independent input denominator | Observed | Baseline verdict / remedy |
|---|---|---|---|
| 49F missing model | One account, known custody/allocation value $100 | Two account nodes, one unique account ID, root sum $200; one model child despite missing assignment | FAIL M2/M3. Count custody contribution once and retain unresolved membership; no fabricated model child. |
| INF shared portfolio | Two custody accounts $70 + $50; one portfolio $100 managed + $20 excluded | Account roots $100 + $100; each root has $120 children | FAIL M2/M3. Preserve account custody values and supported allocation grain without copying portfolio totals to each account. |
| COT denominator | Two accounts $100 + $300; selected known total $400 | Model total weights 1.0 and .75; expected .25 and .75; zero security nodes | FAIL M3. Compute denominator over the complete selected set, separately from parent weights. Security coverage requires further proof. |

These three cases establish code defects, not the dollar size of customer impact. AST isolation does not establish full-module import, packaging, handler, source completeness, or deployed behavior. The baseline findings are P1 completion blockers, not an instruction to halt independent repair work.

## Candidate acceptance matrix

Every candidate result must be PASS, FAIL, or NOT_EVALUATED, with workspace and portal pins, environment/deployed digest when applicable, command/trace path, expected and observed values, tested numerator/declared denominator, source revisions, limitations and exact remedy. Baseline columns below are deliberately separate from the future candidate grade.

| ID | Independent proof and controls required | Denominator / evidence required | Baseline | Candidate |
|---|---|---|---|---|
| M1 Population | Enumerate custody before any model join; include modeled, entirely non-model, mixed, zero, closed and missing-input accounts; unknown value stays unknown; measure source completeness/freshness. | Per firm full account census and unique position census, represented/excluded-with-reason/missing counts; known value plus unknown-value counts; source completion revisions and clocks. | NOT_EVALUATED | NOT_EVALUATED overall; bounded INF unknown/zero/duplicate controls PASS at eeffdc9, closing R3 |
| M2 Identity/grain | Unique account and position contribution; multiple SmartX allocations; shared Eclipse portfolios; missing assignment; model vs target vs actual basis and membership grain explicit. | Identity collision and contribution ledger over independently enumerated custody; synthetic probes plus actual source cases; no parent-and-child double count. | FAIL: 49F/INF probe | NOT_EVALUATED |
| M3 Economics | Model + confirmed non-model + unresolved known value equals independently enumerated custody; selected and parent denominators; signed/cash/zero/unknown/multi-currency handling; distinct custody/overlay clocks. | All selected accounts and positions; independent sums by firm/account/relationship/selection/currency; known three-case regressions and additional adversarial cases. No unexplained currency aggregation. | FAIL: all three probes | NOT_EVALUATED overall; bounded account/nested partition and release controls PASS at eeffdc9, closing R1/R2; original three regressions pass |
| M4 Publication | Gold Parquet history -> accepted bounded Platinum -> one complete manifest; same-day corrections unique; failed schema/reconciliation/incomplete source or partial write does not advance current pointer; prior accepted revision is explicitly stale. | Pre/post pointer object versions, Gold/Platinum hashes/revisions, acceptance receipt, injected failure outcomes and retry/concurrent publication evidence. | NOT_EVALUATED | NOT_EVALUATED |
| M5 Scope/API | Actual grant loader and API event; resolve exact account-set reference; single/relationship/subset; missing mapping fails explicitly; cross-firm/revoked/forged scope negatives; scope filtering creates no fictitious unresolved value. | Paired browser request/event/handler/response evidence with selected members vs permitted members, entitlement/directory revisions and canonical/provider IDs; zero unintended accounts. | NOT_EVALUATED; source shows `_no_grant` and permitted-set projection | NOT_EVALUATED overall; bounded exact saved subset/current loaders/release and warm refusals PASS at aefcfb6541; browser/schema/package integration outstanding |
| M6 UI | First-screen dollars/weights for three attribution buckets; all selected root accounts accessible; complete account/security drill where supported; honest unavailable granularity; source clocks, partial coverage, refresh/reopen retain exact revision. | Mounted UI trace through real wire adapter; account/position counts and totals matched to source/response; signed/invalid-denominator table fallback; no dropped clocks or coverage. | NOT_EVALUATED | NOT_EVALUATED |
| M7 Three-firm E2E | Fresh 49F SmartX, Cottonwood BD Rebalancer, Inflection Eclipse overlay joined to full custody; modeled/non-model/mixed/missing mapping/multi-sleeve/shared portfolio/subset/signed-cash cases. | Coverage grid per firm; actual source -> accepted Gold -> Platinum manifest -> deployed API -> browser trace with environment and revision identities. Three firms required; historical QA or fixtures insufficient. | NOT_EVALUATED | NOT_EVALUATED |
| S1 Selection/access | Selected-set fingerprint distinct from permitted set; server-owned crosswalk and current grants; no broadening on missing mapping; prospect firm/advisor ownership without fabricated client IDs; access rechecked on retrieval/download. | Shared M/P/Y producer-consumer examples and real request tests; dated account/allocation/model and BD crosswalk, model changes/sleeve closures/non-model/cash cases; pinned revisions. | NOT_EVALUATED | NOT_EVALUATED overall; bounded holdings selection/release controls PASS at aefcfb6541; cross-consumer/prospect/export/dated crosswalk proof outstanding |
| S2 Accepted data | Independent full census and unique actual positions; explicit unknowns and supported membership; correct selected weights; reproducible accepted Gold/Platinum revision set. | M1-M4 evidence plus Y's consumed positions artifact; actual custody vs target basis and all rows reconciled/dispositioned. | FAIL for baseline builder grain/economics only | NOT_EVALUATED overall; measured R1-R3 residuals closed at eeffdc9; accepted-source chain remains unevaluated |
| S5 HTTP/UI | Actual browser serialization through actual entry and response adapter; availability, units, selection, source dates, coverage and revision survive every boundary; stale/partial/unavailable negatives. | Paired browser/HTTP/handler/adapter/render artifacts for M; consumers P/Y confirm same shared semantics at the integrated pin. | NOT_EVALUATED | NOT_EVALUATED |
| S7 Storage | Canonical registry/builder addresses match actual readers/writers; firm Gold/Platinum long-form buckets; reporting-only private shared-store policy is explicit; all readers/writers cut over together. | Concrete naming families and policy record; IAM/IaC/build pins; deployed environment destinations and protected object versions; no global relabel, alternate bucket concatenation or standing dual write. | NOT_EVALUATED | NOT_EVALUATED |

## First vertical proof and handoff requirements

First proof: select one investor subset from the real header carrier, resolve canonical account membership and current grants, enumerate unique actual custody, produce reconciled attribution at supported grain, publish an accepted revision, serve exactly that subset through the actual entry, and compare the mounted UI's dollars/weights/accounts/securities/clocks to the accepted data. Start offline where needed; label deployed and live evidence separately. Repeat the firm/case grid before M7 PASS.

COO~M handoff must name candidate workspace/portal commits and worktree, final accepted B/F source pins incorporated, exact test commands and results, S1/S2 schema/examples, full census and source revision manifests, measured deployment environment/digests, and remaining explicit operating gates. A success count without its coverage denominator is insufficient. Candidate changes require a new pin and re-notification.

For CVO~P: share selected-set and dated SmartX/BD crosswalk evidence, current entitlement/retrieval controls and naming/storage proof. 49F performance is SmartX primary, BD separate verification; present model assignment does not prove historical performance ownership. P owns performance/report/export grading.

For CVO~Y: share exact selected custody positions, accepted revision and row reconciliation; no model target substitution or parent/child duplication; preserve prospect firm/advisor ownership. Y owns normalization, generation and recovery grading.

## Coordination defect — CLOSED on actual delivery

Canonical `codex-send.ps1` refused CVO~M -> COO~M under the global L8 CVO-only-to-CTO gate, contradicting this assignment's CONTRACT sections 6/7. Nothing was delivered to COO~M by that attempt. Reported to CTO with requested relay to COO~M and CVO~P/~Y; no direct-file or alternate transport bypass. First CTO note incorrectly said the finding was routed; the immediate correction explicitly records refusal. Independent evidence preparation continues.

CTO repaired the exact P/M/Y exception at `4688c59ef2`. Retried actual coordination through `codex-send.ps1`, using IRPT subjects and the full governing CONTRACT.md path. All three returned successful filesystem delivery to their canonical nested inboxes; no force or alternate transport used:

| Recipient | Actual receipt filename |
|---|---|
| COO~M | `20260922T210126Z_3.0.0_SA_CVO_M_IRPT_M__baseline_failures_and_candidate_.md` |
| CVO~Y | `20260922T210127Z_3.0.0_SA_CVO_M_IRPT_M__ACK_Y_boundary_request__pinned_b.md` |
| CVO~P | `20260922T210128Z_3.0.0_SA_CVO_M_IRPT_M__ACK_P_selection_export_request__.md` |

CTO received the receipt report as `20260922T210147Z_3.0.0_SA_CVO_M_IRPT_M__real_peer_delivery_verified__coo.md`. Delivery is measured; it does not assert recipients have accepted candidate evidence. COO~M now has the baseline findings and exact handoff requirements directly. P/Y requests for selected-set, current entitlement/revocation, unique accepted custody and dated crosswalk evidence were acknowledged, with this matrix/probe at `dfa1121b17`. Candidate producer examples remain owed by the implementation owner, then independently reviewed here and consumed by P/Y. P's query-date/set-reference findings and Y's six-field submit loss are peer-reported baseline evidence, not regraded by this reviewer.

## Accepted backend transition and remaining integration prerequisites

Read the complete backend round-18 L8 compile at `2506c70874`, including final chain merge `4e1091f1e7`. CTO reports B's write claims released and no pending worker branch/worktree. Preserve V3 render_auth/index, V2 index, `_scope/resolve`, `_authz/enforce`, and R17 identity/mint semantics in candidate review. The reported 41/41 assertions are not this seat's independent rerun. Old-round L9/L10 remains with the assigned B reviewer; this M seat does not inherit that adjudication.

The assembled chain does not re-prove item (e)'s V1 verifier; item (f)'s human path is partial/structural behind NETWORK FORBIDDEN; item (g)'s deploy IAM is outside offline coverage. These limits and the pending L9 prerequisite remain binding before render key provisioning/deployment. No old canonical progression follows from this handoff. Final accepted frontend DEV pin and write-claim release were still pending in CTO's update; integrated acceptance must incorporate that final evidence, not silently retain the initial portal baseline.

### Final frontend handoff received — September 22, approximately 5:24 PM Eastern

The preceding pending-frontend state is superseded by CTO's exact delivery `20260922T212325Z_1.0.0_SA_CTO_IRPT_final_F_code_baseline_8e6e2e38__cla.md`. F code handoff is portal DEV `8e6e2e38cc299c4415d42b0fe627edc50ec35e1b`, all old F write claims released. Independently measured portal HEAD equals that full hash, tracked status is clean, and `git merge-base --is-ancestor` returns 0 for that pin. B `2506c70874` and chain `4e1091f1e7` each return ancestor rc=0 against measured workspace HEAD `f82fee6aadbc91a7ffacaf87f7f4c8d1d5dd5094`. Candidate integrations must preserve these and any later accepted changes. This is code inheritance, not a deployed or final independent acceptance grade.

CTO identifies existing App/ProtectedRoute render-claim handling as inherited implementation; payload decoding is not server signature verification. P owns residual `IRPT_FNTEND-W39-S2` fixture corrections (23 other committed fixture files, reported by CTO), with relevant M/Y consumer examples independently checked at candidate handoff. No per-cell frontend test counts are summed into a final-head result. F retains pending administrative proof/status drains; they do not block this functional baseline. B L9/provisioning prerequisite and old canonical hold remain.

Read full P `INTERFACES.md` at `aacb609834`: mandatory current authorization callback, entire-selected-set access, separate prospect owner, immutable receipts, registered destination callbacks, and preserved report envelope. CTO reports primitive candidate `70598ece96498d639b0fb12104ffe9fd4b0d5718` with 19 offline tests; this reviewer has not regraded those tests. M still owes actual verified principal/owner and reauthorization producer examples, selected-set resolution, dated crosswalk and canonical artifact destinations. Published interface and primitive availability do not complete S1/S2/S4/S7 or product E2E. P's shared fixture integration and repository testing remain P-owned; M verifies the relevant producer/consumer cases when delivered.

Push state remains LOCAL; fresh `git ls-remote` observations at this handoff are origin CLOUD `aacb60983400262ffe7ce3406b76982690075e55` and portal DEV `b3d5f59b4534eb653105f9bedc9e178384111c9f`. No push by this seat.

### S7 conditional ruling and B verdict update — September 22, approximately 5:29 PM Eastern

Read RULINGS.md IRPT-S7-01 and OVERSIGHT.md at `bcd38bba00`, following exact CTO delivery `20260922T212727Z_1.0.0_SA_CTO_IRPT_S7_ruling_committed_bcd38bba00__act.md`. Decider/condition owner is CTO under Andrew's session delegation at `ecf350639a`; this is not a claim that Andrew personally approved this bucket. The ruling is a decision record, not the canonical exception register. COO~M issues the bounded order, CRO records it in `infra/logic/06_CONFORMANCE_LEDGER.md` section 6, M implements registry/builder, P implements repository/provisioning/retention and Y consumes. This reviewer owns none of those implementation/registration acts.

S7 candidate evidence must now satisfy all of the following conditions, in addition to the existing matrix row:

1. Return canonical exception ID and committed section-6 carrier, plus the committed M proposal. Prove no writable destination is returned before both canonical registration and enforcement exist; a ruling pin alone is insufficient.
2. Admit exactly three firms (`49financial`, `cottonwood`, `inflection`) and exactly eleven families: ORIGINAL_CSV, NORMALIZED_PORTFOLIO, REQUEST_COMPOSITION, ORIGINAL_VENDOR_PDF, EXTRACTION_EVIDENCE, PERFORMANCE, ANALYSIS, EXPORT_BUNDLE, EXPORT_PDF, EXPORT_RECEIPT, SELECTED_ACCOUNTS. PERFORMANCE/ANALYSIS are bounded platinum JSON reports; the other nine are state families. Prove unknown firm/family and invalid server-owned identifiers are refused.
3. Show canonical grammar, firm identity, server-only validated IDs/digests/keys and unchanged default destinations. Reject browser bucket/key inputs and alternate fallback destinations. Canonical custody/directory/holdings/model Gold/Platinum stay in long-form firm buckets; no global relabel or second process-state machine.
4. Exercise real producer/consumer authorization for exact selected-account or prospect ownership before and after retrieval, cross-firm/revocation negatives, immutable accepted object version/hash verification, and inaccessible interrupted publication. Test these on the candidate modules and registered policy revision, not only a naming example.
5. P supplies concrete retention/expiry for each of eleven families and least-privilege IAM/IaC before provisioning or live writes. Inspect the effective settings at live acceptance; no indefinite-retention assumption or cleanup/deletion authority follows from placement approval.
6. Every affected reader/writer uses the same policy revision. Supply a bounded coordinated cutover and naming-owner review; no standing dual write or estate-wide migration. If conditions cease to hold, affected publication/retrieval must disable as appropriate and route to CTO without silent fallback/broadening. Test revision disagreement and revoked-condition cases.

No canonical exception carrier or enforcing reader/writer evidence was delivered in this message; S7 and candidate product grades remain NOT_EVALUATED. OVERSIGHT reports M source commit `33e630885f` after grant consumption `96b50ca18e`; that progress report alone is not an accepted S7/full-product candidate.

The earlier pending B judgment statements are superseded: CTO's current OVERSIGHT reports independent B slug `f82fee6aad`, **R118-AC5 FAIL / render contract NOT PROVEN**, received and parked. It also reports AC4 28/29 plus V1 import failure and enforcer bundle/tenant/revision/pinning findings. These are the B review's reported verdict, not a fresh M rerun. Keep the failed render prerequisite visible; inherited source ancestry and S7 approval do not authorize render key provisioning/deployment or restart the held B/F flow.

## Bounded source review: 81785d9ae3, September 22 at 21:43 UTC

**Verdict: submitted corrected cases PASS; economic acceptance remains FAIL on the three measured residuals below.** This is the requested independent bounded review, not a rejection of unclaimed complete-product work and not a deployed failure measurement.

Sender/body: COO `2.0.0_SA_COO~M`, exact message `20260922T213351Z_2.0.0_SA_COO_M_IRPT_M__first_source_review_candidate_81.md`, requests independent grading of the corrected cases at `81785d9ae3`, includes selection/store pin `33e630885f`, and expressly excludes subsequent uncommitted Prospect Entry work. Authority remains the direct assignment's `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`. Review acts are assigned to this seat; the notification alone is not a Go.

Measured full candidate: `81785d9ae3ee071a5319a5cad87a1ada3212fc60`. A separate linked checkout at `C:/Users/AndrewBerman/Desktop/ajb_irpt_cvo_m_review`, branch `codex/irpt-m-review-81785d9`, was created from that exact pin because the implementer's checkout contained subsequent uncommitted changes. HEAD matched and tracked status was empty before and after the review. No implementation files were edited. This supersedes the preparatory candidate statuses above only for the explicitly tested cases.

Source byte hashes (SHA256): builder `BC25CF8E2DDE1AA0107FD2E921859F01CDA2A03BE8B72AAE85F07843182CE033`; served projection `8804FC94199FDC5901595580E76FA277BE27095038FA2AC200B19B3EB8B2E3E8`. Tests import the complete actual modules, unlike the earlier AST baseline probe.

### Independent reruns of the submitted suites

All commands below ran from the pinned review checkout, in separate Python processes with `AWS_EC2_METADATA_DISABLED=true`. These are synthetic/offline suite results, with no deployed digest, vendor data, live AWS evidence or browser trace.

| Command | Independent observed result |
|---|---|
| `python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py data/assets/scripts/gold/investor_reporting/tests/test_holdouts.py data/assets/scripts/gold/investor_reporting/tests/test_economic_regressions.py -q` | 41 passed in 3.16s |
| `python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q` | 45 passed in 2.18s |
| `python -m pytest infra/aws/lambda/investor-reporting/_authz/tests -q` | 144 passed in 24.90s |
| `python -m pytest infra/aws/lambda/investor-reporting/_scope/tests -q` | 68 passed, 12 subtests passed in 4.24s |

Total: 298 tests and 12 subtests passed at one exact pin. Local raw outputs: `.runtime/codex-seats/3.0.0_SA_CVO~M/review_81785d9_{builder,holdings,authz,scope}.txt`. This count is not a completeness denominator for M1-M7/S1-S7.

Bounded PASS credit: the 49F unassigned $100 case now has one $100 root and an unresolved child; two allocations $40/$60 share one $100 root with unique children and .4/.6 weights; missing SmartX valuation raises; shared INF portfolio custody $70/$50 remains $120 with unresolved attribution rather than repeated portfolio values; COT $100/$300 target weights are .25/.75. The pre-publication guard refuses the two injected false schema/reconciliation flags before the mocked landing function runs. That last test does not independently establish real source completeness, immutable publication, rollback or accepted manifests.

The submitted projection tests also pass selected weights/fingerprint, no excluded-balance remainder, duplicate/non-finite/unknown value refusals, preservation of false source reconciliation, direct one-account overstatement, missing/unpermitted selection and TARGET-only unresolved value. Current-loader rotation and entitlement-map revision tests pass. Selection/store/prospect primitive tests pass their offline cases; actual HTTP selection wiring, independently verified edge identity, prospect Entry and durable live storage are not established by these counts.

### Additional actual-module probes and required remedies

All amounts below are synthetic USD. The projection fixtures deliberately begin with a true source reconciliation flag, as does the existing candidate overstatement test, to test whether serving detects a contradictory hierarchy. They use the candidate's existing fixture constructors and real ID normalizer, mutate economic values independently, and call both real `snapshot.project` and the real in-process `register_routes`/Enforcer route. No copied projection or AST substitution is involved.

| Probe | Expected | Observed | Grade |
|---|---|---|---|
| Balanced root100 -> assigned model100 | True reconciliation, zero remainder | True; schema valid; guarded route Served/true | PASS control |
| Root100 -> direct assigned model120 | Reconciliation false | Before100, after120, difference20, false; schema valid; guarded route Served/false | PASS control |
| Two roots100 each -> direct assigned models80 and120 | Per-account deficits/excesses cannot cancel into acceptance | Before200, after200, difference0, **true**, remainder0; schema valid; guarded route **Served/true** | FAIL M3/S2, `M-817-R1` |
| Root100 -> observed sleeve100 -> assigned model200 | Nested economic contradiction must be detected | Before100, after100, difference0, **true**, remainder0; schema valid; guarded route **Served/true** | FAIL M3/S2, `M-817-R2` |
| INF custody account with `current_value=None`, no portfolio assignment | Unknown custody stays explicit or build is unavailable | Actual `build_inf` emits an ACCOUNT with **0.0** | FAIL M1/S2 residual, `M-817-R3` |

`M-817-R1`: `infra/aws/lambda/investor-reporting/holdings/snapshot.py:233` accumulates direct-child amounts across all accounts, and line 247 checks only their combined difference. Require account-level conservation before aggregate acceptance; a deficit on one account cannot net against another's excess. Add a two-account discriminator and retain the passing single-account control.

`M-817-R2`: the same module at line 236 reads only immediate account children. Require basis-aware checks at each relationship represented as an economic partition; a correctly valued sleeve cannot certify a contradictory model below it. Do not sum parents and descendants into one total or treat TARGET as actual. Define any non-partition relationship explicitly instead of silently marking it reconciled. The bad probe passed the published schema, so schema validation alone does not catch it.

`M-817-R3`: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:836` maps missing `current_value` to `0.0` while building custody-only/holdout accounts. Preserve the unknown count/value status or fail the acceptance gate. This is a residual on the already acknowledged census/unknown-input gap, not a claim that the candidate newly introduced it or claimed full census completion. The assigned/matched account path's new missing-value refusal does not cover this path.

The first probe attempt omitted a mock for the date-partition reader and stopped on `None.get_paginator`; it produced no verdict and made no network call. After adding that transport-boundary mock, the full probe ran exit 0 and produced all five observations above. Exit 0 means the observational probe executed, not product acceptance. A subsequent targeted extension confirmed both false positives survive the guarded route. No full-suite repetition was needed because candidate source did not change.

### Acceptance boundary and handoff

M1/M3/S2 FAIL above is limited to measured assertions. M2's corrected regression cases receive PASS credit but the whole-row custody/position ledger remains NOT_EVALUATED. M4/M5/S1 have bounded test credit only; M6/M7/S5, three-firm fresh source completeness, actual positions, immutable accepted Gold/Platinum revisions, same-day corrections, request/UI integration, dated SmartX-primary/BD-verification crosswalks and live evidence remain NOT_EVALUATED. S7 remains NOT_EVALUATED under IRPT-S7-01 and requires the canonical exception carrier and enforcing controls. No deployment/provisioning permission or old B/F progression follows from this review.

COO~M received the measured residuals immediately via canonical receipt `20260922T214346Z_3.0.0_SA_CVO_M_IRPT_M__candidate_81785d9_independent_re.md`. In exact reply `20260922T214638Z_2.0.0_SA_COO_M_IRPT_M__residual_reconciliation_defects_.md`, the implementer acknowledged all three findings, is adding per-account/descendant checks and refusing the INF unknown path, and requested this durable review pin. Those are planned remedies, not reviewed fixes. The next review handoff must name a new immutable candidate pin, remedies/tests for R1-R3 and the remaining actual entry/source/consumer evidence. P/Y should not treat the corrected synthetic cases as an accepted full-custody artifact. Keep review and implementation ownership separate.

Related peer evidence, not independently regraded here: exact P message `20260922T214529Z_3.0.0_SA_CVO_P_IRPT_P__f7f5_release-time_revocation_fin.md` reports R-P06 P1 at actual performance entry candidate `f7f5d22a76`: supplied 14 PASS; added 5 PASS/1 FAIL. P revoked A1 ownership and changed entitlement revision during provider execution; the fresh request still returned READY/data, while the subsequent request refused before the provider. P sent the finding to COO~P and CTO and asks that shared-guard work coordinate M ownership. Fresh loaders passing at `81785d9ae3` do not establish release-time reauthorization. M5/S1 remain open for actual post-compute/retrieval and cached-path revocation controls. Relay this exact pin/finding to COO~M; implementation and regression proof belong to the source owners, not this reviewer.

Push state: this review is LOCAL; no push by this seat. Origin CLOUD was freshly measured as `b333db1b4865619909c916741775084396e0b7d1` during this review. The review checkout remains a pinned evidence checkout, not an integration branch.

The reproducible full-module probe is embedded at the end of this file so the review does not depend on an untracked runtime file. Original local probe SHA256: `18699B64240E7EB7289AE34A6249CD6C626F99DAC1D9BA6A761EF3D2FF4F79A0`. Save that block as a `.py` file outside the candidate checkout and invoke `python <probe.py> <absolute-pinned-checkout>`. Its printed JSON includes observed values, schema results and guarded-route outcomes.

## S7-03 acceptance update: 3c55f37800, September 22 at 21:49 UTC

Read exact inbox `20260922T214734Z_1.0.0_SA_CTO_IRPT_S7-03__committed_retention_and_twel.md`, sender CTO, and the complete 68-line RULINGS.md at `3c55f37800`. Requested acts: COO~M amends the existing CRO register order; CRO amends the sole canonical ledger; M/P implement one coherent policy; CVOs independently prove readers/writers and negative controls. This seat updates review criteria and reviews delivered evidence; it does not issue M's order or perform P's provisioning work.

The following supersedes the earlier eleven-family-only candidate acceptance condition, without certifying that the newly allowed family is already registered or writable:

1. Exactly **twelve families: ten state/two platinum**, adding only `PERFORMANCE_SOURCE_EVIDENCE`, state family/table `performance_source_evidence`. Three firms and unchanged long-form custody/directory/holdings/model destinations remain required. Unknown or unregistered family/policy revisions remain non-writable. The notification reports original CRO X10 at `25a9465c7d` is eleven-family only and its C1-C4 proof VALID; this reviewer has not independently regraded that carrier. Require the committed bounded amendment and actual canonical X10 revision covering S7-03 before treating the twelfth family as registered.
2. Require committed preservation of P's reviewed STORAGE_PROVISIONING_PLAN.md (CTO-reported SHA256 `2a21e574adcc4e1e62d47b643df7c2de85085ad17e317a907ece31d01494db86`). `irpt-retention-v1`: unreferenced inputs/selection references 30 days; unfinished exports 7 days; accepted artifact ceilings 2555 days from original creation, limited by the earliest required dependency. Selection references stay at 30 days; accepted reports carry frozen members/revisions plus fresh authorization. These are product-policy values, not a legal determination.
3. Actual repository tests must use a controlled clock at expiry boundaries, expired promotion, concurrent promotion/expiry, and publication ordering. Promotion is conditional and precedes publication. Reads/retries/copies/later report creation cannot renew the creation ceiling or revive expired evidence. Require refusal when a required dependency has expired, including already accepted/exported chains. Logical expiry alone does not establish physical disposal.
4. Preserve request-scoped original SmartX/Black Diamond/Orion performance response bytes and a separately identified redacted request/response receipt. Use server-generated opaque identifiers and immutable original-byte hashes. Negative controls must prove no credentials/cookies/authentication headers are persisted; safely refuse or quarantine without persisting sensitive response bytes when they cannot meet the rule. Never modify bytes while claiming their original-source hash. This is not a general vendor archive or custody-processing replacement.
5. Require M registry/builder, P provider writer/retention and each affected consumer to use the same accepted revision. Preserve existing audited IRPT-S7-02 issuance boundaries, a single canonical exception carrier/history and actual entry recount. A ruling, family constant or proposal alone does not unlock writes.
6. The least-privilege role matrix is implementation direction only. Require concrete IAM/KMS context/DynamoDB LeadingKeys/versioned S3 positive and negative evidence. Source-map grant `a36b72db57` is exact-file and IRPT-member bounded: non-IRPT equality plus actual flat-package imports/entry proof for M's consumed interfaces remain necessary. Do not infer runtime permission from the broader file-granularity ownership hook. Missing prescribed `.tools/terraform.exe` is a repository provisioning defect, not permission to substitute tools or call syntax checks a plan.

S7 stays **NOT_EVALUATED**. Physical disposal stays **OPEN** pending a bounded reference-aware design and separately authorized execution. No provisioning, vendor execution, deployment, lifecycle activation, deletion or render-gate lift follows from S7-03. No criterion receives PASS from the ruling itself. CTO's exact message is information/instructions within the existing review contract, not independent authorization for live action.

## Independent R1-R3 retest: eeffdc9a5b, September 22 at 21:58 UTC

**R1, R2 and R3: PASS / CLOSED at exact candidate `eeffdc9a5b02db9cc77e4e0fab303fddffeeaea8`.** This supersedes their FAIL status at `81785d9ae3`; the earlier evidence remains valid for that earlier pin. Whole M1/M3/S2 rows remain NOT_EVALUATED because these bounded fixes do not establish full source census, complete position/security/pricing evidence, accepted storage or integrated UI behavior.

Exact request `20260922T215518Z_2.0.0_SA_COO_M_IRPT_M__R1-R3_remedy_candidate_eeffdc9a5.md` is from COO~M and asks for independent rerun of these residuals under the existing completion CONTRACT. ACK sent before review. The existing reviewer-owned checkout was verified clean and switched to detached `eeffdc9a5b02db9cc77e4e0fab303fddffeeaea8`; tracked status was empty after all runs. No implementation edits. No uncommitted implementer changes were tested.

| Independent command, from the pinned checkout | Observed result |
|---|---|
| `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q` | 85 passed in 6.98s |
| `python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q` | 50 passed in 0.34s |
| `python <retest_eeffdc9.py> <absolute-pinned-checkout>` | 15/15 independent cases PASS; exit 0; empty failures list |

The complete retest script is embedded in the final appendix. Local script/raw JSON and suite logs are `.runtime/codex-seats/3.0.0_SA_CVO~M/retest_eeffdc9.py`, `.json`, `_builder.txt`, `_holdings.txt`. The script imports actual modules and the existing fixture/transport helpers; it does not copy the reconciliation implementation. The original economic inputs are preserved, with exception capture added because the repaired route now refuses. Actual holdings `entry.lambda_handler` is resolved through the real route/source-map loader; only directory/ownership storage and snapshot transport are synthetic. No vendor/AWS/browser/deployment evidence is claimed.

| Case denominator | Projection / runner / route / actual Entry observations | Grade |
|---|---|---|
| R1: two roots100, assigned children80/120 | Projection false; runner false; guarded route raises SnapshotUnavailable; actual Entry returns `NOT_READY` without data | PASS / CLOSED |
| R2: root100, observed sleeve100, assigned model200 | Same false/refusal outcomes at all four boundaries | PASS / CLOSED |
| Nested under-attribution model80 beneath sleeve100 | Same false/refusal outcomes | PASS negative control |
| Direct model120 beneath root100 | Same false/refusal outcomes | PASS retained control |
| Balanced direct100; nested60+40 beneath100; signed120-20 beneath100; observed zero root | All four cases reconcile in projection and runner, are Served by the guarded route, and succeed through actual Entry | PASS positive controls |
| Missing source acceptance flag on a balanced root100 | Projection false; guarded route refuses; actual Entry `NOT_READY` without data. Runner independently computes true monetary balance, which is not a source-acceptance certificate | PASS negative control |
| R3 custody-only INF values None, NaN, infinity, boolean | All four raise explicit unknown-value refusal; no zero-valued account output | PASS / CLOSED |
| Custody-only INF observed zero; duplicate custody identity | Zero emits exactly one ACCOUNT0; duplicate raises identity-ambiguity refusal | PASS positive/negative controls |

The remedy independently checks each non-TARGET parent/basis partition, and both guarded-route and actual-entry boundaries now require accepted reconciliation. The runner also rejects the measured contradictory partitions. INF's custody enumeration rejects the measured unknown/nonfinite/bool and duplicate cases while retaining observed zero. These observations do not certify every possible relationship/basis combination, multi-currency treatment or full source population. No new defect was observed within this bounded retest.

SHA256 measured bytes: builder `83A24247FC2068CC88AFCCEA829F6B58193BB8245C4D342D0DEC5079A2EBE3A7`; projection `F0A1BF6097FE3ECF10BA6420AE17433C73A330ED881A3FE2B4E22D0A0369C272`; holdings entry `3684AF9CC8B29B8030B1A0CB3E66A24D9A39EAA8C1123BF26CE47F055E728408`; retest script `87AA4BD64DA2DAA5C00FEF81375242CB4835453CB8FBC331D9D6F8EFD56924F4`.

Remaining next M handoff is actual saved-selection resolution and before/after current grants at holdings Entry, as the implementer explicitly states. The exact candidate also contains other prospect/directory/selection changes; this review grades only the requested R1-R3 and exercised holdings dependencies, not those other surfaces in full. Prior 81785d9 authz/scope counts are not recertified at this new pin. S7 remains NOT_EVALUATED under S7-03; physical disposal and the independent render prerequisite remain open/held as recorded above.

Related peer update, not independently rerun here: CVO~P exact message `20260922T215404Z_3.0.0_SA_CVO_P_IRPT_P__R-P06_entry-local_closure_c29662.md` reports R-P06 closed at performance entry `8b913a9414`, review `c2966279ae`, reviewer6/6 and supplied19/19 PASS. This supersedes the earlier P entry-local defect report for that exact repaired entry only. It does not grade generic shared fresh/cache behavior or M holdings release-time authorization.

Review remains LOCAL; this seat did not push. Fresh origin CLOUD measurement during the retest: `b333db1b4865619909c916741775084396e0b7d1`. Source fixes are the implementer's; this reviewer commits only this acceptance/evidence carrier and routes the immutable review pin to COO~M, CTO and CVO~P/~Y.

## Bounded holdings selection/release review: aefcfb6541, September 22 at 22:06 UTC

**PASS for the declared holdings Entry selection/release cases at exact `aefcfb6541fa1d6c0c8b31f2693117718a65e824`.** No new defect observed in this bounded review. M5/S1 remain NOT_EVALUATED as whole product criteria; this grade does not cover integrated schema/package/UI, external edge identity, three-firm source completeness, prospect/export behavior or live storage.

Exact sender/request: COO~M, `20260922T220138Z_2.0.0_SA_COO_M_IRPT_M__exact-selection_release_review_a.md`, under the existing direct completion CONTRACT. ACK sent before work. Diff from accepted residual candidate `eeffdc9a5b` contains only holdings/entry.py and its test_entry_guarded.py. The reviewer checkout was clean, switched to detached full pin above, and remained tracked-clean after tests. R1-R3's original closure remains tied to eeffdc9a5b; builder/projection files are unchanged by this candidate. No implementation edits or candidate commit by this reviewer.

| Independent command at the isolated pin | Observed |
|---|---|
| `python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q` | 61 passed in 0.36s |
| `python <review_aefcfb.py> <absolute-pinned-checkout>` | 18/18 independently defined cases PASS, exit 0, failures=[] |

Probe is embedded in the final appendix; runtime evidence is `.runtime/codex-seats/3.0.0_SA_CVO~M/review_aefcfb.py`, `.json` and `_holdings.txt`. Entry SHA256 `D9596F250DD97EA4FAD235EBDC3322851B4A430AA9D9EDAFF9F1AAF7BF72BA44`; probe SHA256 `9496B3338F8B77F8CA16F64B02D1FA959D5978C82E57B6521C7310053F969E04`.

Unlike the submitted entry tests' dependency substitution, the independent probe keeps real `ENTRY.deps is _loaders.deps`, real `opaque_firm_for`, real grant/directory reads and content-hash entitlement revisions, real SelectionStore conditional writes/consistent reads, real selection creation/resolution, real snapshot pointer/dated read, projection, Enforcer and HTTP Entry. It substitutes only boto3 S3/DynamoDB transports with in-memory synthetic objects and configures a synthetic bucket/table. Actual transport calls must match the server-selected bucket/table/key grammar. No production access or identity-verification claim follows from synthetic trusted headers.

| Case group | Expected and measured boundary result | Count |
|---|---|---|
| Single A2; mixed assigned A1 + unassigned A3; unassigned A3; dated A1 | Exactly [A2]/$40, [A1,A3]/$107, [A3]/$7, [A1]/$100 respectively; selected fingerprint matches the retained reference; excluded account IDs absent from serialized data; one snapshot read each | 4 PASS |
| During snapshot read: revoke selected A1, change ownership content revision while preserving members, rotate directory, tamper retained members, delete retained record | After one snapshot read, actual Entry refuses `OBJECT_NOT_COVERED` with no data in all five cases | 5 PASS |
| Warm subsequent invocation after initial success: revoke A1, tamper record, rotate directory | Second request refuses `OBJECT_NOT_COVERED` with no data and without a second snapshot read | 3 PASS |
| Pre-read partial revocation of [A1,A2]; missing reference; literal account ID; injected browser snapshot | Refused without data and with zero snapshot reads; no fallback to the permitted universe or partial subset | 4 PASS |
| Foreign source firm; economically overstated source | `NOT_READY`, no data, one snapshot read | 2 PASS |

The candidate performs selection resolution before snapshot retrieval and again after projection, then requires equal retained selection/current authorization views before returning data. Warm-process tests exercise separate real HTTP invocations with the actual default `shared_cache is None`; they are not a proof of generic Enforcer cache-hit release behavior under an explicitly shared cache. The real ownership loader hash changed in the revision-only case; the probe did not merely fabricate an entitlement-revision string. Refusal data absence is asserted, not inferred from an error code.

Source code and supplied 61-test suite also cover contract-version refusal, claimed-firm swap, missing/unknown references, multiple browser scope inputs and clock/reconciliation negatives. The new independent transport-composition cases remain single-firm synthetic examples, not mounted browser or physical S3/DynamoDB evidence. No aggregate count is promoted into full M5/S1 readiness.

Next integration evidence must consume P schema `63c6b39af6` or its accepted successor, prove relevant request/response contracts and exact query/reference serialization, package required dependencies in the real flat artifact with source pins/hashes, and demonstrate configured table/IAM and current authorization at the deployed boundary when separately authorized. Accepted source census, actual positions/pricing, immutable Gold/Platinum/storage evidence and mounted UI still remain outstanding. No repeat of unchanged builder suites was needed for this Entry-only change.

The message reports amended X10 carrier `705dae3202` and documentary diff/recount validation. Record that as producer-reported documentary evidence only; this review did not inspect or regrade that carrier, nor prove the S7 reader/writer enforcement, twelve-family policy, expiry/disposal or IAM. S7 remains NOT_EVALUATED with prior S7-03 and render/live gates intact.

Review is LOCAL and no push was made. Fresh origin CLOUD observation: `b333db1b4865619909c916741775084396e0b7d1`. Route this immutable review pin to COO~M, CTO and CVO~P/~Y; the next source/interface candidate needs its own pin and evidence.

## Compiler Tools

| Tool | Result / limitation |
|---|---|
| `comp-which` startup read routing | Near tie to unrelated surfaces; suggested `comp-find`; no meaningful confidence implied. |
| `comp-find` exact contract content | 449 hits / 173,400 scanned, substantial latency and irrelevant archive hits. Used explicit required contract paths for complete reads. |
| `comp-read COO_M.md` | 25 lines / 10 sections, only 8 lines shown; completed direct full read, preserving all qualifiers. |
| `comp-which` builder context | Tied cloud-resource suggestions did not answer source-read concern; selected offered filename search. |
| `comp-find --name holdings_snapshot.py` | Two exact filename hits / 178,563 files scanned; builder and its test. |
| Canonical loader/status | Corrected six-file manifest consumed; exact serial/home/inbox preserved; readiness GREEN 9/9. |
| `sequence-check.py --project IRPT_BCKEND` | PLACED, no project flags; capacity advisory is already addressed in direct assignment authority. |
| `safe-commit.sh` initial attempt | Python lint refused the copied scratch probe's compact formatting; reformatted only this review artifact, Ruff then passed and the probe reproduced identical results. Risk reflex reported PARTIAL_OR_BLIND because its danger map was stale; this is not a clean risk-map verdict. |
| `comp-which` CONTRACT/OVERSIGHT read, follow-up | Its fallback `comp-find OVERSIGHT.md` exceeded the 90-second budget and was killed; no answer inferred. `comp-read` and complete explicit-path reads supplied the actual contract/oversight/compile contents. |

## What you should have asked but did not

Can a correct selected-set snapshot still feed the wrong historical performance ownership? Yes: present membership and dated allocation membership are different evidence. Require an allocation closure/model-change case at the M-to-P boundary, and bind the exact dated crosswalk revision to P's comparison receipt. Separately, a fully reconciled known-value subset can hide missing-value accounts; account/position completeness must accompany monetary reconciliation.

— 3.0.0_SA_CVO~M


## Reproduction appendix: candidate 81785d9ae3

```python
"""Independent synthetic review probes; import the complete pinned modules."""
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pandas as pd

root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "infra/aws/lambda/investor-reporting/holdings/tests"))
from test_snapshot import (
    A1, A2, _authz, _directory, _enforcer, _headers,
    fixture_snapshot, node, scope_for, sn,
)

observations = {}


def inspect_case(name, nodes, selected):
    source = fixture_snapshot()
    source["nodes"] = nodes
    source["attribution_holdouts"]["unassigned"] = {
        "account_count": 0, "account_ids": [],
        "value": {"value": 0, "currency": "USD"}, "basis": "OBSERVED",
        "observable": "MEASURED", "denominator": "0",
    }
    result = sn.project(source, scope_for(selected))
    routes = sn.register_routes(_enforcer(_directory(selected)), lambda request, scope: source)
    served = routes[sn.ROUTE_KEY](_authz.Request(_headers(), sn.KEY_OPERATION, "account", selected[0]))
    observations[name] = {
        "guarded_route_served": isinstance(served, _authz.Served),
        "guarded_route_reconciled": served.payload["attribution_holdouts"]["reconcile"]["reconciled"],
        "reconcile": result["attribution_holdouts"]["reconcile"],
        "coverage": result["coverage"],
        "nodes": [{"id": n["node_id"], "kind": n["node_kind"],
                   "parent": n["parent_node_id"], "value": n["amount"]["value"]}
                  for n in result["nodes"]],
        "schema": sn.validate_slice(result),
    }


inspect_case("balanced_control", [node(A1, 100), node("m1", 100, "MODEL_LEAF", A1, "ASSIGNED")], [A1])
inspect_case("single_account_overstatement", [node(A1, 100), node("m1", 120, "MODEL_LEAF", A1, "ASSIGNED")], [A1])
inspect_case("offsetting_account_errors", [
    node(A1, 100), node("m1", 80, "MODEL_LEAF", A1, "ASSIGNED"),
    node(A2, 100), node("m2", 120, "MODEL_LEAF", A2, "ASSIGNED"),
], [A1, A2])
inspect_case("nested_model_overstatement", [
    node(A1, 100), node("sleeve", 100, "SLEEVE", A1),
    node("m1", 200, "MODEL_LEAF", "sleeve", "ASSIGNED"),
], [A1])

sys.path.insert(0, str(root / "data/assets/scripts/gold/investor_reporting"))
import holdings_snapshot as hs

tables = {"accounts_v2": [{"account_id": "a", "current_value": None}]}


def read(_s3, _bucket, key):
    for name, rows in tables.items():
        if name in key:
            return pd.DataFrame(rows)
    return pd.DataFrame()


with patch.object(hs, "_read_parquet", read), \
        patch.object(hs, "_latest_date_partition", lambda *a, **k: "2026-09-21"), \
        patch.object(hs, "_latest_complete_eclipse_date", lambda *a: "2026-09-21"), \
        patch.object(hs, "_directory_account_ids", lambda *a: None):
    nodes, manifest = hs.build_inf(None, "2026-09-21")
    observations["unassigned_inf_unknown_custody"] = {
        "account_values": [n["amount"]["value"] for n in nodes if n["node_kind"] == "ACCOUNT"],
        "total_market_value": manifest.get("total_market_value"),
    }

print(json.dumps(observations, indent=2, allow_nan=False))

```


## Reproduction appendix: R1-R3 retest eeffdc9a5b

```python
"""Independent bounded R1-R3 retest of complete modules at an explicit checkout."""
import copy
import json
import os
import sys
from pathlib import Path
from unittest.mock import patch

import pandas as pd

os.environ["AWS_EC2_METADATA_DISABLED"] = "true"
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "infra/aws/lambda/investor-reporting/holdings/tests"))
import test_snapshot as T
import test_entry_guarded as E

sys.path.insert(0, str(root / "data/assets/scripts/gold/investor_reporting"))
import holdings_snapshot as hs

node, A1, A2 = T.node, T.A1, T.A2
cases = [
    ("balanced", [node(A1, 100), node("m1", 100, "MODEL_LEAF", A1, "ASSIGNED")], True),
    ("single_over", [node(A1, 100), node("m1", 120, "MODEL_LEAF", A1, "ASSIGNED")], False),
    ("R1_offset", [node(A1, 100), node("m1", 80, "MODEL_LEAF", A1, "ASSIGNED"),
                   node(A2, 100), node("m2", 120, "MODEL_LEAF", A2, "ASSIGNED")], False),
    ("R2_nested_over", [node(A1, 100), node("s", 100, "SLEEVE", A1),
                        node("m1", 200, "MODEL_LEAF", "s", "ASSIGNED")], False),
    ("nested_under", [node(A1, 100), node("s", 100, "SLEEVE", A1),
                      node("m1", 80, "MODEL_LEAF", "s", "ASSIGNED")], False),
    ("nested_balanced", [node(A1, 100), node("s", 100, "SLEEVE", A1),
                         node("m1", 60, "MODEL_LEAF", "s", "ASSIGNED"),
                         node("m2", 40, "MODEL_LEAF", "s", "ASSIGNED")], True),
    ("signed_balanced", [node(A1, 100), node("m1", 120, "MODEL_LEAF", A1, "ASSIGNED"),
                         node("cash", -20, "UNRESOLVED", A1, "ASSIGNED")], True),
    ("observed_zero", [node(A1, 0)], True),
    ("missing_source_acceptance", [node(A1, 100)], False),
]
results, failures = {}, []

for name, nodes, expected in cases:
    source = T.fixture_snapshot()
    source["nodes"] = nodes
    source["attribution_holdouts"]["unassigned"]["account_ids"] = []
    source["attribution_holdouts"]["unassigned"]["account_count"] = 0
    source["attribution_holdouts"]["unassigned"]["value"]["value"] = 0
    members = [n["node_id"] for n in nodes if n["node_kind"] == "ACCOUNT"]
    total = sum(n["amount"]["value"] for n in nodes if n["node_kind"] == "ACCOUNT")
    source["_manifest"] = {"total_market_value": total}
    source["custody_totals"]["total_market_value"]["value"] = total
    if name == "missing_source_acceptance":
        source["attribution_holdouts"].pop("reconcile")
    projected = T.sn.project(copy.deepcopy(source), T.scope_for(members))
    projection_ok = projected["attribution_holdouts"]["reconcile"]["reconciled"]
    runner_ok = hs.reconcile_before_after(copy.deepcopy(source))[0]
    routes = T.sn.register_routes(T._enforcer(T._directory(members)), lambda *args: source)
    route_error = None
    try:
        answer = routes[T.sn.ROUTE_KEY](T._authz.Request(T._headers(), T.sn.KEY_OPERATION, "account", members[0]))
        route_ok = isinstance(answer, T._authz.Served)
    except T.sn.SnapshotUnavailable as exc:
        route_ok, route_error = False, str(exc)
    restore = E._install(members)
    try:
        entry_answer = E.subject()[0](E._event(members[0], snapshot=False, snapshot_fixture=source), None)
    finally:
        restore()
    entry_ok = entry_answer.get("ok") is not False
    reason = entry_answer.get("status", {}).get("public_reason_code")
    passed = projection_ok == expected and route_ok == expected and entry_ok == expected
    if name != "missing_source_acceptance":
        passed = passed and runner_ok == expected
    if not expected:
        passed = passed and reason == "NOT_READY" and not entry_answer.get("data")
    results[name] = {"expected_accepted": expected, "projection_accepted": projection_ok,
                     "builder_reconciled": runner_ok, "guarded_route_served": route_ok,
                     "guarded_route_error": route_error, "actual_entry_served": entry_ok,
                     "actual_entry_reason": reason, "PASS": passed}
    if not passed:
        failures.append(name)

for name, value, expected in [("None", None, False), ("NaN", float("nan"), False),
                              ("infinity", float("inf"), False), ("bool", True, False),
                              ("zero", 0, True), ("duplicate", 100, False)]:
    rows = [{"account_id": "a", "current_value": value}]
    if name == "duplicate":
        rows.append(dict(rows[0]))

    def read(_s3, _bucket, key):
        return pd.DataFrame(rows) if "accounts_v2" in key else pd.DataFrame()

    error, values = None, []
    with patch.object(hs, "_read_parquet", read), \
            patch.object(hs, "_latest_date_partition", lambda *a, **k: "2026-09-21"), \
            patch.object(hs, "_latest_complete_eclipse_date", lambda *a: "2026-09-21"), \
            patch.object(hs, "_directory_account_ids", lambda *a: None):
        try:
            nodes, _manifest = hs.build_inf(None, "2026-09-21")
            values = [n["amount"]["value"] for n in nodes if n["node_kind"] == "ACCOUNT"]
        except ValueError as exc:
            error = str(exc)
    passed = (error is None and values == [0]) if expected else error is not None
    results["R3_" + name] = {"expected_accepted": expected, "error": error,
                             "account_values": values, "PASS": passed}
    if not passed:
        failures.append("R3_" + name)

print(json.dumps({"results": results, "failures": failures}, indent=2, allow_nan=False))
raise SystemExit(bool(failures))

```


## Reproduction appendix: holdings selection/release aefcfb6541

```python
"""Actual holdings/loader/store composition; only boto3 transports are synthetic."""
import copy
import io
import json
import os
import sys
from pathlib import Path
from unittest.mock import patch

os.environ["AWS_EC2_METADATA_DISABLED"] = "true"
os.environ["IRPT_DIRECTORY_BUCKET_MAP"] = json.dumps({"49financial": "review-only-bucket"})
os.environ["IRPT_REQUESTS_TABLE"] = "review-only-table"
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "infra/aws/lambda/investor-reporting/holdings/tests"))
import test_snapshot as T
import test_entry_guarded as E
import boto3

handler, boundary = E.subject()
G = boundary.operations["holdings-snapshot"].__globals__
assert boundary.deps is G["_loaders"].deps
assert boundary.opaque_firm_for is G["_loaders"].opaque_firm_for
assert boundary.shared_cache is None
results = {}


class Transport:
    def __init__(self):
        self.directory = T._directory([T.A1, T.A2, T.A3])
        self.ownership = {"schema_version": 1, "advisors": {
            "ADV": {"accounts": [T.A1, T.A2, T.A3], "relationships": []}}}
        self.snapshot = T.fixture_snapshot()
        self.items, self.keys = {}, []
        self.snapshot_reads = 0
        self.after_snapshot = lambda: None

    def get_object(self, Bucket, Key):
        assert Bucket == "review-only-bucket"
        self.keys.append(Key)
        if Key == "investor-reporting/directory/latest.json":
            value = {"key": "directory-current"}
        elif Key == "directory-current":
            value = self.directory
        elif Key == "platinum/49financial/ownership_map.json":
            value = self.ownership
        elif Key == "investor-reporting/holdings/latest.json":
            value = {"key": "holdings-current"}
        elif Key in {"holdings-current", "investor-reporting/holdings/2026-09-10/snapshot.json"}:
            self.snapshot_reads += 1
            value = copy.deepcopy(self.snapshot)
            self.after_snapshot()
        else:
            raise AssertionError("unexpected server key: " + Key)
        return {"Body": io.BytesIO(json.dumps(value).encode())}

    @staticmethod
    def key(item):
        return item["tenant"]["S"], item["request_revision"]["S"]

    def put_item(self, TableName, Item, ConditionExpression):
        assert TableName == "review-only-table"
        assert ConditionExpression == "attribute_not_exists(tenant) AND attribute_not_exists(request_revision)"
        key = self.key(Item)
        assert key not in self.items
        self.items[key] = copy.deepcopy(Item)

    def get_item(self, TableName, Key, ConsistentRead):
        assert TableName == "review-only-table" and ConsistentRead is True
        item = self.items.get(self.key(Key))
        return {"Item": copy.deepcopy(item)} if item else {}

    def client(self, service, **kwargs):
        assert service in {"s3", "dynamodb"}
        return self


def revoke(t):
    t.ownership["advisors"]["ADV"]["accounts"] = [T.A2, T.A3]


def tamper(t):
    item = next(iter(t.items.values()))
    record = json.loads(item["selection_record"]["S"])
    record["account_ids"] = [T.A2]
    item["selection_record"]["S"] = json.dumps(record)


def run(name, members, expected_members=None, expected_value=None,
        before=None, during=None, warm=None, event_change=None, code=None, reads=1):
    t = Transport()
    headers = T._headers(**{"X-Advisor-Id": "ADV", "X-Firm-Id": T.FIRM, "X-User-Role": "user"})
    headers["X-Contract-Version"] = "v1"
    with patch.object(boto3, "client", t.client):
        enforcer = T._authz.Enforcer(T._authz.FirmBinding(T.FIRM, T.FIRM_OPAQUE),
            *boundary.deps(T.FIRM), id_projection=boundary.id_projection(T.FIRM))
        scope, refusal = enforcer.resolve_now(T._authz.Request(headers, "holdings_snapshot"))
        assert refusal is None
        sel = G["_selection"]
        selection = sel.create_selection(scope, t.directory, members,
            directory_revision=sel.directory_revision(t.directory),
            save_selection=G["_selection_store"].configured_store().save)
        event = {"routeKey": E.ROUTE, "headers": headers,
                 "pathParameters": {"accountSetId": selection["account_set_id"]},
                 "queryStringParameters": {}}
        if event_change:
            event_change(event)
        if before:
            before(t)
        if during:
            t.after_snapshot = lambda: during(t)
        first = handler(copy.deepcopy(event), None)
        answer = first
        if warm:
            assert "data" in first, first
            warm(t)
            answer = handler(copy.deepcopy(event), None)
        observed = {"snapshot_reads": t.snapshot_reads,
                    "ok": answer.get("ok") is not False,
                    "reason": answer.get("status", {}).get("public_reason_code"),
                    "has_data": "data" in answer}
        passed = t.snapshot_reads == reads
        if expected_members is not None:
            data = answer.get("data", {})
            observed["members"] = data.get("scope", {}).get("account_ids")
            observed["value"] = data.get("custody_totals", {}).get("total_market_value", {}).get("value")
            observed["selected_fingerprint_matches"] = (
                data.get("scope", {}).get("resolved_scope_fingerprint") == selection["selected_account_set_fingerprint"])
            passed = passed and observed["ok"] and observed["members"] == sorted(expected_members)
            passed = passed and observed["value"] == expected_value and observed["selected_fingerprint_matches"]
            text = json.dumps(data)
            passed = passed and all(account not in text for account in [T.A1, T.A2, T.A3] if account not in members)
        else:
            passed = passed and not observed["ok"] and not observed["has_data"]
            if code:
                passed = passed and observed["reason"] == code
        observed["PASS"] = passed
        results[name] = observed


run("single_A2", [T.A2], [T.A2], 40)
run("mixed_A1_A3", [T.A1, T.A3], [T.A1, T.A3], 107)
run("unassigned_A3", [T.A3], [T.A3], 7)
run("dated_A1", [T.A1], [T.A1], 100,
    event_change=lambda e: e["queryStringParameters"].update(as_of="2026-09-10"))
for label, change in [
    ("revoke", revoke),
    ("entitlement_revision", lambda t: t.ownership.update(revision="new-revision")),
    ("directory", lambda t: t.directory.update(revision="new-directory")),
    ("record_tamper", tamper),
    ("record_deleted", lambda t: t.items.clear()),
]:
    run("release_" + label, [T.A1], during=change, code="OBJECT_NOT_COVERED")
for label, change in [("revoke", revoke), ("record_tamper", tamper),
                      ("directory", lambda t: t.directory.update(revision="new-directory"))]:
    run("warm_" + label, [T.A1], warm=change, code="OBJECT_NOT_COVERED")
run("partly_revoked_pair", [T.A1, T.A2], before=revoke, code="OBJECT_NOT_COVERED", reads=0)
run("missing_reference", [T.A1], event_change=lambda e: e["pathParameters"].clear(),
    code="OBJECT_NOT_COVERED", reads=0)
run("literal_account", [T.A1], event_change=lambda e: e["pathParameters"].update(accountSetId=T.A1),
    code="OBJECT_NOT_COVERED", reads=0)
run("browser_snapshot", [T.A1], event_change=lambda e: e.update(snapshot_fixture=T.fixture_snapshot()), reads=0)
run("foreign_source", [T.A1], before=lambda t: t.snapshot["scope"].update(firm_id="inflection"), code="NOT_READY")
run("economic_failure", [T.A1], before=lambda t: t.snapshot["nodes"][1]["amount"].update(value=200), code="NOT_READY")

failures = [name for name, observed in results.items() if not observed["PASS"]]
print(json.dumps({"results": results, "failures": failures}, indent=2))
raise SystemExit(bool(failures))

```
