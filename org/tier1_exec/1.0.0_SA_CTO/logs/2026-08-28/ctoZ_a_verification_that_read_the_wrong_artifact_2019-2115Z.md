# CTO~Z -- a byte-perfect verification of the WRONG artifact, and the answer everyone was inferring was sitting in a key name, 2019-2115Z

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, ADJUDICATE, DEPLOY

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 20:19Z -> 21:15Z (continues
`ctoZ_the_adhoc_qa_run_found_what_the_clock_hid_1945-2019Z.md` @`3781fc13c1`)
**Basis:** the KeyError surfaced by the ad-hoc QA run Andrew ordered at 20:0xZ
(*"no excuse to wait for tomorrow when we can find out if data flows and is presented properly
today"*), then `/open-calls`.

---

## 1. WHAT LANDED

- **THE CRASH FIX IS LIVE AND VERIFIED AT THE RUNNING BYTES.** `CodeSha256` moved
  `bnpYayh00uII...` -> `Fijk1sleMv8JoZ2tlemOYsqCbSqvdtmh/zdj3jAIGrM=`, `MDPF_GOLD_COMMIT`
  `70a0828226` -> `7604f2b4bd`, at 21:10:26Z. **Tomorrow's ~13:30Z run no longer crashes.**
- **My half:** `b2a6145f9e` -- `conditional_put:880` widened to catch `KeyError`, exercised with a
  POSITIVE control (declared type OK), the DEFECT reproduced, the fix catching, and a **NEGATIVE
  control proving the OLD tuple does NOT catch it** -- i.e. the widening is load-bearing, not merely
  sufficient.
- **`3.0.0_SA_CVO~Z`'s half** @`7604f2b4bd`: the `category-views` B0 entry, authored to the spec I
  ruled -- exemptions naming `_provenance.process_time` and `_provenance.source_vintage_age_hours`,
  **not** the siblings' `written_at`-only copy. That is what turns a same-`as_of` recompute into a
  correct `unchanged` instead of a false `conflict`.

## 2. THE FINDING: A BYTE-PERFECT VERIFICATION OF THE WRONG ARTIFACT

At 20:48:57Z a seat pushed my fix, deployed it, and verified it AT THE DEPLOYED BYTES -- correctly
refusing the deploy gate's rc=0, clearing the `aws s3 cp` rc=0-writes-nothing trap, and catching its
own guessed-bucket probe. **Every one of those was right, and the all-clear was false.**
```
  s3://opal-data-mdpf/code/scripts/gold/mdpf_gold_consolidator.py   updated 20:48:57Z  <- READ
  mdpf-gold-lambda                                                  LastModified 17:28:29Z
                                                                    runs its own ZIP   <- EXECUTES
```
The function was last updated **3h20m BEFORE** the write taken as its deploy. I downloaded the
package via `get-function -> Code.Location`: the fix was absent, POSITIVE control 1, NEGATIVE 0.
>> **"THE DEPLOYED BYTES" IS NOT A UNIQUE REFERENT.** GRAIN and DISCRIMINATION both pass inside the
   wrong referent; the failure is one rung below both. CLAUDE.md Rule 22a names it exactly:
   *"running-bytes-older-than-built passes every rung."*
**THE DIFFERENCE WAS NOT RIGOUR, IT WAS THE OBJECT.** The deploy tool's success message names its own
destination, which reads as confirmation of the deploy you meant. And the same seat had flagged this
precise risk for the NEXT file two messages earlier -- **the gap was named one file too late, by the
seat closest to being right.**

## 3. THE MEASUREMENT THREE SEATS CALLED UNMEASURED WAS IN A KEY NAME

`0.0.0_AB_MSTR~Z`, `2.0.0_SA_COO~Z` and `3.0.0_SA_CVO~Z` each said the deciding fact was unknown:
does a weekend run recompute an unchanged `as_of`? Two reasoned about code paths to get at it.
The A6 manifest key is `_manifests/{data_as_of}/{run_ts}.json` -- **the path STATES the as_of its run
computed**:
```
  20260821T133107Z under _manifests/2026-08-20/   Fri -> as_of 08-20
  20260822T133104Z under _manifests/2026-08-20/   SAT -> as_of 08-20   UNCHANGED
  20260823T133102Z under _manifests/2026-08-20/   SUN -> as_of 08-20   UNCHANGED
  20260824T133107Z under _manifests/2026-08-21/   Mon -> as_of 08-21
```
4 of 4 weekend runs, plus the same shape the weekend before. And the Sat 08-22 manifest recorded
**`conflict` on FIVE existing keys** -- `conflict` is what `business_equal` returns when it RUNS.
>> **THE CRASHING FUNCTION EXECUTES ON WEEKENDS.** It survived only because those five keys are types
   that HAVE a B0 entry.
**AND IT INVERTED A DOWNGRADE.** "Zero weekend writes in 22" was read as evidence the path is not
reached. **The missing write is the PRODUCT of that path.** A crashed run and a skipped run leave
identical S3 evidence -- the listing could never discriminate them; a THIRD artifact did, in one read.

## 4. WHY 22 CLEAN DAYS PROVED NOTHING

`category-views` had exactly ONE dated key estate-wide, written that same day at 13:31:13Z (manifest
status `written`, 4 scopes). Before it, `existing is None`, so the compare branch was unreachable for
that type. **Past weekends were not a precedent; they were a period when the hazard was absent.**
Latent since the type was born 08-19, armed seven hours before it would first fire.

## 5. MY OWN OVERSTATEMENT, CORRECTED BEFORE IT HARDENED

I wrote that the crash "kills the write for EVERY scope and EVERY artifact_type." Two seats
propagated it from my 13913. Read at source: `category-views` is the **4th and LAST** entry of the
emission loop, with only the manifest write and the return after it. **The crash costs its four puts
and the A6 run manifest; the first three types' puts across all four scopes have already landed.**
Then I discharged the caveat I had attached twice (*"nobody should assert Monday is safe on my
account"*) by reading the two downstream stages instead of leaving it hanging:
```
  publisher :135   `if rel.startswith("_manifests/")`  -> SKIPS the gold manifest prefix
            :289   completeness = "ROSTER-DERIVED"     -> not run-derived
  accrual bridge, its own docstring: "NO convergence/freshness gate: the bridge reads whatever
            the CURRENT gold source objects are"       -> decoupling is DELIBERATE
```
**Neither downstream stage cares. Monday is safe, said on my own account.** No natural experiment
existed to settle it -- 22 consecutive days of gold manifests, zero gaps, so a missing one had never
occurred and could only be resolved at source.

## 6. Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `'opal-assets-mdpf-portal-publisher' --all --files` | 587 hits / 27,874 files, bands printed; located the publisher |
| `comp-which` | publisher + accrual routing | near-tie, 3 of 80 -- correctly refused to guess; I used `Read` instead |
| `comp-pipescript` | `io d_publisher_port.py` | OUT-OF-GRAPH, AST fallback -- and it was the WRONG publisher (ADVI). Caught by reading its writes |
| `build_package.py` | `--pin b2a6145f9e` | 814,462 B, import-closure OK, 18 .py, 22 modules |
| `safe-commit.sh` | `GIT_COMMIT_AUTHOR_OVERRIDE=DS` | `b2a6145f9e`, msg-verify MATCH len=4528 |

**WHAT FAILED, and it is mine:** I queried the manifest write rows on `.outcome` and got a clean
`null` across all 20 -- the field is `status`. A wrong field name returns a full-denominator null that
reads as "no outcomes recorded". Caught only by dumping one row verbatim. **Own instance of the
banked "I write matchers against formats I never read."**
**RAIL:** the `infra/*.tf` limb fired twice on false positives (a JSON key-count and a build
invocation that merely contained `infra/`). Complied with the RULE -- used `Read`, and marked the two
genuine non-searches `# rail-checked:` with a reason rather than routing around the gate.

## 7. Blockers

**NONE.** The deploy landed and is issuer-accepted. One sovereign call is at Andrew (s.9).

## 8. Current State (zero prior context)

- **`mdpf-gold-lambda` runs pin `7604f2b4bd31172d3b41c967b711acb73994c3be`**, `CodeSha256`
  `Fijk1sleMv8JoZ2tlemOYsqCbSqvdtmh/zdj3jAIGrM=`, 818,361 B, applied 21:10:26Z. Package sha256
  `1628e4d6c95e32ff...` == declared `content-sha256` metadata == the staged artifact I read
  PRE-apply. Three-way agreement.
- **NEVER#2 half-landed window:** artifact swapped 21:04:23Z, apply landed 21:10:26Z, ~6 min, closed.
- **STANDING DEFECT, 1 of 4 fixed:** `account-distribution`, `aum-metrics` and
  `aggregate-aua-timeseries` still exempt only `_provenance.written_at`, **which the gold plane never
  emits** (measured on the live artifact: gold `_provenance` carries `process_time` +
  `source_vintage_age_hours`; `written_at` occurs 0 times). So those three record FALSE `conflict` on
  every same-`as_of` run and the guard cannot discriminate a real change from the run clock. The list
  was derived 2026-08-07 against PLATINUM publish instants ("all 12") and is consumed against gold.
  Contract-amendment class, `3.0.0_SA_CVO~Z`.
- **OBSERVATION, inert:** the accrual trigger calls `opal-data-mdpf code/scripts/gold/` the "FROZEN
  loose-object channel ... never updated: the ROLLBACK TARGET" (:49-51), while `safe-deploy.sh`
  routes there by design. Two carriers disagree; does not affect the Lambda.
- **Monday 2026-08-31 remains D1's acceptance date.** A same-`as_of` recompute correctly does not
  advance the served object.

## 9. Next Steps

1. **[ANDREW]** The one open call: reland the `as_of 2026-08-27` `category-views` keys so the SMA L0
   fix is visible in served data before Monday? The served artifact was BUILT 13:30:37Z; the lambda
   carrying that fix deployed 17:28:29Z -- **what is served predates the fix.** REC: **no** (Monday
   produces it naturally, and I have not measured that the content actually differs -- I would measure
   the delta first).
2. **[`3.0.0_SA_CVO~Z`]** The 3-of-4 `process_time` exemption defect. Contract amendment.
3. **[SCHEDULED]** Sat/Sun runs now complete as `unchanged`; Monday ~13:30Z is the acceptance fire.

## 10. One thing worth carrying

**FOUR SEATS WERE WRONG TONIGHT AND EVERY ONE WAS CAUGHT BY A DIFFERENT SEAT THAN THE ONE THAT MADE
THE ERROR.** I said tomorrow was "probably fine"; COO refuted it, then downgraded it on evidence that
proved the opposite of what it was read as; CVO amplified that downgrade; MSTR reopened it and
declared production fixed off the wrong artifact; I overstated the blast radius and two seats carried
it. **Not one of those was caught by its author.**
>> **THE PATTERN THAT ACTUALLY WORKED WAS DISAGREEMENT, NOT CARE.** Every seat was careful. Care
   produced the errors AND the corrections; what separated them was whether a second seat with a
   DIFFERENT instrument looked. A byte-perfect verification, a correct 22-observation census, and a
   sound code-path read each failed while passing their own checks.
**The rule I am carrying: before verifying deployed bytes, ask which artifact the RUNTIME loads --
and answer it from the deploy definition, never from where a deploy tool said it wrote.**
