# Round 70 AMGT-at-6: one prefix, then seven new modules — and two things the halves could not have known — 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

## Objective

Execute `AMGT_RESAPP.TO-AMGT-at-6` on the GO at `d727901457` (msg 29528), AMENDMENT 1's **two legs**:
(1) add exactly one prefix `issuer-site/harvest/silver/filing_source/` to the scoped adapter's grant and
prove AC4 reads YES with `issuer-site/harvest/bronze/` still denied; (2) redeploy `opal-amgt-scoped-api`
at `e041c86791` carrying at-1..at-4 (header figures, exec roster, peer price currency, day-route origin).
Five CTO conditions. `/peers` timed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read infra/aws/terraform/harvest/scoped-amgt-api.tf --for "where is local.scoped_amgt_pool_prefixes defined…"` | ADVISORY | 527 lines / 1 whole-file section; found the grants policy at `:255`, the GetObject interpolation at `:286`, the ListBucket `s3:prefix` at `:294`, + 51 qualifiers. It located the **structure** but not the list body, so the locals block was read at the bytes before editing. |
| comp-iam | declared by the issuer at the cut | **NOT RELIED ON** | It models `(action)`, never `(action, resource)`, so on a one-prefix grant it fails **green**. CTO condition 1 is a per-resource claim. |
| comp-find | order + halves resolved from the GO and from `git show --name-only` | PASS | Deliberate: last round `comp-find --files` returned no HEAD band for the CTO half, because a file does not contain its own name. |
| comp-schedule | declared by the issuer | DECLARED-NOT-APPLICABLE | No cron/alarm/monitor/cadence. |
| comp-adversary | run by the issuer | PASS | Base arm for AC1/AC2: c30-c33 failing at 43 / 84 / 676 / 8. |
| commit-gate.sh | on the `.tf` and on the probe | PASS (probe after a fix) | The probe was **BLOCKED** first time on ruff `E741`, fixed, re-run clean. Recorded because a gate that is run beats one assumed. |
| naming-gate | at commit, on the `.tf` | PASS | `issuer-site/harvest/silver/filing_source/` graded **CONFORMANT as S3Key**. |
| deploy_ledger.py | open / close-leg ×5 / close | PASS | One entry, both legs, 5 legs, opened before the first apply. |
| proof-of-spec-check | on the instance | **INVALID then VALID** | First run: 6 violations. Fixed, then `VALID (rc=0)`, 10 of 10 controls discriminate, 4/4 invocation alignment. |

**Gap:** `comp-iam` is structurally unable to grade a one-prefix grant, and the rail routes raw `aws iam`
inspection to it. The audited `# rail-checked:` marker is the right escape and I used it with the reason
stated per call.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Base read LIVE | `OcKZF34X…` / 1769 / `2026-10-05T04:44:13Z` / role `opal-amgt-scoped-api-role` — equals both halves |
| 2 | `.open_deploys` union | 41 worktrees, **964 row-reads**, 0 amgt rows at HEAD. Artifact-side confirmation: the function still sat at *my own* round-69 sha, so no peer had deployed it |
| 3 | AC4 **before** | controls allowed, C1+C2 `implicitDeny`, `GRANT: NO`, exit=1 — the negative arm |
| 4 | Bronze control **before** | `implicitDeny` on both limbs |
| 5 | NEVER-2 entry, both legs | opened + committed `a5fdcb…`→ `e8578cca6d` **before the first apply** |
| 6 | `.tf` edit | ONE list entry; the file interpolates it into **both** limbs, so one line grants Get + List |
| 7 | Rule 30 check | `key('issuer-site','harvest','silver','filing_source',…)` → that exact prefix. **Builder output, not typed** |
| 8 | Targeted plan | 4 changes, 3 no-op, **1 update**; statements 6→6; strings **68→70**; **+2 exactly**, −0 |
| 9 | Grant `safe-apply` | 0 added, 1 changed, 0 destroyed |
| 10 | AC4 **after** + controls | `GRANT: YES` exit=0; bronze still denied; **two extra width probes** (`issuer-site/`, `issuer-site/harvest/silver/`) also denied |
| 11 | Detached checkout at `e041c86791` | clean porcelain |
| 12 | `--build-only` | `363 / 354 / CHANGED 2 / ADDED 7 / REMOVED 0` = AMENDMENT 1 exactly; 253,913,029 B (96.9%); FATAL `[]`; ISOLATED 3/3 |
| 13 | Ruling 4 arms | all 5 listed paths `allowed` both limbs; isolated ungranted control `identity/` `implicitDeny` |
| 14 | **Subtraction** | 32 granted prefixes vs 24 literals → 11 uncovered, 9 non-S3, **2 store-shaped** → rows Z-S352 |
| 15 | Build + upload | VersionId `.Sj7rblal1sHPyETvJW_ZKXvOzeGVds3`, 41,211,382 B; independent head-object confirms |
| 16 | Code plan (FULL) | 49 changes, 48 no-op, 1 update; **grants policy reads NO-OP** — the proof this leg carries no IAM change |
| 17 | Code `safe-apply` | 0 added, 1 changed, 0 destroyed |
| 18 | Deployed re-read | `GS//XHnVd4+…` / 1769 / CodeSize 41,211,382 = uploaded ContentLength |
| 19 | **c15 FIRST**, 43 s after apply | cold **3 of 3**, 1918.32 / 1899.17 / 1984.69 ms, YES, **first attempt** |
| 20 | AC1/AC2/AC3 + reported set + /peers | all PASS; 11 of 11 YES; /peers worst 136.83 ms |
| 21 | Full replan (both legs) | `No changes.` |
| 22 | Instance + close | VALID rc=0; entry CLOSED 5 of 5 |

## Verification

| Criterion | Verdict | Evidence |
|---|---|---|
| AC1 r70 c30 + c31 | **PASS** | 95 names, non-200 0, 0 failing each; c31 11 served + 84 `chain_tried`+reason = 95. Base 43 / 84 |
| AC2 r70 c32 + c33 | **PASS** | 676 members 0 failing; 8 rows 0 failing, 0 out of order. Base 676 / 8 |
| AC3 r69 c29, r68 c27/c28, r67 c23-c26 | **PASS** | 7 cells YES; c24 fully healthy (699 rows, all zeros); ZZZZ control 404 |
| AC4 grant | **PASS** | NO→YES with 4 arms; 3 independent width/neighbour denies after |
| Reported set | **11 of 11 YES** | r64 c9-c14, r65 c17, r66 c18/c19/c22, r64 c15 |
| /peers STOP bar | **PASS** | worst 136.83 ms of 5,000 ms (2.7%), 0 non-200 over 6 invokes |
| /peers **per segment** | **NOT MET** | 0 of 6 invokes emit `AMGT_SEGMENT`; see below |

## The two things the halves could not have known

**1. `/peers` has no segment instrumentation (row Z-S353).** CTO condition 3 says "/peers timed **per
segment**". The total is measurable and healthy. The breakdown is not: 0 of 6 invokes emitted any
`AMGT_SEGMENT` line. That zero is not a dead parser and not "no time was spent" — the same regex read six
segment pairs per invoke off the **day route** minutes earlier in c15, and `scoped_amgt.py` carries 5 emit
sites. The absence is route-specific. I reported it as unmeetable rather than presenting the total as a
breakdown; wiring emit sites would be a served-code change this act's bounds forbid.

**2. The read-path list was right, but right by accident (row Z-S352).** Both halves listed five new S3
read paths; all five were correct. But a forward list has no denominator, so I subtracted instead:
**32** granted prefixes against **24** slash-bearing literals in the 9 changed/added files → 11 uncovered,
9 of them not S3 at all, and **2 store-shaped**:
- `amgt/harvest/state/pull_log/` in the *added* `harvest/bloomberg.py` — a `put_object` reachable only
  from the one-shot `--move-m1` CLI; `bronze_write` refuses the channel outright.
- `filings/v1/` in the *added* `management/roster.py` — a prefix this role's grant was **deliberately
  stripped of** at AMGT-rk-91 M2. Measured a **dead constant** (occurrence count 1 in 1321 lines);
  roster.py's one real `get_object` goes to the *granted* `amgt/harvest/state/filing_attempt/`.

Neither is reachable at request time, so neither is a STOP and no grant is owed. But "complete by
reachability" is not "complete because it was checked", and that is what the row records.

## Decisions Made

| Decision | Rationale |
|---|---|
| Read the IAM prohibition as binding the **code leg** | §1 and BOUNDS 1 forbid IAM changes; §4a *orders* one. The contradiction resolves the only coherent way, and both halves confirm it by grading the grant plan under condition 1 and listing it as leg 1. Proven, not asserted: the grants policy reads `no-op` in the code leg's full plan. |
| Used the audited `# rail-checked:` marker for `simulate-principal-policy` | The rail routes raw `aws iam` to `comp-iam`, which cannot express `(action, resource)` or an `s3:prefix` context entry. Reason stated per call. |
| Added two width probes nobody asked for | Condition 1 only names bronze. `issuer-site/` and `issuer-site/harvest/silver/` close the "is it really one prefix" question at the two levels bronze doesn't cover. |
| Took c15 **first** | Row Z-S349's lesson, applied deliberately. Cost nothing; produced cold 3 of 3 first attempt vs last round's two failed reads + 925 s idle. |
| Did not flip `<status>` | `task-orders/` is not in `<paths>`. |

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/terraform/harvest/scoped-amgt-api.tf` | +1 pool prefix, house-style comment | Yes — `4700710ca5` |
| `.open_deploys/amgt-resapp-r70-at6-…json` | opened, removed at close | Yes — `e8578cca6d`, `0a26380fe7` |
| `change_management/20261005T0805Z_…md` | NEVER-2 entry, OPEN → CLOSED 5/5 | Yes — `e8578cca6d`, `0a26380fe7` |
| `.../INVESTIGATION_v1.md` | rows Z-S352, Z-S353 | Yes — `0a26380fe7` |
| `.../at6_peers_latency.py` | the /peers probe | Yes — `0a26380fe7` |
| `.../AMGT_RESAPP.TO-AMGT-at-6…proof_of_spec.json` | the instance | Yes — `0a26380fe7` |
| `s3://…/research/opal-amgt-scoped-api.zip` | new version | VersionId `.Sj7rblal1sHPyETvJW_ZKXvOzeGVds3` |

## Blockers

**None owed by this seat.** Both rows are INERT with `disarm_owner 2.0.0_SA_COO~Z`; the `<status>` flip is
the issuer's.

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 GS//XHnVd4+bBIg1VU++r1fp9v495pi6jKFat9KbEYE=` at `MemorySize 1769`,
artifact VersionId `.Sj7rblal1sHPyETvJW_ZKXvOzeGVds3`, 0-diff full plan. Its grant now holds **33** pool
prefixes; `issuer-site/harvest/bronze/`, `issuer-site/`, `issuer-site/harvest/silver/` and `identity/` all
still `implicitDeny`. Package headroom **8,230,971 B at 96.9%** — down 154,234 B from round 69, the cost of
seven new modules. Round 70 served state: c30-c33 YES for the first time; c23-c29 and the r64/r65/r66
reported set unchanged and YES; c15 cold 3 of 3.

**Push state: LOCAL @`0a26380fe7` (ls-remote read)** — origin/CLOUD at `41158af7f9`.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The `<status>` flip on at-6.
2. **[`2.0.0_SA_COO~Z`]** Row Z-S353: either wire `AMGT_SEGMENT` into the `/peers` handler (5 emit sites
   already exist in `scoped_amgt.py`, so it is wiring) or change the ask to "the TOTAL on N names", which
   is what an executor can actually measure.
3. **[`2.0.0_SA_COO~Z` / HARVST]** Row Z-S352: delete `roster.py`'s two dead constants. Two unused lines
   are a smaller act than the AccessDenied they invite for the next caller who wires a reader off them.
4. **[`2.0.0_SA_COO~Z`]** Put the c15 sequencing in the order — it still lists c15 last.
5. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. Everything from this seat is LOCAL.
