# ANDREW_DIRECT 2026-10-15 ~21:4xZ -- J4 read on PROD: the firm chooser works; the ticker swap is missing (the door asks the filer for a proxy)

**Channel:** Claude Code terminal, dell2, to `1.0.0_SA_CTO~DELL2`. **Recorded by:** `1.0.0_SA_CTO~DELL2`, same turn.

Verbatim:

> "Just ran the PROD request. Yes the firm dropdown works, it has all the partner firms. The thing that is missing for now is the ticker
> swap:"

What the PROD form showed him (quoted from his paste):

> "Review required: the file needs a correction. Nothing was filed. Row 100: This holding is a real fund, but our data provider does not
> cover funds of this kind, so it cannot be analyzed as it is. Name a similar ticker to stand in for it (a proxy); the report will use that
> ticker and say that it did. Details TEMPLATE_FINDINGS"

## What it settles
- **J4 is DONE:** the staff firm chooser on PROD (v2.1.226) lists all partner firms. Andrew read it with his own login.
- **A gap against his 10-15 ~14:xxZ word ("swaps are not up to the filer"):**
  - the upload door refuses a covered-but-unpriceable holding (`TICKER_DATA_NOT_ENTITLED`, actions `NAME_PROXY`);
  - it asks the FILER to name a proxy;
  - nothing files.

  PRD v0.15 fixed this path only for a kept `TICKER_NOT_FOUND`. It did not name `TICKER_DATA_NOT_ENTITLED`, which is the same class from
  the filer's side: a security Opal cannot price as given.
