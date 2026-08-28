# 0.7.0_AE_CloudOps~Z -- D1_CATVIEWS publisher gap + reland/refire chain (2132-2240Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE

## Window

2026-08-28T21:32Z (registration) -> 22:40Z. First log of this session; no prior entry to delta from.
Six commits, all lane-authored. Roughly 25 inbound MCP messages handled, 9 substantive dispatches out.

## Scope

Seated by launch brief on D1_CATVIEWS. **Scope CORRECTED by the issuer mid-session** (`2.0.0_SA_COO~Z`
14090 s4): the brief named publisher + promote; the promote is a DT lane (`/prod-deploy` frontmatter
halts non-DT at Step 0, verified at source). Final scope = `CATVP-c-1..c-3` (publisher enumeration)
plus chain steps 2 and 3 (reland + refire).

## Part 1 -- CATVP-c-1..c-3, the publisher enumeration gap

**THE DEFECT.** `opal-assets-mdpf-portal-publisher/lambda_function.py:83` carried
`RULED_TYPES` as a literal 3-tuple frozen at the 2026-08-06 capability snapshot. `category-views`
became the 4th artifact type on 2026-08-28 (first gold write 13:31Z); the live function was last
built 2026-08-07 at pin `c0902245b0`, so **its completeness frame predates the artifact entirely --
it is not stale about a decision, it never had one to make.** `category-views` was never in
`expected`, so it could never appear in `missing_pairs`: if all four objects had vanished,
`all_present` would still have returned True. Served but ungoverned.

**WHAT I DECLINED.** The decomp's own `CATVP-c-3` said *"prefer derive-from-manifest."* If that meant
the per-run gold `_manifests/` object, it re-arms the defect one layer up: a producer that stopped
emitting a type AND stopped declaring it drops `expected` and `derived` together and reads green. A
run manifest is a producer SELF-REPORT; expectedness must not derive from the thing being checked.
Declined in writing to the issuer before building (14129).

**WHAT LANDED @`84fda0fd04`.** The literal is DELETED, not incremented -- bumping 3 to 4 re-arms the
trap for the 5th type. The axis is now derived at BUILD from the producer's own
`mdpf_gold_consolidator.ARTIFACT_TYPE_SCOPE_SET` by AST over `git show <pin>:<path>` (no import, no
execution, so the consolidator's boto3 sibling graph stays out of the zip), emitted as a hash-tied
`artifact_types.json` at zip root. Same transport as the roster, for the reason `build_package.py`
already states in its own words. **No S3 leg added** -- CTO 230319Z forbids the second authority.
Both authorities survive, composed not merged: the ROSTER stays the sole SCOPE authority (D8), the
producer owns only the TYPE axis, carried as per-type `scopes_excluded` computed at build from its
own tuples. Fails closed on both sides; an unreadable axis is UNKNOWN-loud, never a literal fallback.

**STATE: COMMITTED AND EXERCISED, DELIBERATELY NOT APPLIED.** I put the sequencing fork to the issuer
rather than taking it, and recommended AFTER while arguing against my own cell -- CVO's 21:3xZ
narrowing had already established no publisher change is required for the corrected values to reach
platinum, so applying tonight buys zero on the deliverable and spends risk on the path that must not
wobble. `2.0.0_SA_COO~Z` ratified (14197).

## Part 2 -- chain steps 2 and 3 (reland + refire)

Authority: Andrew-direct verbatim *"yes reland once all fixes are in"* (relayed 14134). GO from
`1.0.0_SA_CTO~Z` (14277) and issuer GO from `2.0.0_SA_COO~Z` (14289).

### Deployment sequence

```
  22:15Z     ledger OPENED and committed BEFORE the delete            0b08925e00
  22:16Z     PRE-FIRE CONTROL (condition of the GO): re-enumerate + diff vs authorized 16
               MANIFEST  live == authorized  _manifests/2026-08-27/20260828T211849Z.json
               KEY SET   authorized 16 | live 16 | diff -u IDENTICAL, 0 added, 0 removed
  22:16:5xZ  WINDOW OPEN broadcast, then  mdpf_refresh.py --reland --confirm
               16 dated gold keys DELETED (reland DELETES ONLY; rebuild is step 3)
  22:17:01Z  mdpf_refresh.py gold  (chained, NOT separated by a report)
  22:17:37Z  mdpf-gold-lambda   {"status":"green","errors":[],"a4_objects_built":16}
             run manifest ...20260828T221739Z.json   conflicts=0     <- WINDOW CLOSED
  22:17:40Z  mdpf-accrual-trigger  SSM 9124d754 -> Success
  22:17:55Z  publisher  published 18, unchanged 0, failed [], missing_pairs []
  22:19Z     ledger CLOSED                                            fe0e49f793
```

Window duration ~40s. Steps chained deliberately: the state where 16 gold keys are deleted and step 3
has not run is the one state tonight worse than doing nothing.

### Verification (ACTUAL output, binding un-piped form per 14315)

```
  python verify_step3_served_category_views.py > accept_final.txt 2>&1 ; rc=$?
  rc captured on the VERY NEXT token: 0

  SCORED 11 PASS / 0 FAIL over 11 assertion(s); 0 NA_BY_DATE; 0 scope(s) INDETERMINATE
  VERDICT: ACCEPT

  global       SMA.aum 22794766.25         absent_reason ABSENT   Client.aum 267632047.22
  49financial  SMA.aum 22794766.252499998  absent_reason ABSENT
  cottonwood   SMA.aum 0.0                 absent_reason PRESENT      <- Direction B held
  inflection   SMA.aum 0.0                 absent_reason PRESENT      <- Direction B held
  L2 members carrying aum: 8 of 15   (0 of 15 pre-reland)
  body as_of 2026-08-27 on all four, read from the BYTES (platinum keys are undated)
  CONTROL conservation 267,632,047.22 + 22,794,766.25 = 290,426,813.47 -- PRINTED, NOT SCORED
```

All four stop conditions checked, none tripped. NOT cited as acceptance: `mdpf_refresh`'s own VERIFY
block (it printed PASS x4; reads 1 artifact type of 4 on timestamps only) and `LastModified` (already
advanced tonight for an unrelated reason).

## Findings raised

1. **Authorized by enumeration, executed by live resolution.** `latest_run_manifest()` resolves the
   delete set at CALL time via `max(LastModified)`; Andrew's word named a FROZEN enumeration. Two
   objects, one name. Armed the pre-fire diff as the control; it was adopted as a condition of the GO.
2. **`mdpf_refresh`'s VERIFY block is not acceptance.** `:104-105` reads ONE artifact type, hardcoded;
   `:279-283` scores as_of + write recency, never a value. It passes HONESTLY while answering a
   different question. RULED binding by `1.0.0_SA_CTO~Z` (14212).
3. **The RULED conservation criterion is not discriminating.** 14212 called it "the one that
   matters... cannot pass by accident"; measured, it PASSES on the un-relanded plane
   (290,426,813.47 + 0.00) with nothing done -- the fix reallocates between two siblings, so a
   criterion on their SUM is invariant across the change it exists to accept. Same defect as PRD AC4
   one rung along. Demoted to an unscored control, not deleted.
4. **Corrected a coverage mislabel.** 14248 listed my instrument as GOLD-side; measured at source it
   is PLATINUM, same bucket/keys/client as the CTO's. Two of three claimed independence axes were
   false. The real map: gold had ONE instrument, platinum had THREE -- and gold is the plane the
   reland acts on. `1.0.0_SA_CTO~Z` accepted and re-pointed its instrument to cover both planes.
5. **The window my act creates.** `reland()` DELETES ONLY, so between steps 2 and 3 gold is ABSENT,
   not wrong -- any cross-plane read there is INDETERMINATE by construction. Announced WINDOW
   OPEN/CLOSED as the owner of the state.
6. **`_provenance.trigger` is `"manual"`, not `"adhoc"`.** `:1398` writes `trigger.get("kind")` into
   the ARTIFACT while `:1148` writes the whole dict into the RUN MANIFEST, so `detail.source` never
   reaches the artifact. A ratifier asserting `"adhoc" in trigger` against the artifact would have
   REFUSED A CORRECT RELAND. Sent ahead of my full report because CVO was scoring; independently
   confirmed by `1.0.0_SA_CTO~Z` (14349) and `2.0.0_SA_COO~Z` (14340).

## Defect in my own work, caught by a peer

My step-3 instrument asserted `SMA.aum == 22,794,766.25` UNCONDITIONALLY in its first two commits.
That figure is MARKET-VALUED (~$170-250k/trading day). `3.0.0_SA_CVO~Z` (14264) found it in their own
ratifier and then CHECKED THE OTHER TWO INSTRUMENTS rather than only fixing theirs. Demonstrated
against my own pre-fix commit `b924645c54`: on a correct 2026-08-31 build it returns 2 FAILs, rc=1 --
**it would have failed a correct build.** Fixed @`a4e16bc65f` with a two-track split (STRUCTURAL
scored at every as_of; LITERAL only at `LITERAL_AS_OF`, else `NA_BY_DATE`, excluded from rc both
directions) plus CONTROL B committed alongside, proving a correct later build is ACCEPTED.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | A.3 exercise probe | PASS | forwarder RAN (produced its own banner); 105 of 105 resolve bare |
| `comp-aws` | `comp-aws opal-assets-mdpf-portal-publisher` | FAIL | rejected -- it takes a subcommand (derive/score/snapshot/...), not a resource name |
| `comp-estate` | (cited, not re-run) `--resource category-views` | PASS | `3.0.0_SA_CVO~Z`'s corroborating instrument for `CATVP-c-2`: no chain references it |
| `.tools/commit-gate.sh` | 6 invocations across 5 files | PASS | caught 2 non-ASCII (U+26D4) I introduced; fixed rather than accepting the WARN |
| `.tools/safe-commit.sh` | 6 commits | PASS | one initial FAILURE, see gap below |

**What worked:** `commit-gate` flagged non-ASCII the gate treats as WARN-only. I fixed it anyway --
CLAUDE.md bans non-ASCII in production code regardless of whether the gate blocks, and complying with
the gate rather than the rule is a banked failure mode.

**What failed:** `comp-aws <name>` -- I guessed the CLI shape instead of reading `--help` first. One
wasted call; fell back to native `Grep` which the rail nudges-and-proceeds on.

**Gap found:** my first `safe-commit` invocation used `-F <(printf ...)` -- a SHELL-BUILT message
file, which CLAUDE.md 14a explicitly forbids (F-010 fires at file BUILD, not just at the commit call).
It did not land. **I caught it only because I ran `git log` afterwards instead of trusting the
truncated tool output** -- the tool's own reminder says exactly that: a tool stdout line is the TOOL
DESCRIBING ITSELF; `git log` is the REPOSITORY ANSWERING. Re-authored via the Write tool and
committed cleanly.

## Files Modified

See commit messages: `84fda0fd04`, `51d0462ede`, `b924645c54`, `a4e16bc65f`, `0b08925e00`,
`fe0e49f793`. Extra context on two:

| File | Note |
|---|---|
| `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/build_package.py` | new `extract_artifact_type_axis()` -- AST, fails closed and loud on every unrecognised shape, naming the symbol |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/verify_step3_served_category_views.py` | executor-side acceptance; NAMES `3.0.0_SA_CVO~Z`'s ratifier PRIMARY in its own docstring |

## Blockers

**NONE at this seat.** Nothing is waiting on me.

**Owned elsewhere, listed so they are not read as mine:**
- [`2.0.0_SA_COO~Z`] The `CATVP-c` publisher apply -- committed at `84fda0fd04`, NOT applied by that
  seat's ruling (14197). It needs a future apply window; it is not abandoned, it is deferred.
- [`3.0.0_SA_CVO~Z`] Offered for absorption: the L2 member-`aum` leg and the conservation demotion
  from my instrument. That seat kept both instruments running side by side instead; my file stays.
- [`1.0.0_SA_CTO~Z`] Whether PRD AC1's literal text is amended for Monday. My instrument prints both
  readings, so no verdict waits on it.

## Current State

`opal-assets-mdpf-portal-publisher` is UNCHANGED on the live plane -- still pin `c0902245b0`,
LastModified 2026-08-07T03:40:42Z, still structurally blind to `category-views` (it reported
`unexpected_pairs: [all four]` on tonight's 22:17:55Z run while serving them correctly). The fix for
that is committed at `84fda0fd04` and awaits an apply window.

The SERVED plane is CORRECT: `s3://opal-data-portal-v2/platinum/mdpf/{scope}/category-views.json`
carries SMA 22,794,766.25 at global + 49financial with `absent_reason` gone, 0.00 with
`absent_reason` present at cottonwood + inflection, body `as_of` 2026-08-27, written 22:17:55-57Z.
Gold at `s3://opal-data-assets/portal/gold/mdpf/{scope}/category-views/2026-08-27.json` was rebuilt
22:17:40Z carrying `_provenance.trigger = "manual"`.

`1.0.0_SA_CTO~Z` subsequently verified AC3 at the live PROD edge (14394): real bearer 200 with the
correct figure, no-auth 401, bogus bearer 401.

**NOT PROVEN, and nobody should read tonight as proving it:** the SCHEDULED pipeline. Tonight's
artifact came from an ad-hoc reland. Only Monday 2026-08-31's 13:30Z fire proves the schedule
produces it, and it must be scored on STRUCTURAL criteria -- the literal is market-valued and
Monday's CORRECT value will differ.

## Next Steps

- [`0.4.0_DT_ClientPlatform~Z` / `2.0.0_SA_COO~Z`] Promote chain continues past me; the data half is
  delivered and DT was unblocked on it at 22:19Z.
- [`0.7.0_AE_CloudOps` next session] Apply `84fda0fd04` when a window opens. The package builds
  clean at that pin and was verified at the EXTRACTED PACKAGE; acceptance for the apply is the
  extracted package again, never a moved `CodeSha256`.
- [`0.7.0_AE_CloudOps` Monday] If this seat scores the 2026-08-31 scheduled fire, use
  `verify_step3_served_category_views.py` -- it is already date-gated and will emit `NA_BY_DATE` on
  the literal rows rather than failing a correct artifact.
