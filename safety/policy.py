"""Fail-closed governance for F154 Agentic Insurance Operations."""

PROTECTED_ACTIONS = {
    "approve_or_bind_policy",
    "set_or_change_premium",
    "approve_or_deny_claim",
    "issue_coverage_determination",
    "pay_or_settle_claim",
    "cancel_nonrenew_or_rescind_policy",
}

REQUIRED_REVIEWS = (
    "case_intake_reviewed",
    "policy_evidence_reviewed",
    "coverage_analysis_reviewed",
    "claims_evidence_reviewed",
    "compliance_fairness_reviewed",
    "privacy_security_reviewed",
    "escalation_appeal_reviewed",
    "qualified_insurance_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding underwriting, pricing, coverage, claims, payment, cancellation, nonrenewal, or rescission action is outside reference-system authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required insurance-operations review", "missing": missing}
    checks = {
        "policy_evidence_gap": "material policy form, endorsement, declarations, effective date, jurisdiction, limit, deductible, exclusion, or source issue unresolved",
        "coverage_ambiguity_gap": "material coverage, exclusion, condition, causation, allocation, reservation-of-rights, or interpretation issue unresolved",
        "claims_evidence_gap": "material loss facts, documentation, damage, valuation, causation, chronology, or investigation evidence unresolved",
        "unfair_discrimination_risk": "material protected-class, proxy-discrimination, disparate-treatment, disparate-impact, or unfair-practice concern unresolved",
        "fraud_special_investigation_risk": "material fraud indicator, referral, investigation, accusation, or special-investigation issue requires authorized human handling",
        "privacy_security_gap": "material personal, medical, financial, location, identity, security, consent, access, or retention issue unresolved",
        "complaint_appeal_regulatory_gap": "material complaint, appeal, external review, regulator, notice, deadline, or consumer-protection issue unresolved",
        "provenance_documentation_gap": "policy, claim, evidence, communication, calculation, escalation, compliance, or decision provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "insurance-operations governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "insurance operations support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
