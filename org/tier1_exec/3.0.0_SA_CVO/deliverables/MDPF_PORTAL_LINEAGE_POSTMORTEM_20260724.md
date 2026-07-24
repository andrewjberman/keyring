# MDPF Model-Portfolios — Served-State Lineage Postmortem

    author:        3.0.0_SA_CVO  (folds two independent parallel traces)
    traces folded: 2.0.0_SA_COO  — MDPF_PORTAL_LINEAGE_BRIEFING_20260724.md (provenance-stamp route)
                   3.0.0_SA_CVO  — this session's live trace (ETag-version route)
    date:          2026-07-24
    authorization: Andrew-direct write during the ~1943Z fabric pause ("fold both traces
                   into the postmortem record and commit it"). Read-only investigation
                   throughout; this commit is the single authorized write.
    grounding tag: every load-bearing claim is [MEASURED] (live AWS / HAR / source @commit)
                   or [INFERRED] (reasoned from measured facts). No claim in this record is
                   single-sourced: each is ETag/source-proven OR agreed by both traces.

---

## 0. The question, and the answer in one paragraph

Andrew asked, end to end: what does the portal actually serve for Model Portfolios, what
writes it, on what schedule, where does its data come from, and what triggers the ingestion
behind it. **Answer:** the portal serves four per-firm+global JSON artifacts from
`opal-data-portal-v2/json/mdpf/`, whose bytes are **byte-identical copies of the
`opal-data-assets` monolith gold output** (proven two independent ways). Ingestion upstream is
fully scheduled. **The single failure is the last hop:** the gold→served publish is a
**manual, ad-hoc, uncommitted DS procedure with no schedule on either AWS scheduling
surface**, and it was hand-run on 07-23 to correctly serve 07-22 data. That manual hop, plus
the absence of a freshness monitor and a deployed producer 23 commits behind HEAD, is why the
product froze 07-18→07-23 and only advanced when a person pushed it. **Andrew's hypothesis is
confirmed in full; his architecture recollection is correct on the serve side, with one
correction on where the daily append lives.**

---

## 1. Read path — what the portal serves [MEASURED, both traces]

Ground truth = the browser HAR Andrew recorded (`opalinvest.dev2.har`, 36 requests, 12
data-fetches). The ModelPortfolios page fetches, all HTTP 200, all `server: AmazonS3` via
CloudFront:

| Request `/api/general/mdpf/…` | Served object | HAR ETag ↔ live | data as_of |
|---|---|---|---|
| `global/aggregate-aua-timeseries.json` | `opal-data-portal-v2/json/mdpf/global/…` | `55a8b379…` ✓ | 2026-07-22 |
| `49financial/aggregate-aua-timeseries.json` | `…/json/mdpf/49financial/…` | `50140744…` ✓ | 2026-07-22 |
| `inflection/aggregate-aua-timeseries.json` | `…/json/mdpf/inflection/…` | `e3c8db35…` ✓ | 2026-07-22 |
| `cottonwood/aggregate-aua-timeseries.json` | `…/json/mdpf/cottonwood/…` | `194e5bb0…` ✓ | 2026-07-22 |

Plus `account-distribution.json` per firm and a legacy `portfolios/*` set (§7). **Every HAR
ETag matches the live `opal-data-portal-v2` object byte-for-byte.**

**Serving path (deployed CloudFront `EVTSA9VEHNZVH`, verified live):**
browser → `/api/general/*` → behavior 18 → `public-data-router` Lambda@Edge rewrites
`/api/general/*` → `/json/*` → **S3 `opal-data-portal-v2`**. The deployed origin for that
behavior is `opal-data-portal-v2`, **not** the monolith. The cutover to serve from the
monolith has not happened.

> **Conclusion:** the portal READS `opal-data-portal-v2/json/mdpf/`, not the monolith directly.

---

## 2. Lineage — the served bytes ARE the monolith gold output [MEASURED, two independent proofs]

**Proof A — ETag identity to monolith gold VERSIONS (CVO route).** Each served ETag appears
verbatim as a version of the monolith staging object (S3 versioning is on):

| Served (portal-v2, hyphen key) | = version of (monolith `opal-data-assets`, underscore key) |
|---|---|
| global `55a8b379` | `gold/mdpf_revamp/global/aggregate_aua_timeseries.json` @ **20:55:16Z** |
| 49financial `50140744` | `gold/mdpf_revamp/49financial/…` @ **21:44:30Z** |
| inflection `e3c8db35` | `gold/mdpf_revamp/inflection/…` @ **21:44:30Z** |
| cottonwood `194e5bb0` | `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries_**interpolated**.json` @ **21:45:49Z** |

An ETag is a content hash; a match is identity. (Note cottonwood descends from the
`_interpolated` gold variant, the other three from the plain underscore key.)

**Proof B — in-file provenance stamp (COO route).** The served files self-describe:
`meta.basis="schwab-rps"`, `meta.generated_at="2026-07-23T21:43:50Z"`, `as_of_last="2026-07-22"`,
`source_vintage_last.semantics="…REVAMP-SILVER honest provenance … the REVAMP's OWN consumed
AUA-bearing sources (model_aua = smartx aum_daily [49F] / eclipse fact_portfolios_full [inf])"`.
The feeders named are all `opal-data-assets` monolith silver (`channel_sources.py:56-64`,
`MONOLITH_BUCKET="opal-data-assets"`): `schwab/08242234/silver/fact_rps_s2`,
`smartx/platform/silver/fact_model_aum_daily` + `fact_model_allocation_roster`,
`orion/inflection/silver/fact_assets`, `eclipse/inflection/silver/fact_portfolios_full`,
`blackdiamond/cottonwood/silver/fact_holdings`.

> **Conclusion:** served content is the monolith REVAMP output, as_of 07-22, generated 07-23.
> **Andrew's hypothesis — "lineage is the monolith, we just sent it to portal-v2" — CONFIRMED.**
> Two independent derivations agree; this is the record's most robust claim.

**Key-naming trap (both traces, recorded so no reader conflates them):** monolith STAGING key
is **underscore** (`aggregate_aua_timeseries.json`); portal SERVE key is **hyphen**
(`aggregate-aua-timeseries.json`). The publish renames across buckets. The monolith *hyphen*
key **404s** (COO §2, correct — it does not exist); the monolith *underscore* key **exists and
ETag-matches** (CVO Proof A). Both true; different keys.

---

## 3. Producer — who wrote the code [MEASURED]

Producer = `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, fingerprinted
uniquely (`REVAMP-SILVER`/`serve_real_D1`/`schwab-rps` exist in that file and no other under
`data/mdpf/scripts`).

- **Created:** commit `f4a4091823`, **2026-07-20 16:47:21 EDT**, author
  **`0.4.0_DS_ClientPlatform`** (`git log --diff-filter=A`). Subject: *"feat(MDPF_REVAMP): TO-0
  … Spine skeleton reads monolith silver (aum_daily + roster basis + fact_rps custody), emits
  the served F4 shape."*
- **It does not publish.** Args are `--out-dir` (local) and `--dry-run` only (`:2014-2019`);
  no `--upload`, and its only touch of `SERVED_BUCKET` is a `get_object` READ (`:568`, the
  self-referential prior-output read). It writes a local dir; something else moves bytes to S3.
- **The deployed copy is stale.** Deployed producer artifact = **51,999 B, 2026-07-21T17:42Z**;
  repo HEAD = **124,241 B / 23 commits ahead** on that path (E3 from the pause validation).

Distinct, do not conflate: `channel_sources.py` (four-channel re-source) authored by
`0.7.0_AE_CloudOps` (`d263bf93b2`, 07-23) feeds the **DDB emitter** path, a separate concern.

---

## 4. The publish — how bytes reached the served location [MEASURED + SOURCE-CONFIRMED]

**This is the failure. The gold→served publish is a manual, uncommitted, unscheduled DS
procedure.** No deployed component in the daily chain writes `portal-v2/json/mdpf/*`.

- **The scheduled dispatch stages only, and holds publishing OFF.** `mdpf-daily-dispatch.sh`
  (EC2 runner `i-02448edb624a7a7cf`) runs the producer `--out-dir`, then `aws s3 cp` to
  `opal-data-assets/gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json` (rolling overwrite,
  16 S3 versions), and logs verbatim **"publisher OFF, publish HELD."**
- **The committed publisher is the wrong shape and unwired.**
  `opal-assets-mdpf-portal-publisher` does a **same-bucket** copy *within* `opal-data-assets`
  (`gold/mdpf_revamp/*` → `json/mdpf/*`, `copy_object(Bucket=BUCKET, CopySource={Bucket:BUCKET})`,
  `BUCKET=opal-data-assets`), built as a "build-alongside" for a future CloudFront cutover. It
  has **no EventBridge rule, no schedule, no S3 notification, and no resource policy**
  (manual-invoke-only by construction). It did **not** write the live portal-v2 keys.
- **What actually wrote them: a DS-run procedure, 07-23 evening.** Source-confirmed from the DS
  session log `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-07-23/p1_broken_charts_a2_serve_perfirm_counts.md`
  and the deploy ledger `20260723T1849Z_mdpf-allfirms-serve_deploy_completion.md`:
  per-key `staged-md5 → put → fresh-GET byte-compare → ListObjectsV2` — a hand-run put/copy
  procedure, byte-verified each key, **not a checked-in script.**
  Authority: opened by `0.4.0_DS_ClientPlatform`; **CTO serve-fire 184804Z on COO clean
  counter-sign 184724Z + DE render evidence** (never-widen co-sign satisfied).
- **CloudTrail S3 data events are OFF** — writer identity comes from the ledger + version
  history + the DS log, not CloudTrail. It was never needed.

---

## 5. THE LEAD IMPLEMENTATION FINDING — the serve was NON-ATOMIC [MEASURED]

*(This is the sharpest actionable item and the one divergence the two parallel traces
surfaced. COO's briefing first read the iteration times as uniform across firms; CVO's
independent read of the global key showed they are not. Resolved below — the disagreement was
the finding, exactly as the parallel-trace design intends.)*

Serve write-times on `portal-v2`, per key, differ:

| | write 1 | write 2 | write 3 |
|---|---|---|---|
| **49financial** | 18:49:04Z | 20:57:16Z | **21:47:06Z** |
| **global** | 19:29:40Z | **21:18:53Z** | *(none)* |

The DS log resolves the mechanism: **global's 21:18:53 write was a CORRECTIVE byte-copy** — DE's
parity gate (COO `211752Z`) caught the W-7 count artifact published to the wrong key
(top-level `json/mdpf/aggregate-aua-timeseries.json`, which *no* Global consumer reads — the
consumed key is the `/global/` sibling); DS byte-copied `55a8b379 → /global/`, COO byte-confirmed.
**The per-firm 21:47 writes were a separate count-defect fix** (`@3efc9dc6d`).

**Consequence:** the currently-served **global (`55a8b379`, from the 20:55 gold generation) is
~52 minutes / one gold build OLDER than the currently-served per-firm objects (21:44
generation).** It **reconciles numerically** (CVO residual sweep across all 407 non-null dates:
Global = Σ per-firm on 406, sole exception 07-22 frontier +92, which is SMA-preserve +85 +
roster-split +7 — a known, non-firm-attributable composition residual). **So it is NOT a data
defect** — but it is a fragile publish pattern.

> **REQUIREMENT for the scheduled publisher:** it must write **all four artifacts atomically
> from a single gold generation in one run.** A per-key hand-run publish is exactly how the
> served global and per-firm drifted onto different gold builds. Both traces explicitly
> DECLINED to "fix" the skew by re-serving — a re-run would manufacture a third gold-gen mix;
> the fix is the atomic publisher, not another hand-run.

---

## 6. Renderer re-point — DT, 07-23 [MEASURED, two-trace-confirmed]

Portal DEV→PROD promotes pointed the renderer at the hyphenated `json/mdpf/*` keys:

- **v2.1.145** `5bc8be7e` — subject verbatim: *"ACTIVATE MDPF Global view (cottonwood-inclusive)
  + **point renderer at json/mdpf/\* serving keys**"* — authored `0.2.0_DT_PortfolioAnalytics`.
- v2.1.146 `41ce41eb`, v2.1.147 `7ac7bafd`, v2.1.148 `17256834` (deployed PROD head, pin
  `@343e7b2a`) — all `0.2.0_DT_PortfolioAnalytics`.
- Ledgers: `…1943Z_mdpf-global-view-activate-promote`, `…2020Z`, `…2052Z`, `…2215Z`.

*(Originally single-sourced in COO's briefing; CVO cross-checked it at source — the caveat is
retired.)*

---

## 7. Separate thread — account-distribution [MEASURED that it differs]

`account-distribution.json` (49F/inf) has a **different, fresher** writer — Last-Modified
**2026-07-24 11:30:39Z**, distinct from the 07-23 aggregate serve. Grep points to
`compute_per_firm_account_distribution.py` (SmartX pipeline). Andrew's screenshot (the "Daily
AUM Analysis" chart) is `aggregate-aua-timeseries.json`, the DS revamp serve. **The
account-distribution serve is a separate thread and is NOT traced to its run here** — do not
unify the two in remediation until it is independently traced. [writer INFERRED from grep.]

---

## 8. Schedule surfaces — the whole answer to "does it have scheduling" [MEASURED]

**Two AWS scheduling services exist; `aws events list-rules` sees only one.** Both checked:

- **EventBridge Rules (141, paginated):** exactly 1 matches mdpf — `mdpf-daily-refresh-trigger`,
  **not a cron**: it fires on an S3 event, `opal-data-inf/gold/meta/pipeline-complete.json`
  (Object Created) → `mdpf-daily-trigger`. **MDPF has no schedule of its own; the whole chain
  is a passenger on Inflection's completion.** No Rule writes `portal-v2/json/mdpf`.
- **EventBridge Scheduler (10, separate service):** none touch mdpf/publish/portal. (This
  surface is invisible to `list-rules` — an instrument-boundary trap; the ingestion pullers
  below live here.)

**Ingestion is fully scheduled across BOTH surfaces:**

| Channel | Triggers (cron unless noted) |
|---|---|
| SmartX / 49F model | `smartx-account-distribution-daily` 11:30 · `opal-assets-silver-smartx-sweep-daily` 16:00 · **Scheduler:** `wsb-49f-model-aua-pull-daily` 03:30 Tue–Sat, `smartx-assets/rest/jwt` |
| Schwab / 49F custody | `canonical-schwab-si2-08242234-daily-pull` 10:15+22:15 · `opal-assets-silver-schwab-sweep-daily` 12:15 |
| Eclipse+Orion / INF | `inf-*` suite 13:xx–14:xx · `opal-assets-silver-eclipse/orion-sweep-daily` 16:00 · event chain → `pipeline-complete.json` (which fires MDPF) |
| Black Diamond / COT | `cot-rebalancer-runner-daily` 06:00 · `bd-*-pipeline-trigger` 21:xx · `opal-assets-silver-blackdiamond-sweep-daily` 05:00 · `opal-assets-ingest-mirror-cot-daily` 03:30 |

> **The gap, precisely:** ingestion is scheduled on both surfaces; the **final gold→served
> publish is scheduled on neither.** That hop is a person running the DS procedure.

---

## 9. Architecture reconciliation — Andrew's recollection vs what is built [MEASURED]

Andrew: *"daily appends in `opal-data-assets` in a gold mdpf-tagged subfolder, with overwrites
to the read location inside `opal-data-portal-v2`."*

- **Overwrite to the portal-v2 read location — CORRECT.** Single key per firm, overwritten in
  place. The code even names portal-v2 the **`PLATINUM_BUCKET`**, matching Andrew's gold→platinum
  framing.
- **The daily APPEND is not in gold — correction.** The true dated daily append lives in **DynamoDB
  `opal-assets-daily-aua`** (34,950 items) and in **`portal-v2/platinum/mdpf/aggregate_aua/{date}.json`**
  (dated, but in the portal/platinum bucket, **frozen at 07-18**). The `gold/mdpf_revamp/{firm}/…`
  files are **rolling overwrites** whose daily audit trail is S3 object-versioning, not
  date-partitioned keys. If dated appends *in gold* were the intent, that is not what is built.

---

## 10. The 07-18 confound + why the freeze persisted [MEASURED]

- **Dead legacy platinum path:** `mdpf_aggregate_aua.py` → `platinum/mdpf/aggregate_aua/{date}.json`
  → `build_aggregate_aua_timeseries.py` (reads `platinum`, docstring still claims to feed
  `json/mdpf/`). That path **died 07-18** and is a code/reality drift trap for the next reader.
  The live serving path bypassed it on 07-23.
- **Why the product froze 07-18 → 07-23** (three named absences, one problem):
  1. **No schedule on the final publish (§8)** — it only advances when hand-run.
  2. **No freshness monitor** — `mdpf-freshness-checker` Lambda / trigger / alarm are all named
     in the census and **absent live**; the 3 alarms that exist fire on failure, not on
     "never ran." (E2, pause validation.)
  3. **Deployed producer 23 commits stale (§3).**
  Served version history confirms the freeze: writes at 07-08, 07-10, 07-16(×2), 07-17, 07-18,
  then a four-day gap, then two hand-runs 07-23.

---

## 11. Cleanup / implementation candidates — surfaced, not adjudicated (for CTO routing)

1. **Build the scheduled publisher for the last hop** (gold `opal-data-assets/gold/mdpf_revamp/*`
   → served `opal-data-portal-v2/json/mdpf/*`), **atomic across all four artifacts from one gold
   generation (§5)**, on a schedule, replacing the manual DS procedure. This is the amended
   NEVER#4 ("a production pipeline must have a schedule") applied to the exact live gap.
2. **Emit the colocated daily manifest** with per-channel `as_of` (Andrew's plan). Today
   `mdpf-manifest` is **not a deployed function** (function-not-found); it runs ad-hoc to a
   `gold/mdpf/_manifests_qa/` QA prefix, no schedule, no production/colocated manifest.
3. **Finish or retire the cutover.** The committed publisher writes `opal-data-assets/json/mdpf/`
   (build-alongside) while CloudFront still serves `opal-data-portal-v2`. Decide the intended
   served origin and converge — either re-point behavior 18 at the monolith, or make the
   publisher's destination portal-v2.
4. **Restore a freshness monitor** on the served artifact (E2) — one that fires on "chain did not
   run," not only on failure.
5. **Kill the code/reality drift trap** — `build_aggregate_aua_timeseries.py`'s stale docstrings
   (§10); a scheduled re-enable that trusts them would serve 07-18 data.
6. **Trace the account-distribution thread (§7)** before remediation unifies it with the aggregate.

---

## Appendix — reproduction (read-only, exact)

```
# Read path (HAR ETag ↔ live object)
aws s3api head-object --bucket opal-data-portal-v2 --key json/mdpf/49financial/aggregate-aua-timeseries.json --query '[ETag,LastModified,ContentLength]'
  -> "501407448f554a77a7ff7e2a5dceb954"  2026-07-23T21:47:06Z  183004
aws s3api head-object --bucket opal-data-assets --key gold/mdpf_revamp/49financial/aggregate-aua-timeseries.json
  -> 404  (monolith HYPHEN key absent; portal does not read it)

# Lineage (Proof A: served ETag == monolith gold underscore-key version)
aws s3api list-object-versions --bucket opal-data-assets --prefix gold/mdpf_revamp/global/aggregate_aua_timeseries.json
  -> version 2026-07-23T20:55:16Z ETag 55a8b379…  == served global ETag
aws s3api list-object-versions --bucket opal-data-assets --prefix gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries_interpolated.json
  -> version 2026-07-23T21:45:49Z ETag 194e5bb0…  == served cottonwood ETag

# Non-atomic serve (§5)
aws s3api list-object-versions --bucket opal-data-portal-v2 --prefix json/mdpf/global/aggregate-aua-timeseries.json
  -> 2026-07-23T21:18:53Z 254419 55a8b379 ; 19:29:40Z 242414          (2 writes)
aws s3api list-object-versions --bucket opal-data-portal-v2 --prefix json/mdpf/49financial/aggregate-aua-timeseries.json
  -> 21:47:06Z 183004 501407448 ; 20:57:16Z ; 18:49:04Z              (3 writes)

# Producer creation
git log --diff-filter=A -- data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
  -> f4a4091823 | 2026-07-20T16:47:21-04:00 | 0.4.0_DS_ClientPlatform

# Schedule surfaces (BOTH)
aws events list-rules            (paginate) -> 141 rules; 1 mdpf (event, not cron); none write portal-v2/json/mdpf
aws scheduler list-schedules                 -> 10 schedules; none mdpf/publish/portal; wsb-49f-model-aua-pull-daily lives here

# Serving origin (deployed)
aws cloudfront get-distribution-config --id EVTSA9VEHNZVH  -> behavior /api/general/* origin = S3-opal-data-portal-v2

# Publisher (build-alongside, same-bucket, NOT the live writer)
infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py  (BUCKET=opal-data-assets, same-bucket copy_object; no resource policy)
```

**Source-of-record for the two folded traces:**
- COO: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_PORTAL_LINEAGE_BRIEFING_20260724.md`
  (corrected; §5b carries the CORRECTED per-firm/global cadence note).
- CVO: this session's live trace (this document).
- Serve authorship ledger: `org/critical_paths/change_management/20260723T1849Z_mdpf-allfirms-serve_deploy_completion.md`.
- DS serve log: `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-07-23/p1_broken_charts_a2_serve_perfirm_counts.md`.

— 3.0.0_SA_CVO, folding 2.0.0_SA_COO
