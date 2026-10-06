# 4.0.0_SA_CRO~H -- Opal advised-household count, firm by firm (49F / INF / COT)

**archetype:** EXPLORE
**secondary_archetypes:** TRACE

Session: 2026-10-06 17:31Z -> 18:24Z. Lane `~H` (no `~H` folder exists; logged under the base CRO folder per /log Step 0).

## Andrew-direct (verbatim, Claude Code terminal, 2026-10-06 ~17:35Z-18:10Z)

1. "I need you to do a little research project for me. What I need to know, is how many households are advised by
   Opal. Firm by firm, what that looks like is the following: 1.) For 49 Financial, we are going to be looking in the
   0824 schwab master for all unique active "relationships" ( I believe they use relationship terminology, but they
   may also use "clients", please confirm). 2.) For Inflection, we are going to be looking for "households" that are
   invested in an Opal model. 3.) For Cottonwood, we are going to be looking for all "Relationships" in the
   cottonwood black diamond that are invested in an Opal Model. I think the easiest way to do this across the board
   may be going through the IRPT "Holdings" Tab somehow, because we have all the firm clients being aggregated there
   with their model holdings which in theory should be the shortest distance to the answer for Inflection and
   Cottonwood. For 49 Financial I think you can just go straight to opal-data-assets/schwab/0824/silver and check for
   either unique relationships or clients depending on whatever that terminiology is"
2. "COre satellite are opal, but i dont know what passive is"
3. "if there is an opal model or opal asset in constituent sleeves in eithe rof those things, then yes, it is an opal
   model for this purpose"
4. "Also more important than that is the logic that surrounds the taxpayer id or whatever identification info we have
   from the last good FAM file from schwab. I dont think we can go solely off taxpayer ID because there may be husband
   wife combos who have accounts in different names but still comprise one household. let's come up with a way to
   corroborate this using the info we have from schwab silver october 5 in the 0824 master as well as the last good
   FAM table"
5. "that works /log your work here"

Scope: one-off research for Andrew; no other seat's work changes, so no CTO line is owed.

## Results (claim: measured, read-only against live S3 on 2026-10-06)

| Firm | Unit | Count | Source (as-of) |
|---|---|---|---|
| 49 Financial | household (recommended rule T1) | **3,432** | `s3://opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-05/` + FAM `s3://opal-data-assets/schwab/08335338/silver/fact_fam/date=2026-08-10/` |
| Inflection | household with >=1 account in an Opal model | **265** of 294 | `s3://opal-data-inf/silver/api_dims/accounts_v2/snapshot_date=2026-10-06/` (`model_name`, `household_id`) |
| Cottonwood | relationship with >=1 account in an Opal or Core/Satellite strategy | **196** of 220 | `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_allocations/date=2026-10-05/` (`Account Strategy Name`, `Relationship ID`, '0' = no relationship) |

Total: about 3,893 households.

### Findings
- **Schwab 0824 terminology:** no `relationship` or `client` column in any of the 19 silver tables under
  `schwab/08242234/silver/`. The household grouping is Schwab's FAM feed, which the 0824 master does NOT carry
  (bronze feeds: acc, rld, rlu, rlw, rly, rps, rtu, rty, sec, tcf, tcfx, tnn, trn, uln, ult, upn, upt). FAM rides
  master 08335338; last partition 2026-08-10.
- **FAM household key = the account's own TIN** on 7,067 of 7,067 open 0824 accounts present in FAM (0 households
  with >1 TIN). FAM is therefore a per-taxpayer grouping and cannot join spouses. This is also the basis of
  `gold/advi/dimensions/dim_relationship` (a01_dim_relationship.py), so the IRPT 49F directory's relationship count
  (4,227 active) carries the same per-taxpayer grain.
- **IRPT Holdings/directory is not the shortest path:** `investor-reporting/directory/<date>/directory.json` in each
  firm bucket lists households/relationships with NO model field; model membership was read from the source tables
  the directory is built from (`data/assets/scripts/gold/investor_reporting/directory_runner.py`).
- **INF:** the 29 non-counted households hold only IWM (Inflection Wealth Management) models.
- **COT:** Core | Satellite adds 15 relationships to the 181 Opal-named; "Passive" (Passive 50/60/70/80; 13 accounts,
  10 relationships, `is_opal=False` in `fact_model_definition`, index funds/ETFs) adds 0 because every Passive
  relationship already holds an Opal or Core/Satellite account. Cross-check against `fact_model_assignment`
  (2026-10-06): same 181 Opal-named relationships; 2 accounts disagree between the two strategy sources.

### 49F household method (T1, recommended)
Node = TIN over 7,474 open 0824 accounts (4,411 distinct TINs after stripping dashes). Two TINs join when the
2026-10-05 `fact_acc` evidence agrees: same normalized mailing address (line1+line2+ZIP5) plus a second signal
(surname, email or phone), or a joint-title (`&`) co-owner matched by first+last name and ZIP. Any address/email/phone
shared by >6 TINs is a hub and links nothing (8 / 5 / 4 excluded).

| Rule | Households |
|---|---|
| T0 TIN only (FAM logic) | 4,411 |
| T1 + STRONG (address + second signal, or joint title) | **3,432** |
| T2 + MEDIUM (email/phone + surname, no address) | 3,398 |
| T3 + address-only | 3,261 |

Pair links: STRONG 1,189 / MEDIUM 48 / WEAK 204; top evidence addr+surname 737, addr+email+phone+surname 128.
Risks: adult children at a parent's address merge in; 15 T1 households have >=5 TINs (all single-address); 66 mix
IND with TRUST/ORG.

## Current State
- Answer delivered to Andrew in-session; Andrew accepted the method ("that works").
- Working files are in the session scratchpad ONLY (not in the repo; the review CSV holds PII and must not be
  committed): `...\scratchpad\hh49.py` (T0-T3 build), `count.py` (INF/COT/49F counts), `fam_probe.py` (FAM key test),
  and `hh\hh49_T1_review.csv` (every merged T1 household, 3,208 account rows, for spot checks). The scratchpad is
  session-scoped and will not survive this session.
- No code, pipeline, infra or served artifact changed.

## Blockers
None.

## Next Steps
1. **[4.0.0_SA_CRO~H]** If Andrew wants the T1 count repeatable, persist `hh49.py` (no PII inside it) under
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/` on his word.
2. **[Andrew]** Spot-check the 15 households with >=5 TINs in the review CSV before quoting 3,432 externally.
3. Open item, owner unassigned: the FAM feed has been stale since 2026-08-10 (dim_relationship rows read `fam-carried`).

## MCP Traffic
Inbox empty at load; 0 messages sent or received. Watcher armed at load and re-armed once on expiry.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-which | FAIL | "where does the IRPT Holdings tab get its data" matched no curated rule (top score 0.34) |
| comp-find | WARN | rail refused a piped census; switched to native Grep |
| rail (`aws s3 ls`) | WARN | gated as a freshness/routing question; re-run with `# rail-checked:` because the raw listing was the question |
| python + boto3/pandas (scratchpad) | PASS | all counts measured from live S3 parquet/JSON |

- What worked: native Grep from the portal client (`investor-reporting.ts`) to the Lambda (`holdings/snapshot.py`,
  `directory/handler.py`) to the directory runner, then straight to the source tables.
- What failed: comp-which has no rule for "which table carries a firm's household/model membership".
- Gap found: no comp-tool answers "count households per firm"; the FAM-key == TIN fact is not recorded on
  dim_relationship's docstring (it says "household key", which reads as a spouse-joining grouping).
