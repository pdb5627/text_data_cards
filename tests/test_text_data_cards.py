#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_text_data_cards
----------------------------------

Tests for `text_data_cards` module.
"""

import pytest


from text_data_cards import text_data_cards


# DataCard
@pytest.fixture()
def tc():
    return text_data_cards.DataCard('(I3, F5.4, F8.5, I2, F8.5, F8.5, A8, '
                                    'A5, A5)',
                                    ['IP', 'SKIN', 'RESIS', 'IX', 'REACT',
                                     'DIAM', 'T', 'FIXED', 'RIGHT'],
                                    fixed_fields=(7, 8))


@pytest.fixture()
def tt_nomatch():
    #      I3 F5.4 F8.5    I2F8.5    F8.5    A8      A4
    #      1231234512345678121234567812345678123456781234512345
    tt = ['  3  0.0   .1357 0   .3959    1.18TESTTEXTFIXEDWRONG']
    return tt


@pytest.fixture()
def tt_match():
    #      I3 F5.4 F8.5    I2F8.5    F8.5    A8      A4
    #      1231234512345678121234567812345678123456781234512345
    tt = ['  3  0.0   .1357 0   .3959    1.18TESTTEXTFIXEDRIGHT']
    return tt


def test_DataCard_nomatch(tc, tt_nomatch):
    assert tc.match(tt_nomatch) is False
    with pytest.raises(ValueError):
        tc.read(tt_nomatch)


def test_DataCard_match(tc, tt_match):
    assert tc.match(tt_match) is True
    tc.read(tt_match)
    assert tc.data['IP'] == 3
    assert tc.data['SKIN'] == 0.0
    assert tc.data['RESIS'] == 0.1357
    assert tc.data['IX'] == 0
    assert tc.data['REACT'] == 0.3959
    assert tc.data['DIAM'] == 1.18
    assert tc.data['T'] == 'TESTTEXT'
    assert tc.data['FIXED'] == 'FIXED'
    assert tc.data['RIGHT'] == 'RIGHT'


# DataCardFixedText
@pytest.fixture()
def tc_fixed_text():
    return text_data_cards.DataCardFixedText('SOME FIXED TEXT')


@pytest.fixture()
def tt_fixed_text_nomatch():
    return ['SOME WRONG TEXT']


@pytest.fixture()
def tt_fixed_text_match():
    return ['SOME FIXED TEXT']


def test_DataCardFixedText_match(tc_fixed_text, tt_fixed_text_match):
    assert tc_fixed_text.match(tt_fixed_text_match) is True


def test_DataCardFixedText_nomatch(tc_fixed_text, tt_fixed_text_nomatch):
    assert tc_fixed_text.match(tt_fixed_text_nomatch) is False


# DataCardStack
@pytest.fixture()
def tc_stack():
    return text_data_cards.DataCardStack([tc(), tc_fixed_text()])


@pytest.fixture()
def tt_stack_match():
    return tt_match() + tt_fixed_text_match()


@pytest.fixture()
def tt_stack_nomatch1():
    return tt_nomatch() + tt_fixed_text_match()


@pytest.fixture()
def tt_stack_nomatch2():
    return tt_match() + tt_fixed_text_nomatch()


def test_DataCardStack_match(tc_stack, tt_stack_match):
    test_DataCard_match(tc_stack, tt_stack_match)


def test_DataCardStack_nomatch1(tc_stack, tt_stack_nomatch1):
    test_DataCard_nomatch(tc_stack, tt_stack_nomatch1)


def test_DataCardStack_nomatch2(tc_stack, tt_stack_nomatch2):
    test_DataCard_nomatch(tc_stack, tt_stack_nomatch2)


# DataCardRepeat
@pytest.fixture()
def tc_repeat():
    return text_data_cards.DataCardRepeat(tc(), tc_fixed_text())


@pytest.fixture()
def tt_repeat_match():
    return tt_match() + tt_match() + tt_fixed_text_match()


@pytest.fixture()
def tt_repeat_nomatch1():
    return tt_nomatch() + tt_match() + tt_fixed_text_match()


@pytest.fixture()
def tt_repeat_nomatch2():
    return tt_match() + tt_nomatch() + tt_fixed_text_match()


@pytest.fixture()
def tt_repeat_nomatch3():
    return tt_match() + tt_match() + tt_fixed_text_nomatch()


def test_DataCardRepeat_match(tc_repeat, tt_repeat_match):
    assert tc_repeat.match(tt_repeat_match) is True
    tc_repeat.read(tt_repeat_match)
    for d in tc_repeat.data:
        assert d['IP'] == 3
        assert d['SKIN'] == 0.0
        assert d['RESIS'] == 0.1357
        assert d['IX'] == 0
        assert d['REACT'] == 0.3959
        assert d['DIAM'] == 1.18
        assert d['T'] == 'TESTTEXT'
        assert d['FIXED'] == 'FIXED'
        assert d['RIGHT'] == 'RIGHT'


def test_DataCardRepeat_nomatch1(tc_repeat, tt_repeat_nomatch1):
    test_DataCard_nomatch(tc_repeat, tt_repeat_nomatch1)


def test_DataCardRepeat_nomatch2(tc_repeat, tt_repeat_nomatch2):
    test_DataCard_nomatch(tc_repeat, tt_repeat_nomatch2)


def test_DataCardFixedText_nomatch3(tc_repeat, tt_repeat_nomatch2):
    test_DataCard_nomatch(tc_repeat, tt_repeat_nomatch2)
