from orchestration.orchestrator import run
from safety.policy import PROTECTED_ACTIONS, REQUIRED_REVIEWS, authorize


def approved_context():
    return {key: True for key in REQUIRED_REVIEWS}


def test_orchestrator_runs_five_agents_and_fails_closed():
    result = run({})
    for key in ("intake", "coverage", "claims", "compliance", "escalation"):
        assert key in result
    assert result["released"] is False


def test_missing_reviews_fail_closed():
    result = authorize("release_insurance_support_package", {})
    assert result["allowed"] is False
    assert len(result["missing"]) == 8


def test_reviewed_support_package_can_release():
    assert authorize("release_insurance_support_package", approved_context())["allowed"] is True


def test_policy_evidence_gap_blocks():
    assert authorize("release_insurance_support_package", approved_context() | {"policy_evidence_gap": True})["allowed"] is False


def test_coverage_ambiguity_gap_blocks():
    assert authorize("release_insurance_support_package", approved_context() | {"coverage_ambiguity_gap": True})["allowed"] is False


def test_unfair_discrimination_risk_blocks():
    assert authorize("release_insurance_support_package", approved_context() | {"unfair_discrimination_risk": True})["allowed"] is False


def test_privacy_security_gap_blocks():
    assert authorize("release_insurance_support_package", approved_context() | {"privacy_security_gap": True})["allowed"] is False


def test_protected_actions_never_autonomously_release():
    for action in PROTECTED_ACTIONS:
        assert authorize(action, approved_context())["allowed"] is False
