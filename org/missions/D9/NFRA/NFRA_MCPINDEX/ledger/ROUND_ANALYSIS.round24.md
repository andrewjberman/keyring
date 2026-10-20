# NFRA_MCPINDEX -- ROUND-24 ANALYSIS (L10 answer; the round-25 list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-20 ~15:4xZ.
**Answers:** `2.0.0_SA_COO~MI`'s slug, msg 36246, and `deliverables/2.0.0_SA_COO~MI/round24/evidence/ROUND24_OPEN_ITEMS.md`.
**Issuer:** `2.0.0_SA_COO~MI`.

## 1. As read

- **7 of 7 orders complete, MAY-CLOSE.**
- **Coverage refusals:** 36 down to 7.
- **Link misroutes:** 10 down to 7. Three of the 7 are `code`, with `2.0.0_SA_COO~O`.
- **Traced `serves` is written.** It removes schwab/49financial from `client_resolve_account`.
- **The catalog is in the repo and NOT deployed.**
- **Battery:**
  - PASS 49, EMPTY-CORRECT 4, PREVIEW-ONLY 1, FAIL 73 of 127.
  - The FAIL count was 85 before this round, so the passes rose by 11.
- **Source compare:** 25 agree, 1 disagrees, 78 unreadable.
  - The 78 split into graph 31, integration 9, store 4, and S3 with no date token 34.
  - The one disagreement is `harvest_query_columns`: its answer is dated 2026-10-09 while its source data ends 2026-10-08.
- **Sheets:** 17 written locally, none delivered.
- **One code fault:** `portal_get_security_scan`, whose reader role lacks `s3:ListBucket`. It is row Z-S436 on COO~O's round-48
  list.

## 2. Rulings on the five open items

- **(a) The `client_*` link lines refused by the naming gate.** Use the GROUP-MAP form.
  - The link names the C-GROUP key (`bucket`, `vendor`, `firm`) once per group.
  - It does not name a firm token per line.
  - These are references to existing rows, not new resource names, so no LGIC exception is needed.
- **(b) The two store rows.** Not accepted as forced.
  - C-GROUP item 1 already admits store words (`dynamodb`, `graph`) and requires the value to be read from the row's own
    source. Typing `opal-data-harvest` onto a scoped-API row breaks that.
  - Fix the emitter's vocabulary to admit the store words, and drop the doubled `dynamodb_dynamodb_` prefix.
  - The scoped-API row names its store as `amgt-scoped-api`, with its route as the table.
- **(c) The SharePoint folder.**
  - Name it `Opal Gateway Cheat Sheets`, in the site that `upload_text_to_site` writes to by default, under the owner's
    permissions. Andrew may rename or move it.
  - The sheets carry tool names and example questions only, never data.
  - Writing to the folder is the generator's act. Sending a sheet to a person stays held for Andrew.
- **(d) Test sends.**
  - The battery grades a `sent` result as PASS when the tester reads the message back in their own mailbox. A send with no
    read-back stays FAIL, of class `send_unconfirmed`.
  - `send_chat_message` is PREVIEW-ONLY, named in the REALIZED line, until a self-chat target is measured to exist. It never
    sends to another person.
- **(e) The re-run on opal-data-assets** happens after batch16 is live (2026-10-21 06:00Z), as ruled.

## 3. The round-25 list (ONE issuance, cap 8)

1. Source compare for the 78 unreadable tools, by class:
   - **graph:** compare with the tester's own mailbox, calendar and files, read directly;
   - **integration:** compare with the vendor's own API read once, outside the gateway;
   - **store:** compare with a direct DynamoDB read;
   - **S3 with no date token:** compare object by key.
2. Fix the `harvest_query_columns` date: the answer must not be dated after its source. A code fault goes to COO~O.
3. The group-map link form, for (a).
4. The emitter's store-word vocabulary and the two store rows, for (b).
5. The test-send grading, for (d).
6. The 7 remaining link misroutes.
7. Write the 17 sheets to the folder, for (c).
8. After batch16: re-run the battery and routing on opal-data-assets.

**The catalog emit deploys in COO~O's next batched release,** named in its ask. A catalog left in the repo serves no one.

Battery concurrency: no more than 2 calls at a time until batch16's guard is live.
