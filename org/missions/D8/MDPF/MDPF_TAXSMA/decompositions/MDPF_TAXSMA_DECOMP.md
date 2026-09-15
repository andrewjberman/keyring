# MDPF_TAXSMA -- DECOMPOSITION (L5) -- round 1 -- v2

```json
{
 "project": "MDPF_TAXSMA",
 "directive": "D8",
 "macro": "MDPF",
 "fabric": "laptop",
 "round": 1,
 "decomp_version": "v2",
 "supersedes": "v1 @62cf5796fc (frozen, never issued; cut against PRD v0.3)",
 "step": 5,
 "prd_ref": "org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@671925aecc",
 "prd_version": "v0.5",
 "prd_signed_at": "5061a43a46 (ratified-text 3.0.0_SA_CVO @2560f51f83; brief 4.0.0_SA_CRO @d4b71666ff; metadata finalized @671925aecc); prd-signoff.py status reads ADMITTED",
 "contract_ref": "org/standards/MDPF_TAXSMA_DATA_CONTRACT.json@671925aecc (version 0.5.0, RATIFIED)",
 "manifest_ref": "org/missions/D8/MDPF/MDPF_TAXSMA/prd/component_manifest.yaml@671925aecc (19 owned surfaces S01-S19, 8 dependencies D01-D08, 49 components)",
 "ground_truth_ref": "workflows/atom_decomposition/runs/mdpf-taxsma/20260915T0510Z/rectangle.final.certified.json@4ff8d9bdaa",
 "lgic_exceptions": "R20 X7 (49financial served home, CONDITIONAL) and X2 (Global composite, PERMANENT) GRANTED @9cf4a274db",
 "author": "2.0.0_SA_COO~T",
 "cells": 27,
 "edges": 39,
 "chains_maximal_paths": 21,
 "components": 1,
 "critical_path_cells": 14,
 "cell_id_shape": "TX-<axis>-<n> (DECOMP_CELL_ID_CONVENTION shape 1)",
 "worker_serial": "0.9.0_WK_MDPF_TAXSMA~<slot>",
 "cut_head": "7f1ab996a0",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~T`, seated by `0.0.0_AB_MSTR` (msg 97080, LD-0569 @f0f86cae9a) on Andrew's seat order ~12:5xZ 2026-09-15,
verbatim: *"If push mdpf_taxsma as the next one followed by nfra_oplgtw"* (SEQUENCE.yaml v4 @8f0c4fa2bf, stage 0). One project,
this seat. L5 is the COO's; no seat certifies this before L6.

**Input, graded before use.** `python .tools/prd-signoff.py status MDPF_TAXSMA` at ~20:0xZ: v0.5 @671925aecc **ADMITTED**, both
halves SIGNED and current (v1 was cut at v0.3 @8120db1ff9). `.tools/receiving-check.py` on the PRD: **ACCEPT** (`prd-manifest`: manifest, ENDPOINT, header,
outcome cards and header/section agreement present). v0.3 is the LGIC conformance addendum (CTO 97115; CLAUDE.md Rule 30
@a3d77717df): F1 workbook source `gateway`, F2 the Silver surface S19 between S02 and S03, F3 S08 writes only the two
historical served keys. The v0.2-to-v0.3 diff was read line by line (`git diff 60c722fe64 61748ba2e0`); v1 was cut against v0.3;
this v2 is cut against v0.5.

**v2 against v0.5.** PRD v0.4 (@d317a65ec7, `prd/TRADED_FIELD_ADDENDUM_97192.md`) makes the workbook's existing Traded
column the live-account key, dates membership FIRST_OBSERVED_UTC, retires the manual CONFIRM_EFFECTIVE_MEMBERSHIP step,
separates the source-dated `business_active_accounts` from the valuation-dated expected/covered counts, and records the
named G-A identity. Its own S01-S19 map to v1's cells is the recut's input: the seven-column source interface (TX-g-1,
TX-b-1, TX-b-2) is unchanged; membership, assets, aggregation, publication, consumer, proof, recovery and activation
change. This v2 also carries 1.0.0_SA_CTO's two corrections to v1 (97179): TX-i-3's secret is graded by `grade()`, and
G-R's trigger is LGIC_ENFORCE's EN-r-5 drain. The cell set, edges and chain read are unchanged from v1. PRD v0.5 (@5061a43a46,
`prd/REVIEW_REPAIR_V05.md`) repairs the Gateway row on 3.0.0_SA_CVO's refusal (@91875c897c): the route's own guard runs
before generic `/ms/*` handling, and the named account is bound by its validated Entra tid/oid, the email being display and
audit metadata only (NFRA_OPLGTW v0.2 C1/C2/A3). It also states the UTC-date-to-session comparison.

**Andrew's words in flight, and their class.** ~14:0xZ at this terminal Andrew asked whether Tax SMA needs Gold at all, then said
*"dont take my word for it, just /draw"* (record @1a133f12c2): a QUESTION, answered on the merits, not a ruling; CTO 96960
governs placement (1.0.0_SA_CTO~A ACK97091; CVO N6). ~14:3xZ at the CTO terminal: *"im hesitant on taxsma until i know its in
pattern with lgic rulings"* (97104) -- discharged by the conformance read (97116), "RECS APPROVED" (97127) and both v0.3
signatures. ~16:2xZ: *"I want to push through MDPF_TAXSMA"* (97153). ~18:0xZ: *"id have the opalbloomberg@opalinvest.com sitez terminal
account do it"* (G-A, record @f95470f384). ~18:3xZ: *"We dont need a human we use a key ... "Traded" signifies that the account
is live, thats what we use to count an active account"* (record @1729cef85e), which superseded his ~18:0xZ "active" field.

**Frozen at the cut.** A cell that looks wrong mid-round is a **surprise row, never an edit**
(`org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md`).

**What binds every cell, from the PRD and the law.** Every new S3 address is `lib/opal_naming.py address()` output and every new
resource name is `name()` output (Rule 30); a secret's path is one `grade(<path>, "SECRET")` returns CONFORMANT for (no secret
builder exists; CTO 97179). A builder refusal is a registry row, never a typed path. No production activation of
the workbook read before `TX-r-3` measures access for the named identity (`opalbloomberg@opalinvest.com`, G-A @f95470f384). Synthetic Gateway responses only until then (PRD §3.9). No client
name, full account number, balance or token enters the repository. Unknown deployment facts are measured before they are used.

---

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

```
  SURFACE MANIFEST rows (PRD s.7; manifest expected_owned_ids) ................. 19   S01 .. S19
  minus rows excluded, read-only or delivered at L4 ............................  -0
  ---------------------------------------------------------------------------
  SURFACES THIS ROUND'S CELLS SERVE ............................................ 19   (each has >= 1 cell, s.3 coverage)
  relies-on dependencies D01 .. D08 ............................................  8   read only; no cell writes one
```

**Falsifier 1: the component manifest, the physical grain under the 19 surfaces.** `component_manifest.yaml@8120db1ff9`
declares **49 components**. Subtraction: 49 minus 8 relies-on dependency rows (D01-D08, read only) minus 1 activation record
(S16, written only by `TX-r-3` under G-A) = **40 build or artifact components**, and every one is written or produced by a cell
named in s.3 (the 9 produced artifacts: `workbook_snapshot` TX-b-1, `workbook_silver` TX-b-2, `membership_dispositions` TX-m-1,
`taxsma_assets` TX-m-4, `operational_control`, `firm_category`, `global_category` TX-a-2, `firm_served`, `global_served` TX-u-1).
One plane deviation is recorded in s.10 choice 3.

**Falsifier 2: every path the PRD cites.** `comp-adversary compose` on v0.5 (read-vintage @7f1ab996a0, 20:05:33Z): 19 of 19 cited
commits VERIFIED; 38 cited paths, 30 stable, **8 GONE -- and all 8 are the PRD's own PROPOSED_NEW paths** (the four Tax gold
modules, the Silver module, the journey test, the Gateway module, RECOVERY.md). Absence is their expected state at L5.

**Falsifier 3: the live substrate the addresses land on.** `address()` at HEAD, every artifact the contract declares, called as
declared: **7 of 9 resolve** (membership_dispositions, operational_control, taxsma_assets, firm_category -> `opal-data-49financial`;
global_category -> `opal-data-mdpf`; the two served keys are historical addresses under X7/X2). **2 of 9 refuse**
(`workbook_snapshot`, `workbook_silver`: `source 'gateway' is not a systems.json key`) -- the registry row is gate G-R (s.6).
`s3api head-bucket opal-data-49financial` rc=0, with `opal-data-assets` as the positive control (~14:0xZ).
`name("mdpf","49financial","taxsma","role")` = `mdpf-49f-taxsma-role`.

**Falsifier 4: drift of the v0.3 manifest's own pins.** Every component carrying `existence_check.last_commit`, compared with the
file's last commit at HEAD 7f1ab996a0 (`git log -1`, portal paths in the portal repo): **19 pinned, 14 SAME, 5 DRIFT.**
- `infra/aws/ec2/opal-gateway/app/server.py`: pin e3a9d207dc, now 6a4e94d734. NFRA_OPLGTW is rewriting the Gateway app
  (@51b0f7d823 `OG-a-1` alone was +3,523/-313), and the file moved again during this cut.
- the three portal consumer files: `aum.ts` d3487fc925 -> 46d2bc59a1, `CategoryViewTree.tsx` 0e1c232d5f -> c29a8b86a1,
  `ModelPortfolios.tsx` 2d64653239 -> 09309a40f5 (the 12:12Z portal promote). No open portal branch touches them (5 of 5
  `dsgn`/`d13`/`codex` branches diffed against DEV: 0 files).
- `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`: pin 5061a43a46, now 671925aecc, the approval-state finalization only (its
  `state` field; 1.0.0_SA_CTO~A 20:01Z).

Every cell reads its files at HEAD, never at the manifest pin.

**Status vocabulary.** Evidence columns take four values; NOT-EVALUATED is one of them, so non-evaluation is never a verdict:

| value | meaning |
|---|---|
| `MEASURED` | evidence in hand at the cut, instrument named |
| `DECLARED` | the PRD, contract or rectangle asserts it; not re-measured here |
| `NOT-EVALUATED` | not looked at. Not a pass, not a fail. |
| `N/A` | the field does not apply |

Cell status takes `OPEN`, `HELD` (a named gate stands, s.6) or `DONE`. At v2: 23 OPEN, 4 HELD (`TX-b-1`, `TX-b-2` on G-R;
`TX-r-2` on G-O; `TX-r-3` on G-W, G-P).

---

## 2. THE 8 BOUNDARY QUESTIONS, EACH ASSIGNED

The certified rectangle has 8 entities, each with an `unverified_boundary` cell; PRD §2 carries each as "what it does not
establish" (DECLARED from the PRD's table, not re-read from the rectangle). Assigned 8 of 8. None becomes an expected value
about the world before its cell reads it.

| # | question (short form) | cells that answer it |
|---|---|---|
| 1 | S1: eight traded claims are a snapshot, not a fixed list; the displayed 33.33 million includes prospects | `TX-b-1`, `TX-b-2`, `TX-m-1` |
| 2 | S2: the missing claims have no proven cause; candidates are not automatically traded; same-date non-overlap is not permanent | `TX-m-2`, `TX-m-3` |
| 3 | S3: technical BD enrollment is not the expected traded population | `TX-m-2` |
| 4 | S4: six values are not an eight-account total; a zero accrual placeholder is not proof of no accrual | `TX-m-4` |
| 5 | S5: registry membership proves neither a produced daily contribution nor correct Global inclusion | `TX-a-1`, `TX-a-2` |
| 6 | S6: source inspection, an upload or a declared route is not an authorized page read | `TX-u-1`, `TX-v-3`, `TX-r-3` |
| 7 | S7: an enabled schedule proves neither complete inputs, correct dates nor an exercised recovery | `TX-p-1`, `TX-a-2`, `TX-o-1`, `TX-r-1` |
| 8 | S8: this D8 project does not run or alter the D9 converter, open accounts, change strategy or grant access | every cell's bound 16 (s.8); `TX-m-1` (no workbook/trading write) |

---

## 3. THE CELLS -- 27

Ids per `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, prefix `TX`. Axes: `p` baseline, `g` Gateway capability,
`b` source capture (Bronze and Silver), `m` membership, reconciliation and dated assets, `a` aggregation and consolidation,
`u` publication, `k` Gold packaging, `i` access (one cell per Terraform root), `c` consumer, `v` validation, `o` operations,
`r` release and activation.

Path abbreviations, relative to the repo root: `GW` = `infra/aws/ec2/opal-gateway`; `GOLD` = `data/mdpf/scripts/gold`;
`SILV` = `data/mdpf/scripts/silver`; `TST` = `data/mdpf/tests/taxsma`; `PUB` =
`infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher`; `GLB` = `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda`;
`TFM` = `infra/aws/terraform/mdpf-pipeline`; `TFA` = `infra/aws/terraform/opal-assets`; `TFGW` = `infra/aws/terraform/opal-gateway`;
`PSRC` = `portal/src` (the portal repository, on a worker branch). Every cell also writes
`deliverables/0.9.0_WK_MDPF_TAXSMA~<slot>/` under the project and may append to the investigation file. A cell that can deploy
also writes `org/critical_paths/change_management/` and its `org/critical_paths/.open_deploys/<slug>.json` sentinel.

Each acceptance line is **one criterion**. `J` marks a judgment criterion: no verdict at L7, graded by `3.0.0_SA_CVO` at L9. A
criterion asserting a control states what must DIFFER when the control is engaged, and proves it against the same harness with
the control disengaged (spine L6); those are marked "(difference)".

### Baseline

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-p-1` | the pre-change baseline, read only | FWD-6, FWD-8; inputs to `TX-r-1`, `TX-r-2` | deliverables only | OPEN |

**`TX-p-1` acceptance**
- both served documents are read at their historical keys `s3://opal-data-portal-v2/platinum/mdpf/49financial/category-views.json` and `.../global/category-views.json`, each with object version, UTC LastModified, SHA-256 and the `tax` node's current fields
- the deployed code SHA-256 of `mdpf-gold-lambda` and `opal-assets-mdpf-portal-publisher` is read live and compared with the package each existing builder produces from source at HEAD, MATCH or MISMATCH printed per function
- the `mdpf-scheduled-floor` schedule and the publisher's 13:50 UTC trigger are read back live with state, expression and target
- `mdpf-gold-lambda-role` and `opal-assets-mdpf-egress-publisher-role` trust and every inline and attached policy are read back live
- `opal-data-49financial` versioning, default encryption, the four public-access-block flags and every bucket-policy Deny statement are read back live
- `GetRole` on `mdpf-49f-taxsma-role` returns NoSuchEntity
- a read-only SSM census of the Gateway host's app source reports whether any route string `taxsma-workbook` is registered, with its file denominator printed
- the home and newest partition of the existing b00 `canonical_valuation` output are read from `data/assets/scripts/gold/runners_49f/b00_canonical_valuation.py` and confirmed by a live Head or List, date printed
- `python -m pytest data/mdpf/scripts/gold/tests -q` at the cell's HEAD records its pass and fail counts with every failing test id (cut measurement: 92 collected, 89 passed, 3 failed, all in `test_global_fold_flag2.py`)
- every AWS call in the cell's command log is a read verb (Describe, Get, List, Head)

### S01, S18 -- the Gateway capability

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-g-1` | the `GET /ms/taxsma-workbook` capability module, its route registration and configuration keys, with unit tests | FWD-7 (S01) | `GW/app/taxsma_workbook.py` (new), `GW/app/server.py` (route registration only), `GW/app/config.py` (the two configuration keys only), `GW/tests/test_taxsma_workbook.py` (new) | OPEN |
| `TX-g-2` | the Gateway package carries the module | FWD-7 (S18) | `GW/deploy-to-ec2.sh` only if it does not already bundle the module | OPEN |

**`TX-g-1` acceptance**
- a GET with the configured capability bearer against a synthetic Graph worksheet returns exactly the contract's `capability.response_fields`
- every returned row carries exactly the seven `projected_columns` plus the three `row_metadata` fields
- (difference) the same request with the bearer absent, wrong, or valid only for another route returns UNAUTHORIZED_CAPABILITY, while the correct bearer on the same test client returns 200
- a non-GET method on the route is refused
- a caller-supplied site, item, sheet, range, URL, identity or query parameter is refused and never forwarded to Graph (each selector enumerated)
- the capability bearer is refused on every other Gateway route in the same test client
- with `TAXSMA_WORKBOOK_IDENTITY` unset, the route returns AUTH_REQUIRED and makes no Graph call
- (difference) with the same email and otherwise identical valid inputs, a principal whose tid alone differs from the configured pair yields AUTH_REQUIRED with zero token fetches and zero Graph requests, while the configured pair returns 200
- (difference) with the same email and otherwise identical valid inputs, a principal whose oid alone differs from the configured pair yields AUTH_REQUIRED with zero token fetches and zero Graph requests, while the configured pair returns 200
- a missing, unvalidated or caller-supplied tid/oid pair yields AUTH_REQUIRED before any token fetch
- a generic MCP, ms-ingest or OTP credential presented to the route yields UNAUTHORIZED_CAPABILITY
- a request to `/ms/taxsma-workbook` passes the route's own guard before any generic `/ms/*` handler runs (call-order assertion in the test client)
- the audit record carries the principal's tid/oid reference, with the email as display metadata only
- a NeedsLogin or revoked result from the token broker yields AUTH_REQUIRED, never an empty 200
- a synthetic Graph permission denial on the item maps to one contract error code, recorded in the audit record as distinct from a Gateway guard refusal
- an ETag change between the before and after reads beyond `etag_change_retries` yields SOURCE_CHANGED
- a used range over `max_used_rows_including_header` yields SOURCE_TOO_LARGE with the observed extent, never a truncated `complete: true`
- a duplicate or ambiguous expected header yields SOURCE_SCHEMA_INVALID
- a nonempty unrecognized row is returned with `row_kind` UNRECOGNIZED, never dropped
- across every test case, no response or audit record contains a prohibited field (Name, Advisor Contact, AUM (Mn), Divest Securities, Instruction, Comment, or any token), each enumerated
- every call writes one audit record carrying exactly `capability.audit_fields` and none of `capability.audit_exclusions`
- the Gateway test modules that collected and passed before the edit still do, count printed before and after (the two `moto`-dependent modules named as NOT-EVALUATED on this box)
- the tests add no dependency (no `moto`; the token broker and Graph are stubbed)

**`TX-g-2` acceptance**
- the package the registered deploy path builds at the cell's HEAD contains `app/taxsma_workbook.py` with SHA-256 equal to the source, member list printed
- when the builder already bundles the app directory whole, the cell records VERIFY-REUSE and changes no file
- `infra/aws/ec2/EC2_MANIFEST.json`'s Gateway row is read and its deploy path stated; the cell does not edit `deployed_commit`
- the command log contains no SSM send-command and no S3 put

### S02, S19 -- source capture

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-b-1` | the snapshot acquirer: Gateway call, byte-identical Bronze, typed failure results | FWD-1, 3, 5, 8 (S02) | `GOLD/taxsma_snapshot.py` (new), `TST/test_taxsma_snapshot.py` (new) | HELD (G-R) |
| `TX-b-2` | complete typed workbook Silver | FWD-1, 3, 5, 8 (S19) | `SILV/taxsma_workbook.py` (new), `TST/test_taxsma_workbook_silver.py` (new) | HELD (G-R) |

**`TX-b-1` acceptance**
- `address("gateway","49financial","bronze","taxsma_workbook","date=<YYYYMMDD>","<snapshot_id>-<response_sha256>.json")` resolves at the cell's HEAD, and the module computes its Bronze key only through that call
- a synthetic complete capability response is persisted byte for byte: the stored object's SHA-256 equals the SHA-256 of the response body as received
- ETag, acquisition time and SHA-256 are stored outside the body bytes
- (difference) a second persist of the same response is NO_CHANGE by conditional create, while a response with different body bytes creates a new object in the same harness
- each of the contract's 8 capability error codes maps to a typed failure result carrying the last successful snapshot's date when one exists
- no failure path returns an empty rows list or an empty membership
- with no prior snapshot, a failure yields an UNKNOWN denominator, never zero
- the module reads only the capability bearer and holds no delegated token (call-site census)
- a stalling stub proves the call is bounded by `gateway_total_seconds` 180, with 3 attempts and backoff 1 and 3 seconds

**`TX-b-2` acceptance**
- `address("gateway","49financial","silver","taxsma_workbook","date=<YYYY-MM-DD>","<snapshot_id>-<response_sha256>.parquet")` resolves at the cell's HEAD, and the module computes its Silver key only through that call
- a fixture snapshot with ACCOUNT_SLOT, BLANK, TOTAL and UNRECOGNIZED rows yields a parquet with the same row count and every `row_number` present
- all seven business columns follow `workbook.silver.business_scalar_schema`, and every non-NULL value populates exactly its matching field (checked over every row)
- every envelope field except `rows` is present in the parquet file metadata, including for a zero-row snapshot
- the Bronze address, `response_sha256` and `snapshot_id` lineage are present in the parquet file metadata
- two source rows sharing one account identity remain two rows
- (difference) replaying identical Bronze bytes produces no second leaf, while a response with changed bytes produces a second leaf in the same harness
- conflicting replay bytes for one key raise and never overwrite
- an unrepresentable scalar is refused, never coerced or omitted
- a missing or corrupt Bronze input yields SOURCE_UNAVAILABLE or SOURCE_SCHEMA_INVALID, never an empty parquet
- the output column set equals the contract's `business_columns` plus `row_metadata`, with no business filtering or column slimming

### S03, S04, S05 -- membership, reconciliation, dated assets

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-m-1` | business status and effective-membership history from Silver | FWD-1, 3 (S03) | `GOLD/taxsma_membership.py` (new), `TST/test_taxsma_membership.py` (new) | OPEN |
| `TX-m-2` | full-identity reconciliation, conflicts, candidates, base overlap | FWD-2, 6 (S04) | `GOLD/taxsma_reconcile.py` (new), `TST/test_taxsma_reconcile.py` (new) | OPEN |
| `TX-m-3` | case evidence for the four current exceptions (PRD §3.3), read only | FWD-2 (S04) | deliverables only | OPEN |
| `TX-m-4` | dated account observations and the correction ledger | FWD-3, 4, 5, 8 (S05) | `GOLD/taxsma_assets.py` (new), `TST/test_taxsma_assets.py` (new) | OPEN |

**`TX-m-1` acceptance**
- the module reads only the S19 Silver parquet and its metadata; a harness with the Bronze object deleted still classifies
- a full-sheet fixture (traded, funded-but-untraded, prospect, blank, total, conflicting) places each row in exactly one `business_status`, with a count per population printed
- Traded is parsed by trim and casefold into YES, NO or blank, and every other value is INVALID (each enumerated in the fixture)
- (difference) flipping only Traded from No to Yes on one row raises `business_active_accounts` by one, while changing only Ready or a funded balance on the same row leaves it unchanged
- `business_active_accounts` counts distinct validated full keys with Traded=YES, and the module reads no custodian, master, BD enrollment or value source (call-site census)
- two rows carrying one full key count once in `business_active_accounts`, and both rows carry CONFLICT
- a YES row without a valid full identity stays CONFLICT with its YES claim retained, never PROSPECT
- an invalid identity on a YES claim, an unknown Traded on an identified account and a nonempty unrecognized row each make `business_active_accounts` null with a reason, never a smaller number (each arm enumerated)
- a source or Traded-schema failure makes the current count null with last-good freshness, never an empty census
- a YES first observed at UTC time T opens an OBSERVE_TRADED interval inclusive from date(T), with `membership_date_basis` FIRST_OBSERVED_UTC and the S03 service actor
- (difference) an explicit NO observed on date D closes the interval exclusively on D, while a missing, invalid or disappeared row on D leaves it open
- a NO-to-YES change opens a new interval and keeps the earlier one
- an earlier Inception Date, Last Trade Date or `source_modified_at` never moves an interval's start (fixture with each set earlier)
- an observation at 2026-09-16T00:30Z opens or closes its interval on 2026-09-16, the UTC date, never on the exchange-local 2026-09-15
- (difference) a valuation date before the account's first observation is TRADED_HISTORY_UNVERIFIED, while the same date covered by a retained earlier complete NO observation reads inactive
- replaying one logical snapshot twice with different run UUIDs creates no second event and moves no date (`source_event_id` stable)
- an older unseen snapshot is retained with TRADED_EVENT_ORDER_CONFLICT and does not roll the current state back
- two conflicting snapshots at one `observed_at` are refused
- same-UTC-day transitions keep every event, and the latest accepted state governs that day
- a CORRECT_IDENTITY, CONFIRM_TRANSFER or RESOLVE_STRATEGY record without a source YES leaves the account non-live
- a legacy CONFIRM_EFFECTIVE_MEMBERSHIP record is read as historical evidence and activates nothing
- the dispositions key is computed only by `address("mdpf","49financial","state","taxsma_membership","dispositions.json")`
- the module has no workbook, BD roster or trading write call site

**`TX-m-2` acceptance**
- each accepted form (eight digits, ten digits beginning 00, four-hyphen-four) normalizes to the ten-digit key
- each of the contract's 9 `rejected_forms` is refused with INVALID_ACCOUNT, each enumerated
- an Excel numeric that lost precision, a scientific-notation string and non-ASCII digits are refused
- duplicate full keys raise DUPLICATE_ACCOUNT on both rows and neither is selected
- an expected claim matching 0833 `fact_acc` on full key under reporting master 0008335338 is EXACT_MATCH
- the same key under another master is MASTER_CONFLICT
- a workbook and custodian strategy disagreement is STRATEGY_CONFLICT even when the account number matches
- 0804-4932 is never treated as a reporting master
- (difference) a Tax-labelled custodian account absent from the workbook stays UNCONFIRMED and outside the expected set, while adding its TRADED_CLAIM row makes it expected in the same harness
- (difference) an expected claim with no matching 0833 record stays in the expected population with MISSING_CUSTODIAN, while the same claim with its record present is EXACT_MATCH
- a full-ID overlap against the 0824 base population for the same date yields BASE_OVERLAP
- an unavailable base source yields BASE_OVERLAP_UNVERIFIED and never passes by absence
- BD technical enrollment is carried on its own axis and never removes a claim from the denominator
- no captured log line or ordinary return value contains a full account key (scan over every test case)

**`TX-m-3` acceptance**
- the protected carriers available to a worker that hold full workbook identities are enumerated first, with a statement of whether the two uncorroborated claims can be joined on full key
- for each of the two traded claims absent from the latest 0833, a cause class is stated from dated 0833 and 0824 sources, or UNRESOLVED with the evidence that stops it
- for each of the two strategy conflicts, the workbook label, custodian label and source dates are stated under masked labels
- the deliverable contains no full account number, name or balance (masked last-four labels and aggregate counts only)
- the command log writes no dataset and changes no workbook, roster or custodian record
- J: each stated cause is supported by the evidence the deliverable cites

**`TX-m-4` acceptance**
- every observation row carries exactly the contract's `valuation.history_fields`, `membership_date_basis` and `membership_source_event_id` included
- values join b00 `canonical_valuation` on `account_id` and `business_date` and equal `net_mv_plus_cash` to the cent under decimal128(20,2), over a fixture with cash, long and short exposure, margin and an actual zero
- a missing canonical row yields CANONICAL_MISSING and an explicit unavailable row, never zero
- a duplicate canonical row yields CANONICAL_DUPLICATE
- each of the contract's `rejected_substitutes`, supplied as an input, is unused (each enumerated)
- `covered_accounts` counts only rows passing identity, observed membership, source date and value checks, while `expected_accounts` is computed before those filters
- wherever `expected_accounts` is known, `covered_accounts` + `unresolved_accounts` equals it
- a live claim with no custodian record is counted in `unresolved_accounts` with MISSING_CUSTODIAN and is never dropped
- a valuation date before trustworthy membership history yields TRADED_HISTORY_UNVERIFIED and no covered value, never a zero
- membership intervals are compared to `valuation_date` as ISO calendar dates, start <= valuation_date < end, never through an exchange-local timestamp
- `business_active_accounts` is carried into Gold from S03 unchanged and is never derived from covered rows
- (difference) with one expected claim unresolved `complete_value` is null with reasons, while resolving it in the same harness populates `complete_value`
- an unknown denominator is `expected_accounts` null with its reason, never 0 of 0
- `observation_id` is stable across two runs with different run UUIDs and clocks
- `observation_id` changes when the S03 event it rests on changes, and not otherwise
- (difference) identical knowledge on an existing date partition is NO_CHANGE, while changed knowledge on the same date enters pending control state for the next date and mints no second leaf
- a correction carries `supersedes_observation_id`, and the reader resolves an acyclic chain
- the reader refuses competing corrections, duplicate ids with different payloads and a missing superseded observation
- a correction-only partition does not reduce the resolved cohort (reader test across three partitions)
- the source basis is derived as ADDITIVE and validated against `GOLD/mdpf_category_registry.py` (key `tax`, `SMA_BASIS_ADDITIVE`), and a mismatch refuses the contribution with BASIS_MISMATCH
- the Gold key is computed only by `address("mdpf","49financial","gold","taxsma_assets","date=<knowledge_date>","data.parquet")`

### S06, S07 -- aggregation and consolidation

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-a-1` | the Tax contribution in the firm and Global aggregate series | FWD-6 (S06) | `GOLD/dim_mdpf_aggregate_aua_timeseries.py`, `TST/test_taxsma_aggregate.py` (new) | OPEN |
| `TX-a-2` | the Tax prelude inside the Gold handler, status propagation, run control | FWD-5, 6 (S07) | `GOLD/mdpf_gold_consolidator.py`, `TST/test_taxsma_consolidator.py` (new) | OPEN |

**`TX-a-1` acceptance**
- changed 49financial and Global series carry `aggregate_basis` INCLUDES_ADDITIVE, `base_excluding_tax_aua`, `tax_additive_aua` and `tax_coverage`, each aligned to `dates`
- with a fixed synthetic baseline and known Tax cents, Tax is added exactly once at Tax, SMA, ALT Strategies and 49financial
- Global's Tax equals the sum of firm Tax leaves, and Global's total adds Tax exactly once
- Client and every other firm's series are byte-equal to the same inputs' run without the change
- `source_basis` survives the Global fixed-key and reconstruction path for `tax`
- (difference) a TAXSMA path missing the `aggregate_basis` declaration is a schema failure, while the declared path in the same harness succeeds
- (difference) an overlapping full ID blocks the affected total, while the same fixture without the overlap completes
- unknown or stale Tax makes the SMA, ALT Strategies, 49financial and dependent Global complete totals null with coverage, while unaffected firms keep their values
- Tax coverage carries `business_active_accounts` and the dated expected, covered and unresolved counts as separate fields, each with its own date
- the same-vintage before and after arithmetic control is recorded with its input hashes

**`TX-a-2` acceptance**
- `lambda_handler` runs S02, S19, S03, S04 and S05 in order before 49financial and Global shaping, each gated on the prior stage's observed success record
- (difference) a Tax prelude failure (AUTH_REQUIRED) leaves every other firm's outputs identical to a run with the prelude disabled, while Tax and its dependents carry the failure status
- the `_last` behavior (consolidator lines 621-643 at 1465fd3f7d) never fills an unknown Tax leaf with a default zero or a positive parent (regression test)
- the withhold behavior (lines 646-660 at 1465fd3f7d) withholds an affected scope rather than zero-filling it (regression test)
- `operational_control` is written only at `address("mdpf","49financial","state","taxsma_control","current.json")` and carries no business value (schema assertion)
- firm category Gold resolves through `address("mdpf","49financial","gold","category_views",...)` and Global through `address("mdpf","global","gold","category_views",...)`
- every affected node carries the contract's `categories.wire_status_fields`, `business_active_accounts` included
- TRADED_STATUS_UNVERIFIED, TRADED_HISTORY_UNVERIFIED and TRADED_EVENT_ORDER_CONFLICT each propagate to the affected nodes' `reason_codes` (one arm per code)
- the expected completed session comes from `GOLD/mdpf_calendar_binding.py`, and with the calendar unavailable the run fails closed with CALENDAR_UNAVAILABLE
- a weekend or holiday run processes corrections without minting a new valuation date
- with the capability unconfigured the prelude records run_result DISABLED and the rest of the invocation is unchanged
- the MDPF Gold suite at the cell's HEAD fails only on the 3 pre-existing `test_global_fold_flag2.py` ids (no new failure)

### S08, S17 -- publication

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-u-1` | status-carrying publication to the two historical keys, destination repair, rollout switch | FWD-5, 8 (S08) | `PUB/lambda_function.py`, `TST/test_taxsma_publisher.py` (new) | OPEN |
| `TX-u-2` | the publisher package and its declaration | FWD-8 (S17) | `PUB/build_package.py`, `TFA/mdpf_portal_publisher.tf` | OPEN |

**`TX-u-1` acceptance**
- a harness that perturbs control-state values shows no served numerical value change (values come only from Gold parquet)
- (difference) a status-only control change updates the served document while the numeric source bytes are unchanged, and the same run without the status change is NO_CHANGE
- the control-state version is part of the publication idempotency key
- (difference) with unchanged source hashes a missing or corrupt destination is repaired through the same key, while a matching destination is skipped
- the served document carries `taxsma_contract_version` 0.4.0, document `taxsma_coverage` and node `coverage`
- `business_active_accounts` in the served document comes from Gold, never from control state
- the contract's `nullable_complete_fields` are null only where the complete value is unknown
- a scan of every fixture output finds no account identifier, name or protected evidence link
- the only served writes are `s3://opal-data-portal-v2/platinum/mdpf/49financial/category-views.json` and `.../global/category-views.json` (X7, X2), by call-site census and harness write log
- the 49financial Gold is read from the firm-bucket builder address and Global from the product-bucket address
- (difference) with the rollout switch OFF the served document is byte-equal to the pre-change output for the same Gold inputs, while with it ON the document carries the extension
- publication is reported complete only after source coverage, destination content and matching generation are checked

**`TX-u-2` acceptance**
- the built package contains every changed publisher module and the data contract JSON, each member's SHA-256 equal to its source
- `python .tools/check-lambda-layer-deps --function opal-assets-mdpf-portal-publisher` reports 0 FAIL
- a plan-only Terraform run changes only the publisher function's code and environment
- the rollout switch's environment value defaults to OFF in Terraform
- the command log contains no apply

### S12 -- Gold packaging

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-k-1` | the Gold function package carries the Tax and Silver modules and the contract | FWD-8 (S12) | `GLB/build_package.py`, `GLB/mdpf-gold-lambda.BUILD_MANIFEST.json`, `infra/aws/lambda/ci/lambda-source-map.json`, `TFM/gold-lambda.tf` | OPEN |

**`TX-k-1` acceptance**
- the package contains `taxsma_snapshot`, `taxsma_membership`, `taxsma_reconcile`, `taxsma_assets`, the Silver `taxsma_workbook` module and the data contract JSON, each member's SHA-256 equal to its source
- `python .tools/check-lambda-layer-deps --function mdpf-gold-lambda` reports 0 FAIL
- the Silver module is packaged inside `mdpf-gold-lambda`, and no second function or deployed code tree is declared
- a plan-only Terraform run changes only the Gold function's code and environment and adds no schedule, rule or trigger
- the command log contains no apply

### S13 -- access, one cell per Terraform root

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-i-3` | the capability bearer secret and the Gateway's read of it | FWD-7 (S13, opal-gateway root) | `TFGW/taxsma_workbook.tf` (new) | OPEN (G-S sequences its apply) |
| `TX-i-1` | the scoped Tax prelude role `mdpf-49f-taxsma-role` | FWD-7 (S13, mdpf-pipeline root) | `TFM/iam.tf` | OPEN |
| `TX-i-2` | the publisher's Tax status and firm-bucket category reads | FWD-7 (S13, opal-assets root) | `TFA/mdpf_egress_publisher.tf` | OPEN |

**`TX-i-3` acceptance**
- the plan creates exactly the capability bearer secret and one statement granting `opal-gateway-role` GetSecretValue on exactly that secret ARN
- the secret's path is one `grade(<path>, "SECRET")` returns CONFORMANT for, canonical form printed, its system and purpose tokens taken from `NAMING_SCHEMA.json`'s secret grammar (no literal path is named in this order)
- neither the Terraform source nor the plan output contains a secret value
- the plan shows zero changes to every other resource in the root, `taxsma_gateway_iam.tf`'s and NFRA_OPLGTW's included
- the ledger entry's OPEN sentinel is committed before the apply, citing both halves of G-S (s.6)
- the apply runs through `safe-apply`, and the ledger entry is closed and committed before the reads below
- (difference) from the Gateway host, GetSecretValue on the new secret succeeds for `opal-gateway-role`, while the same call on a secret the role does not hold is AccessDenied
- DescribeSecret shows no current secret value (the value is set only by `TX-r-3`)

**`TX-i-1` acceptance**
- the plan creates `mdpf-49f-taxsma-role`, trusting only `mdpf-gold-lambda-role`, plus one statement letting `mdpf-gold-lambda-role` assume it
- the role's allow statements equal the contract's `runtime_access_matrix` Gold-prelude actions on exact resource ARNs, compared statement by statement
- the role holds no served-JSON write, no workbook or roster write, no other firm's prefix and no wildcard firm-bucket statement
- the plan changes nothing else in the root
- the apply runs through `safe-apply` under a ledger entry opened before and closed before the reads below
- (difference) from a session of the role, a read under another firm's bucket prefix is AccessDenied, while the same read on the 49financial canonical valuation prefix succeeds
- from a session of the role, a PutObject to either served portal-v2 key is AccessDenied
- policy-simulation results and exercised results are recorded in separate, labelled sections

**`TX-i-2` acceptance**
- the plan adds to `opal-assets-mdpf-egress-publisher-role` only a read of the 49financial category Gold prefix and a read of the Tax control key
- the role gains no read of the workbook Bronze or Silver, the capability secret, the membership dispositions or `taxsma_assets`
- the plan changes nothing else in the root, and the existing served-write and Global grants are byte-equal
- the apply runs through `safe-apply` under a ledger entry opened before and closed before the reads below
- (difference) from a session of the role, GetObject on the Tax control key succeeds, while GetObject on a `taxsma_assets` key is AccessDenied
- the role's pre-existing comp-iam finding (GetObject on the portal-v2 latest pointer, GRANTED-ACTION/UNGRANTED-RESOURCE) is recorded as found, not repaired

### S09, S10, S11 -- the consumer (portal repository, worker branch, no push)

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-c-1` | the typed value/status/date accessor, cache TTL, refresh | FWD-5 (S09) | `PSRC/api/endpoints/aum.ts`, `PSRC/api/endpoints/__tests__/aum.taxsma.test.ts` (new) | OPEN |
| `TX-c-2` | the visible unknown, stale and zero Tax leaf | FWD-5, 7 (S10) | `PSRC/components/CategoryViewTree.tsx` | OPEN |
| `TX-c-3` | honest affected totals and real dates | FWD-5, 6 (S11) | `PSRC/pages/ModelPortfolios.tsx` | OPEN |

**`TX-c-1` acceptance**
- the accessor's category types carry the contract's value, status and date fields, `business_active_accounts` and `source_observed_at` included, and `tsc -b --noEmit` exits 0 in the portal
- a document with a missing or unknown `taxsma_contract_version` yields an explicit unavailable result
- `bun test` shows the category cache TTL is at most five minutes
- `bun test` shows a failed or incomplete transport response is not cached
- `bun test` shows an explicit refresh bypasses both the accessor cache and the query cache
- the caller URL remains `/api/general/mdpf/{firmId}/category-views.json`
- the command log contains no portal DEV or PROD push and no workspace gitlink change

**`TX-c-2` acceptance**
- an unknown or stale Tax leaf renders visibly with its date and reason, never hidden and never "$0"
- a true zero, an unknown denominator and known incomplete coverage render as three different states
- the source-dated live count and the valuation-dated expected and covered counts render as separately labelled figures, each with its own date
- TRADED_HISTORY_UNVERIFIED renders as unknown history, never "$0"
- the L1 zero-bucket amendment and the $10,000 display rounding are preserved for known values
- no account identifier or name is rendered
- the `tax` node stays under SMA under ALT Strategies
- `tsc -b --noEmit` exits 0

**`TX-c-3` acceptance**
- an affected total (SMA, ALT Strategies, 49 Financial, Global) whose complete value is null shows "unavailable" with its coverage
- a supplied confirmed subtotal is shown with its label, never in the complete-total field
- displayed dates are the document's valuation, knowledge and acquisition dates, with no time of day fabricated from a date-only field
- a missing transport or schema field yields an explicit unavailable display
- the page never presents the current live count as the dated covered count
- unaffected firms' figures are unchanged
- `tsc -b --noEmit` exits 0

### S14 -- validation (independent of every engine it grades)

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-v-1` | the independent expected-case manifest, A01-A08 | FWD-1 .. FWD-8 (S14) | `TST/expected_cases.json` (new) | OPEN |
| `TX-v-2` | the local controlled journey harness, producer end | FWD-1 .. FWD-8 (S14) | `TST/test_taxsma_journey.py` (new), `TST/fixtures/**` (new) | OPEN |
| `TX-v-3` | the consumer journey: logic tests and headless renders from the harness's own publisher output | FWD-5, 6 (S14) | `PSRC/components/__tests__/taxsma-journey.test.tsx` (new), `PSRC/components/__tests__/fixtures/taxsma/**` (new) | OPEN |

**`TX-v-1` acceptance**
- the manifest enumerates every arm of PRD §4's A01-A08 table with an id, its fixture input, its engaged and disengaged control, and its expected observable, with a count per property printed
- every expected number is worked by decimal arithmetic recorded in the file, and the authoring script imports no TAXSMA engine module (import census)
- the fixtures contain no real account number, name or balance
- J: the arm set is complete against PRD §4

**`TX-v-2` acceptance**
- the harness runs a synthetic Gateway through S02, S19, S03, S04, S05, S06, S07 and S08 against local artifacts only, with network calls blocked and the block asserted
- before any overall verdict, the harness prints expected, executed, missing and extra case counts against `expected_cases.json`
- every A01-A08 arm executes and its observed result matches the expected observable in `expected_cases.json` (per-arm table)
- each control arm runs engaged and disengaged in the same harness run and records what differed
- input, fixture and output SHA-256 are recorded for every arm with the commit the harness ran at
- a scan of every output and captured log finds no synthetic full account key outside the protected fixture files
- the A07 route controls (wrong identity, wrong route, wrong method, wrong bearer, other workbook, denied or revoked access) fail against the Gateway app test client, while the exact named-identity and exact-route control succeeds and is audited
- a Gateway guard refusal and a Graph permission denial are recorded as two distinct results

**`TX-v-3` acceptance**
- `bun test` over `taxsma-journey.test.tsx` passes the accessor and status-derivation arms
- the fixture JSON for each display arm is `TX-v-2`'s publisher output, cited by SHA-256, never hand-written
- for each of the seven A05 display states (complete, partial, unknown denominator, unknown history, stale, unavailable, true zero), the page is rendered headlessly through the installed `playwright` library and one screenshot per state is saved and read
- the seven rendered states are pairwise distinguishable in the captured DOM text
- the fixture with a Schwab record removed and Traded still Yes renders an unchanged live count beside an unavailable complete total
- no rendered page or DOM capture contains an account identifier

### S15 -- operations

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-o-1` | the operator recovery and reversal contract | FWD-8 (S15) | `org/missions/D8/MDPF/MDPF_TAXSMA/operations/RECOVERY.md` (new) | OPEN |

**`TX-o-1` acceptance**
- the runbook names each reader and moment in the contract's `operations.reader_moments` with the command for each decision step
- each named command is run once against `TX-v-2`'s local artifacts, with its output excerpt recorded
- the reversal procedure is dry-run against the local harness, with the non-Tax outputs unchanged
- the runbook commissions no alarm, watcher, email or comparator (text census)
- the runbook names no manual initial-attestation step and no active-column request (text census)
- the runbook separates a Gateway guard refusal from a SharePoint permission failure, with the check for each
- J: an operator can go from a failed receipt to a verified recovery using the runbook alone

### Release and activation (S16)

| cell | what it is | serves | writes | status |
|---|---|---|---|---|
| `TX-r-1` | the backend release with Tax DISABLED and the rollout switch OFF | FWD-8 | the change-management entry and sentinel; applies `TFM` and `TFA` through `safe-apply` | OPEN |
| `TX-r-2` | the Gateway release with the capability disabled | FWD-7 | the change-management entry and sentinel; `infra/aws/ec2/EC2_MANIFEST.json` through its deploy path | HELD (G-O) |
| `TX-r-3` | activation: the measured first capability read under the named identity, bearer value, prelude on, rollout switch on, live authorized readback | FWD-1, 7 (S16) | the protected `TAXSMA_WORKBOOK_IDENTITY` activation record; the change-management entry and sentinel | HELD (G-W, G-P) |

**`TX-r-1` acceptance**
- the change-management entry names both functions and every task family or alias the change reaches, and its OPEN sentinel is committed before the first apply
- the two applies run through `safe-apply`, one root at a time
- the deployed code SHA-256 of both functions equals the packages built by `TX-k-1` and `TX-u-2`
- the applied configuration reads the capability unconfigured and the rollout switch OFF
- an ad-hoc QA invocation of the Gold function records run_result DISABLED for Tax while the other firms complete
- after the next scheduled 13:50 UTC publisher fire, both served historical keys are content-equal to `TX-p-1`'s baseline on every field other than generation time (DELTA=0, comparison printed)
- the ledger entry is closed and committed before the grading reads

**`TX-r-2` acceptance**
- the entry cites NFRA_OPLGTW's `OG-r-1` release as read back (G-O), by path@commit
- the entry's OPEN sentinel is committed before the deploy, and the deploy runs only through `infra/aws/ec2/safe-ec2-deploy.sh`
- on the host, the deployed `app/taxsma_workbook.py` SHA-256 equals the source at the release commit
- the route with no bearer returns UNAUTHORIZED_CAPABILITY, and the Gateway audit record shows no Graph call for it
- with the identity unconfigured, the route with the bearer returns AUTH_REQUIRED
- after the restart an unauthenticated `/mcp` returns 401 with the resource challenge
- the ledger entry is closed and committed before the grading reads

**`TX-r-3` acceptance**
- the ledger entry cites the G-A record `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_180xZ_TAXSMA_WORKBOOK_IDENTITY_OPALBLOOMBERG_AND_ACTIVE_FIELD_MEMBERSHIP.md` @f95470f384 by path@commit
- `TAXSMA_WORKBOOK_IDENTITY` holds the Entra tid/oid principal of `opalbloomberg@opalinvest.com` in protected configuration, with the email as display metadata, and the approval reference is recorded in protected deploy evidence
- the never-widen sign-off (CTO and COO) naming both served keys, their writer count and each key's rollback is cited before the rollout switch turns ON (G-W)
- the compatible consumer is promoted under its applicable authorization before the switch turns ON (G-P), cited
- the configured tid/oid pair is resolved from the validated Entra principal context and recorded before the controlled read, with an email match alone refused as binding
- one controlled read through `GET /ms/taxsma-workbook` records the identity binding, the item and the result in protected evidence without rows or tokens
- the capability is enabled only after that controlled read succeeds; a refused read leaves it disabled and is reported, with no scope or grant change
- the served 49financial and Global documents, read through the authorized consumer route, carry the Tax leaf with its coverage and dates
- an unauthorized route control is refused
- the rollback (capability disabled, switch OFF) is exercised once, and the served documents return to the pre-activation shape
- J: an operator walkthrough explains one inclusion, one exclusion and one exception from the supporting records

### Coverage, run not asserted

**Outcomes, 8 of 8** (the PRD header's `endpoint_outcomes`):

| FWD | cells |
|---|---|
| FWD-1 | `TX-b-1`, `TX-b-2`, `TX-m-1`, `TX-v-1`, `TX-v-2`, `TX-r-3` |
| FWD-2 | `TX-m-2`, `TX-m-3`, `TX-v-1`, `TX-v-2` |
| FWD-3 | `TX-b-1`, `TX-b-2`, `TX-m-1`, `TX-m-4`, `TX-v-1`, `TX-v-2` |
| FWD-4 | `TX-m-4`, `TX-v-1`, `TX-v-2` |
| FWD-5 | `TX-b-1`, `TX-b-2`, `TX-m-4`, `TX-a-1`, `TX-a-2`, `TX-u-1`, `TX-c-1`, `TX-c-2`, `TX-c-3`, `TX-v-1`, `TX-v-2`, `TX-v-3` |
| FWD-6 | `TX-p-1`, `TX-m-2`, `TX-a-1`, `TX-a-2`, `TX-c-3`, `TX-v-1`, `TX-v-2`, `TX-v-3` |
| FWD-7 | `TX-g-1`, `TX-g-2`, `TX-i-1`, `TX-i-2`, `TX-i-3`, `TX-c-2`, `TX-v-1`, `TX-v-2`, `TX-r-2`, `TX-r-3` |
| FWD-8 | `TX-p-1`, `TX-b-1`, `TX-b-2`, `TX-m-4`, `TX-u-1`, `TX-u-2`, `TX-k-1`, `TX-v-1`, `TX-v-2`, `TX-o-1`, `TX-r-1` |

**Surfaces, 19 of 19:** S01 `TX-g-1` · S02 `TX-b-1` · S03 `TX-m-1` · S04 `TX-m-2` `TX-m-3` · S05 `TX-m-4` · S06 `TX-a-1` ·
S07 `TX-a-2` · S08 `TX-u-1` · S09 `TX-c-1` · S10 `TX-c-2` · S11 `TX-c-3` · S12 `TX-k-1` · S13 `TX-i-1` `TX-i-2` `TX-i-3` ·
S14 `TX-v-1` `TX-v-2` `TX-v-3` · S15 `TX-o-1` · S16 `TX-r-3` · S17 `TX-u-2` · S18 `TX-g-2` · S19 `TX-b-2`. Cells serving no
single surface: `TX-p-1` (baseline), `TX-r-1` and `TX-r-2` (releases).

**Acceptance properties, 8 of 8** (PRD §4). Each names the cells that build it and, last, where it is proved:

| A | built by | proved in |
|---|---|---|
| A01 business membership | `TX-b-1`, `TX-b-2`, `TX-m-1` | `TX-v-2` |
| A02 exact reconciliation | `TX-m-2` | `TX-v-2`; case evidence `TX-m-3` |
| A03 activation and dated correction | `TX-m-1`, `TX-m-4` | `TX-v-2` |
| A04 canonical value | `TX-m-4` | `TX-v-2` |
| A05 honest incompleteness | `TX-b-1`, `TX-b-2`, `TX-m-4`, `TX-a-1`, `TX-a-2`, `TX-u-1`, `TX-c-1`, `TX-c-2`, `TX-c-3` | `TX-v-2` (data), `TX-v-3` (rendered) |
| A06 additive arithmetic | `TX-m-2`, `TX-a-1`, `TX-a-2` | `TX-v-2`, `TX-v-3` (displayed totals); live baseline `TX-p-1` |
| A07 protected traceability | `TX-g-1`, `TX-i-1`, `TX-i-2`, `TX-i-3` | `TX-v-2` (route controls); live arms `TX-i-*`, `TX-r-2`, `TX-r-3` |
| A08 repeat and recovery | `TX-m-4`, `TX-a-2`, `TX-u-1`, `TX-o-1` | `TX-v-2`, `TX-o-1`, `TX-r-1` |

---

## 4. PLACEMENT AXIS

**Every cell executes on LAPTOP.** D8 is placed LAPTOP and the row's `fabric_ruling` carries it. AWS acts reach account
313476888478 (us-east-1) from this laptop; on-host Gateway probes run through SSM. **No cell is owned by a seat**; every cell is
served by a worker at L7 (`0.9.0_WK_MDPF_TAXSMA~<n>`). The portal cells (`TX-c-*`, `TX-v-3`) work in a portal worktree inside the
worker's workspace worktree (the portal is a gitlink) on a worker branch; nothing is pushed.

**Sovereign and person-operated acts are not cells.** The workbook identity (G-A, answered), the never-widen sign-off (G-W) and
the consumer's promotion authorization (G-P) are gates (s.6); `TX-r-3` carries out activation once G-W and G-P exist. Under v0.4
membership is automatic from the workbook's Traded column; no person attests it.

---

## 5. DEPENDENCY EDGES, CHAINS, AND THE FAN-OUT THIS SUPPORTS

Edges are keyed to **observed completion**: `A -> B` means B's acceptance cannot be evaluated until A's artifact is at HEAD (or,
for an apply or deploy, live and read back). `TX-i-3 -> TX-i-1` is a resource edge (the role's grant names the secret the Gateway
root creates).

```
  Gateway and access
    TX-g-1 -> TX-g-2      TX-g-2 -> TX-i-3      TX-i-3 -> TX-i-1      TX-g-1 -> TX-b-1      TX-g-1 -> TX-v-2
  capture and engines
    TX-b-1 -> TX-b-2      TX-b-2 -> TX-m-1      TX-m-1 -> TX-m-2      TX-m-2 -> TX-m-4
    TX-m-4 -> TX-a-1      TX-a-1 -> TX-a-2
  publication, packaging, consumer
    TX-a-2 -> TX-u-1      TX-u-1 -> TX-u-2      TX-u-1 -> TX-c-1      TX-c-1 -> TX-c-2      TX-c-2 -> TX-c-3
    TX-a-2 -> TX-k-1      TX-k-1 -> TX-i-1      TX-u-2 -> TX-i-2
  validation and operations
    TX-v-1 -> TX-v-2      TX-u-1 -> TX-v-2      TX-v-1 -> TX-v-3      TX-c-3 -> TX-v-3      TX-v-2 -> TX-v-3
    TX-v-2 -> TX-o-1
  release and activation
    TX-p-1 -> TX-r-1      TX-k-1 -> TX-r-1      TX-u-2 -> TX-r-1      TX-i-1 -> TX-r-1      TX-i-2 -> TX-r-1
    TX-v-2 -> TX-r-1      TX-p-1 -> TX-r-2      TX-g-2 -> TX-r-2      TX-i-3 -> TX-r-2
    TX-r-1 -> TX-r-3      TX-r-2 -> TX-r-3      TX-v-3 -> TX-r-3      TX-o-1 -> TX-r-3      TX-m-3 -> TX-r-3
```

**The chain read, computed from the 39 edges by a script (not chosen):**

```
  cells 27, edges 39, acyclic: yes (Kahn order covers 27 of 27)
  heads (no incoming edge) = 4 :  TX-p-1 TX-g-1 TX-m-3 TX-v-1
  leaves (no outgoing edge) = 1 :  TX-r-3
  edge-connected components = 1
  M, maximal head-to-leaf paths = 21
  longest dependency path = 14 cells :
    TX-g-1 -> TX-b-1 -> TX-b-2 -> TX-m-1 -> TX-m-2 -> TX-m-4 -> TX-a-1 -> TX-a-2 -> TX-u-1 -> TX-c-1 -> TX-c-2 -> TX-c-3 -> TX-v-3 -> TX-r-3
  width by earliest level:  L0 4 | L1 2 | L2 2 | L3 2 | L4 1 | L5 1 | L6 1 | L7 1 | L8 2 | L9 4 | L10 3 | L11 2 | L12 1 | L13 1
```

**THE BINDING FACTS.** (a) The project is **narrow and deep**: one component, four heads, a 14-cell critical path, nowhere
wider than four. The useful fan-out is the level width, not M. (b) The spine is **capture before membership before value
before aggregation before publication**: each engine reads the previous engine's typed output. (c) Two waits sit outside any
worker: **G-R** holds the head of the engine chain (`TX-b-1`) until LGIC_ENFORCE round 2's cell EN-r-5 drains the `gateway` row to CLOUD, and **G-W / G-P**
hold the single leaf (`TX-r-3`).

### The distinct-worker constraint

| cell | must not share a worker with | why |
|---|---|---|
| `TX-v-1` | every engine author: `TX-g-1`, `TX-b-1`, `TX-b-2`, `TX-m-1`, `TX-m-2`, `TX-m-4`, `TX-a-1`, `TX-a-2`, `TX-u-1` | PRD §4: a reviewer independently compares expected case ids to actual results; expectations are not computed with the code under test |
| `TX-v-2` | the same engine authors | the run that grades the integrated build is not its author's |
| `TX-v-3` | `TX-c-1`, `TX-c-2`, `TX-c-3` | the consumer proof is not the consumer author's |

The constraint binds on context, never on the slot number: a cold start is a fresh context.

### A slotting that satisfies every constraint above (L6's to choose and defend)

| slot | queue, in dependency order | cross-slot waits the COO sequences at the drain |
|---|---|---|
| `~1` Gateway | `TX-g-1` -> `TX-g-2` -> `TX-i-3` -> `TX-r-2` | `TX-i-3` after G-S; `TX-r-2` after G-O |
| `~2` engines | `TX-b-1` -> `TX-b-2` -> `TX-m-1` -> `TX-m-2` -> `TX-m-4` -> `TX-a-1` -> `TX-a-2` -> `TX-k-1` -> `TX-i-1` | spawned when G-R lands; `TX-b-1` after `TX-g-1`; `TX-i-1` after `TX-i-3` |
| `~3` publication | `TX-u-1` -> `TX-u-2` -> `TX-i-2` | `TX-u-1` after `TX-a-2` |
| `~4` consumer | `TX-c-1` -> `TX-c-2` -> `TX-c-3` | `TX-c-1` after `TX-u-1` and notice N-2 |
| `~5` independent validation | `TX-v-1` -> `TX-v-2` -> `TX-v-3` -> `TX-o-1` | `TX-v-2` after `TX-u-1` and `TX-g-1`; `TX-v-3` after `TX-c-3` |
| `~6` baseline, evidence, release | `TX-p-1` -> `TX-m-3` -> `TX-r-1` -> `TX-r-3` | `TX-r-1` after `TX-k-1`, `TX-u-2`, `TX-i-1`, `TX-i-2`, `TX-v-2`; `TX-r-3` after G-W, G-P |

**The fan-out this supports: 6 workers over M = 21 maximal paths, cap 8**, with 3 spawned at issuance (`~1`, `~5`, `~6`, one
head each), `~2` when G-R lands, and `~3` and `~4` when their first inputs drain. Each hand-off is a fresh worktree from HEAD
at hand-off time. Disk: a checkout measured 179 MB against 13 GB free on C: at the cut, so disk does not bind the fan-out.

---

## 6. GATES AND NOTICES -- the promises this project creates

None is an approval gate this seat invented. Each is standing law, the PRD's own runtime input, or a shared-resource sequencing
fact, and its carrier is named.

| id | what must exist | carrier of the rule | owner | cells it holds |
|---|---|---|---|---|
| **G-R** | the `gateway` row in `infra/logic/registry/systems.json`, so both source addresses resolve | CLAUDE.md Rule 30; contract `workbook.source_boundary.registry_registration` (CTO 97152: a build prerequisite, not a review wait) | LGIC_ENFORCE round 2's worker cell EN-r-5, issued by `2.0.0_SA_COO~G`; trigger: EN-r-5's drain to CLOUD, after `4.0.0_SA_CRO` re-signs LGIC_ENFORCE v1.2's brief half (CTO 97179) | `TX-b-1`, `TX-b-2` |
| **G-S** | (a) 2.0.0_SA_COO~O's confirmation that no NFRA_OPLGTW apply is in flight in the `opal-gateway` Terraform root (given ~20:1xZ, msg 97223); (b) the root's two owner-less in-place diffs, a `description` backfill on `aws_wafv2_ip_set.opal_blocked_ips_regional_v4` and `_v6` (`waf.tf:261`, `:302`; rows NFRA_OPLGTW-W1-S1 and S3), dispositioned by their owner, so a plan shows only TAXSMA's resources | one Terraform state, one writer at a time; no worker applies another project's diff | (a) `2.0.0_SA_COO~O`; (b) `1.0.0_SA_CTO`, who holds the rows (their project NFRA_OPSEC202609 is CLOSED) | `TX-i-3` (its apply) |
| **G-O** | NFRA_OPLGTW's first release (`OG-r-1`) deployed and read back | one Gateway host, one release in flight; `OG-r-1` carries the OAuth cutover and must not be interleaved | `2.0.0_SA_COO~O` | `TX-r-2` |
| **G-A** | SATISFIED at the cut: Andrew named `opalbloomberg@opalinvest.com` and authorized the unattended read (record @f95470f384). Workbook access is believed but UNMEASURED (@1729cef85e; MSTR 97190) and is first measured by `TX-r-3`'s controlled read | PRD v0.4 §3.9 / S16 | Andrew; recorded by 0.0.0_AB_MSTR | none |
| **G-W** | the never-widen sign-off (CTO and COO) for turning the new served payload on, naming both keys, the writer count and the rollback | CLAUDE.md HARD STOPS, never move served output without it | `1.0.0_SA_CTO` and `2.0.0_SA_COO~T` | `TX-r-3` |
| **G-P** | the compatible consumer promoted under its applicable authorization | contract `categories.wire_extension.rollout_rule`; the frontend freeze record @65a535f194 | the portal promotion owner on Andrew's word | `TX-r-3` |
| **N-1** | a notice, **not a gate**: before `TX-g-1` spawns, this seat sends 2.0.0_SA_COO~O the shared Gateway surfaces (`GW/app/server.py`, the `opal-gateway` state, the release order) | NFRA_OPLGTW has 22 pending orders; 14 of its order files name `GW/app/server.py`, `EC2_MANIFEST.json`, `safe-ec2-deploy` or the `opal-gateway` Terraform root | `2.0.0_SA_COO~T` | none (it precedes a spawn) |
| **N-2** | a notice, **not a gate**: before `TX-c-1` spawns, this seat sends 2.0.0_SA_COO~D the three consumer files and the branch | PRD CONTRACTS "Consumer and migration boundary": coordinated through 2.0.0_SA_COO~D | `2.0.0_SA_COO~T` | none (it precedes a spawn) |

---

## 7. THE BATTERY -- run at L5, each lens with its blindness stated

| lens | disposition | result | what it does NOT cover |
|---|---|---|---|
| `comp-adversary` | RUN | `compose` on v0.5 (read-vintage @7f1ab996a0, 20:05:33Z): 19 of 19 cited commits VERIFIED; 38 cited paths, 30 stable, 8 GONE, all 8 the PRD's own PROPOSED_NEW paths; 2,580 uncited siblings, 25 shown (cap declared). Earlier runs: v0.3 14/14 and 33/25/8; v0.2 13/13 and 29/22/7 | `T11: decomposition neighborhood NOT RESOLVED` (the PRD has no `<decomp_ref>`), so the siblings are filesystem adjacency, not this decomposition's chain; a re-run against each task order at L7 resolves T11 |
| `comp-schedule` | RUN, APPLICABLE | self-test PASS 6/6. View at `--budget 1800`: within budget (507 s), **5 of 5 carriers**, C1 345, C2 6, C3 12, C4 21, C5 334; **25 gates armed, none naming MDPF_TAXSMA, the Gateway capability or a surface here.** Moratoria that bind cells: never-widen (G-15: `TX-r-3`), no half-landed deploy (G-16: `TX-i-*`, `TX-r-*`), no shadow or duplicate output (G-19: `TX-u-1`), no new monitor (G-20: `TX-a-2`, `TX-o-1`), safe-apply and safe-commit (G-22: every writing cell), cross-firm fence (G-23: `TX-i-1`, `TX-i-2`), vendor egress (G-24: no worker calls Graph; `TX-r-3` after G-A), the trading calendar (G-18: `TX-a-2`). The first run at `--budget 540` scanned 0 of 5 carriers (C1 partial over 38 worktrees) and is superseded | C4 and C5 are NOT-DECIDABLE prose carriers: 136 non-null `blocking` fields are a reading list, not gates. The gates this project creates are s.6 |
| `comp-iam` | RUN | DESIRED plane, 472 `.tf` files. `mdpf-gold-lambda-role`: 11 statements (legacy Gold and 0824 silver reads among them); **no statement on `opal-data-49financial`**. Publisher (`opal-assets-mdpf-egress-publisher-role`): 7 operations, 6 UNRESOLVABLE-RESOURCE, 1 GRANTED-ACTION/UNGRANTED-RESOURCE (GetObject on the portal-v2 latest pointer). `opal-gateway-role`: 21 operations floor, 16 UNGRANTED (NFRA_OPLGTW test call sites), 3 UNRESOLVABLE, 2 GRANTED-ACTION/UNGRANTED-RESOURCE | Terraform only, and blind to deny: 26 policy blocks NOT ATTACHED and 2 deny statements unparsed, among them the cross-firm Deny belts. The APPLIED and EXERCISED planes are `TX-p-1`'s reads and the live arms of `TX-i-1`, `TX-i-2`, `TX-i-3` |
| `comp-blast` | DECLARED (L4's run, cited) | PRD §5.2: `_shape_category_views` absent from the extracted graph -- a boundary, not zero impact | extracted edges only; `TX-a-1` and `TX-a-2` re-run it on each changed function at Phase 1 |
| `comp-routes` | DECLARED (L4's run, cited) | PRD §5.2: both `.json` routes trace to the portal-v2 origin through auth-validator-edge and the rewrite to `platinum/mdpf/<scope>/category-views.json` | DESIRED only; the applied edge and authorization are `TX-r-3`'s authorized readback |
| `comp-cache` | DECLARED (L4's run, cited) | PRD §5.2: 634/634 files, 119/119 useQuery calls, 17 shared keys, 0 type mismatches | other hook families and TTL behavior are not covered; `TX-c-1` re-runs it and proves the TTL by test |

**Beyond the core, measured at this cut:** the `address()` census of all 9 declared artifacts (s.1 falsifier 3); `head-bucket`
on the firm bucket; the manifest drift census (s.1 falsifier 4); the MDPF Gold suite at bd2fa195c0 (92 collected, 89 passed,
3 failed: `test_global_fold_flag2.py::test_carry_within_window_carries_and_labels`, `::test_carry_beyond_window_absent_for_real`,
`::test_carry_source_is_measured_never_interpolated`); the Gateway suite (90 collected, 2 collection errors, both
`ModuleNotFoundError: No module named 'moto'`); the portal test instruments (`bun` 1.3.9 and the `playwright` library present;
`vitest`, `jsdom`, `happy-dom`, `@testing-library/react` and `@playwright/test` absent).

---

## 8. BOUNDS THAT BIND EVERY ORDER, inlined at L6

1. **No egress off Opal infrastructure.** No worker calls Microsoft Graph, SharePoint, the live workbook or the live
   `/ms/taxsma-workbook` route with a real identity. Synthetic Gateway responses only, until G-A (PRD §3.9).
2. **No private data in the repository.** No client name, full account number, balance, token, cookie or delegated credential
   enters code, fixtures, deliverables or logs; masked labels and aggregate counts only.
3. **Addresses and names from the builders.** Every new S3 key is `address()` output and every new resource name is `name()`
   output (Rule 30); a secret's path is one `grade(<path>, "SECRET")` returns CONFORMANT for. A builder refusal is a row,
   never a typed path.
4. **Deploy discipline.** A world-changing act opens its change-management entry and commits the OPEN sentinel before the act,
   then closes and commits the entry before the reads that grade it. Terraform through `safe-apply` only, never `-target`; the
   Gateway through `infra/aws/ec2/safe-ec2-deploy.sh` only; no `aws lambda update-function-code`.
5. **One Terraform state, one writer.** Each root is applied by one cell at a time; the `opal-gateway` root never concurrently
   with NFRA_OPLGTW (G-S).
6. **No served output moves without G-W.** `TX-r-1` proves DELTA=0 on both served keys; the rollout switch stays OFF until G-W
   and G-P.
7. **No new monitor, alarm, SNS, email, watcher, schedule or standing comparator.** The 13:30 and 13:50 UTC clocks are reused.
8. **No source mutation.** No workbook, BD roster or custodian write; no change to b00; no rewrite of another source's Bronze
   or Silver; no bucket-policy broadening and no firm-fence exemption.
9. **Exactly two served writers' keys.** S08 writes only the two historical keys (X7, X2); no firm-bucket Platinum twin and no
   migration (MDPF_CANON owns it).
10. **The spec is frozen, and the face instructs refusal.** A criterion that cannot be satisfied as written is REFUSED and
    reported with its measurement, never repaired, widened or met by another route. Anything off-spec is a row.
11. **Every invocation terminates** (`timeout 120`, or the tool's own budget).
12. **Commits go through `.tools/safe-commit.sh` under the worker's serial; every `.py` edit passes `.tools/commit-gate.sh`.**
13. **No portal DEV or PROD push and no workspace gitlink move.** Portal work is committed on a worker branch.
14. **Unknown deployment facts are measured, never presumed.** A cell asserts no deployed state it did not read back.
15. **No new dependency.** `moto`, `vitest`, `jsdom`, `happy-dom` and `@testing-library/react` are absent on this box; tests use
    the standard library, installed packages, stubs and the installed `playwright` library. A missing instrument is a refusal.
16. **D9 is out of scope.** No account opening, margin, money-manager or strategy change, trade, Yang converter change or access
    grant.
17. **The MDPF Gold suite baseline is 89 passed and 3 failed** (s.7). A cell adds no failure; the 3 pre-existing failures are
    not its to fix (a row if its change touches them).

---

## 9. RULE 24 FOUR-POSTULATE RECORD

**(i) MECE over a declared domain.** The domain is s.1's subtraction: 19 manifest rows, every one served, with four falsifiers
run before use (the 49-component manifest, every cited path, the live substrate through the builders, the drift of every pin).
Exhaustive: 19 of 19 surfaces, 8 of 8 outcomes, 8 of 8 acceptance properties, 8 of 8 boundary questions (s.2, s.3). Mutually
exclusive on write surfaces: no file is written by two cells, and every shared Gateway file is written by a single TAXSMA cell
(`TX-g-1`), its cross-project sharing handled by N-1 and G-O.

**(ii) SAME GRAIN.** Every cell is one act by one worker producing one record: one module with its tests, one package, one
apply in one root, one measurement, one grading, or one release. Sovereign words and person-operated acts are a different grain
(a person's act) and are gates, not cells.

**(iii) INTENT COHERENCE.** One axis: **deliver v0.3 so every FWD bar has its deliberate proof.** No cell widens scope: no D9
workflow, no new provider egress, no taxonomy change, no competing valuation, no shadow publisher, no new monitor, no portal
promotion, no migration of a served key.

**(iv) STATE COHERENCE, and what each remedy does NOT move:**
- `TX-g-1` adds a route and moves **no existing route, credential or grant**; the capability stays unusable without G-A.
- `TX-b-1` and `TX-b-2` write source evidence and move **no membership**.
- `TX-m-1` records effective history and moves **no workbook, roster or trading record**.
- `TX-m-4` writes observations and moves **no b00 value or basis**.
- `TX-a-1` and `TX-a-2` add Tax once and move **no Client or other-firm figure**.
- `TX-u-1` changes publication and moves **no served key** (switch OFF) and **no served home**.
- `TX-i-1`, `TX-i-2`, `TX-i-3` add exact grants and move **no existing grant or firm fence**.
- `TX-r-1` and `TX-r-2` release disabled code and move **no served content** (DELTA=0) and **no identity**.
- `TX-v-1` .. `TX-v-3` and `TX-o-1` move **no production code**; a failing arm is a row for the round-N analysis.

---

## 10. CHOICES THIS DECOMPOSITION MAKES THAT THE PRD DID NOT

Each is this seat's call at L5, stated so it can be argued with, and revertible at the round-N analysis.

1. **S13 is three cells, one per Terraform root** (`TX-i-1` mdpf-pipeline, `TX-i-2` opal-assets, `TX-i-3` opal-gateway), because
   each is one apply in one state, and the PRD asks for one actor and act per cell.
2. **S14 is three cells** (`TX-v-1` expected cases, `TX-v-2` producer journey, `TX-v-3` consumer journey), each by a worker who
   authored none of what it grades.
3. **The Gateway unit tests (`GW/tests/test_taxsma_workbook.py`, listed by the manifest as an S14 companion) are written by the
   S01 author in `TX-g-1`;** the independent A07 proof is `TX-v-2`'s route controls. A recorded deviation from the manifest's
   plane assignment, made so that no file has two writers.
4. **The publisher gains a rollout switch defaulting to the legacy payload**, so the contract's `rollout_rule` holds mechanically
   and `TX-r-1` can prove DELTA=0 with the new code deployed.
5. **Release is split in three:** `TX-r-1` backend with Tax disabled (DELTA=0, no sign-off needed), `TX-r-2` Gateway with the
   capability disabled after NFRA_OPLGTW's release, `TX-r-3` activation held on G-A, G-W and G-P.
6. **The four current exception cases are their own read-only cell (`TX-m-3`)** with a judgment criterion, not a rider on
   `TX-m-2`'s code.
7. **Each new engine carries its own unit test file in `TST/`** (the new `data/mdpf/tests/taxsma/` directory the manifest names
   for S14); the journey harness is separate and independent.
8. **`TX-r-1` reads the served keys after the scheduled 13:50 UTC publisher fire**, not after an ad-hoc publisher run, because
   a publisher run writes the served keys and DELTA=0 can only be read after the write; the Gold ad-hoc QA invocation is allowed.
9. **Consumer proof fixtures are the harness's own publisher output** (`TX-v-2 -> TX-v-3`), so the producer and consumer are
   exercised as a pair, as PRD §3.7 requires.

---

## 11. FINDINGS AND CARRIES, for the CTO's L10 read

1. **Cross-project coupling with NFRA_OPLGTW (2.0.0_SA_COO~O).** Three TAXSMA surfaces share state with its 22 pending orders:
   `GW/app/server.py` (the file already moved since the L4 pin, @51b0f7d823 by `OG-a-1`), the Gateway release (`OG-r-1`) and the
   `opal-gateway` Terraform state (`OG-i-1` .. `OG-i-4`); 14 of its order files name one of these Gateway files, the deploy path or
   the Terraform root. Handled by N-1, G-S
   and G-O, not by merging scopes.
2. **The MDPF Gold suite carries 3 pre-existing failures at bd2fa195c0**, all in `test_global_fold_flag2.py` (the Global fold
   carry path that `TX-a-1` and `TX-a-2` touch). Not this project's. Recorded as the baseline (bound 17) and filed as a row at
   the channel's opening.
3. **`moto` is absent from this box's Python**, so two Gateway test modules (`test_access_state.py`, `test_oauth_durable.py`,
   NFRA_OPLGTW's) fail collection. TAXSMA's tests do not use it (bound 15).
4. **No portal unit-test runner or DOM library is installed.** `TX-c-1` and `TX-v-3` use `bun test` for logic and the installed
   `playwright` library for renders; a missing instrument is a refusal, not a new dependency.
5. **The consumer files moved since their manifest pins** (portal promote 12:12Z); no open branch touches them. Cells read HEAD.
6. **SUPERSEDED: v1's unnamed membership attester.** Andrew ~18:3xZ (@1729cef85e) made Traded the key; v0.4 has no manual
   attestation. Carried instead: **workbook access for `opalbloomberg@opalinvest.com` is believed but UNMEASURED** -- the only
   probe (MSTR 97190) was refused by the Gateway's per-identity tool guard before Graph. `TX-r-3`'s controlled read is the first
   measurement, and a refusal there is a reported result, never a grant.
7. **CRO 97162's index gap is carried:** PRD brief-coverage rows I.O3, I.O5 and I.O8 omit S19; this decomposition's own coverage
   table includes S19 under FWD-3, 5 and 8. The PRD fix waits for its next substantive bump.
8. **The publisher role's pre-existing GRANTED-ACTION/UNGRANTED-RESOURCE finding** (GetObject on the portal-v2 latest pointer) is
   recorded by `TX-i-2`, not repaired.
9. **Andrew's Gold-placement question remains a question** (record @1a133f12c2; 1.0.0_SA_CTO~A ACK97091; CVO N6). CTO 96960
   governs. If he rules a change, it arrives as a PRD addendum and this decomposition is recut from the round-N analysis.
10. **The `opal-gateway` Terraform root carries two owner-less in-place diffs** (2.0.0_SA_COO~O, 97223): a `description` backfill on
    the two regional WAF IP sets, which NFRA_OPLGTW's `OG-i-1` also met and was refused on. `TX-i-3`'s "zero changes to every other
    resource" criterion stays strict; the disposition is G-S (b), owned by `1.0.0_SA_CTO`. No TAXSMA worker applies that diff.
11. **Estimate, as a reading.** The machine critical path is 14 cells. At an inferred 1 to 3 worker-hours per cell, roughly 2 to 4
    days of serial work, plus G-R (EN-r-5's drain, after the LGIC_ENFORCE v1.2 re-sign) and G-W, G-P, whose timing is Andrew's. Basis INFERRED, not measured;
    no delivery date is committed.

---

## 12. WHAT THIS DECOMPOSITION DOES NOT CLAIM

1. **No cell has been exercised.** Every target state is a specification.
2. **The `gateway` registry row had not landed at the cut** (`address("gateway", ...)` raised ValueError at 7f1ab996a0).
3. **The home of b00's `canonical_valuation` output was not re-read at the cut.** `TX-p-1` reads it.
4. **No live IAM, schedule or served-document state was read at the cut.** `TX-p-1` reads them.
5. **Whether the estate's rule-13 guard admits a worker serial on `data/mdpf/scripts/gold/` commits is NOT-EVALUATED.** A refusal
   becomes a blocking row and the issuer seats the owning lane for that order alone.
6. **The boundary questions are the PRD's summary of the certified rectangle,** DECLARED, not re-read from the rectangle.
7. **Whether the `mdpf-pipeline` and `opal-assets` Terraform roots carry pre-existing plan drift is NOT-EVALUATED.** `TX-i-1`, `TX-i-2`,
   `TX-k-1`, `TX-u-2` and `TX-r-1` meet it through their "changes nothing else" criteria and refuse; none applies another project's diff.
8. **The chain count and the constraint table are readings.** M = 21 follows from the 39 edges this document declares; a missing
   edge would show as false width.
