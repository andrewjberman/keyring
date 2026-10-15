# ANDREW DIRECT -- no price-date selection for the filer; prices are always the most recent data (2026-10-15 ~20:4xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `4.0.0_SA_CRO~DELL2`. It came after this seat's status read of the
analysis-request workflow.

**Verbatim:**

> By the way there is no point in giving them date selection for prices. The prices should always be whatever the most recent data is. Doing T+1 is most logical, which is what we'd be able to provide internally as well as all our API solutions to my knowledgds

## What it sets (surfaced, not adjudicated)

- **No price-date choice on the Analysis Request form or the upload.** Today the share-quantity path takes a `priceDate`: the form sends
  `priceDate: ''` (`TicketCenter.tsx:411`), and the server requires one for share quantities (AR-y-243/245).
- **Prices are always the most recent data available.**
- **On "T+1" (this seat's reading, for the owner to confirm, not adjudicated):** he means the price of the latest close, available the
  next morning. On the estate's trading calendar that is the T-1 frontier (`lib/trading_calendar.py`), which is what Yahoo (cut at T-1),
  YCharts and Bloomberg all deliver. If the owner reads it otherwise, it asks him once.

## What it touches

- IRPT_ANLREQ:
  - the share-quantity price date (AR-y-242..245; `intake/portfolio.py:208-212`);
  - the form field;
  - C-PRICES (the as-of of every price in the report).

-- recorded by 4.0.0_SA_CRO~DELL2

## Confirmation, minutes later (verbatim)

> You are correct

**Sets:** "T+1" means the latest close, available the next morning. That is the T-1 frontier on `lib/trading_calendar.py`. It is
confirmed by Andrew and is no longer this seat's reading.
