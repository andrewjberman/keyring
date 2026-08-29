# DEPLOY LEDGER -- D1_CATVIEWS.TO-V1-AE: the gold-lambda re-pin `bf74d031c1` -> `70a0828226`

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T17:34Z. Applied in full in-session, verified on the live
plane at the BYTES rung. Opened at start per CLAUDE.md NEVER#6 / NEVER#2. Nothing half-landed.

⚠ **AC7 IS FILED OPEN AND IS NOT PART OF THIS CLOSURE.** It is EVENT-GATED on the next scheduled gold
fire (the ~13:00/13:30Z fire already ran ~4h BEFORE this apply). AC3 is the PACKAGE rung; AC7 is the
SERVED rung; they are different claims and only the first is closed here.

| field | value |
|---|---|
| opened | 2026-08-28T17:25Z |
| closed | 2026-08-28T17:34Z |
| seat | `0.7.0_AE_CloudOps~Z` |
| TO | `D1_CATVIEWS.TO-V1-AE.gold-lambda-repin-and-apply` (face @`81b6173b40`, re-committed mid-execution) |
| decomp cell | `D1-i-2`, with `D1-inv-5` riding every criterion |
| issuer | `2.0.0_SA_COO~Z` |
| authority | **Andrew-direct 2026-08-28 ~17:0xZ, VERBATIM: "all recs approved"** -- record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooZ_ANDREW_DIRECT_20260828_1705Z_SHIP_LIFT_BLOOMBERG_GRANT_D4_READ.md` @`8d86c930cd` |
| stack | `infra/aws/terraform/mdpf-pipeline/` |
| function | `mdpf-gold-lambda` |
| old pin | `bf74d031c1` (declared) / **deployed vintage was `14b077f559`** -- see the note below |
| new pin | `70a08282269217b3ccae4bb2776372690201743f` |
| CodeSha256 | `X8oLXSRZG1W5WBhle6LSg/unVp9m6/0kja3dUMbEA3w=` -> `bnpYayh00uIIIlZEMjc3pKmKz6bFcuHGY6F2DI4HZTY=` |
| CodeSize | 804,455 -> 813,374 |
| LastModified | 2026-08-28T01:12:11Z -> **2026-08-28T17:28:29Z** |
| S3 object version | `2hwZEYAHvPRLw3C5y6xBqHPrWqvXWqmv` -> `zxLyMp0d_xQW1vlHnINvS2b4voNpliyq` (**rollback target = the former**) |
| apply | `0 added, 1 changed, 0 destroyed` via `.tools/safe-apply.sh`, `-target=aws_lambda_function.mdpf_gold` |

## THE NO-SHIP IS LIFTED BY NAME -- the interlock's own release condition is met

`build_package.py`'s interlock stated its release condition: *"the lift is a named act by COO or
Andrew, and no seat has made it."* Andrew made it. **That sentence is now false and has been
superseded in place** (AC6), not deleted -- it is what states the condition this lift satisfies.

## THE TWO BOUNDS -- BOUND 2 CARRIED A FALSE MECHANISM AND IS CORRECTED HERE

**BOUND 1 -- THE SWEEP WAS NON-EXHAUSTIVE BY ITS OWN AUTHOR.** "The four known blockers are gone",
**not** "D1_CATVIEWS is clear." A decision on stated incomplete information is not a clearance.

**BOUND 2 -- THIS SHIPS TWO DEFECTS OF THREE.** It repairs the 49financial SMA branch and the `Models`
L2 `--` render. It does **not** touch the `global` scope.

⛔ **RETRACTION, RECORDED BY NAME RATHER THAN EDITED AWAY.** This entry was OPENED carrying the
framing *"it cannot move the global Client understatement of $359,773,356.74, that gap being exactly
cottonwood + inflection, so 49financial cancels identically."* **THAT MECHANISM IS RETRACTED** --
`1.0.0_SA_CTO~Z` originated it and went after its own (`2.0.0_SA_COO~Z` 13554, `3.0.0_SA_CVO~Z` 13550,
both post-dating this entry's opening). Measured on the served object:

```
global.Client    "predicate": "unavailable"   "held_constituents": ["cottonwood"]   children {}
49f.Client       "predicate": "available"     "held_constituents": null
```

**The node DECLARES ITSELF HELD and names its holder.** `mdpf_gold_consolidator.py:143-160` specifies
exactly that: `global` has no `CLIENT_L1_RULE` entry, `client_l1_split('global')` raises deliberately,
and global unholds by itself when cottonwood clears. **The hold is working as designed. There is no
shortfall to measure.** What exists is a residual `aum` on a held node plus a renderer printing a
headline the data already marked unavailable.

>> **THE CONCLUSION SURVIVES THE RETRACTION: this deploy does not touch `global`, so "category-views
   is now correct" remains the sentence not to write.** Only the mechanism was false, not the bound.

## WHAT ACTUALLY LANDED -- exposure re-measured at this seat

⚠ **THE TO STATES 7 files / 2,521 insertions / 71 deletions. I MEASURE 8 / 2,551 / 82.** Derived by
parsing the live `PACKAGE` list out of `build_package.py` (22 declared members) and running
`git diff --numstat bf74d031c1 70a0828226 --` over those exact paths:

```
   1211 +    0 -   data/mdpf/scripts/gold/mdpf_category_registry.py       <- COMING INTO EXISTENCE
    464 +   20 -   data/mdpf/scripts/gold/mdpf_gold_consolidator.py
    327 +    5 -   data/assets/scripts/gold/build_cottonwood_mdpf_pair.py
    269 +   35 -   data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
    153 +    6 -   data/mdpf/scripts/gold/mdpf_aggregate_aua.py
     55 +    3 -   data/assets/scripts/gold/build_cottonwood_mdpf_slice.py
     42 +    2 -   data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py
     30 +   11 -   data/mdpf/config/partner_roster.json                   <- THE DELTA vs the TO
   TOTAL  8 files, 2,551 insertions, 82 deletions
```

>> **THE DIFFERENCE IS EXACTLY ONE MEMBER: `partner_roster.json` (+30/-11).** 2,551-2,521 = 30 and
   82-71 = 11, both fully accounted for by that single row. The TO's figure covers the seven `.py`
   modules; **a CONFIG member also moves and ships in the same zip.** Recorded because AC5 requires
   this entry to state what actually lands, and a config change is a different KIND of member, not a
   rounding difference. **No defect is implied and nobody has reviewed it.**

**RIDE-ALONG DRIFT = 1,340 lines across 7 members** (total minus the 1,211 that are
`mdpf_category_registry.py` being born). The TO says 1,381 across 6; the gap is the same
`partner_roster.json` row plus the module/config split. **Nobody has reviewed those 1,340 lines and no
defect is asserted.** The claim is only that *"ships the SMA branch fix and the L2 values"* is true
and INCOMPLETE -- which is the entire reason this section exists.

⛔ **THE BREADTH IS INHERENT.** A git pin resolves ANCESTRALLY; `70a0828226` already contains
`a5227cf161` (`is-ancestor` rc=0), so one pin carries both fixes and *"just these two commits"* is not
expressible as a pin. `bf74d031c1` is also an ancestor of `70a0828226` -- an advance, not a divergence.

## ACCEPTANCE

**AC1 -- THE PIN CARRIES BOTH FIXES. PASS.**
```
_l0_of at NEW pin 70a0828226 (source rung)        3    EXPECT >=3        PASS
_l0_of at OLD default bf74d031c1                 0    NEGATIVE CONTROL  clean
is-ancestor a5227cf161 -> 70a0828226            rc=0  one pin, both fixes
```

**AC2 -- DEPLOYED VIA TERRAFORM `safe-apply`. PASS.** Plan reviewed before apply. `0 added, 1 changed,
0 destroyed`. No bare `terraform apply`; no `aws lambda update-function-code`. Post-apply
`terraform plan` shows **`aws_lambda_function.mdpf_gold` 0-diff**.

**AC3 -- THE DEPLOYED BYTES CONTAIN THE CHANGE. PASS, all four arms.**
```
A  deployed package pulled from Code.Location            813,374 B
   in-zip BUILD_MANIFEST source_vintage.commit           70a08282269217b3ccae4bb2776372690201743f
B  _l0_of in running bytes                               3        (pre-deploy 0)
   _l0_of(member.view_path) sites          :637 Models   :644 SMA
C  'elif member.view_path == "SMA"'                      0        (pre-deploy 1, at :591)
D  POSITIVE CONTROL git show 70a0828226:<path> _l0_of    3        MUST return 3
   deployed member sha256   8781c4d7ecde906a8624516fbf8958e699b728999483389188c69769f9d74ad5
   pin source     sha256    8781c4d7ecde906a8624516fbf8958e699b728999483389188c69769f9d74ad5   IDENTICAL
```
Extract and read done under ONE path convention on the session scratchpad ABSOLUTE path (the MSYS
`/tmp` vs native-Windows `C:\tmp` hazard silently corroborates rather than failing).

### ⛔ AC3 ARM C AS WRITTEN CANNOT DISCRIMINATE -- FOUND PRE-DEPLOY, REFINED PREDICATE USED

Arm C is written `grep -n 'member.view_path == "SMA"'`, **EXPECT 0 (pre-deploy: :591)**. The pre-deploy
half is **exactly right** -- measured at line **591** in the deployed bytes. The post-deploy half is
wrong, and it fails in the direction that reads a CORRECT deploy as a FAILED one:

```
                                              DEPLOYED(pre)   POST-DEPLOY
arm C as written   'member.view_path == "SMA"'       1              1     <- CANNOT DISCRIMINATE
refined            'elif member.view_path == "SMA"'  1              0     <- discriminates
```

**The surviving hit is `:547`, inside `_l0_of`'s own docstring** --
`was :611   member.view_path == "SMA"   EXACT -- brittle` -- the historical record of the very defect
being retired. **Documentation, not a branch.** As written the arm returns 1 in BOTH states: its
evidence cannot differ if the claim were false, which is the Rule-22 DISCRIMINATION failure exactly.
The `elif ` prefix is what separates the live branch from the docstring line. **Reported to the issuer
rather than quietly substituted**, because the fix retires a criterion that would have produced a
false FAIL on a correct deploy.

**AC4 -- SOURCE-MAP ENTRY. PASS.** The entry EXISTED (Rule 4 satisfied structurally); its deploy
vintage was **stale by two pins** -- `last_deployed_commit` read `530ba66971` while the actually
deployed vintage was `14b077f559`. Updated: `artifact_sha256`, `last_deployed_commit`,
`last_deployed_at`. Also corrected the entry's `_build_note`, which said "19 entries: 16 modules + 3
configs" while `PACKAGE` declares **22**.

**AC5 -- THIS LEDGER.** Opened at start, closed at completion, carrying the measured exposure above
rather than the TO's figure.

**AC6 -- THE LIFT RECORDED IN `build_package.py`'s INTERLOCK. PASS.** 55 lines, purely additive,
ASCII-only, `py_compile` OK. Records the lift, its date, Andrew's verbatim, the record path + commit,
**and both bounds** (with BOUND 2 carrying the retraction above). ⛔ **The `--pin` default was NOT
advanced** -- asserted programmatically as unchanged at `bf74d031c1` before the write. The interlock's
own expiry clause says *"THEN advance the pin and delete this comment in the same commit"*; **AC6
overrides that instruction** (comment-only; advancing the default is a separate decision -- surface a
rec, do not take it silently). **REC SURFACED, NOT TAKEN.**

**AC7 -- OPEN.** Event-gated on the next scheduled fire. Control set is **`cottonwood` + `inflection`
ONLY**. ⛔ `global` goes in **NEITHER** column -- not a control (its behaviour across a fire is
UNKNOWN) and not expected-to-move (nobody has measured what moves a residual on a held node).
**RECORD IT, UNSCORED.** Baseline: **path
`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_D1_PREDEPLOY_BASELINE_20260828/README.md` AT HEAD** --
⚠ **both `@bc9d11dd8e` AND `@4c4f245316` are SUPERSEDED**, and `@4c4f245316` specifically still
contains the retracted "global is PREDICTED to move" block. *(This entry cited `@4c4f245316` when
opened; corrected here. The PATH is the locator, the hash only a vintage stamp.)* No ad-hoc gold run
was fired -- that prohibition stands and the discriminator is the point.

## A SECOND, UNRELATED CHANGE WAS IN THE PLAN AND I SCOPED IT OUT -- SURFACED, NOT ACTED ON

The unscoped plan was **2 to change**, not 1. The second was
`aws_s3_object.mdpf_route_bindings` (`config/mdpf/route_bindings.yaml`), content-sha256
`c9e54ce2...` -> `98f5e9c5...`. **PRE-EXISTING DRIFT, NOT MINE:**

```
working tree data/mdpf/config/route_bindings.yaml   98f5e9c5...   git status: CLEAN (not my edit)
live S3 config/mdpf/route_bindings.yaml             c9e54ce2...   LastModified 2026-08-07 (21 days)
last tree commit touching it   f999fb25f6  "MDPF_REMED.W1-1: repoint the 49F custody binding off the
                                            deleted DDB table -- ATOMIC across 4 files"
```

>> **A change whose own commit message calls it ATOMIC across 4 files has one leg unlanded for 21
   days.** It is outside this TO, I have not reviewed it, and applying it under this ledger would have
   shipped an unreviewed config change on someone else's behalf. **I targeted the apply to
   `aws_lambda_function.mdpf_gold`** (sanctioned by the cloud-ops pre-flight: *"target the specific
   resource, note targeting in the RAVC"*) and surfaced the drift to `2.0.0_SA_COO~Z`. **Not
   adjudicated here** -- I do not claim it is a live defect, only that it is committed-but-unapplied
   and that its own author called it atomic. It remains pending in `terraform plan`.

## ROLLBACK PATH (unused)

S3 key is versioned. Rollback = re-point at version `2hwZEYAHvPRLw3C5y6xBqHPrWqvXWqmv` (804,455 B) and
re-apply. The pre-deploy package is also retained in the session scratchpad. No destructive step was
taken at any point in this deploy.

---
*Opened and closed `0.7.0_AE_CloudOps~Z` 2026-08-28. AC7 tracked separately and remains OPEN.*
