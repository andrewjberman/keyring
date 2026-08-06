# ANDREW-DIRECT 2026-08-06 -- cohort-A dispositions (daily-agenda-generator DEPRECATED; infrastructure-monitor DORMANT/low-priority)

**Received by:** `0.7.0_AE_CloudOps`  **Channel:** Andrew direct at this terminal
**Date:** 2026-08-06 (session in progress, ~19:0xZ)
**Recorded per:** `org/XXX.md` "Andrew-direct instructions -- RECORD + BROADCAST, same turn."
**Scope handling:** SURFACE, DO NOT ADJUDICATE. Verbatim below; scope read is stated separately
and is explicitly *mine*, not his.

## VERBATIM

On `daily-agenda-generator`, after I gave him what the function does and for whom:

> **"ok i dont care about this, deprecated"**

On `opal-infrastructure-monitor`, earlier in the same exchange:

> **"infrastructure monitor is dormant, I do want to work on that but its a very low priority."**

On the seeking-alpha locus, earlier in the same exchange (bounding Component 2):

> **"if it has anything to do with the seeking alpha system it is a waste of time we do not care about that"**

## WHAT PROMPTED IT

I was executing RCG Component 1 (CRO handoff `RCG_COHORT_A_HANDOFF/HANDOFF.md`, authority R-0024):
build Lambda layers from derived pins for two functions, deploy via Terraform, then `git rm` the
1,482 vendored files deploy-coupled. Before building I ground-truthed the deployed artifacts, and
surfaced to Andrew that most of the work appeared unnecessary. He ruled on both functions.

## MY SCOPE READ -- MINE, NOT HIS. Correct me, do not inherit this as his word.

**`daily-agenda-generator` (114 files) -- DEPRECATED by direct word.**
No layer will be built. Its 114 `package/` files stop being a MIGRATE/layer-refactor cohort and
become a deprecation-class disposition for CRO's ledger. **I did not execute any deletion** --
deprecation is a status ruling; the archive is CRO's ledger mechanics, and I hold no authorization
to sweep on my own read of his word.

**`opal-infrastructure-monitor` (1,368 files) -- DORMANT, LOW PRIORITY, still wanted.**
He explicitly wants this function worked on later. **The function is NOT deprecated** -- only
deprioritized. Nothing here authorizes touching the function itself.

## THE MEASURED FINDING THAT PRECEDED THE RULING (independent of it, and it stands on its own)

**No layer is needed for `opal-infrastructure-monitor` regardless of priority.** Ground-truthed on
the DEPLOYED artifact, not the handoff:

| Check | Instrument | Result |
|---|---|---|
| Deployed artifact contents | downloaded the live zip via `get-function` Code.Location, listed the manifest | **exactly 2 entries**: `lambda_function.py`, `openai_cost_tracker.py`. 40,015 bytes |
| Vendored packages in artifact | same manifest | **ZERO** -- openai/pydantic/httpx/httpcore/anyio/tqdm/certifi all absent |
| What the code imports | source read | `json re boto3 datetime typing`, `anthropic` (try/except, supplied by the already-attached `anthropic-sdk-deps:1` layer), `openai_cost_tracker` (local module, ships in the zip) |
| `import openai` anywhere | source read, both modules | **NONE.** The function migrated off openai to Claude (leg-c) |

**Therefore CRO's 16 derived pins describe packages nothing imports.** The handoff's stated premise
-- *"pins derived from the vendored dist-info deployed today, so the layer reproduces what runs"* --
is **false for this function**: the vendored tree is a PRE-MIGRATION leftover and does not represent
what runs. Building that layer would not reproduce the runtime; it would materialize a stale openai
stack the function no longer calls.

**And the `git rm` is NOT deploy-coupled here.** The deletion cannot break the function, because
those files have never been in its artifact. The deploy-coupling in the handoff was protecting
against a dependency that does not exist.

⚠ **The `infra-monitor.tf` header comment is STALE and says the openai import is "try/except
graceful."** The code imports `anthropic`, not `openai`. Anyone reading that comment as current
state gets the wrong picture -- flagged, not edited (the function is Andrew-wanted future work and
I am not touching it at low priority).

**`daily-agenda-generator` was the genuine case and is now moot.** It really does vendor its deps
in-artifact (1.4 MB deployed, no layer attached, real `import requests`). It writes a GitHub-commit
digest to `s3://opal-data-portal-v2/agendas/`. **That prefix does not exist** -- the bucket has 27
top-level prefixes and `agendas/` is not among them, with `Environment.Variables: null` so the code
defaults are the live config. An EventBridge rule `daily-agenda-generator` still holds invoke
permission. I was mid-check on whether that rule is ENABLED when Andrew ruled it deprecated;
**that check is now moot and was not completed** -- stated so nobody reads this as a liveness census.

## NET EFFECT ON RCG COMPONENT 1

**The layer-build is cancelled by sovereign word + measurement.** Neither function gets a layer:
one is deprecated, the other imports none of the pinned packages. All 1,482 files change disposition
from "MIGRATE / layer-refactor, deploy-coupled" to a plain uncoupled removal -- **CRO's ledger call
to make, on this evidence.** No deploy-completion ledger entry was opened, because no deploy will
occur.

## BROADCAST

MCP to `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` (record+broadcast law), and to
`4.0.0_SA_CRO` as the requesting seat whose ledger disposition this changes.
