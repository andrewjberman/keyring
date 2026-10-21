# RESEARCH 2026-10-21 -- NFRA_FIDUPL: how Wealthscape scopes per firm (the G switch does not)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8998 (self-drive design fork; the CTO rules the mechanism on
this record).
**Given (box probes 2P/2Pv2/2G/2Gv2):** switching the current G changes nothing in the data -- `accountList.json` returns available=5204
under every G; the Export Status list carries the same six file ids; `account.txt` is byte-identical across three G's.
**This record (HARs + UI bundle, no sign-in):** what the G actually scopes, and whether a per-firm export scope exists. Names only.

## 1. What the G number DOES scope -- a service/reporting context, not accounts

Only two calls in any HAR carry the G as a parameter (M):
- `GET /ssc/cst/wc/channel/cst/view?gNumber=...` -- the CST (alerts / customer-service / platform) view.
- `GET /ssc/account-documents/wc/channel/api/v1/statements/getDocumentsSearchResult?accountNumber=&gnumber=...` -- statement-document
  lookup, per account + G.

**No account-membership call is G-scoped.** `accountList.json`, `findClients.json`, the export list and the export files take no G and
return the whole book (confirmed by the box). The `book-of-business` home tile (keys `numberOfAccounts`, `assetsUnderAdministration`,
`primaryAccountHolder`, `asOfDate`) is the ONE untested per-G candidate -- it reads like an advisor-book summary and MIGHT vary per G;
worth one box check (switch G, re-read the tile), but every captured account-data call does not vary.

**Conclusion:** the G number is a **reporting / service-desk context** (which alerts and statements you see), **not an account grouping
key.** The firm split cannot be driven by the G switch. This is the mechanism finding.

## 2. Where a per-firm scope DOES exist -- Wealthscape account GROUPS

The entitlements carry a full **account-Groups** feature (M, from `entitlements.json` / `containers.json`):
`Create a Group`, `View Group`, `Group`, `Group Access Layer`, `Group Import`, `Group Summary`, and (earlier) `Export Groups` /
`ExportGroups`. The Custom export wizard's step 3 is "Choose Filter."

So **a per-firm export is possible via account Groups, not via G:** define one Group per firm (its accounts), then run a Custom export
filtered to that Group, or export the Group list. The group-filtered export calls are **not captured** (the wizard step 3 ran in an
un-recorded pop-up), so the exact filter call needs one capture.

## 3. The firm-split mechanism -- recommendation (the CTO rules)

The G sweep is out. Two viable mechanisms, in order:

1. **Attribute/crosswalk attribution (works today, no new capture).** Already measured
   (`RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md`): join the landed account numbers against the per-firm sources Opal
   already holds -- Orion (Inflection), Black Diamond (Cottonwood, 49F). That attributed **1,418 of ~5,000 with 0 conflicts**; the rest
   are unclaimed (the non-registry firms + unseen). This is the **immediate** split path and needs nothing from Wealthscape. Its gap is
   coverage (the firms we have no source for).
2. **Wealthscape account Groups (native, full coverage, needs setup + one capture).** Create one Group per firm inside Wealthscape (a
   configuration act), then a per-Group export or a Group-filtered Custom export. This gives authoritative per-firm membership for ALL
   firms, including the ones the crosswalk can't reach. It needs: (a) the Groups created (an Andrew/firm config task), and (b) one capture
   of the wizard's "Choose Filter" step and a Group export to build the adapter.
3. **A per-account firm attribute in `accountList.json`** (fallback to probe): fields `regRep`, `affiliateInfo` (planName/planNum),
   `fbsiShortName`, `mslaCode` may encode the advisor/firm. In the one captured page `regRep` had low cardinality; the box can re-measure
   distinct counts per field over the full 5,204 to see if any maps cleanly to the 8 firms. If one does, the split is a pure column read,
   no Groups needed.

**REC:** ship the split on **(1) the crosswalk now** for the firms we can source, land the remainder under `alongside/` named as
unattributed (FWD-9 allows this); in parallel, the box measures **(3)** the accountList per-account fields for a clean firm attribute,
and **(2) Groups** is the durable full-coverage answer if (3) has no clean field -- it needs the Groups set up (the one genuine Andrew/
firm step) and one wizard capture.

## Not measured

- Whether `book-of-business` varies per G (one box check settles it).
- The Group-filtered export's calls (un-captured pop-up; one capture needed).
- Whether any `accountList.json` field maps 1:1 to the 8 firms over the full book (box can measure distinct counts).
