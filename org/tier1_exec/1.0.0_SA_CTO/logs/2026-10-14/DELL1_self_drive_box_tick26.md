# /self-drive dell1 box open calls -- tick 26 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~23:27Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**
Covers the window since tick 25 (@e45c08f1eb, 22:27Z). The dell1 restart stays HELD on Andrew's word.

## Measured (23:26Z)

- **Box list:** rows=85, **open=1**: `a196` (CN-p-2, client-facing, HELD for Andrew).
- **Cross-adjudications:** 19 of 19 RULED.
- **Inbox:** 0 unread. Msgs 5939 to 5961 were acked.

## Andrew-direct this window

| word | record | applied |
|---|---|---|
| "excel fix is fixed, already confirmed." | tick file | TRSB is closed on his test |
| "No I need that mdpf rerun now, i need to smoke that now" | `ANDREW_DIRECT_20261014_225xZ_MDPF_PUBLISH_TREND_TONIGHT_OVERWRITE_OK.md` @44eac4d919 | A 5174 render with real numbers (local override) was up by 22:53Z |
| "do it" (the explicit OK to overwrite tonight) + "currently we're displaying a broken graph on the trend view on PROD so better to just try and overwrite than leave this shit up" | same record | CN-p-1 deployed; one splice publish (below) |
| "i will remote in later and see how it went" | -- | CN-p-2 to PROD was asked; it waits for his yes on row a196 |

## Rulings and acts

- **CN-p-1 pair: CTO half SIGNED @d996228e93** on the COO half @54da2eb87d. I verified the revert pin's exclusion, the origin ancestry, the rollback package `ueXrxiM...` and the baseline function. C1 adds a leg-presence print at the first fire. The missing-leg-as-zero behaviour goes to enrichment (it contradicts PRD override (c)).
- **CN-p-1 deployed 22:49:55Z.** Read by me: CodeSha256 `AEUuWyiM...`, `MDPF_GOLD_COMMIT` `8e2dd0fb36`.
- **ADDENDUM 1 (the one-time splice publish): CTO half SIGNED @83ec2d7b0e, amended @da6e7b36d0.**
  - The writer is a CloudOps `put_object` of 8 builder bodies onto the as-of 2026-10-13 keys, plus one publisher run. The lambda has no overwrite switch, and a re-run would have moved the CN-h-1 counts early.
  - C2 was restated as data-hash identity: the publisher republishes all 18 pairs because its role is denied `GetObject` on `latest.json` (an enrichment).
- **SERVED 23:10-23:11Z.** Read by me:
  - the gold Global timeseries is VersionId `jIrzlWcI...`, 661224 B (= built);
  - the served-plane Global carries the 4 keys (496 dates, 9 carried).
  - ~D1's readback: 11 of 11.
  - ~D1 relaxed R6 to tolerate up to 5 restated cells and widened the mutant to 30 so it still reds. I note it here; it is not re-litigated.
  - 5174 is now plain dev:live over the served object.
- **CN-p-2 row a196** (`cand/dell1/mdpf-canon-global-trend-variant1` @9f5bbbca, cut from PROD 5d64641891): REGISTERED and HELD.
- **A mis-composed send** (wrong `from_agent`, placeholder text) was REFUSED by the identity guard. Nothing was delivered.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE 0. HELD 1 (`a196`, his).

## ACTS ONLY ANDREW CAN DO (cited)

- **Approve row `a196`** (CN-p-2, client-facing: the demo tenant opens Global; CLAUDE.md Agent Autonomy). Until it lands, PROD's Trend shows the pre-05-15 drawing defect he flagged.
- **The restart window, on his next word** (record @11a1d08ef0).
- Carried from earlier ticks: the SECCLASS BD Mix PROD push; his gateway session; the ASTN FT hold; ADVI_BILLING's answers; G4 activation.

## Compiler Tools

`open-calls.py list`; `xadj.py list`; `git merge-base --is-ancestor`; `lambda get-function-configuration`; `s3api head-object`; `s3 cp - | python`.
**Gap:** a hand-composed tool call carried another seat's serial. The identity guard caught it. The mechanism worked; the slip was mine.

-- 1.0.0_SA_CTO~DELL1
