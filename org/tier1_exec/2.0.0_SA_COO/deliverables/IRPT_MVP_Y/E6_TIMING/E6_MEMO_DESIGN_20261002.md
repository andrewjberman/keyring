# E6's per-request read memo -- where it goes (design, reads only)

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~07:4xZ. **Order:** CTO rulings batch 111 (option 1: a per-request read memo; `_final`'s
re-reads never from it, tested; the same two instruments re-measure) and batch 123 item 4 (it lands after E7, before hop 11).
Measure: `E6_TIMING/OUTCOME_E6_20261002.md` (the page's status read: 193 calls for 22 distinct keys).

## Where the repeated reads are

- Every repeated read is a `get_item` on the `irpt-requests` boto3 TABLE resource, through `DynamoReportIndex.get`
  (`reports/repository.py:415`) and `DynamoRetentionIndex` (`reports/retention.py`); both are built on the one `table` port in
  `reports/composition.py:33-34`, which `reports/status_installed.compose_ports` composes once per container.
- `_final` (`ops/owned_requests.py`) re-reads the accepted record through `DynamoAcceptance` (the low-level `dynamodb` client, a
  DIFFERENT port: a memo on `table` never touches it) and then calls `retention.require_live`, which reads through `table`.

## The memo

1. `ops/read_memo.py` (this seat's lane): `ReadMemo(table)` -- a proxy with the table's `get_item`; within one scope it answers
   a repeated `(Key, ConsistentRead)` from the first answer, and every other method passes through. `scope()` clears it;
   `fresh()` is a context in which every read goes to the table and nothing is stored.
2. `reports/status_installed.py` (`2.0.0_SA_COO~P`'s lane, the ONE cross-lane file): `compose_ports` wraps `clients["table"]` in
   `ReadMemo`, and the installed handler opens a new scope per invocation -- so the memo lives for one request and one
   invocation, never across requests.
3. `ops/owned_requests.py._final`, and the same end-of-read checks in `ops/owned_status.py` / `ops/owned_report.py` (this seat's):
   their `require_live` runs inside `fresh()`, so `_final`'s re-reads never come from the memo.
4. Tests: a repeated read inside a scope is one table call; a new scope reads again; `_final` reads the table even when the key
   is held (the batch 111 condition), with a negative control that fails when `_final` is not wrapped.

Expected (E6's upper bound): the status read from 193 calls toward ~22 plus `_final`'s fresh reads; the same two instruments
(`e6_hop_timing.py`, `e6_served_timing.py`) re-measure after the apply.

## For the CTO

One exact-file grant: `infra/aws/lambda/investor-reporting/reports/status_installed.py` (two lines: the wrap and the per-invocation
scope), or `2.0.0_SA_COO~P` makes those two lines and this seat the rest.
