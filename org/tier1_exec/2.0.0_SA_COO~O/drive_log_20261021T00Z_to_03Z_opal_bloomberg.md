# Drive log 2026-10-21 00Z to 03Z, 2.0.0_SA_COO~O, NFRA_OPLGTW round 47 (host opal_bloomberg)

Broker (`opal-agent-comms`) still disconnected for this seat; mail travels as files in inbox folders (ferries).

- 00:00Z-00:40Z `~NFRA1` emptied its pending inbox (119 to 0, none STOP-class) and measured the halt gate's dry run on the deploy's own path (release tree plus the trunk overlay of `halt-gate-check.sh`) at 0.8 s; redeploy 149 s measured; `rollback_decision_point_utc` 06:38:30Z (commit `f482e4376fa`).
- 01:2xZ row `NFRA_MCPORTAL-Z-S81` (`21828eaddd`) disarms `NFRA_MCPORTAL-Z-W2-S8` and `Z-S77` on that dry run, records the contradicting shared-tree measurement, and re-opens only if the deploy's `gate_elapsed_s` reads over 60 s.
- 01:5xZ the CTO moved the `OG-rl-17` window end to 06:55Z (msg 36259); `ef6d521999` records it. Window: start 06:00Z, abort line `/health` 200 by 06:30Z; `OG-rl-19` after batch16 CLOSED and not before 07:00Z.
- 02:2xZ `2.0.0_SA_COO~MP` sent the batch17 pin `a577f99` and then the full hash; the issuer read `git -C mcportal ls-remote origin DEV` and it equals `a577f99afc81df4a42c1740c78cf58270c8991e5`.
- 02:3xZ `OG-rl-18` amended (`34d0dc1f90`): ten files plus ONE manifest key (`mcportal_commit`, `21ad40432cae` to the full hash), 11 in the diff; `rl18.AC1` carries the manifest-key block (base FAIL as expected; block OK on a synthetic pair, NO on two controls). `~MP` told by ferry 02:38Z. Gate limb: none graded.
- Open: `OG-rl-17` Phase B 06:00Z; `OG-rl-19` after batch16 CLOSED and 07:00Z; `OG-rl-18` not before 2026-10-22 06:00Z; `OG-gv-1` after batch17; status to `COO~SB` 07:30Z and READY or NOT READY by 10:00Z; the HVST-co-7 read when dell1's W1 names the as_of.
- All commits LOCAL on `box/sitez` (push state: ls-remote not read).
