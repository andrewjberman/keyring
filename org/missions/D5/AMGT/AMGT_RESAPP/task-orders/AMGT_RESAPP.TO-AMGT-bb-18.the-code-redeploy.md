# AMGT_RESAPP task order -- `AMGT-bb-18` -- THE ROUND-78 CODE REDEPLOY CARRYING THE ADAPTER'S SIX HOOKUPS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bb-18</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm, monitor or cadence; one redeploy by hand. The daily snapshot schedule is unchanged.
comp-iam: RUN by the issuer at the cut -- denominator: 14 build cells whose modules the artifact may carry (bb-1..bb-4, bb-7..bb-11, bb-13, bb-16, bb-17, bb-21, bb-22); they add no read path the function role lacks at the cut; a cell that needs a grant names it in the pair, and the plan STOPs on any IAM resource the pair does not list.
comp-iam coverage: BLIND to an IAM change outside the plan.
comp-adversary: RUN by the issuer at the cut -- deployed MkM9Kf37 (LastModified 2026-10-07T04:40:17Z) reads the round-77 served shape YES; `r78_bb17.py --crit AC1 --where local` at the base reads NO (H1 to H5 fail, H6 reads 2 wrong rows of 60), so the deployed line FAILS until this act.
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-bb-18` (round 78, decomposition s.86)

Under ONE NEVER-2 entry and ONE never-widen pair:
1. **Code leg.** Build from a DETACHED worktree at EXACTLY the commit the GO names, never "at or after" it. `memory_size` stays 1769.
   - The CONTENT-DIFF the pair lists is measured at that commit against deployed `MkM9Kf37`. A file not on the list is a STOP.
   - ONE `safe-apply` on `infra/aws/terraform/harvest/`, the plan graded UNTARGETED: only the function's code (its
     artifact object and hash) may move. No route changes this round. Any other resource is a STOP, unless the pair names it.
   - The new CodeSha256 differs from `MkM9Kf37` AND equals the built artifact's. An unchanged hash is a 0-diff deploy: STOP.
   - Then run `round71/checks/leadpanel_cold_warm.py --label after` and read the cold invokes' `AMGT_PHASE` lines. Reported, not graded.
2. **After the code leg,** invoke the snapshot's scheduled event once (`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`), so
   the /freshness snapshot is written by the new code. Read the stamp.

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/`
(`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), and measure the
artifact before acting on any entry you find. `r78_deployed_cells.txt` (beside the round-78 checks) lists the round's deployed
checks; the GO states how many lines it holds.

A failing criterion is the ROLLBACK trigger: the prior artifact through the module, one code-only `safe-apply`. **Pins:** r76 c62
and c63, and r75 c59 with its 40-wide burst. A c59 that reads UNMEASURED (exit 2) is NOT a rollback trigger: report it and stop.

**Not served by this act, by ruling:** the segment table and its period labels, and the Seeking Alpha record reader. Their
modules may be in the artifact; no route reads them. If the CONTENT-DIFF shows a route reading one, STOP.

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
  <criterion id="AC1" cell_refs="AMGT-bb-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-78 deployed check passes; R78 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bb-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c62 c63; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c59 --where deployed; echo "exit=$?"</invocation><expect>R76 C62 and C63 SERVED: YES (unless the pair states a round-78 cell changes what they read, and then as the pair says) and R75 C59 SERVED: YES with one or more cold invokes inside the bar, on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bb-18"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_served_shape.py" --where deployed; echo "exit=$?"</invocation><expect>R77 SERVED SHAPE: YES on the deployed function (no regression, unless the pair names one a round-78 ruling intends); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-bb-18.the-code-redeploy.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256;
- the CONTENT-DIFF and size;
- every criterion's output lines;
- the leadpanel AFTER output and the cold `AMGT_PHASE` table;
- the snapshot stamp after the event.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.86; staged until the adapter cell (bb-17) drains and the pair is signed. At the GO the issuer fills
`round78/checks/r78_deployed_cells.txt` and states the line count. Checks dry-run at the base: bb-18 AC1 base NO CELLS LISTED exit 2
(FAIL as expected); AC2 pins as round 77's ba-20 proof read them on MkM9Kf37; AC3 base: `r77_served_shape.py --where local` reads YES
at the cut (the deployed read is the round-77 one real run, `round77/ONE_REAL_RUN_20261007.txt`). Peers V below three (bb-13) and
round 77's ba-13 ride this artifact.

<status>staged</status>
<round>78</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
