```json
{
  "project": "NFRA_SPMOVE",
  "directive": "D9",
  "fabric": "laptop",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/schwab-trn-sharepoint-export-brief-20260916.md@d5e870fed2",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6"
  ],
  "status": "DRAFT"
}
```

# NFRA_SPMOVE - AWS to SharePoint file movements as a pattern; first instance: Schwab transactions as monthly workbooks

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO`. Directive D9, Opal Workflows; macro NFRA; execution fabric laptop.

Andrew commissioned it at this terminal 2026-09-16 ~19:4xZ ("a small project") on `4.0.0_SA_CRO~G`'s brief, which carries
his five inputs verbatim: an AWS folder on the main Opal SharePoint whose paths follow the AWS path structure; Schwab
masters 08242234 and 08335338 only; monthly workbooks, separate per master, all 140 columns; standing and daily, about
fifteen minutes after the Schwab pull; Menachem as recipient only after several clean days on his word. He confirmed the
six endpoint outcomes at this terminal 2026-09-17 ~19:0xZ ("3 approved"), record @57a15b2bbe.

**The product:** Andrew opens one spreadsheet per Schwab master per month on the Opal SharePoint site and reads every
transaction in it. Each morning yesterday's rows are already there. Nobody runs anything.

The header stays DRAFT until both halves are signed at L4-R. The author signs neither half.

## Scope and evidence boundary

**This project owns:** the producer that rebuilds a month's workbook from silver into a builder-named S3 home; the bounded
Gateway capability that replaces that object in place under SharePoint's `AWS/` folder; the run record; the SharePoint
path rule as a naming-canon addition; the recipient switch.

**It relies on and does not change:** the Schwab silver tables and their producers; the completion markers; the Gateway's
sign-in, tiers, guard and audit; `lib/opal_naming.py`'s `address()` and `name()`; NFRA_OPLGTW's reader roles, which are
**never widened for this**.

**Explicitly NOT this project's:** de-duplication across masters (Andrew chose separate files, so the 99.98% overlap is
expected, not a defect); any change to `dim_transaction`; vendor egress (SharePoint is Opal's own tenant through the
existing Gateway); NFRA_OPLGTW's Schwab tools; a general-purpose SharePoint write tool.

**Evidence boundary.** The brief's substrate was measured 2026-09-16 against the repo and live S3 reads; the SharePoint
site choice ("the main Opal sharepoint" = `sites/OpalCapital`) is **this seat's reading and is confirmed at L5, not
assumed**; completion markers exist only from 2026-08-31, so any claim about marker behaviour before that date is
UNMEASURED.

## ENDPOINT (step 2, /endpoint --forward)

`org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_SPMOVE_ENDPOINT_FORWARD_20260916.md` @8d5995ec46, six outcomes, confirmed
by Andrew ~19:0xZ 2026-09-17. FWD-1, FWD-2, FWD-4, FWD-5 and FWD-6 bar at EXERCISED; FWD-3 bars at APPLIED.

## CONTRACTS

**C1 -- the workbook.** One file per master per month, holding every transaction of that month with all 140 source
columns from `fact_trn`, rebuilt from silver and never hand-assembled. A row in the workbook matches its source row field
for field. Masters are never merged and nothing is de-duplicated.

**C2 -- the trigger is the MARKER, never a clock.** The rebuild fires on the completion marker
`schwab/{master}/meta/complete/date=YYYY-MM-DD.json`, about fifteen minutes after it lands. A late pull means a late
update, not a missing one. **Two measured irregularities the design must tolerate, both named in the brief: a marker that
arrives on the SECOND fire of the day (2026-09-11), and a marker REWRITTEN later the same day reporting zero tables
(2026-09-15).** A rewritten or zero-table marker never produces a half-written workbook: the run either rebuilds the whole
month or leaves the previous object in place and records why.

**C3 -- the address is builder output.** The S3 home is `address(...)` output and the resource names are `name(...)`
output, never typed (Rule 30). The SharePoint path is `AWS/` + the builder's key, then the object -- the mirror rule
Andrew confirmed. **`NAMING_SCHEMA.json` carries no SharePoint grammar today; adding it is this project's own cell,
ratified through LGIC_NAMING's schema bump, never a rider on LGIC_ENFORCE.** The tier (platinum vs gold) is a canon
question answered at L5 against `infra/logic/02_DOCTRINE.md`, not assumed here.

**C4 -- the write capability is BOUNDED.** The Gateway's existing `upload_text_to_site` writes small text and never
overwrites; this export needs a binary workbook of tens of MB replaced daily. The new capability is a large-file upload
session that may REPLACE **only under the `AWS/` folder**, and may not write anywhere else on the site. Rollback is
SharePoint version history.

**C5 -- the run record.** Every run records which days it read, how many rows it wrote per day, the source vintage and the
outcome. A short file on a quiet day and a short file from a failure are distinguishable from the record alone, without
opening the workbook.

**C6 -- the recipient switch is OFF until Andrew's word.** Menachem receives nothing while the files are being built and
checked. A send attempted before the word is REFUSED, and the refusal is recorded. His word is recorded when given, and
only then does delivery begin.

**C7 -- the pattern, not the instance.** Dataset, masters or firm, period and columns are INPUTS. The trigger, the address
rule, the write capability, the run record and the recipient switch are the pattern. The second delivery is a
configuration change with no new build, and FWD-6 is what proves it.

## SURFACE MANIFEST

| id | surface | what it is | outcomes |
|---|---|---|---|
| S1 | the producer | marker-triggered rebuild of a month's workbook from `fact_trn` into the builder-named S3 home | FWD-1, FWD-2 |
| S2 | the delivery capability | the bounded large-file replace under SharePoint `AWS/`, through the Gateway | FWD-1, FWD-3 |
| S3 | the address rule | `address()`/`name()` output plus the `AWS/` mirror, and its NAMING_SCHEMA addition | FWD-3 |
| S4 | the run record | per-run days read, rows written, vintage, outcome | FWD-4 |
| S5 | the recipient switch | off by default; refusal before the word; recorded enablement | FWD-5 |
| S6 | the configuration surface | dataset, masters, period and columns as inputs | FWD-6 |
| S7 | the read role | scoped to exactly the two masters' `fact_trn` and this project's output prefix | all |

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A1 | one month's workbook opened by Andrew; one row compared field-for-field with its source row; his word that he used it instead of asking for a pull | FWD-1 |
| A2 | two consecutive mornings' files and run records, one of them following a pull that completed on its second fire | FWD-2 |
| A3 | the SharePoint path of a delivered object equals `AWS/` + the builder's key, shown for two different inputs; the rule is IN the naming schema | FWD-3 |
| A4 | two run records read side by side -- a quiet day and a failed/short day -- distinguishable without opening the workbook | FWD-4 |
| A5 | one refused send before the word, the word recorded, then one delivered send | FWD-5 |
| A6 | a second dataset or the second master delivered by changing inputs only; the diff shows no new build | FWD-6 |
| A7 | a rewritten or zero-table marker produces either a whole-month rebuild or no change plus a recorded reason -- never a half-written workbook | C2 |
| A8 | the write capability refuses a path outside `AWS/`, and the refusal is recorded | C4 |

## Canonical handoff

L5 is `2.0.0_SA_COO`'s on a lane `0.0.0_AB_MSTR` seats. **This project is NOT in Andrew's 2026-09-17 seat order** (IRPT_BCKEND,
NFRA_MCPINDEX, MDPF_TAXSMA), so it takes a lane only when he places it or one frees past those three. First cells: confirm
the SharePoint site and the tier (C3), then the producer (S1), because the delivery capability (S2) is only worth building
once the object it delivers exists.
