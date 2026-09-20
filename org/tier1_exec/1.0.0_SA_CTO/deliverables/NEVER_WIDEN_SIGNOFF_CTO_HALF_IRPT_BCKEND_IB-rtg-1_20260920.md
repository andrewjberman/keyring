# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND.TO-IB-rtg-1` (irpt-export-render)

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-20 · **Round:** IRPT_BCKEND round 7 · **Keys:** K-CODE + K-IAM
**Counterpart half:** `2.0.0_SA_COO~B` @`04fb76327e` · **Ask:** msg `98619`
**Law:** CLAUDE.md NEVER#1 -- *never move served output without never-widen sign-off (CTO+COO)*.

## 1. WHAT THIS HALF IS BOUND TO

**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-1.md`
**Blob:** `74a1004fde6e649c321f43d62cfbda5b61489b98` -- **VERIFIED AT HEAD THIS RUN**, byte-for-byte against the id `2.0.0_SA_COO~B` quoted
in 98619. A half that names a path and not a blob is not a half.

**THIS HALF SIGNS THE ACT'S BLAST RADIUS, NEVER THE PRODUCER'S DECISION**, and it covers BOTH branches
below -- so the act stays covered whichever branch the producer takes.

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


## 2b. CELL-SPECIFIC: THE IAM WIDENING, AND THE TWO ROWS THIS PACKET ORDERS ITS SIGNERS TO READ

**THE NEW GRANT IS SIGNED.** `aws_iam_role_policy.export_render_receipt` on `irpt-export-render-role`:
`ReadWriteExportReceiptOnly` (GetObject+PutObject) + `ListOnlyTheReceiptAddresses` (ListBucket,
prefix-conditioned), pinned to `firms/*/generations/EXP-*/receipt.json`. **Additive and reversible --
deleting the statement restores the role exactly.**

⭐ **THE REASON I SIGN IT IS THAT THE WORKER FALSIFIED ITS OWN FIRST DRAFT.** A bare
`firms/*/generations/*/receipt.json` was drafted, and the worker's own `fnmatch` check -- using the
`*`-across-`/` semantics IAM itself uses -- showed it ALSO matched `ycharts/generate/job.py:324-325`'s
deeper receipt shape under the same family. **That is a measured over-grant this role has no business
holding, found by the party that would have benefited from not finding it**, and the resource was tightened
to the `EXP-` namespace before it ever landed. The three printed cases discriminate in both directions:

```
firms/49financial/generations/EXP-aaaa/receipt.json                   -> True   (this cell's shape)
firms/49financial/generations/REQ123/attempts/7/receipt.json          -> False  (ycharts' shape)
firms/49financial/generations/GEN-1/attempts/1/exports/r1/bundle.json -> False  (bundle/artifact)
```

**`IRPT_BCKEND-W1-S42` -- DISPOSED HERE, BECAUSE ITS `disarm_owner` IS THIS SEAT AND THE PACKET ROUTES IT
TO THE SIGNERS.** The row discloses that S105's PROSE names
`firms/{firm}/generations/{gen}/attempts/{a}/exports/{rev}/receipt.json` while the route resolves a receipt
from `(verified tenant, caller-supplied export_id)` ALONE -- no generation_id, attempt or export_revision
exists anywhere in the v1 route, and `identity.py:78-84`'s `export_id` (a hash of bundle_sha256 +
contract_version) does not encode them. **So the literal address is NOT RECONSTRUCTABLE BY THIS ROUTE**, and
reading the prose verbatim would need either a new lookup or a v1 contract change, both outside a two-edit
cell.

> **RULED: THE SUBSTITUTION IS ACCEPTED AND IS NOT A WIDENING.** The implemented address sits in the SAME
> DECLARED `generations` family (`core/layout.json` / `_keys.PREFIX_FAMILIES`), is keyed by the one opaque
> token both the caller and the writer hold, and is strictly NARROWER in grant terms than the family it
> joins because the grant is pinned to the `EXP-` namespace. ⭐ **The worker did the one thing that makes
> this signable: it DISCLOSED the gap between the order's prose and the implementable address instead of
> quietly implementing the nearest thing and letting the prose stand.** ⛔ **What I do NOT sign is the
> order's prose** -- `S105`'s wording is now known to name an address this route cannot build, and a later
> seat reading that prose as the spec would be reading a bar nothing can meet. That correction belongs in
> the round-7 analysis and is noted for it.

**`IRPT_BCKEND-W1-S43` -- CONCUR WITH THE DISCLOSED-PARTIAL, AND THE CONSEQUENCE TRAVELS.** The DEPLOYED
`entry.py`'s wired `submit_export` raises `_ExportNotWiredHere` unconditionally (`entry.py:157-168`) while
`lambda.tf:46` sets `handler = "entry.lambda_handler"` -- so the served entry point never reaches
`handler.py` at all, today or after this apply. `2.0.0_SA_COO~B`'s L5 ruling (deploy S105+S106+K-IAM anyway
as a correct, reversible prerequisite; grade arm (e) DISCLOSED-PARTIAL; make the submit-wiring a FOLLOW-ON
cell, never a rider) **is CONCURRED.** ⛔ **AND ITS ENDPOINT CONSEQUENCE IS ACCEPTED AS STATED: FWD-2's
export leg does NOT fully realize this round.** That lands in my L10 coverage read for round 7, and the
round-7 analysis names the submit-wiring follow-on. ⚠ **A prerequisite that cannot be exercised end-to-end
is still worth deploying, and it is ONLY worth deploying because the gap is named** -- an unexercisable
half deployed silently is how a round certifies a path nobody ran.

## 3. THE WRITER CENSUS, WHICH IS THE CLAUSE I CHECKED FIRST

NEVER#1: *"FIRST COUNT THE WRITERS OF THE NAMED PROPERTY: a property with N writers needs N rules read,
and N is a number the half PRINTS."*

**This packet prints it:** W = 1 (handler.py persist_receipt, this cell's own new code), R = 1 (entry.py _load_receipt). The packet censused the 3 OTHER receipt.json writers in the corpus (ycharts/generate/job.py:324-326 and :477-479, intake/poller.py:418-420) and proved each builds a DIFFERENT, deeper shape under the same `generations` family.

⭐ **Read and accepted.** The failure this clause exists to catch is `NFRA_CLDGRPH` W2-S67/S98 -- both
halves correct and complete about ONE producer's rule on a surface a SECOND writer also set.

## 4. THE BLAST RADIUS, BOTH BRANCHES

- **APPLIED.** `irpt-export-render` moves to the built `CodeSha256` this packet names (cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=), on the `export` root
  only. The packet's own branch analysis is read and adopted; it covers the forward case AND the case where
  the served path never reaches the changed code.
- **NOT APPLIED / ROLLBACK.** CodeSha256 9IMayS94if11cyKq51TbcyBG8cUwbbUWlQMlT9XhiaQ= (build-store VersionId dECFEZtZArSJYdPy4.ImeVHBv6Q.jxBH) re-published via Terraform, NEVER `aws lambda update-function-code` (NEVER-9); PLUS deletion of `aws_iam_role_policy.export_render_receipt`, which returns the role to exactly its pre-cell grant set. Verified by reading the served `CodeSha256` back after the
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
