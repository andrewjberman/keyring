# CVO~Z session log -- 2026-08-28 1745Z-2125Z: the B0 category-views entry, and the obvious remedy was the real bug

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), IMPLEMENT, COORDINATE

**Serial:** `3.0.0_SA_CVO~Z` (site-Z lane, Tier-1 CVO)
**Window:** since `0d335faaed` (the 1628-1745Z log; is-ancestor confirmed) -> ~21:25Z
**Authority:** Andrew-direct ~19:3xZ -- "lets proceed whatever needs to be proceeded to categorically
close this out" / "regarding D4" / "and the items you listed."

---

## 1. WHAT THIS WINDOW DID

Four certifications filed, then the D4 blocking item authored, deployed and exercised.

```
  b5b9f8ae6e  cert ETFS_POSITIONING.TO-1 8/8 + TO-5 6/6
  99c824f9da  cert ETFS_INGEST.TO-6 6/6 + TO-8 6/6  (supersedes the 15:3xZ partial)
  364656f444  cert ETFS_INGEST.TO-9-DS 3/5 + D1_CATVIEWS.TO-N1-DS 3/8  (both PARTIAL)
  0b03cd9fa8  amend cert TO-M1-DS -- vintage note, verdict SURVIVES
  7604f2b4bd  fix MDPF_CANPLAT_G2.B0 -- declare category-views          <- THE ACT
  d3d3718264  amend cert TO9DS/TON1DS -- the lift event was wrong TWICE  <- SELF-CORRECTION
  d075024ac0  cert MDPF_CANPLAT_G2.B0 -- AUTHORED, DEPLOYED, EXERCISED
  33d36d0d2a  doc MDPF_CANPLAT_G2.B0 -- both hazards into the amendment protocol
```

## 2. THE B0 ENTRY -- THE JUDGEMENT THAT MATTERED WAS NOT THE CRASH FIX

`category-views` came into existence in S3 at 13:31Z and was undeclared in the G2 B0 list.
`r7_comparator.py:139` subscripts `sectionb["artifact_types"][atype]` UNGUARDED -> `KeyError` on the
write path. The obvious fix is to copy the three sibling entries.

**All three siblings exempt `_provenance.written_at`, and THE GOLD PLANE NEVER EMITS IT** -- measured
0 at 4 of 4 served scopes. A sibling copy stops the crash and returns a FALSE `conflict` on every
same-`as_of` run FOREVER, because the field that actually varies is `_provenance.process_time`.
**The crash is loud and the false verdict is silent, so the copy PASSES the test the bug report was
written against.** `1.0.0_SA_CTO~Z` caught this before I wrote a line; that is the only reason this
window records a fix rather than a second defect.

CAUSE, adopting `2.0.0_SA_COO~Z`'s framing: the list was derived 2026-08-07 against PLATINUM publish
instants; the gold consolidator's A8-a later reused the same authority against a DIFFERENT provenance
shape. Correct for its original consumer, silently wrong for the second.

**Three exempted paths, three states, one live (Rule 24(iv)):**
- `process_time` -- LIVE AND VARYING, measured 13:30:37Z at 4 of 4. It alone causes the false conflict.
- `source_vintage_age_hours` -- EMITTED BUT NULL at 4 of 4 today. Inert now, ARMS when the custody leg
  populates it. Exempted before it can fire.
- `written_at` -- NEVER EMITTED on this plane. Structurally inert; retained per the ruling.

**`canonical_fields` (my authoring judgement) deliberately OMITS the `nodes.*` members** although they
are identical at 4 of 4 today: they are DATA-DRIVEN, and declaring a data fact as a shape fact would
make a legitimately empty category read as a REGRESSION (Rule 24(ii) SAME GRAIN).

## 3. VERIFICATION -- STATE REACHED EXERCISED, ON THE ARTIFACT THAT RUNS

Defect reproduced FIRST, then the fix, with the sibling pattern as the negative arm:

```
  DEFECT REPRO   load_process_time_paths(HEAD, "category-views") -> KeyError
  same-as_of     MY ENTRY equal=True 0 diffs / 117 paths | SIBLING equal=False [_provenance.process_time]
  age populated  MY ENTRY equal=True 0 diffs             | SIBLING equal=False 2 diffs
  NEG CONTROL    real business change -> equal=False [nodes.Client.aum]  (guard still discriminates)
```

Post-deploy, at the deployed artifact -- **instrument DELIBERATELY DIFFERENT** from the two package
reads already filed by `2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR~Z` (they read strings out of the extracted
zip; a second seat using the first seat's method is repetition):

```
  deployed sectionB_field_paths.json sha256 == BUILD INPUT   IDENTICAL   (Rule 22a, by content)
  deployed r7_comparator.py          sha256 == BUILD INPUT   IDENTICAL
  NEG CONTROL  git show <pin>:<bogus> -> rc=128
  EXECUTED the comparator + B0 list TAKEN FROM THE ZIP against the real artifact:
    same-as_of re-run -> 0 business diffs / 117 paths => UNCHANGED
    real change       -> 1 diff [nodes.Client.aum]
```

Four seats verified at four DIFFERENT rungs -- staged / running / extracted / exercised -- which is
what makes it corroboration rather than one instrument counted four times.

## 4. SELF-CORRECTION: MY OWN COMMITTED CERTIFICATE WAS WRONG TWICE (`d3d3718264`)

`cvoZ_TO9DS_TON1DS_PARTIAL...` said the seven UNCOMPUTABLE criteria lift "at the next scheduled fire,
~13:0xZ 2026-08-29."

1. **2026-08-29 IS A SATURDAY.** I named a calendar date without counting a trading day, against an
   explicit CLAUDE.md NEVER. The five CATV rows lift **MONDAY 2026-08-31**. Measured: 4 of 4 weekend
   runs compute the preceding Friday's `as_of` (denominator 42 manifests), so a same-`as_of` run hits
   an existing key and the served object does not advance.
2. **WORSE -- "all seven lift at ONE event" JOINED TWO PIPELINES.** Five on MDPF gold (13:30Z,
   EventBridge SCHEDULER), two on ETFS positioning (13:00Z, EventBridge RULES). I measured one surface
   and extended its answer to one I never measured. When I did measure the second it returned n=2 with
   neither observation on a weekend, so I LEFT IT UNMEASURED rather than let a thin zero finish the
   sentence.

Both carriers corrected IN PLACE (summary line + section 3) rather than a corrected body under a
stale headline. No verdict moved.

## 5. COORDINATION -- A PIN AMBIGUITY I HELPED CREATE AND HELPED CLOSE

Two pins circulated within ~90 seconds (`7604f2b4bd` mine, `47895f6628` the integrator's). I measured
that **the 23 packaged sources are byte-identical at both pins** -- the only file between them is a DS
log, not a build input -- so no package could differ. `1.0.0_SA_CTO~Z` ruled `7604f2b4bd` (the
provenance line should name the commit that landed the remedy). **I withdrew my own direction.**

My argument had been durability, and **its premise expired mid-message**: I measured
`origin/SITEZ = b2a6145f9e` correctly, and the integrator pushed before anyone read it, making my pin
an ancestor of origin. Stating the instrument and value did not PREVENT the error -- it made it cheap
to find. That is the realistic thing to expect from the rule.

Corrected `0.7.0_AE_CloudOps~Z`'s account of this IN THAT SEAT'S FAVOUR: it was a perishability
failure, not the `ls-remote`-enumerates-ref-tips trap they banked (I used `is-ancestor`). Their trap
is real and should not be left under suspicion for a failure it did not cause.

## 6. COMPILER TOOLS

| Tool | Run | Result | Note |
|---|---|---|---|
| `.tools/proof-of-spec-check.py` (3-arg) | TO-1, TO-5, TO-6, TO-8, TO-9-DS, TO-N1-DS | PASS | rc captured BEFORE any pipe; 2-arg form returns a clean rc=0 meaning COVERAGE UNCHECKED |
| `.tools/proof-of-spec-check.py` neg control | TO-5 / TO-6 instance + bogus id | PASS | rc=1 -- the check discriminates |
| `.tools/safe-commit.sh` | 4 commits this window | PASS | `-F` msgfile authored by a NON-shell writer each time |
| native `Grep` (rail: nudge-and-proceed) | `canonical_fields` estate census | PASS | 3 hits, all definitions, ZERO consumers |
| `comp-which` / `comp-find` | NOT RUN | n/a | see gap below |

**What worked:** the 3-arg proof-of-spec form with an explicit empty-set guard -- earlier today an
`ls`-built path produced an EMPTY expected set and a fully-formed FALSE INVALID that blamed the
executor. The guard now refuses to run rather than scoring against an empty set.

**What failed:** `git log --author="3.0.0_SA_CVO~Z" --since=...` returned ZERO for a seat with 8
commits in range. Silent empty, no error. Recovered with `--pretty` + `grep -F` and a POSITIVE CONTROL
(author histogram showing 10 authors present) so the filter was shown to discriminate.

**Gap found:** `.comp-graph/.agent_context` reads `SERIAL=0.4.0_DS_ClientPlatform~Z` -- ANOTHER SEAT'S
identity. On the site-Z shared checkout that file is a single-writer surface with ~6 seats behind it,
so it CANNOT be cited for one's own identity or TO context. Not cited in this log.

**Why no comp-which/comp-find:** this window's search was a single-token estate census where the
denominator mattered more than connection-awareness, and one native `Grep` with `head_limit 0`
answered it completely. Rule 21's rail nudges rather than denies there.

## 7. FILES MODIFIED

See commit messages: `7604f2b4bd`, `d3d3718264`, `d075024ac0`, `33d36d0d2a`. Rows needing extra context:

| File | Change |
|---|---|
| `org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_CANPLAT_G2/sectionB_field_paths.json` | +category-views entry (18 ins / 1 del), siblings verified BYTE-IDENTICAL across the edit; later +1 amendment-protocol line |
| `.../deliverables/cvoZ_TO9DS_TON1DS_PARTIAL_CERTIFICATION_20260828.md` | amendment block; both carriers of the false lift claim corrected in place |
| `.../deliverables/cvoZ_MDPF_G2_B0_CATEGORYVIEWS_CERTIFICATION_20260828.md` | NEW -- the B0 certificate |

## 8. BLOCKERS

**NONE BLOCKED.** Two items are DEFERRED WITH A NAMED REASON, not blocked:

- `r7_comparator.py:284` subscripts `["exemptions"]` UNGUARDED -- the identical crash class one line
  away, in this seat's own file. Cannot fire today (`category-views` carries `"exemptions": []`
  deliberately). A `.get()` patch needs a package rebuild + terraform apply for a defect that cannot
  fire until someone adds a type; the B0 list is CLOSED by constraint 2, so adding a type is ALREADY
  a contract amendment. Hazard placed in `_meta.amendment_protocol` (`33d36d0d2a`) where the author
  reads it AT THE ACT. Code patch NOT foreclosed.
- Standing B0 defect: 0 of 3 pre-existing types exempt `_provenance.process_time`, so their conflict
  guard cannot discriminate a business change from the run clock. Contract-amendment class, this
  seat's, correctly kept OUT of a time-critical deploy by `1.0.0_SA_CTO~Z`.

## 9. CURRENT STATE (written for a reader with ZERO prior context)

- **PRODUCTION:** `mdpf-gold-lambda` LastModified `2026-08-28T21:10:26Z`, `CodeSha256
  Fijk1sleMv8JoZ2tlemOYsqCbSqvdtmh/zdj3jAIGrM=`, CodeSize 818361, `MDPF_GOLD_COMMIT
  7604f2b4bd31172d3b41c967b711acb73994c3be`. Ledger CLOSED `@6c9a02e212`, tag `mdpf-pipeline-v2.4.1`.
  Rollback target: s3 VersionId `zxLyMp0d_xQW1vlHnINvS2b4voNpliyq`.
- **The lambda resolves the PACKAGED copy of the G2 files first** (`load_g2_equality()` iterates
  `(_HERE, repo_g2)`, `mdpf_gold_consolidator.py:815`); `build_package.py:163-164` bakes both. So a
  repo push does NOT reach the running job -- only a rebuild does.
- **Repo is ONE metadata string ahead of the deployed copy** by design: deployed pin blob
  `2acf980c93e3579a5c213f5c7ccf726f7e869a82`, repo HEAD blob
  `899b81dc3eacc314a709fa65cdf7f0b70c64332e`. Behaviour unaffected; absorbed by the next build. The
  21:1xZ certification was against the PINNED blob and is unaffected.
- **D4 IS NOT CLOSED.** `ETFS_POSITIONING` and `ETFS_INGEST` remain `status: active`. Seven criteria
  across TO-9-DS and TO-N1-DS are UNCOMPUTABLE because the served artifact predates the deploy.
- **MONDAY 2026-08-31 is the acceptance date.** Sat/Sun runs compute Friday's `as_of` -> existing key
  -> `unchanged` -> no write. Monday's frontier advance mints new keys (`existing is None`), so
  `business_equal` is never called and the path is clean.
- **PUSH STATE (measured, ls-remote):** `origin/SITEZ = df2232c357`. `d075024ac0` and `33d36d0d2a` are
  LOCAL at this seat; push is the integrator's leg.

## 10. NEXT STEPS

- [`3.0.0_SA_CVO~Z`] After the **Monday 2026-08-31** fires, in chain order (13:00Z -> 13:30Z -> served
  rung after ~13:50Z): certify `CATV-TON1-AC3..AC7`, `CATV-TOV1-AC7`, `TM1-AC1`, `TS1-AC2`, and
  `TO-9-DS AC3/AC4`. Print each artifact's OWN `as_of` beside every verdict.
- [`3.0.0_SA_CVO~Z`] Determine the `TO-9-DS` lift event on the ETFS positioning plane -- UNMEASURED,
  and the n=2 census cannot distinguish "skips weekends" from "has not run since 08-21".
- [`2.0.0_SA_COO~Z`] `aws_s3_object.mdpf_route_bindings` -- committed-but-unapplied 21 days, surfaced
  by `0.7.0_AE_CloudOps~Z` when an untargeted plan would have swept it into the deploy. Unadjudicated.
- [`0.0.0_AB_MSTR~Z`] Push `d075024ac0` + `33d36d0d2a` at the next integration window.
- [`Andrew`] The D4 register act travels through the sovereign channel with this seat. Any close must
  say 3 of 5 and 3 of 8 -- a close implying full satisfaction is the same falsehood class as
  "STAGED, never started."

## 11. SURPRISE CHANNEL (this seat mans it)

- **OBSERVATION, INERT** -- `1.0.0_SA_CTO~Z`: the 20:48:57Z deploy wrote into
  `opal-data-mdpf code/scripts/gold/`, which the accrual trigger's source comment (`:49-51`) calls
  "the FROZEN loose-object channel ... THE ROLLBACK TARGET", while `safe-deploy.sh` routes there BY
  DESIGN. Two records disagree; neither blocks. Does NOT affect the lambda (it runs its own zip).
- **OBSERVATION, INERT** -- mine: `portal/gold/etfs/positioning/` shows nothing since 2026-08-21 while
  today is 2026-08-28. DENOMINATOR 2. I have NOT established that this is the prefix `TO-9-DS` reads
  and am not chasing it into another lane. Flagged for the owning lane.

-- `3.0.0_SA_CVO~Z`
