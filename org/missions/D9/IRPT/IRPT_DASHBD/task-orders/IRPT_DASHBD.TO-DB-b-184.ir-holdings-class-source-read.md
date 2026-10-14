# TO IRPT_DASHBD.TO-DB-b-184 -- READ where the Inflection client's Investor Reporting holdings page gets a position's asset class (FDRXX's class), and whether it needs its own cash rule; read only

<to_id>IRPT_DASHBD.TO-DB-b-184</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~149</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>98</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7383 ("a read of where the Inflection client's IR Holdings gets FDRXX's class; if it is a separate copy, one rule there under its own pair ... Andrew's smoke item closes only on that page reading CASH.") | **Rows:** IRPT_DASHBD-D2-W149-S<k> | **Decomp cell:** `DB-b-184` (decomposition section 100) | **outcome_ref:** FWD-8 class label, FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-149` (branch `wk-IRPT_DASHBD-149`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~149/`.

**What is known.** Andrew's smoke: "FDRXX should be listed as a 'CASH' tagged asset, not Fixed Income", seen on an Inflection client's Opal report (the Investor Reporting holdings view). The gold ETF classifier (`data/black_diamond/scripts/gold/lib/etf_classifier.py`) now carries a rule: a canonical row whose `sub_asset_class` (trimmed, lower-cased) is `cash` takes the class `cash`; it is committed (`e340e07f4e`) and about to be released to `s3://opal-data-bd/code/gold/lib/etf_classifier.py` for the Black Diamond gold chain (Advisor Intelligence consumers: D_03, D_04, C_06, the silver asset dim). What is NOT established is whether the Investor Reporting (IR) holdings page reads a class that this classifier produces. The COO half of the signed pair says the Cottonwood copy, the partners Lambda's classifier and "the Investor Reporting holdings snapshot path" are NOT covered by it.

**The cell (`DB-b-184`): a READ. Nothing is changed, deployed or written.**
1. **Trace backward from the page.** Start at the portal's Investor Reporting holdings view for a firm's client (find it with `comp-cluster --list` and `comp-cluster <Page> --json`, `comp-find --files` with a bounded `--limit`, and `comp-read <path> --for "<question>"`; never a blind recursive grep). For the field the page shows as a position's asset class, name each hop to its source: the component, the hook or API client, the route, the Lambda handler, and the stored object or table it reads. Each hop is `{layer, file, line, what}` in `hops` (3 or more; the last hop is where the class is read from storage or assigned).
2. **Find the assignment.** Name the ONE site where the class value is assigned or first read as a class (`class_assigned_at`: `file`, `line`, `rule` in words, and `keyed_on` one of `canonical_row_asset_class` (returns the canonical table's row), `ticker_list`, `name`, `sub_asset_class`, `other`). Decide, from the code and imports and not by guess, whether that site imports or copies the gold ETF classifier (`shares_code_with_bd_gold_classifier`) and whether it reads the same canonical table `etf-classifications` (`reads_same_canonical_table`). A copy that has drifted from the gold classifier is a finding: say how, in `other_readers_of_that_assignment` or a row.
3. **Decide whether it needs its own rule.** `needs_its_own_rule` is true when the page's class does NOT come from output the gold classifier release will change. If true: `proposed_rule` {`words` (the rule in one or two sentences), `keyed_on` "sub_asset_class" (never a ticker list), `ticker_list_used` false, `where` (file and function)}. If false: `why_no_rule_needed` in words, naming the evidence. A rule you propose is NOT written by you.
4. **Say what the page shows for a money-market fund TODAY, as far as a read can.** `served_class_of_a_money_market_fund_today` is the class string the page's stored source holds for a Cash-typed fund, and `served_class_read_from` names where you read it (a stored served object read by S3 GET and LIST only, or a test fixture or a source line). If you can establish it only from code, say `NOT_ESTABLISHED` with the reason in `served_class_read_from`. Never print a ticker, an account id, a name or a figure: counts and words only.
5. **Record** `IR_HOLDINGS_CLASS_SOURCE.json` in your folder with exactly: `hops`; `class_assigned_at`; `shares_code_with_bd_gold_classifier`; `reads_same_canonical_table`; `needs_its_own_rule`; `proposed_rule` (when true) or `why_no_rule_needed` (when false); `served_class_of_a_money_market_fund_today`; `served_class_read_from`; `other_readers_of_that_assignment` (a list of strings, possibly empty); `reads` {`vendor_calls` 0, `secret_reads` 0, `writes` 0}; `served_values_changed` false; `pushed` false. No run of eight or more digits in any value (a path or a commit hash is exempt only under a key named `path`, `commit` or `slug`; write line numbers as integers).

<criterion id="DB98-2-AC1" cell_refs="DB-b-184"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r98/p98_round98.py" . DB98-2-AC1</invocation><expect>DB98-2-AC1 PASS</expect></criterion>
`DB98-2-AC1` -- the record names 3 or more hops from the IR holdings page to the class assignment, the one assignment site with its rule and what it is keyed on, whether it shares the gold classifier's code and the canonical table, and whether it needs its own rule (a rule keyed on sub_asset_class with no ticker list, or the reason none is needed); it states the served class of a money-market fund today or NOT_ESTABLISHED with the reason; no vendor call, secret read, write, push or served change; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB98-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. You edit no product file, no portal file, no classifier.
- **No write of any kind to AWS** (no DynamoDB put/update/delete, no S3 put/copy/delete, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files and, if you use them, S3 GET/LIST of served objects with the box's existing identity. A denial is recorded verbatim, not retried by another route.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the page's class path cannot be traced to a storage read, record the hops you have, set the fields you cannot establish to what you can prove, and file a row; do not guess a rule.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W149-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~149/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-184.ir-holdings-class-source-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 100 (round 98), cell `DB-b-184`.
<owned_cells>DB-b-184</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB98-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~149/IRPT_DASHBD.TO-DB-b-184.ir-holdings-class-source-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB98-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the hops in one line each (layer, file, line); where the class is assigned and what it is keyed on; whether it shares the gold classifier's code or table; whether it needs its own rule and, if so, the rule in words; the class a money-market fund shows today and where you read it; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read; nothing is changed, deployed or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: repo reads and, at most, S3 GET/LIST with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
