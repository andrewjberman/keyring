# AMGT_RESAPP task order -- `AMGT-ba-20` -- THE ROUND-77 CODE REDEPLOY CARRYING EVERY BUILD CELL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-20</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm, monitor or cadence; one redeploy by hand. The daily snapshot schedule is unchanged.
comp-iam: RUN by the issuer at the cut -- denominator: 15 build cells (ba-1..ba-3, ba-6..ba-12, ba-14..ba-18); they add no read path the function role lacks at the cut; a cell that needs a grant names it in the pair, and the plan STOPs on any IAM resource the pair does not list.
comp-iam coverage: BLIND to an IAM change outside the plan.
comp-adversary: RUN by the issuer at the cut -- deployed OVpDhfwD reads r76 c62 YES, c63 YES and r75 c59 YES with the 40-wide burst (32 cold invokes of 40, from 789 ms, every one inside the 2,000 ms bar; `round77/checks/base_r75_c59_burst40.txt`, whose cold list is cut at 400 characters). The round-77 deployed checks FAIL there until this act.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ba-20` (round 77, decomposition s.85)

Under ONE NEVER-2 entry and ONE never-widen pair:
1. **Code leg.** Build from a DETACHED worktree at EXACTLY the commit the GO names, never "at or after" it. `memory_size` stays 1769.
   - The CONTENT-DIFF the pair lists is measured at that commit against deployed `OVpDhfwD`. A file not on the list is a STOP.
   - ONE `safe-apply` on `infra/aws/terraform/harvest/`, the plan graded UNTARGETED: only the function's code (its
     artifact object and hash) and the ONE gateway route swap ba-11 wrote as text (`POST /api/scoped/amgt/refresh` removed,
     `GET /api/scoped/amgt/resolve` added) may move. Any other resource is a STOP, unless the pair names it.
   - The new CodeSha256 differs from `OVpDhfwD` AND equals the built artifact's. An unchanged hash is a 0-diff deploy: STOP.
   - Then run `round71/checks/leadpanel_cold_warm.py --label after` and read the cold invokes' `AMGT_PHASE` lines. Reported, not graded.
2. **After the code leg,** invoke the snapshot's scheduled event once (`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`), so
   the /freshness snapshot is written by the new code. Read the stamp.

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/`
(`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), and measure the
artifact before acting on any entry you find. `r77_deployed_cells.txt` (beside the round-77 checks) lists the round's deployed
checks; the GO states how many lines it holds.

A failing criterion is the ROLLBACK trigger: the prior artifact through the module, one code-only `safe-apply`. **Pins:** r76 c62
and c63, and r75 c59 with its 40-wide burst. A c59 that reads UNMEASURED (exit 2) is NOT a rollback trigger: report it and stop.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change the pair does not list, no S3 delete, no vendor or SEC call, no push
   of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-20"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-77 deployed check passes; R77 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-20"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c62 c63; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c59 --where deployed; echo "exit=$?"</invocation><expect>R76 C62 and C63 SERVED: YES (unless the pair states a round-77 cell changes what they read, and then as the pair says) and R75 C59 SERVED: YES with one or more cold invokes inside the bar, on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-20"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c57 c58 c61; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; for c in c53 c55 c56; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where deployed; echo "exit=$?"</invocation><expect>R75 C57/C58/C61, R74 C53/C55/C56 and R71 C38 SERVED: YES on the deployed function (no regression, unless the pair names one a round-77 ruling intends); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ba-20.the-code-redeploy.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256;
- the CONTENT-DIFF and size;
- every criterion's output lines;
- the leadpanel AFTER output and the cold `AMGT_PHASE` table;
- the snapshot stamp after the event.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.85; staged until every round-77 build cell drains and the pair is signed. At the GO the issuer fills
`round77/checks/r77_deployed_cells.txt` with one deployed check per drained build cell and states the line count. Checks dry-run at
the base: ba-20 AC1 base NO CELLS LISTED exit 2 (FAIL as expected); AC2 base PASS as expected (c62/c63 YES in
`round76/REAL_RUN_r76_20261006.txt`; c59 YES in `round77/checks/base_r75_c59_burst40.txt`); AC3 base PASS as expected (AE~A's az-5
proof @5e9c95ad86). Row Z-S361's repair is in `round75/checks/r75_served.py` (`--burst`, default 40; UNMEASURED exit 2).

<status>staged</status>
<round>77</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-07 ~04:0xZ):** both halves are signed: COO @b0bb011946 (`deliverables/2.0.0_SA_COO~Z/round77/NEVER_WIDEN_HALF_COO_BA20.md`) and CTO @90de9b291b (`ledger/NEVER_WIDEN_ROUND77_BA20_CTO_HALF.md`). The build is a DETACHED worktree at EXACTLY `14a36147bd`, never "at or after". The CONTENT-DIFF is CHANGED 8 + ADDED 8 as the COO half lists; any other file is a STOP. The plan may move the function's code and the ONE route swap (`POST /api/scoped/amgt/refresh` removed, `GET /api/scoped/amgt/resolve` added); any other resource is a STOP. The snapshot event is exactly `{"amgt_scheduled_action": "refresh_freshness_snapshot"}`. `r77_deployed_cells.txt` holds THREE lines, so AC1 reads `R77 DEPLOYED: YES 3 of 3`. AC2's c62 is expected YES with more items than before (69 locally); nothing in the pair changes what c62 or c63 grade. Gate limb: GATE (viii) on a modify (`<placeholders>` NONE).

<status>pending</status>
