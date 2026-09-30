# TO NFRA_TRNSPT.TO-TR-f2 -- the mail lander reads the real Graph envelope; the criterion reads the ruled tables

<to_id>NFRA_TRNSPT.TO-TR-f2</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-f-2` (`decompositions/NFRA_TRNSPT_DECOMP_R2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-f-2`, round 2's first thread-breaking item (CTO analysis ruling 3a): "the lander unwraps the Graph `value` envelope (with a
fixture in the real envelope shape) and `load_tables` reads the ruled `authors.json` and the registry's tenant email domains alone."

**Measured facts (read, never edit):**
- The real `list_email_attachments` tool returns the Graph ENVELOPE, not a list:
  `{"@odata.context": "...", "value": [{"@odata.type", "@odata.mediaContentType", "id", "name", "contentType", "size", "isInline"}, ...]}`.
  Round 1's fixture `data/transcripts/scripts/tests/fixtures/outlook_replay/` used a bare list, so `outlook/pull.py --replay` crashes on
  real input in `criterion.classify` (`'str' object has no attribute 'get'`) -- row S9. Real `read_email` output is
  `{"@odata.context", "@odata.etag", "id", "receivedDateTime", "subject", "body": {"contentType": "html", "content"}, "from": {"emailAddress": {"name", "address"}}, "toRecipients": [...]}`.
- `outlook/criterion.py` `load_tables()` (lines ~48-54) reads `data/transcripts/assets/authors.json` only when `client_domains.json`
  ALSO exists; that file was retired by ruling (the client domains are registry data), so the criterion always falls back to its inline
  defaults and never reads the ruled authors table -- row S10.
- The ruled `authors.json` shape: `{"authors": [{"name": "Manav Shah", "addresses": ["manav@opalinvest.com"], ...}, {"name": "Yang Liu",
  "addresses": ["yang@opalinvest.com"], ...}], "firm_domain_rule": "<a sender whose display name equals an author's name and whose
  address domain is a registered FIRM email_domain is sender_ok>", ...}`.
- The registry's client domains: `infra/logic/registry/scopes.json`, rows with `class == "FIRM"` and a non-null `tenant.email_domain`;
  the firm key is the row's `key`. Read them through the registry file at run time. NEVER type a firm token (a firm's name, short form
  or domain) as a literal in any new code file: the commit-time naming gate refuses it.

**Build (LOCAL):**
1. `criterion.classify(message, attachments, ...)` accepts the attachments either as the Graph envelope (use its `value`) or as a list.
   `outlook/pull.py` / `land_bronze.py` keep landing the RECORDED attachments text byte for byte (never the unwrapped form).
2. `load_tables()` reads `authors.json` alone (both address lists, lower-cased, and the `firm_domain_rule` applied: display name match
   + registry FIRM domain => `sender_ok`) and the client domains from the registry; returns a source label `assets+registry`.
   Fall back to the inline defaults only when `authors.json` is absent, labelled `inline-default`.
3. The run record and the `--dry-run` line gain ` tables=<label>`:
   `OUTLOOK-DRY candidates=N ingest=K excluded_trade_update=J near_miss=M fallback_ids=N tables=assets+registry` (the counts keep their order).
4. Fixture `data/transcripts/scripts/tests/fixtures/outlook_replay_envelope/`: FIVE SYNTHETIC messages, each as
   `<id>.message.json` in the real `read_email` shape and `<id>.attachments.json` in the real ENVELOPE shape (invented names and
   local parts; use short invented ids such as `SYN-ENV-001`): (a) an opalinvest author address to a client-firm recipient with a
   620 KB non-inline PDF -> ingest; (b) an author's display name at a client-firm domain (the firm_domain_rule path) with a 480 KB PDF
   and body "YC report attached" -> ingest; (c) an author with only PNG attachments -> near_miss; (d) a "49 Trade Update (...)"
   subject to one distribution address with a 240 KB PDF -> excluded; (e) a non-author with a PDF -> not ingested. Where a fixture must
   carry a client-firm domain, write it at test time from the registry (a conftest-free helper in the test) rather than committing it
   in the JSON, if the naming gate refuses the literal; say which you did.
5. Tests `data/transcripts/scripts/tests/test_outlook_envelope.py`: the five classifications from the envelope fixture; a bare list
   still classifies identically; `load_tables()` label is `assets+registry` and its domains equal the registry's FIRM
   `tenant.email_domain` set; the firm_domain_rule admits (b) and would not admit the same display name at a non-firm domain; the
   landed `msg_<rid16>.attachments.json` bytes equal the recorded envelope text.

### ACCEPTANCE

<criterion id="TR2-f2-AC1" cell_refs="TR-f-2"><invocation>python -m pytest data/transcripts/scripts/tests/test_outlook_envelope.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR2-f2-AC1` -- the real envelope classifies, the ruled tables are read, the firm-domain rule holds, the landed bytes are the recorded bytes.

<criterion id="TR2-f2-AC2" cell_refs="TR-f-2"><invocation>python data/transcripts/scripts/outlook/pull.py --replay data/transcripts/scripts/tests/fixtures/outlook_replay_envelope --dry-run</invocation><expect>OUTLOOK-DRY candidates=5 ingest=2 excluded_trade_update=1 near_miss=1</expect></criterion>
`TR2-f2-AC2` -- the entry the issuer's real run calls, over the real-shape envelope fixture (it crashes on that shape today). The tables label is asserted in AC1's test; append ` tables=<label>` AFTER the counts on this line so the expectation still matches.

<expected_criteria>TR2-f2-AC1,TR2-f2-AC2</expected_criteria>

Dry-run at the base c31230ea02: AC1 "no tests ran" rc 4; AC2 FileNotFoundError (fixture absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** No bucket write, no mailbox read, no real email in the repository.
- **The precision scan (TR-d-2) is the next order in your queue** and calls `classify` and `load_tables`; keep their signatures.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W1-S<k>`, next unused after W1-S5), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/outlook/criterion.py
data/transcripts/scripts/outlook/land_bronze.py
data/transcripts/scripts/outlook/pull.py
data/transcripts/scripts/tests/test_outlook_envelope.py
data/transcripts/scripts/tests/fixtures/outlook_replay_envelope/
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R2.md</decomp_doc> (round 2), cell `TR-f-2`.
<owned_cells>TR-f-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR2-f2-AC1, TR2-f2-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-f2.envelope-and-tables.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR2-f2-AC1,TR2-f2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the five classifications, the tables label and the domain set's size, how fixtures carry client domains, the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (Andrew's IAM user), 1 bucket policy with 2 Deny statements; BLIND: the live IAM plane outside this root (0 of the account's roles read). This cell writes nothing to the bucket.
comp-adversary: RUN -- the real envelope shape and the load_tables pairing (rows S9, S10) are inlined from the issuer's real run.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @acd1033e60 ruling 3a and section 4 item 1; rows S9, S10; decomposition round 2 cell TR-f-2.
