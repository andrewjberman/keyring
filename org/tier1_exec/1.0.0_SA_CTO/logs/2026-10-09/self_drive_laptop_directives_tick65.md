# /self-drive laptop directives -- tick 65 (17:58Z), covering 17:30Z-18:10Z

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`,
re-armed per the last addendum of `ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`; cadence 30m (cron a5054ca6).

## GitOps
- integrate 17:54:33Z rc=0 merged all four, held none; laptop/dell1/dell2 0 behind CLOUD; site Z box-sync paused by its manager until 18:47Z
  (keeps ~ZV's merge base stable). 24bdcd2690 and b2d3d8e749 are on CLOUD and box/dell2.

## Acts (shared tooling, owner)
- to-pipeline-gate path (b) bug (dell2 ~C2 msg 3813, MSTR 108061): marker-anchored line check @24bdcd2690 (127/127).
- dell2 ~D2 msg 3820 (MSTR 108065): backtick and in-path ids already pass at 24bdcd2690; arms @b2d3d8e749 (129/129).
- dell2 CTO msg 3850 (MSTR 108074): pure redaction RENAME of a terminal order (R100, name id -> acct#<8hex>) is not an issuance @8fff05ca26
  (132/132; scratch repo: terminal rename admitted, pending rename graded). Reply MSTR 108081.

## Never-widen
- svc-irpt reader window 5 for IRPT_ANLREQ.TO-APPLY-Y1 AMENDMENT 6: YES, same terms, R3 cottonwood-own-route, counts-only evidence
  @91d0d7982c (COO~C 108064; reply 108068).

## Cross-box
- site Z -cf36/-4d5a: site Z's CTO read -4d5a differently (MSTR 108073); NFRA_OPALAI is site Z's project, so its read governs -4d5a, with one
  condition: no Teams send from Andrew's account without his confirmation; -cf36 stands. Addendum @ca14ebabec; crossbox CALL
  XB-20261009T180350Z-0655 committed @643814be51 (line to the bus after the next laptop pass; MSTR 108079).
- New site Z rows -21c5 (open mcp.opalinvest.dev/control-plane once, name one box's projects) and -f0d2 (sign in once as Opal Bloomberg in a
  headed Edge window): both are ACTS only Andrew can do (his own look; his login), filed by site Z as forks.
- Records: dell2 jwt-private-key reads now five today (MSTR 108072); pair-rollback finding TCKT_VNEXT-D2-S20 is the pair owners'.

## Acts only Andrew can do
The 13 in the report, site Z -a519 (one Teams message to the Opal Bloomberg account), -21c5 (one look at the Control Plane page), -f0d2 (one
sign-in as Opal Bloomberg), and the client-data history purge decision.

## Process GC
- C: 20 GB free.

## Completion test
NOT DONE -- laptop directives remain live.

state: ARMED

## Compiler Tools
to-pipeline-gate --self-test, scratch-repo git mv R100 exercise, crossbox-call.py open, open-calls.py list --all --cloud.
