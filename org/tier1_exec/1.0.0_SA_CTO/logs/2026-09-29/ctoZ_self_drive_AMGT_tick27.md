# /self-drive AMGT_CORPUS AMGT_RESAPP AMGT_HARVST DSGN_AMGTV1 -- ticks 26-27 -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_220xZ_SELF_DRIVE_AMGT_AND_DSGN_AMGTV1.md` @`a0186c364b`.
**Ticks covered:** 26 (10:17Z), 27 (10:44Z), plus the acts between. Previous committed log: tick25 @`2f1c39c4e4`. **state: ARMED**

## Calls ruled by the driver
| call | ruling | where |
|---|---|---|
| HARVST r15 (CVO decision): the `Z-W41-S2` double count | one text span, one count (longest non-overlapping alias); round 16 = 1 cell under a pair | analysis @`ce26d1244b` |
| CORPUS r11 (CVO decision): `Z-W1-S14`, method-version pinning tests | a cut that bumps `METHOD_VERSION` grants its pinning tests in the same order (standing for this project) | analysis @`4dead72211` |
| CORPUS r11: TSM's Base EPS dip | served as written; the pack is the research team's | analysis @`4dead72211` |

## Mail read (READ-acked)
26562 (CVO~Z HARVST r15 slug), 26564 (CVO~Z CORPUS r11 slug), 26565 (COO~H r16 issued; premise correction: the one-count fix moves 8
rows tier C -> D on 6 securities, acknowledged, and the pair names them), 26566 (COO~X r12 half owed).

## Acts
- HARVST r15 analysis @`ce26d1244b`. COO~H issued r16 @`b8c8214ce5`.
- CORPUS r12 re-address CTO half SIGNED + r11 analysis @`4dead72211` (live before-state: `research_dossier` 0, `research-dossier`
  846/95). COO~X opened the ledger @`e7228d6ff1`.
- Observed: vv-4 ROLLED BACK @`1c410c5936` (NEVER-2 entry closed 10 of 10), TO withdrawn @`4311cdd49e`; CVO~Z self-corrected
  (`Z-S299`, @`a910bf58a5`); DSGN r3 issued @`d1c583a705`; RESAPP r47 drain-end packet @`c02010a3b0`, slug pending.

## Completion test
NOT DONE -- 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Acts only Andrew can do (cited)
1. R20 acknowledgment for `amgt/harvest/gold/research-dossier/` [CLAUDE.md Rule 30] -- this now only shortens the wait, because CORPUS
   r12's R19 move re-lands vv-4 without it.
2. Read the Seeking Alpha subscription state (HTTP 402, `AMGT_HARVST-Z-W37-S4`) [entitlement].
3. Lift *"lets hold on pushes and merges for now"* for the portal DEV push of `92a2576254` [hold set by name].
4. Remove the merged worker worktrees [CLAUDE.md Agent Autonomy: recursive deletion].

## Compiler Tools
`check_inbox`, `ack_messages`; a boto3 paginated count of both dossier prefixes; `git diff HEAD...ce3192a363`; a read of `gold.py`
`address_of` / `table_prefix`.
