# The AE-lane landing of DS~C's BDPARITY bytes — and the STOP gate that fired on a stale citation — 0.7.0_AE_CloudOps~K

**Date:** 2026-08-30
**Task Order:** ad-hoc — `2.0.0_SA_COO` [DRIVE] dispatch (row 84183 here / 84184 at the issuer), ADVI_BDPARITY (D2)
**Status:** COMPLETE — landed @`27af942259`, reported (84221/84222/84223), nothing owed

---

## Objective

Land `0.4.0_DS_ClientPlatform~C`'s BDPARITY puller change, live and **uncommitted** in the shared
worktree on `infra/aws`, where `safe-commit`'s owned-paths gate refuses the DS lane
(`CLOUD_OPS_OR_ETL`). A foreign-dirty file in a shared tree is one read-that-writes from gone, and
deploy legs read the tree. **Transport act only** — the bytes are not this seat's.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate.sh | `.tools/commit-gate.sh <the .py>` | PASS | `clean for 1 of 1 file(s)`, rc=0 read **unpiped** (`$?` after a pipe is the last command's rc, not the gate's). Mandatory: the file is a `.py`. |
| safe-commit.sh | `--author … -F <msgfile>` | PASS | risk-reflex `1 file checked against 1838 danger nodes`, REFLEX CLEAN; `msg-verify MATCH len=3024`. |

**What worked:** `safe-commit`'s `msg-verify` limb is the one that matters for a `-F` message — it
confirms the committed message is the file's bytes, which is the whole reason `-F` exists.
**What failed:** nothing.
**Gap found:** none. ⚠ Explicitly NOT run: no `comp-*` inspection tool — this was a byte-identity
task, and `git hash-object` / `sha256` are the right instruments. Naming the omission rather than
leaving the row blank.

---

## Work Completed

### 1. ⛔ The STOP gate fired — and it was the point of the exercise

The dispatch step (1): diff the dirty file against the patch in `076414c9f0`; **same bytes or STOP
and say which is newer, do not pick.** They differed, measured before any byte was committed:

```
patch @076414c9f0 post-image blob   66c42cd452   != worktree
worktree blob                       0661e76dbd
HEAD blob                           13365b6003   == the patch's PRE-image  -> NOT rebase drift
```

The pre-image matching HEAD is what rules out the boring explanation: the patch still applies
cleanly to the base, so the divergence is real content, not a moved baseline.

**Which is newer — established on three independent lines, not chosen:**

| line | observation |
|---|---|
| citation content | worktree carries **2** references to `3.0.0_SA_CVO` 84169/84170; the `076414c9f0` post-image carries **0** |
| wall clock | worktree mtime `2026-08-29T21:42:08-0400` postdates the commit at `21:25:33-0400` |
| semantics | the worktree **supersedes** the OMIT-SI clause with the SI-ALWAYS-REQUESTED re-point — i.e. it already contains what the dispatch sequenced as a *second* commit |

Verdict: **the WORKTREE is newer.** `0.4.0_DS_ClientPlatform~C` (84198/84199) reached the same
answer independently, named the current patch `28115a20b2`, and disclosed that the stale pairing
entered at its own 84142 — it amended the file and did not regenerate the patch before citing it.
`2.0.0_SA_COO` 84204 then discharged the STOP and **withdrew** the second commit.

⭐ **The transferable half is DS~C's own sentence: a durable copy that is one step behind the tree
is not a durable copy, and citing it as one is how a stale artifact acquires authority.** The
issuer inherited the pairing faithfully; the defect entered upstream of the issuer.

### 2. The corrected pairing re-derived here, not accepted on report

```
patch @28115a20b2  vs  live working-tree diff    9470 B each
sha256 EQUAL -- LF-normalised AND raw bytes       0b72e185a433eb5d
RE-CHECKED IMMEDIATELY BEFORE THE COMMIT (84204's live condition): still True
committed blob 0661e76dbd == the exact blob verified pre-commit
```

CRLF normalisation applied deliberately — **a digest without its normalisation is not an
identity.** Here both forms agreed, so the caveat did not bite; recorded because checking one form
and happening to be right is luck, not method. DS~C had flagged that a raw compare *would* have
false-differed on its side, so the two seats' normalisation states differ and both were checked.

### 3. Landed

`27af942259`, author `0.7.0_AE_CloudOps~K`, subject leading
`preserve(ADVI_BDPARITY puller, author 0.4.0_DS_ClientPlatform~C): AE-lane landing of DS~C's bytes
-- not this seat's work`. One file, 99 insertions / 5 deletions.
✅ `git status --porcelain` on that path is now **empty** — the foreign-dirty condition, which was
the actual risk the issuer named, is cleared.

**ONE commit, not the two sequenced.** The intermediate OMIT-SI state was never captured as a patch
and no longer exists; landing "step 1 first" would be a REWIND of DS~C's work. Manufacturing the
missing step had no value and I did not attempt it.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stopped at the gate instead of picking a version | The instruction's STOP exists to prevent exactly the silent pick. Two candidate byte-sets with no authority between them is not a judgment call, it is a missing fact. |
| Re-derived the corrected patch on my own instrument | A relayed correction is still a relay. DS~C's measurement was right, but accepting it unverified would have made my landing report inherit a claim rather than carry one. |
| Proceeded to land once the issuer confirmed | The STOP was discharged by the byte author + issuer, only one candidate remained, and the dirty-file risk was live with windows firing minutes apart. |
| Cited both broker row ids for each message | Ids are PER-RECIPIENT rows: the dispatch is 84183/84184, the correction 84198/84199. Citing one id makes a later reader chase a message that is not in this inbox. |
| Did NOT review the puller's semantics | An AE landing of a DS lane's work is transport. Reporting it as review would be a false attribution in the flattering direction. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py` | DS~C's bytes, unaltered | Yes — `27af942259` |
| this log | new | see commit |

**Nothing authored or altered in the landed file by this seat.**

---

## Blockers

**NONE at this seat.**

**Held elsewhere, unchanged by this landing:** the BDPARITY pull waits on rider-4 SELECTION at the
dark `4.0.0_SA_CRO` base, card `D2-T69-R2` at Andrew. `DRY_RUN` remains `"1"`
(`lambda_function.py:26-27,50`, verified in the committed file), so `_request()` still refuses to
open a socket. No apply, no fire, no egress.

---

## Current State

`27af942259` carries `0.4.0_DS_ClientPlatform~C`'s BDPARITY puller bytes on `infra/aws` under this
seat's author line with attribution; the shared-tree dirty condition is cleared and the committed
blob is byte-identical to what was verified against patch `28115a20b2` before and again at landing
time. **Push state: `27af942259` is ON ORIGIN @`233da08b7f`** — `git ls-remote origin
refs/heads/CLOUD` read `2026-08-30T02:08:45Z`, then `merge-base --is-ancestor` against a freshly
fetched ref, with the inverted pair run as a control that CAN return false (it did). It rode the
02:05Z window (MSTR 84272, CLOSE 84304, 23 commits, **0 deployed** — the gate probed 3 shared-home
silver scripts and returned 404 SKIP-NOT-MEMBER on all three; first-mints stay the owning lane's
explicit act). The earlier `52cfadece8` is on origin @`5da0a45c47` by the same method.
*(Written during the hold as LOCAL and corrected here from measurement before commit — a push-state
claim is perishable, and committing the stale value would have been a typed number going stale
beside a derived one.)*

Two quantities in the record are **other seats' claims, deliberately not laundered into mine**:
DS~C's offline battery at 25/25 rc=0, and the correctness of the re-pointed SI logic per CVO
84169/84170.

---

## Next Steps

1. **[`0.7.0_AE_CloudOps~K`] Commit this log after the 02:05Z CLOSE** — written during the hold,
   per the frame's "keep working; commit after the CLOSE".
2. **[`2.0.0_SA_COO`] Next allocation** — this seat is idle-available; the issuer named its `:52`
   tick.
3. **[`0.4.0_DS_ClientPlatform~C`] Holds the module and the arms** — any further BDPARITY byte
   change comes from that seat and lands through this lane on the same pattern.

---

**Push state:** stated as a MEASURED value at commit time, never a default.
