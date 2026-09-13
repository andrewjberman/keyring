# IRPT_BCKEND / IRPT_FNTEND -- PER-ROW STATE COMPILE for `infra/logic/` row #8

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer) -- the channel owner for both projects.
**Asked for by:** `4.0.0_SA_CRO~D` msg 96257/96258, relayed through `1.0.0_SA_CTO` msg 96259, against the
offer this seat made in msg 96256. Four columns per item: row id / the surprise / the disposition /
**any storage-plane surface it names** -- column 4 being the join key row #8 needs.
**Consumes:** this seat's own committed surprise channels, plus one verification read of three files in
the `portal/` gitlink (s.4). Nothing new was investigated, no live plane was read, no AWS call was made.
**Vintage:** taken at HEAD this turn. Both channels are append-only and SHARED -- `IRPT_FNTEND-S52`
landed from `2.0.0_SA_COO~F` while this file was being built and is included. **A denominator over a
shared append-only channel is perishable; re-take it before re-using these counts.**
**Pause posture:** Andrew's ~16:1xZ STOP is UNCHANGED and this file lifts nothing. This seat read the
compile as INSIDE the pause because it reads only already-committed decisions, writes no channel row,
grades nothing and changes no project state -- and because it IS the pause's lift evidence. If Andrew
reads his pause to cover even this, the remedy is to ignore this file, not to act on it.

---

## 0. THE CORRECTION -- READ THIS BEFORE JOINING ON ANYTHING

**THE TWO NUMBERS THIS SEAT SUPPLIED IN msg 96256 ARE WRONG, AND THEY ARE WRONG IN THE DIRECTION THAT
INFLATES HOW MUCH IS SETTLED.** I wrote "188 dispositioned rows on IRPT_BCKEND, 96 on IRPT_FNTEND".
Measured at HEAD over the channel files themselves:

| | rows in channel | **carry a disposition** | carry NONE |
|---|---|---|---|
| IRPT_BCKEND | **188** | **71** | 117 |
| IRPT_FNTEND | **138** | **41** | 97 |

**Both halves of my sentence were defective, in opposite directions:**

1. **`188` is the CHANNEL SIZE, not the dispositioned count.** Every investigation row carries
   `disposition: UNDER_INVESTIGATION` at intake -- that field is the *intake* value and never moves.
   The operative disposition lives in the ADJUDICATION row that names it in `adjudicates`. 188 of 188
   read `UNDER_INVESTIGATION` in the investigation file; only **71** are named by an adjudication row.
   The other 117 are later-round rows, correctly not yet dispositioned because the round is in flight.
2. **`96` IS NOT THE DISPOSITIONED COUNT FOR IRPT_FNTEND -- IT IS EXACTLY THE UNDISPOSITIONED COUNT.**
   IRPT_FNTEND has TWO investigation files. `INVESTIGATION_v1.md` holds 41 rows, all 41 adjudicated;
   `INVESTIGATION_v2.md` held 96 when I quoted it and holds **97** now, **none** adjudicated. I reported
   the v2 file's SIZE and called it the dispositioned population. The true channel is 41 + 97 = **138**.

**THIS IS THE INHERITED-COUNT TRAP, COMMITTED BY THE SEAT THAT OWNS THE DENOMINATOR.** I handed two
other seats a number with no population attached; it arrived at their end looking measured, and row #8
-- the pause's lift evidence -- was about to be joined onto it. It is the same shape as
`IRPT_BCKEND-C-S85`, which I wrote against my own round 1: a count that can be believed and cannot be
checked. I did not catch it by re-reading my message. I caught it by running the count, which is the
only thing that ever catches it.

**Consequence for row #8, stated plainly:** the row-state column is thinner than my offer implied. Of
the 28 IRPT_BCKEND rows that name a storage-plane surface, **15 are NOT yet dispositioned** and 13 are.
A join that assumes "the project already decided this" will be wrong on the majority of the
storage-plane rows, and s.3 marks every one.

---

## 1. DENOMINATORS, AND HOW EACH WAS TAKEN

| file | rows | instrument |
|---|---|---|
| `IRPT_BCKEND/.../investigations/INVESTIGATION_v1.md` | 188 | `json.loads` of the single fenced block; ids unique (asserted, 0 duplicates) |
| `IRPT_BCKEND/.../adjudications/ADJUDICATION_v1.md` | 78 (71 name a target) | same |
| `IRPT_BCKEND/.../adjudications/ADJUDICATION_v2.md` | 7 (0 name a target -- standalone C-S rows) | same |
| `IRPT_BCKEND/.../remediations/REMEDIATION_v1.md` | 29 | same |
| `IRPT_FNTEND/.../investigations/INVESTIGATION_v1.md` | 41 | same |
| `IRPT_FNTEND/.../investigations/INVESTIGATION_v2.md` | 97 | same |
| `IRPT_FNTEND/.../adjudications/ADJUDICATION_v1.md` | 44 (41 name a target) | same |
| `IRPT_FNTEND/.../adjudications/ADJUDICATION_v2.md` | 6 (0 name a target) | same |
| `IRPT_FNTEND/.../remediations/REMEDIATION_v1.md` | 21 | same |

**Adjudication targets that resolve to no investigation row: 0 on both projects.** The mapping is total
in that direction -- every adjudication names a row that exists. The gap is the other way.

**Disposition vocabulary actually present:** `DISMISSED_WITH_REASON`, `GRADUATED` (adjudication rows);
`REMEDIATED` (remediation rows, keyed by the investigation row's OWN id). No other value occurs.

IRPT_BCKEND dispositions: {'DISMISSED_WITH_REASON': 48, 'GRADUATED': 23, 'NOT-YET-DISPOSITIONED': 117}

IRPT_FNTEND dispositions: {'GRADUATED': 19, 'DISMISSED_WITH_REASON': 22, 'NOT-YET-DISPOSITIONED': 97}

**AND THE C-S85 DEBT IS PARTLY PAID BY THIS FILE.** C-S85's defect was that round 1's consolidated
disposition had no per-item mapping. One exists and I did not know it: the 29 `REMEDIATION_v1.md` rows
are keyed by the INVESTIGATION row's own id, not by a new id. So the mapping was always derivable for
those 29; what was missing was anyone printing it. s.5 prints all 326.

---

## 2. COLUMN 4 -- HOW A "STORAGE-PLANE SURFACE" WAS DECIDED, AND ITS FALSE-POSITIVE MODE

Extraction is a regex sweep over each row's `one_line`, `spec_asserts`, `world_is`, `notes`,
`dismissal_reason` and every `grounding.evidence` string. A row counts as naming a surface if it matches
a **bucket** (`opal-data-*`, `opal-assets-*`, `opalinvest-*`), an **`s3://` URI**, a **tier-rooted key**
(`bronze|silver|gold|platinum/...`), or a named data prefix (`blackdiamond/`, `smartx/`, `corp/`). Repo
paths (`org/`, `infra/`, `src/`, `docs/`, `lib/`, ...) are excluded by construction.

**THE FALSE-POSITIVE MODE MATTERS MORE THAN THE HITS, AND IT DECIDES THE IRPT_FNTEND ANSWER.** A naive
sweep also matches `investor-reporting/...`, which on IRPT_FNTEND is a **URL route or a test fixture
key**, NOT an S3 key. Ten IRPT_FNTEND rows match that way and **every one is a route or a fixture**:
`investor-reporting/print?bundle=...` (a print route), `investor-reporting/export-preview` (a route
listed in `render/manifest.ts`), `investor-reporting/performance-report` and
`investor-reporting/holdings-snapshot` (pre-v1 route strings used as fixture KEYS in
`fixtures/smoke/*.json`). I read the surrounding sentence on all ten rather than trusting the token.
`investor-reporting/` is therefore excluded from column 4 on both projects.

**Two further classes are excluded and named so the exclusion is arguable:** a token that swallowed code
punctuation (`s3://{b['s3_key']}` -- a runtime expression, not a key) and any token whose braces do not
balance (a truncation artifact). **One** token was dropped on that rule, in `IRPT_BCKEND-S27`.

---

## 3. THE JOIN -- IRPT_BCKEND STORAGE-PLANE ROWS AGAINST ROW #8's THREE CONTRADICTS

`4.0.0_SA_CRO~D` graded three CONTRADICTS at `51cbf75cca`. This is what the project's own channel already
says about each, **with the disposition state marked** so no line reads as settled when it is not.

### 3.1 CONTRADICTS R1 -- `<firm bucket>/investor-reporting/...` carries no tier segment

- `IRPT_BCKEND-S1` **DISMISSED_WITH_REASON** (via `C-S1`) is the row that MOVED the directory and
  holdings platinum out of `opal-data-portal-v2` into the firm bucket under `investor-reporting/`. So
  the un-tiered key shape the doctrine now contradicts is **this seat's own accepted outcome**.
- **And its REASON is separately graded and was FALSIFIED.** S1's stated ground was that any key in
  `opal-data-portal-v2` is reachable unauthenticated; that was falsified on two planes, while the
  DESTINATION was independently ratified by Andrew for a different reason (firm separation). Row #8
  should cite S1's destination and must NOT inherit S1's reason.
- Still OPEN on the same surface: `IRPT_BCKEND-W2-S47` and `IRPT_BCKEND-W2-S49`
  (**NOT-YET-DISPOSITIONED**), which name `s3://<bucket>/investor-reporting/` directly.

### 3.2 CONTRADICTS R11+R14 -- platinum emitted directly, no gold parquet between silver and served

- `IRPT_BCKEND-W2-S7` **GRADUATED** names `s3://opal-data-{alias}/platinum/{firmId}/ownership_map.json`
  -- a platinum key written by a `gold`-named runner, which is the contradiction's own shape, already
  graduated by this seat.
- `IRPT_BCKEND-S27` and `IRPT_BCKEND-W2-S44` (**both NOT-YET-DISPOSITIONED**) name the
  `opal-data-mdpf/code/scripts/assets_gold/investor_reporting/` runner home.
- **No row in either channel names a gold parquet artifact for this project.** That is an absence over a
  printed denominator of 326 rows, not a recollection.

### 3.3 CONTRADICTS R4 + GAP-1 -- `opal-data-ycharts`

- **The report's "stale premise" is confirmed by the project's own rows, and they are more specific than
  the census.** `IRPT_BCKEND-S16` (**DISMISSED_WITH_REASON**) and `IRPT_BCKEND-W3-S10` (**GRADUATED**)
  both name `s3://opal-data-ycharts/research/20260911/variants/.../report.pdf` -- a LIVE object, dated,
  at the same prefix the census found 35 objects under. The PRD's "absent at inspection" was already
  contradicted inside this project before the canon existed.
- Four rows remain OPEN on the same bucket: `W4-S20`, `W4-S21`, `S41`, `S42` (**all
  NOT-YET-DISPOSITIONED**).

### 3.4 The two orders behind the external IAM decision -- MEASURED FROM THE ORDERS

- `IRPT_BCKEND.TO-IB-rt-6` -- `<status>pending`, handed by `2.0.0_SA_COO~B` 2026-09-12T05:48:29Z; its
  gate (IB-rt-2, IB-rt-3, IB-rt-5 terminal and merged) is SATISFIED on all three. It is not blocked by
  its own gate; it is blocked downstream of it.
- `IRPT_BCKEND.TO-IB-rtb-1` -- `<status>staged`, and its own text names the condition: it becomes
  pending only after IB-rt-1, -2, -4, **-6**, -7 and -8 are terminal and merged. **So rtb-1 is behind
  rt-6 BY THE ORDER'S OWN TEXT**, which is the dependency this seat has been carrying verbally.

---

## 4. IRPT_FNTEND -- THE ZERO IS WITHDRAWN, AND MY CHANNEL'S SILENCE IS A COVERAGE GAP, NOT A CONFIRMATION

Report v0.1 graded IRPT_FNTEND at ZERO CONTRADICTS citing `IRPT_FNTEND-S51`. `2.0.0_SA_COO~F` retracted
S51 whole (96267/96268) and `4.0.0_SA_CRO~D` regraded to v0.2 `@5288666762`. **An earlier draft of this
file argued the zero was well-supported. That argument is withdrawn.**

**I VERIFIED THE RETRACTION RATHER THAN RELAYING IT** -- four lines read directly in
`portal/src/pages/InvestorReporting/contracts/wire/`, all four present verbatim, in a directory holding
14 `.ts` files (the denominator S51 used):

| file:line | declaration |
|---|---|
| `AnalysisReport.ts:54` | `readonly storage_key: string` |
| `AnalysisRequest.ts:30` | `readonly storage_key: string` |
| `ExportReceipt.ts:20` | `readonly storage_bucket: string` |
| `ExportReceipt.ts:21` | `readonly storage_key: string` |

**The mechanism, which is `2.0.0_SA_COO~F`'s finding and not mine:** the detector was word-bounded, and
`_` is a word character, so `\bbucket\b` cannot match inside `storage_bucket`. Every snake_case compound
was invisible -- and snake_case is the wire contracts' own convention. The positive control fired on the
COMMENT (`opal-data-`), never on a field name, so it certified a detector that could not do its job.

**I WAS ONE STEP FROM THIS AND STOPPED.** My own draft noted that the only `opal-data-assets` token in
the entire IRPT_FNTEND channel sits INSIDE that control string -- and I recorded it as a neat detail
instead of asking what the control had actually exercised. **A control whose only hit is its own literal
is the tell**, and I had the tell in my hand.

**AND MY CHANNEL NUMBER MEASURES A DIFFERENT OBJECT THAN S51's.** My sweep reads ROW TEXT; S51 swept
SOURCE FILES. Two populations, two questions. So my zero does NOT corroborate a zero in the code and
must not be joined as if it did -- that is Rule 22's repetition-not-corroboration with the grain changed
underneath.

**WHAT MY ZERO ACTUALLY SAYS, AND IT IS WORTH MORE THAN THE CONFIRMATION IT IS NOT:** across 138
committed rows over four rounds, exactly **one** row ever mentioned a storage field --
`IRPT_FNTEND-W1-S17` (INERT, **NOT-YET-DISPOSITIONED**, names `storage_key`) -- and **no** row named a
bucket or a key of this project. The four surfaces were in the wire contracts the whole time and my
intake never surfaced them. **That is a coverage gap in my own L8, not evidence of absence**, and it is
the honest row-state answer for the FNTEND side of #8.

**The widened join (96272), complete:** rows touching `AnalysisReport.ts`, `AnalysisRequest.ts`,
`ExportReceipt.ts`, `storage_bucket` or `storage_key` number **2 of 138** -- `IRPT_FNTEND-W1-S17` and
`IRPT_FNTEND-S52` (COO~F's own correction row). **Both are NOT-YET-DISPOSITIONED**, so the FNTEND
row-state column joins to nothing the project has decided. The two rows that DO carry bucket tokens
(`S51`, `S52`) carry them as control literals and correction text, not as project surfaces.

---

## 5. THE PER-ITEM LEDGER -- ALL 326 ROWS

`VIA` names the artifact the disposition comes from. `NOT-YET-DISPOSITIONED` is a live state, not a gap
in this compile: those rows belong to rounds still in flight.

### 5.1 IRPT_BCKEND -- rows that name a storage-plane surface (28 of 188)

| ROW | HAZ | DISPOSITION | VIA | STORAGE-PLANE SURFACE NAMED | THE SURPRISE |
|---|---|---|---|---|---|
| `IRPT_BCKEND-S1` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S1 | `opal-data-bd`; `opal-data-portal-v2`; `opal-data-portal-v2-json` | IB-s-1 / IB-s-12: the PRD's SURFACE MANIFEST homes the directory and holdings PLATINUM JSON in opal-data-portal-v2 -- but that bucket is the origin of CloudFront behavior 19 (/json-tiered/* -> S3 d... |
| `IRPT_BCKEND-S2` | INERT | GRADUATED | adjudication IRPT_BCKEND-C-S2 | `opalinvest-portal` | IB-s-15: the PRD names /api/scoped/investor-reporting/... routes under the partners-api CUSTOM authorizer, but no CloudFront behavior matches that prefix at HEAD (28 behaviors read; the nearest is... |
| `IRPT_BCKEND-S16` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S16 | `opal-data-ycharts`; `s3://opal-data-ycharts/research/20260911/variants/.../report.pdf` | L4 HAND-OFF RELEASED at PRD v0.13 @e6ba5d9878 with both L4-R sign-offs (1.0.0_SA_CTO 95827; the notifier's COO row went to the base inbox that has no session, so the lane message is the delivery).... |
| `IRPT_BCKEND-S27` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/` | TO-IB-rt-5 grades on 'each of the 2 keys (2 of 2)', but the guard's bundle mechanism mints EXACTLY ONE S3 object -- the tar.gz at b['s3_key'] -- so a two-key denominator is not producible through t... |
| `IRPT_BCKEND-W1-S7` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S30 | `opal-data-cot`; `opal-data-inf` | IB-s-12: the first draft used the landed DirectoryEntry population (IB-s-1) as a HARD JOIN GATE for this cell's own custody joins, on the assumption that opaque_id(account, firm, raw) would resolve... |
| `IRPT_BCKEND-W1-S8` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S31 | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/holdings_snapshot.py` | IB-s-12: the issuer amendment required attempting the rule-13 code deploy through the guard's explicit first-mint mechanism (`--mint-bundle`) rather than accepting the push-gate's rc=0/SKIP-NOT-MEM... |
| `IRPT_BCKEND-W1-S11` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd`; `s3://opal-data-bd/investor-reporting/qa/directory/latest.json` | A FOURTH id-shape disagreement, found while moving the id space onto one normalizer (IB-rt-3): `_scope/resolve.py`'s `_OPAQUE_ID_PAT = re.compile(r'^[0-9a-f]{24}$')` -- the shape check `unmatched_r... |
| `IRPT_BCKEND-W2-S1` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S34 | `opal-data-inf`; `blackdiamond/cottonwood/silver/` | IB-s-1: the face's reuse list writes the INF and COT identity runners as `runners_inf/a00_dim_account.py`, `runners_inf/a01_dim_relationship.py`, `runners_inf/runner_common.py` and `runners_cot/a01... |
| `IRPT_BCKEND-W2-S3` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S36 | `silver/api_dims/accounts_v2` | IB-s-1 acceptance arm (c): the face names "the 79 unmapped INF accounts carry a reason each" and "INF 874-of-953 identity fixture". At the live vintage the INF population is 874 accounts of which 8... |
| `IRPT_BCKEND-W2-S4` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S37 | `blackdiamond/49f/silver/dim_account_xref`; `blackdiamond/49f/silver/dim_account_xref/date`; `gold/advi/dimensions/dim_identity_crosswalk/date` | IB-s-1: the face attributes `match_method` / `match_as_of` / `in_0833_universe` to the 49F runner `a06_dim_identity_crosswalk`. That runner emits none of the three; its columns are smartx_allocatio... |
| `IRPT_BCKEND-W2-S5` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S38 | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/directory_runner.py` | IB-s-1 / row IRPT_BCKEND-S4 RESOLVED, BUT NOT IN THE PREDICTED SHAPE, AND THE ACTUAL SHAPE IS A FALSE-GREEN. S4 asked whether .tools/safe-deploy.sh REFUSES a worker serial on a rule-13 gold path. M... |
| `IRPT_BCKEND-W2-S7` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S40 | `s3://opal-data-{alias}/platinum/{firmId}/ownership_map.json` | The face's signature is resolve(headers, directory) -> ResolvedScope, but NEITHER input carries an advisor-to-account link: the injected header set has no account claim, and DirectoryEntry delibera... |
| `IRPT_BCKEND-W2-S11` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S44 | `opal-data-bd`; `s3://opal-data-bd/investor-reporting/qa/holdings/2026-09-11/snapshot.json` | A THIRD ID SPELLING, AND IT MAKES ROW W1-S7 LOOK WORSE THAN IT IS. The holdings snapshot NAMESPACES its account ids -- scope.account_ids reads `49f:acct:acc_e57c30bb3e2ba80252fa0bd4` -- while the d... |
| `IRPT_BCKEND-W2-S27` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd` | A THIRD FIRM ID SPELLING: `performance/tenants.py` routes on `F-49F` / `F-COT` / `F-INF`, which is neither the registry spelling (`49financial`) nor the issued opaque id (`fir_...`), so the perform... |
| `IRPT_BCKEND-W3-S10` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S55 | `opal-data-ycharts`; `s3://opal-data-ycharts/research/20260911/variants/...` | A REAL VENDOR PDF LOSES THE 'fi' LIGATURE TO A FONT-SUBSET GLYPH, AND THE GLYPH'S CODE IS NOT THE SAME IN TWO DOCUMENTS FROM THE SAME VENDOR RUN. Text extracted from the three retained vendor PDFs... |
| `IRPT_BCKEND-W4-S3` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S60 | `opal-assets-bd49f-reporting-pull` | The deployed irpt-performance-adapter cannot carry two of its own dependencies, and neither remedy is inside this order's <paths>. (i) jsonschema is not in the AWS python3.12 runtime and infra/aws/... |
| `IRPT_BCKEND-W4-S15` | ARMED | NOT-YET-DISPOSITIONED | - | `s3://opal-313476888478-lambda-layers/irpt-common.zip` | THE `irpt-common` LAYER IS A SHARED WRITE SURFACE AND TWO ROUND-2 CELLS ARE WRITING IT FROM DISJOINT BRANCHES. One S3 key (s3://opal-313476888478-lambda-layers/irpt-common.zip) and one terraform-ma... |
| `IRPT_BCKEND-W4-S20` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | 'DELETED' ON A VERSIONED BUCKET MEANS 'HIDDEN FROM EVERY ORDINARY READ', NOT 'THE BYTES ARE GONE' -- and the difference is invisible in the receipt. opal-data-ycharts has versioning ENABLED (get-bu... |
| `IRPT_BCKEND-W4-S21` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | A RENDER ON THE SHARED BROWSER HOST NEEDED A GRANT THAT HOST'S OWN ROOT DOES NOT HAVE, so this cell declared it from ITS root against ANOTHER cell's role. irpt-ycharts-runner-role (IB-s-8, ycharts/... |
| `IRPT_BCKEND-S41` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | THE AUTHORIZED PER-VERSION DELETE WAS NOT TAKEN, AND NOT TAKING IT IS THE ACT. Andrew approved (via 1.0.0_SA_CTO 96041, 'All recs approved') the per-version delete of 'the FOUR noncurrent versions... |
| `IRPT_BCKEND-S42` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | DISARM of IRPT_BCKEND-S41 by its named disarm_owner. S41 required 1.0.0_SA_CTO to carry the CORRECTED count back to Andrew and report his answer on that corrected number; until then no version was... |
| `IRPT_BCKEND-W3-S37` | INERT | NOT-YET-DISPOSITIONED | - | `s3://opal-313476888478-terraform-state/investor-reporting/ycharts-research-20260911/tfstate` | After a Terraform root is DELETED from the tree, `terraform state list` in its directory refuses with 'Backend initialization required -- Unsetting the previously set backend s3', writes NOTHING to... |
| `IRPT_BCKEND-W3-S38` | ARMED | NOT-YET-DISPOSITIONED | - | `s3://opal-313476888478-terraform-state/investor-reporting/ycharts-research-20260911/tfstate` | The research root's S3 STATE OBJECT survives its root: the tree no longer declares ycharts-research-20260911 and nothing owns that state key, but the object is still there, empty, addressed by noth... |
| `IRPT_BCKEND-W2-S44` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` | ARM (d) IS BLOCKED ON ONE NAMED DEPENDENCY, measured on the host: `import directory_runner` fails with ModuleNotFoundError: No module named 'ids', the bundle carries only the two runner files, no i... |
| `IRPT_BCKEND-W2-S45` | INERT | NOT-YET-DISPOSITIONED | - | `s3://opal-data-{bd,cot,inf}/investor-reporting/directory/_refresh/` | The completion manifest that refresh.py's own docstring calls 'the ONLY memory this cell has between fires' is NEVER PERSISTED and never read back: refresh.py contains zero references to boto3/s3/p... |
| `IRPT_BCKEND-W2-S47` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd`; `opal-data-cot`; `opal-data-inf`; `s3://<bucket>/investor-reporting/`; `s3://opal-data-bd/`; `s3://opal-data-{bd,cot,inf}/investor-reporting/`; `s3://opal-data-{bd,cot,inf}/investor-reporting/qa/` | Arm (b) asks for a revision 'before and after (r -> r+1)' and for 'the previous revision object still present', but NO production directory artifact has ever existed for any firm: all three latest.... |
| `IRPT_BCKEND-W2-S49` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-49financial`; `opal-data-assets`; `opal-data-bd`; `opal-data-cot`; `opal-data-inf`; `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/`; `gold/eclipse/*`; `silver/api_dims/accounts_v2/*`; `silver/eclipse/*` | THE SCHEDULED-GOLD HOST CANNOT BUILD ANY OF THE THREE DIRECTORIES AND CANNOT WRITE ANY OF THE THREE DESTINATIONS. Measured from the host's own identity, not from a policy read: 5 of 9 source prefix... |
| `IRPT_BCKEND-W2-S50` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd` | S3 CANNOT SAY 'ABSENT' TO A CALLER THAT CANNOT LIST, AND THAT MADE THIS CELL UNABLE TO BOOTSTRAP. A GetObject on a MISSING key returns 403 AccessDenied -- not 404 -- when the principal has no s3:Li... |

### 5.2 IRPT_FNTEND -- rows that name a storage-plane surface (2 of 138, both control/correction text)

| ROW | HAZ | DISPOSITION | VIA | STORAGE-PLANE SURFACE NAMED | THE SURPRISE |
|---|---|---|---|---|---|
| `IRPT_FNTEND-S51` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-assets`; `smartx/account/{uuid}/`; `smartx/allocation/{uuid}/`; `smartx/model/{uuid}/` | THE FIRST TWO RATIFIED CARDS OF THE CENSUS DO NOT CONTRADICT ROUND 4 ON THE PLANE THEY GOVERN -- 0 of 14 investor-reporting wire contracts carry ANY storage-plane surface, detector FIRES on a posit... |
| `IRPT_FNTEND-S52` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-assets` | SELF-CORRECTION, LOAD-BEARING: row S51's headline "0 of 14 wire contract files carry ANY storage-plane surface" IS FALSE. The true figure is 4 SURFACES IN 3 OF 14 FILES -- AnalysisReport.ts:54 and... |

### 5.3 IRPT_BCKEND -- the full channel (188)

| ROW | HAZ | DISPOSITION | VIA | STORAGE-PLANE SURFACE NAMED | THE SURPRISE |
|---|---|---|---|---|---|
| `IRPT_BCKEND-S1` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S1 | `opal-data-bd`; `opal-data-portal-v2`; `opal-data-portal-v2-json` | IB-s-1 / IB-s-12: the PRD's SURFACE MANIFEST homes the directory and holdings PLATINUM JSON in opal-data-portal-v2 -- but that bucket is the origin of CloudFront behavior 19 (/json-tiered/* -> S3 d... |
| `IRPT_BCKEND-S2` | INERT | GRADUATED | adjudication IRPT_BCKEND-C-S2 | `opalinvest-portal` | IB-s-15: the PRD names /api/scoped/investor-reporting/... routes under the partners-api CUSTOM authorizer, but no CloudFront behavior matches that prefix at HEAD (28 behaviors read; the nearest is... |
| `IRPT_BCKEND-S3` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S3 | none | IB-s-6: the PRD (v0.3) marks the Graph/certificate mailbox reuse source UNRESOLVED. One inspect candidate exists in the estate that the brief did not name: infra/aws/ec2/opal-gateway/app/config.py... |
| `IRPT_BCKEND-S4` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S4 | none | IB-s-1 / IB-s-12: both land gold runners under data/assets/scripts/gold/investor_reporting/, a CLAUDE.md rule-13 DS surface whose S3 code deploy runs through .tools/safe-deploy.sh. Whether a worker... |
| `IRPT_BCKEND-S5` | INERT | GRADUATED | adjudication IRPT_BCKEND-C-S5 | none | IB-s-10: section extraction is to be certified against paired PDFs, and no real YCharts PDF exists in the estate (the private packet's PDF response bodies are absent; the four-page Opal export PDF... |
| `IRPT_BCKEND-S6` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S6 | none | DISARM of IRPT_BCKEND-W1-S2 (12 of 74 PATHS tokens unreadable from a fresh worktree) by its named owner, at the drain of IB-s-18: (1) the three gitignored brand sources (deck_generation/brand/opal_... |
| `IRPT_BCKEND-S7` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S7 | none | EVERY L7 WORKER SPAWNED ON THIS FABRIC SINCE 22:43:03Z RUNS ON SONNET, NOT OPUS. .claude/agents/worker.md line 5 reads `model: sonnet` at HEAD since the merge b9ee1966cc (origin/SITEZ into CLOUD, 2... |
| `IRPT_BCKEND-S8` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S8 | none | DISARM of IRPT_BCKEND-W2-S7 (disarm_owner 2.0.0_SA_COO~B), same drain it merged in: the ownership-map/id_projection seam that IB-s-2 injected into the scope resolver fails SAFE-AND-SILENT when the... |
| `IRPT_BCKEND-S9` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S9 | none | DISARM of IRPT_BCKEND-W2-S9 and IRPT_BCKEND-W2-S10 (disarm_owner 2.0.0_SA_COO~B), the same drain they merged in (3cca035c66). W2-S9: the firm id has two spellings (registry id in X-Firm-Id and _key... |
| `IRPT_BCKEND-S10` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S10 | none | DISARM of IRPT_BCKEND-W1-S7 (ARMED) and IRPT_BCKEND-W1-S8 (BLOCKING), disarm_owner 2.0.0_SA_COO~B, the same drain they merged in (3bed36da5b). W1-S8: the rule-13 first-mint of this project's gold s... |
| `IRPT_BCKEND-S11` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S11 | none | PRD MOVED TO v0.8 @d67e9813b5 MID-ROUND (v0.5 at 00:54Z, v0.6/v0.7/v0.8 through 03:09Z; 1.0.0_SA_CTO 95705 and 95751, information only) and the CTO left the amend-at-drain versus re-cut-in-round-2... |
| `IRPT_BCKEND-S12` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S12 | none | PRD v0.9 @86bde3ea26 (1.0.0_SA_CTO 95756, Andrew-direct ~03:1xZ: the proven YCharts cloud chain is FWD-4's FIXED mechanism, same shape as the 09-10 runner-STYLE constraint) folded into the un-hande... |
| `IRPT_BCKEND-S13` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S13 | none | DISARM of IRPT_BCKEND-W3-S5 (ARMED; the worker disarmed it for its own cell and routed the fallback's meaning to the issuer). The issuer's (amend) arm of 812bbec0e9 named `routes.json` as the guard... |
| `IRPT_BCKEND-S14` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S14 | none | PRD v0.10 @3624e60def (1.0.0_SA_CTO 95780, 04:03Z) landed MINUTES AFTER IB-s-9 was handed to slot ~3 at 1f795d1f71: all three YCharts recipes proven live in one Lambda by the CRO on Andrew's word (... |
| `IRPT_BCKEND-S15` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S15 | none | DISARM of IRPT_BCKEND-W2-S11 (ARMED, disarm_owner 2.0.0_SA_COO~B), the same drain it merged in: a THIRD id spelling -- HoldingsSnapshot namespaces account ids (`<firm>:acct:acc_...`) while Director... |
| `IRPT_BCKEND-S16` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S16 | `opal-data-ycharts`; `s3://opal-data-ycharts/research/20260911/variants/.../report.pdf` | L4 HAND-OFF RELEASED at PRD v0.13 @e6ba5d9878 with both L4-R sign-offs (1.0.0_SA_CTO 95827; the notifier's COO row went to the base inbox that has no session, so the lane message is the delivery).... |
| `IRPT_BCKEND-S17` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S17 | none | ISSUER RE-SEQUENCING at 05:1xZ on Andrew's question ('what's holding you up?'): the six remaining cells form ONE sequential chain through slot ~3 by the decomposition's edges (9 -> 10 -> 14 -> 16 -... |
| `IRPT_BCKEND-S18` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S18 | none | TWO ISSUER FACTS at the IB-s-9 drain (7799dcfb10), on Andrew's word 'keep it moving'. (1) RE-SEQUENCING, same shape as S17: IB-s-16 is handed to idle slot ~1 ahead of IB-s-14's merge. Its seven rec... |
| `IRPT_BCKEND-S19` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S19 | none | DISARM-BY-CARRY of IRPT_BCKEND-W4-S9, W4-S10, W4-S12 and W4-S13 (all ARMED, disarm_owner 2.0.0_SA_COO~B) at the IB-s-14 drain. All four are product decisions outside every un-handed face's paths an... |
| `IRPT_BCKEND-S20` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S20 | none | ROUTING of IRPT_BCKEND-W3-S12 (ARMED; disarm_owner '2.0.0_SA_COO~B to route and IB-s-17's assignee to repair') at the IB-s-10 drain: `_keys.s3_evidence_key` lets a client display name or an e-mail... |
| `IRPT_BCKEND-S21` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S21 | none | DISARM of IRPT_BCKEND-W1-S9 (ARMED, disarm_owner 2.0.0_SA_COO~B) -- an ISSUER DEFECT: the S15 amendment (902ea877dc) told four faces to normalise holdings account ids 'through the ONE normaliser IB... |
| `IRPT_BCKEND-S22` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S22 | none | ROUTING of IRPT_BCKEND-W2-S12 (BLOCKING, disarm_owner 2.0.0_SA_COO~B) at the IB-s-15 drain (ac2ee67133). IB-s-15's STOP fired correctly: the portal-auth plan reads 'Plan: 0 to add, 3 to change, 0 t... |
| `IRPT_BCKEND-S23` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S23 | none | DISARM of IRPT_BCKEND-W2-S12 (BLOCKING) by the CTO's ruling 95933 and both never-widen sign-off halves. 1.0.0_SA_CTO, as the gate over the portal-auth root (0.7.0_AE_CloudOps has no live session),... |
| `IRPT_BCKEND-S24` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S71 | none | ROUND 1 TERMINAL at f8860a4a4b: 19 of 19 task orders read <status>complete with VALID instances re-graded by the issuer at each drain (denominator: 19 files under task-orders/). DISARM-BY-CARRY of... |
| `IRPT_BCKEND-S25` | INERT | NOT-YET-DISPOSITIONED | - | none | ROUND 2 ISSUED. On the CTO's round-1 analysis (ledger/ROUND_ANALYSIS.round1.md @0d57ceb2f9: 10 of 10 outcomes served, no addendum, 0 REALIZED, eight rulings) and the CVO's slug (REMEDIATION_v1.md @... |
| `IRPT_BCKEND-S26` | INERT | NOT-YET-DISPOSITIONED | - | none | DISARM of IRPT_BCKEND-W2-S16 (BLOCKING, disarm_owner 2.0.0_SA_COO~B) by a CRITERION RE-CUT at IB-rt-1's first drain (0e60e9645b). The finding: the eleven v1 schemas are DOCUMENT contracts, two can... |
| `IRPT_BCKEND-S27` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/` | TO-IB-rt-5 grades on 'each of the 2 keys (2 of 2)', but the guard's bundle mechanism mints EXACTLY ONE S3 object -- the tar.gz at b['s3_key'] -- so a two-key denominator is not producible through t... |
| `IRPT_BCKEND-S28` | ARMED | NOT-YET-DISPOSITIONED | - | none | The decomposition's literal 'sha_metadata_key: script-sha256' for BOTH bundle members collides inside build_bundle_payload and silently drops one member's sha; implemented literally it produces a s... |
| `IRPT_BCKEND-S29` | ARMED | NOT-YET-DISPOSITIONED | - | none | The guard's own self-test suites were ALREADY FAILING before this cell touched anything -- test_code_trees_invariant.py 3 of 18 and test_safe_deploy.py 7 of 14 -- so RT5-AC1(a)'s 'the guard's self-... |
| `IRPT_BCKEND-S30` | INERT | NOT-YET-DISPOSITIONED | - | none | The task order instructs a DS lane to mint row ids of the form IRPT_BCKEND-D-S<k>, which the ratified investigation-item schema REFUSES: the id pattern admits only the Z-, W<n>- and C- infixes. |
| `IRPT_BCKEND-S31` | INERT | NOT-YET-DISPOSITIONED | - | none | TO-IB-rt-5 contradicts itself: RT5-AC1(c) instructs a no-op CHANGE to a runner committed on the branch, while BOUNDS 1 of the same face says 'do not edit the runners'. |
| `IRPT_BCKEND-S32` | ARMED | NOT-YET-DISPOSITIONED | - | none | Both round-1 batteries grade the first-mint by head-object on a LOOSE per-file key, so now that the mint has correctly landed as a BUNDLE they will read ABSENT / DEPLOY LEG BLOCKED -- a FALSE RED t... |
| `IRPT_BCKEND-S33` | INERT | NOT-YET-DISPOSITIONED | - | none | ROUND 2, SECOND DRAIN BATCH: four branches landed, two orders COMPLETE, one OPEN and routed, one COMPLETE then RE-OPENED on Andrew's word. (1) IB-rt-4 (slot ~3) merged OPEN at 98f756a90c: its withh... |
| `IRPT_BCKEND-S34` | INERT | NOT-YET-DISPOSITIONED | - | none | ROUND 2, THIRD DRAIN: IB-rt-3 (slot ~1) merged COMPLETE at 2a42c9563f through four conflicts -- the channel and PATH_MANIFEST as unions, infra/aws/lambda/layers/irpt-common/build_layer.py as the UN... |
| `IRPT_BCKEND-S35` | INERT | NOT-YET-DISPOSITIONED | - | none | ROUND 2, DRAINS FOUR TO SIX AND THE MANAGED WIND-DOWN. (1) IB-rt-4 (slot ~3) merged COMPLETE at 3ed2c79443: arm (e) at the merged tip, the export root's baseline plan read No changes (W3-S17's thre... |
| `IRPT_BCKEND-S36` | INERT | NOT-YET-DISPOSITIONED | - | none | WIND-DOWN DRAINS. (1) IB-rt-2's wind-down branch (496a2767d2, slot ~2) landed at 5347f30b34: no ledger opened across two runs, arm (a) reads 0 of 11 unguarded across all six functions with the cont... |
| `IRPT_BCKEND-W1-S1` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S24 | none | IB-s-18: the task order's L5 note says the PATH_MANIFEST expands '27 reuse rows ... 5 new homes'. The PRD PATHS table at the pin carries 26 reuse rows and 5 new rows, 31 in total, expanding to 74 c... |
| `IRPT_BCKEND-W1-S2` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S25 | none | IB-s-14 / IB-s-15 / IB-s-2: 12 of the 74 PATHS tokens are NOT READABLE from a worker's fresh worktree, by two different mechanisms. (1) THREE brand sources the PRD names as B14's brand authority --... |
| `IRPT_BCKEND-W1-S3` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S26 | none | IB-s-17: safe-apply's FIRST identity gate (the HALTGT checkpoint) refused the apply fail-closed with 'IDENTITY UNRESOLVED' until org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial named the acting se... |
| `IRPT_BCKEND-W1-S4` | INERT | GRADUATED | adjudication IRPT_BCKEND-C-S27 | none | IB-s-17: the root .gitignore:206 carries '**/.terraform.lock.hcl', so this root's provider lock CANNOT be committed without a forced add -- while 35 sibling roots under infra/aws/terraform/ DO trac... |
| `IRPT_BCKEND-W1-S5` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S28 | none | IB-s-18's S18-AC1 arm (d) asserts 'no .terraform/ directory and no terraform.tfstate* exists under any root' and its proof recorded '0 of 9 roots initialised'. IB-s-17 has now legitimately initiali... |
| `IRPT_BCKEND-W1-S6` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S29 | none | IB-s-5: the preflight declares 'this cell's role is graded at Phase 1 by `comp-iam service irpt-core` once its .tf exists and at Phase 2 by `comp-iam gaps`'. Both ran, after the apply, against the... |
| `IRPT_BCKEND-W1-S7` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S30 | `opal-data-cot`; `opal-data-inf` | IB-s-12: the first draft used the landed DirectoryEntry population (IB-s-1) as a HARD JOIN GATE for this cell's own custody joins, on the assumption that opaque_id(account, firm, raw) would resolve... |
| `IRPT_BCKEND-W1-S8` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S31 | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/holdings_snapshot.py` | IB-s-12: the issuer amendment required attempting the rule-13 code deploy through the guard's explicit first-mint mechanism (`--mint-bundle`) rather than accepting the push-gate's rc=0/SKIP-NOT-MEM... |
| `IRPT_BCKEND-W1-S9` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S32 | none | IB-s-16's hand-off (issuer amendment 812bbec0e9 + 902ea877dc, fact 4) asserts 'IB-s-4's one normaliser' strips the `<firm>:acct:` namespace prefix where a holdings id crosses the directory seam, an... |
| `IRPT_BCKEND-W1-S10` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S33 | none | IB-sb-3's real-file unguarded_routes() census over routes.json (S13's real-file case) reads 6 of 11 handler-bearing routes unguarded, not the 3 the amendment names as the EXPECTED population (row S... |
| `IRPT_BCKEND-W1-S11` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd`; `s3://opal-data-bd/investor-reporting/qa/directory/latest.json` | A FOURTH id-shape disagreement, found while moving the id space onto one normalizer (IB-rt-3): `_scope/resolve.py`'s `_OPAQUE_ID_PAT = re.compile(r'^[0-9a-f]{24}$')` -- the shape check `unmatched_r... |
| `IRPT_BCKEND-W1-S12` | ARMED | NOT-YET-DISPOSITIONED | - | none | TWO ROUND-2 CELLS ARE REBUILDING THE SAME SHARED LAYER CONCURRENTLY, and `aws_lambda_layer_version` REPLACES rather than appends, so each publish DESTROYS the other's version. Measured: at this cel... |
| `IRPT_BCKEND-W1-S13` | INERT | NOT-YET-DISPOSITIONED | - | none | ARM (b)'S FLOOR IS UNREACHABLE BY CONSTRUCTION, AND NOT BECAUSE THE IDS DISAGREE. The face asks for equal ids 'N of N per firm with N >= the round-1 populations (7,453 / 790 / 946)', but N there is... |
| `IRPT_BCKEND-W1-S14` | INERT | NOT-YET-DISPOSITIONED | - | none | THE ISSUER AMENDMENT ORDERS A FIRST ACT ON A PATH THIS ORDER'S <paths> GRANT DOES NOT NAME -- AND THE ACT IS ALREADY A NO-OP ON THE RUNTIME, MEASURED. IB-rt-7's amendment (row W4-S15) makes the FIR... |
| `IRPT_BCKEND-W1-S15` | INERT | NOT-YET-DISPOSITIONED | - | none | THE API ROOT'S PLAN CARRIES THREE LINES, NOT TWO, AND THE THIRD IS THE ROUTE TARGET'S OWN PREREQUISITE. IB-rt-7's third bound reads 'The api root's plan shows only the added integration and route t... |
| `IRPT_BCKEND-W1-S16` | ARMED | NOT-YET-DISPOSITIONED | - | none | `_authz.Enforcer.covers()` ADMITS ANY ADVISOR ID FOR A FIRM-OPERATIONS OR OPAL VIEWER, INCLUDING ANOTHER FIRM'S -- its own docstring says 'within the verified firm' and the branch does not check th... |
| `IRPT_BCKEND-W2-S1` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S34 | `opal-data-inf`; `blackdiamond/cottonwood/silver/` | IB-s-1: the face's reuse list writes the INF and COT identity runners as `runners_inf/a00_dim_account.py`, `runners_inf/a01_dim_relationship.py`, `runners_inf/runner_common.py` and `runners_cot/a01... |
| `IRPT_BCKEND-W2-S2` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S35 | none | IB-s-1 / IB-s-18 contract: DirectoryEntry.schema.json types `ids.relationship_id` as bare {"type": "string"} while its OWN description for that property says "an account-only entry carries null". A... |
| `IRPT_BCKEND-W2-S3` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S36 | `silver/api_dims/accounts_v2` | IB-s-1 acceptance arm (c): the face names "the 79 unmapped INF accounts carry a reason each" and "INF 874-of-953 identity fixture". At the live vintage the INF population is 874 accounts of which 8... |
| `IRPT_BCKEND-W2-S4` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S37 | `blackdiamond/49f/silver/dim_account_xref`; `blackdiamond/49f/silver/dim_account_xref/date`; `gold/advi/dimensions/dim_identity_crosswalk/date` | IB-s-1: the face attributes `match_method` / `match_as_of` / `in_0833_universe` to the 49F runner `a06_dim_identity_crosswalk`. That runner emits none of the three; its columns are smartx_allocatio... |
| `IRPT_BCKEND-W2-S5` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S38 | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/directory_runner.py` | IB-s-1 / row IRPT_BCKEND-S4 RESOLVED, BUT NOT IN THE PREDICTED SHAPE, AND THE ACTUAL SHAPE IS A FALSE-GREEN. S4 asked whether .tools/safe-deploy.sh REFUSES a worker serial on a rule-13 gold path. M... |
| `IRPT_BCKEND-W2-S6` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S39 | none | IB-s-1 acceptance arm (f) requires 'the ledger CLOSED and the sentinel committed (hash)'. Those two clauses cannot BOTH hold at the moment of grading: .tools/deploy_ledger.py close DELETES org/crit... |
| `IRPT_BCKEND-W2-S7` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S40 | `s3://opal-data-{alias}/platinum/{firmId}/ownership_map.json` | The face's signature is resolve(headers, directory) -> ResolvedScope, but NEITHER input carries an advisor-to-account link: the injected header set has no account claim, and DirectoryEntry delibera... |
| `IRPT_BCKEND-W2-S8` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S41 | none | The face names the principal-class vocabulary as (firm-advisor / firm-admin / opal); the ResolvedScope contract this cell must validate against carries a DIFFERENT enum -- OPAL_GLOBAL / FIRM_ADVISO... |
| `IRPT_BCKEND-W2-S9` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S42 | none | THE FIRM ID HAS TWO SPELLINGS AND THE TWO MODULES BENEATH THIS WRAPPER REQUIRE OPPOSITE ONES. X-Firm-Id carries the REGISTRY id (49financial -- index.mjs:387 injects payload.firmId) and _keys.cache... |
| `IRPT_BCKEND-W2-S10` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S43 | none | _keys.KeyComponentRefused NAMES THE REFUSED VALUE IN ITS MESSAGE -- twelve message sites use %r on the component, including keys.py:254 and keys.py:290 (parameter %r value %r matches no admissible... |
| `IRPT_BCKEND-W2-S11` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S44 | `opal-data-bd`; `s3://opal-data-bd/investor-reporting/qa/holdings/2026-09-11/snapshot.json` | A THIRD ID SPELLING, AND IT MAKES ROW W1-S7 LOOK WORSE THAN IT IS. The holdings snapshot NAMESPACES its account ids -- scope.account_ids reads `49f:acct:acc_e57c30bb3e2ba80252fa0bd4` -- while the d... |
| `IRPT_BCKEND-W2-S12` | INERT | GRADUATED | adjudication IRPT_BCKEND-C-S45 | none | THE CLOUDFRONT APPLY IS STOPPED BY ITS OWN GATE AND NOTHING WAS APPLIED. The pre-apply plan on the portal-auth root reads 'Plan: 0 to add, 3 to change, 0 to destroy' and names THREE resources, not... |
| `IRPT_BCKEND-W2-S13` | INERT | NOT-YET-DISPOSITIONED | - | none | THE TWO SIDES DO NOT AGREE ON WHAT AN OPERATION IS: the consumer publishes 11 flat slugs, the producer publishes 12 nested routes; 11 of 11 consumer paths are ROUTE_UNKNOWN under v1, 2 consumer ope... |
| `IRPT_BCKEND-W2-S14` | INERT | NOT-YET-DISPOSITIONED | - | none | FIELD NAMING IS TOTALLY DISJOINT ACROSS THE SEAM: 194 of the producer's 293 published property names are snake_case and 0 are camelCase; 139 of the consumer's 220 fixture keys are camelCase and 0 a... |
| `IRPT_BCKEND-W2-S15` | INERT | NOT-YET-DISPOSITIONED | - | none | REACH LIMIT, NAMED NOT HIDDEN: ops/status.py builds its own boto3 S3 client with no fixture path, so the analysis-report operation reaches AWS the moment the real handler is called in process; the... |
| `IRPT_BCKEND-W2-S16` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE PUBLISHED SCHEMAS ARE DOCUMENT CONTRACTS, NOT RESPONSE CONTRACTS: 0 of the 7 operations that reach a response return anything validating against its route's schema in ANY document position; the... |
| `IRPT_BCKEND-W2-S17` | INERT | NOT-YET-DISPOSITIONED | - | none | SELF-CORRECTION ON A ROW OF MINE, FILED RATHER THAN EDITED: W2-S16 named `FirmDestinationPolicy` as one of the eleven published schemas. It is not one of them. The eleventh is `RenderPackage` -- an... |
| `IRPT_BCKEND-W2-S18` | INERT | NOT-YET-DISPOSITIONED | - | none | THE RE-CUT NAMES TWO DENOMINATORS FOR THE SAME SET: 'one per route in routes.json' is 12 and 'the eleven response schemas ... 11 of 11' is 11. Both hold only if the NO-HANDLER-AT-HEAD route gets no... |
| `IRPT_BCKEND-W2-S19` | ARMED | NOT-YET-DISPOSITIONED | - | none | ARM (a) CANNOT READ `0 of N` IN THIS LANE: three of the eleven handler-bearing routes dispatch to `irpt-status`, whose source dir `infra/aws/lambda/investor-reporting/ops/` and whose Terraform root... |
| `IRPT_BCKEND-W2-S20` | INERT | NOT-YET-DISPOSITIONED | - | none | THE REAL CENSUS READS 11 OF 11 UNGUARDED, NOT 6 OF 11: every one of the six dispatched functions' DECLARED entry point is unwrapped at HEAD. The face's inherited `6 of 11` counted a table the round... |
| `IRPT_BCKEND-W2-S21` | ARMED | NOT-YET-DISPOSITIONED | - | none | TWO SERVED FUNCTIONS CANNOT BE REBUILT FROM COMMITTED SOURCE: irpt-ycharts-generate declares 25 build inputs of which 7 have NEVER existed in this repository, and irpt-status declares 7 of which 5... |
| `IRPT_BCKEND-W2-S22` | ARMED | NOT-YET-DISPOSITIONED | - | none | TWO CELLS ARE POINTED AT ONE SERVED FUNCTION: the issuer's own hand-off states IB-rt-4 is CONCURRENTLY re-applying its error-path envelope on irpt-export-render from slot ~3, while this order's <pa... |
| `IRPT_BCKEND-W2-S23` | INERT | NOT-YET-DISPOSITIONED | - | none | THE ONE ERROR ENVELOPE CANNOT EXPRESS THE REFUSAL THE AMENDMENT REQUIRES: `_authz/errors.py`'s PUBLIC_REASONS is CLOSED and does not contain `CONTRACT_VERSION`, which arm (g) names as the served pu... |
| `IRPT_BCKEND-W2-S24` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE GUARD IS WRITTEN AND HAS NO IN-LANE WAY TO REACH THE FIVE ZIPS: `_authz` is shared source, the estate distributes shared source by the `irpt-common` LAYER, and the layer's source dir, its build... |
| `IRPT_BCKEND-W2-S25` | INERT | NOT-YET-DISPOSITIONED | - | none | v1's RESPONSE CONTRACTS CANNOT REPRESENT A REFUSAL, and serving them is what revealed it: `firm_id` and `data` are both REQUIRED, `firm_id` is the opaque id that only exists inside a firm's directo... |
| `IRPT_BCKEND-W2-S26` | INERT | NOT-YET-DISPOSITIONED | - | none | THE PUBLISHED OPERATION IDS ARE NOT ADMISSIBLE KEY COMPONENTS: v1 names them with hyphens (`narrative-packet`) and `_keys.OPERATION_RE` is `^[a-z][a-z0-9_]{0,63}$`, so every guarded request was ref... |
| `IRPT_BCKEND-W2-S27` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd` | A THIRD FIRM ID SPELLING: `performance/tenants.py` routes on `F-49F` / `F-COT` / `F-INF`, which is neither the registry spelling (`49financial`) nor the issued opaque id (`fir_...`), so the perform... |
| `IRPT_BCKEND-W2-S28` | INERT | NOT-YET-DISPOSITIONED | - | none | THE RENAME ROUTED TO ME CANNOT BE COMPLETED IN LANE: `_authz/dispatch.py`'s ONLY importer is `_contracts/tests/test_seam_paired.py`, and `infra/aws/lambda/investor-reporting/_contracts/` is not in... |
| `IRPT_BCKEND-W2-S29` | INERT | NOT-YET-DISPOSITIONED | - | none | THE DIRECTORY PARITY CHECK IS STRUCTURALLY UNSATISFIABLE, NOT MERELY UNSATISFIED: two functions share one source directory and the builder's disk-to-manifest check runs PER FUNCTION, so whichever o... |
| `IRPT_BCKEND-W3-S1` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S46 | none | THE OFFLINE PROOF OF THE YCHARTS SESSION LIBRARY RUNS WITHOUT A REAL BROWSER. TO-IB-s-8's L5 note specifies 'a local browser against the captured HAR flows ... through a replay server', and arm (a)... |
| `IRPT_BCKEND-W3-S2` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S47 | none | THERE IS NO CAPTURED LOGIN FLOW ANYWHERE IN THIS CELL'S EVIDENCE, SO THE 'REPLAYED LOGIN FLOW' IN S8-AC1 ARM (a) IS MODELLED, NOT REPLAYED. Two separate facts, both measured. (1) The private packet... |
| `IRPT_BCKEND-W3-S3` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S48 | none | THE PER-FIRM EXECUTION ROLES THE FirmDestinationPolicy NAMES CANNOT BE ASSUMED BY ANY RUNNING FUNCTION, SO THE POLICY'S `execution_role` FIELD DESCRIBES A PER-FIRM LAMBDA FLEET RATHER THAN SOMETHIN... |
| `IRPT_BCKEND-W3-S4` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S49 | none | THE CHANGE-MANAGEMENT SENTINEL FOR THIS DEPLOY WAS NEVER COMMITTED IN ITS OPEN STATE, SO THE OPEN WINDOW EXISTS IN THE ENTRY BUT NOT IN GIT. The project bound requires the sentinel org/critical_pat... |
| `IRPT_BCKEND-W3-S5` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S50 | none | THE `routes.json` THE ISSUER AMENDMENT NAMES AS THE FALLBACK FOR THE GUARD CENSUS DOES NOT EXIST ANYWHERE IN THE CORPUS. The amendment's (amend) arm reads: 'Where this cell ships no handler, the sa... |
| `IRPT_BCKEND-W3-S6` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S51 | none | THE FACE ASKS FOR A `StatusEnvelope` VALUE THE CONTRACT DOES NOT DEFINE. The L5 note and the S7-AC1 (d) arm both name the correction state as the StatusEnvelope value `needs-correction` (lowercase,... |
| `IRPT_BCKEND-W3-S7` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S52 | none | THE REUSE PACKET THE ISSUER SUPPLEMENT TELLS THIS CELL TO READ FIRST DOES NOT EXIST IN THIS WORKTREE. The supplement (channel row IRPT_BCKEND-S14, PRD v0.10 @3624e60def) says 'READ THAT PACKET FIRS... |
| `IRPT_BCKEND-W3-S8` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S53 | none | THE CARRIED DECISION TABLE CANNOT SEE A WAF CHALLENGE WHOSE ONLY SIGNAL IS THE RESPONSE HEADER -- AND THE LIVE RUN MEASURED EXACTLY THAT CASE. docs/research/investor_reporting_ycharts_auth_20260910... |
| `IRPT_BCKEND-W3-S9` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S54 | none | THE FIXTURE MANIFEST -- THE ARTIFACT THAT SAYS WHICH FIXTURES ARE MEASURED AND WHICH ARE EXTENDED -- WENT STALE IN MY OWN PACKAGE, AND IT IS A DEPLOYED ZIP MEMBER. infra/aws/lambda/investor-reporti... |
| `IRPT_BCKEND-W3-S10` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S55 | `opal-data-ycharts`; `s3://opal-data-ycharts/research/20260911/variants/...` | A REAL VENDOR PDF LOSES THE 'fi' LIGATURE TO A FONT-SUBSET GLYPH, AND THE GLYPH'S CODE IS NOT THE SAME IN TWO DOCUMENTS FROM THE SAME VENDOR RUN. Text extracted from the three retained vendor PDFs... |
| `IRPT_BCKEND-W3-S11` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S56 | none | THE AnalysisReport CONTRACT REQUIRES A DATE ON EVERY TYPED SECTION; THE DOCUMENTS DO NOT STATE ONE FOR EVERY SECTION. infra/aws/lambda/investor-reporting/_contracts/AnalysisReport.schema.json makes... |
| `IRPT_BCKEND-W3-S12` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S57 | none | `_keys.s3_evidence_key` ACCEPTS A CLIENT DISPLAY NAME AND AN E-MAIL ADDRESS AS A PATH SEGMENT, CONTRADICTING ITS OWN DOCSTRING, AND IT IS THE FUNCTION THAT MINTS DURABLE S3 KEYS. Its docstring stat... |
| `IRPT_BCKEND-W3-S13` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE RULING NAMED ONE LEAKY KEY CONSTRUCTOR; THE CENSUS FOUND TWO, AND THE SECOND IS THE WORSE ONE. CTO ruling 4 closes row W3-S12, which named `_keys.s3_evidence_key` for accepting a client display... |
| `IRPT_BCKEND-W3-S14` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE EXPORT DOWNLOAD ROUTE IS DEAD IN THE DEPLOYED FUNCTION: IT IMPORTS A MODULE THE ZIP DOES NOT CONTAIN. infra/aws/lambda/investor-reporting/export/download.py does `import enforce as _authz` at M... |
| `IRPT_BCKEND-W3-S15` | ARMED | NOT-YET-DISPOSITIONED | - | none | ARM (c)'s DENOMINATOR IS EXCEPT HANDLERS, AND A PUBLIC REASON CAN BE BUILT WITHOUT ONE. The face's arm (c) says 'census the handler error paths ... str(exc) appears in 0 of them (AST census)', and... |
| `IRPT_BCKEND-W3-S16` | INERT | NOT-YET-DISPOSITIONED | - | none | THE RULING SAYS TWELVE %r MESSAGE SITES; THE MODULE CARRIED EIGHTEEN PLACEHOLDERS ACROSS SIXTEEN CONSTRUCTION SITES. CTO ruling 4 and the L5 note both say 'twelve %r message sites become zero'. Mea... |
| `IRPT_BCKEND-W3-S17` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE EXPORT TERRAFORM ROOT CANNOT BE APPLIED WITHOUT DESTROYING THREE LIVE RESOURCES THIS RULING DID NOT ORDER, SO irpt-export-render's CODE CHANGE IS COMMITTED AND ITS APPLY IS WITHHELD. Before any... |
| `IRPT_BCKEND-W3-S18` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE SOURCE MAP'S REGISTERED HASH FOR irpt-export-render AGREES WITH NEITHER S3 NOR THE LIVE FUNCTION, AND NOTHING IN THE ESTATE CATCHES THAT. lambda-source-map.json records artifact_sha256 = HSuSKs... |
| `IRPT_BCKEND-W3-S19` | ARMED | NOT-YET-DISPOSITIONED | - | none | A TWO-PART CHANGE WAS SPLIT BY THE DRAIN: THE CODE HALF MERGED AND THE PACKAGING HALF DID NOT, SO THE SOURCE MAP AT THE TIP DECLARED BUILDS FOR TWO FUNCTIONS THAT CANNOT IMPORT. In round 2 `_authz/... |
| `IRPT_BCKEND-W3-S20` | ARMED | NOT-YET-DISPOSITIONED | - | none | A SIBLING CELL IS WRITING TO THE SHARED EXPORT TERRAFORM STATE WHILE THIS ORDER IS NON-TERMINAL, AND CONVERGING THE ROOT FROM HERE WOULD DESTROY ONE LIVE RESOURCE AND REVERT TWO. This order's own a... |
| `IRPT_BCKEND-W3-S21` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE irpt-common LAYER'S OWN BUILD_MANIFEST DISAGREES WITH THE LAYER THAT IS PUBLISHED, SO THE RECORD OF WHAT THE SHARED RUNTIME CARRIES IS WRONG. infra/aws/lambda/layers/irpt-common/BUILD_MANIFEST.... |
| `IRPT_BCKEND-W3-S22` | ARMED | NOT-YET-DISPOSITIONED | - | none | TWO MODULES NAMED dispatch.py COLLIDE ON THE FLAT sys.path EVERY EXPORT MODULE SHARES, SO IB-rt-8's OWN TESTS CANNOT SEE ITS DISPATCH MODULE. `_authz/dispatch.py` and `export/dispatch.py` both exis... |
| `IRPT_BCKEND-W3-S23` | ARMED | NOT-YET-DISPOSITIONED | - | none | RT9-AC1 ARM (a) REQUIRES RETIRING A LEGACY PROBE THAT IS NOT IN THIS ORDER'S <paths>, AND THE SAME IS TRUE OF A SECOND LEGACY READER. The arm's words are 'legacy any-non-403 probes remaining: 0'. C... |
| `IRPT_BCKEND-W3-S24` | ARMED | NOT-YET-DISPOSITIONED | - | none | W2-S21's PREMISE DOES NOT HOLD AS WRITTEN, AND ACTING ON IT LITERALLY WOULD STRIP THE SHARED LIBRARIES OUT OF irpt-ycharts-generate. The amendment says the function declares 25 build inputs in lamb... |
| `IRPT_BCKEND-W3-S25` | ARMED | NOT-YET-DISPOSITIONED | - | none | _scope/resolve.py GAINED A MODULE-LEVEL 'import ids' AND THE PACKAGING HALF DID NOT FOLLOW FOR ANY OF THE THREE FUNCTIONS THAT SHIP IT. resolve.py at 684e7eb90a carries 'import ids as _ids' at line... |
| `IRPT_BCKEND-W4-S1` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S58 | none | IB-s-11 S11-AC1 arm (b) names `probe_performance.py` run offline over INVESTOR_REPORTING_PERFORMANCE_EVIDENCE_20260910.json, but that file carries RECEIPTS, FIELD SHAPES and VALIDATION AGGREGATES a... |
| `IRPT_BCKEND-W4-S2` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S59 | none | The task order's identity mechanism -- 'Every Bash call begins export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4' -- does NOT satisfy safe-apply.sh's halt gate. `.tools/halt-gate-check.sh` resolves t... |
| `IRPT_BCKEND-W4-S3` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S60 | `opal-assets-bd49f-reporting-pull` | The deployed irpt-performance-adapter cannot carry two of its own dependencies, and neither remedy is inside this order's <paths>. (i) jsonschema is not in the AWS python3.12 runtime and infra/aws/... |
| `IRPT_BCKEND-W4-S4` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S61 | none | The committed fixtures carry REAL client economic values -- market values around 63,000 USD, daily returns, fees and cash flows for one Black Diamond 49F account and one Orion Inflection household... |
| `IRPT_BCKEND-W4-S5` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S62 | none | S13-AC1 arm (h) asks that the layer zip imports jsonschema AND bd_helpers in a clean Python. bd_helpers does, on any host. jsonschema CANNOT on this one, and the reason is that the layer is CORRECT... |
| `IRPT_BCKEND-W4-S6` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S63 | none | The issuer amendment names TWO things the deployed irpt-performance-adapter could not carry (jsonschema and the bounded BD helpers). There is a THIRD, and jsonschema alone would not have moved the... |
| `IRPT_BCKEND-W4-S7` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S64 | none | The first assembled bd_helpers PARSED and could not IMPORT: the AST closure pulled functions and module-level constants but not module-level IMPORTS, so BENCHMARK_IDS = [int(x) for x in os.environ.... |
| `IRPT_BCKEND-W4-S8` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S65 | none | `.tools/aws` cannot be spawned from a Windows Python: subprocess raises OSError [WinError 193] is not a valid Win32 application, because the file is a bash script with no Windows launcher. Any batt... |
| `IRPT_BCKEND-W4-S9` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S66 | none | THE DEPLOYED EXPORT WORKER CANNOT RENDER, and this is the cell's central product gap rather than a packaging detail. A PDF needs a headless browser; none exists in a python3.12 Lambda and one canno... |
| `IRPT_BCKEND-W4-S10` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S67 | none | THE irpt-common LAYER CARRIES 2 OF THE 5 IRPT CONTRACTS THE DEPLOYED FUNCTIONS NEED. IB-s-13 built it for the performance and narrative functions, so it packages PerformanceReport and NarrativePack... |
| `IRPT_BCKEND-W4-S11` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_BCKEND-C-S68 | none | A REPO-RELATIVE PATH COMPUTED AT IMPORT KILLED THE DEPLOYED FUNCTION BEFORE IT COULD REPORT ANYTHING. assets.py resolved the estate's gitignored brand sources from `_HERE.parents[4]`; the packaged... |
| `IRPT_BCKEND-W4-S12` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S69 | none | A RETRY OF A BYTE-IDENTICAL BUNDLE MINTS A NEW export_id, AND NOTHING THIS CELL CAN DO PREVENTS IT. Chromium stamps a creation date and a document /ID into every PDF, so two renders of ONE frozen b... |
| `IRPT_BCKEND-W4-S13` | ARMED | GRADUATED | adjudication IRPT_BCKEND-C-S70 | none | THE BATTERY WRITES FOUR REAL OBJECTS INTO THE LIVE EVIDENCE BUCKET, under firms/49financial/generations/GENIBS14SYN/attempts/1/exports/{r1,v0-11-overview,v0-11-comparison,v0-11-multicomp}/report.pd... |
| `IRPT_BCKEND-W4-S14` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE CLOUD RENDER IS HUMAN-GATED, and the reason is NOT that no host carries a browser -- it is that no host carrying one may be started by this cell. Three candidates, each measured: (1) a NEW expo... |
| `IRPT_BCKEND-W4-S15` | ARMED | NOT-YET-DISPOSITIONED | - | `s3://opal-313476888478-lambda-layers/irpt-common.zip` | THE `irpt-common` LAYER IS A SHARED WRITE SURFACE AND TWO ROUND-2 CELLS ARE WRITING IT FROM DISJOINT BRANCHES. One S3 key (s3://opal-313476888478-lambda-layers/irpt-common.zip) and one terraform-ma... |
| `IRPT_BCKEND-W4-S16` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE ExportReceipt CONTRACT HAS NO SLOT FOR AN ATTEMPT ID, and the ruling asks the receipt to carry one. The CTO's ruling 5 and this face both say 'the receipt carries both plus the raw artifact dig... |
| `IRPT_BCKEND-W4-S17` | INERT | NOT-YET-DISPOSITIONED | - | none | THE ESTATE'S KEY GRAMMAR WAS NOT IN THE RUNTIME, and only a deployed invoke could see it. The export controller builds every S3 key through `_keys.s3_evidence_key` so a client name cannot become a... |
| `IRPT_BCKEND-W4-S18` | INERT | NOT-YET-DISPOSITIONED | - | none | THIS CELL'S OWN PROOF OBJECTS WERE THE CASE ITS EXCLUSION ARM EXISTS TO CATCH, for one run. The RT8 battery's submits write frozen bundles under generation GENRT8PROOF; that name does not end in SY... |
| `IRPT_BCKEND-W4-S19` | ARMED | NOT-YET-DISPOSITIONED | - | none | ROUND 1's RENDERER PRODUCED IDENTICAL CONTENT FROM THREE DIFFERENT BUNDLES, and its arm passed because the arm compared each PDF only to ITSELF. IB-s-14's (v0.11) built three Analysis exports from... |
| `IRPT_BCKEND-W4-S20` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | 'DELETED' ON A VERSIONED BUCKET MEANS 'HIDDEN FROM EVERY ORDINARY READ', NOT 'THE BYTES ARE GONE' -- and the difference is invisible in the receipt. opal-data-ycharts has versioning ENABLED (get-bu... |
| `IRPT_BCKEND-W4-S21` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | A RENDER ON THE SHARED BROWSER HOST NEEDED A GRANT THAT HOST'S OWN ROOT DOES NOT HAVE, so this cell declared it from ITS root against ANOTHER cell's role. irpt-ycharts-runner-role (IB-s-8, ycharts/... |
| `IRPT_BCKEND-W4-S22` | INERT | NOT-YET-DISPOSITIONED | - | none | THE PORTAL ORIGIN THIS CELL HAS BEEN CARRYING SINCE ROUND 2 IS A HOSTNAME THE ESTATE DOES NOT OWN, and only a browser could find out. local.portal_origin read `https://portal.opalcapital.co`; it is... |
| `IRPT_BCKEND-W4-S23` | ARMED | NOT-YET-DISPOSITIONED | - | none | '0 EXTERNAL CONNECTIONS DURING THE RENDER' IS NOT ACHIEVABLE AGAINST THE PORTAL AS BUILT, and the guard is what proved it: 12 requests, opalinvest.dev 10, fonts.googleapis.com 1, fonts.gstatic.com... |
| `IRPT_BCKEND-W4-S24` | ARMED | NOT-YET-DISPOSITIONED | - | none | TWO CELLS' MODULES SHARE ONE NAME ON ONE IMPORT PATH, and `import dispatch` silently answered with the OTHER cell's file. Round 2's IB-rt-2 added infra/aws/lambda/investor-reporting/_authz/dispatch... |
| `IRPT_BCKEND-W4-S25` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE RENDER IS NO LONGER HOST-GATED AND IS NOW SESSION-GATED: with the host authorized and started, Chromium reached https://opalinvest.dev/investor-reporting/print and the route answered with a SIG... |
| `IRPT_BCKEND-S37` | INERT | NOT-YET-DISPOSITIONED | - | none | WIND-DOWN COMPLETE FOR THIS SEAT: the last in-flight branch landed. IB-rt-9's wind-down branch (e021ddcdfd, slot ~3) drained at 22f2238cd7 with the order OPEN: arm (a), the v0.9 cutover, passes wit... |
| `IRPT_BCKEND-W3-S26` | ARMED | NOT-YET-DISPOSITIONED | - | none | The owed ids.py deploy cannot be taken: all THREE roots carry a committed, unapplied handler flip to entry.lambda_handler, and the entry module fails to import in the /var/task layout in 3 of 3 exe... |
| `IRPT_BCKEND-W3-S27` | ARMED | NOT-YET-DISPOSITIONED | - | none | irpt-export-render was never ARMED by the ids.py packaging gap: the irpt-common:5 layer already carries python/ids.py byte-identical to the tree's _ids/ids.py, so a rebuild without ids.py reads 13... |
| `IRPT_BCKEND-W3-S28` | ARMED | NOT-YET-DISPOSITIONED | - | none | The irpt-common:5 layer's python/keys.py is 21320 bytes and the tree's _keys/keys.py is 29894 -- irpt-export-render deliberately does not package keys.py, so the deployed function runs a key gramma... |
| `IRPT_BCKEND-W3-S29` | INERT | NOT-YET-DISPOSITIONED | - | none | Arm (a) does not re-confirm at 4 of 4 in the new worktree: it reads 4 of 5, because battery_ib_rt_9.py became TRACKED when its own branch was drained, and the a1 census (git ls-files) now counts th... |
| `IRPT_BCKEND-W3-S30` | INERT | NOT-YET-DISPOSITIONED | - | none | .tools/terraform.exe was NOT provisioned in this worktree, contrary to the order's bound 4; resolved by copying the SAME binary by path from the primary workspace (v1.9.8), never a PATH substitute. |
| `IRPT_BCKEND-S38` | INERT | NOT-YET-DISPOSITIONED | - | none | ISSUER SELF-CORRECTION, DISARMING W3-S26: my amendment A6 ordered slot ~3 to deploy irpt-export-render, irpt-status and irpt-ycharts-generate ahead of slot ~2 on the reasoning that until IB-rt-2's... |
| `IRPT_BCKEND-W3-S31` | ARMED | NOT-YET-DISPOSITIONED | - | none | The deployed generation job has NO eviction outcome: a 401 at the read-back is recorded as SETTINGS_DRIFTED and a 401 at the create as CREATE_NOT_VERIFIED, so an evicted session and a genuine contr... |
| `IRPT_BCKEND-W3-S32` | ARMED | NOT-YET-DISPOSITIONED | - | none | JobStore keeps only the LATEST state per job, so the durable `model_portfolio_id` written at SUBMITTED is ERASED by the next transition -- the checkpoint a recovery reads back no longer carries the... |
| `IRPT_BCKEND-W3-S33` | INERT | NOT-YET-DISPOSITIONED | - | none | The arm-(a) reader census caught this cell's OWN new broker before it was declared -- 4 of 5, UNACCOUNTED -- which is the table working; recorded because it is the second time in one session that a... |
| `IRPT_BCKEND-S39` | INERT | NOT-YET-DISPOSITIONED | - | none | DISPOSITION of W3-S31 and W3-S32. W3-S31: the worker declined to wire resume_allowed into job.py on the stated premise that job.py is IB-rt-2's artifact this round. THAT PREMISE IS FALSE AND THE DE... |
| `IRPT_BCKEND-W4-S26` | INERT | NOT-YET-DISPOSITIONED | - | none | THE FI-LIGATURE CODES ARE NOT RECOVERABLE FROM THESE DOCUMENTS AND THE RIGHT ANSWER IS THE RULING'S SECOND BRANCH. The TO's arm (a) reads 'the fi ligature is recovered through that document's map (... |
| `IRPT_BCKEND-W4-S27` | INERT | NOT-YET-DISPOSITIONED | - | none | CONTRACT ADDITION, FOR THE CTO'S L10 READ: an OPTIONAL `date_claim` enum (SECTION / REPORT / NONE) is now a property of AnalysisReport.sections[] in BOTH published copies -- infra/aws/lambda/invest... |
| `IRPT_BCKEND-W4-S28` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE ROUND-1 EXTRACTOR DATED ROWS FROM A NEIGHBOURING BLOCK AND FROM A DIFFERENT DOCUMENT, AND ITS OWN CERTIFICATION READ CERTIFIED THROUGHOUT. Re-derived from this run's rows by extract.round1_unda... |
| `IRPT_BCKEND-W4-S29` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE PATH REGISTER'S OWN VERIFIER CANNOT COMPLETE, AND THIS CELL APPENDS TO THAT REGISTER. battery_ib_s_18.py -- the battery that grades infra/aws/lambda/investor-reporting/PATH_MANIFEST.json, the r... |
| `IRPT_BCKEND-W4-S30` | INERT | NOT-YET-DISPOSITIONED | - | none | THE PATH REGISTER'S OWN PRINTED DENOMINATOR WAS STALE BY 41. infra/aws/lambda/investor-reporting/PATH_MANIFEST.json declared _meta.denominators.entries_total = 336 while its `entries` array held 37... |
| `IRPT_BCKEND-W4-S31` | INERT | NOT-YET-DISPOSITIONED | - | none | A HAND-BUILT PDF IS TEXT TO GIT, AND THE FRESH-WORKTREE FAILURE IS A HASH CHANGE ON A FILE NOBODY EDITED. git decides binary-vs-text on whether a NUL byte appears in the first 8 KB, and a PDF is no... |
| `IRPT_BCKEND-S40` | INERT | NOT-YET-DISPOSITIONED | - | none | DISPOSITION of IB-rt-10's six rows at its COMPLETE. W4-S28 IS THE ONE THAT MATTERS AND IT STAYS ARMED: round 1 dated 15 of 61 overview rows and 12 of 108 multi-comparison rows from a NEIGHBOURING b... |
| `IRPT_BCKEND-S41` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | THE AUTHORIZED PER-VERSION DELETE WAS NOT TAKEN, AND NOT TAKING IT IS THE ACT. Andrew approved (via 1.0.0_SA_CTO 96041, 'All recs approved') the per-version delete of 'the FOUR noncurrent versions... |
| `IRPT_BCKEND-W2-S30` | INERT | NOT-YET-DISPOSITIONED | - | none | Arm (a)'s whole-file denominator moved from 11 to 12 while this cell was dead: IB-rt-7's irpt-holdings is now LIVE on its published route, so routes.json resolves 12 handler-bearing routes and the... |
| `IRPT_BCKEND-W2-S31` | INERT | NOT-YET-DISPOSITIONED | - | none | The bypass detector grades a MARK, not a behaviour: is_guarded() reads __irpt_guarded__, so a handler that enforces FirmBinding + Enforcer.guard() INLINE (irpt-holdings' snapshot.lambda_handler) is... |
| `IRPT_BCKEND-W2-S32` | INERT | NOT-YET-DISPOSITIONED | - | none | A4's RULED remedy does not carry the modules: BOTH build scripts resolve a declared input ONLY as source_dir/<name> with no second step, so declaring served.py/loaders.py in files[] without a file... |
| `IRPT_BCKEND-W2-S33` | INERT | NOT-YET-DISPOSITIONED | - | none | The THREE functions A6 says IB-rt-9 deploys first are exactly the three carrying all 20 absent build inputs, so rt-9's first ledgered act refuses at the build before it reaches an apply -- and the... |
| `IRPT_BCKEND-W2-S34` | INERT | NOT-YET-DISPOSITIONED | - | none | The A5 rename leaves the FROZEN v1 contract naming a path that no longer exists: routes.json's `checked_by` and CONTRACT.md's provenance table both point at _authz/dispatch.py, and docs/contracts/... |
| `IRPT_BCKEND-W2-S35` | INERT | NOT-YET-DISPOSITIONED | - | none | A6 conditions this order's deploy on an act its assignee cannot perform -- 'Ask me; do not read its branch and decide for yourself' -- and a spine v3 L7 worker has no broker, no message tool and ca... |
| `IRPT_BCKEND-W2-S36` | INERT | NOT-YET-DISPOSITIONED | - | none | EVERY refusal the guarded boundary serves fails v1's StatusEnvelope on one clause -- source_dates.required is ['business_date'] and the boundary emits source_dates without one -- and the two halves... |
| `IRPT_BCKEND-W2-S37` | INERT | NOT-YET-DISPOSITIONED | - | none | The record corrected in flight: A6 was struck by the issuer mid-run and the six-root deploy landed and verified, so rows W2-S35 (the un-receivable release condition) and W2-S33 (rt-9's build) are O... |
| `IRPT_BCKEND-S42` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-ycharts` | DISARM of IRPT_BCKEND-S41 by its named disarm_owner. S41 required 1.0.0_SA_CTO to carry the CORRECTED count back to Andrew and report his answer on that corrected number; until then no version was... |
| `IRPT_BCKEND-S43` | INERT | NOT-YET-DISPOSITIONED | - | none | THE NINE NONCURRENT VERSIONS ARE PERMANENTLY GONE, AND 'THE FOUR SYNTHETIC EXPORT PDFS ARE GONE' NO LONGER CARRIES A QUALIFIER -- the first time that sentence has been true tonight. Andrew-direct ~... |
| `IRPT_BCKEND-S44` | ARMED | NOT-YET-DISPOSITIONED | - | none | IB-rt-2's EIGHT ROWS DISPOSITIONED, AND THE POST-READ OBLIGATION RE-ROUTED OFF A BATTERY THAT CANNOT FIRE. W2-S30: holdings paths GRANTED additively (holdings/ lambda + the holdings Terraform root)... |
| `IRPT_BCKEND-W3-S34` | INERT | NOT-YET-DISPOSITIONED | - | none | IB-rt-11's ORDERED edit to intake/settings.json moved a DECLARED BUILD INPUT of irpt-ycharts-generate 20 minutes after slot ~2 deployed and closed its ledger on it, so the tree and the served zip n... |
| `IRPT_BCKEND-W3-S35` | ARMED | NOT-YET-DISPOSITIONED | - | none | The shared contract's `corrections` item is additionalProperties:false with exactly four keys and no timestamp, so the WHEN this cell's law requires on a human correction CANNOT travel in the contr... |
| `IRPT_BCKEND-W3-S36` | ARMED | NOT-YET-DISPOSITIONED | - | none | parse.py and corrections.py are declared by 0 of 214 functions, so every currency and unit control this cell certifies is certified in the REPO for a module that has no runtime yet -- and the first... |
| `IRPT_BCKEND-S45` | ARMED | NOT-YET-DISPOSITIONED | - | none | IB-rt-11 ACCEPTED TERMINAL (8 of 12), AND ITS HEADLINE IS A FALSE GREEN CAUGHT BY ITS OWN AUTHOR AFTER THE FLIP. The worker flipped <status> complete, then found that commit 3c28723d20 pinned parse... |
| `IRPT_BCKEND-W2-S38` | INERT | NOT-YET-DISPOSITIONED | - | none | The ycharts root's zip carries intake/settings.json but not fixtures/holdings/security_mapping.json -- literally the asymmetry the issuer named as blocking -- and the discriminator is that NO funct... |
| `IRPT_BCKEND-W2-S39` | INERT | NOT-YET-DISPOSITIONED | - | none | A defect this cell INTRODUCED and has now removed: served.Entry held one cache dict for the MODULE'S lifetime, so a warm container served a payload computed from an artifact that had since changed... |
| `IRPT_BCKEND-W2-S40` | INERT | NOT-YET-DISPOSITIONED | - | none | The investor-reporting package's test suite cannot be run as a whole: a single pytest over the package reads 48 failed and 39 errors from cross-directory bare-name collisions, while every directory... |
| `IRPT_BCKEND-W2-S41` | ARMED | NOT-YET-DISPOSITIONED | - | none | Amendment 3 C1 grants the holdings paths in PROSE and the <paths> block does not carry them, so the lane gate refuses the commit -- C1's work is written, tested and PASSING in the worktree and cann... |
| `IRPT_BCKEND-S46` | ARMED | NOT-YET-DISPOSITIONED | - | none | IB-rt-2 REACHED 15 of 15 ARMS WITH THE TOKEN PRINTING AND DID NOT FLIP, AND BOTH HALVES OF THAT ARE CORRECT. W2-S41 IS THE ISSUER'S DEFECT AND IS FIXED: amendment 3's C1 granted infra/aws/lambda/in... |
| `IRPT_BCKEND-W3-S37` | INERT | NOT-YET-DISPOSITIONED | - | `s3://opal-313476888478-terraform-state/investor-reporting/ycharts-research-20260911/tfstate` | After a Terraform root is DELETED from the tree, `terraform state list` in its directory refuses with 'Backend initialization required -- Unsetting the previously set backend s3', writes NOTHING to... |
| `IRPT_BCKEND-W3-S38` | ARMED | NOT-YET-DISPOSITIONED | - | `s3://opal-313476888478-terraform-state/investor-reporting/ycharts-research-20260911/tfstate` | The research root's S3 STATE OBJECT survives its root: the tree no longer declares ycharts-research-20260911 and nothing owns that state key, but the object is still there, empty, addressed by noth... |
| `IRPT_BCKEND-S47` | ARMED | NOT-YET-DISPOSITIONED | - | none | IB-rt-9 ACCEPTED TERMINAL AT 6 OF 6 ARMS -- round 2 is 9 of 12, IB-rt-2 the only order still open. Issuer verification at HEAD rather than on the report: proof-of-spec-check VALID rc=0, 8 of 8 arti... |
| `IRPT_BCKEND-W2-S42` | ARMED | NOT-YET-DISPOSITIONED | - | none | The ycharts Terraform root now plans 0 to add, 0 to change, 2 to DESTROY -- a LIVE secret and a log group that IB-rt-9 removed from the configuration without applying -- so ANY apply of that root b... |
| `IRPT_BCKEND-W2-S43` | INERT | NOT-YET-DISPOSITIONED | - | none | MY OWN ROW W2-S42 MIS-ATTRIBUTED ITS CAUSE: the ycharts root's two pending destroys were not IB-rt-9 removing declarations, they were MY WORKTREE predating the commit that ADDS them -- `git log --... |
| `IRPT_BCKEND-S48` | INERT | NOT-YET-DISPOSITIONED | - | none | IB-rt-2 ACCEPTED TERMINAL -- round 2 is 10 of 12, IB-rt-6 RELEASED and IB-rtb-1 gated only on it. All seven functions live on entry.lambda_handler, proof-of-spec VALID rc=0 over 23 of 23 rows, stat... |
| `IRPT_BCKEND-W2-S44` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz` | ARM (d) IS BLOCKED ON ONE NAMED DEPENDENCY, measured on the host: `import directory_runner` fails with ModuleNotFoundError: No module named 'ids', the bundle carries only the two runner files, no i... |
| `IRPT_BCKEND-W2-S45` | INERT | NOT-YET-DISPOSITIONED | - | `s3://opal-data-{bd,cot,inf}/investor-reporting/directory/_refresh/` | The completion manifest that refresh.py's own docstring calls 'the ONLY memory this cell has between fires' is NEVER PERSISTED and never read back: refresh.py contains zero references to boto3/s3/p... |
| `IRPT_BCKEND-W2-S46` | INERT | NOT-YET-DISPOSITIONED | - | none | The L5 note's 'dispatch via SSM, WAIT BOUNDED for completion, read the completion manifest' cannot fit the function it is for: irpt-directory-refresh has a 60-SECOND timeout and the measured cost o... |
| `IRPT_BCKEND-W2-S47` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd`; `opal-data-cot`; `opal-data-inf`; `s3://<bucket>/investor-reporting/`; `s3://opal-data-bd/`; `s3://opal-data-{bd,cot,inf}/investor-reporting/`; `s3://opal-data-{bd,cot,inf}/investor-reporting/qa/` | Arm (b) asks for a revision 'before and after (r -> r+1)' and for 'the previous revision object still present', but NO production directory artifact has ever existed for any firm: all three latest.... |
| `IRPT_BCKEND-S49` | ARMED | NOT-YET-DISPOSITIONED | - | none | IB-rt-6's FOUR ROWS DISPOSITIONED AND ITS BLOCKER CLEARED -- it was a <paths> GAP, NOT A LANE REFUSAL. W2-S44: the runner cannot import on the host (ModuleNotFoundError: No module named 'ids', meas... |
| `IRPT_BCKEND-W2-S48` | INERT | NOT-YET-DISPOSITIONED | - | none | THE DEPLOYED REFRESH FUNCTION CANNOT RESOLVE A TRADING CALENDAR AT ALL -- its served zip carries four members and trading_calendar.py is not one of them -- so resolve_calendar() returns None, misse... |
| `IRPT_BCKEND-W2-S49` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-49financial`; `opal-data-assets`; `opal-data-bd`; `opal-data-cot`; `opal-data-inf`; `opal-data-mdpf`; `s3://opal-data-mdpf/code/scripts/`; `gold/eclipse/*`; `silver/api_dims/accounts_v2/*`; `silver/eclipse/*` | THE SCHEDULED-GOLD HOST CANNOT BUILD ANY OF THE THREE DIRECTORIES AND CANNOT WRITE ANY OF THE THREE DESTINATIONS. Measured from the host's own identity, not from a policy read: 5 of 9 source prefix... |
| `IRPT_BCKEND-W2-S50` | INERT | NOT-YET-DISPOSITIONED | - | `opal-data-bd` | S3 CANNOT SAY 'ABSENT' TO A CALLER THAT CANNOT LIST, AND THAT MADE THIS CELL UNABLE TO BOOTSTRAP. A GetObject on a MISSING key returns 403 AccessDenied -- not 404 -- when the principal has no s3:Li... |
| `IRPT_BCKEND-W2-S51` | INERT | NOT-YET-DISPOSITIONED | - | none | THE MINTED BUNDLE CANNOT CARRY WHAT THE RUNNER ACTUALLY NEEDS. directory_runner.py reaches ELEVEN repo paths by derivation; the bundle declares four of the files behind them and the remaining SEVEN... |
| `IRPT_BCKEND-W2-S52` | INERT | NOT-YET-DISPOSITIONED | - | none | `.tools/terraform.exe` was NOT provisioned in this worktree, although the order states the issuer provisioned it and forbids a PATH substitute. I restored it by copying the byte-identical binary fr... |
| `IRPT_BCKEND-W2-S53` | INERT | NOT-YET-DISPOSITIONED | - | none | THE PREFLIGHT THIS ORDER NAMES READS 'statements: 0' FOR A ROLE THAT HOLDS SEVEN. `comp-iam service irpt-directory-refresh` prints statements: 0 for BOTH irpt-directory-refresh-role and irpt-direct... |
| `IRPT_BCKEND-S50` | ARMED | NOT-YET-DISPOSITIONED | - | none | IB-rt-6 WORKED TO ITS WALL AND STAYS OPEN: 14 of 17 graded checks PASS, 0 FAIL, 3 BLOCKED, status untouched at pending. Amendment H's grant WORKED and the worker proved it with a negative control -... |

### 5.4 IRPT_FNTEND -- the full channel (138)

| ROW | HAZ | DISPOSITION | VIA | STORAGE-PLANE SURFACE NAMED | THE SURPRISE |
|---|---|---|---|---|---|
| `IRPT_FNTEND-W1-S1` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S1 | none | F1-AC1 (portal typecheck rc=0) and F1-AC2..AC6 (bun tests under src/) could not both pass without ambient type declarations the order does not name: the portal tsconfig's types array excludes @type... |
| `IRPT_FNTEND-W1-S2` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S2 | none | The order's 'lists fixtures/ and asserts 31 files' cannot be a literal directory listing: the same order puts fixtures/index.ts and fixtures/smoke/default.json in that directory, so a literal listi... |
| `IRPT_FNTEND-S1` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S3 | none | Disarm act for IRPT_FNTEND-W1-S1 assigned by its disarm_owner: TO-FE-s-2 (slot ~1, next in queue) is amended at the FE-s-1 drain to replace the shim's exported `interface Dirent` with an inline str... |
| `IRPT_FNTEND-W1-S3` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S4 | none | TO-FE-s-2 names PageThemeProvider as an export of portal/src/components/PageHeaderVariants.tsx; that file exports only PageHeaderCleanBadge, and PageThemeProvider is defined in portal/src/contexts/... |
| `IRPT_FNTEND-W1-S4` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S5 | none | PageSurfaceControl's `as="dropdown"` shape renders WHITE text on a TRANSPARENT background directly on the silver canvas -- measured on the component's OWN demo route as well as on this cell's heade... |
| `IRPT_FNTEND-W2-S1` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S6 | none | The two brand sources TO-FE-s-4 names -- deck_generation/brand_spec/brand.json and the logo package SVG -- are GITIGNORED, so they exist in the primary checkout and in NO worktree, including this w... |
| `IRPT_FNTEND-W2-S2` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S7 | none | The FE-s-1 ExportBundle contract carries NONE of what the FE-s-4 templates print -- no reportKind, no report payloads, no beginning/ending value, no disclosure text -- so the render package defines... |
| `IRPT_FNTEND-W2-S3` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S8 | none | No Lato font binary exists anywhere reachable -- not in the repo, not in deck_generation, not in either Windows font store -- and obtaining one is egress off Opal infrastructure, so the packaged fo... |
| `IRPT_FNTEND-W2-S4` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S9 | none | recharts 3.7.0 renders an EMPTY wrapper under react-dom/server renderToStaticMarkup -- 127 bytes, no <svg> -- so the cumulative return chart the cell names contributes nothing in a server-side rend... |
| `IRPT_FNTEND-W2-S5` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S10 | none | portal/scripts/ui-smoke.mjs compares window.location.pathname against the FULL route argument, so any route carrying a query string prints 'DID NOT LAND (auth redirect? bad route?)' even when it la... |
| `IRPT_FNTEND-S2` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S11 | none | Disarm act for IRPT_FNTEND-W1-S4 assigned by its disarm_owner: TO-FE-s-3 (slot ~1, next in queue) is amended at the FE-s-2 drain to pass PageSurfaceControl the className ModelPortfolios.tsx passes... |
| `IRPT_FNTEND-S3` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S12 | none | Disarm act for IRPT_FNTEND-W2-S2 assigned by its disarm_owner: TO-FE-s-9 (slot ~1, export) is amended at the FE-s-4 drain to build export/resolveBundle.ts, which turns the counterpart's reference-o... |
| `IRPT_FNTEND-S4` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S13 | none | Disarm act for IRPT_FNTEND-W2-S4 assigned by its disarm_owner: TO-FE-s-8 (slot ~2, next in queue) is amended at the FE-s-4 drain to declare runtime: 'browser' in render/manifest.ts, so the counterp... |
| `IRPT_FNTEND-S5` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S14 | none | IRPT_FNTEND-W2-S3 (no Lato binary anywhere on the estate; fetching one is egress) cannot be disarmed by this lane without Andrew's word: it is recorded as a PENDING INPUT beside the advisor logos a... |
| `IRPT_FNTEND-W2-S6` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S15 | none | FE-s-8's cell names NarrativePacket fields (annotations, trendingTopics, topicCloud, coverage, historyCutoff) and a live-imported MarketRegimeIndicator/SentimentGauge/SentimentPanel that neither ex... |
| `IRPT_FNTEND-S6` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S16 | none | Disarm act for IRPT_FNTEND-W2-S6 split by its disarm_owner: the WIRING half (PeriodInContextPage built and tested but not mounted, because render/performance/PerformanceDocument.tsx was outside FE-... |
| `IRPT_FNTEND-W1-S5` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S17 | none | `bun test` cannot resolve the portal's `@/*` alias AT ALL -- reproduced with a one-line probe importing `@/lib/utils` from a throwaway test file, independent of this cell -- so F3-AC7's `renderToSt... |
| `IRPT_FNTEND-W1-S6` | ARMED | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S18 | none | This order's assigned port 5181 was already bound by an ORPHANED vite dev server from the already-integrated FE-s-2 worker's worktree (wk-irpt_fntend-1-2-fe-s-2), and 5182/5183 were likewise held b... |
| `IRPT_FNTEND-S7` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S19 | none | Disarm act for IRPT_FNTEND-W1-S5 assigned by its disarm_owner: TO-FE-s-5 (slot ~1, next in queue) is amended at the FE-s-3 drain to add the @/* path mapping to portal/tsconfig.json, the solution fi... |
| `IRPT_FNTEND-S8` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S20 | none | Disarm act for IRPT_FNTEND-W1-S6 taken by its disarm_owner at this drain: the vite dev servers left running by the FE-s-2, FE-s-4 and FE-s-8 workers under worktrees already removed were located by... |
| `IRPT_FNTEND-W3-S1` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S21 | none | AnalysisTab.tsx (built per TO-FE-s-6) is not reachable from the running app: TabShell.tsx (FE-s-3, IMPORTED never edited per this order's BOUNDS) fills every tab body with StatusPanel and nothing e... |
| `IRPT_FNTEND-W3-S2` | INERT | GRADUATED | adjudication IRPT_FNTEND-C-S22 | none | TO-FE-s-6's ACT text asserts two fields the shared contracts file does not carry -- AnalysisRequest.inputRevision and ReportSection.parity.passed -- so F6-AC3/F6-AC4 are met by two FE-s-6-LOCAL ext... |
| `IRPT_FNTEND-W4-S1` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S23 | none | FE-s-7's HoldingsTab is built and unit-tested (F7-AC1..AC4 all pass) but is NOT reachable through the real page: TabShell.tsx's holdings body mount still fills with StatusPanel only, TabShell.tsx i... |
| `IRPT_FNTEND-W4-S2` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S24 | none | portal/src/components/CategoryViewTree.tsx is hard-wired to the AUM-domain MdpfCategoryViewsResult contract (fee_taking/advisory axis, Primary/Custom buckets, and a presence rule that DROPS any non... |
| `IRPT_FNTEND-W1-S7` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S25 | none | The row-S7 disarm act's own tsconfig.json edit (required for F5-AC9) REGRESSES the already-terminal FE-s-3 dropdown-class.test.ts (F3-AC7), verified by a controlled A/B; separately, render/performa... |
| `IRPT_FNTEND-S9` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S26 | none | Disarm act for IRPT_FNTEND-W3-S1 and IRPT_FNTEND-W4-S1 assigned by their disarm_owner: the tab shell FE-s-3 built has no mount seam, so the Analysis and Holdings tabs are built and tested but unrea... |
| `IRPT_FNTEND-S10` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S27 | none | Disarm act for IRPT_FNTEND-W1-S7 finding (1) assigned by its disarm_owner: the root tsconfig alias mapping FE-s-5 landed makes FE-s-3's dropdown-class.test.ts per-file mock.module registrations int... |
| `IRPT_FNTEND-S11` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S28 | none | PRD v0.5 @fb5bb6e landed MID-ROUND: it changes candidate F5 (cell FE-s-6, the Analysis tab) to PRODUCE AnalysisRequest's browser request half per docs/research/investor_reporting_ycharts_variants_2... |
| `IRPT_FNTEND-W1-S8` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S29 | none | TO-FE-s-9's own FE-s-8-drain amendment (gate PerformanceDocument's period-in-context page on includeNarrative:true) is satisfied inside this order's grant, but it turns FE-s-4's existing POSITIVE-C... |
| `IRPT_FNTEND-S12` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S30 | none | Disarm act for IRPT_FNTEND-W1-S8 finding (2) assigned by its disarm_owner: the narrative gating FE-s-9 was told to add turns FE-s-4's positive control in __tests__/fe-s-4/analysis-no-narrative.test... |
| `IRPT_FNTEND-S13` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S31 | none | Two worker commits in the WORKSPACE repo carried the portal GITLINK bumped to the worker's own portal-branch commit (FE-s-8 @24c4b211b2 -> 21b17327; FE-s-5 @3ab6275f9f -> e85f6eb8), so origin/CLOUD... |
| `IRPT_FNTEND-W1-S9` | INERT | GRADUATED | adjudication IRPT_FNTEND-C-S32 | none | F10-AC10 required rendering TabShell (and, transitively, AnalysisTab/HoldingsTab) through renderToStaticMarkup; state/hooks.ts's three useSyncExternalStore calls (FE-s-3) were built with only a cli... |
| `IRPT_FNTEND-W1-S10` | INERT | GRADUATED | adjudication IRPT_FNTEND-C-S33 | none | F10-AC8's ui-smoke run for a firm-scoped (--firm 49financial) session prints LOC /market (not /investor-reporting) with rc=0 as the WORKER FACE anticipated ('DID NOT LAND ... a route carrying a que... |
| `IRPT_FNTEND-S14` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S34 | none | FE-s-10 drained (portal DEV 787015e8, workspace eada87592e; the whole Investor Reporting set reads 236 pass, 1 skip, 0 fail on DEV by the issuer's own run). Two worker rows read at the drain: W1-S9... |
| `IRPT_FNTEND-S15` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S35 | none | FE-s-11 reported non-terminal (status blocked) with rows W1-S11 and W1-S12 ARMED, disarm_owner 3.0.0_SA_CVO. The issuer verified both by its own instruments and found a third defect the worker reco... |
| `IRPT_FNTEND-S16` | INERT | DISMISSED_WITH_REASON | adjudication IRPT_FNTEND-C-S36 | none | FE-s-11's second report: the three repairs of the first amendment hold (colour-law 4 of 4, Analysis and Export tabs CLICKED, the print route resolves REFS RESOLVED: 1 of 1, whole set 322 pass 0 fai... |
| `IRPT_FNTEND-W1-S11` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S37 | none | Two FE-s-9 export components (`export/AppliedBranding.tsx`, `export/ReceiptPanel.tsx`) are exported but imported by NOTHING under pages/InvestorReporting/** or portal/src/App.tsx -- confirmed by th... |
| `IRPT_FNTEND-W1-S12` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S38 | none | F11-AC5/AC6/AC7's own named fixtures (fe-s-6-ready.json, fe-s-7-smartx.json, fe-s-9-modal.json) each crash the WHOLE /investor-reporting page with React's 'Maximum update depth exceeded' before any... |
| `IRPT_FNTEND-W1-S13` | INERT | GRADUATED | adjudication IRPT_FNTEND-C-S39 | none | After the issuer's useFirmContext.ts repair (W1-S12) fixed the one-firm infinite loop, F11-AC6's own named fixture (fe-s-7-smartx.json) STILL fails to reach the Holdings tab -- a DIFFERENT, previou... |
| `IRPT_FNTEND-W1-S14` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S40 | none | F11-AC8's amended <expect> text, 'CONSOLE[log]: REFS RESOLVED: 1 of 1', is carried verbatim into the proof_of_spec instance per schema convention and graded by proof-of-spec-check.py as a raw Pytho... |
| `IRPT_FNTEND-S17` | ARMED | GRADUATED | adjudication IRPT_FNTEND-C-S41 | none | FE-s-11 drained in both repos (portal DEV edab15b5, workspace ad959f08ce); eleven of eleven orders complete; the whole Investor Reporting test set reads 322 pass, 1 skip, 0 fail on DEV by the issue... |
| `IRPT_FNTEND-W1-S15` | INERT | NOT-YET-DISPOSITIONED | - | none | TO-FE-s-12's <proof_of_spec> block specifies `phase BUILD`, but org/standards/PROOF_OF_SPEC.schema.json's `phase` enum carries no `BUILD` member -- proof-of-spec-check.py refuses the ordered value... |
| `IRPT_FNTEND-S18` | INERT | NOT-YET-DISPOSITIONED | - | none | Round 2 opened: decomposition v0.2 @430c5fcb4a (seven additive cells on the CTO's seven rulings), ONE issuance @75d2e353a8, COMPLETION_REPORT.round1.json (8 of 8 COVERED). FE-s-12 (the typecheck re... |
| `IRPT_FNTEND-S19` | INERT | NOT-YET-DISPOSITIONED | - | none | FE-s-17 reported non-terminal: seven of nine criteria PASS (the three OFL Lato faces packaged byte-for-byte, hashes 3 of 3, print.css local, stand-in 700<-600 declared, licence present, print route... |
| `IRPT_FNTEND-W2-S7` | INERT | NOT-YET-DISPOSITIONED | - | none | F17-AC6's bar is `EXTERNAL: 0` for font requests to any host other than the dev server's origin; the exercised capture records EXTERNAL: 2 -- both are the PORTAL SHELL's Inter webfont (`src/index.c... |
| `IRPT_FNTEND-W2-S8` | INERT | NOT-YET-DISPOSITIONED | - | none | The cell orders `render/manifest.ts` to gain 'a `fonts` declaration mirroring the manifest (files, weights, stand-ins, not-packaged)', but `RENDER_PACKAGE.fonts` is already consumed as a FLAT STRIN... |
| `IRPT_FNTEND-W1-S16` | INERT | NOT-YET-DISPOSITIONED | - | none | FE-s-13's face orders the two no-route operations RETIRED from InvestorReportingApi (previewExportBundle removed) and says only __tests__/fe-s-1/ needs updating -- but SEVEN test files in FIVE fold... |
| `IRPT_FNTEND-W1-S17` | INERT | NOT-YET-DISPOSITIONED | - | none | Five places where the producer's contract and the consumer's view type do not map 1:1 -- three closed vocabularies lose a value on the way in, one view field could only be filled from a SERVER-ONLY... |
| `IRPT_FNTEND-S20` | ARMED | NOT-YET-DISPOSITIONED | - | none | FE-s-13 (the seam) and FE-s-17 (Lato) are terminal and drained in both repos (portal DEV 8cc43736; workspace ae023bb3d7 + the FE-s-13 drain pending the shared index). MERGED DEV IS RED while each b... |
| `IRPT_FNTEND-W2-S9` | INERT | NOT-YET-DISPOSITIONED | - | none | R1 item 2 orders `fixtures/wire/` copies to come from v1 ("sha256 of the v1 files"), but docs/contracts/investor-reporting/v1/ PUBLISHES NO FIXTURES -- it carries 11 document schemas, responses/ (1... |
| `IRPT_FNTEND-W2-S10` | ARMED | NOT-YET-DISPOSITIONED | - | none | BLOCKING on F14-AC10. Re-basing fixtures/smoke/default.json to v1 DECLARED paths (ordered by R1 item 5, graded by F14-AC16, done) breaks TWO pins on that same file that this order's <paths> does no... |
| `IRPT_FNTEND-W2-S11` | ARMED | NOT-YET-DISPOSITIONED | - | none | The v1 envelope parser is STRICT, but LiveClient still ACCEPTS a body carrying none of `contract_version` / `operation` / `firm_id` -- a PRE-ENVELOPE document -- instead of refusing it, because `__... |
| `IRPT_FNTEND-W2-S12` | INERT | NOT-YET-DISPOSITIONED | - | none | The consumer NARROWS an optional field of the contract: v1's submit-export response marks `status` OPTIONAL (x-response-contract.status_required false) and its `data` is an ExportReceipt, but `Inve... |
| `IRPT_FNTEND-W2-S13` | INERT | NOT-YET-DISPOSITIONED | - | none | The print route was DEAD on the merged tree and the order's own item-5 premise could not be met until it was repaired: `/investor-reporting/print` enters through `export-preview`, which v1 lists as... |
| `IRPT_FNTEND-W2-S14` | INERT | NOT-YET-DISPOSITIONED | - | none | Recorded off-task from this cell's own PNGs: the Holdings tab renders the NO-HANDLER-AT-HEAD refusal as `Failed / IR-REQUEST-FAILED / Retry`, so "this route has no handler at HEAD and the client re... |
| `IRPT_FNTEND-S21` | ARMED | NOT-YET-DISPOSITIONED | - | none | FE-s-14 complete and drained in both repos (portal DEV 84a86c10; workspace ee35a25392): 17 of 17, R1 re-pin to contract v1 (header, envelope parser, producer operation ids, default.json as the publ... |
| `IRPT_FNTEND-S22` | ARMED | NOT-YET-DISPOSITIONED | - | none | Round 2 resumed after the managed wind-down and seated two orders in parallel on fresh worktree pairs: FE-s-15 (slot ~1, port 5181, pair /c/tmp/wk-irpt_fntend-2-5-fe-s-15 plus its portal worktree,... |
| `IRPT_FNTEND-S23` | ARMED | NOT-YET-DISPOSITIONED | - | none | The R2 amendment this seat added to FE-s-15 at the FE-s-14 drain created a dependency edge the FROZEN decomposition v0.2 @430c5fcb4a does not carry: FE-s-16's F16-AC9 ('bun test src/pages/InvestorR... |
| `IRPT_FNTEND-S24` | ARMED | NOT-YET-DISPOSITIONED | - | none | ISSUER AMENDMENT answering a worker REFUSAL that was correct. 0.9.0_WK_IRPT_FNTEND~1 refused F15-AC8 ('a source grep of tabs/analysis/ for inputRevision returns 0 hits') because the criterion is UN... |
| `IRPT_FNTEND-S25` | ARMED | NOT-YET-DISPOSITIONED | - | none | ISSUER AMENDMENT answering a second correct worker REFUSAL. 0.9.0_WK_IRPT_FNTEND~3 refused F16-AC8 because its INVOCATION is stale, not because the code is wrong: the URL 'investor-reporting/print?... |
| `IRPT_FNTEND-S26` | ARMED | NOT-YET-DISPOSITIONED | - | none | THIS SEAT'S OWN SEQUENCING SLIP, recorded because it will surface as a merge conflict at both drains and a successor would otherwise read it as worker error. I created both worktree pairs at worksp... |
| `IRPT_FNTEND-S27` | ARMED | NOT-YET-DISPOSITIONED | - | none | READ OFF-TASK FROM F16-AC8's OWN CAPTURE, by opening the PNG rather than reading the console line the criterion grades on: the served print document contradicts itself about how many accounts are i... |
| `IRPT_FNTEND-W1-S18` | INERT | NOT-YET-DISPOSITIONED | - | none | F15-AC8's second limb (`a source grep of tabs/analysis/ for inputRevision returns 0 hits`) CANNOT be satisfied inside this order's write grant: removing the fallback breaks four assertions in __tes... |
| `IRPT_FNTEND-W1-S19` | INERT | NOT-YET-DISPOSITIONED | - | none | TWO of the composer's eight rows name a wire prefill source v1 does not carry: the COMPARISON CATALOGUE (cell item 4, "the catalogue the wire scope carries") and the PREPARED-FOR / PREPARED-BY / CO... |
| `IRPT_FNTEND-W1-S20` | INERT | NOT-YET-DISPOSITIONED | - | none | The cell requires `report_title` to send `null` when the advisor states no override, but the granted adapter's `toAnalysisGenerateWire` types it `report_title: string` -- and the adapter is READ ON... |
| `IRPT_FNTEND-W1-S21` | INERT | NOT-YET-DISPOSITIONED | - | none | The five job states cannot be read through the typed client at all: `LiveClient.send` returns a response's `data` and DROPS the `status` envelope beside it, and `adapt.ts` maps BOTH wire QUEUED and... |
| `IRPT_FNTEND-W1-S22` | INERT | NOT-YET-DISPOSITIONED | - | none | The seam's request corpus binds `snapshot_id` to the SCOPE FINGERPRINT (`HoldingsSnapshot.scope.resolved_scope_fingerprint`) while the composer sends the SNAPSHOT's own id (`source_set_revision`) -... |
| `IRPT_FNTEND-W1-S23` | INERT | NOT-YET-DISPOSITIONED | - | none | The spawn prompt states the task order file "already reads `<status>pending</status>`"; at the worktree's base commit it reads `<status>blocked</status>`. Recorded, not changed: this worker's flip... |
| `IRPT_FNTEND-W1-S24` | INERT | NOT-YET-DISPOSITIONED | - | none | Retiring `parity.ts` under the widened grant costs a distinction the wire cannot make: v1 publishes ONE support verdict per REPORT (`AnalysisReport.extraction_validation`) and none per SECTION, so... |
| `IRPT_FNTEND-W1-S25` | INERT | NOT-YET-DISPOSITIONED | - | none | The retired revision counter's second half -- "each accepted correction advances the revision by exactly one" -- is NOT a wire fact either: under v1 the PRODUCER issues the next `identity.revision`... |
| `IRPT_FNTEND-W3-S4` | INERT | NOT-YET-DISPOSITIONED | - | none | F16-AC2 names renderToStaticMarkup of the OPEN ExportModal as the instrument, and the cell requires AppliedBranding and ReceiptPanel to mount INSIDE that modal's dark Panel -- but Headless UI v2's... |
| `IRPT_FNTEND-W3-S5` | INERT | NOT-YET-DISPOSITIONED | - | none | v1's submit-export answers the ExportReceipt WHOLE in data (the receipt carries the producer-minted export_ref.export_id) with the ack in status, but the FE-s-13 typed client's submitExport is type... |
| `IRPT_FNTEND-W3-S6` | INERT | NOT-YET-DISPOSITIONED | - | none | The cell says both ExportAnchorSlot mounts in index.tsx pass the tab's real report refs; the REPORTING tab's reference is reachable (that tab identifies its report by ResolvedScope.revision.revisio... |
| `IRPT_FNTEND-W3-S7` | INERT | NOT-YET-DISPOSITIONED | - | none | The cell requires render/narrative/ to read cited_evidence and coverage through the FE-s-13 adapter, but adaptNarrativePacket exposes NEITHER: it hangs evidence off each EVENT and fills it with []... |
| `IRPT_FNTEND-W3-S8` | INERT | NOT-YET-DISPOSITIONED | - | none | F16-AC5 requires the MISSING HISTORY state to name coverage's cutoff, but v1's NarrativePacket coverage object carries NO DATE AT ALL: its four properties are windows_evaluated, windows_covered, mi... |
| `IRPT_FNTEND-W3-S9` | ARMED | NOT-YET-DISPOSITIONED | - | none | F16-AC8 CANNOT PASS AS WRITTEN: its route investor-reporting/print?bundle=fe-s-16-narrative names no ?scope=, and the declared performance route binds that value as its path parameter (GET /api/sco... |
| `IRPT_FNTEND-W3-S10` | ARMED | NOT-YET-DISPOSITIONED | - | none | F16-AC9 (bun test src/pages/InvestorReporting, expect 0 fail) reads 384 pass, 1 skip, 6 FAIL on this branch. The six are exactly the six the task order's own face names as pre-existing and NOT this... |
| `IRPT_FNTEND-W3-S11` | INERT | NOT-YET-DISPOSITIONED | - | none | F16-AC6/AC7 read 'the modal opens on the mounted flow in the ready state', but their invocation carries a single --click Export, which opens the modal and submits nothing: no export exists, so no r... |
| `IRPT_FNTEND-W3-S12` | INERT | NOT-YET-DISPOSITIONED | - | none | The worker face states that TO-FE-s-16 'already reads <status>pending</status>'; the file on this branch reads <status>blocked</status> at line 8. Nothing was changed: the flip this order authorise... |
| `IRPT_FNTEND-S28` | ARMED | NOT-YET-DISPOSITIONED | - | none | THIRD producer move under a consumer cell in one round (S20, S21, now this), and the first one caught BEFORE a cell was seated on it rather than after. Since FE-s-15's re-pin to d9c940244a the coun... |
| `IRPT_FNTEND-S29` | INERT | NOT-YET-DISPOSITIONED | - | none | ISSUER RULING on the cell input 1.0.0_SA_CTO routed in 96062, which explicitly left the sequencing to this seat: F7 renders 'source ages', and under v0.14 an envelope may now legitimately arrive wi... |
| `IRPT_FNTEND-S30` | ARMED | NOT-YET-DISPOSITIONED | - | none | ISSUER CONFIRMATION of IRPT_FNTEND-W1-S33, re-derived with this seat's own instruments rather than taken from the worker's report, because it is the finding of the round and it decides round 3. CON... |
| `IRPT_FNTEND-S31` | ARMED | NOT-YET-DISPOSITIONED | - | none | THIRD criterion of this round cut against a print URL that FE-s-14 made unservable (F16-AC8 first, now F18-AC6). The worker refused it correctly and took a CONTROL with `&tenant=F-49F&scope=fp-49f-... |
| `IRPT_FNTEND-S32` | ARMED | NOT-YET-DISPOSITIONED | - | none | THIS SEAT PATCHED A CRITERION THROUGH A MESSAGE AND THE WORKER IMPLEMENTED IT. In the continue message answering FE-s-18's first report I wrote that I was carrying a standing rule to L10 -- 'a capt... |
| `IRPT_FNTEND-W1-S26` | INERT | NOT-YET-DISPOSITIONED | - | none | gen-wire.ts tests `allOf` BEFORE `type`/`properties`, so a schema carrying BOTH an object body and a JSON Schema CONDITIONAL emits the conditional's rendering INSTEAD of the whole object: regenerat... |
| `IRPT_FNTEND-W1-S27` | INERT | NOT-YET-DISPOSITIONED | - | none | The R3 premise reads `4 stale fixture copies` at producer-fixtures.test.ts:104; the reproduced failure is TWO stale SCHEMA PINS (AnalysisReport, StatusEnvelope) in a different test of the same file... |
| `IRPT_FNTEND-W1-S28` | ARMED | NOT-YET-DISPOSITIONED | - | none | The ordered `add the fourth file name to RENDER_PACKAGE.fonts too` cannot be done inside this order's grant: `__tests__/fe-s-4/manifest.test.ts:216` asserts `RENDER_PACKAGE.fonts.length === 3` and... |
| `IRPT_FNTEND-W1-S29` | INERT | NOT-YET-DISPOSITIONED | - | none | print.css sets font-weight: 600 in NINE rules and declared NO 600 @font-face: those rules matched UP to the 700 face, which was the SemiBold FILE standing in, so 600 text rendered in SemiBold throu... |
| `IRPT_FNTEND-W1-S30` | INERT | NOT-YET-DISPOSITIONED | - | none | The worker face states `FE-s-17's __tests__/fe-s-17/fonts.test.ts is updated for four files and no stand-in` as an accomplished fact. In this worktree it was not: it asserted three files, `['700','... |
| `IRPT_FNTEND-W1-S31` | INERT | NOT-YET-DISPOSITIONED | - | none | The staged Lato-Bold.ttf is NOT recorded in the sources.json of the capture directory it sits in: that file's four entries are Regular, Light, SemiBold and OFL.txt. fonts.manifest.json's per-face `... |
| `IRPT_FNTEND-W1-S32` | INERT | NOT-YET-DISPOSITIONED | - | none | CORRECTION TO THIS WORKER'S OWN ROW IRPT_FNTEND-W1-S29: the count is EIGHT font-weight: 600 rules in print.css, not nine, and the eight line numbers S29 prints are the WORKING-COPY positions after... |
| `IRPT_FNTEND-W1-S33` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE REPORTING AND HOLDINGS TAB BODIES CANNOT MOUNT FROM ANY NETWORK RESPONSE AT HEAD. Both gate on `envelopeFromAvailability(payload.availability).state`, and NO document adapter in contracts/adapt... |
| `IRPT_FNTEND-W1-S34` | INERT | NOT-YET-DISPOSITIONED | - | none | F18-AC3's `no two entries share a file or a hash` is FALSE at this commit and F18-AC3 is refused: the three Holdings captures (AC9 observed, AC10 target, AC11 missing-attribution) are BYTE-IDENTICA... |
| `IRPT_FNTEND-W1-S35` | INERT | NOT-YET-DISPOSITIONED | - | none | One named layout repair -- `the pie labels clip` -- cannot be made under LAYOUT ONLY: the clipping comes from recharts' `outerRadius={100}` and a label callback rendering `name: value` outside the... |
| `IRPT_FNTEND-W1-S36` | INERT | NOT-YET-DISPOSITIONED | - | none | ui-smoke.mjs's landing check compares `window.location.PATHNAME` against the full route STRING, so it prints `<-- DID NOT LAND (auth redirect? bad route?)` on EVERY query-bearing route whether or n... |
| `IRPT_FNTEND-S33` | ARMED | NOT-YET-DISPOSITIONED | - | none | FOURTH producer move of the round, and the one that settles the argument: 58e387b454 landed at 2026-09-11 22:57:36 -0400, FOURTEEN MINUTES AFTER I cut FE-s-18's worktree at 22:43:10 and while its w... |
| `IRPT_FNTEND-S34` | INERT | NOT-YET-DISPOSITIONED | - | none | DISARM SWEEP at the round-2 drain end, one line of evidence per row, nothing swept in bulk. DISARMED: S20, S21, S22, S23, S24, S25, S26, S31, S32, W3-S9, W3-S10, W2-S3, W2-S6 -- thirteen rows whose... |
| `IRPT_FNTEND-S35` | INERT | NOT-YET-DISPOSITIONED | - | none | CORRECTION TO MY OWN ROW IRPT_FNTEND-S33, filed before the drain-end read so the CTO does not cite a wrong number into a round-3 cut. S33 states '3 schema pins stale against 58e387b454'. THE REAL F... |
| `IRPT_FNTEND-W3-S13` | INERT | NOT-YET-DISPOSITIONED | - | none | TO-FE-s-23's stated premise that round 2's seven instances are HONESTLY ALIGNED is FALSE: 2 of the 7 carry a recorded invocation that is not its criterion's invocation modulo placeholder expansion... |
| `IRPT_FNTEND-W3-S14` | ARMED | NOT-YET-DISPOSITIONED | - | none | The cell's two constraints -- 'A mismatch is a VIOLATION' and 'THIS LIMB MUST NOT BREAK THE EXISTING CORPUS' -- are JOINTLY UNSATISFIABLE at a default-ENFORCE setting, measured before the limb was... |
| `IRPT_FNTEND-W3-S15` | INERT | NOT-YET-DISPOSITIONED | - | none | CORRECTION to TO-FE-s-23's own <preflight> instrument fact (2) and to the same claim repeated in the F23-AC6 clause and in the spawn message: `.tools/proof-of-spec-check.py --help` does NOT return... |
| `IRPT_FNTEND-W3-S16` | INERT | NOT-YET-DISPOSITIONED | - | none | DISCLOSED ACT: this worker added ONE element -- <placeholders>WS</placeholders> -- to its OWN task order file, IRPT_FNTEND.TO-FE-s-23, which the order's BOUNDS grant covers ('the <paths> block belo... |
| `IRPT_FNTEND-W4-S3` | INERT | NOT-YET-DISPOSITIONED | - | none | F24-AC3's bar as written -- 'a source scan of __tests__/fe-s-4/manifest.test.ts for a literal length comparison against a digit returns zero hits' -- cannot be met UNSCOPED: that file already carri... |
| `IRPT_FNTEND-W4-S4` | INERT | NOT-YET-DISPOSITIONED | - | none | TO-FE-s-24's BOUNDS order this worker to mint rows 'starting at IRPT_FNTEND-W4-S1 (the W4 coordinate has no round-3 rows yet; if the file carries no W4 sequence, yours opens it)'. Followed literall... |
| `IRPT_FNTEND-S36` | INERT | NOT-YET-DISPOSITIONED | - | none | TWO ISSUER MIS-MEASUREMENTS IN THE ROUND-3 CUT, both caught by the workers reading the world rather than my face. (1) I told FE-s-24 to mint surprise rows from IRPT_FNTEND-W4-S1; the row gate alloc... |
| `IRPT_FNTEND-S37` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE CELL'S PREMISE WAS FALSE AND THE WORKER REFUSED TO SMOOTH IT. FE-s-23's face asserted 'round 2's instances are honestly aligned and must stay VALID'. They are aligned in 5 of 7. TWO REAL DIVERG... |
| `IRPT_FNTEND-S38` | ARMED | NOT-YET-DISPOSITIONED | - | none | ISSUER RULINGS on the two acts 0.9.0_WK_IRPT_FNTEND~3 disclosed rather than assumed. (1) W3-S14, the OPT-IN enforcement split: ACCEPTED. The cell's two constraints -- 'a mismatch is a VIOLATION' an... |
| `IRPT_FNTEND-W2-S15` | ARMED | NOT-YET-DISPOSITIONED | - | none | BLOCKING on the carried half of IRPT_FNTEND-W2-S10. FE-s-20's cell orders `fixtures/smoke/default.json`'s two broken pins resolved 'in the same idiom' -- the corpus binds the CONTENT it replays, no... |
| `IRPT_FNTEND-W2-S16` | INERT | NOT-YET-DISPOSITIONED | - | none | OBSERVATION, disclosed because it is the one thing the new content pin cannot see. FE-s-20 replaces the schema DIGEST table with `contracts/wire/consumed.ts`: the operation ids, route keys and requ... |
| `IRPT_FNTEND-S39` | INERT | NOT-YET-DISPOSITIONED | - | none | THE MEASUREMENT THAT SETTLES THE BYTE-PIN QUESTION, and it is worse than the four-instance argument that produced the ruling. The fourth producer move -- 58e387b454, the one that reddened the whole... |
| `IRPT_FNTEND-S40` | ARMED | NOT-YET-DISPOSITIONED | - | none | CARRIED, NOT CLOSED: W2-S10's producer-side half is outside EVERY portal grant and this seat cannot reach it either. 0.9.0_WK_IRPT_FNTEND~2 refused it correctly as BLOCKING row W2-S15. The consumer... |
| `IRPT_FNTEND-S41` | ARMED | NOT-YET-DISPOSITIONED | - | none | I CUT F19-AC8's BAR ON A PREDICTION AND THE WORKER MEASURED IT FALSE. The criterion read `0 fail` because I wrote into its own prose that F18-AC3's capture collision 'is expected to CLEAR when this... |
| `IRPT_FNTEND-S42` | ARMED | NOT-YET-DISPOSITIONED | - | none | TWO FINDINGS FROM FE-s-19 THAT EXPLAIN ROUND 2's BLINDNESS AT THE INSTRUMENT LEVEL, and one that blocks F18-AC3 permanently until a fixture cell is cut. (a) THE PORTAL INSTALLS NO DOM TEST ENVIRONM... |
| `IRPT_FNTEND-W1-S37` | INERT | NOT-YET-DISPOSITIONED | - | none | TO-FE-s-19's cell text locates the tab-body gate at `tabs/TabShell.tsx:133`, `:148` and `:150`. At the ordered bytes NONE of those three lines gates a tab body: :133 and :150 feed the selection STO... |
| `IRPT_FNTEND-W1-S38` | ARMED | NOT-YET-DISPOSITIONED | - | none | F19-AC8 CANNOT reach `0 fail` from this cell and its premise is falsified twice over. The order predicts F18-AC3's capture collision 'is expected to CLEAR when this cell lands'; F18-AC3 grades ELEV... |
| `IRPT_FNTEND-W1-S39` | ARMED | NOT-YET-DISPOSITIONED | - | none | W2-S11 is only PARTLY closed by this cell, and the remainder is refused rather than silently carried. F19-AC6's three bodies each carry TWO of the three envelope identifiers, so `isEnvelopeShaped`... |
| `IRPT_FNTEND-W1-S40` | INERT | NOT-YET-DISPOSITIONED | - | none | A mid-order message told this worker 'Re-read the criterion from your order file -- the file is authority, not this message', naming commit b0dbbb7a45 as where F19-AC8's bar was corrected from `0 f... |
| `IRPT_FNTEND-S43` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE FIX I DESIGNED FOR S31 HAS A HOLE AND A WORKER FELL INTO IT CORRECTLY. Round 3's spawn prompts say 'your specification is the FILE, not this message' -- which is right, and INCOMPLETE: it does... |
| `IRPT_FNTEND-S44` | ARMED | NOT-YET-DISPOSITIONED | - | none | FE-s-18 CANNOT CLOSE IN ROUND 3 AS CUT, and I am naming it now rather than discovering it at the round close. All four seated round-3 cells are COMPLETE and drained (FE-s-19, 20, 23, 24) and FE-s-2... |
| `IRPT_FNTEND-S45` | ARMED | NOT-YET-DISPOSITIONED | - | none | I FIXED THE INSTANCE AND LEFT THE CLASS -- THIRD TIME TONIGHT, AND THIS TIME I HAD ALREADY WRITTEN THE LESSON DOWN. When row S41 corrected F19-AC8's `0 fail` bar I corrected ONE criterion. THREE fa... |
| `IRPT_FNTEND-S46` | INERT | NOT-YET-DISPOSITIONED | - | none | CORRECTION TO MY OWN ROW S44, MEASURED FALSE BY 0.9.0_WK_IRPT_FNTEND~2. S44 wrote that 'without that limb the scoped rule would have ADMITTED this collision as legitimate.' It would NOT have. The t... |
| `IRPT_FNTEND-W2-S17` | INERT | NOT-YET-DISPOSITIONED | - | none | F22-AC8 CANNOT PASS AS WRITTEN AND THE REMAINING FAILURE IS NOT THIS CELL'S. The order asks the whole Investor Reporting set for `0 fail`; measured on this branch with both of this cell's new files... |
| `IRPT_FNTEND-W2-S18` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE THIRD LIMB S44 ASKED FOR IS BUILT, AND THE TWO FINDINGS TURN OUT TO BE INDEPENDENT -- which corrects one clause of S44 and sharpens the CTO's open question rather than answering it. S44 wrote '... |
| `IRPT_FNTEND-W2-S19` | INERT | NOT-YET-DISPOSITIONED | - | none | W2-S17'S BLOCKER WAS REMOVED BY AN ISSUER AMENDMENT AFTER THE ROW LANDED, AND THE CHANNEL IS APPEND-ONLY -- so this row carries the new measurement rather than W2-S17 being edited. 2.0.0_SA_COO~F c... |
| `IRPT_FNTEND-W1-S41` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE TASK ORDER'S 'PRINTED NINE-STATE ENUM' IS THE PRODUCER'S NINE, AND THE VIEW HAS A DIFFERENT NINE -- so the ordered subtraction yields two different fours depending on which plane you take it ov... |
| `IRPT_FNTEND-W1-S42` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE FIELD THE CONTRACT CLAUSE GOVERNS IS NOT THE FIELD THE AGE IS COMPUTED FROM. The order quotes the state-conditional rule for `StatusEnvelope.business_date` and then names `formatSourceAge(sourc... |
| `IRPT_FNTEND-W1-S43` | ARMED | NOT-YET-DISPOSITIONED | - | none | F21-AC5 ASKS FOR A DISTINCTION THE ADAPTER HAS ALREADY DESTROYED BEFORE ANY PANEL SEES IT. `adaptStatusEnvelope` carries the source dates through `?? null`, so an ABSENT `business_date` and an expl... |
| `IRPT_FNTEND-W1-S44` | INERT | NOT-YET-DISPOSITIONED | - | none | F21-AC7 REFUSED, AS THE ORDER INSTRUCTED. The Investor Reporting suite reads 1 fail against AC7's bar of `0 fail`, and the failure is F18-AC3's capture-hash collision -- pre-existing, not mine, sel... |
| `IRPT_FNTEND-W1-S45` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE SUITE'S FAILURE COUNT IS PORT-CONDITIONAL, AND NOTHING IN THE RUN SAYS SO. `bun test src/pages/InvestorReporting` reads 3 fail with no vite dev server on port 5181 and 1 fail with one -- the sa... |
| `IRPT_FNTEND-W1-S46` | ARMED | NOT-YET-DISPOSITIONED | - | none | THE CELL SAYS 'THE PANELS THAT CONSUME IT' AND THE GRANT REACHES ONE OF THREE. `formatSourceAge` has three consumers; two of them -- tabs/analysis/StageDisplay.tsx and tabs/analysis/VariantSelector... |
| `IRPT_FNTEND-W1-S47` | INERT | NOT-YET-DISPOSITIONED | - | none | W1-S44 IS SUPERSEDED AND I CANNOT EDIT IT, SO THIS ROW CARRIES THE CORRECTION. I filed W1-S44 refusing F21-AC7 against a bar of `0 fail`; the issuer then corrected that bar to `1 fail` with a name... |
| `IRPT_FNTEND-W1-S48` | ARMED | NOT-YET-DISPOSITIONED | - | none | I FLIPPED A SHARED APPEND-ONLY CHANNEL FROM LF TO CRLF AND TURNED A 140-LINE APPEND INTO A 3618-LINE WHOLE-FILE REWRITE. My own defect, caught by reading the commit's diffstat rather than by any ga... |
| `IRPT_FNTEND-S47` | ARMED | NOT-YET-DISPOSITIONED | - | none | MY OWN CHANNEL UNION RESOLVER RE-RENDERS EVERY ROW'S LINE ENDING, and I only looked because 0.9.0_WK_IRPT_FNTEND~1 disclosed the same class in its own commit (W1-S48: a 140-line append whose diffst... |
| `IRPT_FNTEND-S48` | ARMED | NOT-YET-DISPOSITIONED | - | none | ROUND 3 IS DRAINED: all SIX cells COMPLETE (FE-s-19, 20, 21, 22, 23, 24), every worktree pair torn down, zero branches in either repo, 91 rows. FE-s-18 remains CARRIED at pending and is the round's... |
| `IRPT_FNTEND-S49` | ARMED | NOT-YET-DISPOSITIONED | - | none | ANDREW-DIRECT STOP, VERBATIM AND ENTIRE: "Everyone doing backend needs to pause while we figure this out" -- spoken at the 4.0.0_SA_CRO~D terminal ~16:1xZ 2026-09-12, relayed as 96143 by 4.0.0_SA_C... |
| `IRPT_FNTEND-S50` | ARMED | NOT-YET-DISPOSITIONED | - | none | ANDREW'S ~16:2xZ CLARIFICATION MOVED THE PAUSE'S CRITERION from the word "backend" to PROJECTS ACTIVELY BUILDING DATA PIPELINES / DATA STRUCTURES, reason FORWARD-CONTRADICTION. Two instruments were... |
| `IRPT_FNTEND-S51` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-assets`; `smartx/account/{uuid}/`; `smartx/allocation/{uuid}/`; `smartx/model/{uuid}/` | THE FIRST TWO RATIFIED CARDS OF THE CENSUS DO NOT CONTRADICT ROUND 4 ON THE PLANE THEY GOVERN -- 0 of 14 investor-reporting wire contracts carry ANY storage-plane surface, detector FIRES on a posit... |
| `IRPT_FNTEND-S52` | ARMED | NOT-YET-DISPOSITIONED | - | `opal-data-assets` | SELF-CORRECTION, LOAD-BEARING: row S51's headline "0 of 14 wire contract files carry ANY storage-plane surface" IS FALSE. The true figure is 4 SURFACES IN 3 OF 14 FILES -- AnalysisReport.ts:54 and... |

---

## 6. WHAT THIS FILE DOES NOT CLAIM

- **It does not claim any row is correct.** It transcribes what the channel says; a DISMISSED row may
  have been dismissed wrongly, and `C-S85` is this seat's own standing record that round 1's
  consolidation was never auditable item by item.
- **It does not grade the three CONTRADICTS.** Grading them is row #8's act and the CRO's; supplying the
  row state is mine. Where s.3 says a contradiction matches a row's shape, that is a statement about the
  channel, not a verdict on the doctrine.
- **It re-measures nothing on the live plane.** Every `s3://` string here is a quotation from a row, not
  an object this seat confirmed exists today. The YCharts objects in s.3.3 were live when the row was
  written; freshness is not claimed.
- **The four wire-contract lines in s.4 are a TYPE reading, not a runtime one.** `storage_bucket: string`
  names no bucket. `ExportReceipt.ts:22 server_only: true` and `:38 vendor_signed_url_exposed: false` are
  LITERAL TYPES -- declarations, not states. This seat has not verified the runtime honours either, and
  says so rather than offering them as mitigation.
- **Column 4 is extraction, not judgment.** A row that discusses a storage surface without naming one in
  the matched fields will read `none`. The sweep is total over the five text fields plus grounding
  evidence; it is not a reading of every row's intent.
- **It does not claim the 117 + 97 undispositioned rows contain nothing relevant.** They are open, and 15
  of the 28 IRPT_BCKEND storage-plane rows are among them.
- **The disposition semantics were inferred from the data, not from a schema this seat re-read.**
  `disposition` on an investigation row is its intake value; the operative disposition is the
  adjudication row's. If that reading is wrong, s.0's correction is wrong with it, and the raw counts in
  s.1 stand regardless.

---

**Push state:** LOCAL. This seat does not push (CLOUD cadence is `0.0.0_AB_MSTR`'s on Andrew's word).
**Instrument:** stdlib `json` + `re` over the nine channel files at HEAD, plus four `sed -n` reads in the
`portal/` gitlink, this turn.
