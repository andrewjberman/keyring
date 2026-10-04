# Two legs landed, and the third criterion found a second missing grant the halves could not see — 0.7.0_AE_CloudOps~A

**Date:** 2026-10-04
**Task Order:** AMGT_RESAPP.TO-AMGT-aq-5 (sections 1-5, AMENDMENT 1 @551f06751f, AMENDMENT 2 / cell AMGT-aq-6 @4d3db86faa)
**Status:** IN PROGRESS — legs 1 and 2 COMPLETE and reported; leg 3 BLOCKED on `amgt-corpus-r36-al5` closing

---

## Objective

Redeploy `opal-amgt-scoped-api` at build commit `d8bafe6896`, carrying the four round-67 drains
(aq-1 FWD-39 word cloud, aq-2 FWD-36 tone, aq-3 FWD-38(d) /ledger provenance, aq-4 Z-S86 covered-no-block),
under ONE NEVER-2 entry and one never-widen pair. AMENDMENT 1 made it TWO legs: a one-object `s3:GetObject`
grant first (row Z-S345), because aq-4 reads the Security Scanner S&P 500 universe at request time and the
role could not, so code without the grant turns every unknown `_US_Equity` key from 404 into 502.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read infra/aws/terraform/harvest/scoped-amgt-api.tf --for "..."` | PASS | Located `scoped_amgt_api_grants` (:230) and `artifact_key` (:318) and flagged 45 qualifiers in the file. Pointed me at the right lines without a full read. |
| comp-find | `comp-find "build-and-upload-scoped-amgt" --files` | PARTIAL | 503 hits / 111,165 files scanned. Its HEAD band listed siblings but not the builder itself, so the printed denominator is what told me to stop paging and `ls` the builder's own directory. Useful because the denominator was honest, not because the top hit was right. |
| comp-find | `comp-find "issued_to>0\.7\.0_AE_CloudOps~A<" --files --limit 20` | PASS | 92 hits / 52 files; established that this lane's TO history is 37 orders. |
| comp-iam | `comp-iam service opal-amgt-scoped-api` | FAIL (as documented) | Reported 5 of 5 operations `UNRESOLVED-RESOURCE`, 10 unparsed deny statements, 54 unattached policy blocks. It can say **nothing** about either grant: it models `(action)` and never `(action, resource)`. Recorded in the instance as DECLARED-NOT-AN-ORACLE. |
| comp-schedule | — | SKIPPED | Issuer declared NOT-APPLICABLE at the cut: no cron, alarm, monitor or cadence in this act. |

**What worked:** `comp-read`'s qualifier count and `comp-find`'s printed denominator. Both saved time precisely
by being honest about what they had NOT covered.

**What failed:** `comp-iam`, exactly as `cloud-ops` warns — it FAILS GREEN here. The rail routes raw `aws` IAM
inspection to it, but a role holding `s3:GetObject` on any bucket reports `[GRANTED]` for every other. Had I
read it as a pass, I would have missed BOTH grants this round turned on. Every IAM verdict below came from
`simulate-principal-policy` on the live primitive under a `# rail-checked:` marker.

**Gap found:** `r67_served.py` c24 cannot see a denied table read (see Verification). Also: the comp-tool rail
gates `comp-find | grep`, which is correct, but the gate fires on a *summary-aware* pipe too — I hit it twice
and used native `--limit`/`--files` instead, which is the right answer.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Re-read the base LIVE before the build (a moved base is a STOP) | CodeSha256 `FcVBPafwzuPI0RMFjOJJfYN/KeZe3YYns9uqTSOlalU=`, MemorySize 1769, Timeout 29, LastModified `2026-10-03T23:49:22Z` — equal to both halves |
| 1 | Open ONE NEVER-2 entry for BOTH legs (CTO condition 4), sentinel committed BEFORE the grant leg | `cd15421422`, slug `amgt-resapp-r67-aq5-grant-and-code-20261004`, 4 legs |
| 2 | **Leg 1** — add ONE statement `ReadTheScannerSp500UniverseForCoveredNoBlock` to `scoped_amgt_api_grants` | 1 file, +31/-4 |
| 3 | `terraform plan -target=aws_iam_role_policy.scoped_amgt_api_grants` + `show -json`, graded | 4 resource_changes; shapes `{no-op: 3, update: 1}`; statements 5 → 6; exactly 1 ADDED, byte-equal to both halves; 0 REMOVED |
| 4 | `safe-apply.sh` (Rule 18; terraform resolved on PATH, `.tools/terraform.exe` absent on site Z) | rc=0 |
| 5 | Targeted 0-diff replan | `-detailed-exitcode=0` |
| 6 | Commit leg 1 | `f61711ef2b` |
| 7 | **Leg 2** — detached sparse worktree at the pin | `/c/tmp/aq5-pin` @ `d8bafe689663252714d6e70d2d26586e5a784c25` |
| 8 | `build-and-upload-scoped-amgt.sh --build-only` | `CONTENT-DIFF SUMMARY: files 356, IDENTICAL 350, CHANGED 5, ADDED 1, REMOVED 0` vs `FcVBPafw`; SIZE 253,753,630 B of 262,144,000 B (96.8%, 8,390,370 B spare) |
| 9 | Real `build-and-upload-scoped-amgt.sh` | Reproduced step 8 to the byte. UPLOAD VersionId `auoGQqF5cmI7xLgeCy6Z5Qq4w2TQ7icX`, content-sha256 `aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=`, 41,158,901 B |
| 10 | Independent `head-object` (the uploader's read-back is a self-report) | Same VersionId, same length, same sha, SSE AES256, LastModified `2026-10-04T21:35:13Z` |
| 11 | FULL `terraform plan` (deliberately not targeted) + `show -json`, graded | 49 resource_changes; `{no-op: 48, update: 1}`; the one update is `module.scoped_amgt_api.aws_lambda_function.this`; **0** destroy/create/replace, **0** non-no-op IAM, **0** non-no-op route/gateway |
| 12 | `safe-apply.sh` code-only | `Modifications complete after 8s`; `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` |
| 13 | Read the deployed function LIVE (never rc) | CodeSha256 `aoQ+Wref…` (= the uploaded content-sha256), MemorySize **1769**, CodeSize 41,158,901 (= uploaded length), State Active, LastUpdateStatus Successful |
| 14 | FULL 0-diff replan | `No changes. Your infrastructure matches the configuration`, `-detailed-exitcode=0` |
| 15 | Grade AC1 / AC2 / AC3, 10 regression reads, 2 cold reads | AC1 PASS, AC3 PASS, **AC2 FAIL**; 10/10 regressions YES; both cold reads within band |
| 16 | File row `AMGT_RESAPP-Z-S346` (ARMED, disarm_owner `2.0.0_SA_COO~Z`) | `ebf6eda0cb` |
| 17 | Close the NEVER-2 entry, 4 of 4 legs proven | closed `20261004T222741Z`; sentinel removed; slug absent from `check --red` |
| 18 | Commit the instance | `f2f5476f6c` |
| — | Tag + push | **NOT DONE, and not mine.** Rule 6 tagging and the CLOUD push belong to `0.0.0_AB_MSTR` on Andrew's word |

---

## Verification

**The grant leg, on the applied plane.** One `--resource-arns` per call, every control its own invocation
(cloud-ops false-deny mode 1 disarms a co-passed control):

```
TARGET  .../universes/sp500/universe_data.json   implicitDeny  ->  allowed
        MatchedStatements [role_opal-amgt-scoped-api-role_opal-amgt-scoped-api-grants]
CONTROL opal-data-harvest/universe/v1/sp500.json           allowed   (isolated)
WIDEN   .../universes/sp400/universe_data.json             implicitDeny  (after the apply)
```

The sp400 arm is the one that matters: an `allowed` on the target proves the grant exists, but only a DENY on
a sibling proves it is ONE OBJECT and not a prefix. The `allowed` control also disposes of false-deny mode 3,
since a nonexistent action name cannot return `allowed`.

**The graded criteria, against their own base arms.** Every cell was read on the deployed base BEFORE the code
leg, so each PASS has a matching FAIL from the same instrument:

| cell | base (`FcVBPafw`) | after (`aoQ+Wref`) |
|---|---|---|
| r67 c23 (AC1) | NO — 15 own-ticker offenders, 69 extended-list payloads, inverted window wrong | **YES** — 190 payloads, 128 non-empty, **0** offenders |
| r67 c24 (AC2) | NO — mismatches 74, old-reason 95, no-table-row 21 | **NO** — mismatches **74**, old-reason **0**, no-table-row 21 |
| r67 c25 (AC3) | NO — 4 of 6 classes unsourced on BA/AMD/VLO, every news stamp None | **YES** — 9 of 9 clauses, unsourced `[]`, stamps equal to overlay last_run |
| r67 c26 (AC3) | NO — DE 404 on thesis and peers | **YES** — DE 200 both, ZZZZ control still 404 |

c26's served peers sentence — *"Deere & Company (DE) is a covered name (Security Scanner S&P 500 universe, as of
2026-10-02)…"* — is the grant leg proving itself end to end through the payload, since the role could not read
that file an hour earlier.

**Regressions:** 10 of 10 `SERVED YES`, exit=0, none moved adversely — r64 c9/c10/c11/c12/c13/c14, r65 c17,
r66 c18/c19/c22. **r64 c10 now passes outright**, so ap-4's 90/365 carve-out (row Z-S344 instrument rot) is
gone. Reported because the half makes *any* regression movement a rollback, and this one moved the right way.

**Cold reads**, both after a 900 s invoke-free idle (`22:00:18Z → 22:15:18Z`), every invoking check run before it:

```
c15 DAY route (GRADED):  3 of 3 COLD by Init Duration — 1971.51 / 1941.63 / 1936.54 ms
                         bound 5000 ms, margin 3028 ms; headlines 6/6; AMGT_SEGMENT 3/3
RANGE route (REPORTED):  12 concurrent — COLD 9 of 12, status 200 on 12/12,
                         word_cloud 40 terms on 12/12, cold band 1680.54–2586.64 ms,
                         over 5000 ms: 0 of 9
```

No 502 on any key anywhere in this act — AMENDMENT 1's separate rollback trigger.

### Why AC2 failed, and why the check could not say so

AC2 expects `mismatches 0`. The deployed read is `mismatches 74`. Diagnosed on three independent planes rather
than inferred, because the arithmetic invites the wrong conclusion:

1. **The served payload.** `/lead-panel/timeseries/collected/chatter?days=30` answers 200 with 95 rows, and the
   `tone_reason` distribution over the **full 95-row denominator** is a single bucket:
   `95 × "the window table could not be read (AccessDenied)"`.
2. **IAM.** `monthly_chatter.WINDOW_TABLE = "chatter_window"`;
   `store.table_prefix("amgt","gold","chatter_window")` → `amgt/harvest/gold/chatter_window/`. That prefix is
   **absent** from `local.scoped_amgt_pool_prefixes`. `s3:GetObject` on a part key → `implicitDeny`;
   `s3:ListBucket` with `--context-entries s3:prefix=…/chatter_window/` → `implicitDeny`. Each against an
   isolated control on the GRANTED sibling `chatter_daily/` → `allowed`, which also proves the context entries
   were accepted (mode 2 disposed of). The role lacks **both** actions.
3. **The source.** `_window_index()` catches every exception and returns ONE reason for EVERY row, which is why
   this degrades to a plain reason and never a 502.

**The trap.** `74 + 21 = 95` looks like "the function read the table and 21 names have no row". It is not.
`r67_served.py:130-143` increments `no-table-row` from the **check's own** index then `continue`s, so those 21
rows are never compared; and `old-reason` matches only the legacy phrase `"not served on this route yet"`, so an
`AccessDenied` reason is invisible to both counters. A function that cannot read the table AT ALL therefore
scores `old-reason 0, no-table-row 21` — three quarters of the expected PASS shape.

**Not a regression:** the base arm read the SAME `mismatches 74`. The act's only served change on c24 is 95
misleading legacy tone reasons replaced by 95 honest ones.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT take the mandated rollback | The trigger fired on its literal terms (COO failure branch + CTO condition 3), but the rollback restores `FcVBPafw`, which re-breaks c23, c25 and c26 — all three now PASS — restores 95 misleading reasons, and STILL reads mismatches 74. It cannot cure what triggered it. Its blast radius is three proven fixes, so the call belonged to the issuer, not to me. **Ruled STAND** (CTO AMENDMENT 1 @`14aa3c9200`, Andrew "recs approved" @`c700426bc9`). |
| Did NOT add the chatter_window grant myself | Both halves make any IAM change beyond the one scanner statement a STOP. Proposing is legal, implementing is not. Proposed the exact one-line cure instead; it was adopted verbatim as cell AMGT-aq-6. |
| Took the FULL plan for the code leg, not a targeted one | The 48 no-ops are themselves evidence that nothing else in the root moved. A targeted plan cannot show that. |
| Graded every STOP as a printed COUNT | "0 non-no-op IAM resources" discharges the STOP positively; "I didn't see an IAM change" does not. |
| Enumerated the builder's data members instead of widen-and-retry | Two `--build-only` runs died on my own sparse cone. Rather than guess a third time I extracted every `org/` path the builder names (3) and set the cone once. |
| `close`d the NEVER-2 entry rather than `hold` | `deploy_ledger` refused HELD — correctly: HELD is for proven apply legs with verify still open, and nothing was stranded. The open item was a *decision*, which rides ARMED row Z-S346, not the deploy ledger. |
| Kept the project's instance convention over the canonical schema | `PROOF_OF_SPEC.schema.json` describes a different genre; conforming would delete the sections section 5 mandates (regression_reads, cold_reads, status). Fixed what was free — byte-identical invocations, conformed `decomp_ref`/`artifacts_produced` — and cleared both substantive limbs (`alignment`, `artifact-coverage`) that ap-4 failed. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/terraform/harvest/scoped-amgt-api.tf` | +1 IAM statement, one object ARN, with its never-widen comment block | Yes — `f61711ef2b` |
| `org/critical_paths/change_management/20261004T2115Z_amgt-resapp-r67-aq5-…md` | Opened 4-leg NEVER-2 entry; L1-L4 closed with proof; CLOSED | Yes — `cd15421422`, `ebf6eda0cb`, `f2f5476f6c` |
| `org/critical_paths/.open_deploys/amgt-resapp-r67-aq5-…json` | Sentinel; removed at close | Yes — same |
| `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` | Row `AMGT_RESAPP-Z-S346` (739 rows total; gate graded the 1 new row) | Yes — `ebf6eda0cb` |
| `org/missions/.../0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-aq-5.…proof_of_spec.json` | The instance: 23 keys, 3 acceptance rows, 13 controls, cold_reads filled, 0 non-ASCII bytes | Yes — `f2f5476f6c` |
| `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` | New version `auoGQqF5…`; prior `Pj6GLEdK…` retained as rollback | n/a — S3 |

**Push state, measured:** all LOCAL. `origin/CLOUD` @ `b7f2fb4dc7` (`git ls-remote`). This seat commits and
never pushes a shared branch.

---

## Blockers

- **BLOCKED on `2.0.0_SA_COO~Z` / CORPUS al-5:** leg 3 (cell AMGT-aq-6) is fully authorized — both halves
  signed, GO msg 29291 acked — but begins only when
  `org/critical_paths/.open_deploys/amgt-corpus-r36-al5.json` closes. **Verified, not assumed:** that entry
  reads `**Status:** OPEN` and its sentinel is present on CLOUD. I unioned the sentinel across all 26 live
  worktrees (present at HEAD in 1, absent in 25) and the 25 absences are worthless — those branches predate
  the sentinel commit. Monitor `bxd15h1e7` is armed on the close.
- The serialization is substantive, not procedural: al-5 deploys this same function at `288de3d95d` and its
  regression set includes r67 c24, so a grant landing mid-al-5 would move c24 under al-5's own verify and
  confound it (CTO AMENDMENT 1 @`5a8f3ce6ff`).

---

## Current State

`opal-amgt-scoped-api` is live at CodeSha256 `aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=`, MemorySize 1769,
artifact VersionId `auoGQqF5cmI7xLgeCy6Z5Qq4w2TQ7icX`, with a 0-diff full plan in
`infra/aws/terraform/harvest/`. Its role `opal-amgt-scoped-api-role` now reads the Security Scanner S&P 500
universe object (one ARN, sibling keys still denied) but still cannot read
`amgt/harvest/gold/chatter_window/` — so FWD-36's window tone serves
`"the window table could not be read (AccessDenied)"` on 95 of 95 rows, which is AC2's open failure and ARMED
row `AMGT_RESAPP-Z-S346`. The aq-5 NEVER-2 entry is CLOSED (4 of 4 legs proven, sentinel removed), which is
what unblocked CORPUS al-5. Rollback remains available and untaken: a code-only `safe-apply` at VersionId
`Pj6GLEdKjRnDFwBjZzOSR2gYAsQPHilG` restores `FcVBPafw`. Of 37 task orders ever issued to this lane, aq-5 is
the only non-terminal one.

---

## Next Steps

1. **[0.7.0_AE_CloudOps~A] Execute leg 3 the moment `amgt-corpus-r36-al5` closes** — add
   `"amgt/harvest/gold/chatter_window/",` to `local.scoped_amgt_pool_prefixes` (that one list drives both the
   GetObject resources and the ListBucket `s3:prefix` condition, so one entry covers both), ONE `safe-apply`
   targeted at `aws_iam_role_policy.scoped_amgt_api_grants`, under its OWN new NEVER-2 entry. Plan must be
   1-to-change / 0-add / 0-destroy; NO code change and a moved CodeSha256 is a STOP. Re-read the base LIVE
   first — it is whatever sha al-5 records at close, not `aoQ+Wref`. Grade **AC4** (`r67_grant_aq6.sh`;
   the COO half calls the same criterion AC1 — the order's id governs) and it must read `allowed` BEFORE AC2,
   then re-read AC1 and AC3, which a policy-only act should not move.
2. **[0.7.0_AE_CloudOps~A] Expect c24 at full strictness** — c24 gained a C2 clause at the leg-3 cut counting
   the unreadable-table reason over every row (base FAIL 95 of 95, local control PASS 0). `C2` still FAIL after
   AC4 reads YES is a **STOP reported with the simulate output**, not a rollback.
3. **[1.0.0_SA_CTO~Z / standards] Reconcile `PROOF_OF_SPEC.schema.json` with the AE instance genre** — it
   demands `controls={determinism,mutant}` and forbids `scope`/`status`/`regression_reads`/`cold_reads` at the
   root, so every AE code-redeploy instance on this project reads INVALID (mine 21 violations, ap-4 15). A
   validator that always says INVALID trains readers to ignore it.
4. **[0.0.0_AB_MSTR] Push CLOUD on Andrew's word** — 4 commits local; `origin/CLOUD` @ `b7f2fb4dc7`.
