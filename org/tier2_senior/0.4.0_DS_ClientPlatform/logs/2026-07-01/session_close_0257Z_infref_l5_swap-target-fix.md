# 0.4.0_DS_ClientPlatform~A — Session-Close (INFREF L5 swap-target fix, pre-reboot)

**archetype:** DIAGNOSE (secondary: IMPLEMENT, COORDINATE)
**window:** 2026-07-01 ~0215Z → ~0257Z (since last log 639fc3b46 / session_close_0210Z)
**serial:** 0.4.0_DS_ClientPlatform~A | **branch:** CLOUD | **project:** ADVI_INFREF (LEG-5 cutover)
**why this log:** Andrew rebooting the machine (device slow). 0.6.1 already offline. Written for ZERO
prior context — the L5 chain is PAUSED until agents respawn post-reboot.

---

## Window summary

Resumed fresh-context, ground-truthed the riding rebuild (independently confirmed on-track, not
trusting self-report), pre-analyzed the L5 served-extra gate, and — during 0.6.1's pre-swap
never-widen confirms — **caught a swap-target defect that would have broken the irreversible cutover**,
which ALSO existed as a latent bug in my own post-swap harness. Fixed + unit-verified both. The rebuild
compute is still riding; the swap has NOT fired.

## THE HEADLINE (read this first)

**The L5 served swap target is `platinum/` (FULL layer), NOT `platinum/firm/`.**
Correct command 0.6.1 has locked:
`aws s3 cp --recursive s3://opal-data-inf/platinum/_rebuild/20260630T234458Z/ s3://opal-data-inf/platinum/`

- Grounding: compute scripts read `OUTPUT_PREFIX` as the platinum-LAYER root and append the subdir
  themselves (`INF_09:76/258` `f'{OUTPUT_PREFIX}firm/...'`; `INF_D_02:2043` `advisors/{k}/book.json`;
  `INF_D_09:70` `clients/{hh}/accounts/...`). So STEP3 stages `platinum/_rebuild/{ts}/{firm,advisors,clients}/...`
  (subdir NESTED). Proof by symmetry: normal run (default `platinum/`) writes `platinum/firm/dashboard.json`
  = current served.
- 0.6.1's initial plan (`-> platinum/firm/`) would have DOUBLE-NESTED (`platinum/firm/firm/…`) + STRANDED
  advisors/clients. Caught pre-fire; 0.6.1 independently source-grounded + locked target=`platinum/`.
- `gold/_rebuild/{ts}/` = intermediate-provenance, NOT swapped (portal serves only `platinum/` per
  `advisor-intelligence.ts:438`).
- `cp` (not `sync --delete`) → additive, deletes nothing → served-extra survives (matches the whitelist).

## Files Modified — see commit messages (3 commits)

- `d8b55a395` — **L5 served-extra pre-adjudication brief** `docs/briefs/advi-infref-l5-served-extra-preanalysis-20260701.md`.
- `c28755ccf` — **THE harness fix** `data/inf/scripts/verify/validate_post_swap.py`: check-1 now maps staged
  `{ts}/{rel} -> platinum/{rel}` (SWAP_ROOT), FULL-layer (6407-key) ETag+size parity (cp preserves ETag ≤5GB
  == byte-identity) + SHA256 byte-compare on firm top-level views; check-5 compares served firm views vs the
  staged FIRM-top set. Eliminates the double-nest false-RED. Unit-verified live+synthetic; anchors 2/3/4 GREEN.
- `faac533ab` — brief updated with the corrected swap-target section.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which | route "portal consumers of activity_scan/cash_drag" → comp-platinum reverse | PASS (routed) |
| comp-platinum reverse | consumer check on bare vs _{window} keys | PARTIAL — null (dynamic-key fetch); comp-grep decisive |
| comp-grep | portal fetch pattern (advisor-intelligence.ts) + OUTPUT_PREFIX consumers in gold scripts | PASS — the decisive grounding for both served-extra + swap-target |

**Worked:** comp-grep's systems-context surfaced the OUTPUT_PREFIX consumers (the swap-target catch).
**Gap:** comp-platinum reverse can't resolve dynamic period-suffixed keys — expected, not a defect.
**Rail:** several `aws s3 ls`/`head-object` rail-checked (staging/sentinel existence, full-layer key-count
sizing, snapshot content — no comp-tool models an in-flight rebuild keyspace or ad-hoc backup prefix).

## MCP traffic (significant only)

- CTO: RAVC ACK/close — disposition-(a) doc-reconcile (ffef4eeec confirmed my HEAD, in sync).
- 0.6.1: full RAVC loop on the swap-target — their 2 never-widen confirms → my grounded correction
  (target=platinum/) → they source-grounded + locked → I shipped the fixed harness c28755ccf → they
  acked HOLD. **0.6.1 HOLD conditions before firing: (1) fixed harness commit [MET, c28755ccf] +
  (2) CVO L3-GREEN [pending].**
- CVO (async, not yet spawned): 2 front-load msgs — served-extra whitelist + the cosign-material harness update.

## Blockers

NONE (blocker-class). The L5 chain is PAUSED on the machine reboot (Andrew-direct) + the rebuild's
remaining compute. Not a stall.

---

## CURRENT STATE (zero-prior-context handoff)

**ADVI_INFREF LEG-5 = the cutover of the rebuilt inf substrate to served. Gate chain:
`_REBUILD_STAGED` → CVO L3 (pre-swap value-parity) → 0.6.1 L5 atomic swap (target `platinum/`) →
my `validate_post_swap.py` + CVO L5 cosign → cutover.**

**Rebuild — was RIDING at session end (verify freshness post-reboot):**
- SSM `29629fb9-98f1-410e-984a-7c13ad2f6d0f` on `i-0ed5afded2ebd4ed4`, running `/tmp/inf_rebuild_step23.sh`
  (from `s3://opal-data-inf/code/rebuild/inf_rebuild_step23.sh`). Status InProgress, ETA ~03:20Z. Post-reader-fix
  v3 (my L164 fix is in it; the 2 prior Failed runs are pre-fix).
- STEP2 silver-backfill (positions_mv+assets_v2 parallel, then txn+perf sequential) → STEP3 `orion-gold-dispatch.sh
  --stage compute` with `OUTPUT_PREFIX=platinum/_rebuild/20260630T234458Z/`, `GOLD_ARTIFACTS_PREFIX=gold/_rebuild/{ts}/`.
- Sentinel on completion: `s3://opal-data-inf/_rebuild_status/20260630T234458Z/_REBUILD_STAGED.json` (bucket-root
  `_rebuild_status/`, NOT under `platinum/_rebuild/`). At session end: staging + sentinel BOTH still empty.
- Rollback snapshot verified real: `s3://opal-data-inf/_pre_rebuild_backup/20260630T234458Z/` (6061 obj, 5.74GB).

**My harness — GATE-READY (`data/inf/scripts/verify/validate_post_swap.py`, HEAD c28755ccf):**
- Auto-discovers staged `platinum/_rebuild/{ts}/` (fixed TS 20260630T234458Z; `platinum/_rebuild/` empty →
  unambiguous). Runs POST-swap.
- 5 checks: 1 STRUCTURAL (full-layer ETag+size parity 6407 keys + SHA256 firm top-level) · 2 AUA==$202,125,678.08 ·
  3 as-of==2026-06-30 · 4 cross-consist · 5 served-extra.
- **L5 run command:** `python3 data/inf/scripts/verify/validate_post_swap.py --allow-extra-views "activity_scan.json,cash_drag.json"`
- Served-extra whitelist = `{activity_scan.json, cash_drag.json}` — DEPRECATED bare legacy (portal reads only
  `_{window}` variants; `advisor-intelligence.ts:1428/1445` + FE sentinel `InflectionInsightsPanel.tsx:157`).
- Anchors verified GREEN vs LIVE served this session (spread $0.0000).

**Reference:** `docs/briefs/advi-infref-l5-served-extra-preanalysis-20260701.md` (served-extra + swap-target,
full grounding). PRD/path canon: `docs/architecture/ADVI_INFREF_PRD.md` + `ADVI_INFREF_PATHMAP.md`.

---

## NEXT STEPS (post-reboot)

1. **[0.4.0_DS_ClientPlatform~A — fresh me]** On resume: `/watcher`, then re-ground the rebuild —
   check SSM `29629fb9` status + whether `_rebuild_status/20260630T234458Z/_REBUILD_STAGED.json` exists.
   - If NOT staged: rebuild still riding (or the reboot killed the box — the SSM runs on the EC2, NOT this
     laptop, so a laptop reboot does NOT stop it; confirm InProgress). Re-arm the sentinel-watch, standby.
   - If STAGED: stand ready for CVO L3 → on 0.6.1's swap (target `platinum/`), RUN the harness with the
     whitelist above → GREEN → CVO L5 cosign → cutover.
2. **[0.6.1_AE_PartnerETL]** (offline — respawn needed) owns the rebuild SSM → stage → L5 swap (target
   `platinum/`, locked). HOLD until CVO L3-GREEN. Fixed harness (cond 1) already MET.
3. **[3.0.0_SA_CVO]** (not spawned — MSTR respawn at `_REBUILD_STAGED`) owns L3 value-parity + L5 cosign.
   2 front-load msgs waiting in its inbox (served-extra whitelist + swap-target/harness update).
4. **Post-cutover (banked, unchanged):** household repoint (spec'd) → perf-incremental watermark (FINALE)
   → P3 decommission (checklist ready) → deploy-hygiene sweep (retire silver/api_dims/performance/ orphan,
   fix convert_* stale docstrings, ProcessPool GIL-fix variant).

**NOTE:** the laptop reboot does NOT touch the rebuild (SSM runs on `i-0ed5afded2ebd4ed4`). The only thing
lost is this session's sentinel-watch + agent registrations — re-arm on resume.
