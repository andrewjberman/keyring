# /self-drive dell1 box open calls -- tick 11 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~05:58Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. **state: ARMED**

## Measured

- **Box list:** rows=71, **open=1** (f376, an approval row with changes requested, waiting on the asker's new head).
- **Inbox:** 0 unread. msgs 5428, 5431, 5434, 5436 and 5438 were acted on and acked.

## Acts and rulings since tick 10

| item | ruling / act | record |
|---|---|---|
| AI-fill hold pair (`2.0.0_SA_COO~R2` msg 5428) | **CTO half SIGNED.** One env var on `opal-amgt-scoped-api`. Applied 05:10Z, and this seat read the live config: the variable is set, CodeSha256 is equal, memory is 1769 and timeout is 29 | `AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND105_AIFILL_HOLD_CTO_HALF.md` @8bb0402723 |
| Call 263d (MDPF_SECCLASS e97 condition 4, CROSS-BOX) | **Escalated** as XA-20261014T054803Z-7d27. The laptop CTO RULED (a): the condition is re-read as "unchanged inputs produce 0 rewritten keys", proven by a QA re-run of C_06 with the served bytes hashed before and after. **CLOSED** with `--xadj`, and relayed to `~M1` | `org/critical_paths/cross_adjudication/20261014T0552Z_XA-20261014T054803Z-7d27.md` |
| Approval f376 (`~R1` bm-1, Opal-internal) | **Changes requested:** the new grid-dash words claim "the research team's sheet" on non-team rows, which is false there. The fix is to use those words on team rows only and add a harness arm. Approved on the new head | msg to `~R1` 05:56Z |
| bm-2 (a mixed-currency forward P/E) | **The withhold branch is accepted** | same msg |

## Completion test

Box scope: **NOT DONE.** The loop runs until Andrew's stand-down.

## ACTS ONLY ANDREW CAN DO (cited)

- **Sign-in at the dell1 console after the NFRA_CTLPLN restarts**, ~14:45Z and ~15:15Z today (10:45 and 11:15 ET): his login.
- **One session from his own work Claude through the gateway** (NFRA_OPLGTW FWD-21): his identity and login.
- **The MDPF_SECCLASS client-facing BD Mix push:** a client-facing PROD page (CLAUDE.md push law).

## Compiler Tools

`open-calls.py list/close`, `xadj.py open/show`, `.tools/aws lambda get-function-configuration`, `safe-commit.sh`.

-- 1.0.0_SA_CTO~DELL1
