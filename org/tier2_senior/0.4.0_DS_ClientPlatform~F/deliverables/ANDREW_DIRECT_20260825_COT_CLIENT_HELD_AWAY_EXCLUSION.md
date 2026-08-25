# ANDREW-DIRECT 2026-08-25 ~01:0xZ — Cottonwood: CLIENT HELD AWAY is EXCLUDED FROM ALL FIGURES

**Terminal:** `0.4.0_DS_ClientPlatform~F`. **Amends:** the Client L1 per-firm ruleset @6848107cff.
**Status:** RECORDED VERBATIM + BROADCAST SAME TURN. Measurement attached. **NOT EXECUTED** — it
changes a served total; the discriminator is not yet settled (see THE INTERSECTION QUESTION).

## VERBATIM

> The one thing that this needs to take account of for Cottonwood is that Cottonwood does not want
> Client Held Away (unsupervised by opal *AND* Cottonwood) included in any figures for them. WE had
> intended to figure out how to get this done via doing some kind of filtering to pull out the ~22m
> or so assets that Black Diamond has as "Unsupervised" from the total.

## WHAT IT BINDS
Cottonwood's **Client Held Away** — assets unsupervised by Opal **AND** by Cottonwood — is excluded
from **any figures for them**. Not a display suppression: **an exclusion from the total.**

## THE MECHANISM EXISTS AND IS LIVE — `D_05.supervised_split.py`
It already emits exactly this filter to `s3://opal-data-cot/gold/artifacts/supervised_split.json`,
`firm_daily` = {aum_all, aum_supervised, aum_unsupervised, aum_unflagged}, retroactive over full
history (98 daily rows), flag source `accounts_dimension_latest.account_supervised`.

## MEASURED (live artifact, data_as_of 2026-08-19 — the same vintage this lane emits for cot)

| field | value | share |
|---|---|---|
| `aum_all` | **480,056,488.78** | 100% |
| `aum_supervised` | 449,733,561.36 | 93.68% |
| `aum_unsupervised` | **30,322,927.42** | **6.32%** |
| `aum_unflagged` | **0.00** | 0.00% |

`aum_all` ties **EXACTLY** to the cot total this lane emits (480,056,488.78), so the filter sits on
the same plane as the view figures and is directly applicable. Partition ties to the cent.

## TWO FINDINGS THAT ARE NOT WHAT HE EXPECTED

### 1. THE FIGURE IS 30.3M, NOT ~22M — AND THE GAP MAY BE THE WHOLE POINT
He recalled "~22m or so". BD-Unsupervised measures **$30,322,927.42**, ~38% higher.
**LEADING HYPOTHESIS, NOT A CONCLUSION:** his ~$22M may be the **INTERSECTION** he actually
described (unsupervised by Opal **AND** Cottonwood), while $30.3M is only the **Cottonwood leg**.
The ~$8M gap would then be accounts BD flags `Unsupervised` **that nonetheless hold Opal Models** —
which by his own Client L1 rule are **Opal-SUPERVISED** and must NOT be excluded.

### 2. `aum_unflagged` IS 0.00 TODAY
The third bucket (accounts absent from the attributes pull) is **empty on this vintage**. It is real
by construction and `D_05` asserts the three-way partition per date, but it currently carries no
dollars — so Q-h3's labelling question is live in code and moot in practice today.

## ⛔ THE INTERSECTION QUESTION — WHY THIS IS NOT EXECUTED YET
His words are an **AND**: *"unsupervised by opal **AND** Cottonwood"*. `aum_unsupervised` is a
**single-flag** figure — Cottonwood's supervision status only. Applying it wholesale would exclude
any BD-Unsupervised account that holds Opal Models, which contradicts the Client L1 rule he gave in
the same breath (accounts holding Opal Models are Supervised).

**So the exclusion is the intersection: BD-Unsupervised ∧ no Opal Model exposure.** This lane is
measuring that intersection rather than applying the $30.3M single-flag figure. If the intersection
lands near ~$22M, his recollection was of the correct quantity and the mechanism is confirmed from
both ends.

**MAGNITUDE OF GETTING THIS WRONG:** excluding the superset understates Cottonwood's client-facing
total by up to ~$8M and removes assets that carry Opal exposure. NEVER#3 territory — a served total
moving on an inferred discriminator.

**Author:** `0.4.0_DS_ClientPlatform~F`. **Cells:** D1-h-c1/c2/c3, D1-b-1, D1-h-p2 (the cot total).
