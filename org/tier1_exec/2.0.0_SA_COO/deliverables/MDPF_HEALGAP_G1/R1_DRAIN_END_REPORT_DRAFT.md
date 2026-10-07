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

- `hg_fwd1_exercise.py --failed 2026-10-08`: ...
- restore: `--restored` at ...; fallback used? ...
- `hg_fwd1_exercise.py --healed 2026-10-08`: ... (stamp time, keys per feed)
- the reader: `hg_fwd1_reader.py --date 2026-10-08`: ... (baseline 2026-10-07: READER-OK, point 2026-10-06 model measured,
  $205,755,075.09, written 13:50:50Z)
- 13:30Z floor for D: MET / MISSED (from `0.7.0_AE_CloudOps~F`'s ledger)

## For the round-1 analysis

- FWD-1: REALIZED or NOT REALIZED on the exercise above. The next natural failed morning is the negative arm.
- Enrichment list in the PRD's order: FWD-2 (per-feed result), FWD-3 (now: historical source or restated -- S2), FWD-4 (settings
  true to the AWS async cap), FWD-5 (fire time after the session; the re-attempt already runs after it), FWD-6 (class answer, 49F
  first).
- For the next cut: wiring-only deploy orders omit the code-deploy recorder (S9); deploy grants enumerate the tools' writes (S5).
