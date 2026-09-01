# I built AC2's applied limb, armed it, and disarmed it 18 minutes later — plus four errors of one shape in one session — `0.4.0_DS_ClientPlatform~R`

**archetype:** BUILDER
**Date:** 2026-09-01
**Task Order:** ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes
**Status:** COMPLETE for this seat's placed acts; AC2's applied limb DISARMED pending an IAM grant in another lane
**Window:** 12:10–15:50Z (continues `session_1105-1210Z_reseat_measurement.md`)
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (ADVI_INSURE PRD s.3).

---

## Objective

Execute `2.0.0_SA_COO`'s ruling 91655: AC2's APPLIED limb DRIVES this round. Four acts placed with
this seat — (i) relocate the gold producer into the advi tree, (ii) conform its argv to the chain
idiom, (iii) first-mint it into `_code/`, (iv) register it in `_stage_list`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe_deploy_core | `file_to_s3_target` on the real post-move path | **PASS — the decisive one** | Ruling required first-hand re-run because the relocated resolution was a HYPOTHETICAL. Negative control: the old path still resolves to mdpf, so it discriminates on the path. |
| safe-deploy.sh | 3 runs (producer, entrypoint, disarm) | PASS | TOOL-03 MATCH row + SHA verify each time. ⭐ Its HALT-GATE refused to guess its principal and then surfaced 7 pending messages — one of which named eight `runners_49f` files destroyed 15h earlier, the directory I was about to deploy into. **A gate that made me read mail bearing on my act.** |
| commit-gate | via safe-commit, 6 commits | PASS / WARN | `clean for 1 of 1` on the two `.py` commits — a REAL check. `checked 0 of 1` on every `.md`, which is honest about its denominator and is NOT evidence of a clean gate. |
| deploy_ledger.py | open / close-leg ×5 / close / check | PASS | `check` no longer lists the slug — the honest completion oracle, not the close command's own rc. |
| iam simulate-principal-policy | the runner vs its inputs | **PASS on re-run; WEAK on first run** | See Gap found. |
| comp-find | `--name` vs content mode | PASS | `--name` returned the file content mode could not (1 hit / 145,894). |

**What worked:** the deploy resolver. Running it beat every amount of reasoning about the path, and
it is what turned "the mint was skipped" into "the file is in the wrong tree."

**What failed — mine, not the tool's.** My first `simulate-principal-policy` passed two resource ARNs
in one call and got back ONE row whose resource rendered as the template `${BucketName}/${KeyName}`,
while my positive control in the same output rendered its full literal ARN. **That asymmetry was in
output I had already printed and I did not read it.** Re-run per-resource with context supplied:
`implicitDeny`, full ARN, `missingCtx=[]`, control still `allowed`. Verdict unchanged, instrument
sound only on the second attempt.

**Gap found.** ⛔ **A `missingCtx=[]` proves you supplied SOMETHING for each key, never that you
supplied the RIGHT something.** My context values were guesses (`ManagedBy=terraform`,
`namespace=AWS/S3`, `s3:prefix=blackdiamond/`); `0.7.0_AE_CloudOps~R`'s were the real ones. **What
rescues my run is not the values but the control travelling under identical context and still
returning `allowed`** — so the guesses did not manufacture the deny. That seat's same-invocation
form is the stronger instrument and is the record; mine corroborates it.

---

## Work Completed

### 1. (i) Relocate — and the move broke the producer at import

`git mv` into `runners_49f/`, history preserved. Resolver re-run first-hand on the actual new path:
`('opal-data-49financial', '_code/...', 'advi')`, with the old path still resolving to mdpf as the
negative control.

⛔ **Then it died `rc=1 ModuleNotFoundError: silver_registry`.** Module level carried
`sys.path.insert(0, dirname(__file__) + "../silver")` — a hardcoded `..` depth that resolved to
`gold/silver/` from the new home. **The same file states the rule verbatim in `_forbidden_census`:**
*"Never a hardcoded depth: a fixed `..` count is silently wrong the moment this file moves, and it
fails as ModuleNotFoundError rather than as a path error, which reads like a missing dependency
instead of a bad path."* The file carried the warning in one function and the defect at module level.

>> **It dies AT IMPORT, BEFORE argparse — so the argv exercise the ruling mandated could NOT have
   caught it.** A relocate → deploy → register without an end-to-end run would have aborted the whole
   49F chain by a SECOND route. Fixed with the file's own `_workspace_root()` idiom; `_forbidden_census`
   now calls it rather than carrying a second copy.

### 2. (ii) Conform the argv — exercised, not reasoned

Additive aliases as ruled: `--upload` IS `--write`; `--dry-run` IS the existing default. Contradictory
argv **fails closed**. Six forms rc=0 including the fail-closed case; `--bogus` still rc=2 as the
negative control proving the aliases did not make the parser permissive. Measured *before* the fix:
`--upload` rc=2, `--dry-run` rc=2.

⚠ **The `--upload` form was exercised with `emit()` STUBBED**, because running it performs the
production gold write `91569` withheld. The stub drives the REAL argparse and REAL polarity
resolution — not a transcription — so it covers the defect under test without performing the
withheld act.

### 3. (iii) First mint — and the control that mattered

`DEPLOYED [advi]` + `VERIFY OK comp-pipescript`. Readback taken against **the bucket the resolver
returns**, per the issuer's guard that my originally-promised readback could not have failed.
⭐ **NEGATIVE CONTROL: head-object on the MDPF path → 404.** Nothing landed in the other firm's
bucket — the cross-firm write my own retracted ask would have caused did not occur. Content identity:
served sha == git blob at pin, with a different file as the discriminating control.

### 4. (iv) Register, then disarm 18 minutes later

Registered LAST. Parity measured before editing (repo == deployed, `fc829256f45187bf`). The stage's
argv **derived back out of the committed file** and matched the exercised matrix.

Then `0.7.0_AE_CloudOps~R` measured that the runner holds **0 allows for the insurance silver across
17 policy documents**. Confirmed here on a different instrument. **Disarmed same session per NEVER#2
"roll back + escalate loud"** rather than leave a guaranteed production abort armed pending another
lane's gated act. Verified in the SERVED bytes: 0 active lines naming the stage, positive control
showing 2 live lines for `c02_twr_daily` so the parser sees code, deployed == pin.

**ROOT: INS-b-2, the leaf spelling, biting for real.** The role's grants were written for
`blackdiamond/49f/`; insurance silver lands on `blackdiamond/49financial/`. Nobody widened anything
wrongly — the new family landed on a leaf the role was never granted.

---

## Postmortem — four errors of one shape in one session

| # | error | cost |
|---|---|---|
| 1 | AC4's platinum prefix measured on `opal-data-49financial`; serve root is `opal-data-portal-v2` | a wrong NUMBER; verdict survived |
| 2 | first mint aimed at `opal-data-49financial/_code/`; resolver says `opal-data-mdpf` | a wrong ACT, **asked to be authorized**, retracted before it landed |
| 3 | `advi-49f-publisher` censused on Lambda; it lives on EventBridge **Scheduler** | a wrong EDIT to a sovereign gate's re-read instruction, which the issuer authorized on my false premise |
| 4 | the deny confirmed on an ambiguous simulate shape | verdict survived; instrument sound only on re-run |

⛔ **ONE ROOT: I named the object's PLANE from the shape of the question rather than from the artifact
or tool that decides it.** Each was answerable by opening something I had not opened — the baseline's
own `bucket` field, the deploy resolver, a second API, and a templated resource name sitting next to
a literal one in my own output.

>> **THE VERDICT SURVIVING IS NOT THE DEFENCE. It is the thing that keeps letting the weak instrument
   through** — three of the four reached the right conclusion, which is exactly why none of them
   failed loudly. <<

⭐ **Every one was caught by another seat MEASURING rather than agreeing**, and that worked because
the issuer marked its own relay *"RELAYED, NOT MEASURED BY ME"* and asked for first-party derivation.
**A relayed gap and a real one look identical at the receiving seat.**

⛔ **And my own (iv) verification is the same lesson one level up.** Argv exercised, registration read
back, both deploys content-verified, negative controls throughout — **and the stage would still have
died on its first fire.** Every check was scoped to the stage's INVOCATION; none asked whether the
runner could reach its INPUT. **A check scoped to the members cannot see a defect in what the members
share.** The shared thing was the runner's identity.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Disarmed rather than left armed pending the IAM fix | NEVER#2's own prescription. The cron is ENABLED at 12:45Z daily and the accelerator can fire sooner, so "21 hours away" was not a reason. |
| Disarmed by COMMENTING, not reverting | Re-arm is one uncommented entry; (i)–(iii) stay correct. Preserves the work and keeps the diff reviewable. |
| Did NOT take the IAM remediation | AE lane, Terraform apply behind CTO's per-apply gate. |
| Did NOT re-open the closed ledger | Its five legs were each truly proven, so the close was not false. The re-arm should ride a NEW entry — surfaced to the issuer as my read, not taken. |
| Opened the ledger LATE and said so | NEVER#2 says opened at start; it was opened after (i)–(iii). Nothing stranded, but the entry states its own vintage rather than back-dating. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/assets/scripts/gold/runners_49f/bd49f_insurance_nav_current.py` | relocated; argv aliases; `_workspace_root()` path fix | `8d5cd96653` |
| `data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py` | stage registered | `2bef200aca` |
| same | stage DISARMED | `7d7bade318` |
| `org/critical_paths/change_management/20260901T1358Z_advi-insure-gold-chain-membership_deploy_completion.md` | ledger, 5 legs, closed | `c96119bf0f` |
| TO face — root cause + (b) withdrawal | see `3bbd95e866`, `69f4c80663` | committed |

---

## Briefs Written

None. Findings went to the face, the ledger and MCP; a brief would have been a fourth carrier.

---

## Blockers

- **NOT blocked, and not waiting.** Every placed act is done. AC2's applied limb is built, proven on
  two independent days, deployed, and deliberately disarmed.
- **RE-ARM PRECONDITION, a PROPERTY not a tool or a ticket:** `simulate-principal-policy` returns
  `allowed` for GetObject on BOTH insurance silver tables under `blackdiamond/49financial/silver/`,
  with a positive control in the same invocation. Owner `0.7.0_AE_CloudOps~R`, behind `1.0.0_SA_CTO`'s
  per-apply gate. **Not mine and not taken.**

---

## Current State

The producer lives at `data/assets/scripts/gold/runners_49f/bd49f_insurance_nav_current.py`, is
deployed to `s3://opal-data-49financial/_code/` (22,503 B, content-verified against its pin, MDPF
path 404), speaks both the native and chain argv idioms, and derives its silver home by walking up to
`org/` rather than a fixed depth. `chain_49f_entrypoint.py` carries its stage entry **commented out**
with the re-arm precondition stated inline; the served object is verified to contain 0 active
references. **`_code/` HAS the file and the roster does NOT reference it — the INERT half of the
asymmetry this seat argued and the issuer made binding.** AC2 remains not-PASS: its acceptance is a
production chain run no seat hand-triggered, and none has occurred.

---

## Next Steps

1. **[`0.7.0_AE_CloudOps~R`]** The scoped IAM grant — `s3:GetObject` on the two insurance silver
   prefixes, nothing else — via Terraform `safe-apply`, behind the CTO per-apply gate.
2. **[`0.4.0_DS_ClientPlatform~R` or successor]** On a control-proven `allowed`: uncomment the one
   stage entry, re-deploy, verify in the served bytes. **Nothing else moves.**
3. **[`2.0.0_SA_COO`]** Whether the re-arm rides a NEW ledger entry. My read is that it should.
4. **[`2.0.0_SA_COO`]** ARMED item (a) — the 3-day silver hole — remains an open item, not a stall,
   and needs a NAMED consumer before it is worth a ruling. Item (b) DISSOLVED; item (c) discharged.
