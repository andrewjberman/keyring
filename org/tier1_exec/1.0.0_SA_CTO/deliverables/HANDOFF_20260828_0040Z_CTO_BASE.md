# HANDOFF -- 1.0.0_SA_CTO base seat, laptop fabric, 2026-08-28 ~00:40Z

Paste this as the launch message for the reinstantiated `1.0.0_SA_CTO`.

---

1.0.0_SA_CTO. FIRST: run /watcher to self-heal inbox-watcher + broker registration. THEN the
org/XXX.md startup protocol. Zero crons at launch EXCEPT the one carrier clause names below.

WHO YOU ARE / WHAT STANDS: base CTO, laptop fabric, mid-D2. The parallel ~X fabric (CTO~X, COO~X,
CVO~X, CRO~X) runs D11 on this device -- do not write to or ack them; separate workstream.

READ FIRST (in this order, all at HEAD):
1. org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-28/session_close_1830-0035Z_D2_CAMPAIGN_TO_DATE1_REFIRE.md
   -- the predecessor's close; Current State is the handoff surface.
2. org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-28/self_drive_D2-D3_tick7.md -- the loop's last tick.
3. org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D2-D3/VERDICTS.jsonl -- 9 rows; row 9 is the live GO.
4. docs/briefs/d2-critical-path-sequencing-20260827.md -- the D2 critical path (P0-P6).
5. org/ref/DRIVE_PAIR_PROTOCOL.md -- how the loop pairs with COO's /drive.

RE-ARM THE LOOP FROM THE CARRIER, NOT FROM MEMORY: org/XXX.md, the 1.0.0_SA_CTO row, carries
"/self-drive D2 & D3 ARMED ... cadence 30m :07/:37, paired_with: /drive D2 & D3 @ 2.0.0_SA_COO
(+15m, :22/:52)". Re-arm `/self-drive D2 & D3` on that clause (s.0.4/0.5 of the skill: the carrier
gates tick 1; it is already committed @310a20e38c, so tick 1 may run). Scratchpad tick state was
{tick 7, last_log_tick 7}; continue at tick 8. The log cadence is DELTA-DRIVEN (quiet ticks write
nothing; 6-tick floor). The RESERVED classifier is ADJUDICABLE-by-default with citation-on-card;
CVO validates reservations each tick.

THE ONE THING IN FLIGHT: the ADVI_49F 533-date TWR backfill campaign. Both start faces are COMPLETE
(P14-STAMP @f3a51ab26e, c00-SIGNING @8e72ca42b6). Date 1 (2024-07-08) was REFUSED at 00:12Z
(AccessDenied) because the vehicle targeted the BD auto-login box; ruled WRONG HOST (77108), no IAM
change anywhere, re-pointed to the gold runner i-01003b035d2988dfb @c143be5f10 and RE-FIRED
00:33:45Z by 0.7.0_AE_CloudOps~L. Expect ~L's date-1 outcome + V14-4c(e) judgment in the inbox. If
it PASSED: the campaign is running (~17h, 12:45Z blackout); your job is the loop + rulings as they
arise; nothing to dispatch. If it REFUSED AGAIN: that is a NEW finding -- rule from the record
(cite file:line @ HEAD), never from the previous ruling. StartedByDispatcher stays OMITTED on
campaign sends; the driver's halt is conditional on having started the host (the runner is SHARED).

STANDING RULINGS YOU INHERIT (do not re-litigate): keeper-#10 FC-only scope (TR unrecoverable
n=49, banked); P14-STAMP option (i); c02 m-token option (a); MDPF B1 REPOINT / B2 exception; the
line-ending deploy rail APPROVED as a rail (owner 0.8.0_AE_CloudComp, POST-campaign cut, spec
@f90fbeb648, three live specimens left in place as its positive controls); write_bytes never
write_text on anything that deploys.

ANDREW'S STANDING WORDS THIS SESSION: "use comp-find, not grep"; "all recs approved" (the five
/open-calls recs, @3389cc668a); drive pair on one target; no committed log every tick; the
RESERVED-leak restructure; sprint items always build -> ship -> fix -> verify -> scope; team
activity as an area chart from 00:00 ET with hourly ticks; residuals are named, never parked on a
row (he caught 242 "Agent Infrastructure" commits that were 129 unattributed).

WHAT IS ANDREW'S ALONE (do not gate, do not ask twice): the arm-(a) serve read after the
post-campaign P1.5 re-grade; the $51.8M insurance-attribution question to Mike (brief
@45c46236fc, on today's sprint as BLOCKED).

POST-CAMPAIGN QUEUE (COO's obligations carrier D2_CUT_TIME_OBLIGATIONS_20260827.md): rail cut to
0.8.0; base 0.7.0 re-seat carrying X-ii-a + freshguard close + July-23 re-emit decision; V14-2
re-exercise on the runner; D10 sitting after D2 close; D5 hold until serve clears. D3 folds in at
P1-green + serve-gate-clear (EXACT-JOIN spec already delivered @1914fa3fd6).

LOW-PRIORITY OWN-LANE ITEM: the eight remaining directive charters from fresh PRD reads in a quiet
window, then a ratification ask.

MECHANICS THAT BIT TONIGHT: commit via safe-commit -F with a Write-tool msgfile (never shell-built);
never grep a commit's output to decide if it committed -- ask git log; a shared working tree is not
atomic (an unstaged row of yours can ride a peer's commit -- it did, row 9 @415e07a64a); a merge
window from 0.0.0_AB_MSTR means HOLD safe-commits until the CLOSE frame.

THE PAIR REINSTANTIATES TOGETHER: 2.0.0_SA_COO also closed at ~00:4xZ (77147) and its successor
re-arms the paired /drive D2 & D3 half on the same XXX.md carrier at the next :22/:52. Ledger row 9
is consumed EXECUTED (re-point @c143be5f10, date 1 re-fired). V14-2 is SEQUENCED by COO: re-exercise
on the runner after date 1's oracle read and before V14-4c(e) is treated as final -- a campaign-start
judged before that re-run is PROVISIONAL and the 533 do not start on a provisional (e). In the gap
before COO's first tick, the CTO seat is the live reader of ~L's date-1 report.

UPDATE 00:4xZ (before the reboot stand-down, Andrew's word via 1.0.0_SA_CTO~X 77168): DATE 1 IS
ARTIFACT-COMPLETE on the correct host (~L 77153, 00:36:23Z, rc=0, wall 120.7s): 4 of 4 manifests
carry the basis + the -1 sentinel; flow boundary holds on an instrument independent of the driver's
oracle; the conditional halt left the already-running shared runner alone. V14-2 re-exercise was
RUNNING on the runner at stand-down; V14-4c(e) NOT judged; the 533 NOT started. nna schema 1.1 on
date 1 is EXPECTED (each writer has its own ladder; closed 77159). Open non-blocking question to
DS~U: why dim_account's manifest shows no schema field (a00 pins MANIFEST_SCHEMA_VERSION separately).
Successor's first act: read ~L's V14-2 result + (e) judgment from the inbox; the loop ticks from 9.
Tick 8 log @6062b28375. This device REBOOTS after this stand-down; local tails ride the first
post-reboot integration window.

UPDATE 00:52Z: **CAMPAIGN STARTED** (~L 77170, @3fa0cc63c7). V14-4c(e) judged AFFIRMATIVE and FINAL
after V14-2 was restored on the runner (subject control; 2 sends with StartedByDispatcher OMITTED;
host 'running' across 3 ec2 reads; conditional-halt arm REFUSED to stop the shared box). 532 of 533
remaining, mean wall 115.8s (~17.1h). EXPECTED SHAPE: the driver is strictly sequential and PAUSES
ITSELF at the pre-fire blackout ahead of the 12:45Z nightly (~371 dates in), then needs
RE-INVOCATION by ~L and will not resume until the nightly's own artifact is read -- a pause at
~12:2xZ is the design, not a stall. Reporting per 100 dates or session boundary; a HARD-STOP row
stops the pass for operator judgment. Only the structurally-impossible arm gates (code-rule reaching
the admission vocabulary); everything else records. After the campaign: P1.5 re-grade (rate split
FC/TR) -> Andrew's arm-(a) serve read; the base 0.7.0 re-seat window carries the post-campaign cuts.

MOBILE RENDER (Andrew-direct ~00:5xZ + ~01:0xZ): every /daily-sprint render now produces BOTH
daily_reports/out/Desktop_DAILY_REPORT_<date>.html and Mobile_DAILY_REPORT_<date>.html from one
JSON and one shared grammar (templates/_shared_viz.js); the FIRST word of the filename names the
variant (Teams truncates). Renderer default --variant both.

Push state at handoff: HEAD LOCAL, origin/CLOUD @3fbb493cda (ls-remote 00:35Z); integrator-only.
