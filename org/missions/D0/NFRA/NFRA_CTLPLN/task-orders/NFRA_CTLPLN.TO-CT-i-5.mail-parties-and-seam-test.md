# TO NFRA_CTLPLN.TO-CT-i-5 -- workstream INBOUND round 3 CT-i-5: the mail filter reads both domain records, and the box and cloud halves are run against each other

<to_id>NFRA_CTLPLN.TO-CT-i-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~33</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-5` (`decompositions/NFRA_CTLPLN_DECOMP.inbound3.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none (rounds 1 and 2 are merged)

---

## WORKER FACE

### THE CELL

`CT-i-5`, two small items, about 150 lines in all.

**Item 1, the second domain record.** Contract C-SEATS clause 9: a mail message is considered only when "its sender's domain is
one of the five he named (Cottonwood, Inflection, 49 Financial, Alongside, and Opal for internal), each domain string read from
the estate's firm records and never typed". Three of the five are tenant firms, recorded in `infra/logic/registry/scopes.json`
(`tenant.email_domain`), which `data/transcripts/scripts/teams_chat/mail_requests.py` `firm_domains()` reads today. The other
two are recorded in `infra/logic/registry/mail_parties.json`; read its `_about` block for its row fields (`party`,
`email_domains` as a list of {`domain`, `claim`}, `claim`, `considered`). Measured at the cut: that file records one party
with a measured domain and `considered` true, and one party with no domain, claim absent, `considered` false.

**Item 2, the two halves against each other.** A remote job's box side is `.tools/remote-job.py` (`bid`, `accept`, `grade`,
`complete`; `--dry-run` prints `DRY-RUN: would send <envelope JSON>` and sends nothing) and its cloud side is the handlers in
`data/transcripts/scripts/teams_chat/tenant.py` (`on_job_bid`, `on_job_accepted`, `on_job_complete`). Each was tested against
the same written seam, never against the other. Read `.tools/tests/test_remote_job_review.py` (how the box tool is run on a
temporary lock and liveness file) and `data/transcripts/scripts/tests/test_inbound_cloud.py` (how a handler is driven with a
fake context) before you build.

### BUILD

1. `mail_requests.py`: `firm_domains()` returns the union of the firm records and the mail-parties record. From
   `mail_parties.json` take a party ONLY when its `considered` is true, and from it only the domains whose own `claim` is
   "measured". A missing or unreadable `mail_parties.json` adds nothing and raises nothing. No domain string is typed.
   `--check-domains` counts five parties (three firms and the two parties of the record) and prints, as today, one line per
   party with its domain count and no domain string; its LAST line stays `MAIL-DOMAINS ok=<True|False> firms=<f>/5 typed=0`.
   `typed_domains` also treats a domain string read from `mail_parties.json` as read, not typed.
2. `data/transcripts/scripts/tests/test_inbound_mail.py`: add cases, on invented registry content injected by the test: a
   considered party's measured domain is admitted; a party with `considered` false is not; a domain whose claim is not
   "measured" is not; a missing mail-parties file leaves the three firms working. Keep every existing case and its LAST line
   shape.
3. NEW `data/transcripts/scripts/tests/test_inbound_seam.py` (a plain script; nothing leaves the machine): run the REAL
   `.tools/remote-job.py` as a subprocess with `--dry-run` on a temporary lock and liveness file to get the envelopes for
   `bid`, `accept` (with a real brief file), and `complete` after a real `grade ... --verdict PASS` by a reviewer serial;
   parse each printed envelope; feed its `payload` to the REAL cloud handlers under the fake context, in order, on a job
   opened by the test. Assert: the bid is recorded with its `reviewer`; the accepted job reads `working`; the graded
   completion reaches `verify`. The difference control: the envelope of a `complete` the box tool REFUSES is never produced
   (rc 2), and a completion payload with its `grade` removed by the test is refused by the cloud handler and leaves the job
   `working`. If `--dry-run` cannot produce a `complete` envelope after a grade (for example because dry-run touches no
   lock), build the lock the way the box tool's own test does and say so in the report. LAST line
   `INBOUND-SEAM-TEST ok=<True|False> cases=<passed>/<total>`.

### RULES FOR THIS CELL

- **Nothing you run leaves this machine**: no bus send, no event to the cloud, no gateway, mailbox, model, text or AWS call.
  Every run of the box tool is `--dry-run` or on a fake sender; leave the real `.tools/.remote-job.json` as you find it.
- Edit nothing but the three files in `<paths>`. If the two halves DISAGREE (a field one sends and the other does not read, or
  reads under another name), do not repair either half: file a surprise row, class BLOCKING, with both shapes, and leave the
  seam test failing on that case.
- No real person's, client's or firm's name or domain in a test beyond what the registry files already hold; invented ones
  for injected content.
- No non-ASCII in any file you write. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi5-AC1" cell_refs="CT-i-5"><invocation>python data/transcripts/scripts/tests/test_inbound_mail.py</invocation><expect>INBOUND-MAIL-TEST ok=True cases=(1[5-9]|[2-9][0-9])/</expect></criterion>
`CTi5-AC1` -- the union of the two records with its difference control: a party not marked considered, or a domain not measured, is not admitted. The file has 11 cases today; with the four added it reads 15 or more, and the expectation requires that.

<criterion id="CTi5-AC2" cell_refs="CT-i-5"><invocation>python data/transcripts/scripts/tests/test_inbound_seam.py</invocation><expect>INBOUND-SEAM-TEST ok=True</expect></criterion>
`CTi5-AC2` -- the real box tool's envelopes through the real cloud handlers; an ungraded completion refused on both sides.

<criterion id="CTi5-AC3" cell_refs="CT-i-5"><invocation>python data/transcripts/scripts/teams_chat/mail_requests.py --check-domains --expect-missing 1</invocation><expect>MAIL-DOMAINS ok=True firms=4/5 typed=0</expect></criterion>
`CTi5-AC3` -- the real records: four of the five parties load and one is named missing.
</proof_of_spec>

<expected_criteria>CTi5-AC1,CTi5-AC2,CTi5-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~33/NFRA_CTLPLN.TO-CT-i-5.mail-parties-and-seam-test.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi5-AC1,CTi5-AC2,CTi5-AC3`, and flip `<status>` to `complete`
only when every criterion passes and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W33-S<k>`; append lines only
to the investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound3.md</decomp_doc>
<owned_cells>CT-i-5</owned_cells>
</decomp_ref>

<paths>
data/transcripts/scripts/teams_chat/mail_requests.py
data/transcripts/scripts/tests/test_inbound_mail.py
data/transcripts/scripts/tests/test_inbound_seam.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a party admitted that the record marks not considered (considered and measured are both required; tested); a typed domain (the check prints typed=0); the two halves agreeing only on paper (the real tool's envelopes through the real handlers; a disagreement is a BLOCKING row, never a quiet repair by the worker); a seam test that sends (dry-run and a fake context only). BLIND: the deployed function's own packaging of mail_parties.json is the deploy order's, not this cell's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20, C-SEATS clauses 8 and 9; CTO ruling msg 106655;
`4.0.0_SA_CRO` msg 106662; round-1 decomposition, "The issuer's acts after the drain" item 2.
