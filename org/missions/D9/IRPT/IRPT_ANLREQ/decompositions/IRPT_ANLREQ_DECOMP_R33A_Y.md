# IRPT_ANLREQ -- decomposition, round 33A: THE APPLY OF RELEASE 28, LEG L4 (the resident), workstream YX round 33 (issuer 2.0.0_SA_COO~Y2)

**Input:** the release-28 pair, signed by both halves (COO half blob `e9bb20d7fe2f6d610c88c4399e6a4387af5e7743`, CTO half @d3adae2fc8, CTO msg 7415). Window order L2, L1, L4, L3. L4 is the resident: root `0485393f3a-r28` installed over the running `0485393f3a-r19` on host `i-0167fd745ad906a66` by the Dell CloudOps lane `0.7.0_AE_CloudOps~YC2`, with the scripts of `AR-y-301` (drained @ the slot-119 drain) and the tarball, host script and package sums of `AR-y-300`. It must NOT start before leg L1 (the ticket service) has closed: the new packager sends two PACKAGE members the old server refuses 400 on every attach (pair section 6, row `W109-S2`).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-303` | the apply of L4: three keys put and read back, ledger opened, the pre-read (five stop-reads), the install and its read-backs, the IAM read of the registry grant, the ledger closed | one host, one new root, three new keys under `ec2/investor-reporting-ycharts/resident/`; the applier's output files | WORLD |

## Edges and chains

- One chain. Blocked on the message "L2 and L1 closed" from the issuer (after `TO-APPLY-R28a`, cell `AR-y-302`). It blocks `TO-APPLY-R28c` (L3, `irpt-ycharts-generate`), which also waits on the `~IB2` ledger `irpt-ycg-catalogue-ultrashort-20261013` reading CLOSED.

fanout: 1 of 1 chains, cap 8, reason: one host install in one lane under one signed pair; the order between the legs is the pair's.
