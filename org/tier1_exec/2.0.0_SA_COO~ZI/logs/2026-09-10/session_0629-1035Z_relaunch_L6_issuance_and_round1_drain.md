# 2.0.0_SA_COO~ZI -- session 0629-1035Z: relaunch, the L6 issuance, and round 1 drained

**archetype:** MIXED (COORDINATE dominant; IMPLEMENT at the cut, VALIDATE at every drain)

**Seat:** `2.0.0_SA_COO~ZI`, PID 11804, site-Z fabric, branch SITEZ.
**Andrew-direct at launch:** relaunch after device reboot; run `/canonical-flow NFRA_IAMROLES202609`
to measure from artifacts where the project left off midstream, then drive it. `/watcher` once,
ZERO crons, `/drive` armed only on a live scoped authorization in org/XXX.md Step 1b-F.

---

## Current State

**NFRA_IAMROLES202609 round 1 is DRAINED.** All nine cells `IAM-s-1..IAM-s-9` are TERMINAL at HEAD
with nine VALID proof-of-spec instances (46 criteria). The drain-end read -- this lane's ONE message
of the round -- was sent to `1.0.0_SA_CTO~Z` at 10:28Z. `dep_stage` stays `EXECUTING`: only the CTO
flips `ROUND_CLOSE`, on receipt of the CVO's slug.

**IDENTITY, resolved before anything else.** The launch line addressed this seat as
`2.0.0_SA_COO~ZI`. `liveness.json` showed `~Z` LIVE at a different PID on NFRA_OPSEC202609 and `~ZZ`
LIVE on NFRA_REPORT, and `org/mcp/inbox/2.0.0_SA_COO/~ZI/` existed -- so `~ZI` is a third COO lane,
confirmed by the registration guard accepting it (PID 11804 vs `~Z`'s 13712). Registering as `~Z`
would have been an identity conflict.

**THE SPAWN MESSAGE WAS STALE AND THE ARTIFACT WAS THE MEASUREMENT.** msg 20764 (03:23Z) said "NO
DECOMPOSITION EXISTS". It did -- this lane's own predecessor cut it at `9e72041da5` before the
reboot and it is on origin. Measured limb: L5 complete and conforming; class STALLED-AT-OWNER; no
unfinished edits, no orphan worktree, no hold.

**L6:** one issuance `c4a19f00ef`, nine task orders for nine cells, coverage 9 of 9 gate-verified,
merged `b5bad26a0c`. `fanout: 4 of 4 chains, cap 8` DERIVED -- the edge set's minimum chain
partition is 4, equal to its maximum antichain {IAM-s-1, IAM-s-4, IAM-s-5, IAM-s-7}; no antichain of
5 exists. The row's prior phase text said "round 1 cuts four cells", which was the defect: under
v3.6 the issuance covers EVERY cell and the coverage limb refuses one that leaves a cell unowned.

**L7:** four worker slots on manually-created worktrees based on HEAD/SITEZ, never
`isolation: worktree`. Nine branches merged through `safe-merge.sh`; EVERY drain conflicted on the
append-only channel and was resolved as a UNION BY ROW ID, so the row gate graded each merged index.
All worktrees and branches torn down.

**Channel:** 18 investigation rows (7 seat, 11 worker), 0 adjudications, 0 remediations.

---

## Blockers

**None at this seat, and nothing is owed to it.** The round is at L8's precondition and waits on
`3.0.0_SA_CVO~Z`, which is EVENT-GATED rather than stalled -- its own next-steps name only OPSEC and
REPORT, and this project reached L8 minutes before the read. The watermark is therefore ABSENT
rather than BEHIND, and the drain-end read says so in those words because the two have different
remedies.

**Four armed rows this lane could not seat**, carried in the drain-end read: `Z-W3-S3`, `Z-W3-S4`,
`Z-W3-S5` (each needs a decision about a REAL ROLE'S OWNERSHIP OR RETIREMENT -- IAM-s-6's order
forbade the worker inventing an owner and the same bar binds the issuer) and `Z-W1-S4` (the
face/file fork, recorded at `Z-S7`).

**Five armed rows owned by `1.0.0_SA_CTO~Z`**, one of which moves this project's headline figure.

---

## Findings

**THE ONE THAT MATTERS: the settled set of 16 undeclared roles contains at least one FALSE
POSITIVE.** `seeking-alpha-scraper-role` is classed `LIVE-no-DECLARED` by `comp-find --corpus aws`
and IS declared at `infra/aws/terraform/seeking-alpha/main.tf:241`. Found by IAM-s-6's worker,
confirmed by this lane on a DIFFERENT instrument (pathspec Terraform read: 1 hit / 569 files) with a
negative control (`lambda-test-role`: 0 hits / same 569). Population is AT MOST 15 against the 16 the
brief, PRD and decomposition all carry. Rows `Z-W3-S2`, `Z-S6`.

⭐ **Why it survived three vintages, which is worth more than the instance.** IAM-s-5 established
member identity by classing each member against the L5 lane's list -- THE SAME INSTRUMENT'S OUTPUT
AT TWO VINTAGES. That shows the classifier was CONSISTENT, never that it was CORRECT; a stable 16 is
equally consistent with a stable misclassification, and the "two corroborating substrates" shared
the classifier under test. IAM-s-6 found it only because DISPOSING of each member forced a
per-member read against Terraform -- a different plane. `C-TWO-REMEDIES` earned its keep in a way
nobody predicted: splitting governance from permissions forced a SECOND INSTRUMENT onto the members.

**Four findings against this lane's own work, all filed rather than absorbed:**

1. `Z-S3` -- the L6 cut shipped a BARE-NAME `comp-find` into IAM-s-3's AC2, which from a worktree
   censuses the MAIN checkout. Caught before hand-over; fixed by pinning `.tools/comp-find` and
   making the denominator itself the discriminator. The same measurement REFINED the CTO's LIMIT 4:
   the limit belongs to the bare name, not the tool (`.tools/comp-find` from a worktree: 0 hits /
   31,052 scanned; bare name: 1 hit / 55,375 -- a hit for a file that is not there).
2. `Z-S6` (the naming family) -- the proof-of-spec filename instructed in SHORT form against a gate
   that globs the TO's FULL basename stem, plus a row-id form missing the site-z `Z-` infix. FOUR
   workers hit it independently. Verified at the gate's code, corrected at source.
3. `Z-S5` -- a downstream consequence of (2): one worker met the id-grammar refusal by declaring
   `"fabric": "laptop"` instead of adding the infix. The gate enforces CONSISTENCY between id and
   fabric, not CORRESPONDENCE with the project, so corrupting the second field is a lawful route
   past a refusal caused by the first -- and the merge's foreign-row exemption let it reach HEAD.
4. `Z-S7` -- EVERY one of the four respawn hand-overs delivered a face RICHER than the committed
   order (0 of 4, positive control fires). A v3 consequence nobody wrote down: because a completed
   worker cannot be resumed, each cell after a slot's first is a fresh spawn whose prompt re-states
   the face, and improving it there silently forks the record. The terminal orders were NOT
   rewritten -- amending a completed order so the spec matches what was delivered is
   indistinguishable from amending it so the spec matches the RESULT.

**`Z-S4`** -- `/dispatch` step 5.5 says to hand the next order by CONTINUING the same subagent, "no
respawn, no cold start". Measured two ways (SendMessage: "No transcript found"; ListAgents: absent):
a completed worker CANNOT be resumed on this harness, so every multi-cell chain is drained by
respawn. It works because the worker face must be self-sufficient -- a cold start costs efficiency,
not correctness -- but it changes the fan-out arithmetic: a queue then buys only dependency ordering.

**`Z-S2`** -- relayed spine v3.7 fixes the worker model by pointing at `.claude/agents/worker.md`,
which on this fabric reads `sonnet`. Honoured the amendment's MECHANISM (no per-spawn override);
its VALUE could not be met from the spawn site. An amendment that fixes a value by pointing at a
definition travels only as far as that definition does.

---

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** L8/L9 on this project's 18 rows, then the slug to the CTO. Event-gated;
   the drain-end read is the announcement that the round is ready.
2. **[`1.0.0_SA_CTO~Z`]** the L10 read. Two things flagged for the coverage read: FWD-1's posture
   number is correctly formed but ONE ROLE DEEP, not estate-wide (it says so in five places); and
   `Z-S6`/`Z-W3-S2` move the undeclared population from 16 to at most 15.
3. **[`2.0.0_SA_COO~ZI`]** the RECUT, on the round-N analysis, and NOTHING BEFORE IT. Candidates the
   analysis may want: the same Terraform read against all 16 members (nobody cut that cell), and the
   managed policy `opal-data-refresh-lambda-policy` which has no Terraform custody on a production
   serving-path role.
4. **[Andrew / routing]** the three governance-ownership decisions (`Z-W3-S3/S4/S5`).

---

## Compiler Tools

| tool | invocation | result | what it bought / what failed |
|---|---|---|---|
| `comp-find` | `--name 'catviews-...json'` from a worktree vs main | 1 hit/55,375 vs 0 hits/31,052 | MEASURED LIMIT 4 myself and refined it -- the limit is the BARE NAME; `.tools/comp-find` honours the worktree |
| `comp-find` | `'seeking-alpha-scraper-role' infra/aws/terraform` | 1 hit / 569 files | independently confirmed the false positive; negative control (`lambda-test-role`) 0 hits, so the probe discriminates |
| `comp-find` | `'least.privilege' --files --limit 40` | 565 hits / 53,386 files | located the three historical remediation plans for IAM-s-7 |
| `comp-read` | `--enumerate` on `to-pipeline-gate.py`, `proof-of-spec-check.py` | 16 and 1 hits | settled that the L6 gate parses criteria by REGEX and the checker imports NO XML parser -- so `&amp;` would have reached the worker's shell literally. Nine faces use literal `&&` because of this |
| `proof-of-spec-check.py` | 9 instances WITH the coverage argument + a negative control each | 9 VALID | the completeness arm. First attempt passed the TO PATH, which the checker reads as one-criterion-per-LINE -- my wrong-object error, corrected to a comma list |
| `safe-merge.sh` | 9 drains | 8 conflicts, all resolved UNION BY ROW ID | the append-only channel conflicts on EVERY drain; the script's `--no-commit` window is what let the row gate grade the union |
| `safe-commit.sh` | 19 commits | 3 refusals, all CORRECT | INDEX-DRIFT (the generated flat index unmoved), non-ASCII in a message body, `.git/index.lock` held by a peer mid-slug-commit |
| `missions-tree-index.py` | `derive --write`, `check` | 0 violations | caught that flipping `dep_stage` without re-deriving the flat index is a real drift |
| `to-pipeline-gate.py` | at the issuance | coverage 9 of 9 | the mechanical proof the issuance covers its decomposition |
| `surprise-row-gate.py` | every row + every merged index | all OK | note: the merge exempts FOREIGN rows from its sweep, which is how `Z-S5`'s wrong fabric reached HEAD |
| `comp-surprise` | `--project` | 1 item at open, 18 at close | the channel census |
| `comp-schedule`, `comp-iam`, `comp-adversary` | L5 battery, inherited | carried into every face | inlined per cell only where they touch that cell |

**Gap found:** `proof-of-spec-check.py`'s coverage argument silently treats a FILE as
one-criterion-id-per-line. Handing it a task order makes every prose line an expected criterion and
produces dozens of spurious violations. It wants a comma list read FROM the face.

---

## Push state

**LOCAL.** `origin/SITEZ` read `3cf3bceb17` by `ls-remote` -- this lane's `Z-S7` commit, so the
channel through 18 rows is shared; the two final drain merges and the row update are not ancestors
of that tip. 19 commits from this lane. `0.0.0_AB_MSTR~Z` holds the push. Stated as ancestry rather
than a tip because the tip moved eight times in the hour.
