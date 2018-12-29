from flask import url_for


def test_can_start_a_list_and_retrieve_it_later(live_server, browser):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    index_url = url_for('health.health_status', _external=True)

    browser.get(index_url)

    # She notices the page title and header mention to-do lists
    assert 'OK' in browser.page_source
    play_url = url_for('playsimple', play_id='play1', _external=True)
    browser.get(play_url)
    assert 'Tale' in browser.page_source
    # fail('Finish the test!')


def test_can_submit_word_and_get_its_occurences_test(live_server, browser):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    play_url = url_for('wordsimple', word_target='thine', _external=True)
    browser.get(play_url)
    assert 'places' in browser.page_source
    # fail('Finish the test!')