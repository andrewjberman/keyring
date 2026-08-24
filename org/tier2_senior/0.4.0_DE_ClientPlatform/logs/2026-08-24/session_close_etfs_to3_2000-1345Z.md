# SESSION-CLOSE -- 0.4.0_DE_ClientPlatform -- ETFS_POSITIONING TO-3 delivered, seat at rest

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~2000Z -> 2026-08-24 ~1345Z (one seat across the wall-clock gap)
**closing under:** Andrew-direct 2026-08-24 ~13:3xZ, fabric-wide -- *"everyone needs to close out
wherever theyre at to a safe position from which to restart with fresh context"*

---

## CURRENT STATE -- THE HANDOFF FOR A FRESH SEAT

### Nothing is half-landed. Nothing is owed by this seat.

| plane | state | verification primitive |
|---|---|---|
| portal | `DEV @ d43b88c5124c0b6a8ca0db49a1a8bb5826d0ea1c` | `git -C portal rev-parse HEAD` |
| portal remote | **`origin/DEV` == `d43b88c5`** (my HEAD is pushed) | `git -C portal ls-remote origin refs/heads/DEV` |
| portal tracked-dirty | **0** | `git -C portal status --porcelain \| grep -vc '^??'` |
| workspace | my last commit `a030c2c2a8` **IS on a remote branch** | `git branch -r --contains a030c2c2a8` -> 1 |
| origin/PROD | `8a96c916` = v2.1.164, **UNCHANGED** -- no production write | `git -C portal ls-remote origin refs/heads/PROD` |

⚠ **The workspace tree shows ~53 tracked-dirty files. NONE ARE MINE.** Shared worktree, other
seats' work in flight. Do not stage, stash or clean them -- `git stash` parks every seat's files
and the shared-worktree gate correctly refuses it.

### TO-3 is COMPLETE and validated

`org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ETFS_POSITIONING.TO-3.*.md` -> status
BUILD COMPLETE, cell-level. proof-of-spec **VALID rc=0, 6/6 rows, 0 violations**, re-run
independently by COO at their own seat. Instance:
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ETFS_POSITIONING.TO-3_PROOF_OF_SPEC.json`

Re-verify with (positional; **check rc, never the output string** -- the usage banner contains
both verdicts' vocabulary):
```
python .tools/proof-of-spec-check.py \
  org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/ETFS_POSITIONING.TO-3_PROOF_OF_SPEC.json \
  ETFS-TO3-AC1,ETFS-TO3-AC2,ETFS-TO3-AC3,ETFS-TO3-AC4,ETFS-TO3-AC5,ETFS-TO3-AC6
```

### The four portal commits, in order, and what each is for

| commit | purpose |
|---|---|
| `ee90fa8e` | the Models<->ETFs flip + all 12 in-plane membership sites derived from one declaration |
| `a60b558f` | ETF-unavailable notice made CAUSE-AGNOSTIC (it named a blocker that moved twice in an hour) |
| `a7ff6dd4` | added a percent->fraction weight conversion -- **SUPERSEDED, do not resurrect** |
| `d43b88c5` | **deletes** that conversion; unit contract documented instead |

Net effect of `a7ff6dd4`+`d43b88c5` on `etfAdapter.ts` vs `a60b558f`: **the doc comment only.**
Verified by token census (0 at HEAD, positive control 5 at `a7ff6dd4`) and by diff; DT
independently re-ran both at their seat.

### Premises a fresh seat should NOT re-derive, with the primitive that re-checks each

| premise | primitive |
|---|---|
| ETF holdings `weight` is a **FRACTION** (book sums to ~1.0); `aum` is **MILLIONS**; `active` is **int 0\|1** | sum a whole book from `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json` |
| `allocation`/`management` are **PERCENT** in BOTH artifacts (asymmetric with weight, deliberately -- regularising breaks Models parity) | same object, compare to `json/positioning/positioning_data.json` |
| Models mode renders byte-identically pre/post TO-3 | `node portal/.frontend-dev/testing/ac3-models-dom.mjs <out> --fixtures <models-fixture> --port <p>` |
| the ETF route is LIVE; the artifact exists | `aws s3api head-object --bucket opal-data-portal-v2 --key platinum/etfs/positioning_data.json` |

**The AC3 oracle is COMMITTED** at `portal/.frontend-dev/testing/ac3-models-dom.mjs` precisely so
a verifier re-runs the byte-diff instead of trusting this log. Fixture it with the LIVE artifact --
an unfixtured capture on a dev server with no data is byte-identical to any other empty state, and
**a capture that cannot fail proves nothing.**

### Open items -- all with named owners, none owed by me

| item | owner | state |
|---|---|---|
| PROD promote of v2.1.165 | **Andrew** (word), DT (cut), MSTR (push) | HELD pending his ADVI ruling; merge staged at `a239e4a9`, 0 remote branches |
| DIVZ/IDVZ empty allocation bars | DS, via TO-4 | DATA question, not portal -- producer flips `book_only`->`full` with no code change |
| gzip/ContentEncoding contract line (S9) | AE | ARMED; current artifact conformant (`ContentEncoding` none), trap remains for the next producer |
| `aumByModel[code] \|\| 0` partial-aggregate | unassigned | DOCUMENTED, NOT REMEDIATED -- behaviour deliberately unchanged, `missingAum` exposes the drop |
| deploy-ledger `stranded` conflation | COO | prior art found at **LD-0360:37-38**; MSTR verified at source |
| D1_CATVIEWS TO-D1d (territory (c)) | COO decomps; DE-class executes | UNCUT. Three PRD premises re-measured today and HOLDING (below) |

⚠ **DT's staged-refs trap, recorded so it cannot be tripped:** local `refs/heads/PROD` is
INTENTIONALLY at `a239e4a9` and the ephemeral worktree is INTENTIONALLY live. Any other promote
must run `/prod-deploy` Step 3 (update-ref from origin) and `worktree prune` FIRST or it silently
bases on that staged merge. v2.1.114 dry-run-pollution class.

### D1 territory (c), parked with state written

PRD s.5.2's portal evidence RE-MEASURED 2026-08-24 -- **all three hold**, so the decomp may rest
on s.5.2 as written rather than treating it as an unverified vintage:
- `comp-cache collisions` -> "16 shared key(s); 0 with a TYPE MISMATCH" (unchanged; R8 holds)
- `comp-find -i "category-views|category_views" portal/src/` -> **0 hits / 417 files** -- a
  MEASURED zero. **One spelling pair; a floor, not a proof of absence.**
- `ModelPortfolios.tsx` -> **2,471 lines exactly**, last touched `46f127eb 2026-08-19T17:00:53-04:00`
  (i.e. unmoved since the PRD measured it)

**NOT run, deliberately** (close-out order says do not start anything new): the s.5.2 TO-time
mandate (`comp-transform schema-check ModelPortfolios`, `comp-blast`) and any cell-candidate survey.
**Load-bearing clause for whoever takes TO-D1d:** s.4.3's error case is a FEATURE-GATED FALLBACK --
absent `category_views` renders today's view, no hard dependency during rollout -- which means the
portal leg CAN land before the gold projection, decoupling TO-D1d from TO-D1c if COO wants it.

---

## What this session actually delivered

The flip, and **twelve** membership sites derived from one declaration where the TO named five.
The five were correct **for the pattern that found them** -- I positive-controlled that before
disputing anything -- but `comp-find -i "'UST'"` is quote-delimited and structurally cannot match
bare object keys, a fixed-length array, a `repeat(N)` count, or a `.filter()` that silently drops
unknown members. **Fixing only the five would have shipped, and the census would have re-confirmed
it clean.**

Andrew's own catch (NVDA at 994.99%) exposed the deeper one: **CONTRACT v1 fixed the FIELD NAMES
and was silent on UNITS.** DS fixed it in the publisher; I fixed it in the adapter sixty seconds
apart; **the composition was the defect, not either fix** -- both landing would have rendered every
weight 100x too SMALL, which is the version that looks plausible and gets believed. Caught only by
re-pulling the artifact before committing a fix I had already verified by render.

## Recurring lesson across every one of them

**An instrument reporting cleanly about the wrong property.** A quote-delimited census that cannot
see an unquoted fact. A schema check that asks whether a field is present, not whether it is right.
A ledger predicate that cannot tell never-started from half-landed. A type system where `number`
and `number` are the same type whether one is a percent and the other a fraction. Every one passed;
every one was wrong; **not one was caught by care** -- each by a denominator, a control, or another
seat going to look.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `-i "'UST'" portal/src/`; `-i "never-started" org/`; `-i "category-views..."` | 31/415 DEF=11; 9/14,920 across six seats; 0/417 -- every count given with its denominator |
| `ui-smoke.mjs` (/frontend-dev) | `--fixtures`, `--click`, `--fail` | 8 screenshots rendered and READ; found all render defects, incl. two no grep could see |
| `bun run typecheck` | `tsc -b --noEmit`, **mutant first** | rc=0; mutant rc=2. Bare `tsc --noEmit` compiles an EMPTY file set here |
| `proof-of-spec-check` | positional, 6 ids, **rc without a pipe** | VALID rc=0; COO re-ran independently |
| `comp-cache collisions` | portal RQ keys | 16 shared, 0 type mismatches |
| `.tools/deploy_ledger.py` | read at source (DT's refusal) | the HELD precondition is a deliberate anti-escape-hatch |

## Blockers

**None at this seat.** The PROD promote is Andrew's word, not a technical blocker. Nothing is
staged, half-applied, or waiting on me.

## Closing position

Seat is SAFE TO RESTART FROM FRESH CONTEXT. Everything load-bearing is in the record above with
its verification primitive; nothing depends on this session's memory. **HOLDING** per the
close-out order -- no further work started.
