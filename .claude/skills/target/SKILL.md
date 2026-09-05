---
name: target
description: Enrich a company or person surfaced by /find via the Lusha API: `/target <company>` draws the org chart (names, titles, seniority); `/target <person>` returns contact detail (emails, phones -- the credit-costing reveal). Use on `/target ...`, or asks for who works at a firm, decision-makers, or a person's contacts. Paid calls are confirm-first. Driver data/find/dualbiz/scripts/target.py; AE owns the cost gate.
---

# /target -- Lusha enrichment of a company or person

`/target` takes something `/find` surfaced and pulls people data from Lusha. **Two
tiers, two credit costs** -- the tier is chosen by whether the argument is a company
or a person.

```
/target Fairway Financial Partners         -> COMPANY: org chart (cheaper)
/target Paul Tinnirello                     -> PERSON: full reveal (more credits)
/target Paul Tinnirello of Fairway          -> PERSON, company scoped explicitly
```

## Step 0 -- CONFIRM IDENTITY via WebSearch FIRST (prerequisite, do before any Lusha call)

Before spending a Lusha credit, **use the plain (free) WebSearch tool to confirm the firm's
canonical website domain + LinkedIn company URL.** This is a trivial web search -- do NOT use
serp_opal/BrightData (no SERP credits needed) and do NOT rely on Lusha's own company search
for discovery (it's weaker; use it only to resolve the confirmed domain). The registry domain
can be thin/alternate and Lusha will NOT_FOUND it (empirically: `fairwayfp.com` -> NOT_FOUND,
only `fairwayfinancialpartners.com` -> found). A confirmed domain pins the right entity and
avoids a wasted lookup.

```
WebSearch: "<firm name>" <state> wealth OR financial linkedin
```
- Take the firm's OWN site domain (not a directory/aggregator) + its
  `linkedin.com/company/<slug>` URL from the results.
- Pass the confirmed domain to `target.py --domain <confirmed>` (Lusha `companies/search`
  resolves by domain/name; the confirmed domain is the precise key).
- The LinkedIn URL is the confirmation that you have the right firm (and is the identity to
  carry into any LinkedIn-side follow-up). If WebSearch and Lusha disagree on the domain,
  trust the WebSearch-confirmed canonical site.
- If WebSearch can't confirm a real site (or the firm is too small/new to have one), say so
  before calling Lusha -- a NOT_FOUND is then the expected result, not a bug.

## Decide the tier

- **Argument is a company / firm name** -> **COMPANY (org-chart) tier.** Cheaper. Returns
  the roster of who works there (name + title + seniority + department) + firmographics.
  NO emails/phones.
- **Argument is a person's name** -> **PERSON (reveal) tier.** More credits. Finds the
  person in their firm's roster and reveals full contact detail (emails/phones). Needs the
  company context -- if the person's firm isn't obvious, ask which firm (or pass `--company`).

If it's genuinely ambiguous, ask the operator which they meant before spending credits.

## COMPANY tier -- org chart (cheaper)

Maps to Lusha `companies/search` + `companies/enrich` + `contacts/prospecting` (page-0
count is free; roster billed ~1 credit / 25 results). No contact reveal.

```bash
# PREVIEW (stub, no credits, no secret) -- always safe to show first:
python data/find/dualbiz/scripts/target.py --company "Fairway Financial Partners"
# LIVE (real org chart, modest credits) -- CONFIRM-FIRST:
python data/find/dualbiz/scripts/target.py --company "Fairway Financial Partners" --live
# disambiguate by domain if the registry has two matches:
python data/find/dualbiz/scripts/target.py --domain fairwayfp.com --live
```
The firm name is resolved to a domain via the S2 registry (`candidates.json`). If two
firms match (e.g. fairwayfp.com vs fairwayfinancialpartners.com), pass `--domain`.

## PERSON tier -- full reveal (more credits, GATED)

Maps to the roster prospecting + Lusha `contacts/enrich` (emails/phones). `contacts/enrich`
is gated behind `LUSHA_CONTACT_REVEAL_ENABLED`; the driver flips it ONLY with `--live --reveal`.

```bash
# find the person in the roster WITHOUT revealing (free-ish, no reveal credits):
python data/find/dualbiz/scripts/target.py --person "Paul Tinnirello" --company "Fairway Financial Partners" --live
# REVEAL emails/phones (spends reveal credits) -- CONFIRM-FIRST:
python data/find/dualbiz/scripts/target.py --person "Paul Tinnirello" --company "Fairway Financial Partners" --live --reveal
```

## Render

- **Company:** render the org chart as a /draw-style card -- firmographics header, then the
  roster grouped by seniority (C-suite -> VP -> director -> ...), each `name -- title [dept]`.
  Offer `/target <person>` on anyone they want revealed.
- **Person:** a single detail card -- name, title, seniority, firm, then the revealed
  emails/phones (+ FINRA series-license if you also run the free brokercheck enrich).

## Cost gates (CONFIRM-FIRST on every live call)

| Action | Lusha call | Cost | Gate |
|--------|-----------|------|------|
| Preview (default, no `--live`) | none (stub fixtures) | free | run freely |
| Company org chart (`--live`) | search + enrich + prospecting | modest (per-result) | **confirm first** |
| Person reveal (`--live --reveal`) | + contacts/enrich | reveal credits (higher) | **confirm first** |

- Always show the **stub preview first** so the operator sees the shape before spending.
- Lusha key = Secrets Manager `find-insure/lusha-ai/api-key`; **0.5.0_AE_OpalETL owns the
  cost-gate** (DDB cost-state + ceiling alerts). For volume reveals, coordinate with AE.
- The driver prints `credits_charged` from Lusha's billing on every call -- report it.

## Provenance
- Driver: `data/find/dualbiz/scripts/target.py`; Lusha API truth: `data/find/imo/scripts/_util/lusha_client.py`.
- Tiers map to the client's credit model (org-chart prospecting vs contacts/enrich reveal).
- Pair skill: `/find` surfaces the company/person this enriches.
