# CVO session 1805-1920Z -- the cert, the sweep, and the answer that cleared a fire it should not have

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

Continues `session_1628-1805Z_the_channel_ran_a_p0_and_four_of_my_own_claims_died.md`. Written as a
separate entry because the window contains the session's most consequential error and the prior log
predates it.

---

## Current State

**P0: HELD, CORRECTLY, AND NOTHING FIRED.** Cottonwood RESTORED (`as_of_last=2026-08-24`, verified).
**Global STILL FROZEN at 2026-08-19**, gold `2026-08-20T13:31:05Z`, unchanged all window.

The remaining defect is diagnosed: `0.4.0_DS_ClientPlatform~N` established that cross-axis clause
(vi) compares `tot[i-1], tot[i], tot[i+1]` where `tot` is **a sum over legs whose membership changes
date to date** -- a sum over varying membership is not a series, and the clause silently assumes it
is. The `+469` was cottonwood's own 08-19 roster beside its own 08-19 values. **The gate's refusal
was correct and its DIAGNOSIS TEXT was wrong for this instance.** Remedy (C) authorized on a
four-arm test with a planted mutant (ARM D: proposed clause still catches the 2026-07-06 case the
clause was built from).

**THE FIRE IS HELD ON A FORK I HELPED CREATE AND THEN HELPED RESOLVE.** See "The error" below.
Live state at close of window: `~N` owes one command (does their exercised tree contain the new
consolidator, `scopes_for` >= 5); COO's Path-A ruling may invert on the answer; `0.5.0_AE_OpalETL~B`
holds the vendor+deploy, has built nothing, opened no ledger.

**ESTATE-REPORT: 17 PENDING**, unchanged this window. Two sovereign calls still open at Andrew
(frozen corpus; batching order), now joined by three held projects.

**CHANNEL:** `MDPF_COTREMEDIATION` 13 items (4 ARMED, all owned) · `OPAL_KIMIPIPELINE` 6 ·
`NFRA_COMPRAIL` 7. All schema-valid, re-validated from disk after every append.

---

## Blockers

**None at this seat.** Nothing waits on me and I hold no gate.

---

## ⛔ The error, because it is the reason this entry exists

**I answered COO's last-mile question -- WHICH ARTIFACT EXECUTES
`dim_mdpf_aggregate_aua_timeseries.py` -- BY SWEEPING S3 CODE PREFIXES, FINDING ONE COPY, AND CALLING
IT THE EXECUTING COPY. COO CLEARED A PRODUCTION FIRE ON THAT ANSWER.**

There are **two** executors:

```
EC2 dispatch      mdpf-daily-dispatch.sh:125 syncs code/scripts/ AT RUN START
                  -> the S3 copy IS executing, and it carries the fix
mdpf-gold-lambda  imports its OWN vendored copy (:70 sys.path.insert, :78 import), fetches NO code
                  from S3.  CodeSha256 sNAnYFKGr8d1...  LastModified 2026-08-24T12:54:28Z
                  mdpf-scheduled-floor cron(30 13) targets it -> THIS IS THE ACCEPTANCE PATH
                  vendored bytes are PRE-PATCH (count_membership: deployed 0 / patched 14)
```

**I printed `DENOMINATOR: 1 S3 copy` and it was TRUE.** It counted **S3 code objects**. The question
was **executors**. A denominator states the size of what you counted and is **silent about whether
you counted the right KIND of thing** -- Rule 22 `WHOLE`, and one level worse than COO's `list-rules`
sweep (right kind, wrong completeness).

**THE AGGRAVATING FACT, and it is the only part worth carrying: I HAD SOLVED THIS EXACT DISTINCTION
THREE HOURS EARLIER AND USED THE CORRECT ANSWER AS EVIDENCE THAT IT DID NOT APPLY.** On the
`mirror_schemas` thread I established that a Lambda executes vendored package bytes and an S3 code
prefix can be a true non-member. I then wrote, **in the message that failed**: *"That is the OPPOSITE
of the Lambda case from this morning."* **Knowing a failure mode by name does not immunise you
against writing it -- and knowing it WELL is worse, because the correct instance becomes the reason
you stop looking.**

**What firing would have cost:** the ad-hoc EC2 run **would** have restored global; tomorrow's
`cron(30 13)` Lambda run, still pre-patch, would have refused; platinum would have kept republishing.
**Global would have flipped to correct and then BACK, on a client-facing surface, with a green run**
-- a fresh instance of this outage's own signature, manufactured by its repair.

**Caught by `0.4.0_DS_ClientPlatform~N` holding a CLEARED fire** and re-deriving the one input that
would invalidate it, against a senior seat's answer, with COO having said *"I am not asking you to
re-derive it."* They used the rider I attached (*"verify it yourself if it is load-bearing"*).
**The rider is not why it worked; the seat choosing to use it against two seniors is.**

Filed as `NFRA_COMPRAIL-S7` (@1817bed9cc) with the instrument gap as the fileable half: **no comp-tool
answers "what executes this file?" across deploy models.** Gate candidate routed, not built.

---

## Work landed this window

| Act | Evidence |
|---|---|
| **Decomp certification DISCHARGED** | `@73dd2c9251` -- CERTIFIED ON SUBSTANCE, no cell invalidated, no re-decomp owed. Cells were EXERCISED (drove a live P0 to a verified end state), not desk-reviewed |
| **One defect found in it, routed to the HARNESS not COO** | `run.json` 38 cells / `DECOMP.md` 42; machine half stale by four amendments. **`proof-of-spec-check.py:339` reads `DECOMP.md` and never mentions `run.json`** -- the guarded half and the human-read half are different files. Every atom-decomp run has the shape the surprise-channel spec §0 rejected |
| `MDPF_COTREMEDIATION-S11` | global's gate refusal was diagnosed + lane-assigned in a CTO deliverable **28h earlier** (@eb2be76858) and four seats rediscovered it during a live P0. The filing was prompt and correct; **a deliverable is not a queue** |
| `-S12` | the silver first-mint 404, DISMISSED_WITH_REASON on a two-plane trace |
| `-S13` | **ONE served field name, THREE derivations, ONE label** -- ARMED. My attribution INVERTED under CTO's re-measurement: cottonwood is the partner that OBEYS "never total this column" |
| `OPAL_KIMIPIPELINE-S6` | amends S5: the capture uploader **WAS built** (2026-08-11) and runs daily; the gap is the CONSUMER wire |
| `NFRA_COMPRAIL-S7` | above |
| Sweep interaction surfaced | 4 channel projects flagged; **2 real and held** (`OPAL_KIMIPIPELINE`, `WSE_COTMDL`), **2 my over-inclusion** |

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `"DECOMP.md\|run.json"` -> corrected to bare pipe | **PASS after a tool-caught error** | comp-find WARNED that `\|` is literal in python re. **The tool caught my BRE habit before it produced a false zero** |
| `comp-find` | `"not built\|never built\|..."` over the runner | PASS | swept for other stale self-descriptions: exactly 2, both already named. No third hiding |
| `comp-find` | `"code/scripts/silver"` | **FAIL (structural)** | carried from the prior window; the path is runtime-assembled and never exists as a literal |
| `aws lambda get-function-configuration` | `mdpf-gold-lambda` | PASS | the live primitive that confirmed the second executor |
| `aws scheduler get-schedule` | `mdpf-scheduled-floor` | PASS | ENABLED, `cron(30 13)`, target = the Lambda. **The Scheduler plane, which `list-rules` cannot see** |
| `git merge-base --is-ancestor` | `c6b5ab4efe` -> `1234c8779e` | PASS | proved no clean pin exists -- **structural, not a tooling limit** |
| `safe-commit.sh` | x5 | PASS | all `-F`, msg-verify MATCH each |
| jsonschema extractor | x5 | PASS | every append re-validated from disk |

**What worked:** `comp-find`'s BRE warning fired on my own bad pattern and prevented a false zero --
the only time today an instrument caught me before the output did. The ancestry check answered a
fork that three seats were reasoning about in prose.

**What failed:** my executor census (above). **GAP FOUND:** no comp-tool maps a repo path to its
executors across deploy models -- filed `NFRA_COMPRAIL-S7`, gate candidate routed.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform~N]** The one command: does the exercised tree carry `scopes_for` >= 5.
   It decides whether shipping both modules is the EXERCISED config or the novel one.
2. **[2.0.0_SA_COO]** Path-A ruling, which may invert on that answer.
3. **[0.5.0_AE_OpalETL~B]** Lambda vendor+deploy once ruled. **NEVER#6 ledger at start.**
4. **[3.0.0_SA_CVO]** Verify the served global payload when it moves -- bar is `as_of_last` **and**
   `_provenance.source_keys`, never object mtime. A bounded background watch is armed on global's
   gold; **a timeout from it is not a failure signal.**
5. **[3.0.0_SA_CVO]** `OPAL_KIMIPIPELINE-S4` remediation (`/estate-pull` reading
   `readjudication_required`) still NOT done. Separable from S2's enum question -- the carry-forward
   fields are orthogonal to the status axis, so it is not a Rule-24 enumeration act.

---

## Files Modified

See commit messages: `73dd2c9251`, `45f4f53f49`, `092fbe74d1`, `51d932193e`, `198dd4615b`,
`1817bed9cc`. All on `origin/CLOUD` following MSTR's integrator push (`git branch -r --contains`
re-derived, not assumed).
