# AMGT_RESAPP round 12 -- Social source classification (AMGT-rk-10)

**NOT a build cell.** This report classifies four already-filed round-11 rows -- `W22-S3`, `W22-S6`,
`W22-S7`, `W22-S8` (`AMGT_RESAPP-Z-W22-S3/S6/S7/S8`, filed by `0.9.0_WK_AMGT_RESAPP~22` at
`org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md`) -- and reports.
Nothing here is run, built, redeployed or scheduled. Source: `ROUND_ANALYSIS.round11.md` s.5 G,
`REMEDIATION_v11.md` item 6, and the cited rows themselves.

Andrew's reservation stands throughout: recurring collection is RESERVED to him by name
(`9db2a36cdc`) and nothing in this report enables it. The three Windows collection tasks stay DISABLED,
unchanged by this cell.

## Why the two classes matter

**SOURCE ABSENCE** (the source genuinely lacks it) and **FAILED PRIMITIVE** (our pull or our
admission rule missed it) are DIFFERENT and stay separate below. A summary that reads "no items
admitted" without saying WHY is exactly the collapse this cell must not make: it lets an unbuilt
primitive read as an empty source.

## Row-by-row classification

### `W22-S3` -- the X/Twitter second-candidate profile discovery for Boeing

**Classification: FAILED PRIMITIVE.**

The identity account pass (`IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json`) holds Boeing's `social_account`
as `UNRESOLVED`, value `null`, evidence `"REFUSED -- the page at https://www.boeing.com/ returned 25329
bytes and carried NO social links ... THIS IS A LIMIT OF THE INSTRUMENT, not evidence the company has no
accounts."` The pass's own author states the negative result is an instrument limit, not a finding about
Boeing. The instrument is a static-HTML fetch of the corporate homepage; a large public company's social
links commonly sit in a client-rendered (JS) footer a static fetch never sees. `profile_urls_available`
reads 0 downstream in `lib/research/social/collect.py`'s `read_second_candidate_profiles()`, and the
second-candidate method is therefore "not runnable for BA_US_Equity from that artifact" -- not because
Boeing lacks an X presence, but because our one identity primitive (a static page fetch) cannot see where
that presence would be declared. Nothing here establishes SOURCE ABSENCE; the evidence explicitly refuses
that reading.

### `W22-S6` -- the S-1 storage key carries no security coordinate

**Classification: FAILED PRIMITIVE.**

INTERFACE S-1's key `social/v1/_measurement/{as_of}.json` has no security coordinate in it, while the
served record itself carries `security_key`. One security per day fits the key; a second security
measured on the same `as_of` would overwrite the first at the same key (sibling families in the same
bucket, e.g. `management/v1/{security_key}/{as_of}.json`, key by security first -- this family does not).
This is a design property of a primitive WE wrote (the storage-key shape), not a property of the vendor or
the content it returns; it is unrelated to source availability. Built as specified and harmless under this
cell's one-security bound (five overwrites of the same key, same security, all read back correctly this
round) -- a latent gap, not yet exercised as a live collision, and not touched here (a key-shape change is
a new S-1 version, outside this cell's bound).

### `W22-S7` -- cost cannot be measured with the estate's key

**Classification: FAILED PRIMITIVE.**

Three routes were probed. The dataset-progress payload (`GET /datasets/v3/progress/<id>`, both mid-run and
at completion) and the snapshots listing (`GET /datasets/v3/snapshots?dataset_id=...`) carry NO cost field
at all -- at completion the progress payload's only keys are `avg_duration_per_input`,
`collection_duration`, `dataset_id`, `errors`, `records`, `snapshot_id`, `status` (seven keys, no `cost`).
That is a genuine characteristic of those two response shapes for any caller and is the SOURCE-ABSENCE
component of this row. The one route Bright Data does expose for account cost, `GET /customer/balance`,
returned `403 "Your API key lacks the required permissions for this action. You can change your token
permissions at https://brightdata.com/cp/setting/users"` -- and the SAME key returns 200 on
`/datasets/list` (1765 datasets), so the 403 is a permission scope on THIS credential, not a vendor outage
and not a vendor-side absence of the capability. Net classification for the row: FAILED PRIMITIVE -- our
own credential is under-scoped for the one route that could answer the question, so `cost.usd` stays
ABSENT with the 403 recorded as its reason (see Cost section below), and the pre-call estimate is carried
as `held`, never promoted to `measured`.

### `W22-S8` -- the measurement: 48 records, 0 admitted

This row is MIXED and is decomposed rather than given one label, because it is the row where collapsing
the two classes would misrepresent the finding:

- **DELIVERY (the pull itself): neither absence nor primitive failure.** One Reddit-keyword job
  (`sd_mu2wf4v3biieffcle`) ran to completion (`status=ready`) in 713.4 s (vendor `collection_duration`
  709.9 s), delivered 48 of a 50-item cap, 48 of 48 valid, 0 vendor errors. The declared method WORKS on
  this account; this is the positive control that the job-submission-and-retrieval primitive functions.
- **ADMISSION -- 0 of 48 admitted: FAILED PRIMITIVE.** Every one of the 48 items has its author identity
  `UNRESOLVED`, so `validator.attach_to_security` refuses all 48 by construction (the existing item rule
  cannot pass a single Reddit record because the identity-resolution primitive was never built or extended
  to resolve Reddit authors to a security). This is our own admission rule missing the input it needs, not
  a statement about the content the vendor returned.
- **PER-POST SUBJECT: SOURCE ABSENCE.** The vendor's Reddit record carries 30 keys and none of them is a
  per-post subject or company-tag field, so `primary_subject` is `None` on every item by construction of
  the vendor's own schema -- no primitive we could build recovers a field the source never sends. This is
  the one genuinely source-side gap among the four rows.
- **CAP TRACKING ("ambiguous per-input cap"): FAILED PRIMITIVE.** `delivery.capped` reads `False` because
  the job TOTAL (48) sits under the 50 cap, while the `'BA'` keyword input alone hit its own per-input
  limit of 25 and WAS truncated. The flag is job-total by construction, so it silently understates
  per-input truncation on any single high-volume keyword -- our own flag design, not a source
  characteristic.
- **Noted, not classified either way:** the ticker-ambiguity control worked as designed (22 of 25 `'BA'`
  items correctly REFUSED as unrelated -- British Airways, Bachelor of Arts, business-analyst posts -- this
  is the rule succeeding, not a defect); and 2 of 48 items fell outside the local 30-day window because the
  vendor's undocumented "Past month" window differs from the local cut (adjacent row `W22-S5`, not one of
  this cell's four named rows) -- a vendor-window-definition characteristic, informational only here.

## Summary table

| Row | Finding | Classification |
|---|---|---|
| `W22-S3` | X/Twitter profile discovery for Boeing has no input; the account pass's own evidence names this an instrument limit, not company evidence | FAILED PRIMITIVE |
| `W22-S6` | S-1 key carries no security coordinate (unexercised collision risk under this round's one-security bound) | FAILED PRIMITIVE |
| `W22-S7` | Cost unmeasurable with this key; the one route that could answer it (`/customer/balance`) refuses on permission scope, not outage | FAILED PRIMITIVE |
| `W22-S8` | 0 of 48 admitted: driven by our own unbuilt author-identity attachment and a job-total (not per-input) cap flag (FAILED PRIMITIVE), compounded by the vendor's schema carrying no per-post subject field at all (SOURCE ABSENCE) | MIXED -- FAILED PRIMITIVE (admission, cap) + SOURCE ABSENCE (per-post subject) |

**Reading the table:** of the four rows, three (`W22-S3`, `W22-S6`, `W22-S7`) are FAILED PRIMITIVE outright
-- none of them establishes that the underlying source lacks the capability; each traces to an instrument,
a key schema, or a credential scope that is ours. `W22-S8`, the row that actually produced records, is
MIXED: its zero-admission result is driven primarily by FAILED PRIMITIVE (identity resolution not built for
Reddit authors; a job-total cap flag), with exactly one genuine SOURCE ABSENCE component (no per-post
subject field exists anywhere in the vendor's 30-key schema). Stating "48 records, 0 admitted" alone, with
no classification, would read as an empty feed; it is instead mostly an unbuilt admission primitive sitting
in front of a feed that does deliver content, plus one real gap in what that content contains.

## Cost (ADDENDUM 3 s.3, ruled -- this field is not reopened here)

`cost.usd` stays ABSENT with its reason recorded. It cannot be measured with `brightdata-api-key` on any
route probed: the progress payload (running and at completion) and the snapshots listing carry no cost
field at all, and the account-balance route -- the one route that could carry it -- refuses this key with
`403 "Your API key lacks the required permissions for this action. You can change your token permissions
at https://brightdata.com/cp/setting/users"` (the same key succeeds on `/datasets/list`, so this is a
permission scope on the key, not an outage). The pre-call unit-price ESTIMATE (usd 0.0750 for 50 records at
usd 0.0015/record, checked against a usd 5.00 guard cap) is carried with claim `held` and is NEVER promoted
to `measured` -- it is a guard input for the pre-call spend check, not a measurement of what the job cost.
No route probed today can turn `held` into `measured`. A billing-permitted key is a CREDENTIAL act: it is
not taken here and is deliberately not carded -- asking for a credential to measure the cost of a feed not
yet decided on inverts the order this cell was given.

## Recurring collection (out of scope, unchanged)

This report touches no harvest schedule, no Windows Task, and writes no Terraform. Recurring social
collection stays RESERVED to Andrew by name (`9db2a36cdc`); nothing in this document enables it. A nonzero
count against that bar would be a breach of a standing reservation, not a build decision -- none is made
here.

## Sources cited

- `org/tier1_exec/4.0.0_SA_CRO/deliverables/IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json` @`eff1b9f6ae`
- `lib/research/social/collect.py` @`5ac6e20930` (`read_second_candidate_profiles`, `write_pool_object`,
  `VENDOR_ZERO_DATA_MESSAGES`)
- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` rows
  `AMGT_RESAPP-Z-W22-S3`, `AMGT_RESAPP-Z-W22-S6`, `AMGT_RESAPP-Z-W22-S7`, `AMGT_RESAPP-Z-W22-S8` (also
  `W22-S5` for the vendor-window note)
- `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round11.md` s.5 G
- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/remediations/REMEDIATION_v11.md` item 6
- `s3://opal-data-harvest/social/v1/_measurement/2026-09-15.json` (document-sha256
  `ad459b40bbbb7c71e3a66f78cf7e48a2fa0f73e66d5127b2c74d29908f23d424`)
