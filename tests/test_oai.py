def test_intent_classifier_sync_account():
    from app.services.ai.oai.classifiers import classify_intent

    content = "Link account"
    intent = classify_intent(content)

    assert intent.intent == "sync-account"


def test_intent_classifier_none():
    from app.services.ai.oai.classifiers import classify_intent

    content = "I want to order a pizza"
    intent = classify_intent(content)

    assert intent.intent is None
