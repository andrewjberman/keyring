# IRPT_BCKEND registry steps 2-3 landed for the CTO, and R-85's pending rename applied

**archetype:** MIXED (VALIDATE + IMPLEMENT)
**Seat:** `4.0.0_SA_CRO` (base). **Window:** 2026-09-19 ~02:30-03:08Z. **Spawned by:** `1.0.0_SA_CTO`,
one task.

## Current State

Both acts are landed, verified from the repository, and reported.

1. **`14ef431d5a` on CLOUD -- ON ORIGIN** (`origin/CLOUD` 1057a4f113 at the last `ls-remote`).
   `infra/logic/registry/scopes.json` 4/2 and `infra/logic/registry/exemptions.json` 40/0 in ONE commit
   (branch commit `845343f925` in worktree `wk-cro-irpt-registry`, drained via `safe-merge`, worktree and
   branch removed). This is the edit `1.0.0_SA_CTO` could not commit -- lane `PLATFORM_LOGIC_DOCS` names that
   seat by EXCLUSION and no override was taken. `1.0.0_SA_CTO` accepted it whole (98111) after verifying the
   landing independently.
2. **`dfb2930bce` on CLOUD -- LOCAL.** R-85's rename `BOTH-PRESENT` -> `CLAIMED-AND-MEASURED`, 9 occurrences
   across 8 lines in `docs/briefs/d14-lgctfm-pipeline-walk-brief-20260918.md`, confined to O9 and W14.

The push for `dfb2930bce` is `0.0.0_AB_MSTR`'s. No task orders held. No crons. Watcher task `b8lhb5jzd`
live (third arm this session -- the Monitor caps at 30 minutes and was re-armed on each expiry).

## What was done, and the two things worth keeping

**The atomicity requirement was re-derived, not accepted on report.** The handoff said the flip without
`bucket_managed_by` drops both rows out of both branches of the selector at
`s3-lgic-firm-buckets.tf:96-102` and costs a 10-resource DESTROY. Rather than re-run the CTO's instrument
(a `terraform plan`), I transcribed the HCL predicate into Python and evaluated it as a DISCRIMINATING PAIR
over the HEAD blob and over the edit: PRE `{cottonwood, inflection}`, POST `{cottonwood, inflection}`,
delta NONE. NEGATIVE CONTROL, the flip without the field: EMPTY, both rows dropped. The predicted destroy
reproduced. Grain confirmed separately -- the root reads THIS file and no other
(`:65 jsondecode(file("${path.module}/../../../logic/registry/scopes.json"))`).
This mattered more than it looked: the handoff had already filed that `validate()`'s scopes loop never
computes `set(row) - <closed set>` (`lib/opal_naming.py:322-389`), so **a typo in the new field name would
have passed `validate` identically, rc=0 and all.** `rc=0` could not have told me the edit worked.
One citation correction landed against the CTO's own text and it recorded it as mine: the selector's `for`
block spans `:96-102`, not the `:97-100` carried in the handoff and two messages.

**A near-miss on my own arm, which is the more useful entry.** R-85 justified the rename on a census:
`BOTH-PRESENT` is already taken, meaning TWO PROVENANCE COLUMNS EXIST ON A TABLE, in
`0.4.0_DS_ClientPlatform`'s proof-of-spec deliverables -- "five CONFIG hits dated 2026-08-11" beside a list
of exactly FOUR parentheticals. I re-measured with the narrower literal `provenance_cols=BOTH-PRESENT`,
unscoped, 168,465 files: **CONFIG = 4.** Four measured, four listed, five claimed. I had the correction
drafted. The BARE token `BOTH-PRESENT` over 168,466 files returns **CONFIG = 5**: the fifth is
`PROOF_OF_SPEC_P1_COT_PARQUET-WRITER-FORMAT_20260811.json:53`, which writes `provenance BOTH-PRESENT:`
with no `provenance_cols=` prefix. `comp-read --enumerate` on it reports 1 hit, 0 whole / 1 substring, and
WARNs that an anchored probe returns ZERO against that file.
**R-85's count was right and my instrument was the defect** -- a probe scoped NARROWER than the sentence it
was grading, carrying a real printed denominator and therefore reading as MEASURED. It would have survived
any re-run of itself. What caught it was running the bare-token census BESIDE the anchored one instead of
in place of it; and the four-item list in R-85 is what made me look twice, so the ruling's own enumeration
protected its number. Flagged back to the CTO, not edited: the ruling's QUOTED KEY covers four of the five,
so anyone citing that sentence as the pattern to grep gets four.

**Held fences.** `0.0.0_AB_MSTR`'s 23:07Z HOLD (98075) bars this seat from writing under
`infra/logic/registry/` on the `opal-data-harvest` placement. Nothing was started on it -- this seat came up
after both 98072 and 98075 landed -- so the withdrawal is clean with no partial work anywhere; answered to
MSTR, along with the per-side hunk-range read it said it would want at the next `/integrate` (both hunks at
`:123` and `:162` sit INSIDE existing rows and append nothing at the array tail, so a tail-appended SITEZ
row should union mechanically). The 16-principal admit set of `opal-data-49financial` was NOT mirrored onto
the new buckets: operator identities only, and each new row's `reason` states on its face why the census
ground does not carry across a firm boundary. The five DS proof-of-spec JSONs keep their own prior use of
the colliding token -- the collision is resolved by moving the NEWER claimant, not by rewriting another
seat's records.

**Not done and not attempted:** the lockout. Both buckets stay unreachable to every identity this estate
holds until the account ROOT runs `delete-bucket-policy` -- Andrew's act at a console (step 4). No
`terraform apply`, no `aws` write, no ledger edit. IB-rte-3 stays OPEN/RED and W3-S45 stands: 4 TAINTED
resources, so step 5's re-apply REPLACES them and its never-widen sign-off must name those four as its
blast radius.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | `"how do I grep the repo"` | forwarder RAN | Step A.3 exercise; 104 of 104 comp-tools resolve bare |
| `comp-read --enumerate` | `s3-lgic-firm-buckets.tf` / `lgic_registry_scopes` | 2 hits / 171 lines | found the `jsondecode(file(...))` load at `:65` -- the GRAIN check that the tf reads the file I edited |
| `comp-read --enumerate` | the brief / `BOTH-PRESENT` | 9 hits / 419 lines, 46 sections | pre-rename denominator; 7 whole + 2 substring, all PROSE |
| `comp-read --enumerate` | the brief / all four coverage tokens | 20 hits, 18 whole + 2 sub | post-rename verification, other three tokens intact |
| `comp-read --enumerate` | `PROOF_OF_SPEC_P1_COT_PARQUET-WRITER-FORMAT_20260811.json` | 1 hit, 0 whole / 1 SUB + WARN | **the file that broke my own count** -- the WARN ("an anchored probe would report ZERO") is exactly the failure mode I had just committed |
| `comp-find` | `provenance_cols` `--band CONFIG --all` | 20 hits / 168,465 files, CONFIG=4 | the UNDERCOUNT; pattern narrower than the claim |
| `comp-find` | `BOTH-PRESENT` `--files --all` | 48 hits / 168,466 files, CONFIG=5 | the correct denominator; the fifth member surfaced only here |
| `comp-pulse diff` (risk-reflex, in-gate) | both commits | PRESENT_WITH_ZERO_RESULTS | 2 files vs 1,662 danger nodes; 1 file vs 1,906 |

**GAPS FOUND, both real and both cost a call:**
1. `comp-find 'BOTH-PRESENT' --files` unscoped **timed out into the background and completed rc=0 with ZERO
   BYTES of output** -- the catalogued false-zero. It reads identically to a clean absence. Treated as
   UNANSWERED and re-run with an explicit long budget, which returned 48 hits.
2. `comp-find 'provenance_cols=BOTH-PRESENT' -- 'org/**'` returned `0 hit(s) across 0 file(s)` -- a pathspec
   that matched NOTHING, which per CLAUDE.md Rule 21 is OUT-OF-CORPUS and not absence. Dropping the pathspec
   was the fix. Both are known traps; both were hit anyway, in one session, by a seat that had read them.
3. The rail aborted a compound Bash call whose LAST segment was a gated `comp-read` pipe -- so the python
   rename in the FIRST segment never ran. Caught by reading the numstat rather than the exit status, exactly
   as Rule 21's abort clause says to.

## Blockers

None at this seat. `dfb2930bce` awaits `0.0.0_AB_MSTR`'s push -- not a blocker, a different seat's limb. The
`IRPT_BCKEND` lockout awaits Andrew at a console; the `opal-data-harvest` placement is held by MSTR pending
Andrew's answer on the tenancy-vs-doctrine fork.

## Next Steps

1. [`1.0.0_SA_CTO`] Whether `SELF_DRIVE_LGIC_RULINGS_20260917.md:3217` gets the same rename, and whether
   R-85's quoted key (`provenance_cols=BOTH-PRESENT`, which covers four of the five colliding hits) is worth
   widening in the ruling's text. Also carrying the `validate()` field-closure gap as its own carrier.
2. [Andrew] `delete-bucket-policy` at the console on `opal-data-inflection` and `opal-data-cottonwood`
   (IRPT_BCKEND step 4); and the harvest tenancy-vs-doctrine fork MSTR has re-asked in words.
3. [`4.0.0_SA_CRO`] Event-driven: the brief half of any L4-R the notifier routes here; re-arm the watcher on
   each expiry.
