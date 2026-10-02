# ANDREW-DIRECT 2026-10-02 ~13:3xZ -- "LETS USE A NEW SOLVER": Ocilar for hCaptcha

- Channel: site-Z terminal of `2.0.0_SA_COO~H` (session d9ce3a44-2d1e-4745-8265-458874d2c772), typed by Andrew mid-turn.
- Time: 2026-10-02 ~13:3xZ (09:3x ET).
- Recorded by: `2.0.0_SA_COO~H`, same turn.

## Verbatim (the API key is REDACTED here and everywhere in the repo)

Andrew: "bETTER IDEA, LETS USE A NEW SOLVER:" followed by a pasted Ocilar guide ("hCaptcha Solver API: Automate hCaptcha
in Python & Node.js", 2026-03-16; endpoint `POST https://api.ocilar.com/api/v1/solve/hcaptcha` with header `X-API-Key`
and body `{sitekey, url}`, returning `{token, latency_ms, credits_used}`; PAYG $0.16 per 1,000 hCaptcha solves), then
". API KEY - sk-[REDACTED: stored in AWS Secrets Manager `ocilar/credentials`, key `api_key`] ."

Then: "https://console.ocilar.com/integration/"

## What it answered

`2.0.0_SA_COO~H` reported the failure: the NopeCHA Token API is discontinued (error 19, row Z-W92-S18). It proposed the
NopeCHA browser extension (cell aj-6, CTO ruling 28484 YES). Andrew's "better idea" replaces that route with Ocilar.

## Scope (as said, nothing wider)

- **Use Ocilar as the hCaptcha solver.** This is his explicit word to call the Ocilar API, and he supplied the key.
  He named no permanence and no scope beyond "a new solver" in the hCaptcha context of the ft sign-in. A standing
  whitelist row (`org/ref/VENDOR_EGRESS_WHITELIST.yaml`) is the CTO's to land on this record, at the scope his words
  give.
- The key is a secret. It goes to Secrets Manager (`ocilar/credentials`, the publisher-credential naming convention)
  and is read from there; it is never printed or committed. The transcript of this session holds the key as he typed
  it, so rotation is his call.
- NopeCHA (VEW-1) stays whitelisted. This record does not strike it.

## Relay

One line to `1.0.0_SA_CTO~Z` naming this path: a whitelist row for Ocilar at his scope, and cell aj-6 re-pointed from the
NopeCHA extension to the Ocilar API.
