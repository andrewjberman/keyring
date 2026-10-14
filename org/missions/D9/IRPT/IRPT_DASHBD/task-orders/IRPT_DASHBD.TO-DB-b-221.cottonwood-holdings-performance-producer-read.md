# TO IRPT_DASHBD.TO-DB-b-221 -- READ Cottonwood's holdings_performance_daily: its producer, its schedule or trigger (DESIRED against APPLIED, and why it has none), the input frontier against T-1 by the trading calendar, what a scheduled fire needs, and who writes Cottonwood's irpt holdings (which end 2026-10-08); read only, nothing scheduled

<to_id>IRPT_DASHBD.TO-DB-b-221</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~178</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>110</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-110 ANALYSIS section 1 (row S37: "Cottonwood's performance gold ends 2026-09-25 (12 trading days behind T-1), its channel unscheduled ... P1 cannot be met for Cottonwood without a scheduled producer ... The first step is a READ") and section 2 cell 3(b) (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_110_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W178-S<k> | **Decomp cell:** `DB-b-221` (decomposition section 112) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-178` (branch `wk-IRPT_DASHBD-178`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~178/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, names and words only in the repo, a row or your report; an account id, a client name or a figure is never recorded.

**Why.** Andrew's P1 is the performance reporting tab functional for all clients at all firms, internally by Nov 15. Cottonwood's holdings-basis performance gold (`holdings_performance_daily`) is the table its performance reads, and its newest partition is `date=2026-09-25`, twelve trading days behind T-1 on 2026-10-14. CLAUDE.md: production pipelines MUST be scheduled, and success-of-upstream as the only trigger is a defect. Nobody has said what writes this table, why nothing fires it, or what a scheduled fire needs. This cell reads the answer; the schedule itself is a LATER round under a never-widen pair, and you create, change and write nothing.

**What is known (the issuer's own read of the repo, 2026-10-14).** The producer code is `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (`TABLE_DAILY = "holdings_performance_daily"`, `main()` with `--source`, `--date`, `--start`, `--end`, `--upload`, `--dry-run`); its declaration is `data/assets/scripts/gold/irpt_holdings_performance/sources.json`, key `blackdiamond_z09` (line 159: custodian and monolith `blackdiamond`, `registry_key` `z09`, positions under `{monolith}/{scope}/silver/fact_holdings/`, `link_across_gaps` false). Cottonwood's gold lives at the `lib/opal_naming.py address()` bucket `s3://opal-data-cottonwood/irpt/cottonwood/gold/`. The round-103 read of the sibling table (`account_return_daily`) is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~160/COTTONWOOD_RETURN_STALE.json` with its order `task-orders/IRPT_DASHBD.TO-DB-b-195.why-cottonwood-account-return-daily-stops-at-2026-06-22.md`: read both first, they show the method and the routes that answered DESIRED against APPLIED for that table; do not assume the answer carries over.

**The grant of the S3 reads (BY PREFIX).** LIST and GET under `s3://opal-data-cottonwood/irpt/cottonwood/gold/` (the newest partitions' `manifest.json` and key names; counts and keys only) and LIST ONLY (partition key names, never contents) under the Black Diamond silver `positions_prefix` that `holdings_performance.py` resolves for `blackdiamond_z09` (compute it with that module's own resolver by a read-only import; never type the scope). No put, copy or delete. AWS reads otherwise: the served graph first, then live `get` / `describe` / `list` of single named resources through the `.tools/aws` shim (never bare `aws`).

**The cell (`DB-b-221`): a READ. Nothing is changed, scheduled, deployed or written (outside your folder).**
1. **The producer.** Read the newest partition's `manifest.json` beside `holdings_performance_daily` (the writer named there) and the code. Record `producer` {`file` (an EXISTING repo-relative file), `entry` (the function or command that runs it), `channel` "blackdiamond_z09", `table` "holdings_performance_daily", `claim`}.
2. **Its schedule or trigger, DESIRED against APPLIED, and why it has none.** DESIRED = what the repo, the dispatch catalog (`comp-find`/`comp-which "irpt holdings performance schedule"`), Terraform under `infra/` or a doc says should run it and when. APPLIED = what is actually live (an EventBridge rule or schedule, an S3-event trigger, a Lambda, a task definition, or a manual run), read through the SERVED graph first (pick the cloud read route from `org/modules/graph/graph-call-manifest.yaml`: CLAUDE.md rules 20 and 21; read the vintage line it prints), and only then a live describe of one named resource. Record `schedule` {`desired` {`exists`, `where`, `claim`}, `applied` {`exists`, `where`, `plane` ("served_graph" or "live_describe"), `claim`}, `why_none` (words, from evidence: never declared, declared and not applied, applied and disabled, or the producer is manual-only; or `why_scheduled` if one runs), `claim`}.
3. **The input frontier.** `frontier`: `measured_on` (the ISO date you read it), `newest_input_date` (the newest `date=` partition of the Black Diamond silver prefix), `newest_gold_date` (the newest `date=` partition of `holdings_performance_daily`: re-list it, do not copy 2026-09-25), `t_minus_1` (the NYSE trading day before `measured_on`), `trading_days_behind` (trading days after `newest_gold_date` up to and including `t_minus_1`: `trading_days_behind(newest_gold_date, t_minus_1)` of `lib/trading_calendar.py`; the checker recomputes it), `calendar_source` and `claim`. If the input itself is behind T-1 say by how many trading days (words).
4. **What a scheduled fire needs.** `scheduled_fire_needs`: a list of `{need, claim}` (the trigger and its time against the input's own arrival; the identity it runs as and its read and write grants; the inputs and whether they are current at fire time; the method and declaration version; any pair, hold or ledger that applies; what the fire writes and whether that is served output, so a LATER never-widen pair). One need per entry, in words.
5. **Who writes Cottonwood's irpt holdings (the table that ends 2026-10-08).** Find the Cottonwood `holdings` table beside the performance table in the gold prefix and name what writes it and what triggers that writer: `irpt_holdings_writer` {`who_writes` (words), `newest_date` (re-listed, ISO), `claim`}. If it is scheduled and the performance table is not, say so: it is the contrast the CTO needs.
6. **Record** `RD_COTTONWOOD_PRODUCER_R110.json` in your folder with exactly: `producer`; `schedule`; `frontier`; `scheduled_fire_needs`; `irpt_holdings_writer`; `denominator` {`nodes_scanned` (integer: the schedule or rule nodes the served-graph read looked through), `vintage` (the vintage line's words), `scope_words`}; `positive_control` {`description`, `expected`, `observed`, `passed` true: the same schedule read FINDS one producer you know IS scheduled, for example the Cottonwood `holdings` writer when it is, or another named scheduled IRPT producer, so an empty result for this table means absent and not unreadable}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer), `aws_reads` (integer), `aws_writes` 0, `terraform_apply` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. Counts, names, addresses and words only: no account id, no client name, no figure, no run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field.

<criterion id="DB110-6-AC1" cell_refs="DB-b-221"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_reads.py" . DB110-6-AC1</invocation><expect>DB110-6-AC1 PASS</expect></criterion>
`DB110-6-AC1` -- the record names the producer with an existing entry file, channel `blackdiamond_z09` and table `holdings_performance_daily`; states the schedule's DESIRED and APPLIED states each with existence, a place and a claim, the plane the applied state was read from, and why there is none; states the frontier as ISO dates with T-1 equal to the trading day before the read date and `trading_days_behind` equal to the checker's own count from `lib/trading_calendar.py`; lists at least one scheduled-fire need; names the irpt holdings writer with its newest date; prints a denominator with a vintage and a passed positive control; every value group carries a claim in the four-word set; no write, schedule, apply, push or deploy; no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB110-6-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `sources.json`, `holdings_performance.py`, every Terraform file, every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the gold prefix above and LIST of the Black Diamond silver prefix; the served graph; live get, describe and list of single named resources. Writes: your folder only. No write to AWS of any kind: no schedule, rule, Lambda, task or permission is created, changed or deleted; no `terraform apply` or `safe-apply`; no deploy; no push; no vendor call; no secret read; no invocation of the producer with `--upload`.
- **Client data.** The partitions are client data: counts, names and words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the schedule plane cannot be read (an AWS access refusal, a stale or empty graph), record `applied.claim` "absent", name the refusal in `schedule.why_none` and file a BLOCKING row: an unreadable plane is never a zero. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W178-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~178/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-221.cottonwood-holdings-performance-producer-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 112 (round 110), cell `DB-b-221`.
<owned_cells>DB-b-221</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB110-6-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~178/IRPT_DASHBD.TO-DB-b-221.cottonwood-holdings-performance-producer-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB110-6-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the producer and its entry; whether a schedule exists DESIRED and APPLIED and why there is none; the newest input and gold dates and the trading days behind T-1; what a scheduled fire needs (one line each); who writes Cottonwood's irpt holdings and what triggers it; the plane you read the schedule from, its denominator and the positive control; the S3 and AWS read counts; row ids. No account id, client name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and one record in the worker's folder; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of Cottonwood's gold prefix and LIST of one Black Diamond silver prefix, and get, describe and list of single named resources; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the cell READS the schedule plane and creates no schedule; the schedule itself is a later round under a never-widen pair.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB110-6-AC1 FAILS at base (no record) and the checker's 9-arm self-test refuses a trading-days-behind count the calendar disagrees with, a missing schedule plane and an empty denominator.
lane: the <paths> block IS the grant.
</preflight>
