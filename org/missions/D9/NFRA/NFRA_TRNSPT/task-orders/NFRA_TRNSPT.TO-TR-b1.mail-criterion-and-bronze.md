# TO NFRA_TRNSPT.TO-TR-b1 -- the mail criterion and the bronze landing of Andrew's mailbox, replay-fed

<to_id>NFRA_TRNSPT.TO-TR-b1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~3</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-b-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-7 | **depends_on:** TR-g-1 (drained; `address('outlook', ...)` builds on your branch)

---

## WORKER FACE

### THE CELL

`TR-b-1`, communications item 2 (PRD section 3): "The YCharts-report detection rule (one look at a real attachment) and the
dredge of Andrew's mailbox into bronze by the date-sliced method that works under today's tools (v3 addendum 8), then the daily
pull." FWD-7: feedback "that Manav sends a client with a YCharts report attached is filed in the database on its own, every day,
and never altered." C-CRITERION (Andrew-direct): ingest when the SENDER is on the author table AND a YCharts report is attached
AND it is investment feedback; the recipient domain is a stored ATTRIBUTE (`recipient_firm`), never a gate ("Make it a recorded
attribute as well"); "49 Trade Update" automated mail is excluded by rule. C-DEDUP and the ROUND-1 BRONZE CONTRACT are in the
decomposition (`NFRA_TRNSPT_DECOMP.md`, "BRONZE CONTRACT, analysis_commentary, round 1") -- read it; it is binding.

**Measured at the cut (2026-09-30, Andrew's mailbox through the gateway):** `read_email` returns `{id, subject, from{emailAddress{name,address}},
toRecipients[], receivedDateTime, body{contentType:"html", content}}` and NOTHING else (no `internetMessageId`, `ccRecipients`,
`conversationId`, `sentDateTime`); `list_email_attachments` returns `[{id, name, size, contentType, isInline}]`, no bytes. The
author addresses: `Manav@opalinvest.com`, `manav.shah@49financial.com`, `Yang@opalinvest.com` (Yang's 49financial address is
unmeasured). A real Manav reply to a 49financial client on 2026-09-23 carried four non-inline `image/png` charts and NO PDF: a
near-miss the criterion records and does not ingest.

**Build:**
1. `data/transcripts/scripts/outlook/criterion.py`: `classify(message, attachments, authors, client_domains) -> dict` with
   `sender_ok` (from.address, case-insensitive, in the author table), `client_recipient` (any To at a client domain),
   `recipient_firm` (the firm key of the first client-domain To, else `null`), `ycharts_pdf` (a non-inline attachment with
   `contentType == "application/pdf"` and `size >= 300_000`, OR body words `YC report`/`YChart` -- and `ycharts_basis`
   = `"heuristic:name-size-body"`, C-CRITERION's stated heuristic until the attachment tool exists), `trade_update_excluded`
   (subject begins `49 Trade Update`, exactly one To that is a distribution address -- any local part at `49financial.com`
   ending in a distro form or `49@opalinvest.com` -- and no `Re:`/`RE:`/`Fwd:` prefix), `near_miss` (sender_ok and not
   ycharts_pdf), `ingest` = `sender_ok and ycharts_pdf and not trade_update_excluded`. Author and domain tables are read from
   `data/transcripts/assets/authors.json` and `client_domains.json` when present (another chain's cell writes them); when absent,
   from an inline default carrying the three addresses and the three domains above (state which was used in the run record).
2. `data/transcripts/scripts/outlook/land_bronze.py`: `record_id(message)` = sha256 of `lower(from.address) + "|" + receivedDateTime
   + "|" + subject + "|" + sha256(body.content)` hex, `rid16` = its first 16 hex, `id_source = "fallback"`; `land(message_json_text,
   attachments_json_text, classification, *, s3, kms_key_arn, run_id, apply)` writes `msg_<rid16>.json` (the recorded text EXACTLY,
   bytes untouched), `msg_<rid16>.attachments.json` (same), `msg_<rid16>.sidecar.json` (the contract's fields) at
   `lib.opal_naming.address("outlook","transcripts","bronze","analysis_commentary","date=<receivedDateTime UTC date>", object)`
   with the KMS headers (key ARN resolved from `alias/opal-data-transcripts` at run time); existing key with identical sha256 ->
   `SKIP-IDENTICAL`, different -> `REFUSED`; `apply=False` -> `DRY`. Every candidate the replay holds is landed (bronze keeps the
   candidate set, silver keeps what passes: v3 section 2), with its classification in the sidecar.
3. `data/transcripts/scripts/outlook/pull.py`: `run(source, s3, *, kms_key_arn, apply, run_id) -> RunRecord` where `source` is
   `ReplaySource(dir)` (files `<graph_id>.message.json` and `<graph_id>.attachments.json` exactly as the gateway tools returned
   them) or `GatewayMailSource(base_url, bearer)`, a STUB whose methods raise `GatewayToolsAbsent("S12 not landed: <route>")`.
   The run record `{run_id, started_utc, ended_utc, no_person, source, candidates, ingest, near_miss, excluded_trade_update,
   fallback_ids, landed, skipped_identical, refused}` goes to `address("outlook","transcripts","state","pull_runs","run=<ISO>","run.json")`.
   CLI: `python data/transcripts/scripts/outlook/pull.py --replay <dir> [--dry-run|--apply]` prints
   `OUTLOOK-DRY candidates=N ingest=K excluded_trade_update=J near_miss=M fallback_ids=N` (or `OUTLOOK-LANDED ...`).
4. Fixture `data/transcripts/scripts/tests/fixtures/outlook_replay/`: FIVE SYNTHETIC messages in the tool shapes above (invented
   names, invented client at `example-client.49financial.com`-style addresses are NOT allowed -- use the three real DOMAINS with
   invented local parts, since the domain table is the thing under test): (a) Manav@opalinvest.com to a 49financial client with
   a 620 KB non-inline `application/pdf` -> ingest; (b) manav.shah@49financial.com to an inflectionwealth client with four PNGs
   -> near_miss; (c) Yang@opalinvest.com to a cottonwoodmail client with a 480 KB PDF and body "YC report attached" -> ingest;
   (d) subject `49 Trade Update (September 22, 2026)` to one distro address with a 240 KB PDF -> excluded; (e) a non-author
   sender with a PDF -> not ingested. So `candidates=5 ingest=2 excluded_trade_update=1 near_miss=1 fallback_ids=5`.
5. Tests `data/transcripts/scripts/tests/test_outlook_bronze.py` on the fake-S3 pattern: the classification of all five, the
   record id and its fallback flag, byte-exact landing of the message text, the three objects and their addresses, idempotence,
   never-overwrite, the run record.

### ACCEPTANCE

<criterion id="TR1-b1-AC1" cell_refs="TR-b-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_outlook_bronze.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-b1-AC1` -- the criterion's five cases, the fallback id, byte-exact bronze at the builder's address, idempotence.

<criterion id="TR1-b1-AC2" cell_refs="TR-b-1"><invocation>python data/transcripts/scripts/outlook/pull.py --replay data/transcripts/scripts/tests/fixtures/outlook_replay --dry-run</invocation><expect>OUTLOOK-DRY candidates=5 ingest=2 excluded_trade_update=1 near_miss=1</expect></criterion>
`TR1-b1-AC2` -- the entry the daily schedule and the issuer's recorded-sample run will call, over the typed fixture.

<expected_criteria>TR1-b1-AC1,TR1-b1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran", AC2 "No such file" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **SERVED class, but YOUR order writes nothing to the bucket:** the real landing of the recorded sample is the ISSUER's run at
  the drain (`--replay <recorded dir> --apply`). Do not read Andrew's mailbox (you have no gateway tool) and never put a real
  email in the repository: fixtures are synthetic.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W3-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/outlook/criterion.py
data/transcripts/scripts/outlook/land_bronze.py
data/transcripts/scripts/outlook/pull.py
data/transcripts/scripts/tests/test_outlook_bronze.py
data/transcripts/scripts/tests/fixtures/outlook_replay/
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-b-1`.
<owned_cells>TR-b-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-b1-AC1, TR1-b1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~3/NFRA_TRNSPT.TO-TR-b1.mail-criterion-and-bronze.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-b1-AC1,TR1-b1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the classification table of the five cases, the sidecar fields, the three addresses for one case, the OUTLOOK-DRY line,
the pytest line, which author/domain source was used, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the daily schedule rides the headless mail route (S12, site Z) and a later release.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (arn:aws:iam::313476888478:user/Andrew_Berman, the var.reader_principal_arns default), 1 bucket policy with 2 Deny statements (TLS-only, key-only); BLIND: the live IAM plane outside this root was not scanned (0 of the account's roles read). The issuer's real run lands under that one grantee; this cell adds no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the tool shapes, the near-miss and the fallback id (row NFRA_TRNSPT-S2) are inlined.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-CRITERION, C-DEDUP, S10, S11, S13, section 3 communications item 2; decomposition round 1 cell TR-b-1 and its BRONZE CONTRACT.
