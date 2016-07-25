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
# DataCardRepeat
#
