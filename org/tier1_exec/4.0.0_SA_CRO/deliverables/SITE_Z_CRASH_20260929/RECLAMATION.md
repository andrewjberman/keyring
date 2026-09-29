# Joint storage recommendation — MSTR and CRO, 2026-09-29

Andrew asked the two seats to divide the work. MSTR owns developer-residue review;
CRO owns incident evidence, dedicated dump backing, pagefile and crash causality.
This document recommends scope. It does not authorize or execute deletion.

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
