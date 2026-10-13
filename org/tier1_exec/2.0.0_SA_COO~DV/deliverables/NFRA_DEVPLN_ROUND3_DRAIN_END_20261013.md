# NFRA_DEVPLN round 3 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-13 ~22:40Z)

Issuance `f3cc33dddc` (PRD v0.3 @14a0501ee5, round-2 analysis @8cf96d5f52, your ruling `CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md`). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 3` reads `reviewer=present (3.0.0_SA_CVO~L) orders=2 verdict=MAY-CLOSE`. Push state (ls-remote `3a7ea53453`): every round-3 commit through `e4140baac7` is on origin/box/laptop; the waiver is on origin/CLOUD @7bcc270380 and NOT yet on origin/box/dell2 @ec7375df9b. No SERVED or WORLD order this round, so no CVO packet.

## 1. The orders (2 of 2 complete, proofs VALID, suites re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-d-1 | `open-calls.py add --kind approval --waive-overlap <sha,...> --waiver-ref <path>`: the DEV-overlap refusal excused for named commits only; a waiver naming a sha outside the overlap, or lacking its ruling file, is refused; `--check-only` accepts any commit-ish. Waiver test 11/11; register 10/10, approval 13/13, open-calls 19/19. On the real portal: the real head `794b7df4` with its two commits named reads `result=OK ... waived=2`; the same call without the waiver reads `REFUSED reason=dev-overlap overlap=2` | `83c73a230e` |
| DP-d-2 | merge-forward falls back to a local-only branch when the ref is absent on origin (told apart from an unreachable origin by `ls-remote`'s exit code, W2-S7); selftest 26/26. On the real portal: the local-only probe now reads `REFUSED reason=no-approval-row` instead of `fetch-failed` | `11046b0733` |

## 2. Your round-2 list, item by item

1. **S03 gate edit (yours): NOT landed.** `.tools/hooks/never-rules-gate.sh` has no commit since `14a0501ee5`. The refusal arm and the gate-bytes read on all four box branches (issuer act A7) run the moment it lands. Under today's gate, a direct DEV push from this seat is already refused (round 2, tick 2).
2. **FWD-2's declined arm, refused: DONE.** On `cand/laptop/declined-example` (row e89f, DECLINED by you), `portal-merge-forward.sh` and `portal-release-build.sh --features` each print `reason=declined`; DEV unchanged at `24877b67`.
3. **The dell2 ANLREQ feature (FWD-1's client-facing case): waiting on dell2.** No `cand/dell2/<slug>` branch from dell2's own work exists yet; no cell can be cut before it does.
4. **The three re-registered merges (bb8b): prepared, waiting on a dell2 seat.** The issuer created and verified, on portal origin, `cand/dell2/anlreq-90-held-submit` @`794b7df4` (2 commits), `anlreq-88-advisory-fee` @`9ef6a359` (1), `anlreq-87-model-order` @`62d455f5` (1), all cut from PROD; they only name commits DEV already merged. The rows must be written by a dell2 seat on dell2's own list (the tool refuses another box's list). The exact commands are in `NFRA_DEVPLN_A12_DELL2_REGISTRATION_COMMANDS_20261013.md`, relayed through `0.0.0_AB_MSTR`.
5. **One batch repair:** W2-S7 done in `DP-d-2`. W2-S8 NOT cut: the pin-drift advisory line comes from `.tools/proof-of-spec-check.py`, outside this project's paths; the row is an OBSERVATION for the CVO.

## 3. For your ruling (one question)

Your ruling says the overlap refusal is waived "for exactly these three named merge shas". The merge commits (`73d8d3a4`, `0101dd66`, `a577cba5`) lie on no branch, so they are never in a registration's overlap. The set the tool can and does excuse is the FOUR FEATURE COMMITS: `923f7d69` and `794b7df4` (one branch), `9ef6a359`, `62d455f5`. The ruling file names only `62d455f5` literally (worker row W1-S12), and the waiver check on `--waiver-ref` is existence only. Please confirm the four-commit reading, or name another set.

## 4. Rows and watermark

Channel: 31 investigation rows, 7 adjudication rows (CVO compiles `0ad3906e16` and the round-2 one), ARMED 0. Round 3's 3 open rows: `W1-S12` (the question above), `W2-S9` (the local fallback reads `refs/heads/<b>` even when a stale `origin/<b>` exists), `W2-S10` (git prints a "multiple merge bases" warning on the three-dot diff; the verdict is unchanged).

## 5. ENRICHMENT candidates for round 4

1. S03, then A7 (the refusal arm on a box seat; the gate bytes on all four box branches).
2. Register and read the three dell2 rows; Andrew rules them; the next chosen-set promote ships only what he approves (a DT order at that time).
3. dell2's next IRPT_ANLREQ change through the route; this project's part is the registration check, the merge-forward and the read.
4. A repair batch: W2-S9 (prefer the stale-safe ref), W2-S10 (the warning).
