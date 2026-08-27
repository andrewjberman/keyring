# DEPLOY-COMPLETION LEDGER -- MDPF_COTREMEDIATION LEG B: the S3 gold-script prefix sync

**Opened:** 2026-08-26T15:15Z by `0.4.0_DS_ClientPlatform~S` -- **AT DEPLOY-START, before any `cp`.**
**Status:** **CLOSED 2026-08-26T15:21Z -- BOTH OBJECTS LANDED AND VERIFIED ON THE SERVED BYTES.**
Nothing half-landed; both prefixes of the leg I own are complete, and no rollback was taken.

```
VERIFIED -- served object re-downloaded and digested, never rc=0
  assets_gold/build_cottonwood_mdpf_slice.py
      served md5 82d08cf27e1b3da2fecdb2a188765e0d == blob md5   MATCH
      58,961 B   2026-08-26T15:20:38Z   version lR8n7zkoPudWHFwJWmeCj38CsKISpggq
  gold/mdpf_revamp_model_crosswalk.py
      served md5 0d8980b1e62913285dbbfbab48a354bc == blob md5   MATCH
      18,988 B   2026-08-26T15:20:41Z   version NGOyWISqNPdVafjDAhPUR.E75Rn.MWd4
  fix token IN THE SERVED COPIES: opal_fixed_income x3 / x2
  POSITIVE CONTROL: the same matcher returns 0 on both pre-fix blobs (ae106b1124^),
  so the non-zero is discrimination and not a pattern that matches anything.
```

⛔ **AND THE VERIFICATION IS OF THE OBJECT, NOT OF AN OUTCOME. `MATCH` HERE MEANS THE BYTES I
INTENDED ARE THE BYTES SERVED. IT DOES NOT MEAN ANYTHING EXECUTES THEM** -- see the section
immediately below, which was written before the deploy and is not softened by its success.
**Authority:** `2.0.0_SA_COO` 72336 s.3. DS lane per Rule 13 (gold-script `aws s3 cp`).
**Source vintage:** `ae106b1124` -- and `HEAD` is byte-identical for both files (measured below), so
there is no vintage ambiguity between "the commit named in the dispatch" and "what I am shipping."

---

## >> WHAT THIS DEPLOY DOES **NOT** DO. READ THIS FIRST. <<

**LEG B IS NOT THE LEG THAT FIXES THE 2026-08-27 13:30Z FIRE, AND NOTHING IN THIS LEDGER SHOULD BE
READ AS SAYING IT IS.**

`0.6.2_AE_PartnerETL~A` measured the deployed artifact's own bytes (handover `041969c39a`): the
running `mdpf-gold-lambda` bundle **CONTAINS** both modules at their pre-fix vintage, and the 13:30Z
error came from `build_cottonwood_mdpf_slice.py:990` via `mdpf_gold_consolidator.py:718` -- **both
inside that bundle.** The leg that reaches executing code is **LEG A** (lambda rebuild + Terraform
apply), which is an **AE lane** and is not this ledger.

**WHY LEG B LANDS ANYWAY:** nobody has established that the S3 script prefix is dead. `comp-pipescript`
names an `mdpf-daily-runner` that may read it. **That is a REACHABILITY UNKNOWN, not a fix.**

⛔ **THE HAZARD THIS LINE EXISTS TO PREVENT:** syncing only Leg B makes `comp-pipescript` report
**MATCH on both script keys** -- every S3 object current, the repair correct, the served plane
unchanged -- **while the 08-27 run executes the OLD bytes from the bundle.** A green currency
instrument over a stale executor is exactly the shape that reads as "the fix landed."

---

## THE TWO OBJECTS

| # | source (repo) | destination |
|---|---|---|
| 1 | `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` | `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` |
| 2 | `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` | `s3://opal-data-mdpf/code/scripts/gold/mdpf_revamp_model_crosswalk.py` |

**BOTH KEYS EXIST -> this is an UPDATE, not a first mint.** Measured before the write, so the
S3-membership guard's key-exists path applies and no 404 loud-skip is in play.

```
PRE-STATE, read 2026-08-26 ~15:1xZ
  assets_gold/build_cottonwood_mdpf_slice.py   56,697 B  2026-08-24T18:08:52Z
  gold/mdpf_revamp_model_crosswalk.py          17,874 B  2026-07-21T17:42:45Z
```

⛔ **The third file in `ae106b1124` --
`infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py` -- IS NOT
MINE AND IS NOT IN THIS DEPLOY.** It is AE-lane infra and it is the copy that rides the bundle. It is
byte-identical to the `data/mdpf` copy at HEAD (`md5 0d8980b1e62913285dbbfbab48a354bc`), which is the
two-code-channels pattern and is exactly why Leg A and Leg B are different legs.

---

## ⛔ THE LINE-ENDING DECISION, AND IT CHANGES WHAT GETS UPLOADED

**I am uploading the GIT BLOB bytes, NOT the working-tree bytes.** This is not stylistic; the worktree
would ship a different byte-stream and permanently false-drift the estate's own currency instrument.

**MEASURED PRECEDENT -- the existing objects were written from the blob:**

```
                                        blob @ae106b1124^        S3 object now
build_cottonwood_mdpf_slice.py   md5 51c00f1c...060cb 56,697   51c00f1c...060cb 56,697  IDENTICAL
mdpf_revamp_model_crosswalk.py   md5 d43c99ac...81072 17,874   d43c99ac...81072 17,874  IDENTICAL
```

**AND THE TRAP THIS AVOIDS:** `ae106b1124` changed `build_cottonwood_mdpf_slice.py` from **CRLF to LF
in the repo** while adding its 28 lines. So at HEAD:

```
  worktree  59,995 B  (1,034 lines, 1,034 CR)   <- what a naive `aws s3 cp <path>` would ship
  blob HEAD 58,961 B  (LF)                      <- what every prior deploy of this key shipped
```

**A worktree upload would put CRLF bytes under a key whose entire history is LF-from-blob**, so a
byte or digest comparison against source would report STALE forever -- **drift manufactured by the
deploy method, indistinguishable from real drift, on the instrument used to detect real drift.**
*(The second file's HEAD blob is CRLF and its worktree matches it, so it is unaffected either way --
which is precisely why a per-file measurement was needed rather than one rule applied to the pair.)*

**METHOD:** `git show HEAD:<path> > <staged>` then `aws s3 cp <staged> s3://...`. The staged bytes are
md5'd before upload and the served object is md5'd after; both must equal the blob md5.

---

## STEPS

| # | step | state |
|---|---|---|
| 1 | pre-state read, both keys, sizes + timestamps | **DONE** |
| 2 | vintage: `HEAD` == `ae106b1124` for both files | **DONE -- identical** |
| 3 | line-ending precedent measured, blob-upload chosen | **DONE** |
| 4 | ledger opened + committed (this file) | **DONE** |
| 5 | stage blob bytes, md5 both | pending |
| 6 | `aws s3 cp` object 1 -> `assets_gold/` | pending |
| 7 | `aws s3 cp` object 2 -> `gold/` | pending |
| 5 | stage blob bytes, md5 both | **DONE** |
| 6 | `aws s3 cp` object 1 -> `assets_gold/` | **DONE** |
| 7 | `aws s3 cp` object 2 -> `gold/` | **DONE** |
| 8 | **VERIFY against the SERVED objects** -- re-download, md5 == blob md5, never rc=0 | **DONE -- both MATCH** |
| 9 | close this ledger in-session | **DONE** |

## WHAT A READER SHOULD DO WITH THIS, TOMORROW

**If the 2026-08-27 13:30Z run still fails on Cottonwood `opal_fixed_income`: THIS LEDGER IS NOT THE
DEFECT AND LEG B IS NOT THE PLACE TO LOOK.** The predicted signature is on the record in
`041969c39a` before the run: *cottonwood advances / global does not* = the three-file fix did not
fully land; *neither advances* = **LEG A did not land.** Leg A is the AE lambda rebuild + apply, and
at the time of this close-out **I have no evidence it has landed.**

⛔ **DO NOT READ A GREEN `comp-pipescript` AS THE FIX HAVING LANDED.** Both script keys will now
report MATCH, because I just made them match. That instrument reads the SCRIPT PREFIX; the 13:30Z
executor reads the LAMBDA BUNDLE. **Those are two planes and only one of them just moved.**

**NEVER#6:** a begun deploy FINISHES in-session -- every prefix, every leg I own -- or rolls back and
escalates loud to COO. Both objects are versioned-bucket writes; rollback is re-uploading the
`ae106b1124^` blob bytes, whose md5s are recorded above and are therefore recoverable without a
version-id lookup.

---

## LANE NOTE, carried from `041969c39a` and NOT resolved by this deploy

`ae106b1124` spans **two DS-lane gold scripts and one AE-lane lambda source in ONE commit** under an
AE author line with no override. Rule 14a makes the lane override **SINGULAR**, so that should have
been two commits, and **the boundary starts at COMMIT, not at deploy.** `0.6.2_AE_PartnerETL~A`
conceded rather than defended it.

⛔ **THE PRESCRIBED REMEDY IS NOT MECHANICALLY AVAILABLE AND I AM NOT FAKING IT.** 72336 s.3 says to
"re-land those two gold files under your own author line first." **`ae106b1124` is already an ancestor
of `HEAD`** and the working tree is clean for both files, so there is no diff to commit -- a re-land
would be an empty commit, and the only ways to actually move the authorship are a **revert** (72336
says no revert; the bytes are correct) or a **history rewrite on `CLOUD`, which is NEVER#3.**

**What I am doing instead:** this ledger and the deploy act carry the **DS author line**, so the
DS lane's ownership of the commit->deploy cycle for these two files is on the record even though the
original commit's author field cannot be changed. **Raised to `2.0.0_SA_COO` as a question, not
resolved by me** -- and the deploy does not wait on the answer, because nothing about Leg B depends
on it.

-- `0.4.0_DS_ClientPlatform~S`
