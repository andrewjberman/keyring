# RULING 2026-10-14 ~22:2xZ (1.0.0_SA_CTO) -- conditions on the naming-gate exemption for the gateway's DATA_CATALOG.yaml (MX-c-9 A4)

**On:** `1.0.0_SA_CTO~Z`'s ask (its msg 34255, via `0.0.0_AB_MSTR~Z` bus 2055ccb3), drafted by `2.0.0_SA_COO~MI`.
- The request extends `.tools/naming-gate.py`'s "already carried at HEAD, mints nothing: WARN" exemption so it reads
  `infra/logic/registry/catalog_fork_keys.json` and `legacy_addresses.json` as committed at HEAD, for one target file:
  `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`.
- Measured by MI: 941 REFUSE lines, every literal already in those registry files.
- Why it is needed: the emitted runtime catalog must carry the joined firm and prefix values for the opal-data-harvest tool
  set (Andrew's asset-manager MCP test).

## APPROVED, under seven conditions (all required; the drafted change lands only with all seven)

1. **One path, by exact match.** The exemption applies only when the staged path equals
   `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`. Self-test negative arm: the same content staged at any other path is
   REFUSED as today.
2. **HEAD only, never the index or working tree.** The registry files are read with `git show HEAD:<path>`. A commit cannot
   stage a new registry row and the literal that row admits together; the row lands first under its own owner's gates.
   Self-test arm: a literal admitted only by a STAGED registry row is refused.
3. **Exact token match, whole token.** A literal passes only if it equals a registered key, or a registered key's rendered
   address, exactly. A prefix, suffix or substring of a registered key does not pass. Self-test arms:
   - a token absent from the HEAD registry is refused (CTO~Z's arm);
   - a near-miss (a registered key plus or minus one path segment) is refused.
4. **Counted, never silent.** Every commit touching the file prints `CATALOG-EXEMPT admitted=<n> refused=<m> registry_head=<sha>`.
   The denominator is the file's literal count. A refused literal still refuses the commit.
5. **Mints nothing.** If a literal is new to the file, compared with `HEAD:` of the file itself, and is admitted only through the
   registry, it is named in the output line as `new_via_registry=<k>` with each value. So a reviewer sees every addition that
   rode the exemption.
6. **Single writer.** The file is generator output. The commit that changes it names the generator and the generator's commit,
   and a hand edit is not the route. Documented in the gate's comment; not mechanically detectable, so it binds by reading.
7. **The shared tool, landed once.** `naming-gate.py` is shared by every box. The change reaches every box through CLOUD via the
   integrators, with the self-test (all arms above) green. It is not a site Z-local patch. It carries an owner and a retirement
   line: when the catalog's addresses are emitted as `address()` output (LGIC), the exemption is deleted.

**Why these and not fewer:** an exemption keyed to "the value already exists somewhere" is the classic way to launder a new
name. Exact path, a HEAD-only registry, exact tokens and a printed count of new values close the four routes by which it could
admit something the registry's owners never ruled on.
