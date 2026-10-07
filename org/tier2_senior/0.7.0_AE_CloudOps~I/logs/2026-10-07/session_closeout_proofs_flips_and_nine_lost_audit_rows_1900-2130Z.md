# Closeout: the two proofs, the two flips, and nine audit rows that were really gone -- 0.7.0_AE_CloudOps~I

**archetype:** MIXED

**Date:** 2026-10-07
**Task Order:** IRPT_BCKEND.TO-IB-pr-349 and .TO-IB-pr-350 (closeout); plus one off-task finding
**Status:** COMPLETE

---

## Objective

Close both orders properly rather than by assertion, and chase the startup audit-integrity findings
to ground instead of leaving them as a line in a report.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check.py | on both instances, on each root | PASS | The most useful instrument of the session. Its violations are specific enough to act on, and it names the ROOT it resolved the TO under, which is what exposed the two-root split |
| p69_cells.py / p68_cells.py | IB69-1-AC1, IB68-1-AC1 | PASS | r69 needs no harness; r68 does, per row S384 |
| deploy_ledger.py | both entries | PASS | Both CLOSED, both sentinels removed |
| audit-archive-invoker.py | 3 runs across the session | PASS | Correctly held its finding across runs and refused to advance the baseline while clause 2 was violated. The finding was TRUE |
| git show `<ref>:<file>` | record presence at a ref | PASS | The sound oracle. Settled a question `git log -S` had answered wrongly |
| git log -S | record presence in history | **FAIL** | Reported "not in any ref" while HEAD plainly carried the rows. It is a pickaxe and skips merge-commit diffs by default |
| safe-commit.sh | 4 commits | PASS | Refused once, correctly, because another seat's merge was open -- see Decisions |

**What worked:** `git show <ref>:<file>` over a history walk. Rule 22a already says resolve a pin by
CONTENT and never by an ancestry heuristic; this session is a second instance of the same lesson in a
different costume.

**What failed:** `git log --all -S<string> -- <file>` as a presence oracle. It is a diff-based pickaxe
and does not follow merge commits without `-m` / `--full-history`, so on a repo whose audit logs arrive
by cross-device union-merge it returns a confident false negative.

**Gap found:** none new in the tooling. The two gaps already filed stand: no comp-tool has an IAM GROUP
mode (S383's investigation), and the r68 check spawns bare `bash` from Python (S384).

---

## Work Completed

### 1. The two orders, closed on their own terms rather than mine

I had reported "nothing owed" while both orders sat at `pending`. The issuer's relay (msg 106581)
named three outstanding items on IB-pr-350, and two of them were genuinely mine.

| item | state before | action |
|---|---|---|
| IB-pr-350 proof_of_spec instance | **never written** | written at the path the order's `<proof_of_spec>` block names; `VALID (rc=0)`, mode ENFORCE |
| IB-pr-350 `<status>` | `pending` | -> `complete` @`f3e5e8a8b7` (now ON ORIGIN) |
| IB-pr-350 commit hash reported | not sent | sent, with measured push state |
| IB-pr-349 `<status>` | `pending` | -> `complete` @`2bdae1d61a` (LOCAL) |

`IB-pr-350`'s instance declares `surprises: []`. That is intent, not omission: this cell surfaced no
rows. The one notable thing in pass 2 -- the bundle sitting under a separate `exr_` attempt path rather
than beside the receipt -- is exactly what the tool's own docstring describes ("beside the artifact"),
so the system behaved as documented and only my first assumption was wrong. No spec-vs-world gap, so
no row. An empty list that is justified beats a row filed to look thorough.

`IB-pr-349`'s instance was vindicated rather than fixed. It had read INVALID on either root ALONE
because the roots were complementary -- on CLOUD the four rows resolved but the TO was still on the
dell2 branch; on that branch the TO resolved while the rows sat on CLOUD. Once the trunk carried both,
the same unedited instance read `VALID (rc=0)` with 4 of 4 rows resolving. I had said it was
structurally sound and only needed the roots unified; that turned out to be correct, but it was a
prediction until the trunk proved it.

### 2. Nine audit rows were really gone, and the instrument nearly said otherwise

The startup `audit-archive-invoker` findings were not noise. Chased down:

| log | baseline records absent from live |
|---|---|
| law-edit-audit.log | 2 (REFUSED-BUDGET, 1.0.0_SA_CTO) |
| mass-deletion-audit.log | 3 (two BLOCKED at deletions=34 over threshold 25, one ATTRIBUTED) |
| safe-deploy-bypass-audit.log | 4 (ALLOW-STALE, 0.0.0_AB_MSTR) |
| agent-spawn-audit.log | **0 of 16,789** -- unioned, nothing lost |

Three distinctions made this readable rather than alarming-or-dismissible:

- **Not a truncation.** "Divergence at line 1, col 121" looked like an edited first record. Line 1 is
  exactly 120 characters, so col 121 is one PAST its end: line 1 is identical and what differs is the
  sequence after it.
- **Not a reformat.** Classified by TIMESTAMP rather than exact text. All 9 timestamps were absent from
  live, so the events were gone, not restyled.
- **Not everything is a loss.** `agent-spawn-audit.log` broke the same byte-exact-prefix clause with
  zero records missing. "The baseline is not a prefix" proves nothing on its own in either direction.

Surfaced to the owner rather than re-filed as a row: the class had an owner (`0.0.0_AB_MSTR`) and a
documented precedent remedy (@`871da68fbb`), and the invoker itself said this lane is not
GOVERNANCE_AUDIT-permitted. XXX.md says surface only an UNOWNED class. MSTR restored all nine and
committed them @`22ff15f401`; I verified them back by content at the ref, with a negative control.

**The instrument error.** Re-checking whether those rows had ever been committed, `git log --all -S<ts>`
returned "not in any ref" for all nine -- while HEAD plainly contained them. `-S` is a pickaxe and skips
merge-commit diffs by default. I caught it only because `git status` showed no diff against HEAD, which
is incompatible with "not in any ref": two readings that could not both be true. Had I not noticed, I
would have asked MSTR to re-restore rows that were already safe.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Reverted my own status edit when safe-commit refused | The refusal named an open merge, `Merge branch 'wk-NFRA_CTLPLN-6' into CLOUD`, which was another seat's drain. An uncommitted edit in a tree someone else is actively merging either rides their merge commit unnoticed or is lost. The gate says there is deliberately no override, so waiting was the only correct move |
| Re-validated at the NEW HEAD before landing the flip | HEAD had moved while I waited. A verdict obtained at an older HEAD is a stale reading, and the whole point of the gate is that the instance must be valid against the tree it lands on |
| Declared `surprises: []` on IB-pr-350 | No spec-vs-world gap occurred. Filing a row for my own wrong assumption about where a bundle lives would pollute the channel with a non-finding |
| Surfaced the 9 lost rows instead of filing a row or fixing it | Owned class, documented remedy, and this lane is explicitly not GOVERNANCE_AUDIT-permitted. Re-filing an owned class is what XXX.md forbids |
| Flagged the uncommitted-append root cause without building anything | Hook-written audit appends live in the working tree until someone commits them, so any level-set loses them. Proposing a mechanism is legal; implementing a gate unasked is not |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../deliverables/0.7.0_AE_CloudOps~I/...TO-IB-pr-350...proof_of_spec.json` | new, VALID | Yes -- `f3e5e8a8b7` |
| `.../task-orders/IRPT_BCKEND.TO-IB-pr-350...md` | `<status>` complete | Yes -- `f3e5e8a8b7` (ON ORIGIN) |
| `.../task-orders/IRPT_BCKEND.TO-IB-pr-349...md` | `<status>` complete | Yes -- `2bdae1d61a` (LOCAL) |

No audit log was modified by this seat. The restore of the nine rows is `0.0.0_AB_MSTR`'s
@`22ff15f401`, and I touched no baseline.

---

## Blockers

**None.** One handoff outstanding and it is not a blocker on the work: `2bdae1d61a` is LOCAL;
origin/CLOUD read `2e2a71aa78` by `ls-remote` at report time. Landing is the integrator's act under
LD-0367, asked at msg 106600 along with MSTR's own condition for closing this lane.

---

## Current State

Both orders read `complete` with a VALID proof instance each, both NEVER-2 ledgers CLOSED, neither
rolled back. What is served: `irpt-export-render` runs `entry.py` sha256 `fc241d806ecc`, so an export
read whose receipt names no account is refused for every principal including an admin; and the single
receipt that fail-closed behaviour made unreadable is back-filled at version
`Jg0xDC0pFmB8UBfEv0sl1eOQ_OrcSAqs`, admitted for a principal whose scope covers its account and refused
on the counts branch for one that does not. The nine lost audit rows are restored and committed at
`22ff15f401`, verified present at HEAD by content-at-ref -- though still absent from origin/CLOUD, which
is the recurrence condition I named to MSTR. Four rows remain open with their owners and completion does
not disturb them.

---

## Next Steps

1. **[`0.0.0_AB_MSTR`] Land `2bdae1d61a`, then close this lane** -- its own stated condition was a
   report of nothing owed, which msg 106600 is.
2. **[`0.0.0_AB_MSTR`] Get `22ff15f401` onto origin** -- the nine restored audit rows are committed
   locally only. They were already lost once from a working tree; until that commit is on origin, a
   second level-set is the recurrence condition.
3. **[`2.0.0_SA_COO~P2`] Rows S381, S382, S384** -- register the back-fill script so the next build of
   irpt-export-render needs no parity override; disposition the OPEN-BY-DESIGN arms; and fix the r68
   check's bare-`bash` resolution with `.tools/git_bash_resolver.bash_argv`.
4. **[`1.0.0_SA_CTO`] Row S383** -- rule on a read-Deny for the 21 unfenced buckets, with
   `0.7.0_AE_CloudOps~E`'s denominator (24 buckets, 3 fenced) and dell2's 24/24 reach.
5. **[whoever owns the audit instruments] `git log -S` is not a presence oracle** -- it skips merge
   diffs by default. Any future check of the audit-integrity class should read `git show <ref>:<file>`.
