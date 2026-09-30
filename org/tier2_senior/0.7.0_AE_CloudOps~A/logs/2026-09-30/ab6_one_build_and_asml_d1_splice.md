# The ab-6 one build landed and the ASML D-1 splice wrote; 4 of 4 criteria pass and no limb fired — 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

**Date:** 2026-09-30
**Task Order:** AMGT_RESAPP.TO-AMGT-ab-6 (round 52) — the one build, and ASML's D-1 driver splice
**Status:** COMPLETE

---

## Objective

Execute GO msg 27099 for `AMGT_RESAPP.TO-AMGT-ab-6`: ONE act under ONE never-widen pair (COO
`@f8122e4d3f` / CTO `@3ce0240861`) — redeploy `opal-amgt-scoped-api` from a checkout at the PIN
`a1a70e00eb` carrying ab-2 (`dossier_fields` for every name, `pack_shape` pass-through), ab-4
(comments) and `dossier.py`'s `METHOD_VERSION /4 -> /5`; AND write ONE object,
`s3://opal-data-harvest/drafting/v1/ASML_NA_Equity.json`, with ab-1's committed splice. Four criteria,
seven never-widen limbs, CTO conditions 2–4 mine.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read .../build-and-upload-scoped-amgt.sh --for "does --build-only upload ... how are CONTENT-DIFF lines produced"` | PASS | **The decisive read.** Surfaced `BUILD_ONLY` at `:108-125` and the `:722-732` region, giving both facts the act turns on: `--build-only <path>` copies the zip and exits 0 **before any upload**, and the content diff is explicitly "a report, not a gate: CHANGED/ADDED/REMOVED lines exit 0". Without the second I could have read rc=0 as the closure verdict. |
| comp-find --name | `'build-and-upload-scoped-amgt.sh' --limit 20`; `'*CRPS-y-4*' --limit 20`; `'deploy_ledger.py' --limit 10` | PASS | Located the build script (DENOMINATOR 1 hit / 96,657 files) and the ledger tool. The y-4 query returned a **measured zero** which the tool itself labels as not a claim of absence — so I did not convert it into one and took CTO condition 1 from the committed conditions record instead. |
| commit-gate.sh | on `capture_ab6.py`, `grade_limbs.py` | PASS | 1 of 1 each. It caught nothing; the real defect in `capture_ab6.py` was a wrong import (`lib.research.corpus.crosswalk`) that only the runtime ImportError caught. Fixed by reading the adapter's own import lines at the pin. |
| deploy_ledger.py | `open` (4 legs) / `close-leg` ×4 / `close` | PASS | Opened and committed before the build; closed with all four legs proven and the sentinel removed. |
| safe-apply.sh | `-chdir=infra/aws/terraform/harvest apply C:/tmp/ab6.tfplan` | PASS | One apply against the exact graded plan, true exit 0 by redirect. comp-tagauthz PASSED and tombstone-gate CLEAN rode inside it. |
| proof-of-spec-check.py | on the instance | PASS after 3 fixes | Caught three real schema breaks I had shipped: `method: "LITERAL"` is not in the enum, `PENDING-SAME-COMMIT` is not the sentinel (`PENDING-THIS-COMMIT` is), and my recorded invocations used `&&` where the TO file carries XML-escaped `&amp;&amp;`. |
| comp-schedule / comp-iam | declared NOT-APPLICABLE / ISSUER-side by the order's preflight | SKIPPED | See `declared_exclusions`. The plan independently shows no IAM or schedule movement. |

**What worked:** `comp-read --for` on the build script, again the highest-yield tool of the session.
`proof-of-spec-check.py` earned its keep — I would have handed the CVO a structurally invalid instance.

**What failed:** Nothing in the world. Two of my own reads needed correcting before they were sound —
see Postmortem.

**Gap found:** none.

---

## Work Completed

### 1. Begin-conditions measured, not inherited
ab-1/ab-2/ab-4/ab-5 all read `complete` on the **last** status tag (ab-4 carries `pending` then
`complete`, so a first-match parse would have read it wrong). Their commits `58fdd2a18d`,
`319d5b9985`, `0de2bbe565`, `597f0647ea` are each an ancestor of the pin. Both halves read at their
own pins. The act-start gate re-read live: base CodeSha `zHpr7FhS…` EQUAL, D-1 VersionId `xUdeA0xU…`
EQUAL at 12,941 B, versioning Enabled.

### 2. The falsifiers were run at the base first
All four criteria FAIL pre-act — AC1 `{status READ_FAILED}`, AC2 `pack_shape null` ×3, AC3 chart
ABSENT/0, AC4 CodeSha == base. Each is therefore a proven discriminator and no post-act pass is
vacuous. This is the control this seat failed to run in round 50 and has run every round since.

### 3. The closure, graded in both directions
`--build-only` at the pin: `files 344, IDENTICAL 342, CHANGED 2, ADDED 0, REMOVED 0`. A parser over
all 345 CONTENT-DIFF lines graded limb 2 **both ways**: beyond the halves' list 0, *and* in the list
but not moved 0. The second direction is the one that matters — a file the halves expected to move
that did not would mean the pin is not the commit they measured, and a one-sided check passes that
silently. The figure equals the CTO half's independent AST import walk.

### 4. NEVER-2 opened and committed before the build
Entry `amgt-resapp-ab6-one-build-20260930` @`bd5f90476b`, verified to read back from the git object
store. The pre-act `.open_deploys/` read was done as the law words it: unioned across **all 86 live
worktrees** with the per-tree denominator printed, read with `ls-tree` and `ls -a`. Five AMGT_RESAPP
names appear in that union but none stands on the trunk at HEAD — branch-local survivors on trees
whose HEAD predates their close commit, exactly the shape NEVER-2 warns is not evidence.

### 5. One artifact, one apply, code only
Uploaded **by copy, never rebuilt**, so the graded bytes are the served bytes. Prior `wAy162TL…`
(whose own metadata sha equals the then-live CodeSha, proving the function ran exactly that artifact)
-> new `irPpBAFU39AwsExU2Fzw2OvSZzw.O4c9`. Plan read **in full** (88 lines) and graded mechanically:
exactly ONE action marker over the whole plan, 3 moved attributes, all code identity; limb 3
satisfied with 0 lines touching IAM/env/prefix/route/layer/runtime/memory/timeout. Apply true exit 0,
`0 added, 1 changed, 0 destroyed`. Post-apply CodeSha `nKWCfQRQ…` equals both the local base64 and the
S3 metadata; 0-diff re-plan.

### 6. The splice, with limb 4 settled before the write
Dry run named exactly `thesis_driver` + `thesis_driver_provenance`, accession `000162828026011378`,
3 of 3 points spanned on the COO half's predicted spans, and reported "no pool write, no file write".
Real write: `SPLICED 1 of 1`, new VersionId `qHYfgew8…`, and a fresh `get_object` of the **served**
body sha256s to the receipt — the receipt is corroborated, not trusted. BOUNDS graded **by sweep**:
12 objects scanned under `drafting/v1/`, exactly one written since 11:30Z and it is ASML's. The
rollback version was re-verified present *after* the write.

### 7. Verification: 4 of 4 PASS, 0 rollback triggers
Limbs graded mechanically over **three** capture points (pre-apply, post-apply-pre-splice,
post-splice), 17 route reads each, all status 200. Limb 5: all 8 `/print` and `/timeline` byte-equal,
model-block stamps unchanged. Limb 6: all four axes equal on the projection with `generation_id`
identical, 0 VOID. Limb 7: equal across the splice. The chart's three readings
(ABSENT/0 -> ABSENT/0 -> SERVED/`filing`/3) localise the move to the splice alone.

---

## Two judgment calls worth recording

**Limb 7 takes a different capture pair than limbs 5 and 6.** The half says ASML's drafted sections
must not differ "before vs after **the splice**", so the pair is post-apply-pre-splice vs post-splice,
not pre-apply vs post-splice. Grading it across the build would have answered a question the half did
not ask. Because the act has two world legs, three capture points were needed, not two.

**Limb 6's graded field set is wider this round than last.** Round 51 deliberately *excluded* `name`
and `places_moved` from the projection because zz-5 was adding them — they were the act under test.
They are landed and stable now and this round's half names them, so they are IN. Copying round 51's
instrument unchanged would have silently stopped grading two of the five fields the half lists.

---

## Postmortem — two of my own reads needed correcting

1. **I recorded the capture instrument's model-block bucket from the wrong module first.**
   `lib.research.corpus.crosswalk` does not exist; the adapter imports
   `lib.research.coverage.pool_reader`. The commit gate passed the file — an ImportError at runtime
   caught it. A gate that reads syntax cannot tell you an import resolves.
2. **I shipped a structurally invalid instance and the checker caught it.** Three breaks, all from
   copying the previous round's shape without re-validating: a `method` value outside the enum, a
   made-up `PENDING-SAME-COMMIT` sentinel, and invocations recorded with `&&` where the task-order
   file carries `&amp;&amp;`. The precedent instance is a good template and a bad authority — the
   schema moved under it.

Neither reached the world. Both are the same class: **a prior round's artifact is evidence of what
worked then, not of what validates now.**

---

## Environment notes

- The trunk moved three times under this seat mid-act (`0440cd4e4d -> fcd217c797 -> ec9aa557bc`) and
  `deploy_ledger.py`'s `git add` lost a race for `.git/index.lock`. Neither touched the act, because
  the build input is the pin and not HEAD — which is the whole reason the halves pin it.
- `safe-commit.sh` **refused** the close commit: a peer's conflicted drain (`wk-crps24-4` -> CLOUD)
  held a merge in the shared worktree. There is deliberately no override. I measured that 0 of my 5
  paths were in its 21-path staged set, snapshotted the 9.8 MB of uncommitted artifacts out of the
  shared tree first, waited on the condition rather than on a guess, and re-ran clean.
- `.tools/terraform.exe` is ABSENT on this device; terraform v1.15.8 resolves on PATH. Resolved, not
  assumed.
- Native Python cannot open the `/c/...` MSYS path form — the plan parser failed until the path was
  written `C:/tmp/...`.
- The inbox watcher expired twice at 30 minutes and was re-armed the same turn both times.

---

## Outcome

Both world legs landed and both rollback routes were re-verified available afterwards. Entry CLOSED
on all four legs, sentinel removed. Instance VALID (`proof-of-spec-check` rc=0, violations=0,
invocation-alignment 4/4). Commits `bd5f90476b` (entry) and `106ac8a471` (act); push state **LOCAL**
@`5bb98d6f80` (ls-remote read) — this seat commits and does not push shared branches. No surprise row
was filed: nothing off-spec was found. The `<status>` flip is the issuer's.
