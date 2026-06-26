---
name: target
description: Take a company or a person surfaced by /find and enrich it via the Lusha API. Two tiers -- COMPANY level (e.g. "/target Fairway Financial Partners") draws the firm's org chart (names/titles/seniority, the cheaper Lusha prospecting call); PERSON level (e.g. "/target Paul Tinnirello") returns full contact detail (emails/phones -- the true Lusha reveal, more credits). Use when the operator types "/target <company or person>", or asks who works at a firm, to break out employees, find decision-makers, or get a person's contact details. Paid Lusha calls are CONFIRM-FIRST. Driver = data/find/dualbiz/scripts/target.py; key = Secrets Manager find-insure/lusha-ai/api-key (AE owns the cost-gate).
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
