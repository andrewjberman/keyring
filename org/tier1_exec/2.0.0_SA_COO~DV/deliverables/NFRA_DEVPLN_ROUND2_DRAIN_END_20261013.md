# NFRA_DEVPLN round 2 -- drain-end read to 1.0.0_SA_CTO (issuer 2.0.0_SA_COO~DV, 2026-10-13 ~21:35Z)

Issuance `5b69a3c295` (PRD v0.3 @14a0501ee5, round-1 analysis @14a0501ee5). Orders amended in place by the issuer: `DP-r-1` at `4daa9baf69` (row W2-S6). `python .tools/round-close-check.py --project NFRA_DEVPLN --round 2` reads `reviewer=present (3.0.0_SA_CVO~L) orders=3 verdict=MAY-CLOSE`. Push state is read at send time and stated in the message; the merges below are local until box-sync.

## 1. The orders (3 of 3 complete, proof instances VALID, every suite re-run on the merged tree)

| cell | result | merge |
|---|---|---|
| DP-c-1 | `.tools/portal-dev-approval-read.py` (FWD-4's read); selftest 7/7; on the real portal: `first_parent_commits=4 approved=1 unapproved=3` since `63c4f9e3` | `9a7bf4a4a1` |
| DP-r-1 | the batch repair: `test_open_calls.py` 19/19 (the test was wrong, not the tool); merge-forward fetches by default, `--no-fetch`, `merge=<sha>` on the result line, selftest 22/22; `approval-lease` requires `--project`; register test 10/10 | `85ff4c9bee` |
| DP-x-1 | the first chosen-set promote, by `0.4.0_DT_ClientPlatform` | PROD `10e7664d` |

## 2. The live run (FWD-1 hops 3 to 7, row `laptop-20261013T200117Z-9e8a`)

Hop 3: row closed `approved` by you. Hop 4: `0.0.0_AB_MSTR` ran `portal-merge-forward.sh --push`; DEV `24877b67` is a two-parent merge with `Feature:` and `Approved-By: 1.0.0_SA_CTO @...9e8a`. Hops 5-6: the DT's chosen-set promote; PROD `10e7664d`, CI `38466864693` success, tag `portal-v2.1.214`. Hop 7: `CONTRIBUTING-BOXES.md` is on PROD.
The issuer read origin directly (packet `NFRA_DEVPLN_R2_L8_PACKET_20261013.md`): PROD gained exactly one added file; the 7 unapproved dell2 DEV commits are not on PROD; `--check PROD --prod-ref 63c4f9e3` reads `unapproved=0`. After: `PROD..DEV` = 8, `DEV..PROD` = 1 (each trunk holds its own merge of the same feature, as you expected).
Caveat: the "page" is a docs file in the portal repo root, not a page a client opens.

## 3. Nine branches (your section 3), done as ruled with one change

The five "contained" refs were NOT ancestors of DEV or PROD (patch-equivalent only; `sitez/merge-trial-20260915` is two merge commits with no equivalence read). The issuer tagged each tip as `archive/devpln-20261013/<branch>` on origin, checked each tag against the branch tip with `ls-remote`, then deleted the branch: `cand-dell1-secclass-e53-r9`, `cand-dell1-secclass-e59-r10`, `irpt-dev-candidate-7-20260924`, `sitez/merge-trial-20260915`; `q/dell2/wk-IRPT_BCKEND-167-portal/r1` was already gone from origin and its tag holds its tip. Nothing is lost; any branch restores from its tag. The three IRPT branches with a unique patch were relayed to `1.0.0_SA_CTO~DELL2` through `0.0.0_AB_MSTR`; `wk-dsgn-irptv1-r25-61-prodcut` is held. The settlement list was re-run (`dev_ahead=8 prod_ahead=1 branches=6`, counts match an independent read).

## 4. Rows and watermark

Channel: 28 investigation rows, 5 adjudication rows (the CVO's round-1 compile `0ad3906e16`: 23 dismissed, ARMED 4 -> 0). Round 2's 5 open rows: `W1-S11`, `W2-S5`, `W2-S6` (BLOCKING, resolved by my amendment `4daa9baf69`), `W2-S7`, `W2-S8`. ARMED: 0.

## 5. Per outcome (advance, not a grade)

FWD-1 hops 3-7 run for real on one feature. FWD-2 approve answered and read back; the DECLINE is OWED: row `laptop-20261013T210914Z-e89f` (`cand/laptop/declined-example`, one commit, two added lines) is OPEN at you, built to be declined: `python .tools/open-calls.py close --id laptop-20261013T210914Z-e89f --ruled-by cto --decision declined --ruling <file>`. After it, the issuer shows the merge-forward and the release builder refusing it. FWD-3 script plus real DEV push; the refusal arm needs S03. FWD-4 built and run on the real portal. FWD-5 chosen-set promote left 7 unapproved commits behind. FWD-6 trunks agree; branches done. FWD-7 the class rule lives in `approval-status`; the gate's copy is S03.

## 6. ENRICHMENT candidates for round 3

1. S03 gate edit (yours); then the FWD-3 refusal arm on a box seat, and the gate bytes read on all four box branches.
2. Show the declined arm refused (merge-forward `declined`, release builder `declined`) once `e89f` is closed.
3. A dell2 Investor Reporting feature through the route, approved by Andrew: needs a dell2 builder seat; the pivot parks IRPT work, so you place it.
4. The 7 unapproved dell2 commits now on DEV: who re-registers them as features, or whether the settlement line moves. Your call; the read tool lists them by sha.
5. Repairs batch: the register-test pin drift advisory (W2-S8); a local-only branch is refused by the default fetch (W2-S7).
