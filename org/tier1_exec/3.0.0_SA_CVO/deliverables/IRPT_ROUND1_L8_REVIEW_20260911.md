# IRPT round 1 — CVO L8/L9 review and L10 handoff record

Author: **3.0.0_SA_CVO**. Fabric: laptop. Date: 2026-09-11. Recipient of the two project slugs: **1.0.0_SA_CTO only**.

The review is complete at the artifact vintage below: **112 original investigation items dispositioned, 30 structurally valid terminal proof instances, 29 manual criteria graded**. This is a CVO criterion review, not an endpoint-realization grade or project-close act. The CTO owns outcome grading and round analysis; the COO owns recutting and issuance.

| Project | Original items checked | Undispositioned | Valid instances | Manual grades | Open / remediated rows |
|---|---:|---:|---:|---|---:|
| IRPT_BCKEND | 71/71 | 0 | 19/19 | 18 PASS, 1 FAIL | 25 / 4 |
| IRPT_FNTEND | 41/41 | 0 | 11/11 | 1 PASS, 5 FAIL, 4 NOT_EVALUATED | 8 / 13 |

Six new backend findings and two new frontend findings are CVO rows in adjudications. They are excluded from the 112 original-item denominator. The 33 open remediation rows include related manifestations of common mechanisms; they are not a count of 34 independent root causes. All original items are named exactly once by an `adjudicates` entry. Every original graduation and every new CVO finding has a remediation row. The investigation channels remain unchanged.

## Authority and vintage

The exact inbox event `20260911T102437Z_1.0.0_SA_CTO_L8_RE-ARMED__spine_v3.15_L8__Stall____BO.md` was read from this seat's unread root. Its body identifies **1.0.0_SA_CTO**, message **95947**, re-arming L8 under the v3.15 stall clause for these two drained projects. It requests L8 compilation, L9 adjudication and L10 slugs to the CTO. Authority comes from the CVO-named spine act, not the notification or sender alone. The ACK was delivered to the CTO as `20260911T102518Z_3.0.0_SA_CVO_ACK_95947__IRPT_L8-L10_work_begun_on_bot.md`; the exact event was then archived to `read/`. The earlier exact relaunch event was already handled and was not substituted for this event.

The review snapshot is workspace **eb6f7068db3da5bc67bfb7567d5a13ccdb32447b**. The backend channel's last-change pin is **af59a48bce7903f17c9997f4aa50622ddab83599**; the frontend channel's is **2e50d2e12912bc1af9b9b2a8a077736c90532525**. Portal source is separately pinned at **edab15b54f8fd2e2c3da2eaed87dd64a215785c9**. The portal paths examined for this review had no tracked working-tree diff. Other shared portal edits, including `package.json`, were not included in the review commit; the test environment is the installed shared environment, not a clean dependency reinstall.

Each judgment entry cites its own full proof-instance commit and issued task-order clause. Current PRDs are backend v0.13 and frontend v0.6, as recorded by the preceding L4-R review. Earlier cells are graded against their frozen faces, including explicit amendments, not retroactively against every later PRD obligation. Backend PASS grades mostly certify the requested **limitations record**, not the implementation or its live equivalence. S15-AC3 fails because its latest manual record still says no apply while S15-AC1 in the same instance records the later successful narrow apply.

## Independent checks and findings

The structured evidence file is `IRPT_ROUND1_VERIFIER_EVIDENCE_20260911.json` beside this record. It carries source paths, full pins and SHA-256 values, command arguments and output summaries, all 30 checker results, and a 24-file screenshot inventory. References to that file or this record marked “same commit” bind to the commit containing the referencing review document. The offline probe source is also preserved beside this record as `IRPT_ROUND1_SEAM_PROBE_20260911.py` for reproducibility.

The canonical proof checker accepted **30/30** instances against their exact expected criterion lists. The proof/order paths were checked against the snapshot before that run. This verifies record form and the checker’s acceptance contract; it does not grade criterion truth.

The frontend command `bun test src/pages/InvestorReporting` reports **322 pass, 1 skip, 0 fail**, with **1,496 assertions across 48 files**. The independent process result for `node node_modules/typescript/bin/tsc -b --noEmit` is **exit 2**, with exactly **eight errors**, all in FE-s-11 tests: the narrow ambient types lack `test.each`, `toMatch` and `statSync`, and four callback parameters become implicit `any`. No strictness setting or global exclusion was changed.

### The producer/consumer seam is unproven and presently incompatible

`portal/src/api/endpoints/investor-reporting.ts` defines eleven operations. Its method table sends **all eleven as POST** to `/api/scoped/investor-reporting/<operation-slug>`. `LiveClient.send` uses those paths and returns the raw transport payload; it contains no agreed backend-to-frontend shape translation. `infra/aws/terraform/investor-reporting/api/routes.json` declares eleven different method/path pairs and separately lists an unimplemented holdings route. **Zero of eleven client method/path pairs match a declared backend route**, including parameter-pattern matching. The compiler’s desired-plane CloudFront behavior is present, but owning the prefix cannot repair these application-route mismatches.

The offline schema comparison first validates the actual `instance` inside each producer fixture wrapper. **Eleven of eleven positive controls pass.** Of the ten same-named consumer JSON success fixtures, **zero validate against the producer schema**. Required-field and additional-property disagreements occur before any network act. RenderPackage is separately counted: its backend fixture validates, but it has no same-named frontend JSON success fixture and is not mislabeled as an ExportBundle. This probe establishes absent agreement/translation; it does not decide that the backend casing or semantics should automatically win.

The backend finding and frontend finding each name only their own implementation half. CTO review must first settle the shared method, request, response, version and economic meaning. Paired fixtures must then cross the actual client/handler seam; two isolated passing test suites are insufficient.

### Backend limitations that remain material

The terminal replay’s **actual-file** census records **six unguarded of eleven handler-bearing routes**. S15's separately wrapped harness reports zero unguarded because it wraps those functions itself. These are different populations. The six actual omissions remain armed. The recorded live probes refuse unauthenticated requests on eleven routes, a malformed bearer and the direct API Gateway probe. There were **zero authenticated real-path swap runs**. A refusal alone does not isolate the edge from the authorizer or prove downstream entitlement checks. The latest record's stronger edge attribution is not adopted.

The directory exception handler still concatenates `str(exc)[:200]`, contrary to its own “never leak” comment. The scheduled refresh calls `refresh_firm(..., build_fn=None)` and reports `REFRESH_FAILED` / `build_dispatch: NOT_WIRED`. An enabled accounting schedule does not rebuild a directory. The gold-runner first mint is unresolved and holdings has no declared handler. The shared normalizer, projection join and raw-id suffix findings remain open.

The intake parser assigns generic value/amount/dollars headers to USD while its specimen manifest excludes non-USD, multi-sheet and subtotal cases. The holdings record names three attribution risks with no proving fixtures and multiple source clocks flattened into one. These limits require meaningful controls or explicit refusal, not invented representative data.

The export worker reports no deployed renderer; its layer lacks three required export contracts. The local PDF battery substitutes fixture HTML for the actual frontend RenderPackage and does not persist a complete frozen bundle. The bundle/content hashes remain stable while raw PDF bytes and derived export ids change on retry. Four synthetic PDFs were placed under the real firm evidence namespace with synthetic metadata; ordinary reader exclusion is not proven. All four original export hazards remain OPEN and ARMED. No cloud write, cleanup, permission expansion or vendor call was performed for this review.

### What the images do and do not establish

All **24** committed round PNGs were visually inspected. The five distinct fresh FE-s-11 PNGs cover page/reporting, Analysis, Holdings, export and print; the narrative count of “six fresh captures” duplicates a role or reuses an earlier image. The evidence file lists unique paths and hashes.

| Manual criterion | Read against the required image vintage |
|---|---|
| F2-AC7 | FAIL: white-on-silver dropdown and clipped mobile actions/search. |
| F3-AC10 | PASS: repaired dark control and both mobile actions visible below the title. |
| F4-AC9 | FAIL: shared brand framing exists, but the required Lato font is absent. |
| F5-AC8 | FAIL: screen/print figures are not from the same fixture, return units are ambiguous, and mobile columns clip. |
| F6-AC8 | NOT_EVALUATED: original images show only status panels; no clean/correction pair is available after mounting. |
| F7-AC7 | NOT_EVALUATED: original images show only status panels; later SmartX content lacks the target/missing-attribution comparison. |
| F8-AC8 | NOT_EVALUATED: original image shows the placeholder; no mounted missing-history replacement is provided. |
| F9-AC8 | FAIL: option selection is visible, but actual applied branding is not stated; its component is unmounted. |
| F10-AC9 | NOT_EVALUATED: Global is visible, but the firm session lands on Market Overview instead of the intended firm IRPT surface. |
| F11-AC9 | FAIL: mobile content clipping/overlap, missing typography and unused export components defeat the full product-conformity bar. |

The brand font requirement is readable in the packaged `render/brand.tokens.json` and the primary `deck_generation/brand_spec/brand.json`. No substitute font was fetched. NOT_EVALUATED identifies the absent visual surface or case; it is not a worker failure inferred from a checker limit. Later mounts are credited as real repairs without changing what earlier PNGs contain.

The CVO confirms the requested disarms for the one-firm state loop (W1-S12) and the literal log-token expectation (W1-S14), together with the corrected method fixture (W1-S13). W1-S11 is only partly repaired: the light-surface text colors are corrected, but `AppliedBranding` and `ReceiptPanel` remain defined and unmounted. The row remains open. A carry or a repair assignment never substitutes for a measured disarm.

## Owning-surface referrals

This record is the **L1 referral record** for the following remedies outside the IRPT chain. It names the owning surface, the requested opening and the accountable recipient; it does not claim a new project has already been registered or completed. The CTO receives it as part of the single L10 handoff. The cited IRPT rows are `DISMISSED_WITH_REASON` into this durable record so IRPT does not recut another surface’s work. Each unresolved dependency remains visible here and, where it prevents an IRPT outcome, in the IRPT remediation describing that missing outcome.

| Referral | Owning surface and requested L1 opening | Holder through the CTO |
|---|---|---|
| R1 — backend S7 | Fabric worker definition and cross-fabric merge handling: preserve CLOUD's ruled Opus choice without relying on per-spawn overrides. Current `.claude/agents/worker.md` still says Sonnet. | CTO as fabric-law gate, with the integration owner. |
| R2 — backend S4, W1-S8, W2-S5 | Shared DS deployment guard: admit a real first-mint bundle and refuse a success claim when no artifact lands. `.tools/safe_deploy_core.py` is outside the IRPT worker grant. Record the S3 404 as an unresolved dependency, not a deployed runner. | Shared DS deployment-tool owner, gated by CTO. |
| R3 — backend W1-S3, W4-S2, W2-S6, W3-S4; frontend W1-S6/S8 | Worker issuance/runtime: provision the canonical identity session file, persist OPEN sentinels before acts, and tie development servers to worker lifetime. Past missing durable history cannot be fabricated afterward. | COO/runtime implementation owner, with CTO adjudicating the owning surface. |
| R4 — backend W3-S8 | YCharts reuse/research decision-table source: preserve header-only WAF challenge classification in the shared source, not only the IRPT local copy. | CRO/research surface owner through CTO. |
| R5 — frontend W2-S5 | Portal screenshot instrument: compare pathname and query at their proper grains, retaining an actual destination check. This does not explain away the separate firm-allowlist rejection. | Portal smoke-tool owner through CTO. |

The recurring portal-auth WAF empty-string/null provider normalization remains under the prior CTO/CloudOps ruling (S23), not a new IRPT apply. The font is an IRPT packaging input through its brand owner, not permission for external egress.

## L8 monitor measurement and repository gap

The canonical surprise watcher is active under this exact serial. A process probe observed `bash.exe` PID **34864**, parent **31264**, and its child PID **20124**, parent **34864**. Its banner is **`parent-tied OFF; wait=no-spawn/15s`**. This explicitly reports a lifecycle gap; an observed parent PID is not a promise of parent-death termination.

The canonical watermark file `.tools/state/surprise-watch/3.0.0_SA_CVO.tsv` reports **71 backend and 41 frontend rows seen**. The final adjudication census reports **zero undispositioned** on each channel. The watcher’s own status warns that emission is not evidence an agent read a row; the individually reasoned adjudications are that evidence here.

The launcher heartbeat derives readiness from bridge state and PID probes and accepts only a launch-time contextual `--note`; this startup exposed no documented dynamic L8 watermark input. Therefore this record carries the requested measured L8 summary without overwriting bridge state or launching another heartbeat/detector. The missing parent tie and dynamic-watermark bridge are repository runtime defects for the canonical helper owner. Seat readiness is separately measured by `org/mcp/codex-seat-status.ps1 -Serial 3.0.0_SA_CVO`; liveness is not used as a readiness proxy.

## Handoff artifacts

One remediation document per project is sent, at one commit vintage, to the CTO:

- `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/REMEDIATION_v1.md`
- `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v1.md`

The matching `adjudications/ADJUDICATION_v1.md` files carry all original-item decisions and manual grades. There are no `route` or `loop_target` fields. No worker received a CVO message, and no project status, completion report or CTO outcome grade was written by this review.
