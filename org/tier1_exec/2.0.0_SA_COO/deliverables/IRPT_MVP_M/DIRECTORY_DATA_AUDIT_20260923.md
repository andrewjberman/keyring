# Current directory and ownership data audit

Measured **2026-09-23 13:54:39-13:55:00 UTC**. Authority: CTO message
`20260923T134609Z`, completion `CONTRACT.md`, and
`LOCAL_LIVE_PARTNER_SCOPE_20260923.md`. This is M's assigned producer-data audit,
not an independent CVO verdict or a deployed authenticated journey test.
P retains the transferred implementation and integration ownership.

All three directory targets are readable and nonempty. All **5,127** entries
validate against the current DirectoryEntry schema. Registry bucket selection,
canonical opaque firm identity, every entry's firm, pointer metadata, entry counts
and entry revisions agree. There are no cross-firm entries or malformed account
ID shapes. Every directory is dated **September 17**, three NYSE trading days
behind the conservative previous completed day, September 22. This proves dated
lag, not a particular producer SLA or a new entitlement.

| Registry firm | Valid entries / unique accounts | Directory business date | Current ownership | Concrete data limitation |
|---|---:|---|---|---|
| 49financial | 4,576 / 7,532 | 2026-09-17 | Present, schema 1, 179 nonempty advisor records; generated 2026-09-23 05:13:11Z | 69 entire advisor projection calls refuse; substantial account and relationship key-space gaps remain |
| inflection | 291 / 875 | 2026-09-17 | **Absent**, GetObject `NoSuchKey`, HTTP 404 | No current map bytes or advisor-grant population to validate |
| cottonwood | 260 / 842 | 2026-09-17 | **Present but empty**, schema 1, zero advisors; generated 2026-09-23 11:35:08Z | A freshly generated empty map is not a populated grant source |

Cottonwood has 856 account appearances but 842 unique accounts: canonical
`firm_population` collapses 14 repeated appearances. No additional account IDs
are inferred from the directory names or ownership records.

## 49F projection failure and denominators

Executed the existing `ids.projection_for_firm`, `resolve.advisor_grant`,
`firm_population`, relationship-index and `unmatched_reasons` helpers at P pin
`dc51d8920dd25d4c11bf48737cdca31ada3e8a63`. The bundled
`custodian_key_seam.json` contains 6,202 entries and has SHA256
`87f2f92f3c71f7761b387574a3df721474120465b1b0da8028cfc201b619923a`.

The live map contains 22,468 account-grant rows / **6,564 distinct raw accounts**,
and 10,396 relationship-grant rows / **3,105 distinct raw relationships**.
Separate per-key diagnostic calls partition the complete account denominator:

| Result from the existing canonical projection | Distinct raw account count |
|---|---:|
| Projects and matches this directory | 5,015 |
| Projects to issued ID but absent from this directory | 32 |
| Unresolved seam, returned unprojected by canonical helper | 1,230 |
| Bundled seam target refused as an empty raw key | 287 |
| **Total** | **6,564** |

All 287 `EMPTY_RAW_KEY` failures arise at the **bundled seam target**, rather
than proving that the original ownership key itself was empty. These failures
cause **69 of 179** full `advisor_grant` calls to raise `IdRefused`; the helper
does not return a partial grant for those calls. The remaining **110** successful
whole-advisor calls collectively match **1,421** directory accounts. That 1,421
is explicitly the successful-call subset, not the full-map 5,015 per-key overlap.

All 3,105 distinct relationship keys can be projected, but **zero** match the
current directory relationship IDs. Their authoritative raw-key correspondence
is unproven. Neither dropping bad keys nor inventing relationship/account joins
is an authorized remedy. Per-key diagnostics never replace the actual whole
advisor helper or confer a grant.

## Required distinctions for P's Global outcomes

- **Readable, dated data:** all three have usable schema-shaped directory bytes
  with old business dates. Show or retain their actual dates; do not describe
  successful reads as fresh data or full current custody coverage.
- **Absent versus empty grants:** Inflection has no object under the inspected
  key; Cottonwood has a real versioned empty object. Neither proves there are
  no investors, since both directories contain accounts.
- **Incompatible projection versus empty grant:** affected 49F advisor calls
  raise. That refusal must not become a successful empty result. Other 49F
  account/relationship mismatches also remain visible as bounded coverage gaps.
- **Principal-specific outcome:** the scope resolver's existing operations and
  Opal branches derive the selected firm's population independently of advisor
  map intersections. An empty/absent advisor map is not by itself proof that an
  authorized Opal or operations request must fail. Apply actual principal rules;
  do not fabricate advisor membership to make those outcomes agree.
- **Unreadable is separate:** this audit observed no unreadable directory or
  present ownership object under the operator identity. A future AccessDenied
  cannot be called a proven absence from this evidence. Lambda-role access was
  not simulated. The existing loader's AccessDenied-to-empty behavior is not an
  audit finding that the object is absent.

## Exact receipts and reproduction

[DIRECTORY_DATA_AUDIT_20260923.json](DIRECTORY_DATA_AUDIT_20260923.json) contains
every bucket/key, S3 VersionId, SHA256, byte length, LastModified, directory/source
revision, business/completion date, sanitized count and helper source hash.
All eight present objects (three pointers, three directories, two ownership maps)
were reread using their exact non-null VersionIds and matched byte hashes.
Pointer versions stayed current through target reads; present ownership versions
stayed current through projection. This is a measured interval, not an atomic
cross-object snapshot. The missing Inflection object has no invented version or hash.

Runtime configuration was read from `irpt-directory-search`, deployed at
2026-09-23T06:26:25Z with code hash
`iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s=`. Its three-firm bucket map agrees
with the pinned registry. The artifacts declare an opaque firm, not a separate
registry-tenant field; the bucket anchor plus canonical opaque comparison was
checked. The declared `irpt-dir/...` revision differs intentionally from the
canonical content SHA256 used by selection/browse; both are retained distinctly.

```powershell
python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/directory_data_audit.py --source-pin dc51d8920d --out <new-evidence.json>
```

The script reads live pointers when rerun; it does not promise reproduction of
a later latest version. It extracts exact committed helpers to a temporary
directory and retains no client names, advisor IDs, account IDs or raw S3 payloads.
`comp-keys exists investor-reporting/directory/latest.json` independently returned
all three pointers present; its existence result does not grade their contents.

No producer was invoked; no S3/DynamoDB write, role change, production source edit,
deployment, vendor call, user impersonation or principal authorization occurred.
Only M-owned evidence is committed. Push state **LOCAL**; observed origin CLOUD
at resume: `365ab567ba1250a6a3569df38cb75d12fe2e8d0e`.
