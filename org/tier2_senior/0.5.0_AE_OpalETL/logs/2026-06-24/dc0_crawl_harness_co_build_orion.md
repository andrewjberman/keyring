# DC0 Comprehensive-Crawl Harness -- Orion co-build (DC0.2-0.3 half)

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE, COORDINATE

**Session:** 2026-06-24 | **Agent:** 0.5.0_AE_OpalETL | **Project:** DATA_PLATFORM.DC0
**Role:** 2nd AE-CloudOps lane (co-build), base-AE (0.7.0) = DC0 lead. **Phase:** OFFLINE build (arch-GO'd).

---

## Summary

Spawned as the 2nd AE lane for the DATA_PLATFORM comprehensive-crawl harness (DC0 -- the
vendor-endpoint-enumeration engine for the supplant/leverage program). MSTR orient + COO GO +
base-AE direct co-build request. Co-built DC0.2-0.3 (offline) with base-AE: he owns the isolation
safety-core (isolation.ts / xhr-capture.ts / guarded-navigator.ts / gold.ts -- all tested); I built
the 3-component "driving" half against his tested interfaces. Split confirmed with the lead; my half
COMPLETE, 52/52 PASS, pushed; RAVC'd base-AE + COO + CTO.

## Deliverables (my half -- all on origin/CLOUD)

| Component | Commit | What | Tests |
|---|---|---|---|
| `src/orion-config.ts` | `74fc3ec5b` | the Orion VendorConfig + Orion-specific capture wiring (classifier + consumed-today keys) | 12 |
| `src/nav-walker.ts` | `1723b5c8b` | screen-list + drill-decision walker over the GuardedNavigator; HumanizerStrategy seam | 4 |
| `src/crawl.ts` | `d39301362` | DI orchestrator (preflight->attach->walk->write) + a DC0.4-HARD-GATED live path | 5 |

Full harness suite after my adds: **52/52 PASS** (base-AE's 31 + my 21). `bun test`.

## Key engineering decisions

- **Built straight against the tested interface** (no edits to base-AE's files). Every crawl op
  routes through his GuardedNavigator -> IsolationLayer.guardAction (serving + auth + budget +
  pace), NON-BYPASSABLE by construction. crawl.test EXERCISES it (verify, not assert): a serving
  window aborts the whole crawl in preflight (zero navigation).
- **All config inputs grounded** (D3 spec + ADVI_ORIAPI + orion_export.ts + live AWS describe), no
  guesses on the load-bearing isolation inputs:
  - `servingActiveSignal='schedule-only'` -- inf serving is Lambda-driven; base-AE shipped the mode
    (2b0600f33) off my Q1; windows = the inf 12:00-14:00 UTC footprint.
  - `parkedAuth.tokenField='jwt'` -- orion_export.ts `writeJwtToS3` stores the raw bearer (Session-
    prefix stripped) in the `jwt` field of `opal-data-inf/orion/jwt/current.json`.
  - **egress RESOLVED** (live describe): inf-exporter egresses via IGW `igw-0b6e9e626ad5128db` with
    an EPHEMERAL public IP (shared subnet `subnet-023db8cbfd99ffff2`, MapPublicIpOnLaunch=true, NO
    NAT) -- same as smartx. Set `egress.mode='ephemeral-ok'` (Orion already sees inf auth from a
    changing IP daily; a crawl in the same shared subnet rides-existing by co-location). Routed the
    supplant->shared-NAT policy decision to CTO.
  - `s3CatalogBucket='opal-crawl-catalog'`, prefix `orion` (base-AE Q2 standardization).
- **No-live-crawl encoded in CODE, not just procedure:** `runOrionCrawlLive` calls `assertDc04Gate`
  (double opt-in: in-code `liveGateAck` AND env `DC04_LIVE_CRAWL_AUTHORIZED=1`) -> a stray import/
  env can NEVER launch a live vendor crawl pre-DC0.4. Tested.
- **Stealth seam grounded + specified:** the smartx Humanizer (humanMove/humanType/humanScroll) is
  page.mouse-COUPLED, so it can't live in nav-walker (no page); specified as a `HumanizerStrategy`
  hook inside GuardedNavigator (base-AE's, who owns the page), invoked AFTER guardAction. Lean:
  offline v1 = higher-level realism (ordering + RateBudget.pace jitter); the mouse hook = DC0.4
  hardening. Raised to base-AE (his call).

## Current State

- My DC0.2-0.3 offline half: **DONE + pushed + RAVC'd**. base-AE has shipped isolation (e6458b90d),
  xhr-capture (8b47fde05), GuardedNavigator (f2e57ac7d), schedule-only (2b0600f33), catalog-gold
  (a849a35c5). DC0 offline harness is structurally complete + tested end-to-end.
- OFFLINE-gate held throughout. DC0.4 LIVE Orion crawl is the SEPARATE later gate (CTO-isolation-
  verify + Andrew per-vendor ToS) -- NOT started, NOT to be started without that gate.

## Next Steps

- **[0.7.0_AE_CloudOps]** (lead) confirm: (1) stealth-seam A/B -- add the GuardedNavigator
  HumanizerStrategy hook now, or defer to DC0.4 (I author the strategy either way); (2) gold.ts
  enriches WITHIN the capture spine (orchestrator doesn't invoke gold / thread bearer) -- confirm so
  crawl.ts stays at the silver write; (3) opal-crawl-catalog TF-provision at integration.
- **[1.0.0_SA_CTO]** the egress policy decision: supplant-track -> provision a shared NAT, or accept
  ephemeral-ok? (non-blocking for offline; a DC0.4 live-gate input.)
- **[0.5.0_AE_OpalETL]** (self) on base-AE's word: integrate (wire the storage_state ride + any
  gold hook) + author the HumanizerStrategy from the smartx stack when the GuardedNavigator hook
  lands. DC0.5 SmartX vendor-2 (leverage track) reuses this harness parameterized by a smartx
  VendorConfig -- a natural follow-on. IDLE/available meanwhile.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-which "...egress NAT vs ephemeral..."` | route the egress-topology question | MISS -- fell back to a noisy repo grep on "ephemeral" (the known LD-0207 router gap: routes only the curated subset; VPC-topology intent unmapped). |
| `comp-aws inf-exporter` | attempt service-topology lookup | WRONG SHAPE -- comp-aws is a graph derive/score/snapshot tool, not a per-service lookup (rejected the arg). |
| raw `aws ec2 describe-subnets/route-tables` | resolve egress (NAT vs IGW) | `# rail-checked`: no comp-tool surfaces VPC subnet route-table topology (comp-aws=graph-derive, comp-routes=CloudFront/APIGW, comp-iam=IAM, comp-blast=fn-blast). READ-ONLY. Definitive: IGW/ephemeral, no NAT. |

Gap found: comp-which does not route VPC-network-topology questions, and there is no comp-tool for
subnet/route-table egress (the `comp-aws inf-exporter`-style per-service lookup people reach for
doesn't exist). The AE comp minimums (`comp-pipescript deployed` before a gold run, `comp-iam gaps`
after iam.tf, `comp-blast` before infra deletion) did not apply: this is a greenfield OFFLINE TS
harness build -- no gold run, no iam.tf change, no infra deletion, no existing pipeline-graph nodes
touched. Grounding was source-read (D3/ADVI_ORIAPI/orion_export.ts) + one rail-checked read-only AWS
describe. comp-which/comp-aws auto-logged to org/compiler-tools-log.md.

---

## Addendum -- post-RAVC integration close (same session)

All RAVC loops closed; DC0 OFFLINE build DONE + integrated BOTH sides (full suite 55/55).

- **CTO egress RULING 151638Z** (folded, commit `1a3efd1a4`): ephemeral-ok APPROVED, NO NAT. My
  live-describe grounding FLIPPED the CTO's earlier same-egress-IP requirement -> the refined
  principle is "match the existing exporter's egress pattern" (ephemeral blend-in > stable
  stand-out for a reverse-engineered supplant vendor). assertEgress WARN stays as the per-vendor
  guard (it forced the decision = working as designed).
- **base-AE integration** (his 5b2f7d431, 54/54): wired MY HumanizerStrategy contract into
  GuardedNavigator (optional, invoked only AFTER guardAction -> non-bypassable proven). Confirmed:
  gold enriches INSIDE the capture spine (orchestrator stays at cap.catalog(), no double-own);
  opal-crawl-catalog bucket PROVISIONED+LIVE (s3CatalogWriter targets it). Pulled + re-ran 55/55 ->
  my code + his new GuardedNavigator integrate clean (4-arg construction vs optional 5th param).
- **DC1-readiness** (commit `1a3efd1a4`): grounded the storage_state READ-ONLY RIDE in
  runOrionCrawlLive (loadParkedSessionReadOnly -> opal-data-inf/orion/browser-profile/state.json,
  from orion_export.ts) -- the live crawl rides the existing auth, never logs in, NEVER saves back.
  This is the #1 mechanism DC1 needs to fire fast at the gate.

**DC0.4-hardening DONE (commit `924122566`):** the page-coupled OrionHumanizerStrategy. base-AE
resolved the structure fork = option A (vendor, the harness is a separate deployable). Vendored the
smartx Humanizer -> src/stealth/humanize.ts (provenance header; only adaptation = a local logger
interface), authored OrionHumanizerStrategy (humanClick = bezier-move+dwell+click; settleOnScreen =
scroll+dwell) against it, wired into runOrionCrawlLive ONLY (the gated live path). Selector-agnostic
(no UI knowledge); inert until DC0.4; GuardedNavigator invokes it only AFTER guardAction (guard
stays non-bypassable). Suite 62/62.
- **Completeness flag (raised to base-AE):** this is the per-ACTION stealth (mouse/dwell/click). The
  CONTEXT-level fingerprint evasion (smartx fingerprint.ts -- navigator/canvas/webgl at context
  creation) is a SEPARATE layer, NOT yet vendored/wired -- pending base-AE's call (vendor+wire at
  DC0.4 context-creation if we want full stealth). Not over-claiming stealth coverage.

**Remaining path (gated, not mine):** DC0.4 = CTO isolation-verify (the 62-test suite is the
evidence) + Andrew per-vendor ToS -> DC1 Orion live (with base-AE). The exact UI selectors/routes
stay the live-HAR discovery frontier (TBD even in the inf-exporter producer).

**Commits this session:** `74fc3ec5b` orion-config | `1723b5c8b` nav-walker | `d39301362` crawl |
`1a3efd1a4` egress-ruling+storage_state | `924122566` OrionHumanizerStrategy+vendored-stealth |
`86eb9e974`/`31710a396` log+addendum. All on origin/CLOUD. Full suite 62/62.
