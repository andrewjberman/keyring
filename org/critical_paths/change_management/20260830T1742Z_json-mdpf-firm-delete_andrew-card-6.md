# NEVER#2 ledger -- DELETE of `json/mdpf/{firm}`, 8 objects across TWO buckets (Andrew card (6))

**Status:** OPEN 2026-08-30T17:42:10Z by `0.4.0_DS_ClientPlatform~V`.
**Opened BEFORE the act**, per `2.0.0_SA_COO` 88759 shape step 1.

## Authority, and which authority is which

- **THE HUMAN CONFIRMATION IS ANDREW'S**, verbatim (`org/tier1_exec/1.0.0_SA_CTO/deliverables/
  ANDREW_DIRECT_20260830_171xZ_SEVEN_CARD_RULINGS.md`, relayed at 1.0.0_SA_CTO 88638):
  *"Rec approved, just confirm there are no consumers of these materials first, which is likely
  confirmed already but good to double check."*
- **THE EXECUTOR CUT IS THE ISSUER'S** (`2.0.0_SA_COO` 88759): this seat. The cut names who carries
  out an act Andrew already approved; it does not supply the confirmation and could not.
- **THE SCOPE IS ANDREW'S**, read off the card he ruled on rather than interpreted
  (`0.0.0_AB_MSTR` 88671): the card's own subject line reads *"delete the dormant json/mdpf/{firm}
  prefix -- 8 objects across TWO buckets"*, carrying `1.0.0_SA_CTO` 87625's requirement verbatim
  (*"BOTH buckets named as the subject -- a yes covers 8 objects in two buckets or it is not the
  act"*). **A delete scoped to `opal-data-assets` alone would be NARROWER than what he approved,
  and narrowing his word is as much a defect as widening it.**

## Scope

**IN:** 8 objects, by EXACT KEY, never a prefix and never a wildcard.

| bucket | key |
|---|---|
| `opal-data-assets` | `json/mdpf/49financial/account-distribution.json` |
| `opal-data-assets` | `json/mdpf/49financial/aggregate-aua-timeseries.json` |
| `opal-data-assets` | `json/mdpf/cottonwood/account-distribution.json` |
| `opal-data-assets` | `json/mdpf/cottonwood/aggregate-aua-timeseries.json` |
| `opal-data-assets` | `json/mdpf/global/aggregate-aua-timeseries.json` |
| `opal-data-assets` | `json/mdpf/inflection/account-distribution.json` |
| `opal-data-assets` | `json/mdpf/inflection/aggregate-aua-timeseries.json` |
| `opal-data-portal-v2` | `json/mdpf/49financial/aggregate-aua-timeseries.json` |

**OUT, and not stretched:** the IAM grants in `infra/aws/terraform/mdpf-pipeline/iam.tf` and
`mdpf_portal_publisher.tf`'s `json/mdpf/*` write-prefix declaration. Carried on the card as a
**separate follow-on act**; they are not in this word and need their own.

## The gate condition, and why it is re-run rather than cited

Andrew's gate is *"confirm there are no consumers **first**"*. `1.0.0_SA_CTO` 88638 and
`2.0.0_SA_COO` 88759 both rule that the earlier censuses (87742, 87885, 88661) are **NOT spent** as
that confirmation -- they were taken before the word, and the world moved (the CVO retired three
harnesses in between). **The four-plane census therefore runs IN THE SAME STRETCH as the delete.**
88661's PASS is the *method*, controls-firing and proven; it is not the *confirmation*.

Measured support for that, produced unasked by another seat: `0.7.0_AE_CloudOps~L` re-measured its
own host corpus at its act and found it had grown **81 -> 83 objects in four hours**. A stale
census is not a census.

**A non-zero reader on ANY plane STOPS the act and returns to Andrew.** It is not weighed against
a passing census from earlier.

## Recoverability

Both buckets carry versioning **Status=Enabled**; `MFADelete` is **ABSENT from the API response**,
which is how the API renders *not enabled* -- stated as an absence read, not a value seen. A delete
here writes a **DELETE MARKER** over a retained noncurrent version: **RECOVERABLE**.

⛔ **The retained VersionIds are printed WHOLE at close -- all 32 characters, no display slice.**
That handle is what the recoverability claim rests on, and this fabric watched a `[:22]` slice turn
a restore handle into a value that recovered nothing while reading as complete
(`0.7.0_AE_CloudOps~L` 88720, origin `e4_census.py:40`).

## Close criteria

1. four-plane census in this stretch: ZERO consumers, each plane with corpus, denominator and a
   FIRING positive control;
2. 8 deletes by exact key, per bucket;
3. post-delete read of BOTH prefixes + `list-object-versions` showing the delete markers AND the
   retained noncurrent versions, VersionIds whole;
4. this entry closed on that read.

---

## CLOSE

**Status: CLOSED 2026-08-30T17:50Z by `0.4.0_DS_ClientPlatform~V`. Act complete, all four close
criteria met.**

### 1. The gate, re-run IN THIS STRETCH (17:43:15Z - 17:45:30Z), not cited from earlier

| plane | corpus / denominator | consumers | positive control |
|---|---|---|---|
| S3 | 3 buckets named by the repo census; 8 current objects | n/a (the subject) | -- |
| DEPLOYED | 200 live functions counted client-side, 4 match mdpf, **all 4 BOUND** by base64(sha256(zip)) == live CodeSha256 | **0 code reads** (4 text hits, every one OPENED: 3 docstrings in mdpf-gold-lambda, 1 in the publisher reading *"json/mdpf/* is never touched"*) | `portal/gold/mdpf` found in **5 members** |
| REPO @`1b730c8df6` | comp-find corpus=all: **4,410 hits / 137,286 files** (71,594 EPHEMERAL-FLOOR, 16 UNREADABLE, 4,159 BINARY not searched); 1,251 files listed, 30 code-extension, 85 text hits | **0 real call sites** (1 flagged -> OPENED -> a string literal in `comp_legacywriter.py:1206`, inside `sample = ("def load():\n"...)` fed to `ast.parse(sample)` in that module's own self-test; re-verified at THIS head) | the flag itself fired, so the matcher can say yes |
| PORTAL | 2 code files carrying the token | **0** (both comments; `aum.ts:552` records a prior json/mdpf claim FALSIFIED) | -- |

Versioning at the moment of the act: `opal-data-assets` **Enabled**, `opal-data-portal-v2`
**Enabled**, `opal-data-bd` **Enabled**; `MFADelete` **ABSENT from every response** (= not enabled,
stated as an absence read).

### 2. The act

8 deletes by EXACT KEY, never a prefix and never a wildcard. Issued 17:48:34Z - 17:48:54Z,
**rc=0 on all 8**.

### 3. Post-delete read

- `opal-data-assets` `json/mdpf/` -> **0 current objects**, IsTruncated=None
- `opal-data-portal-v2` `json/mdpf/` -> **0 current objects**, IsTruncated=None
- **LISTING CONTROL:** the sibling `portal/gold/mdpf/` still returns objects on the same
  instrument, so the two zeros are measurements and not a broken listing.

### 4. Recoverability -- the 8 delete markers THIS ACT created, VersionIds WHOLE

| bucket | key (under `json/mdpf/`) | delete-marker VersionId | created |
|---|---|---|---|
| opal-data-assets | 49financial/account-distribution.json | `yaMXYKd7hkzFeVHFwGNg38V.L1dVeKcI` | 17:48:39Z |
| opal-data-assets | 49financial/aggregate-aua-timeseries.json | `0bIQs32CiwSxMLjbct65JpPWLiCEpkTC` | 17:48:41Z |
| opal-data-assets | cottonwood/account-distribution.json | `GNu5hffmT6WeygxvX6dbJxt8dLnxo_Hf` | 17:48:43Z |
| opal-data-assets | cottonwood/aggregate-aua-timeseries.json | `.si7ImF6xEvI5thy1mGk3upBxy.jw2.D` | 17:48:45Z |
| opal-data-assets | global/aggregate-aua-timeseries.json | `TvcQr8xJblhNmfO.Zk.65vugtIDsYpzt` | 17:48:48Z |
| opal-data-assets | inflection/account-distribution.json | `zIVQxzqhvSOJ_2m4rV4.AiFlJAQLmK1q` | 17:48:50Z |
| opal-data-assets | inflection/aggregate-aua-timeseries.json | `iqEkbHONpojKSt3WsBSW690LLqEjhd.W` | 17:48:52Z |
| opal-data-portal-v2 | 49financial/aggregate-aua-timeseries.json | `YmqJpduEA2VUGqLyS6VMnEDlDHRARwU4` | 17:48:54Z |

Every VersionId is **32 characters, printed whole**, no display slice.
**33 noncurrent versions are retained** under the two prefixes (23 in assets, 10 in portal-v2),
including a prior version of every one of the 8 keys.
**RESTORE PATH:** delete the delete-marker by its VersionId
(`aws s3api delete-object --bucket <B> --key <K> --version-id <marker>`), which reinstates the
prior version. The handles are in the table above.

### 5. ⛔ 18 MARKERS EXIST UNDER THESE PREFIXES AND ONLY 8 ARE THIS ACT'S

Reporting 18 would overstate the act by 10. Attribution is measured, not counted: the other 10
were created **2026-07-21** (`_oac_b1_test.json`) and **2026-08-19** (nine keys in portal-v2 --
cottonwood, global, inflection, aum-metrics and a root-level aggregate-aua-timeseries.json,
already deleted before today). That is why the card counted **1** current object in portal-v2 and
not ten.

**AND THE FIRST ATTRIBUTION INSTRUMENT FAILED, disclosed rather than quietly replaced:** I tried to
attribute the markers from the delete API's own responses, but I had flattened multi-line JSON into
a single-line pipe-delimited capture, so `json.loads` returned nothing and every VersionId read
`None`. The script then printed **"created by THIS act: 0"** -- a value produced by a broken
parser, which would have read as a finding that my own deletes had not registered. Re-attributed on
a DIFFERENT axis: each marker's own `LastModified` against the act window, with a negative control
(the test EXCLUDED 10 markers, so it can say no). 8 mine, 10 pre-existing, keys matching the act's
list exactly.

### Authority chain, unchanged

Andrew's word (the gate met in-stretch) -> the issuer's executor cut (`2.0.0_SA_COO` 88759) -> this
act. **NOT covered and not touched:** the IAM grants and the publisher's `json/mdpf/*` write-prefix
declaration, carried on the card as a separate follow-on act.
