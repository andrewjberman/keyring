# `/self-drive AMGT_RESAPP` -- relaunch tick 7: amendment 9 validated, S127 measured and carded (`1.0.0_SA_CTO~Z`, 2026-09-16 16:58Z)

**archetype:** VALIDATE · **state:** `ARMED` · **cadence:** 30m at `17,47` · **job (then):** `884c0211` · **ticks covered:** 7.
Authority: `org/XXX.md` Step 1b-F row for `1.0.0_SA_CTO~Z`; this lane adjudicates.

## Completion test

**NOT DONE** -- `status: active`, `dep_stage: EXECUTING`, **7 of 16** orders terminal (rk-1, rk-3, rk-4, rk-5, rk-9, rk-10, rk-11), 0
`COMPLETION_*`. Sequence: UNPLACED, 0 flags. HEAD `4e5dd7201f`; PRD v0.10 ADMITTED, both halves current; round-12 slug ABSENT
(correct); MERGE_HEAD absent; porcelain 0; 0 unmerged branches; the deployed adapter still reads the restored sha `9ubWPnhz`
(16:18:57Z). Live workers: rk-2 (`~24`, the fix-forward under AC7/AC8), rk-13 (`~25`, the ranker re-run).

## Delta since the tick-6 log (@`877782d502`)

1. **ISSUER AMENDMENT 9 @`1c0639a019` VALIDATED on the bytes -- RAVC 4 CLOSE on 23463 s.3-4 (recorded here; no message, heads-down).**
   rk-2 now carries 8 criteria and 11 `<paths>` including `lib/research/rules/`, `org/critical_paths/change_management/` and
   `org/critical_paths/.open_deploys/`. **AC7** = the pre/post GET route census, `CENSUS_MODE=pre` before any deploy, graded after:
   MET only when `lost` and `gained` are both empty AND the deployed code changed (an unchanged plane reads equal-but-not-changed,
   NOT met -- the criterion cannot pass vacuously). **AC8** = a STATIC census of the uploaded artifact: both `rules/data` JSON files
   packaged, 0 rules references to the `~8` deliverables, and every packaged repo-relative line classified in
   `REPO_RELATIVE_CENSUS.json` as PACKAGED / NOT-A-READ / OUT-OF-SCOPE with `unclassified 0` (today 13 lines in 9 of 37 modules,
   0 data files: correct pre-state). The extracted-artifact smoke run was dropped because the zip's Linux-built `rpds` extension
   cannot import on this box -- a static census is the right instrument here and the served census (AC7) is the dynamic one.
   AC5 re-cut to `/overlay`'s posture object (`/posture` is not a served route, W24-S3); AC1's regex repaired (W24-S5). Row S128
   disarms W24-S3. Both conditions of the ruling met; the class censused, not the instance.
2. **S127 MEASURED as ruled (msg 23468):** by a source read of the producer's call graph, not a run -- `lib/research/filings/analyze.py:193-206`
   `anthropic_call`, `:269`/`:425` the two analyzer passes, `:585` the served `thesis_driver` is the model pass's output. As the
   producer stands, regenerating `BA_US_Equity`'s filings document IS a vendor call, so it sits under **CARD 2** as a ONE-NAME pilot
   re-run (~USD 1.1); it becomes the issuer's to order only if rk-15's producer derives the driver's points with no model call --
   unknowable until rk-15 is built, so rk-7 AC5 stays sequenced after rk-15 and the question re-opens at rk-15's drain. Nothing runs
   meanwhile. **CARD 2's register line now carries the S127 rider** (this commit).
3. `4.0.0_SA_CRO~Z` closed its s.3c @`4e5dd7201f` on its own instrument at 16:39:49Z -- three seats, three instruments, one restore.

## Open calls in scope

| call | class | state |
|---|---|---|
| 23440 · S120 · S124 · S125 · ESCALATION 23462 | ADJUDICABLE | all RULED, APPLIED (amendments 3, 6, 7, 8, 9) or EXECUTED (the rollback); closed |
| CARD 1 model-block pull + the price pull (one Bloomberg-gated card at the L10) | RESERVED -- vendor budget | at Andrew |
| CARD 2 filings batch (~USD 1.1/filing) **+ S127's one-name pilot re-run for `BA_US_Equity` if rk-15 still needs the model pass** | RESERVED -- spend / vendor | at Andrew |
| CARD 3 portal DEV fast-forward + push (LD-0367/0368) | RESERVED -- shared-branch push | at Andrew via `0.0.0_AB_MSTR~Z`, rec YES now |
| SITEZ push / merge leg (LD-0522) | RESERVED | `0.0.0_AB_MSTR~Z` on his word |

No new call this tick. Five adjudicable this session, five closed; the all-reserved tell did not fire.

## Who owes what

`2.0.0_SA_COO~Z`: rk-2's fix-forward and redeploy under AC7/AC8 (its census before, its census after); rk-13's drain; rk-8 on chain A;
rk-6 after rk-2 with its fresh co-sign; drains; the L8 packet. `3.0.0_SA_CVO~Z`: L8/L9 on the 7 completions and the rows through
S128. `0.0.0_AB_MSTR~Z`: CARD 3 + the SITEZ push at Andrew. This seat: rk-6's CTO co-sign half when asked (blast radius = every
served route, AMENDMENT 2); the L10 when the slug lands.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criteria + `<paths>` re-read (python over `<criterion>` and `<paths>`) | rk-2 8 criteria, 11 paths | amendment 9 validated on the bytes |
| `.tools/aws lambda get-function-configuration` | sha `9ubWPnhz`, 16:18:57Z | the restore holds |
| `prd-signoff.py status` / `git branch --no-merged HEAD` | ADMITTED / 0 | nothing owed at L4-R; no orphan |
| `missions-tree-index.py check` (at commit) | 0 violations | on the register edit |

**Gap found:** none. The static-vs-dynamic split on AC8/AC7 is the right shape for an artifact this box cannot import; noted for the
round-13 battery as the pattern for any Linux-built zip.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`; none requested.
