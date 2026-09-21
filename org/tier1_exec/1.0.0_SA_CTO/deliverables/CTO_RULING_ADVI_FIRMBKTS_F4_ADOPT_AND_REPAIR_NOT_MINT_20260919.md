# CTO RULING -- `ADVI_FIRMBKTS` F4 is **ADOPT-AND-REPAIR**, not **MINT**. The project is seatable; its premise is not.

**Ruled by:** `1.0.0_SA_CTO`, 2026-09-19 ~20:5xZ. **Owed to Andrew** off his question at ~20:1xZ:
*"i dont know if we can really do advi_firmbckts now that youve locked yourself out of working with the
buckets that we'd need for that"*, and his follow-through *"how could our IAM be able to create buckets
but not delete them?"* -- which is what forced the measurement below.

---

## 1. THE MEASURED WORLD, ON MY OWN INSTRUMENTS, THIS TICK

| # | claim | instrument | result |
|---|---|---|---|
| 1 | the two buckets EXIST | `aws s3api list-buckets` (live plane) | **`opal-data-inflection` and `opal-data-cottonwood`, both created `2026-09-18T20:05:17Z`** -- the SAME SECOND, so one apply, and **not this project's** |
| 2 | the fence is not merely declared | `aws s3api get-bucket-policy --bucket opal-data-inflection` | ⛔ **`AccessDenied ... User: arn:aws:iam::313476888478:user/Andrew_Berman is not authorized to perform: s3:GetBucketPolicy ... with an explicit deny in a resource-based policy`** |
| 3 | the aws corpus can answer this at all | `comp-find --corpus aws` | **0 hits of 2593 nodes** for either bucket -- see §4 |

⭐ **(2) IS THE STRONGEST STATE EVIDENCE THIS ESTATE CAN PRODUCE AND IT COST ONE CALL.** Rule 22's STATE
axis runs DESIRED -> APPLIED -> EXERCISED. This is not a plan file and not a `get-bucket-policy` that
returned a document I then reasoned about: **it is the fence REFUSING, by name, the human admin identity,
and naming its own mechanism in the error string.** EXERCISED-AGAINST, on the first attempt.

**So the world is:** two buckets, live for over 24 hours, **born with a fence that denies `s3:*` to every
identity this estate currently holds** -- including Andrew's own user.

## 2. ⛔ THE PREMISE DEFECT IS NOT "THE FENCE IS LATE". IT IS THAT THE PRECONDITION WAS CONSUMED BY ANOTHER PROJECT.

`ADVI_FIRMBKTS`'s register row, `blocking` line (4), verbatim:

> *"THE FENCE CHANGE (`LGIC_ENFORCE`, ruled ~18:4xZ on three conditions) lands on the template BEFORE this
> project mints `opal-data-inflection` and `opal-data-cottonwood`."*

**That ordering is now UNSATISFIABLE, and not because anything is late.** `IRPT_BCKEND`'s `IB-rte-3`
minted both buckets at `2026-09-18T20:05:17Z`, **with the fence**, and the fence self-locked out the
applying identity -- the cause is named in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`'s
own comment (row `IRPT_BCKEND-W3-S43`). **A precondition stated as an ORDERING between two projects was
satisfied by a THIRD, in the wrong direction, and nothing in either project's carrier could notice.**

## 3. ⛔ AND F4's ACCEPTANCE IS SATISFIABLE BY THE BROKEN WORLD -- THIS IS THE FINDING THAT MATTERS

F4's acceptance line, verbatim from the PRD's cell-candidate table (`:313`):

> *"both buckets exist **born with the fence**, read logging, versioning and blocked public access ..."*

**Read that clause against the live world and every conjunct reads TRUE.** Both buckets exist. Both were
born with the fence. A grader checking F4's first clause gets a **PASS** -- ⛔ **while the fence is
precisely the defect that denies every identity we hold.**

⭐ **THE CRITERION ASSERTS THAT A CONTROL EXISTS AND THE CONTROL DOES EXIST. WHAT IT NEVER ASKS IS WHETHER
THE CONTROL ADMITS THE ESTATE THAT MUST OPERATE THE BUCKET.** "Born with the fence" is a BIRTH-PROPERTY
claim, and a birth property is structurally blind to a fence that fences out its own operator. This is
Rule 22's STATE axis passing at EXERCISED on the wrong subject: the control was exercised, against us.

**GENERALISATION, and I am stating it as the transferable part:** ⛔ **A CRITERION THAT NAMES A GUARD'S
EXISTENCE MUST ALSO NAME AN IDENTITY THAT THE GUARD ADMITS, AND AN ACT THAT IDENTITY CAN PERFORM.** A
guard-existence clause with no admitted-identity clause beside it grades a lockout as a success.
**COST:** one clause per guard criterion. **NON-APPLICATION:** a guard whose whole purpose is to admit
nobody (a tombstone, a retired-bucket deny-all) -- there the lockout IS the outcome.

## 4. ⚠ A SECOND FINDING, FILED SEPARATELY: THE AWS CORPUS RETURNED A CONFIDENT MEASURED ZERO ON A LIVE BUCKET

`comp-find --corpus aws` for `opal-data-(inflection|cottonwood)`: **0 hits across 2593 aws nodes**, vintage
`2026-09-19 12:21:32 UTC` -- **sixteen hours AFTER the buckets were created.** So this is not a vintage lag.

**POSITIVE CONTROL RUN BEFORE CONCLUDING, because a zero cannot distinguish "absent" from "unmodelled":**
`opal-data-bd` returns **159 hits, band `S3_BUCKET=1`**. ⭐ **The corpus models S3 buckets. It does not hold
these two.**

⛔ **AND `drift_class` CANNOT CATCH IT.** `LIVE-no-DECLARED` exists exactly to flag "in AWS, not in the
repo" -- but it is a property of a node that IS in the graph. **A resource missing from the graph
altogether cannot be classed as drift; it is classed as nothing, and reads as absence.** Had I trusted
the corpus read I would have told Andrew the buckets do not exist -- **the exact mirror of the root error
he caught me in two hours ago, in the other direction.** Row filed.

## 5. THE RULING

> **F4 is AMENDED from MINT to ADOPT-AND-REPAIR.** The project does not create `opal-data-inflection` or
> `opal-data-cottonwood`; it **adopts two existing buckets, repairs the fence that was applied at their
> birth, and proves the repair from an identity the repaired fence admits.**

**Why not the alternative (keep the mint, delete and recreate):** it is available -- Andrew asked it
directly -- but it is strictly worse here. ⛔ **A delete-and-recreate spends a destructive act to reach a
state an additive repair reaches**, and the buckets are not empty of consequence: they are already declared
in `s3-lgic-firm-buckets.tf`, already carry whatever `IB-rte-3` put in them, and their Terraform resources
are TAINTED in remote state, so a destroy path re-opens a half-landed apply rather than closing it.
**Repair beats rebirth when a repair path exists.**

**AND THE REPAIR IS ITSELF FENCED, which the amended cell must carry:** re-applying the corrected fence is
an `s3:*` action on a denied bucket, so **Terraform cannot repair its own apply** from an unadmitted
identity.

## 5a. ⛔ CORRECTING MY OWN CLAIM IN §5 BEFORE ANYONE ACTS ON IT: "THE FENCE ADMITS A ROLE WE CAN MINT" IS A **DESIRED-PLANE** READ

**This ruling's first draft said the fence admits `role/*-inf-*` "BY CONSTRUCTION". I read that off
`infra/aws/terraform/modules/opal_name/generated_locals.tf` -- which is the GENERATOR'S OUTPUT, i.e. the
policy the NEXT apply will CREATE. It is not the policy ATTACHED to the bucket now, and I cannot read that
one: `get-bucket-policy` is the call the fence denies me.** Rule 22's STATE axis, DESIRED vs APPLIED, on a
claim I put in a ruling and a message inside one hour.

⛔ **AND `IRPT_BCKEND.TO-IB-rtf-5` ALREADY CARRIES THE EXACT WARNING, IN ONE SENTENCE, IN ITS `<status>`:**

> *"The DESIRED/APPLIED trap for any reader: `exemptions.json`'s three users are the exemptions of the
> policy this apply will CREATE, not of the policy attached now (which admits nobody we hold)."*

**A staged order I had not read was ahead of me on my own finding**, and `infra/logic/registry/exemptions.json`'s
own `_about` says the same from the other side: *"No principal is exempt at this seed."*

⭐ **THE CLAIM IS NOT FALSIFIED EITHER -- AND SAYING SO IS THE POINT.** My `AccessDenied` was against
`arn:aws:iam::313476888478:user/Andrew_Berman`, **an IAM USER**. A pattern reading `role/*-inf-*` could not
admit a user under any reading, so **my denial is evidence about the user path and says NOTHING about the
role path in either direction.** The measurement I ran cannot discriminate the question I used it for.

**THE ONE DISCRIMINATING TEST, NAMED SO IT HAS A CARRIER AND NOT RUN BY ME:** an `s3:*` call against either
bucket from a principal whose ARN matches `role/*-inf-*`. **Nobody has run it.** `IB-rtf-7`
(*step 4 attempted by every credential the seat holds*) is the order that owns the class -- ⛔ **and its
framing is "every credential the seat HOLDS", which is exactly the boundary the AE measured correctly and
the boundary my finding sits OUTSIDE: a role matching the glob is one this estate can MINT and does not
hold.** Minting it is an `infra/aws/**` act in the CLOUD_OPS lane and is not mine; I surface it scoped.

**SO THE RULING'S OPERATIVE PART STANDS UNCHANGED** -- F4 is ADOPT-AND-REPAIR because the buckets exist and
are fenced, which is measured. **What does NOT stand is any sentence of mine promising a repair path that
avoids Andrew's console act.** `IB-rtf-5` holds step 4 as a human act at the console, deliberately excludes
the account root from the exemption set (*"the rollback path must not depend on an exemption, and nobody
adds root to the list"*), and that ordering is the issuer's, not mine to relax from a `.tf` file.

⛔ **THIS IS MY THIRD READING OF THE SAME TWO BUCKETS TODAY AND THE THIRD ONE I HAVE HAD TO NARROW.**
root-is-the-path (inherited, wrong); the-buckets-do-not-exist (corpus zero, caught by a positive control);
the-fence-admits-a-role-by-construction (DESIRED plane, caught by reading the order that owns the act).
⭐ **Each was a faithful instrument answering a question slightly narrower than the sentence I wrote beside
it. The pattern is not carelessness with instruments -- it is a SENTENCE WIDER THAN ITS MEASUREMENT, three
times, on the same object.**

## 6. WHAT MOVES, AND WHOSE SIGNATURE IT RE-OPENS

| carrier | edit | half re-opened |
|---|---|---|
| PRD `CELL CANDIDATES`, F4 row | verb `mint` -> `adopt and repair`; acceptance gains the **admitted-identity clause** per §3 | **BRIEF** |
| PRD `PATHS` (the new-resources row) | the two buckets are **EXISTING, ADOPTED**, not `new` | **BRIEF** |
| PRD `SURFACE MANIFEST` (the never-widen row) | **APPLIED: the fence REPAIRED**, not `APPLIED: two new buckets` | **BRIEF** |
| register `blocking` (4) | the ordering precondition is **CONSUMED**, recorded with its cause, superseded text retained per R-43 | mine, no half |

**MEASURED, NOT PREDICTED:** `python .tools/prd-signoff.py status ADVI_FIRMBKTS` after the edit reads
**`ratified-text SIGNED / current`** and **`brief STALE ... OWED BY 4.0.0_SA_CRO (live)`**. **ONE half is
re-owed, not two.** `.tools/prd-signoff.py` binds each half to the HASH of its sections, never to
`prd_version`, so this is not a header bump -- but only the BRIEF half's bytes moved.

## 6a. ⛔ AND I HAD THIS WRONG IN THIS RULING'S FIRST DRAFT -- THE CORRECTION IS THE POINT

**I wrote that BOTH halves were re-owed, and I assigned the `PATHS` and `SURFACE MANIFEST` rows to the
RATIFIED-TEXT half *because they read like contracts*** -- a never-widen row, a served-resource row, the
vocabulary of the CONTRACTS section. **The partition is not by SUBJECT. It is by TOP-LEVEL SECTION
HEADING**, and `prd_signoff_lib.RATIFIED_SECTIONS` is the literal two-tuple `('ENDPOINT', 'CONTRACTS')`.
Of this PRD's nine top sections, exactly two are ratified-text; `PATHS` and `SURFACE MANIFEST` are their
own sections and both are BRIEF.

⭐ **I restated the law's description of the halves instead of running the instrument that implements
them, and the restatement was wrong in the direction that INVENTS WORK** -- it would have put a re-sign
ask in front of `3.0.0_SA_CVO` for a half whose bytes never moved. **That is an agent-made gate arriving
by arithmetic error rather than by intent, which is the version of it nobody checks for.**

**The tell was available before I wrote the sentence and cost one command:** `prd-signoff.py status` is
named in this project's own `blocking` line (1) as *"the one read of what is owed"*, and I wrote a claim
about what is owed without running it. **COST: one command. NON-APPLICATION: none -- the tool is the
authority on its own partition and there is no case where my reading of it outranks it.**

## 7. ⭐ AND THE ANSWER TO ANDREW'S ACTUAL QUESTION

**`ADVI_FIRMBKTS` IS SEATABLE.** Nothing about the lockout makes the project undoable; it makes F4 a
different cell. What the lockout DID cost is the premise -- and the premise was already wrong before the
lockout, because the mint had moved to another project a day earlier and no carrier said so.

**Non-application of this whole ruling:** it governs `ADVI_FIRMBKTS` F4 and the two buckets it names.
It rules nothing about `IB-rte-3`, about whether the fence's substring glob (`*-inf-*`) is the right
boundary -- that is its own filed row -- or about any other project's mint.

**PUSH STATE:** stated in the commit that carries this file.
