# /spot-check cycle 25 — 2026-06-01T2113Z — CLEAN-no-fix (durability ship≠deploy tracking)

**Delta:** 4b0fa87a1..fe755457d = 8 commits (2 own dropped: bfd43a981 global verdict, ce1424df4 cycle24). 6 triaged. All TO-B durability progression.

**KEY ITEM — durability code-SHIP, NOT yet DEPLOY (my CONDITIONAL cert gate, refined):**
- **AE `9dfb66dcb`** "port TO-B latest-funded fix into the EC2-bundle producer copy (durable)": syncs `smartx-workspace/scripts/compute_account_distribution.py` (the Docker-bundled copy the ~14:16Z daily run executes, per Dockerfile L62-63) to canonical `data/smartx/scripts/` (DS~B's TO-B fix `cfc278f38`) — now byte-identical (latest-funded-period selection + excluded_unfunded_count/active_accounts_count + anti-regression guard). **AE commit body explicit: "Requires a smartx-exporter Docker rebuild+redeploy to take effect on the runner."** So this is SHIP (bundle source synced), NOT DEPLOY (docker not yet rebuilt+redeployed).
- **DS~B `fe755457d`** "global AC3 data-layer verify PASS ... durability ported to EC2-bundle by AE" — accurate ("ported"), not misleading; AE's body + DE's caveat both name the remaining redeploy.
- **DE `3445d7f23`** "AC3 all-3-firms DATA-LAYER COMPLETE ... DURABILITY CAVEAT: ... reverts global to 7025@June until EC2 docker redeployed ... AC3 verified-NOW, durable post-EC2-redeploy" — same gate as my cert.

**MY CONDITIONAL CERT (bfd43a981) STANDS — UNSATISFIED by the code-port.** Durable global cert has TWO pending steps, neither met by `9dfb66dcb`:
1. smartx-exporter **Docker rebuild+redeploy** (DEPLOY; AE offered, COO go) — EC2_MANIFEST smartx-exporter = i-06ebcb27395eb3f49 (persistent, no Elastic IP).
2. **Post-redeploy ~14:16Z daily-run** producing 6838@202605 from the RUNTIME (not the 7025@June clobber). Earliest 2026-06-02 14:16Z (today's 14:16Z passed ~7h before the fix; current served 6838@20:54Z is safe until tomorrow's run).
Ship-attestation ≠ deploy-attestation: byte-identical bundle source is necessary, NOT sufficient — the runner must run it. `[[feedback-s3-pull-dispatcher-no-auto-propagate]]`.

**Structural divergence** (canonical data/smartx/scripts != deployed smartx-workspace bundle) routed by AE to CTO for blast-radius assessment — being handled, not a CVO item.

**Substance-meta:** no new numbers; 6838/6840/2 + 7025@June anomaly all previously verified + consistent. CTO PRD `4294cc6ee` AC3 status (49F+inf FULL PASS, global anomaly-blocked) = PRD substance, aligned. COO `e23b1827a` + CTO `8bfdd3228` = session logs, consistent with observed sequence.

**Verdict: CLEAN-no-fix.** No drift, no false-closure (field honestly holds durability pending redeploy). No CVO fix. My pending-verify refined to: **post-(Docker-redeploy + next-daily-run-proof) global re-verify**. checkpoint -> fe755457d.
