# MDPF_HEALGAP round 1 -- the COO's drain-end read (DRAFT; final after the 2026-10-08 exercise)

**From:** `2.0.0_SA_COO~G1` (dell1). **To:** `1.0.0_SA_CTO~DELL1`, the round's one COO message (spine L7, the drain-end read).
**Status:** DRAFT 2026-10-07 ~19:1xZ. Everything below the line "EXERCISE" is filled in after 2026-10-08 ~14:00Z.

## The round

- Cut on PRD v0.1 @78db344481 (L4-R ADMITTED). Decomposition `decompositions/MDPF_HEALGAP_DECOMP.md` @474ec88e5a, round 1 = the
  FWD-1 thread, hops 0-5. Hop 0 measured at the base (no cell): the 2026-08-31..09-10 model_detail hole was the count-reconcile
  raise, closed by `c53e48f7fb` (row S3); the guard was dead (s3:GetObject UNGRANTED).
- Andrew's words this round: ACT 1 standing vendor word for the same-day re-run, the R20 naming exception, ACT 2 refill NO, two
  worktree deletes (records @e5fb41862f, @06d7fa808f).

| order | what | state | evidence |
|---|---|---|---|
| HG-t-1 | guard by listing + `induce` hook (runner code) | complete, drained @ca914096d7 | proof VALID; issuer re-ran AC1/AC2 + 17 legacy tests |
| HG-t-2 | second target on `cot-bronze-complete` (Terraform) | complete, drained @c266bbbd11 | proof VALID; one literal, source_arn from the target's rule (R20 X16, entry @a79b6838e4) |
| HG-d1 | deploy HG-t-1 (laptop, `0.7.0_AE_CloudOps~F`) | complete | live CodeSha256 `QxLv...Mvk=` 10:44:25Z; proof VALID on origin |
| HG-d2 | apply HG-t-2 (laptop) | complete | SKIP probe live 16:15:36Z (0 bronze writes); apply 16:47Z, plan 2/0/0; `WIRED-OK`; proof VALID |
| HG-d3 | FWD-1 exercise, 2026-10-08 | pending | induce input set 17:40:36Z; fires 06:00Z |

## Rows (the channel `surprise-channel/investigations/INVESTIGATION_v1.md`)

S2 (FWD-3: no as-of to the vendor -> a refill fabricates history; Andrew: no refill), S3 (hop 0 answered; 14-day log retention),
W1-S1 + S4 (ruff drift; disarmed; box fixed), W2-S1 + W2-S2 (naming gate on the literal; ruled), S5 + S9 (my cut defects: a deploy
grant narrower than its tools; a code-deploy recorder copied into a wiring order), S6 + S7 + S10 (tool defects outside the
project: `deploy_ledger.py close` rewrites other sentinels; `safe-apply` reports a path fault as a naming block; plan/recorder
diagnostic ambiguity), S8 (pre-rule terraform checkpoint calls). No ARMED row open.

## EXERCISE (2026-10-08) -- to fill

- `hg_fwd1_exercise.py --failed 2026-10-08`: FAILED-OK -- the 06:00Z fire hit the induced auth-lapse (3 INDUCED log lines),
  0 bronze keys before 11:00Z (read 06:07Z and again 11:45:14Z).
- restore: `--restored` RESTORED-OK at 06:10:23Z. The input was put back at 06:08:46Z (CloudTrail PutTargets, user/Andrew_Berman,
  laptop credential, input `{"mode":"pull"}`, inside the 06:05-06:20Z window) by an actor none of the three named owners claims --
  row D1-S3. Fallback (owner 2) ran 06:10:09Z and the OS task 06:11:01Z: both NOOP-ALREADY-RESTORED.
- `hg_fwd1_exercise.py --healed 2026-10-08`: HEALED-OK -- stamp_at 11:32:25Z; keys rebalancer_models 1, rebalancer_accounts 5,
  rebalancer_model_detail 93. Runner log: the re-attempt target fired on cot-bronze-complete, invoked 11:32:06Z, verdict
  BRONZE-COMPLETE 11:32:24Z (71 models, 992 accounts, 93 model details; 1 of 54 count-reconcile mismatch CARRIED). Branch B
  (same-day manual re-run) not needed.
- the reader: `hg_fwd1_reader.py --date 2026-10-08`: ... (baseline 2026-10-07: READER-OK, point 2026-10-06 model measured,
  $205,755,075.09, written 13:50:50Z)
- 13:30Z floor for D: MET / MISSED (from `0.7.0_AE_CloudOps~F`'s ledger)

## For the round-1 analysis

- FWD-1: REALIZED or NOT REALIZED on the exercise above. The next natural failed morning is the negative arm.
- Enrichment list in the PRD's order: FWD-2 (per-feed result), FWD-3 (now: historical source or restated -- S2), FWD-4 (settings
  true to the AWS async cap), FWD-5 (fire time after the session; the re-attempt already runs after it), FWD-6 (class answer, 49F
  first).
- For the next cut: wiring-only deploy orders omit the code-deploy recorder (S9); deploy grants enumerate the tools' writes (S5).
