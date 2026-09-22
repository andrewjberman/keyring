# Model Overlay independent acceptance matrix

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO~M`. Prepared September 22, 2026, approximately 4:50 PM Eastern.
Scope: Andrew's direct P/M/Y completion assignment; paired implementer `2.0.0_SA_COO~M`.
This is review preparation and a synthetic baseline finding, not a completed-candidate or deployed E2E verdict.

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

No completed candidate, deployed candidate pin, fresh account/position census, or live browser trace has been delivered to this reviewer. Historical cloud measurements in the briefs remain historical evidence.

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
| M1 Population | Enumerate custody before any model join; include modeled, entirely non-model, mixed, zero, closed and missing-input accounts; unknown value stays unknown; measure source completeness/freshness. | Per firm full account census and unique position census, represented/excluded-with-reason/missing counts; known value plus unknown-value counts; source completion revisions and clocks. | NOT_EVALUATED | NOT_EVALUATED |
| M2 Identity/grain | Unique account and position contribution; multiple SmartX allocations; shared Eclipse portfolios; missing assignment; model vs target vs actual basis and membership grain explicit. | Identity collision and contribution ledger over independently enumerated custody; synthetic probes plus actual source cases; no parent-and-child double count. | FAIL: 49F/INF probe | NOT_EVALUATED |
| M3 Economics | Model + confirmed non-model + unresolved known value equals independently enumerated custody; selected and parent denominators; signed/cash/zero/unknown/multi-currency handling; distinct custody/overlay clocks. | All selected accounts and positions; independent sums by firm/account/relationship/selection/currency; known three-case regressions and additional adversarial cases. No unexplained currency aggregation. | FAIL: all three probes | NOT_EVALUATED |
| M4 Publication | Gold Parquet history -> accepted bounded Platinum -> one complete manifest; same-day corrections unique; failed schema/reconciliation/incomplete source or partial write does not advance current pointer; prior accepted revision is explicitly stale. | Pre/post pointer object versions, Gold/Platinum hashes/revisions, acceptance receipt, injected failure outcomes and retry/concurrent publication evidence. | NOT_EVALUATED | NOT_EVALUATED |
| M5 Scope/API | Actual grant loader and API event; resolve exact account-set reference; single/relationship/subset; missing mapping fails explicitly; cross-firm/revoked/forged scope negatives; scope filtering creates no fictitious unresolved value. | Paired browser request/event/handler/response evidence with selected members vs permitted members, entitlement/directory revisions and canonical/provider IDs; zero unintended accounts. | NOT_EVALUATED; source shows `_no_grant` and permitted-set projection | NOT_EVALUATED |
| M6 UI | First-screen dollars/weights for three attribution buckets; all selected root accounts accessible; complete account/security drill where supported; honest unavailable granularity; source clocks, partial coverage, refresh/reopen retain exact revision. | Mounted UI trace through real wire adapter; account/position counts and totals matched to source/response; signed/invalid-denominator table fallback; no dropped clocks or coverage. | NOT_EVALUATED | NOT_EVALUATED |
| M7 Three-firm E2E | Fresh 49F SmartX, Cottonwood BD Rebalancer, Inflection Eclipse overlay joined to full custody; modeled/non-model/mixed/missing mapping/multi-sleeve/shared portfolio/subset/signed-cash cases. | Coverage grid per firm; actual source -> accepted Gold -> Platinum manifest -> deployed API -> browser trace with environment and revision identities. Three firms required; historical QA or fixtures insufficient. | NOT_EVALUATED | NOT_EVALUATED |
| S1 Selection/access | Selected-set fingerprint distinct from permitted set; server-owned crosswalk and current grants; no broadening on missing mapping; prospect firm/advisor ownership without fabricated client IDs; access rechecked on retrieval/download. | Shared M/P/Y producer-consumer examples and real request tests; dated account/allocation/model and BD crosswalk, model changes/sleeve closures/non-model/cash cases; pinned revisions. | NOT_EVALUATED | NOT_EVALUATED |
| S2 Accepted data | Independent full census and unique actual positions; explicit unknowns and supported membership; correct selected weights; reproducible accepted Gold/Platinum revision set. | M1-M4 evidence plus Y's consumed positions artifact; actual custody vs target basis and all rows reconciled/dispositioned. | FAIL for baseline builder grain/economics only | NOT_EVALUATED |
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
