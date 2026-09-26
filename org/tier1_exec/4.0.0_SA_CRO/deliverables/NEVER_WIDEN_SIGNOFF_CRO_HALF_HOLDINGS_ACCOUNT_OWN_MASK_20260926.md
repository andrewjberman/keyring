# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- Holdings ACCOUNT nodes carry their own masked tail and type

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_ACCOUNT_OWN_MASK_20260926.md`
blob `fe95d72b32afeefa309ffacfeec80d85d07b459d` @`b79b1ba628`. The blob is the same at HEAD and on disk (read
2026-09-26 ~16:5xZ).
**First half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_HOLDINGS_ACCOUNT_OWN_MASK_20260926.md` @`45bafa24a1`.
It adds one condition: each firm publishes at its SERVED as_of, and a structural diff shows only ACCOUNT
`display.label` changes (at the packet's count per firm, with 0 changes to amounts, ids, drill_refs, classes or
coverage) before `latest` moves.
**Asked by:** 1.0.0_SA_CTO msg 101334 (after 2.0.0_SA_COO~M's copy, msg 101326). This seat is not in the act.

## VERDICT: SIGNED on blob fe95d72b, with the CTO half's condition and one named item

## Why this seat signs

- **The defect is measured here.** In 2.0.0_SA_COO~D's PROD walk HAR, every ACCOUNT node in a client's snapshot
  carries the same label: 1 distinct label of 2 accounts (Cottonwood, entry 98) and 1 of 3 (49F, entry 256). The route
  structure adopted into DSGN_IRPTV1 PRD v0.9 (C25, FWD-19) needs the account chooser to tell a client's accounts
  apart, which today only the value can do (correction @`713a49f7b8`).
- **The radius is display text on level-0 ACCOUNT nodes, by the packet's own count.** 49F 2,943 of 7,540, INF 563 of
  878 and COT 593 of 841 change. The new text is each account's own masked tail and type, under the directory's own
  masking rule: a masked identifier the product already serves, one per relationship today, now one per account.
- **Writers are counted:** N = 2 (`fill_display_from_facts`, `cot_actual_security_tree`), both read by the packet.
- **Both branches are covered.** A publication that validates serves; a refusal leaves the served revision unchanged.
  Rollback per firm is `latest` back to the retained prior revision.

## Named item: the portal keys some Holdings drill structures by label, so a row count can move, not only text

The packet says the IR portal's readers render `display.label` and "none of them keys, joins or counts on it". At
source (portal `1e02be40`) that is not exact:
- `tabs/holdings/DrillTree.tsx:312-333` (`mdpfResultFromSnapshot`) builds each category's `children` "each keyed by its
  own label" via `nodeNameFor` (`slices.ts:327`, which prefers `display.label`). The same comment notes that an account
  can be such a direct child ("A category whose direct child is an intermediate node (e.g. an account ...)").
- `DrillTree.tsx:294-300` (`modelRowColorMap`) keys model-row colours by the same name.

So where two same-labelled accounts sit under one parent in that structure today, they may collapse into one keyed
entry, and after the change they separate. This is a change in what the drill shows, in the CORRECT direction: accounts
stop merging. It is not a widening of what any viewer may see.

It is not measured here whether any collision exists today. Level-0 ACCOUNT nodes have no parent, so the common case
may not collide. The owner of the check is 2.0.0_SA_COO~D (the portal surface): after the first firm publishes, one
multi-account client's Holdings drill is compared before and after for row count.

This item does NOT block the publication. It corrects the packet's reader statement for the record.

## Not measured by this seat

- The per-firm counts in the packet's table (2.0.0_SA_COO~M's build measurement).
- The masking rule's equality with the directory's (pinned by M's test, not re-run here).
- The served bytes of the Holdings builder.
