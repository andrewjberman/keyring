# AMGT_RESAPP round 63 -- am-6 both legs and am-7's four new keys -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Date:** 2026-10-02
**Task Order:** AMGT_RESAPP.TO-AMGT-am-6 (legs 1 and 2), AMGT_RESAPP.TO-AMGT-am-7 (sections 1, 6, 7)
**Status:** am-7 COMPLETE. am-6 IN PROGRESS -- both legs' acts performed, AC1 UNMET and not self-adjudicated.

## Objective

Three ordered acts on `opal-amgt-scoped-api`, each under its own never-widen pair and NEVER-2 entry:
am-6 leg 1 (code-only redeploy carrying am-3/am-4/am-5), am-7 (four new stored keys), and am-6 leg 2
(am-1's code, then the memory step-down from 10240). All three GOs arrived and were acted on in session.

## Compiler Tools

| Tool | Invocation | Result |
|------|-----------|--------|
| `build-and-upload-scoped-amgt.sh --build-only` | `bash ... --build-only <zip>` (leg 1, leg 2) | PASS. The pre-upload STOP gate. Leg 1 353/343/7/3/0; leg 2 353/352/1/0/0. `content_diff.py` is a REPORT that exits 0 on a mismatch, so the grading is the seat's, not rc's. |
| `build-and-upload-scoped-amgt.sh` | `bash ...` (leg 1, leg 2) | PASS. Each real build reproduced its build-only diff identically, so the diff graded pre-upload is the diff that shipped. |
| `terraform plan` / `show` / `show -json` | `-chdir=infra/aws/terraform/harvest` | PASS. Whole plan read (24 lines leg 1), then graded from JSON across all 49 `resource_changes` rather than from rendered text. |
| `terraform plan -detailed-exitcode` | after each code apply | PASS. Exit 0 = no changes. A machine oracle, not a prose read. |
| `.tools/safe-apply.sh` | `-chdir=... apply <saved plan>` x4 | PASS. One code apply per leg plus three memory applies. comp-tagauthz GATE PASSED; tombstone-gate CLEAN; naming WARNs are all pre-existing names on existing resources, 0 additions. |
| `boto3` S3 | head/put/get/list against `opal-data-harvest` | PASS. Chosen over the `aws` CLI deliberately: the am-7 keys carry real slashes AND a literal `-SLASH-` token, and MSYS argv conversion is a measured mangling class here. boto3 takes the key as a Python string and cannot mangle it. |
| `r63_served.py` c1/c2/c3/c4/c5/c6 `--where deployed` | per each order's literal invocation | Mixed by design: c3/c4/c5/c6 PASS; c2 met as amended; c1 UNMET at every memory. |
| `.tools/deploy_ledger.py` | open / close-leg / close / check | PASS x3 entries, 3+3+4 legs all proven and closed. See "What failed" for the shared-index collision. |
| `.tools/safe-commit.sh` | `--author ... -F <msgfile> -- <paths>` | PASS on 4 commits. Two aborted mid-peer-drain and correctly reported committing nothing. |

**What worked:** `content_diff.py` is the whole gate for a never-widen code act -- it answers "did the artifact
change exactly what the half says" against the DEPLOYED bytes, which no git diff can. Grading the terraform plan
from `show -json` rather than the rendered text let me prove `memory_size before=10240 after=10240` positively
instead of inferring it from absence in a truncated view. `-detailed-exitcode` turns 0-diff from a prose read into
a machine oracle.

**What failed:** `deploy_ledger.py open` STAGES its own two files into the shared index. Three times this session
that collided with a live peer drain: once `safe-merge --continue` refused and `2.0.0_SA_COO~H` applied the
prescribed unstage (msg 28621); once `index.lock` was held so I could not even unstage; and the am-6 leg-2 sentinel
ended `AD` (staged-added, deleted-from-worktree) after `close` removed it, which would have committed a file that
does not exist. Net effect on the record: the am-7 and leg-2 sentinels were NEVER committed (measured: 0 commits
ever touch either path, against a positive control of 2 for leg 1's). Nothing is stranded -- the gate reads
sentinels and an absent sentinel IS the terminal state -- but a seat following NEVER-2 literally would expect the
OPEN entry on record and it is not there.

**Gap found:** the comp-tool rail has no instrument for "is the shared index safe to stage into right now".
`comp-schedule` reads gate ledgers, not git index state. The three collisions above were each found by a tool
refusing, never by a check I could run first.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | am-6 leg 1: base re-read live | `bZBmEtRr...`, 10240, 11:26:56Z, 41118711 B -- all equal to both halves |
| 2 | leg 1 `--build-only` | `353 / 343 / 7 / 3 / 0`; the 10 non-identical files ARE the table's 10, zero outside |
| 3 | leg 1 NEVER-2 opened + committed | `28765a36ca` |
| 4 | leg 1 build + upload | VersionId `Eb6lQYKJX.4eL8K.Qq0LHCRJs5AzCfk2`, sha256 `JVMY1ZDA...`, read back matched |
| 5 | leg 1 code-only `safe-apply` | 0 added, 1 changed, 0 destroyed; `memory_size` before=after=10240 |
| 6 | leg 1 0-diff re-plan | `-detailed-exitcode` 0 |
| 7 | leg 1 graded | AC2 c3 YES, AC3 c4 YES, c5 YES; entry CLOSED; `6e67441488` |
| 8 | am-7: both plan pins + 4 per-key sha256 | all MATCH; 4 of 4 keys 404 with a positive control returning a VersionId |
| 9 | am-7: four PUTs | `IhgGo4SLO2eh...`, `3M7mBXYbQskx...`, `JnY3RSuWrNJP...`, `M.lsmArE9oWT...`; all NEW; read-back by content 4 of 4 |
| 10 | am-7 graded | AC1 c2 met as amended (exit=1 from C1 alone), c6 52 of 52; entry CLOSED; `eb079d1e36` |
| 11 | am-6 leg 2 `--build-only` | `353 / 352 / 1 / 0 / 0`, the one file `lib/research/api/scoped_amgt.py` |
| 12 | leg 2 build + upload | VersionId `CKyMtWEYJ0kZIjstvY2gMYDtm5YhLjlt`, sha256 `wIpMaswM...`, read back matched |
| 13 | leg 2 act (A) `safe-apply` | 0/1/0; `memory_size` untouched; re-plan `-detailed-exitcode` 0 |
| 14 | leg 2 act (B) memory 1769 | one apply, plan diff exactly `{memory_size}`; c1 MISS |
| 15 | leg 2 act (B) memory 3538 | one apply, plan diff exactly `{memory_size}`; c1 MISS |
| 16 | leg 2 act (B) restore 10240 | one apply; c1 MISS; tf byte-identical to HEAD |
| 17 | leg 2 condition 3 + close | 7 of 7 routes 200; c3/c4 unchanged; entry CLOSED; `fe399411c4` |

## Verification

Final live state of `opal-amgt-scoped-api`:
```
{
    "CodeSha256": "wIpMaswMhfNvJaz7WXTyBhN5C3Bb7Qego6+u+aOslfI=",
    "MemorySize": 10240,
    "LastUpdateStatus": "Successful"
}
```

am-6 leg 2 act (B), every memory tried with its three cold durations:
```
1769    run1 11922.53 cold   run2 12079.06 cold   run3 14430.50 cold    FAIL C1 0 of 3
3538    run1 12038.69 cold   run2 12481.75 cold   run3 11740.42 cold    FAIL C1 0 of 3
10240   run1 11966.75 cold   run2 11966.63 cold   run3 10599.80 WARM    FAIL C1 0 of 3
```
All nine invokes: status 200, 6 of 6 articles carrying a headline, `headline_reason` absent.

am-7's four writes, after the PUTs:
```
management/v1/6501_JP_Equity/2026-10-02.json          IhgGo4SLO2eh.LLG7COpr_XiSUBHvapU    3229 B
management/v1/2317_TT_Equity/2026-10-02.json          3M7mBXYbQskxBUsVouH1NWU2PzCCnj5F    3082 B
peers/v1/BP-SLASH-_LN_Equity/2026-10-02T1543Z.json    JnY3RSuWrNJPpP1Fkpzw0Ve9LQnxNyMo   47510 B
peers/v1/NG-SLASH-_LN_Equity/2026-10-02T1543Z.json    M.lsmArE9oWTLmtf_KRJxNP44XwZWLUG   47333 B
```

Condition 3 sweep at the final memory, 7 of 7 at 200 and the six security bodies byte-identical to leg 1:
```
BA overlay 101996   thesis 506924   peers 51165
VLO overlay 104807  thesis 658857   peers 51356
collected/chatter 67005
```

## Decisions Made

1. **Resolved the build pins by CONTENT, not ancestry.** Leg 1's GO named `4197279e67` with HEAD 39 commits
   later. Rather than lean on `merge-base --is-ancestor`, I measured that 0 of the 74 differing paths fall in the
   package's reachable roots and the worktree is clean over them -- so the tree is content-equivalent for
   everything the artifact packages. The authoritative confirmation remained `content_diff.py` against the
   deployed bytes.
2. **Graded both content diffs FILE FOR FILE, not on the four summary counts.** Matching only counts would pass a
   diff that swapped one file for another.
3. **Did not unstage a peer's in-flight work to clear my own commit path.** When `2.0.0_SA_COO~D` held 8 staged
   files, I ran safe-commit scoped to my own pathspec rather than applying cloud-ops' "unstage the strays" remedy,
   which is written for one's own strays. Their work landed intact under their own author line (`9d8b7711e0`).
4. **Left am-6 at `pending` rather than self-marking `complete`.** Both legs' acts are performed and act (B)'s
   escalation is exhausted, but AC1 is UNMET. Marking complete would read as success; the 5 s target is the
   issuer's and the CTO's to adjudicate.
5. **Did not file a surprise row for the flat memory curve.** The order explicitly prescribed the
   1769 -> 3538 -> restore branch, so a miss at all three is an anticipated OUTCOME to report, not a
   `spec_asserts` vs `world_is` divergence.

## Files Modified

See commit messages: `28765a36ca`, `6e67441488`, `eb079d1e36`, `fe399411c4`. No terraform file is changed at
HEAD -- act (B) returned `scoped-amgt-api.tf` to byte-identity with HEAD, so the memory excursion left nothing
behind.

## Blockers

**None owed by this seat.** am-6's AC1 is UNMET but that is an open ADJUDICATION at `2.0.0_SA_COO~Z` and
`1.0.0_SA_CTO~Z`, not a blocker on me: the order's acts are all performed and its escalation exhausted.

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 wIpMaswMhfNvJaz7WXTyBhN5C3Bb7Qego6+u+aOslfI=` (the leg-2 artifact,
built at `6436cc930a`) at `MemorySize 10240`, `Timeout 29`, artifact
`s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip` VersionId
`CKyMtWEYJ0kZIjstvY2gMYDtm5YhLjlt`. All three NEVER-2 entries are CLOSED with every leg proven. Four new objects
are live in `opal-data-harvest` under `management/v1/` (6501_JP, 2317_TT) and `peers/v1/` (BP, NG).

Served state: c3 YES (95 of 95), c4 YES (12 of 12 on BA and VLO), c5 YES (fabricated key 404), c6 YES (52 of 52),
c2 met as amended (6501_JP and 2317_TT serve their own reasons; ASML_NA still ABSENT and HELD), c1 UNMET at
~11.5-12.0 s cold against a 5,000 ms clause.

**The finding that matters for the next cut:** the cold duration curve is FLAT in memory -- means 12810 / 12087 /
11511 ms at 1769 / 3538 / 10240. 5.8x the memory buys about 10% of the time, so the handler is not CPU-bound and
the 5 s target is not reachable by sizing, exactly as `scoped-amgt-api.tf`'s own comment block predicted. What
leg 2's code DID buy is separable and real: al-1 measured 15.1-19.1 s cold at 10240 WITH the request-time silver
read, and removing it (track C, this leg's one changed file) brings 10240 to ~11.5-12.0 s -- roughly 7 s. The
remaining ~12 s is elsewhere.

**Also named, not acted on:** the artifact is at 96.8% of the 262,144,000 B unzipped ceiling with 8,476,082 B
spare. The next cell that ADDS to this artifact measures at cut time; crossing is a deploy STOP.

## Next Steps

1. **[`2.0.0_SA_COO~Z`] / [`1.0.0_SA_CTO~Z`]** Adjudicate am-6's AC1: accept ~12 s, recut against the remaining
   cost, or revisit the 5 s target. The order sits at `pending` awaiting that call. Memory is not the lever and
   the measurement is in the instance.
2. **[`2.0.0_SA_COO~Z`]** FWD-7 stays NOT_REALIZED: ASML_NA's officer list needs the budgeted Bloomberg sign-in,
   which is Andrew's per-use act (row `AMGT_RESAPP-Z-W205-S1`). am-7 wrote the two names that could be written.
3. **[`0.0.0_AB_MSTR~Z`]** The push. All four commits are LOCAL on this device.
4. **[whoever owns `.tools/deploy_ledger.py`]** Consider not staging at `open`, or staging into the invoking
   worktree's index only. Three collisions with live peer drains in one session, and two sentinels that were
   never recorded as a result.
