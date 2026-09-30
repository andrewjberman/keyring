# 2.0.0_SA_COO~D (site Z) -- /canonical-drive DSGN_AMGTV1 -- 2026-09-30 05Z

Lease FULL throughout. Cron `17,47 * * * *` (ANDREW_DIRECT_20260929_183xZ_SELF_DRIVE_AMGT_FABRIC_OPS.md).

## Round 10 -- issued, drained

- **Issued** @35704a8693: ONE issuance over the round-9 analysis @d229d699f3. Fanout 3 of 4 chains, cap 8, 1 queued:
  - ~36 o-2, the dossier;
  - ~37 o-3, the team cases;
  - ~38 o-4, unresolved units;
  - ~39 o-1, the house date form, queued behind the other three because it writes their files.
- **Drained** (every instance VALID, my re-run of each main check matching, `tsc -b` rc=0 after each portal merge, every merge
  "dropped 0, foreign 0"):

  | order | CLOUD | portal DEV |
  |---|---|---|
  | o-4 | df292d6c3f | 7950eadd |
  | o-3 | 1034ca3252 | aada32c8 |
  | o-2 | 747bb50ab7 | 0373aa18 |
  | o-1 | a43730e29f | 5810586a |

  - o-1's base was re-dry-run on 0373aa18 before its slot was provisioned (cut rule (a)): dates 1/3 FAIL as expected, Q1 16/16.
  - After the last drain, every round-8, round-9 and round-10 check read green on the merged bytes.
- **Walk build:** CTO~Z moved 5174 to 6a9ce827, which contains 5810586a (msg 26944; re-read: `--is-ancestor` true, `/` 200).
  The signed-out control read YES at 05:56Z, and walk I (seven names) runs at 05:5xZ.

## Mail

- **CTO~Z msg 26927 (READ):** until AMGT_CORPUS round 23 lands, o-4 correctly shows about a quarter of figures raw. The walk
  expects that and does not grade it a defect.
- **COO~H msg 26928 (READ), relaying Andrew-direct ~05:40Z:** "there should be a mentions counter wherever articles are displayed
  so that its clear at quick glance".
  - The one served article list (/timeline/day) shows "named N times" on every row since round 9.
  - The feed serves 0 items on every captured overlay.
  - Andrew picks this up with this seat directly. It is logged as a round-11 input.

## Andrew, in session

- Asked how the timeline works, and how a day counts as "searched". Both were answered from the code (listing paging reach spans;
  COMPLETE needs all 5 enabled publishers).
- This seat offered to route a coverage-rule ask to AMGT_HARVST. It is held for his word.

## Held for Andrew

Worker worktrees `/c/tmp/wk-dsgn-amgtv1-{18..39}` and the scratch roots `C:/tmp/cood-r{7,8,9,10a,10b}-root`: removing them is a
recursive delete; his word (~20:2xZ) covered 9-17 only.
