# Project Backlog — Post-Close Follow-Ons + Pending Auto-Close Triggers

Standing COO registry of (a) follow-on work re-homed out of CLOSED projects so it
isn't orphaned, and (b) DEFERRED projects carrying an auto-close trigger (they close
automatically when a named gate is met, without a fresh decomposition).

Created 2026-06-16 (2.0.0_SA_COO) during the CTO Andrew-direct closeout sweep
(NFRA_TOOLHUD / ADVI_49NNAFIX / NFRA_GLOBGRPH closed; 4 projects deferred-with-trigger).
Authoritative per-item state lives in each `org/projects/{CODE}.json`; this file is the index.

---

## Post-Close Follow-Ons (re-homed from closed projects)

| From (closed) | Follow-on | Owner | Gate / when |
|---|---|---|---|
| `NFRA_TOOLHUD` | CVO telemetry-tuning: re-run `hud3_classify.py` post-hook over the new-transcript window = the AFTER measurement (TIER-1 comp-answerable rate should DROP; flat = ignorable-noise -> kill/retune); then tune #1 hook patterns + #2 router rule-weights to the per-class accept/ignore signal; consider Read-class + Bash-grep coverage if #3's TIER-2 (~9%) warrants. | CVO (3.0) | After a meaningful post-hook transcript window accrues; measurement-effectiveness, not blocking. |
| `NFRA_GLOBGRPH` | TO-MAINT — standing nightly-Iceberg maintenance (expire-snapshots / compaction on the globgrph Iceberg tables). | AE (0.7) | Standing cadence (nightly piggyback). |
| `NFRA_GLOBGRPH` | ICEBERG-409 — backlog hardening item carried from the 409-commit-storm work. | AE (0.7) | Opportunistic. |
| `NFRA_GLOBGRPH` | L4 — derive-rebuild to full current-state marker (TF-managed standing `globgrph-derive` CodeBuild project; none exists yet). | AE (0.7) | Non-urgent. |
| `NFRA_GLOBGRPH` | L5 — purge stale ~99%-readOnly SQS(37.5k)/DLQ(15.2k) + RE-ENABLE incremental ESM (codified `enabled=false` meanwhile). | AE (0.7) | Gated on ingest-filter LIVE + backlog purged. |
| `NFRA_GLOBGRPH` | TO-Q1 — comp-queue in-flight (uncommitted) event visibility in the comp-kuzu provenance header (P3 enhancement; re-homed 2026-06-18 from AE TO-recon zombie-sweep, TO closed-superseded 14d2f7177). | AE (0.7) | Non-urgent enhancement; opportunistic. |
| `ADHC_GLDINC` | 6-script SHADOW_SET cutovers (B_01/A_03/B_02/B_03/A_01/A_02 -> INCREMENTAL_CAPABLE) -- THE compute capture (the project's economic point; not abandoned, re-homed). The BINDING daily-parity watch (>=5 clean nights, `daily_watch_until` 2026-07-05) RIDES this tail -- NOT dropped at close. | AE (0.6) exec + Andrew per-script nod | Per-script: parity-gate met + Andrew nod -> flip INCREMENTAL_CAPABLE + SHADOW_SET removal. Tail done when all 6 cut over. |
| `ADHC_GLDINC` | SS4c periodic-oracle re-validation APPLY (TIER-1 canary Lambda + 4 egress alarms + weekly-diff) -- build RAVC2-accepted, CloudOps gate-1 closed, DS gold-lib review CLEAN. The standing verifier binding every phase cutover. | AE (0.6) | CVO re-cert + synthetic test -> `safe-apply`. |

---

## Pending Auto-Close Triggers (deferred projects)

| Project | Status | Auto-close gate |
|---|---|---|
| `YANG_SITTW` | active (delivered, riding PROD promote) | The 3 FE legs (DEV a447712b / 27299745 / 700ec9b4) land in PROD via the next normal portal promote. Data fix already LIVE in PROD. Andrew-1950Z RIDE-NORMAL; no dedicated DT push. |
| `NFRA_GRAPHS` | active | `comp-manifest-check` ramps advisory->blocking (AC1 manifest full-population close-gate) AND the D8 critical-surface 3-condition advisory->blocking flip lands. D7/D8 shipped; manifest seeded+populating. |
| `ADVI_PRTORG` | active | AC1/AC4 smoke PASS (COT JWT + platinum via AE_PartnerETL chain) AND AC7 `ownership_map.json` published to `platinum/cottonwood/`. Phase 3 + portal promote already LIVE (v2.1.119/120). |
| `TRSB_LEDGER` | active | TO-12 portal role-aware Execution-tab gating verified at `:5175` (CTO folds this one-action close into his Andrew report). Phases 0-2 dispatched. |

A future /drive (or the owning exec) checks the gate and, when met, executes the 2-step atomic close (JSON status->complete + REGISTRY Active->Completed).
