# AMGT_CORPUS task order -- `CRPS-al-3` -- ROUND 36: the units judgment read (one non-USD name, one field per family x 3 names)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-al-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 get/list of the served model blocks only, through scoped_amgt.read_model_block.
comp-adversary: RUN by the issuer at the cut -- al3_check.py build 0/2 (file absent). Blind spot: the check grades the read's SHAPE; whether each verdict is right is the CVO's judgment (AC2).
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY. NO Bloomberg call, NO vendor call, NO write anywhere but your deliverables folder.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 36.

## 1. THE CELL -- `CRPS-al-3`

Round 35 gave the 52 round-34 mnemonics measured units: each was placed in a unit family of
`integrations/bloomberg/research/build_unit_map.py` from its landed values, and the 96 served model blocks were re-derived. The
CVO's sample over BA read 51 of 52 against filed figures. Two things were NOT read, and this cell reads them:
- whether the families hold ACROSS names (one field per family on three names), and
- one non-USD name's currency labels.

**The 8 families** (round 35): TEXT, DATE, YEAR, PERCENT, ABSOLUTE_OR_MILLIONS, SHARE_COUNT_MILLIONS, PER_SHARE, RATIO. Read each
family's member list from `build_unit_map.py` (the module's family constants; DATE and YEAR were added in round 35).

**The three names:** `BA_US_Equity` (USD), `TSM_US_Equity` (a US-listed ADR whose filings are not in USD), `SAP_GY_Equity` (EUR).
Read each name's newest served block with `lib.research.api.scoped_amgt.read_model_block(<key>)`. Its S3 key is
`derived/model_block/<key>/<stamp>/model_block.json`; name the key you read once per name in your file.

**Write `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/R36_UNITS_JUDGMENT_READ.md`:**
1. **The family table**, one row per (family, name), 24 rows, each exactly 7 cells:
   `| <family> | <security_key> | <MNEMONIC> | <served unit> | <served value> | <basis words> | <verdict> |`
   - pick, per family, ONE member mnemonic that has a served figure on the name where one exists (prefer the same member across
     the three names);
   - `<basis words>`: the producer's `FIELD_BASIS` text for that mnemonic (`integrations/bloomberg/research/model_block_pull.py`),
     shortened;
   - `<verdict>`: `RIGHT` when the served unit and the value's magnitude agree with Bloomberg's definition (cross-read a sibling
     figure where it helps, e.g. a market cap against price x shares, a margin against its numerator / denominator);
     `WRONG` when they disagree; `CANNOT-TELL` when no served figure exists (YEAR: `EQY_FUND_YEAR` landed no value on any name)
     or the values cannot decide. Each row's last cell before the verdict, or a line under the table, says WHY in one sentence.
2. **The currency section** for `TSM_US_Equity`: for each of its figures among the 52, whether its currency label (the figure's
   `currency` and the block's `currencies` entry) is right for what the number is (a price-based figure in the quote currency, a
   statement figure in the filing currency). End with ONE line, exactly:
   `CURRENCY TSM_US_Equity figures <n> labelled <k> right <r> wrong <w> cannot-tell <c>`, where n = its figures among the 52,
   k = those you graded (k must equal n), and r + w + c = k.
3. A short closing note: any WRONG, what it would take to fix, and the family it touches.

## 2. BOUNDS

1. READ ONLY. NO Bloomberg call, NO vendor call, NO S3 write, NO code change.
2. Only the files in `<paths>` change.
3. Write with the Edit/Write tools. ASCII only. Run python from your worktree root as `PYTHONPATH=<worktree root> python ...`; a
   read script, if you write one, goes under your deliverables folder.
4. A WRONG verdict is a finding for the analysis, not a fix: also file it as a row `AMGT_CORPUS-Z-W2-S<k>` (next free k across
   every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-al-3.units-judgment-read.md
</paths>

Read-only: the whole repository, in particular `build_unit_map.py`, `model_block_pull.py` (`FIELD_BASIS`), the committed
`integrations/bloomberg/research/field_map.json`, and the issuer's check under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-al-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/al3_check.py"</invocation><expect>(?m)^al3 build 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-al-3" judgment="true"/>
</proof_of_spec>

- AC1: the read is complete in shape (24 family rows, the 3 block keys named, the CURRENCY line with k = n).
- AC2 (JUDGMENT, graded by the CVO at L9): each verdict is right. Record it as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason`
  naming `3.0.0_SA_CVO~Z`; no verdict.

## 5. WHEN YOU ARE DONE

1. Write the instance at
   `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-al-3.units-judgment-read.proof_of_spec.json`,
   then run `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>` AFTER your final commit. It must
   return rc 0.
2. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME commit as your instance.
3. Report ONCE: the count of RIGHT / WRONG / CANNOT-TELL over the 24 rows and over TSM's currency labels, every WRONG with its
   evidence, AC1's output line, your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-35 analysis @`02bbbc0208` s.3 ruling 2 + s.4 item 2; ADJUDICATION_v41 s.2 ("not read: a non-USD name, and
the per-family sample across names"). Base: al3_check build 0/2. SAP_GY_Equity block present (raw 20261004T130908Z).
<risk>LOCAL</risk>
<status>pending</status>
<round>36</round>
<slot>~2</slot>
<fabric>site-z</fabric>
