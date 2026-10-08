# Graph coherence -- FAST FIX list (ship today; the project comes after)

**Author:** `4.0.0_SA_CRO`, 2026-10-08 ~16:1xZ. **For:** `1.0.0_SA_CTO`, msg 106975.
**Order:** Andrew, verbatim in the addendum of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`
@`fdef7ad167`: "we need to get fast solutions out across the boxes while we get organized".
**Topic:** shared graph read access from every box, and current state (brief
`docs/briefs/multi-device-graph-coherence-brief-20261008.md` @`8b4f996b64`; draft PRD NFRA_GRPHCO).
**CORRECTION 2026-10-08 ~16:5xZ -- F3 IS WITHDRAWN.** Its premise is false: the nightly full rebuild published every
night (projection manifests read live: derive_runner full builds 10-04 02:11Z, 10-05, 10-06, 10-07 02:13Z, 10-08 02:12Z,
849-985 s each). The "last full 2026-10-04" read came from the head marker's `writer_id`, which every later incremental
overwrites. Sent to `2.0.0_SA_COO~C` and `1.0.0_SA_CTO` as msgs 106999/107000. The same correction applies to
`CLOUD_GRAPH_MULTI_AGENT_COHERENCE_PRIOR_ART_20261008.md` sections 3.2 and 6.3, and to the brief's Part IV finding 2.
**Not here:** the fabric layer (who is working on what). That is a build, not a same-day fix.

| # | Change | Applies it | Boxes | Rollback | Cost if wrong |
|---|---|---|---|---|---|
| F1 | **Let the Dells read the graph.** Add a `ruling` to `opal/mcp/graph-read-token` in `infra/aws/terraform/nfra-ctlpln-identity/tests/vendor_secrets_census.json` `decisions` (today `PLATFORM-KEY`, `granted: false`, `ruling: null`) that grants it on Andrew's call 3/4 words of 15:4xZ. Then rebuild the vendor policy and `safe-apply` it. Prove it with one `comp-kuzu` query run on dell1 and on dell2. | Ruling: `1.0.0_SA_CTO`. It must name Andrew's word, because CTO msg 106669 ruled "the gateway bearer tokens" out, and this token is one of them. Apply: the NFRA_CTLPLN apply seat (`2.0.0_SA_COO~C` lane), on the laptop. | dell1, dell2 (the laptop and site Z already read, see F1 note) | Remove the ruling and `safe-apply` again: one policy statement. | A Dell holds a static, read-only bearer for estate METADATA: resource names, IAM, Lambda wiring, SharePoint file names. It is not firm data and gives no write. If it leaks, it must be rotated by hand (it was created out-of-band, 2026-09-04). |
| F2 | **Fix the Cypher example that sends every new seat to an error.** `.tools/comp-which:1198` suggests `comp-kuzu "MATCH (n:LAMBDA) RETURN n.id"`. Change it to `comp-kuzu "MATCH (n:CloudNode) WHERE n.node_type = 'LAMBDA' RETURN n.name LIMIT 5"`. | `0.0.0_AB_MSTR` (tooling) | all four (a tracked file; arrives with the trunk) | `git revert` | None. It is guidance text. |
| F3 | **Re-run the nightly full rebuild once and read why 2026-10-07's did not publish.** The last full rebuild is 2026-10-04, and the served copy has lived on incremental updates since. This is an ad-hoc QA run; the scheduled nightly stays the acceptance. | `0.7.0_AE_CloudOps` | cloud (every box reads the result) | Repoint `projection/current.json` to the 2026-10-08T12:54:23Z vintage, which is the current pointer. | A bad full build is served to every box until it is repointed. The incremental path is unaffected either way. |
| F4 | **Every seat that reads the graph says its vintage.** `comp-kuzu` already prints a `VINTAGE:` line on every answer. Today the gain is in reading it, not building it: one line in the seat's own message whenever a graph answer drives an act. Binds by reading, so nothing is built. | each seat, starting today (the CTO's relay) | all four | none needed | None. |
| F5 | **Do not add a Deny on the Dells' write to the graph bucket.** Disposition row `NFRA_CTLPLN-S31` with Andrew's call 3 ("They should be able to"). The sanctioned write shape is NFRA_GRPHCO FWD-6, not a same-day change. Today's `dell_deploy_policy.json` `s3:PutObject` on `opal-*/*` stays as it is. | the row's disarm owner (control plane) | dell1, dell2 | Re-open the row and add the Deny. | A Dell seat writes the head marker or an Iceberg file by mistake. The bucket is not versioned, but Nessie keeps table history (with a nightly tag kept 13 months) and the head marker can be rewritten to the prior vintage. The exposure is the same as this morning's: nothing new is opened. |

**Measured for F2 (laptop, 16:1xZ).** The suggested form returned
`ERROR: projection service 502 ... Binder exception: Table LAMBDA does not exist.` followed by
`VINTAGE: unavailable -- the projection service did not answer`. The tool therefore reports a wrong query as a service
outage. The corrected form returned 2 rows with the vintage line `2026-10-08 12:54:23 UTC`.

**F1 note (not measured).** That the laptop reads the graph is measured: the query above ran on the laptop. That site Z
reads it is INFERRED: site Z runs under Andrew's own credentials and was not tested. Whether a Dell has any route to the
graph other than the token was not checked. If one exists, F1 shrinks to verifying that route.

**Order of value.** F1 is the one that delivers Andrew's "shared graph read access", and it needs a CTO ruling against
msg 106669. F2 and F4 can land within the hour. F3 makes "current state" true again. F5 prevents wrong work rather than
doing any.
