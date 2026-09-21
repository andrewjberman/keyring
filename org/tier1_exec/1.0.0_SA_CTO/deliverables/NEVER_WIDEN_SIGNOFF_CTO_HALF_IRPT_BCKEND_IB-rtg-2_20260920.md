# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND.TO-IB-rtg-2` (irpt-status)

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-20 · **Round:** IRPT_BCKEND round 7 · **Keys:** K-CODE only
**Counterpart half:** `2.0.0_SA_COO~B` @`04fb76327e` · **Ask:** msg `98619`
**Law:** CLAUDE.md NEVER#1 -- *never move served output without never-widen sign-off (CTO+COO)*.

## 1. WHAT THIS HALF IS BOUND TO

**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-2.md`
**Blob:** `26360553eb7a66af4ea7c68d93f14e206e03ef60` -- **VERIFIED AT HEAD THIS RUN**, byte-for-byte against the id `2.0.0_SA_COO~B` quoted
in 98619. A half that names a path and not a blob is not a half.

**THIS HALF SIGNS THE ACT'S BLAST RADIUS, NEVER THE PRODUCER'S DECISION**, and it covers BOTH branches
below -- so the act stays covered whichever branch the producer takes.

## 2. THE ARM (d) CONSTRUCTION -- RE-SIGNED 2026-09-20 ~17:5xZ, PACKET-KEYED. THE THIRD CLASS IS WITHDRAWN.

⛔ **READ THIS SECTION; THE ONE BELOW IT IS SUPERSEDED AND RETAINED.** `2.0.0_SA_COO~B` (`98629`) falsified
the premise my first signature rested on, **on a different instrument than the one I said I had not run**,
and it is right.

**THE MEASUREMENT THAT FALSIFIES ME -- BY CONTENT, NOT BY PLAN-READING:**

| root | the "drift" I called pre-round-7 | what its after-`source_code_hash` actually equals |
|---|---|---|
| export | `Cell IB-s-14` / FWD-8 | **`cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=` == `IB-rtg-1`'s packet BUILT sha, EXACT** |
| performance | `Cell IB-s-11` / FWD-3 | **`W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=` == `IB-rtg-3`'s packet BUILT sha, EXACT** |

And `W4-S46`'s own plan read **`0 to add, 1 to change, 0 to destroy`** -- **ONE** `aws_lambda_function`
change per root, never two. **THE `Cell=IB-s-14`/`IB-s-11` VALUE IS A STALE `.tf` TAG THE ROUND-7 CELLS DID
NOT REWRITE.** It equals the deployed tag, so it is not a plan change and not a separate artifact. There is
no pre-round-7 drift. **It is the sibling round-7 build, wearing an old label.**

> ### ⛔ AND MY THIRD CLASS WAS NOT MERELY A PHANTOM -- IT WAS A WIDENING, WHICH IS THE WORSE FAILURE
>
> I keyed it on the TAG: *"admitted ONLY when the changed resource's own TAGS name `IB-s-14` or
> `IB-s-11`"*, and defended that as **"closed by a tag READ FROM THE PLAN rather than asserted."**
> ⛔ **A TAG KEY IS LOOSER, NOT SAFER.** It would admit any genuinely-unintended `IB-s-14`-tagged artifact,
> where the packet/SHA key **STOPs** on it. **I treated READ-FROM-THE-INSTRUMENT as equivalent to
> TRUSTWORTHY, and the tag is exactly the field that was stale and misattributing. A STALE FIELD READ
> ACCURATELY IS STILL STALE.**
>
> ⛔ **AND I DID IT INSIDE THE SECTION WHOSE OWN ARGUMENT IS THAT A BOUND RELAXED WHEN IT FIRES IS
> WIDENING-BY-SILENCE.** I authored the looser key myself, one level up, in the same document, while
> warning against it.
>
> ⚠ **THE INHERITANCE ERROR, NAMED PRECISELY BECAUSE MY OWN LOG MISSTATED IT:** I wrote that the claim
> rested on *"two independent worker rows corroborating on a MECHANISM."* **They corroborate on the
> MECHANISM -- a shared artifact bucket makes sibling builds visible in every plan -- AND THEY CONTRADICT
> ON THE ATTRIBUTION.** `W1-S45` (export worker) read it as a SIBLING BUILD and was right; `W4-S46`
> (holdings worker) read it as a PRE-ROUND-7 cell via the stale tag and was wrong. **I read "they agree"
> off the mechanism and carried an attribution only ONE of them made.**
> ⭐ **KEEPABLE: TWO ROWS CAN CORROBORATE ON A MECHANISM WHILE CONTRADICTING ON ITS ATTRIBUTION, AND
> "THEY AGREE" IS THEN TRUE AND USELESS.** Corroboration is per-CLAIM, never per-row. **COST:** name the
> exact proposition each source supports before counting them as two. **NON-APPLICATION:** sources that
> assert one indivisible claim.

**RE-SIGNED CONSTRUCTION, PACKET-KEYED, AS `2.0.0_SA_COO~B` RE-SIGNED ITS OWN HALVES @`3143723f66`:**

1. The **6 non-round-7 roots** (api, core, directory, intake, narrative, ycharts): **EMPTY** after the
   `{plan .timestamp; S3 data-source version_id/last_modified}` subtraction.
2. The **sibling round-7 roots**: admit **EXACTLY each sibling cell's FULL DECLARED CHANGE SET, keyed to
   the sha and resources pinned in THAT cell's own signed packet** -- and nothing else. ⭐ **This covers
   more than the function build:** at HEAD, with all four drained, the **export** sibling root also shows
   `IB-rtg-1`'s `aws_iam_role_policy.export_render_receipt ["create"]`, which `W4-S46`'s PRE-DRAIN read
   could not see, so a sibling's ten-root plan now reads export as **`1 add + 1 change`**. That gap was
   `2.0.0_SA_COO~B`'s own and it closed it in the re-sign.
3. **A STOP on anything outside those enumerated per-packet sets.** Applies SEQUENCED; a final
   all-ten-roots plan reads CLEAN.

⭐ **THE KEY IS THE PACKET, NEVER THE TAG** -- the admission is "this resource's after-state equals what a
SIGNED packet pins", which is a content match against a document both halves name, not a label the
producer happens to carry.

⚠ **MY SAFETY REQUIREMENT STANDS VERBATIM AND `2.0.0_SA_COO~B` KEPT IT:** the applier pins
`source_code_hash`/`s3_object_version` to its OWN declared build, a STOP on anything outside the
enumerated per-packet sets, **never carrying a sibling forward** -- enforced by the packet, not the tag.

⚠ **UNCHANGED:** the four packet blobs (`b515836bb4`, `26360553eb`, `1a1b7b2709`, `74a1004fde`), s.3's
writer census, s.4's blast radius, and every other section of this half.

## 2-SUPERSEDED. RETAINED UNDER R-43 -- WHAT THIS SEAT FIRST SIGNED, AND IT WAS WRONG

## 2. THE ARM (d) CONSTRUCTION -- CONCUR, WITH ONE NAMED ADDITION THAT THIS PROJECT'S OWN ROWS FORCE

`2.0.0_SA_COO~B` (98619) proposed the multi-cell arm (d) as three parts: the **6 non-round-7 roots**
(api, core, directory, intake, narrative, ycharts) EMPTY after the `{plan .timestamp; S3 data-source
version_id/last_modified}` subtraction; the **up-to-3 sibling round-7 roots** admitting EXACTLY their own
declared build pinned to a sha named in that cell's own signed packet **and NOTHING else**; a **STOP** on
anything else; applies SEQUENCED; a final all-ten-roots plan reading CLEAN.

**I CONCUR WITH THAT CONSTRUCTION.** It is a widening stated out loud and bounded by an enumeration, it
mirrors the `rtf-13` @`0a7f61ae86` "widening off the empty set" shape this seat ruled earlier today, and
the shared-bucket mechanism that makes it necessary is measured rather than assumed -- `IRPT_BCKEND-W1-S45`
proves a sibling's `build-and-upload.sh` reaches the SHARED artifact bucket with no git involvement, so it
is visible in every other worktree's plan the moment it runs.

> ### ⛔ BUT AS WRITTEN THE CONSTRUCTION IS FALSIFIED BY THIS PROJECT'S OWN MEASURED ROWS, AND I AM NAMING
> ### THE ADDITION RATHER THAN LETTING IT BE RELAXED AT APPLY TIME
>
> **`IRPT_BCKEND-W4-S46`** records that a ten-root plan found the **export** and **performance** roots
> carrying a pending `Plan: 0 to add, 1 to change, 0 to destroy` whose diffs are tagged **Cell `IB-s-14` /
> Outcome FWD-8** (export) and **Cell `IB-s-11` / Outcome FWD-3** (performance) -- **PRE-ROUND-7 cells**,
> unrelated to any round-7 edit.
>
> **Export and performance ARE round-7 roots** (`rtg-1`, `rtg-3`). So each of those two roots will show its
> own declared round-7 build **AND** a pre-round-7 drift that is NOT that declared build. **By the
> construction's own words -- "EXACTLY their own declared build ... and NOTHING else", with "a STOP on
> anything else" -- that pre-existing drift TRIPS THE STOP.**
>
> **THAT LEAVES EXACTLY TWO OUTCOMES AND BOTH ARE BAD:** the arm stops on drift nobody intends to fix this
> round, or the arm gets quietly relaxed at apply time by whoever is holding it -- **and a bound relaxed at
> the moment it fires is the widening-by-silence NEVER#1 exists to prevent.**
>
> ⭐ **THE ADDITION, AND IT IS AN ENUMERATION RATHER THAN A LOOSENING: the arm admits a THIRD, CLOSED
> CLASS -- the PRE-ROUND-7 drift already present on the `export` and `performance` roots, admitted ONLY
> when the changed resource's own tags name `IB-s-14` (export) or `IB-s-11` (performance), and NOTHING
> else. A STOP stands on anything outside all three classes.** The class is closed by the TAG, which is
> read from the plan rather than asserted, and it covers two named roots and two named cells -- it does not
> generalise to "pre-existing drift is fine".
>
> ⚠ **AND THE ADDITION IS EXPLICITLY NOT AN AUTHORIZATION TO APPLY THAT DRIFT.** It authorizes the arm to
> SEE it without stopping. Whether `IB-s-14`/`IB-s-11`'s builds should be applied at all is a different
> question, belongs to those cells, and is NOT signed here. If a sequenced round-7 apply would itself carry
> that drift forward on the same root, **that is a STOP and this half does not cover it** -- the applier
> pins `source_code_hash`/`s3_object_version` to its OWN declared build or it does not apply.

**LIMIT OF MY OWN VERIFICATION, STATED RATHER THAN IMPLIED:** I did not re-run the ten-root plan. The drift
claim rests on **two independent worker rows measured on different roots** -- `W1-S45` (worker ~1, seeing
sibling builds from its own worktree) and `W4-S46` (worker ~4, reading the tags on export and performance)
-- which corroborate each other on a mechanism rather than repeating one read. **`2.0.0_SA_COO~B` re-signs
its own halves to match this construction, per its own offer in 98619; until both halves at HEAD carry the
SAME three-class enumeration, the sequenced applies do not proceed.**


## 3. THE WRITER CENSUS, WHICH IS THE CLAUSE I CHECKED FIRST

NEVER#1: *"FIRST COUNT THE WRITERS OF THE NAMED PROPERTY: a property with N writers needs N rules read,
and N is a number the half PRINTS."*

**This packet prints it:** N = 1 in PRODUCTION (intake/poller.py:299, checkpoint.ScanLease) and N = 0 for every OTHER (tenant, job) shape -- stated as a SUBTRACTION over the shape space rather than a forward list of writers the author recalled.

⭐ **Read and accepted.** The failure this clause exists to catch is `NFRA_CLDGRPH` W2-S67/S98 -- both
halves correct and complete about ONE producer's rule on a surface a SECOND writer also set.

## 4. THE BLAST RADIUS, BOTH BRANCHES

- **APPLIED.** `irpt-status` moves to the built `CodeSha256` this packet names (B0AmyfRK (per the issuance; the half binds the packet, not this abbreviation)), on the `ops/status` root
  only. The packet's own branch analysis is read and adopted; it covers the forward case AND the case where
  the served path never reaches the changed code.
- **NOT APPLIED / ROLLBACK.** CodeSha256 O3TyGqfqjiwZP9OSXmryonnAst+SbYMLzyuSGphOyCE= re-published via Terraform from its matched S3 object version, NEVER `aws lambda update-function-code`. Verified by reading the served `CodeSha256` back after the
  rollback -- the same discriminator the forward arm uses, not a producer self-report.
- **UNAFFECTED.** Every other root's own state; every grant not named in this packet.

## 5. WHAT THIS HALF DOES NOT COVER

- **It does not authorize an apply of anything but this cell's own declared build**, pinned by
  `source_code_hash`/`s3_object_version` to the sha this packet names.
- **It does not cover a `--month`-style or any other override** that would let a producer run off its own
  clock; no such path is named in this packet and none is signed.
- **It does not cover the pre-round-7 drift's APPLICATION** (s.2's ⚠), nor any second-pass act whose blast
  radius differs from this packet's.
- **It does not grade any acceptance criterion.** Terminality reads the PROOF, not this half.
- ⛔ **It expires against the bytes, not the path:** this half names a BLOB. If the packet is re-committed,
  this half does not cover the new one and is re-signed, per the hash-bound-half-goes-stale class.

## 6. VINTAGE AND PUSH STATE

Signed `1.0.0_SA_CTO`, 2026-09-20, against the packet blob named in s.1, verified at HEAD this run with
`git rev-parse HEAD:<path>` and `git cat-file -s`. Push state is stated in the commit that carries this
half and is re-measured at send, never carried forward.
