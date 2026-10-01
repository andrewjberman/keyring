# Never-widen sign-off packet 3 -- irpt-performance-adapter: a retained vendor figure no longer reopens, and a firm not yet on the holdings basis answers ONE code (row IRPT_BCKEND-S247)

Author `2.0.0_SA_COO~P`, 2026-10-01 ~08:0xZ. Ledger `irpt-adapter-holdings-basis-only-20261001` (OPEN @d9b82c5bf7, two legs). Ordered by
CTO rulings batch 66 items 2-3 (@00c21abade), batch 67 item 4 (@5585734946) and decision 103586 (ship CLOUD's `retained.py`).
Halves owed: `1.0.0_SA_CTO` and `2.0.0_SA_COO~P` (signed below). Packet pin: commit `b15f0ed7df` for the two members that move.
No CRO half: the wording of the code on the page is `2.0.0_SA_COO~D`'s (batch 67 item 4, last sentence), and no figure is added.

## 1. The act, exactly

ONE targeted `safe-apply` of `module.irpt_performance_adapter.aws_lambda_function.this` (root `investor-reporting/performance`).
Full plan of the root at 08:00Z: `0 to add, 1 to change, 0 to destroy`, that resource alone.

| | BEFORE = live | AFTER |
|---|---|---|
| CodeSha256 | `PCcoNYrBQ7Cb7ma0A01SRVRQ3l5t5gr5Jqv8ihH2LR0=` (applied 06:22:07Z, packet 2) | `cdbFZDJAW5g4ym+3wl9kyD9WVfYmm6AVZBuwd0c6eJI=` |
| S3 version of `investor-reporting/irpt-performance-adapter.zip` | `v9P9cM48YRbGrRdruzPCmVkKgVrFRMbW` | `wjneBb9_GyncZ6pLr_Q.hPbk86sXLLUj` (built 07:56Z from d9b82c5bf7, 428,833 bytes) |
| members | 70 | 70: changed `retained.py`, `entry.py`; added 0; removed 0 |

Census against the live zip downloaded from Lambda (its bytes hash to the live CodeSha256). The uploaded zip equals, member for
member, the bundle assembled locally before the upload, which is the bundle section 3's harness ran (0 of 70 differ).

## 2. What the two members change (read from the bytes at b15f0ed7df)

- **`retained.py`** (live pin c7f136c9d8 -> b15f0ed7df; two commits: IB-pr-221's ee3ff32e71 and the fix 4351bc54c1).
  - The fix: when an EXISTING accepted pointer is reopened, a report whose `lineage.provider` is not `OPAL_HOLDINGS` raises
    `RetainedVendorFigureRefused`. The fresh path's own reopen right after persisting is unchanged. No object is deleted.
  - IB-pr-221's part of this file, which rides because the live file is one commit behind (ruled in 103586): a firm is composed
    only when the installation supplies its holdings source. The live `installed.py` supplies one for 49 Financial and none for
    Inflection, so every Inflection request is refused `ProviderPathNotComposed` before any mapping read, where today it reaches
    the Orion mapping. NO Inflection gold is served by this: `installed.py` and `holdings_gold.py` do not move (batch 63 item 4).
- **`entry.py`** (the reasons map only): `VendorEgressRefused` `DEPENDENCY_UNAVAILABLE` -> `OBJECT_NOT_COVERED`;
  `RetainedVendorFigureRefused` named, `OBJECT_NOT_COVERED`; `ProviderPathNotComposed` `UNSUPPORTED_OPERATION` ->
  `OBJECT_NOT_COVERED`. The refusal's action stays `NONE` (no retry offered), which is "retryable false" in this envelope.

## 3. The changed branches, MEASURED before and after on the exact bytes

`IRPT_MVP_P/retained_reopen_before_after.py` (committed with this packet): each bundle's own `runtime._build()`
composes the retained service with the live function's environment. Two things differ from the served path, both by design:
`authorize` is stubbed true (the question is what the reopen RETURNS), and the vendor transport is stubbed to raise the bundle's
own `VendorEgressRefused`, so no vendor call is possible. Reads only (S3 GetObject and ListObjectsV2, DynamoDB GetItem).
BEFORE = the live artifact `PCcoNYrB...`; AFTER = this packet's artifact.

| case (the three retained non-49F reports are every object under `irpt/inflection` and `irpt/cottonwood` `performance_reports/`) | BEFORE | AFTER |
|---|---|---|
| reopen Inflection `RPT-df47a1fc...` (provider ORION), its own account set and window | REOPENED, the ORION figure returned | `ProviderPathNotComposed` -> `OBJECT_NOT_COVERED` |
| reopen Cottonwood `RPT-12b885b8...` (BLACK_DIAMOND) | REOPENED, the vendor figure returned | `RetainedVendorFigureRefused` -> `OBJECT_NOT_COVERED` |
| reopen Cottonwood `RPT-b683f188...` (BLACK_DIAMOND) | REOPENED, the vendor figure returned | `RetainedVendorFigureRefused` -> `OBJECT_NOT_COVERED` |
| fresh Inflection, a window no report covers | `VendorEgressRefused` -> `DEPENDENCY_UNAVAILABLE` | `ProviderPathNotComposed` -> `OBJECT_NOT_COVERED` |
| fresh Cottonwood, a window no report covers | `VendorEgressRefused` -> `DEPENDENCY_UNAVAILABLE` | `VendorEgressRefused` -> `OBJECT_NOT_COVERED` |
| CONTROL: reopen the newest 49 Financial report whose provider is OPAL_HOLDINGS (112 objects listed) | REOPENED, OPAL_HOLDINGS | REOPENED, OPAL_HOLDINGS |

So row S247's open question is answered by measurement: the LIVE reopen path returns all three vendor-figure reports for their
own account set and window. How many of the 47 logged reopens were one of them stays UNMEASURED (the log names no report).

A live HTTP invoke that reaches `retained.py` for Inflection or Cottonwood needs a trusted-header identity that the enforcer
admits to that firm's account. This seat does not forge a privileged subject on the served function; the branch is measured by the
harness above, and condition 4 reads the first real request after the apply from the function's own log.

## 4. Import closure and interface, on the uploaded zip

- `served.py`'s closure (batch 62 item 6): 17 members, 0 differ from CLOUD.
- `retained.py`'s closure (`served_import_closure.py --root retained.py`): 15 members, 14 EQUAL to CLOUD, ONE older:
  `holdings_gold.py` (bundled `afc37c0a0123`, pin a595a14264, one commit behind: IB-pr-221's firm-agnostic rewrite, held by batch
  63 item 4). `retained.py` uses two things from it, `PROVIDER` and `calculate(scope, start, end, source)`; both are in the bundled
  version (interface gate), and 49 Financial runs the same `holdings_gold.py` bytes it runs today.
- `sibling_interface_check.py`: 0 findings from `runtime.py` (41 reachable modules, 302 cross-module calls) and 0 from
  `served.py` (17, 108). The same gate reads 3, 2, 2 findings on the three candidates withdrawn from packet 1 (negative control).
- Tests at b15f0ed7df: the performance suite 230 passed (229 before the fix; one test added).

## 5. Blast radius

| who asks | BEFORE | AFTER |
|---|---|---|
| 49 Financial, any request | holdings basis, served or its named refusals | unchanged (same `holdings_gold.py`, same reopen; control above) |
| Cottonwood, fresh | refused, `DEPENDENCY_UNAVAILABLE` | refused, `OBJECT_NOT_COVERED` |
| Cottonwood, the exact account set and window of a retained report | the BLACK_DIAMOND figure | refused, `OBJECT_NOT_COVERED` |
| Inflection, fresh | Orion mapping read, then refused (`DEPENDENCY_UNAVAILABLE`, or `OBJECT_NOT_COVERED` for an unmapped account) | refused `OBJECT_NOT_COVERED` before any mapping read |
| Inflection, the exact account set and window of the retained report | the ORION figure | refused, `OBJECT_NOT_COVERED` |
| an uncomposed or unknown firm | `UNSUPPORTED_OPERATION` | `OBJECT_NOT_COVERED` |

What a viewer loses: the two firms' three retained vendor figures stop being reachable through the Performance route. That is the
ruling's purpose (FWD-3; Andrew's word of 2026-09-28). The objects stay in `opal-data-irpt` as FWD-13's comparison points.
The page: `2.0.0_SA_COO~D` words `OBJECT_NOT_COVERED` on the Performance tab ("not available for this client yet"); until that
lands the tab shows whatever it shows today for `OBJECT_NOT_COVERED` on a 49 Financial account its gold does not cover.

Writers of the function's code pointer: 1 (its module). Pullers of the artifact: 1 function (live-plane census of packet 1, 224
functions listed; the key is named by no second module).

## 6. Rollback

`s3api copy-object` of version `v9P9cM48YRbGrRdruzPCmVkKgVrFRMbW` (metadata `content-sha256` = the BEFORE CodeSha256) over the key,
then the same targeted `safe-apply`. Same window.

## 7. Conditions

1. One targeted apply; plan exactly `0 to add, 1 to change, 0 to destroy` on `aws_lambda_function.this`.
2. Before and after: one `lambda invoke` with empty headers (`CONTRACT_VERSION`) and one with trusted headers for cottonwood and
   a NON-EXISTENT user naming `performance-report` (a refusal raised after enforcement); no `FunctionError`, no `errorMessage`,
   BEFORE equal to AFTER.
3. Post-apply CodeSha256 equals the AFTER value; a re-plan reads `No changes`.
4. The harness of section 3 re-run with AFTER = the DEPLOYED bytes (downloaded from Lambda after the apply): the same six rows.
5. Ten minutes of the log after the apply: zero `TypeError`, `ImportModuleError`, `Traceback`, timeout lines; any performance
   request in the window that answers `UNEXPECTED` and would not have before is a rollback.
6. Row S247's disarm owner is this seat: it files the disarming row in the channel citing condition 4's six rows, the same turn,
   and `1.0.0_SA_CTO` reads it.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-01 ~08:0xZ, on this packet's bytes at the commit that carries it. Write set: one function's code pointer. The
branches of section 5 are measured in section 3, not predicted.

## CTO half

SIGNED, 2026-10-01T08:13Z, `1.0.0_SA_CTO`, on the pre-signature blob `dbf3006b9f` (@d570f71aa1). Write set: one function's code
pointer. Conditions 1 to 6 stand as written.

Read by this seat, from bytes (script `check_p3.py`, session scratch; reads only):

- Both S3 versions were downloaded by version id. The sha256 of each equals the packet's BEFORE and AFTER CodeSha256. The live
  function configuration reads the BEFORE value (last modified 06:22:07Z).
- 70 members before and 70 after; 0 added, 0 removed; exactly 2 changed, `entry.py` and `retained.py`, each byte-equal to
  `git show b15f0ed7df:` of `performance/entry.py` and `performance/retained.py`.
- The bundled `holdings_gold.py` and `installed.py` are byte-identical to the live bundle. `holdings_gold.py:43` reads
  `PROVIDER = "OPAL_HOLDINGS"` and `:158` reads `calculate(scope, start, end, source)`: the two names the new `retained.py` uses.
  `retained.py` imports neither `installed` nor `request_composition`.
- The diff of the two members, read line by line: the reopen refusal fires only when an EXISTING pointer is reopened and its
  `lineage.provider` is not the holdings basis; an Inflection request with no holdings source is refused before any mapping read;
  the reasons map changes three entries and adds none outside them.

Not verified by this seat: the six rows of section 3 (the COO's measurement; condition 4 repeats it on the deployed bytes), the
interface gate's counts, the 230 tests.

Named by this half in addition:

7. A BRANCH THIS ACT DOES NOT REMOVE. A fresh Cottonwood request made while a one-use vendor plan is ARMED still computes a
   BLACK_DIAMOND figure and returns it once; the fresh path's own reopen is unchanged, and a later reopen of that report is
   refused. The apply neither creates nor closes this branch. The plan is read disarmed at the apply and the read is stated in the
   ledger. Arming it again is its own act under Andrew's vendor word, and a fresh vendor figure for Cottonwood is against FWD-3.
8. The docstring of `RetainedVendorFigureRefused` still names `DEPENDENCY_UNAVAILABLE`; the map answers `OBJECT_NOT_COVERED`. A
   comment, corrected at the file's next change. Not a condition of the apply.
9. Both outcomes of the apply are covered: a plan other than `0 to add, 1 to change, 0 to destroy`, or a post-apply CodeSha256
   other than the AFTER value, ends the act with section 6's rollback in the same window.
