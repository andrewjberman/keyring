# CTO RULING -- NFRA_OPLGTW row W45-S2: `blackdiamond_list_fees` is DENIED to unprofiled principals, after a caller census

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~13:4xZ. **On:** `3.0.0_SA_CVO~Z`'s round-33 slug (HELD), msg 33286, row
`NFRA_OPLGTW-Z-W45-S2` (owner this seat).

## The finding, read in code

`infra/aws/ec2/opal-gateway/app/data_entitlement.py`:
- `blackdiamond_list_fees` sits in `INDEX_TOOLS` (`:131`) and is therefore `CLASS_LEGACY` (`:135`).
- By the module's own table (`:41`), a principal with **no profile** "legacy tools pass on to the existing gates
  unchanged; Schwab tools are hidden and denied".
- So an unprofiled principal reaches the BD tool, while the same principal is denied every Schwab tool.
- A profiled principal is confined by its grant, because the BD tool IS in the data-grant family (`:43-45`).

## Ruling: DENY to unprofiled principals

The BD tool serves a CLIENT FIRM's data (49financial fees), the same kind of data the Schwab tools serve. The module
already treats it as client data for profiled principals. Letting the one class the store knows LEAST about reach it is
the inversion, and nothing recorded chose it: the classification came from MX-t-13's cut-off-date bucket (`:123-125`),
not a decision about this tool. One rule for client data: hidden from and denied to a principal with no profile, and
reachable only through an active grant that names it.

## The cell (round 34, `2.0.0_SA_COO~O`), in this order

1. **Caller census first (read-only):** every principal that called `blackdiamond_list_fees` in the gateway's retained
   logs, each with its profile state. The denominator is printed, with a positive control: a known caller is found.
2. **If every caller is profiled with an active grant that names the tool:** change `decide()` so an unprofiled principal is
   denied this tool, as for the Schwab family. Update `test_ogpf1_ac02` to pin the NEW behaviour, plus a negative
   control: a profiled-and-granted principal still reaches it. It ships under the gateway release procedure (Z-S85: cut on
   the LIVE ref).
3. **If any caller is unprofiled:** the cell STOPS before the code change. Giving that principal a profile and grant is an
   admission act (C8, Andrew's), so it goes to him as a call, naming the principal and its call count. This seat does
   not grant, and the deny does not ship until it does not break a real user.

-- 1.0.0_SA_CTO~Z
