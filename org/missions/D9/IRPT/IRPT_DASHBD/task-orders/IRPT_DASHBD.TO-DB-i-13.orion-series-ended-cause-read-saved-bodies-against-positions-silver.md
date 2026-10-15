# TO IRPT_DASHBD.TO-DB-i-13 -- the SERIES-ENDED CAUSE READ: for each Orion Scope series that ends before the window end, does Opal's positions silver still hold the account after the series ended (STALE_AT_SOURCE) or not (CLOSED_OR_TRANSFERRED)? Saved bodies against fact_positions, no vendor call, counts and words only

<to_id>IRPT_DASHBD.TO-DB-i-13</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~313</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>126</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_122_20261015.md` item 3 and ADDENDUM 1 (msg 8678, open call dell2-20261015T211904Z-4255 ruled yes): "Compare the saved Scope bodies against the positions silver, with no vendor call. For each early-ending series print its last date, whether Opal still holds the account after it (day counts), and the verdict: stale-at-source or closed-or-transferred. Raw bodies and ids stay private; the repo gets counts and words only."

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-313`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/`. Never touch a path outside the `<paths>` block below, except your private folder named here.

**Why.** Round 122's history probe saw two of nine Scope series end 120 and 95 days before the window end (the rest end on it). If Orion's series is stale for an account Opal still holds, the feed would serve a hole for a live account; if the account closed or moved, the end is correct. This cell tells the two apart. It makes NO vendor call: it reads the saved response bodies (private) and Opal's own `fact_positions` silver through the GET-only reader.

**Read first.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~301/tieout_basis_variants.py` (your template: how to find the repository root, import `inflection_account_dim` as `iad` and `inflection_account_return_daily` as `iar`, build `iad.InflectionSilverReader()` and call `reader.list_partitions(iar.ORION_SILVER + "fact_positions")` and `reader.read_parquet(<table uri>/<partition name>/data.parquet)`); `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py` (`account_values(frame, accounts)` returns `{account key: total currentValue}`; an account with no row, or any NaN value, is absent); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r126/p126_cause.py` (its `last_ends`, `measure`, `verdict_of` and `recompute` ARE the rules below; read it first and run `python -I <it> --selftest`).

**The inputs (private; never copy a value into the repo).** The two saved round-122 response bodies `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~309/hist_A.json` and `hist_B.json`. Your private folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~313/` (create it).

**The cell (`DB-i-13`).**
1. **The early-ending series (the checker recomputes them).** In each body, every `calculated-group` with `grouping` `Account` that carries series points (a node with a `factor` and an `endDate`) has a LAST end date (the latest `endDate` among its points; dates are `MM/DD/YYYY` or ISO). The window end is 2026-10-13. An account is EARLY-ENDING when its last end date is strictly before the window end. The account key is `str(int(float(groupEntityId)))`. Count `series_total` (accounts with a series, over both bodies) and the early-ending ones.
2. **The positions read.** `partitions` = the `date=YYYY-MM-DD` partitions of `fact_positions` (from `list_partitions`). Read each partition whose date is strictly after the EARLIEST last end date among the early-ending accounts and not after the window end, in ascending order, one GET each, with `iar.account_values(frame, <set of early-ending account keys>)`. Stop at once if the reads (LIST pages plus GETs) would exceed 200: record the stop and report it, do not widen the cap. No other S3 call; no write of any kind.
3. **The private extract.** Write `positions_extract.json` in your private folder: `{"partitions": [every partition name you read, ascending], "values": {account key: {partition name: total value, or null when the account is absent from that partition}}}`.
4. **Per early-ending account (the checker recomputes these exact fields from the bodies and your extract).** `partitions_after` = the number of partitions in your extract strictly after the account's last end date and not after the window end; `held_days_after` = how many of those have a total value strictly greater than 0; `held_on_newest` = whether the NEWEST of those partitions has a total value strictly greater than 0; `series_ended_days_before_window_end` = the window end minus the last end date, in days. `verdict`: `NOT_DETERMINED` when `partitions_after` is 0; else `STALE_AT_SOURCE` when `held_on_newest` is true (Opal still holds the account after Orion's series ended); else `CLOSED_OR_TRANSFERRED`.
5. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/series_ended_cause.py`, the only code this cell adds. It reads through `InflectionSilverReader` only (GET-only, granted prefixes), makes no vendor or HTTP call, names none of: `put_object`, `upload_file`, `delete_object`, `copy_object`, `put_item`, `update_item`, `invoke(`, `start_execution`, `requests.`, `urllib.request`, `http.client`, `Authorization`, and reads no secret.
6. **Record** `SERIES_ENDED_CAUSE_R126.json` in your folder with exactly: `script` {`file`, `sha256`}; `bodies_sha256` (the sha256 of `hist_A.json` then `hist_B.json`, a list of two); `extract` {`path` (the absolute private path), `sha256`}; `series_total`; `early_end_count`; `accounts` (one entry per early-ending account, sorted by `account_sha256`, each with exactly `account_sha256` (sha256 of the account key as a string), `series_ended_days_before_window_end`, `partitions_after`, `held_days_after`, `held_on_newest`, `verdict`); `verdict_counts` ({`STALE_AT_SOURCE`, `CLOSED_OR_TRANSFERRED`, `NOT_DETERMINED`} counts); `basis_words` (words, at least 200 characters: how many series and how many early-ending, each early-ending account's days-before-window-end and day counts after, the verdict words, what the verdict means for the feed (a STALE_AT_SOURCE account means the feed's SERIES_ENDED_AT_SOURCE rows hide a live account) and what it does not establish (a held position is not proof of a vendor fault); NO value, NO date, NO id); `reads` {`s3_reads`, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits except in a `sha256` value or a `path` / `file` field; no partition name or date.

<criterion id="DBI126-1-AC1" cell_refs="DB-i-13"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r126/p126_cause.py" . DBI126-1-AC1</invocation><expect>DBI126-1-AC1 PASS</expect></criterion>
`DBI126-1-AC1` -- the record is complete and carries no identifier or date; the script is a tracked file hashed as recorded with no write, vendor-call or secret token, reading through `InflectionSilverReader`; the bodies' hashes equal the saved files'; the private extract's hash equals the recorded one; every early-ending account's fields and verdict, the series and early-ending counts and the verdict counts equal the checker's recompute from the saved bodies and your extract; no write, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI126-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and your private folder. Everything else is read, never edited, including `lib/`, `infra/`, `data/`, the template and every issuer check.
- **No vendor call, no secret.** The bodies are already saved. The positions are read through the GET-only reader; no other S3 call, no write, no deploy, no push.
- **Client data.** The bodies, the extract and every value are private; the repo, rows and your report carry counts, verdict words and digests only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A read cap hit, a missing partition, an account absent from every partition or a body shape the rules do not cover is a RESULT: record it with its verdict (`NOT_DETERMINED`) and in `basis_words`; never choose another window, never raise the cap.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W313-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-13.orion-series-ended-cause-read-saved-bodies-against-positions-silver.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 12, cell `DB-i-13`.
<owned_cells>DB-i-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI126-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~313/IRPT_DASHBD.TO-DB-i-13.orion-series-ended-cause-read-saved-bodies-against-positions-silver.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI126-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the number of series, of early-ending series, and the verdict counts; per early-ending account its days-before-window-end, `partitions_after` and `held_days_after`; the S3 reads made (LIST pages plus GETs); row ids. No token, no client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: GET and LIST of Opal's own Orion silver through the round-108 reader (granted prefixes, the principal rounds 108 to 111 used); no new principal or grant, no write.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI126-1-AC1 FAILS at base (no record), and the checker was fed a good record built from the real saved bodies and a synthetic extract (PASS) and nine bad variants (a wrong verdict, a wrong held-day count, wrong verdict counts, an S3 write, an identifier, a tampered extract hash, a put_object script, a vendor-call script, a script without the reader): each FAIL.
</preflight>
