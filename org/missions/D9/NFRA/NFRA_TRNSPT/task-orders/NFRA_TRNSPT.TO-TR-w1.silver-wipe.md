# TO NFRA_TRNSPT.TO-TR-w1 -- silver with the PII wipe; the planted-token test is the gate

<to_id>NFRA_TRNSPT.TO-TR-w1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~4</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-w-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-7 | **depends_on:** TR-a-1 (drained; the assets are on your branch)

---

## WORKER FACE

### THE CELL

`TR-w-1`, communications item 3 (PRD section 3): "Silver with the wipe, and the planted-token test as its gate." Andrew-direct:
"Silver is typed and deduplicated bronze in parquet with PII wiped." C-WIPE (binding, verbatim from the PRD): "Names: a vendored,
hash-pinned dictionary (public name lists) applied case-sensitively, behind an ALLOWLIST (Opal model names, products, tickers,
finance terms, theme labels), plus the client firms' names and advisor names. Identifier-like strings (a token over 4 characters
with a digit, not a percentage, decimal, amount, year or date): replaced by `[ID]`, no hash (a hash of an 8-digit id is reversible
by enumeration). Emails and phone numbers by pattern. Theme labels are wiped too. Anything capitalised and unknown goes to
`pii_residual_flags` and is held out of serving. Block structure is kept because the slicer needs it. STATED LIMIT: the wipe
removes dictionary names, identifier-like numbers and patterns; it does not remove a client name that is on no list."
C-WIPE-GATE: "A planted-token leak test passes (names in a heading, in a salutation, split across an HTML tag, in a different
case, in a common-word name, plus 8-digit and alphanumeric ids). Its result is 'the planted classes were removed', never 'no PII
remains'. No gold body text leaves Opal before it passes."

**The bronze shape you consume** is the decomposition's BRONZE CONTRACT (read it): `msg_<rid16>.json` = a Graph message with
`body.content` raw HTML; `msg_<rid16>.attachments.json`; `msg_<rid16>.sidecar.json` with `record_id`, `id_source`, `received_at`,
`criterion{...}`. The cut rules seen in a real 2026-09-23 reply: the signature is `<div id="Signature">`; the quoted chain begins at
`<div id="appendonsend">`, then `<hr>`, then `<div id="divRplyFwdMsg">` (nested replies repeat with `x_` prefixes); the 49
compliance boilerplate opens "Certain appropriately licensed individuals are registered to offer advisory services"; inline
images are `cid:`; the body is `div.elementToProof` paragraphs with `<br>`-separated allocation lines and bold labels.

**Build:**
1. `data/transcripts/scripts/outlook/wipe.py`: `load_assets(root="data/transcripts/assets") -> Assets` (the dictionary, allowlist,
   theme labels, client firm names and domains, author names); `wipe_blocks(blocks, assets) -> (wiped_blocks, residual_flags,
   counts)`. Order: allowlist first (an allowlisted token is never wiped), then dictionary names case-sensitively on capitalised
   tokens -> `[NAME]`, client firm names and advisor/author names -> `[NAME]`, theme labels -> `[THEME]`, emails -> `[EMAIL]`,
   phones -> `[PHONE]`, identifier-like tokens (len > 4, contains a digit, not a percentage, decimal, comma-grouped or
   `$`-prefixed amount, 4-digit year, or date) -> `[ID]`; any remaining capitalised token not in the allowlist, not sentence-initial
   common English (keep a small stopword list) -> `residual_flags`. `counts` reports each class.
2. `data/transcripts/scripts/outlook/silver.py`: `to_blocks(html) -> [{"kind": "heading|paragraph|list_item", "text"}]` with the
   stdlib `html.parser`, dropping the signature, everything from `appendonsend`/`divRplyFwdMsg` on, the compliance boilerplate,
   images and links (keep link text); `to_row(message, attachments, sidecar, assets) -> row` with columns `record_id, id_source,
   received_at, sender_role ("author"), recipient_firm, sender_ok, client_recipient, ycharts_pdf, ycharts_basis,
   trade_update_excluded, ingest, blocks (list<struct{kind,text}>), body_text (wiped blocks joined by "\n\n"), attachment_classes
   (list<string>: pdf|image|other, sizes kept), attachment_count, pii_residual_flags (list<string>), held_out (bool: flags non-empty),
   wipe_counts (struct)`; no addresses, no display names, no attachment names. `build(bronze_date, *, s3, kms_key_arn, apply) -> key`
   reads every `msg_*` triple under the bronze partition, keeps rows with `ingest` true, de-duplicates on `record_id`, writes ONE
   parquet per date at `address("outlook","transcripts","silver","analysis_commentary","date=<bronze_date>","analysis_commentary.parquet")`
   with the KMS headers. CLI: `python data/transcripts/scripts/outlook/silver.py --date YYYY-MM-DD [--apply]` prints
   `SILVER-COMMENTARY rows=<n> held_out=<h> key=<addr>`.
3. Tests `data/transcripts/scripts/tests/test_wipe_planted.py`: build a SYNTHETIC HTML message with planted tokens -- an invented
   dictionary surname in a heading, a given name in a salutation ("Hi Tarquin,"), a name split across an inline tag
   (`Ta<span>rquin</span>`), a lower-case name in prose, the common-word names "Will" and "Grant" used as names, an 8-digit id
   `08242253`, an alphanumeric id `z09302843`, an email, a phone, a theme label -- and assert every planted class is absent from
   the wiped text, that `75/25`, `0.32%`, `$1,250,000`, `2025`, `09/22/2026` and the allowlisted "Long-Term Portfolio", "Dividend
   Income", "Ultra Short-Term", "UST", "LT" survive, that a planted unknown capitalised token lands in `pii_residual_flags`, and
   that block structure is kept. The test also writes `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/WIPE_GATE_RECORD.json`
   `{"planted": {class: token_count}, "removed": {...}, "residual_flagged": n, "result": "the planted classes were removed",
   "not_claimed": "no PII remains"}` -- the C-WIPE-GATE record.
4. Tests `data/transcripts/scripts/tests/test_outlook_silver.py`: on a synthetic bronze triple in the contract's shape (inline in
   the test; never a real email): the cut rules (signature, quoted chain, boilerplate dropped), the row's columns and types, the
   ingest filter and dedup, `held_out` when a flag exists, the parquet written with the KMS headers on the fake S3.

### ACCEPTANCE

<criterion id="TR1-w1-AC1" cell_refs="TR-w-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_wipe_planted.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-w1-AC1` -- C-WIPE-GATE: every planted class removed, the allowlist and numbers kept, the residual flagged, the record written.

<criterion id="TR1-w1-AC2" cell_refs="TR-w-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_outlook_silver.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-w1-AC2` -- bronze triple to the typed, de-duplicated, wiped silver row and its parquet.

<expected_criteria>TR1-w1-AC1,TR1-w1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 and AC2 "no tests ran" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **SERVED class, but YOUR order writes nothing to the bucket:** the real silver build over the landed sample is the issuer's
  run at the drain, after AC1 passes (C-WIPE-GATE). No real email text in the repository or in any deliverable.
- **Gold (TR-k-1) is the next order in your queue** and reads this parquet by these column names: keep them exact.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W4-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/outlook/wipe.py
data/transcripts/scripts/outlook/silver.py
data/transcripts/scripts/tests/test_wipe_planted.py
data/transcripts/scripts/tests/test_outlook_silver.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-w-1`.
<owned_cells>TR-w-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-w1-AC1, TR1-w1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/NFRA_TRNSPT.TO-TR-w1.silver-wipe.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-w1-AC1,TR1-w1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the wipe order, the planted table (class, planted, removed), the residual rule, the silver columns, the pytest lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the event-triggered silver Lambda (PRD section 4) is round 2.
comp-iam: RUN -- infra/aws/terraform/transcripts/main.tf read at the cut: 1 KMS key policy with 2 statements and 1 reader principal (arn:aws:iam::313476888478:user/Andrew_Berman, the var.reader_principal_arns default), 1 bucket policy with 2 Deny statements (TLS-only, key-only); BLIND: the live IAM plane outside this root was not scanned (0 of the account's roles read). The issuer's real silver build runs under that one grantee; this cell adds no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the real message's cut markers are inlined.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-WIPE, C-WIPE-GATE, S14, section 3 communications item 3; decomposition round 1 cell TR-w-1 and the BRONZE CONTRACT.
