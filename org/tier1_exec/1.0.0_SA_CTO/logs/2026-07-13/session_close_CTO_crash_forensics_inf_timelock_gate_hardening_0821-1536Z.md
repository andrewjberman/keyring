# 1.0.0_SA_CTO — session close: host-crash forensics -> INF time-lock ruling -> gate/fabric hardening

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE, IMPLEMENT, VALIDATE, SCRIBE
**window:** 2026-07-13T08:21Z -> 15:36Z · **28 commits** · ~40 MCP dispatches (rulings/GOs/findings)

---

## Summary

Session opened investigating a suspected host crash (Andrew-direct). Grounded it: NOT a machine
crash — WindowsTerminal.exe faulted at 08:19:20Z under a **43 GB runaway python** (commit limit
46.2 GB), taking every hosted agent tab with it. Built + armed a memory sentinel so the next
runaway names itself. That opened a cascade that consumed the session: fabric recovery, then a
multi-hour INF advisor-NNA investigation in which **six proposed mechanisms were all falsified**
and the real cause (a `build_assets_dim.py` basename collision killing `sync_scripts()` at step
zero) was found at hour eleven by the one agent who read the chain log. Ended on an Andrew-direct
sovereign ruling (NNA time-locked by account to advisor; honour the house account) now being
implemented, plus a run of self-inflicted gate/fabric-hook defects — each caught by another agent
or by a control, never by care.

---

## What happened (chronological, load-bearing only)

1. **Host "crash" grounded (NOT a reboot).** Box up since 05:05:10Z; 05:08Z pythons survived, so
   no reboot at 08:19. Event log: low-virtual-memory 08:16/08:17Z (python PID 19224 @ 39.9->43.2 GB),
   dwm.exe crash, WindowsTerminal.exe fault 08:19:20Z (module igd10umt64xe.DLL). PID 19224
   UNIDENTIFIED — inferred, non-actionable, left open.
2. **mem-sentinel** (`3edf3b029`): names any process >4 GB private / system commit >85%, with cmdline;
   never kills; self-test proven-RED first (my harness's `Start-Process` quoting killed the hog — an
   F4 null "could-not-observe vs observed-nothing" reproduced in the harness), then PASS.
3. **Fabric recovery.** Broker forged liveness for 8 dead agents (`agent-poller._pid_alive` uses
   OpenProcess w/o GetExitCodeProcess — MSTR's F-023 root cause). Cleared zombies; **found
   `deregister_agent` strips the ~lane suffix and hits the BASE serial — it deregistered ME** (F-024,
   fixed `47163c850`). Also **reaped orphan watchers with `Stop-Process` and CASCADED — silenced every
   watcher in the fabric including my own**, caught only by a spare-list assertion I ran before the kill
   (doctrine `de6f8652a`; use `.tools/kill-orphans`, never Stop-Process on MSYS bash).
4. **INF advisor-NNA (the multi-hour spine).** Phantom advisor -> $2.6M all-time credit drift ->
   a phantom $439K "deletion" -> ALL FALSIFIED. Root cause: a filename collision printing itself to
   CloudWatch. Doctrine landed as it fell (see below). The `$439K deletion` premise was struck IN PLACE.
5. **Andrew sovereign rulings (2):** (1) NNA time-locked by account to advisor; backfill first-appearing
   NAMED advisor. (2) Overruled my catch-all fork ruling — HONOUR the house account as AoR for its
   period; do not normalize. Both dispatched to DS with pre-registered invariants + the two poisoned
   snapshots (04-28 = 96% catchall, 05-08 = 0 rows) specified to RAISE not skip.
6. **Self-inflicted defects, all fixed:** orphan-hook inert on the runner (suppressed by 368 stale
   markers the bug itself wrote — F-003b `8dfece4dc`); deregister audit missing (F-004 `e5fcb9e58`,
   and I nearly shipped a silent no-op via a nonexistent WORKSPACE const); swept MSTR's live-log
   un-ignore into .gitignore (`29f35fcca`); never-rules-gate P1 — negative control RED + a hole that
   executed DS~A's commit message (`071fbda9f`).

---

## Compiler Tools

| Tool | Situation | Result | Note |
|---|---|---|---|
| raw `aws s3api list-objects-v2` (ETag) | verify gold backup by content digest | PASS | 8,805/8,805 byte-identical; presence != content |
| raw `aws lambda get-function-configuration` | confirm dispatch HOLD applied on LIVE primitive | PASS | env HOLD set, RELEASE absent, both rules DISABLED — grounded, not self-report |
| `.tools/hooks/tests/test_never_rules_gate.sh` | gate regression, 2-sided | PASS | proven-RED on old hook + green on new, every fix |
| `.tools/commit-gate.sh` | every .py edit | PASS | server.py, mem-sentinel, hook fixes |
| `.tools/owned-paths-validate.py` | new GOVERNANCE_AUDIT lane | PASS (via commit) | UNDEFINED path correctly blocked until lane declared |

**What worked:** grounding every claim on the LIVE primitive (lambda env, S3 ETag, event-rule state)
rather than a deploy log or self-report — it is the only reason two false-mechanism ratifications were
caught before they shipped. **What failed:** I authored ~11,000 words of doctrine directly into CLAUDE.md
(the hot path of every session) instead of the pointer — corrected by MSTR's Andrew-directed refactor
(15,118 -> 3,652 words, `71b37d07d`). **Gap found:** no deploy check verifies a lib IMPORTS — `comp-pipescript
deployed` answers presence+hash, never loadability (DS's rule, now a gate candidate).

---

## Files Modified

See commit messages (28 this window). Load-bearing:
- `.tools/hooks/never-rules-gate.sh` (+tests) — `0332d5d55` (override disarm), `071fbda9f` (P1: command-position anchoring + quote-as-data)
- `.tools/mem-sentinel.ps1` — `3edf3b029`
- `org/mcp/server.py` — `47163c850` (F-024), `e5fcb9e58` (F-004 audit)
- `org/mcp/hook_register_orphan_cleanup.py` — `920a7bb77`, `8dfece4dc` (marker version)
- `CLAUDE.md` — 14 doctrine commits + `71b37d07d` (refactor to /doctrine + /references)
- `.gitignore` + `.owned-paths.yaml` + `org/audit/archive/**` — `fcff61ebc` (13 audit logs, 34,180 lines, now tracked)

---

## Current State

- **INF pipeline: FROZEN, safe, nothing served.** `platinum/firm/advisor_nna_canonical.json` untouched
  since 07-10. Dispatch HOLD applied+exercised on `inf-gold-trigger` (both EventBridge rules DISABLED,
  `INF_GOLD_DISPATCH_RELEASE` absent -> fails closed). Gold backed up + ETag-verified at
  `s3://opal-data-inf/backup/gold_canonical_PRE_REDERIVE_20260713T1012Z/`.
- **Real cause of the 3-day freeze:** `build_assets_dim.py` exists in BOTH `code/gold/` and
  `code/silver/` (different content, silver copy dated 07-10 19:37Z). `sync_scripts()` dies at step
  zero. **DO NOT de-collide it, no `aws s3 rm`** — it is a third layer of defence until the time-lock
  + an IMPORTABLE coverage guard land. Freeze scoped BY FUNCTION.
- **The one real defect:** `patrick_scanlan` short $52,604.80 on the served spine since 07-09 (phantom
  `inflection_unmapped_rep`). Falls out of the time-lock; not a separate fix.
- **mem-sentinel** armed under my Monitor (this session). One per host.
- **never-rules-gate** P1-fixed: 9/9 negative controls PASS, 8/8 real hazards DENY.

## Next Steps

- **[0.4.0_DS_ClientPlatform]** implement the time-lock under HONOUR-CATCHALL: immutable `advisor_key`
  stamp (the fix; backfill is cleanup), poison-assert (RAISE), assignment-gap counter (observability).
  Deploy ATOMICALLY with libs; verify BY IMPORT from the bucket; verify on SERVED artifact. Pre-registered:
  peter +$1,287,189.93+$705,895.51 · patrick +$818,857.99+$52,604.80 · iwm +$705,895.51 · joe pre-07-08=$0 ·
  FIRM UNCHANGED $133,107,667.64. **HELD at deploy** until coverage guard is live+IMPORTABLE.
- **[3.0.0_SA_CVO]** verify the time-lock on the served artifact (not the builder); the 5 feed-absent
  UNBACKED accounts remain an open register item.
- **[0.7.0_AE_CloudOps]** dispatch HOLD stays; alarm on `INF_GOLD_DISPATCH_RELEASE` (prevent what you can,
  detect what you cannot).
- **[Andrew]** open: whether account 4273 was genuinely house-serviced (ruled house per "honour the record");
  PID 19224's identity (unknowable unless it recurs — a quiet week is UNRESOLVED, not fixed).

---

## Doctrine landed (CLAUDE.md, now split to /doctrine + /references per Andrew)

Capstones: **before you model a system, read what it is already telling you** (6 mechanisms/7 agents/11h,
zero correct); **conservation is invariant under a swap AND a both-sides deletion** (why "the total ties"
reassured us all day and was blind to both real defects); **independence of verifiers is not independence
of questions**; **prose cannot govern a cron**; **you cannot disarm by enumerating callers**; **we optimised
for the frightening number, not the wrong one**; **write the property, not the shape of the defect you just
exercised**. Recurring: nearly every defect today was caught by a control or another agent — CONTROLS OVER CARE.
