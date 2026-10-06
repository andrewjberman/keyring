# The recorder runs on site Z, Rule 4's loop is closed, and two gates caught me being wrong — 0.7.0_AE_CloudOps~RV

**Date:** 2026-10-06
**Task Order:** OPAL_BBGTML.TO-GUARD-2.recorder-site-z-fix (@304b05698f, risk LOCAL)
**Status:** COMPLETE (AC1 PASS, AC2 PASS, AC3 FAILED AS WRITTEN and reported as such)

---

## Objective

**archetype:** DIAGNOSE

Disarm surprise row `OPAL_BBGTML-Z-S7`: make `infra/aws/lambda/ci/record-terraform-deploy.sh` run on
site Z, then close deployment Rule 4's parity loop for the guard deploy so `lambda-source-map.json`
reads the deployed commit `513b25f522` for `yang-model-portfolio-benchmarks`.

This order exists because loading `/cloud-ops` — the owed session one-shot I had skipped when
TO-GUARD-1's GO arrived — surfaced two post-deploy rules the first order never named.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate.sh | on the edited `.sh` | PASS | Clean 1 of 1. Flagged 17 pre-existing non-ASCII lines as WARN; it does not distinguish pre-existing from added, so I printed the before/after count myself (unchanged). |
| bash -n | on the edited recorder | PASS | The real oracle for a shell edit, and the one `commit-gate` does not provide. Run WITH a negative control. |
| safe-commit.sh | 4 invocations, 2 refusals | PASS | Both refusals were correct and both were my error. See Postmortem. |
| surprise-row-gate | at commit, 3 refusals | PASS | Caught an out-of-enum `disposition`, an in-place row mutation, and a non-schema `cites` field. Three distinct real defects in my own writing. |
| deploy_ledger.py | n/a this session | SKIPPED | No deploy in this order -- the apply landed under TO-GUARD-1 and its entry is closed. |

**What worked:** the row gate, three times over. Each refusal named the exact field and the exact
rule, and one of them (`MUTATED in place ... content hash 775ec48bffef -> 48ecd6b0ea3f`) printed the
before/after hash so there was no arguing with it.

**What failed:** nothing returned a wrong answer. `record-terraform-deploy.sh`'s own "Next steps"
block prints `.tools/terraform.exe`, which does not exist on this device — the same stale-path defect
its sibling already fixed.

**Gap found:** no instrument answers "does this tool write outside my task order's `<paths>`". The
owned-paths hook did not refuse the CHANGELOG write, and the acceptance criterion written to bound it
was path-scoped (see Postmortem). That gap is now row Z-S8.

---

## Work Completed

### 1. The fix (@8be38c9dec) — three changes, nothing else

Per `1.0.0_SA_CTO~Z` msg 30157:

1. **Detection reordered to node FIRST.** `node` resolves as a BARE NAME here, so no device path
   enters the invocation at all. bun moved to last, still available where it is the only runtime.
2. **All four `$JSON_TOOL` invocation sites quoted** (250, 348, 448, 463). The patcher asserted the
   census before writing a byte: 4 unquoted before, 0 after, 4 quoted after.
3. **Both python gates compare `$(basename "$JSON_TOOL")`**, so a RESOLVED path still selects the
   python branch instead of silently falling through to the JS one.

I also corrected the comment at line 217, which claimed bun was *"derived with command -v, no device
path"* — the exact opposite of what `command -v bun` returns, and the sentence that made the original
choice look safe. Line 787 of the same file already named "the `$JSON_TOOL` hazard" and line 796
already worked around it; the defect was known in one half of the file and unfixed in the other.

**Verified with a live control:** `bash -n` exits 0, and a copy with a truncated `if` appended is
REJECTED by the same `bash -n` — so the pass discriminates rather than merely not erroring.

### 2. AC1 PASS / AC2 PASS

The recorder ran to **exit 0, no "Is a directory"**, committing `@4ddd25eee8`. The source map moved
`last_deployed_commit` from `0ce5aa5ada` (2026-08-18) to **`513b25f52259dcfe10500cdffd564c025d08afda`**
and `last_deployed_at` to 2026-10-06T17:47:56Z. `artifact_sha256` was already current. **Rule 4's
parity loop is closed for the guard deploy** — the map's commit field now matches the deployed bytes.

### 3. AC3 FAILED AS WRITTEN — reported, not self-passed

Two deviations, **neither caused by this fix**; the script previously died before reaching either
writer, so fixing it is what revealed them.

- A **third file** moved: `infra/aws/terraform/yang-pipeline/CHANGELOG.json`, +48, outside the
  order's `<paths>` and outside `infra/aws/lambda/ci/` entirely. The owned-paths hook did not refuse.
- The source-map diff added a per-function key **`recorded_by`** that AC3 does not name. (AC3 named
  `_updated` and `_last_deploy_recorded`; the latter moved, the former did not.)

**AC3's own invocation cannot see the first one.** `git show --stat HEAD -- infra/aws/lambda/ci/` is
path-scoped to the very directory the write escaped. Measured side by side on commit `4ddd25eee8`:

```
scoped   -> 1 file changed,  5 insertions(+), 4 deletions(-)    READS CLEAN, would PASS
unscoped -> 2 files changed, 53 insertions(+), 4 deletions(-)   the overrun
```

A path-scoped proof of a path-containment claim is circular. I graded the criterion FAILED rather
than taking the clean scoped answer it offered me.

### 4. Rows Z-S8 and Z-S9 (@07d1cadca5)

- **Z-S8** — the write-surface overrun and the blind criterion, with three candidate scopes for an
  owner (cheapest: add the CHANGELOG to the `<paths>` of any order that runs the recorder — a
  template fix, not a code fix). Also records that the CHANGELOG hardcodes
  `agent: devops_technician` instead of the `--author` serial, and that its `deployed_commit` is HEAD
  at run time rather than the deployed code commit the source map correctly carries.
- **Z-S9** — Z-S7's fix landed, and why its disposition did not move.

---

## Postmortem

Three things went wrong in my own writing. All three were caught by mechanisms, not by me.

**(a) `RESOLVED` is not a disposition.** TO-GUARD-2's gates say *"Mark Z-S7 RESOLVED in its own
row"*. That step is not executable by any non-CVO seat: `surprise-row-gate.py:174` defines
`UNDISPOSITIONED` as `("UNDER_INVESTIGATION", None, "")`, and `:164-166` resolves the terminal value
`GRADUATED` from a REMEDIATION row bearing the id — and CLAUDE.md states *"REMEDIATION rows stay the
CVO's"*. The gate refused on `/disposition`. I left the disposition alone and asked for the order
template to be re-worded, rather than forcing an out-of-enum string past the audited override.

**(b) I mutated an existing row in place.** After reverting the enum value I left Z-S7 *edited*, and
the gate caught it: *"EXISTING row OPAL_BBGTML-Z-S7 was MUTATED in place (content hash 775ec48bffef
-> 48ecd6b0ea3f). Corrections are NEW items citing the old id; an edited history is a history nobody
can audit."* **I had the rule inverted**: supersede-in-place is for STATE carriers, while a surprise
row is corrected by a NEW row. I restored Z-S7 to its committed 17,757 bytes and moved the
correction into Z-S9.

**(c) Non-ASCII in a commit message.** I was careful about non-ASCII in the code and sloppy about the
message, which carried one `U+26A0`. `safe-commit` blocked it and named the substitutes.

No override was used for any of the three. Each gate was right.

**A fourth stop was not my error:** a peer's worker-drain merge (`wk-AMGT_RESAPP-262`, 0 conflicts)
was in progress in the shared tree, so `safe-commit` refused — correctly, since my change would
otherwise have folded into their merge commit. I waited on an `until [ ! -f .git/MERGE_HEAD ]`
background watch rather than touching their merge, and committed once it cleared at 18:11:14Z.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT take the recorder fix on my own initiative when I first found it | Shared CI tooling, 7 pipelines, 2 devices, no open order, and `/cloud-ops` names this tool a known failure to "surface in RAVC". I filed Z-S7 and asked. The CTO seated me, and then I fixed it. |
| Did NOT cut the `yang-pipeline-v1.5.9` tag, though TO-GUARD-2 permits it locally | Measured first: 11 of 11 yang-pipeline tags and 256 of 264 pipeline tags repo-wide were created by Andrew Berman (7 by MSTR, 1 by an AE lane). Left for one line of confirmation; the recorder's CHANGELOG entry carries the version string either way. |
| Graded AC3 FAILED rather than running only its literal invocation | Its invocation reads clean on the same commit. A criterion that cannot see the thing it bounds is not evidence, and self-passing on it would have hidden a real overrun. |
| Did NOT fix Z-S8 | Same reasoning as Z-S7 before I was seated: the recorder's write set is not mine to re-point without an order. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/ci/record-terraform-deploy.sh` | node-first detection, 4 sites quoted, 2 basename gates, comment corrected | Yes — `8be38c9dec` |
| `infra/aws/lambda/ci/lambda-source-map.json` | `last_deployed_commit` -> `513b25f522`, `last_deployed_at`, `recorded_by` | Yes — `4ddd25eee8` (written by the recorder) |
| `infra/aws/terraform/yang-pipeline/CHANGELOG.json` | +48, the v1.5.9 entry | Yes — `4ddd25eee8` (written by the recorder, **outside this order's `<paths>`** — row Z-S8) |
| `org/surprise_channel/OPAL_BBGTML/INVESTIGATION_v1.md` | rows Z-S8, Z-S9 appended; Z-S7 byte-untouched | Yes — `07d1cadca5` |

**Push state, measured at `git ls-remote` (18:13Z):** all LOCAL. origin/CLOUD read `66b1b42a71`.

---

## Blockers

**None.** Nothing is owed by this seat.

---

## Current State

`record-terraform-deploy.sh` runs on site Z. Deployment Rule 4's parity loop is closed for the guard
deploy: `lambda-source-map.json` reads `last_deployed_commit 513b25f52259dcfe10500cdffd564c025d08afda`
against live `CodeSha256 FLFjTpvIDptT+YqJGG9w3XaWN/Cwq4WJkNlmPd4p0tg=`, and `artifact_sha256` matches
both. Z-S7's defect is fixed and verified but its disposition is deliberately still
`UNDER_INVESTIGATION`, because terminating it is the CVO's act; Z-S9 carries the fix evidence and the
reason. Z-S8 stands open for an owner. Reported once to `2.0.0_SA_COO~Z` at 18:13Z with every
criterion's verdict, the hashes and the push state.

---

## Next Steps

1. **[`3.0.0_SA_CVO~RV`] Graduate Z-S7** — the fix is landed and verified; the disposition is the
   only thing left and it is not a seat's to write.
2. **[`2.0.0_SA_COO~Z`] Re-word the order template** — "mark `<row>` RESOLVED" should read "record
   the fix in a new row citing `<row>`, and hand the disposition to the CVO", or the next order
   repeats this exactly.
3. **[`2.0.0_SA_COO~Z`] Seat an owner for Z-S8**, or decide route (i) — adding the pipeline
   CHANGELOG to the `<paths>` of any order that runs the recorder, which needs no code change.
4. **[`2.0.0_SA_COO~Z`] Flip `<status>` on TO-GUARD-1 and TO-GUARD-2** — terminal status is the
   issuer's.
5. **[Andrew or `0.0.0_AB_MSTR~Z`] The `yang-pipeline-v1.5.9` tag**, and the CLOUD push — five of my
   commits are LOCAL.
