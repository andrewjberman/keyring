# ANDREW-DIRECT 2026-10-05 ~15:5xZ-16:3xZ -- HARVST collection: add the approved research names to the run

**Seat:** `2.0.0_SA_COO~H` (site Z), in session. **Verbatim, in order:**

> "no im fine with having all Opal Securities and the research list being included in the run. if that is 191 securities
> total, we are cool with that."

> "We did an analysis at one poitn of the remaining 56 research names, where if we could resolve them through increasingly
> inferential means, and we actually resolved all of them , and I approved those resolutions. I need you to comp-find wherever
> that list is."

> "Yes I do" (answering: "Do you want me to add the 59?")

**What was found:** the 56 approved resolutions are `lib/research/identity/registrations.json` rows registered 2026-09-24
(@b7819604e0, 20 names; @505fc14404, 36 names). The run universe (`universe/v1/2026-09-16.json`, 191 resolved) was built before
them and never rebuilt. Three research folders added since (Quanta PWR US, AIA 1299 HK, Hitachi 6501 JP) were also absent.

**Correction to the count Andrew was given:** "59" was 56 + 3. Measured at the build, 16 of the 56 were already in the run under
their fund-holding keys (Bunzl, Copa, Idexx, Intuitive Surgical, Mastercard, MercadoLibre, Monster, Netflix, QXO, ServiceNow,
Spotify, TSM, Uber, Universal Music, Visa, Workday). The widening adds **43** names: universe 191 -> 234.

**Scope, verbatim and no wider:**
- Scope of the run = Opal holdings + the research list.
- The 43 are collected for sa, barrons, bbg and wsj as part of the same run, each leg relaunched from its own checkpoint.
- **ft:** unchanged, held until Andrew returns (record `ANDREW_DIRECT_20261005_025xZ_HARVST_NO_FT_UNTIL_RETURN_REST_PROCEED.md`).

Cell: decomposition section 60.2 (`HVST-at-5`). This word binds this seat's HARVST collection only.
