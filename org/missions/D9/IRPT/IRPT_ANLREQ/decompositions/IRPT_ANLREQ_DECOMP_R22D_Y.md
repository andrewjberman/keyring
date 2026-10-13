# IRPT_ANLREQ -- decomposition, round 22 PROXY PLACEHOLDER, workstream YR round 22 (issuer 2.0.0_SA_COO~Y2)

**Input:** the `AR-y-248` portal candidate (`wk-IRPT_ANLREQ-81-portal` @1742505086) puts the whole 163-character proxy hint into the proxy input's placeholder; the input is `w-28`, so a person sees a clipped fragment (worker row `IRPT_ANLREQ-D2-W81-S3`, confirmed by this seat reading the diff). The hint line and the input's title already carry the full words.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-252` | the proxy input's placeholder is the short constant `PROXY_PLACEHOLDER = 'Type a ticker'`; one test; a portal candidate branch on top of the AR-y-248 candidate | a portal candidate branch (`src/` only) | LOCAL |

## Edges and chains

- None. M = 1 chain. The two portal candidates (`AR-y-248`, `AR-y-252`) go to the CTO's review lane together as one stack.

fanout: 1 of 1 chains, cap 8, reason: one portal line, one test.
