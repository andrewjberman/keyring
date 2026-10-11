# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-09 15:59Z to ~16:26Z

**archetype:** VALIDATE

Fifth segment (e71b 06:05-06:45Z, e60b 07:00-07:20Z, e79b 09:39-10:05Z, e84b 11:53-12:25Z). No deploy and
no world change: a client-data sweep reached this seat's own artifacts, and this records what was asked, what
was measured, and the one rule that now binds this seat going forward.

## What arrived

Two relays from `2.0.0_SA_COO~M1` carrying `0.0.0_AB_MSTR~DELL1`'s msgs 2717 and 2763: do not read, grep,
copy, quote, attach or `git show` `org/**/W73_S*_EVIDENCE.json`, the COTBKF worker ~74/~66/~70 cottonwood
manifests, or the IRPT_DASHBD tie-out files (`W73_S2_RESOLUTION.json` included), in the tree or in history,
until MSTR confirms they are out of dell1's tree.

**Complied verbatim, and the second relay changed what compliance looks like.** After msg 2717 this seat
verified non-involvement by a filename/metadata check. Msg 2763 adds "search" to the forbidden verbs, so
after it NO further probe of any restricted path was run -- not even for filenames. Scope is not this seat's
to widen or narrow (`org/XXX.md`: surface, do not adjudicate).

**One instrument lesson from the first check, worth keeping.** `git log --author=... -- 'org/**/W73_S*'`
returned empty and was nearly read as "clean". The positive control returned empty too, so the pathspec
simply was not matching -- `org/**/` does not glob here, `*W73_S*` does. With the working glob the file IS
tracked on this box (committed by `0.9.0_WK_IRPT_DASHBD~75`/`~76` and `2.0.0_SA_COO~D2`) and this lane's
authored count is 0 against a control of 1. **An empty result from an unvalidated pathspec reads exactly like
a true absence.**

## What this seat surfaced, and why it was not just an FYI

Legs P of e79b and e84b committed `E79_PREFIRE_VERSIONS_20261009.json` (18,178 keys, opal-data-bd) and
`E84_PREFIRE_VERSIONS_20261009.json` (1,136 keys, opal-data-cot), both on origin. They hold S3 key paths
under `gold/entities/clients/` -- which embed per-account identifiers -- plus object metadata. A sweep that
found 19,314 such key paths without context could reasonably read them as an unmandated client-data dump,
and this seat wrote them. So it went up as a scope ask rather than being sat on, with the point that they
were MANDATED (CTO condition 3 on e79b, COO condition 2 on e84b) and are the only restore targets for two
live acts. The ask named no identifier value.

Chain: SC1 msg 2779 -> COO msg 2781 -> MSTR msg 2783 -> `1.0.0_SA_CTO~DELL1` ruling @`dc2b1d9ee0`. Issuer's
interim ruling (msg 2782): hold both files in place, act only on MSTR's or the CTO's word.

## The ruling, and the condition it put on this seat

@`dc2b1d9ee0`: **OUT** of the sweep is a file whose only client-linked content is opaque relationship ids in
S3 key paths with object metadata; **IN** is any file pairing an id with a name, account NUMBER, address,
balance, market value, holding or transaction. ADDENDUM 1 (adopted from dell2) makes a bare custodial or
brokerage account number IN on its own.

Its condition 1 is the part that mattered: **M1 and SC1 confirm by a READ, never by recollection.** A
"hold released" message was therefore not the end of the work. The census -- committed @`aee269e3c0`,
`PREFIRE_FIELD_CENSUS_20261009.txt`:

- both files carry exactly ONE distinct per-entry field set, `{ETag, LastModified, VersionId, size}`, across
  all 19,314 entries; 0 fields beyond it; value types `str/str/str/int` only;
- 0 JSON keys matching name/account/balance/market_value/holding/position/transaction/address/household;
- ADDENDUM 1 test: **0** bare digit runs of 6+ without a pseudonym prefix, so no account-number shape;
- identifier shapes printed MASKED (digits -> `#`), because the ruling asks what shape they are, not what
  they are: `z########`, `z#######`, their `_views`/`_composition` siblings, a few single-digit ids, and
  `acct_z##########`.

**One shape was referred back instead of self-cleared:** `acct_z##########` (138 keys, E79). The id behind the
prefix is z-prefixed and pseudonymized, so by the ruling's test it reads as the producer's internal key --
but the prefix is literally `acct_`, and whether that is a custodial account number was the CTO's test to
apply. Clearing it here would have been the adjudication the ruling reserves. ADDENDUM 2 (~16:2xZ, read at
HEAD lines 37-43) ruled it **OUT**, citing this census: the test is whether an id is the CUSTODIAN's account
number resolving to a real account outside Opal's stores, and a vendor pseudonymous key is not. Hold fully
released; both files stay.

## The rule that now binds this seat

**Condition 2 of @`dc2b1d9ee0`: a rollback-handle file carries key paths and object metadata ONLY, never
object contents.** Both existing handles already comply. Any future leg-P-shaped enumeration by this seat
must be written that way from the start -- it is no longer a style choice.

Also still in force: relays 2717/2763 for the other paths, until MSTR confirms they are out of dell1's tree.

## Compiler tools

| tool | invocation | result |
|---|---|---|
| `git ls-files` / `git log --name-only` | `*W73_S*_EVIDENCE.json` with a positive control | The control is the finding: an `org/**/` pathspec matched nothing and read as clean; `*W73_S*` matched 1 tracked file. Lane-authored count 0 against a control of 1 -> true negative. |
| python field census | `PREFIRE_FIELD_CENSUS_20261009.txt` | 19,314 entries, 1 field set, 0 banned keys, 0 account-number shapes, shapes masked. Discharged condition 1 by read. |
| `git show` / `grep` at a pin | ADDENDUM 2 read at HEAD `:37-43`; ruling commit `dc2b1d9ee0` read by `--name-only` | Every ruling this segment was verified at its bytes, never taken from the message that announced it. |

No deploy, no table write, no send to a runner. Three messages out (the ask, the census report), all acked by
the recipient.

## Push state

`aee269e3c0` (the census) -- measured at write time as the newest commit of this segment; this lane does not
push a shared branch and `box-sync` carries it. Earlier segments' commits were confirmed ON ORIGIN at
13:32:00Z.

## AMENDMENT (2026-10-09 ~19:44Z) -- the 2717/2763 read bans are LIFTED; the line above saying they remain in force is superseded

The section "The rule that now binds this seat" ends by saying relays 2717/2763 stay in force "until MSTR
confirms they are out of dell1's tree". That is no longer the state, and a successor acting on it would
decline a read an order legitimately needs.

Sequence: Andrew-direct `9068d6f91d`
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md`,
read at that pin, 1,167 B) stops the containment sweep -- no purge, and no further moving, redacting or
renaming of tracked files for account ids; what landed stays. Reading it against the ban revealed that the
ban's release condition had become **unreachable**: it released only when the files left dell1's tree, and
item 2 guarantees they never will. Raised to `2.0.0_SA_COO~M1` at 19:41Z as a prohibition that had become
permanent by accident rather than by decision. `0.0.0_AB_MSTR~DELL1` msg 3086, relayed 19:44Z: **the bans on
the W73_S* evidence, the COTBKF manifests and the IRPT_DASHBD tie-outs are LIFTED** under that Andrew-direct.

**What replaces them (MSTR's guidance, and it is narrower than "lifted" sounds):** a read happens **only as an
order needs**, with **no copies into new places**. So these paths are not open browsing; an order is the
warrant, and nothing gets duplicated out of them. That sits exactly alongside condition 2 of @`dc2b1d9ee0` --
a rollback-handle file carries key paths and object metadata only, never object contents.

Note the e84b order's `<rules>` still restate the old bans as standing bounds. They bound that order's act,
which is closed (legs V, P, D); they are not a live constraint on new work, and the lift governs. No message
sent about that: it changes no act this seat owes.

**Also carried in practice, from item 3 of the Andrew-direct:** `client-data-check.py` stays wired but
WARN-only, and the hashed id list it needs is deliberately NOT built, so **it can never refuse a commit**.
Its silence is not evidence that a commit is clean, and it must never be cited as a pass.
