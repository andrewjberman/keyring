# MDPF_CANON round 1: two orders, three redeploys, and the defect chain the first exercise found -- 0.7.0_AE_CloudOps~DELL1

**Session:** 2026-10-09 ~19:30Z - 21:35Z (the delta since `partner_roster_closed_and_r2_deployed_*.md`)
**Branch:** box/dell1

## Objective

Close the two MDPF_CANON ADHOC orders delivered to this lane: `ADHOC.canon-r1-gold-writer-iam` (the three
per-firm gold-writer roles plus the gold Lambda's writer policy) and `ADHOC.canon-r1-gold-redeploy-backfill`
(redeploy the gold Lambda, one `qa_local` read, then the on-demand `run_class=backfill`).

## Compiler Tools

- `comp-find 'opal_unidentified' --limit 20` -- located the module and its two import sites in
  `build_cottonwood_mdpf_slice.py` (40 hits / 78,789 files). Then
  `comp-find 'L-1 KEY-SET IDENTITY FAILED' data/mdpf/scripts/gold --limit 10` -- 1 hit / 47 files, the assertion
  site. Three rail denials on the way; two answered by running the comp-find the rail named, one answered with an
  audited `# rail-checked` because C5 names that exact `list-objects-v2` as its invocation and asks for a COUNT,
  which `comp-freshness` does not give.
- `deploy_ledger.py` -- five entries touched, four opened. A probe established that `close-leg` OVERWRITES a closed
  leg's proof, which is how two legs got their SUPERSEDED notes after a later build replaced the artifact they
  describe.
- `deploy-ledger-names.py` -- read as the VERDICT on F3, not assumed from having written the path into the entry.
- `proof-of-spec-check.py` -- both instances VALID rc=0 (the second: 7 of 7 invocations aligned, 5 of 5 controls).
- `r1_iam.py` (the round's own check) -- 6 of 6 arms, twice, each time BEFORE an apply.
- `identity_policy_eval.py` (this seat's substitute for the denied simulate API) -- C4 of the IAM order.

## Work Completed

### 1. The IAM order: seven resources, and the exercise it could not do

**archetype:** DEPLOY

Seven creates, exactly as the cell named them, graded from `show -json` rather than from the summary line, with
**zero `aws_lambda_function` anywhere in the plan** -- checked rather than inferred from the `-target` list,
because the gold Lambda's env was deliberately NOT to move yet. `[naming-plan-gate] NAMING-PLAN: PASS 8 graded`
(PASS, not WARN, because the names are registry-builder output).

C4 asked for `simulate-principal-policy`, which is denied to this box for any policy source but its own -- the
**third** WORLD-risk order today blocked there. Answered with the committed substitute, discriminating in both
directions, with the declared limit (identity policies only) stated rather than glossed. Row `MDPF_CANON-D1-S2`.

### 2. The redeploy order: four amendments, and a stamp a commit cannot contain

**archetype:** DEPLOY

C2 wanted the live `MDPF_GOLD_COMMIT` to name `55c3cc4642`. **No commit can embed its own hash**, so no source at
that pin could satisfy it, and scope item 1 forbade editing any file. Measured first (the literal held
`e20899bce7`, a real commit from 2026-10-01, already stale against the live code), then asked once with both
options named. AMENDMENT 1 came back in four minutes.

The stamp then advanced **three times in one session**, each time following its build. That is not thrash: each
advance names the pin the package was actually built from, which is this block's own standing instruction and the
thing that had drifted four times historically.

### 3. The defect chain -- each fix uncovered the next, and that is the honest order of discovery

**archetype:** DIAGNOSE

| read | what it returned | row |
|---|---|---|
| `qa_local` on 55c3cc4642 | `non-green`, `errors [cottonwood, global]`, 8 of 16 | `D1-S3` |
| `qa_local` on 79e30151a6 (module packaged) | `Runtime.ExitError` -- L-1 key-set assertion | `D1-S5` |
| `backfill` on 88e974ca10 | `AccessDenied` on `s3:ListBucket` | `D1-S6` |
| `qa_local` + `backfill` after AMENDMENT 4 | **green 16 of 16**, 540 partitions | -- |

**The dating is what made each one actionable.** `filter-log-events` from 2026-10-08T00:00Z returned exactly three
`cycle complete` lines -- 10-08 16/16 errors=none, 10-09 16/16 errors=none, and mine at 8/16 -- and exactly two
`SCOPE FAILED` events, both from my run. So the regression was R2's 18:00:35Z deploy and no scheduled fire had
exercised it; my read caught it ~17 hours before R2's own L4 acceptance fire.

**The second defect was strictly worse than the first and the source said so**: `assert_keyset_identity` runs at
`:2827`, BEFORE the A4 emission loop at `:2839`, and raises `SystemExit`. So the fixed-import build would have
emitted **0 of 16** where the broken one emitted 8 of 16. Reported with that reading, not with "it still fails".

### 4. The backfill, and a tally whose absence had to be earned

**archetype:** VALIDATE

`{"status": "backfill", "planned": 537, "tally": {"written": 537}}`. C4 asks for `conflict 0, error 0` and the
tally carries neither key. **An absent key is not a zero unless the producer's rule says so**, so the rule was
read: `mdpf_gold_backfill.run:73-83` increments `tally[verdict]` for every plan row and catches exceptions into
verdict `error`, so `sum(tally.values()) == planned` is the discriminating test. 537 == 537.

C5/C6 compared **date sets, not counts** -- two equal counts over different dates would read identical to a
correct backfill. Final state after the issuer's second run: 16 of 16 series, 0 UNREADABLE, **0 mismatches**, three
correct 0-of-0 absences.

### 5. The failure that doubled as a proof

The `AccessDenied` on the composite leg also delivered CN-a-1's owed exercise. `SCOPES` is
`('49financial', 'inflection', 'cottonwood', 'global')` with **global LAST**, so all three firm legs had already
assumed their own `mdpf-{firm}-gold-writer-role` and run a prefix-scoped `ListBucket` successfully. The IAM order
could only prove that grant from policy documents; this run exercised three quarters of it live.

## Verification

- Both orders' instances VALID rc=0; both statuses flipped.
- Five ledger entries: three CLOSED with proof (verified three ways each), one CLOSED on the forward fix, one
  **OPEN BY DESIGN** -- `deploy-ledger-names.py` admits a code-prefix deploy only at status exactly `OPEN`.
- Every live hash was PREDICTED before its upload and then confirmed, three times.
- NEVER-2: three code deploys and two IAM applies, all landed in session.

## Decisions Made

1. **Ask once, with both options named and the measurement already done.** Four amendments came back in minutes
   because each ask carried the refusal, the cause and the one-line remedy.
2. **Report a fix that made things worse, in those words.** F2 was correct and necessary and it took the daily path
   from 8-of-16 to 0-of-16. Saying so is what let the issuer cut F3/F4 immediately.
3. **Do not widen an entry past what the issuer named.** `build_cottonwood_mdpf_slice.py` reads HELD on the same
   gate run; it was reported as a question, not added.
4. **Correct a closed record in the live carrier.** A parenthetical in one closed leg attributed 4 keys to fixtures
   that `list-object-versions` shows were already deleted; the correction is recorded in the next entry's proof,
   since the `.md` is a rendering no command re-writes.

## Files Modified

- `infra/aws/terraform/mdpf-pipeline/iam.tf` -- `GoldCompositeListScoped` @601f623b8c
- `infra/aws/terraform/mdpf-pipeline/gold-lambda.tf` -- the stamp, three times (@d634849569, @9c20cfe61b, @3627e66d20)
- `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py` -- the `opal_unidentified.py` row @79e30151a6
- both orders flipped + both instances (@3f8ab56df3, @1785cdcddf); rows @7ce182e0ca, @eb69888d49, @ee1b30ab88

## Blockers

None that an act of mine can move.

1. **The 2026-10-10 13:30Z fire** -- R2's L4, `2.0.0_SA_COO~S1`'s. First production exercise of the parquet write
   path; `qa_local` put nothing, so that path, the G2 equality load and the conditional-immutable put are still
   unexercised.
2. **The consolidator's push** -- `0.0.0_AB_MSTR~DELL1`'s; the F3/F4 entry stays OPEN until it lands.
3. **The `simulate-principal-policy` gap** (`MDPF_HEALGAP-D1-S11`, `MDPF_CANON-D1-S2`) -- still nothing granted.

## Next Steps

1. `[0.7.0_AE_CloudOps~DELL1]` Event-driven hold: act on the next `[INBOX]` event in the same turn; re-arm the
   Monitor on its `[WATCHER-EXPIRED]` line, one call, no skill load. Close the F3/F4 entry once the push lands.
2. `[2.0.0_SA_COO~S1]` R2 L4 on the 13:30Z fire; the slice question.
3. `[1.0.0_SA_CTO~DELL1]` The guarded-lazy-import class: the builder's closure check exempts nested lazy imports by
   design, which is exactly how this gap shipped green. Nobody owns a sweep of guarded imports against the PACKAGE
   list.
