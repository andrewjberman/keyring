# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 37 closing into round 38 (EXECUTING), 2026-10-16 10:30Z to 12:45Z (site Z)

Continues `drive_log_20261016T10Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z. Commits LOCAL on `box/sitez` unless box-sync pushed them.

## Done this stretch

| act | result |
|---|---|
| `OG-rr-3` (110 CRO ruling_refs) and `OG-rr-2` (the gate checks `ruling_ref`) | merged `12bd6a77d4` and `2c5bd6f1ac`; main-tree checks PASS, pytest 10 passed, planted controls through a throwaway index (unresolved ref REFUSE, new row without a ref REFUSE, unchanged registry PASS); full-add re-grade moved 0 names |
| `OG-mg-1` Phase B (R1 Andrew, R2 the Bloomberg mirror) | all three halves signed (COO `020264306c`, CTO `c92d6c7c07`, CVO `5c4025b899`); `~Z` wrote both, read back, ledger CLOSED; my `mg1.AC2.sh` had read `calendar_months` at the wrong level (Z-S174, mine), fixed `f30d9fdce8`, PASS on the live store |
| E2 (the Bloomberg seat's 8-tool re-exercise) | 7 PASS, 1 NOT PROVEN (`gateway_query_catalog`, reached and refused on key resolution), 0 DENIED; relayed; the CVO graded `OG-ap-14` and `OG-mg-1` AC3 MET, bounded (v33) |
| CVO AC3 grades | ap-18, -20, -21 MET; ap-23 PARTIAL (client holdings lacked a weight unit and currency -> E4); ap-19 closed by an empty-window body (`OG-ev-1` A2); the issuer's two reworded markers (ap-19 A3, ap-23 A8) stated to the CVO |
| ROUND-37 ANALYSIS (CTO msg 34961): MAY-CLOSE | ONE round-38 issuance `e08686be6a` (R3-T.93): `OG-en-4/5/6/8`, `OG-ts-1` to workers `~118..~122`, `OG-en-7` to `~Z`; E1 = `OG-mg-1`, E2 a seat act, E3 mine; the L6 gate floored the five gateway-path orders to WORLD |
| Drained | `OG-en-5` `1c0878d967`, `OG-ts-1` `de390f73e1`, `OG-en-6` `d67f755657`, `OG-en-4` `1a535637fd`, `OG-en-8` `b3427bff5d` (the append-only conflict in the shared investigation file resolved keep-both, then `--continue` through the guards); main-tree named tests PASS for each |
| `OG-en-7` | `~Z`: 6010 SmartX candidates checked, 0 map to another firm; 75 of 10268 roster rows carry an advisor name the map does not hold (outside n) |
| CTO additions | E9 (row Z-S175: a key that does not resolve answers not-found, not 403) and the 429 finding (msg 34991) -> `OG-en-9` (`~123`) and `OG-en-10` (`~124`) `060e0ba6e2` (R3-T.94, workstream `ENRICH-R38-B`); row Z-S177 (ARMED, mine) filed; the CTO ruled the plan: measure first, do not raise the limit or split identities until the first audit rows exist, include an "exempt initialize and tools/list from the count" arm |
| Row dispositions | found that `comp-surprise` moves a row only when a LATER row names it in `adjudicates`; my Z-S166 and Z-S167 lacked it; 114 BLOCKING or ARMED rows (round-37 era) need a disposition before the L10 slug; two read-only triage agents (57 rows each) are reading them |

## Rulings and notes

- **My errors, stated plainly:** `ap27.AC1.sh` (s3:prefix counted as an action), `mg1.AC2.sh` (typed-map top level) and the Z-S166/Z-S167 rows (no `adjudicates`): each was a check or record that did not exercise its own PASS arm against a real shape before it was relied on.
- The lane gate gives a worker's deliverables folder to that serial alone; the issuer does not rewrite a worker's attestation (an override was considered and rejected). A re-seat in a cone that lacked files the gate and tests read failed twice; the main-tree truth stands and the `OG-ng-3` instance row is closed in a later pass.
- `OG-en-4`: eclipse builds no position row (its refusal is pinned); orion's weight scale is unestablished so its unit stays null (carried); the `<status>` flip waits on the worker's instance file name (the gate wants the slug).
- The MCPINDEX v2 catalog landed under OPLGTW's classification pins: 18 of 32 rows absent, all intended removals (16 CTO exclusions, 2 advisor-intelligence scope drops, 0 renames, MI msg 34971); `OG-ts-1` re-pinned the two tests.

## Open

`OG-en-9`, `OG-en-10` (workers running); the batched gateway release cell for `~Z` (E4, E5, E6, E8, E9, E10 on the live ref `1bc2df0b13`, `mcportal_commit` `c66ca82952` for MP, a never-widen narrowing ask for E8, the muse client id configured later by a separate act); the triage-driven `adjudicates` rows for the 114; the post-merge full-suite parity; E3 (the harvest stand-in read, waits on the gateway MCP, itself under the 429); the `OG-ng-3` instance row; then the L10 slug to the CTO.

## Traps met

- A worker's sparse cone needs every file its checks and the commit gate read; each worktree is now widened at provision time (`infra/aws/ec2/opal-gateway`, `lib`, `infra/aws/globgrph`, `.tools`, `infra/logic`, `org/devices`, `org/mcp`, `infra/aws/terraform`, `infra/aws/lambda/ci`, the project tree).
- `safe-merge.sh` refuses to land over an uncommitted edit of a shared path (the append-only investigation file); wait for the peer's commit and retry.
- Any `<paths>` entry under `infra/aws/ec2/opal-gateway/` floors an order's risk at WORLD.

## Compiler Tools

`round-close-check.py --round 37`, `comp-surprise --json` (armed 60, open 288 at 11:3xZ), `git cat-file -e` for the 110 refs, `.tools/wk-provision.sh`, `.tools/safe-merge.sh` (`--continue`). Gap: no tool tells which files a check reads, to size a worker's cone.
