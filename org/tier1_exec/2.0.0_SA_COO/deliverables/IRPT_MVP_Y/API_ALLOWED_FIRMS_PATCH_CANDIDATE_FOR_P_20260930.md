# Exact patch candidate for `~P` -- allowedFirmIds enforced at the API for service principals (CTO ruling 103317 item 1)

Author `2.0.0_SA_COO~Y`, 2026-09-30 ~16:5xZ. CONTRACT.md row 21: shared auth/scope is `~P`'s writer surface; Y supplies the
exact patch. This is that patch, measured against HEAD; `~P` cuts it with its test at the top of its next issuance
(CTO 103317). Nothing here is applied by Y.

## The admission point, measured (`infra/aws/lambda/investor-reporting/_authz/served.py` @HEAD 41bd4deea9)

Step 2 of the entry (around lines 924-960): `verified` = the edge-injected firm header (`opal-capital` for this
principal); `internal = verified_internal_subject(headers) is not None`; `selected = selected_tenant(event)`. Then:

```python
        if selected is not None and selected != verified:
            if not internal:
                return refuse(operation or self.function_name, None, "FIRM_BINDING")
            from loaders import bucket_for
            try:
                bucket_for(selected)  # Terraform's registry-derived tenant allow-list.
            except ValueError:
                return refuse(operation or self.function_name, None, "FIRM_BINDING")
            verified = selected
```

An INTERNAL subject may select ANY registry firm. That is the branch `svc-irpt-analysis` took on 2026-09-30 16:2xZ
(row S238: one inflection directory entry served). The nine trusted headers (`_scope/resolve.py` `TRUSTED_HEADERS`)
carry no `allowedFirmIds`, and two existing tests pin the set at exactly nine, so the edge is not the place.

## The patch (one branch, one read, one refusal)

Insert between `bucket_for(selected)` and `verified = selected`:

```python
            # A SERVICE principal's reach is its row's allowedFirmIds (absent or "ALL" = unrestricted). Read from the
            # maintained profile row (CanonicalProfileReaders.get_user projects allowedFirmIds since IB-yr-293), never
            # from a header. Mirrors ycharts/generate/current_authority.allowed_firm_ids exactly.
            if trusted.get("x-user-type", "").strip().lower() == "service":
                allowed = self._service_allowed_firms(trusted.get("x-user-email", ""))
                if allowed is not None and selected not in allowed:
                    return refuse(operation or self.function_name, None, "FIRM_BINDING")
```

with, on the entry class:

```python
    def _service_allowed_firms(self, email):
        """None = unrestricted (attribute absent or 'ALL'); else the list. A row that cannot be read restricts
        everything (fail closed), which the caller turns into FIRM_BINDING."""
        try:
            from canonical_profile_reads import CanonicalProfileReaders
            row = CanonicalProfileReaders(self._ddb()).get_user(email.strip().lower()) or {}
        except Exception:
            return []
        value = row.get("allowedFirmIds")
        if value is None or value == "ALL":
            return None
        items = value.split(",") if isinstance(value, str) else list(value)
        return [t.strip() for t in items if isinstance(t, str) and t.strip()]
```

`self._ddb()` is whatever DynamoDB client the entry already holds for its other reads (`~P` knows the installer's
binding; Y does not type it). `FIRM_BINDING` is the existing refusal the same branch already uses for a non-internal
subject, so the public envelope and its 403 shape are unchanged; if `~P` prefers a named code, `ACTOR_FIRM_NOT_ALLOWED`
would need a `PUBLIC_REASONS` member (rule 24 proposal) -- not asked here.

## The test `~P` owes (CTO 103317: "with a test")

`_authz/tests/`: a service subject (`x-user-type service`, `x-user-email svc@...`) whose stubbed row carries
`allowedFirmIds "cottonwood"`: `selected_tenant=cottonwood` admitted (200), `selected_tenant=inflection` refused
`FIRM_BINDING` (403); the same subject with the attribute ABSENT: both admitted (today's behaviour, unchanged); a
non-service internal subject: unchanged. Base at HEAD: the inflection case is ADMITTED (the S238 measurement).

## The live re-read Y owes after it lands (CTO 103317 item 2)

`python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/svc_principal.py negcontrol <out.json>` under
`svc-irpt-analysis`: `directory/search?selected_tenant=inflection` must answer a refusal, `selected_tenant=cottonwood`
200 with an entry. Both prints go to the CTO; S238 disarms on the CTO's read of them.


## CORRECTION (2026-09-30 ~20:5xZ, 2.0.0_SA_COO~Y) -- this candidate was DEFECTIVE as written; ~P caught it at the cut

`2.0.0_SA_COO~P` (103391) measured at the cut of `TO-IB-pr-271` @22b99e32fd: `_authz/served.py` ships in **7** Lambda
bundles, and `canonical_profile_reads.py` ships in only **2** (irpt-performance-adapter, irpt-ycharts-generate). My
`_service_allowed_firms` imported it lazily inside `try:` and answered `[]` on ANY exception, so in the other **5**
bundles
(directory-search, export-render, holdings, narrative, status) a MISSING MODULE would have read as "restricted to
nothing": every service principal refused on every firm, and the lazy import is exempt from the import-closure check,
so no gate would have noticed. That is exactly the class CTO 103372 now rules on (prove an import in the DEPLOYED
layout). The candidate conflated two different failures under one fail-closed branch: "the row says no" and "this
bundle cannot read the row". `~P`'s cut carries the reader and its closure (maintained_sources, ids) into all 7
bundles and proves the import per bundle (P27-1-AC2). Lesson kept at this lane: a fail-closed branch must never
catch an ImportError; a missing dependency is a build defect to surface loudly, not an authorization answer.
