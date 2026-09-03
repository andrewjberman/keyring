---
name: mdpf-refresh
description: Fresh gold run + platinum publish for MDPF Model Portfolios in one invocation: fires the same Lambdas the production schedules target (floor -> accrual -> publisher; optionally the COT/INF legs first), waits each leg, verifies every firm scope's served platinum against trading-calendar T-1. Use on "refresh mdpf", "fresh gold run", "re-publish model portfolios", "reset run". Any agent for status/gold/full; `--reland` needs Andrew's explicit in-session word.
---

# /mdpf-refresh — fresh gold + platinum reset run for MDPF

**Driver:** `mdpf_refresh.py` in this skill directory. Pure boto3 (no subprocess `aws` — the
MSYS argv class never enters), device-agnostic (repo root via `git rev-parse`), ASCII-only.

**Authorization / lineage:** Andrew-direct 2026-08-14 ~1517Z, recorded verbatim at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260814_EMITTER_EMPLOY_AND_REFRESH_SKILL.md`.
Chain shape is the exercised AE tonight-refresh
(`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-14/session_0541-0625Z_mdpf_trgaln_tonight_refresh.md`).

## What one invocation does

| Form | Behavior |
|---|---|
| `/mdpf-refresh status` | READ-ONLY preflight: expected T-1 (trading calendar, never wall-clock), per-scope platinum `as_of_last` + write time, monolith input partition frontiers (49F smartx+schwab, INF orion+eclipse, COT bd holdings + dim). Zero invocations. |
| `/mdpf-refresh` (= `gold`) | Preflight, then: **floor** (`mdpf-gold-lambda`) -> conflict scan of the run manifest -> **accrual** (`mdpf-accrual-trigger`, SSM polled to terminal) -> **publisher** (`opal-assets-mdpf-portal-publisher`) -> **verify** each scope's platinum `as_of_last == T-1` and freshly written, plus the inflection reconstructed-dates/empty-dates transparency line. Assumes monolith inputs are current (preflight shows you). |
| `/mdpf-refresh full` | The COT + INF vendor/mirror legs FIRST (cot session via SSM -> cot mirror; INF jwt -> reps -> accounts -> bronze-runner -> assets -> eclipse -> positions -> txn -> inf mirror), then everything `gold` does. **49F vendor legs are morning FILE DELIVERIES — not ad-hoc invocable; preflight reports their freshness, nothing fires them.** |
| `--reland` / `--reland --confirm` | See CONFLICT PROTOCOL below. |

Run it: `python .claude/skills/mdpf-refresh/mdpf_refresh.py [status|gold|full] [--reland [--confirm]]`

## CONFLICT PROTOCOL (the guard you WILL meet on a same-day re-run)

The gold consolidator's conditional-put guard (`mdpf_gold_consolidator.py` A8) records
business-different content at an EXISTING dated gold key as **`conflict` — held, never
overwritten, no override parameter by design.** A reset run that recomputes existing dates
(new reconstruction artifacts, corrected inputs, same-day re-publish) will hold exactly those
keys; the driver prints them from the run manifest (`portal/gold/mdpf/_manifests/`).

Resolution is delete-and-re-land of the named keys (all regenerable derivatives):
1. **Take Andrew's explicit in-session word first** — this is a RESERVED-CATEGORY act; do not
   infer it from "fresh run" (COO boundary ruling, held four times on 2026-08-14 alone).
2. `--reland` lists the conflicted keys (dry-run, always safe).
3. `--reland --confirm` deletes EXACTLY those keys, then re-run `gold` to re-land them.
Platinum keys are never deleted by this skill; the publisher re-publishes platinum in place.

## Design rules this skill honors (do not "improve" them away)

- **The schedules stay the production path.** This is the sanctioned ad-hoc accelerator
  (run-and-read); its artifacts are never production evidence; ad-hoc invokes carry a
  non-`aws.events` source label so the A6 run manifest records the kind honestly.
- **No watchers, alarms, monitors, or SNS/SES are armed** (standing moratorium 2026-07-28).
  Verification is artifact reads, in-line, same run.
- **DOOR 6:** the INF gold sentinel (`opal-data-inf/gold/meta/pipeline-complete.json`) is
  NEVER hand-written — that is a forged completion signal. Serving does not need it.
- **T-1 is trading-calendar-resolved** (`lib/trading_calendar`), never wall-clock (NEVER#1).
- Known ceilings the driver reports rather than fights: BD bakes ~01:02 ET (a COT session
  before that re-lands the prior snapshot — the ingest's own floors refuse partials);
  Orion values T-1 overnight; schwab/smartx are morning deliveries. An early-hours `full`
  run aligns everything to the freshest VENDOR truth, which may legitimately be T-2.

## Known residuals (surfaced, not fought here)

- Publisher IAM degradation (pre-existing, in its own manifest): egress role lacks
  `s3:GetObject` on `platinum/mdpf/_manifests/latest.json` — prior-pointer read fails,
  publish unaffected.
- `inf-api-eclipse` writes the BR1 staging prefix (`bronze/eclipse_qa/`) until the Gate-3
  cut — inert to serving; production eclipse bronze rides the bronze-runner EC2 leg.
- Portal edge caching: platinum rewrites surface on TTL; if a just-published change must be
  visible instantly, the edge invalidation is a DT/CTO act, not this skill's.
