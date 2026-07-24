"""
Route extractor -- maps the full serving path from S3 artifact to frontend component.

Authoritative sources:
  1. cloudfront-distribution.tf  -- behaviors, origins, Lambda@Edge associations
  2. shared-advisor-router/index.mjs -- URL->S3 key rewrite rules
  3. api-gateway.tf files -- API GW route_key -> Lambda mapping
  4. advisor-intelligence.ts (+ other endpoint files) -- frontend function -> URL
  5. *.tsx components -- component -> function imports + calls

Builds a route table where each entry is:
  path_pattern -> origin -> [edge_functions] -> auth_layers -> s3_key_or_lambda -> endpoint_fn -> component

Zero API calls. Pure static analysis from Terraform + source.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class CloudFrontOrigin:
    """A CloudFront origin."""
    origin_id: str           # e.g., S3-opal-data-bd
    domain_name: str         # e.g., opal-data-bd.s3.us-east-1.amazonaws.com
    origin_type: str         # "s3" or "api_gateway"
    origin_path: str = ""    # e.g., /prod for API GW
    bucket_name: str = ""    # for S3 origins: opal-data-bd
    oai_or_oac: str = ""     # OAI or OAC identifier


@dataclass
class EdgeFunction:
    """A Lambda@Edge association on a behavior."""
    event_type: str          # viewer-request, origin-request, origin-response
    function_name: str       # e.g., auth-validator-edge
    arn: str = ""


@dataclass
class CloudFrontBehavior:
    """A CloudFront cache behavior (ordered or default)."""
    path_pattern: str        # e.g., /api/scoped/advisor-intelligence/artifacts/*/*
    origin_id: str           # target origin
    edge_functions: list[EdgeFunction] = field(default_factory=list)
    has_auth: bool = False   # True if auth-validator-edge is attached
    has_router: bool = False # True if shared-advisor-router is attached
    order: int = 0           # position in behavior list
    comment: str = ""        # from TF comments


@dataclass
class EdgeVersionBinding:
    """A Lambda@Edge version binding from the locals block."""
    local_name: str          # e.g., auth_validator_edge_arn
    function_name: str       # e.g., auth-validator-edge
    pinned_version: int | None = None   # e.g., 9 (None if dynamic)
    is_dynamic: bool = False             # True if uses qualified_arn
    tf_resource: str = ""                # e.g., aws_lambda_function.auth_validator_edge
    raw_value: str = ""                  # full RHS from locals block


@dataclass
class CustomErrorResponse:
    """A CloudFront custom error response rule."""
    error_code: int              # e.g., 403, 404, 500
    response_code: int           # e.g., 200 (CF substitutes this)
    response_page_path: str      # e.g., /index.html
    ttl_seconds: int = 0         # error_caching_min_ttl


class RouterParseError(Exception):
    """A Lambda@Edge router branch shape the parser does not recognize.

    Raised LOUD, never swallowed. The transcribed-table defect this parser replaces was silent
    under-representation: a branch that could not be expressed (a 401 refusal, a firm-parametric
    origin) was simply omitted, and its absence read as a rule that never existed. A parser that
    quietly skips an unrecognized branch would be the exact same defect one level up -- so an
    unrecognized shape is a hard error that forces a human to extend the parser or the model, never
    a dropped rule.
    """


# RewriteRule.kind vocabulary. A prefix->prefix table can ONLY say "rewrites to a fixed place"; the
# router says more than that, and an outcome the vocabulary cannot represent is not omitted, it is
# MISFILED as whatever the vocabulary can say (a refusal became a RESOLVED S3 key; a per-firm bucket
# became a literal one). Each kind below is a state the old table structurally could not hold.
RULE_REWRITE = "rewrite"            # url_prefix -> s3_prefix, the ordinary case
RULE_REFUSE = "refuse"              # the router BLOCKS this path (e.g. HTTP 401); there is NO S3 key
RULE_MULTISTEP = "rewrite_multistep"  # a transform that is not a single prefix swap (id extraction etc.)


@dataclass
class RewriteRule:
    """A URL->S3 rewrite rule parsed from a Lambda@Edge router.

    Parsed, not transcribed: `source_file` + `source_line` pin the branch this came from, so a drift
    between the table and the router is a test failure rather than an invisible hand-copy skew.
    """
    url_prefix: str          # matched URL prefix
    s3_prefix: str           # rewritten S3 key prefix (empty for a REFUSE rule)
    condition: str = ""      # human description of the branch condition
    kind: str = RULE_REWRITE  # RULE_REWRITE | RULE_REFUSE | RULE_MULTISTEP
    # REFUSE rules: the router blocks the path and no S3 key exists. Reporting an s3_key here is the
    # false-secure defect that motivated the parse (a PII path the router 401s read as RESOLVED).
    refuse_status: str = ""       # e.g. "401"
    refuse_reason: str = ""       # the router's own stated reason
    # A REFUSE rule may need a suffix predicate beyond the prefix (the platinum summary.json case is
    # prefix AND endswith AND one-of two subprefixes). require_endswith/require_any_prefix encode it.
    require_endswith: str = ""            # the path must also end with this (else the rule does not apply)
    require_any_prefix: tuple = ()        # the path must also start with one of these full prefixes
    # FIRM-PARAMETRIC origin: the router rewrites the origin BUCKET per requesting firm, so no single
    # bucket is correct for this rule. A consumer must not emit a fixed s3://bucket/... for it.
    firm_parametric: bool = False
    source_file: str = ""    # the router file this branch was parsed from
    source_line: int = 0     # 1-indexed line of the branch


@dataclass
class ApiGatewayRoute:
    """An API Gateway route."""
    route_key: str           # e.g., GET /api/scoped/advisor-intelligence/timeseries/{dimension}
    method: str = ""         # GET, POST, etc.
    path: str = ""           # /api/scoped/advisor-intelligence/timeseries/{dimension}
    lambda_name: str = ""    # target Lambda
    tf_file: str = ""        # source Terraform file
    pipeline: str = ""       # pipeline name


@dataclass
class EndpointFunction:
    """A frontend API endpoint function."""
    name: str                # e.g., getPartnerAnalytics
    url_template: str = ""   # URL pattern this function calls
    source_file: str = ""    # e.g., portal/src/api/endpoints/advisor-intelligence.ts


@dataclass
class ComponentBinding:
    """A React component that calls endpoint functions."""
    name: str                # e.g., PartnerAnalytics
    file_path: str = ""
    endpoint_calls: list[str] = field(default_factory=list)  # function names called


@dataclass
class Route:
    """A complete route from S3 artifact to frontend component."""
    # Request path
    url_pattern: str = ""              # what the browser requests
    # CloudFront layer
    cf_behavior: str = ""              # matching behavior path_pattern
    cf_origin: str = ""                # origin ID
    cf_origin_type: str = ""           # s3 or api_gateway
    # Auth layer
    auth_edge: bool = False            # auth-validator-edge present
    auth_api_gw: bool = False          # API GW authorizer present
    auth_lambda: str = ""              # Lambda-level auth check
    # Routing layer
    edge_router: str = ""              # shared-advisor-router, public-data-router, etc.
    s3_rewrite: str = ""               # rewritten S3 key (if S3 origin)
    api_gw_route: str = ""             # API GW route_key (if API GW origin)
    # Backend
    lambda_handler: str = ""           # Lambda that handles the request
    s3_key: str = ""                   # final S3 key read (by router or Lambda)
    # Frontend
    endpoint_function: str = ""        # JS function that makes the call
    components: list[str] = field(default_factory=list)  # React components
    # Static-resolvability of the request URL. False when the endpoint's URL is
    # CLIENT-COMPOSED at runtime (a base built from a non-file-level local const /
    # template literal, leaving a leading "{param}") so the tool CANNOT map it to a
    # CloudFront behavior. When False, the auth_* flags are UNDETERMINED, NOT proven
    # absent -- consumers must report UNRESOLVED, never a false auth:NONE.
    url_resolvable: bool = True
    resolve_reason: str = ""           # why the URL is unresolvable (when url_resolvable is False)


@dataclass
class RoutingTable:
    """Complete routing table for the portal."""
    origins: dict[str, CloudFrontOrigin] = field(default_factory=dict)
    behaviors: list[CloudFrontBehavior] = field(default_factory=list)
    custom_error_responses: list[CustomErrorResponse] = field(default_factory=list)
    rewrite_rules: list[RewriteRule] = field(default_factory=list)
    api_gw_routes: list[ApiGatewayRoute] = field(default_factory=list)
    endpoints: dict[str, EndpointFunction] = field(default_factory=dict)
    components: list[ComponentBinding] = field(default_factory=list)
    routes: list[Route] = field(default_factory=list)

    def match_behavior(self, url: str) -> CloudFrontBehavior | None:
        """Match a URL to the most specific CloudFront behavior.
        CloudFront evaluates ordered behaviors first (most specific wins),
        then falls back to the default behavior."""
        # Check ordered behaviors first (order > 0), then default (order == 0)
        ordered = [b for b in self.behaviors if b.order > 0]
        default = [b for b in self.behaviors if b.order == 0]
        # Within ordered behaviors, more specific patterns (longer, more segments) win.
        # CloudFront checks them in declared order, so we preserve that.
        for b in ordered:
            if _cf_pattern_matches(b.path_pattern, url):
                return b
        for b in default:
            if _cf_pattern_matches(b.path_pattern, url):
                return b
        return None

    def match_api_route(self, url: str) -> ApiGatewayRoute | None:
        """Match a URL to an API Gateway route."""
        for r in self.api_gw_routes:
            if _api_route_matches(r.path, url):
                return r
        return None

    def _rule_applies(self, rule: "RewriteRule", url: str) -> bool:
        """Whether `rule` matches `url`, honoring the full branch condition -- not just the prefix.

        A REFUSE rule (the platinum summary.json 401) carries a COMPOUND condition the router
        actually evaluates: prefix AND endswith AND one-of two subprefixes. Matching on the prefix
        alone would over-refuse (block platinum/ paths that are NOT summary.json). The router's
        if/else order is preserved by the caller iterating in declared order.
        """
        if not url.startswith(rule.url_prefix):
            return False
        if rule.require_endswith and not url.endswith(rule.require_endswith):
            return False
        if rule.require_any_prefix and not any(url.startswith(p) for p in rule.require_any_prefix):
            return False
        return True

    def match_rewrite_rule(self, url: str) -> "RewriteRule | None":
        """THE rewrite matcher. Rules are in ROUTER DECLARATION ORDER (parsed from the if/else-if
        chain), and the FIRST match wins -- exactly as the Lambda@Edge router evaluates. Honors the
        full branch condition via _rule_applies, so a compound-conditioned REFUSE rule does not
        over-match.

        resolve_s3_key() delegates here so there is exactly ONE matcher: the rule NAMED by
        comp-routes trace and the key it resolves can never disagree. Returns None when nothing
        covers the path -- missing COVERAGE, not proof no key exists.
        """
        for rule in self.rewrite_rules:
            if self._rule_applies(rule, url):
                return rule
        return None

    def resolve_s3_key(self, url: str) -> str:
        """Apply rewrite rules to resolve a URL to an S3 KEY (the path within a bucket). "" when no
        rule matches OR the matched rule does not resolve to a key.

        A REFUSE rule has NO key -- the router blocks the path; emitting one here is the false-secure
        defect the parse exists to close. A MULTISTEP rule computes its key by transform, not a prefix
        swap. Both are handled explicitly; a plain rewrite is the prefix substitution.
        NOTE: this returns the KEY only. The BUCKET may be firm-parametric (see rule.firm_parametric);
        callers building a full s3:// URI must consult that and REFUSE a fixed bucket when it is set.
        """
        rule = self.match_rewrite_rule(url)
        if rule is None or rule.kind == RULE_REFUSE:
            return ""
        if rule.kind == RULE_MULTISTEP:
            return _apply_multistep(rule, url)
        return rule.s3_prefix + url[len(rule.url_prefix):]


_S3_ORIGIN_DOMAIN_RE = re.compile(r'^(.+?)\.s3(?:[.-][a-z0-9-]+)?\.amazonaws\.com$')


def _s3_bucket_from_domain(domain: str) -> str:
    """Bucket name for an S3 origin domain, or "" when the domain is not an S3 endpoint.

    Matches both the regional (`bucket.s3.us-east-1.amazonaws.com`) and legacy global
    (`bucket.s3.amazonaws.com`) forms, and is INDEPENDENT of whether the origin declares OAI or
    OAC -- that access mechanism says nothing about whether the origin is a bucket.
    """
    m = _S3_ORIGIN_DOMAIN_RE.match(domain.strip().lower())
    return m.group(1) if m else ""


def _cf_pattern_matches(pattern: str, url: str) -> bool:
    """CloudFront pattern matching. * matches any characters including /."""
    # Strip query params from URL before matching
    url_path = url.split('?')[0]
    # CloudFront * matches everything (including slashes), unlike nginx
    regex = re.escape(pattern).replace(r'\*', '.*')
    regex = '^' + regex + '$'
    return bool(re.match(regex, url_path))


def _api_route_matches(route_path: str, url: str) -> bool:
    """API Gateway route matching. {param} matches one path segment."""
    regex = re.sub(r'\{[^}]+\}', '[^/]+', re.escape(route_path))
    regex = '^' + regex.replace(r'\*', '.*') + '(?:\\?.*)?$'
    return bool(re.match(regex, url))


def _url_is_statically_resolvable(url: str) -> bool:
    """A URL template is statically resolvable iff it begins with a LITERAL absolute
    path segment ('/...').

    The frontend endpoint parser substitutes file-level string constants
    (e.g. PLATINUM_BASE = '/api/scoped/...') and only THEN collapses remaining
    runtime interpolations to '{param}'. So:
      - '/api/scoped/advisor-intelligence/platinum/advisors/{param}/book.json' is
        RESOLVABLE -- an absolute literal with a mid-path '{param}' that CloudFront
        '*' behavior patterns match.
      - '{param}/book.json{param}' is NOT resolvable -- the BASE itself was
        client-composed at runtime (a local template-literal const the tool cannot
        see), leaving a LEADING '{param}'. The tool cannot map it to any CloudFront
        behavior, so its auth posture is UNDETERMINED (not proven-absent).

    This is the discriminator that keeps a false auth:NONE off client-composed URLs
    WITHOUT blanket-relabelling genuinely-resolvable open routes."""
    return url.startswith('/')


# ---------------------------------------------------------------------------
# Step 1: Parse CloudFront distribution Terraform
# ---------------------------------------------------------------------------

def _parse_cloudfront(workspace_root: Path) -> tuple[dict[str, CloudFrontOrigin], list[CloudFrontBehavior], list[CustomErrorResponse]]:
    """Parse cloudfront-distribution.tf for origins and behaviors."""
    cf_file = workspace_root / "infra" / "aws" / "terraform" / "portal-auth" / "cloudfront-distribution.tf"
    if not cf_file.exists():
        return {}, [], []

    content = cf_file.read_text(encoding="utf-8", errors="replace")

    # Parse edge function name from ARN locals (handles both hardcoded and qualified_arn)
    edge_name_map: dict[str, str] = {}  # local var -> function name
    # Hardcoded: "${local.edge_arn_prefix}:auth-validator-edge:9"
    for m in re.finditer(r'(\w+_arn)\s*=\s*"\$\{local\.edge_arn_prefix\}:([^:]+):\d+"', content):
        edge_name_map[m.group(1)] = m.group(2)
    # Dynamic/ternary: ...qualified_arn : "${...}:shared-advisor-router:13"
    for m in re.finditer(r'(\w+_arn)\s*=.*?:([a-z][a-z0-9_-]+):\d+"', content):
        if m.group(1) not in edge_name_map:
            edge_name_map[m.group(1)] = m.group(2)

    # Parse origins
    origins: dict[str, CloudFrontOrigin] = {}
    for m in re.finditer(r'origin\s*\{', content):
        block = _extract_tf_block(content, m.start())
        origin_id_m = re.search(r'origin_id\s*=\s*"([^"]+)"', block)
        domain_m = re.search(r'domain_name\s*=\s*"([^"]+)"', block)
        if not origin_id_m or not domain_m:
            continue

        origin_id = origin_id_m.group(1)
        domain = domain_m.group(1)
        origin_path_m = re.search(r'origin_path\s*=\s*"([^"]+)"', block)

        # WHAT AN ORIGIN *IS* COMES FROM ITS DOMAIN, NOT FROM HOW CLOUDFRONT AUTHENTICATES TO IT.
        # This used to be `'s3_origin_config' in block` -- the LEGACY OAI form. An OAC-fronted S3
        # origin declares only `origin_access_control_id`, so both OAC origins
        # (S3-opal-data-portal-v2-json = the MDPF one, and S3-opal-data-assets) were typed
        # "api_gateway" despite *.s3.us-east-1.amazonaws.com domains.
        # Source-grounded: infra/aws/terraform/portal-auth/cloudfront-distribution.tf:169-172 @HEAD
        # 2026-07-23 -- the block carries domain_name + origin_id + origin_access_control_id and no
        # s3_origin_config.
        #
        # THIS WAS A FALSE-SECURE READING, not a cosmetic mistype (NFRA_TOOLARCH.MACHINEFLAG R1, ruled
        # P1 by 1.0.0_SA_CTO~Z). cmd_auth_map groups by origin_type, so it reported /api/general/* and
        # /api/general/json-tiered/* -- S3 origins behind an edge JWT validator -- under "EDGE JWT +
        # API GW AUTHORIZER". An agent asking what protects an origin was told an API Gateway
        # authorizer guards a path no authorizer guards. The wrongness pointed toward safety, and a
        # reassuring answer does not get re-checked.
        is_s3 = bool(_s3_bucket_from_domain(domain)) or 's3_origin_config' in block
        bucket_name = _s3_bucket_from_domain(domain)

        oai_m = re.search(r'origin_access_identity\s*=\s*"([^"]*)"', block)
        oac_m = re.search(r'origin_access_control_id\s*=\s*"([^"]*)"', block)
        oai_or_oac = ""
        if oac_m and oac_m.group(1):
            oai_or_oac = f"OAC:{oac_m.group(1)}"
        elif oai_m and oai_m.group(1):
            oai_or_oac = f"OAI:{oai_m.group(1)}"

        origins[origin_id] = CloudFrontOrigin(
            origin_id=origin_id,
            domain_name=domain,
            origin_type="s3" if is_s3 else "api_gateway",
            origin_path=origin_path_m.group(1) if origin_path_m else "",
            bucket_name=bucket_name,
            oai_or_oac=oai_or_oac,
        )

    # Parse behaviors
    behaviors: list[CloudFrontBehavior] = []

    # Default behavior
    default_m = re.search(r'default_cache_behavior\s*\{', content)
    if default_m:
        block = _extract_tf_block(content, default_m.start())
        origin_m = re.search(r'target_origin_id\s*=\s*"([^"]+)"', block)
        behaviors.append(CloudFrontBehavior(
            path_pattern="/*",
            origin_id=origin_m.group(1) if origin_m else "",
            order=0,
            comment="default (SPA)",
        ))

    # Ordered behaviors
    order = 1
    for m in re.finditer(r'ordered_cache_behavior\s*\{', content):
        block = _extract_tf_block(content, m.start())
        pattern_m = re.search(r'path_pattern\s*=\s*"([^"]+)"', block)
        origin_m = re.search(r'target_origin_id\s*=\s*"([^"]+)"', block)
        if not pattern_m or not origin_m:
            continue

        # Extract edge functions
        edge_fns: list[EdgeFunction] = []
        for ef_m in re.finditer(r'lambda_function_association\s*\{([^}]+)\}', block):
            ef_block = ef_m.group(1)
            event_m = re.search(r'event_type\s*=\s*"([^"]+)"', ef_block)
            arn_m = re.search(r'lambda_arn\s*=\s*local\.(\w+)', ef_block)
            if event_m and arn_m:
                fn_name = edge_name_map.get(arn_m.group(1), arn_m.group(1))
                edge_fns.append(EdgeFunction(
                    event_type=event_m.group(1),
                    function_name=fn_name,
                ))

        has_auth = any(ef.function_name == 'auth-validator-edge' for ef in edge_fns)
        has_router = any(ef.function_name in ('shared-advisor-router', 'public-data-router')
                         for ef in edge_fns)

        # Extract comment above behavior (look for # N. comment)
        block_start = m.start()
        preceding = content[max(0, block_start - 200):block_start]
        comment_m = re.search(r'#\s*\d+[a-z]?\.\s*(.+)', preceding)
        comment = comment_m.group(1).strip() if comment_m else ""

        behaviors.append(CloudFrontBehavior(
            path_pattern=pattern_m.group(1),
            origin_id=origin_m.group(1),
            edge_functions=edge_fns,
            has_auth=has_auth,
            has_router=has_router,
            order=order,
            comment=comment,
        ))
        order += 1

    # Parse custom_error_response blocks
    custom_error_responses: list[CustomErrorResponse] = []
    for m in re.finditer(r'custom_error_response\s*\{', content):
        block = _extract_tf_block(content, m.start())

        error_code_m = re.search(r'error_code\s*=\s*(\d+)', block)
        response_code_m = re.search(r'response_code\s*=\s*(\d+)', block)
        response_page_m = re.search(r'response_page_path\s*=\s*"([^"]+)"', block)
        ttl_m = re.search(r'error_caching_min_ttl\s*=\s*(\d+)', block)

        if error_code_m and response_code_m and response_page_m:
            custom_error_responses.append(CustomErrorResponse(
                error_code=int(error_code_m.group(1)),
                response_code=int(response_code_m.group(1)),
                response_page_path=response_page_m.group(1),
                ttl_seconds=int(ttl_m.group(1)) if ttl_m else 0,
            ))

    return origins, behaviors, custom_error_responses


def parse_edge_versions(workspace_root: Path) -> list[EdgeVersionBinding]:
    """Parse the locals block in cloudfront-distribution.tf for Lambda@Edge version bindings.

    Detects hardcoded version numbers (`:9`) vs dynamic references (`qualified_arn`).
    Cross-references against aws_lambda_function resources in lambda-edge.tf.
    """
    cf_file = workspace_root / "infra" / "aws" / "terraform" / "portal-auth" / "cloudfront-distribution.tf"
    edge_tf = workspace_root / "infra" / "aws" / "terraform" / "portal-auth" / "lambda-edge.tf"

    if not cf_file.exists():
        return []

    content = cf_file.read_text(encoding="utf-8", errors="replace")

    # Build map of Lambda resource names -> tf resource identifiers from lambda-edge.tf
    resource_map: dict[str, str] = {}  # function-name -> aws_lambda_function.X
    if edge_tf.exists():
        edge_content = edge_tf.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(
            r'resource\s+"aws_lambda_function"\s+"(\w+)"\s*\{', edge_content
        ):
            tf_name = m.group(1)
            block = _extract_tf_block(edge_content, m.start())
            fn_m = re.search(r'function_name\s*=\s*"([^"]+)"', block)
            if fn_m:
                resource_map[fn_m.group(1)] = f"aws_lambda_function.{tf_name}"

    # Parse the locals block for _arn assignments
    locals_m = re.search(r'locals\s*\{', content)
    if not locals_m:
        return []

    locals_block = _extract_tf_block(content, locals_m.start())

    bindings: list[EdgeVersionBinding] = []
    for m in re.finditer(
        r'(\w+_arn)\s*=\s*(.+)', locals_block
    ):
        local_name = m.group(1)
        raw_value = m.group(2).strip().rstrip(',')

        # Skip the prefix definition itself
        if local_name == "edge_arn_prefix":
            continue

        # Detect dynamic (qualified_arn) vs hardcoded
        is_dynamic = "qualified_arn" in raw_value

        # Extract function name from either pattern
        fn_name = ""
        pinned_version = None

        # Hardcoded: "${local.edge_arn_prefix}:auth-validator-edge:9"
        hardcoded_m = re.search(r':([a-z][a-z0-9_-]+):(\d+)', raw_value)
        if hardcoded_m:
            fn_name = hardcoded_m.group(1)
            if not is_dynamic:
                pinned_version = int(hardcoded_m.group(2))

        # Dynamic: aws_lambda_function.shared_advisor_router[0].qualified_arn
        dynamic_m = re.search(r'aws_lambda_function\.(\w+)\[?\d*\]?\.qualified_arn', raw_value)
        if dynamic_m:
            tf_name = dynamic_m.group(1)
            # Resolve function name from resource if available
            for fname, res in resource_map.items():
                if res == f"aws_lambda_function.{tf_name}":
                    fn_name = fname
                    break
            if not fn_name:
                fn_name = tf_name.replace('_', '-')

        # Ternary: may have both dynamic and hardcoded (fallback)
        # e.g., var.enable_lambda_edge ? ...qualified_arn : "${...}:shared-advisor-router:13"
        if "?" in raw_value and is_dynamic and hardcoded_m:
            # Ternary with qualified_arn on true branch and hardcoded fallback
            fallback_m = re.search(r':\s*"[^"]*:([a-z][a-z0-9_-]+):(\d+)"', raw_value)
            if fallback_m and not fn_name:
                fn_name = fallback_m.group(1)

        if not fn_name:
            continue

        tf_resource = resource_map.get(fn_name, "")

        bindings.append(EdgeVersionBinding(
            local_name=local_name,
            function_name=fn_name,
            pinned_version=pinned_version,
            is_dynamic=is_dynamic,
            tf_resource=tf_resource,
            raw_value=raw_value,
        ))

    return bindings


def _extract_tf_block(content: str, start: int) -> str:
    """Extract a Terraform {} block starting from a position."""
    brace_pos = content.find('{', start)
    if brace_pos == -1:
        return ""
    depth = 1
    i = brace_pos + 1
    while i < len(content) and depth > 0:
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
        i += 1
    return content[brace_pos:i]


# ---------------------------------------------------------------------------
# Step 2: PARSE (not transcribe) the Lambda@Edge routers for URL->S3 rewrite rules.
#
# History: these rules were HAND-TRANSCRIBED from the routers' if/else chains -- and they drifted.
# By 2026-07-24 the transcription was MISSING the platinum/**/summary.json 401 refusal (so
# comp-routes reported a PII path the router blocks as a RESOLVED S3 key) and the client_timeseries
# multi-step rewrite, and it had no way to express that the advisor-intelligence origin BUCKET is
# firm-parametric (so it named one firm's bucket for every firm). NFRA_TOOLARCH.MACHINEFLAG R2:
# parse the source so the table cannot drift, and FAIL LOUD on any branch shape not representable --
# a parser that silently emits fewer rules is the transcription defect one level up.
# ---------------------------------------------------------------------------

# Match `X.startsWith("literal")`. Group 1 = the tested var (request.uri | suffix), group 2 = literal.
_JS_STARTSWITH = re.compile(r'(\w[\w.]*)\.startsWith\(\s*"([^"]*)"\s*\)')
# Match `request.uri = "literal" + suffix;`  -> group 1 = literal prefix.
_JS_ASSIGN_PREFIX = re.compile(r'request\.uri\s*=\s*"([^"]*)"\s*\+\s*(\w+)\s*;')
# Match `request.uri = request.uri.replace("A", "B");` -> groups A, B.
_JS_ASSIGN_REPLACE = re.compile(r'request\.uri\s*=\s*request\.uri\.replace\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\)')
# Match a `const suffix = request.uri.replace("PREFIX", "");` binding.
_JS_SUFFIX_BIND = re.compile(r'const\s+(\w+)\s*=\s*request\.uri\.replace\(\s*"([^"]*)"\s*,\s*""\s*\)')
# A 401/403 refusal return.
_JS_REFUSE_STATUS = re.compile(r'status:\s*"(\d{3})"')
_JS_REFUSE_ERROR = re.compile(r'"error"\s*:\s*"([^"]*)"|error:\s*"([^"]*)"')


def _apply_multistep(rule: "RewriteRule", url: str) -> str:
    """Resolve a MULTISTEP rule's key. Currently one shape: the client_timeseries id extraction
    (client_timeseries/{id}.json -> gold/entities/clients/{id}/timeseries.json). Kept as an explicit,
    named transform rather than a prefix swap because it is not one -- and the parser refuses to
    invent a prefix rule for it."""
    suffix = url[len(rule.url_prefix):]
    if rule.condition == "client_timeseries id-extraction":
        _id = suffix[len("client_timeseries/"):].replace(".json", "") if suffix.startswith("client_timeseries/") else suffix.replace(".json", "")
        return f"gold/entities/clients/{_id}/timeseries.json"
    raise RouterParseError(f"MULTISTEP rule with unknown transform: {rule.condition!r}")


def _parse_public_data_router(path: Path) -> list[RewriteRule]:
    """Parse public-data-router: a flat chain of
        if (request.uri.startsWith(P)) request.uri = request.uri.replace(P, S);
    Each recognized branch -> one RewriteRule. An unrecognized action line inside a startsWith branch
    raises."""
    rules: list[RewriteRule] = []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    in_handler = False
    for i, line in enumerate(lines, start=1):
        if "handler" in line and "=>" in line:
            in_handler = True
        if not in_handler:
            continue
        sw = _JS_STARTSWITH.search(line)
        if not sw or sw.group(1) != "request.uri":
            continue
        prefix = sw.group(2)
        # The rewrite action is on this line or the next few (the routers put it within the block).
        window = "\n".join(lines[i - 1:i + 4])
        rep = _JS_ASSIGN_REPLACE.search(window)
        if not rep:
            raise RouterParseError(
                f"{path.name}:{i}: startsWith({prefix!r}) branch with no recognized "
                f"`request.uri = request.uri.replace(...)` action within it")
        frm, to = rep.group(1), rep.group(2)
        if frm != prefix:
            raise RouterParseError(
                f"{path.name}:{i}: replace() FROM {frm!r} != startsWith prefix {prefix!r} "
                f"-- unexpected branch shape")
        rules.append(RewriteRule(
            url_prefix=prefix,
            s3_prefix=to.lstrip("/"),
            condition=f"general router {prefix} -> {to}",
            source_file=str(path), source_line=i,
        ))
    return rules


def _parse_shared_advisor_router(path: Path) -> list[RewriteRule]:
    """Parse shared-advisor-router's suffix-based if/else chain into rules, IN ORDER.

    The outer guard binds `const suffix = request.uri.replace(OUTER, "")`, then a chain of
    `if (suffix.startsWith(Y)) request.uri = <LITERAL> + suffix` branches, a REFUSE branch (401),
    a MULTISTEP branch (client_timeseries), a compound `startsWith(A) || startsWith(B)` branch, and a
    final `else`. Every branch is represented or the parser raises. The origin is FIRM-PARAMETRIC
    (request.origin.s3.domainName is rebuilt from FIRM_BUCKET_MAP), so every rule carries
    firm_parametric=True.
    """
    rules: list[RewriteRule] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    firm_parametric = "request.origin.s3.domainName" in text and "FIRM_BUCKET_MAP" in text

    bind = _JS_SUFFIX_BIND.search(text)
    if not bind:
        raise RouterParseError(f"{path.name}: no `const suffix = request.uri.replace(OUTER, '')` binding found")
    suffix_var, outer = bind.group(1), bind.group(2)

    # Walk the branch chain after the suffix binding. Each branch runs from its `if/else if/else`
    # header to the NEXT branch header (or the firm-routing tail) -- so an action separated from its
    # condition by a comment block is still inside its own branch. Branch grain, not line grain.
    bind_line = text[:bind.start()].count("\n") + 1
    n = len(lines)

    # A BRANCH HEADER is an `if (`, `else if (`, or `} else {` line -- keyed on the keyword, NOT on
    # startsWith, so a compound condition spanning continuation lines (platinum/ && endsWith(...) &&
    # (advisors/ || clients/)) is ONE branch, not several. Its condition literals are collected from
    # the header line through the line that opens the block (`) {`).
    _HDR = re.compile(r'^\s*(\}\s*)?(else\s+)?if\s*\(|^\s*\}\s*else\s*\{')
    headers: list[int] = []
    stop = n
    for j in range(bind_line, n):
        if "Route to firm-specific S3 bucket" in lines[j]:
            stop = j
            break
        if _HDR.match(lines[j]):
            headers.append(j)

    for idx, hdr in enumerate(headers):
        end = headers[idx + 1] if idx + 1 < len(headers) else stop
        block = "\n".join(lines[hdr:end])
        line1 = hdr + 1  # 1-indexed source line
        # Condition literals: from the header down to (and including) the line that opens the block.
        cond_end = hdr
        while cond_end < end and ") {" not in lines[cond_end] and not lines[cond_end].rstrip().endswith("{"):
            cond_end += 1
        cond_text = "\n".join(lines[hdr:cond_end + 1])
        sw_all = _JS_STARTSWITH.findall(cond_text)
        sw_suffix = [lit for var, lit in sw_all if var == suffix_var]

        # (1) REFUSAL: the branch returns a status BEFORE any request.uri assignment.
        refuse = _JS_REFUSE_STATUS.search(block)
        uri_pos = block.find("request.uri")
        if sw_suffix and refuse is not None and (uri_pos == -1 or block.find("status:") < uri_pos):
            err = _JS_REFUSE_ERROR.search(block)
            reason = next((g for g in (err.groups() if err else ()) if g), "") if err else ""
            ends = "/summary.json" if "summary.json" in block else ""
            # Compound predicate: the OTHER startsWith literals in the header (platinum/advisors/, clients/).
            any_pref = tuple(outer + lit for var, lit in sw_all
                             if var == suffix_var and lit != sw_suffix[0])
            rules.append(RewriteRule(
                url_prefix=outer + sw_suffix[0], s3_prefix="", kind=RULE_REFUSE,
                condition=f"REFUSE {refuse.group(1)}: {reason}",
                refuse_status=refuse.group(1), refuse_reason=reason,
                require_endswith=ends, require_any_prefix=any_pref,
                firm_parametric=firm_parametric, source_file=str(path), source_line=line1,
            ))
            continue

        # (2) MULTISTEP: an intermediate `const X = suffix.replace(...)` then a rebuilt uri (not
        # "literal" + suffix). Deterministic transform, resolved by _apply_multistep, never a prefix rule.
        if sw_suffix and re.search(r'const\s+\w+\s*=\s*' + re.escape(suffix_var) + r'\.replace\(', block) \
                and "+ " + suffix_var not in block:
            rules.append(RewriteRule(
                url_prefix=outer + sw_suffix[0], s3_prefix="", kind=RULE_MULTISTEP,
                condition="client_timeseries id-extraction",
                firm_parametric=firm_parametric, source_file=str(path), source_line=line1,
            ))
            continue

        # (3) ORDINARY REWRITE (incl. compound `startsWith(A) || startsWith(B)`): request.uri =
        # "<LITERAL>" + suffix. One rule per alternative literal, same target.
        assign = _JS_ASSIGN_PREFIX.search(block)
        if sw_suffix:
            if not assign or assign.group(2) != suffix_var:
                raise RouterParseError(
                    f"{path.name}:{line1}: {suffix_var}.startsWith branch with no recognized "
                    f"`request.uri = \"literal\" + {suffix_var}` action (shape not representable -- "
                    f"extend the parser rather than dropping the branch)")
            literal = assign.group(1)
            for var, lit in sw_all:
                if var != suffix_var:
                    continue
                rules.append(RewriteRule(
                    url_prefix=outer + lit, s3_prefix=(literal.lstrip("/") + lit),
                    condition=f"advisor router {lit} -> {literal}",
                    firm_parametric=firm_parametric, source_file=str(path), source_line=line1,
                ))
            continue

        # (4) FINAL else: request.uri = "<LITERAL>" + suffix -- the catch-all rewrite.
        if lines[hdr].strip().startswith("} else {") and assign and assign.group(2) == suffix_var:
            rules.append(RewriteRule(
                url_prefix=outer, s3_prefix=assign.group(1).lstrip("/"),
                condition=f"advisor router default -> {assign.group(1)}",
                firm_parametric=firm_parametric, source_file=str(path), source_line=line1,
            ))

    if not rules:
        raise RouterParseError(f"{path.name}: parsed zero rules -- the chain shape changed, refusing to emit an empty table")
    return rules


def _parse_rewrite_rules(workspace_root: Path) -> list[RewriteRule]:
    """PARSE (not transcribe) the Lambda@Edge routers for URL->S3 rewrite rules.

    Order across routers does not matter (their URL prefixes are disjoint: /api/general/* vs
    /api/scoped/advisor-intelligence/*); WITHIN a router, declaration order is preserved so the
    first-match matcher mirrors the if/else chain.
    """
    edge = workspace_root / "infra" / "aws" / "lambda-edge"
    rules: list[RewriteRule] = []

    advisor = edge / "shared-advisor-router" / "index.mjs"
    if advisor.exists():
        rules.extend(_parse_shared_advisor_router(advisor))

    public = edge / "public-data-router" / "index.mjs"
    if public.exists():
        rules.extend(_parse_public_data_router(public))

    return rules


# ---------------------------------------------------------------------------
# Step 3: Parse API Gateway routes
# ---------------------------------------------------------------------------

def _parse_api_gw_routes(workspace_root: Path) -> list[ApiGatewayRoute]:
    """Parse API Gateway route_key definitions from Terraform."""
    routes: list[ApiGatewayRoute] = []
    tf_base = workspace_root / "infra" / "aws" / "terraform"

    for pipeline_dir in sorted(tf_base.iterdir()):
        if not pipeline_dir.is_dir():
            continue

        for tf_file in pipeline_dir.glob("api-gateway*.tf"):
            try:
                content = tf_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            rel_path = str(tf_file.relative_to(workspace_root)).replace("\\", "/")

            for m in re.finditer(r'route_key\s*=\s*"([^"]+)"', content):
                route_key = m.group(1)
                parts = route_key.split(' ', 1)
                method = parts[0] if len(parts) == 2 else "ANY"
                path = parts[1] if len(parts) == 2 else parts[0]

                # Try to find target Lambda from integration in same block
                block_start = content.rfind('resource ', 0, m.start())
                if block_start >= 0:
                    block = _extract_tf_block(content, block_start)
                    # integration_uri pattern
                    int_m = re.search(r'integration_uri\s*=\s*(?:module\.(\w+)\.invoke_arn|aws_lambda_function\.(\w+)\.invoke_arn|"([^"]+)")', block)
                    lambda_name = ""
                    if int_m:
                        lambda_name = int_m.group(1) or int_m.group(2) or int_m.group(3) or ""

                routes.append(ApiGatewayRoute(
                    route_key=route_key,
                    method=method,
                    path=path,
                    lambda_name=lambda_name,
                    tf_file=rel_path,
                    pipeline=pipeline_dir.name,
                ))

    return routes


# ---------------------------------------------------------------------------
# Step 4: Parse frontend endpoint functions
# ---------------------------------------------------------------------------

def _parse_frontend_endpoints(workspace_root: Path) -> dict[str, EndpointFunction]:
    """Parse portal/src/api/endpoints/*.ts for function->URL mappings."""
    endpoints: dict[str, EndpointFunction] = {}
    api_dir = workspace_root / "portal" / "src" / "api" / "endpoints"
    if not api_dir.exists():
        return endpoints

    # Pattern: export async function getFoo(...) { ... apiRequest<T>(`/api/...`) }
    fn_pattern = re.compile(r'export\s+(?:async\s+)?function\s+(\w+)\s*\(')

    # Pre-scan: extract file-level URL constants (e.g., PLATINUM_BASE, API_BASE_URL)
    # These are used in template literals: `${PLATINUM_BASE}/firm/dashboard.json`
    file_constants: dict[str, dict[str, str]] = {}  # filename -> {const_name: value}

    # Item 2 (@7a2805d4e): strip comments BEFORE any URL extraction. The raw-text
    # scan resolved getAccountDistribution to a commented-out /api/private TODO
    # (dead call preceded the live one; first regex match won) -- the
    # FALSE-PRESENCE class. Dead code is never presented to the resolver.
    from .extract_ts_source import strip_comments

    for ts_file in sorted(api_dir.glob("*.ts")):
        try:
            content = strip_comments(ts_file.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        consts: dict[str, str] = {}
        for cm in re.finditer(r"(?:const|let)\s+(\w+)\s*=\s*['\"]([^'\"]+)['\"]", content):
            name, value = cm.group(1), cm.group(2)
            if '/' in value:  # only URL-like constants
                consts[name] = value
        file_constants[ts_file.name] = consts

    for ts_file in sorted(api_dir.glob("*.ts")):
        try:
            content = strip_comments(ts_file.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue

        rel_path = str(ts_file.relative_to(workspace_root)).replace("\\", "/")
        consts = file_constants.get(ts_file.name, {})
        fn_starts = list(fn_pattern.finditer(content))

        for i, fm in enumerate(fn_starts):
            fn_name = fm.group(1)
            start = fm.start()
            end = fn_starts[i + 1].start() if i + 1 < len(fn_starts) else len(content)
            chunk = content[start:end]

            # Extract URL from apiRequest, fetch, or template literal
            url = ""
            # apiRequest<T>('/api/...')  or  apiRequest<T>(`/api/...`)
            url_m = re.search(r'apiRequest\s*<[^>]*>\s*\(\s*[`\'"]([^`\'"]+)[`\'"]', chunk)
            if url_m:
                url = url_m.group(1)
            else:
                # apiRequest<T>(`${base}...`) where base is defined earlier
                url_m = re.search(r'apiRequest\s*<[^>]*>\s*\(\s*`([^`]+)`', chunk)
                if url_m:
                    url = url_m.group(1)
                else:
                    # fetch(url, ...) where url is built from a const
                    url_m = re.search(r"const\s+(?:url|base|endpoint)\s*=\s*[`'\"](/[^`'\"]+)[`'\"]", chunk)
                    if url_m:
                        url = url_m.group(1)
                    else:
                        # const base = `${CONST}/path`; ... apiRequest(base) or fetch(url)
                        url_m = re.search(r"const\s+(?:url|base)\s*=\s*`([^`]+)`", chunk)
                        if url_m:
                            url = url_m.group(1)

            # Resolve file-level constants in template literals: ${PLATINUM_BASE} -> /api/scoped/...
            for const_name, const_value in consts.items():
                url = url.replace(f'${{{const_name}}}', const_value)

            # Clean remaining template literal interpolations (dynamic params)
            url = re.sub(r'\$\{[^}]+\}', '{param}', url)

            endpoints[fn_name] = EndpointFunction(
                name=fn_name,
                url_template=url,
                source_file=rel_path,
            )

    return endpoints


# ---------------------------------------------------------------------------
# Step 5: Parse component -> endpoint bindings
# ---------------------------------------------------------------------------

def _parse_component_bindings(workspace_root: Path, endpoints: dict[str, EndpointFunction]) -> list[ComponentBinding]:
    """Parse .tsx files for which endpoint functions they import and call."""
    bindings: list[ComponentBinding] = []
    pages_dir = workspace_root / "portal" / "src" / "pages"
    if not pages_dir.exists():
        return bindings

    import_pattern = re.compile(r'import\s*\{([^}]+)\}\s*from\s*[\'"]([^\'"]+)[\'"]')

    for tsx_file in sorted(pages_dir.rglob("*.tsx")):
        try:
            content = tsx_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        rel_path = str(tsx_file.relative_to(workspace_root)).replace("\\", "/")

        # Find endpoint imports
        imported_fns: set[str] = set()
        for m in import_pattern.finditer(content):
            source = m.group(2)
            if 'api/' in source or 'endpoints/' in source:
                names = [n.strip().split(' as ')[0].strip()
                         for n in m.group(1).split(',')]
                for name in names:
                    if name in endpoints:
                        imported_fns.add(name)

        if not imported_fns:
            continue

        # Check which are actually called
        called_fns = []
        for fn_name in imported_fns:
            if re.search(rf'\b{re.escape(fn_name)}\s*\(', content):
                called_fns.append(fn_name)

        if called_fns:
            bindings.append(ComponentBinding(
                name=tsx_file.stem,
                file_path=rel_path,
                endpoint_calls=sorted(called_fns),
            ))

    return bindings


# ---------------------------------------------------------------------------
# Main: build the complete routing table
# ---------------------------------------------------------------------------

def build_routing_table(workspace_root: Path) -> RoutingTable:
    """Build the complete routing table from all authoritative sources."""
    rt = RoutingTable()

    # Step 1: CloudFront
    origins, behaviors, custom_error_responses = _parse_cloudfront(workspace_root)
    rt.origins = origins
    rt.behaviors = behaviors
    rt.custom_error_responses = custom_error_responses

    # Step 2: Rewrite rules
    rt.rewrite_rules = _parse_rewrite_rules(workspace_root)

    # Step 3: API Gateway
    rt.api_gw_routes = _parse_api_gw_routes(workspace_root)

    # Step 4: Frontend endpoints
    rt.endpoints = _parse_frontend_endpoints(workspace_root)

    # Step 5: Component bindings
    rt.components = _parse_component_bindings(workspace_root, rt.endpoints)

    # Step 6: Build resolved routes (connect endpoint URLs through the full chain)
    for fn_name, ep in rt.endpoints.items():
        if not ep.url_template:
            continue

        url = ep.url_template
        route = Route(url_pattern=url, endpoint_function=fn_name)

        # Static-resolvability gate. A client-composed URL (runtime-templated base,
        # leading "{param}") cannot be mapped to a CloudFront behavior, so its auth
        # posture is UNDETERMINED -- we must NOT let it fall through to the default
        # all-False auth flags, which read as a proven-open auth:NONE. Only attempt
        # a behavior match on a statically-resolvable absolute URL.
        statically_resolvable = _url_is_statically_resolvable(url)
        behavior = rt.match_behavior(url) if statically_resolvable else None
        if not statically_resolvable:
            route.url_resolvable = False
            route.resolve_reason = "client-composed URL (runtime-templated base, no static literal)"
        elif behavior is None:
            route.url_resolvable = False
            route.resolve_reason = "no CloudFront behavior matched the static URL"

        # Match CloudFront behavior
        if behavior:
            route.cf_behavior = behavior.path_pattern
            route.cf_origin = behavior.origin_id
            route.auth_edge = behavior.has_auth
            route.edge_router = next(
                (ef.function_name for ef in behavior.edge_functions
                 if ef.event_type == "origin-request"), ""
            )

            origin = rt.origins.get(behavior.origin_id)
            if origin:
                route.cf_origin_type = origin.origin_type

                if origin.origin_type == "s3":
                    # Resolve S3 key via rewrite rules
                    s3_key = rt.resolve_s3_key(url)
                    route.s3_key = s3_key
                    route.s3_rewrite = s3_key

                elif origin.origin_type == "api_gateway":
                    route.auth_api_gw = True
                    # Match API GW route
                    api_route = rt.match_api_route(url)
                    if api_route:
                        route.api_gw_route = api_route.route_key
                        route.lambda_handler = api_route.lambda_name

        # Find components that call this endpoint
        for comp in rt.components:
            if fn_name in comp.endpoint_calls:
                route.components.append(comp.name)

        rt.routes.append(route)

    return rt
