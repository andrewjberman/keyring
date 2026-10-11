# AMGT_RESAPP task order -- `AMGT-bc-1` -- READ, DO NOT CHANGE: DOES THE STORED BLOOMBERG DATA FOR THE LISTING OF SAN FP AND CSL AU CARRY A SECTOR OR INDUSTRY FIELD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~392</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bc-1.read-whether-the-stored-bloomberg-data-for-the-listing-carries-a-sector</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only reading; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads (S3 GET and DynamoDB GetItem of already-landed objects) with the caller's own credentials; no write and no Bloomberg call.
comp-adversary: RUN at the cut -- r96_sector_reading_check.py reads NO at the base (no reading exists) and YES against a throwaway sample reading that carries every heading, three denominated sources, both listings, a census, a control, two read surfaces and one not read, one OUTCOME and the two NONE lines.
EGRESS CLASS, declared: NONE (no Bloomberg call; stored objects only).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-392` (branch `wk-AMGT_RESAPP-392`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-392`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-bc-1` (round 96, decomposition s.104): A READING, NOTHING CHANGED

CTO~DELL1 round-95 analysis item 1. The classifications table is keyed by the BARE Bloomberg ticker; `CSL` is Carlisle and `SAN` carries a legacy 'Health Care' under a Santander-cleaned
name, so the page now says "classification not available for this listing" for `SAN_FP_Equity` (Bloomberg ticker `SAN FP`) and `CSL_AU_Equity` (`CSL AU`). The next question is whether the
STORED Bloomberg-fed data for the LISTING (the exchange-qualified security, not the bare ticker) already carries a sector or industry value, so a classification could be served from it
with its source named. Answer it by reading, and write ONE reading to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~392/BC1_LISTING_SECTOR_READING_20261011.md` in the shape `checks/r96_sector_reading_check.py` grades (its docstring is the template; headings
Sources, Listings, Census, Control, Surfaces, Outcome, Not changed).

HOW (the law says search the estate with its own tools, never blind recursive grep): start with `comp-which "<the question>"` and `comp-estate --layers`, then `comp-find` for the field
words with `-i` (`GICS`, `sector`, `industry`, `BICS`) and print the denominator; read a named file with `comp-read <path> --for "<question>"`. Candidate surfaces to read, each only if it
exists (say so if it does not): (a) the stored research MODEL BLOCK of each key (`lib/research/api/scoped_amgt.py::_read_model_block_pool(security_key)` returns the block and its record;
read its header and any field whose name matches the words above); (b) the identity crosswalk record of each key (`lib/research/identity/crosswalk.py`, `resolve_identity`); (c) the
classifications table rows for the bare tickers `SAN` and `CSL` (GetItem; all fields); (d) any landed Bloomberg REFERENCE-DATA table for equities in the data pool (silver or gold) that the
census finds; (e) the Bloomberg field dictionary in `integrations/bloomberg/` only to name which mnemonics are sector-class (`GICS_SECTOR_NAME`, `GICS_INDUSTRY_NAME`,
`GICS_INDUSTRY_GROUP_NAME`, `INDUSTRY_SECTOR`, `INDUSTRY_GROUP`, `BICS_LEVEL_1_SECTOR_NAME` are examples, not a closed list). Run the SAME sweep over a CONTROL listing that is served with
a sector today (`BA_US_Equity`: the table says 'Industrials'): if the sweep cannot see the control's field, the absence for the two listings proves nothing and the reading says so.

**THE LESSON OF `integrations/bloomberg/READ_HERE.md` section 4, applied: a clean zero measured inside one surface says nothing about the surface next door.** Name, under `## Surfaces`,
every surface you read and at least one you did NOT, and never write SECTOR-ABSENT from one surface.

OUTCOME tokens: `SECTOR-SERVED` (both listings carry a sector value, source and field named), `PARTIAL` (one does), `SECTOR-ABSENT` (neither, with the census denominator and the control
shown). For SECTOR-SERVED or PARTIAL name the `SERVE-FROM:` source and field. A fix or a serve is NOT part of this order: it is cut only after the reading, as its own cell.

WRITE NOTHING anywhere but the reading file and, if a premise fails, a surprise row. **NO BLOOMBERG CALL OF ANY KIND** (no `bloomberg_health`, no `reference_data`, no
`blp_client`, no terminal sign-in): Bloomberg is reached only through its queue and never by this order; the reading is of already-landed objects.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W392-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (S3 GET, DynamoDB GetItem, local file reads). No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`. Never mint `data/bloomberg/`.
3. Standing: no push of shared branches.
4. 49 Financial data never goes into another firm's tree; the reading names no client, firm or account.
5. A surface you cannot read is a finding in the reading (`NOT READ: <why>`), never a reason to guess.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~392/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bc-1"><invocation>cd C:/dev/wk-resapp-392 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round96_prep/checks/r96_sector_reading_check.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~392/BC1_LISTING_SECTOR_READING_20261011.md"; echo "exit=$?"</invocation><expect>PASS S1 (every heading present, in order, non-empty), PASS S2 (at least three sources, each with an n= denominator), PASS S3 (both listings carry FIELDS and SOURCE), PASS S4 (the sweep's denominator and matches), PASS S5 (a control shows the sweep sees a sector field), PASS S6 (at least two surfaces read and one not read), PASS S7 (exactly one allowed OUTCOME), PASS S8 (WRITES: none and BLOOMBERG CALLS: none); R96 SECTOR READING SHAPE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~392 <0.9.0_WK_AMGT_RESAPP~392@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~392/AMGT_RESAPP.TO-AMGT-bc-1.read-whether-the-stored-bloomberg-data-for-the-listing-carries-a-sector.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC2 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- criterion AC1's output lines;
- the reading's OUTCOME line and the FIELDS line of each listing and of the control;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-95 analysis `ledger/ROUND_ANALYSIS.round95.md` section 3 item 1: "A classification for SAN FP and CSL AU from an exchange-qualified source (round-94 ADDENDUM 1). First, read only: does the served Bloomberg block for the LISTING already carry a sector or industry field (`comp-which` first)? If yes, serve it with its source named, under its own redeploy pair, measured route by route. If no, the withheld state with its reason IS the outcome, and the cell closes on that read." READ: the serve is NOT cut now (it depends on the read and rides AMGT_CORPUS's /13 pair, because the next scoped-api redeploy from a merged pin carries their corpus files: the CTO's round-95 note 2). AC2 is the CVO's judgment (the outcome follows from the evidence, the control and the named surfaces). `AMGT-bc-2` (the serve, conditional) and `AMGT-bc-3` (ss-7 / pp-4) are STAGED, no order.

<status>complete -- 2026-10-11T19:03Z by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-392 @60a45d6d6c (reading @755ecf5f56) merged @91ad4b03f2, proof instance VALID; issuer re-run: AC1 R96 SECTOR READING SHAPE YES (8 of 8; the base read NO). OUTCOME: SECTOR-SERVED. The issuer's OWN read of the three stored model blocks (S3 GET): derived/model_block/SAN_FP_Equity/20261011T130935Z figures[3] {mnemonic GICS_SECTOR_NAME, value 'Health Care', source bloomberg-dapi}; CSL_AU_Equity/20260930T093804Z figures[3] the same value; the control BA_US_Equity/20261011T130241Z 'Industrials'. Stated by the reading: the field dictionaries hold exactly one sector-class mnemonic (GICS_SECTOR_NAME); no GICS_INDUSTRY_*, BICS or INDUSTRY_SECTOR is in them; bestdata, segments, identity, exec_officers, histdata, silver/listing_hit and the equity reference tables of opal-data-assets were NOT read; CSL AU's stored objects end 2026-09-30 (model block) and 2026-09-19 (refdata). Rows W392-S1..S3 INERT. AC2 (the outcome follows from the evidence, the control and the named surfaces) is the CVO's judgment. Nothing was written; no Bloomberg call.</status>
<round>96</round>
<slot>0.9.0_WK_AMGT_RESAPP~392</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
