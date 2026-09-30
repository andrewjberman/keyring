# /self-drive AMGT_CORPUS AMGT_RESAPP AMGT_HARVST DSGN_AMGTV1 -- tick 28 -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_220xZ_SELF_DRIVE_AMGT_AND_DSGN_AMGTV1.md` @`a0186c364b`.
**Ticks covered:** 28 (11:17Z), plus the acts since tick27 @`51e6ac498a`. **state: ARMED**

## Calls ruled by the driver
| call | ruling | where |
|---|---|---|
| RESAPP r47 (CVO decision): FWD-30's harness has two writers | one writer per artifact: `exportCompare.harness.cjs` = DSGN_AMGTV1 (its r3 cell 3 closes `Z-S297`); `render_pack.py` = AMGT_RESAPP | analysis @`657b9283a2` |
| DSGN tick-19 pitch (COO~D 26575): `/closer`? | NO -- full limbs; hop 3 is owned by AMGT_RESAPP r48 cell 2, so no seam is unowned | msg to COO~D 11:08Z |

## Mail read (READ-acked)
26571 (CVO~Z RESAPP r47 slug), 26574 (COO~D 5174 walk), 26575 (COO~D closer pitch), 26577 (COO~H e-2 half owed).

## Acts
- RESAPP r47 analysis @`657b9283a2`; round 48 = 3 cells (the vv-4 re-land on `research_dossier` after CORPUS r12, the served company name,
  the export's wording from one source).
- 5174 walk build merged portal `a93071b8` -> `80a0df1f` (tsc 0, HTTP 200) for DSGN r3's close walk.
- HARVST r16 e-2 CTO half SIGNED @`73fce69599` (own rebuild: 14 rows over 6 securities, 8 C -> D, events 8/8; span_attribution 212, DRIFT 0).
- Observed: DSGN r3 drained 5/5 (@`4e8d423c8b`); HARVST e-1 drained @`5f25e64267`; CORPUS r12 act running (ledger @`e7228d6ff1`).

## Completion test
NOT DONE -- 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Acts only Andrew can do (cited)
1. R20 acknowledgment for `amgt/harvest/gold/research-dossier/` [CLAUDE.md Rule 30] (it only shortens the wait for CORPUS r12).
2. Read the Seeking Alpha subscription state (HTTP 402, `AMGT_HARVST-Z-W37-S4`) [entitlement].
3. Lift *"lets hold on pushes and merges for now"* for the portal DEV push of `92a2576254` [hold set by name].
4. Remove the merged worker worktrees [CLAUDE.md Agent Autonomy: recursive deletion].

## Compiler Tools
`check_inbox`, `ack_messages`; `d2_check.py` and `e2_tier.py` (in-memory rebuilds); `span_attribution.py`; `tsc -b` plus an HTTP read of 5174.
