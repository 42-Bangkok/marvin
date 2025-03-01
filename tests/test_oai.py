async def test_intent_classifier_sync_account():
    from app.services.ai.oai.classifiers import classify_intent

    content = "Link account"
    intent = await classify_intent(content)

    assert intent.intent == "link-account"


async def test_intent_classifier_none():
    from app.services.ai.oai.classifiers import classify_intent

    content = "I want to order a pizza"
    intent = await classify_intent(content)

    assert intent.error
