# The dell1 deploy refusal closed by exercise, and the CRLF phantom's remedy found already-landed -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-08 (Eastern; the later entries fall after 00:00Z 10-09)
**Task Order:** ad-hoc -- no TO held this session
**Status:** COMPLETE

Delta log. The seating/startup half is `seating_and_startup.md` @ab7bfa89d9 in this folder; this covers
everything after it.

---

## Objective

Read the applier-exception record once it reached this box, and turn the deploy refusal it NAMES into something
the control plane can act on. Then the CRLF phantom that followed.

---

## Compiler Tools

**archetype:** DIAGNOSE

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'APPLIER' --limit 20` | PASS | Found the real carrier (a COO inbox file) when the launcher's named deliverable path was ENOENT. Denominator 31/70,214, bands printed. |
| comp-find | `comp-find 'filemd5(\|filesha256(\|...' --limit 40` | PASS | Sized the TF file-hash surface: 79 hits / 70,836 files, SURFACED=16. Answered "which hash sites read a TEXT file" -- exactly one. |
| comp-find | `comp-find 'partner_roster' --limit 15` | PASS | HEAD/DEF bands put `safe_deploy_core.py`'s S3 mapping on screen immediately, which is what made the uncovered file a DEPLOYED-artifact finding rather than a config nit. |
| comp-iam | `comp-iam role cloudops-dell1-agent-user` | WARN (correct) | `No role matching` -- empty and right. It is TF-ROLE-scoped; the subject is an IAM USER absent from the TF role corpus. Honored the rail, got a true negative, then used the `# rail-checked:` marker. |
| comp-which | rail exercise | PASS | forwarder RAN. |

**What worked:** `comp-find`'s bands twice decided the shape of a finding rather than just locating text --
`[HEAD]`/`[DEF]` surfacing `safe_deploy_core.py` is why section 4 of the CRLF record says "deployed artifact"
instead of "another CRLF file".

**What failed:** nothing wrong, but two rail interactions are worth recording because both were MY error and
the rail was right:
1. I piped a `comp-find` census into `head`. The hook refused it -- CLAUDE.md's own "never `head` any census".
   Re-ran with `--limit`. A page is not an answer and a `head` destroys the denominator that makes it one.
2. `comp-find` WARNED that `\(` and `\|` are literal to python `re` and that "a 0-hit result may be this, not
   a real absence." My pattern used a bare `|` so alternation held, but the warning is the right shape: an
   instrument that can manufacture an absence should say so before you read the zero.

**Gap found:** `comp-iam` has no view of IAM USERS or GROUPS -- only TF roles. For an agent principal (which
is what every box seat authenticates as) there is no comp-tool, so the rail's only correct outcome is the
`# rail-checked:` marker. Worth a tool row someday; recorded, not escalated.

---

## Work Completed

### 1. The record, and an instrument that nearly produced a false absence

CTO msg 1215 said the 220xZ record was on `origin box/laptop 8fd120ea89`. My first check was
`git show --stat 8fd120ea89`, which listed 3 files, none of them the record -- i.e. it read as ABSENT.

**That was the wrong instrument.** `8fd120ea89` is a MERGE, and a merge's combined diff omits files that
arrive unchanged from one parent. The right test is tree membership:

```
git ls-tree -r --name-only 8fd120ea89 -- <path>   -> the path          (present)
positive control on the 212xZ sibling             -> the path          (instrument is live)
git log --oneline origin/CLOUD -1 -- <path>       -> f28690b46f        (already on CLOUD)
```

Read the bytes at `8fd120ea89:<path>`. Andrew's verbatim and both placements are in the record; placement 2
names the refusal that became the rest of this session.

### 2. The refusal: measured, not inherited

The record STATES dell1 is denied `ssm:GetParameter` on `/mdpf/custody_source`. It does not measure it, and
the grain of the grant cell depends on which kind of denial it is. Exercised on the live primitive as
`cloudops-dell1-agent-user` -- deliberately NOT `comp-iam` (models `(action)`, never `(action, resource)`,
fails GREEN) and NOT `simulate-principal-policy` (four false-deny modes, one false-allow):

| probe | result | what it establishes |
|---|---|---|
| `get-parameter /mdpf/custody_source` | rc=254, `AccessDeniedException ... no identity-based policy allows the action` | MISSING ALLOW, not a Deny to remove |
| same action, parameter that does NOT exist | **byte-identical denial** | denial is ACTION-level; principal holds it on NOTHING -> cell is "add the action", not "widen a resource" |
| `describe-parameters` | rc=0, 17 visible, target is 1 of the 17 | creds live, SSM reachable, parameter EXISTS -- only its VALUE is refused |

Control 2 also pinned a rule-22a RETRIEVAL trap live: for this principal **`AccessDenied` MASKS
`ParameterNotFound`**, so a failed `get-parameter` is never evidence about existence.

Then closed the two rows I had honestly left open rather than hand them over as questions:
- **No KMS leg** -- `lambdas.tf:25` declares `type = "String"`. Read from the build input, which is the sound
  route when the API that would answer is the one refused.
- **"cannot plan mdpf-pipeline" reproduced, and it is the ONLY refusal** -- the read-only plan refreshed every
  other resource and printed a full execution plan before failing on that single error.

Record: `707afdc6af`, then `7639399f60`.

### 3. The narrowing, which mattered

`lambdas.tf:25`'s own comment: the parameter's VALUE is operationally controlled -- the `bd -> schwab`
co-activation flip is a served-critical cutover via `aws ssm put-parameter` under never-widen + CVO co-sign,
with `lifecycle.ignore_changes = [value]`. Terraform only READS it. So the ask named the cell as
`ssm:GetParameter` and said explicitly it must NOT carry `PutParameter`, which would have handed this seat a
served-critical cutover the record does not grant it.

### 4. Grant landed; accepted by exercise

While reading the full grant surface I found `cloudops-dell-agent-plan-reads-policy` already granting
`GetParameter` on exactly that ARN -- which contradicted my own measurement. Rather than report a
declared-vs-applied gap, I re-exercised, which was the decisive move:

```
created 2026-10-08T23:24:52Z   (AFTER my 22:35Z measurement and the 22:38Z ask)
get-parameter        -> rc=0   (was 254).  Type String, Version 4, Value "schwab"
terraform plan       -> rc=0, ZERO Error: lines, "Plan: 0 to add, 1 to change, 0 to destroy"
PermissionsBoundary  -> null   (nothing was silently capping the set)
```

Cut read-only as asked, no `PutParameter`. The 220xZ carve-out ("only until that grant lands, and only for
that refusal") is spent: **dell1 plans mdpf-pipeline itself now.** Record `d11dfc18ba`.

**A correction belongs here:** I reported "2 writers of this principal's permission set." It is **10** -- the
group is a container for nine policies, not one writer. 451 action-entries across 10 documents, 10/10 fetched
with none silently failing. Had I stopped at two I would have reported a missing grant that already existed.

### 5. The CRLF phantom: the proposed remedy was already landed

CTO msg 1261 called the `mdpf_route_bindings` pending in-place PHANTOM and put the remedy at a
`.gitattributes eol=lf`. Confirmed the phantom independently off `terraform plan`'s own printed hashes --
md5 `650f893a` = HEAD blob, `f94e8e4c` = CRLF worktree; sha256 `98f5e9c5` = blob, `37eb8451` = worktree; all
four exact, and `13701 - 13516 = 185` = the exact CR count.

**But `.gitattributes:153` already carries the rule and `check-attr` has it in force, while `ls-files --eol`
reads `i/lf w/crlf attr/text eol=lf`.** An eol attribute governs CHECKOUT and never rewrites a file already in
the tree. DECLARED-but-UNAPPLIED; editing the rule changes nothing. Positive control:
`route_bindings_tieout.py`, same directory and attribute, reads `w/lf`. Sized: **28 of 28 worktrees**. And
`git status` is EMPTY, because autocrlf makes a CRLF copy read clean against an LF blob -- which is why it
survives in plain sight.

Uncovered member by subtraction (the glob is `*.yaml`): `data/mdpf/config/partner_roster.json`, `i/lf w/crlf
attr/`, no rule -- and `safe_deploy_core.py:202` ships it to `s3 code/scripts/gold/`. Exposure named, not
measured. TF blast radius: of the live file-hash sites exactly ONE reads a text file; all others hash `.zip`.

Record `8430c79f13`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Exercised the live primitive instead of `comp-iam`/`simulate` | `/cloud-ops` is explicit that comp-iam fails GREEN and the simulator has four false-deny modes plus one false-allow. The exercised call is the sound oracle. |
| Re-exercised rather than report a declared-vs-applied gap | The policy said granted, my measurement said denied. One of them was stale, and the call settles which. It was mine. |
| Did NOT re-normalize the CRLF file | Byte-identical content and a one-command fix, but it sits in 28 worktrees with 9 live seats. Choosing the scope is a decision about other seats' trees, not a one-file edit. |
| Cut the over-cap message instead of `send_override` | The broker refused at 151 words against 150. The override exists for a human operator's request; none was made. Cited the file instead, which is what rule 31 asks for anyway. |
| Did not spawn an L7 worker | Workers are COO subagents of the issuing task order. An AE seat spawning one is out of lane, and no order existed to cut into cells. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../deliverables/DELL1_SSM_GETPARAMETER_REFUSAL_MEASURED_20261008.md` | created, then both held rows closed, then closed-by-grant | `707afdc6af`, `7639399f60`, `d11dfc18ba` |
| `.../deliverables/DELL1_CRLF_PHANTOM_DIFF_SIZED_20261008.md` | created | `8430c79f13` |
| `.../logs/2026-10-08/grant_cell_and_crlf_phantom.md` | this log | see commit |

**No infrastructure was touched all session.** Reads only: AWS reads, three read-only `terraform plan` runs
(`-lock=false`, no state lock taken), source and git reads. The grant was cut by the control plane, not here.

---

## Blockers

None. Zero TOs held; the dell1 COOs are gated on 2026-10-09 scheduled fires. Two asks sit with
`1.0.0_SA_CTO~DELL1`: the CRLF re-normalization routing, and (now closed) the grant cell.

---

## Current State

`0.7.0_AE_CloudOps~DELL1` live (PID 8656), watcher re-armed each expiry (current task `bpbauuqxh`, script pid
17000), delivery ledger 2/2 ackable READ, 0 TOs assigned. **dell1 can now plan `mdpf-pipeline`** -- grant cut
23:24:52Z, verified by `get-parameter` rc=0 and a clean `terraform plan`, so the laptop no longer covers this
box for that refusal. Four records on `origin/CLOUD`. The one open technical item is the CRLF
re-normalization, whose scope is the CTO's call, plus the unmeasured `partner_roster.json` exposure.

---

## Next Steps

1. **Re-arm the watcher on each `[WATCHER-EXPIRED]`** -- one Monitor call, same turn, census first; reap only
   against the recorded pid.
2. **On the first apply order:** read it, flip `<status>` to `pending`, open the deploy-completion ledger entry
   in `org/critical_paths/change_management/` BEFORE acting (NEVER-2), apply via `.tools/safe-apply.sh`.
3. **If the CRLF re-normalization is routed here,** run it per the commands in `8430c79f13` and verify with
   `ls-files --eol` -> `i/lf w/lf` plus a `terraform plan` reading "No changes".
