# Session log -- 0.7.0_AE_CloudOps~S -- 2026-09-03 1600-1700Z -- NFRA_OPSEC202609 TO-OP-S-16-17-8R2 + TO-OP-S-25-26-27

**Serial:** 0.7.0_AE_CloudOps~S (fresh session; the predecessor was killed by Andrew at ~14:0xZ for
fabric-wide API connection issues -- not for anything it did, and nothing it filed is retracted)
**Project:** NFRA_OPSEC202609 ONLY (Rule 27, one project per instance)
**Issuer:** 2.0.0_SA_COO~Z

**Round 2 on this seat:** TO-OP-S-25-26-27 and TO-OP-S-16-17-8R2, both flipped **complete** this
session with VALID instances.

## Current state

**Both task orders are terminal and both deploy ledgers are CLOSED.** Five ~S-authored
change-management entries are committed; three commits sit LOCAL awaiting the integrator.

| what | state |
|---|---|
| `partner-firms/demo.tf` | **COMMITTED @`f570d3981e`** -- the first act, and the thing that unblocked everything else |
| TO-OP-S-25-26-27 | **complete** @`71f74091d0`, instance VALID rc=0, 7 of 7 PASS |
| TO-OP-S-16-17-8R2 | **complete**, instance VALID rc=0, 4 PASS + 2 UNCOMPUTABLE-by-ruling |
| ledger `opsec-r2-key-role-logs-target` | CLOSED, 6 of 6 legs |
| ledger `opsec-r2b-key-flips-and-demo-import` | CLOSED, 6 of 6 legs |
| push state | **LOCAL** -- `ls-remote origin SITEZ` = `001709c96e`; `is-ancestor` FALSE for all three commits |

**The bucket limb was NOT performed and is not owed.** Deliverable 2 is RETIRED by the face's 15:5xZ
amendment on PRD v0.9 @`001709c96e` (row Z-S37). `opal-data-security` reads AES256 at 16:44:47Z,
unchanged; no `put-bucket-encryption` was ever issued.

## The thing that mattered most this session: I did not re-run an apply that had already run

The restart package told me to re-quote the plan and **apply** the demo table's two settings diffs,
on the stated basis that the apply had never run. Two seats measured otherwise -- `0.0.0_AB_MSTR~Z`
in row **Z-S42** @`9a6343cf40`, then `2.0.0_SA_COO~Z` at 16:08Z, who **withdrew the instruction**
(19846) before I reached it.

**NEVER-2 is the whole lesson and it is worth stating plainly: an open ledger leg proves only that
the device that opened it saw no completion. It was a missing RECORD, not an unchanged WORLD.** The
fix for a missing record is a measurement, never a repeat of the act -- a re-apply here would have
been the rewind class.

**What settles authorship of the change is the TAGS, not the settings.** `Partner=demo` derives from
the module's `var.firm_id` and `Environment`/`System` from the provider's `default_tags`. A console
toggle of PITR or SSE writes none of them. All five were live.

## What was verified, and what could have failed

**The replace control, on BOTH tables.** A DynamoDB SSE change is an in-place `UpdateTable`, but a
forced replacement would look like success at every other rung -- right name, right settings, plan
applied, data gone. `TableId` + `CreationDateTime` is the only pair that discriminates, because both
survive an update and neither survives a replace. `opal-suspicious-addresses` `b4af2a9e...` /
2026-09-03T04:29:37 and `opal-partner-demo` `99ddc090...` / 2026-06-03T15:26:08, both identical to
the cut.

**The plan decode, because live state cannot exclude a third diff.** Reading the live table proves
PITR and SSE are *present*; it cannot prove nothing *else* changed. `terraform show -json` on the
saved `r2b-demo.tfplan` gave the discriminating read: exactly **1 non-no-op row of 4**,
`actions=update`, `replace_paths` empty, the three real firms no-op. It also surfaced a **third
diff the face's "two expected diffs" wording does not name** -- `tags {} -> five`. Disclosed in
S8R2-AC1 rather than absorbed.

**A negative control on the deletion-protection instrument.** Row Z-S41's severity turned on
`DeletionProtectionEnabled=True`. `opal-pii-lookup` returns **False** on the same probe, so a True
is reported per table and is not the instrument's default. A positive-only pair could not have shown
that.

**The fixture as the EXERCISED rung.** `describe-table` says the project key is *attached*. Only a
write and a read through it say it is *usable*. put / get / GSI query (Count 1) / delete / scan
Count **0**, plus a re-issued `get-item` returning no Item as the control on the absence.

**Unscoped re-plans, deliberately.** `partner-firms` holds four instantiations of ONE shared module;
a `-target` re-plan cannot see a defect in what the members have in common. Both roots read
`No changes` rc=0.

## What I got wrong, and what caught it

- **I nearly reported a plan verdict from a clobbered exit code.** A command chain broke early on an
  unset `$TMPDIR`, and the trailing `${PIPESTATUS[0]}` printed **rc=2** beside the words "OPSEC
  PLAN". That 2 belonged to a **failed `jq`** -- terraform never ran. Caught by noticing the chain
  was `&&`-linked and could not have reached terraform. Both plans were re-run with `rc` captured
  into a variable immediately after its own command. *A pipe or a substitution resets the status,
  and rc=2 happens to be terraform's own "changes present" -- the wrong value was plausible, which
  is what made it dangerous.*
- **My first mint of the r2b instance was INVALID (rc=1, 7 violations).** I invented
  `method: "artifact_read"` (not an enum member) and put `cell_refs` on the acceptance rows, where
  the schema forbids them -- they live on the face's `<criterion .../>` tags. Fixed and re-validated
  to rc=0. *The checker also warned that its alignment figures print identically for an invalid
  instance and are not evidence of validity -- I did not quote them until the verdict was VALID.*
- **I assumed the TO directory was `task_orders/`.** `comp-find --name 'TO-OP-S-*'` returned a
  MEASURED zero over 20 files, which was informative rather than empty: the tree uses
  **`task-orders/`** with a hyphen. The pattern was right and my assumed path shape was wrong.

## A discrepancy I am reporting rather than smoothing

The restart package says **four** uncommitted change-management entries are mine to land. Measured:
**five** -- 0822Z, 0921Z, 0929Z, 1153Z and 1309Z all declare `0.7.0_AE_CloudOps~S`. I committed all
five and excluded the 1605Z `opsec-s2` entry and its sentinel, which declare `0.7.0_AE_CloudOps~Z`
and are **OPEN and in-window** -- a live peer's work on a shared tree. Classified by each entry's own
`Authored by` field, because a duplicate-id check is not a foreign-content check.

Separately, `S16178-AC3`'s status_reason discloses that the face asks for **two** ledger entries
("the two `opsec/` flips as one entry, the import + settings as another") and **one** was opened
covering both limbs across six legs. The face's phrasing presumes two opsec flips; deliverable 2 was
retired, so only one existed.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `terraform plan` (UNSCOPED) | `-detailed-exitcode -no-color` on `opsec` and `partner-firms` | Both `No changes` rc=0. The partner-firms run doubles as proof the first act worked -- before `demo.tf` was committed that root planned a destroy LINE. |
| `terraform show -json` | read-only decode of `r2b-demo.tfplan` | The instrument S8R2-AC1 needs; enumerated 1 non-no-op row of 4 and surfaced the unnamed tags diff. |
| `comp-read --enumerate` | `'<status>'` and `'status'` on both faces | Banded 3 hits to 1 WHOLE + 2 SUBSTRING and located the single `<status>pending</status>` at line 8 -- the flip target. A bare grep returns the same 3 and settles nothing. It also WARNed that every hit was a fragment, i.e. an anchored probe would read ZERO. |
| `comp-find --name` | `'TO-OP-S-*'` under the project tree | 0 hits / 20 files scanned -- a measured zero that corrected my path assumption. |
| `deploy_ledger.py` | `close-leg` x3, `close` x2, `check` | Both entries CLOSED, all legs proven. `check` then showed the remaining OPEN entries belong to other serials and other projects -- not mine to touch. |
| `proof-of-spec-check.py` | both instances, r2b with the face's expected id list | S-25-26-27 VALID rc=0 (7 rows); r2b INVALID rc=1 -> fixed -> VALID rc=0 (6 rows), 3 surprises all resolving to channel rows. |
| `aws dynamodb` (fixture) | put / get / query / delete / scan COUNT | The EXERCISED rung for S16-AC4; Count 0 at report with a positive control on the absence. |
| `safe-commit.sh` | 3 commits, `-F` msgfiles written by a non-shell writer | All rc=0, msg-verify MATCH. Its `commit-gate` WARNed it checked **0 of N** files on the `.md`/`.json` commits -- recorded here because that line is explicitly **not** evidence of a clean gate. |

## Blockers

**NONE that stop work.** One state to name rather than a blocker: **push is the integrator lane's
act**, not this seat's, so `f570d3981e`, `4370bcc705` and `71f74091d0` are correctly LOCAL. Stated as
MEASURED (`ls-remote` + `is-ancestor`), never defaulted.

## Next

Per the r2b face, this seat's next task orders are **OP-s-18** (the IP-set rules deriving from the
address table) and, after it, **OP-s-15** and **OP-s-19** carrying the deferred deny-outside-list --
**cut by the issuer on this task order's complete flip**, which this session has now made. Awaiting
those cuts; not started, correctly.

**Not mine, and deliberately untouched:** the three broker task orders addressed to the BASE serial
(MDPF_GLOBAL.T2C, NFRA_SUBSTRATECARDING.TO-CARD-R-W4-COX, WSE_COTMDL.WS5) -- barred by the issuer;
and `opal-data-security`'s default encryption, retired by PRD v0.9.
