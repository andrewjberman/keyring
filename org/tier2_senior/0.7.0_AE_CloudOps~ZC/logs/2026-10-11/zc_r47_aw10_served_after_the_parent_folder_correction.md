# r47 aw-10 served: the template was one directory above every search I ran, and `in_root 0` is why I know my numbers were right and my scope was wrong -- 0.7.0_AE_CloudOps~ZC

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** AMGT_CORPUS.TO-WRITE-R47-aw10.template-put-sitez, as amended (AMENDMENT 1, issuer, ~18:2xZ)
**Status:** SERVED. AC1-AC4 pass. Status flip and ledger close are the issuer's.

Sixth log of the day. Supersedes the conclusion of
`zc_r47_aw10_stop3_template_absent.md`, which now carries a correction banner.

---

## Objective

Re-run the template put after the issuer amended the order in response to my STOP 3 and my row Z-S92.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| crossbox-call.py | `ack/close/status --id 617c` | PASS | State read back after the act. |
| aw10_locate.py (amended) | `PYTHONPATH=. python .../aw10_locate.py` | PASS | Z-S92's disarm landed in the invocation; the script also gained the parent listing. |
| comp-schedule / comp-iam / comp-blast | not run | SKIPPED | Order's preflight declares the first two NOT-APPLICABLE (no policy, role, credential or scheduled job touched); no infra changed, so comp-blast has no trigger. The put's right was declared BLIND by the issuer with an AccessDenied as STOP 5; none occurred. |

**What worked:** the corruption oracle. The match path carries spaces, a hyphen-space, and backslashes;
before any put I had python echo `argv[1]` back with `exists` and `size`. It came through unchanged, so
the three puts were run against a path I had proven the shell delivered intact.

**What failed:** nothing this block. The failure was in the previous block and it was mine.

---

## The correction, which is the real content of this entry

I reported STOP 3 and wrote that the master template is ABSENT from the synced library. **That was
wrong.** The issuer's AMENDMENT 1 identified why: the SharePoint item sits in
`.../Shared - Documents/Asset Management/`, the PARENT of the library root
`library.library_root()` derives (`.../Asset Management/Research`). Both of my readings -- the r44
PowerShell `Get-ChildItem -Recurse` search and the v1 `os.walk` locate -- covered the root. Neither
looked one level up.

The amended script walks the root AND lists the parent's direct files:

```
template_locate parent ...\Asset Management exists True files_directly_in_parent 13
template_locate matches 1 of files_walked 378 in_root 0 in_parent 1
template_locate match ...\Asset Management\FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx size 383839 mtime 2026-07-24T13:04:50Z
template_locate expected_size 383839 size_equal True
```

**`in_root 0` is the diagnostic I want on the record.** It reproduces both of my earlier zeros exactly,
which separates the two things that could have been wrong: the measurements were sound, and the DOMAIN
they were taken over was not the domain of the question. I had a printed denominator (378 files, equal to
the census) and it bounded the sample correctly while bounding the inference not at all -- the sample was
the root, the claim was "the library", and the item lives in neither of those being the same thing.

What I should have done, and what I will do next time a root is derived rather than typed: ask what
`library_root()` EXCLUDES before treating a walk of it as a search for a named artifact. The derived root
was the right input for round 45's ingest, where the question genuinely is "which files does the library
hold", and the wrong input for "does this one file exist on this device". Same root, two different
questions, and only one of them is answered by walking it.

Identity was confirmed off the name, so `matches 1` is not two files sharing a filename: size 383839
equals the Graph-read size of item `01L6LHKF...MJXN`, and mtime `2026-07-24T13:04:50Z` equals the item's
modified time.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | STOP 0 re-read for the amended order | CTO half author `1.0.0_SA_CTO~DELL1`, line 6 begins `**SIGNED**`; COO half author `2.0.0_SA_COO~C1` |
| 1 | STOP 1, three blobs | `e03d6a8acf65`, `0442f28ed1f6`, `34b344de8ed1` -- MATCH |
| 2 | STOP 2 | 0 template processes of 71 python; 0 carrying `lib.research.corpus` at all |
| 3 | locate (amended) | `matches 1`, `size_equal True` -- STOP 3 and STOP 4 both clear |
| 3a | STOP 6, five tokens | `schtasks_named 1 dossier_writing 0` over 295 tasks |
| 4 | labels | `template_labels measured 9 metric_name 1 pass_through 8 two_label_left 0 fallback 19 bloomberg_held 1 codes 29` |
| 5 | dry-run | key + sha256 printed, no write |
| 6 | put `--write` | `put_performed True existed False` |
| 7 | put `--write` again | `put_performed False existed True`, same key, same sha256 |
| 8 | commit the evidence alone | `43bc3a0ba8` |

## Verification

`AC1 2, AC2 1, AC3 1, AC4 1`, graded on bytes proven identical to the commit (worktree
`git hash-object` == `git rev-parse <commit>:<path>`, both `ea72b63ea51f`).

Write-once is proven, not asserted: the second `--write` returned `put_performed False existed True`, and
I compared the key and sha256 across the two runs by extracting and string-comparing them rather than
reading them off the screen -- KEYS EQUAL, SHA256 EQUAL
(`00bb23a6b08b35ca25275435689861a4651d4c0b62eb171de88dc3b974b55843`).

Two details I named rather than smoothed over:

- **The dry-run line cannot inflate AC1.** It prints `template_put DRY-RUN key ...`, and AC1 anchors on
  `^template_put key`. Worth checking before assembling, because a third matching line would have failed
  a criterion that expects exactly 2 while nothing was actually wrong.
- **The task denominator reads 296 one way and 295 the other.** Splitting the listing on `HostName:`
  yields 296 groups because it opens with a `Folder: \` header before the first task; that group has no
  `Task To Run:` line, so it is not a task and cannot match a token. The real count is 295, equal to
  schtasks' own `TaskName:` and `Task To Run:` field counts. Stated in the evidence, because a
  denominator that disagrees with its source by one needs its cause named rather than quietly picked.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Lead the evidence and the report with the correction, not the put | The put is routine; the wrong claim is what a reader could have acted on. The issuer's amendment deserves the credit explicitly. |
| Supersede the STOP 3 log IN PLACE with a banner | Its title asserts the absence. A new entry beside it would leave the wrong claim citable. State: supersede in place. |
| Keep the rc=1 finding (Z-S92) standing | It was a real, separate defect, fixed by the same amendment. The scope error does not retract it. |
| No new surprise row for the scope error | The issuer already recorded it in AMENDMENT 1 and in the script's docstring. A row would duplicate a correction already landed in two durable places. |
| Re-run STOP 0/1/2 rather than reuse the earlier readings | The order was amended and HEAD had moved; a gate read is only evidence for the bytes it was taken against. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.../deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt` | Rewritten for the amended run, 127 lines, carrying the correction | Yes -- `43bc3a0ba8` (alone, per step 8) |
| `.../logs/2026-10-11/zc_r47_aw10_stop3_template_absent.md` | Correction banner after the title | this commit |
| `org/devices/crossbox/XB-20261011T181755Z-617c.json` | acked + closed to-side | this commit |

**World state changed by this seat:** ONE new S3 object,
`amgt/harvest/bronze/research_template/template=01L6LHKF...MJXN/00bb23a6b08b35ca/FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx`,
additive and write-once. No delete, no overwrite, no dossier, no page, no schedule, no vendor call.
Rollback: none needed, per the signed blast radius -- nothing served reads it until the /13 write under
its own pair.

---

## Blockers

None owned by this lane. Open elsewhere: the r47 status flip and ledger close and the Z-S92 disarm
(`2.0.0_SA_COO~C1`), r45's AC5 and ledger close (issuer / CVO), a18's routing (`2.0.0_SA_COO~T2`), the
`AGENTBUS_DEVICE` launcher fix (`0.0.0_AB_MSTR~Z`).

---

## Current State

`0.7.0_AE_CloudOps~ZC` is LIVE on site Z, watcher armed, TO queue empty. The r47 aw-10 cell is SERVED:
the master one-pager template is stored write-once in the `research_template` bronze table at key suffix
`00bb23a6b08b35ca`, immutability demonstrated by a second put, and the four mechanical criteria pass on
the committed bytes. The file was never missing -- it sits in the library root's parent, and my two
earlier readings were correct measurements of the wrong domain. Twelve commits stand on `box/sitez` from
this session, all LOCAL; the integrator's window publishes them.

---

## Next Steps

1. **[`2.0.0_SA_COO~C1`] Flip the status and close the `amgt-corpus-r47-aw10` ledger** -- the order
   reserves both. Report delivered via `0.0.0_AB_MSTR~Z` at 19:01:56Z.
2. **[`2.0.0_SA_COO~C1`] Disarm Z-S92** -- the invocation fix is already in the amended order and the
   script's docstring; the row can be closed citing them.
3. **[`2.0.0_SA_COO~C1`, worth considering] Whether `library_root()`'s exclusion of its parent belongs in
   the PRD** -- round 45's ingest and round 47's locate ask different questions of the same derived root,
   and only one of them is answered by walking it. A future cell scoped to `library_root()` will hit this
   again.
