# Advisor Intelligence relationship view: why the performance suite shows only captions

**By:** `4.0.0_SA_CRO~DELL1`, 2026-10-13, ~13:4xZ. **Asked:** Andrew-direct ~13:3xZ, relayed by `1.0.0_SA_CTO~DELL1` msg 4848:
"there is a performance reporting suite that seems to have nerver been connected in the relationship view on Advisor Intelligence. I
want you to send CRO to explore what is going on here".
**Method:** read-only. I read the portal source on DEV and PROD, the register row, the producer and publisher code, and made live
AWS reads of the publisher schedule, its run document, and the served S3 prefix. I did not render any page.

## 1. The answer

The suite is a finished frontend over a data feed that was **deliberately never switched on**. It was built by `ADVI_PERFRP` in
August.
- The cards fetch per-firm "perfrp" files.
- The programs that compute those files exist.
- The scheduled publisher that would serve the files is DISABLED, and the document it would run does not exist.
- Andrew's 2026-08-25 hold keeps publication off "until we know the data pipeline and all underlying data is verified end to end".

When a file is missing, a card renders only its caption and subtitle, by design. Only 3 of the files were ever published, by hand,
on 2026-09-01.

## 2. Which project built it

- **`ADVI_PERFRP`**: "49 Financial performance attribution and reporting per client", meant to be comparable to Black Diamond's
  Performance Reporting dashboard.
  - Register row: `org/projects/ADVI_PERFRP.json`. It reads fabric **laptop**, status active, dep_stage EXECUTING, round 1.
  - The last substantive record is 2026-08-31 to 09-01 (commits d363a16ffa and 5e11737907); there is no round analysis.
  - PRD: `docs/architecture/ADVI_PERFRP_PRD.md` v0.3, approved by Andrew on 2026-08-24.
- **The laptop CRO's box report today** (`BOX_STATUS_REPORT_laptop_20261013.md`) recommends **PARK**. Its reason: the spine project
  `ADVI_49F` was closed on 2026-10-07 "as an old vision", and the same question should be asked of this one.

## 3. Each card: what it reads, the producer, and whether the data is served

The served tier is `opal-data-portal-v2/platinum/advi/49financial/`, routed by `shared-advisor-router` v14 (P4R-3). Producers live in
`data/assets/scripts/gold/runners_49f/` (18 `perfrp_*` files). The served listing under `.../perfrp*` was read at ~13:45Z.

| Card | File it fetches | Producer | Served today? |
|---|---|---|---|
| Activity Summary | `perfrp_activity_{relationship,account}.json` | `perfrp_activity_*.py` | **no** |
| Performance | `perfrp_performance_{relationship,account}.json` (`getPerfrpPerformanceLeaf`) | `perfrp_performance_*.py` | **no** |
| Allocation | `perfrp_allocation_*.json` (`getPerfrpAllocationLeaf`) | `perfrp_allocation_*.py` | **no** |
| Gain/Loss (shown only when its file exists) | `perfrp_gainloss_*.json` | `perfrp_gainloss_*.py` | **yes**: account and relationship, hand-published 2026-09-01 03:16-03:17Z |
| Transactions | `perfrp_transactions_relationship.json` | `perfrp_transactions_relationship.py` | **no, and it never will be in this form** (see note 2) |
| Book view | `perfrp_book_advisor.json` | `perfrp_book_advisor.py` | **yes**, hand-published 2026-09-01 07:27Z |

Notes on the table:
1. **The listing.** All files under the `perfrp` prefix total 3. A listing of `platinum/advi/49financial/` was the positive control,
   and it returned `_manifests/...` keys. The new 49 Financial bucket (`opal-data-49financial`) and `opal-data-bd` both read 0 under
   every candidate perfrp prefix.
2. **Transactions.** Its registry entry carries `deferred` (`d_publisher_port.py:179-184`). It is never published as a firm-wide
   file. Serving waits for a per-relationship paged form, "deferred to round 2 fan-out (CTO 67106(2))". Round 2 never ran.
3. **The two notes Andrew saw on the Transactions card.** These are ruled column absences, mirrored from the PRD amendment
   (`portal/src/pages/AdvisorIntelligence/_shared/perfrp/cards.ts:146-190`):
   - **"Description" is `NO-SOURCE-TODAY`:** an ordinary gap that can be re-opened when a source turns up.
   - **"Notes" is `PII-EXCLUDED-PERMANENT`:** a boundary. Every candidate source is client-sensitive, and one is wire instructions.
4. **Data limits recorded at build time.**
   - **Performance:** it was not computable for 529 of 529 accounts. Daily time-weighted return was refused at the frontier
     (`cards.ts` header).
   - **Roster:** 6 of 8 columns have no field in the served type, which is a producer and schema gap (register `blocking`,
     2026-08-31).
   - Neither has been re-measured since.

## 4. Why nothing is served: the switch is off, three ways

1. **The schedule is off.** The `advi-49f-publisher` schedule is **DISABLED** (live `get-schedule`; last modified 2026-08-19;
   `cron(15 13 * * ? *)`).
2. **The run document is missing.** `advi-49f-publisher-dispatch` **does not exist** (live `describe-document`: InvalidDocument). The
   dispatcher refuses any document not on its allowlist (`infra/aws/terraform/opal-assets/advi_49f_publisher.tf` header).
3. **Andrew's hold is still standing.** Andrew-direct 2026-08-25 ~08:5xZ: "I'm fine with it on PROD, let's just get the data part
   sorted." The tf header records that the branch half of his hold was released. The data half, "until we know the data pipeline
   and all underlying data is verified end to end", stands, "and PERFRP publication is inside it". A manual publish needs both
   `--publish` and `OPAL_ADVI_PUBLISH_GRANT=1`.

## 5. DEV versus PROD

- **Both branches carry it.** Portal `origin/DEV` and `origin/PROD` each hold the 13 files under
  `src/pages/AdvisorIntelligence/_shared/perfrp/`. The last PROD change there was 2026-10-07 (77335a21, MDPF_SECCLASS allocation
  labels). `AdvisorBookView.tsx` (83 references), `AdvisorBookClientDetail.tsx` and `AdvisorBookAccountModal.tsx` mount it.
- **On PROD, partner advisors very likely see the same captions-only cards.** That includes the internal notes `NO-SOURCE-TODAY` and
  `PII-EXCLUDED-PERMANENT`, on the 49 Financial Books tab, a client-facing surface. This is **inferred from source, not rendered**.
- **What the earlier diagnosis said.** The register's 2026-08-31 entry showed the same captions-only state on DEV. It found two
  separate causes for the empty cards, as summarized there: no published files, and a schema gap in the roster.

## 6. How it touches this week's work

- **ADVI_BDPRCE** (registered today): every figure the suite would show rests on the Black Diamond prices and lot values that
  project is correcting. Andrew's constraint applies directly: no estimate in a served performance figure. The 13% of capped lots
  read UNVERIFIED.
  - Publishing the Performance, Gain/Loss or Activity cards before BDPRCE's FWD-8 and FWD-9 would serve figures he has just ruled
    out.
  - The two Gain/Loss files already served are dated 2026-09-01 and pre-date both the cap ruling and the pricing findings.
- **ADVI_FIRMBKTS:** it moved 49 Financial's data to its own bucket yesterday. Its flip commit (69679b90e3) is the last change in
  `runners_49f/`. Any revival has to re-read the producers against the new home.

## 7. Proposed next step (for Andrew)

1. **Decide whether the suite is wanted at all.** The laptop CRO recommends PARK pending the same "old vision" question that closed
   ADVI_49F. I agree it should not be driven this week: its figures depend on ADVI_BDPRCE landing exact prices and lot data first.
2. **If it stays, close it properly, after BDPRCE's exact-data cells.** That means a `/closer trace` of the relationship view, which
   is read-only and needs no word. The trace grades each hop: card, then fetch, then router, then served file, then publisher, then
   producer, then source. The publisher switch stays behind his hold until the data is verified.
3. **Now, either way: decide what partner advisors see on PROD.** The four empty cards, with their internal notes, are very likely
   visible. Hiding them until they are served is a client-facing PROD change and needs his word. Leaving them is also a choice.
   This brief does not decide it.

## 8. Not checked

- No page was rendered on DEV or PROD, so what a 49 Financial login actually sees is inferred from source.
- No producer was run. Whether today's data would compute Performance (529 of 529 refused in August) is not re-measured.
- The three open order files the laptop report counts for ADVI_PERFRP were not read.
- The two served Gain/Loss files were not opened.
