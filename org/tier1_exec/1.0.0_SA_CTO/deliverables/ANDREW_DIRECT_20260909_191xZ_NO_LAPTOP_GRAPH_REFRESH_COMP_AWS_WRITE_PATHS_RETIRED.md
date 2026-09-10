# ANDREW-DIRECT 2026-09-09 ~19:0xZ-19:1xZ, at the `1.0.0_SA_CTO` terminal -- VERBATIM

Two messages, entire, in order:

> (1) "Also I want you to take a quick look at CLDGRPH. Based on the work here, shouldnt there be no need for comp-aws as a tool in
> general? Wouldn't every tool simply just be pointed at the AWS-based cloud KuzuDB (where is this stored? Does the CLDGRPH define
> that?)?"

> (2) "Thats what im getting at, it seems like running comp-aws is a laptop-operated graph refresh, but there should be no need for
> the laptop (or any other user) to be running manual refreshes, as the manual refresh happens every morning and the little ECS is
> running stitches live."

Recorded at 19:1xZ; broadcast the same turn to `2.0.0_SA_COO~A`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`. Inside his
~12:5xZ standing word (adjudicate and push forward on NFRA_CLDGRPH); acted on as a CLDGRPH addendum, PRD v0.8 row S30.

## What his words name, on the measured record (the CTO's reading, at the scope of the words)

**The premise holds for every READER.** By ruling R6 the consumers (`comp-kuzu`, `comp-blast`, `comp-find --corpus aws`) write
Cypher against the served projection; `comp-kuzu` holds no store and prints the VINTAGE line per call; there is no refresh an agent
runs (CG-s-17, manifest entry `cloud.read.served_vintage`).

**comp-aws is the COMPILER, not a reader**, and the estate's own schedule already runs it where it belongs:
- the nightly Fargate derive-runner (`infra/aws/globgrph/derive_runner.py`, NFRA_GLOBGRPH Item-2a) calls `comp_aws_cli.cmd_derive`
  in-process (`:101`), overwrites `graph_nodes`/`graph_edges` in the Nessie catalog, tags the branch, and archives the tarball to
  `s3://opal-313476888478-globgrph/snapshots/` -- this is "the manual refresh every morning": scheduled, in the cloud;
- the incremental-updater Lambda mirrors the compiler's class map and applies cloud changes intraday (near-real-time);
- the projection worker rebuilds the KuzuDB artifact on the branch-head marker (R5) and the small always-on ECS service SERVES it
  (R3, his call of 2026-09-02) -- the ECS service holds the artifact; it does not stitch;
- the cross-layer stitch runs nightly on CodeBuild (`opal-stitch-produce`, first SUCCEEDED publish 18:49:23Z today, S23/S71).
His conclusion holds under this mapping: **no laptop and no user has a reason to run a refresh.**

**What is still wrong, and what S30 retires:** the agent-facing CLI kept three PRODUCER paths that a laptop can run today with no
guard (help read 19:1xZ):
- `comp-aws iceberg-commit` -- writes the derive into the Nessie tables from a laptop: a person starting the rebuild that FWD-2's
  accept forbids ("no question anyone asks is ever the reason a rebuild starts");
- `comp-aws snapshot` -- publishes a tarball and the `latest.txt` pointer to the shared `snapshots/` prefix (`--commit-to-nessie`
  is the same Nessie write): the laptop as a producer of what the stitch derive reads;
- bare `comp-aws derive` as an agent act -- a compile nobody reads, on live-AWS API calls, the shape FWD-6 retired for `comp-kuzu`.
The engine (`cmd_derive`) stays for the cloud runner; the six read-only analysis subcommands stay (`classes`, `metrics`, `diff`,
`dual-managed`, `score`, `contract-diff`) because they answer what the graph cannot (Terraform-state apply conflicts, a live
security tally, two-snapshot forensics, the compiler's own F1) and Rule 20 keeps live reads legitimate for verifying one's own fresh
change. The registry entry (`comp-tools.yaml:125-136`, `comp-aws-agent-usage.yaml`) still describes the laptop as a producer
(`-> .comp-graph`, "snapshot tarballs -> opal-313476888478-globgrph") and is rewritten with the row.

**Grading note for the next L10:** FWD-6 graded REALIZED at round 5 on probes (LIVE_ROUTES_BACK 0 of 126, RETIRED_ROUTES 0 of 3,
HELP_ROUTES_BACK 0 of 8) that enumerated the KuzuDB refresh routes and not the compiler's write paths; S30 is the residue those
probes did not cover. The grade stands until the next read; the row says what the read must include.

## Push state
LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 19:01Z; re-read at send).

---

## ANDREW-DIRECT ~19:3xZ, same terminal, on the report of S30 (v0.8) -- VERBATIM, appended 19:3xZ, never silently

> (3) "ok please inform COO~A accordingly. I would also fold in some function first about how comp-aws is no longer callable,
> effectively deprecate it and pull it off from being surfaced via comp-which. We do not need to gate it, merely need to pull it out
> of comp-which selection, that will be enough."

**What it changes (PRD v0.9, S30 amended in place, the v0.8 shape superseded before any cut):** the verb is DEPRECATE, not retire.
No refusal, no exit-code change on any comp-aws subcommand -- his words: *"We do not need to gate it."* Two acts instead:
1. **A deprecation preamble function at the CLI entry** (`comp_aws_cli.py` main and the `.tools/comp-aws` wrapper), printed before any
   subcommand runs: deprecated for agent use since 2026-09-09 on Andrew's word; the graph is SERVED (`comp-kuzu`, manifest entry
   `cloud.read.served_vintage`) and REFRESHED by the nightly derive-runner and the incremental updater; this CLI is no longer routed by
   `comp-which`. Then the subcommand runs as before.
2. **Pulled out of `comp-which` selection:** marked deprecated at TOOL grain in the population authority (`comp-coverage-map.yaml`;
   R14 already fixes `deprecated` as the tool-grain value in its only consumer), the carriers REGENERATED, and `comp-which`'s curated
   routes that name comp-aws repointed to the served surface -- never hand-edited.
The engine (`cmd_derive`) stays untouched for the nightly Fargate derive-runner. **Noted, not re-litigated:** the three write paths
(`iceberg-commit`, `snapshot`, bare `derive`) remain callable by name; the deprecation banner and the absence of a route are the
whole control, by his word. Relayed to `2.0.0_SA_COO~A` at 19:3xZ (hold on the v0.8 cut) and re-broadcast with v0.9.
