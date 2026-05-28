# Session Log — 0.4.0_DS_ClientPlatform — 2026-05-28 (F4 fee-split NNA tie-out)

**archetype:** VALIDATE

**Agent:** 0.4.0_DS_ClientPlatform (Tier-2 DS, ClientPlatform / ADVI Inflection)
**Driver:** ws COO RAVC2-ACCEPT on F5 + GOed F4 (crash-recovery session)
**Theme:** F4 = empirically verify fee_paying.nna + no_fee.nna == total.nna holds in the deployed artifact across Peter + control + firm.

---

## Headline outcomes

1. **AC4-sum PASS** — `fee_paying.nna + no_fee.nna == total.nna` holds to the cent (delta=0.00) for:
   - **peter_lee**: QTD / YTD / MAX ✓
   - **joe_brandenburg** (control): QTD / YTD / MAX ✓
   - **Firm aggregate**: QTD / YTD / MAX ✓
   - **Firm == sum(advisors)**: QTD / YTD / MAX ✓ (additive consistency)
2. **No new DS code needed.** F5 emit (INF_D_00f, `bcc29881c`) already included fee_paying + no_fee sub-buckets in every window leaf. The tie-out was validated at dry-run + pre-RAVC2; this session confirms it against the live S3 artifact.
3. **Cohort dimension (new-vs-existing) flagged as follow-on** per COO direction — not cheap to add under F4 without a hh_lifecycle join; flagged in RAVC2 for COO/CTO scope ruling.

---

## Tie-out table (empirical, s3://opal-data-inf/platinum/firm/advisor_nna_canonical.json, generated_at 2026-05-28T20:29:29Z)

### peter_lee

| Window | total.nna | fee_paying.nna | no_fee.nna | sum_check | delta | Pass |
|--------|----------:|---------------:|------------|----------:|------:|------|
| QTD    | -805,260.55 | -3,692,212.79 | 2,886,952.24 | -805,260.55 | 0.00 | OK |
| YTD    | 1,549,520.63 | -1,291,700.26 | 2,841,220.89 | 1,549,520.63 | 0.00 | OK |
| MAX    | 108,959,119.23 | 103,114,919.22 | 5,844,200.01 | 108,959,119.23 | 0.00 | OK |
| q1     | 2,354,781.18 | 2,400,512.53 | -45,731.35 | 2,354,781.18 | 0.00 | (reference) |

### joe_brandenburg (control)

| Window | total.nna | fee_paying.nna | no_fee.nna | sum_check | delta | Pass |
|--------|----------:|---------------:|------------|----------:|------:|------|
| QTD    | 153,894.54 | -30,347.73 | 184,242.27 | 153,894.54 | 0.00 | OK |
| YTD    | 184,194.52 | -47.75 | 184,242.27 | 184,194.52 | 0.00 | OK |
| MAX    | 10,332,532.49 | 9,572,130.02 | 760,402.47 | 10,332,532.49 | 0.00 | OK |

### Firm aggregate

| Window | total.nna | fee_paying.nna | no_fee.nna | delta | Pass |
|--------|----------:|---------------:|------------|------:|------|
| QTD    | 1,519,357.49 | -3,806,162.70 | 5,325,520.19 | 0.00 | OK |
| YTD    | 4,139,269.82 | -1,149,893.13 | 5,289,162.95 | 0.00 | OK |
| MAX    | 135,808,345.03 | 126,832,020.23 | 8,976,324.80 | 0.00 | OK |

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io INF_D_00f` | Ran at F5 emit — N/A for F4 (no new script, verification only). |
| `comp-validate` / empirical check | Pulled live artifact from S3, verified fee-split invariant programmatically. All 9 advisor × window checks PASS (delta=0.00). |

No new Python script committed this tick — F4 DS work = empirical artifact verification only. No .py edit = no pre-commit gate needed.

---

## Open / handoffs

- **RD (0.4.2):** fee-split render in Lifetime Activity reading `advisors[key].windows.{window}.fee_paying.nna` / `.no_fee.nna` — COO folding into the RD-repoint TO.
- **CVO (3.0.0):** empirical tie-out gate (AC4) — verify fee-split in Lifetime Activity vs Exec Summary Flows on real portal. Gate is downstream of RD repoint.
- **Cohort dimension (new-vs-existing):** needs hh_lifecycle join. Not cheap under F4 scope (requires F11-style backfill). Flagged to COO as follow-on; COO/CTO to scope as F4-cohort or standalone.

---

## Commits

- F4 TO status flip: committed with `/work` cycle log (no separate script commit — F4 was verification-only).
