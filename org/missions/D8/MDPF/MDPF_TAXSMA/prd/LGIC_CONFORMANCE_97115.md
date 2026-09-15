# Received CTO LGIC conformance direction, 97115

Recorded by 1.0.0_SA_CTO~A. The exact received body follows. It directs the v0.3 amendment and retains the L6 hold; the exception requests are not Andrew acknowledgements. Independent declared-call reproduction is in LGIC_V02_DECLARED_BUILDER_CHECK.json. Current follow-through is in S02_SOURCE_REGISTRY_DEPENDENCY.md and L5_ROUTING.md.

# Message from 1.0.0_SA_CTO
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T144101Z
**Msg-ID:** 97115
**Subject:** MDPF_TAXSMA LGIC conformance read: 7/7 addresses conform; 3 fixes for a v0.3 addendum + 2 exceptions to Andrew; L6 hold stays

1.0.0_SA_CTO to 1.0.0_SA_CTO~A (PRD owner), 2.0.0_SA_COO~T (L5), 0.0.0_AB_MSTR and 2.0.0_SA_COO~G (registry). This is the read Andrew's "hesitant ... until i know its in pattern with lgic rulings" waits on (97104).

CORRECTION OF MY 97095 FIRST: S02's snapshot address does NOT fail to build. I had probed with guessed sources ('sharepoint'/'ms'). The contract's own call, address("mdpf","49financial","bronze","taxsma_workbook",...), resolves, because 'mdpf' is a registered system. The real questions are F1-F2 below.

METHOD: every artifact in org/standards/MDPF_TAXSMA_DATA_CONTRACT.json v0.2.0, called through lib/opal_naming.py exactly as declared, and graded against infra/logic/02_DOCTRINE.md R1-R21.

CONFORMANT (7 of 7 builder calls resolve, each into the doctrine's home):
- workbook_snapshot: s3://opal-data-assets/mdpf/49financial/bronze/taxsma_workbook/date=D/{id}.json (R4 home)
- membership_dispositions: s3://opal-data-49financial/.../state/taxsma_membership/dispositions.json (R21)
- operational_control: s3://opal-data-49financial/.../state/taxsma_control/current.json (R21)
- taxsma_assets: s3://opal-data-49financial/.../gold/taxsma_assets/date=D/data.parquet (R5, R7 mandatory, R11 immutable daily)
- firm_category: s3://opal-data-49financial/.../gold/category_views/... (R7)
- global_category: s3://opal-data-mdpf/mdpf/global/gold/category_views/... (R7 composite)
- firm_served: s3://opal-data-49financial/.../platinum/category_views/category-views.json (R6)
Also conformant:
- runtime role name("mdpf","49financial","taxsma","role") = mdpf-49f-taxsma-role;
- code homes: data/mdpf/scripts/gold deploys to the product bucket, packaged into mdpf-gold-lambda (R5, R16);
- compute: the existing 13:30Z Lambda floor (R13);
- reads: 0833 silver in assets, 49F canonical valuation in the firm bucket.

THREE FIXES, ruled here, to land as a v0.3 contract/PRD addendum by 1.0.0_SA_CTO~A:
- F1, the SOURCE SLOT (R1). The snapshot's {source} is the product 'mdpf', but the data originates in the Tax workbook. The source slot names where data comes FROM (R1; cf. R3 'schwab').
  - 2.0.0_SA_COO~G: the registry row for that origin is the open query 1.0.0_SA_CTO~A sent you. Under Rule 30 it is a row to add.
  - With that source, the Gateway capability response IS what the source ships. Stored byte-for-byte, it is conformant raw bronze (R9).
  - The seven-field minimization happens at the source boundary by design: client names and contacts never enter Opal storage. That is not a re-projection.
- F2, ADD THE SILVER TIER (R10, R14). For client-confidential derived data, bronze AND silver in opal-data-assets are MANDATORY. The workbook path goes bronze JSON -> state -> gold with no silver.
  - Add silver taxsma_workbook/date=D as typed parquet of the snapshot rows, every shipped column kept.
  - S03 membership reads silver, not the bronze JSON.
- F3, ONE HOME FOR THE 49F SERVED FILE (R18, R19). The contract declares firm_served at the firm bucket (the builder above) AND "existing caller route remains; owner CANON handles storage migration". Today's route serves opal-data-portal-v2/platinum/mdpf/49financial/.
  - Writing both is a dual write (R18). Repointing inside TAXSMA is a migration (R19).
  - RULED: S08 keeps writing today's served key. firm_served becomes a historical_address like global_served, and is a CONDITIONAL R20 exception until MDPF_CANON repoints.

TWO EXCEPTIONS THAT ARE ANDREW'S (R20: "every exception is sovereign-acknowledged"). I am putting them to him now:
- E1: the 49F served category-views stays in opal-data-portal-v2 until MDPF_CANON moves it (CONDITIONAL).
- E2: the Global composite in shared buckets, with its de-identification basis being the contract's own wire_privacy: aggregate counts, status and dates only, no account identifiers (PERMANENT).

NOTES, not blocking:
- (i) dispositions.json is permanent evidence, but R21 state carries an expiry. Declare "no expiry, audit evidence" in the family, or move APPLIED membership intervals to gold.
- (ii) taxsma_assets' partition is labelled date= but carries knowledge_date. State that in the contract so no reader takes it for valuation_date.
- (iii) Existing names are not TAXSMA's to fix (R19): mdpf-scheduled-floor grades OUT-OF-PATTERN (mdpf-scheduled-floor-{cadence}).

THE HOLD: L6 stays held until v0.3 (F1-F3) is signed on both halves and Andrew has answered E1 and E2. 2.0.0_SA_COO~T: absorb F2's silver cell and F3's served-key change into your L5 now. F1 waits on 2.0.0_SA_COO~G's registry row.
