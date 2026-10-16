# TO IRPT_DASHBD.TO-DB-f-601 -- the FWD-3 THREAD READ: where the asset-class gold table stands (built, applied, served), whether the served series carries class data, what the portal already holds for asset classes, the hops from gold to the Performance tab with an owner and a risk class each, and a proposed served shape; a read, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-601</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~601</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the parallelization ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, Move 2: "`~F2`: IRPT_DASHBD FWD-3 per the PRD's surface row S09 (gold `account_class_daily`, classes sum to the account)"), on Andrew's go | **Rows:** IRPT_DASHBD-D2-W601-S<k> | **Decomp cell:** `DB-f-601` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R119_F.md`) | **outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-601` (branch `wk-IRPT_DASHBD-601`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~601/`. Never push; never commit the workspace `portal` gitlink (you have no portal work). This is a READ of repository files and git history: no AWS call of any kind, no network, no vendor call, no secret read. Any real client, household or account id and any client figure is never written in the repo, a row or your report.

**Why.** FWD-3 reads: "A person sees how each asset class performed over the window and how the mix moved between two dates, in Opal's canonical classes. ACCEPT: a person says in one sentence which class drove the window and how the mix moved, without reading a table; the classes add up to the account; unclassified holdings show as their own class and are never folded away" (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, FWD-3 and the surface row S09). Nobody has started it. What the issuer measured at the cut: the gold table `account_class_daily` has a contract (`org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`, columns `firm`, `account_id`, `business_date`, `asset_class` (cash, fixed_income, equity, structured, alternatives, commodities, unclassified), `market_value_eod`, `class_return_daily` (the class's CONTRIBUTION to the account's daily total return), `method_version`, `coverage`), a producer (`data/assets/scripts/gold/irpt_reporting/account_class_daily.py`), and a prepared release (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~19/NEVER_WIDEN_PACKET_ACCOUNT_CLASS_DAILY_RELEASE.md` with a CTO half and a COO half beside it) whose contract note says "No object of this table exists in any bucket"; the `reporting-gold` lambda handler names the table; the publisher's comment (`infra/aws/lambda/investor-reporting/reporting-publish/publisher.py`, line 6) says the class keys are ABSENT from the served series because the table did not exist in round 1; the portal holds an asset-class vocabulary and order (`portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts`: Cash, Fixed Income, Equity, Structured, Alternatives, Commodities, then Unclassified; Andrew's order). This cell finds out exactly where the thread stands and what is missing between the gold table and a Performance-tab section.

**The cell (`DB-f-601`).**
1. **The gold table.** Read the contract, the producer, the three release documents (`NEVER_WIDEN_PACKET_ACCOUNT_CLASS_DAILY_RELEASE.md`, the CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ACCOUNT_CLASS_DAILY_RELEASE_CTO_HALF.md`, the COO half `.../2.0.0_SA_COO~D2/NEVER_WIDEN_ACCOUNT_CLASS_DAILY_RELEASE_COO_HALF.md`) and the `reporting-gold` handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`): is the table built (yes: a producer and tests), are both halves of the release signed, and is there any record that it was APPLIED and written (a deploy-ledger entry under `org/critical_paths/` naming it; a later record or packet of `~D2` stating live gold; use `comp-find --files '<term>' <folder> --limit 20`, never `head` a census). Answer `applied` (true or false) with words and a claim; where only the cloud could answer, the claim is `absent` and the words say what live read would settle it and who owns it (no AWS call by you).
2. **The producer.** Record the producer file and the line of its asset-class mapping (the class source: the `etf-classifications` table), how `unclassified` arises, and the sum rule (the classes of one account-day sum to the account's value).
3. **The served series.** Read `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` and the publisher (`reporting-publish/publisher.py`, `handler.py`): does the served series or manifest carry any class key today (`carries_class_keys` true or false, with the line), and what would a per-class window read need: a new file, or new keys in `series`.
4. **The route.** Read `infra/aws/lambda/investor-reporting/reporting/entry.py` (the `which` values of the account route and how the summary and the filled-report routes are added) and say, in words, the smallest route change that would let the page read a class document for one account (cite the line that decides the `which` set).
5. **The portal's reuse.** Read `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts` and say what can be imported unchanged (the class type, order, colors) and what the Performance tab holds today for classes (read `portal/src/pages/InvestorReporting/tabs/reporting/` file names; do not read client data). Cite the file and the line that holds the class order.
6. **The hops.** List the hops that carry one account's class-window figures from gold to a Performance-tab section, in order, each with: `hop` (1, 2, 3 ...), `what` (words), `owner` (a serial or workstream from the files: `2.0.0_SA_COO~D2` for the contract and gold, `2.0.0_SA_COO~S2` or `2.0.0_SA_COO~P2` for the route and publisher, an AE seat for an apply, `2.0.0_SA_COO~F2` for the portal; where none can be named write `UNOWNED`), `risk` (`LOCAL`, `SERVED` or `WORLD` by the issuer's rule: a code or test change is LOCAL; a served data path or a PROD promotion is SERVED; a deploy, a grant, a key or a schedule is WORLD) and `exists_today` (true or false). At least 4 hops; the first is the gold table and the last is the portal section.
7. **A proposed served shape.** One proposal for what the page reads: a document per account with, per business date and per class, `market_value_eod` and `class_return_daily` aligned by index like the series (cite the series contract's convention), the classes in the enum order, a `coverage` per day. State the field names as a list and the words of why this shape lets the page compute a window's per-class contribution and the mix at two dates with no server work.
8. **Record** `RD_FWD3_THREAD_R119.json` in your folder with EXACTLY these fields: `as_of` (ISO date of the read); `gold_table` {`applied`, `words`, `claim`}; `producer` {`file`, `line`, `words`, `claim`}; `series_contract` {`carries_class_keys`, `words`, `claim`}; `served_path` {`file`, `line`, `words`, `claim`}; `portal_reuse` {`file`, `line`, `words`, `claim`}; `proposed_shape` {`words`, `fields` (a non-empty list of field names)}; `hops` (the list of step 6); `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Every `claim` is one of `measured` (you read the line), `inferred`, `held`, `absent` (not found or only the cloud could say, with the reason in `words`; never invented). A `file` is an existing repo path with an INTEGER `line` whose text holds the thing the record says it holds (the checker reads that line: the producer line must hold `account_class_daily`, `class_return_daily` or `asset_class`; the served-path line `manifest`, `series`, `summary`, `route`, `publish` or `class`; the portal-reuse line `asset`, `class`, `order` or `color`). No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `path_template` field.

<criterion id="DBF119-2-AC1" cell_refs="DB-f-601"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r119/p119_fwd3.py" . DBF119-2-AC1</invocation><expect>DBF119-2-AC1 PASS</expect></criterion>
`DBF119-2-AC1` -- `RD_FWD3_THREAD_R119.json` has exactly the form of step 8; each cited file exists and each cited line holds the token class its field names; `hops` has at least 4 entries numbered from 1, each with an owner, a risk class in the set and a boolean `exists_today`; `gold_table` carries a boolean `applied` and words; every claim is in the four-word set; the reads block is all zero, the four flags are false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF119-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, every contract, the packets, the portal, the issuer's check.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call (the gold, the publisher and the route are read from their code and records, not from the cloud); no network. Where only the cloud could answer a question, the answer is `absent` with that reason, never a guess.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a thing is not found, the record says `absent` and what you searched; a zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W601-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~601/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-601.read-fwd3-thread-class-gold-served-path-portal-reuse-hops-owners.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R119_F.md</decomp_doc> round 119, workstream ~F2 (F-SHIP), cell `DB-f-601`.
<owned_cells>DB-f-601</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF119-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~601/IRPT_DASHBD.TO-DB-f-601.read-fwd3-thread-class-gold-served-path-portal-reuse-hops-owners.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF119-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether the gold table is applied (and the evidence or the reason it is `absent`); whether the served series carries class keys; the smallest route change; what the portal can reuse; the hops in order with owner, risk and `exists_today`; the proposed shape's field names; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the cell reads the route's code.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF119-2-AC1 FAILS at base (no record) and the record form is exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
