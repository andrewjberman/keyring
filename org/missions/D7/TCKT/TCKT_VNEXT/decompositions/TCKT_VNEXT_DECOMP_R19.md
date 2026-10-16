# TCKT_VNEXT decomposition -- ROUND 19, 2026-10-16, issuer 2.0.0_SA_COO~V2, dell2 -- the four cross-firm admissions of the ticket service (row IRPT_ANLREQ-D2-S134)

**Authority:** CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 7 (msg 8833): owner `2.0.0_SA_COO~V2`,
items 1 to 4 ruled; `2.0.0_SA_COO~T2`'s FWD-5 cross-firm tests are the acceptance, red before and green after; fan-out 4 per issuance (the dell2 CPU budget). No PRD addendum:
the ruling is a defect fix inside PRD C-FENCE, not an endpoint change. Row S134 disarms when T2's tests read green on all four.

## Measured at HEAD (box/dell2, 2026-10-16), read-only

- Item 1: `create_ticket` stores `requester.email` from the body (`lambda_function.py` about :1373); `notify_client` sends to `_client_recipients(item)` = that address (about :1182-1210).
- Item 2: `list_tickets` for `svc-analyst-intake` is unscoped (`_resolve_scope` scopes only INTERNAL); `authorize("LIST")` admits it (about :188).
- Item 3: `_profile_scope` returns `(None, None)` (every firm) for a PROFILE row with no `allowedFirmIds` or an empty list (about :418-423); pinned by `tests/test_no_row_refuses.py`.
- **Live data (read-only scan of `opal-users-v2`, internal rows only, no address read):** 23 internal PROFILE rows: 19 ACTIVE with NO `allowedFirmIds` (14 with no userType, 5 `Dev`), 1 disabled, 2 with a non-empty list (1 `Dev`, 1 `service`), 1 `service` row whose value is a string. So item 3 as ruled **locks out 19 active staff the moment it deploys** unless those rows first carry the explicit marker. The ruling names the marker ("Opal staff who file for any firm carry the explicit global marker") but not its shape or the migration: both are fixed below and the migration is a cell (a users-table write, under its own pair).

## CONTRACT (fixed by the issuer; every order cites it; a change is an amendment to each order it touches)

1. **Notice recipient (item 1).** Env `CLIENT_NOTICE_CONTACT_MAP`: JSON `{"<firm id>": ["<address>", ...]}` (default `{}`; malformed = `{}` and a log line). The client notice's recipient for a ticket is
   derived ONLY from `map[ticket.requester.firm]`: if the stored `requester.email` (stripped, lower-cased) is IN that list it is the recipient; else the FIRST address of the list is, and the
   body value is ignored and logged as `WE_CLIENT_RECIPIENT_IGNORED firm=<f> to_digest=<digest of the ignored address>` (never the address). An absent firm or empty list: NO send, log
   `WE_CLIENT_NO_CONTACT firm=<f>`. Single-recipient by construction stays. `requester.email` is still STORED as today (display). No other route changes.
2. **Analyst-intake scope (item 2).** Env `ANALYST_INTAKE_ALLOWED_FIRMS`: csv of firm ids, `ALL` dropped as a wildcard (the `COMMENTARY_ALLOWED_FIRMS` pattern, `lambda_function.py:82`), unset or empty = NO firm.
   `list_tickets` for `svc-analyst-intake` returns only tickets whose `requester.firm` is in that set (a firm filter applied BEFORE `limit` is not required: the table is small and the item filter
   already follows the fetch); every other route's behaviour for the principal is unchanged. Live value: `49financial,inflection,cottonwood`.
3. **Fail-closed profile scope (item 3).** A PROFILE row's firm scope is exactly one of: (a) `allowedFirmIds` a non-empty list of non-empty strings: that set (as today); (b) the attribute `scope_all_firms`
   exactly BOOL `True` and NO `allowedFirmIds`: every firm (the explicit global marker, for Opal staff who file for any firm, J7); anything else is REFUSED with `403 {"error": "firm scope not configured"}`
   and the log line `FIRM-SCOPE-NONE-CONFIGURED` (no attribute and no marker, an empty list, or a `scope_all_firms` of any type but BOOL True), or `403 firm scope malformed` (BOTH the list and the marker present, a
   non-list `allowedFirmIds`). The status test, the no-row and the lookup-error refusals are unchanged.
4. **The register (item 4)** is the issuer's own direct act: `deliverables/2.0.0_SA_COO~V2/R19_GLOBAL_ADMISSIONS_REGISTER.md`, one row per global admission (route, principal, reason, source line).
5. **Terraform (cell tr):** the ticket Lambda's environment gains exactly `CLIENT_NOTICE_CONTACT_MAP` = `{}` and `ANALYST_INTAKE_ALLOWED_FIRMS` = `49financial,inflection,cottonwood`; nothing else.
6. **Migration (cell mig, the applier's, staged):** `scope_all_firms = True` written to EXACTLY the active internal PROFILE rows with no `allowedFirmIds` at the read (19 today, count and a list of opaque row keys printed, no
   address), each with `ConditionExpression attribute_not_exists(allowedFirmIds) AND attribute_not_exists(scope_all_firms)`. It runs BEFORE the code release of item 3. Rollback per row: remove the one attribute.

## Cells

| cell | builds | item | write surface | risk | depends on |
|---|---|---|---|---|---|
| `R19-nr-1` | `_client_recipients` derivation + the two log tokens + tests | 1 | `lambda_function.py` (the recipient functions and their call sites only), `tests/test_notice_recipient_firm.py` (new) | WORLD (path floor) | none |
| `R19-ai-2` | `svc-analyst-intake` list scope + the config read + tests; re-pin `test_list_scoped_firm.py:240` | 2 | `lambda_function.py` (`list_tickets` and a config constant only), `tests/test_analyst_intake_scoped.py` (new), `tests/test_list_scoped_firm.py` | WORLD | none |
| `R19-ps-3` | `_profile_scope` fail-closed + the marker + tests; re-pin `test_no_row_refuses.py:104` and every double that returned a row without a list | 3 | `lambda_function.py` (`_profile_scope` only), `tests/test_profile_scope_fail_closed.py` (new), the existing tests whose doubles lack the list | WORLD | none |
| `R19-ev-4` | the two environment values as Terraform source | 1, 2 | `infra/aws/terraform/ticket-center/main.tf` (the Lambda environment block only) | WORLD | the contract (names fixed above) |
| `R19-rg-5` | the global-admissions register | 4 | issuer's deliverables folder | LOCAL, DIRECT-ACT by the issuer | none |
| `R19-mg-6` | the staff-row migration | 3 | `opal-users-v2` (19 rows, one attribute each) | WORLD | pair, before REL |
| `R19-rl-7` | the release pair for items 1 to 3 (code, env), after `TO-R18-REL` or combined with it | 1, 2, 3 | `opal-ticket-api` | WORLD | L1, L2, L3, TR merged; MIG done; pair signed |

**AMENDMENT 1 (issuer, 2026-10-16, found at the drain; no new cell).** The whole-folder run on the merged tree (L1, L2, L3, TR) read 451 passed, 1 failed: `R19-ai-2`'s users stub in `tests/test_analyst_intake_scoped.py` returns a PROFILE row with no list and no marker, which `R19-ps-3` refuses. The fix (the stub's row gains `scope_all_firms: True`, no assertion changes) is a re-opening of `TO-R19-L2` (its step 7), re-seated in slot 46: the gate refuses a new order file in a round that already has an issuance, and the fix belongs to the cell that wrote the stub.

**Chains (M = 5):** {L1}, {L2}, {L3}, {TR}, {MIG, REL}. **Fan-out: 4 of 5 chains, cap 4 (the dell2 CPU budget), reason:** the three lambda cells edit disjoint functions of one file and merge at the drain (conflicts are
resolved by the issuer, hunks do not overlap); the applier's chain is staged behind them.

## Acceptance

Each worker cell has its own failing-at-base tests (the mechanical criterion) and one mutant that fires. The acceptance of the ROW is `2.0.0_SA_COO~T2`'s FWD-5 cross-firm tests, run red before and green after, by T2
after the release (`R19-rl-7`): T2 is told which tests this round makes green when each cell merges.

## Rule 24 record

- **MECE over the ruling's four items.** Items 1, 2, 3 are code cells L1, L2, L3 (one each); item 3's data consequence is MIG; the config values are TR; item 4 is REG; the release is REL. Nothing of the ruling is uncovered.
- **Same grain / one axis:** one cell per item per surface (lambda, terraform, data, register, release). **State coherence:** the marker's absence is refusal, so a staff row not yet migrated is LOCKED OUT, never
  widened; the migration runs first, which is why MIG precedes REL.
- **A name this round does not choose:** none (no S3 address, no resource name; env names and the attribute `scope_all_firms` are contract strings above).

## Battery

comp-schedule: DECLARED-NOT-APPLICABLE (no schedule). comp-iam: DECLARED-NOT-APPLICABLE for the worker cells (no IAM change; the migration is a table write the applier already holds). comp-adversary: the lens for L3 is a staff
row locked out by the deploy (measured: 19), for L2 an intake poller that loses a firm it needs (the three served firms are listed), for L1 an empty contact map (no client notice at all until Andrew or the CTO supplies the contacts: an
OPEN INPUT with owner `1.0.0_SA_CTO~DELL2`, not blocking the release).
