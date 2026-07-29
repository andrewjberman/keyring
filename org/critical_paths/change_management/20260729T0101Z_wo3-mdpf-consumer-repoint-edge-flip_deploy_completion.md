# Deploy: wo3-mdpf-consumer-repoint-edge-flip

**Opened:** 2026-07-29T01:01Z by 0.2.0_DT_PortfolioAnalytics · **Authority:** MDPF_RESET WO-3
(Andrew ~2334Z "do the consumer re-point" + ~2357Z "ok proceed with the DT flip, that is my GO" +
~0000Z "Option 1, fix then flip tonight" + ~0059Z via COO "I do not want to wait to tomorrow to
repoint"; CTO GO 005733Z with full four-leg chain; COO acceptance diff PASS 005548Z/005606Z;
AE trio verified 6/7-EXACT accepted by CTO 003928Z; Step-0 ACCEPTED 000536Z).

**The change:** ONE added prefix-disjoint branch in `public-data-router` (Lambda@Edge):
`/api/general/mdpf/` -> `/platinum/mdpf/` (was: fell through the default to `/json/mdpf/`).
Nothing else in the router moves. Deploy = build (esbuild minify) -> S3 artifact ->
safe-apply portal-auth (one apply mints the new version AND re-points all three behavior
associations via `qualified_arn`) -> L@E replication -> scoped CF invalidation
`/api/general/mdpf/*` only.

**Pre-flip baselines (all authenticated live-URL fetches, positive-controlled 00:10-00:14Z):**
| what | value |
|---|---|
| live global URL (pre) | 200, 254,419 B == S3 `json/mdpf/global/` ETag `5f758b470372da18ad04e5248037cdd0`, as_of_last 07-22 |
| non-mdpf control `portfolios/aum-metrics.json` | 200, 7,234 B, md5 `9bae4b42ff312c72817ca27861c1e28b` |
| firm URLs (pre) | 49f 183,004 B `50140744...` · inflection 146,290 B `e3c8db35...` · cottonwood 87,262 B `194e5bb0...` |
| deployed router (pre) | `public-data-router:5` on dist `EVTSA9VEHNZVH` (CF config ETag `E2DYWYC9UJPDWJ`) |
| post-flip expected global | platinum object ETag `31e64570d3090eff4df3baab91d2a1dd`, 200,059 B, as_of_last 07-27, last value 1,950,519,805.86 |

**Acceptance (CTO dispatch 234425Z + addendum 234528Z + COO 005606Z):**
1. live global URL -> 1,950,519,805.86 @ as_of_last 07-27 (B content)
2. one URL per firm (49financial / inflection / cottonwood) -> 200, platinum per-scope content
3. CONTROL: non-mdpf `/api/general/` path byte-identical to pre-flip
4. NEGATIVE: frozen `json/mdpf/global/` object UNTOUCHED (ETag `5f758b47` unmoved)
Plus: no historical value change on any of the 447 shared dates (COO's oracle: any historical
delta = routing/caching artifact -> escalate, do not rationalise).

## Legs
- **L1 (git):** router edit + ledger committed to CLOUD. — *opened*
- **L2 (deploy):** build+upload zip -> source map commit -> safe-apply portal-auth -> new version
  live on all 3 behavior associations -> 0-diff plan. — *opened*
- **L3 (activation):** CF distribution Deployed + scoped invalidation `/api/general/mdpf/*`
  Completed. — *opened*
- **L4 (verify):** four exercises + negative + shared-date spot-check; report to CTO/COO. — *opened*

## Ledger items beyond the script (recorded at open, discharged at close)
- **CLOBBER-DETECTOR RE-BASELINE (COO 005606Z, CTO 005733Z):** at cutover the serve-integrity
  baseline MOVES: new served-content reference = `platinum/mdpf/global/aggregate-aua-timeseries.json`
  (ETag `31e64570d3090eff4df3baab91d2a1dd` at flip). The old `json/mdpf/global` ETag `5f758b47`'s
  ONLY remaining meaning is the NEGATIVE control (frozen legacy, must never move). Any reader
  verifying the serve against `5f758b47` after this deploy is verifying a retired baseline.
  (The A.3 served-freshness instrument re-point is separately routed by CTO — not this deploy.)
- **JWT wipe attestation due at close:** the one-night verify token + key material
  (scratchpad `jwt-priv.pem`, `svc.jwt`) destroyed after L4. One-night instrument per CTO
  001643Z — a durable serve-verification identity, if ever wanted, is a designed artifact with
  its own review, flagged as an open item, never a quiet re-mint.
- **Riding for awareness (CTO):** COO O4 — the artifact's trading-day calendar mechanism changed
  (hardcoded-fallback -> pandas_market_calendars), value-equivalent across all 447 shared dates
  tonight; frontier-definition change on record at CTO's desk. Andrew ~0059Z: "using NYSE
  official market calendar is the way to go for this."
- **Render-disclosure question (COO item 3, raised pre-render):** the three frontier dates carry
  cottonwood `carried_at_declared_cadence(as_of=2026-07-22)`; whether the portal renders a
  carried point distinguishably from a measured one is a disclosure question for DE/CTO — named
  here so Andrew hears it from us first.

## 2026-07-29T01:17Z — APPLY HALTED BY DT, ESCALATED TO CTO. NOTHING LANDED.

**AWS state UNCHANGED:** `public-data-router` still `:5` on `EVTSA9VEHNZVH`, distribution untouched,
serve still `json/mdpf/*`. L1 + L2a closed clean; **L2b (apply) HALTED BEFORE IT RAN.**

**Cause — the module carries held work that is one `apply` from live.** `terraform plan` on
portal-auth = **1 to add, 2 to change**, and exactly ONE line of it belongs to this deploy
(`public_data_router` s3_object_version, v5 -> v6). The rest is `0.7.0_AE_CloudOps`'
**MDPF_REVAMP.S5 CF flip**, committed `328248c135` (2026-07-22), subject verbatim *"HELD for
CTO+COO+Andrew re-land co-sign; apply the pinned plan on GO"*, whose predecessor `9a59360605` is
the **P0 rollback of the same flip** (*"buggy Global aggregate-aua on the live serve"*):
- `aws_cloudfront_origin_access_control.assets` CREATED — *"OAC for opal-data-assets MDPF served keys (Option C direct behaviors)"*
- `aws_cloudfront_distribution.portal` **+11 ordered_cache_behaviors** (live 24 -> 35; 7 further
  render as positional `path_pattern` rewrites; **0 removed**; the `origin` -/+ pairs are TF
  set-ordering noise — same `domain_name`/`origin_id` re-added, verified line-by-line).

**Why this is a mechanism swap, not a ride-along.** The 11 behaviors are EXACT-KEY and therefore
**more specific** than `/api/general/*`, so CloudFront matches them first and the request **never
reaches `public-data-router`** — the GO'd Mechanism-A branch would be inert on arrival. And they
target origin **`S3-opal-data-assets`** (the gold tree), while tonight's verified artifact — AE's
11/11, COO's PASS diff, `1,950,519,805.86` @ 07-27 — lives in
**`opal-data-portal-v2/platinum/mdpf/`**. Applying would have served clients an origin nobody
verified tonight.

**No `-target` rescues it:** the behaviors and this deploy's Lambda association live in the same
`aws_cloudfront_distribution.portal` resource; applying only the Lambda publishes v6 while the
distribution stays pinned to `:5` — no flip.

**Escalated:** CTO `011658Z` (ruling requested; recommendation **(A)** AE de-stages the S5 block —
their lane, held work preserved on a branch/patch — leaving this plan at exactly `1 to change`,
then apply tonight per Andrew's in-session order), AE `011720Z`, COO cc.
**Standing warning raised with both: the module is one un-targeted `apply` from ANY lane away from
landing S5.**

**Environment defect found + fixed en route (L2a):** `/tmp` resolved to `C:\Program Files\Git\tmp`
(unwritable — the build died at `mktemp`). Restored the mapping the build script's own comment
assumes, additively and non-durably: `mount -f C:/Users/AndrewBerman/AppData/Local/Temp /tmp`
(MSYS shared memory, dies on reboot; same class as the `mount -f C: /c` harness-rc fix).

## 2026-07-29T01:22–01:31Z — HALT CLEARED, FLIP LANDED AT THE ROUTING LAYER

AE de-staged S5 (`5bb23c45a6`, held block preserved verbatim in their deliverables + a tombstone
comment). **I re-planned myself** (CTO required my read, not AE's report): `Plan: 0 to add, 1 to
change, 0 to destroy`, the single change being `public_data_router[0]` `s3_object_version`; residue
grep for `S3-opal-data-assets|origin_access_control|path_pattern` = **0**.

**The documented version-pinning hazard fired, and the 0-diff step caught it.** Apply #1 published
`public-data-router:6` but the plan never listed the distribution — exactly the failure
`cloudfront-distribution.tf:59-64` documents (*"caught 2026-04-15 when auth-validator-edge v13 was
published but CF stayed pinned at v12"*). The post-apply re-plan surfaced
`aws_cloudfront_distribution.portal will be updated in-place`, diff = **only** `:5 -> :6` on both
router associations, zero residue. **Apply #2 landed it. Two applies were required, not one** —
reported rather than smoothed over.

| check | result |
|---|---|
| live CF association (applied plane) | `public-data-router:6` on `/api/general/*` AND `/api/general/json-tiered/*` |
| distribution | `Deployed`, **24** ordered behaviors (unchanged — no S5 residue landed) |
| TF 0-diff | `No changes. Your infrastructure matches the configuration.` |
| scoped invalidation | `I6PA7CJZQ07WPOHQGLTSYH11OP`, paths `/api/general/mdpf/*` only, **Completed** 01:31:42Z |

## 2026-07-29T01:33Z — INCIDENT: 403 ON ALL MDPF URLS (reader-grant absent)

**The re-point is correct; the origin refuses the read.** Root cause source-confirmed at 01:35Z,
~4 minutes from first observation — live `get-bucket-policy` on `opal-data-portal-v2`, statement
`AllowCloudFrontOACPublicData`:
```
Principal cloudfront.amazonaws.com · Action s3:GetObject
Resource  [ .../json/*, .../json-tiered/* ]          <-- platinum/* ABSENT
Condition AWS:SourceArn = .../EVTSA9VEHNZVH
```
The router rewrites to `/platinum/mdpf/...`; the OAC principal holds no grant on that prefix → S3
`AccessDenied` → CF 403 (body is the S3 AccessDenied XML). **AE confirmed the same absence in TF
desired state (`shared-infra/s3-portal-v2-import.tf:108`) — a grant never written, not drift.**

**Blast radius, MEASURED and CONFINED:**
```
/api/general/mdpf/{global,49financial,inflection,cottonwood}/agg-aua-ts   403  (4/4)
CONTROL  /api/general/portfolios/aum-metrics.json      200, 7,234 B == pre-flip byte size
NEGATIVE frozen json/mdpf/global   ETag 5f758b47 / 254,419 B / LM 13:41:05Z  UNMOVED
```
*(Stated honestly: a probe of `/api/general/json-tiered/positioning/latest.json` also returned 403,
but I hold NO pre-flip baseline for it and will not call it a regression — most likely a
nonexistent key. My baselined control is clean.)*

**THE MISS, owned:** I verified the platinum **keys existed** (11/11, hyphen spellings) and never
verified the **reader could reach them**. Presence is not access — READER-side. CTO's proportions
note (013747Z): the reader-reach check was in nobody's plan — not the WO-3 dispatch, not the WO-2
spec review; AE's WO-2 verify exercised the WRITER's path end-to-end only. **Standing item for the
WO-3 class going forward: every re-point verifies the reader's grant on the new prefix BEFORE the
flip.**

**Escalated, not self-authorized:** CTO 013530Z + AE 013548Z with both options priced
(fix-forward ~2 min, one Resource line / rollback ~10 min, byte-exact and still available). I
reverted nothing on my own initiative and touched no serve object or policy.

### RESOLUTION RULED — FIX FORWARD (sovereign + CTO, converging independently)
**ANDREW-DIRECT, VERBATIM, at the DT terminal 2026-07-29 ~0138Z:**
> *"no we're not wasting time rolling back, lets just do this properly in the first place and
> point to the right place with right permissions"*

Recorded + broadcast same turn (CTO 013844Z, COO 013907Z, MSTR 013925Z) per XXX.md. Scope surfaced,
**not adjudicated by me**: the second clause may reach past tonight's one-line fix — CTO/COO own
that read. **CTO ruled Option A independently at 013747Z**, ~1 minute before the sovereign word
arrived. AE executes the one-line append (`platinum/mdpf/*` → the existing OAC Resource array) —
the READ-direction twin of the exact prefix COO co-signed 221211Z for the publisher WRITE.

**Acceptance fires on AE's confirmation:** four mdpf URLs 200 + platinum content (global
`1,950,519,805.86` @ as_of_last 07-27), the 447-shared-date read against COO's free oracle (ANY
historical value change = routing/caching artifact → escalate, never rationalise), non-mdpf control
byte-identical, frozen `5f758b47` unmoved.

## Completion
*(open — awaiting AE's grant, then the acceptance battery; NEVER#6 window live, closes in-session)*
