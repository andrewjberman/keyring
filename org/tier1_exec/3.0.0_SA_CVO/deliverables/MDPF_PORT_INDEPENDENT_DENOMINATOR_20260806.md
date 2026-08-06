# MDPF EC2 port — the INDEPENDENT DENOMINATOR

**Seat:** `3.0.0_SA_CVO~Z` · **Authorized:** MSTR~Z, read-only, no TO required
**Purpose:** the listing the porter's claim gets checked AGAINST — never the porter's own list.
**Measured:** 2026-08-06, live plane `313476888478`/`us-east-1`. Read-only.

## Why this, and not a snapshot restore

`infra/aws/ec2/EC2_MANIFEST.json:425-443` registers instance `i-02448edb624a7a7cf`
(service `mdpf-daily-runner`) and declares its code home:

```
:436  code_prefix             s3://opal-data-mdpf/code/scripts/     "THE SCRIPT TREE"
:437  dispatch_script_prefix  s3://opal-data-mdpf/code/
:438  dispatch_script         s3://opal-data-mdpf/code/mdpf-daily-dispatch.sh
:441  source_path             infra/aws/ec2/mdpf-daily-runner
:443  parity_note             "runs the S3-staged mdpf chain (parity instrument = comp-pipescript deployed)"
```

Rule 8 (the manifest is the source of truth) meeting Rule 12 (S3 is the artifact store for ALL EC2
code) means **the port denominator's canonical home was never the volume.** It is S3 + the repo — 
enumerable read-only right now, and it **survives termination completely.**

The volume's only unique contribution is the residual delta (§4).

---

## 1. LEG A — dispatch/shell layer

**S3 `s3://opal-data-mdpf/code/` (depth-1) — DENOMINATOR: 3 objects**

```
code/mdpf-catchup-etlfix-ws3.sh
code/mdpf-daily-dispatch.sh
code/mdpf-dim-backfill-20260729.sh
```

**Repo `infra/aws/ec2/mdpf-daily-runner/` — DENOMINATOR: 4 files** (`comp-glob`, on-rails)

```
infra/aws/ec2/mdpf-daily-runner/mdpf-catchup-etlfix-ws3.sh
infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh
infra/aws/ec2/mdpf-daily-runner/mdpf-dim-backfill-20260729.sh
infra/aws/ec2/mdpf-daily-runner/user-data.sh
```

**Asymmetry, explained rather than left as a discrepancy:** the three shell scripts correspond 1:1.
`user-data.sh` exists in the repo and NOT in S3 — expected, because user-data is EC2 launch
configuration applied at instance creation, not an artifact the instance pulls from S3. **This is a
correct asymmetry, not a gap.** It is written down here so nobody later "discovers" it as a missing
port item, and so nobody ports it into a Lambda where it is meaningless.

## 2. LEG B — the script tree

**S3 `s3://opal-data-mdpf/code/scripts/` — DENOMINATOR: 38 objects**

```
assets_gold/  build_cottonwood_mdpf_pair.py · build_cottonwood_mdpf_slice.py
              build_dim_model_portfolio.py
backfill/     .crosswalk_cache.pkl · HANDOFF_AE_lambda_route.diff
              HANDOFF_AE_lambda_route.md · aggregate_aua_count_backfill_pre0518.json
              build_aggregate_aua_timeseries.py · build_custody_crosswalk_cache.py
              build_legacy_compat_emit.py · build_mdpf_count_backfill_pre0518.py
              build_mdpf_process_backfill.py · build_mdpf_v0_bandaid_backfill.py
bronze/       mdpf_stage0_token_gate.py · pull_orion_model_composition.py
feeders/      HANDOFF_DSA_wsd2_aggregator_wire.md · verify_wsd2_clears_identity2.py
              wsb_49f_smartx_model_aua.py · wsd_partner_held_etf.py
gold/         _trading_day_calendar.py · build_mdpf_etf_ownership_timeseries.py
              build_mdpf_etf_ownership_timeseries_fixtures.py · build_mdpf_spine.py
              build_mdpf_wsc_inflection_feeder.py · build_mdpf_wsd2_etf_netassets_feeder.py
              build_mdpf_wse_49f_non_model_aua.py · build_portal_gold_accrual.py
              dim_mdpf_account_distribution.py · dim_mdpf_aggregate_aua_timeseries.py
              dim_mdpf_aum_metrics.py · dim_mdpf_non_model_assets.py
              mdpf_aggregate_aua.py · mdpf_aggregate_aua_fixtures.py
              mdpf_model_registry.json · mdpf_revamp_model_crosswalk.py
              partner_roster.json · validate_schwab_native_custody.py
silver/       rebalancer_schemas.py
```

---

## 3. ⚠ THE DENOMINATOR HAS A DEFECT — 38 IS NOT 38 SCRIPTS

**Do not use 38 as the executable denominator.** The prefix mixes four content kinds, and a
"38 of 38 ported" claim computed off the raw count would be counting handoff notes as code:

| Kind | Count | Objects |
|---|---|---|
| Executable Python | **31** | the `.py` files above |
| Config JSON (likely PORT) | 2 | `mdpf_model_registry.json`, `partner_roster.json` |
| Backfill DATA (not code) | 1 | `aggregate_aua_count_backfill_pre0518.json` |
| Human handoff docs | 3 | 2× `HANDOFF_*.md`, 1× `HANDOFF_*.diff` |
| Binary cache artifact | 1 | `.crosswalk_cache.pkl` |

**`.crosswalk_cache.pkl` deserves its own line.** It is a **pickle cache in the code tree** — a
derived artifact stored beside source. It is neither code to port nor a config to carry, and its
presence means the prefix is not a clean code tree. If a port checklist treats it as a source file it
will be "ported" meaninglessly; if a cleanup treats it as deletable it may be a rebuild input.
**Someone must classify it deliberately, not by extension.**

**So the porter check is: 31 executable + 2 config = 33 items requiring a disposition, not 38.**
Each still needs one of MSTR~Z's three buckets — byte-identical to committed source / ported and
hash-tied in `BUILD_MANIFEST.json` / demonstrated unnecessary with evidence.

---

## 4. WHAT THIS LISTING DOES NOT COVER — the residual

This is the trunk, not the whole tree. The volume's unique contribution remains, and it is exactly
what `02_NEEDED_VS_NOT_AUDIT.md` names:

1. **"any EC2 script not directly visible in Stage 6 but used as a library or imported source"** — a
   file present on the volume and absent from both S3 and the repo.
2. **The runtime-installed package set** — 02 records the EC2 performs runtime package installation,
   which Lambda must not inherit. That resolved dependency state exists on the live volume.

**Neither is answerable from this listing, and neither is answerable read-only.** Determining them
requires `create-volume` from a snapshot + attach + mount — writes, and AE~Z's lane, not mine. Routed
to COO~Z as a TO. **I do not perform what I verify.**

## 5. Instrument blind spots

| Instrument | Blind to |
|---|---|
| `s3api list-objects-v2` (materialized keys, counted with `wc -l`, **never `length()`** on a paginated call) | Object *content*. Two keys with identical names and different bytes list identically. Also blind to anything deleted before today — this is current-state. |
| `comp-glob` (on-rails, .gitignore-aware) | Uncommitted and gitignored files. Its 4-file result is 4 *tracked* files. |
| `EC2_MANIFEST.json` | Reality. It is a **declaration** of where code should live (Rule 8 source-of-truth), not a measurement that the instance obeys it. **The entire residual in §4 is the case where the instance did not.** |

**The load-bearing caveat:** this listing establishes what the code home *should* contain per the
estate's own law. It cannot, by construction, establish that nothing exists outside it. That is §4,
and it stays open.

## 6. Recommended reconciliation instrument

`EC2_MANIFEST.json:443` names it: **`comp-pipescript deployed`** — MATCH/STALE/MISSING between repo
source and the deployed S3 artifact. Use it rather than a hand-diff for Leg B; a hand-diff of 38 keys
is exactly where a silent miss lands. Per CLAUDE.md the flagless no-arg mode is the one correctly
flagless (all-trees, firm-separated).

---

*Read-only. No repository file outside this deliverable, no AWS resource, S3 object, or served
artifact was changed in producing it.*
