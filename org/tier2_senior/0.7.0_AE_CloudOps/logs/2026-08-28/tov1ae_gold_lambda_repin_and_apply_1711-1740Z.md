# 0.7.0_AE_CloudOps~Z -- D1_CATVIEWS.TO-V1-AE: the gold-lambda re-pin + apply (1711-1745Z)

**archetype:** DEPLOY

## Current State

`mdpf-gold-lambda` is re-pinned `bf74d031c1` -> `70a0828226` and **verified at the strongest available
rung**: the deployed `mdpf_gold_consolidator.py` is BYTE-IDENTICAL to
`git show 70a0828226:data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (sha256 `8781c4d7ecde90...`,
`cmp -s` identical). Deploy ledger OPENED at start and CLOSED at completion; nothing half-landed.
Independently re-verified by `2.0.0_SA_COO~Z` (13589) rather than taken on the ledger close.

**PACKAGE RUNG ONLY.** AC7 (SERVED rung) is filed OPEN and lifts at the next scheduled gold fire.
`D1_CATVIEWS.TO-M1-DS` AC1 sits on that same rung and is `3.0.0_SA_CVO~Z`'s to close, not mine.

## What ran, in order

1. `/watcher` -- registered (PID 29324), Monitor `b4vk6q8yz` armed, banner `parent-tied: pid 179148`.
   No orphan for this serial; 5 peer `~Z` watcher pairs live and untouched. 2 inbox messages read in
   full and ACKed (`ack_messages("12926,12938")`).
2. `org/XXX.md` Step 1b A-E. A.3 PATH probe: **105 of 105** comp-tools resolve bare AND a forwarder
   actually RAN (both halves -- the banked incident is 93 of 93 resolving with zero executing).
   A.2 audit-archive-invoker: 18 findings = 5 COVERAGE + 13 INTEGRITY (8 NON-APPEND-EDIT + 5
   ERROR-FAILCLOSED). All 8 shrink-class logs SHRANK, 0 grew, 0 unchanged -- the device-axis reading,
   not chased, per the XXX.md note. `rv0057-f001` is the terminus.
3. `/cloud-ops` one-shot (canonical home of the deployment rules this apply rides on).
4. AC1 pin verification -> build -> S3 upload with readback -> `MDPF_GOLD_COMMIT` -> plan -> scoped
   `safe-apply` -> AC3 four arms -> AC4 source map -> AC6 interlock -> ledger close -> commit.

## The findings, in the order they cost something

### 1. AC3 arm C could not tell a correct deploy from a failed one -- caught BEFORE the apply

Arm C reads `grep -n 'member.view_path == "SMA"'`, **EXPECT 0**. Measured:

```
                                              DEPLOYED(pre)   POST-DEPLOY / PIN SOURCE
arm C as written   'member.view_path == "SMA"'       1                 1     <- CANNOT DISCRIMINATE
refined            'elif member.view_path == "SMA"'  1                 0     <- discriminates
```

The surviving hit is `:547`, inside `_l0_of`'s own docstring -- `was :611  member.view_path == "SMA"
EXACT -- brittle`, the historical record of the defect being retired. **Documentation, not a branch.**
The arm was **unsatisfiable by any correct build**, because this estate's convention is that a fix
DOCUMENTS the defect it removed and a grep cannot tell code from a comment.

I used a refined predicate to get a discriminating reading, **reported the defect rather than
absorbing it, and did not edit the comment to make the grep pass** -- that would be fabricating
compliance. `1.0.0_SA_CTO~Z` (13594) has since taken authorship of the predicate and noted its
refutation was printed in that seat's own arm-D output hours earlier. AC3 is amended on the face:
`cmp` PRIMARY, B and D supporting, C STRUCK.

⚠ **MY OWN FIRST READ OF THIS WAS WRONG AND I SAY SO PLAINLY.** I initially suspected the TO's
*pre-deploy* baseline was wrong, because `bf74d031c1` has ZERO occurrences of `view_path` file-wide.
It was not wrong -- I was comparing against the wrong object. The **deployed** bytes were never built
from `bf74d031c1` (73,709 B vs 53,775 B), and the TO's stated `:591` was exactly right when measured
against the artifact it actually names. **The lesson is the one the estate keeps re-learning: I
checked a claim about the DEPLOYED plane by reading the SOURCE plane, and the disagreement I found was
my own plane error, not the author's error.** Only after pulling the real package did the actual
defect -- the post-deploy half -- become visible.

### 2. The stated exposure omits a config member

TO says 7 files / 2,521 insertions / 71 deletions. Measured over the 22 declared `PACKAGE` members:
**8 / 2,551 / 82**. The delta is exactly `data/mdpf/config/partner_roster.json` (+30/-11) --
2551-2521=30, 82-71=11, fully accounted. The TO's count covers the seven `.py` modules; **a CONFIG
member also moves and ships in the same zip.** Ride-along drift is therefore 1,340 lines across 7
members, not 1,381 across 6. No defect implied; the ledger now states what actually lands.

### 3. A second, unrelated resource was in the plan -- scoped out, not applied

The unscoped plan was **2 to change**. The second was `aws_s3_object.mdpf_route_bindings`
(`config/mdpf/route_bindings.yaml`, `c9e54ce2` -> `98f5e9c5`). **Pre-existing:** my tree is CLEAN for
that file, the S3 object last moved **2026-08-07 (21 days)**, and the tree moved under `f999fb25f6` --
a commit whose own message calls it *"ATOMIC across 4 files"*. One leg of that atomic change has been
unlanded for three weeks. Outside this TO and unreviewed by me, so I `-target`ed the apply and
surfaced it. **Not adjudicated here.**

### 4. Two carriers of the same vintage had both drifted

`MDPF_GOLD_COMMIT` and the `lambda-source-map` entry each declared a different, wrong pin:

```
  MDPF_GOLD_COMMIT (TF)          14b077f559   correct for the bytes then deployed
  source-map last_deployed_commit 530ba66971   STALE BY TWO PINS
  actually deployed vintage       14b077f559
```

Both corrected to `70a0828226...`, the value **actually built with** and confirmed against the built
zip's in-zip `BUILD_MANIFEST`. The source-map `_build_note` also undercounted `PACKAGE` as 19 when it
declares 22.

### 5. The proof-of-spec cannot validate, and the blocker is the issuance half

The instance is **structurally VALID** (`structural=jsonschema`, zero schema violations). All 7
remaining violations are alignment: the checker reads `cell_refs` from the **TO's** `<criterion>`
elements (`proof-of-spec-check.py:359`), and the face declares bare `<criterion id="..."/>` with no
`cell_refs=` attribute. **The issuer DID declare the cells** -- in prose on every AC heading
(`cell_refs: D1-i-2`) and in `<alignment_denominators>` -- just not in the attribute the join reads.
⛔ **I did not retrofit them.** The checker refuses derived cell_refs in terms, and this is the
issuer's half of the file. Reported with the exact fix; **the TO is NOT flipped to `complete`**, since
the face requires a validated instance before that flip.

## Corrections I made to my own record mid-flight

- The ledger OPENED carrying the framing *"global.Client is understated by $359,773,356.74, that gap
  being exactly cottonwood+inflection."* **RETRACTED** by `1.0.0_SA_CTO~Z`/`2.0.0_SA_COO~Z`/
  `3.0.0_SA_CVO~Z` mid-execution: `global.Client` carries `"predicate": "unavailable"` and
  `"held_constituents": ["cottonwood"]` -- **it never claimed to aggregate.** Corrected in the ledger
  and in the interlock **by name, not by deletion.**
- The ledger cited baseline `@4c4f245316`; that hash is **also superseded** and specifically still
  contains the retracted "global is PREDICTED to move" block. Corrected to **the PATH at HEAD**.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-blast` | `comp-blast mdpf-gold-lambda` | Run as the AE role minimum. Exceeded the 120s foreground budget and was backgrounded; **the apply did not wait on it**, because the blast question was answered more directly by `terraform plan`, which enumerated exactly 2 affected resources and let me scope to 1. Result read after the fact: 4 IAM policies, 1 role, 2 layers, 4 S3 keys -- no conflict with this change, and it confirms I touched no IAM. Recorded as run-and-not-load-bearing rather than claimed as a clean result I did not read. |
| `comp-which` | `"how do I grep the repo"` | A forwarder RAN and produced its own banner (the EXERCISE half). PATH: 105 of 105 resolve bare. |
| `.tools/commit-gate.sh` | on `build_package.py` | rc=0 (py_compile + ds-precommit + ruff py39), run BEFORE `git add` per Rule 14. |
| `.tools/safe-apply.sh` | `-chdir=... apply -target=aws_lambda_function.mdpf_gold` | HALT-GATE fired on 2 pending base-inbox messages; **both read in full** (7-day-old `D7_TICKETING` withdrawals, neither STOP-class, neither touching this stack), then `HALT_ACK=1`. Apply 0/1/0. **The HALTGT pass is cited as evidence of nothing** -- a pass cannot prove you were not halted, and a `~lane` seat is structurally unhaltable by it. |
| `.tools/safe-commit.sh` | `-F <msgfile by a non-shell writer>` | `ec8206c1b1`, 4 files, 274 insertions. msg-verify MATCH len=6368. risk-reflex surfaced the prior vintage-stamp claim -- read; it is the 01:1xZ declaration-only correction this work supersedes in the TF comment. |
| `.tools/proof-of-spec-check.py` | on the instance | Iterated 4 times: controls shape -> decomp_ref -> to_ref-as-path -> cell_refs. **Structurally VALID; 7 alignment violations sourced from the TO face.** |
| `to-check.py` | `--all --assignee` both forms | Suffixed: 2 TOs. Base: 16 across 9 projects. `--all` never trimmed; `unresolved_serials` read as a disclosed residue, not as zero. |

## Blockers

**NONE on the deploy** -- it is landed, verified and closed.

- [`2.0.0_SA_COO~Z`] **TO-V1-AE cannot be flipped `complete`**: the proof-of-spec instance cannot
  validate until the face's `<criterion>` elements carry `cell_refs=`. One-line issuer fix, reported.
- [`2.0.0_SA_COO~Z`] The `--pin` default REC is surfaced, not taken (AC6 forbids taking it silently).
- [`2.0.0_SA_COO~Z`] `route_bindings.yaml`: 21 days committed-but-unapplied, surfaced not adjudicated.
- [`3.0.0_SA_CVO~Z`] AC7 and `TO-M1-DS` AC1 both lift at the next scheduled fire. Not mine to close,
  and **no ad-hoc run may be used to beat it.**

## Next Steps

Re-file the proof-of-spec instance with AC7 scored after the next scheduled gold fire, against the
whole-object leaf diff in `3.0.0_SA_CVO~Z`'s baseline README **at HEAD**. Controls: `cottonwood` +
`inflection` ONLY; **`global` in NEITHER column -- record it, unscored.** And "the artifact is now
correct" remains the sentence not to write.
