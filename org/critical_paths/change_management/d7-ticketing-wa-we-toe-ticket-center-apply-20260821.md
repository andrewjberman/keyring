# DEPLOY LEDGER — D7 ticket-center: W-A queue + W-E + TO-E + E-2 (ACT 1 of 4)

**Opened:** 2026-08-21T13:55:46Z by `0.5.0_AE_OpalETL~Z` (deploy-start; NEVER#6)
**Status:** **CLOSED 2026-08-21T14:07:57Z** — applied (1 added / 2 changed / 0 destroyed), 0-diff confirmed,
deployed bytes verified byte-identical to HEAD, both new grants verified on the live IAM primitive
with negative controls holding. **All 7 legs closed; nothing stranded.**
**GO:** Andrew-direct ~1346Z, VERBATIM: *"approved on all three, proceed"* — relayed by
`1.0.0_SA_CTO~Z` msg 4344, record @`8a99d851f2`
**Applying seat / device:** `0.5.0_AE_OpalETL~Z` on **site Z**, per **Rule 26** (the apply runs on the
device that owns the work). Measured, not assumed: all four build commits are ancestors of HEAD on
this box and all four are authored by this seat. **No ferry.**
**Terraform:** resolved on **PATH at v1.15.8**. ⚠ `.tools/terraform.exe` **does not exist on this
device** — the Git-section path is not device-portable; resolve, never assume.

## THIS IS A QUEUE, NOT A SINGLE CHANGE — and that framing is part of what Andrew approved

| commit | carries |
|---|---|
| `81c502cff2` | W-A native lifecycle analytics + claim enrichment + the day-one field set |
| `9121a55330` | WA-10 — the two enrichment degradation modes emit distinct greppable tokens |
| `b121c2f26e` | strips a non-ASCII glyph from production Lambda code |
| `8a748d8d31` | WF-5 (c) — `cutoff_et` on the LIST response |
| `180aa91223` | *(tests only — no deployable byte)* |
| `4d5a92f4d7` | W-E — the SES DL leg, sender pinned to `opalinvest.dev`, refuse-if-unset |
| `78cd2b0695` | TO-A — the W-E re-cut: recipient seam, field collapse, supersession sweep |
| `bbd6d4d842` | TO-E — the client leg: firm-aware link OMITTED not defaulted, single recipient |
| `429730ef7f` | E-2 — "An Opal advisor" + the three-way discriminating degradation log |

**9 commits, 8 deployable.** Surface: `lambda_function.py` + `main.tf`.

## PRE-STATE — Rule 22a CODE layer, measured before anything moved

Not the source map's self-report, not a plan 0-diff, not `get-function-configuration` — **all three
pass on stale code.** The deployed package was downloaded and its member hashed, resolved through
the **BUILD INPUT** (source map `source_dir` + `files`), never by filename:

```
deployed package        7,029 B   sha256(b64) s7HQH4u0ImUiNKZk2xgjuBQRDCqmUSACYJjcW7hl26E=
                                  == source map artifact_sha256                        TRUE
deployed lambda_function.py      22,333 B  sha256 4b7e1bbc...a426
  vs 1fd9ef2750 (recorded vintage)          IDENTICAL = TRUE
  vs HEAD                        59,874 B  IDENTICAL = FALSE      <- the queue, unlanded
  NEGATIVE CONTROL HEAD~20                  IDENTICAL = FALSE      <- so TRUE means something
```
**The deployed bytes are byte-identical to their recorded vintage.** No drift, no surprise; the
atom-decomp's finding re-derived independently at deploy-start.

## Legs (all must close in-session or roll back loud — NEVER#6)

| # | Leg | Change | Status |
|---|---|---|---|
| 1 | artifact | build + upload `ticket-center/opal-ticket-api.zip` with `content-sha256` metadata (the module reads it as `source_code_hash`) | **CLOSED** |
| 2 | data source | `data.aws_dynamodb_table.opal_users_v2` — a READ of the auth estate's table; plan fails loud if renamed/absent | **CLOSED** |
| 3 | data source | `data.aws_sesv2_email_identity.opalinvest_dev` — declared elsewhere (`ses.tf`), read not re-declared | **CLOSED** |
| 4 | IAM | statement `UsersDirectoryReadForClaimEnrichment` (`dynamodb:GetItem` on `opal-users-v2`) into `opal-tickets-table-rw` | **CLOSED** |
| 5 | IAM | NEW policy `opal-ticket-api-ses-send` (`ses:SendRawEmail` on `identity/opalinvest.dev`) — separate resource on purpose | **CLOSED** |
| 6 | env | `USERS_TABLE`, `TICKET_DL_MAP="{}"`, `TICKET_DEEP_LINK_BASE=""`, `CLIENT_LINK_MAP="{}"` | **CLOSED** |
| 7 | code | Lambda package -> the queue's `lambda_function.py` (22,333 -> 59,874 B) | **CLOSED** |

## ⛔ EXPECTED POST-APPLY STATE — read this before calling anything broken

**Legs 5 and 6 land an SES grant and THREE EMPTY CONFIG SLOTS. That is deliberate and it means the
internal DL leg will REFUSE on every ticket, loudly, by design:**

- `TICKET_DL_MAP="{}"` -> `DLAddressUnset` -> **`WE_DL_UNCONFIGURED` on every create.** The DL does
  not exist yet (**`WE-1` is open — a tenant-admin act, not this seat's**). The refusal is the
  refuse-if-unset contract working, **not a failed deploy.**
- `CLIENT_LINK_MAP="{}"` -> **the client link is OMITTED for every firm.** Omission is the ruled
  degradation, never a default: an inflection client must not be handed a 49F link. **The client
  email still SENDS.**
- **A ticket create still returns 201 and a claim still returns 200 regardless**, because both
  notification legs are wrapped (`notify_dl_isolated:534`, `notify_client_isolated:729`) and the
  `put_item` commits before either runs.

**SEQUENCING, because it is easy to get backwards:** the IAM grant and the code land in the SAME
apply, so there is no intra-apply ordering problem. The constraint is on **EXERCISING** — a ticket
created *before* the grant lands reads *"works, no names"*, a green run that proves nothing.
**Exercise after the apply, never across it.**

## Rollback

Same-window `git revert` + re-apply of the prior `main.tf`, plus re-upload of the `1fd9ef2750`
artifact (its exact bytes are recoverable: `git show 1fd9ef2750:infra/aws/lambda/ticket_center/lambda_function.py`,
sha256 `4b7e1bbc...a426`, verified above). **No data mutation in this deploy** — the DynamoDB writes
the new code performs are additive (`if_not_exists` / `list_append`), so no row is destroyed and a
rollback loses no history.

## Close-out checklist (NEVER#6)

- [x] artifact uploaded + `head-object` verified (never trust a `cp` exit alone — the 2026-07-13 hung-shim lesson)
- [x] `terraform plan` read
- [x] applied through `.tools/safe-apply.sh` (never bare)
- [x] re-plan -> **0-diff**
- [x] **Rule 22a POST-STATE:** deployed package bytes re-downloaded and diffed against the build input
- [x] **WA-6:** `simulate-principal-policy` re-run -> `implicitDeny` must flip to `allowed`, one `--resource-arns` per call, positive control as a SEPARATE invocation
- [x] source map updated (`last_deployed_commit`, `artifact_sha256`, `last_deployed_at`)
- [ ] tag + `push --follow-tags` (Rule 6)  <- NOT YET DONE at ledger-close-write; ticked only after the act
- [x] ledger CLOSED

## Close-out record (2026-08-21T14:07:57Z)

```
plan            1 to add, 2 to change, 0 to destroy
apply           rc=0 -- 1 added, 2 changed, 0 destroyed
re-plan         -detailed-exitcode = 0  ("No changes")            <- THE 0-DIFF
tag-authz gate  PASSED (0 candidate resources overwrite an access-granting tag)
tombstone gate  PASSED (1 create checked against 7 tombstones, clean)
CODE (22a)      deployed member 59874 B sha 96bd2df5... == HEAD; PRE was 22333 B == 1fd9ef2750
                negative control HEAD~20 != deployed, before AND after
IAM  (WA-6)     GetItem/opal-users-v2  implicitDeny -> ALLOWED
                SendRawEmail/opalinvest.dev  implicitDeny -> ALLOWED
                +1 positive control allowed, +2 negative controls HELD denied
source map      artifact_sha256, last_deployed_commit 1fd9ef2750 -> 8c1f26d84b, last_deployed_at
```

**TWO GATE EVENTS, both correct:**
1. **HALT-GATE blocked the first apply** on a pending message — my own, 15h old, and it is about
   **ACT 3**: it records the on-box path as `/opt/m365-mcp-gateway`, which is exactly the G1
   question reopened 90 seconds earlier. Acked with `HALT_ACK=1` after reading it; it does not bear
   on this apply.
2. **comp-tagauthz failed closed** — *"could not produce a plan JSON"*. **I did not override it.**
   Reproducing its own two commands by hand showed both succeed, which located the real cause:
   `safe-apply.sh:31` resolves `$TERRAFORM` to `$SCRIPT_DIR/terraform.exe`, and **`.tools/terraform.exe`
   does not exist on site Z.** The gate could not run because its BINARY was missing — not because
   the plan was dangerous. Resolved with the script's own documented `SAFE_APPLY_TERRAFORM` knob,
   which makes the gate **RUN** rather than bypass it. ⚠ **The error message steers toward
   `TAGAUTHZ_OVERRIDE`, i.e. toward bypassing a safety gate, when the actual fault is a device-specific
   path.** Surfaced separately as a finding.

## NOT DONE, deliberately — WA-1 / WA-2 stay open

The **deployed exercise on a REAL ROW** was not performed. Creating a live ticket fires the client
leg, which is **an SES send to a real address** — an external egress act outside ACT 1's scope, and
not something to do unilaterally to tick a box. WA-1/WA-2 remain `UNCOMPUTABLE-BY-CONSTRUCTION`
with that exercise named as their later run.
