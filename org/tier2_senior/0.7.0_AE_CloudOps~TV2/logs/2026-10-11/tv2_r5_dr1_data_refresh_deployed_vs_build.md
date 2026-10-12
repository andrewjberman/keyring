# The data-refresh deployed bytes equal their build input — 0.7.0_AE_CloudOps~TV2

**archetype:** READ

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-READ-R5-dr1.data-refresh-deployed-vs-build-input-dell2 (read at `c4374e733d`)
**Status:** COMPLETE — `MEMBERS 2 EQUAL 2 DIFFERENT 0 NOT_IN_SOURCE_DIR 0`; AC1 `DR1-MEMBERS-OK`

---

## Objective

One read, nothing written to AWS: download `opal-data-refresh-api`'s deployed package, compare it member by
member with its build input at the commit the source map records, and state what the deployed
`validate_user_type` admits. Closes the condition the CTO's round-5 analysis set on ARMED row
`TCKT_VNEXT-D2-W6-S2`: *"Equal closes the row; unequal comes back as a release under a pair."*

**It is equal.** No ledger was opened — this is a read, and the order says to open none.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| aws lambda get-function-configuration | on one function | PASS | `qHMjXkK1…`, matching the issuer's read |
| curl + zipfile + hashlib | download, hash zip and members | PASS | **zip sha256 in base64 == live CodeSha256** |
| git show (from bash, `MSYS_NO_PATHCONV=1`) | member at the recorded commit, and at HEAD | PASS | after a CR failure — below |
| **git ls-tree** | the source dir at the recorded commit | **PASS, and decisive** | the control that caught my false ABSENT |
| the source map | read live, not taken from the order | PASS | 2 files, commit `d9539cc0b7…` |

**What worked:** proving the download *is* the deployed artifact before diffing anything. `CodeSha256` is the
base64 of the package's sha256, so one comparison turns every member hash from a statement about a file into
a statement about running bytes.

**What failed:** my first pass reported **both members ABSENT at the recorded commit** — and it was my
instrument, not the world. See below.

**Gap found:** none to file. The one trap hit is already named twice in CLAUDE.md.

---

## The control that changed the answer

The member names came from a Windows `python print`, so each carried a trailing **CR**. `git show` was asked
for `lambda_function.py\r`, returned rc 128, and echoed the argument back with the CR rendered as `?`:

```
fatal: path 'infra/aws/lambda/data_refresh/check_triggered_by.py?' does not exist in 'd9539cc0b7...'
```

The positive control CLAUDE.md requires beside any ABSENT verdict — `git ls-tree` of the directory at that
same commit — listed **both files present**. That contradiction is what exposed it. I stripped the CR,
verified the bytes with `od -c`, and both files resolved at rc 0 with sizes matching the deployed members
exactly.

**Had I skipped the control**, this read would have reported
`MEMBERS 2 EQUAL 0 DIFFERENT 0 NOT_IN_SOURCE_DIR 2` — the exact shape of *"the deployed package contains
nothing from its source dir"* — and escalated a release problem that does not exist. An early stop and a true
absence read identically; so do a mangled argument and a missing file.

No surprise row: the corruption oracle (echo the argument back) and the rule about `git show` returning
clean-empty both already hold this hazard, and both worked as written.

---

## Verification

```
STEP 1  live CodeSha256 qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=
        LastModified 2026-10-09T07:59:39Z, python3.11
        map entry: source_dir infra/aws/lambda/data_refresh
                   files [lambda_function.py, check_triggered_by.py]
                   artifact_sha256 == live, last_deployed_commit d9539cc0b7...

STEP 2  zip 20716 bytes, sha256 a873235e42b5ff53...
        base64 of that digest == live CodeSha256   <- the download IS the deployed artifact
        MEMBER COUNT 2 (exactly the map's 2 files, so NOT_IN_SOURCE_DIR is measured, not assumed)

STEP 3/4  member                  size    deployed          commit            HEAD
          check_triggered_by.py   1825    7e813322799f4f7a  7e813322799f4f7a  7e813322799f4f7a  EQUAL
          lambda_function.py      83888   ead1011f45b91912  ead1011f45b91912  ead1011f45b91912  EQUAL

        MEMBERS 2 EQUAL 2 DIFFERENT 0 NOT_IN_SOURCE_DIR 0
        all three planes agree on both members
        built-not-deployed changes at HEAD: NONE
        nothing normalised -- raw bytes hashed

STEP 5  is_opal_internal    deployed line 142
        validate_user_type  deployed line 168   (file is 1956 lines, 83888 bytes)
```

### The three sentences

1. **Admitted userType values:** exactly one — `Dev`, by exact match. Any other value is admitted only if the
   principal is independently Opal-internal (`tier == 'internal'` or `firmId == 'opal-capital'`).
2. **A caller with NO userType:** **not admitted** on that basis. Missing/empty/`'null'` normalises to `''`
   (line 204) and is refused (line 220) unless `is_opal_internal` returns True. **This is the question row
   W6-S2 armed, and the deployed bytes answer it closed.**
3. **A caller with tier `internal` and any userType:** **admitted** — `is_opal_internal` returns True on
   `tier == 'internal'` before userType is consulted again.

Two defensive details in the deployed bytes: `firmId` is compared by exact match because the authorizer
defaults it to the *string* `'null'` (`if firm_id` would be True for it); and Method 3, no authorizer context
at all, fails **closed** where it previously returned True as `dev@test.com`.

---

## Decisions Made

1. **Proved the download was the deployed artifact before diffing.** Without that, two equal hashes would only
   say a zip matches a commit — not that the *running* code does.
2. **Ran `git show` from bash, never from python argv.** CLAUDE.md routes python-spawned MSYS binaries through
   `msys_argv_guard`; writing outputs to files from bash sidesteps the argv plane entirely. The CR still bit
   me one layer up, in the filename list.
3. **Took the control's word over my own first result.** Two ABSENTs looked like a finding; the control said
   the files were there, so the instrument was wrong, not the world.
4. **Filed no surprise row.** The trap is already law, twice over, and behaved as documented. Filing it would
   add noise to a channel that exists for spec-versus-world gaps.
5. **Said what the read does not settle.** Whether `tier == 'internal'` is reachable by a caller who should
   not hold it is a property of the *authorizer*, not of this function — and I read one function's bytes.
6. **Called no route and minted no token.** The rule is read from code; ABSENT of a live refusal is not
   evidence of one. This function's 9 routes are a write path the FWD-1 runner is itself forbidden to probe.
7. **Deleted my downloaded copy** after writing the result, as step 6 asks — my own temp file; nothing in the
   repository or in AWS was removed.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r5_dr1/members.json`, `…/DATA_REFRESH_DEPLOYED_VS_BUILD_INPUT_20261011.md` | this commit |
| proof_of_spec, this log, TO status | this commit |

No AWS write, no code change, no ledger entry.

---

## Blockers

None owed by this seat. The row's disposition is `1.0.0_SA_CTO~DELL2`'s; this read supplies its closing
condition and changes no row.

---

## Current State

`opal-data-refresh-api` is running exactly the bytes its source map's commit holds, and exactly what this
tree's HEAD holds — three planes, both members, byte-identical. The admission rule that row
`TCKT_VNEXT-D2-S17` read in the tree is the rule in production: a missing userType does **not** admit, an
Opal-internal principal does, and an unauthenticated call is refused rather than recorded as a fictional
actor.

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` dispositions row `TCKT_VNEXT-D2-W6-S2` on this read.
2. If the authorizer's minting of `tier`/`firmId` is to be examined, that is a different plane and a
   different order.
