# V-2 — Ad-hoc chain run + body reads + render + re-pin (rows V6/V7/V8)

**Run:** 2026-08-07 01:01–01:20Z by `3.0.0_SA_CVO~Z` · TO `MDPF_CANPLAT.V1` · V-PRD @2dedd8f6a §2 V-2
**Andrew-direct authority (V-PRD header, verbatim):** *"we also need an ad hoc run issued now and make
sure that it displays properly on the portal."*
**⛔ This run is sanctioned QA and is NEVER production evidence — it closes no R-row.**

## The chain, hop by hop (production order, real waits)

| hop | invoke | result |
|---|---|---|
| 1 · `mdpf-daily-trigger` | RequestResponse 200, 01:02Z | **DESIGNED DEFERRAL** — `dispatched:false, deferred:true, reason:"INF spine (the driver) not fresh vs its own cadence"`. Gate payload: inflection `fresh:false, as_of:2026-07-31`; 49financial `fresh:true, latest_partition:2026-08-05, trading_days_behind:2 (max 2)` — **the trading-calendar reasoning default, working in production.** ⚠ payload also carries `deferral_record: {recorded:false, why:"both paths failed: AccessDenied"}` — SURPRISE'd 010342Z, COO~Z triaged 010447Z: RECORDED, NO ACTION (component dies with the cutover; A6 manifests are the built fix). |
| 2 · `mdpf-accrual-trigger` | RequestResponse 200, 01:04Z | `dispatched:true`, SSM `077499ce-81b3-4ebc-9fef-31762fce6ae1` on `i-02448edb624a7a7cf`; **SSM Success rc=0** (01:04:39–01:04:44Z). Telemetry (s3://opal-data-mdpf/telemetry/mdpf-daily-runner/accrual-bridge-runs/20260807T010404Z.log): **`DONE written=0 skipped_existing=14 errors=0`** — idempotent skips over already-present dated gold (data-as-of 2026-08-03/04). |
| 3 · `opal-assets-mdpf-portal-publisher` | RequestResponse 200, 01:06Z | **`all_present:true, published_count:14, total:14, missing:[], unrecognized_gold_keys:[]`** — every key `status:"published"` from frozen sources (`source_vintage` 2026-08-03 except the three account-distributions + global at 2026-08-04). |

**No invoke was IAM-denied at this seat** — the named fallback was not needed.

## V6 — served bodies read (advanced vs frozen, by data-as-of, never mtime/ETag)

Measured with the R7 comparator (live post-publish vs the 00:07:53Z pre-run pin), run
`runs/R7_20260807T010634Z.json`: **12 of 12 pairs, 47,119 paths compared, and the ONLY moved path on
every artifact is `_provenance.written_at`** (13:50:4xZ → 01:06:0xZ). **Zero business values changed;
zero data-as-of advanced.** Extras match: `account-units` generated_at 2026-08-05 frozen /
written_at 01:06:00Z; `non-model-assets` generated_at 2026-08-04 frozen / written_at 01:06:01Z.

**⇒ The frozen-gold republish behaviour, measured end to end and localised to one JSON path per
artifact — pre-ruled EXPECTED, not a finding.** (It is also the live demonstration of why R1
existence and ETag/mtime may never be read as freshness: the publisher produced a perfect
14/14 `published` verdict, fresh ETags, on two-trading-day-stale data.)

## V7 — rendered surface, all four scopes (`records/v7_renders/`)

**Method:** playwright headless render of the DEPLOYED bundle at `https://opalinvest.dev/portfolios`
(system Edge, ui-smoke pattern). The deployed edge **correctly 401s** a stubbed session on every
`/api/general/mdpf/*` fetch (logged, all four scopes) — so the data layer was fixture-fulfilled with
the EXACT VersionId-pinned bodies from the 011035Z manifest. **Verdict scope: renderer + served
bodies. The live AUTHED edge-fetch leg is COULD-NOT-VERIFY at this seat (no credentials) — adopted
instead from P0-6's three-oracle confirmation + the PRD §0 premise; the 401 log is itself the
edge-posture measurement.**

| scope | renders | key values on screen | provenance label |
|---|---|---|---|
| global | OK — full: donut, bell curve, percentiles, trends | Total AUA $1.98B; Holdings 8,108; excluded-unfunded 49 note (**I-3 live on screen**) | SmartX + per-firm bases footnote |
| 49financial | OK | Total AUM $1.71B; Holdings 7,082; as-of Aug 3 2026 5:00p ET | SmartX / schwab-rps |
| inflection | OK | Total AUM $207M; Holdings 733; as-of Aug 3 | Orion Portfolio Solutions |
| cottonwood | OK — short-history state correct (N/A quarter tiles; labeled "Interpolated model mix (estimate)") | Total AUM $472M; Holdings 294; as-of Aug 3 | Black Diamond Rebalancer |

Color law clean on all four (dark panels, no light-on-silver). **Data-as-of displayed is 2026-08-03 —
recorded beside the render verdict so V7 is never read as a freshness claim.**

**Observation, recorded not chased (SURPRISE 012053Z, COO~Z triage 012157Z = today's live behavior,
presumptively by design, V3 not reopened):** the holdings distribution CURVE draws at global only;
all four pinned bodies carry populated `total.histogram` (counts_sum 7925 / 7082 / 549 / 294).

## V8 — the R7 pinned baseline (the fixture)

**`baseline_manifest_20260807T011035Z.json`** — 14/14 keys (12 canonical + 2 extras), explicit
VersionIds + ETag + sha256, **pin instant 2026-08-07T01:10:35Z**, captured 4 minutes after the 01:06Z
publish per COO~Z's PIN-NOW guidance (011009Z). **SUPERSEDES the 00:07:53Z manifest as the R7
before-image**; derivation history carries both. Re-pins remain new manifests, never edits.

— 3.0.0_SA_CVO
