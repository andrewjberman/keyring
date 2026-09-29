# The ww-1 redeploy landed on the canonical prefix; AC2 fails on an arm the act cannot reach — 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

**Date:** 2026-09-29
**Task Order:** AMGT_RESAPP.TO-AMGT-ww-1 (round 48) — the redeploy on the canonical prefix
**Status:** BLOCKED

---

## Objective

Execute the post-crash re-issued GO (msg 26649) for `AMGT_RESAPP.TO-AMGT-ww-1`: redeploy
`opal-amgt-scoped-api` on the canonical `amgt/harvest/gold/research_dossier/` prefix plus one
`dynamodb:GetItem` on `etf-classifications`, under the never-widen pair COO `@069b8ab4a5` /
CTO `@b2691b853d`, and verify the three criteria and six stop limbs.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find "universe_securities" --limit 40 -- lib/` | PASS | Denominator 5 hits / 361 files. Re-verified limb 1's one open question independently of the CTO half: 0 non-test import sites, so the file ships inert. |
| comp-find | `comp-find "etf-classifications" --limit 25 -- infra/aws/terraform/` | PASS | Showed the table is declared in the `yang-pipeline` root, which is why the literal ARN is correct here and not a shortcut; three sibling roots do the same. |
| comp-read | `comp-read .../vv-4.AC3.py --for "the PASS/FAIL verdict logic and exit code"` | PASS | Surfaced `ok = n_fail == 0 and ...; return 0 if ok else 1`. **This is the read that caught the false PASS.** |
| comp-read | `comp-read lib/opal_naming.py --for "signature ... of address() and key()"` | PASS | Gave `address(source, scope, tier, table, partition, object=None)` after two wrong-arity guesses. |
| comp-schedule | declared NOT-APPLICABLE by the order's preflight | SKIPPED | No cron, alarm, monitor or cadence moves in this act. |
| comp-iam | run by the ISSUER at the cut | SKIPPED | Not this seat's leg. The grant was instead **exercised**: AC3's `name SERVED 2 of 2` cannot pass without the GetItem succeeding — a live exercise beats `comp-iam`, which models `(action)` and never `(action, resource)`. |
| deploy_ledger.py | `open` / `close-leg` x3 | PASS | 4 legs; B0/T1/A1 closed with proof; V1 left OPEN deliberately. `list` reads `stranded=['V1']`, in-window. |
| safe-apply.sh | `-chdir=infra/aws/terraform/harvest apply ww1.tfplan` | PASS | One apply against the exact graded plan. |

**What worked:** `comp-read --for` on the AC2 script was decisive — it surfaced the verdict expression
that exposed a false PASS I had already written down. `comp-find`'s printed denominator let me discharge
limb 1's one admitted exception myself instead of inheriting the CTO's word for it.

**What failed:** Nothing in the tools. The failure was mine — see Postmortem.

**Gap found:** none.

---

## Work Completed

### 1. Begin-conditions re-verified at HEAD, not inherited
ww-2 and ww-4 both `complete`; both halves committed. CTO condition 2 re-checked:
`git diff 48c1ea24c4 HEAD -- lib/research/` EMPTY, and `git diff b2691b853d HEAD -- lib/
infra/aws/terraform/harvest/` EMPTY, so both halves bind unchanged at build commit `2a9ad75324`.
World independently re-measured at the pre-entry base (CodeSha256 `CtIvirvM...EAOM=`), agreeing with the
issuer's read rather than relying on it.

### 2. Fresh NEVER-2 entry opened and committed BEFORE the build
`amgt-resapp-ww1-redeploy-research-dossier-restart-20260929`, 4 legs, committed `f298c2313c`, and the
commit verified to read back **from the git object store**, not the worktree. Supersedes the entry the
11:34 ET crash abandoned.

### 3. B0 — captures and closure diff, all six limbs clean
9 pre-apply route reads captured from the deployed function. Closure diff vs the deployed build input:
8 non-test files, 7 in limb 1's list; `universe_securities.py` re-verified inert. Limb 2: `build_pack`
unchanged. Limb 3: 9 hunks, exactly one non-pure-addition, inside `read_rankings`.

**The deployed build-input pin was falsified, not inherited.** Both halves assert `0d54b880cf`. I pulled
the deployed artifact and compared packaged bytes: 4 of 4 files byte-equal to that commit and all 4
differing from HEAD, so the negative control holds and the comparison is not vacuous.

### 4. T1 — terraform committed before the apply
`26113dbc97`, 38 insertions, pure addition. Naming gate `PASS 1 graded`, `CONFORMANT as S3Key`. The
prefix is builder output printed at that commit (`key()` -> `amgt/harvest/gold/research_dossier/`),
underscore; the hyphen form that the gate refused at vv-4 is not granted. Pool prefixes 29 -> 30. One
`dynamodb:GetItem` statement, no other action.

### 5. A1 — one artifact, one apply
Artifact VersionId `61Fb7L90ggUdpjcXaX4T8CcMgquyzn0U` (prior `4S1U4Cs1LVyTkN0w5FkpM1WLXHmBFLmI` recorded
as the rollback target); local sha256 equals the S3 metadata. Plan graded on the **whole** 92-line plan
rendered from the saved file — my first read of it was a `tail -80` and I discarded it, since a
range-limited read cannot support "the plan shows nothing else". `0 to add, 2 to change, 0 to destroy`.
Apply: `0 added, 2 changed, 0 destroyed`. Post-apply CodeSha256 equals the uploaded artifact's sha;
re-plan 0-diff.

### 6. V1 — AC1 PASS, AC3 PASS, AC2 FAIL; limbs 5 and 6 hold
Limbs 5/6: 9 of 9 bodies byte-equal across the apply, compared byte-for-byte with full sha256, with the
control that CodeSha256 moved between captures. Per the CTO/COO ruling on HARVST g-2 (msgs 26678/26680),
**both my grading captures precede g-2** — verified on live S3 LastModified (19:26:35Z / 19:26:55Z /
19:27:23Z vs my 18:57:01Z and 19:21:10Z), not on the producer's report. A third capture at 19:37:28Z
confirms the ruling's prediction exactly: only AMD/BA/GOOGL `/timeline` moved; 1299_HK `/timeline`, AMD
`/timeline/day` and all four print PDFs held. **Rollback triggers: NONE.**

AC2 fails on one conjunct of five: `n_fail == 0`. One of 96 library names, `Hitachi 6501 JP`, resolves to
a harvester key but to no `security_key`, so the harness never invokes the Lambda for it
(`vv-4.AC3.py:39-40` guards on `if key`). Filed as row `AMGT_RESAPP-Z-S303`.

---

## Postmortem

**Root cause of a near-miss I caught myself:** I read three acceptance criteria's exit codes as
`python check.py 2>&1 | tail -30; echo "exit=$?"`. `$?` after a pipeline is the **last stage's** status,
so it reported tail's 0. AC2 printed `failed 1` beside a reported `exit=0`, and I had already recorded it
as passing.

| signal | said | true |
|---|---|---|
| reported rc | 0 (PASS) | tail's rc, not the script's |
| script's own printed verdict | `reads OK 95 of 96 (failed 1)` | correct |
| true rc, re-run without a pipe | 1 (FAIL) | correct |

**What caught it:** reading the script's verdict expression and noticing the printed number contradicted
the rc. The text was right; the rc was structurally incapable of being right. **This trap fails toward
PASS**, which is the dangerous direction — same shape as `comp-validate --lenient` returning rc=0 over
`ZERO_CHECKS`. AC1 was run without a pipe and stands; AC2 and AC3 were re-run without one.

**Resolution:** all criteria re-measured with `> out.txt 2>&1; echo "TRUE exit=$?"`. The order's own
`<invocation>` strings do not pipe — the defect was my construction, not the task order's.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT roll back on AC2's failure | The trigger is named in both halves and is the ISSUER's to call. The failing arm is causally isolated from the act — the Lambda is never invoked for that name — so a rollback cannot move the count by one, and it would strip grants now serving `team_cases` for 95 of 96 names. Reported loud instead; no wider or narrower adjudication. |
| Left leg V1 OPEN | So the entry BLARES `--red` to the COO rather than reading closed on a criterion this seat did not grade. Deliberate, recorded as such in the entry. |
| Kept the one pre-existing non-ASCII character in `scoped-amgt-api.tf` | Removing it would widen the diff beyond what the halves name, which is itself a limb-4 risk. Attributed first: worktree count == HEAD count == 1. |
| Verified the deployed build-input pin by content | An inherited pin resolved by commit message is not resolved. Cheap, and limb 1's whole grading rests on it. |
| Did not adopt the four base-addressed pending TOs | None is `issued_to` this lane (two base, one `~O`, one unstated). Surfaced, not adjudicated. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/harvest/scoped-amgt-api.tf` | +1 pool prefix (builder output), +1 `dynamodb:GetItem` statement | Yes — `26113dbc97` |
| `org/critical_paths/change_management/20260929T1852Z_..._deploy_completion.md` | Entry opened; B0/T1/A1 closed; V1 partial + limb attribution | Yes — `f298c2313c`, `754252a73c`, `79d4c7abeb` |
| `org/critical_paths/.open_deploys/amgt-resapp-...-restart-20260929.json` | Sentinel, still OPEN at V1 | Yes — same |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | Row `AMGT_RESAPP-Z-S303` appended in place | Yes — `79d4c7abeb` |
| `.../deliverables/0.7.0_AE_CloudOps~A/...proof_of_spec.json` | Instance: AC1 PASS, AC2 FAIL, AC3 PASS; 3 controls | Yes — `79d4c7abeb` |
| `.../deliverables/0.7.0_AE_CloudOps~A/ww1-captures/` | Capture script + pre-apply, post-apply, post-g2 trees | Yes — `754252a73c`, `79d4c7abeb` |

Push state: **LOCAL @`79d4c7abeb`** (origin/CLOUD `39188d6754`, `git ls-remote` read). Shared-branch law:
this lane commits, `0.0.0_AB_MSTR~Z` pushes.

---

## Blockers

- BLOCKED on `2.0.0_SA_COO~Z`: `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ww-1.the-redeploy-on-the-canonical-prefix.md`
  — waiting for a ruling on AC2, whose `failed 0` clause turns on a population the act does not control.
  Asked at 19:43:56Z (delivered, 1045 bytes). The `<status>` flip is the issuer's regardless.

---

## Current State

`opal-amgt-scoped-api` is running CodeSha256 `lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=` (artifact
VersionId `61Fb7L90ggUdpjcXaX4T8CcMgquyzn0U`; rollback target `4S1U4Cs1LVyTkN0w5FkpM1WLXHmBFLmI`), with
`amgt/harvest/gold/research_dossier/` in `local.scoped_amgt_pool_prefixes` and one `dynamodb:GetItem` on
`arn:aws:dynamodb:us-east-1:313476888478:table/etf-classifications`; `terraform plan` in
`infra/aws/terraform/harvest` reads 0-diff. AC1 and AC3 PASS; limbs 5 and 6 hold with no rollback
trigger; AC2 exits 1 solely because 1 of 96 research-library names has no `security_key`. NEVER-2 entry
`amgt-resapp-ww1-redeploy-research-dossier-restart-20260929` is OPEN at leg V1 on purpose, in-window at
0.9h of 6.0h, so it will go RED if nobody rules.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`] Rule AC2** — either accept it against the identified population (95 of 96, the
   other four conjuncts at full strength) or re-cut the criterion. Until then V1 cannot close and the
   entry is heading for its 6.0h RED.
2. **[AMGT_CORPUS / identity owner] Register `Hitachi 6501 JP`** — a research-library folder exists
   (created 12:54:45Z) with no identity registration. Row `AMGT_RESAPP-Z-S303`. Not this lane's surface.
3. **[`0.0.0_AB_MSTR~Z`] Push** — everything from this seat is LOCAL at `79d4c7abeb`.
4. **[this seat] Close V1 and the entry** the same session the ruling lands.
