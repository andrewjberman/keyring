# L2 endpoint draft -- the MCP as an AWS-CLI shim (for Andrew's confirmation)

By: `1.0.0_SA_CTO~Z`, 2026-10-21 ~14:2xZ. From the brief `docs/briefs/mcp-cli-shim-bounded-query-brief-20261021.md`
@df92b9d9b3 (`4.0.0_SA_CRO~Z`) and Andrew-direct of 13:3xZ and 14:xxZ (records @1ca1fc4dcb, @243c25998e), plus this seat's
record of 2026-10-21 (Menachem). Nothing is cut until Andrew confirms the DONE WHEN lines.

## The thread (round 1 builds it whole)

A person granted the folder `opal-data-assets/schwab/08335338/` asks Claude: "list this account's transactions between
October 1 and October 20" and "how many accounts held DIVZ on Friday, and their total value?"
- Claude lists the folder, reads the table's columns, and runs one query.
- The answer is one page of rows, or a total; never the file.
- The same question against a folder the person is not granted is refused, naming that folder.

## Outcomes

**FWD-23 (NFRA_OPLGTW): list, describe, query -- the AWS CLI over MCP.**
- DONE WHEN, exercised by a granted principal through the served gateway:
  - (a) `list` of `schwab/<master>/silver/` shows every table, as `aws s3 ls` would;
  - (b) `describe` of `fact_trn` returns its columns and types without reading rows;
  - (c) a `query` of `fact_trn` for one account between two trade dates returns at most one page plus a cursor, and the
    row count equals a direct read of the same files;
  - (d) a name filter on `fact_acc` finds the client's accounts;
  - (e) Orion/Inflection `fact_transactions` (1.53M rows, 31 row groups): one account between two dates answers inside the
    engine's memory and time ceilings, without the file loaded whole on the gateway;
  - (f) Cottonwood Black Diamond transactions and fees return their rows, with the MM/DD/YYYY dates parsed (part-1 D2),
    and the count equals a direct read.
  - First cut, per Andrew's ~14:0xZ addendum (brief @8c8fa480de): Schwab, Orion, Cottonwood Black Diamond only. SmartX,
    Eclipse, Commonwealth and the rest are deferred.
- Negative arm: the same query by a principal without the folder is refused by folder name, with 0 reads.

**FWD-24 (NFRA_OPLGTW): the entitlement is a bucket or a folder, per person, and nothing else.**
- DONE WHEN: the owner grants Menachem `opal-data-assets/`, `opal-data-etfs/` and `opal-data-portal-v2/`. He reads under
  them and is refused under `opal-data-harvest/`.
- The contract's per-account, per-column and masked-reference clauses are revised to say they are superseded.

**FWD-26 (NFRA_MCPINDEX): the light index.**
- DONE WHEN: for a plain-words question, Claude picks the right folder and table from the index without listing the
  bucket first. Every indexed table carries its meaning and a size class (small / large / very large), and the size class
  decides aggregate-or-page.

**MCPORTAL:** the `/opalgateway` People panel's channel switch becomes a folder switch (the 10-20 brief's mechanics).

## Andrew's calls (needed before the cut)

1. **Redaction.** At 13:5xZ you agreed to keep tax IDs, mailing addresses, email and phone out. At 14:xxZ you said "We're not
   going to try to redact tables". The CVO adds that a raw text read of bronze carries all four, and that date of birth is
   unclassed.
   - REC: keep the four classes plus date of birth out, by column name in Parquet, and keep bronze out of every grant.
2. **The typed tools** (`client_*`, `schwab_*`, `etfs_*`, `portal_*`).
   - REC: keep them as conveniences until FWD-23 is proven on the thread; retire each one the generic query replaces.
3. **The SmartX mixed-firm folder** (one file holds several firms): deferred with SmartX by the ~14:0xZ addendum. No call now.
