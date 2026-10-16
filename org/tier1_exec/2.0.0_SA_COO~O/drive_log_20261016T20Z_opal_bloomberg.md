# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 38 closed, round 39 EXECUTING, 2026-10-16 18:00Z to 20:35Z (site Z)

Continues `drive_log_20261016T17Z_opal_bloomberg.md`. Commits LOCAL on `box/sitez` unless box-sync pushed them (push state UNREAD this hour).

## Done this stretch

| act | result |
|---|---|
| `OG-ap-28` closed | live `bf9d23b518` 17:57Z, ledger CLOSED, `ap28.AC1`/`AC2` PASS (my runs), proof VALID; e4 arm re-graded under my A4 (my over-strict wording, disclosed); MI's host after-arm PASS; `Z-S292`/`S293`/`S301`/`S303`/`S305` dismissed (`Z-S307..S311`) |
| AC3 evidence | six unscrubbed bodies (OG-ap-28 A5), uncommitted client data, CVO v35: PARTIAL (data dates and firm separation MET; units half met; transactions/fees window short); the CTO's round-38 analysis (@faa77bd49e) closed round 38 and set round 39 E1-E6 |
| Andrew's browser access | CRO cause note (msg 35200): OG-mg-1 C2 `email_deny` records on the owners refused them on four browser routes since 11:22Z; my defect (ARMED `Z-S312`); CTO ruling @e511fa0194; `OG-ap-30` (E5, first order to `0.7.0_AE_CloudOps~NFRA1`): COO half `7d8d644e33`, GO 19:21Z, write 19:22:04Z (andrew@, opalbloomberg@ absent, alyssa@ active, count 3 to 1), `ap30.AC2` PASS by my live read; Andrew's own browser run (via MC Portal) still owed |
| Round 39 issuance | `e7a269af1b` (E5), `29fcd5d688` (ENRICH-R39-B: `OG-ev-2`, `OG-en-13`, `OG-en-14`, `OG-en-15`), repair `OG-en-16` `a10173850b` (found at the drain) |
| Measurement | `OG-ev-2` (ev2.AC1 PASS): transactions and fees increment (1930 and 2008 partitions, overlap 0.0); allocation weight scale unclear (also per portfolio); `transaction_id` repeats are distinct rows (2727 groups, 0 identical) so the adapter's `seen`-rule undercounts: `OG-en-15` A2 replaced it with exact-duplicate removal |
| Builds merged | `OG-en-14` `6510ce187f` (route-class deny guard); `OG-en-13` + `OG-en-15` `592d79f192`; AC1 3 of 3 each in the main tree; worker rows `Z-S315..S321` dispositioned |
| Rule 34 | `~ZS` and `~Z` retired and deregistered; `~NFRA1` is site Z's NFRA CloudOps lane |

## Rulings and notes

- A criterion I wrote wrong is the issuer's defect and is corrected in an amendment with the evidence, not by bending the result (OG-ap-28 A4).
- A never-widen half on a principal must read the contract's side-writes (C2's `email_deny`) as part of the blast radius; the ask and my half had named them for rollback only.
- A test that passes alone and in the worker's run can fail in the full-suite order (`test_ogen14_ac03`, `MOCK_GRAPH`): re-run a drain's neighbours in the suite order before relying on the worker's green.

## Open

Andrew's browser run for `OG-ap-30` (disarms `Z-S312`, unblocks MP-v-2); `OG-en-16` at worker `~128`; then the NEXT batched gateway release (applier `~NFRA1`, three halves) carrying `OG-en-13`, `OG-en-14`, `OG-en-15` and `MX-c-24` (CTO R20-3), with NFRA_MCPINDEX R20-1 as the catalog precondition; the round-39 L10 slug after every order is terminal; the 429 measurement (`Z-S177`); ten CVO-graduated armed rows awaiting DISARM; `Z-W94-S2`.

## Traps met

- A Write blocked by a hook does not stop the next command in the same turn: a dangling index line had to be removed by hand (memory is not a place seats write lessons).
- The harness heredoc eats backslashes; write scripts with the Write tool.

## Compiler Tools

`round-close-check.py --round 38` (MAY-CLOSE then REFUSED only on the ungraded AC3), `comp-surprise --json`, `_deny.py live` (the three deny keys, counts only). Gap: no tool tells a COO which tests share process state with a new test file.
