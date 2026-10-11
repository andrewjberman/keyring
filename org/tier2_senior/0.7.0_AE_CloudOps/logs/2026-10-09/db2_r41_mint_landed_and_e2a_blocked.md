# The svc-custody-statement token is live and its reader grant proven; the real statement is blocked three gates upstream — 0.7.0_AE_CloudOps~DB2

**Date:** 2026-10-09
**Task Order:** IRPT_DASHBD.TO-DB-b-84 (COMPLETE) and IRPT_DASHBD.TO-DB-b-86 (issued, blocked)
**Status:** COMPLETE for DB-b-84; BLOCKED for DB-b-86

**archetype:** MIXED

---

## Objective

Land leg M of the signed svc-custody-statement never-widen pair on dell2 (mint one RS256 service token,
create one secret, get one reader ARN routed to the laptop and verify it), then run the pair's positive and
negative arms as the first real retained Performance client statement. The first order landed. The second
stopped before its first act on an input that has no producer this seat can reach.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| commit-gate.sh | `.tools/commit-gate.sh .../mint_svc_custody_statement.py` | PASS | py_compile + ds-precommit + ruff py39, 1 of 1 file. Its own WARN says it reads only .py/.sh/.tf/org/projects/*.json, so it was NOT cited for the .json or .md artifacts. |
| opal_naming.grade | `grade('opal/investor-reporting/svc-custody-statement','SECRET')` | PASS | CONFORMANT, canonical form equal to the name as given; control `svc-analyst-intake` also CONFORMANT. |
| opal_naming.name | `name('opal','investor-reporting','custody-statement','SECRET')` | WARN | ValueError "scope resolves to no scopes.json row" — CORRECT behaviour of the BUILD verb on a graded node type. My reading of it as a gate defect was wrong (rows S38/S39). |
| deploy_ledger.py | `open` / `close-leg B,M,R,V` / `hold` / `close` | PASS | `hold` REFUSED while an apply leg was open ("a half-landed deploy cannot be HELD (stays RED)") — the law working; not overridden. Legs hand-committed because fix 00d3393ff3 is not yet in dell2 HEAD. |
| proof-of-spec-check.py | `<instance> DB41-1-AC1,AC2,AC3 --governing-order <order>` | PASS | VALID rc=0 after four refusals, each fixed rather than overridden. |
| p41_round41.py (issuer's) | `. DB41-1-AC1 / AC2 / AC3` | PASS | 3/3 PASS. AC2 genuinely read FAIL between the mint and the grant and was committed as FAIL at that point. |
| comp-find | `--files 'issued_to>0.7.0_AE_CloudOps~DB2' org/missions`; `'CONFORMANT' lib infra/logic`; `'sel_[0-9a-f]{64}' org data`; `'cottonwood' .../IRPT_CUSTDY` | PASS | The zero over 21,422 files proved no order had landed unannounced; the second found `grade()`'s home; the third showed the only `sel_` ids in the estate are localhost dev fixtures. |
| comp-iam | not run | SKIPPED | Deliberate: it models `(action)` and never `(action, resource)`, so it reports GRANTED for a principal holding GetSecretValue on ANY secret. The criterion was precisely an (action, resource) question, so the live policy document plus per-ARN simulations with a positive control were the sound instruments. comp-iam would have read green on an ungranted ARN. |
| comp-blast / comp-routes / comp-cache / comp-schedule | not run | SKIPPED | The orders' own preflight declares them RUN-by-the-pair or NOT-APPLICABLE; no route, cache or schedule surface was touched. |

**What worked:** `comp-find`'s printed denominators turned three "is it absent?" questions into measured
zeros with their blind spots named (ephemeral-floor and binary files excluded). `grade()` settled the naming
question in one call once I read the full export list. `deploy_ledger`'s refusal to park an open apply leg
was exactly right and stopped me from hiding a RED entry.

**What failed:** nothing silently. Every refusal this session was loud and specific, and each named the fix.

**Gap found:** `PROOF_OF_SPEC.schema.json` `artifacts_produced` has no git-exempt `kind` for a live AWS
resource (the checker skips only `s3_object`/`ddb_rows`), so an order whose one deliverable IS a secret
cannot register it. Row `IRPT_DASHBD-S41`, routed to the schema owner.

---

## Work Completed

### 1. TO-DB-b-84 — the mint (COMPLETE, drained @`bf93e7f643`)

| Leg | Proof |
|---|---|
| B before-read | 3/3. Secret ABSENT (ResourceNotFoundException + a separate-invocation positive control on an existing secret, so a true negative). IB-pr-385 LIVE verified **by content**: `irpt-export-render` live CodeSha256 `c7jOyysB/…` EQUALS the built sha the CLOSED IB-pr-390 ledger declares for that function — deployed bytes against the BUILD INPUT, never by filename. Release 6b LIVE at `tdpterTM…`. |
| M mint + secret | `arn:…:secret:opal/investor-reporting/svc-custody-statement-9CmPmS`, version `733fd650…`, created 10:05:57Z. Claims exactly the pair's; the five forbidden claims absent; the minter also refuses any claim OUTSIDE the pair's set, so the set is closed rather than spot-checked. TTL exactly 90.0 days, exp 2027-01-07T10:05:57Z, rotate-by 2026-12-24. |
| R reader ARN | Applied by laptop `0.7.0_AE_CloudOps~CTL` at 12:21:00Z under `NFRA_CTLPLN.TO-APPLY-29`. I read the **v4 document**, not the version bump: 30 → 31 ARNs, exactly +1, my ARN present, 0 wildcards, 1 statement, 1 action. |
| V read-backs | MINT_RECORD.json + 3/3 criteria + proof_of_spec VALID. |

Credential discipline: `opal/auth/jwt-private-key` (`AWSCURRENT`, VersionId `579af491…`) read into memory
only and dropped after signing; the token handed to `CreateSecret` **in-process**, because a
`--secret-string` would have put a live bearer credential into process arguments. Nothing printed,
committed or recorded holds the key, the token or its signature.

The grant's evidence is a **true before/after**: the identical simulation — same principal, action, resource
ARN, binary and credential — returned `implicitDeny` before the apply and `allowed` after. Recorded as the
instance's mutant, because that is the control that discriminates. The unlisted arm used an *adjacent*
secret (`opal/auth/jwt-public-key-Z6dqNK`, sharing the `opal/auth/` prefix with a LISTED secret) so its deny
also shows the list is per-ARN, not prefix-wide. A positive control on a known-listed ARN, in its own
invocation, excluded the all-deny-instrument reading.

### 2. TO-DB-b-86 — the real statement (BLOCKED before its first act)

Both served reads AMENDMENT 1 names were done. They yield three of the runner's four selection fields:
`client_id` and `account_ids` from the served custody directory
(`s3://opal-data-cot/investor-reporting/directory/2026-10-07/directory.json`, 269 entries), and
`snapshot_id` from the served holdings `current/manifest.json` (latest_date 2026-10-07, revision
`8982ba98…967e`).

`account_set_id` (`sel_<64 hex>`) is the fourth and has no producer this seat can reach. An **exhaustive
nested key census** over all 269 directory entries — every path counted against a printed denominator —
contains no path named set, sel or snapshot. The runner's own docstring lists the selection among the
"INPUTS the runner does not invent", from an Opal operator's selection-create answer; `svc-custody-statement`
is admitted on three operations and selection-create is not one. Typing one would be a filled figure — a
defect under this order's refusal clause — riding a REAL Cottonwood submission as its query parameter.
Reuse was checked: 4,449 `sel_` hits over 57,618 files, all localhost dev fixtures.

Stopped per the order's own clause. Nothing submitted, nothing persisted, and **no deploy ledger opened** —
one for an act that cannot proceed would be a RED half-landed entry for no act.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Proceeded on the pair-signed secret name after `name()` refused it | Both signed halves and the order name it verbatim and the CTO half signs "exactly this one secret"; the registry remedy was out of grant. Superseded for the better reason by ADDENDUM 9.3: secrets are GRADED, and `grade()` says CONFORMANT. |
| Did NOT override the row gate when it blocked on a foreign row | The blocking row was the issuer's own uncommitted `S42`, which carried a real id-coordinate defect. Overriding would have landed someone else's broken row. The issuer fixed it to `-D2-S1` itself. |
| Did NOT register the created secret in `artifacts_produced` | Measured twice as refused; recorded as a declared exclusion with the gap filed as `S41`, rather than mis-typing the kind to get past the checker. |
| Opened no ledger for DB-b-86 | The act cannot proceed, so an entry would be a RED half-landed deploy for no act. |
| Reverted my own `pending` flip on DB-b-86 to `issued` | ADDENDUM 11.1 states "DB-b-86 stays issued". The ruling governs over my reading, and it is the better description: the order waits on another project's cell. |
| Chose `comp-iam` NOT as the IAM oracle | It cannot express `(action, resource)` and would have read green on an ungranted ARN. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.../0.7.0_AE_CloudOps~DB2/mint_svc_custody_statement.py` | the minter (new) | Yes — `5b9cf603a9` |
| `.../0.7.0_AE_CloudOps~DB2/MINT_RECORD.json` | the record (new) | Yes — `5c81bbf102` |
| `.../0.7.0_AE_CloudOps~DB2/…TO-DB-b-84….proof_of_spec.json` | the instance (new, VALID) | Yes — `5c81bbf102` |
| `org/critical_paths/change_management/20261009T0952Z_svc-custody-statement-mint-20261009_…md` | ledger: 4 legs + NOTE 1 (grade verdict) + NOTE 2 (rollback trigger) | Yes — `d8f1432b22`, closed `5c81bbf102` |
| `.../task-orders/IRPT_DASHBD.TO-DB-b-84….md` | status → complete | Yes — `5c81bbf102` |
| `.../task-orders/IRPT_DASHBD.TO-DB-b-86….md` | status pending → reverted to issued | Yes — `4e42b99489`, `dd30563a89` |
| `.../IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` | rows S38, S39, S41, S43 | Yes — `fe6b451cee`, `ab1cd36b12`, S41 and S43 swept by `2.0.0_SA_COO~D2`'s own commits (the shared append-only race rule 14b tells you to take) |

---

## Blockers

- **BLOCKED on `ADVI_COTBKF`:** the Cottonwood returns gold holds **0 objects**
  (`crf._returns_paths('cottonwood')` computes `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/`;
  `head-bucket` rc=0 as the positive control, so a true empty and not a deny). CTO ADDENDUM 11.1 names this
  the real blocker, first in line, and says FWD-12 waits on it **and nothing else**.
- **BLOCKED on the laptop (via `0.0.0_AB_MSTR~DELL2`):** `hop3_real_run.py` must RUN there — the firm bucket
  denies the dell2 user by design and that is not widened — and no hop3 output exists in the repo. It runs
  only after the returns gold lands rows.
- **BLOCKED on a future IRPT_DASHBD cell:** the runner is to accept the seat-authored selection FILE.
  An operator seat minting `account_set_id` was REFUSED (ADDENDUM 9.2 stands).

---

## Current State

`svc-custody-statement` is live and usable: secret
`arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/investor-reporting/svc-custody-statement-9CmPmS`,
firm-bound to `cottonwood`, TTL 90 days to 2027-01-07, rotate-by 2026-12-24 with rotation owned by
`2.0.0_SA_COO~D2`; its ARN is ARN #31 on `cloudops-dell-agent-platform-secrets-policy` v4, which
`cloudops-dell2-agent-user` simulates `allowed` on and `implicitDeny` on an unlisted sibling (laptop
`2.0.0_SA_COO~C` independently confirmed with a LIVE `GetSecretValue` at 13:0xZ, a stronger oracle than my
simulation and agreeing with it). TO-DB-b-84 is complete, its ledger CLOSED 12:36:36Z with 4/4 legs proven
and its sentinel gone, drained to `box/dell2` @`bf93e7f643`. TO-DB-b-86 is `issued` and parked behind the
three gates above, none of them this seat's. No ledger open, no worktree, nothing in flight.

## Next Steps

1. **[`ADVI_COTBKF`] Land the Cottonwood returns gold** — FWD-12 waits on it and nothing else (ADDENDUM 11.2).
2. **[`2.0.0_SA_COO~D2`] Cut the selection-FILE cell** — the runner takes a seat-authored file; if the API's
   `sel_<64 hex>` is a deterministic hash the runner computes it the same way and the ledger prints both
   inputs, else the statement records `selection_source: file` with its sha256 (ADDENDUM 11.1 item 1).
3. **[`0.0.0_AB_MSTR~DELL2`] Carry the cross-box hop3 ORDER to the laptop** after step 1 lands rows; the
   output returns as a file with its sha256.
4. **[`0.7.0_AE_CloudOps~DB2`] Re-cut a worktree and run DB-b-86** once those land — the before-read, the one
   submission, the two other-firm refusals and the one unrelated scoped read.
5. **[schema owner] Add a git-exempt `kind` to `PROOF_OF_SPEC.schema.json`** for live AWS resources (row S41).
6. **[`2.0.0_SA_COO~D2`] Rotate the token by 2026-12-24** — 14 days before exp, as the pair requires.
