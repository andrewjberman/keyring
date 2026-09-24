# ANDREW-DIRECT 2026-09-23 ~22:0xZ -- the GitOps split of opal_ai from ajb_workspace (portal-shaped submodule)

**Channel:** Andrew-direct at the `4.0.0_SA_CRO~X` terminal (site Z / SITEZ fabric), in-session, ~22:0xZ 2026-09-23
(~6:0x PM Eastern). The message follows this seat's delivery of the opal_ai L1 brief (RCN-0014, drained @2c4a813784).
**Received and recorded by:** `4.0.0_SA_CRO~X`, the same turn, before any research act.

## Verbatim (THE PHRASING IS THE RULING)

> Ok now I need another spec from you where you basically figure out what needs to happen to properly split this off
> in GitOps from ajb_workspace. It should be the same structure as the portal where it is contained in the monolith,
> but it has its own git submodule or whatever so we can keep it clean and separated but still have the benefit of the
> ajb_workspace tooling and process ops and so on.

## What this seat reads as asked (surfaced, NOT adjudicated)

- ONE deliverable: a SPEC from this seat saying what must happen to split `opal_ai` off from `ajb_workspace` in GitOps
  terms.
- The target shape is his: the same structure as `portal/` -- the code lives inside the monolith's tree, but in its own
  repository wired in as a git submodule ("or whatever"), so it stays clean and separate while keeping the
  `ajb_workspace` tooling and process ops.
- "this" is read as `opal_ai`, the repo the brief of 2026-09-23 describes. "or whatever" leaves the mechanism open, so a
  measured alternative to a submodule is in scope for the spec to compare. It is not assumed away.
- ⚠ NOT asked, and not done by this seat: creating the GitHub repository, adding the submodule, moving files, or changing
  any gate, hook or deploy path. The spec is intake for `1.0.0_SA_CTO~Z`, the L2+ router Andrew named on 2026-09-22
  (call 7). Repository creation is outward-facing and is his and MSTR's.

## Broadcast

Same turn, MCP to `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR~Z`.
