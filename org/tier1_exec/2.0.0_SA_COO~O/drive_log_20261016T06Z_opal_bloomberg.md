# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 37 (EXECUTING), 2026-10-16 04:05Z to 06:30Z (site Z)

Continues `drive_log_20261016T04Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z (PRD v3.12). Commits LOCAL on `box/sitez` unless box-sync has pushed them.

## Done this stretch

| act | result |
|---|---|
| `OG-ng-2` (the commit-time naming gate reads `name_rulings.json`) merged | `f1b3aeb579`; dell1's after-the-fact review ACCEPTED it (msg 34731); announced to the other boxes by `0.0.0_AB_MSTR~Z` |
| `OG-cl-7`, `OG-cl-8` closed by the issuer | `46768b5d8c` (their AC2 failed only because the gate did not read the rows; re-run PASS on trunk) |
| `OG-cl-9`, `OG-cl-10` (the `etfs` row, then its ruling citation) | `80e59dd45e`, `869beac0fa` |
| `OG-ac-1` census of DynamoDB `etf-classifications` | `a69cf430b1`: 11,362 items, hash key `ticker`, `last_updated`, newest 2026-10-08 in a 200-item sample |
| `OG-ac-2` `mdpf_get_security_classification` merged, hooked up | `a7fc4f0499`, `d398a799bc` (registry 122) |
| `OG-ap-25` (one `dynamodb:GetItem` policy) | three halves signed, applied by `~ZS` `3ba4af364d`, ledger CLOSED |
| `OG-rc-1` round-close proof hygiene merged | `647c5b2786` (round-close PROOF-BAD 5 to 2) |
| `OG-ng-3` (two label sites, one `bloomberg_profile` row) merged, closed | `396b0690d5`, `e0a6483e79` |
| `OG-ap-23` Phase A by `~Z` | release `59390627`, 27 tools, gate 0 REFUSE; STOPPED at two measured host gaps |
| `OG-ap-26` Phase A by `~ZS` | `52b0ff8f89`; COO half SIGNED `90b589c58f`; CTO and CVO halves owed |

## Rulings this stretch

- **Z-S161 (ap-23 Phase A blocked on 23 lines, `~Z` msg 34745):** the roster and registry copies leave the release commit and ship by the deploy script at bundle time (amendment A2 `e8b666bc17`); the sparse release tree needs `infra/aws/globgrph` in its cone (the gate's live-read client); `OG-ng-3` took the three real lines. A registry row is global, not per file, so no row for `mdpf` or for a firm token.
- **ap-23 gaps 1 and 2 (`~Z` msg 34753):** (1) the deploy writes none of the six vendor reader env keys: amendment A3 `be681541ec` adds them to the deploy hunk; (2) the classification grant sat on the instance role while the tool reads as the internal reader role: my placement error, corrected by `OG-ap-26` (a one-for-one replacement onto `gateway-global-internal-reader-role`); no dormant ship.
- MC Portal's bundle at `090b9cdc85` rides `OG-ap-23` (amendment A1 `86885e22c8`); `admin_gateway_breakdown.py:164` needs no row.
- The CTO's two later cells (ruling_ref backfill, then the gate refusing an unresolved ref) are drafted (`33076511cf`) and held until `OG-ap-23` has released.

## Open

`OG-ap-23` re-cut on A3 (`~Z`); `OG-ap-26` halves (CTO, CVO); then Phase B GOs. Pending orders to reconcile at round close: `OG-ap-17`, `OG-mg-1`, `OG-cp-1`, `OG-cp-2` (`OG-ap-21` instance written by `~Z`). Row Z-W111-S15 (gf-1 artifact pins) and Z-S160 (three probe principals in the grant store: record as known residue unless Andrew says delete) are mine to disposition.

## Traps met (each cost a retry)

- The harness unescapes a doubled backslash in a heredoc: a Python heredoc that wrote `\n` into a shell script wrote a real newline. Write the byte with `chr(92)` or patch the file from a Write-tool script.
- A check script named `ng1.AC1.sh` already belonged to an older order; list the checks directory before naming one.
- The deliverables lane (`TREE_DELIVERABLES`) lets only a folder's own serial write it; renames and re-proofs of another worker's instance go through a worker order that names the paths.
- A preflight line `comp-iam: RUN-BY-ISSUER` needs a denominator on the same line (`comp-iam stats`), or the issuance gate refuses.
- A worker's sparse tree lacks the gate's live-read client; a worker AC that runs the naming gate can FAIL on an environment line the main tree grades clean: re-run in the main tree before ruling.

## Compiler Tools

`comp-iam stats` (222 roles, 197 services, 1175 operations, 345 gaps) for a preflight denominator; `python .tools/round-close-check.py --project NFRA_OPLGTW --round 37` read-only (REFUSED, 2 proof-bad, 5 ungraded judgment); `comp-surprise --project NFRA_OPLGTW --json` (992 rows, 148 ARMED under investigation project-wide). Gap: no tool answers "which env keys does the host `.env` hold"; `~Z` read names over SSM.
