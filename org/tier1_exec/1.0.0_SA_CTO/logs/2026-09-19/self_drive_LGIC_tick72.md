# /self-drive LGIC -- tick 72 (2026-09-19 ~05:5xZ-06:2xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260916_052xZ_LGIC_GOAL_AND_30M_SELF_DRIVE_ADJUDICATE.md`
**Scope:** `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM`. **Device:** laptop. **state: ARMED**

## Sequence and scope

Clean; CAPACITY **AT CAP 3/3**. **0 open of 153** again (NAMING 0/34, ENFORCE 0/65, CANON 0/30, LGCTFM 0/24),
re-measured at write time. **COMPLETION TEST: NOT DONE -- 1 of 4** (`LGIC_NAMING` `complete`; the other three
`active`). LGCTFM round 4's **L9 landed @`d383c4f360`** while this tick ran; **no L10 slug yet**, so no round
analysis is owed by this seat this tick. **No open calls in scope.** Inbox: one message, `98145`, acked READ.

## THE ACT -- **`W3-S47` TAKEN, AND IT SPLIT IN HALF ALONG A LANE I DID NOT KNOW I WAS ON THE WRONG SIDE OF**

`W3-S47`: `terraform fmt -check` rc=3 on `generated_locals.tf`, alignment-only, at **every** registry state ever
measured. Cause found and fixed @`9d876af0b0`: `lib/opal_naming.py::_hcl()` emitted exactly one space before `=`,
and `terraform fmt` aligns an attribute group on its **widest key**, so the file could never be canonical.

**Proved on the check's own run, never on the padding rule restated:**

| arm | result |
|---|---|
| `terraform fmt -check -diff` on the patched output | **rc=0** (was rc=3) |
| `diff -w` committed vs patched output | **rc=0** -- ZERO semantic delta; 88 lines, all whitespace |
| `validate` | OK, 25 system rows / 9 scope rows |
| `pytest lib/tests/test_opal_naming.py` | 2 failed / 91 passed -- **IDENTICAL at HEAD unpatched** |
| `_hcl(` call-site census | 9 sites, **every one** inside `_gen_locals` -- one consumer, no other carrier moves |

The suite arm is a **negative control, not an assertion**: I restored HEAD's blob `30a818c7fe`, ran the suite, got
the same two failures, then re-applied and verified by hash `7af34272c5`. Both failures **pre-date** the edit.

### ⛔ AND THE HALF I CANNOT DO -- MEASURED, NOT ASSUMED

| file | rule | lane | this seat |
|---|---|---|---|
| `lib/opal_naming.py` | `lib/**` | `BASE_EXEC` | **PERMITTED** |
| `infra/aws/terraform/modules/opal_name/generated_locals.tf` | `infra/aws/**` | `CLOUD_OPS_OR_ETL` | ⛔ **REFUSED** |

⛔ **THE GENERATOR'S OWNER IS MECHANICALLY BARRED FROM LANDING THE GENERATOR'S OUTPUT.** `W3-S47`'s rc=3 is measured
on the **committed** file, so the fix commit does not disarm it. ⚠ **My tick-70 AND tick-71 logs both called this
"a `lib/opal_naming.py` edit, mine as the generator's owner" -- HALF TRUE, and the half they named is the half I
can do.** Two ticks of carrying an item whose blocking half I had never resolved.

**Held on a SECOND ground that is my own signature:** blob `494ac9aa39` is input #4 of the `IB-rtf-5` halves and my
half refuses a plan read from different bytes for any of the first four. A whitespace regen before Andrew's step 4
**voids both halves and buys nothing.** ⭐ **So the unblocking condition is ON THE ROW and falsifiable, not in a
seat's memory:** an AE-lane seat regenerates and commits **after** the apply lands or is abandoned; `W3-S47`
disarms on the `fmt -check` rerun **against the committed file** at that point. Asked of `2.0.0_SA_COO~B`, whose
apply already runs from a permitted lane -- **no new seat, one command, ordering load-bearing.**

## ⭐ THE UNSCOPED ARM PAID FOR ITSELF TWICE

**Regenerating ALL targets writes TEN files, not one.** Eight differ from their committed bytes -- and **printed
rather than counted, 8 of 8 are MARK-LINE-ONLY.** Every generated **body** is current; eight provenance marks name a
registry state one revision old, because `IB-rtf-4` regenerated `generated_locals.tf` after the CRO's flip
@`845343f925` and nothing regenerated the other eight. ⭐ **The flip moved `bucket_provisioned` /
`bucket_managed_by` -- fields NONE of those eight blocks render. That is why nothing went red, and it is the S77
asymmetry from a THIRD instrument: the field whose two readers disagree is one most generated consumers never read.**

### ⛔ AND THE TRAP THAT CAUGHT ME FIRST

**One `generate` run prints two different hashes under the same `registry@` label, six lines apart:**
the summary `GENERATE: ... at registry@9f4a569d7a54b53c`, the file it wrote `registry@bde094a53078c35b`.
Neither is wrong -- the summary hashes **ALL** registry files, the mark hashes **only the files that target reads**
(`:1680`). The **mark** prints its scope as its own `over <files>` clause; **the summary prints none**, so the whole
asymmetry lands on the reader. ⛔ **I read the two, concluded STALE, and was ONE `diff` from reporting a stale input
on a SIGNED never-widen act.** The diff came back **byte-for-byte identical** -- so blob `494ac9aa39` is now
**CONFIRMED LIVE rather than merely pinned**, corroboration the sign-off did not have when I signed it.
⭐ **A false STALE on a generated carrier is exactly the reading that triggers a regen -- the act that would have
voided both halves for a file that had not changed.**

**Second trap beside it:** the worktree registry files carry **CRLF** (`scopes.json` 297 CR, `exemptions.json` 161
CR) where the HEAD blobs are **pure LF**. The generator normalizes; a hand-rolled content hash would not.

## Rows filed @`48ecbe6bf8`

`IRPT_BCKEND-S80` (the two-lane split + the hold condition) - `LGIC_ENFORCE-S94` (the two-hash trap + 8-of-10
stale marks) - `LGIC_ENFORCE-S95` (the suite's 2/91 baseline, surfaced off-task, **EXPOSURE not INCIDENT**, and the
name()-vs-worked-case question deliberately **NOT** adjudicated -- guessing it would be the forward-list error).

## Errors this tick

1. A heredoc **halved my backslashes**, so a `str.replace` patch matched 0 of 1 and silently did nothing -- caught
   by an `assert count==1`. Re-done with the `Edit` tool.
2. A `find` segment hit the comp-rail; ⛔ **the denial aborted the whole call, so the regen chained after it never
   ran.** Re-run with `os.walk`. **The catalogued failure mode, met in the wild.**
3. `send_message` refused twice on `message` vs `body` -- **loudly, nothing sent**, which is the gate working.

## RESERVED cards at Andrew -- unchanged, all five unruled

**Step 4 is still the only gate on `IB-rtf-5`** -- `AccessDenied` 2 of 2, re-measured by `2.0.0_SA_COO~B` at 05:2xZ.

## Compiler Tools

`sequence-check.py` - `surprise-row-gate.py::_open_tos_census` (twice: open and write time) - `.owned-paths.yaml`
lane resolution by most-specific rule with `permitted_agents` printed - `lib/opal_naming.py generate` (targeted and
**unscoped**) - `terraform.exe fmt -check -diff` + `validate` - `diff` / `diff -w` - `pytest` with a **restored-HEAD
negative control** - `git hash-object` / `rev-parse` (CRLF and blob arms) - `comp-find --name` - `commit-gate.sh` -
`safe-commit.sh` x3 - `ack_messages` - `send_message` x2.

**PUSH STATE at write time:** LOCAL @`fb90ef5e9e`; origin/CLOUD `d574016490` (`ls-remote` read). **state: ARMED**
