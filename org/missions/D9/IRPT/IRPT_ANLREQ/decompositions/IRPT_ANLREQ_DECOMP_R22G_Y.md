# IRPT_ANLREQ -- decomposition, round 22 THE LIVE QA RUNNER, workstream YR round 24 (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's ruling (a') (msg 7137): the proof for the search-based swap is the QA harness passing on a fixed set written before the run (`TIMXX` plus at least 4 known funds, each suggestion schema-valid and provider-verified, 0 errors); fails or does not finish this round means fallback (b). The harness (`AR-y-250`) is tested with fakes only; the advisory (`AR-y-249`) and the wiring (`AR-y-251`) are drained. What does not exist is the runner that wires the REAL ports (the Kimi send and search over the secret named `astn/kimi/api-key`, and the provider's exact-match verify) and writes the QA record; a Dell CloudOps lane executes it under a signed pair.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-266` | `ycharts/generate/kimi_search_qa_live.py`: a `--dry-run` default that calls nothing and prints the planned calls, a guarded `--live` that wires the real ports and writes the QA record outside the repository, tested offline with spies and fakes; the Dell runbook | one new source file, one new test file | WORLD |

## Edges and chains

- None. M = 1 chain. After the drain: the CTO signs a pair for the live run (a read-only live act: a search endpoint, a chat call and a provider read per case, nothing written to AWS), the Dell lane runs it once, and its receipt decides between the capability file (the swap goes live in a signed release) and fallback (b).

fanout: 1 of 1 chains, cap 8, reason: one runner, one test file.
