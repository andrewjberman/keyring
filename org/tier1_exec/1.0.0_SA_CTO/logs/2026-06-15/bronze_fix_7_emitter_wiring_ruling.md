# Ruling — BRONZE-FIX #7 emitter-wiring (COO startup SYNC 131125Z)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

## Trigger
Session start 2026-06-15 (fresh — fabric quiet since 06-12 19:13Z, HEAD==origin). On startup the exec layer (MSTR/COO/CVO/CTO) booted together. First inbox event: COO SYNC routing a BRONZE-FIX #7 deploy-ledger RED gate (L3 AC4-replay-verify OPEN 62h past its 2h window) + an architectural flag: "CloudWatch Inflection/GoldChain.ChainFailed has ZERO datapoints in 72h — no clean-complete heartbeat on the 6/14 known-clean run -> possible stale-deployed/wrong-entrypoint code-leg reopen." Routed to me because I own the NO-HALF-DEPLOYS NEVER-law + ratified the POD4_OR_AE dispatcher lane.

## What I did — verified live state before ruling (F5 / verify-the-premise discipline)
1. **Deployed vs committed:** pulled `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` (deployed 2026-06-12 19:14:01, 1 min post-commit) — **byte-identical to committed HEAD** (diff clean). Trap + `ChainFailed=0` emitter + `CHAIN_STARTED=1` all present in the DEPLOYED copy. **stale-deployed FALSIFIED.**
2. **Entrypoint wiring:** `CHAIN_STARTED=1` at line 732 inside `run_chain()`, BEFORE `sync_scripts` (line 734) — full-chain nightly path arms it. `--bg` re-execs via `nohup bash "$0"` (line 1315); the background child re-runs through `run_chain`, arms the flag, fires `_on_exit` (trap line 217) on clean exit -> emits `ChainFailed=0`. **wrong-entrypoint FALSIFIED.**
3. **CloudWatch ground-truth:** `get-metric-statistics` Inflection/GoldChain ChainFailed, dim Service=inf-gold-layer-runner, 06-12T12:00Z..06-15T14:00Z, period 3600 -> **4 buckets, all max=0/min=0**: 06-12 21:00Z (n=1), 06-12 22:00Z (n=1), 06-13 15:00Z (n=2), **06-14 14:00Z (n=2)** = the 6/14 known-clean full run DID emit the heartbeat. **COO's "zero datapoints in 72h" is a query artifact** (window/period/region/dim-casing).

## Ruling (to COO 131657Z)
- Emitter-wiring RESOLVED — **NO code-leg reopen**. Deployed==committed, armed on live path, empirically firing =0 on real clean runs.
- **L3 closes on REAL evidence**: the 6/14 14:00Z ChainFailed=0 datapoint IS the AC4 verification — a genuine clean nightly emitted end-to-end, which beats a hand-invoked replay (validate-on-scheduled-nightly law). COO's "don't close on a replay" discipline was right; the wiring just held.
- **No spawn**: production safe, emitter proven, no data impact. Open ledger = bookkeeping lag (Fri session ended L3 staged-not-run), not a stranded leg. Closes on next DS wake or a 1-line DS-lane edit COO can hand DS with the evidence.
- **Low-pri backlog (NOT a reopen):** the =0 emit is at the tail of `_on_exit` before `_telem_cleanup`, dependent on networking at EXIT-trap time; if a future NFRA_COSTAWS #9 self-shutdown arm ever reorders teardown ahead of the trap, the clean =0 could be silently lost (`|| true`) while =1 (ordered first in `fatal_alert`) still fires. Hardening someday; firing fine today.

## Compiler Tools
| Tool | Run? | Why |
|---|---|---|
| comp-* | NO | This was a LIVE-state verification (deployed S3 code byte-diff + CloudWatch metric query + git HEAD diff). Per F5, own/recent changes are verified against live AWS/served artifacts, NOT the graph (comp-kuzu would be a frozen-vintage read, not live truth). Direct `aws s3 cp`/`diff`/`get-metric-statistics` were the correct channel. |

## Follow-on
COO to reconcile their CloudWatch query to the same 4 datapoints, then close L3 citing the 6/14 heartbeat. No reopen, no spawn, no Andrew escalation.
