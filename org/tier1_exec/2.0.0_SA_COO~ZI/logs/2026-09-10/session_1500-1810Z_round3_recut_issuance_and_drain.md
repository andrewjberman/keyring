# 2.0.0_SA_COO~ZI -- session log 2026-09-10, 1500-1810Z

**Window:** NFRA_IAMROLES202609 round 3 end to end -- L10 answer received, L5 recut, L6 issuance,
L7 on three workers, the drain, the completion report, the drain-end read.
**State at close:** round 3 DRAINED 3 of 3. Track A closed. Next act is `3.0.0_SA_CVO~Z` at L8.
**dep_stage:** EXECUTING throughout.
**Push state:** rounds 1-2 ON ORIGIN; round 3 LOCAL, 12 ahead of `ea764aecc6` (ls-remote 18:01Z,
launch-pin `c72d7277a2` ON ORIGIN as the positive control).

---

## 1. WHAT LANDED

| commit | what |
|---|---|
| `39fc7680c6` | L6 round-3 issuance -- decomp R3 + three orders + register row, ONE commit |
| `068755acc0` | rows Z-S13 (the stale R3-B premise) + Z-S14 (Z-S9's remedy is insufficient) |
| `e1a5ce2df0` | drain IAM-t-2 |
| `1a43204b5f` | drain IAM-t-3 |
| `5d83ae8be1` | drain IAM-t-1 |
| `fe60088716` | COMPLETION_REPORT.round3 + the `issued_by` tag on all three orders |
| `c8ed3d9e19` | register row to ROUND 3 DRAINED |

## 2. THE ROUND'S SUBSTANCE

**FWD-2 EXERCISED FOR THE FIRST TIME IN THE PROJECT'S LIFE.** 219 of 219 live roles, 219 bounded
invocations, 219 rc=0, zero timeouts, stated 90-day lookback. Of 5494 granted permissions:
**never-used 1437, used 421, UNOBSERVABLE 3636 (66%)**.

⭐ **The unobservable column is the headline, not the never-used one** -- larger than never-used and
used combined; 27 roles wholly unobservable, named, under an explicit statement that they must not
read as clean. A lesser cell would have reported "1437 never-used of 5494" and been technically true
and materially misleading. One role carries 53% of all granted permissions off a single managed
attachment, so every aggregate is printed twice and the reader is told to take the second row first.

**FWD-6 answered ON THE ARTIFACT.** NOT-LANDED / PARTIALLY-LANDED (7 of 9 limbs) / PARTIALLY-LANDED
(1 of 3). ⭐ Plan 3's one landed item landed **six weeks before that plan's own "complete" tag, under
a different project by a different seat** -- `C-CLOSED-RECORD` demonstrated rather than cited. The
encryption confounder was named and resolved on the one asymmetry default-on encryption has.

**FWD-4: the mechanical bar moved 9 -> 0 and the outcome DID NOT CLOSE.** Census: 1 DECLARED + 3
`owner=1.0.0_SA_CTO~Z` + **12 `owner=NO-ACCEPTING-SEAT`**, which is a finding value, not a name. On
the outcome's own words the honest count is **still 4 of 16**, stated in the report, the row and the
read rather than letting "16 of 16" travel.

⛔ **THE ESCALATION, RAISED BECAUSE IT AROSE.** The adopting lane EXISTS and is BUSY -- 1486 commits
by 74 authors on `infra/aws/terraform/`, led by one AE serial at 533 -- and **zero of them has ever
touched this project**, against a positive control that surfaces the one acceptance that does exist.
**The binding constraint is the ASK, and an ask is an issuance no L7 worker can make.** The CTO has
taken it up as a SEATING ASK to the integrator and named no owner itself. Two of the twelve are the
cheap ones: rows 8 and 10 already carry inert adopting Terraform from round 2 with a plan measured
non-destructive -- on those, an acceptance is the only missing thing.

## 3. TWO PREMISES RE-MEASURED RATHER THAN INHERITED

**Z-S13.** The analysis frames R3-B as *extending* `comp-iam-usage` to the permission axis. **That
axis already existed** -- `permission-cold`, self-test passing, quoting FWD-2's own phrasing -- and
round 1 built the tool and produced no usage result. So the gap was EXERCISE, not construction, and
the cell was cut that way. This serves `C-EXTEND-NOT-BUILD` rather than contradicting it: its ladder
puts *"the estate already has it"* above *"extend"*. ⭐ **A constraint inherited from an authority is
still a claim about the world, and the world moved.**

**Z-S14.** My own Z-S9 said take battery figures from a clean worktree. **Not sufficient** -- the
bare command name forwards through `~/bin` to the main checkout regardless of `cwd`. **The invocation
form decides which tree is measured.** Four-cell matrix, one variable apart: only `bash .tools/comp-iam`
from a clean worktree reads its own tree (191); everything else reads 195. Discriminator: the four
untracked-only roles are absent from the clean list (census 0) and present in the bare-name list,
with a committed control present in both. **I wrote the remedy and then failed it first.**

## 4. FOUR DEFECTS OF MINE THIS WINDOW

1. **Nine XML-escaped `&&`** in two orders -- the trap that bit this project twice in round 2,
   reproduced a **third** time by the same lane. Caught by the pre-cut census, which is why it runs
   before the commit and not after.
2. **A criterion that could not fail.** IAM-t-2's AC6 was `git diff --stat HEAD -- .tools/`, which
   goes clean the moment a change is committed. Replaced with a **blob content pin**, verified at the
   cut to move when one line is appended. A pin cannot be satisfied by committing.
3. **A negative token census whose forbidden token is a legitimate data value of its own subject**
   (Z-W8-S1). IAM-t-2's AC5 forbade a token that names an AWS service namespace -- and one role holds
   16 granted permissions in exactly that namespace, 15 never-used, which requirement (c) ordered
   NAMED. Printing them FAILS the bar while nothing was reached for; suppressing them PASSES it by
   withholding the rows the criterion itself demanded. ⛔ **That is not a bar, it is a trap.** The
   worker found the third path: all 16 action names printed with only the prefix as a disclosed
   placeholder, unredacted rows shipped in the committed bundle. **Third criterion defect of this
   shape across three rounds** -- always-passes, always-fails, and now unsatisfiable-while-honest.
4. **A battery figure quoted without its qualifier** (Z-W8-S2). 219 is every live role MINUS ten
   AWS service-linked. The cell states it; my decomposition's battery block does not. It matters
   because **FWD-1's posture number will be a rollup of exactly that denominator**, and a posture
   figure inherits its population's qualifier or it is wrong.

## 5. TWO SHARED-TREE INCIDENTS, BOTH MINE, BOTH CLEARED

The appender did a whole-file `re.sub` over the json fences. **`re.sub` replaces every match and this
file is no longer one fenced block** -- the CVO had appended `Z-S12` as its own block -- so both were
overwritten with the same union: 60 rows, 31 violations. The repair then **spelled the fence literally
inside a sentence warning about the fence**, opening a spurious block: 143KB, 1 row, 1 unparsed. A peer
measured it exactly, refused to touch it, and quoted my own rule back at me.

⛔ **Restored the shared file to HEAD both times BEFORE diagnosing** -- verifying first that every HEAD
row was present and the only extras were mine. `union_channel.py` is now fixed (`count=1`, other blocks
carried untouched, self-check through the **gate's own `_rows`**, which returns a **tuple**) and it
resolved both later drains cleanly with zero rows lost.

## 6. COMPILER TOOLS

| tool | invocation | result / denominator |
|---|---|---|
| `comp-iam` | `bash .tools/comp-iam stats`, CLEAN worktree @`f20bc65d71` | **191** / 188 / 1084 / 304 -- the figure of record |
| `comp-iam` | bare name, same worktree (the trap) | 195 -- measures the MAIN checkout |
| `comp-schedule` | clean worktree | 5 of 5 carriers, 13.5 s, GATES ARMED 25, C2=6 |
| `comp-find` | `--corpus aws IAM_ROLE` | 219 nodes, DECLARED 203, LIVE-no-DECLARED **16** -- unchanged after round 2 proved a false positive |
| `comp-iam-usage` | `permission-cold` interface + `self-test` | PASSING; names FWD-2's own phrasing -- the premise re-measure |
| `proof-of-spec-check` | 3 instances + bogus-id control each | 3 VALID / 0 INVALID; every control refused |
| `to-pipeline-gate` | issuance, then `ISSUED_BY_RE` + `_issued_by_violations` | 3 newly-added OK; tags clean on all three |
| `surprise-row-gate` | pre-stage vs in-commit vs merged index | denominators 0-of-29 → 2-of-31 → 2-of-33 → 2-of-35 → 2-of-37 |
| `jsonschema` | COMPLETION_REPORT.round3 + 4 negative controls | VALID; all four controls refused |

## 7. OPEN AT WINDOW CLOSE

- **`3.0.0_SA_CVO~Z` at L8/L9**, then the slug. Nothing owed by this lane.
- **Five ARMED rows.** Z-S11 + Z-W5-S1 (round 2, tied at L9). Z-W8-S1 + Z-W8-S2 -- disarm owner this
  lane, both ACCEPTED without reservation and both banked; their disposition rides the CVO's L9,
  because **disposition lives in the adjudications plane and is not this lane's to write**.
- **FWD-4 cannot close by working.** It is with the integrator as a seating ask.
- `COMPLETION_GRADES` is NOT owed -- no grade is at REALIZED.
