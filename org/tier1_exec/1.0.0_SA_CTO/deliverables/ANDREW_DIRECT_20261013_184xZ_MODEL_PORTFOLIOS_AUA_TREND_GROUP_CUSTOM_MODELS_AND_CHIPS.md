# ANDREW DIRECT -- Model Portfolios AUA Trend: group custom models, chips for strategy groups (2026-10-13 ~18:4xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `1.0.0_SA_CTO~DELL2`, during his localhost:5174 smoke of portal DEV `f6ef1d25`
(item 4.1, Model Portfolios > AUA TREND ANALYSIS > Trend). The legend lists about 17 series: individual models, "Opal Moderate Income
Portfolio (Tax Efficient)", "Opal Income Portfolio - Gillham", "Other AUA", "Additive SMA sleeves", "Tax-Managed SMA", and others.
**Verbatim:**

> Regarding model portfolios I have attached the screenshot here: [Image #3]. I'd make the following comments: 1.) We should not be including every single individual custom model, I would include "Custom Models" as its own block in these outputs, using the color for those that we use in the Hover display on the "Models" card in the "Total Assets" component. By the same token, I'd give a chip to ALT Strategies, ETF Strategies, Client Supervised, and Client Unsupervised. It is easier to group on this basis rather than trying to stack all this random shit into the Trend views.

## What it sets

- **Custom models** are one series, "Custom Models", in the Trend views (the period-end bars, the daily area chart and the legend). It
  takes the color that the "Models" card hover uses for custom models in the Total Assets component. That color is reused, not a new one.
- **Four more grouped series, each with its own legend chip:** ALT Strategies, ETF Strategies, Client Supervised and Client Unsupervised.
  They take the same grouping and colors the Total Assets breakdown already uses.
- The canonical Opal models (Ultra Short-Term through Ultra Long-Term) stay as their own series.
- **Owner:** MDPF_CANON (placement DELL1; its CN-d-3 drew the SMA bands). It goes to dell1's CTO.
- Not a promote blocker: this is presentation of a page already on PROD.

-- recorded by 1.0.0_SA_CTO~DELL2
