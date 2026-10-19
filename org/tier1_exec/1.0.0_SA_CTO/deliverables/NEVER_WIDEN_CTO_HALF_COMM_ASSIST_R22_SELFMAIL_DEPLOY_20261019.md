# CTO never-widen half -- COMM_ASSIST round 22, cell CA-p-2: the mail handler refuses mail Andrew sent (targeted apply of `module.ldo_001`, CODE ONLY)

**Author:** `1.0.0_SA_CTO` (laptop), 2026-10-19 ~17:0xZ. **Binds:** the COO half
`org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/NEVER_WIDEN_HALF_COO_COMM_ASSIST_R22_SELFMAIL_DEPLOY_20261019.md` (SIGNED by
`2.0.0_SA_COO~CA`), on the SAME PIN **`e6c37673c8`**, staged @b0782e1a73. **Authority:** Andrew's word to `2.0.0_SA_COO~CA` at ~16:26Z (record
`org/tier1_exec/2.0.0_SA_COO~CA/ANDREW_DIRECT_20261019_162xZ_MUSE_NO_SELF_DRAFT_RULE_APPROVED_AND_CALL_2396_WAIT_NATURAL.md` @8eb8c7408a).

## Blast radius (what the act may touch)

- **Exactly two functions' CODE:** `module.ldo_001.aws_lambda_function.handler` and `.ingress[0]`. No environment value, policy, secret,
  Terraform resource, image or queue moves. The `INGRESS_MARK_MODE` stays `enforce`.
- **One data effect:** a `from_andrew` count key added to mail objects' `counts`. The old code ignores it, so rollback leaves it harmlessly.
- **Behaviour change, read from the code at the pin, not predicted:** `data/transcripts/scripts/teams_chat/mail_requests.py` @e6c37673c8 adds
  `_my_addresses()` (Andrew's mailbox from the cached `/me` answer, key `mail`, lowercased) and refuses a mail whose sender address equals it
  as `from_andrew`, BEFORE the domain and body tests. Read by this seat: `git diff 1aa63bde67 e6c37673c8` on that file is the only runtime
  change (+17 -5); the Terraform root, the ldo module and `handlers.py` read 0 changed.

## Both branches (the COO half's own rule, as written)

- **A** (targeted plan 0/2/0, keys a subset of {`source_code_hash`, `last_modified`}, never `environment`, pre-state hash
  `RoH5DIiH/lWEutB+Qb3CswFUB402LhOjbx6P5sbk2DE=`, mode gate `verdict=OK`, `check_p2_equiv.py` `ok=True`): APPLY through `safe-apply.sh`.
- **B** (anything else listed in the COO half): apply NOTHING and report.

Both are covered. Branch B is the guard against a live state other than the one the COO read at ~16:5xZ, so this half does not re-read it.

## Rollback, per key

As the COO half states: the saved live zip, then a targeted apply from a detached worktree at `1aa63bde67` back to the `RoH5DIiH...` hash, plan
0/2/0, no environment change. ACCEPTED.

## Rulings on the two items flagged for the CTO

1. **The four foreign files** (`exemptions.json`, `legacy_addresses.json`, `lib/opal_naming.py`, `NAMING_SCHEMA.json`) ride the package. ACCEPTED:
   they are other seats' merged changes already on box/laptop, and the COO's equivalence check reads 17 of 17 address probes identical, so
   nothing the assistant writes or reads moves. Their presence is named in the ledger entry.
2. **"Thread whose latest message is Andrew's" is not buildable for mail** (one message per event). ACCEPTED as a named residual. For mail the
   rule is "never draft for a mail he sent"; a colleague's earlier mail in a thread he has since answered keeps its draft until he drops it.
   The same holds for an alias or second address of his.

## Condition added by this half

**The `me-without-mail` raise is a full stop of mail drafting, not a single-event fault.** If the cached `/me` has no `mail`, EVERY mail event
raises and retries. So the COO half's condition 8 tightens here: the applier reads the first mail event after the apply, and if that event
raises `me-without-mail`, it rolls back the same window without waiting for a second one.

**SIGNED** -- `1.0.0_SA_CTO`, pin `e6c37673c8`. The CVO half is still owed (`3.0.0_SA_CVO`).
