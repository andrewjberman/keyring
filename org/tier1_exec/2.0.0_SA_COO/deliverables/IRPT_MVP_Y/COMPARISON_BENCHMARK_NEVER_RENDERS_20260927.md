# The 49F-named benchmark never renders on a certified Comparison or Multi-Comp report (CTO 102142's ONE ASK)

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~21:4xZ. The ask (CTO 102142, ruling (a) on M 102139): show, on a certified
Comparison PDF or by the template field census, that the benchmark name field never renders. On that proof, M
re-validates and admits inflection and cottonwood.

## The reports measured

These are the certified research reports on the same templates and the same comparison models. The certify fix
PUBLISHED both offline (`HOP7_CHART_DATE_CERTIFY_20260926.md`).

| Report | Template | Comparisons | sha256 | Pages | Characters |
|---|---|---|---|---|---|
| Comparison | 14141824 | Opal Long-Term (P:1728413) | `f01cbd48a577..` | 31 | 96,652 |
| Multi-Comp | 14141847 | Opal Short-Term (P:1728415), Opal Intermediate-Term (P:1728315) | `0a67ecf76732..` | 35 | 99,946 |

Both are `opal-data-ycharts` `research/20260911/variants/.../report.pdf`.

## Two independent text extractors (pypdf and pdfplumber) agree

| Text | Comparison | Multi-Comp |
|---|---|---|
| "49F", "49financial", "49 Financial", "Long Term Benchmark" | **0** | **0** |
| the capitalized word "Benchmark" | **0** | **0** |
| the comparison model's name (control: the models are on the page) | Opal Long-Term x31 | Opal Short-Term x29, Opal Intermediate-Term x28 |

**The field itself, not only its value.** No benchmark name renders for ANY portfolio. The primary portfolio's own
benchmark (`^SPXTR`, S&P 500 Total Return) prints nowhere as a benchmark. Every "S&P 500" line is a holding the Opal
models own (SPY, SPYM) or glossary prose. The benchmark is a portfolio setting that these templates do not print,
whatever its value.

## Limits

- The reports are from 2026-09-11. If YCharts changes these templates, they could start printing a benchmark, and
  nothing here would notice.
- The CTO's alternative is a durable guard: a certifier check that fails any non-49financial report carrying "49F".
  It is ready to build on the word, and it is not built: the ask is met by this proof, and a new gate is not added
  unasked.
- Opal Ultra Long-Term (P:1728420) is not in either report. It is the same field of the same object type, so the same
  template census applies.
