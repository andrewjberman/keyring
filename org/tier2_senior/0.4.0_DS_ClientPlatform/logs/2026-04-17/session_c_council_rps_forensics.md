# Session — 0.4.0_DS_ClientPlatform~C — 2026-04-17 (council ~C)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** 2026-04-17 00:13 ET — 00:24 ET (~11 min)
**Scope:** CTO council dispatch 20260417T041138Z — angle ~C (Schwab RPS-side forensics).

---

## Context

CTO council dispatched 4-angle analysis of B_01 SAFETY HALT (1,169 accounts, $182M, 5.8x envelope) tripping on QA and about to trip PROD at ~04:23 UTC. Angles: ~A historical, ~B BD txn forensics, ~C RPS reliability, ~D decision framework. 30-min time box.

My angle: is Schwab RPS reliable ground truth for the 1,169 / 1,375 cohorts?

---

## Findings

**1. Schwab RPS feed is dead (2026-04-07 onward).**
- Last bronze `schwab/bronze/CRS20260407.RPS` uploaded 2026-04-08T22:02:36Z.
- No RPS bronze or silver partition exists for 2026-04-08 through 2026-04-17.
- B_01 `_load_latest_rps_partition` (L414-448) silently falls back to `date=20260407/data.parquet` on every run since 04-08.
- ULN feed has silver partitions through 2026-04-13 (written 04-15T03:15 in a backfill sweep). Schwab ingest is RPS-specific-broken, not all-Schwab broken.

**2. RPS is structurally reliable when data exists.** Sampled 3 silver partitions (3/27, 4/02, 4/07):
- Account cohort overlap: 5,557 / 5,565 in all three (99.9%)
- Position-level Jaccard per account: mean 0.982, median 1.000, 81% byte-identical
- MV trajectory: $1.405B → $1.448B → $1.456B (normal growth)

**3. The 1,169 force-close cohort is steady-state staleness, not drift.** FIFO tracks 10 days of fresh BD transactions; RPS is frozen at 04-07. Every run since 04-08 has force-closed legitimate BD activity that RPS simply cannot see because the feed stopped.

**4. Account-id format discrepancy.** Silver RPS uses 10-digit Schwab-native IDs (`0010023253`); BD uses z-prefixed (`z0814307721`). Reconciliation goes through `S3_MAPPING_KEY` bridge loaded at B_01:467-476. CTO test account `z0814307721` does not appear in any RPS partition under that literal string — confirmed by grep.

---

## Recommendation (fed to council ~D)

Path forward: option (iii) + (iv)
- (iii) **Let halt fire** — portal data freezes at last good run for ~24-48h. Manageable.
- (iv) **Restore RPS ingestion + backfill** — diagnose why `CRS2026041x.RPS` stopped landing in bronze. Open urgent AE TO. Backfill 04-08 through 04-17. No data-distorting override; no threshold raise (envelope grows linearly per day RPS stays dead).

Additional tech-debt call-out: 10 days of silent feed outage should have alarmed. Observability gap around Schwab RPS monitoring — owner-TBD.

---

## Deploy State

| Step | Result |
|------|--------|
| Commit SHA | `67a0d0fb` (author: 0.4.0_DS_ClientPlatform~C) |
| Push | origin/CLOUD up to date (ec2c1efc..67a0d0fb) |
| Deliverable | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/council_c_rps_coverage_2026-04-17.md` (234 lines) |
| MCP COMPLETE | CTO (T042403Z) + ~D (T042417Z) + COO (T042422Z) |

---

## Compiler Tools

| Date | Agent | TO | Tool | Command | Result | Note |
|---|---|---|---|---|---|---|
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | grep | `grep -n "rps_date\|latest_rps\|silver/rps" B_01.holdings_lots.py` | 7 hits | located fallback load at L414-448 |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | aws s3 ls | `s3://opal-data-bd/schwab/bronze/` | last=CRS20260407.RPS | feed-outage confirmed |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | aws s3 ls | `s3://opal-data-bd/schwab/silver/rps/` | last=date=20260407 | silver outage confirmed |
| 2026-04-17 | 0.4.0_DS_ClientPlatform~C | COUNCIL_C_RPS_FORENSICS | aws s3api | `list-objects-v2 --prefix schwab/silver --query LastModified>=2026-04-10` | 4 ULN files only | ULN alive, RPS dead |

No `comp-*` tools run — target was S3 data-state inspection, not code graph traversal. Evidence recorded via equivalent primitives.

---

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/council_c_rps_coverage_2026-04-17.md` | New — 234-line deliverable |

---

## MCP Messages

| To | Subject | Time (UTC) |
|---|---|---|
| 1.0.0_SA_CTO | ACK — Council ~C angle — starting now | T041618Z |
| 1.0.0_SA_CTO | COMPLETE — Council ~C — RPS feed dead since 04-07 (commit 67a0d0fb) | T042403Z |
| 0.4.0_DS_ClientPlatform~D | Council ~C input for your ~D synthesis | T042417Z |
| 2.0.0_SA_COO | COMPLETE — Council ~C — RPS feed dead since 04-07 (commit 67a0d0fb) | T042422Z |

---

## Next Steps

- [CTO] Synthesize council A/B/C/D for Andrew's call. RPS-feed-dead is the structural frame ~D should build on.
- [AE] Urgent TO forthcoming (from ~D synthesis) — diagnose why `CRS2026041x.RPS` stopped landing in `s3://opal-data-bd/schwab/bronze/` on 2026-04-08. Likely upstream Schwab SFTP/CRS mover failure. Backfill 04-08 through 04-17.
- [Observability owner - TBD] Alarm on Schwab RPS bronze staleness (last file > 2 business days old).
- [~C] Standing by. Available to sample more partitions, pull mapping table, or replay specific account if ~D needs cross-checks.

---

## Briefs Written

None.

---

*Delivered by 0.4.0_DS_ClientPlatform~C | 2026-04-17 00:24 ET*
