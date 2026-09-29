# Joint storage recommendation — MSTR and CRO, 2026-09-29

Andrew asked the two seats to divide the work. MSTR owns developer-residue review;
CRO owns incident evidence, dedicated dump backing, pagefile and crash causality.
This document recommends scope. It does not authorize or execute deletion.

**Updated 13:01 ET:** the execution addendum in section 4 supersedes the provisional
proposal and resolves its count/time discrepancies. Sections 1–3 retain the
pre-execution record; their candidate totals are not the executed scope.

## 1. Denominators and candidate reconciliation

CRO whole-volume census: **473.705 GiB capacity**, **235.756 GiB logical contents
assigned to 180 measured registered roots** from 185 registrations across the
workspace and portal repositories. Main/nested checkouts are included and each
file is assigned to the deepest registered root. This is not 235 GiB of disposable
scratch, and logical size is not guaranteed reclaimable allocation.

MSTR's narrower candidate census: **128 linked workspace worktrees**, totaling
**210.21 GiB** by summing its rounded per-tree measurements. This excludes other
registered roots in CRO's larger denominator. The underlying tier JSON reads:

| MSTR class | Roots | GiB | CRO disposition |
|---|---:|---:|---|
| Clean apart from generated manifest changes | 65 | 93.49 | Candidate for owner and process review |
| Submodule-pointer drift only | 39 | 74.89 | Candidate only after nested working-file and commit preservation checks |
| Real uncommitted edits | 6 | 9.95 | REVIEW; preserve edited bytes; pinned `wk-mcpindex-r4-15` stays KEEP |
| Recent git writes | 18 | 31.88 | KEEP, including damaged `wk-crps14-5` |
| Unregistered C:\tmp directories, reported separately by MSTR | 60 | ~2.5 | Review exact paths and untracked contents before removal |
| Anaconda package cache | One pool | ~7.5 | REVIEW using owning package manager and restoration requirements |

**Reconciliation pending at this draft:** MSTR message 26617 proposes **102
checkouts / about 165 GiB**, while its tier JSON and table total **104 candidate
checkouts / 168.38 GiB**. These must not be represented as the same exact batch.
The table also labels measurements 12:30–12:45 despite being received at 12:27:54;
those future clock labels are not accepted as measured timestamps. CRO requested
the two exclusions and corrected times in message 26619. The source files are
fingerprinted in the evidence summary; do not use this provisional table as an
executable deletion manifest.

## 2. Preservation conditions for an approved batch

MSTR proposes removing checkouts while retaining branches and pinning detached
HEADs under archival refs. That can retain committed work, but **six-hour git
write age is not proof that no process or person is using a checkout**. A clean
tracked status also says nothing about valuable untracked/ignored source, nested
submodule working files or a frozen deployment candidate.

Proposed owner: MSTR with COO lanes and each checkout owner. Before an approved
removal, they must resolve exact absolute paths, prove each target is the intended
checkout, preserve unique commits and non-disposable working files, check live
use and pinned candidates, and remeasure free space after the batch. An aggregate
capacity estimate is not a branch-deletion recommendation.

## 3. Crash-owned bytes — keep

| Item | GiB logical | Owner and recommendation |
|---|---:|---|
| MEMORY.DMP and minidump | 17.40 + 0.009 | CRO/endpoint administrator: keep; hashes recorded; preserve on approved storage before retention changes |
| 08:28 Sentinel Agent service dump | 6.40 (4.68 allocated) | CRO/MSP: keep with the kernel dump for driver investigation |
| Desktop historical freeze evidence | 25.24 | CRO/endpoint administrator: keep pending a deliberate retention and preservation decision |
| Dedicated dump backing | 32.00 | Endpoint administrator: keep until capture design is reviewed and a replacement is verified |
| Pagefile | 4.00 now, 6.47 at capture | Endpoint administrator: keep; reducing memory headroom is not a sound response to earlier allocation failures |

Dedicated backing is a reserved capture file, not itself a unique historical
dump. July 30's elevated setup deliberately allocated it to support capture with
a small pagefile. Today's usable dump demonstrates its value. Boot-time volmgr
46/164 errors nevertheless require checking readiness for the next capture.
Current overwrite behavior means a later crash can replace MEMORY.DMP: evidence
preservation should be completed before another intentional reproduction.

**Recommendation:** obtain substantial capacity from reviewed developer checkouts
first. Retain crash evidence and enough runtime/capture headroom. Prevent recurrence
through capacity admission checks, truthful write failures and the separate
SentinelMonitor remediation described in the main brief.

## 4. Execution addendum — 13:01 ET

Source: exact MSTR~Z message **26623**, timestamp **17:00:44Z**, and the
`EXECUTED 12:31-12:59 ET` section added to local `MSTR_RESIDUE_TABLE.md`.
Manifest: `.runtime/crash-investigation-20260929/mstr-reclaim-go.jsonl`.

MSTR records Andrew's 12:29 ET instruction verbatim:

> go, just make sure not to touch any recent AMGT and NFRA worktrees that
> might be in tmp

MSTR interpreted "recent" as HEAD commit younger than 24 hours, and extended the
exclusion to Desktop as well as C:\tmp. It reports leaving **70 recent AMGT/NFRA
checkouts** untouched: 59 in tmp and 11 on Desktop. This is MSTR's reported rule
and execution, not a new CRO deletion grant or an independent 70-path audit.

| Executed result | Independent CRO check at 13:01 ET |
|---|---|
| 34 candidates; 33 removed, 1 skipped | Manifest has 34 rows; all 33 removed paths are absent; skipped `wk-hvst-z2-r11` remains present |
| Removed contents total about 44.7 GiB logical | Manifest's rounded per-tree values sum to **44.67 GiB**; not a direct measurement of net freed clusters |
| All removed HEADs preserved | **33/33** HEADs remain reachable from current kept refs, checked using `git for-each-ref --contains` |
| Five detached HEADs pinned | **5/5** named archive refs resolve to the recorded HEAD |
| Scratch preserved in local archive | **14/14** archive directories exist; contents were not independently compared byte-for-byte |
| One candidate excluded for untracked work | Manifest verdict UNTRACKED for `wk-hvst-z2-r11`, an AMGT_HARVST deliverable directory |

MSTR reports per-row checks for git write age, HEAD age, tracked changes,
submodule commit preservation and untracked content before removal. Those checks
are preserved in its execution record; CRO's independent checks above are narrower
and do not prove that every potentially valuable file was classified correctly.

**Fresh volume measurement:** at **13:01:40.232 ET**, free space was
**54,703,968,256 bytes = 50.95 GiB (54.70 decimal GB)**, against the unchanged
473.705 GiB capacity. MSTR's script reports "4.34 GB before -> 54.77 GB after";
its summary does not establish the byte divisor, so this brief uses the fresh
byte-denominated CRO measurement. Concurrent writers mean the free-space delta
need not equal summed logical checkout sizes.

**Proposal corrections:** MSTR says the classification reads ran approximately
**12:18–12:28 ET**, not 12:30–12:45. The 102-candidate message meant the original
104 candidates minus two that became LIVE at the 12:27 dry run. Both discrepancies
flagged in section 1 are now explained; neither figure describes the final batch
after Andrew's recent-worktree exclusion.

The completed reclamation reduces immediate capacity pressure. It does not
resolve the SentinelMonitor deadlock, restore the damaged CRPS14-5 checkout,
recover the empty message, or prove future crash-capture readiness. The proposed
owners and remaining prevention actions in the main brief still apply. CRO
performed read-only verification and record updates, with no destructive action.
