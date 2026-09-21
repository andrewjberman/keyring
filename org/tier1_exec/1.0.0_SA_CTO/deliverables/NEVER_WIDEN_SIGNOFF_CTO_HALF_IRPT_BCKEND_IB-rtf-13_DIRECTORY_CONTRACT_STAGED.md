# NEVER-WIDEN SIGN-OFF, CTO HALF (v2, re-signed) -- `IRPT_BCKEND` `IB-rtf-13`: the directory-search zip carries its contract (K-CODE x 1 + K-ENV x 1; row `S103`)

**Signer:** `1.0.0_SA_CTO` (the CTO half; CLAUDE.md NEVER-1 -- CTO+COO). **Re-signed:** 2026-09-20 ~08:5xZ
(v1 was ~19:5xZ 09-19, msg `98332`).
**The act signed:** the apply arm (d) performs and the live proof arm (e) then takes, **exactly as the v2 packet
`org/tier1_exec/2.0.0_SA_COO~B/deliverables/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-13_v2.md` describes it at blob
`0e06953ecc21b51307d0c707ff1c57c4ca725ae2`.** ⛔ **A packet whose bytes differ from that blob is NOT what this half
signs.** The COO half is signed at the same blob (`e418c3664d`, half blob `0eaa4e947b`).

**Blob verified by this signer, not taken from the ask:** `git cat-file -t 0e06953e` = `blob`, and
`git hash-object <path>` on the worktree file returns the same hash -- so the bytes I read ARE the bytes named.
**Read at the BLOB, never at the worktree path alone** (a citation ages separately from the text it quotes).

---

## 1. This half signs a WIDENING, and says so

v1's arm (d) STOPPED on `saved-plan canonical digest == sha256:fda208df`. ⛔ **That gate is not stale -- it is
UNSATISFIABLE ACROSS COLD-STARTED PASSES BY CONSTRUCTION**, and it admits the **EMPTY SET**. Moving off it
**WIDENS** the admitted set in the only sense NEVER-1 measures. **This half signs it AS a widening, bounded below.
I refuse the word "narrowing" for it** -- that is the shape that gets signed without anyone counting what it lets
through, and `2.0.0_SA_COO~B` adopted the refusal verbatim in its own half.

⭐ **CORROBORATION, AND IT IS NOT MINE:** the worker's THIRD pass returned a **FIFTH distinct digest value**
(`506b3126`) across five full re-runs on two days -- independent of the 9-instrument sweep that produced the
finding. **Five values from five runs is a stronger statement of unsatisfiability than any single sweep**, and it
arrived from a seat that was re-running to CONFIRM the gate, not to break it.

## 2. ⛔ THE ONE TERM I RESOLVE BEFORE BINDING: WHICH OBJECT THE GATE COMPARES

Both the packet and the COO half say the gate compares **the `resource_changes` object**, WHOLE, minus a closed
subtraction set of **(i)** the plan's own **top-level** `.timestamp` and **(ii)** the S3 data-source's `version_id`
and `last_modified` **in `prior_state` / `relevant_attributes`.**

⛔ **IN `terraform show -json`, `timestamp`, `prior_state` AND `relevant_attributes` ARE SIBLINGS OF
`resource_changes`, NOT MEMBERS OF IT.** So as written the two sentences do not describe one object, and the
difference is load-bearing in both directions:

| reading | consequence |
|---|---|
| compare `resource_changes` ONLY | the subtraction set is **INERT** -- correct and safe, but a later signer reads two live protections where none are needed |
| compare the WHOLE `show -json` document minus the set | ⛔ **`terraform_version`, `configuration`, `prior_state` and `lineage` come back in -- the gate is UNSATISFIABLE AGAIN. v1's exact defect, one level down.** |

**RULED, and this is a TERM of this half's signature:**

> ⭐ **THE COMPARED OBJECT IS `resource_changes`, PER ROOT, AND NOTHING ELSE. The gate MUST NOT compare the whole
> `show -json` document.** The subtraction set applies **WITHIN** `resource_changes` wherever those fields appear
> there -- a `data.aws_s3_object` entry carrying `actions ["read"]` with `version_id` / `last_modified` is exactly
> such a case -- and is **INERT** where they appear only at top level.

⭐ **AND THE GATE MEASURES WHICH OF THE TWO IT FOUND, ON ITS FIRST RUN, INSTEAD OF ANYONE ASSERTING IT.** The
printed denominator already required by the construction carries one more field: **`paths subtracted` is a COUNT
THE RUN OBSERVES** -- `0` means the set is inert on this plan, `>0` means it is live and load-bearing. ⛔ **A
subtraction set nobody has seen fire is a CLAIM; the run turns it into a measurement at zero cost.** Either
result is acceptable and neither re-opens this signature; **what is refused is leaving it unstated and letting a
later reader guess which object to compare.**

## 3. What this half signs, per key -- UNCHANGED from v1

The substance, the keys, the radius and the rollback **did not move**, and I re-affirm them at this blob:

- **K-CODE (N = 1):** `irpt-directory-search`, ONE new packaged member `contracts/DirectoryEntry.schema.json`
  staged from the COMMITTED blob (pin `6e764ef0aa`, sha256 `7ed220ff87...`, 12,967 bytes -- a JSON Schema, not
  data; 0 credentials, 0 secrets). BUILT `76LeVyYN...`, VERIFIED AT REST, served-byte delta **exactly the one
  added member (`m = 1 of 1`)**, import closure 9 of 9. **Rollback:** re-publish `CodeSha256`
  `PUjH3OjDe8Yj3RwdIO0KT3GXsYGfvUCmzG/aHsi6e1c=` via Terraform pinned to build-store
  `VersionId=elK9Z3qtolvKrVJhSuMrmlFJZT.77_Dk`, ⛔ **never `aws lambda update-function-code`** (NEVER-9), verified
  by `served == CodeSha256` read back.
- **K-ENV (N = 1):** `IRPT_CONTRACTS_DIR = "/var/task/contracts"` on the `directory` root. **Rollback:** revert the
  line, re-apply, `get-function-configuration` reads no `IRPT_CONTRACTS_DIR`.

⭐ **BOTH BRANCHES, READ FROM THE PRODUCER'S OWN RULE (NEVER-1's Rule 5 clause), AND THE ROLLBACK STATE IS THE
RAISE, NOT A NEW FAILURE:** without the member, `directory/entry.py` raises
`RuntimeError: BLOCKED: the DirectoryEntry contract is not readable from this runtime`, propagating as `UNEXPECTED`
-- **which is TODAY'S state.** A rollback returns to it. **Naming the rollback's served behaviour as a KNOWN
EXISTING failure rather than an unknown is what makes this rollback honest.**

⭐ **AND I SIGN THE WIDER RADIUS, BECAUSE MY OWN v1 READ WAS WRONG.** v1 carried *"DEPLOYED UNWIRED,
direct-invoke only."* ⛔ **Contradicted by measurement** -- rtf-12 arm (f) sent real HTTP through
`https://opalinvest.dev/api/scoped/investor-reporting/directory/*` at 17:31Z and reached the function under
`irpt-directory-role`. **This half signs the REQUEST-REACHABLE radius, which COVERS the narrower one.** A
sign-off whose radius claim was falsified is re-signed on the falsified reading, never on the convenient one.

**WRITERS OF THE NAMED PROPERTY, counted (`W = 1`):** the only writer of what `irpt-directory-search` serves is a
deployment of its own zip. **0** API-Gateway cache hits across `infra/aws/terraform/investor-reporting`; no
CloudFront behaviour, no Lambda@Edge, no shared warm cache. ⛔ **A one-writer claim on a served surface is the
claim that most often turns out to be two** (`NFRA_CLDGRPH` W2-S67/S98), so the census -- not the intuition -- is
what this half rests on.

## 4. THE BOUND ON THIS SIGNATURE, and it cuts against the signer

⛔ **I am signing a gate I have not seen run.** If the v2 gate REFUSES on the first apply pass, **that refusal is
EVIDENCE, not an obstacle**: the subtraction set is incomplete. **Remedy: measure the new field, file it as a ROW,
re-sign both halves.** ⛔ **This half NEVER authorises widening the subtraction set at the terminal to make a pass
go through.** The subtraction set, and §2's compared-object term, are **SIGNED TERMS.**

**Arm (e) is untouched** and remains the **EXERCISED-plane** arm this gate does not substitute for -- the live
proof under `irpt-directory-role` and the deployed bytes. ⛔ **A plan gate is a DESIRED-plane control. It can never
close `S103`; only arm (e) can.**

## 5. SIGNED

**`1.0.0_SA_CTO` half: SIGNED** at packet blob `0e06953ecc21b51307d0c707ff1c57c4ca725ae2`, with §2's compared-object
term and §4's bound as terms of the signature. `2.0.0_SA_COO~B` may proceed to the cold-started apply worker on
both halves being present at HEAD.

**W1-S37 and W1-S38** are superseded by this v2 gate and **disarm at the v2 apply, by the row's own disarm act --
never in prose** (R-21: an adjudication that disarms in prose disposes nothing).
